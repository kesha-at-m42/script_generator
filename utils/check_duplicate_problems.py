"""
check_duplicate_problems.py

Scans SequencePool files from the second-to-last pipeline step and flags
duplicate sequences within each template.

Severity levels:
  1 (ERROR)   - Same template + same mastery_tier + same frozenset(identifiers)
  2 (WARNING) - Same template + different mastery_tier + same frozenset(identifiers)
  3 (INFO)    - Same template + same mastery_tier + same steps[0].prompt.text

Usage:
  python utils/check_duplicate_problems.py
  python utils/check_duplicate_problems.py --module 11
  python utils/check_duplicate_problems.py --godot
  python utils/check_duplicate_problems.py --godot --module 11
  python utils/check_duplicate_problems.py path/to/file.json
"""

import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict


REPO_ROOT = Path(__file__).parent.parent
OUTPUTS_DIR = REPO_ROOT / "outputs"
MODULES_DIR = REPO_ROOT / "modules"
GODOT_SEQUENCES_DIR = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")


# ---------------------------------------------------------------------------
# Template parameter coverage
# ---------------------------------------------------------------------------

def load_template_info(module_filter: str | None = None) -> dict[str, dict]:
    """
    Load template metadata from problem_templates.json for all relevant modules.
    Returns {template_id: {skill, problem_type, parameter_coverage}}.
    """
    info: dict[str, dict] = {}

    if module_filter:
        module_dirs = [MODULES_DIR / f"module{module_filter}"]
    else:
        module_dirs = sorted(MODULES_DIR.glob("module*"))

    for module_dir in module_dirs:
        templates_file = module_dir / "problem_templates.json"
        if not templates_file.exists():
            continue
        try:
            with open(templates_file, encoding="utf-8") as f:
                templates = json.load(f)
            for t in templates:
                tid = t.get("template_id")
                if tid:
                    info[str(tid)] = {
                        "skill": t.get("skill", ""),
                        "problem_type": t.get("problem_type", ""),
                        "parameter_coverage": t.get("parameter_coverage", {}),
                    }
        except (json.JSONDecodeError, OSError):
            pass

    return info


# ---------------------------------------------------------------------------
# Discovery helpers
# ---------------------------------------------------------------------------

def find_latest_version(module_dir: Path) -> Path | None:
    versions = sorted(
        [d for d in module_dir.iterdir() if d.is_dir() and d.name[1:].isdigit() and d.name.startswith("v")],
        key=lambda d: int(d.name[1:])
    )
    return versions[-1] if versions else None


def find_second_to_last_step(version_dir: Path) -> Path | None:
    """Return the second-to-last step_NN_* directory inside version_dir."""
    step_dirs = sorted(
        [d for d in version_dir.iterdir() if d.is_dir() and d.name.startswith("step_")],
        key=lambda d: int(d.name.split("_")[1])
    )
    if len(step_dirs) < 2:
        return None
    return step_dirs[-2]


def discover_current_files(outputs_dir: Path, module_filter: str | None) -> list[tuple[Path, str]]:
    results = []
    pattern = "problem_pool_generator_module_*"
    for module_dir in sorted(outputs_dir.glob(pattern)):
        if not module_dir.is_dir():
            continue
        if module_filter and f"_module_{module_filter}_" not in module_dir.name:
            continue

        latest = find_latest_version(module_dir)
        if not latest:
            print(f"  [skip] {module_dir.name}: no versioned subdirs found")
            continue

        step_dir = find_second_to_last_step(latest)
        if not step_dir:
            print(f"  [skip] {module_dir.name}/{latest.name}: fewer than 2 step dirs")
            continue

        files = [
            f for f in step_dir.glob("*.json")
            if not f.name.endswith("_validation.json")
        ]
        if not files:
            print(f"  [skip] {module_dir.name}/{latest.name}/{step_dir.name}: no JSON files")
            continue

        for f in sorted(files):
            label = f"{module_dir.name}/{latest.name}/{step_dir.name}/{f.name}"
            results.append((f, label))
            print(f"  [found] {label}")

    return results


def discover_godot_files(module_filter: str | None) -> list[tuple[Path, str]]:
    results = []
    for pool_file in sorted(GODOT_SEQUENCES_DIR.glob("module_*/problem_pool.json")):
        module_dir = pool_file.parent
        if module_filter and module_dir.name != f"module_{module_filter}":
            continue
        label = f"godot/{module_dir.name}/problem_pool.json"
        results.append((pool_file, label))
        print(f"  [found] {label}")
    return results


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load_sequences(file_path: Path) -> list[dict]:
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  [error] Could not read {file_path}: {e}")
        return []

    if isinstance(data, dict):
        return data.get("sequences", [])
    if isinstance(data, list):
        return data
    return []


# ---------------------------------------------------------------------------
# Duplicate detection
# ---------------------------------------------------------------------------

def collect_usage(sequences: list[dict]) -> dict:
    """
    Returns {template_id: {tier: [sorted identifier list, ...]}} for every
    problem in sequences. Each inner list entry is one problem's identifier set.
    Duplicate sets are kept so the count is visible.
    """
    usage: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for seq in sequences:
        meta = seq.get("metadata", {})
        tid = meta.get("template_id", "UNKNOWN")
        tier = meta.get("mastery_tier", "UNKNOWN")
        identifiers = sorted(str(x) for x in meta.get("identifiers", []))
        if identifiers:
            usage[tid][tier].append(identifiers)
    return usage


def get_first_prompt(seq: dict) -> str:
    steps = seq.get("steps", [])
    if not steps:
        return ""
    return steps[0].get("prompt", {}).get("text", "").strip().lower()


def check_sequences(sequences: list[dict], source: str) -> list[dict]:
    """Group by template_id, then check for duplicates within each group."""
    by_template: dict[str, list[dict]] = defaultdict(list)
    for seq in sequences:
        tid = seq.get("metadata", {}).get("template_id", "UNKNOWN")
        by_template[tid].append(seq)

    issues = []
    for template_id, group in by_template.items():
        issues.extend(_check_template_group(template_id, group, source))
    return issues


def _check_template_group(template_id: str, sequences: list[dict], source: str) -> list[dict]:
    issues = []

    # Maps for each check level
    tier_ids_map: dict[tuple, list] = defaultdict(list)   # (tier, frozenset(ids)) -> [problem_ids]
    ids_tiers_map: dict[frozenset, list] = defaultdict(list)  # frozenset(ids) -> [(problem_id, tier)]
    tier_prompt_map: dict[tuple, list] = defaultdict(list)  # (tier, prompt) -> [problem_ids]

    for seq in sequences:
        meta = seq.get("metadata", {})
        raw_id = meta.get("problem_id", "?")
        problem_id = int(raw_id) if isinstance(raw_id, (int, float)) else raw_id
        tier = meta.get("mastery_tier", "UNKNOWN").strip().upper()
        identifiers = frozenset(str(x).strip() for x in meta.get("identifiers", []))
        prompt = get_first_prompt(seq)

        if identifiers:
            tier_ids_map[(tier, identifiers)].append(problem_id)
            ids_tiers_map[identifiers].append((problem_id, tier))

        if prompt:
            tier_prompt_map[(tier, prompt)].append(problem_id)

    # Level 1 ERROR: same tier + same identifiers
    for (tier, identifiers), pids in tier_ids_map.items():
        if len(pids) > 1:
            issues.append({
                "severity": 1,
                "label": "ERROR",
                "description": f"Same tier ({tier}) + same identifiers {sorted(identifiers)}",
                "problem_ids": [f"#{pid}" for pid in pids],
                "source": source,
                "template_id": template_id,
            })

    # Level 2 WARNING: same identifiers across different tiers
    for identifiers, entries in ids_tiers_map.items():
        tiers_seen = {tier for _, tier in entries}
        if len(tiers_seen) > 1:
            issues.append({
                "severity": 2,
                "label": "WARNING",
                "description": f"Same identifiers {sorted(identifiers)} in multiple tiers: {sorted(tiers_seen)}",
                "problem_ids": [f"#{pid} ({tier})" for pid, tier in entries],
                "source": source,
                "template_id": template_id,
            })

    # Level 3 INFO: same tier + same first-step prompt text
    for (tier, prompt), pids in tier_prompt_map.items():
        if len(pids) > 1:
            issues.append({
                "severity": 3,
                "label": "INFO",
                "description": f"Same tier ({tier}) + identical first-step prompt text",
                "problem_ids": [f"#{pid}" for pid in pids],
                "prompt_preview": prompt[:80],
                "source": source,
                "template_id": template_id,
            })

    return issues


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def format_report(all_issues: list[dict], template_info: dict | None = None, identifier_usage: dict | None = None) -> str:
    lines = []
    if not all_issues:
        lines.append("No duplicate issues found.")
        return "\n".join(lines)

    labels = {
        1: "ERRORS (same tier, same identifiers)",
        2: "WARNINGS (cross-tier same identifiers)",
        3: "INFO (same tier, same prompt text)",
    }

    total = len(all_issues)
    lines.append("")
    lines.append("=" * 70)
    lines.append(f"  DUPLICATE PROBLEM REPORT  —  {total} issue(s) found")
    lines.append("=" * 70)

    # Group by template, then severity within each template
    by_template: dict[str, list] = defaultdict(list)
    for issue in all_issues:
        by_template[issue["template_id"]].append(issue)

    for tid in sorted(by_template):
        template_issues = by_template[tid]
        lines.append("")
        lines.append(f"template {tid}")

        if template_info and tid in template_info:
            tinfo = template_info[tid]
            if tinfo.get("skill"):
                lines.append(f"  skill: {tinfo['skill']}")
            if tinfo.get("problem_type"):
                lines.append(f"  type: {tinfo['problem_type']}")
            for key, values in tinfo.get("parameter_coverage", {}).items():
                lines.append(f"  available {key}: {values}")

        if identifier_usage and tid in identifier_usage:
            for tier in sorted(identifier_usage[tid]):
                sets = identifier_usage[tid][tier]
                sets_str = "  |  ".join(str(s) for s in sets)
                lines.append(f"  used in {tier}: {sets_str}")

        by_severity: dict[int, list] = defaultdict(list)
        for issue in template_issues:
            by_severity[issue["severity"]].append(issue)

        for sev in [1, 2, 3]:
            issues = by_severity.get(sev, [])
            if not issues:
                continue
            lines.append(f"  -- {labels[sev]} ({len(issues)}) --")
            lines.append("")
            for issue in issues:
                lines.append(f"    [{issue['label']}] {issue['description']}")
                lines.append(f"      Problem IDs: {', '.join(issue['problem_ids'])}")
                if "prompt_preview" in issue:
                    lines.append(f"      Prompt: \"{issue['prompt_preview']}...\"")
                lines.append("")

    return "\n".join(lines)


def save_outputs(all_issues: list[dict], report_text: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "duplicate_report.json"
    txt_path = output_dir / "duplicate_report.txt"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_issues, f, indent=2)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(report_text)
        f.write("\n")

    print(f"\nResults saved to:")
    print(f"  {json_path}")
    print(f"  {txt_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def collect_files(args) -> tuple[list[tuple[Path, str]], Path]:
    """Return (file_list, output_dir)."""
    outputs_base = OUTPUTS_DIR / "duplicate_report"

    # Explicit files mode
    if args.files:
        files = [(Path(p), p) for p in args.files]
        output_dir = Path(args.output_dir) if args.output_dir else outputs_base / "current" / "all_modules"
        return files, output_dir

    # Scope subdir
    scope = f"module_{args.module}" if args.module else "all_modules"

    if args.godot:
        mode_dir = outputs_base / "godot"
        print("Discovering Godot source files...")
        files = discover_godot_files(args.module)
    else:
        mode_dir = outputs_base / "current"
        print("Discovering current pipeline files (second-to-last step)...")
        files = discover_current_files(OUTPUTS_DIR, args.module)

    output_dir = Path(args.output_dir) if args.output_dir else mode_dir / scope
    return files, output_dir


def main():
    parser = argparse.ArgumentParser(
        description="Check for duplicate problems in SequencePool files."
    )
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--current", action="store_true", default=False,
        help="Read from second-to-last pipeline step (default)"
    )
    mode_group.add_argument(
        "--godot", action="store_true", default=False,
        help="Read from Godot project problem_pool.json files"
    )
    parser.add_argument("--module", type=str, help="Only check a specific module number (e.g. 11)")
    parser.add_argument("--output-dir", type=str, dest="output_dir", help="Override output directory")
    parser.add_argument("files", nargs="*", help="Explicit JSON file paths (bypasses auto-discovery)")
    args = parser.parse_args()

    files, output_dir = collect_files(args)

    if not files:
        print("No files found to check.")
        sys.exit(0)

    module_filter = args.module if not args.files else None
    template_info = load_template_info(module_filter)

    print(f"\nChecking {len(files)} file(s)...\n")

    all_issues = []
    all_usage: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for file_path, source_label in files:
        sequences = load_sequences(file_path)
        if not sequences:
            print(f"  [empty] {source_label}: 0 sequences loaded")
            continue
        print(f"  {source_label}: {len(sequences)} sequences")
        issues = check_sequences(sequences, source_label)
        all_issues.extend(issues)
        for tid, tiers in collect_usage(sequences).items():
            for tier, sets in tiers.items():
                all_usage[tid][tier].extend(sets)

    report_text = format_report(all_issues, template_info=template_info, identifier_usage=all_usage)
    print(report_text)
    save_outputs(all_issues, report_text, output_dir)

    has_errors = any(i["severity"] == 1 for i in all_issues)
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
