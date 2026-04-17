"""Sync the latest pipeline output into tracked_scripts/.

Copies the latest version directory for each registered Notion entry into:

    tracked_scripts/{unit}/module_{N}/{script_type}/

preserving the full step folder structure (step_01_..., step_02_..., etc.).
The destination is replaced on every run so it always reflects the latest run.

Optionally pulls from Notion first before copying (--pull flag).

Usage:
    python cli/pull_tracked_scripts.py
    python cli/pull_tracked_scripts.py --pull          # pull from Notion first
    python cli/pull_tracked_scripts.py --unit unit1
    python cli/pull_tracked_scripts.py --module 12
    python cli/pull_tracked_scripts.py --type lesson
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from utils.notion import is_configured, load_registry, pull_lesson, blocks_to_lesson  # noqa: E402

TRACKED_DIR = project_root / "tracked_scripts"

_PIPELINE_RE = re.compile(
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
)
_SCRIPT_TYPE_LABELS = {
    "lesson": "lesson",
    "warmup": "warmup",
    "exitcheck": "exit_check",
    "synthesis": "synthesis",
}
_SKIP_FILES = {"notion_blocks.json", "notion_push_log.json"}


def _parse_registry_key(key: str) -> tuple[str, str, str] | None:
    """Parse a registry key into (unit, script_type, module_number), or None."""
    parts = key.split("/")
    if len(parts) < 3 or parts[0] != "outputs":
        return None
    unit = parts[1]
    pipeline = parts[2]
    m = _PIPELINE_RE.match(pipeline)
    if not m:
        return None
    return unit, _SCRIPT_TYPE_LABELS[m.group(1)], m.group(2)


def _latest_version_dir(key: str, entry: dict) -> Path | None:
    """Return the latest version directory for a registry entry."""
    parts = key.split("/")
    if len(parts) < 3:
        return None
    pipeline_dir = project_root / "/".join(parts[:3])
    if not pipeline_dir.exists():
        return None

    last_version = entry.get("last_version")
    if last_version:
        d = pipeline_dir / last_version
        return d if d.exists() else None

    version_dirs = sorted(
        [d for d in pipeline_dir.iterdir() if d.is_dir() and re.match(r"^v\d+$", d.name)],
        key=lambda d: int(d.name[1:]),
    )
    return version_dirs[-1] if version_dirs else None


def _find_last_step_json(version_dir: Path, skip_pull: bool = False) -> Path | None:
    """Find the main JSON output in the last step of a version directory.

    If skip_pull is True, ignores step_*_pull directories (returns the last
    non-pull pipeline step instead).
    """
    step_dirs = sorted(
        [d for d in version_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )
    for step_dir in reversed(step_dirs):
        if skip_pull and re.match(r"^step_\d+_pull$", step_dir.name):
            continue
        json_files = [f for f in step_dir.glob("*.json") if f.name not in _SKIP_FILES and "flag" not in f.name]
        for f in json_files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(data, list) or (isinstance(data, dict) and isinstance(data.get("sections"), list)):
                    return f
            except Exception:
                pass
    return None


def _notion_pull(version_dir: Path, page_id: str) -> str | None:
    """Pull from Notion into the last step of version_dir. Returns error string or None.

    Also writes a reverse-stamped copy of the pipeline source file (last non-pull step)
    so that future pulls can use ID-based matching instead of LEGACY content matching.
    """
    source = _find_last_step_json(version_dir)
    if not source:
        return "no source JSON found"
    try:
        original = json.loads(source.read_text(encoding="utf-8"))
        patched, _flags, raw_blocks = pull_lesson(page_id, original)
        source.write_text(json.dumps(patched, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        # Reverse-stamp: apply the same Notion blocks to the pipeline source (e.g. step_12)
        # so it gains _notion_block_id on every matched beat without a re-push.
        pipeline_source = _find_last_step_json(version_dir, skip_pull=True)
        if pipeline_source and pipeline_source != source:
            pipeline_original = json.loads(pipeline_source.read_text(encoding="utf-8"))
            pipeline_stamped, _ = blocks_to_lesson(raw_blocks, pipeline_original)
            stamped_path = pipeline_source.parent / (pipeline_source.stem + "_notion_stamped.json")
            stamped_path.write_text(
                json.dumps(pipeline_stamped, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
    except Exception as e:
        return str(e)
    return None


def _sync_entry(key: str, entry: dict, do_pull: bool) -> str:
    """Sync one registry entry. Returns a status string."""
    parsed = _parse_registry_key(key)
    if not parsed:
        return f"SKIP  {key} (not a unit/module pipeline)"

    unit, script_type, module_num = parsed
    version_dir = _latest_version_dir(key, entry)
    if not version_dir:
        return f"SKIP  {key} (no version directory found)"

    if do_pull:
        err = _notion_pull(version_dir, entry["page_id"])
        if err:
            return f"PULL ERROR  {key}: {err}"

    dest = TRACKED_DIR / unit / f"module_{module_num}" / script_type
    if dest.exists():
        shutil.rmtree(dest)

    shutil.copytree(
        version_dir,
        dest,
        ignore=shutil.ignore_patterns(*_SKIP_FILES),
    )

    rel = dest.relative_to(project_root)
    version_note = f" ({version_dir.name})"
    return f"OK    {rel}{version_note}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync latest pipeline outputs into tracked_scripts/"
    )
    parser.add_argument("--pull", action="store_true", help="Pull from Notion before copying")
    parser.add_argument("--unit", help="Filter by unit (e.g. unit1)")
    parser.add_argument("--module", help="Filter by module number (e.g. 12)")
    parser.add_argument("--type", dest="script_type", help="Filter by script type (lesson/warmup/exitcheck/synthesis)")
    args = parser.parse_args()

    if args.pull and not is_configured():
        print("[ERROR] NOTION_API_KEY or NOTION_PARENT_PAGE_ID not set in .env")
        sys.exit(1)

    registry = load_registry()
    entries = list(registry.items())

    if args.unit or args.module or args.script_type:
        filtered = []
        for key, entry in entries:
            parsed = _parse_registry_key(key)
            if not parsed:
                continue
            unit, script_type, module_num = parsed
            if args.unit and unit != args.unit:
                continue
            if args.module and module_num != args.module:
                continue
            if args.script_type and script_type != args.script_type:
                continue
            filtered.append((key, entry))
        entries = filtered

    if not entries:
        print("No matching registry entries.")
        return

    # Deduplicate: for each (unit, script_type, module) keep only the most recently pushed entry
    best: dict[tuple, tuple[str, dict]] = {}
    skipped_keys = []
    for key, entry in entries:
        parsed = _parse_registry_key(key)
        if not parsed:
            skipped_keys.append((key, entry))
            continue
        slot = parsed  # (unit, script_type, module_num)
        existing_key, existing_entry = best.get(slot, (None, {}))
        if existing_key is None or entry.get("pushed_at", "") > existing_entry.get("pushed_at", ""):
            best[slot] = (key, entry)

    deduped = list(best.values())
    total = len(deduped) + len(skipped_keys)
    action = "Pulling from Notion and syncing" if args.pull else "Syncing"
    print(f"{action} {len(deduped)} pipeline(s) into tracked_scripts/... ({total - len(deduped)} skipped as duplicates)\n")

    for key, entry in skipped_keys:
        print(f"SKIP  {key} (not a unit/module pipeline)")
    for key, entry in deduped:
        print(_sync_entry(key, entry, do_pull=args.pull))


if __name__ == "__main__":
    main()
