"""Notion integration — push JSON data to Notion pages for review and comments.

Architecture
------------
JSON files (source of truth)  ──push──►  Notion pages (review / comment layer)
                               ◄──pull──  (reads the raw JSON code block)

Every push appends a hidden "Raw JSON" code block at the bottom of the page.
Pull reads that code block and parses it, so the round-trip is lossless even
if reviewers edit the human-readable section above it.

Setup
-----
Add to .env:
    NOTION_API_KEY=secret_...
    NOTION_PARENT_PAGE_ID=<page-id of the parent page in your workspace>

Usage
-----
    from utils.notion_sync import push_to_notion, pull_from_notion, get_page_url, is_configured

    if is_configured():
        page_id = push_to_notion(data, title="Module 4", file_path=path)
        url = get_page_url(page_id)

    data = pull_from_notion(page_id)
    comments = get_page_comments(page_id)
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from notion_client import Client

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# Registry of { relative_file_path: { page_id, title, pushed_at } }
_REGISTRY_PATH = Path(__file__).parent.parent / "config" / "notion_pages.json"

# Notion's hard limit for a single rich_text span is 2000 chars.
# We use 1900 to stay safely under it.
_RT_LIMIT = 1900


# ---------------------------------------------------------------------------
# Client & helpers
# ---------------------------------------------------------------------------


def is_configured() -> bool:
    """Return True if both required env vars are present."""
    return bool(os.getenv("NOTION_API_KEY")) and bool(os.getenv("NOTION_PARENT_PAGE_ID"))


def get_notion_client() -> Client:
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        raise ValueError("NOTION_API_KEY is not set in your .env file.")
    return Client(auth=api_key)


def get_page_url(page_id: str) -> str:
    return f"https://notion.so/{page_id.replace('-', '')}"


# ---------------------------------------------------------------------------
# Page registry  (config/notion_pages.json)
# ---------------------------------------------------------------------------


def _registry_key(file_path: Path) -> str:
    """Stable, version-agnostic key: path relative to project root.

    Strips version directories (v0, v1, …) and everything after them so that
    outputs/unit1/pipeline/v0/step_01_foo/foo.json  →  outputs/unit1/pipeline/notion_page.json
    outputs/unit1/pipeline/v1/step_01_foo/foo.json  →  same key (updates same page)
    outputs/unit1/pipeline2/v0/…                    →  different key (new page)
    Paths without a version component are returned as-is (e.g. lesson.json).
    """
    try:
        root = Path(__file__).parent.parent
        rel = str(file_path.resolve().relative_to(root.resolve())).replace("\\", "/")
        parts = rel.split("/")
        for i, part in enumerate(parts):
            if re.match(r"^v\d+$", part):
                return "/".join(parts[:i]) + "/notion_page.json"
        return rel
    except ValueError:
        return str(file_path)


def load_registry() -> dict:
    if _REGISTRY_PATH.exists():
        return json.loads(_REGISTRY_PATH.read_text(encoding="utf-8"))
    return {}


def save_registry(registry: dict) -> None:
    _REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    _REGISTRY_PATH.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def get_registry_entry(file_path: Path) -> dict | None:
    return load_registry().get(_registry_key(file_path))


def get_file_path_for_page(page_id: str) -> Path | None:
    """Reverse lookup: return the source file Path for a given page_id, or None."""
    root = Path(__file__).parent.parent
    normalised = page_id.replace("-", "")
    for key, entry in load_registry().items():
        if entry.get("page_id", "").replace("-", "") == normalised:
            return root / key
    return None


def set_registry_entry(file_path: Path, page_id: str, title: str) -> None:
    registry = load_registry()
    registry[_registry_key(file_path)] = {
        "page_id": page_id,
        "title": title,
        "pushed_at": datetime.now(timezone.utc).isoformat(),
    }
    save_registry(registry)


# ---------------------------------------------------------------------------
# Notion block builders
# ---------------------------------------------------------------------------


def _rt(text: str) -> list[dict]:
    """Single rich_text span (truncated to Notion's limit)."""
    return [{"text": {"content": str(text)[:_RT_LIMIT]}}]


def _heading(level: int, text: str) -> dict:
    t = f"heading_{level}"
    return {"object": "block", "type": t, t: {"rich_text": _rt(text)}}


def _paragraph(text: str) -> dict:
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": _rt(str(text))}}


def _bullet(text: str) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": _rt(str(text))},
    }


def _toggle(text: str, children: list[dict]) -> dict:
    return {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": _rt(text),
            "children": children or [_paragraph("—")],
        },
    }


def _divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def _code_blocks(text: str) -> list[dict]:
    """Split a long string into ≤ _RT_LIMIT-char code blocks."""
    return [
        {
            "object": "block",
            "type": "code",
            "code": {
                "language": "json",
                "rich_text": [{"text": {"content": text[i : i + _RT_LIMIT]}}],
            },
        }
        for i in range(0, len(text), _RT_LIMIT)
    ]


# ---------------------------------------------------------------------------
# JSON → Notion blocks  (human-readable view)
# ---------------------------------------------------------------------------

_LABEL_HINTS = (
    "name",
    "title",
    "misconception",
    "label",
    "phase_name",
    "problem_instance_id",
    "id",
)


def _item_label(item: dict, index: int) -> str:
    for hint in _LABEL_HINTS:
        val = item.get(hint)
        if val is not None and str(val).strip():
            return f"{index + 1}. {val}"
    return f"Item {index + 1}"


def _value_blocks(value: Any, depth: int = 0) -> list[dict]:
    """Recursively convert a JSON value to Notion blocks."""
    if value is None:
        return [_paragraph("—")]
    if isinstance(value, bool):
        return [_paragraph("Yes" if value else "No")]
    if isinstance(value, (int, float)):
        return [_paragraph(str(value))]
    if isinstance(value, str):
        return [_paragraph(value) if value.strip() else _paragraph("—")]

    if isinstance(value, list):
        if not value:
            return [_paragraph("(empty)")]
        # List of scalars → bullets
        if all(isinstance(v, (str, int, float, bool)) or v is None for v in value):
            return [_bullet(str(v)) for v in value]
        # List of dicts → toggles
        if all(isinstance(v, dict) for v in value):
            return [
                _toggle(_item_label(item, i), _dict_blocks(item, depth + 1))
                for i, item in enumerate(value)
            ]
        # Mixed
        return [_paragraph(json.dumps(value))]

    if isinstance(value, dict):
        return _dict_blocks(value, depth)

    return [_paragraph(str(value))]


def _dict_blocks(data: dict, depth: int = 0) -> list[dict]:
    blocks: list[dict] = []
    for key, value in data.items():
        label = key.replace("_", " ").capitalize()
        blocks.append(_heading(2 if depth == 0 else 3, label))
        blocks.extend(_value_blocks(value, depth + 1))
    return blocks


def json_to_blocks(data: Any) -> list[dict]:
    """
    Convert JSON to Notion blocks:
      - Human-readable formatted section (for reading and commenting)
      - Divider
      - "Raw JSON" heading + code block(s) (used by pull_from_notion)
    """
    blocks: list[dict] = []

    if isinstance(data, dict):
        blocks.extend(_dict_blocks(data, depth=0))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                blocks.append(_heading(2, _item_label(item, i)))
                blocks.extend(_dict_blocks(item, depth=1))
            else:
                blocks.append(_bullet(str(item)))
    else:
        blocks.append(_paragraph(str(data)))

    # Raw JSON footer — used for lossless pull
    blocks.append(_divider())
    blocks.append(_heading(3, "Raw JSON — do not edit"))
    blocks.extend(_code_blocks(json.dumps(data, indent=2, ensure_ascii=False)))

    return blocks


# ---------------------------------------------------------------------------
# Notion blocks → JSON  (pull direction)
# ---------------------------------------------------------------------------


def _extract_rt(rich_text: list[dict]) -> str:
    return "".join(span.get("text", {}).get("content", "") for span in rich_text)


def blocks_to_json(blocks: list[dict]) -> Any | None:
    """
    Reconstruct the original JSON from the raw-JSON code block(s) at the
    bottom of the page.  Returns None if no code blocks are found.
    """
    raw_parts = [
        _extract_rt(block.get("code", {}).get("rich_text", []))
        for block in blocks
        if block.get("type") == "code"
    ]
    if not raw_parts:
        return None
    return json.loads("".join(raw_parts))


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------


def _all_blocks(client: Client, block_id: str, recursive: bool = False) -> list[dict]:
    """Fetch all child blocks, handling Notion's pagination.

    When recursive=True, also fetches and embeds children for any block that
    has_children (e.g. toggle headings, toggle blocks). Children are stored
    under block[block_type]["children"].
    """
    results: list[dict] = []
    cursor: str | None = None
    while True:
        kwargs: dict = {"block_id": block_id}
        if cursor:
            kwargs["start_cursor"] = cursor
        response = client.blocks.children.list(**kwargs)
        results.extend(response["results"])
        if not response["has_more"]:
            break
        cursor = response["next_cursor"]
    if recursive:
        for block in results:
            if block.get("has_children"):
                btype = block.get("type", "")
                block_data = block.get(btype, {})
                block_data["children"] = _all_blocks(client, block["id"], recursive=True)
    return results


# ---------------------------------------------------------------------------
# Block sync
# ---------------------------------------------------------------------------


def _block_content_equal(existing: dict, new_block: dict) -> bool:
    """Return True if two blocks have identical type and text content."""
    if existing.get("type") != new_block.get("type"):
        return False
    btype = existing["type"]
    ex_data = existing.get(btype, {})
    new_data = new_block.get(btype, {})
    if _extract_rt(ex_data.get("rich_text", [])) != _extract_rt(new_data.get("rich_text", [])):
        return False
    # For callouts also compare the icon emoji
    if btype == "callout":
        if ex_data.get("icon", {}).get("emoji") != new_data.get("icon", {}).get("emoji"):
            return False
    return True


_HEADING_TYPES = {"heading_1", "heading_2", "heading_3"}


def _refresh_children(client: Client, block_id: str, new_children: list[dict]) -> None:
    """Archive all existing children of block_id and append new_children."""
    for child in _all_blocks(client, block_id):
        client.blocks.update(child["id"], archived=True)
    for i in range(0, len(new_children), 100):
        client.blocks.children.append(block_id, children=new_children[i : i + 100])


def _block_skeleton(block: dict) -> str:
    """Return a structural fingerprint for a block (type + emoji for callouts)."""
    btype = block.get("type", "")
    if btype == "callout":
        emoji = block.get("callout", {}).get("icon", {}).get("emoji", "")
        return f"callout:{emoji}"
    return btype


def _update_block_content(client: Client, block_id: str, new_block: dict) -> None:
    """Update an existing Notion block's displayable content in-place.

    Children are intentionally excluded — manage those separately via
    _refresh_children so block IDs (and any comments) are preserved.
    """
    btype = new_block.get("type", "")
    bdata = dict(new_block.get(btype, {}))
    bdata.pop("children", None)
    bdata.pop("is_toggleable", None)
    if bdata:
        client.blocks.update(block_id, **{btype: bdata})


def _smart_sync_children(client: Client, parent_id: str, new_children: list[dict]) -> None:
    """Sync children of a section heading block.

    Compares the structural skeleton — the ordered sequence of block types and
    callout emojis — of new_children against existing children.

    - Skeleton matches: positional update-in-place.  Each beat's Notion block ID
      (and any reviewer comments on it) is preserved; only changed text is
      patched via blocks.update.  Toggle children (validator states, current_scene
      snapshots) recurse into _smart_sync_children so comments inside them also
      survive re-push when their structure is unchanged.
    - Skeleton differs: fall back to _refresh_children (archive all, re-append).
      This handles structural edits (added/removed beats, reordered steps) and
      also recovers from previously scrambled Notion pages where prior syncs left
      beats in the wrong order.
    """
    existing = _all_blocks(client, parent_id)

    new_skel = [_block_skeleton(b) for b in new_children]
    ex_skel = [_block_skeleton(b) for b in existing]

    if new_skel != ex_skel:
        _refresh_children(client, parent_id, new_children)
        return

    # Positional update — walk new / existing in lockstep
    for nb, eb in zip(new_children, existing):
        btype = nb["type"]
        nb_children = nb.get(btype, {}).get("children")

        if not _block_content_equal(nb, eb):
            _update_block_content(client, eb["id"], nb)

        if nb_children is not None:
            if btype == "toggle":
                _smart_sync_children(client, eb["id"], nb_children)
            else:
                _refresh_children(client, eb["id"], nb_children)
        elif eb.get("has_children"):
            # New version has no children here — clear existing ones
            for child in _all_blocks(client, eb["id"]):
                client.blocks.update(child["id"], archived=True)


def _section_sort_key(section_id: str) -> tuple:
    """Return a sort key for a section ID so headings are ordered s1_1, s1_2, …, s1_a, s1_b, …"""
    m = re.match(r"^s(\d+)_(\d+)([a-z]?)(?:_.*)?$", section_id)
    if m:
        return (int(m.group(1)), int(m.group(2)), m.group(3))
    m2 = re.match(r"^s(\d+)_([a-z].+)$", section_id)
    if m2:
        return (int(m2.group(1)), float("inf"), m2.group(2))
    return (0, 0, "")


def _sync_blocks(client: Client, parent_id: str, new_blocks: list[dict]) -> None:
    """Sync new_blocks into parent_id using forward content-matching.

    For each new block, scans forward in existing blocks to find a content match:
    - Match found: keep block in place (preserves ID and comments); archive any
      existing blocks skipped over.
    - No match: insert after the last matched/inserted block via Notion's
      ``after=`` parameter.  For heading_2 blocks (lesson sections), the insertion
      point is determined by sorted section ID order so new sections land in the
      correct position among existing ones.

    Heading blocks (section toggle headings) recurse into _smart_sync_children,
    which does positional in-place updates when the beat structure is unchanged
    and falls back to a full refresh when structure has changed.
    Toggle blocks (validator states, current_scene) are refreshed wholesale.
    """
    existing = _all_blocks(client, parent_id)
    ex_ptr = 0
    last_id: str | None = None  # ID anchor for `after=` insertions
    anchor_id: str | None = None  # ID of the 💡 reviewer guide callout (stable first block)

    # Pre-parse existing heading_2 blocks with their section sort keys.
    # Used to find the correct sorted insertion point for new sections.
    # Only pre-existing h2s are valid sort anchors — newly inserted ones must not
    # be used, because blocks inserted after them in the same sync run (dividers)
    # would end up in the wrong position.
    existing_h2s: list[tuple[dict, tuple]] = []
    pre_existing_h2_ids: set[str] = set()
    for block in existing:
        if block.get("type") == "heading_2":
            rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
            m = re.search(r"\[([^\]]+)\]\s*$", rt)
            if m:
                existing_h2s.append((block, _section_sort_key(m.group(1))))
                pre_existing_h2_ids.add(block["id"])

    for new_block in new_blocks:
        btype = new_block["type"]
        bdata = new_block.get(btype, {})
        new_children = bdata.get("children")

        # Scan forward for a content match
        match_idx = None
        for k in range(ex_ptr, len(existing)):
            if _block_content_equal(existing[k], new_block):
                match_idx = k
                break

        if match_idx is not None:
            # Archive every existing block we skipped over
            for skipped in existing[ex_ptr:match_idx]:
                client.blocks.update(skipped["id"], archived=True)

            ex = existing[match_idx]
            block_id = ex["id"]
            last_id = block_id
            ex_ptr = match_idx + 1

            # Track the 💡 anchor callout so new sections can use it as fallback after=
            if anchor_id is None and btype == "callout":
                if bdata.get("icon", {}).get("emoji") == "💡":
                    anchor_id = block_id

            if new_children is not None:
                if btype in _HEADING_TYPES:
                    _smart_sync_children(client, block_id, new_children)
                else:
                    _refresh_children(client, block_id, new_children)
            elif ex.get("has_children"):
                for child in _all_blocks(client, block_id):
                    client.blocks.update(child["id"], archived=True)
        else:
            # No match — determine insertion point
            after_id = last_id
            if btype == "heading_2":
                # Find sorted position: insert after the last existing h2 whose key < new key
                rt = _extract_rt(bdata.get("rich_text", []))
                m = re.search(r"\[([^\]]+)\]\s*$", rt)
                if m:
                    new_key = _section_sort_key(m.group(1))
                    after_h2: dict | None = None
                    for h2_block, h2_key in existing_h2s:
                        if h2_key < new_key:
                            after_h2 = h2_block
                    if after_h2 is not None and after_h2["id"] in pre_existing_h2_ids:
                        after_id = after_h2["id"]
                    else:
                        after_id = anchor_id or last_id

            kwargs: dict = {"children": [new_block]}
            if after_id is not None:
                kwargs["after"] = after_id
            resp = client.blocks.children.append(parent_id, **kwargs)
            inserted_id = resp["results"][0]["id"]
            last_id = inserted_id

            # Register the newly inserted h2 so subsequent insertions sort correctly
            if btype == "heading_2":
                rt = _extract_rt(bdata.get("rich_text", []))
                m = re.search(r"\[([^\]]+)\]\s*$", rt)
                if m:
                    new_key = _section_sort_key(m.group(1))
                    insert_at = len(existing_h2s)
                    for i, (_, k) in enumerate(existing_h2s):
                        if k > new_key:
                            insert_at = i
                            break
                    existing_h2s.insert(insert_at, ({"id": inserted_id, "type": "heading_2"}, new_key))

    # Archive remaining unmatched existing blocks
    for leftover in existing[ex_ptr:]:
        client.blocks.update(leftover["id"], archived=True)


# ---------------------------------------------------------------------------
# Notion block ID tag-back
# ---------------------------------------------------------------------------


def _tag_section(section: dict, children: list[dict]) -> None:
    """Write _notion_block_id onto each editable beat using positional alignment.

    Notion children for a section are: 🎬/💬/❔ callouts (one per scene/dialogue/
    prompt beat), 📋 toggle blocks (current_scene), and · · · paragraph separators.
    We match only the callout blocks to the corresponding editable beats, skipping
    current_scene beats and toggle/paragraph Notion blocks, so the zip aligns
    correctly across all steps.
    """
    beats = section.get("beats", [])
    editable_beats = [b for b in beats if b.get("type") in {"scene", "dialogue", "prompt"}]

    # Filter Notion children to the matching callout types (🎬 💬 ❔)
    notion_callouts = [
        b for b in children
        if b.get("type") == "callout"
        and b.get("callout", {}).get("icon", {}).get("emoji") in {"🎬", "💬", "❔"}
    ]

    for beat, nb in zip(editable_beats, notion_callouts):
        beat["_notion_block_id"] = nb["id"]


def tag_notion_ids(client: Client, page_id: str, sections: list) -> list:
    """Fetch Notion block IDs and write ``_notion_block_id`` back onto each beat.

    After a push, Notion has assigned block IDs to each rendered beat callout.
    This function reads those IDs and stores them on the corresponding beat dicts
    so that subsequent pushes can match beats by ID rather than by content text.

    Returns a modified deep copy of *sections* with ``_notion_block_id`` added to
    every beat that could be positionally matched.  Sections whose skeleton no
    longer matches the Notion page (e.g. structural edits were made in Notion
    since the last push) are skipped.
    """
    import copy
    import re

    sections = copy.deepcopy(sections)
    section_by_id = {s["id"]: s for s in sections if isinstance(s, dict) and "id" in s}

    blocks = _all_blocks(client, page_id, recursive=True)

    for block in blocks:
        if block.get("type") != "heading_2":
            continue
        rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
        m = re.search(r"\[([^\]]+)\]\s*$", rt)
        if not m:
            continue
        section = section_by_id.get(m.group(1))
        if section is None:
            continue
        children = block.get("heading_2", {}).get("children", [])
        if children:
            _tag_section(section, children)

    return sections


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def push_to_notion(
    data: Any,
    title: str,
    file_path: Path | None = None,
    existing_page_id: str | None = None,
    blocks_fn: Any | None = None,
) -> str:
    """
    Push JSON data to Notion.  Returns the Notion page ID.

    - If existing_page_id is given (or found in the registry), the page is
      updated in-place (old blocks archived, new blocks appended).
    - Otherwise a new child page is created under NOTION_PARENT_PAGE_ID.
    - The page ID is saved to the registry if file_path is provided.
    - blocks_fn: optional callable(data) -> list[dict] to override the default
      json_to_blocks renderer (e.g. lesson_to_blocks for lesson.json files).
    """
    client = get_notion_client()
    parent_page_id = os.environ["NOTION_PARENT_PAGE_ID"]

    # Look up existing page from registry
    if existing_page_id is None and file_path is not None:
        entry = get_registry_entry(file_path)
        if entry:
            existing_page_id = entry["page_id"]

    blocks = blocks_fn(data) if blocks_fn is not None else json_to_blocks(data)

    if existing_page_id:
        # Sync blocks in place — if page is gone (404), fall through to create a new one
        try:
            _sync_blocks(client, existing_page_id, blocks)
            # Update title
            client.pages.update(
                existing_page_id,
                properties={"title": {"title": [{"text": {"content": title}}]}},
            )
            page_id = existing_page_id
        except Exception as e:
            status = getattr(e, "status", None) or getattr(
                getattr(e, "response", None), "status_code", None
            )
            if status == 404:
                existing_page_id = None  # fall through to create new page below
            else:
                raise
    if not existing_page_id:
        # Create new page (first 100 blocks inline, rest appended)
        page = client.pages.create(
            parent={"page_id": parent_page_id},
            properties={"title": {"title": [{"text": {"content": title}}]}},
            children=blocks[:100],
        )
        page_id = page["id"]
        for i in range(100, len(blocks), 100):
            client.blocks.children.append(page_id, children=blocks[i : i + 100])

    if file_path is not None:
        set_registry_entry(file_path, page_id, title)

    return page_id


def push_blocks_to_notion(
    blocks: list[dict],
    title: str,
    file_path: Path | None = None,
    existing_page_id: str | None = None,
) -> str:
    """
    Push pre-built Notion blocks to a page.  Returns the page ID.

    Use this instead of push_to_notion when you've already constructed the
    blocks yourself (e.g. aggregated from multiple sources).  The registry
    and create/sync logic is identical to push_to_notion.
    """
    return push_to_notion(
        data=None,
        title=title,
        file_path=file_path,
        existing_page_id=existing_page_id,
        blocks_fn=lambda _: blocks,
    )


def pull_from_notion(page_id: str) -> Any:
    """
    Pull the original JSON data from a Notion page.
    Reads the raw-JSON code block appended during push.
    Raises ValueError if no raw JSON block is found.
    """
    client = get_notion_client()
    blocks = _all_blocks(client, page_id)
    data = blocks_to_json(blocks)
    if data is None:
        raise ValueError(
            "No raw JSON code block found on this Notion page. "
            "Was this page created by push_to_notion?"
        )
    return data


def get_page_comments(page_id: str) -> list[dict]:
    """
    Return all top-level comment threads on a Notion page.
    Each entry has: created_by, created_time, rich_text (list of spans).
    """
    client = get_notion_client()
    response = client.comments.list(block_id=page_id)
    return response.get("results", [])
