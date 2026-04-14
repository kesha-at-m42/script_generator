# Prompt: starterpack_parser
# Generated: 2026-04-07T13:22:07.888848
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 16000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are converting a freeform lesson spec into a structured JSON format. Your job is precise extraction: pull every field from the spec as written, faithfully and completely.

----------------------------------------------------------------------

### Block 2: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

Parse the markdown spec in <input> into a flat array of section objects.

One section object per spec section header. Sub-sections (e.g. W.3a, W.3b,
W.3c) become separate section objects — do not nest them.

**Section boundaries come only from spec headers** (e.g. `### Interaction 1.3`,
`## Section W.1`). Never split a section because of text inside a field value,
including `[Immediately followed by:]` annotations. That content stays in the
same section object, captured verbatim in its field.

---

## PARSING RULES

### Field extraction

Every line in the spec following the pattern `**Label:** content` becomes a
field. The label (before the colon) is the field key, converted to snake_case.
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

If a label appears that is not in this table, still include it — use its
snake_case form as the key. Do not drop any field from the spec.

If the same label appears more than once in a section, suffix each occurrence with `_1`, `_2`, `_3`, etc. (e.g. three `**Student Action:**` fields become `student_action_1`, `student_action_2`, `student_action_3`). Apply this to all repeated labels including `visual`, `guide`, `prompt`, `correct_answer`, `on_correct`, etc. Never silently overwrite a field — every occurrence must be preserved.

### Prose between fields

Spec sections sometimes contain plain sentences or bold step markers between key-value pairs (e.g. `**Step 1 — Specification:**` with no content after the colon, or a sentence like "Sequential enforcement same as 3.2/3.3."). These are not fields and not section boundaries. Capture them as `"divider": "..."` — one divider entry per run of such text. Do not let them interrupt field parsing or bleed into adjacent field values.

Any `**Label:** content` lines that follow a divider are still parsed as normal fields — the divider does not consume them. If a step marker like `**Step 1 — Specification:**` is immediately followed by bullet-point fields (`- **Student Action:** ...`, `- **Correct State:** ...`), those bullets are fields, not divider content. Only lines with no `**Label:** content` structure belong in the divider.

### Section IDs

All sections use `s<major>_<minor>_<slug>` — no phase prefix, no letter suffixes.
- Major = top-level spec group number (W.1 → major 1, W.3 → major 3, Section 2 → major 2)
- Minor = sequential interaction counter within that group, starting at 1, **never reused**
- Slug = snake_case purpose phrase

When the spec has sub-sections (e.g. W.3a, W.3b, W.3c), each becomes its own section with a unique minor number — do not append letters.

Examples:
- `Section W.1: Data Collection Game` → `s1_1_data_collection`
- `Section W.2: Symbol Introduction` → `s2_1_symbol_introduction`
- `W.3a: Guide Models First Category` → `s3_1_model_first_category`
- `W.3b: Student Completes Second Category` → `s3_2_student_places_category_b`
- `W.3c: Student Completes Third Category` → `s3_3_student_places_category_c`
- `Section W.4: Bridge to Lesson` → `s4_1_bridge_to_lesson`
- `Section 1.2: Least Votes` → `s1_2_least_votes`

### Tables

If the spec contains a table (e.g. Game Specifications), capture it as a
nested object under the key derived from the table's heading label.

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Entire response must be an array starting with `[` and ending with `]`
- One object per section, in spec order
- Flat — no nested sections arrays
- Use double quotes throughout
- Omit fields that are empty or not present in the spec for that section
- **Escape all double quotes inside string values** — if a field value contains a `"` character (e.g. `"3 columns of 4"`), it must be written as `"3 columns of 4"` in the JSON string



----------------------------------------------------------------------

### Block 3: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>

[
  {
    "id": "s1_1_data_collection",
    "purpose": "Generate personalized data via counting game. Create investment through active participation and Minis context.",
    "hook": "Minis characters appear in animated counting scenario.",
    "game_specifications": {
      "style": "Mario Party-style counting game",
      "categories": 3,
      "values_range": "3-7 per category",
      "duration": "~60 seconds",
      "student_interaction": "Up/down counter to track count"
    },
    "task": "Student participates in counting activity, using up/down counter to record their count for each category.",
    "on_correct": "Let's see if you counted them all. Guide counts visually, revealing correct answer. There were [X] [category A] and [Y] [category B] and [Z] [category C].",
    "design_note": "Student counter attempt is checked by Guide reveal. Ensures all students have correct data regardless of counting accuracy."
  },
  {
    "id": "s2_1_symbol_introduction",
    "purpose": "Give student agency in graph creation. Builds investment in their graph.",
    "visual": "Picture Graphs (Mode 2: Creating). Symbol palette appears (6-8 options). Empty horizontal graph template visible below with 3 category rows. Data from W.1 displayed as reference text.",
    "engagement_anchor": "Choice/Agency (student selects their symbol)",
    "guide": "Let's make a graph with the data."
  },
  {
    "id": "s3_1_model_first_category",
    "purpose": "Guide models placing symbols for category A.",
    "visual": "Picture Graphs (Mode 2: Creating). Empty horizontal picture graph. Selected symbol ready. Key reads Each [symbol] = 1 [item]. W.1 data visible as reference. Data Table not visible.",
    "guide": "Watch how I show our [category A] on the graph. You counted [X] [category A]. So I add [X] [symbols]. One... two... three... [X] [symbols]. Each one means 1 [category A].",
    "scaffolding_note": "System places symbols while guide narrates. No student interaction."
  },
  {
    "id": "s3_2_student_places_category_b",
    "purpose": "Student places symbols for category B.",
    "visual": "Picture Graphs (Mode 2: Creating). Horizontal picture graph. Category A complete (Guide-modeled). Categories B and C empty. Key visible. Data Table not visible.",
    "guide": "Your turn. You counted [Y] [category B]. Add [Y] [symbols]. Click to place them - one for each [category B] you counted.",
    "correct_answer": "[Y] symbols placed",
    "on_correct": "[Y] [symbols]. One for each [category B].",
    "on_incorrect": "Let's count the symbols. We need [Y] — one for each [category B] we counted. Allows retry."
  }
]

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
## 1.6 WARMUP

---

### Purpose

Activate equation-building knowledge from M10 and create curiosity about the difference between clustered equal groups and rectangular arrangements. Students build a complete equation (M10 skill, M9 fluency) and then compare a familiar equal groups image to a new rectangular arrangement of the same items — priming the "array" concept the Lesson will name and formalize.

---

### Parameters

| Element | Specification |
| --- | --- |
| Interactions | 2 meaningful interactions + bridge |
| Active Participation | 2 of 2 require student response |
| Format | Equation Callback (M10 skill) → Visual Comparison (Notice & Wonder) → Bridge |
| Cognitive Load | 20-30% (W.1 is prior skill; W.2 is low-demand noticing) |
| Remediation | Light only |
| Tone | Medium-High energy, curious, building toward "something new about equal groups" |

---

### Constraints

| USE | AVOID |
| --- | --- |
| Session-relative language ("Last time / this time") | Temporal language ("yesterday/today") |
| "Groups of" / "times" / "equals" (M7-M10 owned vocabulary) | "Array" / "row" / "column" (Lesson 1.1-1.2 introduces) |
| "Lined up" / "organized" / "arranged" (informal, primes concept) | "Rectangular arrangement" or any formal geometry language |
| Equal Groups with Pictures (W.1 only) | Equal Groups in any phase after Warmup |
| Equation Builder with full template `[___] × [___] = [___]` (M10 format) | Expression-only mode (Lesson introduces Equation Builder modes) |
| Bags context for W.1 (familiar, clean M10 callback) | New contexts (rows, stacks — M10 Lesson territory; arrays — M11 Lesson) |
| Observable feedback only | Assumed internal states ("You understand equations") |

Opening Hook (15-20 seconds)

* **Visual:** Split screen — both images appear simultaneously. Left: 3 bags with 5 items each (clustered, familiar from M7-M10). Right: The same 15 items arranged in a 3×5 rectangle — no bags, just the items lined up in rows and columns. Both show 15 items, same objects.
* **Guide:** "Same items, two different pictures. What's going on here? Let's start with the one you know."
* **No student action** (curiosity/activation only)
**Engagement Anchor 1:** Curiosity Gap ("Same items, two different pictures" — creates genuine question: why do these look different? What matters about how items are arranged?)

---

### Interaction W.1: Equation Building Callback

* **Purpose:** Activate equation-building skill from M10. Confirm students can build a complete equation from an equal groups visual. Quick success with familiar skill.
* **Visual:** Equal Groups with Pictures: 3 bags with 5 items each. Equation Builder alongside with full equation template: `[___] × [___] = [___]`. Tile palette:  2, `3, 4`, `5`, 6, `8`, 12, 14 `15, 16`.
* **Guide:** "Let's warm up. Check out these bags. Build the equation."
* **Prompt:** "Build the equation to match this picture."
* **Student Action:** Equation Builder Methods C/D (tiles).
* **Correct Answer:** Equation must be `3 × 5 = 15`.
* **On Correct:** "3 times 5 equals 15. You've got it."
* **Remediation:** Pipeline
---

### Interaction W.2: Equal Groups vs. Rectangular Arrangement

* **Purpose:** Present the same quantity (15 items) shown two ways: as the clustered bags from W.1 AND as a rectangular arrangement (3 rows, 5 in each row). Student notices the difference. Creates the curiosity gap that Lesson 1.1 will satisfy.
* **Visual:** Split screen. Left side: The 3 bags of 5 from W.1 remain (clustered equal groups). Right side: The same 15 items from the bags, now arranged in a 3×5 rectangle — no bags, just the items lined up, aligned horizontally and vertically. Same objects, different arrangement.
* **Guide:** "Look at both of these pictures. They both show 15 items — 3 groups of 5. But something looks different about the one on the right. What do you see that's different?"
* **Prompt:** "What's different about the picture on the right? Select one."
* **Student Action:** MC (A: "Everything is lined up" / B: "There are more items" / C: "The groups are bigger" / D: "They're in bags")
* **Correct Answer:** A ("Everything is lined up")
* **On Correct:** "You see it. Everything is lined up. Same groups, but organized so every item has a spot."
* **On Incorrect (B, C, or D):** "Both pictures show 15 items, 3 groups of 5. Look at how the dots on the right are arranged: what's different about their position?"
---

Bridge to Lesson

* **Purpose:** Create anticipation for Lesson without teaching.
* **Visual:** The bags fade from the left side. The 3×5 item arrangement remains, centered. System briefly highlights the horizontal lines (rows), then the vertical lines (columns) — a visual tease without narration naming them.
* **Guide:** "That lined-up arrangement? It has a name, and there's a lot to discover about how it works. Let's find out."
* **No student action.**
**Backbone Departure:** Backbone §1.5 specified Guide names "array," "rows," "columns" in bridge. Departure: Bridge does NOT name these terms. Per Warmup Phase Playbook §4B, formal vocabulary is prohibited in Warmup. All three terms relocated to Lesson (array at 1.1, row/column at 1.2).

---

### Verification Checklist

---
</input>

======================================================================

## Prefill

[

