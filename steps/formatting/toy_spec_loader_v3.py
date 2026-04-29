# ── V3 / Phase 8 skeleton ────────────────────────────────────────────────────
# Derived from: toy_spec_loader.py
# For use with: *_generator_v3 pipelines (unit100+ Phase 8 skeleton format)
# ─────────────────────────────────────────────────────────────────────────────
"""
toy_spec_loader_v3 - Formatting Step

Reads toy_specs.md (single file at units/unit{N}/toy_specs.md), parses the §3
toy roster and §5 beat-by-beat table, then enriches each section with
workspace_specs containing the toys used and student interaction types.

Replaces both toy_spec_loader + glossary_drift_checker in v3 pipelines.

workspace_specs per section:
  {
    "toys": ["hundred_grid_mode_c", "drop_down"],
    "student_interactions": ["multiple_choice"]
  }

Toy matching strategy (per section):
  1. Beat-table lookup: extracts the beat code from the section header and
     maps it directly to the toy/mode entry in the §5 beat table.
  2. Keyword fallback: searches all string fields of the section against
     a phrase map built from §3 toy roster names.

Student interaction inference (per section):
  Keyword matching on student_action / teacher_move fields.
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Ordered keyword rules for student interaction inference.
# Each entry: (phrases_any_of, interaction_type).
# First match wins; a section may collect multiple types (all rules are tried).
_STUDENT_INTERACTION_RULES = [
    (["select all that apply", "check all", "both correct", "both must be selected",
      "checkbox"], "checkbox"),
    (["multiple choice", "choose one", "tap the one", "select one",
      "select the correct", "selects the correct"], "multiple_choice"),
    (["fill the stem", "fill-in-the-blank", "fill in the blank",
      "completes a", "completes the", "complete the stem",
      "sentence stem", "drop down", "guided stem", "short closure stem"], "fill_in_blank"),
    (["tap and hold", "taps and holds"], "tap_and_hold"),
    (["taps check", "tap check", "taps the check"], "check"),
    (["observation only", "no student action", "no production",
      "taps to observe", "tap to observe"], "observe"),
]

# Regex to extract beat codes from section headers.
# Matches W.N, L.N, EC.N, S.N patterns.
_BEAT_CODE_RE = re.compile(
    r'\b((?:W|L|EC|S)\.\d+)\b',
    re.IGNORECASE,
)


def _parse_toy_catalog(toy_specs_path: Path) -> dict:
    """
    Parse §3 toy roster table from toy_specs.md.

    Returns {canonical_name: description} for each toy row.
    The canonical_name is the bold text in column 1 (without qualifiers).
    """
    content = toy_specs_path.read_text(encoding="utf-8")
    m = re.search(r'^## §3', content, re.MULTILINE)
    if not m:
        return {}

    next_sec = re.search(r'^## §', content[m.end():], re.MULTILINE)
    roster_text = content[m.start(): m.start() + next_sec.start()] if next_sec else content[m.start():]

    catalog = {}
    for line in roster_text.splitlines():
        # Table row: | **Toy Name** (qualifier) | col2 | col3 | description | ...
        row_m = re.match(r'^\|\s*\*\*([^*|]+)\*\*', line)
        if not row_m:
            continue
        raw_name = row_m.group(1).strip()
        # Skip header row
        if raw_name.lower() in ("toy", "field"):
            continue
        cols = [c.strip() for c in line.split("|")[1:] if c.strip()]
        description = cols[3] if len(cols) > 3 else (cols[0] if cols else "")
        catalog[raw_name] = description

    return catalog


def _parse_beat_toy_map(toy_specs_path: Path) -> dict:
    """
    Parse §5 beat-by-beat table from toy_specs.md.

    Returns {beat_code: toy_description} e.g. {"W.1": "Hundred Grid Mode B..."}.
    """
    content = toy_specs_path.read_text(encoding="utf-8")
    m = re.search(r'^## §5', content, re.MULTILINE)
    if not m:
        return {}

    next_sec = re.search(r'^## §', content[m.end():], re.MULTILINE)
    table_text = content[m.start(): m.start() + next_sec.start()] if next_sec else content[m.start():]

    beat_map = {}
    for line in table_text.splitlines():
        cols = [c.strip() for c in line.split("|")[1:] if c.strip()]
        if len(cols) < 4:
            continue
        # Column layout: Beat | Code | Stage | Toy/Mode | ...
        code_raw = re.sub(r"\*\*", "", cols[1]).strip()
        toy_raw = re.sub(r"\*\*", "", cols[3]).strip()
        if _BEAT_CODE_RE.match(code_raw):
            beat_map[code_raw.upper()] = toy_raw

    return beat_map


def _build_keyword_map(toy_catalog: dict) -> dict:
    """
    Build {lowercase_phrase: canonical_name} from the toy catalog.

    Each toy name is split on '/' and the §N.N prefix is stripped so that
    substrings like "drop down" and "fill-in-the-blank" both map to the
    same canonical entry.
    """
    phrase_map = {}
    for name in toy_catalog:
        # Strip section-reference prefix (§2.10 etc.)
        clean = re.sub(r'§\d+\.\d+\s*', '', name).strip()
        phrase_map[clean.lower()] = name
        for part in clean.split("/"):
            p = part.strip()
            if len(p) > 3:
                phrase_map[p.lower()] = name
    return phrase_map


def _extract_beat_code(section: dict) -> str | None:
    """Extract beat code (e.g. 'W.1', 'L.2', 'EC.1') from section header."""
    header = section.get("header", "")
    m = _BEAT_CODE_RE.search(header)
    return m.group(1).upper() if m else None


def _match_toys(section: dict, toy_catalog: dict, beat_toy_map: dict, phrase_map: dict) -> list:
    """
    Return a list of matched canonical toy names for a section.

    Primary: look up the beat code in the §5 beat table, then check which
    catalog entries appear in that toy description string.
    Fallback: keyword search over all string fields of the section.
    """
    matched = set()

    # Primary: beat-table lookup
    beat_code = _extract_beat_code(section)
    if beat_code and beat_code in beat_toy_map:
        toy_desc = beat_toy_map[beat_code].lower()
        for phrase, canonical in phrase_map.items():
            if phrase in toy_desc:
                matched.add(canonical)

    # Fallback: keyword search over all section string fields
    if not matched:
        combined = " ".join(
            v for k, v in section.items()
            if isinstance(v, str) and k not in ("id", "header")
        ).lower()
        for phrase, canonical in phrase_map.items():
            if phrase in combined:
                matched.add(canonical)

    return sorted(matched)


def _infer_student_interactions(section: dict) -> list:
    """
    Infer student interaction types from student_action / teacher_move fields.
    Returns a list of interaction type strings.
    """
    fields_to_check = ("student_action", "teacher_move", "setup", "prompt")
    combined = " ".join(
        section.get(f, "") or ""
        for f in fields_to_check
    ).lower()

    if not combined.strip():
        return []

    matched = []
    for phrases, interaction_type in _STUDENT_INTERACTION_RULES:
        if any(p in combined for p in phrases):
            if interaction_type not in matched:
                matched.append(interaction_type)

    return matched


def load_specs_for_lesson(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Main entry point for the v3 pipeline formatting step.

    Reads toy_specs.md from units/unit{N}/toy_specs.md, enriches each
    section with workspace_specs (toys + student_interactions).

    Args:
        input_data: Parsed structured_spec.json (list of section dicts)
        unit_number: Unit number for locating toy_specs.md
        module_number: Unused in v3 (no per-module glossary lookup)
        verbose: Enable verbose logging

    Returns:
        List of sections, each with a workspace_specs field added.
    """
    if unit_number is not None:
        toy_specs_path = project_root / "units" / f"unit{unit_number}" / "toy_specs.md"
    else:
        toy_specs_path = project_root / "units" / "toy_specs.md"

    if not toy_specs_path.exists():
        if verbose:
            print(f"  [WARN] toy_specs.md not found: {toy_specs_path}")
        return input_data if isinstance(input_data, list) else input_data

    toy_catalog = _parse_toy_catalog(toy_specs_path)
    beat_toy_map = _parse_beat_toy_map(toy_specs_path)
    phrase_map = _build_keyword_map(toy_catalog)

    if verbose:
        print(f"  [TOY_SPEC_LOADER_V3] Catalog: {list(toy_catalog.keys())}")
        print(f"  [TOY_SPEC_LOADER_V3] Beat map: {beat_toy_map}")

    if isinstance(input_data, str):
        import json as _json
        try:
            input_data = _json.loads(input_data)
        except Exception:
            raise ValueError(
                "toy_spec_loader_v3 received raw text instead of parsed JSON. "
                "Step 1 (starterpack_parser_v3) likely produced malformed JSON — rerun from step 1."
            )

    sections = input_data if isinstance(input_data, list) else input_data.get("sections", [])

    for section in sections:
        section_id = section.get("id", "?")

        if section.get("workspace_specs"):
            if verbose:
                print(f"  [{section_id}] Using existing workspace_specs")
            continue

        toys = _match_toys(section, toy_catalog, beat_toy_map, phrase_map)
        student_interactions = _infer_student_interactions(section)

        workspace_specs = {
            "toys": toys,
            "student_interactions": student_interactions,
        }
        section["workspace_specs"] = workspace_specs

        if verbose:
            print(f"  [{section_id}] toys={toys}  student_interactions={student_interactions}")

    return sections
