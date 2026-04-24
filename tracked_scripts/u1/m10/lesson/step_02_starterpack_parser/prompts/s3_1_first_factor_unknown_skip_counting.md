# Prompt: starterpack_parser
# Generated: 2026-04-20T12:01:03.245718
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 4000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are extracting structured fields from a single pre-split lesson spec section into a JSON object. Your job is precise extraction: pull every field from the body as written, faithfully and completely.

----------------------------------------------------------------------

### Block 2: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

<input> is a single spec section with these fields:
- `index`: position in the spec (ignore)
- `major`: major group number (e.g. 1, 2, 3) — use this exactly in the ID
- `minor`: sequential position within the major group — use this exactly in the ID
- `header`: the raw section header line (e.g. `### Interaction 1.1: Transition from Warmup`)
- `body`: the section's content

Your job:
1. Extract every field from `body` using the field rules below
2. Return a single JSON object

The section ID is pre-computed and already written at the start of your response — do not change it.

---

## PARSING RULES

### Field extraction

Every line in the body following the pattern `**Label:** content` becomes a field.
The label (before the colon) is the field key, converted to snake_case.
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

If a label appears that is not in this table, still include it — use its snake_case form as the key. Do not drop any field from the body.

If the same label appears more than once, suffix each occurrence with `_1`, `_2`, `_3`, etc. (e.g. three `**Guide:**` fields become `guide_1`, `guide_2`, `guide_3`). Apply this to all repeated labels. Never silently overwrite a field — every occurrence must be preserved.

If a label contains any qualifier in parentheses `()` or brackets `[]` — e.g. `**On Correct (example: 4 × 5 = 20):**`, `**Visual [selected_rows]:**`, `**Student Action [selected_columns]:**` — strip the qualifier from the label and prepend it to the extracted value. Use the bare base label for key generation and apply `_1`/`_2` suffixing as normal. The qualifier stays in the value as-is (preserving its `()` or `[]` delimiters).

Examples:
- `**On Correct (example: 4 × 5 = 20):** "4 times 5 equals 20..."` → key `on_correct_2`, value `"(example: 4 × 5 = 20) "4 times 5 equals 20..."`
- `**Visual [selected_rows]:** Rows buttons activate.` → key `visual_2`, value `"[selected_rows] Rows buttons activate."`
- `**Visual [selected_columns]:** Columns buttons activate.` → key `visual_3`, value `"[selected_columns] Columns buttons activate."`

### Prose between fields

Body sections sometimes contain plain sentences or bold step markers between key-value pairs (e.g. `**Step 1 — Specification:**` with no content after the colon, or a sentence like "Sequential enforcement same as 3.2/3.3."). These are not fields and not section boundaries. Capture them as `"divider": "..."` — one divider entry per run of such text. Do not let them interrupt field parsing or bleed into adjacent field values.

Any `**Label:** content` lines that follow a divider are still parsed as normal fields — the divider does not consume them. Only lines with no `**Label:** content` structure belong in the divider.

### Tables

If the body contains a table (e.g. Game Specifications), capture it as a nested object under the key derived from the table's heading label.

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Return a single object starting with `{` and ending with `}`
- Use double quotes throughout
- Omit fields that are empty or not present in the body
- **Escape all double quotes inside string values** — if a field value contains a `"` character, it must be written as `"` in the JSON string

---

## EXAMPLE OUTPUT (section 1.1)

The `id` field is pre-filled for you. Continue from it:

```json
{"id": "s1_1_transition_from_warmup",
  "visual": "Arrays with Pictures (concrete mode): Sticker sheet showing 3 rows of 4 stickers in a clear rectangular arrangement.",
  "guide": "In the Warmup, you saw equal groups lined up into a rectangle.",
  "guide_2": "See how the stickers are lined up? They go across, and they go up and down.",
  "visual_2": "System briefly outlines the full rectangle shape around the sticker sheet.",
  "guide_3": "When objects are arranged like this — lined up in a rectangle, with every spot filled — that's called an ARRAY.",
  "vocabulary": "array — formally introduced here."
}
```

This is an example for section 1.1 only. Other sections will have different fields depending on their body content — extract exactly what is present.



----------------------------------------------------------------------

### Block 3: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>

{
  "id": "s<major>_<minor>_<slug>",
  "visual": "...",
  "guide": "..."
}

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
{
  "id": "s3_1_first_factor_unknown_skip_counting",
  "index": 9,
  "major": 3,
  "minor": 1,
  "slug": "first_factor_unknown_skip_counting",
  "header": "### Interaction 3.1: First Factor Unknown — Skip-Counting Strategy \\\\\\[WORKED EXAMPLE\\\\\\]",
  "body": "- **Purpose:** Model backward reasoning for unknown first factor (number of groups). This position is taught FIRST because it has a clean, modelable strategy: skip-count by the known second factor and track how many counts it takes to reach the total. This directly extends M9 skip-counting — students count by a familiar number, with the added step of tracking how many jumps.\n- **Visual:** Equal Groups with Pictures: ☐ clusters of 5 birds — clusters are faded. Total shown: \"20 birds total.\" Equation Builder with pre-filled template: `☐ × 5 = 20`. Language prompt displayed above Equation Builder: \"\\\\*\\\\*\\\\_ groups of 5 equals 20 total.\"\n- **Guide:** \"Here's the new unknown. I know there are 5 birds in each group. And I know the total is 20 birds. But I don't know how many groups — that's the unknown.\"\n- **Guide:** \"Let me read the sentence: HOW MANY groups of 5 equals 20 total? I need to figure out how many groups of 5 make 20.\"\n- **Guide:** \"I can skip-count by 5s — I know how to do that. Watch: 5...\"\n- **Visual:** First cluster of 5 birds reveals/highlights. Running count: \"5\"\n- **Guide:** \"...10...\"\n- **Visual:** Second cluster reveals. Running count: \"10\"\n- **Guide:** \"...15...\"\n- **Visual:** Third cluster reveals. Running count: \"15\"\n- **Guide:** \"...20. I'm at 20\\\\!\"\n- **Visual:** Fourth cluster reveals. Running count: \"20\"\n- **Guide:** \"I counted 4 times. That means 4 groups. 4 groups of 5 equals 20.\"\n- **Visual:** Equation updates: `4 × 5 = 20`. All 4 clusters fully visible.\n- **Guide:** \"The unknown was 4\\\\. I used skip-counting — something I already know — to figure out how many groups.\"\n- **No student action** (observation — worked example)\n**Design Note:** First-factor unknown is taught before second-factor because skip-counting by the known second factor is a direct M9 extension and produces the cleanest think-aloud. The Guide models: skip-count by the known factor (5s), stop when you hit the total (20), count your jumps (4). The visual reveals clusters one at a time, synchronized with each skip-count — making the strategy concrete, not abstract. This avoids division language entirely. Second-factor unknown (3.3) follows after students have the backward-reasoning framework established."
}
</input>

======================================================================

## Prefill

{"id": "s3_1_first_factor_unknown_skip_counting",

