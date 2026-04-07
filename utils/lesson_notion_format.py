"""lesson_notion_format.py

Converts a lesson.json structure into human-readable Notion blocks,
formatted as a script rather than a raw JSON dump.

Layout per main section
-----------------------
  ─────────────────────────────────────
  1.1  Most Votes
  ─────────────────────────────────────

  🎬 Show pg_fruits
  🎬 Show data_table
  💬 "You made a graph with your Minis' votes..."

  · · ·

  ❓ click_category  on  pg_fruits
     "Which fruit got the most votes? Click it."

  [toggle] Student selected Apples  [if selected = Apples]
    💬 "Apples got 6 votes — the most of any fruit."

  [toggle] First wrong attempt  [attempt 1]
    💬 "Look at the numbers next to each row. Which one is biggest?"

  · · ·

  💬 "Apples got 6 votes — more than any other fruit."

  📋 data_table, pg_fruits
"""

from __future__ import annotations

import copy
import difflib
import json
import os
import re

# ---------------------------------------------------------------------------
# Notion block primitives
# ---------------------------------------------------------------------------

_RT_LIMIT = 1900


def _rt(text: str) -> list[dict]:
    return [{"text": {"content": str(text)[:_RT_LIMIT]}}]


def _rt_rich(spans: list[dict]) -> list[dict]:
    """Pass through a pre-built rich_text list (truncating each span)."""
    return [
        {"text": {"content": s["text"]["content"][:_RT_LIMIT]}}
        for s in spans
        if s.get("text", {}).get("content")
    ]


def _heading(level: int, text: str) -> dict:
    t = f"heading_{level}"
    return {"object": "block", "type": t, t: {"rich_text": _rt(text)}}


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
        "paragraph": {"rich_text": _rt(text)},
    }


def _bullet(text: str) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": _rt(text)},
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
# Beat renderers
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
        branch_condition = state.get("branch_condition")
        branch_prefix = f"🔀 {branch_condition} — " if branch_condition else ""
        toggle_header = f"{indicator} {branch_prefix}{description}"

        child_blocks: list[dict] = []
        prev_was_current_scene = False
        for beat in state.get("beats", []):
            if prev_was_current_scene:
                child_blocks.append(_step_sep_block())
            child_blocks.extend(_render_beat(beat, section_id, nested=True))
            prev_was_current_scene = beat.get("type") == "current_scene"

        blocks.append(_toggle(toggle_header, child_blocks))
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
        blocks = _render_dialogue(beat)
    elif t == "scene":
        blocks = _render_scene(beat)
    elif t == "current_scene":
        if nested:
            return []
        blocks = _render_current_scene(beat)
    elif t == "prompt":
        blocks = _render_prompt(beat, section_id)
    else:
        blocks = [_paragraph(str(beat))]

    branch_condition = beat.get("branch_condition")
    if branch_condition and blocks and blocks[0].get("type") == "callout":
        prefix = f"🔀 {branch_condition} — "
        prefix_span = {"text": {"content": prefix}, "annotations": {"bold": True}}
        existing_rt = blocks[0]["callout"].get("rich_text", [])
        blocks[0]["callout"]["rich_text"] = [prefix_span] + existing_rt

    return blocks


# ---------------------------------------------------------------------------
# Step separator  (· · ·)
# ---------------------------------------------------------------------------


def _step_sep_block() -> dict:
    return _paragraph("· · ·")


# ---------------------------------------------------------------------------
# Section renderer
# ---------------------------------------------------------------------------


def _render_main_section(section: dict) -> list[dict]:
    """Render a main section as script blocks with step separators derived from current_scene beats."""
    section_id = section["id"]
    num, title = _section_label(section_id)
    header = f"{num}  {title}" if num else title

    beats = section.get("beats", [])
    content: list[dict] = []

    for i, beat in enumerate(beats):
        content.extend(_render_beat(beat, section_id))
        # Insert · · · after current_scene if more beats follow
        if beat.get("type") == "current_scene" and i < len(beats) - 1:
            content.append(_step_sep_block())

    return [
        _divider(),
        _toggle_heading(2, f"{header}  [{section_id}]", content),
    ]


# ---------------------------------------------------------------------------
# Public entry point
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

    Returns
    -------
    list[dict]
        Notion block objects ready for blocks.children.append.
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

    # Always-first anchor block for reviewer guidance and after= insertion
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
# Pull helpers
# ---------------------------------------------------------------------------

_HEADING2_ID_RE = re.compile(r"\[([^\]]+)\]\s*$")
_EDITABLE_BEAT_TYPES = {"dialogue", "scene", "prompt"}
_EDITABLE_CALLOUT_EMOJIS = {"💬", "🎬", "❔"}


def _extract_rt_text(rich_text: list[dict]) -> str:
    return "".join(span.get("text", {}).get("content", "") for span in rich_text)


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
            text = _extract_rt_text(block.get("callout", {}).get("rich_text", []))
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
            text = _extract_rt_text(block.get("paragraph", {}).get("rich_text", []))
            if text.strip() == "· · ·":
                groups.append({"callouts": list(current_callouts), "toggles": list(current_toggles)})
                current_callouts = []
                current_toggles = []
                continue
        if btype == "callout":
            emoji = _callout_emoji(block) or ""
            text = _extract_rt_text(block.get("callout", {}).get("rich_text", []))
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
            raw = _extract_rt_text(heading_data.get("rich_text", []))
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
            # New format: JSON array e.g. ["Same dots, just organized differently", ...]
            fields["options"] = json.loads(raw_opts)
        except (json.JSONDecodeError, ValueError):
            # Legacy format: comma-separated plain values (may be ambiguous for string options)
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
                    # Insert before the current editable beat using identity lookup
                    if beat_ptr < len(editable_beats):
                        target = editable_beats[beat_ptr]
                        actual_pos = next(
                            idx for idx, b in enumerate(json_beats) if b is target
                        )
                        json_beats.insert(actual_pos, new_beat)
                        # editable_beats references are still valid; target shifted by 1
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
                    # If option count changed, the parse split on commas inside option text —
                    # restore the original options rather than corrupt the beat.
                    if len(beat.get("options") or []) != len(original_options):
                        beat["options"] = original_options
                        beat["notion_flag"] = "options_parse_failed"
                        beat["_original_options"] = original_options
                        # Extract raw options string from the first line of the callout text
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
            # Extra Notion step group beyond JSON groups → new suggested step group
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
    - "options_parse_failed": ❔ options could not be parsed (legacy comma format with commas in
      option text); re-push the page to upgrade to JSON format and make options editable.
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
    - List of scene flag dicts where a 🎬 description was edited in Notion.
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


# ---------------------------------------------------------------------------
# Public pull helper
# ---------------------------------------------------------------------------


def pull_lesson_from_notion(page_id: str) -> dict:
    """
    Fetch a lesson page from Notion, patch it with any text edits, and write
    the result back to the source file recorded in config/notion_pages.json.
    """
    from utils.notion_sync import _all_blocks, get_file_path_for_page, get_notion_client

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
