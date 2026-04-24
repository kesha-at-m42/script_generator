# Prompt: starterpack_parser
# Generated: 2026-04-20T11:59:56.216638
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
  "id": "s2_3_near_independent_graph_callback_identify",
  "index": 7,
  "major": 2,
  "minor": 3,
  "slug": "near_independent_graph_callback_identify",
  "header": "### Interaction 2.3: Near-Independent + Graph Callback \\[IDENTIFY + NOTATION\\]",
  "body": "- **Purpose:** Students identify structure and select expression with minimal Guide support. Include a callback to graphs (Warmup W.1) to make the M6 → M7 connection explicit.\n- **Visual: Context Visualizations.** 4 circles, 5 dots in each circle (same structure as Warmup graph: 4 × 5 = 20).\n- **Guide:** \"You know this already. You did something like this in the graph.\"\n- **Prompt:** \"What do you see?\"\n- **Student Action:** Identify: 4 groups of 5 (with minimal or no Guide support).\n- **Correct Answer:** 4 groups of 5.\n- **On Correct:** \"4 groups of 5. Just like the graph. 4 symbols, each worth 5. Here, 4 circles, 5 dots each.\"\n- **Guide:** \"That's multiplication.\"\n- **Prompt:** \"Which expression matches?\"\n- **Student Action:** Select: A) 4 × 5, B) 5 × 4, C) 4 + 5, D) 5 + 4.\n- **Correct Answer:** A (4 × 5).\n- **On Correct:** \"4 × 5. Four circles, five dots each. Same as the graph scale: 4 groups of 5.\"\n- **Remediation:** Pipeline\n> **Remediation Note:** Distractor B (5 × 4) targets reversal of group count and items-per-group. Distractor C/D (addition) targets the misconception that equal groups use addition. For either error, redirect: \"How many containers? (4) How many inside ONE? (5) That's 4 groups of 5, which is 4 × 5.\"\n> **Voice Note:** The graph callback is celebratory but matter-of-fact. \"You know this already\" affirms prior success. \"Just like the graph\" makes the connection explicit without over-explaining. This is M7's signature insight: multiplication is the same structure that has been hiding inside graphs all along.\n---\n### \\[SECTION TRANSITION\\]\n- **Visual:** Section divider.\n- **Guide:** \"You've described equal groups as 'X groups of Y.' You've matched them to the × expression. Now, can you pick the expression when you just see the picture?\"\n**Voice Note:** Signals the shift from descriptive (\"3 groups of 4\") to symbolic (\"Which expression?\"). Section 3 demands independent selection without the routine's two-step framing.\n---\n## 1.7.3 LESSON SECTION 3: Expression Recognition\n**Purpose:** Students select the correct × expression from MC options based purely on the visual. No scaffolding (\"How many groups?\"). No Guide model. Section 3 tests transfer of the entire routine to independent symbolic recognition. This is the skill that bridges to M8 (where students build expressions)."
}
</input>

======================================================================

## Prefill

{"id": "s2_3_near_independent_graph_callback_identify",

