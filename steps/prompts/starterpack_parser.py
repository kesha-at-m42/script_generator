"""
starterpack_parser - AI Prompt

Converts a freeform markdown lesson/warmup/synthesis spec into a flat array
of structured section objects. Each section captures the spec's content as
key-value fields.

This is Step 1 in the pipeline. Its output feeds toy_spec_loader, which
scans the visual fields to load only the relevant toy specs, then
section_structurer converts the enriched spec into full section JSON.

Input (user message):
    <input>   - full markdown spec content (lesson.md, warmup.md, etc.)
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

STARTERPACK_PARSER_PROMPT = Prompt(
    role="""You are converting a freeform lesson spec into a structured JSON format. Your job is precise extraction: pull every field from the spec as written, faithfully and completely.""",
    instructions="""
## TASK

Parse the markdown spec in <input> into a flat array of section objects.

One section object per spec section header. Sub-sections (e.g. W.3a, W.3b,
W.3c) become separate section objects — do not nest them.

**Section boundaries come only from spec headers** (e.g. `### Interaction 1.3`,
`## Section W.1`). Never split a section because of text inside a field value,
including `[Immediately followed by:]` annotations. That content stays in the
same section object, captured verbatim in its field.

---

## PARSING RULES

### Field extraction

Every line in the spec following the pattern `**Label:** content` becomes a
field. The label (before the colon) is the field key, converted to snake_case.
The content (after the colon) is the field value as a string.

Common field mappings:
| Spec label | JSON key |
|---|---|
| Visual | `visual` |
| Guide | `guide` |
| Prompt | `prompt` |
| Task | `task` |
| Correct Answer | `correct_answer` |
| On Correct | `on_correct` |
| On Incorrect | `on_incorrect` |
| Purpose | `purpose` |
| Hook | `hook` |
| Engagement Anchor | `engagement_anchor` |
| Design Note | `design_note` |
| Scaffolding Note | `scaffolding_note` |
| Student Action | `student_action` |

If a label appears that is not in this table, still include it — use its
snake_case form as the key. Do not drop any field from the spec.

If the same label appears more than once in a section, suffix each occurrence with `_1`, `_2`, `_3`, etc. (e.g. three `**Student Action:**` fields become `student_action_1`, `student_action_2`, `student_action_3`). Apply this to all repeated labels including `visual`, `guide`, `prompt`, `correct_answer`, `on_correct`, etc. Never silently overwrite a field — every occurrence must be preserved.

### Prose between fields

Spec sections sometimes contain plain sentences or bold step markers between key-value pairs (e.g. `**Step 1 — Specification:**` with no content after the colon, or a sentence like "Sequential enforcement same as 3.2/3.3."). These are not fields and not section boundaries. Capture them as `"divider": "..."` — one divider entry per run of such text. Do not let them interrupt field parsing or bleed into adjacent field values.

Any `**Label:** content` lines that follow a divider are still parsed as normal fields — the divider does not consume them. If a step marker like `**Step 1 — Specification:**` is immediately followed by bullet-point fields (`- **Student Action:** ...`, `- **Correct State:** ...`), those bullets are fields, not divider content. Only lines with no `**Label:** content` structure belong in the divider.

### Section IDs

All sections use `s<major>_<minor>_<slug>` — no phase prefix, no letter suffixes.
- Major = top-level spec group number (W.1 → major 1, W.3 → major 3, Section 2 → major 2)
- Minor = sequential interaction counter within that group, starting at 1, **never reused**
- Slug = snake_case purpose phrase

When the spec has sub-sections (e.g. W.3a, W.3b, W.3c), each becomes its own section with a unique minor number — do not append letters.

Examples:
- `Section W.1: Data Collection Game` → `s1_1_data_collection`
- `Section W.2: Symbol Introduction` → `s2_1_symbol_introduction`
- `W.3a: Guide Models First Category` → `s3_1_model_first_category`
- `W.3b: Student Completes Second Category` → `s3_2_student_places_category_b`
- `W.3c: Student Completes Third Category` → `s3_3_student_places_category_c`
- `Section W.4: Bridge to Lesson` → `s4_1_bridge_to_lesson`
- `Section 1.2: Least Votes` → `s1_2_least_votes`

### Tables

If the spec contains a table (e.g. Game Specifications), capture it as a
nested object under the key derived from the table's heading label.

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Entire response must be an array starting with `[` and ending with `]`
- One object per section, in spec order
- Flat — no nested sections arrays
- Use double quotes throughout
- Omit fields that are empty or not present in the spec for that section
- **Escape all double quotes inside string values** — if a field value contains a `"` character (e.g. `"3 columns of 4"`), it must be written as `\"3 columns of 4\"` in the JSON string

""",
    doc_refs=[ ],
    output_structure="""
[
  {
    "id": "s1_1_data_collection",
    "purpose": "Generate personalized data via counting game. Create investment through active participation and Minis context.",
    "hook": "Minis characters appear in animated counting scenario.",
    "game_specifications": {
      "style": "Mario Party-style counting game",
      "categories": 3,
      "values_range": "3-7 per category",
      "duration": "~60 seconds",
      "student_interaction": "Up/down counter to track count"
    },
    "task": "Student participates in counting activity, using up/down counter to record their count for each category.",
    "on_correct": "Let's see if you counted them all. Guide counts visually, revealing correct answer. There were [X] [category A] and [Y] [category B] and [Z] [category C].",
    "design_note": "Student counter attempt is checked by Guide reveal. Ensures all students have correct data regardless of counting accuracy."
  },
  {
    "id": "s2_1_symbol_introduction",
    "purpose": "Give student agency in graph creation. Builds investment in their graph.",
    "visual": "Picture Graphs (Mode 2: Creating). Symbol palette appears (6-8 options). Empty horizontal graph template visible below with 3 category rows. Data from W.1 displayed as reference text.",
    "engagement_anchor": "Choice/Agency (student selects their symbol)",
    "guide": "Let's make a graph with the data."
  },
  {
    "id": "s3_1_model_first_category",
    "purpose": "Guide models placing symbols for category A.",
    "visual": "Picture Graphs (Mode 2: Creating). Empty horizontal picture graph. Selected symbol ready. Key reads Each [symbol] = 1 [item]. W.1 data visible as reference. Data Table not visible.",
    "guide": "Watch how I show our [category A] on the graph. You counted [X] [category A]. So I add [X] [symbols]. One... two... three... [X] [symbols]. Each one means 1 [category A].",
    "scaffolding_note": "System places symbols while guide narrates. No student interaction."
  },
  {
    "id": "s3_2_student_places_category_b",
    "purpose": "Student places symbols for category B.",
    "visual": "Picture Graphs (Mode 2: Creating). Horizontal picture graph. Category A complete (Guide-modeled). Categories B and C empty. Key visible. Data Table not visible.",
    "guide": "Your turn. You counted [Y] [category B]. Add [Y] [symbols]. Click to place them - one for each [category B] you counted.",
    "correct_answer": "[Y] symbols placed",
    "on_correct": "[Y] [symbols]. One for each [category B].",
    "on_incorrect": "Let's count the symbols. We need [Y] — one for each [category B] we counted. Allows retry."
  }
]
""",
    prefill="[",
    examples=[],
    module_ref={},
    template_ref={},
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=16000,
    stop_sequences=[],
)
