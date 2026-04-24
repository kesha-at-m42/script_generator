# Prompt: starterpack_parser
# Generated: 2026-04-20T12:00:13.032863
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
  "id": "s2_3_5s_discovery_partial_worked_example",
  "index": 5,
  "major": 2,
  "minor": 3,
  "slug": "5s_discovery_partial_worked_example",
  "header": "### Interaction 2.3: 5s Discovery + Partial Worked Example \\[ABSTRACT — NEW FAMILY INTRODUCTION\\]",
  "body": "This is a two-part interaction: brief animated accumulation for 5s, then tile computation.\n**Part A — 5s Animated Accumulation (Compressed):**\n- **Purpose:** Introduce 5s family with compressed animation (students have now seen format twice).\n- **Visual Phase 1:** Context Visualization clears. Circles with 5 dots each appear one at a time (\\~1 second per circle), system-driven. Equation Builder updates in sync. Only 6 circles shown (compressed — students have seen the format):\n| Circle | Equation Builder | Guide |\n| --- | --- | --- |\n| 1 circle (5 dots) | `1 × 5 = 5` | \"1 group of 5. That's 5.\" |\n| 2 circles | `2 × 5 = 10` | \"2 groups of 5. That's 10.\" |\n| 3 circles | `3 × 5 = 15` | \"15...\" |\n| 4 circles | `4 × 5 = 20` | \"20...\" |\n| 5 circles | `5 × 5 = 25` | \"25...\" |\n| 6 circles | `6 × 5 = 30` | \"30.\" |\n- **Visual Phase 2:** Circles compress. Products Strip appears:\n[ 5 ] [ 10 ] [ 15 ] [ 20 ] [ 25 ] [ 30 ]\n- **Guide:** \"Look at the multiples of 5: 5, 10, 15, 20, 25, 30.\"\n- **Visual:** Highlighting shown of the ones digit of all numbers on the Products Strip.\n- **Guide:** \"Look at the ones place. Interesting! They all end in 0 or 5. Every single one. That's the 5s pattern — multiples of 5 always have 0 or 5 as the ones digit.\"\n- **Student Action:** None (system-driven animation — observation)\n**Part B — 5s Tile Computation (Partial Worked Example):**\n- **Purpose:** First tile placement; bridge pattern discovery to computation.\n- **Visual:** Products Strip remains visible for reference. Equation Builder transitions to: `3 × 5 = [___]` with factors pre-filled. Methods C/D active. Tile palette: 8, 10, 15, 20.\n- **Guide:** \"Now let's use that. Here's 3 times 5. I put the factors: 3 and 5. You find the product. Skip-count by 5s, three times. Place the product tile.\"\n- **Prompt:** \"Find the product of 3 × 5. Place the tile.\"\n- **Student Action:** Equation Builder Methods C or D (tile placement for product slot only)\n- **Correct Answer:** 15\n- **On Correct:** \"3 times 5 equals 15. Ends in 5 — fits the pattern.\"\n- **Remediation:** Pipeline\n> **Remediation Note:** Have student count by 5s three times to find the product (5, 10, 15).\n> **Design Note:** Same two-phase approach as 2s, compressed — 6 circles instead of 10, full narration on circles 1-2 only, faster pacing for 3-6. Students have seen the animated accumulation twice (Warmup + Lesson 1.1); they know the format. Pattern stated by Guide after Products Strip — explicit naming. Then immediate transition to Equation Builder for computation with tiles (first C/D use in M9). Products Strip stays visible during computation as pattern reference.\n---"
}
</input>

======================================================================

## Prefill

{"id": "s2_3_5s_discovery_partial_worked_example",

