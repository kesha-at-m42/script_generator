"""Pull Notion edits into tracked_scripts/.

For each registry entry that has a directory in tracked_scripts/, fetches
the latest edits from Notion and writes:

    tracked_scripts/{unit}/{module}/{script_type}/step_NN_pull/pull.json

The source for patching is the last non-push/pull step (typically
merge_remediation.json). Use fixes/stitch_pipeline_outputs.py to sync
pipeline outputs into tracked_scripts/ first.

Usage:
    python cli/pull_tracked_scripts.py
    python cli/pull_tracked_scripts.py --unit unit1
    python cli/pull_tracked_scripts.py --module 12
    python cli/pull_tracked_scripts.py --type lesson
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))
sys.path.insert(0, str(project_root / "steps" / "prompts"))

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from claude_client import ClaudeClient  # noqa: E402
from comment_analyzer import COMMENT_ANALYZER_PROMPT  # noqa: E402

from utils.notion import (  # noqa: E402
    fetch_lesson_comments,
    is_configured,
    load_registry,
    pull_lesson,
    pull_out_path,
)

TRACKED_DIR = project_root / "tracked_scripts"

_PIPELINE_RE = re.compile(
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_)?module_(\d+)$"
)
_SCRIPT_TYPE_LABELS = {
    "lesson": "lesson",
    "warmup": "warmup",
    "exitcheck": "exitcheck",
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


def _find_source_json(tracked_dir: Path) -> Path | None:
    """Find the last non-push/pull step JSON (e.g. merge_remediation.json)."""
    step_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )
    for step_dir in reversed(step_dirs):
        if re.match(r"^step_\d+_pull$", step_dir.name):
            continue
        if re.match(r"^step_\d+_push$", step_dir.name):
            continue
        json_files = [
            f for f in step_dir.glob("*.json") if f.name not in _SKIP_FILES and "flag" not in f.name
        ]
        for f in json_files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(data, list) or (
                    isinstance(data, dict) and isinstance(data.get("sections"), list)
                ):
                    return f
            except Exception:
                pass
    return None


def _notion_pull(tracked_dir: Path, page_id: str) -> str | None:
    """Pull from Notion into tracked_dir. Returns error string or None."""
    source = _find_source_json(tracked_dir)
    if not source:
        return "no source JSON found"
    try:
        original = json.loads(source.read_text(encoding="utf-8"))
        patched, flags, raw_blocks = pull_lesson(page_id, original)

        out_path = pull_out_path(source)
        out_path.write_text(
            json.dumps(patched, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        if flags:
            (out_path.parent / "notion_flags.json").write_text(
                json.dumps(flags, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
        (out_path.parent / "notion_blocks.json").write_text(
            json.dumps(raw_blocks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    except Exception as e:
        return str(e)
    return None


def _analyze_comment(comment: dict, sections: list) -> dict:
    """Call Claude to identify which pipeline step introduced the issue in a comment thread."""
    section_by_id = {s["id"]: s for s in sections if isinstance(s, dict) and "id" in s}
    surrounding = section_by_id.get(comment.get("section_id") or "", {})

    user_message = json.dumps(
        {
            "thread": comment["thread"],
            "section_id": comment.get("section_id"),
            "beat_description": comment.get("beat_description"),
            "beat": comment.get("beat"),
            "surrounding_section": surrounding,
        },
        ensure_ascii=False,
    )

    system_text = (
        (COMMENT_ANALYZER_PROMPT.role or "") + "\n\n" + COMMENT_ANALYZER_PROMPT.instructions
    )

    logs_dir = project_root / "logs"
    logs_dir.mkdir(exist_ok=True)
    client = ClaudeClient(log_file=str(logs_dir / "claude_usage.jsonl"))

    try:
        raw = client.generate(
            system=system_text,
            user_message=user_message,
            max_tokens=COMMENT_ANALYZER_PROMPT.max_tokens or 600,
            temperature=COMMENT_ANALYZER_PROMPT.temperature or 0.3,
        )
        return json.loads(raw)
    except Exception as e:
        return {"error": str(e), "raw": raw if "raw" in dir() else ""}


def _sweep_comments(tracked_dir: Path, page_id: str) -> str:
    """Fetch @claude comments from Notion, analyze each, write notion_comments.json."""
    pull_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_pull$", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )
    if not pull_dirs:
        return "no pull dir"

    pull_file = pull_dirs[-1] / "pull.json"
    if not pull_file.exists():
        return "pull.json missing"

    sections = json.loads(pull_file.read_text(encoding="utf-8"))
    if not isinstance(sections, list):
        return "pull.json not a list"

    try:
        comments = fetch_lesson_comments(page_id, sections)
    except Exception as e:
        return f"comment fetch error: {e}"

    if not comments:
        out_path = pull_dirs[-1] / "notion_comments.json"
        if out_path.exists():
            out_path.unlink()
        return "no @claude comments"

    analyzed = []
    for comment in comments:
        analysis = _analyze_comment(comment, sections)
        entry = {
            "discussion_id": comment["discussion_id"],
            "block_id": comment["block_id"],
            "section_id": comment.get("section_id"),
            "beat_description": comment.get("beat_description"),
            "beat": comment.get("beat"),
            "thread": comment["thread"],
        }
        entry.update(analysis)
        analyzed.append(entry)

    out_path = pull_dirs[-1] / "notion_comments.json"
    out_path.write_text(json.dumps(analyzed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    rel = out_path.relative_to(project_root)
    return f"{len(analyzed)} @claude comment(s) → {rel}"


def _pull_entry(key: str, entry: dict) -> str:
    """Pull one registry entry. Returns a status string."""
    parsed = _parse_registry_key(key)
    if not parsed:
        return f"SKIP  {key} (not a unit/module pipeline)"

    unit, script_type, module_num = parsed
    unit_short = re.sub(r"^unit(\d+)$", r"u\1", unit)
    dest = TRACKED_DIR / unit_short / f"m{module_num}" / script_type

    if not dest.exists():
        return f"SKIP  {key} (not in tracked_scripts — sync first)"

    err = _notion_pull(dest, entry["page_id"])
    if err:
        return f"PULL ERROR  {key}: {err}"

    comment_status = _sweep_comments(dest, entry["page_id"])
    rel = dest.relative_to(project_root)
    return f"OK    {rel}  [{comment_status}]"


def main() -> None:
    parser = argparse.ArgumentParser(description="Pull Notion edits into tracked_scripts/")
    parser.add_argument("--unit", help="Filter by unit (e.g. unit1)")
    parser.add_argument("--module", help="Filter by module number (e.g. 12)")
    parser.add_argument(
        "--type",
        dest="script_type",
        help="Filter by script type (lesson/warmup/exitcheck/synthesis)",
    )
    args = parser.parse_args()

    if not is_configured():
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

    # Deduplicate: keep only the most recently pushed entry per (unit, script_type, module)
    best: dict[tuple, tuple[str, dict]] = {}
    skipped_keys = []
    for key, entry in entries:
        parsed = _parse_registry_key(key)
        if not parsed:
            skipped_keys.append((key, entry))
            continue
        slot = parsed
        existing_key, existing_entry = best.get(slot, (None, {}))
        if existing_key is None or entry.get("pushed_at", "") > existing_entry.get("pushed_at", ""):
            best[slot] = (key, entry)

    deduped = list(best.values())
    total = len(deduped) + len(skipped_keys)
    print(
        f"Pulling {len(deduped)} pipeline(s) from Notion into tracked_scripts/... ({total - len(deduped)} skipped as duplicates)\n"
    )

    for key, entry in skipped_keys:
        print(f"SKIP  {key} (not a unit/module pipeline)")
    for key, entry in deduped:
        print(_pull_entry(key, entry))


if __name__ == "__main__":
    main()
