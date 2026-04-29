# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T16:16:37.330370
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
  "id": "s3_1_build_produce_fixed_side_length",
  "index": 3,
  "major": 3,
  "minor": 1,
  "slug": "build_produce_fixed_side_length",
  "header": "### EC.3: Build and Produce — Fixed Side Length [CREATE + CONNECT]",
  "body": "**Setup:**\n§2.13 Hundred Grid Mode B / B-snap-ON; fixed-side-length lock = 5; labels hidden pre-Check; equation overlay SUPPRESSED. Companion §2.10 Drop Down stem ready to unlock at Check. Tier: STRETCH. Prompt: \"Build a rectangle that has a side length of 5 and an area of 30. Tap Check when you are done, then fill in the sentence.\"\n\n**Student Action:**\nStudent extends the free dimension via row-extension handle to reach area 30 (i.e., 6 rows of 5). Student taps Check; labels reveal (W=5, H=6, area=30). Stem unlocks. Student fills `___ is a multiple of ___ because ___ × ___ = ___` to produce `30 is a multiple of 5 because 5 × 6 = 30` and taps Check on the stem.\n\n**Teacher Move:**\nLight prompt: \"Build the rectangle first. Then use the checked rectangle to fill the sentence.\" Post-Check correct: \"Your rectangle is 5 squares wide and 6 squares tall. The area is 30. 30 is a multiple of 5 because 5 × 6 = 30.\" Post-Check incorrect build (Medium remediation): \"Check the number of rows. You need 6 rows of 5 to reach 30. Try adding one more row.\" Do not reveal target dimensions directly.\n\n**Key Observation:**\nStudent produces a valid build and a valid multiple statement independently. Mastery components: PROCEDURAL (build) + TRANSFER (stem).\n\n**Common Detour:**\nStudent makes an off-target build (e.g., 5×5 = 25 or 5×7 = 35) or finishes the build but cannot complete the sentence correctly.\n\n**Intervention:**\nBrief redirect: \"Check the side length that stayed the same and count how many rows of that side you made.\" If still off-target after one redirect, mark item as Needs Practice and route to Practice intervention path.\n\n**Next Move:**\nRecord mastery state across all three EC items and route to §1.8.5 Practice (or intervention).\n\n**Duration:**\n~90 seconds.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s3_1_build_produce_fixed_side_length",

