# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T14:28:19.527406
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
  "id": "s3_1_operations_both_sides_recognition_hybrid",
  "index": 3,
  "major": 3,
  "minor": 1,
  "slug": "operations_both_sides_recognition_hybrid",
  "header": "### Interaction L.3: Operations-Both-Sides Recognition — Hybrid Beat (RELATIONAL) [IDENTIFY]",
  "body": "*(Engineering-internal note: This beat is the L.3 NEW Hybrid per SME 2026-04-28. Recognition-only. Multiplicative-commutative form `a × b = b × a` ONLY. NOT exit-checked. The word \"multiple\" is FORBIDDEN in student-facing copy at this beat.)*\n\n**Setup:**\nMode C hosts a paired-equation display: left panel `4 × 5 = 20` (the reversed-orientation fact already established in L.1/L.2), right panel `4 × 5 = 5 × 4` (the operations-on-both-sides multiplicative-commutative form). The canonical 4 × 5 = 20 Mode B rectangle is visible above the paired display.\n\n§2.11 Multiple Choice surfaces two candidates. Tutor prompt (student-facing): \"Both of these equations describe the same rectangle. Tap the one that says it correctly.\"\n\nCandidate set: `4 × 5 = 5 × 4` ✓ (operations-on-both-sides, multiplicative-commutative, correct), `4 × 5 = 5 + 4` ✗ (mixed-operation distractor, incorrect).\n\nPost-Check Drop Down stem: `Both sides of `4 × 5 = 5 × 4` show the ___.` Target completion: \"same value.\" Pre-filled options: \"same value\" / \"same number of square tiles only\" / \"same number of rows only.\"\n\n**Student Action:**\nStudent taps `4 × 5 = 5 × 4`, then taps Check. Completes the Drop Down stem.\n\n**Teacher Move:**\nPost-Check: \"You got it. Both sides of `4 × 5 = 5 × 4` show the same value — 20. The equal sign means same value on both sides, no matter how many operations are on each side.\" *(Required phrase: \"same value on both sides.\")*\n\n**Key Observation:**\nStudent selects the correct multiplicative-commutative form AND completes the stem with \"same value.\" This confirms the relational equal-sign framing extends to forms with operations on both sides.\n\n**Common Detour:**\nStudent selects the mixed-operation distractor (`4 × 5 = 5 + 4`). Tutor: \"Does `5 + 4` equal 20? Let's check: 5 + 4 = 9, not 20. The equal sign means same value on both sides — which equation has the same value on both sides?\" Re-offer the choice.\n\n**Intervention:**\nIf student is unsure, the tutor highlights each panel of the Mode C display and narrates: \"Left side: `4 × 5` — what is that?\" (student mentally confirms: 20). \"Right side: `5 × 4` — what is that?\" (student mentally confirms: 20). \"Same value on both sides.\" Then re-offer the choice.\n\n**Misconception Prevention Note:**\nThis beat does NOT test `4 × 5 = 2 × 10` or any equivalent-product form — that is M03 territory. The distractor uses `5 + 4` to avoid equivalent-product confusion. The word \"multiple\" / \"is a multiple of\" does NOT appear in any student-facing copy at this beat. The word \"commutative\" does NOT appear in student-facing copy (engineering-internal only).\n\n**Next Move:**\nProceed to Section 3 (Abstract), Interaction L.4.\n\n**Duration:** 2–3 minutes.\n\n---\n\n### Section 3: ABSTRACT (L.4)"
}
</input>

======================================================================

## Prefill

{"id": "s3_1_operations_both_sides_recognition_hybrid",

