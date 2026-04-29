"""One-off fix: stamp _notion_block_id onto all beats in tracked_scripts pull.json files.

Tracked scripts that were pushed/pulled before the _tag_section bug fix have scene beats
(and any dialogue beats edited in Notion) missing _notion_block_id. This script uses the
already-saved notion_blocks.json in each pull step to re-stamp all beats without any
Notion API call.

Usage:
    python fixes/stamp_notion_block_ids.py [--dry-run]
    python fixes/stamp_notion_block_ids.py --unit u1 --module 3
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import Counter
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.notion import _tag_sections_from_blocks  # noqa: E402


TRACKED_DIR = project_root / "tracked_scripts"


def _count_stamped(sections: list) -> Counter:
    counts: Counter = Counter()
    for section in sections:
        for beat in section.get("beats", []):
            btype = beat.get("type", "?")
            counts[f"{btype}_total"] += 1
            if "_notion_block_id" in beat:
                counts[f"{btype}_stamped"] += 1
    return counts


def _stamp_pull_dir(pull_dir: Path, dry_run: bool) -> str:
    pull_file = pull_dir / "pull.json"
    blocks_file = pull_dir / "notion_blocks.json"

    if not pull_file.exists():
        return "SKIP  pull.json missing"
    if not blocks_file.exists():
        return "SKIP  notion_blocks.json missing"

    sections = json.loads(pull_file.read_text(encoding="utf-8"))
    if not isinstance(sections, list):
        return "SKIP  pull.json is not a list"

    blocks = json.loads(blocks_file.read_text(encoding="utf-8"))

    before = _count_stamped(sections)

    stamped = copy.deepcopy(sections)
    _tag_sections_from_blocks(stamped, blocks)

    after = _count_stamped(stamped)

    beat_types = {k.split("_")[0] for k in before if k.endswith("_total")}
    changes = []
    for btype in sorted(beat_types):
        b_total = before[f"{btype}_total"]
        b_stamped = before[f"{btype}_stamped"]
        a_stamped = after[f"{btype}_stamped"]
        if a_stamped != b_stamped:
            changes.append(f"{btype}: {b_stamped}→{a_stamped}/{b_total}")
        elif b_stamped < b_total:
            changes.append(f"{btype}: {b_stamped}/{b_total} (unchanged, still missing)")

    if not changes:
        return "OK    no changes needed"

    if not dry_run:
        pull_file.write_text(
            json.dumps(stamped, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    prefix = "DRY   " if dry_run else "OK    "
    return prefix + ", ".join(changes)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unit", help="e.g. u1")
    parser.add_argument("--module", help="e.g. 3")
    args = parser.parse_args()

    pull_dirs = sorted(TRACKED_DIR.rglob("step_*_pull"))

    if args.unit or args.module:
        filtered = []
        for d in pull_dirs:
            parts = d.parts
            unit_idx = next((i for i, p in enumerate(parts) if re.match(r"^u\d+$", p)), None)
            mod_idx = next((i for i, p in enumerate(parts) if re.match(r"^m\d+$", p)), None)
            if args.unit and (unit_idx is None or parts[unit_idx] != args.unit):
                continue
            if args.module and (mod_idx is None or parts[mod_idx] != f"m{args.module}"):
                continue
            filtered.append(d)
        pull_dirs = filtered

    if not pull_dirs:
        print("No pull directories found.")
        return

    for pull_dir in pull_dirs:
        rel = pull_dir.relative_to(project_root)
        result = _stamp_pull_dir(pull_dir, dry_run=args.dry_run)
        print(f"{rel}  {result}")


if __name__ == "__main__":
    main()
