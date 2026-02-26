"""
fix_select_answer_ambiguity.py

For sequences with a SelectionValidator where the first tangible is read-only
(reference bar), checks that:
  1. The answer index points to a tangible that actually matches the reference
     fraction. Flags as WRONG_ANSWER if not.
  2. No OTHER tangible also matches the reference fraction (ambiguous).
     Fixes ambiguous extras by randomly adding or removing one shaded interval.

Applies to both problem_pool.json and problem_pool_shuffled.json for all
modules in a given base directory.

Usage:
    python fix_select_answer_ambiguity.py [--modules 4 5 ... 12] [--dry-run]

Options:
    --modules   Module numbers to process (default: 4-12)
    --dry-run   Report issues without modifying files
"""

import argparse
import json
import random
import sys
from fractions import Fraction
from pathlib import Path


POOL_BASE = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")
DEFAULT_MODULES = list(range(4, 13))
POOL_FILES = ["problem_pool.json", "problem_pool_shuffled.json"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def bar_value(tangible: dict) -> Fraction | None:
    """Return the fraction value (shaded/total) of a bar tangible, or None."""
    intervals = tangible.get("intervals", "")
    shaded = tangible.get("intervals_is_shaded", [])
    if not intervals or shaded is None:
        return None
    try:
        num_str, den_str = intervals.split("/")
        num, den = int(num_str), int(den_str)
    except (ValueError, AttributeError):
        return None
    if den == 0:
        return None
    return Fraction(len(shaded) * num, den)


def normalize_answer(answer) -> list[int]:
    """Always return answer as a list of ints."""
    if isinstance(answer, list):
        return [int(a) for a in answer]
    return [int(answer)]


def fix_extra_tangible(tangible: dict, ref_val: Fraction) -> dict:
    """
    Mutate tangible in-place so its bar_value no longer equals ref_val.
    Randomly adds or removes one shaded interval (keeping contiguous shading).
    Returns the mutated tangible.
    """
    intervals = tangible.get("intervals", "")
    shaded = list(tangible.get("intervals_is_shaded", []))
    try:
        _, den_str = intervals.split("/")
        n = int(den_str)
    except (ValueError, AttributeError):
        return tangible  # can't fix without intervals

    k = len(shaded)  # current shaded count; shaded = [0, 1, ..., k-1]

    can_add = k < n
    can_remove = k > 0

    if not can_add and not can_remove:
        return tangible  # degenerate case, skip

    # Randomly pick direction, biased toward what's available
    choices = []
    if can_add:
        choices.append("add")
    if can_remove:
        choices.append("remove")

    direction = random.choice(choices)

    if direction == "add":
        new_shaded = list(range(k + 1))
    else:
        new_shaded = list(range(k - 1))

    tangible["intervals_is_shaded"] = new_shaded
    return tangible


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def is_bar(tangible: dict) -> bool:
    """Return True if the tangible is a bar-type NumLine (has interval shading)."""
    return (
        tangible.get("visual") == "bar"
        or tangible.get("intervals") is not None
        or tangible.get("intervals_is_shaded") is not None
    )


def process_data(data: dict | list, dry_run: bool = False) -> tuple[int, list[str]]:
    """
    Scan sequences for SelectionValidator issues and fix ambiguous extras.
    Only inspects steps where the reference tangible is a bar-type NumLine.
    Returns (num_fixed, list_of_issue_messages).
    """
    sequences = data.get("sequences", data) if isinstance(data, dict) else data
    issues = []
    fixed = 0

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        pid = seq.get("metadata", {}).get("problem_id", "?")

        for step in seq.get("steps", []):
            if not isinstance(step, dict):
                continue
            prompt = step.get("prompt", {})
            validator = prompt.get("validator", {})
            tool = prompt.get("tool", {})

            if validator.get("@type") != "SelectionValidator":
                continue
            if tool.get("@type") != "Select":
                continue

            tangibles = step.get("workspace", {}).get("tangibles", [])
            if not tangibles:
                continue

            # Must have a reference bar (is_read_only: true) that is a bar visual
            ref_indices = [
                i for i, t in enumerate(tangibles)
                if t.get("is_read_only") and is_bar(t)
            ]
            if not ref_indices:
                continue  # no bar reference — skip (may be line-type or no reference)

            ref_tang = tangibles[ref_indices[0]]
            ref_val = bar_value(ref_tang)
            if ref_val is None:
                continue  # reference bar has incomplete data — skip silently

            answer_indices = normalize_answer(validator["answer"])

            # --- Check 1: intended answer bar(s) must match reference ---
            for idx in answer_indices:
                if idx >= len(tangibles):
                    issues.append(
                        f"  pid={pid}: answer idx={idx} is out of range "
                        f"(tangibles={len(tangibles)}) — WRONG_ANSWER"
                    )
                    continue
                t = tangibles[idx]
                if t.get("is_read_only"):
                    issues.append(
                        f"  pid={pid}: answer idx={idx} points to the read-only "
                        f"reference bar — WRONG_ANSWER"
                    )
                    continue
                if not is_bar(t):
                    continue  # non-bar tangible (line type) — skip fraction check
                actual_val = bar_value(t)
                if actual_val is None:
                    issues.append(
                        f"  pid={pid}: answer idx={idx} bar has no valid fraction "
                        f"(intervals={t.get('intervals')!r} "
                        f"shaded={t.get('intervals_is_shaded')}) — WRONG_ANSWER"
                    )
                elif actual_val != ref_val:
                    issues.append(
                        f"  pid={pid}: answer idx={idx} value={actual_val} "
                        f"!= reference={ref_val} — WRONG_ANSWER (cannot auto-fix)"
                    )

            # --- Check 2: extra bar tangibles that also match reference ---
            intended_set = set(answer_indices)
            extras = []
            for i, t in enumerate(tangibles):
                if i in intended_set:
                    continue
                if t.get("is_read_only"):
                    continue
                if not is_bar(t):
                    continue  # skip non-bar tangibles
                if bar_value(t) == ref_val:
                    extras.append(i)

            if extras:
                issues.append(
                    f"  pid={pid}: ref={ref_val} answer={validator['answer']} "
                    f"AMBIGUOUS — extra matching bar tangibles at idx={extras}"
                )
                if not dry_run:
                    for idx in extras:
                        fix_extra_tangible(tangibles[idx], ref_val)
                        fixed += 1
                    issues[-1] += " -> FIXED"

    return fixed, issues


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

def process_file(path: Path, dry_run: bool) -> tuple[int, list[str]]:
    if not path.exists():
        return 0, [f"  SKIP {path.name} — not found"]

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    fixed, issues = process_data(data, dry_run=dry_run)

    if fixed > 0 and not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return fixed, issues


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Check and fix SelectionValidator answer ambiguity in problem pools"
    )
    parser.add_argument(
        "--modules",
        type=int,
        nargs="+",
        default=DEFAULT_MODULES,
        metavar="N",
        help="Module numbers to process (default: 4-12)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report issues without modifying files",
    )
    args = parser.parse_args()

    mode = "DRY RUN" if args.dry_run else "FIX MODE"
    print(f"fix_select_answer_ambiguity — {mode}")
    print(f"Modules: {args.modules}\n")

    total_issues = 0
    total_fixed = 0

    for m in args.modules:
        module_dir = POOL_BASE / f"module_{m}"
        print(f"[module {m}]")
        for filename in POOL_FILES:
            path = module_dir / filename
            fixed, issues = process_file(path, dry_run=args.dry_run)
            if issues:
                print(f"  {filename}:")
                for msg in issues:
                    print(msg)
                total_issues += len(issues)
                total_fixed += fixed
            else:
                if path.exists():
                    print(f"  {filename}: OK (no issues)")

    print(f"\nTotal issues: {total_issues}")
    if not args.dry_run:
        print(f"Total tangibles fixed: {total_fixed}")


if __name__ == "__main__":
    main()
