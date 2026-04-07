"""
figma_visual_dict.py — Build units/unit1/visual_dict.md.

Fetches the direct children of a root Figma node, exports them as PNGs,
sends each to Claude for a visual description, and writes visual_dict.md
with embedded images and descriptions.

Usage:
    python figma_experiment/figma_visual_dict.py
"""

import base64
import io
import os
from pathlib import Path

import anthropic
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
ROOT_NODE = "17936:124560"  # parent node from Figma dev link

ASSETS_DIR = Path("units/unit1/assets/visual_dict")
OUTPUT_PATH = Path("units/unit1/visual_dict.md")

HEADERS = {"X-Figma-Token": FIGMA_TOKEN}
claude = anthropic.Anthropic()


# ---------------------------------------------------------------------------
# Figma helpers (same pattern as figma_auto_describe.py)
# ---------------------------------------------------------------------------


def fetch_children(node_id: str) -> list[dict]:
    node_id_fmt = node_id.replace(":", "-")
    r = requests.get(
        f"https://api.figma.com/v1/files/{FILE_KEY}/nodes",
        headers=HEADERS,
        params={"ids": node_id_fmt, "depth": 2},
    )
    r.raise_for_status()
    nodes = r.json().get("nodes", {})
    node_data = nodes.get(node_id) or nodes.get(node_id_fmt)
    if not node_data:
        raise ValueError(f"Node {node_id} not found")
    doc = node_data["document"]
    print(f"Root: {doc.get('name')} ({doc.get('type')}), {len(doc.get('children', []))} children")
    return doc.get("children", [])


def batch_export_urls(node_ids: list[str]) -> dict[str, str]:
    ids = ",".join(nid.replace(":", "-") for nid in node_ids)
    r = requests.get(
        f"https://api.figma.com/v1/images/{FILE_KEY}",
        headers=HEADERS,
        params={"ids": ids, "format": "png", "scale": 2},
    )
    r.raise_for_status()
    return r.json().get("images", {})


def fetch_and_compress(url: str) -> bytes:
    img = Image.open(io.BytesIO(requests.get(url).content))
    img = img.resize((img.width // 2, img.height // 2))
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


# ---------------------------------------------------------------------------
# Claude description (same pattern as figma_auto_describe.py)
# ---------------------------------------------------------------------------


def describe_frame(name: str, img_bytes: bytes) -> str:
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": "image/png", "data": img_b64},
                    },
                    {
                        "type": "text",
                        "text": (
                            f'This is a Figma frame named "{name}" from an interactive math toy for Grade 3 students.\n\n'
                            "Describe it in 1-2 sentences covering:\n"
                            "- What type of toy/interaction is shown\n"
                            "- Key visual state (mode, values, scaffold level)\n"
                            "- Any notable UI elements\n\n"
                            "Be specific and concise. No preamble."
                        ),
                    },
                ],
            }
        ],
    )
    return response.content[0].text.strip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Get children of root node
    children = fetch_children(ROOT_NODE)
    frame_children = [
        c for c in children
        if c.get("type") in ("FRAME", "COMPONENT", "COMPONENT_SET", "INSTANCE", "GROUP")
    ]
    print(f"\n{len(frame_children)} frame children:")
    for c in frame_children:
        print(f"  {c['id']:<25} {c['name']}")

    if not frame_children:
        print("No frame children found.")
        return

    # 2. Batch fetch image URLs
    print("\nFetching image URLs from Figma...")
    node_ids = [c["id"] for c in frame_children]
    image_urls = batch_export_urls(node_ids)
    print(f"Got {len(image_urls)} URLs")

    # 3. Download, describe, save PNG for each frame
    results = []  # [{"node_id", "name", "description", "png_path"}]

    for i, child in enumerate(frame_children):
        nid = child["id"]
        name = child["name"]
        url = image_urls.get(nid) or image_urls.get(nid.replace(":", "-"))

        if not url:
            print(f"[{i+1}/{len(frame_children)}] SKIP (no URL): {name}")
            continue

        print(f"[{i+1}/{len(frame_children)}] {name}")

        try:
            img_bytes = fetch_and_compress(url)

            # Save PNG
            slug = name.lower().replace(" ", "_").replace("/", "_")
            png_path = ASSETS_DIR / f"{slug}.png"
            png_path.write_bytes(img_bytes)

            # Describe with Claude
            description = describe_frame(name, img_bytes)
            print(f"    → {description[:80]}...")

            results.append({
                "node_id": nid,
                "name": name,
                "description": description,
                "png_path": png_path,
            })
        except Exception as e:
            print(f"    ERROR: {e}")

    # 4. Write visual_dict.md
    lines = [
        "# Unit 1 — Visual Dictionary",
        "",
        "UI screenshots and descriptions of each canonical toy.",
        "Re-generated by `figma_experiment/figma_visual_dict.py`.",
        "",
    ]

    for entry in results:
        lines.append(f"## {entry['name']}")
        lines.append("")
        lines.append(entry["description"])
        lines.append("")
        rel = entry["png_path"].relative_to(OUTPUT_PATH.parent)
        lines.append(f"![{entry['name']}]({rel})")
        lines.append(f"<small>`{entry['node_id']}`</small>")
        lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {OUTPUT_PATH} ({len(results)} entries)")


if __name__ == "__main__":
    main()
