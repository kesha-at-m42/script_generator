"""utils/notion.py

Notion integration for script_generator — push, pull, and sync lesson JSON with Notion pages.

Architecture
------------
JSON files (source of truth)  ──push──►  Notion pages (review / comment layer)
                               ◄──pull──  (reads rendered callout blocks + raw JSON footer)

Every push renders the lesson as a human-readable script (emoji callouts, toggle validators)
and appends a hidden "Raw JSON" code block at the bottom of the page.
Pull merges reviewer edits from the rendered section back into the JSON.

Setup
-----
Add to .env:
    NOTION_API_KEY=secret_...
    NOTION_PARENT_PAGE_ID=<page-id of the parent page in your workspace>

Usage
-----
    from utils.notion import push_lesson, pull_lesson, is_configured, get_page_url

    if is_configured():
        page_id = push_lesson(data, title="Module 4", file_path=path)
        url = get_page_url(page_id)

    patched, flags, blocks = pull_lesson(page_id, original)
"""

from __future__ import annotations

import copy
import difflib
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


def _extract_version(file_path: Path) -> str | None:
    """Return the version component (e.g. 'v2') from the path, or None."""
    try:
        root = Path(__file__).parent.parent
        parts = str(file_path.resolve().relative_to(root.resolve())).replace("\\", "/").split("/")
        for part in parts:
            if re.match(r"^v\d+$", part):
                return part
    except ValueError:
        pass
    return None


def set_registry_entry(file_path: Path, page_id: str, title: str) -> None:
    registry = load_registry()
    entry = {
        "page_id": page_id,
        "title": title,
        "pushed_at": datetime.now(timezone.utc).isoformat(),
    }
    version = _extract_version(file_path)
    if version is not None:
        entry["last_version"] = version
    registry[_registry_key(file_path)] = entry
    save_registry(registry)


# ---------------------------------------------------------------------------
# Block primitives
# ---------------------------------------------------------------------------


def _rt(text: str) -> list[dict]:
    """Single rich_text span (truncated to Notion's limit)."""
    return [{"text": {"content": str(text)[:_RT_LIMIT]}}]


def _rt_rich(spans: list[dict]) -> list[dict]:
    """Pass through a pre-built rich_text list (truncating each span)."""
    return [
        {"text": {"content": s["text"]["content"][:_RT_LIMIT]}}
        for s in spans
        if s.get("text", {}).get("content")
    ]


def _heading(level: int, text: str, color: str = "default") -> dict:
    t = f"heading_{level}"
    block = {"object": "block", "type": t, t: {"rich_text": _rt(text)}}
    if color != "default":
        block[t]["color"] = color
    return block


def _toggle_heading(level: int, text: str, children: list[dict]) -> dict:
    t = f"heading_{level}"
    return {
        "object": "block",
        "type": t,
        t: {
            "rich_text": _rt(text),
            "is_toggleable": True,
            "children": children or [_paragraph("—")],
        },
    }


def _paragraph(text: str) -> dict:
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": _rt(str(text))},
    }


def _bullet(text: str) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": _rt(str(text))},
    }


def _divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def _toggle(summary: str, children: list[dict]) -> dict:
    return {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": _rt(summary),
            "children": children or [_paragraph("—")],
        },
    }


def _callout(text: str, emoji: str = "💬") -> dict:
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": _rt(text),
            "icon": {"type": "emoji", "emoji": emoji},
        },
    }


def _reviewer_guide_callout(reviewer_user_id: str | None = None) -> dict:
    """Anchor block — always first on every pushed page. Yellow 💡 tip for reviewers."""
    if reviewer_user_id:
        rich_text = [
            {
                "type": "text",
                "text": {
                    "content": (
                        "Toggle all sections: Ctrl+Alt+T (Win) / Cmd+Opt+T (Mac)"
                        "  •  Suggest edits: Ctrl+Shift+Alt+X"
                        "  •  Questions? "
                    )
                },
            },
            {
                "type": "mention",
                "mention": {"type": "user", "user": {"id": reviewer_user_id}},
            },
        ]
    else:
        rich_text = _rt(
            "Toggle all sections: Ctrl+Alt+T (Win) / Cmd+Opt+T (Mac)"
            "  •  Suggest edits: Ctrl+Shift+Alt+X"
            "  •  Questions? @Kesha"
        )
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": rich_text,
            "icon": {"type": "emoji", "emoji": "💡"},
            "color": "yellow_background",
        },
    }


# Block types that carry a color field inside their type-specific object
_COLORABLE_TYPES = {
    "paragraph", "heading_1", "heading_2", "heading_3",
    "bulleted_list_item", "numbered_list_item", "toggle",
    "callout", "quote", "to_do",
}


def _colorize_blocks(blocks: list[dict], color: str) -> list[dict]:
    """Recursively apply a background color to all colorable blocks."""
    result = []
    for block in blocks:
        block = dict(block)
        btype = block.get("type")
        if btype in _COLORABLE_TYPES and btype in block:
            inner = dict(block[btype])
            inner["color"] = color
            if "children" in inner:
                inner["children"] = _colorize_blocks(inner["children"], color)
            block[btype] = inner
        result.append(block)
    return result


def _column_list(columns: list[list[dict]]) -> dict:
    """Wrap a list of block-lists into a Notion column_list block."""
    return {
        "object": "block",
        "type": "column_list",
        "column_list": {
            "children": [
                {
                    "object": "block",
                    "type": "column",
                    "column": {"children": col_blocks or [_paragraph("—")]},
                }
                for col_blocks in columns
            ]
        },
    }


# ---------------------------------------------------------------------------
# Generic JSON → Notion blocks
# ---------------------------------------------------------------------------


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
        if all(isinstance(v, (str, int, float, bool)) or v is None for v in value):
            return [_bullet(str(v)) for v in value]
        if all(isinstance(v, dict) for v in value):
            return [
                _toggle(_item_label(item, i), _dict_blocks(item, depth + 1))
                for i, item in enumerate(value)
            ]
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

    blocks.append(_divider())
    blocks.append(_heading(3, "Raw JSON — do not edit"))
    blocks.extend(_code_blocks(json.dumps(data, indent=2, ensure_ascii=False)))

    return blocks


# ---------------------------------------------------------------------------
# Generic Notion blocks → JSON  (raw-footer pull)
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
# Block sync engine
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
    last_id: str | None = None
    anchor_id: str | None = None  # ID of the 💡 reviewer guide callout (stable first block)

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

        match_idx = None
        for k in range(ex_ptr, len(existing)):
            if _block_content_equal(existing[k], new_block):
                match_idx = k
                break

        if match_idx is not None:
            for skipped in existing[ex_ptr:match_idx]:
                client.blocks.update(skipped["id"], archived=True)

            ex = existing[match_idx]
            block_id = ex["id"]
            last_id = block_id
            ex_ptr = match_idx + 1

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
            after_id = last_id
            if btype == "heading_2":
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

    for leftover in existing[ex_ptr:]:
        client.blocks.update(leftover["id"], archived=True)


# ---------------------------------------------------------------------------
# Notion block ID tag-back
# ---------------------------------------------------------------------------


def _tag_section(section: dict, heading_block_id: str, beat_blocks: list[dict]) -> None:
    """Write _notion_block_id onto the section heading and each editable beat."""
    section["_notion_block_id"] = heading_block_id

    beats = section.get("beats", [])
    editable_beats = [b for b in beats if b.get("type") in {"scene", "dialogue", "prompt"}]

    notion_callouts = [
        b for b in beat_blocks
        if b.get("type") == "callout"
        and b.get("callout", {}).get("icon", {}).get("emoji") in {"🎬", "💬", "❔"}
    ]

    for beat, nb in zip(editable_beats, notion_callouts):
        beat["_notion_block_id"] = nb["id"]


def tag_notion_ids(client: Client, page_id: str, sections: list) -> list:
    """Fetch Notion block IDs and write ``_notion_block_id`` back onto each section and beat.

    Supports both flat headings (beats are page-level siblings after the H2) and
    toggle headings (beats are children of the H2).

    After a push Notion assigns block IDs to each heading and callout.
    This function stores them:
    - section["_notion_block_id"] = heading_2 block ID
    - beat["_notion_block_id"]    = callout block ID for each editable beat

    Returns a modified deep copy of *sections* with ``_notion_block_id`` added.
    """
    sections = copy.deepcopy(sections)
    section_by_id = {s["id"]: s for s in sections if isinstance(s, dict) and "id" in s}

    # recursive=True fetches children for toggle headings
    blocks = _all_blocks(client, page_id, recursive=True)

    current_section_id: str | None = None
    flat_beats: list[dict] = []
    h2_by_section: dict[str, dict] = {}  # section_id → h2 block

    def _flush_flat() -> None:
        if current_section_id and current_section_id in h2_by_section:
            section = section_by_id.get(current_section_id)
            if section:
                _tag_section(section, h2_by_section[current_section_id]["id"], flat_beats)

    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            _flush_flat()
            flat_beats = []
            rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
            m = re.search(r"\[([^\]]+)\]\s*$", rt)
            sid = m.group(1) if m else None
            current_section_id = sid
            if sid:
                h2_by_section[sid] = block
                # Toggle heading: beats are children — tag immediately
                children = block.get("heading_2", {}).get("children", [])
                if children:
                    section = section_by_id.get(sid)
                    if section:
                        _tag_section(section, block["id"], children)
                    current_section_id = None  # already handled
        elif btype == "divider":
            _flush_flat()
            flat_beats = []
            current_section_id = None
        elif current_section_id:
            flat_beats.append(block)

    _flush_flat()  # flush last section if page ends without a divider

    return sections


def _render_section_children(section: dict) -> list[dict]:
    """Return the beat content blocks for a section (without divider or heading)."""
    section_id = section["id"]
    beats = section.get("beats", [])

    branch_start = next(
        (i for i, b in enumerate(beats) if b.get("branch_name")), len(beats)
    )
    pre_branch = beats[:branch_start]
    post_branch = beats[branch_start:]

    branches: dict[str | None, list[dict]] = {}
    branch_order: list[str | None] = []
    for beat in post_branch:
        bc = beat.get("branch_name") or None
        if bc not in branches:
            branches[bc] = []
            branch_order.append(bc)
        branches[bc].append(beat)

    pre_content: list[dict] = _render_beat_group(pre_branch, section_id)

    named_branches = [bc for bc in branch_order if bc]
    if len(named_branches) == 2:
        _branch_colors = ["brown_background", "gray_background"]
        columns = []
        for i, bc in enumerate(named_branches):
            color = _branch_colors[i % len(_branch_colors)]
            col = [_heading(3, f"🔀 {bc}", color=color)]
            col.extend(_colorize_blocks(_render_beat_group(branches[bc], section_id), color))
            columns.append(col)
        branch_blocks: list[dict] = [_column_list(columns)]
        if None in branches:
            branch_blocks.extend(_render_beat_group(branches[None], section_id))
        return [*pre_content, *branch_blocks]
    else:
        content = pre_content
        for bc in branch_order:
            if bc:
                content.append(_heading(3, f"🔀 {bc}"))
            content.extend(_render_beat_group(branches[bc], section_id))
        return content


def push_section(
    client: Client,
    page_id: str,
    section: dict,
    page_blocks: list[dict] | None = None,
) -> str:
    """Push a single section to Notion (flat heading style). Returns the heading_2 block ID.

    Looks up the section on the page by heading text. If found, archives the
    old beat blocks and inserts the new ones after the heading. If not found,
    creates a new divider + heading + beats at the correct sorted position.

    page_blocks: current page children (fetched once by the caller and passed
    in to avoid redundant API calls when pushing multiple sections).
    """
    section_id = section["id"]
    num, title = _section_label(section_id)
    header = f"{num}  {title}" if num else title
    heading_text = f"{header}  [{section_id}]"
    new_beats = _render_section_children(section)

    if page_blocks is None:
        page_blocks = _all_blocks(client, page_id)

    # Locate the existing H2 for this section (by block ID if tagged, else by text)
    heading_block_id = section.get("_notion_block_id")
    h2_block: dict | None = None
    h2_idx: int | None = None
    for i, block in enumerate(page_blocks):
        if block.get("type") != "heading_2":
            continue
        if heading_block_id and block["id"] == heading_block_id:
            h2_block = block
            h2_idx = i
            break
        rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
        if f"[{section_id}]" in rt:
            h2_block = block
            h2_idx = i
            break

    if h2_block is not None:
        # Archive old beats (flat siblings between this H2 and the next H2/divider)
        old_beats = []
        for block in page_blocks[h2_idx + 1:]:
            if block.get("type") in ("heading_2", "divider"):
                break
            old_beats.append(block)
        for b in old_beats:
            client.blocks.update(b["id"], archived=True)

        # Also archive toggle-heading children (older push style stored beats inside the H2)
        if h2_block.get("has_children"):
            for child in _all_blocks(client, h2_block["id"]):
                client.blocks.update(child["id"], archived=True)

        # Convert toggle heading to plain heading if needed
        if h2_block.get("heading_2", {}).get("is_toggleable"):
            rt = h2_block["heading_2"]["rich_text"]
            client.blocks.update(h2_block["id"], heading_2={"rich_text": rt, "is_toggleable": False})

        # Insert new beats after the H2
        last_after = h2_block["id"]
        for i in range(0, max(len(new_beats), 1), 100):
            chunk = new_beats[i : i + 100]
            if not chunk:
                break
            resp = client.blocks.children.append(page_id, children=chunk, after=last_after)
            last_after = resp["results"][-1]["id"]

        return h2_block["id"]

    # Section not on page yet — insert at sorted position
    new_key = _section_sort_key(section_id)
    after_id: str | None = None
    for block in page_blocks:
        if block.get("type") != "heading_2":
            continue
        rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
        m = re.search(r"\[([^\]]+)\]\s*$", rt)
        if m and _section_sort_key(m.group(1)) < new_key:
            after_id = block["id"]

    new_h2 = _heading(2, heading_text)
    intro_blocks = [_divider(), new_h2] + new_beats[:98]
    kwargs: dict = {"children": intro_blocks}
    if after_id:
        kwargs["after"] = after_id
    resp = client.blocks.children.append(page_id, **kwargs)
    last_after = resp["results"][-1]["id"]
    for i in range(98, len(new_beats), 100):
        resp = client.blocks.children.append(page_id, children=new_beats[i : i + 100], after=last_after)
        last_after = resp["results"][-1]["id"]
    # H2 is the second block in intro_blocks
    return resp["results"][0]["id"] if len(intro_blocks) > 2 else last_after


# ---------------------------------------------------------------------------
# Public push/pull API
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

    if existing_page_id is None and file_path is not None:
        entry = get_registry_entry(file_path)
        if entry:
            existing_page_id = entry["page_id"]

    if existing_page_id:
        url = get_page_url(existing_page_id)
        print(f"Updating existing page: {url}")
        confirm = input("Overwrite this page? [y/N] ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            raise SystemExit(0)

    blocks = blocks_fn(data) if blocks_fn is not None else json_to_blocks(data)

    if existing_page_id:
        try:
            _sync_blocks(client, existing_page_id, blocks)
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
                existing_page_id = None
            else:
                raise
    if not existing_page_id:
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
    blocks yourself (e.g. aggregated from multiple sources).
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


# ---------------------------------------------------------------------------
# Section ID → human label
# ---------------------------------------------------------------------------

# s1_1_most_votes  →  ("1.1", "Most Votes")
# s2_transition    →  ("2",   "Transition")
# s3_3b_two_step   →  ("3.3b","Two Step")
_SECTION_RE = re.compile(
    r"^s(\d+)_(\d+[a-z]?)_(.+)$"  # s<major>_<minor>_<words>
    r"|"
    r"^s(\d+)_([a-z].+)$"  # s<major>_<words>  (transition etc.)
)


def _section_label(section_id: str) -> tuple[str, str]:
    """Return (number_string, title_string) for a section ID."""
    m = _SECTION_RE.match(section_id)
    if not m:
        return ("", section_id.replace("_", " ").title())

    if m.group(1):  # s<major>_<minor>_<words>
        num = f"{m.group(1)}.{m.group(2)}"
        title = m.group(3).replace("_", " ").title()
    else:  # s<major>_<words>
        num = m.group(4)
        title = m.group(5).replace("_", " ").title()

    return (num, title)


# ---------------------------------------------------------------------------
# Beat renderers  (lesson JSON → Notion blocks)
# ---------------------------------------------------------------------------


def _render_dialogue(beat: dict) -> list[dict]:
    text = beat.get("text", "")
    tags = beat.get("tags", [])
    tag_str = f"  [{', '.join(tags)}]" if tags else ""
    return [_callout(f'"{text}"{tag_str}', "💬")]


def _render_scene(beat: dict) -> list[dict]:
    method = beat.get("method", "").lower()
    tid = beat.get("tangible_id", "")
    params = beat.get("params", {})
    description = params.get("description", "").strip() if params else ""

    if method == "update":
        skip = {"description"}
        changed = {k: v for k, v in (params or {}).items() if k not in skip}
        if changed:
            params_str = ", ".join(f"{k}: {v}" for k, v in changed.items())
            fields_part = f" [{params_str}]"
        else:
            fields_part = ""

        if description:
            text = description
        else:
            text = f"Update {tid}{fields_part}" if fields_part else f"Update {tid}"
        return [_callout(text, "🎬")]

    if method == "show":
        action = f"Show {tid}"
    elif method == "hide":
        action = f"Hide {tid}"
    elif method == "remove":
        action = f"Remove {tid}"
    elif method == "lock":
        action = f"Lock {tid}"
    elif method == "unlock":
        action = f"Unlock {tid}"
    elif method == "animate":
        action = f"Animate {tid}"
    elif method == "add":
        action = f"Add {tid}"
    else:
        action = f"{method.upper()} {tid}"

    text = description if description else action
    return [_callout(text, "🎬")]


def _condition_summary(condition: dict) -> str:
    """Build a short readable string from a validator condition dict."""
    if not condition:
        return "fallback"

    if "and" in condition:
        parts = [_condition_summary(sub) for sub in condition["and"]]
        return " AND ".join(parts)

    if "or" in condition:
        parts = [_condition_summary(sub) for sub in condition["or"]]
        return " OR ".join(parts)

    parts = []
    for key, val in condition.items():
        if key == "selected":
            parts.append(f"if selected = {val}")
        elif key == "incorrect_count":
            parts.append(f"attempt {val}")
        elif key == "tangible_id":
            field = condition.get("field", "")
            if field:
                parts.append(f"{val}.{field} = {condition.get('value', '?')}")
            else:
                parts.append(f"tangible_id = {val}")
        elif key == "field":
            pass
        elif key == "value" and "field" in condition:
            pass
        else:
            parts.append(f"{key} = {val}")

    return ", ".join(parts) if parts else "fallback"


def _render_validator(validator: list, section_id: str) -> list[dict]:
    """Render validator states as toggle blocks."""
    blocks: list[dict] = []
    for state in validator:
        description = state.get("description", "?")
        is_correct = state.get("is_correct")
        if is_correct is True:
            indicator = "✅"
        elif is_correct is False:
            indicator = "❌"
        else:
            indicator = "◻️"
        branch_prefix = "🔀 " if state.get("branch") else ""
        toggle_header = f"{indicator} {branch_prefix}{description}"

        child_blocks: list[dict] = []
        prev_was_current_scene = False
        for beat in state.get("beats", []):
            if prev_was_current_scene:
                child_blocks.append(_step_sep_block())
            child_blocks.extend(_render_beat(beat, section_id, nested=True))
            prev_was_current_scene = beat.get("type") == "current_scene"

        if child_blocks:
            blocks.append(_toggle(toggle_header, child_blocks))
        else:
            blocks.append(_paragraph(f"{indicator} {branch_prefix}{description} — student moves forward"))
    return blocks


def _render_prompt(beat: dict, section_id: str) -> list[dict]:
    text = beat.get("text", "")
    tool = beat.get("tool", "")
    target = beat.get("target")
    options = beat.get("options", [])
    validator = beat.get("validator", [])

    blocks: list[dict] = []

    parts = [f"tool: {tool}"]
    if target is not None:
        if isinstance(target, list):
            parts.append("target: " + ", ".join(str(t) for t in target))
        elif isinstance(target, dict):
            parts.append(f"target: {target.get('type', '?')} (all)")
        else:
            parts.append(f"target: {target}")
    if options:
        parts.append("options: " + json.dumps(options))

    callout_lines = ["  ".join(parts), f'"{text}"']
    blocks.append(_callout("\n".join(callout_lines), "❔"))

    if isinstance(validator, list):
        blocks.extend(_render_validator(validator, section_id))

    return blocks


def _render_current_scene(beat: dict, nested: bool = False) -> list[dict]:
    """Render current_scene as a collapsed toggle (reference-only)."""
    parts: list[str] = []
    for element in beat.get("elements", []):
        description = element.get("description", "").strip()
        if not description:
            continue
        tid = element.get("tangible_id", "")
        parts.append(f"{tid}: {description}" if tid else description)

    if not parts:
        return []

    if nested:
        summary = "  |  ".join(parts)
        return [_callout(f"Scene: {summary}", "📋")]

    children = [_bullet(p) for p in parts]
    return [_toggle("📋 Current scene state (for reference, not to be edited)", children)]


def _render_beat(beat: dict, section_id: str, nested: bool = False) -> list[dict]:
    t = beat.get("type", "")
    if t == "dialogue":
        return _render_dialogue(beat)
    elif t == "scene":
        return _render_scene(beat)
    elif t == "current_scene":
        if nested:
            return []
        return _render_current_scene(beat)
    elif t == "prompt":
        return _render_prompt(beat, section_id)
    elif t == "empty":
        return []
    else:
        return [_paragraph(str(beat))]


# ---------------------------------------------------------------------------
# Step separator  (· · ·)
# ---------------------------------------------------------------------------


def _step_sep_block() -> dict:
    return _paragraph("· · ·")


# ---------------------------------------------------------------------------
# Section renderer
# ---------------------------------------------------------------------------


def _render_beat_group(beats: list[dict], section_id: str) -> list[dict]:
    """Render a contiguous group of beats with · · · separators after each current_scene."""
    blocks: list[dict] = []
    for i, beat in enumerate(beats):
        blocks.extend(_render_beat(beat, section_id))
        if beat.get("type") == "current_scene" and i < len(beats) - 1:
            blocks.append(_step_sep_block())
    return blocks


def _render_main_section(section: dict) -> list[dict]:
    """Render a main section as script blocks (divider + H2 + children)."""
    section_id = section["id"]
    num, title = _section_label(section_id)
    header = f"{num}  {title}" if num else title

    return [
        _divider(),
        _heading(2, f"{header}  [{section_id}]"),
        *_render_section_children(section),
    ]


# ---------------------------------------------------------------------------
# Lesson → Notion blocks  (public)
# ---------------------------------------------------------------------------


def lesson_to_blocks(lesson: dict | list, reviewer_user_id: str | None = None) -> list[dict]:
    """
    Convert lesson data to Notion blocks formatted as a readable script.

    Accepts either:
    - A full lesson dict (lesson.json format) with "id", "tangibles", "sections".
    - A bare list of section dicts (lesson_generator.json output format).

    Parameters
    ----------
    lesson : dict | list
        Parsed lesson data.
    reviewer_user_id : str | None
        Notion user ID for the reviewer @mention in the anchor callout.
        Falls back to env var NOTION_REVIEWER_USER_ID if None.
    """
    if reviewer_user_id is None:
        reviewer_user_id = os.getenv("NOTION_REVIEWER_USER_ID")

    if isinstance(lesson, list):
        sections = lesson
        lesson_id = None
        tangibles = {}
    else:
        sections = lesson.get("sections", [])
        lesson_id = lesson.get("id")
        tangibles = lesson.get("tangibles", {})

    blocks: list[dict] = []

    blocks.append(_reviewer_guide_callout(reviewer_user_id))

    if lesson_id:
        blocks.append(_heading(1, lesson_id.replace("_", " ").title()))

    if tangibles:
        tang_blocks = [
            _bullet(f"{tid}: {t.get('type', '?')} — {t.get('title', t.get('input_type', ''))}")
            for tid, t in tangibles.items()
        ]
        blocks.append(_toggle("Tangibles", tang_blocks))

    for section in sections:
        blocks.extend(_render_main_section(section))

    return blocks


# ---------------------------------------------------------------------------
# Pull helpers  (Notion blocks → lesson JSON)
# ---------------------------------------------------------------------------

_HEADING2_ID_RE = re.compile(r"\[([^\]]+)\]\s*$")
_EDITABLE_BEAT_TYPES = {"dialogue", "scene", "prompt"}
_EDITABLE_CALLOUT_EMOJIS = {"💬", "🎬", "❔"}


def _callout_emoji(block: dict) -> str | None:
    """Return the emoji of a callout block, or None if not a callout."""
    if block.get("type") != "callout":
        return None
    icon = block.get("callout", {}).get("icon", {})
    return icon.get("emoji") if icon.get("type") == "emoji" else None


def _collect_toggle_callouts(toggle_block: dict) -> list[tuple[str, str]]:
    """Return (emoji, text) callouts from inside a toggle's children."""
    children = toggle_block.get("toggle", {}).get("children", [])
    results: list[tuple[str, str]] = []
    for block in children:
        if block.get("type") == "callout":
            emoji = _callout_emoji(block) or ""
            text = _extract_rt(block.get("callout", {}).get("rich_text", []))
            results.append((emoji, text))
    return results


def _blocks_to_steps(blocks: list[dict]) -> list[dict]:
    """
    Group a flat list of section content blocks into step groups.

    Step groups are delimited by paragraph blocks containing "· · ·".
    Each group is {"callouts": [(emoji, text), ...], "toggles": [block, ...]}.
    """
    groups: list[dict] = []
    current_callouts: list[tuple[str, str]] = []
    current_toggles: list[dict] = []

    for block in blocks:
        btype = block.get("type")
        if btype == "paragraph":
            text = _extract_rt(block.get("paragraph", {}).get("rich_text", []))
            if text.strip() == "· · ·":
                groups.append({"callouts": list(current_callouts), "toggles": list(current_toggles)})
                current_callouts = []
                current_toggles = []
                continue
        if btype == "callout":
            emoji = _callout_emoji(block) or ""
            text = _extract_rt(block.get("callout", {}).get("rich_text", []))
            current_callouts.append((emoji, text))
        elif btype == "toggle":
            current_toggles.append(block)

    if current_callouts or current_toggles:
        groups.append({"callouts": list(current_callouts), "toggles": list(current_toggles)})

    return groups


def _section_callouts_from_blocks(blocks: list[dict]) -> dict[str, dict]:
    """
    Walk all blocks and build a mapping of section_id → section_data.

    section_data has:
      - "steps": [{"callouts": [(emoji, text), ...], "toggles": [toggle_block, ...]}, ...]
    """
    mapping: dict[str, dict] = {}
    current_section: str | None = None
    current_blocks: list[dict] = []

    def _flush() -> None:
        if current_section is not None:
            mapping[current_section] = {"steps": _blocks_to_steps(current_blocks)}

    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            _flush()
            current_blocks = []
            heading_data = block.get("heading_2", {})
            raw = _extract_rt(heading_data.get("rich_text", []))
            m = _HEADING2_ID_RE.search(raw)
            current_section = m.group(1) if m else None

            if heading_data.get("is_toggleable") and heading_data.get("children"):
                if current_section is not None:
                    mapping[current_section] = {"steps": _blocks_to_steps(heading_data["children"])}
                current_section = None
                current_blocks = []

        elif current_section is not None:
            current_blocks.append(block)

    _flush()
    return mapping


def _strip_dialogue_text(text: str) -> str:
    """Strip surrounding quotes and trailing tag annotation from a dialogue callout text."""
    s = text
    if s.startswith('"'):
        s = s[1:]
    s = re.sub(r'"\s*\[[^\]]*\]\s*$', "", s)
    if s.endswith('"'):
        s = s[:-1]
    return s


def _parse_prompt_fields(text: str) -> dict:
    """Parse a ❔ callout text into prompt field updates (tool, target, options, text)."""
    all_lines = text.split("\n")
    first_line = all_lines[0].strip() if all_lines else ""

    kv: dict = {}
    for pair in re.split(r"  +", first_line):
        if ": " in pair:
            k, v = pair.split(": ", 1)
            kv[k.strip()] = v.strip()

    fields: dict = {}
    if "tool" in kv:
        fields["tool"] = kv["tool"]
    if "target" in kv:
        raw = kv["target"]
        if raw.endswith(" (all)"):
            fields["target"] = {"type": raw[:-6].strip()}
        elif ", " in raw:
            fields["target"] = [t.strip() for t in raw.split(", ")]
        else:
            fields["target"] = raw
    if "options" in kv:
        raw_opts = kv["options"].strip()
        try:
            fields["options"] = json.loads(raw_opts)
        except (json.JSONDecodeError, ValueError):
            parsed_opts = []
            for o in raw_opts.split(", "):
                o = o.strip()
                try:
                    parsed_opts.append(int(o))
                except ValueError:
                    try:
                        parsed_opts.append(float(o))
                    except ValueError:
                        parsed_opts.append(o)
            fields["options"] = parsed_opts

    fields["text"] = all_lines[1].strip().strip('"') if len(all_lines) >= 2 else text.strip('"')
    return fields


_NEW_BEAT_TAG = re.compile(r"\s*\[new beat\]\s*", re.IGNORECASE)


def _scene_rendered_text(beat: dict) -> str:
    """Return the text that _render_scene would display for this beat (description or fallback)."""
    method = beat.get("method", "").lower()
    tid = beat.get("tangible_id", "")
    params = beat.get("params", {})
    description = params.get("description", "").strip() if params else ""
    if description:
        return description
    if method == "update":
        skip = {"description"}
        changed = {k: v for k, v in (params or {}).items() if k not in skip}
        if changed:
            params_str = ", ".join(f"{k}: {v}" for k, v in changed.items())
            return f"Update {tid} [{params_str}]"
        return f"Update {tid}"
    action_map = {
        "show": f"Show {tid}", "hide": f"Hide {tid}", "remove": f"Remove {tid}",
        "lock": f"Lock {tid}", "unlock": f"Unlock {tid}",
        "animate": f"Animate {tid}", "add": f"Add {tid}",
    }
    return action_map.get(method, f"{method.upper()} {tid}")


def _parse_new_beat(emoji: str, text: str) -> dict:
    """Convert a [new beat]-tagged Notion callout into a suggested beat."""
    if emoji == "💬":
        return {"type": "dialogue", "text": _strip_dialogue_text(text), "notion_flag": "suggested"}
    if emoji == "🎬":
        return {
            "type": "scene",
            "method": "PLACEHOLDER",
            "tangible_id": "PLACEHOLDER",
            "params": {"description": text.strip()},
            "notion_flag": "suggested",
        }
    if emoji == "❔":
        beat: dict = {"type": "prompt", "notion_flag": "suggested"}
        beat.update(_parse_prompt_fields(text))
        beat.setdefault("tool", "PLACEHOLDER")
        return beat
    return {"type": "unknown", "text": text, "notion_flag": "suggested"}


def _beats_to_step_groups(beats: list[dict]) -> list[list[dict]]:
    """Split a flat beats list into step groups at each current_scene boundary."""
    groups: list[list[dict]] = []
    current: list[dict] = []
    for beat in beats:
        current.append(beat)
        if beat.get("type") == "current_scene":
            groups.append(current)
            current = []
    if current:
        groups.append(current)
    return groups


def _patch_section_beats(section: dict, section_data: dict) -> None:
    """
    Merge Notion callouts into the beats of *section* (mutates in place).

    Splits both the Notion callouts and JSON beats into step groups (each
    group ends at current_scene / · · · boundary), then matches groups
    positionally. Within each group, editable beats are matched to callouts.
    """
    notion_step_groups = section_data.get("steps", [])
    json_beats = section.get("beats", [])
    json_step_groups = _beats_to_step_groups(json_beats)

    for i, notion_group in enumerate(notion_step_groups):
        notion_callouts = [
            (e, t) for e, t in notion_group["callouts"] if e in _EDITABLE_CALLOUT_EMOJIS
        ]
        toggle_iter = iter(notion_group["toggles"])

        if i < len(json_step_groups):
            group_beats = json_step_groups[i]
            editable_beats = [b for b in group_beats if b.get("type") in _EDITABLE_BEAT_TYPES]
            beat_ptr = 0

            for emoji, text in notion_callouts:
                if _NEW_BEAT_TAG.search(text):
                    clean_text = _NEW_BEAT_TAG.sub("", text).strip()
                    new_beat = _parse_new_beat(emoji, clean_text)
                    if beat_ptr < len(editable_beats):
                        target = editable_beats[beat_ptr]
                        actual_pos = next(
                            idx for idx, b in enumerate(json_beats) if b is target
                        )
                        json_beats.insert(actual_pos, new_beat)
                    else:
                        json_beats.append(new_beat)
                    continue

                if beat_ptr >= len(editable_beats):
                    break

                beat = editable_beats[beat_ptr]
                beat_ptr += 1
                btype = beat.get("type")

                if btype == "dialogue":
                    beat["text"] = _strip_dialogue_text(text)
                elif btype == "scene":
                    new_desc = text.strip()
                    if new_desc != _scene_rendered_text(beat):
                        original_desc = (beat.get("params") or {}).get("description", "").strip()
                        beat.setdefault("params", {})["description"] = new_desc
                        beat["_original_description"] = original_desc
                        beat["notion_flag"] = "updated"
                elif btype == "prompt":
                    original_options = list(beat.get("options") or [])
                    beat.update(_parse_prompt_fields(text))
                    if len(beat.get("options") or []) != len(original_options):
                        beat["options"] = original_options
                        beat["notion_flag"] = "options_parse_failed"
                        beat["_original_options"] = original_options
                        first_line = text.split("\n")[0]
                        m = re.search(r"options:\s*(.+?)(?:  |$)", first_line)
                        beat["_notion_options_text"] = m.group(1).strip() if m else first_line
                    validator = beat.get("validator", [])
                    if isinstance(validator, list):
                        for state in validator:
                            try:
                                toggle_block = next(toggle_iter)
                            except StopIteration:
                                break
                            toggle_callouts = _collect_toggle_callouts(toggle_block)
                            tc_iter = iter(toggle_callouts)
                            for state_beat in state.get("beats", []):
                                if state_beat.get("type") == "dialogue":
                                    try:
                                        t_emoji, t_text = next(tc_iter)
                                    except StopIteration:
                                        break
                                    if t_emoji == "💬":
                                        state_beat["text"] = _strip_dialogue_text(t_text)
        else:
            new_beats = [
                _parse_new_beat(e, _NEW_BEAT_TAG.sub("", t).strip())
                for e, t in notion_callouts
                if e in _EDITABLE_CALLOUT_EMOJIS
            ]
            if new_beats:
                json_beats.extend(new_beats)


def _collect_scene_flags(sections: list) -> list[dict]:
    """Collect flagged beats. Cleans up temp fields set during patching.

    Flag types:
    - "scene_description_updated": 🎬 description was edited in Notion; needs manual config update.
    - "options_parse_failed": ❔ options could not be parsed; re-push to upgrade to JSON format.
    """
    flags = []
    for section in sections:
        sid = section["id"]
        for beat in section.get("beats", []):
            flag = beat.get("notion_flag")
            if beat.get("type") == "scene" and flag == "updated":
                original_desc = beat.pop("_original_description", "")
                flags.append(
                    {
                        "flag_type": "scene_description_updated",
                        "section_id": sid,
                        "tangible_id": beat.get("tangible_id", ""),
                        "method": beat.get("method", ""),
                        "original_description": original_desc,
                        "notion_description": (beat.get("params") or {}).get("description", ""),
                    }
                )
            elif beat.get("type") == "prompt" and flag == "options_parse_failed":
                beat.pop("notion_flag")
                notion_options_text = beat.pop("_notion_options_text", "")
                original_options = beat.pop("_original_options", beat.get("options", []))
                flags.append(
                    {
                        "flag_type": "options_parse_failed",
                        "section_id": sid,
                        "beat_id": beat.get("id", ""),
                        "original_options": original_options,
                        "notion_options_text": notion_options_text,
                        "message": "Options could not be parsed from legacy comma format — re-push to enable editing.",
                    }
                )
    return flags


def blocks_to_lesson(blocks: list[dict], original: dict | list) -> tuple[dict | list, list[dict]]:
    """
    Merge Notion edits into *original* lesson data.

    Returns a tuple of:
    - Deep copy of *original* with Notion edits applied.
    - List of flag dicts for scenes/prompts that need follow-up.
    """
    from steps.formatting.id_stamper import stamp_ids

    patched = copy.deepcopy(original)
    section_map = _section_callouts_from_blocks(blocks)

    if isinstance(patched, list):
        patched = stamp_ids(patched)
        sections = patched
    else:
        patched["sections"] = stamp_ids(patched.get("sections", []))
        sections = patched["sections"]

    for section in sections:
        sid = section["id"]
        if sid in section_map:
            _patch_section_beats(section, section_map[sid])

    flags = _collect_scene_flags(sections)
    return patched, flags


def pull_lesson_from_notion(page_id: str) -> tuple:
    """
    Fetch a lesson page from Notion, patch it with any text edits, and write
    the result back to the source file recorded in config/notion_pages.json.

    Returns (patched, flags, diff).
    """
    file_path = get_file_path_for_page(page_id)
    if file_path is None:
        raise ValueError(
            f"No registry entry found for page {page_id}. "
            "Push the file first so the relationship is recorded."
        )

    original_text = file_path.read_text(encoding="utf-8")
    original = json.loads(original_text)

    client = get_notion_client()
    blocks = _all_blocks(client, page_id, recursive=True)
    patched, flags = blocks_to_lesson(blocks, original)

    patched_text = json.dumps(patched, indent=2, ensure_ascii=False) + "\n"
    file_path.write_text(patched_text, encoding="utf-8")

    flags_path = file_path.parent / "notion_flags.json"
    if flags:
        flags_path.write_text(
            json.dumps(flags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    elif flags_path.exists():
        flags_path.unlink()

    diff_lines = list(
        difflib.unified_diff(
            original_text.splitlines(keepends=True),
            patched_text.splitlines(keepends=True),
            fromfile=f"{file_path.name} (before)",
            tofile=f"{file_path.name} (after)",
        )
    )
    diff = "".join(diff_lines) if diff_lines else "No changes."
    print(diff)

    return patched, flags, diff


# ---------------------------------------------------------------------------
# Convenience wrappers
# ---------------------------------------------------------------------------


def push_lesson(
    data: Any,
    title: str,
    file_path: Path | None = None,
    reviewer_user_id: str | None = None,
    sections: list[str] | None = None,
) -> str:
    """Push lesson data to Notion section by section. Returns the page ID.

    Each section is pushed via push_section (flat heading style):
    - Sections whose _notion_block_id is set are considered in-sync and SKIPPED.
    - Sections without _notion_block_id are pushed (archive old beats, insert new).

    sections: optional allowlist of section IDs to push. Default: all sections
    that lack _notion_block_id (i.e. changed or new sections only).

    Pass file_path=None to skip registry (e.g. for test pushes).
    """
    client = get_notion_client()
    parent_page_id = os.environ["NOTION_PARENT_PAGE_ID"]

    if isinstance(data, list):
        all_sections = data
    else:
        all_sections = data.get("sections", [])

    if sections is not None:
        # Explicit allowlist: push only these section IDs
        target_ids = set(sections)
        target_sections = [s for s in all_sections if s.get("id") in target_ids]
    else:
        # Default: push only sections that are new or changed (no block ID)
        target_sections = [s for s in all_sections if not s.get("_notion_block_id")]

    existing_page_id: str | None = None
    if file_path is not None:
        entry = get_registry_entry(file_path)
        if entry:
            existing_page_id = entry["page_id"]

    if existing_page_id:
        url = get_page_url(existing_page_id)
        print(f"Updating existing page: {url}")
        if not target_sections:
            print("Nothing to push — all sections are in sync.")
            return existing_page_id
        # Ask for confirmation only when running interactively
        try:
            confirm = input(f"Push {len(target_sections)} section(s)? [y/N] ").strip().lower()
            if confirm != "y":
                print("Aborted.")
                raise SystemExit(0)
        except EOFError:
            pass  # non-interactive (pipeline) — proceed
        try:
            if sections is None:
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
                existing_page_id = None
            else:
                raise

    if not existing_page_id:
        # First push: create page with anchor callout, then sections
        intro_blocks: list[dict] = [_reviewer_guide_callout(reviewer_user_id)]
        for section in target_sections:
            intro_blocks.extend(_render_main_section(section))
        page = client.pages.create(
            parent={"page_id": parent_page_id},
            properties={"title": {"title": [{"text": {"content": title}}]}},
            children=intro_blocks[:100],
        )
        page_id = page["id"]
        for i in range(100, len(intro_blocks), 100):
            client.blocks.children.append(page_id, children=intro_blocks[i : i + 100])
        if file_path is not None:
            set_registry_entry(file_path, page_id, title)
        return page_id

    # Existing page: push each target section individually
    page_blocks = _all_blocks(client, page_id)

    # Archive stale sections from the page.
    # Full push: archive everything not in current data.
    # Surgical push: only archive sections at the same sort position as the
    # target sections (i.e. old versions of the sections being pushed).
    current_ids = {s.get("id") for s in all_sections if isinstance(s, dict)}
    if sections is not None:
        target_sort_keys = {_section_sort_key(sid) for sid in sections}
    for i, block in enumerate(page_blocks):
        if block.get("type") != "heading_2":
            continue
        rt = _extract_rt(block.get("heading_2", {}).get("rich_text", []))
        m = re.search(r"\[([^\]]+)\]\s*$", rt)
        if not m:
            continue
        sid = m.group(1)
        if sid in current_ids:
            continue
        if sections is not None and _section_sort_key(sid) not in target_sort_keys:
            continue
        # Archive this stale H2 and its sibling beats
        stale_beats = []
        for b in page_blocks[i + 1 :]:
            if b.get("type") in ("heading_2", "divider"):
                break
            stale_beats.append(b)
        for b in stale_beats:
            client.blocks.update(b["id"], archived=True)
        if block.get("has_children"):
            for child in _all_blocks(client, block["id"]):
                client.blocks.update(child["id"], archived=True)
        client.blocks.update(block["id"], archived=True)
        print(f"  [ARCHIVE] stale section {sid}")
    page_blocks = _all_blocks(client, page_id)

    for section in target_sections:
        sid = section.get("id", "?")
        print(f"  [PUSH] {sid}")
        push_section(client, page_id, section, page_blocks=page_blocks)
        # Refresh page blocks after each section so insert positions are current
        page_blocks = _all_blocks(client, page_id)

    if file_path is not None:
        set_registry_entry(file_path, page_id, title)

    return page_id


def pull_lesson(
    page_id: str,
    original: dict | list,
) -> tuple[dict | list, list[dict], list[dict]]:
    """Pull lesson edits from Notion. Returns (patched, flags, raw_blocks).

    raw_blocks is the full fetched block tree, returned so callers can save
    it as a debug artifact if needed.
    """
    client = get_notion_client()
    blocks = _all_blocks(client, page_id, recursive=True)
    patched, flags = blocks_to_lesson(blocks, original)
    return patched, flags, blocks
