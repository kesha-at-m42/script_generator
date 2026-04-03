#!/usr/bin/env python3
"""
sp_notion_pull.py — Convert Notion-fetched SP content to local evaluable format.

Takes a Notion fetch JSON result (saved to file) and converts it to the
standard Notion-ready markdown format that the evaluation pipeline expects.

Usage:
  python sp_notion_pull.py <notion_json_file> --module <N> [--output PATH]

  # Or pipe from stdin:
  cat notion_result.json | python sp_notion_pull.py - --module 3

The input JSON should be the raw result from the Notion MCP fetch tool.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime


def extract_content_from_notion(raw_text: str) -> str:
    """Extract the <content>...</content> block from Notion enhanced markdown."""
    # The content is between <content> and </content> tags
    match = re.search(r'<content>\s*\n?(.*?)\s*</content>', raw_text, re.DOTALL)
    if match:
        return match.group(1)

    # Fallback: if no <content> tags, try to find the markdown body
    # (starts after </properties> or after the metadata section)
    match = re.search(r'</properties>\s*\n?(.*)', raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()

    return raw_text


def extract_properties(raw_text: str) -> dict:
    """Extract properties from the <properties> JSON block."""
    match = re.search(r'<properties>\s*\n?(\{.*?\})\s*\n?</properties>', raw_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    return {}


def extract_title(raw_text: str) -> str:
    """Extract the page title from the Notion response."""
    # Look for title in the JSON wrapper
    match = re.search(r'"title"\s*:\s*"([^"]+)"', raw_text)
    if match:
        return match.group(1)
    return ""


def clean_notion_markdown(content: str) -> str:
    """Strip Notion-specific markup that the checkers don't understand."""
    # Remove <mention-user> tags
    content = re.sub(r'<mention-user[^>]*>.*?</mention-user>', '', content)
    # Remove <mention-page> tags but keep the text
    content = re.sub(r'<mention-page[^>]*>(.*?)</mention-page>', r'\1', content)
    # Remove <bookmark> tags
    content = re.sub(r'<bookmark[^>]*>.*?</bookmark>', '', content)
    # Remove <callout> wrapper but keep content
    content = re.sub(r'<callout[^>]*>\s*', '', content)
    content = re.sub(r'\s*</callout>', '', content)
    # Remove <toggle> wrappers
    content = re.sub(r'<toggle[^>]*>\s*', '', content)
    content = re.sub(r'\s*</toggle>', '', content)
    # Remove inline <page> references but keep text
    content = re.sub(r'<page[^>]*>(.*?)</page>', r'\1', content)
    # Remove synced block markers
    content = re.sub(r'<synced-block[^>]*>\s*', '', content)
    content = re.sub(r'\s*</synced-block>', '', content)
    # Remove discussion/comment span wrappers but keep text
    content = re.sub(r'<span\s+discussion-urls=[^>]*>(.*?)</span>', r'\1', content)
    # Clean up any remaining Notion HTML-like tags
    content = re.sub(r'</?(?:column-list|column)[^>]*>', '', content)
    return content


def build_hub_properties(props: dict, module_num: int, title: str) -> str:
    """Build the Hub Properties HTML comment block."""
    # Extract and format properties
    unit_raw = props.get('Unit', 'Unit 2')
    unit_num = re.search(r'\d+', str(unit_raw))
    unit = unit_num.group(0) if unit_num else '2'

    lessons = props.get('IM/OUR Lessons', [])
    if isinstance(lessons, str):
        lessons = [lessons]
    lessons_str = ', '.join(lessons) if lessons else ''

    status = props.get('Status', 'Draft')

    # Primary/Secondary toys come as relation URLs — we can only show the URL
    # The skill should resolve these by fetching the related pages
    primary_toys = props.get('Primary Toys', [])
    if isinstance(primary_toys, list) and primary_toys:
        # These are page URLs; mark as needing resolution
        primary_str = f"(relation — {len(primary_toys)} linked)"
    else:
        primary_str = str(primary_toys) if primary_toys else 'none'

    secondary_toys = props.get('Secondary Toys', [])
    if isinstance(secondary_toys, list) and secondary_toys:
        secondary_str = f"(relation — {len(secondary_toys)} linked)"
    else:
        secondary_str = 'none'

    return f"""<!-- HUB PROPERTIES (set manually after import):
  module_id: M{module_num:02d}
  module_title: {title}
  domain: measurement_area
  unit: {unit}
  primary_toys: {primary_str}
  secondary_toys: {secondary_str}
  our_lessons: {lessons_str}
  status: {status}
-->"""


def convert_notion_to_local(input_text: str, module_num: int, output_path: str = None) -> str:
    """
    Convert Notion fetch result to local Notion-ready markdown format.

    Returns the converted markdown string.
    """
    # Parse the JSON if it looks like JSON
    raw_text = input_text
    if input_text.strip().startswith('['):
        try:
            data = json.loads(input_text)
            if isinstance(data, list) and len(data) > 0:
                raw_text = data[0].get('text', '')
                if isinstance(raw_text, str) and raw_text.startswith('{'):
                    inner = json.loads(raw_text)
                    raw_text = inner.get('text', raw_text)
        except (json.JSONDecodeError, KeyError):
            pass
    elif input_text.strip().startswith('{'):
        try:
            data = json.loads(input_text)
            raw_text = data.get('text', input_text)
        except json.JSONDecodeError:
            pass

    # Extract components
    title = extract_title(input_text)
    props = extract_properties(raw_text)
    content = extract_content_from_notion(raw_text)
    content = clean_notion_markdown(content)

    # Build the module title from the page title or properties
    if not title:
        title = props.get('Name', f'Module {module_num}')

    # Strip "Module N: " prefix if present (we'll add our own)
    title_clean = re.sub(r'^Module\s+\d+\s*:\s*', '', title).strip()

    # Assemble the file
    lines = []
    lines.append(f"# MODULE {module_num}: {title_clean}")
    lines.append("")
    lines.append(f"**Version:** {datetime.now().strftime('%m.%d.%y')} (Notion pull)")
    lines.append("")
    lines.append(build_hub_properties(props, module_num, title_clean))
    lines.append("")

    # Add the content body
    # The content from Notion may already start with "# BACKBONE" — keep it
    lines.append(content)

    result = '\n'.join(lines)

    # Write output if path specified
    if output_path:
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Written to: {output_path}", file=sys.stderr)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Convert Notion-fetched SP to local evaluable format"
    )
    parser.add_argument(
        "input_file",
        help="Path to Notion fetch JSON result file (or '-' for stdin)"
    )
    parser.add_argument(
        "--module", "-m",
        type=int,
        required=True,
        help="Module number (e.g., 3 for M03)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (default: stdout)"
    )
    args = parser.parse_args()

    # Read input
    if args.input_file == '-':
        input_text = sys.stdin.read()
    else:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()

    result = convert_notion_to_local(input_text, args.module, args.output)

    if not args.output:
        print(result)


if __name__ == '__main__':
    main()
