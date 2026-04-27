# Prompt: starterpack_parser
# Generated: 2026-04-27T10:52:38.500224
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
  "id": "s2_1_reversed_equation_judgment_task_curiosity",
  "index": 1,
  "major": 2,
  "minor": 1,
  "slug": "reversed_equation_judgment_task_curiosity",
  "header": "### Interaction W.2: Reversed Equation — Judgment Task \\\\\\[CURIOSITY GAP\\\\\\]",
  "body": "- **Purpose:** Present the reversed orientation of the student's own equation as a genuine judgment task. Creates the curiosity gap that Lesson 1.2 will satisfy (\"equals means same value as\"). All responses are valid Warmup responses — none are wrong, because the student's reasoning reveals their current understanding of \\\\=. The Lesson teaches the concept regardless.\n- **Visual:** The equation from W.1 (`5 × 2 = 10`) remains on screen. A second equation appears alongside or below it, reversed: `10 = 5 × 2`.\n- **Guide**: \"Now look at this equation. What do you think?\"\n- **Prompt**: \"What do you think about 10 \\\\= 5 × 2?\"\n- **Method**: MC (4 options — reasoning-based)\n- **Options**:\n\t- A: \"It's true — both sides are 10\"\n\t- B: \"It's true — it's just written differently\"\n\t- C: \"It's wrong — the answer should come last\"\n\t- D: \"I'm not sure\"\n\tOn A: \"You checked both sides. Smart thinking. Hold that thought.\"\n\tOn B: \"You noticed it's the same equation, just flipped. Hold that thought.\"\n\tOn C: \"Interesting — something looks different about it. Hold that thought.\"\n\tOn D: \"That's honest — it does look different. Hold that thought.\"\n**Engagement Anchor 2:** Curiosity Gap (\"Is this still true?\" — genuine question that creates anticipation for the Lesson's answer)\n**Design Note:** This is the Warmup's key priming moment. Students who say \"Yes\" may already have flexible \\\\= sign understanding — Lesson 1.2 will deepen and formalize it. Students who say \"No\" hold the common misconception (\\\\#19: equals means \"answer comes next\") — Lesson 1.2 directly addresses this. Either way, the student has now THOUGHT about what \\\\= means before the Lesson teaches it. This is the difference between teaching and priming: the Warmup raises the question, the Lesson provides the answer. Guide says \"Hold that thought\" for both responses — maintaining mystery without validating either answer as correct. No \"You're right\" or \"Not quite\" — that would constitute teaching.\n---\n**Bridge to Lesson:**\n- **Visual:** Both equations remain visible (`5 × 2 = 10` and `10 = 5 × 2`).\n- **Guide:** \"You can build equations. But today, equations have some surprises. You'll see them in new ways and figure out missing numbers.\"\n- **No student action**\n**Design Note:** Bridge previews all three Lesson demands in compressed form: \"new ways\" (= sign flexibility \\\\+ context variety) and \"missing numbers\" (unknowns). Session-relative language avoided — no \"today\" in the Guide line, replaced with \"but today\" which functions as a natural conjunction. The preview matches the backbone's specified language: *\"You'll write equations, see them in new ways, and figure out missing numbers.\"* Both equations staying visible through transition creates seamless visual continuity into Lesson 1.1.\n---"
}
</input>

======================================================================

## Prefill

{"id": "s2_1_reversed_equation_judgment_task_curiosity",

