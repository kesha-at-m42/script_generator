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
    elif method == "update":
        cats = params.get("highlight_categories", []) if params else []
        if cats:
            action = f"Highlight {', '.join(str(c) for c in cats)} on {tid}"
        else:
            action = f"Update {tid}"
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
        is_correct = state.get("is_correct")
        if is_correct is True:
            indicator = "✅"
        elif is_correct is False:
            indicator = "❌"
        else:
            indicator = "◻️"
        toggle_header = f"{indicator} {description}  [{cond_summary}]"

        # Render child beats for each step inside this state
        child_blocks: list[dict] = []
        for i, step in enumerate(state.get("steps", [])):
            if i > 0:
                child_blocks.append(_step_sep_block())
            for beat in step:
                child_blocks.extend(_render_beat(beat, section_id, nested=True))

        blocks.append(_toggle(toggle_header, child_blocks))
    return blocks


def _render_prompt(beat: dict, section_id: str) -> list[dict]:
    text = beat.get("text", "")
    tool = beat.get("tool", "")
    target = beat.get("target")
    options = beat.get("options", [])
    validator = beat.get("validator", [])

    blocks: list[dict] = []

    # First line: labeled key-value pairs separated by two spaces
    parts = [f"tool: {tool}"]
    if target is not None:
        if isinstance(target, list):
            parts.append("target: " + ", ".join(str(t) for t in target))
        elif isinstance(target, dict):
            parts.append(f"target: {target.get('type', '?')} (all)")
        else:
            parts.append(f"target: {target}")
    if options:
        parts.append("options: " + ", ".join(str(o) for o in options))

    callout_lines = ["  ".join(parts), f'"{text}"']
    blocks.append(_callout("\n".join(callout_lines), "❔"))

    # Validator states as toggles (flat array)
    if isinstance(validator, list):
        blocks.extend(_render_validator(validator, section_id))

    return blocks


def _render_current_scene(beat: dict, nested: bool = False) -> list[dict]:
    """Render current_scene as a collapsed toggle (reference-only).

    Only elements with a description are shown, as bullets.

    When *nested* is True (inside a validator state toggle), Notion's API
    forbids children on a toggle that is itself already nested inside another
    toggle (L3 block cannot have children).  In that case we flatten to a
    single callout so no extra nesting depth is required.
    """
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
        # Single callout — no children, safe at any nesting depth.
        summary = "  |  ".join(parts)
        return [_callout(f"Scene: {summary}", "📋")]

    # Top-level (inside section steps): toggle with bullets is fine (L2→L3).
    children = [_bullet(p) for p in parts]
    return [_toggle("📋 Current scene state (for reference, not to be edited)", children)]


def _render_beat(beat: dict, section_id: str, nested: bool = False) -> list[dict]:
    t = beat.get("type", "")
    if t == "dialogue":
        return _render_dialogue(beat)
    if t == "scene":
        return _render_scene(beat)
    if t == "current_scene":
        return _render_current_scene(beat, nested=nested)
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

    # Track visible workspace, starting from section's declared workspace.
    # "scene" is the key used by lesson_generator.json output; "workspace" by lesson.json.
    visible: set[str] = set(section.get("workspace") or section.get("scene") or [])

    # Collect section content as children of the toggle heading
    content: list[dict] = []

    # Steps (just visual grouping, no "Step N" label)
    steps = section.get("steps", [])
    for i, step in enumerate(steps):
        if i > 0:
            content.append(_step_sep_block())
        for beat in step:
            content.extend(_render_beat(beat, section_id))
            # Update visible set based on scene beats
            if beat.get("type") == "scene":
                method = beat.get("method", "")
                tid = beat.get("tangible_id", "")
                if method in ("show", "add") and tid:
                    visible.add(tid)
                elif method in ("hide", "remove") and tid:
                    visible.discard(tid)

    return [
        _divider(),
        _toggle_heading(2, f"{header}  [{section_id}]", content),
    ]


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def lesson_to_blocks(lesson: dict | list) -> list[dict]:
    """
    Convert lesson data to Notion blocks formatted as a readable script.

    Accepts either:
    - A full lesson dict (lesson.json format) with "id", "tangibles", "sections".
    - A bare list of section dicts (lesson_generator.json output format).

    Parameters
    ----------
    lesson : dict | list
        Parsed lesson data.

    Returns
    -------
    list[dict]
        Notion block objects ready for blocks.children.append.
    """
    if isinstance(lesson, list):
        sections = lesson
        lesson_id = None
        tangibles = {}
    else:
        sections = lesson.get("sections", [])
        lesson_id = lesson.get("id")
        tangibles = lesson.get("tangibles", {})

    blocks: list[dict] = []

    # Lesson title
    if lesson_id:
        blocks.append(_heading(1, lesson_id.replace("_", " ").title()))

    # Tangibles summary as a collapsed toggle
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
    Group a flat list of section content blocks into steps.

    Steps are delimited by paragraph blocks containing "· · ·".
    Each step is {"callouts": [(emoji, text), ...], "toggles": [block, ...]}.
    """
    steps: list[dict] = []
    current_callouts: list[tuple[str, str]] = []
    current_toggles: list[dict] = []

    for block in blocks:
        btype = block.get("type")
        if btype == "paragraph":
            text = _extract_rt_text(block.get("paragraph", {}).get("rich_text", []))
            if text.strip() == "· · ·":
                steps.append({"callouts": list(current_callouts), "toggles": list(current_toggles)})
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
        steps.append({"callouts": list(current_callouts), "toggles": list(current_toggles)})

    return steps


def _section_callouts_from_blocks(blocks: list[dict]) -> dict[str, dict]:
    """
    Walk all blocks and build a mapping of section_id → section_data.

    section_data has:
      - "steps": [{"callouts": [(emoji, text), ...], "toggles": [toggle_block, ...]}, ...]
        One entry per step group, delimited by · · · paragraph blocks.
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

            # Toggle heading: children are embedded after recursive fetch.
            # Non-toggleable headings (legacy format) fall through to flat sibling handling.
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
        parsed_opts = []
        for o in kv["options"].split(", "):
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


def _parse_new_beat(emoji: str, text: str) -> dict:
    """
    Convert a [new beat]-tagged Notion callout into a suggested beat with placeholders.
    The returned beat has notion_flag: "suggested".
    """
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


def _patch_section_beats(section: dict, section_data: dict) -> None:
    """
    Merge Notion callouts into the beats of *section* (mutates in place).

    Single forward pass per step: walk Notion callouts in order, maintain a pointer
    into JSON beats.
    - Callout has [new beat] tag → strip tag, insert suggested beat at current position,
      do NOT advance the JSON beat pointer (matching resumes from the same beat).
    - No tag → merge with current JSON beat (Notion-editable fields only), advance both.
    - Callouts exhausted before JSON beats → remaining JSON beats left untouched.

    Editable fields per beat type:
    - dialogue: text
    - scene: params.description (method/tangible_id are not in Notion)
    - prompt: tool, target, options, text + validator dialogue beats via toggles
    """
    notion_steps = section_data.get("steps", [])
    json_steps = section.get("steps", [])

    for i, notion_step in enumerate(notion_steps):
        notion_callouts = [
            (e, t) for e, t in notion_step["callouts"] if e in _EDITABLE_CALLOUT_EMOJIS
        ]
        toggle_iter = iter(notion_step["toggles"])

        if i < len(json_steps):
            json_step = json_steps[i]
            editable_beats = [b for b in json_step if b.get("type") in _EDITABLE_BEAT_TYPES]
            beat_ptr = 0
            insert_offset = 0  # tracks how many suggested beats were inserted before beat_ptr

            for emoji, text in notion_callouts:
                if _NEW_BEAT_TAG.search(text):
                    clean_text = _NEW_BEAT_TAG.sub("", text).strip()
                    insert_pos = beat_ptr + insert_offset
                    json_step.insert(insert_pos, _parse_new_beat(emoji, clean_text))
                    insert_offset += 1
                    continue

                if beat_ptr >= len(editable_beats):
                    break

                beat = editable_beats[beat_ptr]
                beat_ptr += 1
                btype = beat.get("type")

                if btype == "dialogue":
                    beat["text"] = _strip_dialogue_text(text)
                elif btype == "scene":
                    original_desc = (beat.get("params") or {}).get("description", "").strip()
                    new_desc = text.strip()
                    if original_desc != new_desc:
                        beat.setdefault("params", {})["description"] = new_desc
                        beat["_original_description"] = original_desc
                        beat["notion_flag"] = "updated"
                elif btype == "prompt":
                    beat.update(_parse_prompt_fields(text))
                    validator = beat.get("validator", [])
                    if isinstance(validator, list):
                        for state in validator:
                            try:
                                toggle_block = next(toggle_iter)
                            except StopIteration:
                                break
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
                                            state_beat["text"] = _strip_dialogue_text(t_text)
        else:
            # Extra Notion step group beyond JSON steps → new suggested step
            new_step = [
                _parse_new_beat(e, _NEW_BEAT_TAG.sub("", t).strip())
                for e, t in notion_callouts
                if e in _EDITABLE_CALLOUT_EMOJIS
            ]
            if new_step:
                json_steps.append(new_step)


def _collect_scene_flags(sections: list) -> list[dict]:
    """
    Collect scene beats flagged as "updated" by _patch_section_beats.
    Cleans up the temp _original_description key from each flagged beat.
    """
    flags = []
    for section in sections:
        sid = section["id"]
        for step in section.get("steps", []):
            for beat in step:
                if beat.get("type") == "scene" and beat.get("notion_flag") == "updated":
                    original_desc = beat.pop("_original_description", "")
                    flags.append(
                        {
                            "section_id": sid,
                            "tangible_id": beat.get("tangible_id", ""),
                            "method": beat.get("method", ""),
                            "original_description": original_desc,
                            "notion_description": (beat.get("params") or {}).get("description", ""),
                        }
                    )
    return flags


def blocks_to_lesson(blocks: list[dict], original: dict | list) -> tuple[dict | list, list[dict]]:
    """
    Merge Notion edits into *original* lesson data.

    Returns a tuple of:
    - Deep copy of *original* with Notion edits applied.
    - List of scene flag dicts where a 🎬 description was edited in Notion.

    Accepts either a full lesson dict (with "sections" key) or a bare list
    of section dicts (lesson_generator.json output format).
    """
    patched = copy.deepcopy(original)
    section_map = _section_callouts_from_blocks(blocks)

    if isinstance(patched, list):
        sections = patched
    else:
        sections = patched.get("sections", [])

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
