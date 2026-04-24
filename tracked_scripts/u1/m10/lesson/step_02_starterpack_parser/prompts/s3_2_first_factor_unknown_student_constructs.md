# Prompt: starterpack_parser
# Generated: 2026-04-20T12:01:11.627965
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
  "id": "s3_2_first_factor_unknown_student_constructs",
  "index": 10,
  "major": 3,
  "minor": 2,
  "slug": "first_factor_unknown_student_constructs",
  "header": "### Interaction 3.2: First Factor Unknown — Student Constructs (Construction → Equation)",
  "body": "- **Purpose:** Student uses Construction Mode to apply the skip-counting strategy from 3.1. First-factor unknown — student builds groups of a known size until the running total hits the target.\n- **Visual:** Equal Groups with Pictures in Construction Mode. Equation Builder with pre-filled template: `☐ × 10 = 40`. Language prompt: \"\\\\*\\\\*\\\\_ groups of 10 equals 40 total.\" Construction area starts empty. \\\\+/- group control available (each new group pre-set to 10 items per the equation's known factor). Running total display: \"Total: 0 / 40.\"\n- **Guide:** \"Now you try. Groups of 10\\\\. Total is 40\\\\. How many groups do you need? Build groups until you hit 40.\"\n- **Prompt:** \"☐ × 10 \\\\= 40\\\\. Build groups of 10 until the total reaches 40.\"\n- **Student action:** Uses \\\\+ to add groups of 10\\\\. Running total updates: 10, 20, 30, 40\\\\.\n- **On Correct (4 groups of 10, total \\\\= 40):**\n\t- **Guide:** \"4 groups of 10 equals 40\\\\. You skip-counted — 10, 20, 30, 40 — and it took 4 groups.\"\n\t- **Visual:** Equation completes: `4 × 10 = 40`. Reversed shown: `40 = 4 × 10`.\n- **On Overshoot (e.g., 5 groups of 10 \\\\= 50):**\n\t- **Guide:** \"That's 50 — too many. Remove a group and check again.\"\n**Design Note:** Uses ×10 family for the student's first attempt — simplest skip-counting pattern, lowest computation load, so cognitive effort goes to the new backward-reasoning process. Construction Mode makes the skip-counting strategy physical: each group added IS a skip-count. The running total makes \"how many jumps to reach the target\" visible. **Fallback if Construction Mode unavailable:** MC specification: `[2] [3] [4] [5]` → system builds visual for selected answer.\n<empty-block/>\n**New Interaction 3.3: Second Factor Unknown — Construction Strategy**\n- **Purpose:** Unknown moves to the second factor position (items per group). This is harder than first-factor because you can't directly skip-count by an unknown number. Strategy: builds groups to match with Construction Equation Builder, demonstrating structural understanding.\n- **Visual:** Equation Builder with pre-filled template: `2 × ☐ = 10`. Language prompt: \"2 groups of \\\\*\\\\*\\\\_ equals 10 total.\" Equal Groups with Pictures in Construction Mode: 2 empty groups displayed (group count locked at 2 per equation) — 2 circled groups visible, items inside covered/hidden. Per-group \\\\+/- controls. Running total: “Total: 0.\"\n- **Guide:** \"Here's the equation. 2 groups of how many cats equals 10\\\\. We need to build the groups. Let’s add equal items to the 2 groups until you reach 10\\\\. Add 5 to each group so the total reaches 10.\"\n- **Prompt:** \"2 × ☐ \\\\= 10\\\\. Add 5 cats to each of the 2 groups to make 10 total.\"\n- **Student action:** Uses \\\\+/- to add 5 items to both individual groups. Running total updates live.\n- **On Correct (2 equal groups of 5, total \\\\= 10):**\n\t- **Guide:** \"2 times 5 equals 10\\\\. You started with the equation and BUILT the answer. Now we can skip count by 5s two times: 5, 10\\\\. That’s the total of 10\\\\. Each side of the equation has the same value.\"\n- **On Correct Total, Unequal Groups:**\n\t- **Guide:** \"You hit 10\\\\. But check — are the groups equal? Multiplication needs equal groups. Adjust so each group has the same number.\"\n- **On Equal Groups, Wrong Total:**\n\t- **Guide:** \"Equal groups — great\\\\! But the total isn't 10\\\\. Add more to each group (or remove some) and watch the total.\"\n- **Guide:** \"Your turn with a different one. 2 groups, 14 total. 2 times what equals 14?\"\n- **Prompt:** \"2 × ☐ \\\\= 14\\\\. How many in each group?\"\n- **Student action:** Uses \\\\+/- to add items to individual groups. Running total updates live.\n- **Correct Answer:** `7`\n- **On Correct (2 equal groups of 7, total \\\\= 14):**\n\t- **Visual:** 7 cats appear in each group. Equation completes: `2 × 7 = 10`.\n\t- **Guide:** \"2 times 7 equals 14\\\\. 2 groups of 7 is 14\\\\. You built the answer.\"\n\t- **Visual:** Reversed form: `14 = 2 × 7`.\n- **On Correct Total, Unequal Groups:**\n\t- **Guide:** \"You hit 14\\\\. But check — are the groups equal? Multiplication needs equal groups. Adjust so each group has the same number.\"\n- **On Equal Groups, Wrong Total:**\n\t- **Guide:** \"Equal groups — great\\\\! But the total isn't 14\\\\. Add more to each group (or remove some) and watch the total.\"\n**Design Note:** The Guide explicitly names why second-factor is harder: \"I can't skip-count by a number I don't know yet.\" This validates the difference students may feel. The strategy — recalling facts from the known factor's family — is less mechanical than skip-counting but leverages M9 fluency directly. Uses ×2 family (most automatic from M9) to keep computation trivial while students internalize the new reasoning direction. MC scaffolds the answer space. Placed third in the sequence so students already have the backward-reasoning mindset from 3.1-3.2."
}
</input>

======================================================================

## Prefill

{"id": "s3_2_first_factor_unknown_student_constructs",

