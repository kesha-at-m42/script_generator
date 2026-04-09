"""
Tests for the Notion pull (blocks_to_lesson) round-trip.

Covers the edit features in lesson_notion_format._patch_section_beats and helpers.
Each test builds a minimal lesson, renders it to Notion blocks, optionally mutates
the blocks to simulate a reviewer edit, then pulls back and asserts the result.
"""

import copy
import json
import pytest

from utils.notion import (
    blocks_to_lesson,
    lesson_to_blocks,
    _strip_dialogue_text,
    _parse_prompt_fields,
    _scene_rendered_text,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_section(section_id: str, beats: list[dict]) -> dict:
    return {"id": section_id, "beats": beats}


def _make_lesson(sections: list[dict]) -> list[dict]:
    return sections


def _push_pull(lesson: list[dict], mutate_blocks=None) -> tuple[list[dict], list[dict]]:
    """Render lesson → blocks, optionally mutate blocks, pull back."""
    blocks = lesson_to_blocks(lesson)
    if mutate_blocks:
        mutate_blocks(blocks)
    patched, flags = blocks_to_lesson(blocks, lesson)
    return patched, flags


def _find_section(patched: list[dict], section_id: str) -> dict:
    return next(s for s in patched if s["id"] == section_id)


def _find_beat(section: dict, beat_type: str, index: int = 0) -> dict:
    matches = [b for b in section["beats"] if b.get("type") == beat_type]
    return matches[index]


def _callout_blocks(blocks: list[dict], section_id: str) -> list[dict]:
    """Return callout blocks that follow the heading_2 for section_id (flat layout)."""
    collecting = False
    result = []
    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            rt = block["heading_2"]["rich_text"][0]["text"]["content"]
            if f"[{section_id}]" in rt:
                collecting = True
                continue
            elif collecting:
                break
        if collecting and btype == "callout":
            result.append(block)
    return result


def _section_blocks(blocks: list[dict], section_id: str) -> list[dict]:
    """Return all blocks that follow the heading_2 for section_id (flat layout)."""
    collecting = False
    result = []
    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            rt = block["heading_2"]["rich_text"][0]["text"]["content"]
            if f"[{section_id}]" in rt:
                collecting = True
                continue
            elif collecting:
                break
        if collecting:
            result.append(block)
    return result


def _set_callout_text(callout: dict, new_text: str) -> None:
    callout["callout"]["rich_text"][0]["text"]["content"] = new_text
    callout["callout"]["rich_text"][0]["plain_text"] = new_text


# ---------------------------------------------------------------------------
# 1. No-op round-trip — untouched page produces identical output
# ---------------------------------------------------------------------------


def test_roundtrip_no_changes():
    """Pull on an untouched page is a no-op (modulo ID stamping)."""
    lesson = _make_lesson([
        _make_section("s1_1_intro", [
            {"type": "dialogue", "text": "Hello world."},
            {"type": "scene", "method": "show", "tangible_id": "pg_fruits"},
        ])
    ])
    patched, flags = _push_pull(lesson)
    assert flags == []
    sec = _find_section(patched, "s1_1_intro")
    assert _find_beat(sec, "dialogue")["text"] == "Hello world."


# ---------------------------------------------------------------------------
# 2. Dialogue text edit
# ---------------------------------------------------------------------------


def test_dialogue_edit():
    lesson = _make_lesson([
        _make_section("s1_1_intro", [
            {"type": "dialogue", "text": "Original line."},
        ])
    ])

    def mutate(blocks):
        callouts = _callout_blocks(blocks, "s1_1_intro")
        dialogue = next(c for c in callouts if c["callout"]["icon"]["emoji"] == "💬")
        _set_callout_text(dialogue, '"Edited line."')

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s1_1_intro")
    assert _find_beat(sec, "dialogue")["text"] == "Edited line."
    assert flags == []


# ---------------------------------------------------------------------------
# 3. Prompt text edit
# ---------------------------------------------------------------------------


def test_prompt_text_edit():
    lesson = _make_lesson([
        _make_section("s1_2_q", [
            {"type": "prompt", "tool": "click", "target": "pg_fruits",
             "text": "Which fruit got the most votes?", "validator": []},
        ])
    ])

    def mutate(blocks):
        callouts = _callout_blocks(blocks, "s1_2_q")
        prompt = next(c for c in callouts if c["callout"]["icon"]["emoji"] == "❔")
        original = prompt["callout"]["rich_text"][0]["text"]["content"]
        new_text = original.replace("Which fruit got the most votes?", "Which fruit has the highest count?")
        _set_callout_text(prompt, new_text)

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s1_2_q")
    beat = _find_beat(sec, "prompt")
    assert beat["text"] == "Which fruit has the highest count?"
    assert flags == []


# ---------------------------------------------------------------------------
# 4. Scene description edit
# ---------------------------------------------------------------------------


def test_scene_description_edit():
    lesson = _make_lesson([
        _make_section("s1_3_scene", [
            {"type": "scene", "method": "show", "tangible_id": "pg_fruits",
             "params": {"description": "Show the fruit chart."}},
        ])
    ])

    def mutate(blocks):
        callouts = _callout_blocks(blocks, "s1_3_scene")
        scene = next(c for c in callouts if c["callout"]["icon"]["emoji"] == "🎬")
        _set_callout_text(scene, "Show the fruit chart with labels.")

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s1_3_scene")
    beat = _find_beat(sec, "scene")
    assert beat["params"]["description"] == "Show the fruit chart with labels."
    assert beat["notion_flag"] == "updated"
    assert len(flags) == 1
    assert flags[0]["flag_type"] == "scene_description_updated"
    assert flags[0]["original_description"] == "Show the fruit chart."
    assert flags[0]["notion_description"] == "Show the fruit chart with labels."


# ---------------------------------------------------------------------------
# 5. Scene with no description — fallback text not treated as an edit  (bug fix)
# ---------------------------------------------------------------------------


def test_scene_no_description_no_false_positive():
    """A scene beat with no description renders a fallback; pull must not flag it."""
    lesson = _make_lesson([
        _make_section("s1_4_scene", [
            {"type": "scene", "method": "remove", "tangible_id": "equation_builder_rows"},
        ])
    ])
    patched, flags = _push_pull(lesson)
    sec = _find_section(patched, "s1_4_scene")
    beat = _find_beat(sec, "scene")
    assert "notion_flag" not in beat
    assert flags == []


# ---------------------------------------------------------------------------
# 6. New beat insertion
# ---------------------------------------------------------------------------


def test_new_beat_insertion():
    lesson = _make_lesson([
        _make_section("s1_5_insert", [
            {"type": "dialogue", "text": "First line."},
            {"type": "dialogue", "text": "Second line."},
        ])
    ])

    def mutate(blocks):
        heading_idx = None
        for i, block in enumerate(blocks):
            if block.get("type") == "heading_2":
                rt = block["heading_2"]["rich_text"][0]["text"]["content"]
                if "[s1_5_insert]" in rt:
                    heading_idx = i
            elif heading_idx is not None:
                if block.get("type") == "callout" and block["callout"]["icon"]["emoji"] == "💬":
                    new_callout = copy.deepcopy(block)
                    _set_callout_text(new_callout, '"[new beat] Inserted line."')
                    blocks.insert(i, new_callout)
                    return
                elif block.get("type") == "heading_2":
                    return

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s1_5_insert")
    dialogue_beats = [b for b in sec["beats"] if b.get("type") == "dialogue"]
    assert len(dialogue_beats) == 3
    assert dialogue_beats[0]["notion_flag"] == "suggested"
    assert dialogue_beats[0]["text"] == "Inserted line."


# ---------------------------------------------------------------------------
# 7. Validator state dialogue edit
# ---------------------------------------------------------------------------


def test_validator_dialogue_edit():
    lesson = _make_lesson([
        _make_section("s2_1_validator", [
            {
                "type": "prompt",
                "tool": "click",
                "target": "pg_fruits",
                "text": "Which got the most votes?",
                "validator": [
                    {
                        "description": "Correct answer",
                        "is_correct": True,
                        "beats": [{"type": "dialogue", "text": "That's right!"}],
                    }
                ],
            }
        ])
    ])

    def mutate(blocks):
        collecting = False
        for block in blocks:
            if block.get("type") == "heading_2":
                rt = block["heading_2"]["rich_text"][0]["text"]["content"]
                if "[s2_1_validator]" in rt:
                    collecting = True
                    continue
                elif collecting:
                    return
            if collecting and block.get("type") == "toggle":
                for tc in block.get("toggle", {}).get("children", []):
                    if tc.get("type") == "callout" and tc["callout"]["icon"]["emoji"] == "💬":
                        _set_callout_text(tc, '"That\'s correct! Great job."')
                        return

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s2_1_validator")
    prompt = _find_beat(sec, "prompt")
    state_beat = prompt["validator"][0]["beats"][0]
    assert state_beat["text"] == "That's correct! Great job."
    assert flags == []


# ---------------------------------------------------------------------------
# 8. Extra step group — new beats appended
# ---------------------------------------------------------------------------


def test_extra_step_group_appended():
    """Callouts in a Notion step group beyond the JSON groups become suggested beats."""
    lesson = _make_lesson([
        _make_section("s3_1_extra", [
            {"type": "scene", "method": "show", "tangible_id": "pg_a"},
            {"type": "current_scene", "elements": []},
            {"type": "dialogue", "text": "Step 2 dialogue."},
        ])
    ])

    def mutate(blocks):
        heading_found = False
        insert_at = len(blocks)
        for i, block in enumerate(blocks):
            if block.get("type") == "heading_2":
                rt = block["heading_2"]["rich_text"][0]["text"]["content"]
                if "[s3_1_extra]" in rt:
                    heading_found = True
                elif heading_found:
                    insert_at = i
                    break
        if heading_found:
            blocks.insert(insert_at, {
                "object": "block", "type": "paragraph",
                "paragraph": {"rich_text": [{"text": {"content": "· · ·"}}]},
            })
            blocks.insert(insert_at + 1, {
                "object": "block", "type": "callout",
                "callout": {
                    "rich_text": [{"text": {"content": '"Extra step."'}}],
                    "icon": {"type": "emoji", "emoji": "💬"},
                },
            })

    patched, flags = _push_pull(lesson, mutate)
    sec = _find_section(patched, "s3_1_extra")
    suggested = [b for b in sec["beats"] if b.get("notion_flag") == "suggested"]
    assert len(suggested) == 1
    assert suggested[0]["text"] == "Extra step."


# ---------------------------------------------------------------------------
# 9. Options round-trip — JSON format  (bug fix)
# ---------------------------------------------------------------------------


def test_options_json_roundtrip():
    """Options containing commas must survive a push/pull cycle."""
    lesson = _make_lesson([
        _make_section("s1_6_opts", [
            {
                "type": "prompt",
                "tool": "multiple_choice",
                "options": ["Same dots, just organized differently", "The numbers are close together"],
                "text": "Why are they equal?",
                "validator": [],
            }
        ])
    ])
    patched, flags = _push_pull(lesson)
    sec = _find_section(patched, "s1_6_opts")
    beat = _find_beat(sec, "prompt")
    assert beat["options"] == ["Same dots, just organized differently", "The numbers are close together"]
    assert flags == []


# ---------------------------------------------------------------------------
# 10. Section isolation — edits in one section don't bleed into another
# ---------------------------------------------------------------------------


def test_section_isolation():
    lesson = _make_lesson([
        _make_section("s1_1_a", [{"type": "dialogue", "text": "Section A."}]),
        _make_section("s1_2_b", [{"type": "dialogue", "text": "Section B."}]),
    ])

    def mutate(blocks):
        callouts = _callout_blocks(blocks, "s1_1_a")
        dialogue = next(c for c in callouts if c["callout"]["icon"]["emoji"] == "💬")
        _set_callout_text(dialogue, '"Section A edited."')

    patched, flags = _push_pull(lesson, mutate)
    sec_a = _find_section(patched, "s1_1_a")
    sec_b = _find_section(patched, "s1_2_b")
    assert _find_beat(sec_a, "dialogue")["text"] == "Section A edited."
    assert _find_beat(sec_b, "dialogue")["text"] == "Section B."
