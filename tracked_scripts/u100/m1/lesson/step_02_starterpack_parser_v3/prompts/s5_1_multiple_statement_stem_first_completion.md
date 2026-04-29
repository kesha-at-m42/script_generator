# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T16:16:57.324417
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
  "id": "s5_1_multiple_statement_stem_first_completion",
  "index": 5,
  "major": 5,
  "minor": 1,
  "slug": "multiple_statement_stem_first_completion",
  "header": "### Interaction L.5: Multiple Statement Stem — First Completion [ACTIVATION]",
  "body": "**Setup:**\nHundred Grid Mode B is in post-Check state (dimension labels W × H and area label visible; equation overlay SUPPRESSED). The companion §2.10 Drop Down stem has unlocked: `___ is a multiple of ___ because ___ × ___ = ___`. At BASELINE, some slots are pre-filled via linked values from the Mode B Check (dimension values + area value auto-pushed); student confirms or fills remaining slots. At STRETCH/CHALLENGE, slots are blank (full production). Tutor prompt: \"Now fill in the sentence about your rectangle.\"\n\n**Student Action:**\nStudent taps each blank slot, selects from dropdown or types a numeric value, and taps Check on the stem. Linked slots (pre-filled values) are visually distinct from student-entered slots. If incorrect: the incorrect blank highlights in a distinct color without revealing the correct answer. Correct: all slots filled; stem confirms. Student reads the completed stem in context of the visible rectangle.\n\n**Teacher Move:**\nPost-Check correct: \"Your sentence says ___ is a multiple of ___ because ___ × ___ = ___. That matches the rectangle you built.\" (Observable only — no \"you understood,\" \"you got it.\") Incorrect slot highlight: \"Check the area of the rectangle. Count the rows of ___.\"\n\n**Key Observation:**\nThis is the moment \"multiple\" enters the student's vocabulary, anchored to a concrete artifact. The student should be able to point from the stem to the labeled rectangle: \"The area is the first blank; the fixed side length is the second blank.\"\n\n**Common Detour:**\nStudent fills the area blank and the side-length blank in reversed order (M01-3 / slot-filling pattern). Address by pointing to the labeled rectangle: \"The area label is the big number. That's the number that is a multiple.\"\n\n**Intervention:**\n\"Look at the rectangle. The area — the total squares — goes in the first blank. The side length — the fixed one — goes in the second blank. What's the area?\"\n\n**Next Move:**\nBASELINE: Proceed to L.6 (additional fixed-side-length build, varied free dimension). STRETCH: Proceed to blank-build with a different fixed side length. CHALLENGE: Open-ended multiple discovery (find as many areas as possible for the given side length).\n\n**Duration:**\n~2 minutes (stem completion + Check).\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s5_1_multiple_statement_stem_first_completion",

