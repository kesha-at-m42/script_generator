"""
Fetches all frames from figma_nodes_raw.json, sends each to Claude for
auto-description, and writes figma_manifest.json.
Run once to bootstrap the manifest.
"""

import base64
import io
import json
import os

import anthropic
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
RAW_NODES_PATH = "scripts/figma_nodes_raw.json"
MANIFEST_PATH = "scripts/figma_manifest.json"

client = anthropic.Anthropic()

# Load nodes from previous manifest run
with open(RAW_NODES_PATH) as f:
    nodes = json.load(f)

frame_nodes = [n for n in nodes if n.get("type") == "FRAME"]
print(f"Found {len(frame_nodes)} FRAME nodes to describe\n")

# Batch export all frame IDs from Figma in one call
node_ids = ",".join(n["id"] for n in frame_nodes)
print("Fetching image URLs from Figma...")
r = requests.get(
    f"https://api.figma.com/v1/images/{FILE_KEY}",
    headers={"X-Figma-Token": FIGMA_TOKEN},
    params={"ids": node_ids, "format": "png", "scale": 1},
)
r.raise_for_status()
image_urls = r.json().get("images", {})
print(f"Got {len(image_urls)} image URLs\n")


def fetch_and_compress(url):
    img = Image.open(io.BytesIO(requests.get(url).content))
    img = img.resize((img.width // 2, img.height // 2))
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")


def describe_frame(name, image_data):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": f"""This is a Figma frame named "{name}" from an educational math toy for Grade 3 students.

Describe it in 1-2 sentences covering:
- What type of toy/interaction is shown
- Key visual state (e.g. number of groups, items, scaffold level, mode)
- Any notable UI elements

Be specific and concise. No preamble.""",
                    },
                ],
            }
        ],
    )
    return response.content[0].text.strip()


manifest = {}

for i, node in enumerate(frame_nodes):
    node_id = node["id"]
    name = node["name"]
    url = image_urls.get(node_id)

    if not url:
        print(f"[{i + 1}/{len(frame_nodes)}] SKIP (no image URL): {name}")
        continue

    print(f"[{i + 1}/{len(frame_nodes)}] Describing: {name}")
    try:
        image_data = fetch_and_compress(url)
        description = describe_frame(name, image_data)
        slug = name.lower().replace(" ", "-").replace("/", "-")
        manifest[slug] = {
            "node_id": node_id,
            "name": name,
            "description": description,
        }
        print(f"    → {description}\n")
    except Exception as e:
        print(f"    ERROR: {e}\n")

with open(MANIFEST_PATH, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"Manifest saved to {MANIFEST_PATH} ({len(manifest)} entries)")
