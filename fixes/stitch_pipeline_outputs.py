"""Stitch pipeline version directories into tracked_scripts/.

Two modes:

  NEW MODE — additive merge of one or more versions (same section IDs):
    python fixes/stitch_pipeline_outputs.py --unit unit1 --module 12 --type warmup --versions v0 v11
    python fixes/stitch_pipeline_outputs.py --unit unit1 --module 12   # latest version, all types

  LEGACY MODE — merge old pipeline (different section IDs) into new pipeline structure.
    Positionally maps old section IDs → new, then merges content.
    Can be removed once module 1 and 2 ingestion is complete.

    python fixes/stitch_pipeline_outputs.py old_pipeline new_pipeline [--dest PATH]

    Typical invocation:
      python fixes/prune_pipeline_sections.py \\
          outputs/unit1/lesson_generator_dialogue_pass_module_1/v10 \\
          s3_6_solving_with_selected_data s3_7_two_step_sequential

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

OUTPUTS_DIR = project_root / "outputs"
TRACKED_DIR = project_root / "tracked_scripts"

_PIPELINE_RE = re.compile(
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
)
_STEP_RE = re.compile(r"^step_(\d+)_(.+)$")
_SCRIPT_TYPES = ("lesson", "warmup", "exitcheck", "synthesis")
_SKIP_FILES = {"notion_blocks.json", "notion_push_log.json"}


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _get_sections(data) -> tuple[list | None, str]:
    if isinstance(data, list):
        return data, "list"
    if isinstance(data, dict) and isinstance(data.get("sections"), list):
        return data["sections"], "dict"
    return None, ""


def _merge_sections(base: list, overlay: list) -> list:
    """Merge overlay sections into base by ID. New IDs appended."""
    if not overlay:
        return base
    overlay_by_id = {s.get("id"): s for s in overlay if isinstance(s, dict)}
    result = []
    for item in base:
        sid = item.get("id") if isinstance(item, dict) else None
        result.append(overlay_by_id.pop(sid, item) if sid else item)
    result.extend(overlay_by_id.values())
    return result


# ---------------------------------------------------------------------------
# New mode
# ---------------------------------------------------------------------------


def _find_pipeline_dir(unit: str, module: str, script_type: str) -> Path | None:
    unit_dir = OUTPUTS_DIR / unit
    if not unit_dir.exists():
        return None
    for d in unit_dir.iterdir():
        m = _PIPELINE_RE.match(d.name)
        if m and m.group(1) == script_type and m.group(2) == module:
            return d
    return None


def _latest_version(pipeline_dir: Path) -> str | None:
    versions = sorted(
        [d for d in pipeline_dir.iterdir() if d.is_dir() and re.match(r"^v\d+$", d.name)],
        key=lambda d: int(d.name[1:]),
    )
    return versions[-1].name if versions else None


def _merge_step(dest_step: Path, src_step: Path) -> None:
    for f in src_step.iterdir():
        if not f.is_file() or f.name in _SKIP_FILES:
            continue
        dest_f = dest_step / f.name
        if f.suffix == ".json":
            try:
                src_data = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                shutil.copy2(f, dest_f)
                continue
            src_secs, _ = _get_sections(src_data)
            if src_secs is not None and dest_f.exists():
                try:
                    dest_data = json.loads(dest_f.read_text(encoding="utf-8"))
                    dest_secs, dest_shape = _get_sections(dest_data)
                    if dest_secs is not None:
                        merged = _merge_sections(dest_secs, src_secs)
                        out = merged if dest_shape == "list" else {**dest_data, "sections": merged}
                        dest_f.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                        continue
                except Exception:
                    pass
            dest_f.write_text(json.dumps(src_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        else:
            shutil.copy2(f, dest_f)

    for subdir in src_step.iterdir():
        if not subdir.is_dir():
            continue
        dest_subdir = dest_step / subdir.name
        dest_subdir.mkdir(exist_ok=True)
        for f in subdir.iterdir():
            if f.is_file():
                shutil.copy2(f, dest_subdir / f.name)


def _stitch(pipeline_dir: Path, versions: list[str], dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)

    for i, ver in enumerate(versions):
        src = pipeline_dir / ver
        if not src.exists():
            print(f"  [SKIP] {ver} — not found in {pipeline_dir.relative_to(project_root)}")
            continue
        if i == 0:
            shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*_SKIP_FILES))
            print(f"  [BASE]    {ver}")
        else:
            for step_dir in sorted(src.iterdir()):
                if not step_dir.is_dir() or not _STEP_RE.match(step_dir.name):
                    continue
                dest_step = dest / step_dir.name
                dest_step.mkdir(exist_ok=True)
                _merge_step(dest_step, step_dir)
            for fname in ("metadata.json", "console.txt"):
                f = src / fname
                if f.exists():
                    shutil.copy2(f, dest / fname)
            print(f"  [OVERLAY] {ver}")

    for step_dir in sorted(dest.glob("step_*")):
        for f in step_dir.glob("*.json"):
            if f.name in _SKIP_FILES or "flag" in f.name:
                continue
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                secs, _ = _get_sections(data)
                if secs:
                    print(f"  {step_dir.name}/{f.name}: {len(secs)} sections — {[s.get('id') for s in secs]}")
            except Exception:
                pass


def run_new_mode(args) -> None:
    types = [args.script_type] if args.script_type else list(_SCRIPT_TYPES)
    unit_short = re.sub(r"^unit(\d+)$", r"u\1", args.unit)

    for script_type in types:
        pipeline_dir = _find_pipeline_dir(args.unit, args.module, script_type)
        if not pipeline_dir:
            print(f"[SKIP] No pipeline dir found for {args.unit} module {args.module} {script_type}")
            continue

        versions = args.versions or []
        if not versions:
            latest = _latest_version(pipeline_dir)
            if not latest:
                print(f"[SKIP] No versions in {pipeline_dir.relative_to(project_root)}")
                continue
            versions = [latest]

        dest = TRACKED_DIR / unit_short / f"m{args.module}" / script_type
        print(f"\n{script_type}: {' + '.join(versions)} -> {dest.relative_to(project_root)}")
        _stitch(pipeline_dir, versions, dest)

    print("\nDone.")


# ---------------------------------------------------------------------------
# Legacy mode — remove after module 1 & 2 ingestion is complete
# ---------------------------------------------------------------------------

_STEP_ALIASES: dict[str, str] = {
    "script_generator": "section_structurer",
}


def _resolve_version(path: Path) -> Path:
    if any(_STEP_RE.match(d.name) for d in path.iterdir() if d.is_dir()):
        return path
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
    if isinstance(data, list):
        return [{**item, "id": id_map[item["id"]]} if isinstance(item, dict) and item.get("id") in id_map else item for item in data]
    return data


def _rename_section_files(directory: Path, id_map: dict[str, str]) -> None:
    for subdir in directory.iterdir():
        if not subdir.is_dir():
            continue
        for f in list(subdir.iterdir()):
            if f.stem in id_map:
                f.rename(subdir / (id_map[f.stem] + f.suffix))


def _apply_id_renames(step_dir: Path, id_map: dict[str, str]) -> None:
    for json_file in step_dir.glob("*.json"):
        if json_file.name in _SKIP_FILES:
            continue
        data = json.loads(json_file.read_text(encoding="utf-8"))
        renamed = _rename_ids_in_json(data, id_map)
        if renamed is not data:
            json_file.write_text(json.dumps(renamed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _rename_section_files(step_dir, id_map)


def _merge_json_arrays(dest_data: list, new_data: list) -> list:
    new_by_id = {s["id"]: s for s in new_data if isinstance(s, dict) and "id" in s}
    result = []
    for item in dest_data:
        sid = item.get("id") if isinstance(item, dict) else None
        result.append(new_by_id.pop(sid, item))
    result.extend(new_by_id.values())
    return result


def _overlay_step_legacy(dest_step: Path, new_step: Path) -> None:
    for new_json in new_step.glob("*.json"):
        if new_json.name in _SKIP_FILES:
            continue
        dest_json = dest_step / new_json.name
        new_data = json.loads(new_json.read_text(encoding="utf-8"))
        if dest_json.exists() and isinstance(new_data, list):
            dest_data = json.loads(dest_json.read_text(encoding="utf-8"))
            if isinstance(dest_data, list):
                new_data = _merge_json_arrays(dest_data, new_data)
        dest_json.write_text(json.dumps(new_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for subdir in new_step.iterdir():
        if not subdir.is_dir():
            continue
        dest_subdir = dest_step / subdir.name
        dest_subdir.mkdir(exist_ok=True)
        for f in subdir.iterdir():
            shutil.copy2(f, dest_subdir / f.name)

    for f in new_step.iterdir():
        if f.is_file() and f.name not in _SKIP_FILES and not f.name.endswith(".json"):
            shutil.copy2(f, dest_step / f.name)


def _derive_dest_legacy(new_pipeline: Path) -> Path | None:
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


def run_legacy_mode(args) -> None:
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

    dest = (project_root / args.dest).resolve() if args.dest else _derive_dest_legacy(new_pipeline)
    if dest is None:
        print("ERROR: could not derive destination; use --dest", file=sys.stderr)
        sys.exit(1)
    dest = (project_root / dest).resolve()

    print(f"Old pipeline : {old_pipeline.relative_to(project_root)}")
    print(f"New pipeline : {new_pipeline.relative_to(project_root)}")
    print(f"Destination  : {dest.relative_to(project_root)}")
    print()

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

    with tempfile.TemporaryDirectory() as tmp:
        tmp_old = Path(tmp) / "old"
        shutil.copytree(old_pipeline, tmp_old, ignore=shutil.ignore_patterns(*_SKIP_FILES))
        old_steps_tmp = _step_dirs(tmp_old, aliases=_STEP_ALIASES)

        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)

        for suffix in matched_suffixes:
            new_step_dir = new_steps[suffix]
            old_step_tmp = old_steps_tmp[suffix]
            dest_step = dest / new_step_dir.name

            shutil.copytree(old_step_tmp, dest_step)
            _apply_id_renames(dest_step, id_map)

            old_suffix = _STEP_RE.match(old_step_tmp.name).group(2)
            if old_suffix != suffix:
                old_json = dest_step / f"{old_suffix}.json"
                new_json = dest_step / f"{suffix}.json"
                if old_json.exists() and not new_json.exists():
                    old_json.rename(new_json)

            print(f"  [BASE]    {new_step_dir.name}  (from old '{old_step_tmp.name}')")

        for suffix in sorted(new_steps, key=lambda s: int(_STEP_RE.match(new_steps[s].name).group(1))):
            new_step_dir = new_steps[suffix]
            dest_step = dest / new_step_dir.name

            if suffix in matched_suffixes:
                _overlay_step_legacy(dest_step, new_step_dir)
                print(f"  [OVERLAY] {new_step_dir.name}")
            else:
                shutil.copytree(new_step_dir, dest_step, ignore=shutil.ignore_patterns(*_SKIP_FILES))
                print(f"  [NEW]     {new_step_dir.name}")

    for fname in ("metadata.json", "console.txt"):
        src = new_pipeline / fname
        if src.exists():
            shutil.copy2(src, dest / fname)

    print(f"\nDone. {dest.relative_to(project_root)} updated.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    # Detect legacy mode: positional args provided
    parser.add_argument("old_pipeline", nargs="?", type=Path, help="[LEGACY] Old pipeline version dir")
    parser.add_argument("new_pipeline", nargs="?", type=Path, help="[LEGACY] New pipeline version dir")
    parser.add_argument("--dest", type=Path, help="[LEGACY] Destination override")

    # New mode args
    parser.add_argument("--unit", default="unit1", help="Unit (e.g. unit1)")
    parser.add_argument("--module", help="Module number (e.g. 12)")
    parser.add_argument("--type", dest="script_type", choices=_SCRIPT_TYPES, help="Script type")
    parser.add_argument("--versions", nargs="+", metavar="VERSION", help="Versions to stitch in order (e.g. v0 v11)")

    args = parser.parse_args()

    if args.old_pipeline and args.new_pipeline:
        run_legacy_mode(args)
    elif args.module:
        run_new_mode(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
