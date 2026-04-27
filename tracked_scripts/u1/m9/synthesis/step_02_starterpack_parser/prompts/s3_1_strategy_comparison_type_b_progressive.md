# Prompt: starterpack_parser
# Generated: 2026-04-27T10:52:51.312271
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
  "id": "s3_1_strategy_comparison_type_b_progressive",
  "index": 3,
  "major": 3,
  "minor": 1,
  "slug": "strategy_comparison_type_b_progressive",
  "header": "**Task S.3: Strategy Comparison (Type B — Progressive / Metacognitive)**",
  "body": "- **Purpose:** Students see three representations of the same problem and reflect on which approach works for them. This is connection-making between representations, not preference polling.\n- **Visual:** Three-panel display showing 6 × 5 = 30 solved three ways:\n\t- Left: Context Visualization — 6 groups of 5 dots\n\t- Center: Skip-counting display: 5, 10, 15, 20, 25, 30 (six counts highlighted)\n\t- Right: Repeated addition: 5 + 5 + 5 + 5 + 5 + 5 = 30\n\t- Below all three: The equation 6 × 5 = 30\n- **Guide:** \"Three ways to find 6 times 5 equals 30. You can look at the groups and count. You can skip-count: 5, 10, 15, 20, 25, 30. Or you can add: 5 plus 5 plus 5 plus 5 plus 5 plus 5 equals 30. Same answer — all three work.\"\n- **Guide:** \"Which way made more sense to you today?\"\n- **Prompt:** \"Which strategy helped you more?\"\n- **Method:** MC (three options: Looking at the groups / Skip-counting / Repeated addition)\n- **On \"Looking at the groups\":** \"Seeing the groups makes it real — you can count each one. And notice: counting those groups by 5s IS skip-counting. The picture and the counting go together.\"\n- **On \"Skip-counting\":** \"Skip-counting is fast when you know the counts. That'll keep being useful.\"\n- **On \"Repeated addition\":** \"Adding lets you see each group. As you add, you're also counting by 5s. That's a solid strategy too.\"\n**Design Note:** This is a Type 3 metacognitive reflection (Tool/Approach Preference) per the playbook. All three responses are validated — no \"right\" answer. The three-panel display shows strategies as parallel representations progressing from concrete (visual groups) to efficient (skip-counting). Per SME feedback, the visual option completes the representational chain from M7–M8 and the Guide response for that option explicitly bridges it to skip-counting: \"counting those groups by 5s IS skip-counting.\" This reinforces M9's core message that the strategies are connected, not competing. No identity labels (\"you're a skip-counter\"). Observable only: \"which helped you\" not \"which do you understand better.\"\n**Voice compliance:** No assumed internal states. All responses reference what the strategy DOES, not what the student thinks or feels.\n---"
}
</input>

======================================================================

## Prefill

{"id": "s3_1_strategy_comparison_type_b_progressive",

