"""
fix_partition_step2_workspace.py

For two-step sequences where:
  - Step 1 has a TickValidator with a plain fraction string answer (e.g. "1/4")
    and a plain NumLine tangible (no pre-existing ticks)
  - Step 2 is missing workspace tangibles

Fixes step 2 by copying step 1's workspace tangibles and adding
`ticks` set to step 1's TickValidator answer.

Usage:
    python fix_partition_step2_workspace.py [--modules 4 5 ...] [--dry-run] [--report-missing]

    --report-missing  Scan all multi-step sequences and flag any non-first step
                      that is missing a workspace, regardless of pattern.
"""

import argparse
import copy
import json
import sys
from pathlib import Path


POOL_BASE = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")
DEFAULT_MODULES = list(range(4, 13))
POOL_FILES = ["problem_pool.json", "problem_pool_shuffled.json"]


def endpoints_for_range(num_range: list) -> list[str]:
    """Return integer label strings for every whole number in the range, e.g. [0,2] -> ["0","1","2"]."""
    return [str(i) for i in range(int(num_range[0]), int(num_range[1]) + 1)]


def step2_needs_fix(
    step: dict,
    s1_v_type: str,
    s1_answer,
    tang1_src: dict,
    int_endpoints: list[str],
) -> bool:
    """
    Return True if a non-first LabelValidator step is missing a workspace or
    has any field that doesn't match the expected state derived from step 1.
    """
    p = step.get("prompt", {})
    if p.get("validator", {}).get("@type") != "LabelValidator":
        return False

    tang = (step.get("workspace") or {}).get("tangibles", [])

    # Missing workspace entirely
    if not tang or all(not t.get("ticks") and not t.get("intervals") for t in tang):
        return True

    expected_labels = tang1_src.get("labels", int_endpoints)
    expected_ticks_ro = tang1_src.get("ticks", int_endpoints)

    for t in tang:
        if not t.get("ticks") and not t.get("intervals"):
            continue
        if s1_v_type == "PointValidator":
            if t.get("points") != s1_answer:
                return True
        else:
            if t.get("ticks") != s1_answer:
                return True
        if t.get("labels") != expected_labels:
            return True
        tro = t.get("ticks_is_read_only")
        if not tro or tro is True or tro != expected_ticks_ro:
            return True

    return False


def needs_fix(seq: dict) -> bool:
    """Return True if this sequence has any non-first step that needs workspace creation or correction."""
    steps = seq.get("steps", [])
    if len(steps) < 2:
        return False

    s1 = steps[0]
    validator = s1.get("prompt", {}).get("validator", {})
    v_type = validator.get("@type")
    s1_answer = validator.get("answer")

    if v_type not in ("TickValidator", "PointValidator"):
        return False
    if v_type == "TickValidator" and not isinstance(s1_answer, (str, list)):
        return False
    if v_type == "PointValidator" and not isinstance(s1_answer, list):
        return False

    tang1 = (s1.get("workspace") or {}).get("tangibles", [])
    if not tang1:
        return False

    num_range = tang1[0].get("range", [0, 1])
    int_endpoints = endpoints_for_range(num_range)
    tang1_src = tang1[0]

    return any(
        step2_needs_fix(steps[si], v_type, s1_answer, tang1_src, int_endpoints)
        for si in range(1, len(steps))
    )


def fix_seq(seq: dict) -> int:
    """
    Mutate seq in place. Returns number of steps updated.
    For each non-first LabelValidator step:
      - If workspace is missing: build it from step 1
      - If workspace exists: update ticks/points, labels, ticks_is_read_only to match step 1
    """
    steps = seq.get("steps", [])
    s1 = steps[0]
    s1_validator = s1["prompt"]["validator"]
    s1_v_type = s1_validator.get("@type")
    s1_answer = s1_validator.get("answer")
    tang1 = (s1.get("workspace") or {}).get("tangibles", [])

    num_range = tang1[0].get("range", [0, 1]) if tang1 else [0, 1]
    int_endpoints = endpoints_for_range(num_range)
    tang1_src = tang1[0] if tang1 else {}
    fixed = 0

    for si in range(1, len(steps)):
        step = steps[si]
        p2 = step.get("prompt", {})
        if p2.get("validator", {}).get("@type") != "LabelValidator":
            continue

        if not step2_needs_fix(step, s1_v_type, s1_answer, tang1_src, int_endpoints):
            continue

        tang = (step.get("workspace") or {}).get("tangibles", [])

        if not tang or all(not t.get("ticks") and not t.get("intervals") for t in tang):
            # Workspace missing — build from step 1
            new_tangibles = []
            for i, t in enumerate(tang1):
                new_t = copy.deepcopy(t)
                if s1_v_type == "PointValidator":
                    new_t["points"] = s1_answer
                else:
                    new_t["ticks"] = s1_answer
                if not new_t.get("labels"):
                    new_t["labels"] = int_endpoints
                tro = new_t.get("ticks_is_read_only")
                if not tro or tro is True:
                    new_t["ticks_is_read_only"] = int_endpoints
                new_tangibles.append(new_t)

            if not step.get("workspace"):
                step["workspace"] = {"@type": "WorkspaceData", "tangibles": new_tangibles}
            else:
                step["workspace"]["tangibles"] = new_tangibles
        else:
            # Workspace exists — update fields to match expected state
            for i, t in enumerate(tang):
                if not t.get("ticks") and not t.get("intervals"):
                    continue
                src = tang1[i] if i < len(tang1) else tang1_src
                if s1_v_type == "PointValidator":
                    t["points"] = s1_answer
                else:
                    t["ticks"] = s1_answer
                t["labels"] = src.get("labels", int_endpoints)
                t["ticks_is_read_only"] = src.get("ticks", int_endpoints)

        fixed += 1

    return fixed


def step_missing_workspace(step: dict) -> bool:
    """Return True if a step has no workspace tangibles at all."""
    tangibles = (step.get("workspace") or {}).get("tangibles", [])
    return not tangibles


def scan_missing_workspaces(data: dict | list) -> list[str]:
    """
    Scan all multi-step sequences and return a line per sequence where any
    non-first step is missing a workspace entirely, regardless of pattern.
    """
    sequences = data.get("sequences", data) if isinstance(data, dict) else data
    issues = []

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        steps = seq.get("steps", [])
        if len(steps) < 2:
            continue

        missing = []
        for i in range(1, len(steps)):
            if step_missing_workspace(steps[i]):
                validator_type = (
                    steps[i].get("prompt", {}).get("validator", {}).get("@type", "?")
                )
                missing.append(f"step {i + 1} ({validator_type})")

        if missing:
            pid = seq.get("metadata", {}).get("problem_id", "?")
            tid = seq.get("metadata", {}).get("template_id", "?")
            issues.append(f"  pid={pid} tid={tid}: missing workspace in {', '.join(missing)}")

    return issues


def process_data(data: dict | list, dry_run: bool = False) -> tuple[int, list[str]]:
    sequences = data.get("sequences", data) if isinstance(data, dict) else data
    issues = []
    fixed = 0

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        if not needs_fix(seq):
            continue

        pid = seq.get("metadata", {}).get("problem_id", "?")
        v_type = seq["steps"][0]["prompt"]["validator"].get("@type", "?")
        issues.append(f"  pid={pid}: workspace needs update ({v_type})")

        if not dry_run:
            n = fix_seq(seq)
            fixed += n
            issues[-1] += f" -> FIXED ({n} step(s))"

    return fixed, issues


def process_file(
    path: Path, dry_run: bool, report_missing: bool = False
) -> tuple[int, list[str], list[str]]:
    """Returns (fixed_count, fix_issues, missing_issues)."""
    if not path.exists():
        return 0, [], []

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    fixed, fix_issues = process_data(data, dry_run=dry_run)
    missing_issues = scan_missing_workspaces(data) if report_missing else []

    if fixed > 0 and not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return fixed, fix_issues, missing_issues


def main():
    parser = argparse.ArgumentParser(
        description="Fix missing step-2 workspace in two-step partition sequences"
    )
    parser.add_argument(
        "--modules", type=int, nargs="+", default=DEFAULT_MODULES, metavar="N"
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--report-missing",
        action="store_true",
        help="Also flag all multi-step sequences where any non-first step is missing a workspace",
    )
    args = parser.parse_args()

    mode = "DRY RUN" if args.dry_run else "FIX MODE"
    print(f"fix_partition_step2_workspace -- {mode}")
    print(f"Modules: {args.modules}\n")

    total_fix_issues = 0
    total_fixed = 0
    total_missing_issues = 0

    for m in args.modules:
        module_dir = POOL_BASE / f"module_{m}"
        printed_header = False
        for filename in POOL_FILES:
            path = module_dir / filename
            fixed, fix_issues, missing_issues = process_file(
                path, dry_run=args.dry_run, report_missing=args.report_missing
            )
            if fix_issues or missing_issues:
                if not printed_header:
                    print(f"[module {m}]")
                    printed_header = True
                print(f"  {filename}:")
                for msg in fix_issues:
                    print(msg)
                if missing_issues:
                    print(f"    -- missing workspaces (all patterns) --")
                    for msg in missing_issues:
                        print(msg)
                total_fix_issues += len(fix_issues)
                total_fixed += fixed
                total_missing_issues += len(missing_issues)

    if total_fix_issues == 0 and total_missing_issues == 0:
        print("All modules OK (no issues found)")
    else:
        if total_fix_issues:
            print(f"\nTotal auto-fixable sequences: {total_fix_issues}")
            if not args.dry_run:
                print(f"Total steps fixed: {total_fixed}")
        if total_missing_issues:
            print(f"\nTotal sequences with missing workspaces (unfixed): {total_missing_issues}")


if __name__ == "__main__":
    main()
