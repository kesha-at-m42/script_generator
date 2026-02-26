"""
Shuffles problem_pool.json for modules 4-12 to maximize variety across
skill, template, and mastery tier.

Output: same directory as input, named problem_pool_shuffled.json

Usage:
  python shuffle_problem_pools.py [--seed N] [--modules 4 5 6 ...]
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from any directory
sys.path.insert(0, str(Path(__file__).parent.parent))
from steps.formatting.sequence_shuffler import shuffle_for_variety, _get_meta, TIER_ORDER
from collections import defaultdict

POOL_BASE = Path("C:/git/launchpad/project/edtech.apl/resources/sequences")
DEFAULT_MODULES = list(range(4, 13))


def consecutive_repeats(seqs, key_fn):
    return sum(
        1 for i in range(1, len(seqs))
        if key_fn(seqs[i]) == key_fn(seqs[i - 1])
    )


def variety_report(before, after):
    get_tid = lambda s: _get_meta(s).get("template_id", "")
    get_sid = lambda s: _get_meta(s).get("skill_id", "")

    tiers_before = defaultdict(list)
    tiers_after = defaultdict(list)
    for seq in before:
        tiers_before[_get_meta(seq).get("mastery_tier", "UNKNOWN")].append(seq)
    for seq in after:
        tiers_after[_get_meta(seq).get("mastery_tier", "UNKNOWN")].append(seq)

    all_tiers = [t for t in TIER_ORDER if t in tiers_after]
    all_tiers += [t for t in tiers_after if t not in TIER_ORDER]

    lines = []
    for tier in all_tiers:
        b = tiers_before.get(tier, [])
        a = tiers_after[tier]
        for label, fn in [("template_id", get_tid), ("skill_id", get_sid)]:
            bv = consecutive_repeats(b, fn) if b else "-"
            av = consecutive_repeats(a, fn)
            ok = "v" if not isinstance(bv, int) or av <= bv else "!"
            lines.append(f"      {ok} [{tier}] {label}: {bv} -> {av}")
    return "\n".join(lines)


def process_module(module_number, seed=None):
    input_path = POOL_BASE / f"module_{module_number}" / "problem_pool.json"
    output_path = input_path.parent / "problem_pool_shuffled.json"

    if not input_path.exists():
        print(f"  [module {module_number}] SKIP — file not found: {input_path}")
        return False

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    before = list(data.get("sequences", []))
    result = shuffle_for_variety(data, seed=seed)
    after = result.get("sequences", [])

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"  [module {module_number}] {len(after)} sequences -> {output_path.name}")
    if before:
        print(variety_report(before, after))

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Shuffle problem_pool.json for modules 4-12"
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
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible shuffling",
    )
    args = parser.parse_args()

    print(f"Shuffling modules: {args.modules}")
    if args.seed is not None:
        print(f"Seed: {args.seed}")
    print()

    ok = 0
    for m in args.modules:
        if process_module(m, seed=args.seed):
            ok += 1

    print(f"\nDone: {ok}/{len(args.modules)} modules shuffled.")


if __name__ == "__main__":
    main()
