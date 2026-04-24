# Prompt: starterpack_parser
# Generated: 2026-04-20T11:59:33.727080
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
  "id": "s3_1_reduced_scaffolding_3_step_chain",
  "index": 8,
  "major": 3,
  "minor": 1,
  "slug": "reduced_scaffolding_3_step_chain",
  "header": "**Interaction 3.1: Reduced Scaffolding (3-Step Chain)**",
  "body": "- **Visual:** NEW bar graph (horizontal, scale of 5, 4 categories). Title: \"Fruit Stand Sales\". Values: Grapes 15, Apples 45, Bananas 30, Oranges 25.\n- **Visual:** Question appears: \"How many fewer oranges and grapes combined were sold than apples?\"\n- **Guide:** \"Here's another one. What should we find first?\"\n\n**[CHAINED - Step 1: Identify Strategy]**\n\n- **Prompt:** Select what to find first.\n- **Options:** [A) Add oranges and grapes, B) Subtract grapes from oranges, C) Compare apples to oranges]\n- **Correct Answer:** A\n- **On Correct:** \"Right—oranges and grapes combined. Find that total.\"\n- **On Incorrect:** \"Look for 'combined' in the question. Oranges and grapes combined—add those first.\"\n\n**[CHAINED - Step 2: Execute Combining]**\n\n- **Visual:** Oranges bar (25) and Grapes bar (15) highlight.\n- **Guide:** \"Oranges is 25. Grapes is 15. What's the combined total?\"\n- **Prompt:** How many oranges and grapes combined?\n- **Options:** [A) 10, B) 30, C) 40, D) 45]\n- **Correct Answer:** C (25 + 15 = 40)\n- **On Correct:** \"40 combined.\"\n- **On Incorrect (A):** \"You subtracted. 'Combined' means add: 25 plus 15.\"\n- **On Incorrect (B or D):** \"Check your addition. 25 plus 15 equals...\"\n\n**[CHAINED - Step 3: Execute Comparison]**\n\n- **Visual:** Combined value (40) displayed. Apples bar (45) highlights.\n- **Guide:** \"Oranges and grapes combined is 40. Apples is 45. Now find how many fewer.\"\n- **Prompt:** How many fewer oranges and grapes combined than apples?\n- **Options:** [A) 85, B) 45, C) 40, D) 5]\n- **Correct Answer:** D (45 - 40 = 5)\n- **On Correct:** \"5 fewer. You found the combined total first, then compared.\"\n- **On Incorrect (A):** \"You added. 'How many fewer' means compare—subtract.\"\n- **On Incorrect (B or C):** \"Those are values from the problem. The question asks for the difference: 45 minus 40.\"\n\n**Design Note:** Reduced scaffolding—Guide asks \"What should we find first?\" but doesn't say \"This needs two steps.\" Three-step chain ensures student EXECUTES both operations, not just identifies them.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s3_1_reduced_scaffolding_3_step_chain",

