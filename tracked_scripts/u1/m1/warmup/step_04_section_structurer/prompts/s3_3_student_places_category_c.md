# Prompt: section_structurer
# Generated: 2026-04-02T14:27:24.725118
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 32000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are translating a lesson specification into structured section JSON. Your job is faithful, precise translation: every interaction in the spec becomes a correctly structured section object with the right beats, tools, validators, and scene state. Dialogue is functional. Preserve the pedagogical intent from the spec without embellishment.

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

<input> is a single structured section object produced by starterpack_parser.

It contains key-value fields extracted from the original spec
(visual, guide, prompt, correct_answer, on_correct, on_incorrect, purpose, etc.)
and a `workspace_specs` field: `{ "toys": ["picture_graph", "data_table"], "tools": ["click_category"] }`.

**Canonical names:** `workspace_specs.toys` lists the only valid `tangible_type` values for this section.
`workspace_specs.tools` lists the only valid `tool` values. Use these exact strings verbatim — they have
already been resolved to their canonical forms.

Convert this section object into a single section JSON object following the lesson script schema.
Output only that one section object (not an array).

Scripts are static. Use concrete values throughout. Values are defined
in the spec. Do not invent values; do not use placeholders like [X].

**Dialogue:** carry the spec's dialogue intent directly into the text field.
Keep it clear and functional. Do not add warmth, personality, or flair.
A separate pass handles dialogue enhancement. Do not use em dashes (—).

Include all required phrases from <input>. Avoid all forbidden phrases.

---

## WHAT IS A STEP

A step is a **do-together block**: all beats in a step play together without pausing. The step ends, and the system pauses, when student input is required.

Student input is required when:
1. **Dialogue plays** (animations happen alongside dialogue): the student must act or respond after the guide speaks
2. **A prompt beat**: the student explicitly interacts with a tangible or overlay tool

Everything before that pause belongs in the same step. Beat order within a step:

1. Scene beats (`add`, `show`, `animate`, `update`): things appear or change on screen
2. Dialogue beats: the guide speaks (animations play alongside)
3. Prompt beat: student interacts (only one prompt per step; always the last non-snapshot beat)
4. `current_scene`: snapshot of what is on screen after all beats in this step

---

## SECTION STRUCTURE

```json
{
  "id": "s{group}_{seq}_{slug}",
  "steps": [ [...], [...] ]
}
```

- `id`: copy verbatim from the input section's `id` field. Do not modify or re-derive it.
- `steps`: array of arrays; each inner array is one step (do-together block ending when student input is required)

Every section begins with an empty screen. Everything visible must be put on screen explicitly by `scene` beats in the first step. Nothing carries over from the previous section.

**Transition sections** use `"type": "transition"` on the section object.
They have scene and dialogue beats. No prompts.

---

## BEAT TYPES

### Scene: things happen on screen

```json
{ "type": "scene", "method": "add", "tangible_id": "picture_graph_fruits", "tangible_type": "picture_graph",
  "params": { "mode": "reading", "orientation": "horizontal",
              "categories": ["Apples", "Bananas", "Oranges", "Grapes"],
              "description": "Horizontal picture graph appears. Favorite Fruits data. Each fruit symbol = 1 vote." } }
```
```json
{ "type": "scene", "method": "animate", "tangible_id": "bg_animals",
  "params": { "event": "draw_bar_guideline", "status": "confirmed",
              "description": "Horizontal line draws from top of Monkeys bar to vertical axis, 7 highlights" } }
```
```json
{ "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
  "params": { "highlight_categories": ["Blue", "Yellow"],
              "description": "Blue and Yellow bars highlight." } }
```

Methods: `add` `show` `hide` `animate` `update` `remove`

- Use **`add`** when a tangible appears for the first time. Always include
  `tangible_type` and a `params.description` of what the student sees.
  Include all relevant state fields in `params` (mode, orientation,
  categories, axis range, etc.) drawn from <toy_specs>.
- Use **`animate`** for named animation events: `event` (snake_case),
  `status` (`proposed` = setup in progress / `confirmed` = complete),
  `description` (plain English).
- Use **`update`** when a toy's state changes (highlighting, mode switch,
  template change, button state, expression value, etc.). Always include a
  `params.description` — plain English of what visually changes as a result.
- Use **`show`** / **`hide`** to toggle visibility of a tangible that
  already exists.

For the section-to-section transition (picture graph → bar graph), use
`animate` with `event: "transform_to_bar_graph"` on the picture graph
tangible, then treat subsequent sections as having the bar graph on screen.

### Dialogue: guide speaks

```json
{ "type": "dialogue", "text": "Every part of a graph has a job." }
```
```json
{ "type": "dialogue", "text": "The KEY shows the SCALE." }
```

Translate the spec's dialogue intent directly. Keep it clear and on-point.
Do not embellish. Voice enhancement happens in a later step.

### Prompt: student interacts

```json
{
  "type": "prompt",
  "text": "Click on the category that got the MOST votes.",
  "tool": "click_category",
  "target": "picture_graph_fruits",
  "validator": [ ... ]
}
```

Every prompt requires `tool` and `validator`. The tangible in `target` must
already exist in the scene at this point in the step.

**Tool and target usage:**

| `tool` | `target` | `options` |
|---|---|---|
| `click_category` | tangible ID string | — |
| `click_component` | `"tangible_id.component"` string | — |
| `click_tangible` | array of IDs or `{ "type": "..." }` | — |
| `multiple_choice` | — | array of numbers or strings |
| `multi_select` | — | array of strings |

`target` shapes:
- Single tangible: `"target": "picture_graph_fruits"`
- Specific component: `"target": "picture_graph_animals.key"`
- Multiple tangibles: `"target": ["pg_fruits", "pg_animals"]`
- All of a type: `"target": { "type": "picture_graph" }`

For `multiple_choice`, include the exact options from the spec:
`"tool": "multiple_choice", "options": [5, 6, 7, 8]`

For `multi_select`, include the category names:
`"tool": "multi_select", "options": ["Dogs", "Cats", "Fish", "Birds", "Lizards"]`

### current_scene: snapshot of the resulting scene

**Must be the last beat in every step** (and the last beat in every
validator state's inner step). It is a pure derived snapshot: reflect
only what `scene` beats have established. Tangibles carry forward
within a section — a tangible stays on screen until a `scene` beat
removes or hides it. Never introduce a tangible or state that no
`scene` beat has declared.

```json
{
  "type": "current_scene",
  "elements": [
    {
      "tangible_id": "picture_graph_fruits",
      "description": "Horizontal picture graph. Favorite Fruits data. Apples row highlighted. Data table alongside.",
      "tangible_type": "picture_graph",
      "mode": "reading",
      "orientation": "horizontal",
      "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
    },
    {
      "tangible_id": "data_table",
      "description": "Data table showing Favorite Fruits values.",
      "tangible_type": "data_table"
    }
  ]
}
```

Each element includes:
- `tangible_id`: the instance ID
- `description`: plain English of what's visible and its current state
- `tangible_type`: canonical type from <toy_specs>
- Relevant state fields from <toy_specs> (mode, orientation, categories, etc.)

If the scene is empty at the end of a step, write `"elements": []`.

---

## VALIDATOR STRUCTURE

Define only the correct state. The remediation generator adds incorrect
states later. Always include `"is_correct": true` on every validator state
you generate.

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student clicked Apples, correct, 6 votes",
    "is_correct": true,
    "steps": [
      [
        { "type": "scene", "method": "animate", "tangible_id": "picture_graph_fruits",
          "params": { "event": "highlight_category", "status": "confirmed",
                      "description": "Apples row highlights to confirm selection", "category": "Apples" } },
        { "type": "dialogue", "text": "Apples got the most. 6 people chose it. You read that from the graph." },
        { "type": "current_scene", "elements": [ ... ] }
      ]
    ]
  }
]
```

Validator state `steps` follow the same beat ordering and also end with
`current_scene`. **Scene beats are allowed and expected in correct validator
states whenever a visual change accompanies the feedback.**

**`current_scene` in validator states must follow the same rule as everywhere
else: it only mirrors what `scene` beats have declared. If the correct response
requires no visual change, the `current_scene` must describe the tangibles in
exactly the same state as before — no new adjectives, no "confirmed", no added
state. Do not use the description field to imply a change that no `scene` beat
produced.**

```json
// WRONG — current_scene inventing a visual state:
[
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Red items confirmed as 40." }] }
]

// RIGHT — if no visual change, description is identical to prior state:
[
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Minis counting scene. Red, Blue, Yellow items visible." }] }
]

// RIGHT — if a visual change is needed, declare it with a scene beat first:
[
  { "type": "scene", "method": "animate", "tangible_id": "minis_counting_scene",
    "params": { "event": "mark_counted", "status": "confirmed",
                "description": "Red items highlight as counted, count of 40 appears", "category": "Red" } },
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Minis counting scene. Red items highlighted as counted." }] }
]
```

For `multiple_choice`: `{ "condition": { "selected": 7 } }`

For `multi_select` requiring multiple selections:
```json
{ "condition": { "and": [ { "selected": "Dogs" }, { "selected": "Fish" } ] } }
```

**Any-response-advances** (no wrong answer): `"condition": {}`

---

## TWO-STEP INTERACTIONS

Two-step sections have two separate steps, each ending with `current_scene`.
The correct validator state of step 1 sets up the visual state for step 2
(highlight the next target, display the running total, etc.), then step 2
begins with those scene changes already reflected.

```json
"steps": [
  [
    { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
      "params": { "highlight_categories": ["Yellow", "Red"] } },
    { "type": "dialogue", "text": "Step 1: Find how many chose Yellow or Red in all." },
    { "type": "prompt", "text": "How many liked Yellow or Red in all?",
      "tool": { "name": "multiple_choice", "options": [5, 6, 11, 14] },
      "validator": [
        {
          "condition": { "selected": 11 },
          "description": "Student answered 11, correct",
          "steps": [
            [
              { "type": "dialogue", "text": "11 in all. Yellow has 6, Red has 5. 6 plus 5 equals 11." },
              { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
                "params": { "highlight_categories": ["Green"] } },
              { "type": "current_scene", "elements": [ ... ] }
            ]
          ]
        }
      ]
    },
    { "type": "current_scene", "elements": [ ... ] }
  ],
  [
    { "type": "dialogue", "text": "Step 2: Now compare that total to Green." },
    { "type": "prompt", "text": "How many MORE is 11 than Green's 4?",
      "tool": { "name": "multiple_choice", "options": [4, 7, 11, 15] },
      "validator": [
        {
          "condition": { "selected": 7 },
          "description": "Student answered 7, correct",
          "steps": [
            [
              { "type": "dialogue", "text": "7 more. You used TWO steps: first added, then subtracted to compare." },
              { "type": "current_scene", "elements": [ ... ] }
            ]
          ]
        }
      ]
    },
    { "type": "current_scene", "elements": [ ... ] }
  ]
]
```

---

## TANGIBLE IDs

| Visual described | ID convention | Examples |
|---|---|---|
| Picture graph | `picture_graph_{slug}` | `picture_graph_fruits`, `picture_graph_animals`, `picture_graph_pets` |
| Bar graph | `bar_graph_{slug}` | `bar_graph_animals`, `bar_graph_books`, `bar_graph_colors` |
| Data table | `data_table` | `data_table` |

Use the same ID consistently. When the spec says "NEW graph," assign a new ID.
`tangible_type` must match the canonical name in <toy_specs> exactly.

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Output a single section object starting with `{` and ending with `}`
- Use double quotes throughout



----------------------------------------------------------------------

### Block 4: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>

{
    "id": "s1_1_most_votes",
    "steps": [
      [
        {
          "type": "scene",
          "method": "add",
          "tangible_id": "picture_graph_fruits",
          "tangible_type": "picture_graph",
          "params": {
            "mode": "reading",
            "orientation": "horizontal",
            "categories": ["Apples", "Bananas", "Oranges", "Grapes"],
            "description": "Horizontal picture graph appears. Favorite Fruits data. Apples=6, Bananas=4, Oranges=5, Grapes=3. Key: each fruit symbol = 1 vote."
          }
        },
        {
          "type": "scene",
          "method": "add",
          "tangible_id": "data_table",
          "tangible_type": "data_table",
          "params": {
            "description": "Data table appears alongside graph, showing same Favorite Fruits values."
          }
        },
        {
          "type": "dialogue",
          "text": "Now let's read some other graphs. Every part gives us information to READ. Look at this Favorite Fruits graph."
        },
        {
          "type": "prompt",
          "text": "Click on the category that got the MOST votes.",
          "tool": { "name": "click_category", "tangible_id": "picture_graph_fruits" },
          "validator": [
            {
              "condition": { "selected": "Apples" },
              "description": "Student clicked Apples, correct, 6 votes",
              "is_correct": true,
              "steps": [
                [
                  { "type": "dialogue", "text": "Apples got the most votes: 6." },
                  {
                    "type": "current_scene",
                    "elements": [
                      {
                        "tangible_id": "picture_graph_fruits",
                        "description": "Horizontal picture graph. Apples row highlighted. Favorite Fruits data.",
                        "tangible_type": "picture_graph",
                        "mode": "reading",
                        "orientation": "horizontal",
                        "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
                      },
                      {
                        "tangible_id": "data_table",
                        "description": "Data table showing Favorite Fruits values.",
                        "tangible_type": "data_table"
                      }
                    ]
                  }
                ]
              ]
            }
          ]
        },
        {
          "type": "current_scene",
          "elements": [
            {
              "tangible_id": "picture_graph_fruits",
              "description": "Horizontal picture graph in reading mode. Favorite Fruits data. click_category tool active.",
              "tangible_type": "picture_graph",
              "mode": "reading",
              "orientation": "horizontal",
              "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
            },
            {
              "tangible_id": "data_table",
              "description": "Data table showing Favorite Fruits values alongside the graph.",
              "tangible_type": "data_table"
            }
          ]
        }
      ]
    ]
  }
}

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
{
  "id": "s3_3_student_places_category_c",
  "purpose": "Student completes third category.",
  "visual": "Picture Graphs (Mode 2: Creating). Horizontal picture graph. Categories A and B complete. Category C empty. Key visible. Data Table not visible.",
  "guide": "Now show your [category C]. You counted [Z]. Click to add [Z] [symbols].",
  "task": "Student clicks to add symbols.",
  "correct_answer": "[Z] symbols placed",
  "on_correct": "Right. [Z] [symbols]. You made a picture graph!",
  "on_incorrect": "Count the [symbols]. You need [Z] — one for each [category C]. System allows retry.",
  "workspace_specs": {
    "toys": [
      "data_table",
      "picture_graph"
    ],
    "tools": []
  }
}
</input>

======================================================================

## Prefill

{

