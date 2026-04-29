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
    r"^(lesson|warmup|exitcheck|synthesis)_generator_(?:dialogue_pass_|v\d+_)?module_(\d+)$"
)
_SCRIPT_TYPE_LABELS = {
    "lesson": "lesson",
    "warmup": "warmup",
    "exitcheck": "exitcheck",
    "synthesis": "synthesis",
}
_SKIP_FILES = {"notion_blocks.json", "notion_push_log.json"}
_STEP_PROMPT_FILES = {
    "section_structurer": "steps/prompts/section_structurer.py",
    "dialogue_rewriter": "steps/prompts/dialogue_rewriter.py",
    "remediation_generator": "steps/prompts/remediation_generator.py",
    "starterpack_parser": "steps/prompts/starterpack_parser.py",
}


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


def _count_notion_block_ids(obj: object) -> int:
    """Count how many _notion_block_id values are present in a data structure."""
    if isinstance(obj, dict):
        count = 1 if "_notion_block_id" in obj else 0
        return count + sum(_count_notion_block_ids(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(_count_notion_block_ids(item) for item in obj)
    return 0


def _find_source_json(tracked_dir: Path) -> Path | None:
    """Find the best source JSON for patching.

    Scores each candidate by how many _notion_block_id values it contains and
    returns the one with the highest coverage. More IDs means more beats can be
    matched via Layer 1 (ID match) rather than falling back to LEGACY content
    matching. Falls back to any valid pipeline step output if no candidates score.
    """
    step_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )

    best_path: Path | None = None
    best_score: int = -1

    for step_dir in reversed(step_dirs):
        if re.match(r"^step_\d+_push$", step_dir.name):
            continue
        is_pull = re.match(r"^step_\d+_pull$", step_dir.name)
        candidates = (
            [step_dir / "pull.json"]
            if is_pull
            else [f for f in step_dir.glob("*.json") if f.name not in _SKIP_FILES and "flag" not in f.name]
        )
        for f in candidates:
            if not f.exists():
                continue
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if not (
                    isinstance(data, list)
                    or (isinstance(data, dict) and isinstance(data.get("sections"), list))
                ):
                    continue
                score = _count_notion_block_ids(data)
                if score > best_score:
                    best_score = score
                    best_path = f
            except Exception:
                pass

    return best_path


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


def _extract_beat_from_data(data: list | dict, section_id: str, beat_idx: int) -> dict | None:
    """Extract a specific beat by section ID and flat beat index from any pipeline JSON."""
    sections = data if isinstance(data, list) else data.get("sections", [])
    for section in sections:
        if not isinstance(section, dict) or section.get("id") != section_id:
            continue
        from steps.formatting.id_stamper import flatten_beats
        beats = flatten_beats(section)
        if 0 <= beat_idx < len(beats):
            return beats[beat_idx]
    return None


def _trace_beat_backwards(tracked_dir: Path, section_id: str, beat_description: str) -> list[dict]:
    """Walk pipeline steps backwards and return [{step, beat, prompt_file}] newest to oldest.

    For each step that has the section, also loads the per-section prompt file
    from the step's prompts/ subdirectory if it exists.
    Skips push/pull steps.
    """
    m = re.match(r"beats\[(\d+)\]", beat_description or "")
    if not m:
        return []
    beat_idx = int(m.group(1))

    step_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )

    history = []
    for step_dir in reversed(step_dirs):
        if re.match(r"^step_\d+_(push|pull)$", step_dir.name):
            continue
        candidates = [
            f for f in step_dir.glob("*.json")
            if f.name not in _SKIP_FILES and "flag" not in f.name and "comment" not in f.name
        ]
        for f in candidates:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if not (isinstance(data, list) or (isinstance(data, dict) and isinstance(data.get("sections"), list))):
                    continue
                beat = _extract_beat_from_data(data, section_id, beat_idx)
                if beat is None:
                    break
                entry: dict = {"step": step_dir.name, "beat": beat}
                prompt_file = step_dir / "prompts" / f"{section_id}.md"
                if prompt_file.exists():
                    entry["prompt_file"] = str(prompt_file.relative_to(project_root))
                history.append(entry)
                break
            except Exception:
                pass

    return history


def _analyze_comment(comment: dict, sections: list, tracked_dir: Path | None = None) -> dict:
    """Call Claude to identify which pipeline step introduced the issue in a comment thread."""
    section_by_id = {s["id"]: s for s in sections if isinstance(s, dict) and "id" in s}
    surrounding = section_by_id.get(comment.get("section_id") or "", {})

    pipeline_history: list[dict] = []
    if tracked_dir is not None:
        pipeline_history = _trace_beat_backwards(
            tracked_dir,
            comment.get("section_id") or "",
            comment.get("beat_description") or "",
        )

    user_message = json.dumps(
        {
            "thread": comment["thread"],
            "section_id": comment.get("section_id"),
            "beat_description": comment.get("beat_description"),
            "beat": comment.get("beat"),
            "surrounding_section": surrounding,
            "pipeline_history": pipeline_history,
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
        text = raw.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```$", "", text).strip()
        result = json.loads(text)
        result["pipeline_history"] = pipeline_history
        return result
    except Exception as e:
        return {"error": str(e), "raw": raw if "raw" in dir() else "", "pipeline_history": pipeline_history}


def _find_notion_blocks(tracked_dir: Path) -> list[dict] | None:
    """Find the most recent notion_blocks.json anywhere in the tracked dir."""
    step_dirs = sorted(
        [d for d in tracked_dir.iterdir() if d.is_dir() and re.match(r"^step_\d+_", d.name)],
        key=lambda d: int(re.match(r"^step_(\d+)_", d.name).group(1)),
    )
    for step_dir in reversed(step_dirs):
        blocks_file = step_dir / "notion_blocks.json"
        if blocks_file.exists():
            try:
                return json.loads(blocks_file.read_text(encoding="utf-8"))
            except Exception:
                pass
    return None


def _sweep_comments(tracked_dir: Path, page_id: str) -> str:
    """Fetch @claude comments from Notion, analyze each, write notion_comments.json."""
    # Use the best source: pull.json if available, else pipeline source JSON
    source_file = _find_source_json(tracked_dir)
    if not source_file:
        return "no source JSON found"

    raw = json.loads(source_file.read_text(encoding="utf-8"))
    sections = raw if isinstance(raw, list) else raw.get("sections", [])
    if not isinstance(sections, list):
        return "source JSON has no sections list"

    # Load pre-fetched blocks for full-tree comment sweep (catches untagged blocks)
    blocks = _find_notion_blocks(tracked_dir)

    try:
        comments = fetch_lesson_comments(page_id, sections, blocks=blocks)
    except Exception as e:
        return f"comment fetch error: {e}"

    # Write output next to the source file
    out_dir = source_file.parent
    out_path = out_dir / "notion_comments.json"

    if not comments:
        if out_path.exists():
            out_path.unlink()
        return "no @claude comments"

    analyzed = []
    for comment in comments:
        analysis = _analyze_comment(comment, sections, tracked_dir=tracked_dir)
        entry = {
            "discussion_id": comment["discussion_id"],
            "block_id": comment["block_id"],
            "section_id": comment.get("section_id"),
            "beat_description": comment.get("beat_description"),
            "beat": comment.get("beat"),
            "thread": comment["thread"],
            "pipeline_history": analysis.pop("pipeline_history", []),
        }
        entry.update(analysis)
        analyzed.append(entry)

    out_path.write_text(json.dumps(analyzed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = []
    for entry in analyzed:
        sid = entry.get("section_id") or "?"
        beat_desc = entry.get("beat_description") or "?"
        lines.append(f"## {sid} · {beat_desc}")
        thread = entry.get("thread", [])
        if thread:
            lines.append(f"> {thread[0].get('comment_text', '').strip()}")
            if len(thread) > 1:
                for msg in thread[1:]:
                    lines.append(f"> {msg.get('comment_text', '').strip()}")
        if entry.get("error"):
            lines.append(f"**Analysis error:** {entry['error']}")
        else:
            issue = entry.get("issue_summary", "—")
            step = entry.get("likely_step", "—")
            conf = entry.get("confidence", "—")
            reasoning = entry.get("reasoning", "—")
            suggested_fix = entry.get("suggested_fix", "—")
            beat_obj = entry.get("beat") or {}
            history = entry.get("pipeline_history") or []
            prompt_file = _STEP_PROMPT_FILES.get(step, f"steps/prompts/{step}.py")

            lines.append(f"**Issue:** {issue}")
            lines.append(f"**Step:** `{step}`  [{conf}]")
            lines.append(f"**Reasoning:** {reasoning}")
            lines.append(f"**Fix:** {suggested_fix}")
            lines.append(f"**Prompt file:** `{prompt_file}`")

            # Find the step in history that has the prompt file (where issue was introduced)
            origin_step = next((h for h in history if "prompt_file" in h), None)
            if origin_step:
                lines.append(f"**Input prompt for this section:** `{origin_step['prompt_file']}`")

            lines.append("")

            thread_text = "\n".join(
                f'  "{m.get("comment_text", "").strip()}"' for m in thread
                if m.get("comment_text", "").strip() not in ("@Claude", "@claude")
                and "@claude" not in m.get("comment_text", "").lower()
            )
            beat_summary = json.dumps(beat_obj, ensure_ascii=False)
            origin_prompt_ref = (
                f"\nInput prompt used: `{origin_step['prompt_file']}`"
                if origin_step else ""
            )
            chat_prompt = (
                f"Reviewer comment on `{sid}` ({beat_desc}):\n"
                f"{thread_text}\n\n"
                f"Issue: {issue}\n"
                f"Beat: {beat_summary}\n\n"
                f"Responsible step: `{step}` — `{prompt_file}`{origin_prompt_ref}\n\n"
                f"Please read `{prompt_file}` and identify the specific rule or instruction "
                f"that should have prevented this. Then suggest a targeted fix to that rule."
            )
            lines.append("**Paste into chat to fix:**")
            lines.append("```")
            lines.append(chat_prompt)
            lines.append("```")
        lines.append("")

    report_path = out_path.parent / "notion_comments_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    rel = out_path.relative_to(project_root)
    return f"{len(analyzed)} @claude comment(s) -> {rel}"


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
