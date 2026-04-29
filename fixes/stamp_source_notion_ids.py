"""One-off fix: stamp _notion_block_id onto pipeline source JSONs by fetching blocks live.

Use this for tracked_scripts directories that have been stitched from outputs/ but
never pulled — they have no notion_blocks.json so stamp_notion_block_ids.py can't help.

Fetches Notion blocks for each pipeline, stamps _notion_block_id onto the best source
JSON (_find_source_json logic), and writes it back in place. Does NOT create a pull.json.

Usage:
    python fixes/stamp_source_notion_ids.py [--dry-run]
    python fixes/stamp_source_notion_ids.py --unit u1 --module 4
    python fixes/stamp_source_notion_ids.py --module 4 --module 7
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

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from utils.notion import (  # noqa: E402
    _tag_sections_from_blocks,
    get_notion_client,
    is_configured,
    load_registry,
)

TRACKED_DIR = project_root / "tracked_scripts"
_PIPELINE_RE = re.compile(
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
)
_SKIP_FILES = {"notion_blocks.json", "notion_push_log.json"}


def _parse_registry_key(key: str) -> tuple[str, str, str] | None:
    parts = key.split("/")
    if len(parts) < 3 or parts[0] != "outputs":
        return None
    unit = parts[1]
    m = _PIPELINE_RE.match(parts[2])
    if not m:
        return None
    type_map = {"lesson": "lesson", "warmup": "warmup", "exitcheck": "exitcheck", "synthesis": "synthesis"}
    return unit, type_map[m.group(1)], m.group(2)


def _find_source_json(tracked_dir: Path) -> Path | None:
    """Find the best stampable source — prefers pipeline step over pull."""
    step_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )
    for step_dir in reversed(step_dirs):
        if re.match(r"^step_\d+_(pull|push)$", step_dir.name):
            continue
        candidates = [
            f for f in step_dir.glob("*.json")
            if f.name not in _SKIP_FILES and "flag" not in f.name
        ]
        for f in candidates:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(data, list) or (
                    isinstance(data, dict) and isinstance(data.get("sections"), list)
                ):
                    return f
            except Exception:
                pass
    return None


def _count_beats(sections: list, stamped_only: bool = False) -> Counter:
    counts: Counter = Counter()
    for section in sections:
        beats = section.get("beats", [])
        for step in section.get("steps", []):
            beats = beats + (step if isinstance(step, list) else [step])
        for beat in beats:
            btype = beat.get("type", "?")
            if not stamped_only or "_notion_block_id" in beat:
                counts[btype] += 1
    return counts


def _all_blocks_from_notion(client, page_id: str) -> list[dict]:
    from utils.notion import _all_blocks
    return _all_blocks(client, page_id, recursive=True)


def _stamp_tracked_dir(tracked_dir: Path, page_id: str, client, dry_run: bool) -> str:
    source = _find_source_json(tracked_dir)
    if not source:
        return "SKIP  no source JSON found"

    data = json.loads(source.read_text(encoding="utf-8"))
    sections = data if isinstance(data, list) else data.get("sections", [])

    before_stamped = _count_beats(sections, stamped_only=True)
    before_total = _count_beats(sections)

    try:
        blocks = _all_blocks_from_notion(client, page_id)
    except Exception as e:
        return f"ERROR fetching blocks: {e}"

    stamped_sections = copy.deepcopy(sections)
    _tag_sections_from_blocks(stamped_sections, blocks)

    after_stamped = _count_beats(stamped_sections, stamped_only=True)

    changes = []
    for btype in sorted(before_total):
        total = before_total[btype]
        b = before_stamped[btype]
        a = after_stamped[btype]
        if a != b:
            changes.append(f"{btype}: {b}→{a}/{total}")
        elif b < total:
            changes.append(f"{btype}: {b}/{total} (unchanged, still missing)")

    if not changes:
        return "OK    no changes needed"

    if not dry_run:
        if isinstance(data, list):
            out = stamped_sections
        else:
            out = {**data, "sections": stamped_sections}
        source.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        # Also save notion_blocks.json into the push step dir for future use
        push_dirs = [
            d for d in tracked_dir.iterdir()
            if d.is_dir() and re.match(r"^step_\d+_push$", d.name)
        ]
        if push_dirs:
            blocks_path = sorted(push_dirs)[-1] / "notion_blocks.json"
            blocks_path.write_text(json.dumps(blocks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    rel = source.relative_to(project_root)
    prefix = "DRY   " if dry_run else "OK    "
    return prefix + f"{rel.parent.name}/{rel.name}  " + ", ".join(changes)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unit", default="u1", help="e.g. u1")
    parser.add_argument("--module", action="append", dest="modules", metavar="N", help="Module number(s), repeatable")
    args = parser.parse_args()

    if not is_configured():
        print("[ERROR] NOTION_API_KEY or NOTION_PARENT_PAGE_ID not set in .env")
        sys.exit(1)

    registry = load_registry()
    client = get_notion_client()

    # Build (unit_short, module_num, script_type) → page_id from registry,
    # keeping only the most-recently-pushed entry per slot.
    slot_map: dict[tuple, tuple[str, str]] = {}  # slot → (page_id, pushed_at)
    for key, entry in registry.items():
        parsed = _parse_registry_key(key)
        if not parsed:
            continue
        unit, script_type, module_num = parsed
        unit_short = re.sub(r"^unit(\d+)$", r"u\1", unit)
        slot = (unit_short, module_num, script_type)
        existing = slot_map.get(slot)
        pushed_at = entry.get("pushed_at", "")
        if existing is None or pushed_at > existing[1]:
            slot_map[slot] = (entry["page_id"], pushed_at)

    # Filter to requested unit/modules
    target_modules = set(args.modules) if args.modules else None

    for slot, (page_id, _) in sorted(slot_map.items()):
        unit_short, module_num, script_type = slot
        if unit_short != args.unit:
            continue
        if target_modules and module_num not in target_modules:
            continue

        tracked_dir = TRACKED_DIR / unit_short / f"m{module_num}" / script_type
        if not tracked_dir.exists():
            print(f"SKIP  {unit_short}/m{module_num}/{script_type} (not in tracked_scripts)")
            continue

        result = _stamp_tracked_dir(tracked_dir, page_id, client, dry_run=args.dry_run)
        print(f"{unit_short}/m{module_num}/{script_type}  {result}")


if __name__ == "__main__":
    main()
