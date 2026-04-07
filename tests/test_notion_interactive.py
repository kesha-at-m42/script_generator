"""
Interactive Notion push/pull walkthrough.

Creates ONE sandbox page and walks through each user journey in sequence.
Pauses at each step so you can inspect and edit in Notion before continuing.

Run with:
    pytest tests/test_notion_interactive.py -v -s --keep-sandbox

Journeys:
  1. First push     — inspect structure: sections, beats, separators, toggles
  2. Surgical push  — change one section; verify only that section updates, comments survive
  3. Structural push — add a beat to one section; verify full refresh on that section only
  4. New section    — add a section between existing ones; verify sorted insertion
  5. Pull edits     — edit dialogue/scene/prompt in Notion; pull and verify diff
  6. New beat       — insert [new beat] callout in Notion; pull and verify suggested beat
"""

import pytest
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.insert(0, ".")

from utils import notion_sync
from utils.lesson_notion_format import lesson_to_blocks, blocks_to_lesson
from utils.notion_sync import (
    _all_blocks, _extract_rt, get_notion_client, get_page_url, push_to_notion,
)
from steps.formatting.id_stamper import stamp_ids

notion_configured = pytest.mark.skipif(
    not notion_sync.is_configured(),
    reason="NOTION_API_KEY / NOTION_PARENT_PAGE_ID not set",
)

# ---------------------------------------------------------------------------
# Lesson fixture — realistic multi-section, multi-step, multi-beat
# ---------------------------------------------------------------------------

LESSON_V1 = [
    {
        "id": "s1_1_worked_example",
        "beats": [
            {"type": "scene", "method": "show", "tangible_id": "array_3x4",
             "params": {"description": "3×4 dot array appears on screen."}},
            {"type": "dialogue", "text": "Here's a 3 by 4 array. Count the rows first."},
            {"type": "dialogue", "text": "3 rows of 4 dots. We write that as 3 times 4."},
            {"type": "current_scene", "elements": [
                {"tangible_id": "array_3x4", "description": "3×4 dot array visible."}
            ]},
            {"type": "scene", "method": "animate", "tangible_id": "array_3x4",
             "params": {"description": "Array rotates 90 degrees to show 4×3."}},
            {"type": "dialogue", "text": "Now it's 4 rows of 3. We write that as 4 times 3."},
            {"type": "dialogue", "text": "Same dots. Different order. Same total."},
        ],
    },
    {
        "id": "s1_2_student_tries",
        "beats": [
            {"type": "scene", "method": "show", "tangible_id": "array_blank",
             "params": {"description": "Blank array grid appears."}},
            {"type": "current_scene", "elements": [
                {"tangible_id": "array_blank", "description": "Empty grid shown."}
            ]},
            {
                "type": "prompt",
                "tool": "click_region",
                "target": "array_blank",
                "text": "Click to show the array by rows.",
                "options": [],
                "validator": [
                    {
                        "description": "Clicked rows correctly",
                        "is_correct": True,
                        "beats": [
                            {"type": "dialogue", "text": "Exactly. 3 rows of 4."},
                        ],
                    },
                    {
                        "description": "First wrong attempt",
                        "is_correct": False,
                        "beats": [
                            {"type": "dialogue", "text": "Look at the horizontal lines. Those are rows."},
                        ],
                    },
                ],
            },
        ],
    },
    {
        "id": "s1_3_consolidation",
        "beats": [
            {"type": "scene", "method": "show", "tangible_id": "equation_display",
             "params": {"description": "Equation 3×4 = 4×3 displayed."}},
            {"type": "dialogue", "text": "You just proved the turn-around rule."},
            {"type": "current_scene", "elements": [
                {"tangible_id": "equation_display", "description": "Equation visible."}
            ]},
            {
                "type": "prompt",
                "tool": "multiple_choice",
                "target": None,
                "text": "What does the turn-around rule tell us?",
                "options": [
                    "Switching the order of factors keeps the product the same",
                    "Adding numbers in any order gives the same sum",
                    "Multiplying always gives a bigger number",
                    "Arrays must always be square",
                ],
                "validator": [
                    {
                        "description": "Correct",
                        "is_correct": True,
                        "beats": [
                            {"type": "dialogue", "text": "That's it. Order doesn't change the product."},
                        ],
                    },
                    {
                        "description": "Wrong — picked addition rule",
                        "is_correct": False,
                        "beats": [
                            {"type": "dialogue", "text": "That's the rule for addition. Think about multiplication."},
                        ],
                    },
                ],
            },
        ],
    },
]


def _deep_copy_lesson(lesson):
    import copy
    return copy.deepcopy(lesson)


def _callouts_for_section(blocks, section_id):
    for block in blocks:
        if block.get("type") == "heading_2":
            rt = _extract_rt(block["heading_2"]["rich_text"])
            if f"[{section_id}]" in rt:
                return [
                    c for c in block["heading_2"].get("children", [])
                    if c.get("type") == "callout"
                ]
    return []


def _beat_text(callouts, emoji):
    c = next((c for c in callouts if c["callout"]["icon"]["emoji"] == emoji), None)
    return _extract_rt(c["callout"]["rich_text"]) if c else None


def _hr(title):
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print('─' * 60)


def _step(msg):
    print(f"\n  👉 {msg}")


def _check(msg):
    print(f"  ✓  {msg}")


def _wait(request, prompt):
    if request.config.getoption("--pause"):
        input(f"\n  ⏸  {prompt}\n     Press Enter when ready... ")
    else:
        print(f"\n  [pause skipped] {prompt}")


# ---------------------------------------------------------------------------
# Single test — all journeys in sequence on one page
# ---------------------------------------------------------------------------


@notion_configured
def test_interactive_walkthrough(sandbox_page, request):
    client = get_notion_client()
    url = get_page_url(sandbox_page)

    # -----------------------------------------------------------------------
    # JOURNEY 1: First push — inspect structure
    # -----------------------------------------------------------------------
    _hr("JOURNEY 1 — First push: inspect structure")

    lesson = _deep_copy_lesson(LESSON_V1)
    push_to_notion(data=lesson, title="[TEST] Interactive Walkthrough",
                   existing_page_id=sandbox_page, blocks_fn=lesson_to_blocks)

    _step(f"Page pushed → {url}")
    _step("Open the page and verify:")
    print("       • 3 sections: 1.1 Worked Example, 1.2 Student Tries, 1.3 Consolidation")
    print("       • Each section is a toggle heading — expand them")
    print("       • 1.1 has a · · · separator between the two steps")
    print("       • 1.2 has a 🎬 scene, then · · ·, then ❔ prompt with 2 validator toggles inside")
    print("       • 1.3 has 🎬 scene, 2× 💬 dialogue, · · ·, then ❔ prompt with 2 toggles")
    print("       • Dividers (---) sit BETWEEN sections, not at the end of the page")

    _wait(request, "Inspect the page structure, then continue")

    blocks_j1 = _all_blocks(client, sandbox_page, recursive=True)
    s1_callouts = _callouts_for_section(blocks_j1, "s1_1_worked_example")
    s2_callouts = _callouts_for_section(blocks_j1, "s1_2_student_tries")
    s3_callouts = _callouts_for_section(blocks_j1, "s1_3_consolidation")
    assert any(c["callout"]["icon"]["emoji"] == "🎬" for c in s1_callouts), "s1_1 missing 🎬"
    assert any(c["callout"]["icon"]["emoji"] == "💬" for c in s1_callouts), "s1_1 missing 💬"
    assert any(c["callout"]["icon"]["emoji"] == "❔" for c in s2_callouts), "s1_2 missing ❔"
    assert any(c["callout"]["icon"]["emoji"] == "❔" for c in s3_callouts), "s1_3 missing ❔"
    _check("Journey 1 passed — structure is correct")

    # Capture block IDs of unchanged sections for later comparison
    s1_first_dialogue = next(
        c for c in s1_callouts if c["callout"]["icon"]["emoji"] == "💬"
    )
    s3_first_callout = s3_callouts[0]
    s1_dialogue_id_before = s1_first_dialogue["id"]
    s3_callout_id_before = s3_first_callout["id"]

    # Add a comment to s1_1's first dialogue before re-push
    client.comments.create(
        parent={"block_id": s1_dialogue_id_before},
        rich_text=[{"text": {"content": "Reviewer: love this line, keep it."}}],
    )
    _step("Comment added to s1_1's first dialogue beat.")
    _wait(request, "Open s1_1 in Notion and verify the comment is visible on the first 💬 beat")

    # -----------------------------------------------------------------------
    # JOURNEY 2: Surgical re-push — change s1_2 only
    # -----------------------------------------------------------------------
    _hr("JOURNEY 2 — Surgical re-push: change s1_2 only")

    lesson_v2 = _deep_copy_lesson(LESSON_V1)
    lesson_v2[1]["beats"][2]["text"] = "Click to highlight the rows in the array."  # changed
    # s1_1 and s1_3 unchanged

    _step("Pushing v2: only the prompt text in s1_2 changed.")
    push_to_notion(data=lesson_v2, title="[TEST] Interactive Walkthrough",
                   existing_page_id=sandbox_page, blocks_fn=lesson_to_blocks)

    _step("After re-push, verify:")
    print("       • s1_2 prompt text reads: 'Click to highlight the rows in the array.'")
    print("       • s1_1 and s1_3 content is identical to v1")
    print("       • The comment on s1_1's dialogue is still there")
    _wait(request, "Inspect: s1_2 updated, comment on s1_1 survived")

    blocks_j2 = _all_blocks(client, sandbox_page, recursive=True)
    s2_callouts_j2 = _callouts_for_section(blocks_j2, "s1_2_student_tries")
    prompt_j2 = next(c for c in s2_callouts_j2 if c["callout"]["icon"]["emoji"] == "❔")
    prompt_text_j2 = _extract_rt(prompt_j2["callout"]["rich_text"])
    assert "Click to highlight the rows" in prompt_text_j2

    # Block IDs of unchanged sections must be the same (in-place update)
    s1_callouts_j2 = _callouts_for_section(blocks_j2, "s1_1_worked_example")
    s3_callouts_j2 = _callouts_for_section(blocks_j2, "s1_3_consolidation")
    s1_dialogue_id_after = next(
        c for c in s1_callouts_j2 if c["callout"]["icon"]["emoji"] == "💬"
    )["id"]
    s3_callout_id_after = s3_callouts_j2[0]["id"]
    assert s1_dialogue_id_after == s1_dialogue_id_before, "s1_1 block recreated — surgical update failed"
    assert s3_callout_id_after == s3_callout_id_before, "s1_3 block recreated — surgical update failed"

    comments = client.comments.list(block_id=s1_dialogue_id_after).get("results", [])
    comment_texts = ["".join(s["text"]["content"] for s in c["rich_text"]) for c in comments]
    assert any("Reviewer" in t for t in comment_texts), "Comment lost after surgical re-push"
    _check("Journey 2 passed — surgical update correct, comment survived")

    # -----------------------------------------------------------------------
    # JOURNEY 3: Structural re-push — add a beat to s1_1
    # -----------------------------------------------------------------------
    _hr("JOURNEY 3 — Structural re-push: beat added to s1_1")

    lesson_v3 = _deep_copy_lesson(LESSON_V1)
    lesson_v3[0]["beats"].insert(2, {
        "type": "dialogue",
        "text": "Notice how the shape of the array doesn't change — just the way we read it.",
    })

    _step("Pushing v3: one extra dialogue beat inserted into s1_1.")
    _step("After re-push, verify:")
    print("       • s1_1 now has 3 consecutive 💬 dialogue beats in step 1")
    print("       • s1_2 and s1_3 are unchanged")

    push_to_notion(data=lesson_v3, title="[TEST] Interactive Walkthrough",
                   existing_page_id=sandbox_page, blocks_fn=lesson_to_blocks)

    _wait(request, "Inspect: s1_1 has extra beat, others unchanged")

    blocks_j3 = _all_blocks(client, sandbox_page, recursive=True)
    s1_callouts_j3 = _callouts_for_section(blocks_j3, "s1_1_worked_example")
    dialogues_j3 = [c for c in s1_callouts_j3 if c["callout"]["icon"]["emoji"] == "💬"]
    assert len(dialogues_j3) == 5, f"Expected 5 💬 in s1_1 after inserting 1 (was 4), got {len(dialogues_j3)}"
    _check("Journey 3 passed — extra beat present in s1_1")

    # -----------------------------------------------------------------------
    # JOURNEY 4: New section inserted in sorted order
    # -----------------------------------------------------------------------
    _hr("JOURNEY 4 — New section: inserted between s1_2 and s1_3")

    lesson_v4 = _deep_copy_lesson(LESSON_V1)
    lesson_v4.insert(2, {
        "id": "s1_2b_extra_practice",
        "beats": [
            {"type": "dialogue", "text": "Let's try one more example before moving on."},
            {"type": "scene", "method": "show", "tangible_id": "array_2x6",
             "params": {"description": "2×6 array appears."}},
        ],
    })

    _step("Pushing v4: new section s1_2b inserted between s1_2 and s1_3.")
    _step("After re-push, verify:")
    print("       • Section order is: 1.1, 1.2, 1.2b Extra Practice, 1.3")
    print("       • New section sits between s1_2 and s1_3 — NOT at the bottom")

    push_to_notion(data=lesson_v4, title="[TEST] Interactive Walkthrough",
                   existing_page_id=sandbox_page, blocks_fn=lesson_to_blocks)

    _wait(request, "Inspect: s1_2b appears between s1_2 and s1_3")

    blocks_j4 = _all_blocks(client, sandbox_page, recursive=True)
    h2s = [b for b in blocks_j4 if b.get("type") == "heading_2"]
    section_ids = [
        _extract_rt(b["heading_2"]["rich_text"]).split("[")[-1].rstrip("]")
        for b in h2s if "[" in _extract_rt(b["heading_2"]["rich_text"])
    ]
    idx_s12  = section_ids.index("s1_2_student_tries")
    idx_s12b = section_ids.index("s1_2b_extra_practice")
    idx_s13  = section_ids.index("s1_3_consolidation")
    assert idx_s12 < idx_s12b < idx_s13, f"Section order wrong: {section_ids}"
    _check("Journey 4 passed — new section inserted in sorted order")

    # -----------------------------------------------------------------------
    # JOURNEY 5: Pull after Notion edits — dialogue, scene, prompt
    # -----------------------------------------------------------------------
    _hr("JOURNEY 5 — Pull after Notion edits")

    _step("Now make edits directly in Notion:")
    print(f"       Page: {url}")
    print()
    print("       1. In s1_1 (Worked Example), edit the FIRST 💬 dialogue:")
    print("          Change: 'Here's a 3 by 4 array. Count the rows first.'")
    print("          To:     'Here's a 3 by 4 array. How many rows do you see?'")
    print()
    print("       2. In s1_1, edit the 🎬 scene description (first one):")
    print("          Add ' [edited]' to the end of its text")
    print()
    print("       3. In s1_3 (Consolidation), edit the ❔ prompt question text:")
    print("          Change: 'What does the turn-around rule tell us?'")
    print("          To:     'What does the commutative property tell us?'")

    _wait(request, "Make the 3 edits above in Notion, then press Enter to pull")

    blocks_j5 = _all_blocks(client, sandbox_page, recursive=True)
    original_for_pull = _deep_copy_lesson(LESSON_V1)
    patched, flags = blocks_to_lesson(blocks_j5, original_for_pull)

    sec_s11 = next(s for s in patched if s["id"] == "s1_1_worked_example")
    sec_s13 = next(s for s in patched if s["id"] == "s1_3_consolidation")

    print("\n  Pull result:")
    first_dialogue = next(b for b in sec_s11["beats"] if b["type"] == "dialogue")
    print(f"    s1_1 dialogue: {first_dialogue['text']!r}")

    prompt_s13 = next(b for b in sec_s13["beats"] if b["type"] == "prompt")
    print(f"    s1_3 prompt:   {prompt_s13['text']!r}")

    if flags:
        print(f"\n  Flags ({len(flags)}):")
        for f in flags:
            if f["flag_type"] == "scene_description_updated":
                print(f"    🎬 [{f['section_id']}] {f['method']} {f['tangible_id']}")
                print(f"       was: {f['original_description']!r}")
                print(f"       now: {f['notion_description']!r}")

    _wait(request, "Check the pull results above look correct")

    # -----------------------------------------------------------------------
    # JOURNEY 6: Pull [new beat] insertion
    # -----------------------------------------------------------------------
    _hr("JOURNEY 6 — Pull [new beat] insertion")

    _step("In Notion, add a new 💬 callout to s1_3 (Consolidation):")
    print(f"       Page: {url}")
    print()
    print("       1. Open the s1_3 Consolidation section")
    print("       2. Before the existing 💬 'You just proved the turn-around rule.'")
    print("          add a new callout block with emoji 💬 and text:")
    print('          "[new beat] Let\'s take a moment to reflect."')
    print("       (In Notion: type /callout, pick 💬, paste that text)")

    _wait(request, "Add the [new beat] callout in Notion, then press Enter to pull")

    blocks_j6 = _all_blocks(client, sandbox_page, recursive=True)
    original_for_j6 = _deep_copy_lesson(LESSON_V1)
    patched_j6, flags_j6 = blocks_to_lesson(blocks_j6, original_for_j6)

    sec_s13_j6 = next(s for s in patched_j6 if s["id"] == "s1_3_consolidation")
    suggested = [b for b in sec_s13_j6["beats"] if b.get("notion_flag") == "suggested"]

    print(f"\n  Suggested beats found: {len(suggested)}")
    for b in suggested:
        print(f"    type={b['type']!r}  text={b.get('text','')!r}")

    assert len(suggested) >= 1, "No suggested beats found — check the [new beat] tag was included"
    _check("Journey 6 passed — suggested beat inserted correctly")

    print(f"\n{'═' * 60}")
    print("  All 6 journeys complete.")
    print(f"  Sandbox page: {url}")
    print('═' * 60)
