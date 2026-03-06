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
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

sys.path.insert(0, str(project_root / "core"))

from version_manager import get_next_version  # noqa: E402

from utils import notion_sync  # noqa: E402
from utils.lesson_notion_format import blocks_to_lesson, lesson_to_blocks  # noqa: E402


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
    args = parser.parse_args()

    if not notion_sync.is_configured():
        print("[ERROR] NOTION_API_KEY or NOTION_PARENT_PAGE_ID not set in .env")
        sys.exit(1)

    file_path = Path(args.file).resolve()
    if not file_path.exists():
        print(f"[ERROR] File not found: {file_path}")
        sys.exit(1)

    if args.pull:
        _pull(file_path, new_version=args.new_version)
    else:
        _push(file_path, args.title)


def _push(file_path: Path, title: str | None) -> None:
    data = json.loads(file_path.read_text(encoding="utf-8"))
    title = title or file_path.parent.parent.parent.name

    print(f"Pushing: {file_path.relative_to(project_root)}")

    existing = notion_sync.get_registry_entry(file_path)
    if existing:
        print(f"Updating existing page: {notion_sync.get_page_url(existing['page_id'])}")
    else:
        print("Creating new page...")

    page_id = notion_sync.push_to_notion(
        data=data, title=title, file_path=file_path, blocks_fn=lesson_to_blocks
    )
    print(f"[OK] {notion_sync.get_page_url(page_id)}")


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

    # Find the highest-numbered step dir before the push step
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
    out_step_dir = version_dir / f"step_{push_step_num + 1:02d}_pull"
    out_step_dir.mkdir(parents=True, exist_ok=True)
    return original_path, out_step_dir / "pull.json"


def _pull(file_path: Path, new_version: bool = False) -> None:
    entry = notion_sync.get_registry_entry(file_path)
    if not entry:
        print("[ERROR] No Notion page found for this file. Push it first.")
        sys.exit(1)

    page_id = entry["page_id"]
    print(f"Pulling from: {notion_sync.get_page_url(page_id)}")

    # If the file is a push step output, resolve the real source and output path.
    push_source = _resolve_push_source(file_path)
    if push_source:
        original_path, out_path = push_source
        print(f"[PUSH OUTPUT] Using source: {original_path.relative_to(project_root)}")
        print(f"[PUSH OUTPUT] Saving pull to: {out_path.relative_to(project_root)}")
        original = json.loads(original_path.read_text(encoding="utf-8"))
    else:
        original = json.loads(file_path.read_text(encoding="utf-8"))
        if new_version:
            pipeline_dir = file_path.parent.parent.parent
            next_ver = get_next_version(pipeline_dir)
            step_dir = pipeline_dir / next_ver / file_path.parent.name
            step_dir.mkdir(parents=True, exist_ok=True)
            out_path = step_dir / file_path.name
            print(f"Creating new version: {next_ver}")
        else:
            out_path = file_path

    client = notion_sync.get_notion_client()
    blocks = notion_sync._all_blocks(client, page_id, recursive=True)
    patched, flags = blocks_to_lesson(blocks, original)

    out_path.write_text(json.dumps(patched, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[OK] Saved to {out_path.relative_to(project_root)}")

    flags_path = out_path.parent / "notion_flags.json"
    if flags:
        flags_path.write_text(
            json.dumps(flags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"\n[FLAGS] {len(flags)} scene description(s) changed — manual config update needed:")
        for f in flags:
            print(f"  [{f['section_id']}] {f['method']} {f['tangible_id']}")
            print(f"    was:   {f['original_description']}")
            print(f"    now:   {f['notion_description']}")
        print(f"\n  Saved to: {flags_path.relative_to(project_root)}")
    else:
        if flags_path.exists():
            flags_path.unlink()
        print("[OK] No scene description changes flagged.")


if __name__ == "__main__":
    main()
