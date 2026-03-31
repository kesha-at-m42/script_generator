#!/usr/bin/env python3
"""
sp_parse_interactions.py — Shared utility for parsing Starter Pack markdown files.

Extracts structured data from SP markdown: interactions, dialogue lines, sections,
YAML front matter, vocabulary lists, and toy specifications.

Used by sp_vocab_scan.py, sp_voice_scan.py, sp_interaction_check.py, and others.
"""

import re
import sys
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class DialogueLine:
    """A single Guide:, Prompt:, or On Correct: line from an interaction."""
    field_type: str          # "Guide", "Prompt", "On Correct", "On Selection"
    text: str                # The quoted dialogue text
    interaction_id: str      # e.g. "W.1", "1.3", "S.2"
    interaction_title: str
    phase: str               # "Warmup", "Lesson", "EC", "Synthesis", or section like "Lesson S1"
    line_number: int


@dataclass
class Interaction:
    """A parsed interaction block."""
    id: str                        # e.g. "W.1", "1.3", "S.2"
    title: str                     # e.g. "Count the Tiles"
    type_label: Optional[str]      # e.g. "[Type B]", "[WORKED EXAMPLE]"
    phase: str                     # "Warmup", "Lesson", "EC", "Synthesis"
    lesson_section: Optional[int]  # 1, 2, 3... for Lesson interactions
    pattern: str                   # "student_action", "teaching_only", "system_driven", "unknown"
    line_number: int               # line where the ### header appears
    has_purpose: bool = False
    has_visual: bool = False
    has_guide: bool = False
    has_prompt: bool = False
    has_student_action: bool = False
    has_correct_answer: bool = False
    has_on_correct: bool = False
    has_remediation: bool = False
    has_no_student_action: bool = False
    has_options: bool = False
    has_answer_rationale: bool = False
    has_connection: bool = False   # Synthesis-specific
    has_on_complete: bool = False  # System-driven
    remediation_text: str = ""     # The actual remediation line content
    visual_text: str = ""          # The full Visual: line
    is_multi_step: bool = False
    sub_parts: list = field(default_factory=list)
    raw_lines: list = field(default_factory=list)
    dialogue_lines: list = field(default_factory=list)


@dataclass
class Section:
    """A major section of the SP (§1.0, §1.1, §1.6 Warmup, etc.)."""
    id: str              # "1.0", "1.1", "1.6", etc.
    title: str
    line_number: int
    level: int           # heading level (1=H1, 2=H2, 3=H3)


@dataclass
class YAMLFrontMatter:
    """Parsed YAML front matter."""
    raw: str
    fields: dict
    line_start: int
    line_end: int
    has_module_id: bool = False
    has_unit: bool = False
    has_domain: bool = False
    has_primary_toys: bool = False
    has_secondary_toys: bool = False
    has_interaction_tools: bool = False
    primary_toys_are_objects: bool = False  # name/url objects vs flat strings
    legacy_fields: list = field(default_factory=list)


@dataclass
class VocabSection:
    """Parsed §1.3 Vocabulary Architecture."""
    terms_to_teach: list = field(default_factory=list)
    terms_to_avoid: list = field(default_factory=list)
    assessment_vocab: list = field(default_factory=list)
    staging_entries: list = field(default_factory=list)  # (phase, terms)
    line_number: int = 0


@dataclass
class ParsedSP:
    """Complete parsed Starter Pack."""
    filename: str
    lines: list
    sections: list = field(default_factory=list)
    interactions: list = field(default_factory=list)
    dialogue_lines: list = field(default_factory=list)
    yaml: Optional[YAMLFrontMatter] = None
    vocab: Optional[VocabSection] = None
    toys_in_spec: list = field(default_factory=list)      # toy names from §1.5
    toys_in_interactions: list = field(default_factory=list)  # toy names from Visual: lines
    forbidden_phrases: list = field(default_factory=list)  # from §1.7 Forbidden Phrases
    required_phrases: list = field(default_factory=list)   # from §1.7 Required Phrases


# ---------------------------------------------------------------------------
# Phase detection
# ---------------------------------------------------------------------------

def detect_phase(lines: list, line_idx: int) -> tuple:
    """
    Walk backward from line_idx to determine which phase and lesson section
    the line belongs to. Returns (phase_name, lesson_section_number_or_None).
    """
    phase = "Unknown"
    lesson_section = None

    for i in range(line_idx, -1, -1):
        line = lines[i].strip()

        # Phase-level headers — must be H1 or H2 section headers, NOT interaction
        # headers which may contain type labels like [PRACTICE] or [SYNTHESIS].
        # Allow optional bold markers (**) after ##, as M1 uses ## **1.6 WARMUP**
        if re.match(r'^#{1,2}\s+\**§?1\.6\b|^#{1,2}\s+\**WARMUP\b', line, re.IGNORECASE):
            phase = "Warmup"
            break
        if re.match(r'^#{1,2}\s+\**§?1\.7\b|^#{1,2}\s+\**LESSON\b', line, re.IGNORECASE):
            phase = "Lesson"
            break
        if re.match(r'^#{1,2}\s+\**§?1\.8\b(?!\.5)|^#{1,2}\s+\**EXIT\s*CHECK\b', line, re.IGNORECASE):
            phase = "EC"
            break
        if re.match(r'^#{1,2}\s+\**§?1\.8\.5\b|^#{1,2}\s+\**PRACTICE\s+INPUTS?\b', line, re.IGNORECASE):
            phase = "Practice"
            break
        if re.match(r'^#{1,2}\s+\**§?1\.9\b|^#{1,2}\s+\**SYNTHESIS\b', line, re.IGNORECASE):
            phase = "Synthesis"
            break

        # Lesson section headers (e.g. "## Section 2: ...")
        # Only record the FIRST (closest) section header found walking backward
        if lesson_section is None and re.match(r'^#{2,3}\s*Section\s+(\d+)', line, re.IGNORECASE):
            m = re.match(r'^#{2,3}\s*Section\s+(\d+)', line, re.IGNORECASE)
            if m:
                lesson_section = int(m.group(1))

    # If we found a lesson section but not a phase, it's in the Lesson
    if lesson_section and phase == "Unknown":
        phase = "Lesson"

    # Detect lesson section for Lesson interactions
    if phase == "Lesson" and lesson_section is None:
        for i in range(line_idx, -1, -1):
            m = re.match(r'^##\s*Section\s+(\d+)', lines[i].strip(), re.IGNORECASE)
            if m:
                lesson_section = int(m.group(1))
                break

    return phase, lesson_section


# ---------------------------------------------------------------------------
# Interaction parsing
# ---------------------------------------------------------------------------

# Pattern for interaction headers:
# ### Interaction W.1: Count the Tiles [Type B]
# ### Interaction 1.3: Now You Name It — "Rows" [Type A]
# ### Interaction Constraints (All Toys)  <-- NOT an interaction
# ## Connection Task S.1: Two Ways to See It [Type A]
# ## Metacognitive Reflection S.3: What Helped You Most? [Type B]
# ## Opening Frame [Type A]
# ## Identity-Building Closure S.4 [Type A]
INTERACTION_HEADER_RE = re.compile(
    r'^#{2,3}\s+'
    r'(?:'
    r'(?:Interaction\s+|Connection\s+Task\s+|Metacognitive\s+Reflection\s+|'
    r'EC\s+Problem\s+|'
    r'Opening\s+Frame|Identity-Building\s+Closure\s*)'
    r'(?:([A-Z]?\d*\.?\d*):?\s*)?'     # optional ID like W.1, 1.3, S.2, EC.1
    r'|'
    r'(EC\.\d+)\s*:\s*'                 # direct "EC.1:" format (M6 style)
    r')'
    r'(.*?)$',                           # title + type label
    re.IGNORECASE
)

# Bold-text interaction header variant (M1 format):
# **Interaction W.1: Comparison Set 1 — Same Shape, Different Sizes** — [Type B]
# **Opening Frame**
# **Identity-Building Closure + M2 Bridge**
BOLD_INTERACTION_RE = re.compile(
    r'^\*\*'
    r'(?:Interaction\s+|Connection\s+Task\s+|Metacognitive\s+Reflection\s+|'
    r'EC\s+Problem\s+|'
    r'Opening\s+Frame|Identity-Building\s+Closure\s*)'
    r'(?:([A-Z]?\d*\.?\d*):?\s*)?'     # optional ID like W.1, 1.3, S.2
    r'(.*?)$',                           # title + type label
    re.IGNORECASE
)

# Skip these — they look like interaction headers but aren't
SKIP_HEADERS = [
    'interaction constraints',
    'interaction block compliance',
    'interaction tools',
]


def parse_interaction_header(line: str):
    """
    Parse an interaction header line. Returns (id, title, type_label) or None.
    Supports two formats:
      H3:   ### Interaction W.1: Count the Tiles [Type B]
      Bold: **Interaction W.1: Comparison Set 1 — Same Shape** — [Type B]
    """
    stripped = line.strip()

    # Skip non-interaction headers
    lower = stripped.lower()
    for skip in SKIP_HEADERS:
        if skip in lower:
            return None

    # Try H3 header first
    m = INTERACTION_HEADER_RE.match(stripped)
    is_bold = False

    # Try bold-text header if H3 didn't match
    if not m:
        m = BOLD_INTERACTION_RE.match(stripped)
        is_bold = True

    if not m:
        return None

    if is_bold:
        # Bold regex has 2 groups: (1) = ID, (2) = rest
        raw_id = (m.group(1) or "").strip().rstrip(':')
        rest = (m.group(2) or "").strip()
    else:
        # H3 regex has 3 groups: (1) = standard ID, (2) = EC.N ID, (3) = rest
        raw_id = (m.group(1) or m.group(2) or "").strip().rstrip(':')
        rest = (m.group(3) or "").strip()

    # For bold headers, strip trailing ** and em-dash separators
    if is_bold:
        rest = rest.rstrip('*').strip()

    # Extract type label from brackets at end (or after em-dash for bold format)
    # Bold format may have: Title** — [Type B]  so check full line
    type_label = None
    search_text = rest if not is_bold else stripped
    type_match = re.findall(r'\[([^\]]+)\]', search_text)
    if type_match:
        type_label = type_match[-1]  # last bracketed item
        # Remove all bracket contents from title
        title = re.sub(r'\s*\[[^\]]*\]', '', rest).strip().rstrip('—').strip()
    else:
        title = rest.strip()

    # Clean up residual bold markers and em-dashes from title
    title = title.replace('**', '').strip().rstrip('—').strip()
    title = title.strip('*').strip()

    # Generate ID if missing (Opening Frame, etc.)
    if not raw_id:
        if 'opening frame' in lower:
            raw_id = 'OF'
        elif 'identity' in lower or 'closure' in lower:
            raw_id = 'IC'
        elif 'purpose frame' in lower:
            raw_id = 'PF'
        else:
            raw_id = 'X'

    return raw_id, title, type_label


def parse_interactions(lines: list) -> list:
    """Parse all interaction blocks from the SP lines."""
    interactions = []
    current = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Check for interaction header (H3 format)
        is_heading = stripped.startswith('#')
        # Check for bold interaction header (M1 format: **Interaction W.1: ...)
        is_bold_interaction = (stripped.startswith('**Interaction') or
                               stripped.startswith('**Connection Task') or
                               stripped.startswith('**Metacognitive') or
                               stripped.startswith('**EC Problem') or
                               stripped.startswith('**Opening Frame') or
                               stripped.startswith('**Identity-Building'))

        if is_heading or is_bold_interaction:
            parsed = parse_interaction_header(stripped)
            if parsed:
                # Save previous interaction
                if current:
                    _finalize_interaction(current)
                    interactions.append(current)

                int_id, title, type_label = parsed
                phase, lesson_section = detect_phase(lines, i)

                current = Interaction(
                    id=int_id,
                    title=title,
                    type_label=type_label,
                    phase=phase,
                    lesson_section=lesson_section,
                    pattern="unknown",
                    line_number=i + 1,  # 1-indexed
                )
                continue

            # A non-interaction heading ends the current interaction
            if current and is_heading and stripped.startswith('##'):
                heading_lower = stripped.lower()
                # Don't end on sub-part headers like "**Part 1 —"
                if not any(s in heading_lower for s in SKIP_HEADERS):
                    # Check if this is a section/phase header (not a sub-element)
                    if re.match(r'^#{1,3}\s+\**(?:Section\s+\d|§|1\.\d|BACKBONE|PHASE|Verification|Core Purpose|Lesson Structure|Lesson Req|Pedagogical)', stripped, re.IGNORECASE):
                        _finalize_interaction(current)
                        interactions.append(current)
                        current = None

        if current is None:
            continue

        current.raw_lines.append((i + 1, line))

        # Parse fields within the interaction
        if stripped.startswith('* **Purpose:**'):
            current.has_purpose = True
        elif stripped.startswith('* **Visual:'):
            current.has_visual = True
            current.visual_text = stripped
        elif stripped.startswith('* **Guide:**'):
            current.has_guide = True
            text = _extract_quoted(stripped, '* **Guide:**')
            if text:
                dl = DialogueLine("Guide", text, current.id, current.title, current.phase, i + 1)
                current.dialogue_lines.append(dl)
        elif stripped.startswith('* **Prompt:**'):
            current.has_prompt = True
            text = _extract_quoted(stripped, '* **Prompt:**')
            if text:
                dl = DialogueLine("Prompt", text, current.id, current.title, current.phase, i + 1)
                current.dialogue_lines.append(dl)
        elif stripped.startswith('* **Student Action:**'):
            current.has_student_action = True
        elif stripped.startswith('* **Correct Answer:**'):
            current.has_correct_answer = True
        elif stripped.startswith('* **On Correct:**'):
            current.has_on_correct = True
            text = _extract_quoted(stripped, '* **On Correct:**')
            if text:
                dl = DialogueLine("On Correct", text, current.id, current.title, current.phase, i + 1)
                current.dialogue_lines.append(dl)
        elif stripped.startswith('* **On Selection'):
            text = _extract_quoted_after_colon(stripped)
            if text:
                dl = DialogueLine("On Selection", text, current.id, current.title, current.phase, i + 1)
                current.dialogue_lines.append(dl)
        elif stripped.startswith('* **Remediation:**'):
            current.has_remediation = True
            current.remediation_text = stripped.replace('* **Remediation:**', '').strip()
        elif stripped.startswith('* **No student action.**'):
            current.has_no_student_action = True
        elif stripped.startswith('* **Options:**') or stripped.startswith('  * **Options:**'):
            current.has_options = True
        elif stripped.startswith('* **Answer Rationale:**'):
            current.has_answer_rationale = True
        elif stripped.startswith('* **Connection:**'):
            current.has_connection = True
        elif stripped.startswith('* **On Complete:**') or stripped.startswith('**On Complete:**'):
            current.has_on_complete = True

        # Also capture Guide lines that aren't in the standard field format
        # (e.g. multi-part interactions with "* **Guide (synced):**")
        elif '**Guide' in stripped and ':**' in stripped and not stripped.startswith('* **Guide:**'):
            text = _extract_quoted_after_colon(stripped)
            if text:
                dl = DialogueLine("Guide", text, current.id, current.title, current.phase, i + 1)
                current.dialogue_lines.append(dl)

    # Don't forget the last interaction
    if current:
        _finalize_interaction(current)
        interactions.append(current)

    return interactions


def _finalize_interaction(interaction: Interaction):
    """Determine the pattern type of the interaction."""
    # If both student-action fields and "No student action" are present,
    # prioritize student-action (the "No student action" likely leaked
    # from an adjacent section transition or teaching block)
    if interaction.has_no_student_action and not (interaction.has_student_action or interaction.has_prompt):
        interaction.pattern = "teaching_only"
    elif interaction.has_on_complete:
        interaction.pattern = "system_driven"
    elif interaction.has_student_action or interaction.has_prompt:
        interaction.pattern = "student_action"
    elif interaction.has_guide and not interaction.has_prompt:
        # Has Guide but no Prompt and no "No student action" — might be missing fields
        interaction.pattern = "teaching_only"  # assume teaching-only if no action indicated
    else:
        interaction.pattern = "unknown"


def _extract_quoted(line: str, prefix: str) -> str:
    """Extract text after a field prefix, stripping quotes."""
    text = line.replace(prefix, '', 1).strip()
    # Remove surrounding quotes
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    elif text.startswith('"'):
        text = text[1:]
    return text


def _extract_quoted_after_colon(line: str) -> str:
    """Extract quoted text after the last colon in a field line."""
    parts = line.split(':**', 1)
    if len(parts) > 1:
        text = parts[1].strip()
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        elif text.startswith('"'):
            text = text[1:]
        return text
    return ""


# ---------------------------------------------------------------------------
# YAML parsing
# ---------------------------------------------------------------------------

def parse_yaml(lines: list) -> Optional[YAMLFrontMatter]:
    """Parse YAML front matter from the SP.

    Supports three formats:
      1. Standard YAML delimiters: ---\n...\n---
      2. Code-block wrapped: ```yaml\n---\n...\n---\n```
      3. HTML comment (Notion-ready): <!-- HUB PROPERTIES\n...\n-->
    """
    yaml_start = None
    yaml_end = None
    in_yaml = False
    in_code_block = False
    is_html_comment = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # HTML comment format: <!-- HUB PROPERTIES ... -->
        if stripped.startswith('<!-- HUB PROPERTIES') or stripped.startswith('<!--HUB PROPERTIES'):
            yaml_start = i
            in_yaml = True
            is_html_comment = True
            # Check if comment closes on same line
            if '-->' in stripped[4:]:
                yaml_end = i
                break
            continue

        if is_html_comment and in_yaml:
            if '-->' in stripped:
                yaml_end = i
                break
            continue

        # YAML might be in a code block (```---...---```)
        if stripped == '```' or stripped == '```yaml':
            if not in_code_block:
                in_code_block = True
                continue
            else:
                in_code_block = False
                if in_yaml:
                    yaml_end = i
                    break
                continue

        if stripped == '---':
            if yaml_start is None:
                yaml_start = i
                in_yaml = True
            elif in_yaml:
                yaml_end = i
                break

    if yaml_start is None or yaml_end is None:
        return None

    raw = '\n'.join(lines[yaml_start:yaml_end + 1])
    fields = {}

    content_start = yaml_start + 1 if not is_html_comment else yaml_start
    for i in range(content_start, yaml_end + (1 if is_html_comment else 0)):
        line = lines[i].strip()
        # Strip HTML comment markers
        line = re.sub(r'<!--.*?HUB PROPERTIES\s*', '', line).strip()
        line = line.replace('-->', '').strip()
        if not line:
            continue
        if ':' in line and not line.startswith('-') and not line.startswith('#') and not line.startswith('*'):
            key, _, val = line.partition(':')
            fields[key.strip()] = val.strip()

    yaml = YAMLFrontMatter(
        raw=raw,
        fields=fields,
        line_start=yaml_start + 1,
        line_end=yaml_end + 1,
    )

    yaml.has_module_id = 'module_id' in fields
    yaml.has_unit = 'unit' in fields
    yaml.has_domain = 'domain' in fields
    yaml.has_interaction_tools = 'interaction_tools' in fields

    # Check for primary_toys
    for i in range(yaml_start + 1, yaml_end):
        if 'primary_toys' in lines[i]:
            yaml.has_primary_toys = True
            # Check if next lines have name/notion_url (object format)
            for j in range(i + 1, min(i + 10, yaml_end)):
                if 'name:' in lines[j] or 'notion_url:' in lines[j]:
                    yaml.primary_toys_are_objects = True
                    break
            break

    for i in range(yaml_start + 1, yaml_end):
        if 'secondary_toys' in lines[i]:
            yaml.has_secondary_toys = True
            break

    # Check for legacy fields
    legacy = ['path', 'fractions_required', 'shapes']
    for key in legacy:
        if key in fields:
            yaml.legacy_fields.append(key)

    return yaml


# ---------------------------------------------------------------------------
# Section parsing
# ---------------------------------------------------------------------------

def parse_sections(lines: list) -> list:
    """Parse all heading-level sections."""
    sections = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^(#{1,4})\s+(.+)$', stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            # Extract section ID if present (e.g. "1.0", "1.1.1")
            id_match = re.search(r'(\d+\.\d+(?:\.\d+)?)', title)
            sec_id = id_match.group(1) if id_match else ""
            sections.append(Section(
                id=sec_id,
                title=title,
                line_number=i + 1,
                level=level,
            ))
    return sections


# ---------------------------------------------------------------------------
# Vocabulary parsing (§1.3)
# ---------------------------------------------------------------------------

def parse_vocabulary(lines: list) -> Optional[VocabSection]:
    """Parse §1.3 Vocabulary Architecture."""
    vocab = VocabSection()

    # Find §1.3
    sec_start = None
    sec_end = None
    for i, line in enumerate(lines):
        if re.match(r'^##\s+.*1\.3\b', line.strip()):
            sec_start = i
            vocab.line_number = i + 1
        elif sec_start is not None and re.match(r'^##\s+.*1\.[4-9]\b', line.strip()):
            sec_end = i
            break

    if sec_start is None:
        return None
    if sec_end is None:
        sec_end = len(lines)

    in_terms_to_avoid = False
    in_assessment = False

    for i in range(sec_start, sec_end):
        line = lines[i].strip()
        lower = line.lower()

        if 'terms to avoid' in lower:
            in_terms_to_avoid = True
            in_assessment = False
            continue
        if 'assessment vocabulary' in lower:
            in_assessment = True
            in_terms_to_avoid = False
            continue
        if line.startswith('##') or line.startswith('### '):
            if 'terms to avoid' not in lower and 'assessment' not in lower:
                in_terms_to_avoid = False
                in_assessment = False

        # Collect terms from bullet lists
        if in_terms_to_avoid and (line.startswith('*') or line.startswith('-')):
            term = re.sub(r'^[\*\-]\s*', '', line)
            term = re.sub(r'\(.*?\)', '', term).strip().strip('*').strip()
            if term and len(term) > 1:
                vocab.terms_to_avoid.append(term)

        if in_assessment and (line.startswith('*') or line.startswith('-')):
            term = re.sub(r'^[\*\-]\s*', '', line)
            term = re.sub(r'\(.*?\)', '', term).strip().strip('*').strip()
            if term and len(term) > 1:
                vocab.assessment_vocab.append(term)

    return vocab


# ---------------------------------------------------------------------------
# Forbidden/Required Phrases parsing (§1.7)
# ---------------------------------------------------------------------------

def parse_phrase_lists(lines: list) -> tuple:
    """Parse Required Phrases and Forbidden Phrases from the Lesson section."""
    forbidden = []
    required = []

    in_forbidden = False
    in_required = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        lower = stripped.lower()

        if 'forbidden phrases' in lower and stripped.startswith('#'):
            in_forbidden = True
            in_required = False
            continue
        if 'required phrases' in lower and stripped.startswith('#'):
            in_required = True
            in_forbidden = False
            continue
        if stripped.startswith('#') and ('forbidden' not in lower and 'required' not in lower):
            in_forbidden = False
            in_required = False

        if in_forbidden and (stripped.startswith('*') or stripped.startswith('-') or stripped.startswith('❌')):
            phrase = re.sub(r'^[\*\-❌]\s*', '', stripped)
            phrase = re.sub(r'\(.*?\)', '', phrase).strip().strip('*').strip()
            if phrase and len(phrase) > 2:
                forbidden.append(phrase)

        if in_required and (stripped.startswith('*') or stripped.startswith('-')):
            phrase = re.sub(r'^[\*\-]\s*', '', stripped)
            phrase = re.sub(r'\(.*?\)', '', phrase).strip().strip('*').strip()
            if phrase and len(phrase) > 2:
                required.append(phrase)

    return forbidden, required


# ---------------------------------------------------------------------------
# Toy parsing
# ---------------------------------------------------------------------------

def parse_toys_from_spec(lines: list) -> list:
    """Extract toy names from §1.5 Toy Specifications headers.

    Supports multiple formats:
      Format A (M3/M4): ### **1.5.1 Grid Rectangles**  or  ### 1.5.1 Grid Rectangles
      Format B (M5):    ### Primary Toy: Grid Rectangles (Module-Specific Configuration)
                        ### Secondary Tool: Equation Builder

    Stops at §1.6, Interaction Constraints, or phase headers.
    """
    toys = []
    in_15 = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Enter §1.5
        if re.match(r'^##\s+.*1\.5\b', stripped):
            in_15 = True
            continue
        if not in_15:
            continue
        # Exit conditions
        if re.match(r'^##\s+.*1\.[6-9]\b', stripped):
            break
        if re.match(r'^#\s+.*(?:PHASE|WARMUP|LESSON)', stripped, re.IGNORECASE):
            break
        # Interaction Constraints marks end of toy specs
        if 'interaction constraint' in stripped.lower():
            break
        # Look for toy subsection headers: ### 1.5.1 Toy Name or ### Toy Name
        if re.match(r'^###\s+', stripped):
            title = re.sub(r'^###\s+', '', stripped).strip()
            # Strip bold markers
            title = title.strip('*').strip()
            # Skip obviously non-toy headers
            skip_patterns = [
                'interaction', 'verification', 'parameters', 'constraints',
                'purpose', 'required', 'forbidden', 'misconception',
                'incomplete', 'success criteria', 'warmup', 'lesson',
                'section', 'kdd', 'ec problem', 'connection task',
                'metacognitive', 'opening frame', 'identity', 'closure',
                'data constraint', 'progression of', 'example data',
                'data pairings',
                # Toy spec subsection headers (not toy names)
                'overview', 'notion link', 'changes from', 'configuration',
                'guardrail', 'progression', 'data set', 'in development',
            ]
            if any(p in title.lower() for p in skip_patterns):
                continue
            # Clean up numbered prefix like "1.5.1 "
            title = re.sub(r'^\d+\.\d+\.\d+\s+', '', title).strip()
            # Handle "Primary Toy: Name (description)" / "Secondary Tool: Name"
            primary_m = re.match(r'^(?:Primary\s+Toy|Secondary\s+(?:Toy|Tool))\s*:\s*(.+)', title, re.IGNORECASE)
            if primary_m:
                title = primary_m.group(1).strip()
                # Remove parenthetical descriptions
                title = re.sub(r'\s*\(.*\)', '', title).strip()
            if title:
                toys.append(title)
    return toys


def parse_toys_from_visuals(interactions: list) -> list:
    """Extract toy names from Visual: lines across all interactions."""
    toys = set()
    for interaction in interactions:
        if interaction.visual_text:
            # Pattern: **Visual: Toy Name (Mode).**
            m = re.search(r'\*\*Visual:\s*([^(.*]+?)(?:\s*\(|\.?\*\*)', interaction.visual_text)
            if m:
                toy = m.group(1).strip()
                toys.add(toy)
    return sorted(toys)


# ---------------------------------------------------------------------------
# Main parse function
# ---------------------------------------------------------------------------

def parse_sp(filepath: str) -> ParsedSP:
    """Parse a Starter Pack markdown file into structured data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    sp = ParsedSP(filename=filepath, lines=lines)
    sp.yaml = parse_yaml(lines)
    sp.sections = parse_sections(lines)
    sp.interactions = parse_interactions(lines)
    sp.vocab = parse_vocabulary(lines)
    sp.toys_in_spec = parse_toys_from_spec(lines)
    sp.toys_in_interactions = parse_toys_from_visuals(sp.interactions)

    forbidden, required = parse_phrase_lists(lines)
    sp.forbidden_phrases = forbidden
    sp.required_phrases = required

    # Collect all dialogue lines
    for interaction in sp.interactions:
        sp.dialogue_lines.extend(interaction.dialogue_lines)

    return sp


# ---------------------------------------------------------------------------
# Gate-aware filtering
# ---------------------------------------------------------------------------

PHASE_GATE_MAP = {
    1: [],  # No interactions at Gate 1
    2: ["Warmup", "Lesson"],
    3: ["Warmup", "Lesson", "EC", "Practice", "Synthesis"],
    4: ["Warmup", "Lesson", "EC", "Practice", "Synthesis"],
}


def filter_by_gate(sp: ParsedSP, gate: int) -> ParsedSP:
    """
    Return a filtered view of the SP appropriate for the given gate.
    Does NOT modify the original — returns a new ParsedSP with filtered interactions/dialogue.
    """
    allowed_phases = PHASE_GATE_MAP.get(gate, [])

    filtered = ParsedSP(
        filename=sp.filename,
        lines=sp.lines,
        sections=sp.sections,
        yaml=sp.yaml,
        vocab=sp.vocab,
        toys_in_spec=sp.toys_in_spec,
        forbidden_phrases=sp.forbidden_phrases,
        required_phrases=sp.required_phrases,
    )

    filtered.interactions = [i for i in sp.interactions if i.phase in allowed_phases]
    filtered.dialogue_lines = [d for d in sp.dialogue_lines if d.phase in allowed_phases]
    filtered.toys_in_interactions = parse_toys_from_visuals(filtered.interactions)

    return filtered


# ---------------------------------------------------------------------------
# CLI: quick diagnostic
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: sp_parse_interactions.py <sp_file.md> [--gate N]")
        sys.exit(1)

    filepath = sys.argv[1]
    gate = None
    if '--gate' in sys.argv:
        idx = sys.argv.index('--gate')
        gate = int(sys.argv[idx + 1])

    sp = parse_sp(filepath)
    if gate:
        sp = filter_by_gate(sp, gate)

    print(f"File: {sp.filename}")
    print(f"Total lines: {len(sp.lines)}")
    print(f"Sections found: {len(sp.sections)}")
    print(f"Interactions found: {len(sp.interactions)}")
    print(f"Dialogue lines found: {len(sp.dialogue_lines)}")
    if sp.yaml:
        print(f"YAML: module_id={sp.yaml.fields.get('module_id', 'MISSING')}")
    if sp.vocab:
        print(f"Terms to Avoid: {len(sp.vocab.terms_to_avoid)}")
    print(f"Toys in §1.5: {sp.toys_in_spec}")
    print(f"Toys in interactions: {sp.toys_in_interactions}")

    print("\n--- Interactions ---")
    for ix in sp.interactions:
        print(f"  {ix.phase:10s} | {ix.id:6s} | {ix.pattern:15s} | {ix.title[:50]}")

    print(f"\n--- Dialogue Lines ({len(sp.dialogue_lines)}) ---")
    for dl in sp.dialogue_lines[:10]:
        print(f"  {dl.phase:10s} | {dl.interaction_id:6s} | {dl.field_type:12s} | {dl.text[:60]}...")
    if len(sp.dialogue_lines) > 10:
        print(f"  ... and {len(sp.dialogue_lines) - 10} more")
