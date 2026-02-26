"""
Applies add_shuffle_tangibles_for_select to problem_pool.json and
problem_pool_shuffled.json for modules 4-12, modifying files in place.

Usage:
  python add_shuffle_tangibles.py [--modules 4 5 6 ...]
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from steps.formatting.sequence_schema_fixer import add_shuffle_tangibles_for_select

POOL_BASE = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")
DEFAULT_MODULES = list(range(4, 13))
POOL_FILES = ["problem_pool.json", "problem_pool_shuffled.json"]


def count_shuffle_tangibles(data):
    count = 0
    for seq in data.get("sequences", []):
        for step in seq.get("steps", []):
            if step.get("workspace", {}).get("shuffle_tangibles"):
                count += 1
    return count


def process_file(path):
    if not path.exists():
        return None, "not found"

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    before = count_shuffle_tangibles(data)
    result = add_shuffle_tangibles_for_select(data)
    after = count_shuffle_tangibles(result)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    added = after - before
    return added, None


def main():
    parser = argparse.ArgumentParser(
        description="Add shuffle_tangibles to problem pool files for modules 4-12"
    )
    parser.add_argument(
        "--modules",
        type=int,
        nargs="+",
        default=DEFAULT_MODULES,
        metavar="N",
        help="Module numbers to process (default: 4-12)",
    )
    args = parser.parse_args()

    print(f"Modules: {args.modules}\n")

    for m in args.modules:
        module_dir = POOL_BASE / f"module_{m}"
        print(f"  [module {m}]")
        for filename in POOL_FILES:
            path = module_dir / filename
            added, err = process_file(path)
            if err:
                print(f"    SKIP {filename} — {err}")
            else:
                print(f"    OK   {filename} (+{added} shuffle_tangibles)")

    print("\nDone.")


if __name__ == "__main__":
    main()
