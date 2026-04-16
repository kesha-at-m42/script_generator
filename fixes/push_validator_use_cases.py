"""
push_validator_use_cases.py - Push 1-2 real example sections per validator use case to Notion.

For each use case in docs/references/validator_use_cases.md, renders the doc context
(tool, conditions, design note) as a toggle, then shows 1-2 matching example sections
from the unit's merge_remediation.json files.

Usage:
    python fixes/push_validator_use_cases.py [--unit N]

    --unit N : unit number to scan (default: 1)
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Callable

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from core.path_manager import get_project_paths  # noqa: E402
from core.version_manager import get_latest_version  # noqa: E402
from utils.notion import _divider, _heading, _render_main_section, get_page_url, push_blocks_to_notion  # noqa: E402

_REGISTRY_STUB = project_root / "review" / "validator_use_cases_unit{unit}.json"
_DOC_PATH = project_root / "docs" / "references" / "validator_use_cases.md"

EXAMPLES_PER_USE_CASE = 1


# ---------------------------------------------------------------------------
# Inline markdown → Notion rich_text spans (for doc context rendering)
# ---------------------------------------------------------------------------

def _parse_inline(text: str) -> list[dict]:
    """Convert **bold** and `code` to Notion rich_text spans."""
    spans: list[dict] = []
    i = 0
    while i < len(text):
        if text[i : i + 2] == "**":
            end = text.find("**", i + 2)
            if end != -1:
                spans.append(
                    {"type": "text", "text": {"content": text[i + 2 : end]}, "annotations": {"bold": True}}
                )
                i = end + 2
                continue
        if text[i] == "`":
            end = text.find("`", i + 1)
            if end != -1:
                spans.append(
                    {"type": "text", "text": {"content": text[i + 1 : end]}, "annotations": {"code": True}}
                )
                i = end + 1
                continue
        j = i
        while j < len(text) and text[j : j + 2] != "**" and text[j] != "`":
            j += 1
        if j > i:
            spans.append({"type": "text", "text": {"content": text[i:j]}})
        i = j
    return spans or [{"type": "text", "text": {"content": text}}]


def _para(text: str) -> dict:
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": _parse_inline(text)}}


def _bull(text: str) -> dict:
    return {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": _parse_inline(text)}}


def _callout(spans: list[dict], emoji: str = "📋") -> dict:
    return {
        "object": "block",
        "type": "callout",
        "callout": {"rich_text": spans, "icon": {"type": "emoji", "emoji": emoji}},
    }


def _toggle(summary: str, children: list[dict]) -> dict:
    return {
        "object": "block",
        "type": "toggle",
        "toggle": {"rich_text": _parse_inline(summary), "children": children or [_para("—")]},
    }


# ---------------------------------------------------------------------------
# Doc context parser
# ---------------------------------------------------------------------------

def _body_to_blocks(lines: list[str]) -> list[dict]:
    """Convert body lines from a use-case section in the doc to Notion blocks."""
    blocks: list[dict] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()

        if s.startswith("> "):
            parts: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                parts.append(lines[i].strip()[2:])
                i += 1
            blocks.append(_callout(_parse_inline("  ".join(parts)), emoji="📋"))
            continue

        if s.startswith("- "):
            blocks.append(_bull(s[2:]))
            i += 1
            continue

        if not s:
            i += 1
            continue

        blocks.append(_para(s))
        i += 1

    return blocks


def load_doc_context() -> dict[str, list[dict]]:
    """
    Parse validator_use_cases.md and return a mapping of
    use case label → list of Notion blocks for the body of that section.
    """
    if not _DOC_PATH.exists():
        print(f"[WARN] Doc not found: {_DOC_PATH}")
        return {}

    text = _DOC_PATH.read_text(encoding="utf-8")
    chunks = re.split(r"\n---\n", text)

    context: dict[str, list[dict]] = {}
    for chunk in chunks:
        lines = chunk.strip().splitlines()
        if not lines:
            continue
        first = lines[0].strip()
        if not first.startswith("## Use Case "):
            continue
        label = first[3:]  # strip "## "
        context[label] = _body_to_blocks(lines[1:])

    return context


# ---------------------------------------------------------------------------
# Validator condition matchers
# ---------------------------------------------------------------------------

def _correct_cond(validator: list[dict]) -> dict:
    for b in validator:
        if b.get("is_correct"):
            return b.get("condition", {})
    return {}


def _wrong_branches(validator: list[dict]) -> list[dict]:
    return [b for b in validator if not b.get("is_correct") and b.get("condition") != {}]


def _is_uc1(validator: list[dict]) -> bool:
    wrong = _wrong_branches(validator)
    return sum(1 for b in wrong if "selected" in b.get("condition", {})) >= 2


def _is_uc2(validator: list[dict]) -> bool:
    if "selected" not in _correct_cond(validator):
        return False
    wrong = _wrong_branches(validator)
    if not wrong:
        return False
    return all("incorrect_count" in b.get("condition", {}) for b in wrong) and not _is_uc1(validator)


def _is_uc3(validator: list[dict]) -> bool:
    if "selected" not in _correct_cond(validator):
        return False
    return len(_wrong_branches(validator)) == 0


def _is_uc4(validator: list[dict]) -> bool:
    c = _correct_cond(validator)
    return "category" in c and "symbols_placed" in c


def _is_uc5(validator: list[dict]) -> bool:
    c = _correct_cond(validator)
    if "and" not in c:
        return False
    return any("category" in item and "symbols" in item for item in c["and"])


def _is_uc6(validator: list[dict]) -> bool:
    return "placed" in _correct_cond(validator)


def _is_uc7(validator: list[dict]) -> bool:
    c = _correct_cond(validator)
    if "and" not in c:
        return False
    items = c["and"]
    return any("selected" in item for item in items) and any("not" in item for item in items)


def _is_uc8(validator: list[dict]) -> bool:
    c = _correct_cond(validator)
    return "container_count" in c or "items_per_container" in c


USE_CASES: list[tuple[str, Callable[[list[dict]], bool]]] = [
    ("Use Case 1 — Single-select: pick the right answer", _is_uc1),
    ("Use Case 2 — Click to identify: tap a category or bar", _is_uc2),
    ("Use Case 3 — Click a structural part: no remediation", _is_uc3),
    ("Use Case 4 — Place symbols: build a picture graph row", _is_uc4),
    ("Use Case 5 — Set bar heights: build a bar graph", _is_uc5),
    ("Use Case 6 — Place a tile: fill an equation", _is_uc6),
    ("Use Case 7 — Select all that apply: multi-select", _is_uc7),
    ("Use Case 8 — Build equal groups: set containers and items", _is_uc8),
]


# ---------------------------------------------------------------------------
# Section scanning helpers
# ---------------------------------------------------------------------------

def _flatten_branch_steps(branch: dict) -> dict:
    """Flatten steps → beats inside a single validator branch."""
    if "beats" not in branch and "steps" in branch:
        flat = [b for step_group in branch["steps"] for b in step_group]
        return {**branch, "beats": flat}
    return branch


def _flatten_steps(section: dict) -> dict:
    """Flatten steps → beats at the section level and inside every validator branch.

    merge_remediation sections (and their validator branches) use `steps` (list of
    lists) but the notion rendering layer reads the flat `beats` key.
    """
    result = dict(section)

    # Section-level steps → beats
    if "beats" not in result and "steps" in result:
        result["beats"] = [b for step_group in result["steps"] for b in step_group]

    # Validator branch steps → beats
    fixed_beats = []
    for beat in result.get("beats", []):
        if beat.get("type") == "prompt" and "validator" in beat:
            beat = {
                **beat,
                "validator": [_flatten_branch_steps(br) for br in beat["validator"]],
            }
        fixed_beats.append(beat)
    result["beats"] = fixed_beats

    return result


def _section_matches(section: dict, matcher: Callable[[list[dict]], bool]) -> bool:
    # sections from older pipelines use steps (list of lists)
    for step_group in section.get("steps", []):
        for beat in step_group:
            if beat.get("type") == "prompt" and "validator" in beat:
                if matcher(beat["validator"]):
                    return True
    # dialogue_pass pipelines use a flat beats list
    for beat in section.get("beats", []):
        if beat.get("type") == "prompt" and "validator" in beat:
            if matcher(beat["validator"]):
                return True
    return False


def _find_latest_merge_remediation(pipeline_dir: Path) -> Path | None:
    """Return merge_remediation.json from the latest version, regardless of step number."""
    latest = get_latest_version(pipeline_dir)
    if not latest:
        return None
    version_dir = pipeline_dir / latest
    matches = sorted(version_dir.glob("step_*_merge_remediation/merge_remediation.json"))
    return matches[-1] if matches else None


def _pipeline_label(name: str) -> str:
    m = re.match(r"(.+?)_module_(\d+)(?:_path_([abc]))?$", name)
    if not m:
        return name.replace("_", " ").title()
    base = m.group(1).replace("_", " ").title()
    mod = m.group(2)
    path = f" Path {m.group(3).upper()}" if m.group(3) else ""
    return f"{base} — Module {mod}{path}"


# ---------------------------------------------------------------------------
# Main collection
# ---------------------------------------------------------------------------

def collect_blocks_for_unit(unit_number: int) -> list[dict]:
    out_base = get_project_paths()["outputs"] / f"unit{unit_number}"
    if not out_base.exists():
        print(f"Error: outputs directory not found: {out_base}")
        sys.exit(1)

    doc_context = load_doc_context()

    # Load all sections from all pipelines once
    all_sections: list[tuple[str, str, dict]] = []
    for pipeline_dir in sorted(out_base.iterdir()):
        if not pipeline_dir.is_dir():
            continue
        if not re.match(r".+_module_\d+", pipeline_dir.name):
            continue
        merge_path = _find_latest_merge_remediation(pipeline_dir)
        if not merge_path:
            continue
        try:
            data = json.loads(merge_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  [WARN] Could not read {merge_path}: {e}")
            continue
        sections = data if isinstance(data, list) else data.get("sections", [])
        label = _pipeline_label(pipeline_dir.name)
        ver = get_latest_version(pipeline_dir) or ""
        for section in sections:
            all_sections.append((label, ver, section))

    print(f"Loaded {len(all_sections)} sections across all pipelines.\n")

    all_blocks: list[dict] = []
    found_any = False

    for use_case_label, matcher in USE_CASES:
        matches = [
            (label, ver, section)
            for label, ver, section in all_sections
            if _section_matches(section, matcher)
        ]

        if not matches:
            print(f"  {use_case_label}  — no examples found")
            continue

        examples = matches[:EXAMPLES_PER_USE_CASE]
        print(f"  {use_case_label}  — showing {len(examples)} of {len(matches)} match(es)")
        found_any = True

        all_blocks.append(_divider())
        all_blocks.append(_heading(1, use_case_label))

        # Doc context inline
        all_blocks.extend(doc_context.get(use_case_label, []))

        # Example sections from pipelines
        for _, _, section in examples:
            all_blocks.extend(_render_main_section(_flatten_steps(section)))

    if not found_any:
        print("No matching sections found for any use case.")
        sys.exit(0)

    return all_blocks


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Push validator use case example sections to a Notion review page"
    )
    parser.add_argument("--unit", type=int, default=1, help="Unit number (default: 1)")
    args = parser.parse_args()

    title = f"Validator Use Cases — Unit {args.unit}"
    registry_path = Path(str(_REGISTRY_STUB).format(unit=args.unit))

    print(f"\nCollecting validator use case examples for unit {args.unit}...\n")
    blocks = collect_blocks_for_unit(args.unit)

    print(f'\nPushing to Notion: "{title}"...')
    page_id = push_blocks_to_notion(blocks, title=title, file_path=registry_path)

    url = get_page_url(page_id)
    print(f"\nDone. Page: {url}")


if __name__ == "__main__":
    main()
