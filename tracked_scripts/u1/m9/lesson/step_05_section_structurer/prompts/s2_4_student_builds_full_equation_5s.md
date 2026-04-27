# Prompt: section_structurer
# Generated: 2026-04-27T10:57:15.250866
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
| `picture_graph` | Horizontal or vertical graph using symbols to represent data. Supports reading and building modes. | Fully specced |
| `bar_graph` | Horizontal or vertical bar graph. Supports reading and building modes. | Fully specced |
| `data_table` | Table showing category names and their values alongside a graph. | Fully specced |
| `equation_builder` | Interactive equation construction tool — student fills in blanks using `place_tile`. Described as an array of strings: `__` for a blank, `x` for multiplication symbol, plain words for labels. Variants: equation style and word style — both use the same string array format. Always uses `place_tile` tool. | Fully specced — not yet used in M1–M6 |
| `equation` | Static, read-only equation displayed on screen. Same string array format as `equation_builder` but not interactive — no tool. | UX Done |
| `multiple_choice_options` | Answer options panel displayed alongside `arrays`. Student answers a multiple choice question *about* the array. Always uses `multiple_choice` tool. | UX Done |
| `data_collection_game` | Animated counting game used in warmups to generate class data. Replaces `counting_game`, `interactive_game`. | Needs spec |
| `sorting_area` | Workspace for drag-to-sort activities. | Needs spec |
| `word_problem_area` | Container that composes a text stem, optional visual support, and a hosted response mechanism into a problem-solving interaction. Hosts other toys (bar graphs, arrays, equal groups) and response components (multiple choice, dropdown_fillin, equation builder). | Initial Spec Draft |
| `dropdown_fillin` | Sentence-frame response widget with one or more inline fill blanks, each linked to an option palette via a shared icon indicator. | Initial Spec Draft |
| `image` | Static image displayed for real-world connection or context. | Needs spec |
| `equal_groups` | Visual representation of multiplication through equal groups — clusters of pictures or dots with optional containers. Supports highlighting, counting animations, and connection lines. Modes: `"reading"` (pre-built groups, student identifies structure) and `"building"` (student sets container count and items per container). | UX in Process |
| `arrays` | Rectangular grid of objects or dots organized in rows and columns. Covers both read and build modes — mode is determined by which toys are present on screen. Modes: `"reading"` (displayed alone or alongside `multiple_choice_options` or `equation_builder`) and `"building"` (always paired with `row_builder` or `column_builder`). See `toy_specs/arrays.md`. | UX Done |
| `row_builder` | Bottom panel for building by rows. Contains two button pairs: Row +/− and Items per Row +/−. Mutually exclusive with `column_builder`. | UX Done |
| `column_builder` | Bottom panel for building by columns. Contains two button pairs: Column +/− and Items per Column +/−. Mutually exclusive with `row_builder`. | UX Done |

**Common spec phrases** — natural language used in lesson specs that maps to canonical toy names:

| Spec phrase | Canonical name |
|---|---|
| picture graph | `picture_graph` |
| bar graph | `bar_graph` |
| data table | `data_table` |
| equation builder | `equation_builder` |
| arrays | `array` |
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
| `select_fill_option` | Student selects an option from a palette to fill a blank in a sentence frame. Dropdowns only exist in the `dropdown_fillin` toy — if the section does not use `dropdown_fillin`, this tool never applies. | `dropdown_fillin` | `{ "selected": "option_text" }` |

### Creating / Building Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_to_place` | Student clicks to place symbols one at a time on a picture graph | `picture_graph` (mode: building) | `{ "symbols_placed": 3 }` |
| `click_to_set_height` | Student clicks or drags to set a bar to a specific height | `bar_graph` (mode: building) | `{ "bar_height": 30 }` |
| `add_row` | Student presses Row + button to append a row | `row_builder` | `{ "rows": 3 }` |
| `add_item_per_row` | Student presses Items per Row + button to add an item to each row | `row_builder` | `{ "items_per_row": 4 }` |
| `add_row_and_item_per_row` | Both Row + and Items per Row + are active; student may tap either | `row_builder` | `{ "rows": 3, "items_per_row": 4 }` |
| `add_column` | Student presses Column + button to append a column | `column_builder` | `{ "columns": 2 }` |
| `add_item_per_column` | Student presses Items per Column + button to add an item to each column | `column_builder` | `{ "items_per_column": 3 }` |
| `add_column_and_item_per_column` | Both Column + and Items per Column + are active; student may tap either | `column_builder` | `{ "columns": 2, "items_per_column": 3 }` |


### Equal Groups Building Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `set_container_count` | Student sets the number of groups (containers) | `equal_groups` (mode: building) | `{ "container_count": 3 }` |
| `set_items_per_container` | Student sets the number of items in each group | `equal_groups` (mode: building) | `{ "items_per_container": 4 }` |

These two tools are always used in sequence within a building section: `set_container_count` first (How many groups?), then `set_items_per_container` (How many in each?).

### Drag Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `drag_to_sort` | Student drags items into categorized drop zones | `sorting_area` | `{ "placed": { "zone_id": ["item_id"] } }` — needs spec |
| `place_tile` | Student drags or clicks a numbered tile from the palette into an expression/equation slot | `equation_builder` | `{ "placed": { "groups": 4, "items": 2 } }` — only student-filled slots included; keys are `groups`, `items`, `total`. Dynamic forms: `{ "product_equals": 20 }` (any factor pair with that product); `{ "product_equals": 20, "matches_step": "section_id" }` (product check + values must match placed output of the named prior section) |

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
| `drag_tile` | `place_tile` |
| `equation builder methods c/d` | `place_tile` |
| `methods c/d` | `place_tile` |

---

## Canonical Toy Modes

The `mode` field on a toy must use one of these exact string values. Do not invent synonyms.

| Toy | Mode value | Meaning |
|---|---|---|
| `picture_graph` | `"reading"` | Pre-built graph; student reads/identifies |
| `picture_graph` | `"building"` | Student places symbols to build the graph |
| `bar_graph` | `"reading"` | Pre-built graph; student reads/identifies |
| `bar_graph` | `"building"` | Student adjusts bar heights |
| `arrays` | `"reading"` | Pre-built array; student reads/identifies (alone, with `multiple_choice_options`, or with `equation_builder`) |
| `arrays` | `"building"` | Student constructs the array (always paired with `row_builder` or `column_builder`) |
| `equal_groups` | `"reading"` | Pre-built groups; student identifies structure |
| `equal_groups` | `"building"` | Student sets container count and items per container |

**Non-canonical mode values to avoid:**

| Seen in outputs | Use instead |
|---|---|
| `"build"` | `"building"` |
| `"read"` | `"reading"` |
| `"create"` | `"building"` |
| `"creating"` | `"building"` |

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

## Array Template Screens

Valid toy combinations for array-based sections. No other combinations are permitted.

| Template | Toys | Tool(s) |
|---|---|---|
| array-read-mc | `arrays` + `multiple_choice_options` | `multiple_choice` — student answers MCQ about the array |
| array-read-eq | `arrays` + `equation_builder` | `place_tile` — student describes the array using the equation |
| array-build-rows | `arrays` + `row_builder` | `add_row`, `add_item_per_row`, or `add_row_and_item_per_row` |
| array-build-cols | `arrays` + `column_builder` | `add_column`, `add_item_per_column`, or `add_column_and_item_per_column` |
| array-build-eq | `arrays` + `equation_builder` | `place_tile` — student drags factor tiles into equation slots; array updates to match |

**Coupling constraints:**
- `row_builder` and `column_builder` are mutually exclusive — never on the same screen
- `row_builder` / `column_builder` always require `arrays`
- `equation_builder`, `row_builder`, and `column_builder` are mutually exclusive — only one build mechanism per screen
- `multiple_choice_options` always requires `arrays` and the `multiple_choice` tool

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

It may contain a `prior_section_summaries` field — a running document summarising every section processed so far, newest at the bottom. Use it to:
- Resolve under-specified visual references ("Same data", "Full data visible", "remains visible", "picture graph from Section 1") — look up the most recent matching tangible in the summaries and use its exact dataset, categories, values, scale, and orientation.
- Understand what concepts and vocabulary have already been introduced so you don't contradict prior content.
- Know the current screen state so `add`, `update`, and `remove` beats are consistent with what has been established.
When `prior_section_summaries` is absent (first section), treat the screen as empty.

It contains key-value fields extracted from the original spec
(visual, guide, prompt, correct_answer, on_correct, on_incorrect, purpose, etc.)
and a `workspace_specs` field: `{ "toys": ["picture_graph", "data_table"], "tools": ["click_category"] }`.

**Map all fields by meaning, not by name.** The input object may present
information in various field names and formats — interpret every field and
map it to the appropriate schema context:
- `student_action: "MC (2, 6, 8, 12)"` → `multiple_choice` prompt with
  options `[2, 6, 8, 12]`
- `student_action: "Multi-select: Dogs, Cats, Fish"` → `multi_select` with
  those options
- `guide_2`, `prompt_2`, `on_correct_2` etc. → a second step in the section. When `prompt_2` (or any numbered prompt field) exists without a corresponding `guide_2`, you must still generate a dialogue beat before that prompt — infer it from `visual_N`, the prompt text itself, or surrounding context. A missing `guide_N` is never a reason to omit the required dialogue beat.
- `divider` fields are contextual labels only — they describe what is happening at that point in the spec. Do not use them to determine step boundaries and do not output them as beats. Use the surrounding prompt, student_action, and guide fields to determine structure.
- A `student_action` field that contains two actions joined by "and" (e.g. "selects X or Y and fills two number slots") represents two sequential prompts — split them into separate steps
- Inline annotations in any text field (e.g. `[System highlights rows
  sequentially]`, `[3 tile places into first slot]`) → `scene` beats at
  that point in the step
- `task` describing a build/click/drag action → infer the tool type from it
- Any beat in the outer `beats` array that only applies on a specific branch gets a `"branch_name": "<condition_id>"` field — referencing the `condition_id` of the validator state that established the branch (e.g. `"branch_name": "selected_rows"`). Omit the field when the beat is unconditional. When pushed to Notion, beats with the same `branch_name` are grouped under an H3 heading `🔀 <branch_name>`.
- **Once a branch is established, output ALL beats for one branch consecutively before writing ANY beat for the other branch.** Do not interleave. Wrong: rows-step-1, cols-step-1, rows-step-2. Correct: rows-step-1, rows-step-2 … then cols-step-1, cols-step-2. Complete one branch entirely, then the other.
- Fields whose value begins with a `[branch_name]` or `(qualifier)` prefix — e.g. `visual_2: "[selected_rows] Rows buttons activate."`, `on_correct_2: "(example: 4 × 5 = 20) "4 times 5...""` — carry inline context about which branch or condition the content belongs to. Strip the prefix when using the content; use `[branch_name]` values to assign `branch_name` to the corresponding beats, and use `(qualifier)` values to generate named validator states with `condition_id` matching the qualifier.

Do not ignore fields because their name is unfamiliar. Read every field in
the input object and decide where it belongs in the output structure.

**Canonical names:** `workspace_specs.toys` lists the only valid `tangible_type` values for this section.
`workspace_specs.tools` lists the only valid `tool` values. Use these exact strings verbatim — they have already been resolved to their canonical forms.

When `workspace_specs.tools` contains multiple tools, the section has multiple prompt beats — one per tool. Map each tool to the step it belongs to using the dividers and numbered fields as context.


Convert this section object into a single section JSON object following the lesson script schema.
Output only that one section object (not an array).

Scripts are static. Use concrete values throughout. Values are defined
in the spec. Do not invent values; do not use placeholders like [X].

**Dialogue:** carry the spec's dialogue intent directly into the text field.
Keep it clear and functional. Do not add warmth, personality, or flair.
A separate pass handles dialogue enhancement. Do not use em dashes (—).

Include all required phrases from <input>. Avoid all forbidden phrases.

---

## WHAT IS A STEP GROUP

A step group is one **teaching moment** — one idea, paired with its visual. Everything in the group serves that moment. The student presses Next once to advance past it.

**Scene and dialogue are partners.** A step is usually the guide teaching something using a visual: the scene beat shows what appears or changes on screen; the dialogue beat says what it means. They co-narrate the same moment and belong together in the same step.

**Scene beat ordering depends on method.** `add`, `update`, `show`, and `hide` beats set up state — place them before the dialogue they establish. `animate` beats play concurrently with dialogue — place them in the same step alongside the dialogue they accompany.

**Dialogue is animation-agnostic.** Scene beats own the visual description — what highlights, pulses, or animates. Guide dialogue stays at the level of meaning. Prefer dialogue that says what something means ("That bar shows the total for the week.") over dialogue that narrates the animation ("notice the highlighted bar"). Where the spec dialogue already does this well, keep it.

A step group contains at most one prompt beat, always contains dialogue, and always ends with `current_scene`. Multiple dialogue beats are allowed — they collapse into a single block of text for the student.

**Step sizing** — the question for every step boundary is: is this one teaching moment, or two?

- **One moment: keep together.** When beats co-narrate the same thing — a visual and the narration explaining it, an animation and the dialogue it plays alongside — they belong in one step. Splitting them breaks the student's understanding of what's being shown.
- **Two moments: split.** When the section is naming something, introducing a property, or making a distinct conceptual point, each idea belongs in its own step. Two unrelated explanations in one step mean the student is absorbing different things before they can advance.
- **Scene setup is never its own step.** Setup beats (`add`, `update`, `show`, `hide`) always belong to the step whose dialogue they establish. Never end a step immediately after setup beats with no dialogue.

The same principle drives both: if removing one beat would leave the other incomplete or out of context, they belong together. If each beat could stand on its own as a distinct moment, split them.

Valid step group compositions:
- Scene setup beat(s) → Dialogue → `current_scene`  ← default
- Scene setup beat(s) → Dialogue → Prompt → `current_scene`
- Dialogue → Prompt → `current_scene`

**Every prompt is preceded by a dialogue beat.** Dialogue is heard; prompt text is read. The dialogue beat is the guide's narrated setup — the same CTA in spoken register. The prompt text is the concise written instruction the student reads on screen. Both are required; they are not redundant. Consequently, a `student_action` that describes multiple interactions means multiple step groups — one per interaction, each with its own preceding dialogue and ending with `current_scene`. When interactions are closely related, additional dialogue beats may appear within a step group to narrate the transition between them.

`current_scene` is always the last beat in every step group. All step groups are in the flat `beats` array — do not wrap them in a `steps` array.

---

## SECTION STRUCTURE

```json
{
  "id": "s{group}_{seq}_{slug}",
  "beats": [ ... ]
}
```

- `id`: copy verbatim from the input section's `id` field. Do not modify or re-derive it.
- `beats`: flat array of all beats for the entire section. Do **not** nest beats inside steps — put everything in one flat list.

Step groups are implicit: a new step begins after each `current_scene` beat. Every step group ends with a `current_scene` beat.

Every section begins with an empty screen. Everything visible must be put on screen explicitly by `scene` beats in the first step group. Nothing carries over from the previous section.

**Visual clearing phrases** — phrases like "Clean transition", "Practice clears", "Lesson graph clears", "Equation Builder clears", "Lesson visualization fades", and any similar `[thing] clears/fades` form in a `visual` field describe the empty starting state of the section, not an animation to generate. Do **not** create any `scene` or `animate` beat for these. The section already starts with an empty screen; these phrases confirm that and carry no actionable information.

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

Never use letter labels (A, B, C) in dialogue even if the spec uses them as identifiers. Those labels are system-level placeholders; the visual narration handles what they refer to. Use the actual name, value, or a plain description instead.

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

For all other tools (`place_tile`, `add_row`, `add_column`, `select_fill_option`, etc.) — refer to the **Canonical Tools** table in <glossary.md> for the correct `target` and validator condition shape.

`target` shapes:
- Single tangible: `"target": "picture_graph_fruits"`
- Specific component: `"target": "picture_graph_animals.key"`
- Multiple tangibles: `"target": ["pg_fruits", "pg_animals"]`
- All of a type: `"target": { "type": "picture_graph" }`

For `multiple_choice`, include the exact options from the spec:
`"tool": "multiple_choice", "options": [5, 6, 7, 8]`

**Options must be taken verbatim from the `student_action` field.** If `student_action` does not list options explicitly, draw them only from values that appear in the spec's dataset. Never invent, approximate, or calculate distractor values — even plausible-looking ones. An invented distractor may violate module-level constraints (e.g. "all values are multiples of 5") that the spec author enforced but did not repeat in every field.

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

Every validator state requires a `condition_id` — a short, semantic, stable
identifier (e.g. `"correct"`, `"selected_rows"`, `"placed_3x4"`). Use snake_case.

```json
"validator": [
  {
    "condition_id": "correct",
    "condition": { "selected": "Apples" },
    "description": "Student clicked Apples, correct, 6 votes",
    "is_correct": true,
    "beats": [
      { "type": "scene", "method": "animate", "tangible_id": "picture_graph_fruits",
        "params": { "event": "highlight_category", "status": "confirmed",
                    "description": "Apples row highlights to confirm selection.", "category": "Apples" } },
      { "type": "dialogue", "text": "Apples got the most. 6 people chose it. You read that from the graph." }
    ]
  }
]
```

**Validator beats are feedback only.** They contain the immediate response to
the student's answer: a confirmation scene animation and/or dialogue. They do
NOT contain `current_scene`, do NOT set up the next step's scene, and do NOT
advance the interaction. After the validator fires, execution returns to the
outer beats and the next outer beat runs.

This means:
- Scene setup for the NEXT step goes in outer beats, not in validator beats.
- `current_scene` belongs in the outer beats array, not inside validators.
- Remediation (incorrect) states added later follow the same rule: feedback only.

**On-correct beats must only contain feedback directly about acknowledging
the correct answer.** Do not add beats that narrate the student's specific
path, set up the next scene, or make assumptions about what the student chose.

**When there is a way to be wrong — when the condition specifies a concrete
required answer (any condition that is not `{}` and is not a branching prompt) —
the correct state must have substantive on_correct dialogue.** Name the answer and
close with the principle. `{ "type": "empty" }` is only for interactions where the
student cannot be wrong: branching prompts (both choices are valid) and
any-response-advances (`condition: {}`). Even in two-step interactions, each step
with a concrete correct answer needs its own acknowledgment beat — it may be brief
("4 boxes.") but it must exist.

- For concrete answers (MC, click_category): name the answer, then close by
  naming what the answer demonstrates — the principle or structural insight
  the student just proved. The closing sentence should be transferable to the
  next problem.
  "Apples got the most votes: 6." is the answer. "That's how you read the
  tallest bar." is the principle. Together: "Apples got the most votes: 6.
  That's how you read the tallest bar."
- For open-ended interactions (`variable_answer: true`): simple achievement
  acknowledgment only. Do not narrate the specific values the student may
  have used. You may still close with a transferable principle that does not
  reference the student's specific values. "You got to 20. Any combination
  of equal groups that reaches the total works."
- For branching prompts or any-response-advances where there is no meaningful
  feedback to give: use `{ "type": "empty" }` to signal intentional silence.
  Prefer this over an empty array.

**Never embed a CTA inside on-correct dialogue.** If the feedback text trails
into a lead-in for the next prompt ("5 in each box. So what do you have?"),
split it: the acknowledgment stays in the validator beat ("5 in each box."),
and the CTA ("So what do you have?") goes as a top-level `dialogue` beat
immediately after the prompt in the outer beats array.

**Flag variable-answer interactions.** When a prompt has no fixed correct
answer (`product_equals`, `sum_equals`, or any condition that does not check
a fixed `selected` value), add `"variable_answer": true` to the prompt beat.
This applies to all feedback for that prompt — on_correct and all remediation
states. Downstream steps use this flag to avoid generating language that
assumes a specific answer.

For `multiple_choice`: `{ "condition": { "selected": 7 } }`

For `multi_select` requiring multiple selections:
```json
{ "condition": { "and": [ { "selected": "Dogs" }, { "selected": "Fish" } ] } }
```

**Any-response-advances** (no wrong answer): `"condition": {}`

Use `"condition": {}` only when every response leads to the exact same next scene and step. If the choice determines what the student sees or does next, use a branching prompt instead (see **Branching prompts** above).

Use `condition` for answer-checking (one correct answer, remediation possible). Use `branch: true` for path-taking (both options valid, different beat sequences follow).

### Branching prompts

A **branching prompt** occurs when a student's choice leads to fundamentally
different sequences of interactions — only one path is followed, paths do not
reconverge. Both choices are valid; they lead to different beat sequences.

Use branching when the student picks between options and each choice leads to
different tools, different scene setup, or different follow-up prompts. Do NOT
use branching for standard correct/incorrect validation.

Set `"branching": true` on the prompt beat. Each validator state that
establishes a branch gets `"branch": true` and a short stable `condition_id`
(e.g. `"selected_rows"`, `"selected_columns"`). Both states have `"is_correct": true`.
Branch validator beats must not contain scene setup. Scene setup for each
branch goes in the outer beats with `branch_name`. Branch validator beats
may contain a dialogue beat acknowledging the choice, or `{ "type": "empty" }`
if there is nothing to say. No `current_scene`.

```json
{
  "type": "prompt",
  "text": "Choose rows or columns.",
  "tool": "multiple_choice",
  "options": ["Rows", "Columns"],
  "branching": true,
  "validator": [
    {
      "condition_id": "selected_rows",
      "branch": true,
      "description": "Student chose rows",
      "is_correct": true,
      "beats": [ { "type": "empty" } ]
    },
    {
      "condition_id": "selected_columns",
      "branch": true,
      "description": "Student chose columns",
      "is_correct": true,
      "beats": [ { "type": "empty" } ]
    }
  ]
}
```

All outer beats that belong to a specific branch get `"branch_name": "<condition_id>"`.
Output ALL beats for one branch together before any beats for the other branch.
The unconditional `current_scene` right after the branching prompt captures
the pending-choice state; each branch's own `current_scene` carries `branch_name`.

```json
{ "type": "current_scene", "elements": [ ... ] },

{ "type": "scene", "method": "add", ..., "branch_name": "branch_a" },
{ "type": "prompt", ..., "branch_name": "branch_a",
  "validator": [ { "condition_id": "correct", "condition": { ... }, ... } ] },
{ "type": "current_scene", "elements": [ ... ], "branch_name": "branch_a" },

{ "type": "scene", "method": "add", ..., "branch_name": "branch_b" },
{ "type": "prompt", ..., "branch_name": "branch_b",
  "validator": [ { "condition_id": "correct", "condition": { ... }, ... } ] },
{ "type": "current_scene", "elements": [ ... ], "branch_name": "branch_b" }
```

---

## TWO-STEP INTERACTIONS

Two-step sections have two separate steps, each ending with `current_scene`
in the outer beats. Scene setup for step 2 goes in the outer beats after
step 1's `current_scene` — not inside step 1's validator.

```json
"beats": [
  { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
    "params": { "highlight_categories": ["Yellow", "Red"] } },
  { "type": "dialogue", "text": "Step 1: Find how many chose Yellow or Red in all." },
  { "type": "prompt", "text": "How many liked Yellow or Red in all?",
    "tool": "multiple_choice", "options": [5, 6, 11, 14],
    "validator": [
      {
        "condition_id": "correct",
        "condition": { "selected": 11 },
        "description": "Student answered 11, correct",
        "is_correct": true,
        "beats": [
          { "type": "dialogue", "text": "11 in all. Yellow has 6, Red has 5. 6 plus 5 equals 11." }
        ]
      }
    ]
  },
  { "type": "current_scene", "elements": [ ... ] },
  { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
    "params": { "highlight_categories": ["Green"], "description": "Green bar highlights for step 2." } },
  { "type": "dialogue", "text": "Step 2: Now compare that total to Green." },
  { "type": "prompt", "text": "How many MORE is 11 than Green's 4?",
    "tool": "multiple_choice", "options": [4, 7, 11, 15],
    "validator": [
      {
        "condition_id": "correct",
        "condition": { "selected": 7 },
        "description": "Student answered 7, correct",
        "is_correct": true,
        "beats": [
          { "type": "dialogue", "text": "7 more. You used TWO steps: first added, then compared." }
        ]
      }
    ]
  },
  { "type": "current_scene", "elements": [ ... ] }
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

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Do not reference concepts from <advanced_concepts>. Ground the section's teaching in <the_one_thing>. Include <required_phrases> where genuinely appropriate in dialogue.

These constraints define what this module's students have been taught and what they have not. Values, counts, and data points in scene descriptions, dialogue, and prompt options must be consistent with the module's dataset. Never construct values (e.g. distractor counts, made-up quantities) that fall outside the numerical patterns established by the module's data — even plausible-looking values can violate constraints the spec author enforced implicitly.

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
  "beats": [
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
          "beats": [
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
}

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
{
  "id": "s2_4_student_builds_full_equation_5s",
  "purpose": "First fully independent equation construction (all three slots, tile method).",
  "visual": "Equation Builder: `[___] × [___] = [___]` with Methods C/D active. Tile palette: 4, 5, 6, 11, 20, 25, 30, 35. No Context Visualization. Products Strip from 2.3 may remain visible or fade per UX decision.",
  "guide": "\"Build the whole equation this time. 6 groups of 5. Place the factors and the product.\"",
  "prompt": "\"Build the equation for 6 groups of 5.\"",
  "student_action": "Equation Builder Methods C or D (all three slots)",
  "correct_answer": "`6 × 5 = 30`",
  "on_correct": "\"6 times 5 equals 30. Ends in 0 which matches the 5s pattern. You built the complete equation with the factors and product.\"",
  "remediation": "Pipeline",
  "remediation_note": "Guide factor identification from verbal description: how many groups? (6 — first factor). What are we counting by? (5 — second factor). Then skip-count by 5s six times.",
  "design_note": "First fully independent equation construction. No context visualization — student works from verbal description alone. Tests whether student can manage all three slots (both factors + product) and compute via skip-counting.",
  "_generated_at": "2026-04-27T15:53:24.076038+00:00",
  "workspace_specs": {
    "toys": [
      "equation_builder"
    ],
    "tools": [
      "place_tile"
    ],
    "unresolved": [
      "No Context Visualization",
      "UX decision"
    ]
  },
  "prior_section_summaries": "## s1_1_extend_accumulation_5_10_concrete\n# Section Summary: s1_1_extend_accumulation_5_10_concrete\n\n**VISUAL STATE AT SECTION END:**\nThree tangibles are displayed: (1) Equal Groups (circles mode, reading mode): 10 containers with 2 items per container; (2) Products Strip (reading mode): displays values 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 with all highlighted and labeled \"Multiples of 2\"; (3) Equation Builder (reading mode): shows expression \"10 × 2 = 20.\"\n\n**CONTENT:**\nThis section introduced the concept of **multiples** and **accumulation through repeated multiplication**. Students observed the pattern of multiplying by 2 sequentially (from 5 groups through 10 groups), watching products increase by 2 each time. The vocabulary term **\"multiples of 2\"** was formally introduced to describe all products generated when multiplying by 2.\n\n**STUDENT ACTION:**\nThe student passively observed an animated sequence where equal groups were added one at a time (groups 6–10), with corresponding equations updating dynamically (6 × 2 = 12 through 10 × 2 = 20). The student then viewed the complete Products Strip displaying all 10 multiples of 2 in a single visual collection.\n\n---\n\n## s1_2_pattern_discovery_2s_are_always\n# Section Summary: Pattern Discovery – \"2s Are Always Even\"\n\n**VISUAL STATE:** A Products Strip tangible displays ten values (2, 4, 6, 8, 10, 12, 14, 16, 18, 20) labeled \"Multiples of 2\" in reading mode with all products highlighted/glowing throughout the section.\n\n**CONTENT:** Students discovered and formalized the pattern that all products of 2 are even numbers. The section introduced the concept of using this pattern as a \"checking tool\"—a self-verification strategy where an odd result from multiplying by 2 signals an error. The vocabulary term \"even numbers\" was reinforced in connection to the property of splitting perfectly into groups of 2.\n\n**STUDENT ACTION:** The student answered a multiple-choice question selecting \"They are all even numbers\" from four options (even numbers, odd numbers, greater than 10, end in 5), demonstrating pattern recognition and receiving confirmatory dialogue explaining the mathematical reasoning.\n\n---\n\n## s1_3_bridge_pattern_check_concrete_relational\n# Section Summary: s1_3_bridge_pattern_check_concrete_relational\n\n**VISUAL STATE AT SECTION END:**\nFour tangibles are displayed simultaneously in reading mode:\n1. **Products Strip** (dataset: Multiples of 2): values 2, 4, 6, 8, 10, 12, 14, 16, 18, 20—all highlighted\n2. **Equal Groups** (circles): 5 containers with 2 items per container, all highlighted\n3. **Equation Builder**: expression \"5 × 2 = 10\"\n4. **Equation** (repeated addition): \"2 + 2 + 2 + 2 + 2 = 10\"\n\n**CONTENT:**\nThe section bridges concrete (equal groups, repeated addition) and relational (multiplication, skip-counting) representations of the same quantity. Key concepts introduced: skip-counting by 2s IS multiplication by 2; multiplication is a shorter notation for repeated addition; any number multiplied by 2 always yields an even product (because items in groups of 2 always have pairs with no remainder).\n\n**STUDENT ACTION:**\nStudent answered a multiple-choice question selecting \"Even\" as the correct response to: \"When you multiply any number by 2, is the product even or odd?\"\n\n---\n\n## s2_1_worked_example_first_full_equation\n# Section Summary: s2_1_worked_example_first_full_equation\n\n**VISUAL STATE AT SECTION END:**\nTwo tangibles are displayed: (1) Equal Groups visualization (\"equal_groups_bags\") showing 7 bags in reading mode, each containing 2 items; (2) Equation Builder (\"equation_builder_7x2\") in reading mode displaying the complete equation template with three slots [__] × [__] = [__], pre-filled with factors 7 and 2, and product 14. Labels identifying \"factor,\" \"factor,\" and \"product\" have appeared and faded.\n\n**CONTENT:**\nThe section introduced the formal concept of an **equation** (a complete multiplication statement with an equals sign and answer) and distinguished it from an **expression** (7 times 2 alone). Two key vocabulary terms were formally introduced: **factors** (the numbers being multiplied: 7 and 2) and **product** (the answer to multiplication: 14). The worked example modeled solving 7 × 2 by skip-counting by 2s seven times (2, 4, 6, 8, 10, 12, 14) to reach the product.\n\n**STUDENT ACTION:**\nThe student observed a guided worked example. The Guide demonstrated interpreting the equal groups model, performing skip-counting, and completing the equation by filling the product slot with 14. No direct student interaction occurred; this was a demonstration of the full problem-solving process.\n\n---\n\n## s2_2_student_computes_product_method_relational\n# Section Summary: s2_2_student_computes_product_method_relational\n\n**VISUAL STATE:** Two tangibles are on screen at section end:\n1. **Equal Groups (equal_groups_bags)**: 8 bags (containers), each containing 2 circles (items), displayed in reading mode.\n2. **Equation Builder (equation_builder_8x2)**: A completed multiplication equation template showing 8 × 2 = 16, with all three slots filled (slot_0: 8, slot_2: 2, slot_4: 16).\n\n**CONTENT:** The student practiced computing a multiplication product using the relational method—interpreting \"8 times 2\" as \"8 groups of 2\" and skip-counting by 2s eight times to find the product. The vocabulary reinforced includes: *product*, *times*, *groups*, and *skip-count*.\n\n**STUDENT ACTION:** The student selected the correct multiple-choice answer (16) from options {10, 14, 16, 18} to complete the equation 8 × 2 = ___. Upon correct selection, the equation builder automatically filled the product slot with 16, and feedback confirmed the relationship between the equal groups model and the completed equation.\n\n---\n\n## s2_3_5s_discovery_partial_worked_example\n# Section Summary: s2_3_5s_discovery_partial_worked_example\n\n**VISUAL STATE AT SECTION END:**\nThree tangibles are on screen: (1) **Products Strip** (products_strip_5s), reading mode, displaying values 5, 10, 15, 20, 25, 30 with ones digits highlighted; (2) **Equation Builder** (equation_builder_5s), reading mode, showing completed equation 3 × 5 = 15 with all slots filled; (3) **Tile Palette** (tile_palette_3x5) containing tile options 8, 10, 15, 20.\n\n**CONTENT:**\nThis section introduced the **5s multiplication pattern** through a worked example. Students discovered that all multiples of 5 end in either 0 or 5 in the ones place—the defining characteristic of the 5s pattern. Key vocabulary formally introduced: \"multiples of 5,\" \"ones digit,\" and \"5s pattern.\" The section modeled skip-counting by 5s (1×5=5, 2×5=10, 3×5=15, 4×5=20, 5×5=25, 6×5=30) and connected visual equal groups to symbolic equations.\n\n**STUDENT ACTION:**\nThe student placed a tile (15) into the product slot of an equation builder to complete 3 × 5 = __, selecting from four options (8, 10, 15, 20). This was a single tile-placement interaction that required applying the skip-counting strategy and pattern recognition to find the correct product."
}
</input>

======================================================================

## Prefill

{

