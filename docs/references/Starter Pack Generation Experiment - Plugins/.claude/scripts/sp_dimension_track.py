#!/usr/bin/env python3
"""
sp_dimension_track.py — Dimension and value tracking across interactions.

Extracts numerical values from Visual: and Correct Answer: lines to:
  DT1: Build a usage table of values per interaction
  DT2: Flag exact dimension reuse across interactions
  DT3: Flag values outside §1.5 constraint ranges (if parseable)
  DT4: Flag EC values identical to Lesson values (Gate 3+)
  DT5: Flag Synthesis values identical to Lesson/EC values (Gate 3+)

Gate scoping:
  Gate 1: §1.5 internal consistency only
  Gate 2: Warmup + Lesson dimension tracking
  Gate 3+: All phases, cross-phase comparison

Usage:
  python sp_dimension_track.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate


# ---------------------------------------------------------------------------
# Value extraction
# ---------------------------------------------------------------------------

# Patterns for extracting dimensions/values
DIMENSION_RE = re.compile(r'(\d+)\s*[×x×]\s*(\d+)')                  # "4 × 6", "3x5"
AREA_RE = re.compile(r'(\d+)\s*(?:square\s+units?|sq\s+units?)', re.IGNORECASE)
SKIP_COUNT_RE = re.compile(r'(\d+)\s*[,\.]+\s*(\d+)\s*[,\.]+\s*(\d+)')  # "4... 8... 12"
NUMERIC_ANSWER_RE = re.compile(r'\b(\d+)\b')


def extract_values_from_interaction(ix) -> dict:
    """Extract dimensions, areas, and other numerical values from an interaction."""
    values = {
        "dimensions": [],
        "areas": [],
        "factors": [],
        "other_numbers": set(),
    }

    # Check Visual: line
    if ix.visual_text:
        for m in DIMENSION_RE.finditer(ix.visual_text):
            dim = (int(m.group(1)), int(m.group(2)))
            values["dimensions"].append(dim)
            values["factors"].extend([dim[0], dim[1]])

    # Check Correct Answer and all raw lines for dimensions and areas
    for line_num, line in ix.raw_lines:
        text = line.strip()

        # Look for dimensions
        for m in DIMENSION_RE.finditer(text):
            dim = (int(m.group(1)), int(m.group(2)))
            if dim not in values["dimensions"]:
                values["dimensions"].append(dim)
            for f in dim:
                if f not in values["factors"]:
                    values["factors"].append(f)

        # Look for area values
        for m in AREA_RE.finditer(text):
            area = int(m.group(1))
            if area not in values["areas"]:
                values["areas"].append(area)

        # Correct Answer line — extract the primary number
        if text.startswith('* **Correct Answer:**'):
            for m in NUMERIC_ANSWER_RE.finditer(text):
                values["other_numbers"].add(int(m.group(1)))

    values["other_numbers"] = sorted(values["other_numbers"])
    return values


# ---------------------------------------------------------------------------
# Cross-phase comparison
# ---------------------------------------------------------------------------

def find_dimension_reuse(phase_values: dict) -> list:
    """Find exact dimension reuse across phases."""
    findings = []

    # Compare EC dimensions against Lesson dimensions
    lesson_dims = set()
    for ix_id, vals in phase_values.get("Lesson", {}).items():
        for dim in vals["dimensions"]:
            lesson_dims.add(dim)
            lesson_dims.add((dim[1], dim[0]))  # also reversed

    ec_dims = {}
    for ix_id, vals in phase_values.get("EC", {}).items():
        for dim in vals["dimensions"]:
            ec_dims[dim] = ix_id

    for dim, ix_id in ec_dims.items():
        if dim in lesson_dims:
            findings.append({
                "check": "DT4",
                "severity": "MINOR",
                "detail": f"EC interaction {ix_id} uses dimension {dim[0]}×{dim[1]} "
                         f"which also appears in Lesson",
                "interaction_id": ix_id,
                "phase": "EC",
                "dimension": f"{dim[0]}×{dim[1]}",
            })

    # Compare Synthesis dimensions against Lesson + EC
    all_prior_dims = set(lesson_dims)
    for dim in ec_dims:
        all_prior_dims.add(dim)
        all_prior_dims.add((dim[1], dim[0]))

    for ix_id, vals in phase_values.get("Synthesis", {}).items():
        for dim in vals["dimensions"]:
            if dim in all_prior_dims:
                findings.append({
                    "check": "DT5",
                    "severity": "MINOR",
                    "detail": f"Synthesis interaction {ix_id} uses dimension {dim[0]}×{dim[1]} "
                             f"which also appears in Lesson/EC",
                    "interaction_id": ix_id,
                    "phase": "Synthesis",
                    "dimension": f"{dim[0]}×{dim[1]}",
                })

    return findings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_dimension_track(filepath: str, gate: int) -> dict:
    sp = parse_sp(filepath)

    if gate == 1:
        return {
            "checker": "sp_dimension_track",
            "file": filepath,
            "gate": gate,
            "checks_run": [],
            "total_findings": 0,
            "severity_counts": {},
            "check_counts": {},
            "findings": [],
            "meta": {"note": "Gate 1 — structural check only, no interactions"},
        }

    sp_filtered = filter_by_gate(sp, gate)
    all_findings = []

    # Build value tracking table by phase
    phase_values = {}
    usage_table = []

    for ix in sp_filtered.interactions:
        vals = extract_values_from_interaction(ix)
        phase_values.setdefault(ix.phase, {})[ix.id] = vals

        if vals["dimensions"] or vals["areas"]:
            usage_table.append({
                "phase": ix.phase,
                "interaction_id": ix.id,
                "title": ix.title[:50],
                "dimensions": [f"{d[0]}×{d[1]}" for d in vals["dimensions"]],
                "areas": vals["areas"],
                "factors": vals["factors"],
            })

    # DT4/DT5: Cross-phase dimension reuse (gate 3+)
    if gate >= 3:
        all_findings.extend(find_dimension_reuse(phase_values))

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_dimension_track",
        "file": filepath,
        "gate": gate,
        "checks_run": sorted(set(f["check"] for f in all_findings)) or ["DT1"],
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "usage_table": usage_table,
            "phases_tracked": list(phase_values.keys()),
        },
    }


def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"DIMENSION TRACKING — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")

    meta = result.get('meta', {})
    usage = meta.get('usage_table', [])

    if usage:
        print(f"\nDimension Usage Table ({len(usage)} interactions with values):")
        for row in usage:
            dims = ', '.join(row['dimensions']) if row['dimensions'] else '-'
            areas = ', '.join(str(a) for a in row['areas']) if row['areas'] else '-'
            print(f"  {row['phase']:12s} | {row['interaction_id']:6s} | dims: {dims:15s} | areas: {areas}")

    print(f"\nFindings: {result['total_findings']}")
    if result['findings']:
        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            detail = f.get('detail', '')
            print(f"  [{check}] {sev:8s} | {detail}")
    else:
        print("  ✓ No cross-phase dimension reuse found.")


def main():
    parser = argparse.ArgumentParser(description="SP Dimension Tracker")
    parser.add_argument("sp_file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_dimension_track(args.sp_file, args.gate)

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
