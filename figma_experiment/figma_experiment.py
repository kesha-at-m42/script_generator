"""
Figma visual grounding experiment.
Claude uses tool_use to select and fetch Figma frames, grounding the beats
of a specific lesson section. Gemini then generates an edited image for each
scene beat matching its described state.
Output: HTML file with beats + source frame + Gemini-generated image side by side.
"""

import base64
import io
import json
import os
from pathlib import Path

import anthropic
from google import genai
from google.genai import types
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
MANIFEST_PATH = "figma_experiment/figma_manifest.json"
LESSON_PATH = "outputs/unit1/lesson_generator_dialogue_pass_module_11/v31/step_11_merge_remediation/merge_remediation.json"
SECTION_ID = "s3_4_open_specification_build_given_total"
OUTPUT_PATH = "figma_experiment/experiment_output.html"

manifest = json.loads(Path(MANIFEST_PATH).read_text())
lesson = json.loads(Path(LESSON_PATH).read_text())
section = next(s for s in lesson if s["id"] == SECTION_ID)
section_beats = section["beats"]

claude = anthropic.Anthropic()
gemini = genai.Client(api_key=GEMINI_API_KEY)

print(f"Section: {SECTION_ID} ({len(section_beats)} beats)")


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


def edit_frame_with_gemini(img_b64: str, edit_prompt: str) -> str | None:
    """
    Use Gemini to generate an edited version of a Figma frame.
    Returns edited image as base64 PNG, or None on failure.
    """
    try:
        ref_bytes = base64.b64decode(img_b64)
        full_prompt = (
            f"{edit_prompt}. "
            "Keep the exact same UI layout, background, guide character, buttons, and visual style. "
            "Only change the interactive content area to match the described state. "
            "Match the existing flat illustration style exactly."
        )
        response = gemini.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[
                types.Part.from_bytes(data=ref_bytes, mime_type="image/png"),
                full_prompt,
            ],
        )
        for part in response.candidates[0].content.parts:
            if hasattr(part, "inline_data") and part.inline_data:
                return base64.b64encode(part.inline_data.data).decode("utf-8")
    except Exception as e:
        print(f"  [gemini error] {e}")
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

system_prompt = f"""You are reviewing an existing lesson section for an interactive Grade 3 math product.

Your workflow per scene beat:
1. Call fetch_figma_frame to find the best-matching Figma frame for the beat's tangible_type and state
2. Call generate_edit_prompt to write a precise Gemini editing instruction — describe what the
   frame currently shows, what needs to change to match the beat's described state, and what stays the same
3. Assign that frame as the figma_ref for the beat

Focus on scene beats that add or animate arrays, row_builder, column_builder, or equation_builder.
Skip dialogue, prompt, and current_scene beats.

Section beats to ground:
<beats>
{json.dumps(section_beats, indent=2)}
</beats>

Available Figma frames (Arrays section):
<manifest>
{json.dumps(manifest, indent=2)}
</manifest>

Rules:
- Fetch at least one frame per unique tangible_type in the section
- figma_ref = the manifest slug that best represents this beat's visual state
- Return final mapping as JSON array in a ```json block:
  [{{"beat_id": "...", "tangible_type": "...", "figma_ref": "<slug>", "node_id": "..."}}]
"""

# --- Claude tool-use loop ---

fetched_images = {}  # slug -> base64
edit_prompts = {}  # slug -> gemini edit prompt written by Claude
messages = [
    {"role": "user", "content": f"Ground the scene beats of section {SECTION_ID} against the Figma manifest."}
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

# --- Extract grounding map ---

final_text = "".join(b.text for b in response.content if hasattr(b, "text"))
grounding = []
if "```json" in final_text:
    raw = final_text.split("```json")[1].split("```")[0].strip()
    try:
        grounding = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Warning: could not parse grounding JSON: {e}")

grounding_by_beat = {g["beat_id"]: g for g in grounding}
print(f"\nGrounded {len(grounding)} beats | Frames fetched: {len(fetched_images)}")

# --- Gemini editing pass ---
# For each grounded scene beat, edit the source frame to match the beat's described state

print("\nRunning Gemini editing pass...")
edited_images = {}  # slug -> edited base64

for beat in section_beats:
    if beat.get("type") != "scene":
        continue
    bid = beat.get("id", "")
    ground = grounding_by_beat.get(bid)
    if not ground:
        continue
    slug = ground.get("figma_ref", "")
    if not slug or slug not in fetched_images or slug in edited_images:
        continue

    prompt = edit_prompts.get(slug)
    if not prompt:
        print(f"  [gemini skip] {slug} — no edit prompt from Claude")
        continue

    print(f"  [gemini edit] {slug}")
    edited = edit_frame_with_gemini(fetched_images[slug], prompt)
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
    bid = beat.get("id", "")

    if btype == "dialogue":
        return f'<div class="beat dialogue"><span class="label">dialogue</span><p>{beat.get("text", "")}</p></div>'

    if btype == "prompt":
        return (
            f'<div class="beat prompt"><span class="label">prompt</span>'
            f"<p>{beat.get('text', '')}</p>"
            f"<code>tool: {beat.get('tool', '')} → {beat.get('target', '')}</code></div>"
        )

    if btype == "scene":
        ground = grounding_by_beat.get(bid)
        slug = ground["figma_ref"] if ground else ""
        params = json.dumps(beat.get("params", {}), indent=2)
        return (
            f'<div class="beat scene"><span class="label">scene · {beat.get("method", "")} · {beat.get("tangible_type", "")}</span>'
            f'<div class="scene-body">'
            f"{render_frame(slug)}"
            f'<pre class="scene-params">{params}</pre>'
            f"</div>"
            f"{'<div class=\"figma-ref\">figma_ref: ' + slug + '</div>' if slug else ''}"
            f"</div>"
        )

    if btype == "current_scene":
        elements = ", ".join(e.get("tangible_id", "") for e in beat.get("elements", []))
        return f'<div class="beat current-scene"><span class="label">current scene</span><p>{elements}</p></div>'

    return f'<div class="beat unknown"><pre>{json.dumps(beat, indent=2)}</pre></div>'


beats_html = "\n".join(beat_html(b) for b in section_beats)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Figma Experiment — {SECTION_ID}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 1100px; margin: 40px auto; padding: 0 24px; background: #f9f9f9; color: #1a1a1a; }}
    h1 {{ font-size: 1.4rem; margin-bottom: 4px; }}
    .meta {{ color: #888; font-size: 0.85rem; margin-bottom: 32px; }}
    .beat {{ background: white; border-radius: 8px; padding: 16px 20px; margin-bottom: 16px; border-left: 4px solid #ccc; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
    .beat.dialogue      {{ border-left-color: #4f8ef7; }}
    .beat.prompt        {{ border-left-color: #f7a94f; }}
    .beat.scene         {{ border-left-color: #4fc98e; }}
    .beat.current-scene {{ border-left-color: #ddd; background: #f5f5f5; }}
    .beat.unknown       {{ border-left-color: #e04f4f; }}
    .label {{ font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 8px; }}
    .beat.dialogue .label      {{ color: #4f8ef7; }}
    .beat.prompt   .label      {{ color: #f7a94f; }}
    .beat.scene    .label      {{ color: #4fc98e; }}
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
  <h1>Figma Visual Grounding — {SECTION_ID}</h1>
  <p class="meta">{len(section_beats)} beats · {len(fetched_images)} frames fetched · {len(edited_images)} edited by Gemini</p>
  {beats_html if beats_html else '<p style="color:#e04f4f">No beats rendered.</p>'}
</body>
</html>"""

Path(OUTPUT_PATH).write_text(html, encoding="utf-8")
print(f"\nDone → {OUTPUT_PATH}")
