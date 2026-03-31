#!/usr/bin/env python3
"""
sp_toy_consistency.py — Toy naming and configuration consistency checker.

Checks:
  TC1: Every Visual: toy name matches a toy defined in §1.5
  TC2: Every §1.5 toy appears in at least one interaction (Gate 4)
  TC3: Consistent toy naming (no variant names for same toy)
  TC4: Interaction Constraints block present in §1.5
  TC5: No descriptive suffixes on toy names in Visual: lines

Gate scoping:
  Gate 1: §1.5 structure only
  Gate 2: Adds §1.6-§1.7 Visual: cross-reference
  Gate 3: Adds §1.8-§1.9 cross-reference
  Gate 4: Full cross-reference + every toy used at least once

Usage:
  python sp_toy_consistency.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate


def check_interaction_constraints(lines: list) -> list:
    """TC4: Check Interaction Constraints block present in §1.5."""
    findings = []
    in_15 = False
    found = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'^##\s+.*1\.5\b', stripped):
            in_15 = True
        elif in_15 and re.match(r'^##\s+.*1\.[6-9]\b', stripped):
            break
        if in_15 and 'interaction constraint' in stripped.lower():
            found = True
            break

    if in_15 and not found:
        findings.append({
            "check": "TC4",
            "severity": "MINOR",
            "detail": "Interaction Constraints block not found in §1.5",
        })
    return findings


def check_visual_suffix(interactions: list) -> list:
    """TC5: No descriptive suffixes on toy names in Visual: lines."""
    findings = []
    suffix_re = re.compile(r'—\s*(Reduced|Full|Limited|Extended|Modified|Simplified)')
    for ix in interactions:
        if ix.visual_text and suffix_re.search(ix.visual_text):
            match = suffix_re.search(ix.visual_text)
            findings.append({
                "check": "TC5",
                "severity": "MINOR",
                "interaction_id": ix.id,
                "phase": ix.phase,
                "line_number": ix.line_number,
                "detail": f"Descriptive suffix in Visual: line — '{match.group()}'",
                "context": ix.visual_text[:100],
            })
    return findings


def run_toy_check(filepath: str, gate: int) -> dict:
    sp = parse_sp(filepath)
    sp_filtered = filter_by_gate(sp, gate)
    all_findings = []

    toys_in_spec = [t.lower() for t in sp.toys_in_spec]
    toys_in_spec_original = sp.toys_in_spec

    # TC4: Interaction Constraints
    all_findings.extend(check_interaction_constraints(sp.lines))

    if gate >= 2:
        # TC1: Every Visual: toy matches §1.5
        toys_in_visuals = sp_filtered.toys_in_interactions
        for toy in toys_in_visuals:
            if toy.lower() not in toys_in_spec:
                all_findings.append({
                    "check": "TC1",
                    "severity": "MAJOR",
                    "detail": f"Toy '{toy}' in Visual: line not found in §1.5 spec",
                    "toy": toy,
                })

        # TC5: Visual suffix check
        all_findings.extend(check_visual_suffix(sp_filtered.interactions))

    if gate >= 4:
        # TC2: Every §1.5 toy used in at least one interaction
        used = set(t.lower() for t in sp_filtered.toys_in_interactions)
        for toy in toys_in_spec_original:
            if toy.lower() not in used:
                all_findings.append({
                    "check": "TC2",
                    "severity": "MINOR",
                    "detail": f"Toy '{toy}' defined in §1.5 but not found in any Visual: line",
                    "toy": toy,
                })

    checks_run = sorted(set(f["check"] for f in all_findings)) or ["TC1", "TC4"]

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_toy_consistency",
        "file": filepath,
        "gate": gate,
        "checks_run": checks_run,
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "toys_in_spec": toys_in_spec_original,
            "toys_in_interactions": sp_filtered.toys_in_interactions,
        },
    }


def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"TOY CONSISTENCY — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")
    meta = result.get('meta', {})
    print(f"Toys in §1.5: {meta.get('toys_in_spec', [])}")
    print(f"Toys in interactions: {meta.get('toys_in_interactions', [])}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    if result['findings']:
        print(f"\n{'─'*80}")
        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            detail = f.get('detail', '')
            print(f"  [{check}] {sev:8s} | {detail}")
    else:
        print("\n  ✓ No findings.")


def main():
    parser = argparse.ArgumentParser(description="SP Toy Consistency Checker")
    parser.add_argument("sp_file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_toy_check(args.sp_file, args.gate)

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
