"""
Live Notion push tests — require NOTION_API_KEY and NOTION_PARENT_PAGE_ID.

Each test creates a fresh sandbox child page, runs assertions against the
real Notion API, then archives the page on teardown.

Run with:
    pytest tests/test_notion_push_live.py -v -s

Keep pages open after the run (so you can inspect them in Notion):
    pytest tests/test_notion_push_live.py -v -s --keep-sandbox
"""

import os
import pytest

from dotenv import load_dotenv
load_dotenv()

from utils import notion_sync
from utils.lesson_notion_format import lesson_to_blocks, blocks_to_lesson
from utils.notion_sync import (
    _all_blocks,
    _extract_rt,
    get_notion_client,
    get_page_url,
    push_to_notion,
)

notion_configured = pytest.mark.skipif(
    not notion_sync.is_configured(),
    reason="NOTION_API_KEY / NOTION_PARENT_PAGE_ID not set",
)


def _pause(request, message=""):
    if request.config.getoption("--pause"):
        input(f"\n  ⏸  {message} — press Enter to continue... ")




def _make_lesson(sections):
    return sections


def _section(sid, beats):
    return {"id": sid, "beats": beats}


def _callouts_for_section(blocks, section_id):
    """Return callout children of the heading_2 block for section_id."""
    for block in blocks:
        if block.get("type") == "heading_2":
            rt = _extract_rt(block["heading_2"]["rich_text"])
            if f"[{section_id}]" in rt:
                return [
                    c for c in block["heading_2"].get("children", [])
                    if c.get("type") == "callout"
                ]
    return []


def _paragraphs_for_section(blocks, section_id):
    """Return paragraph children of the heading_2 block for section_id."""
    for block in blocks:
        if block.get("type") == "heading_2":
            rt = _extract_rt(block["heading_2"]["rich_text"])
            if f"[{section_id}]" in rt:
                return [
                    c for c in block["heading_2"].get("children", [])
                    if c.get("type") == "paragraph"
                ]
    return []


# ---------------------------------------------------------------------------
# 1. Push creates page with correct top-level structure
# ---------------------------------------------------------------------------


@notion_configured
def test_push_creates_reviewer_guide_and_sections(sandbox_page):
    lesson = _make_lesson([
        _section("s1_1_intro", [
            {"type": "dialogue", "text": "Hello world."},
        ]),
        _section("s1_2_next", [
            {"type": "dialogue", "text": "Second section."},
        ]),
    ])
    push_to_notion(
        data=lesson, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    client = get_notion_client()
    blocks = _all_blocks(client, sandbox_page, recursive=True)

    # First block is 💡 reviewer guide callout
    assert blocks[0]["type"] == "callout"
    assert blocks[0]["callout"]["icon"]["emoji"] == "💡"

    # Both sections present as heading_2 blocks
    h2_texts = [
        _extract_rt(b["heading_2"]["rich_text"])
        for b in blocks if b.get("type") == "heading_2"
    ]
    assert any("[s1_1_intro]" in t for t in h2_texts)
    assert any("[s1_2_next]" in t for t in h2_texts)


# ---------------------------------------------------------------------------
# 2. Callout emojis match beat types in order
# ---------------------------------------------------------------------------


@notion_configured
def test_push_callout_emojis_in_order(sandbox_page):
    lesson = _make_lesson([
        _section("s1_1_mixed", [
            {"type": "scene", "method": "show", "tangible_id": "pg_fruits"},
            {"type": "dialogue", "text": "Look at this."},
            {"type": "prompt", "tool": "click", "target": "pg_fruits",
             "text": "Click the biggest.", "validator": []},
        ])
    ])
    push_to_notion(
        data=lesson, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    client = get_notion_client()
    blocks = _all_blocks(client, sandbox_page, recursive=True)

    callouts = _callouts_for_section(blocks, "s1_1_mixed")
    emojis = [c["callout"]["icon"]["emoji"] for c in callouts]
    assert emojis == ["🎬", "💬", "❔"]


# ---------------------------------------------------------------------------
# 3. Step separator · · · appears after current_scene
# ---------------------------------------------------------------------------


@notion_configured
def test_push_step_separator_after_current_scene(sandbox_page):
    lesson = _make_lesson([
        _section("s1_1_steps", [
            {"type": "dialogue", "text": "Step 1."},
            {"type": "current_scene", "elements": [
                {"tangible_id": "pg_a", "description": "Chart is shown."}
            ]},
            {"type": "dialogue", "text": "Step 2."},
        ])
    ])
    push_to_notion(
        data=lesson, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    client = get_notion_client()
    blocks = _all_blocks(client, sandbox_page, recursive=True)

    paragraphs = _paragraphs_for_section(blocks, "s1_1_steps")
    sep_texts = [_extract_rt(p["paragraph"]["rich_text"]) for p in paragraphs]
    assert "· · ·" in sep_texts


# ---------------------------------------------------------------------------
# 4. Re-push updates changed dialogue text in place
# ---------------------------------------------------------------------------


@notion_configured
def test_repush_updates_dialogue_text(sandbox_page, request):
    lesson_v1 = _make_lesson([
        _section("s1_1_update", [
            {"type": "dialogue", "text": "Original text."},
        ])
    ])
    lesson_v2 = _make_lesson([
        _section("s1_1_update", [
            {"type": "dialogue", "text": "Updated text."},
        ])
    ])
    client = get_notion_client()

    push_to_notion(
        data=lesson_v1, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    _pause(request, "v1 pushed — inspect the page, optionally add a Notion comment or edit another beat")

    push_to_notion(
        data=lesson_v2, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    _pause(request, "v2 pushed — check that only the dialogue text changed")

    blocks = _all_blocks(client, sandbox_page, recursive=True)
    callouts = _callouts_for_section(blocks, "s1_1_update")
    dialogue = next(c for c in callouts if c["callout"]["icon"]["emoji"] == "💬")
    text = _extract_rt(dialogue["callout"]["rich_text"])
    assert "Updated text." in text


# ---------------------------------------------------------------------------
# 5. New section inserted in sorted order on re-push
# ---------------------------------------------------------------------------


@notion_configured
def test_repush_new_section_sorted(sandbox_page, request):
    lesson_v1 = _make_lesson([
        _section("s1_1_first", [{"type": "dialogue", "text": "First."}]),
        _section("s1_3_third", [{"type": "dialogue", "text": "Third."}]),
    ])
    lesson_v2 = _make_lesson([
        _section("s1_1_first", [{"type": "dialogue", "text": "First."}]),
        _section("s1_2_second", [{"type": "dialogue", "text": "Second."}]),
        _section("s1_3_third", [{"type": "dialogue", "text": "Third."}]),
    ])
    client = get_notion_client()

    push_to_notion(
        data=lesson_v1, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    _pause(request, "v1 pushed (s1_1, s1_3 only) — check the page before s1_2 is inserted")

    push_to_notion(
        data=lesson_v2, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    _pause(request, "v2 pushed — verify s1_2 appears between s1_1 and s1_3")

    blocks = _all_blocks(client, sandbox_page, recursive=True)
    h2_order = [
        _extract_rt(b["heading_2"]["rich_text"])
        for b in blocks if b.get("type") == "heading_2"
    ]
    ids_in_order = [t.split("[")[-1].rstrip("]") for t in h2_order if "[" in t]
    assert ids_in_order == ["s1_1_first", "s1_2_second", "s1_3_third"]


# ---------------------------------------------------------------------------
# 6. Surgical re-push — multiple sections, only changed section updated,
#    unchanged block IDs preserved, comments on unchanged beats survive
# ---------------------------------------------------------------------------


@notion_configured
def test_surgical_repush_multi_section(sandbox_page, request):
    """Re-push with one section changed out of three.

    Verifies:
    - Changed dialogue text is updated.
    - Unchanged sections keep the same Notion block IDs (in-place update, not recreate).
    - A comment added to an unchanged beat before re-push is still present after.
    """
    lesson_v1 = _make_lesson([
        _section("s1_1_unchanged", [{"type": "dialogue", "text": "Section 1 — unchanged."}]),
        _section("s1_2_changed",   [{"type": "dialogue", "text": "Section 2 — original."}]),
        _section("s1_3_unchanged", [{"type": "dialogue", "text": "Section 3 — unchanged."}]),
    ])
    lesson_v2 = _make_lesson([
        _section("s1_1_unchanged", [{"type": "dialogue", "text": "Section 1 — unchanged."}]),
        _section("s1_2_changed",   [{"type": "dialogue", "text": "Section 2 — updated."}]),
        _section("s1_3_unchanged", [{"type": "dialogue", "text": "Section 3 — unchanged."}]),
    ])
    client = get_notion_client()

    push_to_notion(
        data=lesson_v1, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )

    # Collect block IDs of the unchanged sections' callouts before re-push
    blocks_v1 = _all_blocks(client, sandbox_page, recursive=True)
    s1_callouts_v1 = _callouts_for_section(blocks_v1, "s1_1_unchanged")
    s3_callouts_v1 = _callouts_for_section(blocks_v1, "s1_3_unchanged")
    s1_dialogue_id = next(c["id"] for c in s1_callouts_v1 if c["callout"]["icon"]["emoji"] == "💬")
    s3_dialogue_id = next(c["id"] for c in s3_callouts_v1 if c["callout"]["icon"]["emoji"] == "💬")

    # Add a comment to s1_1's dialogue beat
    client.comments.create(
        parent={"block_id": s1_dialogue_id},
        rich_text=[{"text": {"content": "Test comment — should survive re-push."}}],
    )

    _pause(request, "v1 pushed + comment added to s1_1 — open the page, check the comment is visible")

    push_to_notion(
        data=lesson_v2, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )

    _pause(request, "v2 pushed — check s1_2 updated, s1_1 comment still there")

    blocks_v2 = _all_blocks(client, sandbox_page, recursive=True)

    # s1_2 dialogue text updated
    s2_callouts_v2 = _callouts_for_section(blocks_v2, "s1_2_changed")
    s2_text = _extract_rt(
        next(c for c in s2_callouts_v2 if c["callout"]["icon"]["emoji"] == "💬")["callout"]["rich_text"]
    )
    assert "Section 2 — updated." in s2_text

    # Unchanged sections kept the same block IDs
    s1_callouts_v2 = _callouts_for_section(blocks_v2, "s1_1_unchanged")
    s3_callouts_v2 = _callouts_for_section(blocks_v2, "s1_3_unchanged")
    s1_dialogue_id_v2 = next(c["id"] for c in s1_callouts_v2 if c["callout"]["icon"]["emoji"] == "💬")
    s3_dialogue_id_v2 = next(c["id"] for c in s3_callouts_v2 if c["callout"]["icon"]["emoji"] == "💬")
    assert s1_dialogue_id_v2 == s1_dialogue_id, "s1_1 block ID changed — beat was recreated, not updated in place"
    assert s3_dialogue_id_v2 == s3_dialogue_id, "s1_3 block ID changed — beat was recreated, not updated in place"

    # Comment on s1_1's dialogue beat survived
    comments = client.comments.list(block_id=s1_dialogue_id_v2).get("results", [])
    comment_texts = [
        "".join(span["text"]["content"] for span in c["rich_text"])
        for c in comments
    ]
    assert any("Test comment" in t for t in comment_texts), "Comment was lost after re-push"


# ---------------------------------------------------------------------------
# 7. Push → pull round-trip on a live page
# ---------------------------------------------------------------------------


@notion_configured
def test_push_pull_roundtrip_live(sandbox_page, request):
    lesson = _make_lesson([
        _section("s1_1_rt", [
            {"type": "scene", "method": "show", "tangible_id": "pg_a",
             "params": {"description": "Show the chart."}},
            {"type": "dialogue", "text": "Here it is."},
            {"type": "prompt", "tool": "click", "target": "pg_a",
             "text": "Click it.", "options": ["Yes", "No"], "validator": []},
        ])
    ])
    client = get_notion_client()

    push_to_notion(
        data=lesson, title="[TEST]", existing_page_id=sandbox_page,
        blocks_fn=lesson_to_blocks,
    )
    _pause(request, "pushed — edit any 💬 or 🎬 callout in Notion, then press Enter to pull")

    blocks = _all_blocks(client, sandbox_page, recursive=True)
    patched, flags = blocks_to_lesson(blocks, lesson)

    assert flags == []
    from steps.formatting.id_stamper import stamp_ids
    stamped = stamp_ids(lesson)
    sec = next(s for s in patched if s["id"] == "s1_1_rt")
    src_sec = next(s for s in stamped if s["id"] == "s1_1_rt")

    dialogue = next(b for b in sec["beats"] if b["type"] == "dialogue")
    assert dialogue["text"] == "Here it is."

    prompt = next(b for b in sec["beats"] if b["type"] == "prompt")
    assert prompt["text"] == "Click it."
    assert prompt["options"] == ["Yes", "No"]
