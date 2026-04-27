# Prompt: starterpack_parser
# Generated: 2026-04-27T10:53:11.367719
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
  "id": "s2_2_equal_vs_unequal_groups_identification",
  "index": 5,
  "major": 2,
  "minor": 2,
  "slug": "equal_vs_unequal_groups_identification",
  "header": "### Interaction 2.2: Equal vs. Unequal Groups — Identification \\\\\\[CONCEPTUAL CHECK\\\\\\]",
  "body": "- **Purpose:** Teach that not every grouping of objects represents equal groups — and only equal groups can be described with multiplication. Students evaluate four visual arrangements and select which ones show equal groups. This surfaces the \"equal\" criterion explicitly, preventing students from writing multiplication equations for any collection of items that happen to be clustered.\n- **Visual:** Four images displayed in a 2×2 grid, labeled A-D:\n\t- A: 3 shelves with 6 jars on each shelf (equal — 3 × 6\\\\)\n\t- B: 4 plates with different numbers of cookies: 5, 6, 5, 2 (unequal — same containers, different amounts)\n\t- C: 2 equal stacks of 9 books (equal — 2 × 9\\\\)\n\t- D: 3 groups of animals: 7 ducks, 4 ducks, 7 ducks (unequal — similar visual pattern but middle group differs)\n- **Guide:** \"Equal groups are everywhere — but not EVERY group of things is an equal group. Look at these four pictures. Each picture has 18 items in total. Which ones show equal groups — the same number in every group?\"\n- **Prompt:** \"Select ALL the pictures that show equal groups.\"\n- **Student Action:** Multi-select (select all that apply: A, B, C, D)\n- **Correct Answer:** A and C\n- **On Correct (both A and C selected):**\n\t- **Guide:** \"A has 3 shelves with 6 on each — equal groups. C has 2 stacks of 9 — equal groups. We can write multiplication equations for these. B and D? The groups aren't equal — different amounts in different groups. We can't write a multiplication equation for those.\"\n- **Remediation:** Pipeline\n> **Remediation Note:** Partial correct (selected A/C plus B or D): highlight the incorrectly added image group by group with counts — ask if every group has the same number. Missed A or C: direct student to count items in every group in each picture; equal groups means every group has the same count. Distractor B uses identical containers with unequal contents; Distractor D uses a near-miss 7/4/7 pattern.\n**Design Note:** This is the explicit instructional moment for equal vs. unequal groups. Placed after the variety announcement (2.1) and before the first product-unknown task (2.3), it establishes the evaluation criterion students need before building equations from new contexts. Distractor B uses identical containers with unequal contents — testing whether students check the amounts, not just the containers. Distractor D uses a near-miss pattern (7, 4, 7\\\\) that could be mistaken for equal at a glance. Multi-select rather than binary avoids the lab-testing issue flagged for W.2. This is a recognition/judgment task, not a construction task — students evaluate representations rather than building them.\n---"
}
</input>

======================================================================

## Prefill

{"id": "s2_2_equal_vs_unequal_groups_identification",

