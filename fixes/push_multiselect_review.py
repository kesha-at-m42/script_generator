"""
push_multiselect_review.py - Push multiselect MC sections to a Notion review page.

Scans all pipelines in a unit for their latest merge_remediation.json, filters
to sections that contain at least one multi_select prompt, and pushes a combined
human-readable script to a single Notion page.

Usage:
    python cli/push_multiselect_review.py [--unit N]

    --unit N : unit number to scan (default: 1)
"""

import argparse
import json
import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.path_manager import get_project_paths  # noqa: E402
from core.version_manager import get_latest_version  # noqa: E402
from utils.notion import _divider, _heading, get_page_url, lesson_to_blocks, push_blocks_to_notion  # noqa: E402

# Registry key path (no real file — used only as a stable key for notion_pages.json)
_REGISTRY_STUB = project_root / "review" / "multiselect_mc_unit{unit}.json"


def _has_multiselect_prompt(section: dict) -> bool:
    """Return True if any beat in the section uses tool=multi_select."""
    for step_beats in section.get("steps", []):
        for beat in step_beats:
            if beat.get("type") == "prompt" and beat.get("tool") == "multi_select":
                return True
    return False


def _filter_multiselect_sections(sections: list) -> list:
    """Return only sections that contain a multi_select prompt."""
    return [s for s in sections if _has_multiselect_prompt(s)]


def _find_latest_merge_remediation(pipeline_dir: Path) -> Path | None:
    """Return the merge_remediation.json from the latest version, or None."""
    latest = get_latest_version(pipeline_dir)
    if not latest:
        return None
    candidate = pipeline_dir / latest / "step_04_merge_remediation" / "merge_remediation.json"
    return candidate if candidate.exists() else None


def _pipeline_label(pipeline_dir_name: str) -> str:
    """Convert e.g. 'lesson_generator_module_5' -> 'Lesson Generator — Module 5'."""
    m = re.match(r"(.+?)_module_(\d+)(?:_path_([abc]))?$", pipeline_dir_name)
    if not m:
        return pipeline_dir_name.replace("_", " ").title()
    base = m.group(1).replace("_", " ").title()
    mod = m.group(2)
    path = f" Path {m.group(3).upper()}" if m.group(3) else ""
    return f"{base} — Module {mod}{path}"


def collect_blocks_for_unit(unit_number: int) -> list[dict]:
    """
    Walk all pipelines in the unit and build Notion blocks for multiselect sections.
    Returns a flat list of Notion block dicts.
    """
    out_base = get_project_paths()["outputs"] / f"unit{unit_number}"
    if not out_base.exists():
        print(f"Error: outputs directory not found: {out_base}")
        sys.exit(1)

    all_blocks: list[dict] = []
    found_any = False

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
        multiselect_sections = _filter_multiselect_sections(sections)
        if not multiselect_sections:
            continue

        label = _pipeline_label(pipeline_dir.name)
        latest_ver = get_latest_version(pipeline_dir)
        print(f"  {label}  ({latest_ver})  — {len(multiselect_sections)} multiselect section(s)")

        all_blocks.append(_divider())
        all_blocks.append(_heading(1, label))
        all_blocks.extend(lesson_to_blocks(multiselect_sections))
        found_any = True

    if not found_any:
        print("No multiselect MC sections found.")
        sys.exit(0)

    return all_blocks


def main():
    parser = argparse.ArgumentParser(
        description="Push multiselect MC sections from all pipelines to a Notion review page"
    )
    parser.add_argument("--unit", type=int, default=1, help="Unit number (default: 1)")
    args = parser.parse_args()

    title = f"Testing Multi select MC questions — Unit {args.unit}"
    registry_path = Path(str(_REGISTRY_STUB).format(unit=args.unit))

    print(f"\nCollecting multiselect MC sections for unit {args.unit}...\n")
    blocks = collect_blocks_for_unit(args.unit)

    print(f'\nPushing to Notion: "{title}"...')
    page_id = push_blocks_to_notion(blocks, title=title, file_path=registry_path)

    url = get_page_url(page_id)
    print(f"\nDone. Page: {url}")


if __name__ == "__main__":
    main()
