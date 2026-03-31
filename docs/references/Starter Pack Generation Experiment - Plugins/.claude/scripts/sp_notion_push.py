#!/usr/bin/env python3
"""
sp_notion_push.py — Convert local Notion-ready SP to Notion page format.

Strips local-only artifacts (# MODULE H1, Hub Properties block) and outputs:
  1. Page content (markdown body suitable for Notion create/replace)
  2. Database properties (JSON for the 📖 Level Curriculum Documents schema)

The Notion page title IS the module name, and database columns hold the
properties — so those local elements don't belong in the page body.

Usage:
  python sp_notion_push.py <local_sp.md> [--json] [--content-only]

  --json           Output structured JSON with 'content' and 'properties' keys
  --content-only   Output just the markdown body (for piping to Notion tools)
"""

import argparse
import json
import os
import re
import sys


def parse_hub_properties(lines: list[str]) -> dict:
    """Extract properties from the <!-- HUB PROPERTIES --> comment block."""
    props = {}
    in_hub = False
    for line in lines[:40]:  # Hub block is always near the top
        if '<!--' in line and ('hub' in line.lower() or 'properties' in line.lower()):
            in_hub = True
            continue
        if in_hub and '-->' in line:
            break
        if in_hub:
            # Parse "  key: value" lines
            m = re.match(r'\s+(\w[\w_]*)\s*:\s*(.*)', line)
            if m:
                props[m.group(1)] = m.group(2).strip()
    return props


def parse_yaml_front_matter(lines: list[str]) -> dict:
    """Extract properties from YAML front matter (pre-conversion format)."""
    props = {}
    if not lines or lines[0].strip() != '---':
        return props
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            break
        m = re.match(r'(\w[\w_]*)\s*:\s*(.*)', line)
        if m:
            props[m.group(1)] = m.group(2).strip()
    return props


def extract_module_title(lines: list[str]) -> str:
    """Get the module title from the first H1 heading."""
    for line in lines[:10]:
        m = re.match(r'^#\s+MODULE\s+\d+\s*:\s*(.*)', line, re.IGNORECASE)
        if m:
            return m.group(1).strip()
        # Also handle "# Module N: Title" without caps
        m = re.match(r'^#\s+(?:Module\s+)?\d+\s*:\s*(.*)', line, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def extract_module_number(lines: list[str], props: dict) -> int:
    """Get module number from H1, Hub Properties, or YAML."""
    # Try Hub/YAML props first
    mid = props.get('module_id', '')
    m = re.search(r'M?0*(\d+)', mid)
    if m:
        return int(m.group(1))

    # Try the H1
    for line in lines[:10]:
        m = re.match(r'^#\s+MODULE\s+(\d+)', line, re.IGNORECASE)
        if m:
            return int(m.group(1))

    return 0


def strip_local_artifacts(content: str) -> str:
    """
    Remove local-only elements from the SP content to produce
    a clean Notion page body:
      - The # MODULE N: H1 line (Notion uses page title)
      - The **Version:** line (metadata, not content)
      - The <!-- HUB PROPERTIES --> block (Notion uses DB columns)
      - Leading/trailing whitespace
    """
    lines = content.split('\n')
    output = []
    skip_hub = False
    skip_yaml = False
    first_line = True

    for i, line in enumerate(lines):
        # Skip YAML front matter
        if first_line and line.strip() == '---':
            skip_yaml = True
            first_line = False
            continue
        first_line = False

        if skip_yaml:
            if line.strip() == '---':
                skip_yaml = False
            continue

        # Skip Hub Properties comment block
        if '<!--' in line and ('hub' in line.lower() or 'properties' in line.lower()):
            skip_hub = True
            continue
        if skip_hub:
            if '-->' in line:
                skip_hub = False
            continue

        # Skip the # MODULE H1
        if re.match(r'^#\s+MODULE\s+\d+', line, re.IGNORECASE):
            continue

        # Skip the Version line
        if re.match(r'^\*\*Version:\*\*', line.strip()):
            continue

        output.append(line)

    # Clean leading blank lines
    while output and not output[0].strip():
        output.pop(0)

    return '\n'.join(output)


def build_notion_properties(props: dict, module_num: int, title: str) -> dict:
    """
    Build the database properties dict matching the
    📖 Level Curriculum Documents schema:
      Name (title), Module Number, Unit, Status, IM/OUR Lessons
    """
    db_props = {}

    # Name (title field) — "Module N: Title"
    full_title = f"Module {module_num}: {title}" if title else f"Module {module_num}"
    db_props["Name"] = full_title

    # Module Number
    db_props["Module Number"] = module_num

    # Unit
    unit = props.get('unit', '')
    if unit and not unit.startswith('Unit'):
        unit = f"Unit {unit}"
    if unit:
        db_props["Unit"] = unit

    # Status — map local status values to DB options
    status = props.get('status', '')
    status_map = {
        'draft': 'Initial Draft',
        'initial draft': 'Initial Draft',
        'sme review': 'SME Review',
        'resolutions': 'Resolutions Pass',
        'resolutions pass': 'Resolutions Pass',
        'ready': 'Ready for Script Pipeline',
    }
    mapped = status_map.get(status.lower(), status) if status else None
    if mapped:
        db_props["Status"] = mapped

    # IM/OUR Lessons — stored as JSON array of strings
    lessons = props.get('our_lessons', '')
    if lessons:
        lesson_list = [l.strip() for l in lessons.split(',') if l.strip()]
        if lesson_list:
            db_props["IM/OUR Lessons"] = json.dumps(lesson_list)

    return db_props


def convert_local_to_notion(filepath: str) -> dict:
    """
    Convert a local SP file to Notion-ready format.

    Returns:
        {
            "content": str,       # Markdown body for Notion page
            "properties": dict,   # Database column values
            "module_num": int,
            "title": str,
        }
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    lines = raw.split('\n')

    # Extract metadata from whichever format is present
    hub_props = parse_hub_properties(lines)
    yaml_props = parse_yaml_front_matter(lines)
    props = {**yaml_props, **hub_props}  # Hub overrides YAML if both present

    title = extract_module_title(lines)
    module_num = extract_module_number(lines, props)

    # Strip local-only artifacts
    content = strip_local_artifacts(raw)

    # Build Notion DB properties
    db_properties = build_notion_properties(props, module_num, title)

    return {
        "content": content,
        "properties": db_properties,
        "module_num": module_num,
        "title": title,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Convert local SP to Notion page format"
    )
    parser.add_argument("sp_file", help="Path to the local SP markdown file")
    parser.add_argument("--json", action="store_true",
                        help="Output structured JSON")
    parser.add_argument("--content-only", action="store_true",
                        help="Output just the markdown body")
    args = parser.parse_args()

    result = convert_local_to_notion(args.sp_file)

    if args.content_only:
        print(result["content"])
    elif args.json:
        print(json.dumps(result, indent=2))
    else:
        # Default: show summary + content
        print(f"Module: M{result['module_num']:02d} — {result['title']}")
        print(f"Properties: {json.dumps(result['properties'])}")
        print(f"Content length: {len(result['content'])} chars")
        print(f"\n--- Content preview (first 20 lines) ---")
        for line in result['content'].split('\n')[:20]:
            print(line)


if __name__ == '__main__':
    main()
