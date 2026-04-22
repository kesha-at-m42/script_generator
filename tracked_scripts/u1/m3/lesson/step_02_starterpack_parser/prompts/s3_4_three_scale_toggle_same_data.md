# Prompt: starterpack_parser
# Generated: 2026-04-20T11:57:19.535938
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
  "id": "s3_4_three_scale_toggle_same_data",
  "index": 19,
  "major": 3,
  "minor": 4,
  "slug": "three_scale_toggle_same_data",
  "header": "**Interaction 3.2b: Three-Scale Toggle — Same Data, Your Choice of Scale \\[OBSERVATION ONLY\\]**",
  "body": "- **Purpose:** Extend M2's binary scale comparison to a three-way pattern. Student toggles between scales 1, 2, and 5 on their own graph data, discovering that \"bigger scale = fewer symbols\" is a general principle. Builds metarepresentational competence through direct manipulation—the student causes the transformation, making scale a visible choice rather than an invisible given.\n- **Visual: Picture Graphs (side-by-side comparison).** Student's completed 1:5 horizontal \"Books Read\" graph displayed. Scale toggle control with three options: \"Each ⭐ = 1,\" \"Each ⭐ = 2,\" \"Each ⭐ = 5.\" Defaults to scale of 5. Data Table visible as stable anchor (Liam=35, Emma=20, Noah=25, Olivia=40). Key updates dynamically. Toggle sequence: 5→1 (Olivia: 8→40 symbols), 1→2 (Olivia: 40→20 symbols; half-symbols appear for odd-divided values), 2→5 (return to original).\n- **Guide:** \"You built this graph with scale of 5. But what would it look like with a different scale? Try it.\"\n- **Prompt:** \"Toggle the scale to 1. What happens?\"\n- **Student Action:** Click scale toggle from 5 to 1. Graph animates: symbols multiply (Olivia: 8 → 40; Liam: 7 → 35; Noah: 5 → 25; Emma: 4 → 20). Key updates to \"Each ⭐ = 1.\"\n- **Guide:** \"Olivia went from 8 symbols to 40! That's a LOT of symbols. Now try scale of 2.\"\n- **Student Action:** Click scale toggle from 1 to 2. Graph animates: symbols reduce. Key updates to \"Each ⭐ = 2.\"\n- **Guide:** \"Fewer symbols — but still more than scale of 5. Toggle back to 5.\"\n- **Student Action:** Click scale toggle from 2 to 5. Graph animates back to original state. Key updates to \"Each ⭐ = 5.\"\n- **Guide:** \"Same 40 books for Olivia every time. Scale of 1: 40 symbols. Scale of 2: 20 symbols. Scale of 5: just 8.\"\n- **Prompt:** \"Which scale uses the fewest symbols?\"\n- **Student Action:** \\[Multiple choice: Scale of 1, Scale of 2, Scale of 5\\]\n- **Correct Answer:** Scale of 5\n- **On Correct:** \"Scale of 5. Bigger scale, fewer symbols — same data.\"\n- **Remediation (Light):** \"Toggle through all three again and count Olivia's symbols each time. 40, then 20, then 8. Which is fewest?\"\n- **Guide:** \"All three showed the same information. The scale just changes how many symbols you need. Now let's use YOUR graph to answer some questions.\"\n- **Duration:** 45–55 seconds\n- **No student graph creation** (toggle is observation/exploration only)\n\n**Design Notes:**\n\n- Student toggles through all three scales in sequence (5→1→2→5). The full cycle makes scale of 5's efficiency feel earned, not asserted.\n- Half-symbols appear naturally at scale of 2 for odd-valued results. Guide does NOT call attention to this—it's background observation. Students already learned half-symbols in M2.\n- Animation between states should be smooth (~0.5s). The toggle becomes inactive after the MC question is answered.\n- The data table stays visible throughout as the stable reference point. The graph transforms; the data doesn't.\n\n---"
}
</input>

======================================================================

## Prefill

{"id": "s3_4_three_scale_toggle_same_data",

