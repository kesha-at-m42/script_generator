"""
spec_splitter - Formatting Step

Deterministically splits a raw markdown spec (lesson/warmup/synthesis/exitcheck)
into one item per interaction or transition section.

Detected header patterns:
  ### Interaction X.Y: <title>           (lesson specs)
  ### Interaction W.N: <title>           (warmup specs)
  ### Interaction S.N: <title>           (synthesis specs — bold variant allowed)
  ## Section W.X: <title>               (warmup sub-sections)
  ### W.Xa: <title>                      (warmup sub-sections)
  **[SECTION N TRANSITION]**             (in-lesson transition blocks)
  Bridge to <word>                       (closing bridge — lesson, warmup)
  Problem EC.N: <title>                  (exitcheck problems)
  **Task S.N: <title>                    (synthesis tasks — bold variant; ### prefix optional)
  ### Transition into Exit Check         (exitcheck opener)
  ### Exit Check Closure                 (exitcheck closer)
  ### Opening Hook                        (warmup opener — bold variant allowed)
  ### Opening Frame                      (synthesis opener — bold variant allowed)
  ### Metacognitive Reflection           (synthesis reflection — #### and bold variants allowed)
  ### Identity-Building Closure          (synthesis closer — bold variant allowed)

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

# Matches any ## or ### header — used to detect trailing metadata sections
# (Required Phrases, Forbidden Phrases, etc.) that should not be captured
# in the last interaction section's body.
_META_HEADER_RE = re.compile(r"^#{2,3}\s+\S", re.MULTILINE)

# Matches the start of a real interaction/section header line.
# Does NOT match meta-headers like "### 1.7.1 LESSON SECTION 1: ..." (start with digits).
_HEADER_RE = re.compile(
    r'^(?:'
    r'#{2,3}\s+\*{0,2}Interaction\s+\d+\.\d+[^\n]*'    # ### Interaction X.Y: ... (lesson), bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Interaction\s+W\.\d+[^\n]*'      # ### Interaction W.N: ... (warmup), bold variant allowed
    r'|'
    r'#{2,3}\s+Section\s+W\.\d+[^\n]*'                 # ## Section W.X: ...
    r'|'
    r'#{2,3}\s+W\.\d+[a-z][^\n]*'                      # ### W.3a: ...
    r'|'
    r'\*\*\\?\[SECTION(?:\s+\d+)?\s+TRANSITION\\?\]\*\*[^\n]*'  # **[SECTION N TRANSITION]** or **\[SECTION TRANSITION\]** (escaped brackets)
    r'|'
    r'(?:#{2,3}\s+\*{0,2})?Bridge to \w[^\n]*'         # Bridge to Lesson / Bridge to Exit Check (plain or ### **Bridge to)
    r'|'
    r'(?:#{2,3}\s+\*{0,2})?\*{0,2}Problem\s+EC\.\d+:[^\n]*'   # ### Problem EC.1: / **Problem EC.1: (exitcheck, with or without heading)
    r'|'
    r'#{2,3}\s+\*{0,2}Interaction\s+S\.\d+[^\n]*'      # ### Interaction S.N: ... (synthesis), bold variant allowed
    r'|'
    r'(?:#{2,3}\s+)?\*{0,2}(?:Synthesis\s+)?Task\s+S\.\d+:[^\n]*'  # **Task S.1: / ### Task S.1: / ### Synthesis Task S.1: (synthesis)
    r'|'
    r'#{2,3}\s+\*{0,2}Transition\s+into\s+Exit\s+Check[^\n]*'  # ### Transition into Exit Check, bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Exit\s+Check\s+Closure[^\n]*'    # ### Exit Check Closure, bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Opening\s+Frame[^\n]*'            # ### Opening Frame (synthesis), bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Opening\s+Hook[^\n]*'            # ### Opening Hook (warmup), bold variant allowed
    r'|'
    r'#{2,4}\s+\*{0,2}Metacognitive\s+Reflection[^\n]*'  # ### / #### Metacognitive Reflection (synthesis), bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Identity[-\s]Building\s+Closure[^\n]*'  # ### Identity-Building Closure (synthesis), bold variant allowed
    r'|'
    r'\*\*Section\s+\d+\.\d+[a-z]?(?::[^\n]*)?\*\*'           # **Section X.Y: title** or **Section X.Ya** (bold, no ###)
    r')',
    re.MULTILINE,
)


def _slug_from_header(header: str) -> str:
    """Derive a deterministic snake_case slug from a section header.

    Takes the descriptive text (after ':', '—', or the full header),
    strips markdown/punctuation, drops filler words, and joins the first
    five meaningful words with underscores.
    """
    text = header
    # Take text after the first ':' or '—' separator
    for sep in (":", "—", " - "):
        if sep in text:
            text = text.split(sep, 1)[-1]
            break
    # Strip markdown markers and non-alphanumeric characters
    text = re.sub(r"[#*\[\]()\\_]", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text.lower()).strip()
    _STOP = {"a", "an", "the", "and", "or", "of", "to", "in", "for", "from"}
    words = [w for w in text.split() if w and w not in _STOP]
    return "_".join(words[:5]) or "section"


_NUMBERED_INTERACTION_RE = re.compile(
    r'Interaction\s+[\dW]\.|Task\s+S\.|W\.\d+|Problem\s+EC\.',
    re.IGNORECASE,
)


def _is_numbered_interaction(header: str) -> bool:
    """True if the header carries an explicit interaction/task number (W.N, X.Y, S.N, EC.N)."""
    return bool(_NUMBERED_INTERACTION_RE.search(header))


def _extract_major(header: str, last_major: int) -> int:
    """Derive the major group number from a header line."""
    # Interaction X.Y → X (lesson)
    m = re.search(r'Interaction\s+(\d+)\.', header)
    if m:
        return int(m.group(1))
    # Interaction W.N → N (warmup)
    m = re.search(r'Interaction\s+W\.(\d+)', header, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Interaction S.N → N (synthesis tasks)
    m = re.search(r'Interaction\s+S\.(\d+)', header, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Task S.N → N (synthesis tasks — legacy format)
    m = re.search(r'Task\s+S\.(\d+)', header, re.IGNORECASE)
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
    # **Section N.X: title** (bold, no ###) → N
    m = re.search(r'\*\*Section\s+(\d+)\.', header)
    if m:
        return int(m.group(1))
    # Bridge / exitcheck / synthesis named sections → inherit last major
    return last_major


def split_spec(input_data, **kwargs):
    """
    Split a raw markdown spec into sections.

    Args:
        input_data: Raw markdown string (lesson.md / warmup.md / etc.)

    Returns:
        List of {index, major, minor, slug, header, body} dicts.
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

        # Unnamed preamble sections (Opening Hook, Opening Frame, etc.) that
        # arrive before any numbered interaction in their major group get
        # minor=0 so they don't displace existing s{major}_1 items on rerun.
        if not _is_numbered_interaction(header) and minor_counters[major] == 0:
            minor = 0
        else:
            minor_counters[major] += 1
            minor = minor_counters[major]

        body_start = match.end()
        if i + 1 < len(matches):
            body_end = matches[i + 1].start()
        else:
            # Last section: stop at the first ## or ### header that wasn't
            # matched as an interaction (trailing metadata like Required Phrases).
            meta = _META_HEADER_RE.search(text, body_start)
            body_end = meta.start() if meta else len(text)
        body = text[body_start:body_end].strip()
        body = re.sub(r"```[^\n]*\n(.*?)\n```", r"\1", body, flags=re.DOTALL)

        slug = _slug_from_header(header)
        sections.append({
            "id": f"s{major}_{minor}_{slug}",
            "index": i,
            "major": major,
            "minor": minor,
            "slug": slug,
            "header": header,
            "body": body,
        })

    return sections
