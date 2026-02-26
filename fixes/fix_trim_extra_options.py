"""
fix_trim_extra_options.py

Finds questions where choices.options has more than 7 entries and removes
one option that is not in the answer, updating answer indices accordingly.

Usage:
    python fix_trim_extra_options.py [--modules 4 5 ...] [--dry-run]
"""

import argparse
import json
import random
from pathlib import Path


POOL_BASE = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")
DEFAULT_MODULES = list(range(4, 13))
POOL_FILES = ["problem_pool.json", "problem_pool_shuffled.json"]


def process_data(data: dict | list, dry_run: bool = False) -> tuple[int, list[str]]:
    sequences = data.get("sequences", data) if isinstance(data, dict) else data
    issues = []
    fixed = 0

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        pid = seq.get("metadata", {}).get("problem_id", "?")

        for step in seq.get("steps", []):
            prompt = step.get("prompt", {})
            choices = prompt.get("choices", {})
            options = choices.get("options")
            if not isinstance(options, list) or len(options) <= 7:
                continue

            validator = prompt.get("validator", {})
            answer = validator.get("answer", [])
            answer_set = set(answer) if isinstance(answer, list) else {answer}

            non_answer = [i for i in range(len(options)) if i not in answer_set]
            if not non_answer:
                issues.append(f"  pid={pid}: {len(options)} options but all are in answer -- skipped")
                continue

            # Pick a random non-answer index to remove
            remove_idx = random.choice(non_answer)
            removed_val = options[remove_idx]

            issues.append(
                f"  pid={pid}: {len(options)} options, answer={answer}, "
                f"removing idx={remove_idx} ({removed_val!r})"
            )

            if not dry_run:
                # Remove the option
                options.pop(remove_idx)

                # Update answer indices: any index > remove_idx shifts down by 1
                if isinstance(answer, list):
                    validator["answer"] = [
                        a - 1 if a > remove_idx else a for a in answer
                    ]
                elif isinstance(answer, int) and answer > remove_idx:
                    validator["answer"] = answer - 1

                fixed += 1
                issues[-1] += " -> FIXED"

    return fixed, issues


def process_file(path: Path, dry_run: bool) -> tuple[int, list[str]]:
    if not path.exists():
        return 0, []

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    fixed, issues = process_data(data, dry_run=dry_run)

    if fixed > 0 and not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    return fixed, issues


def main():
    parser = argparse.ArgumentParser(
        description="Trim options arrays with more than 7 entries"
    )
    parser.add_argument(
        "--modules", type=int, nargs="+", default=DEFAULT_MODULES, metavar="N"
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    mode = "DRY RUN" if args.dry_run else "FIX MODE"
    print(f"fix_trim_extra_options -- {mode}")
    print(f"Modules: {args.modules}\n")

    total_issues = 0
    total_fixed = 0

    for m in args.modules:
        module_dir = POOL_BASE / f"module_{m}"
        printed_header = False
        for filename in POOL_FILES:
            path = module_dir / filename
            fixed, issues = process_file(path, dry_run=args.dry_run)
            if issues:
                if not printed_header:
                    print(f"[module {m}]")
                    printed_header = True
                print(f"  {filename}:")
                for msg in issues:
                    print(msg)
                total_issues += len(issues)
                total_fixed += fixed

    if total_issues == 0:
        print("All modules OK (no issues found)")
    else:
        print(f"\nTotal flagged: {total_issues}")
        if not args.dry_run:
            print(f"Total fixed: {total_fixed}")


if __name__ == "__main__":
    main()
