"""
starter_pack_json_loader - Formatting Step (Semi-AI)

Reads _starter_pack_ref.md (the raw Notion markdown produced by
notion_pull_starter_pack) and extracts structured module metadata.

Extraction strategy — deterministic first, Claude fallback:
  1. Regex/parsing for well-structured fields: module header, learning goals,
     vocabulary, required/forbidden phrases, misconceptions, the_one_thing, etc.
  2. Any field that couldn't be reliably extracted is sent to Claude with the
     relevant document section to fill in.

Output (starter_pack.json): structured module metadata dict.
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\uFE00-\uFE0F"
    "\u200D"
    "]+",
    flags=re.UNICODE,
)


def _clean_md_text(s: str) -> str:
    """Unescape markdown escape sequences and strip bold/italic markers from a content string."""
    if not s:
        return s
    # Unescape: \# → #,  \* → *,  \_ → _,  \[ → [  etc.
    s = re.sub(r"\\([*_#\[\](){}|`~>])", r"\1", s)
    # Strip bold/italic markers (**text** → text, *text* → text)
    s = re.sub(r"\*{2,}([^*]+)\*{2,}", r"\1", s)
    s = re.sub(r"\*([^*\n]+)\*", r"\1", s)
    return s.strip()


def _strip_emoji(obj):
    """Recursively strip emoji characters from all strings in a dict/list."""
    if isinstance(obj, str):
        return _EMOJI_RE.sub("", obj).strip()
    if isinstance(obj, dict):
        return {k: _strip_emoji(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_strip_emoji(i) for i in obj]
    return obj


# ---------------------------------------------------------------------------
# Deterministic extractors
# ---------------------------------------------------------------------------


def _bullets(text: str) -> list:
    """Extract * or - bullet list items from a text block."""
    items = re.findall(r"^[*\-]\s+(.+)", text, re.MULTILINE)
    return [i.strip() for i in items if i.strip()]


def _extract_module_header(text: str):
    """Return (module_name, module_number) from the title line.

    Handles:
      - '# **MODULE 1: DATA SENSE & 1:1 GRAPHS**'  (standard format)
      - '# BACKBONE' + '# END OF MODULE 11 STARTER PACK'  (backbone format)
    """
    # Standard: # **MODULE N: NAME**
    m = re.search(r"#\s+\**MODULE\s+(\d+)\s*:\s*([^*\n]+)", text, re.IGNORECASE)
    if m:
        return m.group(2).strip().rstrip("*").strip(), int(m.group(1))
    # Backbone format: module number buried in closing line, name not in title
    m = re.search(r"MODULE\s+(\d+)\s+STARTER PACK", text, re.IGNORECASE)
    if m:
        return None, int(m.group(1))
    return None, None


def _extract_learning_goals(text: str):
    goals = []
    for m in re.finditer(r'\*\*L\d+:\*\*\s*"([^"]+)"', text):
        goals.append(m.group(1).strip())
    return goals or None


def _extract_student_facing_goal(text: str):
    m = re.search(r'\*\*Module Goal \(Student-Facing\):\*\*\s*"([^"]+)"', text)
    return m.group(1).strip() if m else None


def _extract_exit_check_tests(text: str):
    # Format A: bullet list after the label (with optional blank lines)
    m = re.search(r"\*{0,2}Exit Check Tests:\*{0,2}\s*\n+((?:[*\-]\s*.+\n?)+)", text)
    if m:
        return _bullets(m.group(1))
    # Format B: inline numbered list — "**Exit Check Tests:** (1) ... (2) ... (3) ..."
    m = re.search(r"\*{0,2}Exit Check Tests:\*{0,2}\s*(.+?)(?=\n\n|\n###|\Z)", text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        items = re.split(r"\s*\(\d+\)\s*", raw)
        items = [_clean_md_text(i) for i in items if i.strip()]
        # Strip trailing decision notes like "*(Decision Q5)*"
        items = [re.sub(r"\s*\*\(Decision[^)]*\)\*\s*$", "", i).strip() for i in items]
        return [i for i in items if i] or None
    return None


def _extract_vocabulary(text: str):
    m = re.search(r"\*\*Assessment Vocabulary[^:]*:\*\*\s*(.+)", text)
    if not m:
        return None
    terms = [t.strip() for t in m.group(1).split(",")]
    return [t for t in terms if t] or None


def _extract_vocabulary_staging(text: str):
    # Scope to the subsection only — stop at the next ### heading to avoid
    # bleeding into adjacent tables (toy specs, data constraints, etc.)
    header_m = re.search(r"Vocabulary Staging by Phase", text, re.IGNORECASE)
    if not header_m:
        return None
    start = header_m.end()
    next_m = re.search(r"^#{2,3}\s", text[start:], re.MULTILINE)
    section = text[start : start + next_m.start()] if next_m else text[start : start + 3000]

    table_m = re.search(r"((?:\|.+\n)+)", section)
    if not table_m:
        return None
    rows = [r.strip() for r in table_m.group(1).strip().splitlines() if r.strip().startswith("|")]
    if len(rows) < 3:
        return None
    result = []
    for row in rows[2:]:  # skip header + divider
        cells = [_clean_md_text(c) for c in row.strip("|").split("|")]
        if len(cells) < 3:
            continue
        phase, terms_raw, approach = cells[0], cells[1], cells[2]
        terms = re.findall(r'"([^"]+)"', terms_raw)
        if not terms:
            terms = [terms_raw.strip("()").strip()]
        result.append({"phase": phase.strip(), "terms": terms, "approach": approach.strip()})
    return result or None


def _extract_required_phrases(text: str):
    # Handle both '### **Required Phrases...**' and '### Required Phrases...**' (missing opening **)
    m = re.search(
        r"### \*{0,2}Required Phrases[^*\n]*\*{0,2}.*?\n+((?:[*\-]\s*.+\n?)+)",
        text,
        re.IGNORECASE,
    )
    if not m:
        return None
    items = re.findall(r"^[*\-]\s*(.+)", m.group(1), re.MULTILINE)
    cleaned = []
    for item in items:
        item = _clean_md_text(item)
        item = re.sub(r'"\s*\(or equivalent[^)]*\)\s*', "", item)
        item = item.replace('"', "")             # strip all quotes (visual emphasis only)
        item = item.strip()
        if item:
            cleaned.append(item)
    return cleaned or None


def _extract_forbidden_phrases(text: str):
    m = re.search(
        r"### \*{0,2}Forbidden Phrases[^*\n]*\*{0,2}.*?\n+((?:[*\-]\s*.+\n?)+)",
        text,
        re.IGNORECASE,
    )
    if not m:
        return None
    items = re.findall(r"^[*\-]\s*(.+)", m.group(1), re.MULTILINE)
    result = []
    for item in items:
        item = _clean_md_text(item.strip())
        reason_m = re.search(r"\(([^)]+)\)\s*$", item)
        if reason_m:
            phrase = item[: reason_m.start()].strip().strip("\"'")
            reason = reason_m.group(1).strip()
        else:
            phrase = item.strip("\"'")
            reason = ""
        # Strip any remaining ** bold markers from the phrase text
        phrase = re.sub(r"\*+", "", phrase).strip()
        if phrase:
            result.append({"phrase": phrase, "reason": reason})
    return result or None


def _extract_the_one_thing(text: str):
    # Handle both '## **1.0 THE ONE THING**' and '## 1.0 THE ONE THING' (no bold)
    sec_m = re.search(
        r"## \*{0,2}1\.0 THE ONE THING\*{0,2}.*?\n(.*?)(?=^## |\Z)",
        text,
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not sec_m:
        return None
    sec = sec_m.group(1)

    # Module 1 format: line that IS entirely **bold** → the statement
    statement_m = re.search(r"^\*\*([^*\n]+)\*\*\s*$", sec.strip(), re.MULTILINE)
    if statement_m:
        statement = statement_m.group(1).strip()
    else:
        # Module 11 format: first substantial paragraph (may contain partial bold)
        plain_m = re.search(r"^([A-Z][^\n]{30,})", sec.strip(), re.MULTILINE)
        statement = plain_m.group(1).strip() if plain_m else None

    crit_m = re.search(r"\*\*Critical Misconception:\*\*\s*(.+?)(?:\n|$)", sec)
    critical_misconception = None
    if crit_m:
        crit_text = crit_m.group(1).strip()
        id_m = re.search(r"#(\d+)", crit_text)
        label_m = re.match(r"^([^(\\#]+?)(?:\s*[\\(]\s*#\d+|\s*—)", crit_text)
        label = label_m.group(1).strip() if label_m else crit_text
        why_m = re.search(r"—\s*(.+)$", crit_text)
        critical_misconception = {
            "id": id_m.group(1) if id_m else "",
            "label": label,
            "why_critical": why_m.group(1).strip() if why_m else "",
        }

    success_m = re.search(r"\*\*Success Indicator:\*\*\s*(.+?)(?:\n|$)", sec)
    risk_m = re.search(r"\*\*Biggest Risk:\*\*\s*(.+?)(?:\n|$)", sec)

    result = {}
    if statement:
        result["statement"] = statement
    if critical_misconception:
        result["critical_misconception"] = critical_misconception
    if success_m:
        result["success_indicator"] = success_m.group(1).strip()
    if risk_m:
        result["biggest_risk"] = risk_m.group(1).strip()
    return result or None


def _extract_misconceptions(text: str):
    # Handle both '## **1.4 MISCONCEPTIONS**' and '## 1.4 MISCONCEPTIONS'
    sec_m = re.search(
        r"## \*{0,2}1\.4 MISCONCEPTIONS\*{0,2}.*?\n(.*?)(?=^## |\Z)",
        text,
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not sec_m:
        return None
    sec = sec_m.group(1)

    result = []
    # Match any ### subsection within 1.4 that contains a misconception ID.
    # Handles two ID formats:
    #   Module 1:  ### **1.4.1 Graph as Picture (PRIMARY) — Misconception \#16**
    #   Module 11: ### **1.4.1 Rows/Columns Confusion (#8) — PRIMARY**
    for m in re.finditer(r"### \*{0,2}([\d.]+)\s+([^*\n]+?)\*{0,2}\s*\n", sec):
        header_content = m.group(2)
        id_m = re.search(r"[\\(#]+(\d+)", header_content)
        if not id_m:
            continue
        misconception_id = id_m.group(1)

        # Build clean label: strip ID (including trailing colon), PRIMARY/SECONDARY markers
        label = re.sub(r"\s*[\\(#]+\d+\)?:?", "", header_content)
        label = re.sub(r"\s*—\s*(PRIMARY|SECONDARY)[^—]*", "", label, flags=re.IGNORECASE)
        label = re.sub(r"\s*\((PRIMARY|SECONDARY)[^)]*\)", "", label, flags=re.IGNORECASE)
        label = re.sub(r"\s*Misconception\b", "", label, flags=re.IGNORECASE)
        label = _clean_md_text(label.strip(" —*)").strip())

        sec_start = m.end()
        next_m = re.search(r"^###\s", sec[sec_start:], re.MULTILINE)
        block = sec[sec_start : sec_start + next_m.start()] if next_m else sec[sec_start:]

        # Description: 'Trigger Behavior' (M1) or 'What It Looks Like' (M11)
        desc_m = re.search(
            r"\*\*(?:Trigger Behavior|What It Looks Like):\*\*\s*(.+?)(?=\n\n|\*\*|\Z)",
            block,
            re.DOTALL,
        )
        # Prevention: bold or plain label
        prev_m = re.search(
            r"\*{0,2}Prevention Strategy:\*{0,2}.*?\n((?:[*\-]\s*.+\n?)+)",
            block,
            re.IGNORECASE,
        )
        result.append({
            "id": misconception_id,
            "misconception": label,
            "description": _clean_md_text(desc_m.group(1)) if desc_m else "",
            "prevention": [_clean_md_text(b) for b in _bullets(prev_m.group(1))] if prev_m else [],
        })
    return result or None


def _extract_scope_fence_extras(text: str):
    """Extract advanced_vocabulary and advanced_concepts for scope_fence."""
    result = {}
    avoid_m = re.search(
        r"Terms to Avoid[^#\n]*\n((?:[*\-]\s*.+\n?)+)", text, re.IGNORECASE
    )
    if avoid_m:
        items = re.findall(r'^[*\-]\s*"?([^"(\n]+)', avoid_m.group(1), re.MULTILINE)
        result["advanced_vocabulary"] = [i.strip() for i in items if i.strip()]

    excl_m = re.search(r"Must Not Include.*?\n((?:[*\-]\s*.+\n?)+)", text, re.IGNORECASE)
    if excl_m:
        result["advanced_concepts"] = _bullets(excl_m.group(1))
    return result


def _extract_standards(text: str):
    """Extract standards cascade table + module bridge paragraphs."""
    # ---- Cascade table --------------------------------------------------------
    sec_m = re.search(r"### 1\.1\.1 Standards Cascade\n(.*?)(?=^###|\Z)", text, re.DOTALL | re.MULTILINE)
    if not sec_m:
        return None

    table_m = re.search(r"((?:\|.+\n)+)", sec_m.group(1))
    result = {"building_on": [], "addressing": [], "building_toward": []}
    _key_map = {
        "building on": "building_on",
        "addressing": "addressing",
        "building toward": "building_toward",
    }
    current_key = None
    if table_m:
        rows = [r for r in table_m.group(1).strip().splitlines() if r.strip().startswith("|")]
        for row in rows:
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) < 2 or "---" in cells[0]:
                continue
            label_raw = _clean_md_text(cells[0]).lower().strip()
            value = _clean_md_text(cells[1]).strip()
            if label_raw:
                current_key = _key_map.get(label_raw)
            if current_key and value:
                result[current_key].append(value)

    # ---- Bridge paragraphs ---------------------------------------------------
    bridge_m = re.search(r"### 1\.1\.2 Module Bridges\n(.*?)(?=^##|\Z)", text, re.DOTALL | re.MULTILINE)
    if bridge_m:
        bridge = {}
        for para_m in re.finditer(r"\*\*([^*]+):\*\*\s*(.+?)(?=\n\*\*[^*]+:\*\*|\Z)", bridge_m.group(1), re.DOTALL):
            raw_label = para_m.group(1).strip()
            content = re.sub(r"\s+", " ", para_m.group(2)).strip()
            # Normalise label: "From Module 10" → "from_module_10", "This Module" → "this_module"
            key = re.sub(r"\s+", "_", raw_label.lower())
            key = re.sub(r"[^a-z0-9_]", "", key)
            bridge[key] = _clean_md_text(content)
        if bridge:
            result["bridge"] = bridge

    return result if any(result[k] for k in ("building_on", "addressing", "building_toward")) else None


def _extract_core_concepts(text: str):
    """Extract bullet items from the Must Teach section."""
    sec_m = re.search(
        r"### \*{0,2}[^\S\n]*✅?[^\S\n]*Must Teach\*{0,2}\n(.*?)(?=^###|\Z)",
        text,
        re.DOTALL | re.MULTILINE,
    )
    if not sec_m:
        return None
    items = [_clean_md_text(b) for b in _bullets(sec_m.group(1))]
    return items or None


def _extract_variables(text: str):
    """Extract the Data Constraints table as a list of phase objects."""
    sec_m = re.search(r"### \*{0,2}Data Constraints\*{0,2}\n(.*?)(?=^###|\Z)", text, re.DOTALL | re.MULTILINE)
    if not sec_m:
        return None
    table_m = re.search(r"((?:\|.+\n)+)", sec_m.group(1))
    if not table_m:
        return None

    rows = [r for r in table_m.group(1).strip().splitlines() if r.strip().startswith("|")]
    if len(rows) < 3:
        return None

    # Parse header row to get column names
    headers = [_clean_md_text(c).lower().replace(" ", "_") for c in rows[0].strip("|").split("|")]

    result = []
    for row in rows[2:]:  # skip header + divider
        cells = [_clean_md_text(c) for c in row.strip("|").split("|")]
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        entry = {headers[i]: cells[i] for i in range(len(headers)) if cells[i]}
        if entry.get("phase"):
            result.append(entry)
    return result or None


# ---------------------------------------------------------------------------
# Claude fallback
# ---------------------------------------------------------------------------

_FALLBACK_PROMPT = """The following is a module starter pack document:

<document>
{markdown}
</document>

Extract the following fields that could not be parsed automatically.
Return ONLY a valid JSON object containing exactly the keys listed below.
Omit any key whose value genuinely cannot be found in the document.

Fields needed:
{fields_needed}

Rules:
- No markdown fences, no explanation — just the JSON object.
- Use the exact key names listed above.
- For list fields, return a JSON array.
- For grade_level, return an integer (e.g. 3)."""


def _claude_fallback(markdown: str, missing_fields: list, verbose: bool) -> dict:
    """Use Claude to fill in fields that deterministic extraction missed."""
    fields_description = "\n".join(
        f"- {f}" for f in missing_fields
    )
    prompt = _FALLBACK_PROMPT.format(
        markdown=markdown,
        fields_needed=fields_description,
    )

    sys.path.insert(0, str(project_root / "core"))
    from claude_client import ClaudeClient  # noqa: E402

    client = ClaudeClient()
    if verbose:
        print(f"  [SP_JSON_LOADER] Claude fallback for: {missing_fields}")

    raw = client.generate(
        user_message=prompt,
        max_tokens=2000,
        temperature=0,
        prefill="{",
        model="claude-haiku-4-5-20251001",
    )

    sys.path.insert(0, str(project_root / "utils"))
    from json_utils import extract_json  # noqa: E402

    result = extract_json(raw)
    return result if isinstance(result, dict) else {}


# ---------------------------------------------------------------------------
# Misconceptions registry
# ---------------------------------------------------------------------------

_MISCONCEPTIONS_REGISTRY = project_root / "config" / "misconceptions.json"


def _update_misconceptions_registry(misconceptions: list, module_number: int, verbose: bool):
    """Upsert module misconceptions into config/misconceptions.json.

    Registry is a dict keyed by misconception ID. Each entry stores the latest
    description/prevention and a list of all modules that reference it.
    """
    import json as _json

    if not misconceptions:
        return

    try:
        registry = _json.loads(_MISCONCEPTIONS_REGISTRY.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        registry = {}

    for m in misconceptions:
        mid = str(m.get("id", ""))
        if not mid:
            continue
        entry = registry.get(mid, {})
        entry["id"] = mid
        entry["misconception"] = m.get("misconception", entry.get("misconception", ""))
        if m.get("description"):
            entry["description"] = m["description"]
        if m.get("prevention"):
            entry["prevention"] = m["prevention"]
        refs = entry.get("referenced_by_modules", [])
        if module_number not in refs:
            refs.append(module_number)
        entry["referenced_by_modules"] = sorted(refs)
        registry[mid] = entry

    # Write sorted by numeric ID
    sorted_registry = dict(sorted(registry.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999))
    _MISCONCEPTIONS_REGISTRY.write_text(
        _json.dumps(sorted_registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if verbose:
        print(f"  [SP_JSON_LOADER] Updated misconceptions registry ({len(registry)} entries)")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def load(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Extract structured module metadata from _starter_pack_ref.md.

    Tries deterministic parsing first. Falls back to Claude only for
    fields that couldn't be reliably extracted.

    Args:
        input_data: Ignored — reads _starter_pack_ref.md from the module directory.
        unit_number: Unit number (e.g. 1).
        module_number: Module number (e.g. 3).
        verbose: Enable verbose logging.

    Returns:
        Dict of structured module metadata.
    """
    if unit_number is None or module_number is None:
        raise ValueError("starter_pack_json_loader requires unit_number and module_number")

    module_dir = project_root / "units" / f"unit{unit_number}" / f"module{module_number}"
    md_path = module_dir / "_starter_pack_ref.md"

    if not md_path.exists():
        raise FileNotFoundError(
            f"No _starter_pack_ref.md found at {md_path.relative_to(project_root)}. "
            "Run notion_pull_starter_pack first."
        )

    text = md_path.read_text(encoding="utf-8")
    if verbose:
        print(f"  [SP_JSON_LOADER] Reading {md_path.relative_to(project_root)} ({len(text)} chars)")

    # ------------------------------------------------------------------
    # 0. Page properties from YAML frontmatter (written by notion_pull)
    # ------------------------------------------------------------------
    page_props: dict = {}
    fm_m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if fm_m:
        for line in fm_m.group(1).splitlines():
            kv = line.split(":", 1)
            if len(kv) == 2:
                k, v = kv[0].strip(), kv[1].strip().strip('"')
                page_props[k] = v
        if verbose:
            print(f"  [SP_JSON_LOADER] Page props: {list(page_props.keys())}")

    # ------------------------------------------------------------------
    # 1. Deterministic extraction
    # ------------------------------------------------------------------
    module_name, module_number_parsed = _extract_module_header(text)
    required_phrases = _extract_required_phrases(text)
    forbidden_phrases = _extract_forbidden_phrases(text)
    learning_goals = _extract_learning_goals(text)
    student_facing_goal = _extract_student_facing_goal(text)
    exit_check_tests = _extract_exit_check_tests(text)
    vocabulary = _extract_vocabulary(text)
    vocabulary_staging = _extract_vocabulary_staging(text)
    the_one_thing = _extract_the_one_thing(text)
    misconceptions = _extract_misconceptions(text)
    scope_fence_extras = _extract_scope_fence_extras(text)
    standards = _extract_standards(text)
    core_concepts = _extract_core_concepts(text)
    variables = _extract_variables(text)

    # ------------------------------------------------------------------
    # 2. Identify what deterministic extraction missed
    # ------------------------------------------------------------------

    # Try page properties for module_name if markdown didn't have it
    if not module_name and page_props:
        # Common property names for the module/lesson name
        for prop_key in ("Name", "Module Name", "Title", "Lesson Name"):
            val = page_props.get(prop_key)
            if val and isinstance(val, str) and val.strip():
                module_name = val.strip()
                break

    missing = []
    if not module_name:
        missing.append("module_name (string, e.g. 'Data Sense & 1:1 Graphs')")
    if not learning_goals:
        missing.append("learning_goals (list of strings — verbatim L1, L2 goals)")
    if not student_facing_goal:
        missing.append("student_facing_goal (string)")
    if not exit_check_tests:
        missing.append("exit_check_tests (list of strings)")
    if not vocabulary:
        missing.append("vocabulary (list of term strings in introduction order)")
    if not required_phrases and re.search(r"Required Phrases", text, re.IGNORECASE):
        missing.append("scope_fence.required_phrases (list of strings)")
    if not forbidden_phrases and re.search(r"Forbidden Phrases", text, re.IGNORECASE):
        missing.append("scope_fence.forbidden_phrases (list of {phrase, reason})")
    if not the_one_thing:
        missing.append(
            "the_one_thing ({statement, critical_misconception: {id, label, why_critical}, "
            "success_indicator, biggest_risk})"
        )
    if not misconceptions:
        missing.append(
            "misconceptions (list of {id, misconception, description, prevention: list})"
        )
    # grade_level is always 3 for this curriculum
    grade_level = 3

    # ------------------------------------------------------------------
    # 3. Claude fallback for anything missing
    # ------------------------------------------------------------------
    fallback = {}
    if missing:
        fallback = _claude_fallback(text, missing, verbose=verbose)

    # ------------------------------------------------------------------
    # 4. Assemble result — deterministic values take priority over fallback
    # ------------------------------------------------------------------
    scope_fence = {
        **scope_fence_extras,
        "required_phrases": required_phrases or fallback.pop("scope_fence.required_phrases", []),
        "forbidden_phrases": forbidden_phrases or fallback.pop("scope_fence.forbidden_phrases", []),
    }

    result = {
        "module_name": module_name or fallback.get("module_name", ""),
        "module_number": module_number_parsed or module_number,
        "grade_level": grade_level,
        "the_one_thing": the_one_thing or fallback.get("the_one_thing"),
        "student_facing_goal": student_facing_goal or fallback.get("student_facing_goal"),
        "exit_check_tests": exit_check_tests or fallback.get("exit_check_tests", []),
        "learning_goals": learning_goals or fallback.get("learning_goals", []),
        "vocabulary": vocabulary or fallback.get("vocabulary", []),
        "vocabulary_staging": vocabulary_staging or fallback.get("vocabulary_staging", []),
        "scope_fence": scope_fence,
        "misconceptions": misconceptions or fallback.get("misconceptions", []),
        "standards": standards,
        "core_concepts": core_concepts,
        "variables": variables,
    }

    # Drop None values at top level, strip emojis from all strings
    result = {k: v for k, v in result.items() if v is not None}
    result = _strip_emoji(result)

    # Update config/misconceptions.json registry
    _update_misconceptions_registry(result.get("misconceptions", []), module_number, verbose)

    # Write to _starter_packs/module_N.json alongside the pipeline output
    import json as _json

    sp_dir = project_root / "units" / f"unit{unit_number}" / "_starter_packs"
    sp_dir.mkdir(exist_ok=True)
    sp_path = sp_dir / f"module_{module_number}.json"
    sp_path.write_text(_json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    if verbose:
        print(f"  [SP_JSON_LOADER] Written: {sp_path.relative_to(project_root)}")

    print(
        f"  [SP_JSON_LOADER] Done: {result.get('module_name', '?')} "
        f"(module {result.get('module_number', '?')}, "
        f"grade {result.get('grade_level', '?')})"
    )
    return result
