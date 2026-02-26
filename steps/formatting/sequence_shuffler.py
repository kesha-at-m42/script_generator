"""
Sequence Shuffler - Shuffles sequences to maximize variety across skill, template, and mastery tier.

The adaptive algorithm selects sequences by tier based on student performance:
  Start → Baseline → (2 correct) → Stretch → (2 correct) → Challenge
          Baseline/Stretch → (2 incorrect) → Support → (1 incorrect) → Confidence
          Support/Confidence → (1 correct) → Baseline

Since the algorithm draws from each tier's queue independently, variety is maximized
within each tier. Within each tier, a skill-aware round-robin ensures:
  - All templates appear before any repeats (round-robin guarantee)
  - Same-skill templates are spread as far apart as possible
  - Sequences within each template are randomized

Tier output order: BASELINE → STRETCH → CHALLENGE → SUPPORT → CONFIDENCE

Can be used as a pipeline step or run directly on a file:
  python -m steps.formatting.sequence_shuffler <input.json> [output.json] [--seed N]
"""

import json
import random
import sys
from collections import defaultdict, deque


# Output order reflects the adaptive flow
TIER_ORDER = ["BASELINE", "STRETCH", "CHALLENGE", "SUPPORT", "CONFIDENCE"]


def _get_meta(seq):
    return seq.get("metadata", {})


def _build_template_order(skill_of_template):
    """
    Return template_ids ordered so templates sharing the same skill_id
    are spread as far apart as possible.

    Groups templates by skill_id, shuffles within each group, then
    round-robins across skill groups (largest first).
    """
    by_skill = defaultdict(list)
    for tid, sid in skill_of_template.items():
        by_skill[sid].append(tid)

    for tids in by_skill.values():
        random.shuffle(tids)

    skill_groups = sorted(by_skill.values(), key=len, reverse=True)
    random.shuffle(skill_groups)

    template_order = []
    max_len = max(len(g) for g in skill_groups)
    for i in range(max_len):
        for group in skill_groups:
            if i < len(group):
                template_order.append(group[i])

    return template_order


def _shuffle_tier(seqs):
    """
    Shuffle a single tier's sequences using skill-aware round-robin across templates.
    Guarantees all templates appear before any template repeats.
    """
    by_template = defaultdict(list)
    skill_of_template = {}

    for seq in seqs:
        meta = _get_meta(seq)
        tid = meta.get("template_id", "unknown")
        sid = meta.get("skill_id", "unknown")
        by_template[tid].append(seq)
        skill_of_template[tid] = sid

    for template_seqs in by_template.values():
        random.shuffle(template_seqs)

    template_order = _build_template_order(skill_of_template)
    template_queues = [deque(by_template[tid]) for tid in template_order]

    result = []
    while any(template_queues):
        for q in template_queues:
            if q:
                result.append(q.popleft())
    return result


def shuffle_for_variety(data, seed=None, module_number=None, path_letter=None):
    """
    Shuffle sequences in a SequencePool to maximize variety across
    skill_id, template_id, and mastery_tier.

    Shuffles within each mastery tier independently (since the adaptive
    algorithm draws from each tier's queue based on student performance).
    Within each tier, all templates appear before any template repeats.

    Args:
        data: SequencePool dict with "@type" and "sequences"
        seed: Optional int for reproducible shuffling
        module_number: Passed automatically by pipeline (unused)
        path_letter: Passed automatically by pipeline (unused)

    Returns:
        SequencePool dict with sequences reordered for maximum variety
    """
    if not isinstance(data, dict) or data.get("@type") != "SequencePool":
        raise ValueError("Expected SequencePool with @type='SequencePool' and sequences array")

    if seed is not None:
        random.seed(seed)

    sequences = data.get("sequences", [])
    if not sequences:
        return data

    # Group by mastery_tier
    by_tier = defaultdict(list)
    for seq in sequences:
        tier = _get_meta(seq).get("mastery_tier", "UNKNOWN")
        by_tier[tier].append(seq)

    # Shuffle within each tier independently
    shuffled_tiers = {tier: _shuffle_tier(seqs) for tier, seqs in by_tier.items()}

    # Combine in adaptive flow order
    result = []
    for tier in TIER_ORDER:
        if tier in shuffled_tiers:
            result.extend(shuffled_tiers.pop(tier))
    # Any unexpected tiers go at the end
    for seqs in shuffled_tiers.values():
        result.extend(seqs)

    # Preserve all non-sequence fields from the original SequencePool
    output = {"@type": "SequencePool"}
    for key, value in data.items():
        if key not in ("@type", "sequences"):
            output[key] = value
    output["sequences"] = result

    return output


# ---------------------------------------------------------------------------
# CLI entrypoint for direct file use
# ---------------------------------------------------------------------------

def _parse_args(argv):
    import argparse
    parser = argparse.ArgumentParser(
        description="Shuffle a SequencePool JSON file to maximize skill/template variety per tier"
    )
    parser.add_argument("input", help="Path to input SequencePool JSON file")
    parser.add_argument(
        "output",
        nargs="?",
        help="Path for output JSON file (default: overwrites input)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible shuffling",
    )
    return parser.parse_args(argv)


def _print_variety_report(before, after):
    """Print consecutive repeat counts per identifier, broken down by tier."""
    def consecutive_repeats(seqs, key_fn):
        return sum(
            1 for i in range(1, len(seqs))
            if key_fn(seqs[i]) == key_fn(seqs[i - 1])
        )

    get_tid = lambda s: _get_meta(s).get("template_id", "")
    get_sid = lambda s: _get_meta(s).get("skill_id", "")

    # Per-tier breakdown
    tiers_after = defaultdict(list)
    for seq in after:
        tier = _get_meta(seq).get("mastery_tier", "UNKNOWN")
        tiers_after[tier].append(seq)

    tiers_before = defaultdict(list)
    for seq in before:
        tier = _get_meta(seq).get("mastery_tier", "UNKNOWN")
        tiers_before[tier].append(seq)

    print("  Variety report (consecutive repeats within each tier — lower is better):")
    for tier in TIER_ORDER + [t for t in tiers_after if t not in TIER_ORDER]:
        if tier not in tiers_after:
            continue
        b_seqs = tiers_before.get(tier, [])
        a_seqs = tiers_after[tier]
        for label, fn in [("template_id", get_tid), ("skill_id", get_sid)]:
            b = consecutive_repeats(b_seqs, fn) if b_seqs else "-"
            a = consecutive_repeats(a_seqs, fn)
            ok = "v" if not isinstance(b, int) or a <= b else "!"
            print(f"    {ok} [{tier}] {label}: {b} -> {a}")


if __name__ == "__main__":
    args = _parse_args(sys.argv[1:])

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)

    before = list(data.get("sequences", []))
    result = shuffle_for_variety(data, seed=args.seed)
    after = result.get("sequences", [])

    out_path = args.output or args.input
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Shuffled {len(after)} sequences -> {out_path}")
    if before:
        _print_variety_report(before, after)
