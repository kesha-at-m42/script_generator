# Prompt: starterpack_parser
# Generated: 2026-04-20T11:59:23.263760
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
  "id": "s2_4_guided_practice_full_scaffolding",
  "index": 6,
  "major": 2,
  "minor": 4,
  "slug": "guided_practice_full_scaffolding",
  "header": "**Interaction 2.4: Guided Practice (Full Scaffolding)**",
  "body": "- **Visual:** NEW bar graph appears (vertical, scale of 10, 4 categories: Skateboards 15, Rollerblades 10, Bikes 65, Scooters 30). Title: \"Favorite Ways to Roll\"\n- **Guide:** \"Your turn. Here's a new graph.\"\n- **Visual:** Question appears: \"How many more students chose bikes than scooters and skateboards together?\"\n- **Guide:** \"This problem needs two steps. What should we find first?\"\n- **Prompt:** Select what to find first.\n- **Options:** [A) Add scooters and skateboards, B) Compare bikes to scooters, C) Add all four categories]\n- **Correct Answer:** A\n- **On Correct:** \"Right—scooters and skateboards combined. Let's find that total.\"\n- **On Incorrect (B):** \"Not yet. The question asks about 'scooters and skateboards together.' We need to find that total FIRST, then compare to bikes.\"\n- **On Incorrect (C):** \"The question only mentions three categories: bikes, scooters, and skateboards. We don't need rollerblades.\"\n\n**[CHAINED - Step 2]**\n\n- **Visual:** Scooters (30) and Skateboards (15) highlight. Shows: 30 + 15 = 45\n- **Guide:** \"Scooters and skateboards combined is 45. Now we compare. How many more is bikes than 45?\"\n- **Prompt:** How many more is bikes than 45?\n- **Options:** [A) 110, B) 65, C) 45, D) 20]\n- **Correct Answer:** D (65 - 45 = 20)\n- **On Correct:** \"20 more. Bikes is 65, combined is 45, so 65 minus 45 is 20. You used the strategy: find the combined total first, then compare.\"\n- **On Incorrect (A - added all):** \"You added instead of compared. After finding the combined total, we SUBTRACT to compare.\"\n- **On Incorrect (B - just bikes value):** \"65 is bikes, but the question asks how many MORE than the combined total. Subtract: 65 minus 45.\"\n- **On Incorrect (C - combined total):** \"45 is the combined total—good first step! But now we need to compare: how many more is 65 than 45?\"\n\n**Design Note:** Full scaffolded problem with chained submission. Student identifies first step, then completes second step. Guide provides explicit feedback connecting to strategy.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s2_4_guided_practice_full_scaffolding",

