#!/usr/bin/env python3
"""
sp_interaction_check.py — Programmatic interaction block format checker for Starter Packs.

Checks every interaction block for format compliance based on its pattern type.

Checks:
  Pattern 1 (student_action):
    I1: Purpose field present
    I2: Visual field present
    I3: Guide field present
    I4: Prompt field present
    I5: Student Action field present
    I6: Correct Answer field present
    I7: On Correct field present
    I8: Remediation field present (should be "Pipeline")
    I9: If MC → Options + Answer Rationale present

  Pattern 2 (teaching_only):
    I10: Visual field present
    I11: Guide field present
    I12: "No student action." present
    I13: No contradictory fields (Prompt, Student Action, Correct Answer, Remediation)

  Cross-interaction:
    I14: Type label present (brackets)
    I15: No legacy [Type A/B/C] labels (WARNING — many SPs still use these)
    I16: Guide/Prompt independence — both present on student-action interactions

  Aggregate:
    I17: Interaction count per phase within expected ranges
    I18: Phase coverage (each expected phase has at least one interaction)

  Quantitative (migrated from L2 agents):
    I19: Consecutive teaching-only clustering — max 2 in a row per phase
    I20: On Correct feedback word count — flag if >20 words (target 5-15)
    I21: Purpose line sentence count — flag if >3 sentences

Gate scoping:
  Gate 1: Skipped (no interactions)
  Gate 2: Warmup + Lesson only
  Gate 3: All phases, plus aggregate counts
  Gate 4: All phases, full validation

Usage:
  python sp_interaction_check.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate, ParsedSP


# ---------------------------------------------------------------------------
# Expected phase interaction count ranges
# ---------------------------------------------------------------------------

PHASE_COUNT_RANGES = {
    "Warmup": (2, 5),
    "Lesson": (6, 30),      # broad range — varies by module
    "EC": (2, 8),
    "Practice": (2, 20),
    "Synthesis": (3, 8),     # 3-4 tasks + frame + closure
}


# ---------------------------------------------------------------------------
# Per-interaction field checks
# ---------------------------------------------------------------------------

def check_student_action_fields(ix) -> list:
    """Check required fields for Pattern 1 (student_action) interactions."""
    findings = []
    loc = f"{ix.phase}/{ix.id}"

    if not ix.has_purpose:
        findings.append(_finding("I1", "MAJOR", ix, "Missing Purpose field"))

    if not ix.has_visual:
        findings.append(_finding("I2", "MAJOR", ix, "Missing Visual field"))

    if not ix.has_guide:
        findings.append(_finding("I3", "MAJOR", ix, "Missing Guide field"))

    if not ix.has_prompt:
        findings.append(_finding("I4", "MAJOR", ix, "Missing Prompt field — student-action interaction requires both Guide and Prompt"))

    if not ix.has_student_action:
        findings.append(_finding("I5", "MINOR", ix, "Missing Student Action field"))

    if not ix.has_correct_answer:
        findings.append(_finding("I6", "MAJOR", ix, "Missing Correct Answer field"))

    if not ix.has_on_correct:
        findings.append(_finding("I7", "MINOR", ix, "Missing On Correct field"))

    if not ix.has_remediation:
        findings.append(_finding("I8", "MAJOR", ix, "Missing Remediation field"))
    elif ix.remediation_text:
        # Check that remediation is "Pipeline" (not authored dialogue)
        rem_lower = ix.remediation_text.lower().strip()
        if rem_lower and 'pipeline' not in rem_lower:
            findings.append(_finding("I8", "MINOR", ix,
                f"Remediation is '{ix.remediation_text[:60]}' — expected 'Pipeline' (no intensity qualifiers)"))

    # MC-specific: if Options present, Answer Rationale should be too
    if ix.has_options and not ix.has_answer_rationale:
        findings.append(_finding("I9", "MAJOR", ix, "MC interaction has Options but missing Answer Rationale"))

    return findings


def check_teaching_only_fields(ix) -> list:
    """Check required fields for Pattern 2 (teaching_only) interactions."""
    findings = []

    if not ix.has_visual:
        # Visual is expected but not always critical for teaching-only
        # Some teaching-only interactions (bridges, closures) legitimately skip Visual
        if ix.id not in ('OF', 'IC', 'PF') and 'bridge' not in ix.title.lower():
            findings.append(_finding("I10", "MINOR", ix, "Missing Visual field"))

    if not ix.has_guide:
        findings.append(_finding("I11", "MAJOR", ix, "Missing Guide field"))

    if not ix.has_no_student_action:
        # Not all teaching-only interactions explicitly state "No student action"
        # but they should
        findings.append(_finding("I12", "MINOR", ix,
            "Missing 'No student action.' marker — teaching-only interaction should include it"))

    # Contradictory fields
    contradictions = []
    if ix.has_prompt:
        contradictions.append("Prompt")
    if ix.has_student_action:
        contradictions.append("Student Action")
    if ix.has_correct_answer:
        contradictions.append("Correct Answer")
    if ix.has_remediation:
        contradictions.append("Remediation")

    if contradictions:
        findings.append(_finding("I13", "MAJOR", ix,
            f"Teaching-only interaction has contradictory fields: {', '.join(contradictions)}"))

    return findings


def check_system_driven_fields(ix) -> list:
    """Check required fields for Pattern 3 (system_driven) interactions."""
    findings = []

    if not ix.has_on_complete:
        findings.append(_finding("I14", "MAJOR", ix, "System-driven interaction missing On Complete block"))

    return findings


# ---------------------------------------------------------------------------
# Cross-interaction checks
# ---------------------------------------------------------------------------

def check_type_labels(interactions: list) -> list:
    """Check interaction type labels."""
    findings = []
    legacy_labels = {'Type A', 'Type B', 'Type C'}

    for ix in interactions:
        if not ix.type_label:
            # Opening Frame and Identity-Building Closure often lack type labels
            if ix.id not in ('OF', 'IC', 'PF') and 'bridge' not in ix.title.lower():
                findings.append(_finding("I14", "MINOR", ix,
                    "Missing type label in brackets (e.g., [WORKED EXAMPLE], [ACTIVATION])"))
        elif ix.type_label in legacy_labels:
            findings.append(_finding("I15", "INFO", ix,
                f"Legacy type label [{ix.type_label}] — consider pedagogical label "
                f"(e.g., [WORKED EXAMPLE], [EXAMPLE-PROBLEM PAIR])"))

    return findings


def check_guide_prompt_independence(interactions: list) -> list:
    """
    Check that every student-action interaction has BOTH Guide and Prompt fields.
    The Guide/Prompt independence rule: each must be independently complete.
    """
    findings = []
    for ix in interactions:
        if ix.pattern == "student_action":
            if ix.has_guide and not ix.has_prompt:
                findings.append(_finding("I16", "MAJOR", ix,
                    "Student-action interaction has Guide but no Prompt — both required for independence"))
            elif ix.has_prompt and not ix.has_guide:
                findings.append(_finding("I16", "MAJOR", ix,
                    "Student-action interaction has Prompt but no Guide — both required for independence"))

    return findings


# ---------------------------------------------------------------------------
# Quantitative checks (migrated from L2 agents)
# ---------------------------------------------------------------------------

def check_teaching_only_clustering(interactions: list) -> list:
    """I19: Flag runs of >2 consecutive teaching-only interactions within a phase.

    Migrated from L2 agent m42-lesson-eval (IQ3.2). Teaching-only clusters
    longer than 2 risk losing student engagement — the student is passive
    for too long without any action.
    """
    findings = []

    # Group interactions by phase, preserving order
    phase_runs = {}
    for ix in interactions:
        phase_runs.setdefault(ix.phase, []).append(ix)

    for phase, ixs in phase_runs.items():
        streak = 0
        streak_start = None
        for ix in ixs:
            if ix.pattern == "teaching_only":
                streak += 1
                if streak == 1:
                    streak_start = ix
            else:
                if streak > 2:
                    findings.append({
                        "check": "I19",
                        "severity": "MINOR",
                        "phase": phase,
                        "interaction_id": streak_start.id,
                        "detail": f"{streak} consecutive teaching-only interactions "
                                  f"starting at {streak_start.id} in {phase} "
                                  f"(max 2 without student action)",
                        "line_number": streak_start.line_number,
                    })
                streak = 0
                streak_start = None

        # Check final run
        if streak > 2 and streak_start:
            findings.append({
                "check": "I19",
                "severity": "MINOR",
                "phase": phase,
                "interaction_id": streak_start.id,
                "detail": f"{streak} consecutive teaching-only interactions "
                          f"starting at {streak_start.id} in {phase} "
                          f"(max 2 without student action)",
                "line_number": streak_start.line_number,
            })

    return findings


# Sentence-ending pattern for Purpose line analysis
_SENTENCE_END_RE = re.compile(r'[.!?]+(?:\s|$)')


def check_on_correct_length(interactions: list) -> list:
    """I20: Flag On Correct feedback that exceeds 20 words.

    Migrated from L2 agent m42-ec-practice-eval (EP2.4). On Correct feedback
    should be brief reinforcement (5-15 words), not extended teaching. Extended
    feedback after a correct answer slows pacing and dilutes the reinforcement.
    """
    findings = []

    for ix in interactions:
        if ix.pattern != "student_action":
            continue
        for dl in ix.dialogue_lines:
            if dl.field_type == "On Correct":
                # Count words in the dialogue text
                text = dl.text.strip().strip('"').strip()
                word_count = len(text.split())
                if word_count > 20:
                    findings.append(_finding("I20", "MINOR", ix,
                        f"On Correct feedback is {word_count} words "
                        f"(target 5-15, max ~20): \"{text[:60]}...\""))

    return findings


def check_purpose_length(interactions: list) -> list:
    """I21: Flag Purpose lines with more than 3 sentences.

    Migrated from L2 agent m42-lesson-eval (LS1.5). The Purpose line should be
    a concise framing statement (~15 seconds spoken). More than 3 sentences
    indicates over-explanation that delays engagement.
    """
    findings = []

    for ix in interactions:
        if not ix.has_purpose:
            continue
        # Find the Purpose line in raw_lines
        for line_num, line in ix.raw_lines:
            stripped = line.strip()
            if stripped.startswith('* **Purpose:**'):
                # Extract the text after the field label
                text = re.sub(r'^\*\s*\*\*Purpose:\*\*\s*', '', stripped)
                # Count sentences by splitting on sentence-ending punctuation
                sentences = [s.strip() for s in _SENTENCE_END_RE.split(text) if s.strip()]
                if len(sentences) > 3:
                    findings.append(_finding("I21", "MINOR", ix,
                        f"Purpose has {len(sentences)} sentences (max 3): "
                        f"\"{text[:80]}...\""))
                break  # Only check first Purpose line per interaction

    return findings


# ---------------------------------------------------------------------------
# Aggregate checks
# ---------------------------------------------------------------------------

def check_phase_counts(interactions: list) -> list:
    """Check interaction counts per phase are within expected ranges."""
    findings = []
    phase_counts = {}
    for ix in interactions:
        phase_counts[ix.phase] = phase_counts.get(ix.phase, 0) + 1

    for phase, (min_count, max_count) in PHASE_COUNT_RANGES.items():
        count = phase_counts.get(phase, 0)
        if count == 0:
            continue  # phase might not be in scope yet
        if count < min_count:
            findings.append({
                "check": "I17",
                "severity": "MAJOR",
                "phase": phase,
                "detail": f"{phase} has {count} interactions (expected {min_count}-{max_count})",
                "count": count,
                "expected_min": min_count,
                "expected_max": max_count,
            })
        elif count > max_count:
            findings.append({
                "check": "I17",
                "severity": "MINOR",
                "phase": phase,
                "detail": f"{phase} has {count} interactions (expected {min_count}-{max_count})",
                "count": count,
                "expected_min": min_count,
                "expected_max": max_count,
            })

    return findings


def check_phase_coverage(interactions: list, gate: int) -> list:
    """Check that expected phases have at least one interaction."""
    findings = []
    phases_present = set(ix.phase for ix in interactions)

    if gate >= 2:
        for expected in ["Warmup", "Lesson"]:
            if expected not in phases_present:
                findings.append({
                    "check": "I18",
                    "severity": "CRITICAL",
                    "phase": expected,
                    "detail": f"No {expected} interactions found — expected at Gate {gate}",
                })

    if gate >= 3:
        # At least one of EC/Practice should be present, and Synthesis
        if "EC" not in phases_present and "Practice" not in phases_present:
            findings.append({
                "check": "I18",
                "severity": "MAJOR",
                "detail": "Neither EC nor Practice interactions found — expected at Gate 3+",
            })
        if "Synthesis" not in phases_present:
            findings.append({
                "check": "I18",
                "severity": "MAJOR",
                "phase": "Synthesis",
                "detail": "No Synthesis interactions found — expected at Gate 3+",
            })

    return findings


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _finding(check_id: str, severity: str, ix, detail: str) -> dict:
    """Build a finding dict for a specific interaction."""
    return {
        "check": check_id,
        "severity": severity,
        "interaction_id": ix.id,
        "interaction_title": ix.title[:80],
        "phase": ix.phase,
        "pattern": ix.pattern,
        "line_number": ix.line_number,
        "detail": detail,
    }


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_interaction_check(filepath: str, gate: int) -> dict:
    """Run all interaction checks for the given gate."""
    sp = parse_sp(filepath)

    if gate == 1:
        return {
            "checker": "sp_interaction_check",
            "file": filepath,
            "gate": gate,
            "checks_run": [],
            "total_findings": 0,
            "severity_counts": {},
            "check_counts": {},
            "findings": [],
            "meta": {"note": "Gate 1 — no interactions to check"},
        }

    sp_filtered = filter_by_gate(sp, gate)
    all_findings = []
    checks_run = set()

    # Per-interaction field checks
    for ix in sp_filtered.interactions:
        if ix.pattern == "student_action":
            findings = check_student_action_fields(ix)
        elif ix.pattern == "teaching_only":
            findings = check_teaching_only_fields(ix)
        elif ix.pattern == "system_driven":
            findings = check_system_driven_fields(ix)
        else:
            findings = [{
                "check": "I0",
                "severity": "MINOR",
                "interaction_id": ix.id,
                "interaction_title": ix.title[:80],
                "phase": ix.phase,
                "pattern": ix.pattern,
                "line_number": ix.line_number,
                "detail": f"Unknown interaction pattern '{ix.pattern}' — cannot validate fields",
            }]

        all_findings.extend(findings)
        for f in findings:
            checks_run.add(f["check"])

    # Cross-interaction checks
    type_findings = check_type_labels(sp_filtered.interactions)
    all_findings.extend(type_findings)
    if type_findings:
        checks_run.update(f["check"] for f in type_findings)

    independence_findings = check_guide_prompt_independence(sp_filtered.interactions)
    all_findings.extend(independence_findings)
    if independence_findings:
        checks_run.update(f["check"] for f in independence_findings)

    # Quantitative checks (gate 2+)
    cluster_findings = check_teaching_only_clustering(sp_filtered.interactions)
    all_findings.extend(cluster_findings)
    if cluster_findings:
        checks_run.update(f["check"] for f in cluster_findings)

    on_correct_findings = check_on_correct_length(sp_filtered.interactions)
    all_findings.extend(on_correct_findings)
    if on_correct_findings:
        checks_run.update(f["check"] for f in on_correct_findings)

    purpose_findings = check_purpose_length(sp_filtered.interactions)
    all_findings.extend(purpose_findings)
    if purpose_findings:
        checks_run.update(f["check"] for f in purpose_findings)

    # Aggregate checks (gate 3+)
    if gate >= 3:
        count_findings = check_phase_counts(sp_filtered.interactions)
        all_findings.extend(count_findings)
        if count_findings:
            checks_run.update(f["check"] for f in count_findings)

    coverage_findings = check_phase_coverage(sp_filtered.interactions, gate)
    all_findings.extend(coverage_findings)
    if coverage_findings:
        checks_run.update(f["check"] for f in coverage_findings)

    # Build summary
    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    # Phase breakdown
    phase_breakdown = {}
    for ix in sp_filtered.interactions:
        p = ix.phase
        if p not in phase_breakdown:
            phase_breakdown[p] = {"total": 0, "student_action": 0, "teaching_only": 0, "system_driven": 0, "unknown": 0}
        phase_breakdown[p]["total"] += 1
        phase_breakdown[p][ix.pattern] = phase_breakdown[p].get(ix.pattern, 0) + 1

    return {
        "checker": "sp_interaction_check",
        "file": filepath,
        "gate": gate,
        "checks_run": sorted(checks_run),
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "interactions_checked": len(sp_filtered.interactions),
            "phase_breakdown": phase_breakdown,
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_findings_table(result: dict):
    """Print human-readable findings summary."""
    print(f"\n{'='*80}")
    print(f"INTERACTION CHECK — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")
    print(f"Checks run: {', '.join(result['checks_run'])}")
    print(f"Interactions checked: {result['meta'].get('interactions_checked', '?')}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    # Phase breakdown
    breakdown = result['meta'].get('phase_breakdown', {})
    if breakdown:
        print("\nPhase breakdown:")
        for phase, counts in sorted(breakdown.items()):
            print(f"  {phase:12s}: {counts['total']} total "
                  f"({counts.get('student_action',0)} student, "
                  f"{counts.get('teaching_only',0)} teaching, "
                  f"{counts.get('system_driven',0)} system)")

    if result['findings']:
        print(f"\n{'─'*80}")
        print("FINDINGS:")
        print(f"{'─'*80}")

        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            int_id = f.get('interaction_id', '')
            phase = f.get('phase', '')
            loc = f"{phase}/{int_id}" if phase and int_id else phase or ''
            line = f.get('line_number', '')
            line_str = f" L{line}" if line else ""
            detail = f.get('detail', '')

            print(f"  [{check:3s}] {sev:8s} | {loc:25s} |{line_str} {detail}")
    else:
        print("\n  ✓ No findings.")


def main():
    parser = argparse.ArgumentParser(description="SP Interaction Block Checker")
    parser.add_argument("sp_file", help="Path to the Starter Pack markdown file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_interaction_check(args.sp_file, args.gate)

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
