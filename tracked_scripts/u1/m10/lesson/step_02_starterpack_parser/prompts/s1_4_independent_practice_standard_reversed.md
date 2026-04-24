# Prompt: starterpack_parser
# Generated: 2026-04-20T12:00:24.016817
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
  "id": "s1_4_independent_practice_standard_reversed",
  "index": 3,
  "major": 1,
  "minor": 4,
  "slug": "independent_practice_standard_reversed",
  "header": "### Interaction 1.5: Independent Practice — Standard or Reversed",
  "body": "- **Purpose:** Student builds an equation independently with minimal support.\n- **Visual:** Equal Groups with Pictures: 4 bags, 6 marbles in each. Equation Builder with template `[___] × [___] = [___]`. Tile palette: `3, 4, 5, 6, 7, 10, 16, 18, 24, 28`.\n- **Guide:** \"One more with bags. Build the equation.\"\n- **Prompt:** \"Build the equation that matches the picture.\"\n- **Correct Answer:** `4 × 6 = 24`\n- **On Correct:** \"4 times 6 equals 24\\\\. Four bags, 6 in each, same value as 24.\"\n- **Visual on Correct:** Reversed version appears: `24 = 4 × 6`. Guide: \"And we can write it this way too — same value.\"\n**Design Note:** Last bags/boxes interaction in the entire curriculum. Standard form assigned (reversed was just practiced in 1.4). Guide shows reversed version on correct to maintain dual-orientation exposure without requiring a template toggle. This also serves as a readiness check: if the student struggles here, Section 2's added complexity (variety \\\\+ unknowns) will compound the difficulty.\n---\n**→ SECTION 1 COMPLETE. PROCEED TO SECTION 2\\\\.**\n---\n## 1.7.2 LESSON SECTION 2: Context Variety \\\\+ Product Unknowns\\*\\*\n**Purpose:** Explicitly introduce non-bag/box equal groups contexts (rows, stacks, groups) and first unknown position (product). Students learn that equal groups appear in many real-world forms. \"\\\\*\\\\*\\\\_ groups of \\\\*\\\\*\\\\_\" remains the structural anchor; context-specific terms (rows, stacks, etc.) are used descriptively, then bridged back: \"\\\\\\[context term\\\\\\] → that's \\\\\\[X\\\\\\] groups of \\\\\\[Y\\\\\\].\" Product unknowns (3 × 5 \\\\= ☐) are the simplest unknown type — students count or skip-count to find the total.\n**Transition from Section 1:**\n- **Guide:** \"You built equations with bags and boxes — and you know that the equals sign means same value as. Now, check this out.\"\n---"
}
</input>

======================================================================

## Prefill

{"id": "s1_4_independent_practice_standard_reversed",

