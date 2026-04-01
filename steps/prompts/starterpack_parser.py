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

One section object per interaction. Sub-sections (e.g. W.3a, W.3b, W.3c)
become separate section objects — do not nest them.

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

If a label appears that is not in this table, still include it — use its
snake_case form as the key. Do not drop any field from the spec.

### Section IDs

Derive `id` from the section header. Convert to snake_case, remove punctuation.

Examples:
- `Section W.1: Data Collection Game` → `w1_data_collection`
- `W.3a: Guide Models First Category` → `w3a_model_first_category`
- `Section 1.2: Least Votes` → `s1_2_least_votes`
- `Bridge to Lesson` → `bridge_to_lesson`

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

""",
    doc_refs=[
        "glossary.md",
    ],
    output_structure="""
[
  {
    "id": "w1_data_collection",
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
    "id": "w2_symbol_selection",
    "purpose": "Give student agency in graph creation. Builds investment in their graph.",
    "visual": "Picture Graphs (Mode 2: Creating). Symbol palette appears (6-8 options). Empty horizontal graph template visible below with 3 category rows. Data from W.1 displayed as reference text.",
    "engagement_anchor": "Choice/Agency (student selects their symbol)",
    "guide": "Let's make a graph with the data."
  },
  {
    "id": "w3a_model_first_category",
    "purpose": "Guide models placing symbols for category A.",
    "visual": "Picture Graphs (Mode 2: Creating). Empty horizontal picture graph. Selected symbol ready. Key reads Each [symbol] = 1 [item]. W.1 data visible as reference. Data Table not visible.",
    "guide": "Watch how I show our [category A] on the graph. You counted [X] [category A]. So I add [X] [symbols]. One... two... three... [X] [symbols]. Each one means 1 [category A].",
    "scaffolding_note": "System places symbols while guide narrates. No student interaction."
  },
  {
    "id": "w3b_student_places_category_b",
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
