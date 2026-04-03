"""
phase_splitter - Formatting Step

Reads _starter_pack_ref.md (raw Notion starter pack content) and deterministically
splits it into four phase markdown files by section heading:

  ## 1.6 WARMUP     → warmup.md
  ## 1.7 LESSON     → lesson.md
  ## 1.8 EXIT CHECK → exitcheck.md
  ## 1.9 SYNTHESIS  → synthesis.md

Also converts Notion HTML table markup to markdown tables.

Returns a dict of {phase: content} so the result can be inspected, but the
primary output is the written .md files in the module directory.
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Maps phase keyword → output filename
PHASE_FILES = {
    "warmup": "warmup.md",
    "lesson": "lesson.md",
    "exit check": "exitcheck.md",
    "synthesis": "synthesis.md",
}

# Regex: matches top-level phase headings (## only, not ###) like:
#   "## 1.6 WARMUP", "## **1.6 WARMUP (~3 minutes)**"
# Requiring exactly ## prevents sub-headings like "### Exit Check Closure" from matching.
_SECTION_RE = re.compile(
    r'^(##\s+\**\s*(?:\d+\.\d+\s+)?(WARMUP|LESSON|EXIT CHECK|SYNTHESIS)\b)',
    re.IGNORECASE | re.MULTILINE,
)


# ---------------------------------------------------------------------------
# HTML table → markdown converter
# ---------------------------------------------------------------------------

def _parse_table(table_html: str) -> str:
    """Convert a single <table> block to a markdown table string."""
    has_header = 'header-row="true"' in table_html or "header-row='true'" in table_html

    # Extract all rows
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
    if not rows:
        return table_html  # can't parse — return as-is

    md_rows = []
    for row in rows:
        # Extract cells (td or th)
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL)
        # Clean cell content: strip inner HTML tags, normalise whitespace
        cleaned = []
        for cell in cells:
            # Replace <br> with space
            cell = re.sub(r'<br\s*/?>', ' ', cell, flags=re.IGNORECASE)
            # Strip remaining HTML tags
            cell = re.sub(r'<[^>]+>', '', cell)
            # Collapse whitespace, strip
            cell = re.sub(r'\s+', ' ', cell).strip()
            # Escape pipe characters inside cells
            cell = cell.replace('|', '/')
            cleaned.append(cell)
        if cleaned:
            md_rows.append(cleaned)

    if not md_rows:
        return table_html

    # Determine column count from widest row
    ncols = max(len(r) for r in md_rows)

    # Pad all rows to same width
    md_rows = [r + [''] * (ncols - len(r)) for r in md_rows]

    lines = []
    if has_header:
        # First row is the header
        lines.append('| ' + ' | '.join(md_rows[0]) + ' |')
        lines.append('| ' + ' | '.join(['---'] * ncols) + ' |')
        for row in md_rows[1:]:
            lines.append('| ' + ' | '.join(row) + ' |')
    else:
        for row in md_rows:
            lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(lines)


def _convert_html_tables(text: str) -> str:
    """Replace all <table>...</table> blocks with markdown tables."""
    def replace_table(m):
        return _parse_table(m.group(0))

    return re.sub(r'<table[^>]*>.*?</table>', replace_table, text, flags=re.DOTALL)


def _clean_notion_markup(text: str) -> str:
    """Remove Notion-specific XML tags that aren't content."""
    # Remove colgroup/col blocks entirely
    text = re.sub(r'<colgroup>.*?</colgroup>', '', text, flags=re.DOTALL)
    # Remove any remaining lone HTML tags (not inside tables — those are handled above)
    text = re.sub(r'<(?:br|hr)\s*/?>', '\n', text, flags=re.IGNORECASE)
    return text


# ---------------------------------------------------------------------------
# Section splitter
# ---------------------------------------------------------------------------

def _split_phases(text: str) -> dict:
    """
    Split starter pack content into phase sections by heading.

    Returns dict with keys: warmup, lesson, exitcheck, synthesis.
    Each value is the full text of that section (including its heading line).
    """
    matches = list(_SECTION_RE.finditer(text))
    if not matches:
        return {}

    phases = {}
    for i, m in enumerate(matches):
        heading_lower = m.group(2).lower()  # "warmup", "lesson", etc.

        # Find the phase key
        phase_key = None
        for key in PHASE_FILES:
            if key in heading_lower:
                phase_key = key
                break
        if not phase_key:
            continue

        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section_text = text[start:end].strip()
        phases[phase_key] = section_text

    return phases


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def split_phases(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    output_file_path: Path = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Split _starter_pack_ref.md into phase markdown files.

    Reads the raw starter pack text, splits by section heading, converts HTML
    tables to markdown, and writes warmup.md / lesson.md / exitcheck.md /
    synthesis.md to the module directory.

    Args:
        input_data: Raw text content of _starter_pack_ref.md
        unit_number: Unit number for locating module directory
        module_number: Module number for locating module directory
        output_file_path: Pipeline output path (used to locate module dir if needed)
        verbose: Enable verbose logging
    """
    if isinstance(input_data, (dict, list)):
        # Shouldn't happen — input should be raw text
        if verbose:
            print("  [PHASE_SPLITTER] Unexpected JSON input — expected raw markdown text")
        return input_data

    text = input_data if isinstance(input_data, str) else str(input_data)

    # 1. Clean up Notion markup
    text = _clean_notion_markup(text)

    # 2. Convert HTML tables
    text = _convert_html_tables(text)

    # 3. Split by phase heading
    phases = _split_phases(text)

    if not phases:
        print("  [PHASE_SPLITTER] WARNING: No phase sections found in input")
        return {}

    # 4. Locate module directory
    if unit_number is not None and module_number is not None:
        module_dir = project_root / "units" / f"unit{unit_number}" / f"module{module_number}"
    elif output_file_path is not None:
        # Fall back to inferring from pipeline output path
        module_dir = None
        for part in output_file_path.parts:
            if part.startswith("module"):
                module_dir = project_root / "units" / f"unit{unit_number or 1}" / part
                break
    else:
        module_dir = None

    # 5. Write files
    written = []
    for phase_key, filename in PHASE_FILES.items():
        content = phases.get(phase_key)
        if not content:
            if verbose:
                print(f"  [PHASE_SPLITTER] No content for '{phase_key}' — skipping {filename}")
            continue

        if module_dir and module_dir.exists():
            out_path = module_dir / filename
            out_path.write_text(content, encoding="utf-8")
            written.append(filename)
            if verbose:
                print(f"  [PHASE_SPLITTER] {filename} ({len(content)} chars)")

    if written:
        print(f"  [PHASE_SPLITTER] Written to module{module_number}: {', '.join(written)}")
    elif module_dir:
        print(f"  [PHASE_SPLITTER] WARNING: module dir not found: {module_dir}")

    return phases
