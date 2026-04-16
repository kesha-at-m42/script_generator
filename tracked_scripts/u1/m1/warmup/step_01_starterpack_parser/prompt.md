# Prompt: starterpack_parser
# Generated: 2026-04-02T14:26:26.506222
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

### Block 2: Reference Doc (glossary.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: glossary.md

<glossary>
# Unit 1 — Glossary

This document is the authoritative reference for all vocabulary used in lesson specs and generated JSON across Unit 1.

---

## Core Concepts

### Toy
A **toy** is a visual, interactive object placed on screen. Toys are the tangible elements students see and work with. They have state (mode, orientation, values, etc.) and can be added, updated, animated, or removed across a lesson.

### Tool
A **tool** is an interaction pattern — the mechanism by which a student acts on a toy. A tool defines *how* the student interacts, not *what* they interact with. Tools appear in `prompt` beats and always have a corresponding `validator`.

---

## Canonical Toys

These are the only valid `tangible_type` values. Do not invent new types.

| `tangible_type` | Description | Spec status |
|---|---|---|
| `picture_graph` | Horizontal or vertical graph using symbols to represent data. Supports reading and creating modes. | Fully specced |
| `bar_graph` | Horizontal or vertical bar graph. Supports reading and creating modes. | Fully specced |
| `data_table` | Table showing category names and their values alongside a graph. | Fully specced |
| `equation_builder` | Interactive equation construction tool. | Fully specced — not yet used in M1–M6 |
| `data_collection_game` | Animated counting game used in warmups to generate class data. Replaces `counting_game`, `interactive_game`. | Needs spec |
| `sorting_area` | Workspace for drag-to-sort activities. | Needs spec |
| `word_problem_area` | Container that composes a text stem, optional visual support, and a hosted response mechanism into a problem-solving interaction. Hosts other toys (bar graphs, arrays, equal groups) and response components (multiple choice, dropdown_fillin, equation builder). | Initial Spec Draft |
| `dropdown_fillin` | Sentence-frame response widget with one or more inline fill blanks, each linked to an option palette via a shared icon indicator. | Initial Spec Draft |
| `image` | Static image displayed for real-world connection or context. | Needs spec |
| `equal_groups` | Visual representation of multiplication through equal groups — clusters of pictures or dots with optional containers. Supports highlighting, counting animations, and connection lines. | UX in Process |
| `arrays` | Rectangular grid of objects or dots organized in rows and columns. Supports toggling between row and column interpretations. Progresses from concrete objects through mixed to abstract dot grids. **Mode: creating** — Add Row / Add Column button interface for student-constructed arrays (M11+). | Ready for UX |

**Common spec phrases** — natural language used in lesson specs that maps to canonical toy names:

| Spec phrase | Canonical name |
|---|---|
| picture graph | `picture_graph` |
| bar graph | `bar_graph` |
| data table | `data_table` |
| equation builder | `equation_builder` |
| arrays | `arrays` |
| equal groups | `equal_groups` |
| drop down | `dropdown_fillin` |
| fill-in-the-blank | `dropdown_fillin` |
| fill in the blank | `dropdown_fillin` |
| word problem | `word_problem_area` |

**Spec aliases** — renamed or superseded terms; flag these if they appear in a spec:

| Spec term | Canonical name |
|---|---|
| `counting_game` | `data_collection_game` |
| `interactive_game` | `data_collection_game` |
| `word_problems` | `word_problem_area` |
| `animation` | — (not a toy; use `animate` scene beats) |
| `animation_canvas` | — (not a toy; use `animate` scene beats) |

---

## Canonical Tools

These are the only valid `tool` values in a `prompt` beat.

### Reading / Identification Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_category` | Student clicks a category row or bar to identify it | `picture_graph`, `bar_graph` | `{ "selected": "CategoryName" }` |
| `click_component` | Student clicks a named structural part of a toy (key, title, axis, label) | `picture_graph`, `bar_graph` | `{ "selected": "component_name" }` |
| `click_tangible` | Student clicks on one or more whole toys | any | `{ "selected": "tangible_id" }` or `{ "selected": ["id1", "id2"] }` |

### Answer / Selection Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `multiple_choice` | Student picks one answer from a fixed list | standalone, `word_problem_area` | `{ "selected": value }` |
| `multi_select` | Student picks multiple items from a list | standalone | `{ "selected": ["A", "B"] }` |
| `select_fill_option` | Student selects an option from a palette to fill a blank in a sentence frame | `dropdown_fillin` | `{ "selected": "option_text" }` |

### Creating / Building Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_to_place` | Student clicks to place symbols one at a time on a picture graph | `picture_graph` (mode: creating) | `{ "symbols_placed": 3 }` |
| `click_to_set_height` | Student clicks or drags to set a bar to a specific height | `bar_graph` (mode: creating) | `{ "bar_height": 30 }` |
| `add_row` | Student presses Add Row button to append a row to an array under construction | `arrays` (mode: creating) | `{ "rows": 3 }` |
| `add_column` | Student presses Add Column button to append a column to an array under construction | `arrays` (mode: creating) | `{ "columns": 2 }` |


### Drag Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `drag_to_sort` | Student drags items into categorized drop zones | `sorting_area` | `{ "placed": { "zone_id": ["item_id"] } }` — needs spec |

### Scale Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_scale_button` | Student selects a scale option (1, 2, 5, or 10) from the scale selector on a bar graph (M5+) | `bar_graph` | `{ "selected": 2 }` (the scale value chosen) |

**Spec aliases** — renamed or superseded terms; flag these if they appear in a spec:

| Spec term | Canonical name |
|---|---|
| `click_to_set_bars` | `click_to_set_height` |
| `bar_graph_creator` | `click_to_set_height` |
| `click_place_symbols` | `click_to_place` |
| `explore_scales` | `click_scale_button` |

---

## Section and Scene Model

### Section
A **section** is a self-contained interaction unit. Every section begins with a completely fresh scene — no toys, no state, nothing from any previous section. All toys visible in a section must be explicitly declared by `add` scene beats in the first step of that section.

### Workspace
The **workspace** is the set of toys on screen at any point within a section. A section's workspace is fully declared at the start using `add` beats. Within a section, `animate` and `update` beats modify what is already there.

### Scene beats vs Animation beats
- **Setup beats** (`add`, `show`): place toys on screen at section start. Always required — a toy cannot be referenced before it is added.
- **Animation beats** (`animate`, `update`, `hide`, `remove`): modify the state of toys already on screen. These are used within a section after the workspace is established.

### Carry-over (incorrect pattern)
A section that assumes a toy from a previous section is still on screen is **incorrect**. Every section must re-declare all toys it uses, even if the spec says "same graph as before." Carry-over is a spec shorthand, not an instruction to skip `add` beats.

Sections flagged with `"workspace_carry_over": true` in `workspace_specs` were detected as likely assuming carry-over from the spec language (e.g. "Same graph", "Same visual"). These must be reviewed to ensure the section fully re-declares its workspace.

---

## Key Distinction: Tool vs Scene Beat

**Prompt beats** use `tool` — this is a student action.
**Scene beats** use `method` (`add`, `update`, `animate`, `show`, `hide`, `remove`) — these are system actions.

Highlighting, animating, and revealing are always **scene beats**, never tools. Do not use `highlight` or `animate` as a tool value.

</glossary>

----------------------------------------------------------------------

### Block 3: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

Parse the markdown spec in <input> into a flat array of section objects.

One section object per interaction. Sub-sections (e.g. W.3a, W.3b, W.3c)
become separate section objects — do not nest them.

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

If a label appears that is not in this table, still include it — use its
snake_case form as the key. Do not drop any field from the spec.

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



----------------------------------------------------------------------

### Block 4: Output Schema
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
## **1.6 WARMUP (3-4 minutes)**

**Detail Level:** Structure \+ parameters (AI writes dialogue)

### **Purpose**

Activate prior knowledge of data collection and graphing from Grade 2\. Build ownership by having students create a graph with THEIR collected data before the Lesson focuses on interpretation.

### **Parameters**

| Element | Specification |
| :---- | :---- |
| Interactions | 3 meaningful interactions \+ bridge |
| Format | Data Collection Game → Symbol Introduction → Graph Creation |
| Cognitive Load | 20-30% (light, accessible) |
| Remediation | Light only |
| Tone | Medium-High energy, playful, inviting |
| Engagement Anchors | Narrative Setup (Minis), Personalization (their data), Anticipation (graph about to be built) |

### **Constraints**

| USE | AVOID |
| :---- | :---- |
| Informal language ("Let's count," "Check this out") | Formal phrasing ("Observe the following") |
| Observable acknowledgments ("You counted 5") | Assumed states ("You thought carefully") |
| 2 categories only | 3+ categories |
| Values 3-7 per category | Values outside range |

---

### **Warmup Type Rationale**

**Standard Playbook Types:** Binary Choice, WODB, Number Talk, Notice & Wonder, Estimation 180, Visual Patterns, Mystery Reveal

**M1 Deviation:** Data Collection Game \+ Graph Creation

**Why this serves the concept:**

- Unit 1 is about DATA—students need to experience collecting data before interpreting graphs
- OUR classroom version has students gather class data collaboratively; Data Collection Game provides equivalent "their data" experience in digital 1:1 format
- Graph creation in Warmup (not Lesson) creates ownership and investment
- Follows Playbook PRINCIPLES (low cognitive load, engagement anchors, judgment tasks, bridge) while adapting STRUCTURE for data unit context

**Test:** If we removed this Warmup, would students lose mathematical preparation for Lesson? YES—they would miss the foundational experience that graphs represent real collected information, not just pictures.

---

**Section W.1: Data Collection Game**

* **Purpose:** Generate personalized data. Create investment through active participation and Minis context.
* **Hook (first 15-20 seconds):**
  * **Visual:** Minis characters appear in animated counting scenario.
  * **Guide:** Brief framing for counting task.
* **Engagement Anchor:** Narrative Setup (Minis context creates investment)
* **Game Specifications (for script writer):**

| Element | Specification |
| :---- | :---- |
| Style | Mario Party-style counting game |
| Categories | 3 (design determines what's being counted) |
| Values | 3-7 per category |
| Duration | \~60 seconds |
| Student Interaction | Up/down counter to track count |

* **Task:** Student participates in counting activity, using up/down counter to record their count for each category.
* **On Complete \- Guide Reveal:**
  * **Guide:** "Let's see if you counted them all."
  * Guide counts visually (animation shows count), revealing correct answer
  * **Guide:** "There were \[X\] \[category A\] and \[Y\] \[category B\] and \[Z\] \[category C\]."
  * These revealed values become the data for graph creation

**Design Note:** Student's counter attempt is checked by Guide reveal. This ensures all students have correct data for graph creation regardless of counting accuracy. The counting game builds investment; the reveal ensures accurate data.

---

### **Interaction W.2: Symbol Introduction**

**Purpose:** Establish that ONE symbol represents all data on this graph; introduce "each symbol = 1 item" rule.

**Engagement Anchor:** Anticipation (graph is about to be built)

**Visual:**

- Data from W.1 displayed as reference text: "You counted [X] [category A], [Y] [category B], and [Z] [category C]."
- Empty horizontal picture graph template appears with 3 category rows
- Symbol pre-assigned by system (e.g., stars) and visible in key area

**Guide [verbal]:** "Let's make a picture graph with your data. We'll use stars. Each star shows 1 item."

**No student interaction** — proceeds directly to W.3.

**Design Note:** Symbol is system-assigned (no student selection). This maintains the pedagogical point: ONE symbol type for entire graph, KEY shows what symbols represent. Student agency comes from graph creation in W.3, not symbol choice.

---

**Section W.3: Graph Creation (Worked Example)**

**Purpose:** Model graph creation before student attempts. Applies "each symbol \= 1 item" rule from W.2.

**Engagement Anchor:** Cognitive Apprenticeship (I do → You do → You do)

**W.3a: Guide Models First Category**

- **Visual: Picture Graphs (Mode 2: Creating).** Empty horizontal picture graph. Selected symbol ready. Key reads "Each \[symbol\] \= 1 \[item\]." W.1 data visible as reference. Data Table not visible.
- **Guide:** "Watch how I show our \[category A\] on the graph."
- **System:** Symbols appear one at a time as Guide narrates
- **Guide:** "You counted \[X\] \[category A\]. So I add \[X\] \[symbols\]. One... two... three..." *(counts aloud to X)*
- **Guide:** "\[X\] \[symbols\]. Each one means 1 \[category A\]."

**W.3b: Student Completes Second Category**

- **Visual: Picture Graphs (Mode 2: Creating).** Horizontal picture graph. Category A complete (Guide-modeled). Categories B and C empty. Key visible. Data Table not visible.
- **Guide:** "Your turn. You counted \[Y\] \[category B\]. Add \[Y\] \[symbols\]. Click to place them \- one for each \[category B\] you counted."
- **Interaction:** Student clicks to add symbols
- **On Correct (\[Y\] symbols):**
  - Guide: "\[Y\] \[symbols\]. One for each \[category B\]."
- **On Incorrect (wrong count):**
  - Guide: "Let's count the \[symbols\]. We need \[Y\] — one for each \[category B\] we counted."
  - System: Allows retry

**W.3c: Student Completes Third Category**

- **Visual: Picture Graphs (Mode 2: Creating).** Horizontal picture graph. Categories A and B complete. Category C empty. Key visible. Data Table not visible.
- **Guide:** "Now show your \[category C\]. You counted \[Z\]. Click to add \[Z\] \[symbols\]."
- **Interaction:** Student clicks to add symbols
- **On Correct (\[Z\] symbols):**
  - Guide: "Right. \[Z\] \[symbols\]. You made a picture graph\!"
- **On Incorrect (wrong count):**
  - Guide: "Count the \[symbols\]. You need \[Z\] — one for each \[category C\]."
  - System: Allows retry

**Scaffolding Note:** Support fades across categories — full narration (A) → prompted (B) → lighter prompt (C).

---

**Section W.4: Bridge to Lesson**

* **Purpose:** Create anticipation for Lesson without teaching. Frame the shift from making to reading.
* **Visual: Picture Graphs (Mode 2: Creating).** Student's completed 1:1 horizontal picture graph (3 categories). Key visible. Data Table not visible.
* **Guide:** "You made a PICTURE GRAPH with your data. "Graphs can be used to show us all types of data\! Ready to learn more about them?"

---

### **Verification Checklist**

**Structure:**

- [ ] Hook appears in first 15-20 seconds (Minis appear with items)
- [ ] 2+ engagement anchors from approved types (Narrative, Personalization, Choice)
- [ ] 2+ meaningful interactions requiring judgment (counting, graph creation)
- [ ] 1+ task requires thinking beyond clicking (placement decisions)
- [ ] Clear bridge to Lesson creates anticipation without teaching
- [ ] "Picture graph" named explicitly in bridge
- [ ] Total time 3-4 minutes

**Constraints:**

- [ ] Zero formal vocabulary introduced
- [ ] Maximum 3 categories (not 4+)
- [ ] Values in 3-7 range per category
- [ ] Maximum 2 visual states (game scene → graph template)
- [ ] Cognitive load feels light (20-30%)

</input>

======================================================================

## Prefill

[

