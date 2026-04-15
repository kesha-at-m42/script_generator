#!/usr/bin/env python3
"""
fixes/prune_pipeline_sections.py

Remove specified section IDs from all step outputs in a pipeline version directory.

Affects:
  - Main collated JSON files (*.json at step root): removes matching items from arrays
  - Per-section files in items/ and prompts/ subdirs: deletes matching files

Usage:
  python fixes/prune_pipeline_sections.py PIPELINE_VERSION_DIR ID [ID ...]
      [--from-step N]

  --from-step N   only prune steps with number >= N (default: 1)

Example — prune from section_structurer (step 5) onwards only:
  python fixes/prune_pipeline_sections.py \\
      outputs/unit1/lesson_generator_dialogue_pass_module_1/v10 \\
      s3_6_solving_with_selected_data s3_7_two_step_sequential \\
      --from-step 5
"""

import argparse
import json
import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
_STEP_RE = re.compile(r"^step_(\d+)_")
_SKIP_FILES = {"notion_blocks.json"}


def prune_step(step_dir: Path, prune_ids: set[str]) -> None:
    removed_sections = 0
    removed_files = 0

    # Remove from collated JSON arrays
    for json_file in step_dir.glob("*.json"):
        if json_file.name in _SKIP_FILES:
            continue
        data = json.loads(json_file.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue
        filtered = [s for s in data if not (isinstance(s, dict) and s.get("id") in prune_ids)]
        if len(filtered) < len(data):
            removed_sections += len(data) - len(filtered)
            json_file.write_text(json.dumps(filtered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Remove per-section files in subdirs (items/, prompts/, etc.)
    for subdir in step_dir.iterdir():
        if not subdir.is_dir():
            continue
        for f in list(subdir.iterdir()):
            if f.stem in prune_ids:
                f.unlink()
                removed_files += 1

    if removed_sections or removed_files:
        print(f"  {step_dir.name}: -{removed_sections} sections, -{removed_files} files")


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove section IDs from pipeline step outputs")
    parser.add_argument("version_dir", type=Path)
    parser.add_argument("ids", nargs="+", help="Section IDs to prune")
    parser.add_argument("--from-step", type=int, default=1, metavar="N",
                        help="Only prune steps with number >= N (default: 1)")
    args = parser.parse_args()

    version_dir = (project_root / args.version_dir).resolve()
    prune_ids = set(args.ids)

    if not version_dir.exists():
        print(f"ERROR: {version_dir} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Pruning {prune_ids} from {version_dir.relative_to(project_root)} (from step {args.from_step})")

    for step_dir in sorted(version_dir.iterdir(), key=lambda d: d.name):
        if not step_dir.is_dir():
            continue
        m = _STEP_RE.match(step_dir.name)
        if m and int(m.group(1)) >= args.from_step:
            prune_step(step_dir, prune_ids)

    print("Done.")


if __name__ == "__main__":
    main()
