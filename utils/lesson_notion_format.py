"""lesson_notion_format.py

Converts a lesson.json structure into human-readable Notion blocks,
formatted as a script rather than a raw JSON dump.

Layout per main section
-----------------------
  ─────────────────────────────────────
  1.1  Most Votes
  ─────────────────────────────────────

  🎬 SHOW  pg_fruits
  🎬 SHOW  data_table
  💬 "You made a graph with your Minis' votes..."

  · · ·

  ❓ PROMPT  click_category
     "Which fruit got the most votes? Click it."
     ✓  correct → (continue)
     ↩  attempt 1 → s1_1_light
     ↩  attempt 2 → s1_1_medium
     ↩  fallback  → s1_1_heavy

  · · ·

  💬 "Apples got 6 votes — more than any other fruit."

Remediation child sections are collapsed into toggles at the bottom
of their parent section so they don't interrupt the main flow.
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
# s1_1_light       →  None  (remediation — handled as toggle)
_SECTION_RE = re.compile(
    r"^s(\d+)_(\d+[a-z]?)_(.+)$"  # s<major>_<minor>_<words>
    r"|"
    r"^s(\d+)_([a-z].+)$"  # s<major>_<words>  (transition etc.)
)
_REMED_SUFFIXES = ("_light", "_medium", "_heavy")


def _is_remediation(section_id: str) -> bool:
    return any(section_id.endswith(s) for s in _REMED_SUFFIXES)


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
    method = beat.get("method", "").upper()
    tid = beat.get("tangible_id", "")
    params = beat.get("params", {})

    icons = {
        "SHOW": "🎬",
        "HIDE": "🙈",
        "UPDATE": "✏️",
        "ANIMATE": "🎞️",
        "ADD": "➕",
    }
    icon = icons.get(method, "🎬")

    if params:
        parts = []
        for k, v in params.items():
            if isinstance(v, list):
                parts.append(f"{k}: {', '.join(str(x) for x in v)}")
            elif isinstance(v, dict):
                parts.append(
                    ", ".join(f"{kk}: {vv}" for kk, vv in v.items() if kk != "description")
                )
            else:
                parts.append(f"{k}: {v}")
        param_str = "  |  " + "  |  ".join(parts)
    else:
        param_str = ""

    # Callout so the method emoji shows as the block icon, not buried in text
    return [_callout(f"{method}  {tid}{param_str}", icon)]


def _render_validator(validator: dict, section_id: str) -> list[dict]:
    """Render validator states as indented bullets."""
    blocks: list[dict] = []
    for state in validator.get("states", []):
        name = state.get("name", "?")
        child = state.get("child_section")
        cond = state.get("condition", {})

        if name == "correct":
            icon = "✓"
            target = "(continue)"
        else:
            icon = "↩"
            target = child if child else "(continue)"

        # Condition summary
        if "operator" in cond:
            right = cond.get("right", {}).get("value", "?")
            cond_str = f"→ {target}  [if answer = {right}]" if name == "correct" else f"→ {target}"
        elif "evaluate" in cond:
            desc = cond.get("description", cond.get("evaluate", ""))
            cond_str = f"→ {target}  [{desc}]"
        else:
            cond_str = f"→ {target}  [fallback]"

        blocks.append(_bullet(f"{icon}  {name.replace('_', ' ')}  {cond_str}"))
    return blocks


def _render_prompt(beat: dict, section_id: str) -> list[dict]:
    text = beat.get("text", "")
    tool = beat.get("tool", "")
    options = beat.get("options", [])
    validator = beat.get("validator", {})

    blocks: list[dict] = []
    # tool name on first line, prompt text on second — icon is the callout marker
    blocks.append(_callout(f'{tool}\n"{text}"', "❓"))
    # Options if present
    if options:
        blocks.append(_bullet("Options: " + "  |  ".join(str(o) for o in options)))
    # Validator states
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


def _render_remediation_section(section: dict) -> list[dict]:
    """Render a remediation section compactly (for use inside a toggle)."""
    blocks: list[dict] = []
    steps = section.get("steps", [])
    for i, step in enumerate(steps):
        if i > 0:
            blocks.append(_step_sep_block())
        for beat in step:
            blocks.extend(_render_beat(beat, section["id"]))
    return blocks


def _step_sep_block() -> dict:
    return _paragraph("· · ·")


def _render_main_section(
    section: dict,
    remediation_map: dict[str, list[dict]],
) -> list[dict]:
    """Render a main section as script blocks, with remediation as toggles."""
    section_id = section["id"]
    num, title = _section_label(section_id)
    header = f"{num}  {title}" if num else title

    blocks: list[dict] = []

    # Section header — [section_id] at end enables reliable pull parsing
    blocks.append(_divider())
    blocks.append(_heading(2, f"{header}  [{section_id}]"))

    # Workspace hint
    workspace = section.get("workspace", [])
    if workspace:
        blocks.append(_callout(", ".join(workspace), "📋"))

    # Steps (just visual grouping, no "Step N" label)
    steps = section.get("steps", [])
    for i, step in enumerate(steps):
        if i > 0:
            blocks.append(_step_sep_block())
        for beat in step:
            blocks.extend(_render_beat(beat, section_id))

    # Remediation toggles
    remed = remediation_map.get(section_id, [])
    if remed:
        blocks.append(_paragraph(""))  # breathing room
        for child_section in remed:
            suffix = child_section["id"].replace(section_id + "_", "")
            toggle_label = f"↩ {suffix}"
            child_blocks = _render_remediation_section(child_section)
            blocks.append(_toggle(toggle_label, child_blocks))

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

    # Separate main sections from remediation children
    main_sections = [s for s in sections if not _is_remediation(s["id"])]

    # Build remediation map: parent_id → [child_section, ...]
    remediation_map: dict[str, list[dict]] = {}
    for s in sections:
        if _is_remediation(s["id"]):
            # Find parent: strip _light / _medium / _heavy (and _step\d+)
            sid = s["id"]
            # Try stripping _step1_light etc. first, then plain _light
            parent = re.sub(r"_step\d+_(light|medium|heavy)$", "", sid)
            parent = re.sub(r"_(light|medium|heavy)$", "", parent)
            remediation_map.setdefault(parent, []).append(s)

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

    # Main sections
    for section in main_sections:
        blocks.extend(_render_main_section(section, remediation_map))

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
) -> dict[str, list[tuple[str, str]]]:
    """
    Walk all blocks and build a mapping of section_id → [(emoji, text), ...].

    Main sections: callouts collected between consecutive h2 markers.
    Remediation sections: callouts collected from toggle children whose
    heading text matches a known remediation suffix pattern.
    """
    mapping: dict[str, list[tuple[str, str]]] = {}
    current_section: str | None = None
    current_callouts: list[tuple[str, str]] = []
    current_remed_toggles: list[dict] = []

    def _flush():
        if current_section is not None:
            mapping[current_section] = list(current_callouts)
            # Process remediation toggles
            for toggle in current_remed_toggles:
                toggle_text = _extract_rt_text(toggle.get("toggle", {}).get("rich_text", []))
                # "↩ light" → suffix "light"
                suffix = toggle_text.strip().lstrip("↩ ").strip()
                remed_id = f"{current_section}_{suffix}"
                mapping[remed_id] = _collect_toggle_callouts(toggle)

    for block in blocks:
        btype = block.get("type")
        if btype == "heading_2":
            _flush()
            current_callouts = []
            current_remed_toggles = []
            raw = _extract_rt_text(block.get("heading_2", {}).get("rich_text", []))
            m = _HEADING2_ID_RE.search(raw)
            current_section = m.group(1) if m else None
        elif btype == "callout" and current_section is not None:
            emoji = _callout_emoji(block) or ""
            text = _extract_rt_text(block.get("callout", {}).get("rich_text", []))
            current_callouts.append((emoji, text))
        elif btype == "toggle" and current_section is not None:
            current_remed_toggles.append(block)

    _flush()
    return mapping


def _patch_section_beats(
    section: dict,
    callouts: list[tuple[str, str]],
) -> None:
    """
    Overlay callout texts onto the beats of *section* (mutates in place).

    Positional matching: DialogueBeat → next 💬 callout, PromptBeat → next ❓.
    SceneBeats are skipped (no callout emitted during push).

    Limitation: adding/removing callout blocks in Notion breaks alignment.
    """
    callout_iter = iter(callouts)

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
                    # First line is "❓  tool_id\n\"prompt text\""
                    lines = text.split("\n", 1)
                    if len(lines) == 2:
                        beat["text"] = lines[1].strip('"')
                    else:
                        beat["text"] = text.strip('"')
            # scene beats produce no callout — skip


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
    callout_map = _section_callouts_from_blocks(blocks)

    for section in patched.get("sections", []):
        sid = section["id"]
        if sid in callout_map:
            _patch_section_beats(section, callout_map[sid])

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
