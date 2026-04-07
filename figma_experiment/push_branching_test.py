"""
One-off script: push tests/test_outputs/s2_4_branching_test.json to a new Notion page
to verify branch_condition rendering.
"""

import json
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv(project_root / ".env")

from notion_client import Client
from utils.lesson_notion_format import lesson_to_blocks

PARENT_PAGE_ID = os.environ["NOTION_PARENT_PAGE_ID"]
TEST_FILE = project_root / "tests/test_outputs/s2_4_branching_test.json"

data = json.loads(TEST_FILE.read_text())
blocks = lesson_to_blocks(data)

client = Client(auth=os.environ["NOTION_API_KEY"])

page = client.pages.create(
    parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
    properties={"title": [{"text": {"content": "s2_4 branch_condition rendering test"}}]},
)
page_id = page["id"]
print(f"Created page: https://notion.so/{page_id.replace('-', '')}")

# Append in chunks of 100 (Notion API limit)
for i in range(0, len(blocks), 100):
    client.blocks.children.append(block_id=page_id, children=blocks[i:i+100])

print("Done.")
