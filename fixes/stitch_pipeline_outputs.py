#!/usr/bin/env python3
"""
fixes/stitch_pipeline_outputs.py

Merge two pipeline version directories into a destination (tracked_scripts).

Algorithm:
  1. BASE PASS — copy the old pipeline's steps that have a matching step in the
     new pipeline (matched by name suffix, e.g. "merge_remediation").
     Each matched step is written to the dest using the NEW pipeline's step
     directory name (so numbering follows the new structure).
     Section IDs in JSON files and per-section filenames are renamed via a
     positional mapping built from the new pipeline's starterpack_parser.

  2. OVERLAY PASS — additively copy every step from the new pipeline on top.
     For matched steps: section objects in the new pipeline overwrite the
     corresponding section in dest (by id); old sections absent from the new
     pipeline are kept as-is.
     For new-pipeline-only steps (no old equivalent): copied straight to dest.

  Old-only steps (no name match in new pipeline) are skipped — dest mirrors
  the new pipeline's step structure.

Parameters:
  OLD_PIPELINE  path to old pipeline version dir, or a tracked_scripts leaf dir
  NEW_PIPELINE  path to new pipeline version dir

  --dest PATH   override destination (default: derived from new pipeline path,
                e.g. tracked_scripts/unit1/module_1/lesson)

Typical invocation for module 1 lesson:
  # First prune sections that should NOT come from the new pipeline:
  python fixes/prune_pipeline_sections.py \\
      outputs/unit1/lesson_generator_dialogue_pass_module_1/v10 \\
      s3_6_solving_with_selected_data s3_7_two_step_sequential

  # Then stitch:
  python fixes/stitch_pipeline_outputs.py \\
      tracked_scripts/unit1/module_1/lesson \\
      outputs/unit1/lesson_generator_dialogue_pass_module_1/v10
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

_SKIP_FILES = {"notion_blocks.json"}
_STEP_RE = re.compile(r"^step_(\d+)_(.+)$")

# Maps old pipeline step name suffixes → new pipeline step name suffixes
# when the two pipelines use different names for equivalent steps.
_STEP_ALIASES: dict[str, str] = {
    "script_generator": "section_structurer",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _resolve_version(path: Path) -> Path:
    """
    Given a path that is either a pipeline directory (containing vN subdirs)
    or already a version directory (containing step_* subdirs), return the
    resolved version directory.
    """
    # Already a version dir if it contains step_* directories
    if any(_STEP_RE.match(d.name) for d in path.iterdir() if d.is_dir()):
        return path
    # Pipeline dir — resolve latest version
    latest_txt = path / "latest.txt"
    if latest_txt.exists():
        v = latest_txt.read_text(encoding="utf-8").strip()
        return path / v
    versions = sorted(
        [d for d in path.iterdir() if d.is_dir() and re.match(r"^v\d+$", d.name)],
        key=lambda d: int(d.name[1:]),
    )
    if not versions:
        raise FileNotFoundError(f"No version directories found in {path}")
    return versions[-1]


def _step_dirs(pipeline: Path, aliases: dict[str, str] | None = None) -> dict[str, Path]:
    """Return {step_name_suffix: step_dir} for all step_NN_* dirs.
    If aliases is provided, old suffix keys are remapped to their alias values."""
    result: dict[str, Path] = {}
    for d in pipeline.iterdir():
        if not d.is_dir():
            continue
        m = _STEP_RE.match(d.name)
        if m:
            suffix = m.group(2)
            if aliases and suffix in aliases:
                suffix = aliases[suffix]
            result[suffix] = d
    return result


def _load_id_map(old_pipeline: Path, new_pipeline: Path) -> dict[str, str]:
    """
    Build {old_section_id: new_section_id} by positionally zipping:
      old  = old pipeline's merge_remediation.json (any step_*_merge_remediation)
      new  = new pipeline's step_02_starterpack_parser/starterpack_parser.json
    """
    # Find old merge_remediation
    old_merge: list[dict] | None = None
    for step_dir in old_pipeline.iterdir():
        if step_dir.is_dir() and "merge_remediation" in step_dir.name:
            f = step_dir / "merge_remediation.json"
            if f.exists():
                old_merge = json.loads(f.read_text(encoding="utf-8"))
                break
    if old_merge is None:
        raise FileNotFoundError(f"No merge_remediation.json found in {old_pipeline}")

    new_starter = new_pipeline / "step_02_starterpack_parser" / "starterpack_parser.json"
    if not new_starter.exists():
        raise FileNotFoundError(f"starterpack_parser.json not found in {new_pipeline}")
    new_sections: list[dict] = json.loads(new_starter.read_text(encoding="utf-8"))

    if len(old_merge) != len(new_sections):
        print(
            f"WARNING: section count mismatch ({len(old_merge)} old vs "
            f"{len(new_sections)} new) — positional mapping may be wrong.",
            file=sys.stderr,
        )

    return {old["id"]: new["id"] for old, new in zip(old_merge, new_sections)}


def _rename_ids_in_json(data: object, id_map: dict[str, str]) -> object:
    """Replace top-level 'id' fields in a list of section dicts."""
    if isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, dict) and item.get("id") in id_map:
                item = {**item, "id": id_map[item["id"]]}
            result.append(item)
        return result
    return data


def _rename_section_files(directory: Path, id_map: dict[str, str]) -> None:
    """Rename per-section files in items/ and prompts/ subdirs."""
    for subdir in directory.iterdir():
        if not subdir.is_dir():
            continue
        for f in list(subdir.iterdir()):
            if f.stem in id_map:
                f.rename(subdir / (id_map[f.stem] + f.suffix))


def _apply_id_renames(step_dir: Path, id_map: dict[str, str]) -> None:
    """Rename all section IDs in a step directory (JSON content + filenames)."""
    for json_file in step_dir.glob("*.json"):
        if json_file.name in _SKIP_FILES:
            continue
        data = json.loads(json_file.read_text(encoding="utf-8"))
        renamed = _rename_ids_in_json(data, id_map)
        if renamed is not data:
            json_file.write_text(
                json.dumps(renamed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
    _rename_section_files(step_dir, id_map)


def _merge_json_arrays(dest_data: list, new_data: list) -> list:
    """
    Merge two lists of section dicts by id.
    New pipeline sections overwrite matching dest sections in-place;
    new pipeline sections not found in dest are appended.
    """
    new_by_id = {s["id"]: s for s in new_data if isinstance(s, dict) and "id" in s}
    result = []
    for item in dest_data:
        sid = item.get("id") if isinstance(item, dict) else None
        result.append(new_by_id.pop(sid, item))
    result.extend(new_by_id.values())
    return result


def _overlay_step(dest_step: Path, new_step: Path) -> None:
    """Overlay new pipeline step onto dest step (additive by section id)."""
    # Merge main collated JSON files
    for new_json in new_step.glob("*.json"):
        if new_json.name in _SKIP_FILES:
            continue
        dest_json = dest_step / new_json.name
        new_data = json.loads(new_json.read_text(encoding="utf-8"))
        if dest_json.exists() and isinstance(new_data, list):
            dest_data = json.loads(dest_json.read_text(encoding="utf-8"))
            if isinstance(dest_data, list):
                new_data = _merge_json_arrays(dest_data, new_data)
        dest_json.write_text(
            json.dumps(new_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    # Copy per-section files (items/, prompts/) — overwrite if present
    for subdir in new_step.iterdir():
        if not subdir.is_dir():
            continue
        dest_subdir = dest_step / subdir.name
        dest_subdir.mkdir(exist_ok=True)
        for f in subdir.iterdir():
            shutil.copy2(f, dest_subdir / f.name)

    # Copy any other non-JSON files (prompt.md, flags, etc.)
    # JSON files are already handled by the merge loop above — don't overwrite.
    for f in new_step.iterdir():
        if f.is_file() and f.name not in _SKIP_FILES and not f.name.endswith(".json"):
            shutil.copy2(f, dest_step / f.name)


def _derive_dest(new_pipeline: Path) -> Path | None:
    """Derive tracked_scripts destination from new pipeline path structure."""
    # Expect: .../outputs/{unit}/{pipeline_name}_module_{N}/v{K}
    _PIPELINE_RE = re.compile(
        r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
    )
    _TYPE_MAP = {"lesson": "lesson", "warmup": "warmup", "exitcheck": "exit_check", "synthesis": "synthesis"}
    pipeline_dir = new_pipeline.parent
    m = _PIPELINE_RE.match(pipeline_dir.name)
    if not m:
        return None
    unit_dir = pipeline_dir.parent
    unit = unit_dir.name
    script_type = _TYPE_MAP[m.group(1)]
    module_num = m.group(2)
    return project_root / "tracked_scripts" / unit / f"module_{module_num}" / script_type


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge old + new pipeline outputs into tracked_scripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("old_pipeline", type=Path, help="Old pipeline version dir or tracked_scripts leaf")
    parser.add_argument("new_pipeline", type=Path, help="New pipeline version dir")
    parser.add_argument("--dest", type=Path, default=None, help="Destination directory (default: auto-derived)")
    args = parser.parse_args()

    old_pipeline = (project_root / args.old_pipeline).resolve()
    new_pipeline = (project_root / args.new_pipeline).resolve()

    if not old_pipeline.exists():
        print(f"ERROR: old pipeline not found: {old_pipeline}", file=sys.stderr)
        sys.exit(1)
    if not new_pipeline.exists():
        print(f"ERROR: new pipeline not found: {new_pipeline}", file=sys.stderr)
        sys.exit(1)

    old_pipeline = _resolve_version(old_pipeline)
    new_pipeline = _resolve_version(new_pipeline)

    dest = args.dest
    if dest is None:
        dest = _derive_dest(new_pipeline)
    if dest is None:
        print("ERROR: could not derive destination; use --dest", file=sys.stderr)
        sys.exit(1)
    dest = (project_root / dest).resolve()

    print(f"Old pipeline : {old_pipeline.relative_to(project_root)}")
    print(f"New pipeline : {new_pipeline.relative_to(project_root)}")
    print(f"Destination  : {dest.relative_to(project_root)}")
    print()

    # Build section ID map (old_id → new_id)
    id_map = _load_id_map(old_pipeline, new_pipeline)
    print(f"ID map: {len(id_map)} sections")

    old_steps = _step_dirs(old_pipeline, aliases=_STEP_ALIASES)
    new_steps = _step_dirs(new_pipeline)

    matched_suffixes = set(old_steps) & set(new_steps)
    new_only_suffixes = set(new_steps) - set(old_steps)
    old_only_suffixes = set(old_steps) - set(new_steps)

    print(f"Steps matched (base+overlay): {sorted(matched_suffixes)}")
    print(f"Steps new-only (copy as-is) : {sorted(new_only_suffixes)}")
    print(f"Steps old-only (skipped)    : {sorted(old_only_suffixes)}")
    print()

    # Work from a temp copy of old pipeline so dest can equal old_pipeline path
    with tempfile.TemporaryDirectory() as tmp:
        tmp_old = Path(tmp) / "old"
        shutil.copytree(old_pipeline, tmp_old, ignore=shutil.ignore_patterns(*_SKIP_FILES))
        old_steps_tmp = _step_dirs(tmp_old, aliases=_STEP_ALIASES)

        # Clear and recreate dest
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)

        # --- BASE PASS: matched steps from old pipeline ---
        for suffix in matched_suffixes:
            new_step_dir = new_steps[suffix]        # authoritative name/number
            old_step_tmp = old_steps_tmp[suffix]
            dest_step = dest / new_step_dir.name    # use new pipeline's step name

            shutil.copytree(old_step_tmp, dest_step)
            _apply_id_renames(dest_step, id_map)

            # If this step was aliased (e.g. script_generator → section_structurer),
            # rename the main JSON file so the overlay can find and merge it.
            old_suffix = _STEP_RE.match(old_step_tmp.name).group(2)
            if old_suffix != suffix:
                old_json = dest_step / f"{old_suffix}.json"
                new_json = dest_step / f"{suffix}.json"
                if old_json.exists() and not new_json.exists():
                    old_json.rename(new_json)

            print(f"  [BASE]    {new_step_dir.name}  (from old '{old_step_tmp.name}')")

        # --- OVERLAY PASS: new pipeline steps ---
        for suffix in sorted(new_steps, key=lambda s: int(_STEP_RE.match(new_steps[s].name).group(1))):
            new_step_dir = new_steps[suffix]
            dest_step = dest / new_step_dir.name

            if suffix in matched_suffixes:
                # Merge on top of base
                _overlay_step(dest_step, new_step_dir)
                print(f"  [OVERLAY] {new_step_dir.name}")
            else:
                # New-only: copy as-is
                shutil.copytree(new_step_dir, dest_step, ignore=shutil.ignore_patterns(*_SKIP_FILES))
                print(f"  [NEW]     {new_step_dir.name}")

    # Copy top-level metadata from new pipeline
    for fname in ("metadata.json", "console.txt"):
        src = new_pipeline / fname
        if src.exists():
            shutil.copy2(src, dest / fname)

    print(f"\nDone. {dest.relative_to(project_root)} updated.")


if __name__ == "__main__":
    main()
