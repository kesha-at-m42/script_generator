"""
Figma visual grounding experiment.
Claude uses tool_use to select and fetch Figma frames, generates a lesson
script grounded in what it sees. Gemini then edits each frame to match
the exact params in the scene beat (e.g. correct group/item counts).
Output: HTML file with beats + edited images side by side.
"""

import base64
import io
import json
import os
from pathlib import Path

import anthropic
import requests
import torch
from diffusers import Flux2KleinPipeline
from dotenv import load_dotenv
from huggingface_hub import login
from PIL import Image

load_dotenv()
login(token=os.environ.get("HF_TOKEN"))

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
MANIFEST_PATH = "scripts/figma_manifest.json"
TOY_SPECS_PATH = "units/unit1/toy_specs.md"
OUTPUT_PATH = "scripts/experiment_output.html"

manifest = json.loads(Path(MANIFEST_PATH).read_text())
lines = Path(TOY_SPECS_PATH).read_text(encoding="utf-8").splitlines()
toy_specs_section = "\n".join(lines[3059:3831])

claude = anthropic.Anthropic()

print("Loading FLUX.2-Klein model...")
flux_pipe = Flux2KleinPipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B",
    torch_dtype=torch.bfloat16,
    device_map="balanced",
)
print("Model loaded.")


# --- Helpers ---


def fetch_figma_frame(node_id: str) -> str:
    """Fetch Figma frame, compress, return base64 PNG."""
    node_id_fmt = node_id.replace(":", "-")
    r = requests.get(
        f"https://api.figma.com/v1/images/{FILE_KEY}",
        headers={"X-Figma-Token": FIGMA_TOKEN},
        params={"ids": node_id_fmt, "format": "png", "scale": 1},
    )
    r.raise_for_status()
    url = r.json()["images"][node_id]
    img = Image.open(io.BytesIO(requests.get(url).content))
    img = img.resize((img.width // 2, img.height // 2))
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")


def edit_frame_with_flux(img_b64: str, edit_prompt: str) -> str | None:
    """
    Use FLUX.2-Klein to edit a Figma frame using a Claude-generated prompt.
    Returns edited image as base64 PNG, or None on failure.
    """
    try:
        ref_image = Image.open(io.BytesIO(base64.b64decode(img_b64))).convert("RGB")
        full_prompt = (
            f"{edit_prompt}. "
            "Keep the exact same UI layout, background, guide character, buttons, and visual style. "
            "Only change the interactive content area. "
            "Match the existing flat illustration style exactly."
        )
        w, h = ref_image.size
        result = flux_pipe(
            image=ref_image,
            prompt=full_prompt,
            height=h,
            width=w,
            guidance_scale=4.0,
            num_inference_steps=4,
            generator=torch.Generator(device="cpu").manual_seed(42),
        ).images[0]
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"  [flux error] {e}")
    return None


# --- Claude tool definition ---

tools = [
    {
        "name": "fetch_figma_frame",
        "description": (
            "Fetch a Figma frame as an image by its node_id from the manifest. "
            "Use this to visually inspect a frame before writing a scene beat for it."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "node_id": {
                    "type": "string",
                    "description": "node_id from manifest (e.g. '11254:42318')",
                },
                "slug": {"type": "string", "description": "manifest slug (e.g. '10x10-groups')"},
            },
            "required": ["node_id", "slug"],
        },
    },
    {
        "name": "generate_edit_prompt",
        "description": (
            "Write a precise Gemini image editing prompt for a fetched frame, based on what "
            "you saw in the image and what the scene beat params require. Call this after "
            "fetch_figma_frame and before finalising the scene beat. "
            "Describe specifically what needs to change in the interactive area — "
            "e.g. how many groups, how many items per group, what the items look like, "
            "what stays the same. Be concrete and visual, not abstract."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "slug": {"type": "string", "description": "manifest slug of the frame to edit"},
                "prompt": {
                    "type": "string",
                    "description": (
                        "The editing instruction for Gemini. Describe what the image currently "
                        "shows, what needs to change, and what must stay the same. "
                        "Reference the actual visual elements you observed."
                    ),
                },
            },
            "required": ["slug", "prompt"],
        },
    },
]

system_prompt = f"""You are a lesson script author for an interactive Grade 3 math product.

Your workflow per scene beat:
1. Call fetch_figma_frame to visually inspect a frame
2. Call generate_edit_prompt to write a precise Gemini editing instruction based on what
   you see and what the scene beat params require — describe what currently exists,
   what needs to change, and what must stay the same
3. Write the scene beat grounded in what you observed

Toy specs for Equal Groups:
<toy_specs>
{toy_specs_section}
</toy_specs>

Available Figma frames:
<manifest>
{json.dumps(manifest, indent=2)}
</manifest>

Output a lesson script with 6-10 beats introducing equal groups for Module 7.
Beat types:
- dialogue: {{"type": "dialogue", "text": "..."}}
- prompt: {{"type": "prompt", "text": "...", "tool": "...", "target": "..."}}
- scene: {{"type": "scene", "method": "add"|"animate"|"remove", "tangible_id": "...",
          "tangible_type": "equal_groups", "params": {{...}}, "figma_ref": "<slug>"}}

Rules:
- Fetch at least 3 frames before writing scene beats
- params must include: groups, items_per_group, grouping_type, item_type, mode
- figma_ref = the manifest slug this beat is visually based on
- Return final script as JSON array in a ```json block
"""

# --- Claude tool-use loop ---

fetched_images = {}  # slug -> base64
edit_prompts = {}  # slug -> gemini edit prompt written by Claude
messages = [
    {"role": "user", "content": "Generate a lesson script introducing equal groups for Module 7."}
]

print("Running Claude tool-use loop...\n")

while True:
    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=system_prompt,
        tools=tools,
        messages=messages,
    )

    for block in response.content:
        if hasattr(block, "text") and block.text.strip():
            print(block.text[:200] + "..." if len(block.text) > 200 else block.text)

    if response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            slug = block.input.get("slug", "")
            node_id = block.input.get("node_id", "")
            if block.name == "fetch_figma_frame":
                print(f"  [fetch] {slug} ({node_id})")
                try:
                    img_b64 = fetch_figma_frame(node_id)
                    fetched_images[slug] = img_b64
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": [
                                {
                                    "type": "image",
                                    "source": {
                                        "type": "base64",
                                        "media_type": "image/png",
                                        "data": img_b64,
                                    },
                                }
                            ],
                        }
                    )
                except Exception as e:
                    print(f"  [error] {e}")
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": f"Error: {e}",
                            "is_error": True,
                        }
                    )

            elif block.name == "generate_edit_prompt":
                slug = block.input["slug"]
                prompt = block.input["prompt"]
                edit_prompts[slug] = prompt
                print(f"  [edit prompt] {slug}: {prompt[:80]}...")
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Edit prompt stored for {slug}.",
                    }
                )

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
    else:
        messages.append({"role": "assistant", "content": response.content})
        break

# --- Extract script ---

final_text = "".join(b.text for b in response.content if hasattr(b, "text"))
script_beats = []
if "```json" in final_text:
    raw = final_text.split("```json")[1].split("```")[0].strip()
    try:
        script_beats = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Warning: could not parse script JSON: {e}")

print(f"\nScript: {len(script_beats)} beats | Frames fetched: {len(fetched_images)}")

# --- Gemini editing pass ---
# For each scene beat, edit the source frame to match the exact params

print("\nRunning Gemini editing pass...")
edited_images = {}  # slug -> edited base64

for beat in script_beats:
    if beat.get("type") != "scene":
        continue
    slug = beat.get("figma_ref", "")
    if not slug or slug not in fetched_images or slug in edited_images:
        continue

    prompt = edit_prompts.get(slug)
    if not prompt:
        print(f"  [gemini skip] {slug} — no edit prompt from Claude")
        continue

    print(f"  [gemini edit] {slug}")
    edited = edit_frame_with_flux(fetched_images[slug], prompt)
    if edited:
        edited_images[slug] = edited
        print("    → edited successfully")
    else:
        print("    → failed, using original")

print(f"Edited: {len(edited_images)} frames")


# --- HTML rendering ---


def render_frame(slug: str) -> str:
    """Render original + edited image side by side if edit exists, else just original."""
    original = fetched_images.get(slug)
    edited = edited_images.get(slug)

    if not original:
        return '<div class="no-image">no frame fetched</div>'

    original_html = f'<div class="frame-col"><div class="frame-label">source frame</div><img src="data:image/png;base64,{original}" alt="{slug}"></div>'

    if edited:
        edited_html = f'<div class="frame-col"><div class="frame-label edited-label">edited for scene</div><img src="data:image/png;base64,{edited}" alt="{slug} edited"></div>'
        return f'<div class="frame-pair">{original_html}{edited_html}</div>'

    return f'<div class="frame-pair">{original_html}</div>'


def beat_html(beat: dict) -> str:
    btype = beat.get("type", "unknown")

    if btype == "dialogue":
        return f'<div class="beat dialogue"><span class="label">dialogue</span><p>{beat.get("text", "")}</p></div>'

    if btype == "prompt":
        return (
            f'<div class="beat prompt"><span class="label">prompt</span>'
            f"<p>{beat.get('text', '')}</p>"
            f"<code>tool: {beat.get('tool', '')} → {beat.get('target', '')}</code></div>"
        )

    if btype == "scene":
        slug = beat.get("figma_ref", "")
        params = json.dumps(beat.get("params", {}), indent=2)
        return (
            f'<div class="beat scene"><span class="label">scene · {beat.get("method", "")} · {beat.get("tangible_type", "")}</span>'
            f'<div class="scene-body">'
            f"{render_frame(slug)}"
            f'<pre class="scene-params">{params}</pre>'
            f"</div>"
            f"{"<div class='figma-ref'>figma_ref: " + slug + '</div>' if slug else ''}"
            f"</div>"
        )

    return f'<div class="beat unknown"><pre>{json.dumps(beat, indent=2)}</pre></div>'


beats_html = "\n".join(beat_html(b) for b in script_beats)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Figma Experiment — Lesson Script</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 1100px; margin: 40px auto; padding: 0 24px; background: #f9f9f9; color: #1a1a1a; }}
    h1 {{ font-size: 1.4rem; margin-bottom: 4px; }}
    .meta {{ color: #888; font-size: 0.85rem; margin-bottom: 32px; }}
    .beat {{ background: white; border-radius: 8px; padding: 16px 20px; margin-bottom: 16px; border-left: 4px solid #ccc; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
    .beat.dialogue {{ border-left-color: #4f8ef7; }}
    .beat.prompt   {{ border-left-color: #f7a94f; }}
    .beat.scene    {{ border-left-color: #4fc98e; }}
    .beat.unknown  {{ border-left-color: #e04f4f; }}
    .label {{ font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 8px; }}
    .beat.dialogue .label {{ color: #4f8ef7; }}
    .beat.prompt   .label {{ color: #f7a94f; }}
    .beat.scene    .label {{ color: #4fc98e; }}
    p {{ margin: 0 0 8px; line-height: 1.5; }}
    code {{ font-size: 0.8rem; background: #f0f0f0; padding: 2px 6px; border-radius: 4px; display: inline-block; }}
    .scene-body {{ display: flex; gap: 20px; align-items: flex-start; margin-top: 8px; }}
    .frame-pair {{ display: flex; gap: 12px; flex-shrink: 0; }}
    .frame-col {{ display: flex; flex-direction: column; gap: 4px; }}
    .frame-col img {{ max-width: 300px; border-radius: 6px; border: 1px solid #e0e0e0; display: block; }}
    .frame-label {{ font-size: 0.68rem; color: #aaa; text-transform: uppercase; letter-spacing: 0.04em; }}
    .edited-label {{ color: #4fc98e; }}
    .no-image {{ width: 200px; height: 120px; background: #f0f0f0; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: #aaa; font-size: 0.8rem; }}
    pre.scene-params {{ background: #f5f5f5; border-radius: 6px; padding: 12px; font-size: 0.78rem; flex: 1; margin: 0; overflow-x: auto; white-space: pre-wrap; }}
    .figma-ref {{ font-size: 0.75rem; color: #aaa; margin-top: 8px; }}
  </style>
</head>
<body>
  <h1>Figma Visual Grounding — Experiment Output</h1>
  <p class="meta">Module 7 · Equal Groups · {len(script_beats)} beats · {len(fetched_images)} frames fetched · {len(edited_images)} edited by FLUX.2-Klein</p>
  {beats_html if beats_html else '<p style="color:#e04f4f">No script beats parsed.</p>'}
</body>
</html>"""

Path(OUTPUT_PATH).write_text(html, encoding="utf-8")
print(f"\nDone → {OUTPUT_PATH}")
