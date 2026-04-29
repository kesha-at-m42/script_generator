# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T14:28:05.467490
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
  "id": "s1_1_mode_c_first_reveal_balance",
  "index": 1,
  "major": 1,
  "minor": 1,
  "slug": "mode_c_first_reveal_balance",
  "header": "### Interaction L.1: Mode C First Reveal + Balance Framing (CONCRETE → RELATIONAL) [CONNECT]",
  "body": "**Setup:**\nHundred Grid Mode B reloads the canonical 4 × 5 = 20 M01 rectangle. Build affordances are DISABLED — the student sees the rectangle but cannot place new square tiles. Tutor prompt (student-facing): \"Here is the rectangle you built last lesson. It has 4 square tiles in each row and 5 rows. The area is 20 square tiles.\"\n\nStudent taps Check. **Mode C activates automatically post-Check.** Two-panel strip appears below the rectangle: left panel `4 × 5 = 20`, right panel `20 = 4 × 5`. A bridge element (double-headed arrow or `=`) between panels signals equivalence. Both panels render at identical font size, identical background, identical visual weight.\n\n**Simultaneously**, the static balance-scale tutor-layer asset appears in the tutor explanation zone alongside (not inside) the Mode C strip. Tutor narration (student-facing): \"Look at the equal sign. It is not a 'go' button. It is a balance. What is on this side has the same value as what is on that side. The equal sign means both sides have the same value.\"\n\n**Student Action:**\nStudent taps and holds the left panel (`4 × 5 = 20`) — the rectangle highlights on Mode B above. Student taps and holds the right panel (`20 = 4 × 5`) — the same rectangle highlights. The student observes that both equations point to the same rectangle.\n\nThen the student fills the Drop Down stem: `The equal sign means ___.` Pre-filled options (student selects): \"both sides have the same value\" / \"the answer goes on the right\" / \"I should multiply.\" Only \"both sides have the same value\" is correct.\n\n**Teacher Move:**\nAfter stem completion: \"You got it. The equal sign means both sides have the same value — it is a balance, not a 'go' button.\" *(Observable language only. Balance-scale asset remains visible during the stem.)*\n\n**Key Observation:**\nStudent selects \"both sides have the same value\" in the stem AND demonstrates the tap-and-hold cross-highlighting on both panels. Both behaviors confirm early relational-equal-sign framing.\n\n**Common Detour:**\nStudent selects \"the answer goes on the right\" — the tutor redirects to the balance visual: \"Look at the balance. Both sides of a balance have the same weight. Both sides of the equal sign have the same value. Which option matches the balance?\" Re-offer the stem.\n\n**Intervention (Light):**\nIf student hesitates on which equation is \"correct,\" pulse the Mode C right panel (`20 = 4 × 5`) and animate attention across both panels. Prompt: \"This equation and that equation both show the same rectangle. Can you tap and hold each one to see?\" Do not reveal the answer; return student to the stem.\n\n**Next Move:**\nProceed to Section 2 (Relational), Interaction L.2.\n\n**Duration:** 3–4 minutes.\n\n---\n\n### Section 2: RELATIONAL (L.2 and L.3)"
}
</input>

======================================================================

## Prefill

{"id": "s1_1_mode_c_first_reveal_balance",

