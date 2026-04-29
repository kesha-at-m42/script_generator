# ── V3 / Phase 8 skeleton ────────────────────────────────────────────────────
# Derived from: spec_splitter.py
# For use with: *_generator_v3 pipelines (unit100+ Phase 8 skeleton format)
# ─────────────────────────────────────────────────────────────────────────────
"""
spec_splitter_v3 - Formatting Step

Deterministically splits a raw markdown spec (lesson/warmup/synthesis/exitcheck)
into one item per interaction or transition section.

Detected header patterns:
  ### Interaction X.Y: <title>           (lesson specs; ### optional — bold-only accepted)
  ### Interaction W.N: <title>           (warmup specs; ### optional — bold-only accepted)
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
    r'(?:#{2,3}\s+)?\*{0,2}Interaction\s+\d+\.\d+[^\n]*'    # ### Interaction X.Y: ... (lesson), bold+headingless variant allowed
    r'|'
    r'(?:#{2,3}\s+)?\*{0,2}Interaction\s+W\.\d+[^\n]*'  # ### Interaction W.N: ... (warmup), bold+headingless variant allowed
    r'|'
    r'(?:#{2,3}\s+)?\*{0,2}Interaction\s+L\.\d+[^\n]*'  # ### Interaction L.N: ... (Phase 8 lesson beats)
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
    r'#{2,3}\s+EC\.\d+:[^\n]*'                          # ### EC.1: ... (Phase 8 exit check beats, no "Problem" prefix)
    r'|'
    r'#{2,3}\s+\*{0,2}Interaction\s+S\.\d+[^\n]*'      # ### Interaction S.N: ... (synthesis), bold variant allowed
    r'|'
    r'(?:#{2,3}\s+)?\*{0,2}(?:(?:Connection|Synthesis)\s+)?Task\s+S\.\d+:[^\n]*'  # ### Connection Task S.1: / Task S.1: / Synthesis Task S.1:
    r'|'
    r'#{2,3}\s+\*{0,2}Transition\s+into\s+Exit\s+Check[^\n]*'  # ### Transition into Exit Check, bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Transition\s+Frame[^\n]*'         # ### Transition Frame (Phase 8 exit check opener)
    r'|'
    r'#{2,3}\s+\*{0,2}Exit\s+Check\s+Closure[^\n]*'    # ### Exit Check Closure, bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Opening\s+Frame[^\n]*'            # ### Opening Frame (synthesis), bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Opening\s+Hook[^\n]*'            # ### Opening Hook (warmup), bold variant allowed
    r'|'
    r'#{2,3}\s+\*{0,2}Purpose\s+Frame[^\n]*'            # ### Purpose Frame (Phase 8 lesson opener)
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
    r'Interaction\s+[\dWLS]\.|Task\s+S\.|W\.\d+|Problem\s+EC\.|\bEC\.\d+',
    re.IGNORECASE,
)


def _is_numbered_interaction(header: str) -> bool:
    """True if the header carries an explicit interaction/task number (W.N, X.Y, S.N, EC.N)."""
    return bool(_NUMBERED_INTERACTION_RE.search(header))


def _extract_major(header: str, last_major: int) -> int:
    """Derive the major group number from a header line."""
    # Interaction X.Y → X (lesson, digit-prefixed)
    m = re.search(r'Interaction\s+(\d+)\.', header)
    if m:
        return int(m.group(1))
    # Interaction L.N → N (Phase 8 lesson beats)
    m = re.search(r'Interaction\s+L\.(\d+)', header, re.IGNORECASE)
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
    # EC.N (bare, no "Problem" prefix) → N (Phase 8 exit check)
    m = re.search(r'\bEC\.(\d+)', header, re.IGNORECASE)
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


import json as _json  # noqa: E402  (placed here to keep top-of-file imports clean)

_AI_SPLIT_SPEC_PROMPT = """\
You are splitting a Phase 8 lesson spec markdown document into individual interaction sections.

Each section starts with a heading like:
  ### Interaction L.1: Title
  ### Interaction L.2: Title
  ### EC.1: Title
  ### Purpose Frame
  ### Transition Frame
  ### Opening Frame
  ### Opening Hook
  ### Connection Task S.1: Title
  ### Identity-Building Closure
  etc.

Return ONLY a JSON array. Each element must be an object with:
  "index": integer (0-based position)
  "major": integer (for L.N use N; for EC.N use N; for unnamed openers/closers inherit last)
  "minor": integer (sequential counter within the major group, starting at 1; use 0 for preamble/unnamed)
  "header": the exact header line from the document
  "body": all text belonging to that section — exclude the header line itself

Exclude preamble content before the first section, and trailing metadata sections
(Required Phrases, Forbidden Phrases, Verification Checklists, Success Criteria, KDDs, etc.).

Return only the raw JSON array — no explanation, no markdown fences.
"""


def _ai_split_spec(text: str) -> list:
    """Use Claude to split a spec when the regex finds no sections or misses some."""
    try:
        from core.claude_client import ClaudeClient

        client = ClaudeClient()
        response = client.generate(
            system=_AI_SPLIT_SPEC_PROMPT,
            user_message=text,
            max_tokens=16000,
        )

        raw = response.strip()
        if raw.startswith("```"):
            raw = re.sub(r"^```[a-z]*\n?", "", raw).rstrip("`").strip()
        items = _json.loads(raw)
        if not isinstance(items, list):
            return []

        seen_ids: dict = {}
        for i, item in enumerate(items):
            item.setdefault("index", i)
            item.setdefault("major", 1)
            item.setdefault("minor", i + 1)
            header = item.get("header", "")
            slug = _slug_from_header(header)
            item["slug"] = slug
            base_id = f"s{item['major']}_{item['minor']}_{slug}"
            seen_ids[base_id] = seen_ids.get(base_id, 0) + 1
            item["id"] = base_id if seen_ids[base_id] == 1 else f"{base_id}_{seen_ids[base_id]}"

        print(f"  [SPEC_SPLITTER_V3] AI fallback found {len(items)} sections")
        return items

    except Exception as e:
        print(f"  [SPEC_SPLITTER_V3] AI fallback failed: {e}")
        return []


_BROAD_RE = re.compile(
    r'^#{2,4}\s+\**\s*(?:Interaction\s+[\w.]+|Transition\s+(?:into|Frame)|'
    r'Opening\s+(?:Hook|Frame)|Purpose\s+Frame|'
    r'Exit\s+Check\s+Closure|Metacognitive\s+Reflection|Identity.Building\s+Closure|'
    r'Bridge\s+to\s+\w|EC\.\d+:|(?:Connection\s+)?Task\s+S\.\d+:)',
    re.MULTILINE | re.IGNORECASE,
)


def _build_sections(matches, text):
    minor_counters: dict = defaultdict(int)
    seen_ids: dict = defaultdict(int)
    last_major = 1
    sections = []

    for i, match in enumerate(matches):
        header = match.group(0).strip()
        major = _extract_major(header, last_major)
        last_major = major

        if not _is_numbered_interaction(header) and minor_counters[major] == 0:
            minor = 0
        else:
            minor_counters[major] += 1
            minor = minor_counters[major]

        body_start = match.end()
        if i + 1 < len(matches):
            body_end = matches[i + 1].start()
        else:
            meta = _META_HEADER_RE.search(text, body_start)
            body_end = meta.start() if meta else len(text)
        body = text[body_start:body_end].strip()
        body = re.sub(r"```[^\n]*\n(.*?)\n```", r"\1", body, flags=re.DOTALL)

        slug = _slug_from_header(header)
        base_id = f"s{major}_{minor}_{slug}"
        seen_ids[base_id] += 1
        section_id = base_id if seen_ids[base_id] == 1 else f"{base_id}_{seen_ids[base_id]}"
        sections.append({
            "id": section_id,
            "index": i,
            "major": major,
            "minor": minor,
            "slug": slug,
            "header": header,
            "body": body,
        })

    return sections


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
        print("  [SPEC_SPLITTER_V3] WARNING: No sections found — trying AI fallback")
        return _ai_split_spec(text)

    sections = _build_sections(matches, text)

    broad_count = len(_BROAD_RE.findall(text))
    if broad_count > len(sections):
        print(
            f"  [SPEC_SPLITTER_V3] Regex found {len(sections)} sections but broad scan sees "
            f"{broad_count} — trying AI fallback"
        )
        ai_sections = _ai_split_spec(text)
        if len(ai_sections) >= len(sections):
            return ai_sections

    return sections
