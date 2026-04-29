# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T16:16:49.759947
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
  "id": "s4_1_fixed_side_build_row_extension",
  "index": 4,
  "major": 4,
  "minor": 1,
  "slug": "fixed_side_build_row_extension",
  "header": "### Interaction L.4: Fixed-Side Build — Row Extension [ACTIVATION]",
  "body": "**Setup:**\n§2.13 Hundred Grid Mode B is in B-snap-ON. Fixed-side-length lock is active (one dimension locked per authored task — e.g., side length = 4). Tutor prompt: \"Build a rectangle where one side is ___ squares long. Drag the handle to extend the rectangle, then tap Check.\" Tile placement is grid-snapped. Side handle is exposed (B-snap-ON only). Locked-side label visibility governed by label-visibility flag (OQ-M01-LABELS-V4). Free-side label and area label are hidden until Check. U1.1 detection active.\n\n**Student Action:**\nStudent drags the free-side handle (or taps cells) to extend the free dimension, building the rectangle one row at a time. Student taps Check when satisfied. Check reveals dimension labels (W × H) and area label at center. Equation overlay remains SUPPRESSED. Module stem (`___ is a multiple of ___ because ___ × ___ = ___`) unlocks for Interaction L.5.\n\n**Teacher Move:**\nObserve whether student uses the handle (row extension = multiplicative) or taps cells one at a time (tile-by-tile = U1.1 risk). If tile-by-tile detection fires in B-snap-ON: apply U1.1 remediation per §1.4.1 (row highlight + prompt \"How many squares are in each row?\"). Post-Check observable response: \"Your rectangle is ___ wide and ___ tall. The area is ___ square units.\"\n\n**Key Observation:**\nStudent uses the handle drag to extend a full row at once — this is the Relational-stage manifestation of row-based thinking. Handle drag is the observable signal that the student is thinking multiplicatively rather than by 1s.\n\n**Common Detour:**\nStudent taps cells individually instead of using the handle, triggering U1.1 detection even in B-snap-ON. Apply U1.1 Medium remediation: row ghost-extension preview + scaffold stem.\n\n**Intervention:**\n\"Try dragging the side of the rectangle to make it taller. Each drag adds a whole row at once.\"\n\n**Next Move:**\nProceed to L.5 (Multiple Statement Stem — Abstract First Encounter).\n\n**Duration:**\n~2 minutes (build + Check).\n\n---\n\n→ **SECTION 2 COMPLETE. PROCEED TO SECTION 3.**\n\n---\n\n### Section 3: Abstract First Encounter — Multiple Statement (ABSTRACT)\n\nThe equation form appears for the first time — inside the companion Drop Down stem, not on the toy surface. The word \"multiple\" is introduced here. Because equations are suppressed on the Hundred Grid Mode B surface even post-Check, the \"because ___ × ___ = ___\" clause in the stem is the student's first encounter with the multiplication equation for this rectangle. The companion Mode B post-Check state (dimension labels + area label visible) remains on screen as reference while the student fills the stem.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s4_1_fixed_side_build_row_extension",

