"""
toy_spec_loader - Formatting Step

Reads structured_spec.json (output of starterpack_parser), processes each section
individually to infer which toys and tools are used, loads the corresponding spec
files from units/unit{N}/toy_specs/, and outputs an enriched_spec.json with:
  - toy_specs: global dict of loaded spec content (union across all sections)
  - sections: original sections, each enriched with a `workspace_specs` field

workspace_specs per section:
  {
    "toys": [{"type": "picture_graph"}, {"type": "data_table"}],
    "tools": ["click_category"]
  }

Toy matching strategy (per section):
  1. Keyword map: known toy phrases → spec filename (fast, deterministic)
  2. AI fallback: for visual mentions that don't match the keyword map, extract
     WHAT excerpts from all spec files and ask Claude to pick the best match.

Tool inference (per section):
  Keyword matching on prompt + guide text to identify interaction type.
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Phrase map is loaded from glossary.md at runtime via _load_phrase_map().
# The KEYWORD_MAP that was here has been migrated to the glossary's
# "Common spec phrases" table — edit that file to add new phrase mappings.

# Phrases in visual fields that describe section-start state (empty screen) — not toys.
# Every section begins with a clear screen by definition, so these carry no toy information.
# Exact forms (phrases that don't end in a clearing/fading verb but are still transition boilerplate):
_SECTION_START_PHRASES = {
    "clean transition",
    "clean transition screen",
}

# Any capitalized phrase extracted from a visual field that ends with a clearing or fading verb
# is also transition boilerplate — e.g. "Practice clears", "Lesson graph clears",
# "Equation Builder clears", "Lesson visualization fades".
_CLEARING_VERB_RE = re.compile(r'\b(clears?|fades?)\s*$', re.IGNORECASE)

# Phrases in visual fields that suggest the spec assumes workspace carries over from a prior section.
_CARRY_OVER_PHRASES = [
    "same graph", "same picture graph", "same bar graph", "same visual",
    "same data table", "same '", 'same "',
    "continues from", "graph remains", "remains on screen",
    "still visible", "still on screen",
]

# Ordered tool inference rules: (phrases_any_of, tool_name_or_list)
# First match wins per section. tool_name may be a list for interactions requiring multiple tools.
_TOOL_RULES = [
    (["select all that apply", "select all"], "multi_select"),
    (["click on the part", "click the part", "click on the key", "click on the title",
      "click on the label", "click on the component"], "click_component"),
    (["click on", "click the bar", "click the category", "click the"], "click_category"),
    (["tile palette", "equation builder tiles", "using tiles", "drag tile",
      "place tile", "drag the tile", "place the tile",
      "build the expression", "build an expression", "build the equation",
      "build an equation"], "place_tile"),
    (["add row", "add the row", "add rows", "add the rows",
      "add column", "add the column", "add columns", "add the columns"],
     ["add_row", "add_column"]),
]

# Pattern to extract toy-like phrases from visual fields.
_TOY_PHRASE_RE = re.compile(
    r'\b([A-Z][A-Za-z\s\-/]+?)\s*(?:\(Mode|\(mode|visible|appears|alongside|\.|,)',
    re.MULTILINE
)


def _extract_what_excerpt(spec_file: Path, max_chars: int = 300) -> str:
    """Extract the WHAT description from a spec file."""
    content = spec_file.read_text(encoding="utf-8")
    match = re.search(r'>\s*\*\*WHAT:\*\*\s*(.*?)(?:\n\n|\n>|\*\*WHY)', content, re.DOTALL)
    if match:
        return match.group(1).strip()[:max_chars]
    for line in content.splitlines():
        stripped = line.strip().lstrip(">").strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("Category"):
            return stripped[:max_chars]
    return content[:max_chars]


def _load_excerpts(toy_specs_dir: Path) -> dict:
    """Load WHAT excerpts from all spec files in the directory."""
    excerpts = {}
    for spec_file in sorted(toy_specs_dir.glob("*.md")):
        excerpts[spec_file.stem] = _extract_what_excerpt(spec_file)
    return excerpts


def _match_toys_from_visual(visual_text: str, available: set, phrase_map: dict) -> set:
    """Return spec names matched by the glossary phrase map from a single visual field."""
    text_lower = visual_text.lower()
    matched = set()
    for phrase, spec_name in phrase_map.items():
        if phrase in text_lower and spec_name in available:
            matched.add(spec_name)
    return matched


def _extract_unmatched_phrases(visual_text: str, already_matched: set, phrase_map: dict) -> list:
    """Extract capitalised toy-like phrases from visual text that weren't matched."""
    candidates = []
    for m in _TOY_PHRASE_RE.finditer(visual_text):
        phrase = m.group(1).strip()
        if len(phrase) < 4:
            continue
        phrase_lower = phrase.lower()
        known = phrase_map.get(phrase_lower)
        if known and known in already_matched:
            continue
        if phrase_lower in {"each", "same", "new", "student", "guide", "key", "data"}:
            continue
        if phrase_lower in _SECTION_START_PHRASES:
            continue
        if _CLEARING_VERB_RE.search(phrase_lower):
            continue
        candidates.append(phrase)
    return candidates


def _ai_match(unmatched_phrases: list, excerpts: dict, visual_context: str) -> dict:
    """
    Use Claude to match unmatched phrases to the best available spec.
    Returns dict: {phrase -> spec_name or None}
    """
    if not unmatched_phrases:
        return {}

    sys.path.insert(0, str(project_root / "core"))
    from claude_client import ClaudeClient

    spec_descriptions = "\n".join(
        f"- {name}: {excerpt}" for name, excerpt in excerpts.items()
    )
    phrases_list = "\n".join(f"- {p}" for p in unmatched_phrases)

    prompt = f"""A lesson visual description mentions these elements that may be toy/component types:
{phrases_list}

Visual context:
{visual_context[:400]}

Available toy specs (name: description):
{spec_descriptions}

For each element, output the single best matching spec name from the list above, or "none" if no spec covers it.
Output one line per element in the format: element_name -> spec_name
No explanation, just the mappings."""

    client = ClaudeClient()
    response = client.generate(
        user_message=prompt,
        max_tokens=200,
        temperature=0,
    )

    result = {}
    for line in response.strip().splitlines():
        if "->" in line:
            parts = line.split("->", 1)
            phrase = parts[0].strip()
            spec = parts[1].strip().lower().replace(" ", "_")
            for orig in unmatched_phrases:
                if orig.lower() in phrase.lower() or phrase.lower() in orig.lower():
                    result[orig] = spec if spec != "none" and spec in excerpts else None
                    break
    return result


def _detect_carry_over(section: dict) -> bool:
    """Return True if the visual field suggests the spec assumes workspace carry-over."""
    visual = (section.get("visual", "") or "").lower()
    return any(phrase in visual for phrase in _CARRY_OVER_PHRASES)


def _ai_infer_tools(section: dict, tool_descriptions: dict) -> list | None:
    """
    Use Claude to infer interaction tools when no keyword rule matched.
    Returns a list of tool names, or None if inference is inconclusive.
    """
    if not tool_descriptions:
        return None

    sys.path.insert(0, str(project_root / "core"))
    from claude_client import ClaudeClient

    tools_list = "\n".join(
        f"- {name}: {desc}" for name, desc in sorted(tool_descriptions.items())
    )

    section_text = "\n".join(
        f"{k}: {v}" for k, v in section.items()
        if isinstance(v, str) and k not in ("id", "purpose")
    )

    prompt = f"""A lesson section describes one or more student interactions (sometimes across numbered steps like Step 1, Step 2, Step 3). Identify every tool the student uses across ALL steps in this section.

Section:
{section_text[:800]}

Available tools (name: description):
{tools_list}

Rules:
- A single student_action field may describe two actions joined by "and" (e.g. "selects X or Y and fills slots") — identify a tool for each sub-action separately.
- Choosing between two named word options (e.g. "rows" or "columns") is multiple_choice.
- Output each tool name once (no duplicates), one per line.
- If the section is purely observational with no student action, output "none".
- No explanation."""

    client = ClaudeClient()
    response = client.generate(user_message=prompt, max_tokens=200, temperature=0)

    tools = []
    for line in response.strip().splitlines():
        name = line.strip().lstrip("-").strip()
        if name and name != "none" and name in tool_descriptions:
            tools.append(name)

    return tools if tools else None


def _infer_tools(section: dict, tool_descriptions: dict | None = None) -> list:
    """
    Infer interaction tools from all string fields in the section.
    First tries keyword rules, then AI inference, then falls back to multiple_choice.
    Returns a list of tool names (may be empty for transition sections).
    """
    # Check for any prompt field to determine if this section has student interaction
    has_prompt = any(
        (k == "prompt" or (k.startswith("prompt") and k[6:].lstrip("_").isdigit()))
        and bool(v)
        for k, v in section.items()
    )
    if not has_prompt:
        return []

    combined = " ".join(
        v for k, v in section.items()
        if isinstance(v, str) and k not in ("id", "purpose")
    ).lower()

    matched = []
    for phrases, tool_name in _TOOL_RULES:
        if any(p in combined for p in phrases):
            tools = tool_name if isinstance(tool_name, list) else [tool_name]
            for t in tools:
                if t not in matched:
                    matched.append(t)

    is_multi_step = any(
        k.startswith("prompt_") and k[7:].isdigit()
        for k in section.keys()
    )

    if tool_descriptions and (not matched or is_multi_step):
        ai_result = _ai_infer_tools(section, tool_descriptions)
        if ai_result:
            for t in ai_result:
                if t not in matched:
                    matched.append(t)

    if matched:
        return matched

    # Final fallback: flag for review
    return ["multiple_choice", "__fallback__"]


def _match_section_toys(
    section: dict,
    available: set,
    excerpts: dict,
    phrase_map: dict,
    verbose: bool = False,
) -> tuple:
    """
    Infer toy types for a single section.

    Returns (matched_toys, unresolved_phrases) where:
      - matched_toys: list of {"type": toy_name} dicts
      - unresolved_phrases: list of visual phrases that couldn't be matched to any spec
    """
    visual = section.get("visual", "")
    if not visual:
        return [], []

    matched = _match_toys_from_visual(visual, available, phrase_map)

    unmatched_phrases = _extract_unmatched_phrases(visual, matched, phrase_map)
    unresolved = []

    if unmatched_phrases:
        if verbose:
            print(f"    [AI fallback] Unmatched phrases: {unmatched_phrases}")
        ai_matches = _ai_match(unmatched_phrases, excerpts, visual)
        for phrase, spec_name in ai_matches.items():
            if spec_name and spec_name in available:
                matched.add(spec_name)
                if verbose:
                    print(f"    [AI] '{phrase}' → {spec_name}")
            else:
                unresolved.append(phrase)
                if verbose:
                    print(f"    [UNRESOLVED] '{phrase}' — no matching spec")

    return [{"type": name} for name in sorted(matched)], unresolved


def _load_glossary(unit_number: int = None, module_number: int = None):
    """Load and parse glossary.md. Returns GlossaryData or None if not found."""
    sys.path.insert(0, str(project_root / "core"))
    from path_manager import resolve_doc_path

    glossary_path = resolve_doc_path(
        "glossary.md",
        unit_number=unit_number,
        module_number=module_number,
    )
    if not glossary_path or not glossary_path.exists():
        return None

    sys.path.insert(0, str(project_root / "utils"))
    from glossary_parser import parse_glossary

    return parse_glossary(glossary_path)


def _load_phrase_map(unit_number: int = None, module_number: int = None) -> dict:
    """Load the phrase → canonical name map from glossary.md."""
    data = _load_glossary(unit_number=unit_number, module_number=module_number)
    return data.full_alias_map if data else {}


def _load_tool_descriptions(unit_number: int = None, module_number: int = None) -> dict:
    """Load tool name → description map from glossary.md for AI inference."""
    data = _load_glossary(unit_number=unit_number, module_number=module_number)
    return data.tool_descriptions if data else {}


def load_specs_for_lesson(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Main entry point for the pipeline formatting step.

    Processes each section individually to infer workspace_specs (toys + tools),
    then loads spec markdown files for all matched toy types.

    Phrase → canonical name matching is driven by glossary.md (Common spec phrases
    + Spec aliases tables). Phrases that can't be matched to any spec file are
    tracked in workspace_specs["unresolved"] for the downstream drift checker.

    Args:
        input_data: Parsed structured_spec.json (list of section dicts)
        unit_number: Unit number for locating toy_specs directory and glossary.md
        module_number: Module number for locating glossary.md
        verbose: Enable verbose logging

    Returns:
        List of sections, each with workspace_specs (toys, tools, and optionally unresolved)
    """
    if unit_number is not None:
        toy_specs_dir = project_root / "units" / f"unit{unit_number}" / "toy_specs"
    else:
        toy_specs_dir = project_root / "units" / "toy_specs"

    if not toy_specs_dir.exists():
        if verbose:
            print(f"  [WARN] toy_specs directory not found: {toy_specs_dir}")
        return {"toy_specs": {}, "sections": input_data}

    available = {p.stem for p in toy_specs_dir.glob("*.md")}
    if verbose:
        print(f"  [TOY_SPEC_LOADER] Available specs: {sorted(available)}")

    glossary = _load_glossary(unit_number=unit_number, module_number=module_number)
    phrase_map = glossary.full_alias_map if glossary else {}
    tool_descriptions = glossary.tool_descriptions if glossary else {}
    if verbose:
        print(f"  [TOY_SPEC_LOADER] Loaded {len(phrase_map)} phrase mappings from glossary")
        print(f"  [TOY_SPEC_LOADER] Loaded {len(tool_descriptions)} tool descriptions for AI inference")

    if isinstance(input_data, str):
        import json as _json
        try:
            input_data = _json.loads(input_data)
        except Exception:
            raise ValueError(
                "toy_spec_loader received raw text instead of parsed JSON. "
                "Step 1 (starterpack_parser) likely produced malformed JSON — rerun from step 1."
            )
    sections = input_data if isinstance(input_data, list) else input_data.get("sections", [])

    # Lazy-load excerpts only if AI fallback is needed
    excerpts_cache = {}

    def get_excerpts():
        if not excerpts_cache:
            excerpts_cache.update(_load_excerpts(toy_specs_dir))
        return excerpts_cache

    for section in sections:
        section_id = section.get("id", "?")

        # Already has workspace_specs — preserve and skip inference
        if section.get("workspace_specs"):
            if verbose:
                print(f"  [{section_id}] Using existing workspace_specs")
            continue

        toys, unresolved = _match_section_toys(
            section, available, get_excerpts(), phrase_map, verbose=verbose
        )
        tools = _infer_tools(section, tool_descriptions=tool_descriptions)
        tool_fallback = "__fallback__" in tools
        tools = [t for t in tools if t != "__fallback__"]

        toy_names = [t["type"] for t in toys]
        workspace_specs = {"toys": toy_names, "tools": tools}
        if tool_fallback:
            workspace_specs["tool_inferred_by_fallback"] = True

        if unresolved:
            workspace_specs["unresolved"] = unresolved

        if _detect_carry_over(section):
            workspace_specs["workspace_carry_over"] = True
            if verbose:
                print(f"  [{section_id}] ⚠ carry-over detected")

        section["workspace_specs"] = workspace_specs

        if verbose:
            toys_str = f"toys={toy_names}"
            unresolved_str = f"  unresolved={unresolved}" if unresolved else ""
            print(f"  [{section_id}] {toys_str}  tools={tools}{unresolved_str}")

    return sections
