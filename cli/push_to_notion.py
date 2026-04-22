"""Push or pull a lesson JSON output file to/from Notion.

Usage:
    python cli/push_to_notion.py <path/to/output.json> [--title "Custom Title"]
    python cli/push_to_notion.py <path/to/output.json> --pull

Push: renders the lesson with emoji callouts and updates the Notion page.
Pull: fetches edits from Notion, patches dialogue/prompt text back into the
      file, and saves a notion_flags.json sidecar listing any scene
      descriptions that changed (those need manual config updates).
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

sys.path.insert(0, str(project_root / "core"))

from version_manager import get_next_version  # noqa: E402

from utils.notion import (  # noqa: E402
    blocks_to_lesson,
    get_page_url,
    get_registry_entry,
    is_configured,
    pull_lesson,
    pull_out_path,
    push_lesson,
    set_registry_entry,
)

TRACKED_DIR = project_root / "tracked_scripts"
_PIPELINE_RE = re.compile(
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
)
_STITCH_SKIP = {"notion_blocks.json", "notion_push_log.json"}


def _auto_stitch(file_path: Path) -> str | None:
    """If file_path is inside outputs/, copy its version dir to tracked_scripts/.

    Returns the relative dest path on success, or None if not applicable.
    """
    try:
        rel = file_path.relative_to(project_root / "outputs")
    except ValueError:
        return None

    parts = rel.parts
    if len(parts) < 3:
        return None

    unit, pipeline, version = parts[0], parts[1], parts[2]
    if not re.match(r"^v\d+$", version):
        return None

    m = _PIPELINE_RE.match(pipeline)
    if not m:
        return None

    script_type, module_num = m.group(1), m.group(2)
    unit_short = re.sub(r"^unit(\d+)$", r"u\1", unit)
    version_dir = project_root / "outputs" / unit / pipeline / version
    dest = TRACKED_DIR / unit_short / f"m{module_num}" / script_type

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(version_dir, dest, ignore=shutil.ignore_patterns(*_STITCH_SKIP))
    return str(dest.relative_to(project_root))


def main():
    parser = argparse.ArgumentParser(description="Push or pull a lesson JSON file with Notion")
    parser.add_argument("file", help="Path to the JSON file")
    parser.add_argument("--title", help="Notion page title (push only, auto-generated if omitted)")
    parser.add_argument(
        "--pull", action="store_true", help="Pull edits from Notion back into the file"
    )
    parser.add_argument(
        "--new-version",
        action="store_true",
        help="Pull into a new version directory instead of overwriting",
    )
    parser.add_argument(
        "--test-push",
        action="store_true",
        help="Create a new temporary page without updating the registry",
    )
    parser.add_argument(
        "--sections",
        nargs="+",
        metavar="SECTION_ID",
        help="Push only these section IDs (surgical update using their _notion_block_id)",
    )
    parser.add_argument(
        "--page-id",
        help="Notion page ID to pull from (overrides registry lookup, useful for tracked_scripts)",
    )
    args = parser.parse_args()

    if not is_configured():
        print("[ERROR] NOTION_API_KEY or NOTION_PARENT_PAGE_ID not set in .env")
        sys.exit(1)

    file_path = Path(args.file).resolve()
    if not file_path.exists():
        print(f"[ERROR] File not found: {file_path}")
        sys.exit(1)

    if args.pull:
        _pull(file_path, new_version=args.new_version, page_id_override=args.page_id)
    else:
        _push(file_path, args.title, test_push=args.test_push, sections=args.sections)


def _push(
    file_path: Path, title: str | None, test_push: bool = False, sections: list[str] | None = None
) -> None:
    data = json.loads(file_path.read_text(encoding="utf-8"))
    title = title or file_path.parent.parent.parent.name
    if test_push:
        title = f"[TEST] {title}"

    print(f"Pushing: {file_path.relative_to(project_root)}")

    if test_push:
        print("Test push — creating new page (registry not updated)...")
    if sections:
        print(f"Sections: {', '.join(sections)}")

    page_id = push_lesson(
        data=data,
        title=title,
        file_path=None if test_push else file_path,
        sections=sections,
    )
    print(f"[OK] {get_page_url(page_id)}")

    if not test_push:
        dest = _auto_stitch(file_path)
        if dest:
            print(f"[OK] Stitched to {dest}")


def _resolve_push_source(file_path: Path) -> tuple[Path, Path] | None:
    """If file_path is a push step output, return (original_path, out_path).

    Detects a push output by its content being {"notion_url": "..."}.
    Finds the previous step's main JSON as the original data source.
    Sets the pull output to step_{N+1}_pull/pull.json in the same version dir.

    Returns None if file_path is not a push step output.
    """
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
    except Exception:
        return None

    if not (isinstance(data, dict) and set(data.keys()) == {"notion_url"}):
        return None

    step_dir = file_path.parent
    version_dir = step_dir.parent
    m = re.match(r"step_(\d+)_", step_dir.name)
    if not m:
        return None
    push_step_num = int(m.group(1))

    step_dirs = sorted(
        [d for d in version_dir.iterdir() if d.is_dir() and re.match(r"step_(\d+)_", d.name)],
        key=lambda d: int(re.match(r"step_(\d+)_", d.name).group(1)),
    )
    prev_step = next(
        (
            d
            for d in reversed(step_dirs)
            if int(re.match(r"step_(\d+)_", d.name).group(1)) < push_step_num
        ),
        None,
    )
    if prev_step is None:
        return None

    json_files = [f for f in prev_step.glob("*.json") if f.name != "notion_flags.json"]
    if not json_files:
        return None

    original_path = json_files[0]
    # Reuse existing pull dir if present; only create a new one on first pull.
    existing_pull_dirs = sorted(
        [
            (int(m.group(1)), d)
            for d in version_dir.iterdir()
            if d.is_dir() and (m := re.match(r"step_(\d+)_pull$", d.name))
        ]
    )
    if existing_pull_dirs:
        out_step_dir = existing_pull_dirs[-1][1]
    else:
        existing_nums = [
            int(m.group(1))
            for d in version_dir.iterdir()
            if d.is_dir() and (m := re.match(r"step_(\d+)_", d.name))
        ]
        next_num = max(existing_nums) + 1 if existing_nums else push_step_num + 1
        out_step_dir = version_dir / f"step_{next_num:02d}_pull"
        out_step_dir.mkdir(parents=True, exist_ok=True)
    return original_path, out_step_dir / "pull.json"


def _collect_notion_ids(obj: Any, acc: dict[str, str]) -> None:
    """Recursively collect {beat_id: _notion_block_id} from a lesson structure."""
    if isinstance(obj, dict):
        if "id" in obj and "_notion_block_id" in obj:
            acc[obj["id"]] = obj["_notion_block_id"]
        for v in obj.values():
            _collect_notion_ids(v, acc)
    elif isinstance(obj, list):
        for item in obj:
            _collect_notion_ids(item, acc)


def _stamp_notion_ids(obj: Any, id_map: dict[str, str]) -> None:
    """Recursively stamp _notion_block_id onto any object whose 'id' is in id_map."""
    if isinstance(obj, dict):
        obj_id = obj.get("id")
        if obj_id and obj_id in id_map:
            obj["_notion_block_id"] = id_map[obj_id]
        for v in obj.values():
            _stamp_notion_ids(v, id_map)
    elif isinstance(obj, list):
        for item in obj:
            _stamp_notion_ids(item, id_map)


def _ids_changed(original: Any, patched: Any) -> bool:
    """Return True if the Notion block IDs in patched differ from those in original."""
    orig_ids: dict[str, str] = {}
    patched_ids: dict[str, str] = {}
    _collect_notion_ids(original, orig_ids)
    _collect_notion_ids(patched, patched_ids)
    if not orig_ids:
        return True  # no IDs yet — first pull, always stamp
    return orig_ids != patched_ids


def _copy_and_stamp_version(
    src_version_dir: Path, dst_version_dir: Path, id_map: dict[str, str]
) -> None:
    """Copy all step outputs from src to dst, stamping _notion_block_id values."""
    for step_dir in sorted(src_version_dir.glob("step_*")):
        dst_step = dst_version_dir / step_dir.name
        dst_step.mkdir(parents=True, exist_ok=True)
        for f in step_dir.iterdir():
            if not f.is_file():
                continue
            if f.name == "notion_blocks.json":
                continue  # raw Notion data, don't copy stale blocks
            if f.suffix == ".json":
                data = json.loads(f.read_text(encoding="utf-8"))
                _stamp_notion_ids(data, id_map)
                (dst_step / f.name).write_text(
                    json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
                )
            else:
                shutil.copy2(f, dst_step / f.name)


def _pull(file_path: Path, new_version: bool = False, page_id_override: str | None = None) -> None:
    if page_id_override:
        page_id = page_id_override.replace("-", "")
        # Normalise to dashed UUID format if needed
        if len(page_id) == 32:
            page_id = (
                f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"
            )
    else:
        entry = get_registry_entry(file_path)
        if not entry:
            print("[ERROR] No Notion page found for this file. Push it first.")
            sys.exit(1)
        page_id = entry["page_id"]

    print(f"Pulling from: {get_page_url(page_id)}")

    push_source = _resolve_push_source(file_path)
    if push_source:
        original_path, default_out_path = push_source
        print(f"[PUSH OUTPUT] Using source: {original_path.relative_to(project_root)}")
        original = json.loads(original_path.read_text(encoding="utf-8"))
    else:
        original = json.loads(file_path.read_text(encoding="utf-8"))
        default_out_path = file_path

    version_dir = file_path.parent.parent
    pipeline_dir = version_dir.parent

    patched, flags, blocks = pull_lesson(page_id, original)

    # Determine whether this path lives inside a versioned pipeline (outputs/).
    # tracked_scripts and other non-versioned paths skip version management and save in place.
    in_versioned_pipeline = re.match(r"^v\d+$", version_dir.name) is not None

    if in_versioned_pipeline and _ids_changed(original, patched):
        next_ver = get_next_version(pipeline_dir)
        print(f"[IDs changed] Creating new version {next_ver} with reverse-stamped block IDs...")
        id_map: dict[str, str] = {}
        _collect_notion_ids(patched, id_map)
        new_version_dir = pipeline_dir / next_ver
        _copy_and_stamp_version(version_dir, new_version_dir, id_map)
        rel = default_out_path.relative_to(version_dir)
        out_path = new_version_dir / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[IDs changed] Reverse-stamped {len(id_map)} block IDs across {next_ver}")
    elif in_versioned_pipeline and new_version:
        next_ver = get_next_version(pipeline_dir)
        step_dir = pipeline_dir / next_ver / default_out_path.parent.name
        step_dir.mkdir(parents=True, exist_ok=True)
        out_path = step_dir / default_out_path.name
        print(f"Creating new version: {next_ver}")
    elif not in_versioned_pipeline:
        out_path = pull_out_path(file_path)
        # Reverse-stamp: create a copy of the pipeline source (file_path) with
        # _notion_block_id stamped on every matched beat, without overwriting the original.
        if out_path != file_path:
            pipeline_original = json.loads(file_path.read_text(encoding="utf-8"))
            pipeline_stamped, _ = blocks_to_lesson(blocks, pipeline_original)
            stamped_path = file_path.parent / (file_path.stem + "_notion_stamped.json")
            stamped_path.write_text(
                json.dumps(pipeline_stamped, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            print(f"[OK] Reverse-stamped source saved to {stamped_path.relative_to(project_root)}")
    else:
        out_path = default_out_path

    out_path.write_text(json.dumps(patched, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[OK] Saved to {out_path.relative_to(project_root)}")

    # Register the page_id so future pulls don't need --page-id
    if page_id_override:
        title = file_path.parent.parent.parent.name  # best-effort title from path
        set_registry_entry(out_path, page_id, title)
        print(f"[OK] Registered {page_id} in notion_pages.json")

    blocks_path = out_path.parent / "notion_blocks.json"
    blocks_path.write_text(
        json.dumps(blocks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[OK] Notion blocks saved to {blocks_path.relative_to(project_root)}")

    flags_path = out_path.parent / "notion_flags.json"
    if flags:
        flags_path.write_text(
            json.dumps(flags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"\n[FLAGS] {len(flags)} issue(s) flagged:")
        for f in flags:
            ftype = f.get("flag_type", "")
            if ftype == "scene_description_updated":
                print(
                    f"  [scene_description_updated] [{f['section_id']}] {f['method']} {f['tangible_id']}"
                )
                print(f"    was:   {f['original_description']}")
                print(f"    now:   {f['notion_description']}")
            elif ftype == "options_parse_failed":
                print(
                    f"  [options_parse_failed] [{f['section_id']}] beat {f['beat_id']} — {f['message']}"
                )
                if f.get("original_options"):
                    print(f"    source: {f['original_options']}")
                if f.get("notion_options_text"):
                    print(f"    notion: {f['notion_options_text']}")
            elif ftype == "section_not_in_notion":
                print(
                    f"  [section_not_in_notion] [{f['section_id']}] type={f.get('section_type')} — dropped"
                )
            else:
                print(f"  {f}")
        print(f"\n  Saved to: {flags_path.relative_to(project_root)}")
    else:
        if flags_path.exists():
            flags_path.unlink()
        print("[OK] No flags.")


if __name__ == "__main__":
    main()
