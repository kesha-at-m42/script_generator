# Prompt: starterpack_parser
# Generated: 2026-04-27T10:52:31.269272
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
  "id": "s1_1_extend_accumulation_5_10_concrete",
  "index": 0,
  "major": 1,
  "minor": 1,
  "slug": "extend_accumulation_5_10_concrete",
  "header": "### Interaction 1.1: Extend Accumulation — 5 to 10 \\[CONCRETE — EXTENSION\\]",
  "body": "- **Purpose:** Extend animated accumulation from Warmup, revealing full set of 2s multiples.\n- **Visual (Opening):** 5 circles from Warmup visible (or re-displayed). Products Strip shows: `[2] [4] [6] [8] [10]`. Equation Builder shows: `5 × 2 = 10`.\n- **Guide:** \"You saw 5 groups of 2. Let's see what happens when we keep going.\"\n- **Visual (Animation):** Circles 6-10 appear at accelerated pace (\\~0.5 sec each). Equation Builder updates in sync:\n| Circle | Equation Builder | Guide |\n| --- | --- | --- |\n| 6 circles | `6 × 2 = 12` | \"12...\" |\n| 7 circles | `7 × 2 = 14` | \"14...\" |\n| 8 circles | `8 × 2 = 16` | \"16...\" |\n| 9 circles | `9 × 2 = 18` | \"18...\" |\n| 10 circles | `10 × 2 = 20` | \"20.\" |\n- **Visual (Products Strip extends):** Strip grows from 5 to 10 products:\n[ 2 ] [ 4 ] [ 6 ] [ 8 ] [ 10 ] [ 12 ] [ 14 ] [ 16 ] [ 18 ] [ 20 ]\nAll 10 products glow or highlight. Label appears: \"Multiples of 2\"\n- **Guide:** \"These are the multiples of 2 — all the products you get when you multiply by 2. Look at them together.\"\n- **Student Action:** None (system-driven animation — observation)\n> **Design Note:** Faster than full animation — only 5 new circles at accelerated pace instead of 10 from scratch. Builds directly on Warmup: \"What happens when we keep going?\" feels like continuation, not repetition. Vocabulary: \"multiples\" introduced here, attached to the full Products Strip. Guide does not name the pattern yet — that's 1.2.\n---"
}
</input>

======================================================================

## Prefill

{"id": "s1_1_extend_accumulation_5_10_concrete",

