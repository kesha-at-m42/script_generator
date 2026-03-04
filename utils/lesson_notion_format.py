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


def _quote(text: str) -> dict:
    return {
        "object": "block",
        "type": "quote",
        "quote": {"rich_text": _rt(text)},
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

    icons = {
        "show": "🎬",
        "hide": "🙈",
        "update": "✏️",
        "animate": "🎞️",
        "add": "➕",
        "remove": "🗑️",
        "lock": "🔒",
        "unlock": "🔓",
    }
    icon = icons.get(method, "🎬")

    if method == "show":
        text = f"Show {tid}"
    elif method == "hide":
        text = f"Hide {tid}"
    elif method == "update":
        cats = params.get("highlight_categories", [])
        if cats:
            cats_str = ", ".join(str(c) for c in cats)
            text = f"Highlight {cats_str} on {tid}"
        else:
            # Fallback: render any params
            parts = [f"{k}: {v}" for k, v in params.items()]
            text = f"Update {tid}" + (f"  ({', '.join(parts)})" if parts else "")
    elif method == "animate":
        text = params.get("description", f"Animate {tid}")
    elif method == "add":
        base = (
            f"Add {params.get('tangible_type', tid)} as {tid}"
            if "tangible_type" in params
            else f"Add {tid}"
        )
        extra_params = {k: v for k, v in params.items() if k != "tangible_type"}
        if extra_params:
            parts = [f"{k}: {v}" for k, v in extra_params.items()]
            base += f"  ({', '.join(parts)})"
        text = base
    elif method == "remove":
        text = f"Remove {tid}"
    elif method == "lock":
        text = f"Lock {tid}  (override)"
    elif method == "unlock":
        text = f"Unlock {tid}  (override)"
    else:
        text = f"{method.upper()}  {tid}"

    return [_callout(text, icon)]


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
            # May pair with "field"
            field = condition.get("field", "")
            if field:
                parts.append(f"{val}.{field} = {condition.get('value', '?')}")
            else:
                parts.append(f"tangible_id = {val}")
        elif key == "field":
            # Already handled above with tangible_id
            pass
        elif key == "value" and "field" in condition:
            # Already handled above
            pass
        else:
            parts.append(f"{key} = {val}")

    return ", ".join(parts) if parts else "fallback"


def _render_validator(validator: list, section_id: str) -> list[dict]:
    """Render validator states as toggle blocks (flat array schema)."""
    blocks: list[dict] = []
    for state in validator:
        description = state.get("description", "?")
        condition = state.get("condition", {})
        cond_summary = _condition_summary(condition)
        toggle_header = f"{description}  [{cond_summary}]"

        # Render child beats for each step inside this state
        child_blocks: list[dict] = []
        for i, step in enumerate(state.get("steps", [])):
            if i > 0:
                child_blocks.append(_step_sep_block())
            for beat in step:
                child_blocks.extend(_render_beat(beat, section_id))

        blocks.append(_toggle(toggle_header, child_blocks))
    return blocks


def _render_prompt(beat: dict, section_id: str) -> list[dict]:
    text = beat.get("text", "")
    tool = beat.get("tool", {})
    validator = beat.get("validator", [])

    blocks: list[dict] = []

    # First line of callout: tool name + tangible_id if present (workspace tool)
    tool_name = tool.get("name", "") if isinstance(tool, dict) else str(tool)
    tangible_id = tool.get("tangible_id", "") if isinstance(tool, dict) else ""
    if tangible_id:
        first_line = f"{tool_name}  on  {tangible_id}"
    else:
        first_line = tool_name

    blocks.append(_callout(f'{first_line}\n"{text}"', "❓"))

    # Options from tool (overlay tools like multiple_choice, multi_select)
    options = tool.get("options", []) if isinstance(tool, dict) else []
    if options:
        blocks.append(_bullet("Options: " + "  |  ".join(str(o) for o in options)))

    # Config if present
    config = tool.get("config", {}) if isinstance(tool, dict) else {}
    if config:
        config_parts = [f"{k}: {v}" for k, v in config.items()]
        blocks.append(_bullet("config: " + ", ".join(config_parts)))

    # Validator states as toggles (flat array)
    if isinstance(validator, list):
        blocks.extend(_render_validator(validator, section_id))

    return blocks


def _render_beat(beat: dict, section_id: str) -> list[dict]:
    t = beat.get("type", "")
    if t == "dialogue":
        return _render_dialogue(beat)
    if t == "scene":
        return _render_scene(beat)
    if t == "prompt":
        return _render_prompt(beat, section_id)
    # fallback
    return [_paragraph(str(beat))]


# ---------------------------------------------------------------------------
# Step separator  (· · ·)
# ---------------------------------------------------------------------------

_STEP_SEP = _paragraph("· · ·")


# ---------------------------------------------------------------------------
# Section renderer
# ---------------------------------------------------------------------------


def _step_sep_block() -> dict:
    return _paragraph("· · ·")


def _render_main_section(section: dict) -> list[dict]:
    """Render a main section as script blocks with per-step workspace callouts."""
    section_id = section["id"]
    num, title = _section_label(section_id)
    header = f"{num}  {title}" if num else title

    blocks: list[dict] = []

    # Section header — [section_id] at end enables reliable pull parsing
    blocks.append(_divider())
    blocks.append(_heading(2, f"{header}  [{section_id}]"))

    # Track visible workspace, starting from section's declared workspace
    visible: set[str] = set(section.get("workspace", []))

    # Steps (just visual grouping, no "Step N" label)
    steps = section.get("steps", [])
    for i, step in enumerate(steps):
        if i > 0:
            blocks.append(_step_sep_block())
        for beat in step:
            blocks.extend(_render_beat(beat, section_id))
            # Update visible set based on scene beats
            if beat.get("type") == "scene":
                method = beat.get("method", "")
                tid = beat.get("tangible_id", "")
                if method in ("show", "add") and tid:
                    visible.add(tid)
                elif method in ("hide", "remove") and tid:
                    visible.discard(tid)
        # After each step, emit workspace state callout
        blocks.append(_callout(", ".join(sorted(visible)), "📋"))

    return blocks


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def lesson_to_blocks(lesson: dict) -> list[dict]:
    """
    Convert a lesson dict to Notion blocks formatted as a readable script.

    Parameters
    ----------
    lesson : dict
        Parsed lesson.json content.

    Returns
    -------
    list[dict]
        Notion block objects ready for blocks.children.append.
    """
    sections: list[dict] = lesson.get("sections", [])

    blocks: list[dict] = []

    # Lesson title
    lesson_id = lesson.get("id", "lesson")
    blocks.append(_heading(1, lesson_id.replace("_", " ").title()))

    # Tangibles summary as a collapsed toggle
    tangibles = lesson.get("tangibles", {})
    if tangibles:
        tang_blocks = [
            _bullet(f"{tid}: {t.get('type', '?')} — {t.get('title', t.get('input_type', ''))}")
            for tid, t in tangibles.items()
        ]
        blocks.append(_toggle("Tangibles", tang_blocks))

    # All sections are main sections — no remediation separation
    for section in sections:
        blocks.extend(_render_main_section(section))

    return blocks


# ---------------------------------------------------------------------------
# Pull helpers
# ---------------------------------------------------------------------------

_HEADING2_ID_RE = re.compile(r"\[([^\]]+)\]\s*$")


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


def _section_callouts_from_blocks(
    blocks: list[dict],
) -> dict[str, dict]:
    """
    Walk all blocks and build a mapping of section_id → section_data.

    section_data has:
      - "callouts": [(emoji, text), ...]  — callouts directly in the section
      - "toggles": [toggle_block, ...]    — validator state toggles (in order)
    """
    mapping: dict[str, dict] = {}
    current_section: str | None = None
    current_callouts: list[tuple[str, str]] = []
    current_toggles: list[dict] = []

    def _flush():
        if current_section is not None:
            mapping[current_section] = {
                "callouts": list(current_callouts),
                "toggles": list(current_toggles),
            }

    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            _flush()
            current_callouts = []
            current_toggles = []
            raw = _extract_rt_text(block.get("heading_2", {}).get("rich_text", []))
            m = _HEADING2_ID_RE.search(raw)
            current_section = m.group(1) if m else None
        elif btype == "callout" and current_section is not None:
            emoji = _callout_emoji(block) or ""
            text = _extract_rt_text(block.get("callout", {}).get("rich_text", []))
            current_callouts.append((emoji, text))
        elif btype == "toggle" and current_section is not None:
            current_toggles.append(block)

    _flush()
    return mapping


def _patch_section_beats(
    section: dict,
    section_data: dict,
) -> None:
    """
    Overlay callout texts onto the beats of *section* (mutates in place).

    Positional matching: DialogueBeat → next 💬 callout, PromptBeat → next ❓.
    SceneBeats are skipped (display-only, not editable).
    Workspace (📋) and scene-icon callouts are also skipped.

    For prompt beats, also patches dialogue beats inside validator state toggles.

    Limitation: adding/removing callout blocks in Notion breaks alignment.
    """
    callouts = section_data.get("callouts", [])
    toggles = section_data.get("toggles", [])

    # Only editable callouts: 💬 dialogue and ❓ prompt
    _EDITABLE_EMOJIS = {"💬", "❓"}
    filtered_callouts = [(e, t) for e, t in callouts if e in _EDITABLE_EMOJIS]
    callouts = filtered_callouts

    callout_iter = iter(callouts)
    toggle_iter = iter(toggles)

    for step in section.get("steps", []):
        for beat in step:
            btype = beat.get("type")
            if btype == "dialogue":
                try:
                    emoji, text = next(callout_iter)
                except StopIteration:
                    return
                if emoji == "💬":
                    # Format pushed: "text content"  [tag1, tag2]
                    # Strip leading quote, remove trailing "  [tags]" annotation, strip closing quote
                    s = text
                    if s.startswith('"'):
                        s = s[1:]
                    s = re.sub(r'"\s*\[[^\]]*\]\s*$', "", s)
                    if s.endswith('"'):
                        s = s[:-1]
                    beat["text"] = s
            elif btype == "prompt":
                try:
                    emoji, text = next(callout_iter)
                except StopIteration:
                    return
                if emoji == "❓":
                    # First line: "{tool_name}  on  {tangible_id}" or just "{tool_name}"
                    # Second line: the prompt text
                    lines = text.split("\n", 1)
                    if len(lines) >= 2:
                        # Parse tool from first line
                        first_line = lines[0].strip()
                        if "  on  " in first_line:
                            parts = first_line.split("  on  ", 1)
                            beat["tool"] = {
                                "name": parts[0].strip(),
                                "tangible_id": parts[1].strip(),
                            }
                        else:
                            existing_tool = beat.get("tool", {})
                            if isinstance(existing_tool, dict):
                                beat["tool"] = dict(existing_tool, name=first_line.strip())
                            else:
                                beat["tool"] = {"name": first_line.strip()}
                        # Prompt text
                        beat["text"] = lines[1].strip().strip('"')
                    else:
                        beat["text"] = text.strip('"')

                    # Recover options from next bullet block if present (handled by caller via callout_iter)
                    # The options are in the tool object, not patched from Notion (display-only)

                    # Patch validator state beats from corresponding toggles
                    validator = beat.get("validator", [])
                    if isinstance(validator, list):
                        for state in validator:
                            try:
                                toggle_block = next(toggle_iter)
                            except StopIteration:
                                break
                            # Walk toggle children for 💬 callouts, patch dialogue beats positionally
                            toggle_callouts = _collect_toggle_callouts(toggle_block)
                            tc_iter = iter(toggle_callouts)
                            for state_step in state.get("steps", []):
                                for state_beat in state_step:
                                    if state_beat.get("type") == "dialogue":
                                        try:
                                            t_emoji, t_text = next(tc_iter)
                                        except StopIteration:
                                            break
                                        if t_emoji == "💬":
                                            s = t_text
                                            if s.startswith('"'):
                                                s = s[1:]
                                            s = re.sub(r'"\s*\[[^\]]*\]\s*$', "", s)
                                            if s.endswith('"'):
                                                s = s[:-1]
                                            state_beat["text"] = s
            # scene beats are display-only — skip


def blocks_to_lesson(blocks: list[dict], original: dict) -> dict:
    """
    Patch *original* lesson dict with text edits found in Notion *blocks*.

    Returns a deep copy of *original* with dialogue/prompt text overlaid
    from the corresponding callout blocks.  All other fields are unchanged.

    Parameters
    ----------
    blocks : list[dict]
        Flat list of Notion blocks fetched from the lesson page
        (as returned by notion_sync._all_blocks).
    original : dict
        Parsed lesson.json content — used as the structural template.

    Returns
    -------
    dict
        Deep-copied lesson dict with text edits applied.
    """
    patched = copy.deepcopy(original)
    section_map = _section_callouts_from_blocks(blocks)

    for section in patched.get("sections", []):
        sid = section["id"]
        if sid in section_map:
            _patch_section_beats(section, section_map[sid])

    return patched


# ---------------------------------------------------------------------------
# Public pull helper
# ---------------------------------------------------------------------------


def pull_lesson_from_notion(page_id: str) -> dict:
    """
    Fetch a lesson page from Notion, patch it with any text edits, and write
    the result back to the source file recorded in config/notion_pages.json.

    Parameters
    ----------
    page_id : str
        Notion page ID (from the registry or push return value).

    Returns
    -------
    dict
        Deep-copied lesson dict with text edits applied.

    Raises
    ------
    ValueError
        If page_id is not found in the registry.
    """
    import json

    from utils.notion_sync import _all_blocks, get_file_path_for_page, get_notion_client

    file_path = get_file_path_for_page(page_id)
    if file_path is None:
        raise ValueError(
            f"No registry entry found for page {page_id}. "
            "Push the file first so the relationship is recorded."
        )

    original = json.loads(file_path.read_text(encoding="utf-8"))

    client = get_notion_client()
    blocks = _all_blocks(client, page_id)
    patched = blocks_to_lesson(blocks, original)

    file_path.write_text(json.dumps(patched, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return patched
