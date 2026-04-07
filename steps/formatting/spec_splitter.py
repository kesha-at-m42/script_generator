"""
spec_splitter - Formatting Step

Deterministically splits a raw markdown spec (lesson/warmup/synthesis/exitcheck)
into one item per interaction or transition section.

Detected header patterns:
  ### Interaction X.Y: <title>      (lesson specs)
  ## Section W.X: <title>           (warmup specs)
  ### W.Xa: <title>                 (warmup sub-sections)
  **[SECTION N TRANSITION]**        (in-lesson transition blocks)
  Bridge to Exit Check              (closing bridge)

Preamble (content before the first header) and trailing metadata are excluded.

Output: [{index, major, minor, header, body}, ...]
  - index:  0-based position in the spec (used as batch_id_field)
  - major:  top-level group number (e.g. Interaction 2.x → 2)
  - minor:  sequential counter within the major group, starting at 1
  - header: raw header line from the spec
  - body:   spec content for this section (fields, bullets, tables)
"""

import re
from collections import defaultdict

# Matches the start of a real interaction/section header line.
# Does NOT match meta-headers like "### 1.7.1 LESSON SECTION 1: ..." (start with digits).
_HEADER_RE = re.compile(
    r'^(?:'
    r'#{2,3}\s+Interaction\s+\d+\.\d+[^\n]*'         # ### Interaction X.Y: ...
    r'|'
    r'#{2,3}\s+Section\s+W\.\d+[^\n]*'               # ## Section W.X: ...
    r'|'
    r'#{2,3}\s+W\.\d+[a-z][^\n]*'                    # ### W.3a: ...
    r'|'
    r'\*\*\[SECTION\s+\d+\s+TRANSITION\]\*\*[^\n]*'  # **[SECTION N TRANSITION]**
    r'|'
    r'Bridge to Exit Check[^\n]*'                     # Bridge to Exit Check
    r')',
    re.MULTILINE,
)


def _extract_major(header: str, last_major: int) -> int:
    """Derive the major group number from a header line."""
    # Interaction X.Y → X
    m = re.search(r'Interaction\s+(\d+)\.', header)
    if m:
        return int(m.group(1))
    # Section W.X → X
    m = re.search(r'Section\s+W\.(\d+)', header, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # W.Xa → X
    m = re.search(r'W\.(\d+)[a-z]', header, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # [SECTION N TRANSITION] → N
    m = re.search(r'SECTION\s+(\d+)\s+TRANSITION', header, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Bridge / other unlabelled → inherit last major
    return last_major


def split_spec(input_data, **kwargs):
    """
    Split a raw markdown spec into sections.

    Args:
        input_data: Raw markdown string (lesson.md / warmup.md / etc.)

    Returns:
        List of {index, major, minor, header, body} dicts.
    """
    text = input_data if isinstance(input_data, str) else ""
    if not text:
        return []

    matches = list(_HEADER_RE.finditer(text))
    if not matches:
        return []

    minor_counters: dict = defaultdict(int)
    last_major = 1
    sections = []

    for i, match in enumerate(matches):
        header = match.group(0).strip()
        major = _extract_major(header, last_major)
        last_major = major

        minor_counters[major] += 1
        minor = minor_counters[major]

        body_start = match.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()

        sections.append({
            "index": i,
            "major": major,
            "minor": minor,
            "header": header,
            "body": body,
        })

    return sections
