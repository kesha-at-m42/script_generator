# Prompt: starterpack_parser_v3
# Generated: 2026-04-29T14:28:05.997511
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
  "id": "s1_1_3_item_exit_check_application",
  "index": 1,
  "major": 1,
  "minor": 1,
  "slug": "3_item_exit_check_application",
  "header": "### EC.1: 3-Item Exit Check [APPLICATION]",
  "body": "*(EC.1 is delivered as a single Exit Check arc containing three sub-items — EC1, EC2, EC3 — per the Mini contract. The Mini Design Doc and Tool Flow Document consistently treat the EC arc as one beat. Sub-items are sequenced; mastery is computed across all three.)*\n\n**Purpose:** Test the reversed-orientation Focus skill bidirectionally. The L.3 operations-on-both-sides recognition exposure is NOT exit-checked — EC.1 tests only reversed-orientation recognition and production.\n\n**Toy:** §2.10 Drop Down (production sub-items EC2, EC3) + §2.11 Multiple Choice / Checkbox (recognition sub-item EC1) + Hundred Grid Mode B/C companion display.\n\n**Introduction (student-facing):** \"Now show what you know. Three quick questions about the same fact, both ways around.\"\n\n| EC Sub-Item | Display | Student Task | Skill Tested | Mastery Contribution |\n|---------|---------|-------------|-------------|---------------------|\n| **EC1** | `5 × 8 = 40` rectangle displayed (canonical-adjacent fact, NOT the 4 × 5 instructional rectangle). §2.11 Checkbox. Candidates: `5 × 8 = 40` ✓, `40 = 5 × 8` ✓, `5 + 8 = 40` ✗, `8 × 40 = 5` ✗. | Select ALL correct equations. | Recognition: both reversed orientations, both must be selected | Strong requires both correct selected with no distractors |\n| **EC2** | `7 × 6 = 42` displayed as given. §2.10 Drop Down stem: `The same rectangle shows ___ × ___ = ___ AND ___ = ___ × ___ because the equal sign means both sides have the same value.` | Complete the stem — fill both orientations. | Production: reversed form from given standard | Needs Practice if EC1+EC3 correct but EC2 wrong |\n| **EC3** | `36 = 9 × 4` displayed as given. §2.10 Drop Down stem: `The same rectangle shows ___ × ___ = ___ AND ___ = ___ × ___ because the equal sign means both sides have the same value.` | Complete the stem — fill both orientations. | Production: standard form from given reversed | Still Gathering if 0–1 items correct OR if EC1 selects only `a × b = c` and rejects `c = a × b` |\n\n**Vocabulary check (EC items):** No \"factor,\" \"factor pair,\" \"prime,\" \"composite,\" \"height,\" \"handle,\" bare \"squares,\" or WODB language. \"Multiple\" / \"is a multiple of\" is permitted in EC items (Abstract section). No operations-both-sides items in EC.1.\n\n**Required phrase (verbatim in EC2 and EC3 production stems):**\n`The same rectangle shows ___ × ___ = ___ AND ___ = ___ × ___ because the equal sign means both sides have the same value.`\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s1_1_3_item_exit_check_application",

