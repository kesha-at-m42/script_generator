#!/usr/bin/env python3
"""
Diff lesson dialogue between generated output and Notion-edited pull.

Compares step_12_merge_remediation/merge_remediation.json (pre-push)
against step_14_pull/pull.json (post-Notion-edit) for a given tracked
script directory.

Dialogue is separated into three categories:
  lesson      — teacher speech before the prompt
  correct     — validator entries where is_correct=true
  remediation — validator entries where is_correct=false (LIGHT/MEDIUM/HEAVY or per-distractor)

Usage:
    python cli/diff_dialogue.py tracked_scripts/u1/m1/lesson
    python cli/diff_dialogue.py tracked_scripts/u1/m1/lesson -o report.md

    # Or pass paths directly:
    python cli/diff_dialogue.py --pre old.json --post new.json
"""

import json
import argparse
from pathlib import Path

PRE_PUSH_FILENAME = "merge_remediation.json"
POST_PULL_FILENAME = "pull.json"


# ---------------------------------------------------------------------------
# Condition labelling
# ---------------------------------------------------------------------------

def condition_label(condition: dict) -> str:
    if not condition:
        return "HEAVY"
    if "incorrect_count" in condition:
        n = condition["incorrect_count"]
        return {1: "LIGHT", 2: "MEDIUM"}.get(n, f"ATTEMPT_{n}")
    if "selected" in condition:
        return f"selected={condition['selected']}"
    if "and" in condition or "or" in condition:
        return f"branch:{json.dumps(condition, separators=(',', ':'))}"
    return json.dumps(condition, separators=(",", ":"))


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def flat_beats(node: dict) -> list[dict]:
    """
    Normalize both schema variants to a flat list of beat dicts.

    Older format (m1-style):  node["steps"] = [[beat, ...], ...]  (list of sequences)
    Newer format (m11-style): node["beats"] = [beat, ...]          (flat list)
    """
    if node.get("beats"):
        return node["beats"]
    return [beat for seq in (node.get("steps") or []) for beat in seq]


def collect_dialogue(node: dict) -> str:
    """Collect all dialogue text from a validator entry (either beats or steps)."""
    return " ".join(b["text"] for b in flat_beats(node) if b.get("type") == "dialogue")


def parse_section(section: dict) -> dict:
    """
    Flatten a section's beats into per-prompt records.

    Returns:
        {
            "id": str,
            "prompts": [
                {
                    "prompt_text": str,
                    "lesson_dialogue": str,        # speech before this prompt
                    "correct":     [{"label", "condition", "description", "dialogue"}],
                    "remediation": [{"label", "condition", "description", "dialogue"}],
                }
            ]
        }
    """
    pending: list[str] = []
    prompts: list[dict] = []

    for beat in flat_beats(section):
        btype = beat.get("type")
        if btype == "dialogue":
            pending.append(beat["text"])
        elif btype == "prompt":
            correct, remediation = [], []
            for v in beat.get("validator", []):
                cond = v.get("condition", {})
                entry = {
                    "label": condition_label(cond),
                    "condition": cond,
                    "description": v.get("description", ""),
                    "dialogue": collect_dialogue(v),
                }
                (correct if v.get("is_correct") else remediation).append(entry)

            prompts.append({
                "prompt_text": beat.get("text", ""),
                "lesson_dialogue": " ".join(pending),
                "correct": correct,
                "remediation": remediation,
            })
            pending = []

    return {"id": section["id"], "prompts": prompts}


# ---------------------------------------------------------------------------
# Diffing
# ---------------------------------------------------------------------------

def _diff_validator_group(
    dtype: str,
    section_id: str,
    prompt_text: str,
    old_entries: list,
    new_entries: list,
) -> list[dict]:
    old_by_label = {e["label"]: e for e in old_entries}
    new_by_label = {e["label"]: e for e in new_entries}
    all_labels = list(old_by_label) + [k for k in new_by_label if k not in old_by_label]

    rows = []
    for label in all_labels:
        old_e = old_by_label.get(label)
        new_e = new_by_label.get(label)
        old_text = old_e["dialogue"] if old_e else ""
        new_text = new_e["dialogue"] if new_e else ""
        if old_text == new_text:
            continue
        ref = old_e or new_e
        rows.append({
            "section_id": section_id,
            "prompt": prompt_text,
            "type": dtype,
            "label": label,
            "condition": ref["condition"],
            "description": ref["description"],
            "old": old_text or "**[MISSING]**",
            "new": new_text or "**[MISSING]**",
        })
    return rows


def diff_prompt_pair(section_id: str, pre: dict | None, post: dict | None) -> list[dict]:
    rows = []
    ref = pre or post
    prompt_text = ref["prompt_text"]

    old_lesson = pre["lesson_dialogue"] if pre else ""
    new_lesson = post["lesson_dialogue"] if post else ""
    if old_lesson != new_lesson:
        rows.append({
            "section_id": section_id,
            "prompt": prompt_text,
            "type": "lesson",
            "label": "—",
            "condition": {},
            "description": "",
            "old": old_lesson or "**[MISSING]**",
            "new": new_lesson or "**[MISSING]**",
        })

    for dtype in ("correct", "remediation"):
        rows.extend(_diff_validator_group(
            dtype,
            section_id,
            prompt_text,
            pre[dtype] if pre else [],
            post[dtype] if post else [],
        ))

    return rows


def diff_scripts(pre_path: Path, post_path: Path) -> list[dict]:
    pre_data = json.loads(pre_path.read_text(encoding="utf-8"))
    post_data = json.loads(post_path.read_text(encoding="utf-8"))

    pre_map = {s["id"]: parse_section(s) for s in pre_data}
    post_map = {s["id"]: parse_section(s) for s in post_data}

    all_ids = list(pre_map) + [k for k in post_map if k not in pre_map]
    rows = []

    for sid in all_ids:
        pre_sec = pre_map.get(sid)
        post_sec = post_map.get(sid)

        if pre_sec and post_sec:
            for pre_p, post_p in zip(pre_sec["prompts"], post_sec["prompts"]):
                rows.extend(diff_prompt_pair(sid, pre_p, post_p))
        elif pre_sec:
            for p in pre_sec["prompts"]:
                rows.extend(diff_prompt_pair(sid, p, None))
        else:
            for p in post_sec["prompts"]:
                rows.extend(diff_prompt_pair(sid, None, p))

    return rows


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_markdown(rows: list[dict], pre_label: str, post_label: str) -> str:
    if not rows:
        return "No dialogue differences found.\n"

    by_section: dict[str, list[dict]] = {}
    for row in rows:
        by_section.setdefault(row["section_id"], []).append(row)

    lines = [
        "# Dialogue Diff Report\n",
        f"**Pre-push (generated):** `{pre_label}`  \n**Post-pull (Notion):** `{post_label}`\n",
    ]

    for section_id, section_rows in by_section.items():
        lines.append(f"\n## {section_id}\n")
        lines.append("| Prompt | Type | Condition | Description | Pre-push | Post-pull |")
        lines.append("|---|---|---|---|---|---|")
        for row in section_rows:
            lines.append(
                f"| {_cell(row['prompt'])} "
                f"| {row['type']} "
                f"| {row['label']} "
                f"| {_cell(row['description'])} "
                f"| {_cell(row['old'])} "
                f"| {_cell(row['new'])} |"
            )

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def is_script_dir(path: Path) -> bool:
    return (path / "step_12_merge_remediation" / PRE_PUSH_FILENAME).exists()


def resolve_script_dirs(root: Path) -> list[tuple[Path, Path, str]]:
    """
    Return list of (pre_path, post_path, label) for all diffable script dirs
    at or under root. Works at any depth: script-type dir, module dir, or unit dir.
    Label is the path relative to root's parent so it reads as e.g. "m1/lesson".
    """
    results = []

    def walk(path: Path):
        if is_script_dir(path):
            post = path / "step_14_pull" / POST_PULL_FILENAME
            if not post.exists():
                print(f"  [skip] {path.relative_to(root.parent)}: pull.json not found", flush=True)
                return
            pre = path / "step_12_merge_remediation" / PRE_PUSH_FILENAME
            label = str(path.relative_to(root.parent))
            results.append((pre, post, label))
        else:
            for child in sorted(path.iterdir()):
                if child.is_dir():
                    walk(child)

    walk(root)

    if not results:
        raise FileNotFoundError(
            f"No diffable script dirs found under {root}\n"
            f"Expected step_12_merge_remediation/{PRE_PUSH_FILENAME} somewhere inside."
        )
    return results


def render_markdown_multi(
    script_results: list[tuple[str, list[dict]]], root_label: str
) -> str:
    lines = [f"# Dialogue Diff Report — {root_label}\n"]
    any_diffs = False

    for script_name, rows in script_results:
        lines.append(f"\n# {script_name}\n")
        if not rows:
            lines.append("_No dialogue differences found._\n")
            continue
        any_diffs = True
        by_section: dict[str, list[dict]] = {}
        for row in rows:
            by_section.setdefault(row["section_id"], []).append(row)
        for section_id, section_rows in by_section.items():
            lines.append(f"\n## {section_id}\n")
            lines.append("| Prompt | Type | Condition | Description | Pre-push | Post-pull |")
            lines.append("|---|---|---|---|---|---|")
            for row in section_rows:
                lines.append(
                    f"| {_cell(row['prompt'])} "
                    f"| {row['type']} "
                    f"| {row['label']} "
                    f"| {_cell(row['description'])} "
                    f"| {_cell(row['old'])} "
                    f"| {_cell(row['new'])} |"
                )

    if not any_diffs:
        return "No dialogue differences found.\n"
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Diff dialogue between generated output and Notion-edited pull"
    )
    parser.add_argument(
        "script_dir",
        nargs="?",
        help="Script dir or module dir (e.g. tracked_scripts/u1/m1 or tracked_scripts/u1/m1/lesson)",
    )
    parser.add_argument("--pre", help="Override: path to pre-push JSON")
    parser.add_argument("--post", help="Override: path to post-pull JSON")
    parser.add_argument("--output", "-o", type=Path, help="Write report to file (default: stdout)")
    args = parser.parse_args()

    if not args.pre and not args.post and not args.script_dir:
        args.script_dir = "."

    if args.pre and args.post:
        pre_path, post_path = Path(args.pre), Path(args.post)
        rows = diff_scripts(pre_path, post_path)
        report = render_markdown(rows, str(pre_path), str(post_path))
    else:
        root = Path(args.script_dir)
        entries = resolve_script_dirs(root)
        script_results = [(label, diff_scripts(pre, post)) for pre, post, label in entries]
        report = render_markdown_multi(script_results, root.name)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
