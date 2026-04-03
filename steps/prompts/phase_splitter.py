"""
phase_splitter - AI Prompt

Reads a raw lesson starter pack (Notion page content in markdown/HTML) and
extracts the four phase sections — Warmup, Lesson, Exit Check, Synthesis —
into clean markdown, outputting a JSON object keyed by phase name.

This is the first step in the starter_pack_splitter pipeline. Its output
feeds phase_writer, which writes each section to its respective .md file
in the module directory.

Input (user message):
    <input>   - full _starter_pack_ref.md content (raw Notion page markdown)
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

PHASE_SPLITTER_PROMPT = Prompt(
    role="""You are a curriculum document parser. Your job is to extract specific phase sections from a lesson starter pack and output them as clean markdown.""",
    instructions="""
## TASK

<input> is the raw content of a Notion starter pack page for a single lesson module.
It contains multiple sections including a BACKBONE (curriculum theory) and four instructional phases.

Extract exactly these four phases and output them as a JSON object:

```json
{
  "warmup": "...full warmup section as clean markdown...",
  "lesson": "...full lesson section as clean markdown...",
  "exitcheck": "...full exit check section as clean markdown...",
  "synthesis": "...full synthesis section as clean markdown..."
}
```

---

## SECTION IDENTIFICATION

Find each phase by its section header. Common header patterns:

| Phase | Header patterns |
|---|---|
| Warmup | `## 1.6 WARMUP`, `## WARMUP`, `## 1.6` |
| Lesson | `## 1.7 LESSON`, `## LESSON`, `## 1.7` |
| Exit Check | `## 1.8 EXIT CHECK`, `## EXIT CHECK`, `## 1.8` |
| Synthesis | `## 1.9 SYNTHESIS`, `## SYNTHESIS`, `## 1.9` |

Each phase runs from its header up to (but not including) the next phase header or the end of the PHASE SPECIFICATIONS section.

Include everything within the phase: purpose, parameters, constraints, interactions, design notes, voice notes, verification checklists. Do not truncate.

---

## HTML TO MARKDOWN CONVERSION

The raw content contains HTML table markup. Convert all tables to markdown format.

**HTML input:**
```html
<table header-row="true">
<tr>
<td>Element</td>
<td>Specification</td>
</tr>
<tr>
<td>**Time**</td>
<td>3-4 minutes</td>
</tr>
</table>
```

**Markdown output:**
```markdown
| Element | Specification |
|---|---|
| **Time** | 3-4 minutes |
```

Rules:
- The first `<tr>` in a `<table header-row="true">` becomes the header row, followed by a separator row `|---|---|...`
- For tables WITHOUT `header-row="true"`, there is no header row — start directly with data rows
- `<colgroup>` and `<col>` tags: discard entirely
- `<br>` or `<br/>`: replace with a space (do not break table cells)
- `<td>` content: preserve all markdown formatting inside (bold, italic, inline code, links)
- Nested HTML inside `<td>`: flatten to inline text, preserve markdown
- Empty `<td>`: render as empty cell ` `

---

## FORMATTING RULES

- Preserve all section headers (`##`, `###`) exactly as they appear
- Preserve all bullet point lists, numbered lists, and bold/italic formatting
- Preserve blockquotes (`>`) for design notes and voice notes
- Preserve inline code (backticks)
- Remove any Notion-specific XML tags: `<page>`, `<properties>`, `<ancestor-path>`, `<content>`, `<mention-user>`, etc.
- Do not add or remove any interaction content
- Do not paraphrase or summarize — extract verbatim

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Entire response must be a single object starting with `{` and ending with `}`
- String values: use escaped newlines (`\\n`) for line breaks within JSON strings
- Use double quotes throughout
- Each phase value is a single string containing the full markdown text of that phase

""",
    doc_refs=[],
    output_structure="""
{
  "warmup": "## 1.6 WARMUP (3-4 minutes)\\n\\n**Detail Level:** Structure + parameters...\\n\\n### Purpose\\n...",
  "lesson": "## 1.7 LESSON (~12 minutes)\\n\\n**Detail Level:** Structure + parameters...\\n\\n### Core Purpose\\n...",
  "exitcheck": "## 1.8 EXIT CHECK\\n\\n**Detail Level:** Structure + full scripts...\\n\\n### Purpose\\n...",
  "synthesis": "## 1.9 SYNTHESIS\\n\\n**Detail Level:** Structure + parameters...\\n\\n### Purpose\\n..."
}
""",
    prefill="{",
    examples=[],
    module_ref={},
    template_ref={},
    cache_docs=False,
    temperature=0,
    max_tokens=32000,
    stop_sequences=[],
)
