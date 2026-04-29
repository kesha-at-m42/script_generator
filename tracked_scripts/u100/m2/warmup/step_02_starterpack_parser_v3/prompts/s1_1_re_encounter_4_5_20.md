# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T14:28:01.236271
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
  "id": "s1_1_re_encounter_4_5_20",
  "index": 0,
  "major": 1,
  "minor": 1,
  "slug": "re_encounter_4_5_20",
  "header": "### Interaction W.1: Re-encounter the 4 × 5 = 20 Rectangle [REVIEW]",
  "body": "**Setup:**\nFour equation candidates appear via §2.11 Multiple Choice. All four candidates involve the canonical 4 × 5 = 20 fact. Three share a pattern: they are written with the product on the right side (`a × b = c`). One breaks the pattern: it is written with the product on the left side (`c = a × b`). Hook: \"Look at the rectangle you built last lesson. Four equations all describe it. Three share a pattern. One breaks it. Which one?\"\n\nCandidate set (authoring constraint, single canonical fact only): `4 × 5 = 20` ✓-pattern, `5 × 4 = 20` ✓-pattern, `4 × 5 = 20` ✓-pattern (presented with neutral variation in display order so visual placement is not the discriminator), `20 = 4 × 5` ✗-pattern-breaker (breaks the \"product on right\" pattern).\n\n*(Authoring note 1: To preserve four distinct candidates while keeping the single canonical fact discipline, content authors may use the four equivalent canonical-fact equations: `4 × 5 = 20`, `5 × 4 = 20`, `20 = 4 × 5`, `20 = 5 × 4`. Three should display with the product on the right; one — and only one — with the product on the left as the pattern-breaker. The pattern-breaker MUST be a reversed-orientation form of the canonical 4 × 5 = 20 fact. Per SME 2026-04-28, no non-canonical facts (e.g., `3 × 6 = 18`, `2 × 7 = 14`) appear in W.1.)*\n\n*(Authoring note 2: The purpose of W.1 is not to teach that the reversed orientation is \"wrong\" — the tutor framing after Check will immediately note that BOTH forms are used in today's lesson. The warmup serves only to orient the student's attention to equation orientation as a dimension of variation.)*\n\n**Student Action:**\nStudent taps the equation that breaks the pattern, then taps Check.\n\n**Teacher Move:**\nPost-Check (observable only): \"You tapped that one — it looks different from the others. **That form is today's topic — and you'll see that it is just as correct as the others.** Let's go.\"\n\n*(Bridge statement is REQUIRED verbatim per ISF-M02-5: prevents the warmup from inadvertently signalling that `c = a × b` is aberrant. The post-Check teacher move must explicitly name the reversed-orientation form as \"just as correct\" before the lesson proceeds.)*\n\n**Key Observation:**\nStudent notices orientation as a dimension of variation — the product position is different. Any correct or incorrect tap is acceptable in the warmup; the teacher move is non-evaluative and bridges forward.\n\n**Common Detour:**\nStudent taps a standard-orientation equation as \"the pattern-breaker\" (incorrect selection). The post-Check teacher move is the same either way — non-evaluative, bridges to the lesson. Do not correct.\n\n**Intervention:**\nIf student appears disengaged or taps randomly, acknowledge the selection in observable terms: \"You tapped that one. Let's look at what makes these equations different.\" Proceed to Purpose Frame.\n\n**Next Move:**\nProceed to Purpose Frame, then to Interaction L.1.\n\n**Duration:** 60–90 seconds.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s1_1_re_encounter_4_5_20",

