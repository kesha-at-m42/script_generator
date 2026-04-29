# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T16:16:25.229313
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
  "id": "s1_1_wodb_recognition_exposure",
  "index": 0,
  "major": 1,
  "minor": 1,
  "slug": "wodb_recognition_exposure",
  "header": "### Interaction W.1: WODB Recognition [EXPOSURE]",
  "body": "**Setup:**\nFour rectangles appear in a 2×2 grid via §2.11 Multiple Choice. Each rectangle is a prebuilt Hundred Grid Mode B observation display (build affordances disabled). A companion §2.13 Mode B display adjacent to the 2×2 grid is also in prebuilt-observation mode. Hook (curiosity gap, ≤15 words): \"Four rectangles. Three go together. One is different. Which one?\"\n\n**Student Action:**\nStudent views all four rectangles — differing in row count, side length, area, or aspect ratio. Student taps the rectangle that does not share the property of the others, then taps Check. After Check, the tapped option is highlighted and the companion §2.13 Mode B display fires a linked highlight reflecting the student's selection. Optional non-gating follow-up stem surfaces via §2.10 Drop Down: `I chose ___ because ___` (pre-filled options; student selects reasoning without free text).\n\n**Teacher Move:**\nAfter Check, acknowledge the selection in observable terms without teaching: \"You chose that one.\" or \"Let's look at what you noticed.\" Do not evaluate or correct — WODB has no wrong answer in the warmup context. If the student selects the optional reasoning stem, acknowledge the selected reason briefly (5–10 words, observable only). Do not introduce vocabulary.\n\n**Key Observation:**\nStudent uses structural language — rows, side, length, total squares, area — even informally. Any mention of row count or side-length difference signals readiness for Beat 2. *(Engineering note: if a student spontaneously uses any of the four fenced terms, the tutor should not correct it in the warmup; address the fence boundary at Beat 2 if needed.)*\n\n**Common Detour:**\nStudent selects an option based on a non-structural visual cue (e.g., apparent size on screen, position in the grid) rather than a mathematical attribute. This is acceptable in the warmup (WODB is low-stakes). The bridge interaction will redirect attention to structure.\n\n**Intervention:**\nIf student appears disengaged or taps randomly, the tutor acknowledges the selection and briefly names one structural property of the chosen rectangle in observable terms: \"That one has ___ rows of ___ squares.\" Do not re-teach or evaluate. Continue to W.2.\n\n**Next Move:**\nProceed to Interaction W.2 (Bridge to Lesson). The companion §2.13 Mode B observation display remains visible; the linked highlight from the student's selection persists briefly, then clears as the bridge begins.\n\n**Duration:**\n60–90 seconds (recognition-only; no production load).\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s1_1_wodb_recognition_exposure",

