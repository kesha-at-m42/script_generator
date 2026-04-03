#!/usr/bin/env python3
"""
sp_timing_estimate.py — Ballpark phase timing estimator for Starter Packs.

Rough heuristics to catch obviously over- or under-scoped phases.
NOT authoritative timing predictions.

Heuristics per interaction:
  teaching_only: ~20-30s
  student_action: ~30-60s  (MC ~45-60s, free response ~30-45s)
  system_driven: ~15-20s
  multi_step: ~60-90s

Targets (Activity Queue Rulebook):
  Warmup: 2-3 min (hard cap: 5 min)
  Lesson: 8-10 min
  EC: 3-4 min
  Practice: 5-8 min
  Synthesis: 5-7 min
  Total session: ~25-30 min

Gate scoping:
  Gate 1: Skipped
  Gate 2: Warmup + Lesson
  Gate 3+: All phases, full session estimate

Usage:
  python sp_timing_estimate.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate


# ---------------------------------------------------------------------------
# Timing heuristics (seconds)
# ---------------------------------------------------------------------------

TIMING_HEURISTICS = {
    "teaching_only": (20, 30),
    "student_action": (30, 60),
    "system_driven": (15, 20),
    "unknown": (30, 45),
}

# MC interactions take longer
MC_BONUS = (15, 15)  # extra seconds for MC

# Phase targets in minutes
PHASE_TARGETS = {
    "Warmup": (2, 3, 5),      # min, max, hard_cap
    "Lesson": (8, 14, 16),
    "EC": (3, 4, 6),
    "Practice": (5, 8, 12),
    "Synthesis": (5, 7, 9),
}

SESSION_TARGET = (25, 30)


# ---------------------------------------------------------------------------
# Estimation
# ---------------------------------------------------------------------------

def estimate_interaction_time(ix) -> tuple:
    """Return (min_seconds, max_seconds) for an interaction."""
    base = TIMING_HEURISTICS.get(ix.pattern, (30, 45))
    lo, hi = base

    # MC bonus
    if ix.has_options:
        lo += MC_BONUS[0]
        hi += MC_BONUS[1]

    # Multi-step bonus
    if ix.is_multi_step or len(ix.sub_parts) > 1:
        lo = int(lo * 1.5)
        hi = int(hi * 1.5)

    return lo, hi


def estimate_phase(interactions: list) -> dict:
    """Estimate timing for a group of interactions in one phase."""
    total_lo = 0
    total_hi = 0
    details = []

    for ix in interactions:
        lo, hi = estimate_interaction_time(ix)
        total_lo += lo
        total_hi += hi
        details.append({
            "id": ix.id,
            "title": ix.title[:50],
            "pattern": ix.pattern,
            "has_mc": ix.has_options,
            "est_seconds": f"{lo}-{hi}",
        })

    return {
        "interaction_count": len(interactions),
        "est_min_seconds": total_lo,
        "est_max_seconds": total_hi,
        "est_min_minutes": round(total_lo / 60, 1),
        "est_max_minutes": round(total_hi / 60, 1),
        "details": details,
    }


def run_timing_estimate(filepath: str, gate: int) -> dict:
    sp = parse_sp(filepath)

    if gate == 1:
        return {
            "checker": "sp_timing_estimate",
            "file": filepath,
            "gate": gate,
            "checks_run": [],
            "total_findings": 0,
            "severity_counts": {},
            "check_counts": {},
            "findings": [],
            "meta": {"note": "Gate 1 — no interactions to time"},
        }

    sp_filtered = filter_by_gate(sp, gate)
    all_findings = []

    # Group interactions by phase
    phase_groups = {}
    for ix in sp_filtered.interactions:
        phase_groups.setdefault(ix.phase, []).append(ix)

    phase_estimates = {}
    for phase, interactions in phase_groups.items():
        est = estimate_phase(interactions)
        phase_estimates[phase] = est

        # Check against targets
        if phase in PHASE_TARGETS:
            target_min, target_max, hard_cap = PHASE_TARGETS[phase]

            if est["est_min_minutes"] > hard_cap:
                all_findings.append({
                    "check": "TM1",
                    "severity": "CRITICAL",
                    "phase": phase,
                    "detail": f"{phase} estimated {est['est_min_minutes']}-{est['est_max_minutes']} min "
                             f"(hard cap: {hard_cap} min)",
                    "est_min": est["est_min_minutes"],
                    "est_max": est["est_max_minutes"],
                    "target_max": target_max,
                    "hard_cap": hard_cap,
                })
            elif est["est_min_minutes"] > target_max:
                all_findings.append({
                    "check": "TM1",
                    "severity": "MAJOR",
                    "phase": phase,
                    "detail": f"{phase} estimated {est['est_min_minutes']}-{est['est_max_minutes']} min "
                             f"(target: {target_min}-{target_max} min)",
                    "est_min": est["est_min_minutes"],
                    "est_max": est["est_max_minutes"],
                })
            elif est["est_max_minutes"] < target_min:
                all_findings.append({
                    "check": "TM1",
                    "severity": "MINOR",
                    "phase": phase,
                    "detail": f"{phase} estimated {est['est_min_minutes']}-{est['est_max_minutes']} min "
                             f"(target: {target_min}-{target_max} min) — may be under-scoped",
                    "est_min": est["est_min_minutes"],
                    "est_max": est["est_max_minutes"],
                })

    # Session total (gate 3+)
    if gate >= 3:
        total_lo = sum(e["est_min_minutes"] for e in phase_estimates.values())
        total_hi = sum(e["est_max_minutes"] for e in phase_estimates.values())

        if total_hi > SESSION_TARGET[1] * 1.3:
            all_findings.append({
                "check": "TM2",
                "severity": "MAJOR",
                "detail": f"Total session estimated {total_lo:.1f}-{total_hi:.1f} min "
                         f"(target: {SESSION_TARGET[0]}-{SESSION_TARGET[1]} min)",
            })
        elif total_lo < SESSION_TARGET[0] * 0.7:
            all_findings.append({
                "check": "TM2",
                "severity": "MINOR",
                "detail": f"Total session estimated {total_lo:.1f}-{total_hi:.1f} min "
                         f"(target: {SESSION_TARGET[0]}-{SESSION_TARGET[1]} min) — may be under-scoped",
            })

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_timing_estimate",
        "file": filepath,
        "gate": gate,
        "checks_run": sorted(set(f["check"] for f in all_findings)) or ["TM1", "TM2"],
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "phase_estimates": {k: {kk: vv for kk, vv in v.items() if kk != "details"}
                               for k, v in phase_estimates.items()},
            "session_total_min": round(sum(e["est_min_minutes"] for e in phase_estimates.values()), 1),
            "session_total_max": round(sum(e["est_max_minutes"] for e in phase_estimates.values()), 1),
        },
    }


def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"TIMING ESTIMATE — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")

    meta = result.get('meta', {})
    estimates = meta.get('phase_estimates', {})

    if estimates:
        print("\nPhase Timing Estimates:")
        for phase, est in sorted(estimates.items()):
            target = PHASE_TARGETS.get(phase)
            target_str = f" (target: {target[0]}-{target[1]} min)" if target else ""
            print(f"  {phase:12s}: {est['est_min_minutes']:.1f}-{est['est_max_minutes']:.1f} min "
                  f"({est['interaction_count']} interactions){target_str}")

        total_lo = meta.get('session_total_min', 0)
        total_hi = meta.get('session_total_max', 0)
        print(f"\n  {'TOTAL':12s}: {total_lo:.1f}-{total_hi:.1f} min "
              f"(target: {SESSION_TARGET[0]}-{SESSION_TARGET[1]} min)")

    print(f"\nFindings: {result['total_findings']}")
    if result['findings']:
        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            detail = f.get('detail', '')
            print(f"  [{check}] {sev:8s} | {detail}")
    else:
        print("  ✓ All phases within expected ranges.")


def main():
    parser = argparse.ArgumentParser(description="SP Timing Estimator")
    parser.add_argument("sp_file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_timing_estimate(args.sp_file, args.gate)

    if args.json or args.output:
        json_str = json.dumps(result, indent=2)
        if args.output:
            os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
            with open(args.output, 'w') as f:
                f.write(json_str)
            print(f"Output written to {args.output}")
        if args.json:
            print(json_str)
    else:
        print_findings_table(result)


if __name__ == '__main__':
    main()
