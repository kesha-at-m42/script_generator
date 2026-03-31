#!/usr/bin/env python3
"""
sp_structure_check.py — Structural presence and ordering checker for Starter Packs.

Checks:
  ST1:  YAML front matter present with required fields
  ST2:  No legacy YAML fields
  ST3:  Required sections present (gate-aware)
  ST4:  Section ordering correct
  ST5:  No placeholder text
  ST6:  No development tags
  ST7:  Version line present
  ST8:  End marker present and formatted correctly (Gate 4)
  ST9:  Exactly 3 H1s (Module title, BACKBONE, END OF MODULE)
  ST10: No H4s anywhere
  ST11: §1.7 internal ordering (Gate 2+): Required Phrases → Forbidden Phrases →
        Purpose Frame → [Interactions] → Misconception Prevention → ISF →
        Success Criteria → Verification Checklist
  ST12: Section transition markers present in §1.7 (Gate 2+)
  ST13: Verification checklists present per phase (Gate 2+)

Gate scoping:
  Gate 1: §1.0–§1.5 + YAML
  Gate 2: §1.0–§1.7 (adds Warmup + Lesson sections)
  Gate 3: §1.0–§1.10 (adds EC, Practice, Synthesis, KDDs)
  Gate 4: Everything including end marker

Usage:
  python sp_structure_check.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp


# ---------------------------------------------------------------------------
# Required sections by gate
# ---------------------------------------------------------------------------

REQUIRED_SECTIONS_GATE1 = [
    ("1.0", "The One Thing"),
    ("1.1", "Learning Goals"),
    ("1.2", "Scope Boundaries"),
    ("1.3", "Vocabulary Architecture"),
    ("1.4", "Misconceptions"),
    ("1.5", "Toy Specifications"),
]

REQUIRED_SECTIONS_GATE2 = REQUIRED_SECTIONS_GATE1 + [
    ("1.6", "Warmup"),
    ("1.7", "Lesson"),
]

REQUIRED_SECTIONS_GATE3 = REQUIRED_SECTIONS_GATE2 + [
    ("1.8", "Exit Check"),
    ("1.9", "Synthesis"),
    ("1.10", "Key Design Decisions"),
]

# Gate 4 = Gate 3 + end marker (no §1.11 per Structural Skeleton)
REQUIRED_SECTIONS_GATE4 = REQUIRED_SECTIONS_GATE3

GATE_SECTIONS = {
    1: REQUIRED_SECTIONS_GATE1,
    2: REQUIRED_SECTIONS_GATE2,
    3: REQUIRED_SECTIONS_GATE3,
    4: REQUIRED_SECTIONS_GATE4,
}

# Required YAML fields
REQUIRED_YAML_FIELDS = ['module_id', 'unit', 'domain']
OPTIONAL_YAML_FIELDS = ['primary_toys', 'secondary_toys', 'interaction_tools']
LEGACY_YAML_FIELDS = ['path', 'fractions_required', 'shapes']

# Placeholder patterns
PLACEHOLDER_PATTERNS = [
    (re.compile(r'\[TBD\]', re.IGNORECASE), "[TBD]"),
    (re.compile(r'\[Section to be added\]', re.IGNORECASE), "[Section to be added]"),
    (re.compile(r'\[PLACEHOLDER\]', re.IGNORECASE), "[PLACEHOLDER]"),
    (re.compile(r'\[TODO\]', re.IGNORECASE), "[TODO]"),
    (re.compile(r'\[INSERT\b', re.IGNORECASE), "[INSERT...]"),
]

# Development tag patterns
DEV_TAG_PATTERNS = [
    (re.compile(r'\[Modeling\]', re.IGNORECASE), "[Modeling]"),
    (re.compile(r'\[MODIFY\]', re.IGNORECASE), "[MODIFY]"),
    (re.compile(r'\[Vocab_Staging\]', re.IGNORECASE), "[Vocab_Staging]"),
    (re.compile(r'\[Tool_Intro\]', re.IGNORECASE), "[Tool_Intro]"),
    (re.compile(r'Detail Level:', re.IGNORECASE), "Detail Level:"),
]


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_yaml(sp, gate: int) -> list:
    """ST1/ST2: YAML front matter checks."""
    findings = []

    if sp.yaml is None:
        findings.append({
            "check": "ST1",
            "severity": "CRITICAL",
            "detail": "YAML front matter not found",
        })
        return findings

    # Required fields
    for field in REQUIRED_YAML_FIELDS:
        if field not in sp.yaml.fields:
            findings.append({
                "check": "ST1",
                "severity": "MAJOR",
                "detail": f"YAML missing required field: {field}",
                "line_number": sp.yaml.line_start,
            })

    # Check module_id format
    mid = sp.yaml.fields.get('module_id', '')
    if mid and not re.match(r'^M\d{2}$', mid):
        findings.append({
            "check": "ST1",
            "severity": "MINOR",
            "detail": f"YAML module_id format unexpected: '{mid}' (expected M01-M99)",
            "line_number": sp.yaml.line_start,
        })

    # Optional but recommended fields
    if not sp.yaml.has_primary_toys:
        findings.append({
            "check": "ST1",
            "severity": "MINOR",
            "detail": "YAML missing recommended field: primary_toys",
            "line_number": sp.yaml.line_start,
        })

    # Legacy fields
    for field in sp.yaml.legacy_fields:
        findings.append({
            "check": "ST2",
            "severity": "MINOR",
            "detail": f"YAML contains legacy field: {field}",
            "line_number": sp.yaml.line_start,
        })

    return findings


def check_required_sections(sp, gate: int) -> list:
    """ST3: Required sections present."""
    findings = []
    required = GATE_SECTIONS.get(gate, GATE_SECTIONS[4])

    # Build a set of section IDs found
    found_ids = set()
    for sec in sp.sections:
        if sec.id:
            # Normalize: "1.0" matches "1.0", "1.10" matches "1.10"
            base_id = sec.id.split('.')[0] + '.' + sec.id.split('.')[1] if '.' in sec.id else sec.id
            found_ids.add(base_id)
            # Also add the raw id
            found_ids.add(sec.id)

    for req_id, req_name in required:
        if req_id not in found_ids:
            # Check for partial matches (e.g., §1.10 might appear as "1.10")
            partial = any(req_id in sid for sid in found_ids)
            if not partial:
                findings.append({
                    "check": "ST3",
                    "severity": "MAJOR",
                    "detail": f"Required section §{req_id} ({req_name}) not found",
                    "expected_id": req_id,
                })

    return findings


def _match_section_id(found_id: str, required_ids: list) -> int:
    """
    Match a found section ID against the required IDs list.
    Returns the index in required_ids, or None if no match.
    Uses exact match or dot-delimited prefix (e.g., "1.7.2" matches "1.7" but "1.10" does NOT match "1.1").
    """
    # Try exact match first
    if found_id in required_ids:
        return required_ids.index(found_id)

    # Try dot-delimited prefix: "1.7.2" → check "1.7"
    parts = found_id.split('.')
    for length in range(len(parts) - 1, 0, -1):
        prefix = '.'.join(parts[:length + 1])
        if prefix in required_ids:
            return required_ids.index(prefix)

    return None


def check_section_ordering(sp, gate: int) -> list:
    """ST4: Section ordering is correct."""
    findings = []
    required = GATE_SECTIONS.get(gate, GATE_SECTIONS[4])
    required_ids = [r[0] for r in required]

    # Get ordered list of found section IDs
    found_order = []
    for sec in sp.sections:
        if sec.id and sec.level <= 2:
            base_id = sec.id
            # Match against required IDs with exact or dot-delimited prefix
            matched = _match_section_id(base_id, required_ids)
            if matched is not None:
                found_order.append((base_id, sec.line_number, matched))

    # Check ordering
    last_idx = -1
    for sec_id, line_num, matched_idx in found_order:
        idx = matched_idx
        if idx < last_idx:
            findings.append({
                "check": "ST4",
                "severity": "MAJOR",
                "detail": f"Section §{sec_id} at line {line_num} appears out of order "
                         f"(after §{required_ids[last_idx]})",
                "line_number": line_num,
            })
        last_idx = max(last_idx, idx)

    return findings


def check_placeholders(sp, gate: int) -> list:
    """ST5: No placeholder text."""
    findings = []
    for i, line in enumerate(sp.lines):
        for pattern, label in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                findings.append({
                    "check": "ST5",
                    "severity": "MAJOR",
                    "detail": f"Placeholder text found: {label}",
                    "line_number": i + 1,
                    "context": line.strip()[:100],
                })
    return findings


def check_dev_tags(sp, gate: int) -> list:
    """ST6: No development tags."""
    findings = []
    for i, line in enumerate(sp.lines):
        for pattern, label in DEV_TAG_PATTERNS:
            if pattern.search(line):
                findings.append({
                    "check": "ST6",
                    "severity": "MINOR",
                    "detail": f"Development tag found: {label}",
                    "line_number": i + 1,
                    "context": line.strip()[:100],
                })
    return findings


def check_version_line(sp) -> list:
    """ST7: Version line present."""
    findings = []
    found = False
    for line in sp.lines[:30]:  # Check first 30 lines
        # Match both plain "Version: 1.0" and bold "**Version:** 03.12.26"
        # Also check inside HTML comments (version: 03.24.26)
        if re.search(r'[Vv]ersion\**\s*[:]\s*\**\s*\d', line) or \
           re.search(r'^v\d+\.\d+', line.strip()) or \
           re.search(r'\bversion:\s+\S', line, re.IGNORECASE):
            found = True
            break
    if not found:
        findings.append({
            "check": "ST7",
            "severity": "MINOR",
            "detail": "No version line found in first 30 lines",
        })
    return findings


def check_end_marker(sp) -> list:
    """ST8: End marker present and correctly formatted."""
    findings = []
    end_re = re.compile(r'^#\s+END OF MODULE', re.IGNORECASE)
    found = False
    for i, line in enumerate(sp.lines):
        if end_re.match(line.strip()):
            found = True
            # Check format
            if not re.match(r'^# END OF MODULE \d+ STARTER PACK', line.strip(), re.IGNORECASE):
                findings.append({
                    "check": "ST8",
                    "severity": "MINOR",
                    "detail": f"End marker format unexpected: '{line.strip()[:60]}'",
                    "line_number": i + 1,
                })
            break
    if not found:
        findings.append({
            "check": "ST8",
            "severity": "MAJOR",
            "detail": "End marker '# END OF MODULE [X] STARTER PACK' not found",
        })
    return findings


def check_h1_count(sp) -> list:
    """ST9: Exactly 3 H1s — Module title, BACKBONE, END OF MODULE."""
    findings = []
    h1_lines = []
    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        # Match H1: starts with exactly one '#' followed by space (not '##')
        if re.match(r'^#\s+[^#]', stripped):
            h1_lines.append((i + 1, stripped[:80]))

    if len(h1_lines) != 3:
        findings.append({
            "check": "ST9",
            "severity": "MAJOR",
            "detail": f"Expected exactly 3 H1s (Module title, BACKBONE, END OF MODULE), found {len(h1_lines)}",
            "h1s_found": [{"line": ln, "text": txt} for ln, txt in h1_lines],
        })
    else:
        # Verify the expected H1s
        _, text0 = h1_lines[0]
        _, text1 = h1_lines[1]
        _, text2 = h1_lines[2]
        if not re.search(r'MODULE\s+\d', text0, re.IGNORECASE):
            findings.append({
                "check": "ST9",
                "severity": "MINOR",
                "detail": f"First H1 doesn't look like a module title: '{text0}'",
                "line_number": h1_lines[0][0],
            })
        if 'BACKBONE' not in text1.upper():
            findings.append({
                "check": "ST9",
                "severity": "MAJOR",
                "detail": f"Second H1 should be 'BACKBONE', found: '{text1}'",
                "line_number": h1_lines[1][0],
            })
        if 'END OF MODULE' not in text2.upper():
            findings.append({
                "check": "ST9",
                "severity": "MAJOR",
                "detail": f"Third H1 should be 'END OF MODULE ...', found: '{text2}'",
                "line_number": h1_lines[2][0],
            })

    return findings


def check_no_h4(sp) -> list:
    """ST10: No H4s anywhere — use bold inline labels instead."""
    findings = []
    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        # Match H4: exactly four '#' followed by space (not '#####')
        if re.match(r'^#{4}\s+[^#]', stripped):
            findings.append({
                "check": "ST10",
                "severity": "MINOR",
                "detail": f"H4 heading found (use bold inline label instead): '{stripped[:70]}'",
                "line_number": i + 1,
            })
    return findings


# §1.7 internal ordering landmarks — canonical sequence per Structural Skeleton
_LESSON_ORDERING_LANDMARKS = [
    ("Required Phrases",       re.compile(r'^###\s+\**Required\s+Phrases', re.IGNORECASE)),
    ("Forbidden Phrases",      re.compile(r'^###\s+\**Forbidden\s+Phrases', re.IGNORECASE)),
    ("Purpose Frame",          re.compile(r'^###\s+\**Purpose\s+Frame', re.IGNORECASE)),
    ("Section 1",              re.compile(r'^###\s+\**Section\s+1\b', re.IGNORECASE)),
    ("Misconception Prevention", re.compile(r'^###\s+\**Misconception\s+Prevention', re.IGNORECASE)),
    ("Incomplete Script Flags", re.compile(r'^###\s+\**Incomplete\s+Script\s+Flags', re.IGNORECASE)),
    ("Success Criteria",       re.compile(r'^###\s+\**Success\s+Criteria', re.IGNORECASE)),
    ("Verification Checklist", re.compile(r'^###\s+\**Verification\s+Checklist', re.IGNORECASE)),
]


def check_lesson_internal_ordering(sp, gate: int) -> list:
    """ST11: §1.7 internal ordering follows Structural Skeleton sequence."""
    if gate < 2:
        return []

    findings = []

    # Find §1.7 and §1.8 boundaries
    lesson_start = None
    lesson_end = None
    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        if re.match(r'^##\s+\**§?1\.7\b', stripped, re.IGNORECASE) or \
           re.match(r'^##\s+\**LESSON\b', stripped, re.IGNORECASE):
            lesson_start = i
        elif lesson_start is not None and (
            re.match(r'^##\s+\**§?1\.8\b', stripped, re.IGNORECASE) or
            re.match(r'^##\s+\**EXIT\s+CHECK\b', stripped, re.IGNORECASE)
        ):
            lesson_end = i
            break

    if lesson_start is None:
        # §1.7 not found — ST3 already flags this
        return []
    if lesson_end is None:
        lesson_end = len(sp.lines)

    # Scan the §1.7 block for landmarks in order
    lesson_lines = sp.lines[lesson_start:lesson_end]
    found_landmarks = []
    for line_offset, line in enumerate(lesson_lines):
        stripped = line.strip()
        for name, pattern in _LESSON_ORDERING_LANDMARKS:
            if pattern.match(stripped):
                found_landmarks.append((name, lesson_start + line_offset + 1))
                break

    # Check ordering — each found landmark should appear after the previous
    last_idx = -1
    last_name = None
    for name, line_num in found_landmarks:
        expected_idx = next(
            (i for i, (n, _) in enumerate(_LESSON_ORDERING_LANDMARKS) if n == name),
            -1
        )
        if expected_idx < last_idx:
            findings.append({
                "check": "ST11",
                "severity": "MAJOR",
                "detail": f"§1.7 ordering violation: '{name}' (L{line_num}) appears after "
                         f"'{last_name}' — expected before it per Structural Skeleton",
                "line_number": line_num,
            })
        if expected_idx >= last_idx:
            last_idx = expected_idx
            last_name = name

    # Check that Required Phrases and Forbidden Phrases are BEFORE first interaction
    first_interaction_line = None
    for line_offset, line in enumerate(lesson_lines):
        stripped = line.strip()
        if re.match(r'^###\s+(?:Interaction\s+L\.?\d|Section\s+\d)', stripped, re.IGNORECASE):
            first_interaction_line = lesson_start + line_offset + 1
            break

    if first_interaction_line:
        for name, line_num in found_landmarks:
            if name in ("Required Phrases", "Forbidden Phrases") and line_num > first_interaction_line:
                findings.append({
                    "check": "ST11",
                    "severity": "CRITICAL",
                    "detail": f"'{name}' (L{line_num}) appears AFTER first interaction/section "
                             f"(L{first_interaction_line}) — must come BEFORE per Structural Skeleton",
                    "line_number": line_num,
                })

    return findings


def check_section_transition_markers(sp, gate: int) -> list:
    """ST12: Section transition markers (→ **SECTION X COMPLETE.**) in §1.7."""
    if gate < 2:
        return []

    findings = []

    # Find §1.7 boundaries
    lesson_start = None
    lesson_end = None
    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        if re.match(r'^##\s+\**§?1\.7\b', stripped, re.IGNORECASE) or \
           re.match(r'^##\s+\**LESSON\b', stripped, re.IGNORECASE):
            lesson_start = i
        elif lesson_start is not None and (
            re.match(r'^##\s+\**§?1\.8\b', stripped, re.IGNORECASE) or
            re.match(r'^##\s+\**EXIT\s+CHECK\b', stripped, re.IGNORECASE)
        ):
            lesson_end = i
            break

    if lesson_start is None:
        return []
    if lesson_end is None:
        lesson_end = len(sp.lines)

    lesson_lines = sp.lines[lesson_start:lesson_end]

    # Count section headers and transition markers
    section_headers = []
    transition_markers = []
    for line_offset, line in enumerate(lesson_lines):
        stripped = line.strip()
        if re.match(r'^###\s+\**Section\s+\d+\b', stripped, re.IGNORECASE):
            section_headers.append((lesson_start + line_offset + 1, stripped[:60]))
        if re.match(r'^→\s*\*\*SECTION\s+\d+\s+COMPLETE', stripped):
            transition_markers.append((lesson_start + line_offset + 1, stripped[:60]))

    if len(section_headers) >= 2 and len(transition_markers) == 0:
        findings.append({
            "check": "ST12",
            "severity": "MINOR",
            "detail": f"§1.7 has {len(section_headers)} sections but no transition markers "
                     f"(→ **SECTION X COMPLETE. PROCEED TO SECTION Y.**)",
        })
    elif len(section_headers) >= 2 and len(transition_markers) < len(section_headers) - 1:
        findings.append({
            "check": "ST12",
            "severity": "MINOR",
            "detail": f"§1.7 has {len(section_headers)} sections but only "
                     f"{len(transition_markers)} transition markers "
                     f"(expected {len(section_headers) - 1})",
        })

    return findings


# Verification checklists expected per phase
_PHASE_VERIFICATION_CHECKLISTS = {
    2: [  # Gate 2+
        ("Warmup", re.compile(r'(?:Warmup\s+)?Verification\s+Checklist\s*\(?\s*Warmup\s*\)?|Verification\s+Checklist\s*\(?\s*Warmup\s*\)?', re.IGNORECASE)),
        ("Lesson", re.compile(r'(?:Lesson\s+)?Verification\s+Checklist\s*\(?\s*Lesson\s*\)?|Verification\s+Checklist\s*\(?\s*Lesson\s*\)?', re.IGNORECASE)),
    ],
    3: [  # Gate 3+
        ("Warmup", re.compile(r'Verification\s+Checklist.*Warmup|Warmup\s+Verification\s+Checklist', re.IGNORECASE)),
        ("Lesson", re.compile(r'Verification\s+Checklist.*Lesson|Lesson\s+Verification\s+Checklist', re.IGNORECASE)),
        ("EC", re.compile(r'EC\s+Verification\s+Checklist|Exit\s+Check\s+Verification|Verification\s+Checklist.*EC|Verification\s+Checklist.*Exit\s+Check', re.IGNORECASE)),
        ("Synthesis", re.compile(r'Synthesis\s+Verification\s+Checklist|Verification\s+Checklist.*Synthesis', re.IGNORECASE)),
    ],
}


def check_verification_checklists(sp, gate: int) -> list:
    """ST13: Verification checklists present per phase."""
    if gate < 2:
        return []

    findings = []
    full_text = '\n'.join(sp.lines)

    expected = _PHASE_VERIFICATION_CHECKLISTS.get(gate, _PHASE_VERIFICATION_CHECKLISTS.get(3, []))
    # Gate 4 uses same as Gate 3
    if gate >= 3:
        expected = _PHASE_VERIFICATION_CHECKLISTS[3]

    for phase_name, pattern in expected:
        if not pattern.search(full_text):
            findings.append({
                "check": "ST13",
                "severity": "MINOR",
                "detail": f"Verification Checklist not found for {phase_name} phase",
            })

    return findings


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_structure_check(filepath: str, gate: int) -> dict:
    sp = parse_sp(filepath)
    all_findings = []

    # YAML checks (all gates)
    all_findings.extend(check_yaml(sp, gate))

    # Required sections
    all_findings.extend(check_required_sections(sp, gate))

    # Section ordering
    all_findings.extend(check_section_ordering(sp, gate))

    # Placeholder/dev tag scans (all gates)
    all_findings.extend(check_placeholders(sp, gate))
    all_findings.extend(check_dev_tags(sp, gate))

    # Version line (all gates)
    all_findings.extend(check_version_line(sp))

    # Heading hierarchy checks (all gates)
    all_findings.extend(check_h1_count(sp))
    all_findings.extend(check_no_h4(sp))

    # §1.7 internal ordering (Gate 2+)
    all_findings.extend(check_lesson_internal_ordering(sp, gate))

    # Section transition markers (Gate 2+)
    all_findings.extend(check_section_transition_markers(sp, gate))

    # Verification checklists (Gate 2+)
    all_findings.extend(check_verification_checklists(sp, gate))

    # End marker (Gate 4 only)
    if gate >= 4:
        all_findings.extend(check_end_marker(sp))

    checks_run = sorted(set(f["check"] for f in all_findings)) or [
        "ST1", "ST3", "ST4", "ST5", "ST6", "ST7", "ST9", "ST10",
    ]

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_structure_check",
        "file": filepath,
        "gate": gate,
        "checks_run": checks_run,
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "total_sections": len(sp.sections),
            "yaml_present": sp.yaml is not None,
            "module_id": sp.yaml.fields.get('module_id', 'MISSING') if sp.yaml else 'NO YAML',
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"STRUCTURE CHECK — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")
    print(f"Sections found: {result['meta'].get('total_sections', '?')}")
    print(f"Module ID: {result['meta'].get('module_id', '?')}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    if result['findings']:
        print(f"\n{'─'*80}")
        print("FINDINGS:")
        print(f"{'─'*80}")

        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            line = f.get('line_number', '')
            line_str = f" L{line}" if line else ""
            detail = f.get('detail', '')

            print(f"  [{check:3s}] {sev:8s} |{line_str} {detail}")

            if 'context' in f:
                print(f"           {f['context'][:70]}")
    else:
        print("\n  ✓ No findings.")


def main():
    parser = argparse.ArgumentParser(description="SP Structure Checker")
    parser.add_argument("sp_file", help="Path to the Starter Pack markdown file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_structure_check(args.sp_file, args.gate)

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
