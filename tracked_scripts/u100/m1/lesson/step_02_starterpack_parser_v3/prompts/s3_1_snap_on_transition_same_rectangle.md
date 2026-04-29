# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T16:16:42.923002
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
  "id": "s3_1_snap_on_transition_same_rectangle",
  "index": 3,
  "major": 3,
  "minor": 1,
  "slug": "snap_on_transition_same_rectangle",
  "header": "### Interaction L.3: Snap-On Transition — Same Rectangle, Grid-Snapped [TRANSITION]",
  "body": "**Setup:**\nThe snap-on toggle fires (tutor-commanded). The student's free-placed rectangle re-anchors to grid coordinates through a snap animation. Each tile moves from its loose position to a grid coordinate — smooth movement, not teleport. Ambiguous tile overlaps (if any) resolve to one tile per cell; extras silently removed with undo affordance. After the animation, the same §2.13 Hundred Grid Mode B surface is now in B-snap-ON. U1.1 detection continues active.\n\n**Student Action:**\nStudent observes the snap animation. After the animation settles, the tutor highlights one row and prompts the student to tap a highlighted row or side to acknowledge the structure. This is a low-cognitive-load confirmation tap.\n\n**Teacher Move:**\n\"Watch what happens to your rectangle — it's snapping into the grid. Same rectangle, easier to read.\" After the student's acknowledgment tap: \"Do you see the rows? Every row has the same number of squares.\" No new vocabulary. No equation.\n\n**Key Observation:**\nStudent's recognition that the snapped rectangle is \"the same one\" is the conceptual payload of this interaction — it establishes continuity between the Concrete (loose tiles) and Relational (grid-snapped) stages. If student expresses surprise at the shape change (e.g., tiles moved slightly), acknowledge it as part of the snap.\n\n**Common Detour:**\nStudent expects a new rectangle to appear (thinks the snap is a reset). Reassure: \"Your tiles just lined up — same number of squares, now organized in the grid.\"\n\n**Intervention:**\nNo remediation needed for this beat; it is observational and guided. If the student is visibly confused, name continuity: \"It has the same squares as before. Just easier to see now.\"\n\n**Next Move:**\nProceed to L.4 (Fixed-Side-Length Build, B-snap-ON).\n\n**Duration:**\n45–60 seconds (transition + acknowledgment tap).\n\n---\n\n→ **SECTION 1 COMPLETE. PROCEED TO SECTION 2.**\n\n---\n\n### Section 2: Relational Build — Fixed Side Length (RELATIONAL)\n\nThe student builds new rectangles in B-snap-ON with a fixed side length locked. One dimension is locked by the authored activity; the other is student-built using the handle or cell taps. Tiles are grid-snapped. The locked-side label visibility follows the label-visibility flag (OQ-M01-LABELS-V4); the free-side dimension label and area label remain hidden until Check regardless of flag setting. Equation overlays remain SUPPRESSED. After Check, the module stem (Beat 5) unlocks — this is the student's first encounter with the equation form.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s3_1_snap_on_transition_same_rectangle",

