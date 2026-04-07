"""
Explore a Figma file's top-level structure and direct children of a node.
Run once to find the right parent node ID before building the manifest.
"""

import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
NODE_ID = "17936-124560"  # Arrays section


def fetch_node(file_key, node_id):
    # Pages are fetched differently — use depth=2 on the file and find the page
    r = requests.get(
        f"https://api.figma.com/v1/files/{file_key}",
        headers={"X-Figma-Token": FIGMA_TOKEN},
        params={"ids": node_id, "depth": 2},
    )
    r.raise_for_status()
    pages = r.json()["document"]["children"]
    node_id_colon = node_id.replace("-", ":")
    for page in pages:
        if page["id"] == node_id_colon:
            return page
    raise ValueError(f"Node {node_id} not found in file pages")


def fetch_file_pages(file_key):
    r = requests.get(
        f"https://api.figma.com/v1/files/{file_key}",
        headers={"X-Figma-Token": FIGMA_TOKEN},
        params={"depth": 1},
    )
    r.raise_for_status()
    return r.json()["document"]["children"]


# --- Show top-level pages ---
print("=" * 60)
print("PAGES IN FILE")
print("=" * 60)
pages = fetch_file_pages(FILE_KEY)
for page in pages:
    print(f"  {page['id']:<25} {page['name']}")

# --- Show direct FRAME children of target node ---
print()
print("=" * 60)
print(f"DIRECT FRAME CHILDREN OF {NODE_ID}")
print("=" * 60)
node = fetch_node(FILE_KEY, NODE_ID)
direct_frames = [
    c
    for c in node.get("children", [])
    if c.get("type") in ("FRAME", "COMPONENT", "INSTANCE", "GROUP")
]

print(f"{'NODE ID':<25} {'TYPE':<15} NAME")
print("-" * 70)
for c in direct_frames:
    print(f"  {c['id']:<25} {c.get('type', ''):<15} {c['name']}")

print(f"\nTotal direct children shown: {len(direct_frames)}")

# Save for reference
with open("scripts/figma_nodes_raw.json", "w") as f:
    json.dump(direct_frames, f, indent=2, default=str)
print("Saved direct children to scripts/figma_nodes_raw.json")
