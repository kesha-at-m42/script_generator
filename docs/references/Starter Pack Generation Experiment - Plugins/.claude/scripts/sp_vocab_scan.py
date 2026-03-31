#!/usr/bin/env python3
"""
sp_vocab_scan.py — Programmatic vocabulary compliance checker for Starter Packs.

Checks:
  V1: Terms to Avoid in dialogue lines
  V2: Forbidden Phrases in dialogue lines
  V3: Vocabulary timing (formal terms before designated staging phase)
  V4: Assessment Vocabulary appears in at least one EC interaction
  V5: Session-relative language ("yesterday", "today", "tomorrow")
  V6: Module reference numbers in student-facing dialogue
  V7: Terms to Avoid list present in §1.3 (completeness)

Gate scoping:
  Gate 1: V7 (completeness checks only — no dialogue to scan)
  Gate 2: V1, V2, V5, V6 on Warmup+Lesson; V7
  Gate 3: V1-V7 on Warmup+Lesson+EC+Synthesis
  Gate 4: V1-V7 full document

Usage:
  python sp_vocab_scan.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Add parent dir to path for shared module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate, ParsedSP


# ---------------------------------------------------------------------------
# Vocabulary timing: phase ordering
# ---------------------------------------------------------------------------

# Canonical ordering for timing checks. A term introduced at phase N
# should not appear in dialogue at any phase < N.
PHASE_ORDER = {
    "Warmup": 0,
    "Lesson S1": 1,
    "Lesson S2": 2,
    "Lesson S3": 3,
    "EC": 4,
    "Practice": 4,   # same level as EC
    "Synthesis": 5,
}


def dialogue_phase_rank(dialogue_line) -> int:
    """Get the ordering rank of a dialogue line's phase + section."""
    phase = dialogue_line.phase
    if phase == "Lesson":
        # Use interaction's lesson_section if available
        section = getattr(dialogue_line, '_lesson_section', None)
        if section:
            key = f"Lesson S{section}"
            return PHASE_ORDER.get(key, 1)
        return 1  # default to Lesson S1 if no section info
    return PHASE_ORDER.get(phase, 99)


# ---------------------------------------------------------------------------
# Session-relative and module-reference patterns
# ---------------------------------------------------------------------------

SESSION_RELATIVE_PATTERNS = [
    (re.compile(r'\byesterday\b', re.IGNORECASE), "yesterday"),
    (re.compile(r'\btoday\b', re.IGNORECASE), "today"),
    (re.compile(r'\btomorrow\b', re.IGNORECASE), "tomorrow"),
    (re.compile(r'\blast time\b', re.IGNORECASE), "last time"),
    (re.compile(r'\bnext time\b', re.IGNORECASE), "next time"),
    (re.compile(r'\blast class\b', re.IGNORECASE), "last class"),
    (re.compile(r'\blast lesson\b', re.IGNORECASE), "last lesson"),
]

MODULE_REF_RE = re.compile(r'\b[Mm]odule\s+\d+\b')


# ---------------------------------------------------------------------------
# Staging table parser
# ---------------------------------------------------------------------------

def parse_staging_table(lines: list) -> dict:
    """
    Parse the Vocabulary Staging by Phase table to extract phase→terms mappings.
    Returns dict mapping normalized phase names to lists of terms.

    The table looks like:
    | Phase | Terms | Introduction Approach |
    | **Warm-Up** | area, square unit, ... | ... |
    | **Lesson Section 1 (...)** | row, "rows of" | ... |
    """
    staging = {}
    in_staging = False
    past_header = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        lower = stripped.lower()

        # Find the staging section
        if 'vocabulary staging' in lower and ('phase' in lower or '###' in stripped.lower()):
            in_staging = True
            continue

        if not in_staging:
            continue

        # Exit on next section
        if stripped.startswith('#') and 'staging' not in lower:
            break

        # Skip table header rows
        if '---' in stripped and '|' in stripped:
            past_header = True
            continue

        # Must be a table row with phase info
        if not stripped.startswith('|') or not past_header:
            # Check for the first header row
            if stripped.startswith('|') and 'phase' in lower:
                continue
            if not stripped.startswith('|'):
                continue
            continue

        cells = [c.strip() for c in stripped.split('|')]
        cells = [c for c in cells if c]  # remove empty from leading/trailing |

        if len(cells) < 2:
            continue

        phase_cell = cells[0].strip('*').strip()

        # Normalize phase names
        phase_norm = _normalize_staging_phase(phase_cell)
        if not phase_norm:
            continue

        # Extract terms from ALL vocabulary columns (not just the first).
        # Some SPs have a single terms column; others split into
        # Primary / Secondary / Reinforcement etc.  We read every column
        # except the first (phase) and the last (often a "Notes" column
        # containing prose, not comma-separated terms).  Heuristic: if the
        # last column contains 5+ words of running text with no commas,
        # treat it as notes and skip it.
        term_cells = cells[1:]  # everything after phase column
        if len(term_cells) > 1:
            last = term_cells[-1].strip('*').strip()
            # Skip last column if it looks like prose (long, few commas)
            if len(last.split()) >= 5 and ',' not in last:
                term_cells = term_cells[:-1]

        terms = []
        for tc in term_cells:
            terms.extend(_extract_terms_from_cell(tc.strip('*').strip()))

        if terms:
            if phase_norm in staging:
                staging[phase_norm].extend(terms)
            else:
                staging[phase_norm] = terms

    return staging


def _normalize_staging_phase(phase_text: str) -> str:
    """Normalize a staging table phase name to our canonical names."""
    lower = phase_text.lower()

    if 'warm' in lower:
        return "Warmup"
    if 'exit' in lower or lower.startswith('ec'):
        return "EC"
    if 'synthesis' in lower:
        return "Synthesis"
    if 'practice' in lower:
        return "Practice"

    # Lesson variants
    if 'lesson' in lower or 'section' in lower:
        # Try to extract section number
        m = re.search(r'section\s*(\d+)', lower)
        if m:
            return f"Lesson S{m.group(1)}"
        if 'early' in lower or 'intro' in lower or 'comparison' in lower:
            return "Lesson S1"
        if 'mid' in lower or 'post' in lower:
            return "Lesson S2"
        if 'late' in lower or 'independent' in lower or 'capstone' in lower:
            return "Lesson S3"
        return "Lesson S1"  # default

    return ""


def _extract_terms_from_cell(cell: str) -> list:
    """Extract individual vocabulary terms from a staging table cell."""
    # Handle "(all terms)" or "(row, column practiced)" style
    if cell.startswith('(') and cell.endswith(')'):
        inner = cell[1:-1].strip()
        if 'all terms' in inner.lower():
            return []  # means all previously introduced terms are in scope
        # Could contain actual terms like "(row, column practiced)"
        cell = inner

    terms = []
    # Split on commas, handling quoted terms like "rows of"
    parts = re.split(r',\s*', cell)
    for part in parts:
        term = part.strip().strip('"').strip("'").strip()
        # Remove parenthetical notes
        term = re.sub(r'\s*\(.*?\)', '', term).strip()
        # Remove trailing descriptive text after slash
        term = term.split('/')[0].strip()
        # Skip empty, meta-notes, or very long strings (descriptions not terms)
        if not term or len(term) > 40 or term.lower() in ('all terms', 'practiced'):
            continue
        terms.append(term)

    return terms


def build_timing_map(staging: dict) -> dict:
    """
    Build a map of term → earliest_phase_rank from the staging table.
    Terms introduced at a given phase can appear at that phase or later.
    """
    timing = {}
    for phase, terms in staging.items():
        rank = PHASE_ORDER.get(phase, 99)
        for term in terms:
            term_lower = term.lower()
            if term_lower not in timing or rank < timing[term_lower]:
                timing[term_lower] = rank
    return timing


# ---------------------------------------------------------------------------
# Assessment vocabulary parser
# ---------------------------------------------------------------------------

def parse_assessment_vocab(lines: list) -> list:
    """Extract Assessment Vocabulary terms from §1.3.

    Handles two formats:
      - Simple: "**Assessment Vocabulary (...):** area, unit square, ..."
      - Narrative (M5-style): "**Assessment Vocabulary (...):** **NEW in M7:** side length, dimension.
        **REVIEW from M5/M6:** square inch, ... **From M4 (used, not taught):** multiply, ..."

    In the narrative format, bold category labels like **NEW in M7:** are stripped
    before extracting the comma-separated terms.
    """
    terms = []
    for i, line in enumerate(lines):
        lower = line.strip().lower()
        if 'assessment vocabulary' in lower and ('state test' in lower or ':' in line):
            # Extract everything after the first colon (the AV header colon)
            _, _, rest = line.partition(':')
            if not rest:
                continue

            # Strip bold category labels: **NEW in M7:**, **REVIEW from M5/M6:**,
            # **From M4 (used, not taught):**, etc.  These are bold spans ending
            # with a colon that categorise the terms but aren't terms themselves.
            rest = re.sub(r'\*\*[^*]+?:\*\*', '', rest)

            # Remove parenthetical notes and known junk
            rest = re.sub(r'\(.*?\)', '', rest)
            # Strip "+" prefixed additions like "+ row, column (new for 3.MD.C.6)"
            rest = rest.replace('+', ',')

            # Split on commas and periods (narrative format uses sentence-ending periods)
            parts = re.split(r'[,\.]\s*', rest.strip().rstrip('*').strip())
            for p in parts:
                term = p.strip().strip('*').strip()
                if term and len(term) > 1 and len(term) < 40:
                    terms.append(term)
            break
    return terms


# ---------------------------------------------------------------------------
# Core scan functions
# ---------------------------------------------------------------------------

def scan_terms_in_dialogue(dialogue_lines: list, terms: list, check_id_prefix: str) -> list:
    """
    Scan dialogue lines for occurrences of forbidden/avoided terms.
    Returns list of finding dicts.
    """
    findings = []
    term_patterns = []
    for term in terms:
        # Build word-boundary regex for each term
        # Handle multi-word terms and slash-separated variants
        variants = [t.strip() for t in term.split('/') if t.strip()]
        for variant in variants:
            escaped = re.escape(variant)
            pattern = re.compile(r'\b' + escaped + r'\b', re.IGNORECASE)
            term_patterns.append((term, variant, pattern))

    for dl in dialogue_lines:
        for orig_term, variant, pattern in term_patterns:
            matches = list(pattern.finditer(dl.text))
            if matches:
                for match in matches:
                    findings.append({
                        "check": check_id_prefix,
                        "severity": "MAJOR",
                        "term": orig_term,
                        "matched": match.group(),
                        "interaction_id": dl.interaction_id,
                        "interaction_title": dl.interaction_title,
                        "field_type": dl.field_type,
                        "phase": dl.phase,
                        "line_number": dl.line_number,
                        "context": dl.text[:120],
                    })

    return findings


def check_vocab_timing(sp: ParsedSP, timing_map: dict, interactions: list) -> list:
    """
    Check that vocabulary terms don't appear before their staging phase.
    """
    findings = []

    # Build a lookup from interaction_id to lesson_section
    int_sections = {}
    for ix in interactions:
        int_sections[ix.id] = ix.lesson_section

    for dl in sp.dialogue_lines:
        dl_phase = dl.phase
        dl_section = int_sections.get(dl.interaction_id)

        # Compute this dialogue line's phase rank
        if dl_phase == "Lesson" and dl_section:
            rank = PHASE_ORDER.get(f"Lesson S{dl_section}", 1)
        else:
            rank = PHASE_ORDER.get(dl_phase, 99)

        # Check each timed term
        for term_lower, earliest_rank in timing_map.items():
            if earliest_rank <= rank:
                continue  # term is allowed at this phase

            # Check if term appears in this line
            pattern = re.compile(r'\b' + re.escape(term_lower) + r'\b', re.IGNORECASE)
            matches = list(pattern.finditer(dl.text))
            if matches:
                for match in matches:
                    findings.append({
                        "check": "V3",
                        "severity": "MAJOR",
                        "term": term_lower,
                        "matched": match.group(),
                        "interaction_id": dl.interaction_id,
                        "interaction_title": dl.interaction_title,
                        "field_type": dl.field_type,
                        "phase": dl.phase,
                        "line_number": dl.line_number,
                        "expected_earliest_phase": _rank_to_phase_name(earliest_rank),
                        "context": dl.text[:120],
                    })

    return findings


def _rank_to_phase_name(rank: int) -> str:
    """Convert rank back to a human-readable phase name."""
    for name, r in PHASE_ORDER.items():
        if r == rank:
            return name
    return f"rank-{rank}"


def check_session_relative(dialogue_lines: list) -> list:
    """Check for session-relative language in dialogue."""
    findings = []
    for dl in dialogue_lines:
        for pattern, label in SESSION_RELATIVE_PATTERNS:
            matches = list(pattern.finditer(dl.text))
            if matches:
                for match in matches:
                    findings.append({
                        "check": "V5",
                        "severity": "MINOR",
                        "term": label,
                        "matched": match.group(),
                        "interaction_id": dl.interaction_id,
                        "field_type": dl.field_type,
                        "phase": dl.phase,
                        "line_number": dl.line_number,
                        "context": dl.text[:120],
                    })
    return findings


def check_module_references(dialogue_lines: list) -> list:
    """Check for explicit module number references in student-facing dialogue."""
    findings = []
    for dl in dialogue_lines:
        matches = list(MODULE_REF_RE.finditer(dl.text))
        if matches:
            for match in matches:
                findings.append({
                    "check": "V6",
                    "severity": "MINOR",
                    "term": match.group(),
                    "matched": match.group(),
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "context": dl.text[:120],
                })
    return findings


def check_assessment_in_ec(assessment_terms: list, interactions: list) -> list:
    """Check that each Assessment Vocabulary term appears in at least one EC interaction."""
    findings = []
    ec_interactions = [ix for ix in interactions if ix.phase == "EC"]

    if not ec_interactions:
        return findings  # no EC interactions to check (might be gate 2)

    # Collect all EC dialogue text
    ec_text = ""
    for ix in ec_interactions:
        for dl in ix.dialogue_lines:
            ec_text += " " + dl.text

    for term in assessment_terms:
        pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
        if not pattern.search(ec_text):
            findings.append({
                "check": "V4",
                "severity": "MAJOR",
                "term": term,
                "detail": f"Assessment term '{term}' not found in any EC interaction dialogue",
                "ec_interaction_count": len(ec_interactions),
            })

    return findings


def check_completeness(sp: ParsedSP) -> list:
    """Gate 1 check: verify §1.3 structural completeness."""
    findings = []

    if sp.vocab is None:
        findings.append({
            "check": "V7",
            "severity": "CRITICAL",
            "detail": "§1.3 Vocabulary Architecture section not found",
        })
        return findings

    if len(sp.vocab.terms_to_avoid) == 0:
        findings.append({
            "check": "V7",
            "severity": "MAJOR",
            "detail": "§1.3 Terms to Avoid list is empty — should contain at least the standard avoid terms",
        })

    return findings


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_vocab_scan(filepath: str, gate: int, verbose: bool = False) -> dict:
    """Run all vocabulary checks for the given gate. Returns structured results."""
    sp = parse_sp(filepath)

    all_findings = []
    checks_run = []

    # -- V7: Completeness (all gates) --
    checks_run.append("V7")
    all_findings.extend(check_completeness(sp))

    if gate == 1:
        # Gate 1: completeness only
        pass
    else:
        # Gate 2+: filter interactions by gate
        sp_filtered = filter_by_gate(sp, gate)

        # Collect terms
        terms_to_avoid = sp.vocab.terms_to_avoid if sp.vocab else []
        forbidden_phrases = sp.forbidden_phrases or []
        assessment_terms = parse_assessment_vocab(sp.lines)

        # Parse staging table for timing
        staging = parse_staging_table(sp.lines)
        timing_map = build_timing_map(staging)

        # -- V1: Terms to Avoid in dialogue --
        checks_run.append("V1")
        all_findings.extend(
            scan_terms_in_dialogue(sp_filtered.dialogue_lines, terms_to_avoid, "V1")
        )

        # -- V2: Forbidden Phrases in dialogue --
        if forbidden_phrases:
            checks_run.append("V2")
            all_findings.extend(
                scan_terms_in_dialogue(sp_filtered.dialogue_lines, forbidden_phrases, "V2")
            )

        # -- V3: Vocabulary timing --
        if timing_map:
            checks_run.append("V3")
            all_findings.extend(
                check_vocab_timing(sp_filtered, timing_map, sp_filtered.interactions)
            )

        # -- V5: Session-relative language --
        checks_run.append("V5")
        all_findings.extend(check_session_relative(sp_filtered.dialogue_lines))

        # -- V6: Module references --
        checks_run.append("V6")
        all_findings.extend(check_module_references(sp_filtered.dialogue_lines))

        # -- V4: Assessment vocab in EC (gate 3+ only) --
        if gate >= 3 and assessment_terms:
            checks_run.append("V4")
            all_findings.extend(
                check_assessment_in_ec(assessment_terms, sp_filtered.interactions)
            )

    # Build summary
    severity_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    check_counts = {}
    for f in all_findings:
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    result = {
        "checker": "sp_vocab_scan",
        "file": filepath,
        "gate": gate,
        "checks_run": checks_run,
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "terms_to_avoid_count": len(sp.vocab.terms_to_avoid) if sp.vocab else 0,
            "forbidden_phrases_count": len(sp.forbidden_phrases),
            "dialogue_lines_scanned": len(filter_by_gate(sp, gate).dialogue_lines) if gate > 1 else 0,
            "assessment_vocab": parse_assessment_vocab(sp.lines),
            "staging_phases_parsed": list(parse_staging_table(sp.lines).keys()),
        },
    }

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_findings_table(result: dict):
    """Print human-readable findings summary."""
    print(f"\n{'='*80}")
    print(f"VOCAB SCAN — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")
    print(f"Checks run: {', '.join(result['checks_run'])}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    if result['check_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['check_counts'].items())]
        print(f"By check: {', '.join(parts)}")

    meta = result.get('meta', {})
    print(f"\nTerms to Avoid: {meta.get('terms_to_avoid_count', '?')}")
    print(f"Forbidden Phrases: {meta.get('forbidden_phrases_count', '?')}")
    print(f"Dialogue lines scanned: {meta.get('dialogue_lines_scanned', '?')}")
    print(f"Assessment Vocabulary: {meta.get('assessment_vocab', [])}")
    print(f"Staging phases parsed: {meta.get('staging_phases_parsed', [])}")

    if result['findings']:
        print(f"\n{'─'*80}")
        print("FINDINGS:")
        print(f"{'─'*80}")

        for i, f in enumerate(result['findings'], 1):
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            term = f.get('term', f.get('detail', ''))
            phase = f.get('phase', '')
            int_id = f.get('interaction_id', '')
            field = f.get('field_type', '')

            loc = f"{phase}/{int_id}" if phase else ""
            if field:
                loc += f" ({field})"

            line = f.get('line_number', '')
            line_str = f" L{line}" if line else ""

            print(f"  [{check}] {sev:8s} | {term:25s} | {loc:30s} |{line_str}")

            if 'context' in f:
                print(f"           {f['context'][:70]}...")

            if 'expected_earliest_phase' in f:
                print(f"           ↳ Term should not appear before: {f['expected_earliest_phase']}")

            if 'detail' in f:
                print(f"           {f['detail']}")
    else:
        print("\n  ✓ No findings.")


def main():
    parser = argparse.ArgumentParser(description="SP Vocabulary Scanner")
    parser.add_argument("sp_file", help="Path to the Starter Pack markdown file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4],
                        help="Gate number (1-4)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of table")
    parser.add_argument("--output", type=str, help="Write JSON output to file")
    args = parser.parse_args()

    result = run_vocab_scan(args.sp_file, args.gate)

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
