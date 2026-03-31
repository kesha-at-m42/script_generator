#!/usr/bin/env python3
"""
sp_notion_convert_check.py — Notion conversion compliance checker (standalone).

NOT part of the gate system. Runs after Notion conversion, before Gate 4.

Checks:
  NC1: YAML front matter replaced with HTML comment block
  NC2: Interaction headers at H3 level (not bold)
  NC3: KDD items at H3 level (not numbered list)
  NC4: No [Type A/B/C] labels in headers
  NC5: Bullet style uses * not - (except checklists)
  NC6: No old field names (Method:, Validation:, Detail Level:)
  NC7: All Student Action: (not Method:), all Correct Answer: (not Validation:)
  NC8: Exactly 3 H1s: Module title, BACKBONE, END OF MODULE
  NC9: No H4 headings anywhere (Structural Skeleton rule)
  NC10: All numbered sections (1.0–1.10) are H2
  NC11: Hub Properties block contains required fields

Usage:
  python sp_notion_convert_check.py <notion_ready_file.md> [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys


def run_notion_check(filepath: str) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    all_findings = []

    # NC1: YAML should be replaced with HTML comment
    has_yaml = False
    has_html_comment = False
    for i, line in enumerate(lines[:30]):
        if line.strip() == '---':
            has_yaml = True
        if '<!--' in line and ('hub' in line.lower() or 'properties' in line.lower()):
            has_html_comment = True

    if has_yaml and not has_html_comment:
        all_findings.append({
            "check": "NC1",
            "severity": "MAJOR",
            "detail": "YAML front matter not replaced with HTML comment block",
        })

    # NC2: Interaction headers should be H3 (not bold)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('**Interaction') and not stripped.startswith('#'):
            all_findings.append({
                "check": "NC2",
                "severity": "MAJOR",
                "detail": f"Bold interaction header should be H3: '{stripped[:60]}'",
                "line_number": i + 1,
            })

    # NC3: KDD items should be H3
    in_kdd = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^##.*(?:KDD|Working Notes|1\.10)', stripped, re.IGNORECASE):
            in_kdd = True
        elif stripped.startswith('##') and in_kdd:
            if '1.11' in stripped or 'END OF' in stripped:
                in_kdd = False
        if in_kdd and re.match(r'^\d+\.\s+\*\*KDD', stripped):
            all_findings.append({
                "check": "NC3",
                "severity": "MAJOR",
                "detail": f"KDD item should be H3 heading, not numbered list: '{stripped[:60]}'",
                "line_number": i + 1,
            })

    # NC4: No [Type A/B/C] in headers
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('#') and re.search(r'\[Type [ABC]\]', stripped):
            all_findings.append({
                "check": "NC4",
                "severity": "MAJOR",
                "detail": f"Legacy [Type A/B/C] label in header: '{stripped[:60]}'",
                "line_number": i + 1,
            })

    # NC5: Bullet style check (* not -)
    dash_bullet_count = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip checklist items (- [ ] or - [x])
        if stripped.startswith('- ['):
            continue
        if re.match(r'^-\s+', stripped) and not stripped.startswith('---'):
            dash_bullet_count += 1
            if dash_bullet_count <= 5:  # Only report first 5
                all_findings.append({
                    "check": "NC5",
                    "severity": "MINOR",
                    "detail": f"Dash bullet should use asterisk: '{stripped[:60]}'",
                    "line_number": i + 1,
                })

    if dash_bullet_count > 5:
        all_findings.append({
            "check": "NC5",
            "severity": "MINOR",
            "detail": f"... and {dash_bullet_count - 5} more dash bullets found",
        })

    # NC6: No old field names
    old_fields = [
        (re.compile(r'\*\*Method:\*\*'), "Method:"),
        (re.compile(r'\*\*Validation:\*\*'), "Validation:"),
        (re.compile(r'Detail Level:'), "Detail Level:"),
    ]
    for i, line in enumerate(lines):
        for pattern, label in old_fields:
            if pattern.search(line):
                all_findings.append({
                    "check": "NC6",
                    "severity": "MAJOR",
                    "detail": f"Old field name '{label}' found — should be converted",
                    "line_number": i + 1,
                })

    # NC7: Student Action / Correct Answer naming
    for i, line in enumerate(lines):
        if '**Method:**' in line and '**Student Action:**' not in line:
            all_findings.append({
                "check": "NC7",
                "severity": "MAJOR",
                "detail": "Field 'Method:' should be 'Student Action:'",
                "line_number": i + 1,
            })
        if '**Validation:**' in line and '**Correct Answer:**' not in line:
            all_findings.append({
                "check": "NC7",
                "severity": "MAJOR",
                "detail": "Field 'Validation:' should be 'Correct Answer:'",
                "line_number": i + 1,
            })

    # NC8: Exactly 3 H1s — Module title, BACKBONE, END OF MODULE
    h1_lines = []
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            h1_lines.append((i + 1, line.strip()))

    if len(h1_lines) != 3:
        all_findings.append({
            "check": "NC8",
            "severity": "MAJOR",
            "detail": f"Expected exactly 3 H1 headings, found {len(h1_lines)}",
        })
        for ln, text in h1_lines:
            all_findings.append({
                "check": "NC8",
                "severity": "MINOR",
                "detail": f"H1 at line {ln}: '{text[:60]}'",
                "line_number": ln,
            })
    else:
        # Verify identity of each H1
        # H1 #1 should be module title (# MODULE N: ...)
        if not re.match(r'^#\s+MODULE\s+\d+', h1_lines[0][1], re.IGNORECASE):
            all_findings.append({
                "check": "NC8",
                "severity": "MAJOR",
                "detail": f"First H1 should be module title (# MODULE N: ...), got: '{h1_lines[0][1][:60]}'",
                "line_number": h1_lines[0][0],
            })
        # H1 #2 should be BACKBONE
        if 'BACKBONE' not in h1_lines[1][1].upper():
            all_findings.append({
                "check": "NC8",
                "severity": "MAJOR",
                "detail": f"Second H1 should be '# BACKBONE', got: '{h1_lines[1][1][:60]}'",
                "line_number": h1_lines[1][0],
            })
        # H1 #3 should be END OF MODULE
        if 'END OF MODULE' not in h1_lines[2][1].upper():
            all_findings.append({
                "check": "NC8",
                "severity": "MAJOR",
                "detail": f"Third H1 should be '# END OF MODULE', got: '{h1_lines[2][1][:60]}'",
                "line_number": h1_lines[2][0],
            })

    # NC9: No H4 headings (Structural Skeleton: use bold inline labels instead)
    for i, line in enumerate(lines):
        if line.startswith('#### '):
            all_findings.append({
                "check": "NC9",
                "severity": "MINOR",
                "detail": f"H4 heading found (should be H3 or bold label): '{line.strip()[:60]}'",
                "line_number": i + 1,
            })

    # NC10: All numbered sections (1.0–1.10) must be H2
    # Negative lookahead excludes subsections like 1.1.1, 1.1.2 etc.
    section_re = re.compile(r'^(#{1,6})\s+(1\.\d{1,2})\b(?!\.\d)')
    for i, line in enumerate(lines):
        m = section_re.match(line.strip())
        if m:
            level = len(m.group(1))
            section_num = m.group(2)
            if level != 2:
                all_findings.append({
                    "check": "NC10",
                    "severity": "MAJOR",
                    "detail": f"Section §{section_num} is H{level}, must be H2",
                    "line_number": i + 1,
                })

    # NC11: Hub Properties block has required fields
    if has_html_comment:
        hub_block = ""
        in_hub = False
        for line in lines[:30]:
            if '<!--' in line and ('hub' in line.lower() or 'properties' in line.lower()):
                in_hub = True
            if in_hub:
                hub_block += line + "\n"
            if in_hub and '-->' in line:
                break

        required_hub_fields = [
            "module_id", "module_title", "domain", "unit",
            "primary_toys", "status",
        ]
        for field in required_hub_fields:
            if field + ":" not in hub_block:
                all_findings.append({
                    "check": "NC11",
                    "severity": "MAJOR",
                    "detail": f"Hub Properties missing required field: '{field}'",
                })

    checks_run = sorted(set(f["check"] for f in all_findings)) or [
        "NC1", "NC2", "NC3", "NC4", "NC5", "NC6", "NC7",
        "NC8", "NC9", "NC10", "NC11",
    ]

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_notion_convert_check",
        "file": filepath,
        "checks_run": checks_run,
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
    }


def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"NOTION CONVERSION CHECK — {result['file']}")
    print(f"{'='*80}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    if result['findings']:
        print(f"\n{'─'*80}")
        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            line = f.get('line_number', '')
            line_str = f" L{line}" if line else ""
            detail = f.get('detail', '')
            print(f"  [{check}] {sev:8s} |{line_str} {detail}")
    else:
        print("\n  ✓ No findings — Notion conversion looks clean.")


def main():
    parser = argparse.ArgumentParser(description="SP Notion Conversion Checker")
    parser.add_argument("sp_file", help="Path to the Notion-ready markdown file")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_notion_check(args.sp_file)

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
