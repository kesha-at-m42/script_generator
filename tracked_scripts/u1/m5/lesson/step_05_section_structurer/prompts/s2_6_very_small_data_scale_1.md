# Prompt: section_structurer
# Generated: 2026-05-05T13:19:12.657533
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
| Scale Preview System | `bar_graph` or `picture_graph` (scale is a component of the graph, not a separate toy — use whichever graph type is present in context) |

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
| `multiple_choice` | `select_one_option` |
| `multi_select` | `select_all_options` |

> **⚠ Naming review needed:** The `u1_toy_glossary.md` uses more intent-readable names for several of these tools and may be a better canonical. Consider renaming:
>
> | Current canonical | Proposed name | Rationale |
> |---|---|---|
> | `click_to_place` | `build_category` | Describes the student goal (build a category), not the gesture |
> | `click_to_set_height` | `build_bar` | Same — "set height" is implementation detail |
> | `click_tangible` | `select_toy` | "Select" is clearer than "click" for touch/pointer-agnostic contexts |
> | `click_scale_button` | `select_scale` | Describes what the student is choosing, not the UI element |
>
> Also consider adding `select_category` (select multiple categories that all apply) — currently unlisted.

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
- A `student_action` that uses "OR" to offer two equivalent click targets for the same interaction (e.g. "Click on the bar OR the symbols for that category") is a **single prompt with a multi-target** — use `"target": ["tangible_id_1", "tangible_id_2"]`. A `correct_answer` of "Either correct location accepted" confirms this pattern. Do NOT split it into two sequential prompts.
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

**When a multi-step interaction is split into sequential steps, each prompt's `text` must scope to only its own step.** Do not carry forward the combined task description into individual prompts. "Click on the category showing 35 in the vertical graph." not "What category shows 35 in BOTH graphs?"

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
  **`params.description` must be neutral.** It describes what appears on screen. It must not direct the student's attention toward the feature they are about to identify — that is hint or remediation language and belongs only in validator beats, not in scene setup.
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

**Reference scenario images by highlighting, not by letter.** When a validator on-correct beat (or any dialogue that would otherwise say "Image A", "scenario B", etc.) needs to call out a specific scenario image tangible, emit a `scene animate` beat with `event: "highlight"` on that tangible ID immediately before the dialogue. The dialogue then says "this image" or describes the scenario content — never a letter label.

```json
{ "type": "scene", "method": "animate", "tangible_id": "scenario_image_counting",
  "params": { "event": "highlight", "status": "confirmed",
              "description": "Counting money scenario image highlights." } },
{ "type": "dialogue", "text": "This one works. Counting money in stacks uses groups of 10." }
```

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

**Prefer `click_tangible` over `multiple_choice` when the choices are on-screen visuals.** If the spec presents a question where the options are scenario images, illustrations, or any tangibles displayed on screen — even if the spec labels them A, B, C or lists them as MC options — use `click_tangible` targeting those tangible IDs. The student clicks the visual directly. Never convert on-screen visuals into a word-based MCQ. Letter labels (A, B, C) in the spec are spec-author identifiers for those visuals, not answer choices; they must not appear in options arrays or dialogue.

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

**Exception — described answer rationale:** If the spec includes a field (e.g. `on_incorrect`, `answer_rationale`, or any field describing why a specific wrong answer is wrong), create a stub `is_correct: false` state for each described condition. Use the spec's rationale verbatim as the `description` field. Derive the `condition` from the described wrong answer using the same shape as the correct state's condition (e.g. if the correct condition is `{ "selected": 10 }` and the spec describes a student choosing 5, use `{ "selected": 5 }`). Leave `beats: []`. Only create a stub when you can express a concrete condition — do not use `condition: {}` for stubs, as the remediation generator uses that shape exclusively for the Heavy catch-all. Do not invent rationale; only stub out conditions the spec explicitly describes.

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
any-response-advances (`condition: {}`). Every step with a concrete correct answer needs its own acknowledgment beat. It must exist.

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
- For branching prompts where both choices are equally valid and there is nothing to say about the choice itself: use `{ "type": "empty" }` to signal intentional silence. Prefer this over an empty array.
- For any-response-advances (`condition: {}`) that complete an activity — a game, a build task, a counting interaction — write brief acknowledgment dialogue even though the student cannot be wrong. Use the spec's `on_complete`, `on_correct`, or purpose field to inform it. A single sentence confirming the activity is done is sufficient.

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
- **Flag placeholders and uncertain content:** When a beat or section field contains content that could not be grounded in the spec — unresolved visual elements (present in `workspace_specs.unresolved`), game data values not defined in the spec, invented quantities or distractor values — add `"flag": "placeholder — <brief reason>"` to that beat or object. This makes uncertain content findable for human review without blocking output. Example: `"flag": "placeholder — toy spec not yet defined, tool and validator shape are best-guess"`.
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
  "id": "s2_6_very_small_data_scale_1",
  "visual": "NEW data context: \"Stickers Earned Today\"\n  * Vertical Data Table: Mia: 9, Noah: 5, Olivia: 7, Pete: 3\n  * Scale Preview System available. Vertical bar graphs. No bars showing.",
  "guide": "\"Look at these numbers: 9, 5, 7, 3. They're really small!\"",
  "guide_2": "\"What happens if we try Scale of 10?\"",
  "prompt": "\"Click 'Scale of 10'\"",
  "student_action": "Click \"Scale of 10\" button.",
  "preview_displays": "Only tick marks at 0 and 10. Bars appear with ⚠️ indicators.",
  "guide_3": "\"The bars fit, but we don't know the exact value for any of the bars.\"",
  "guide_4": "\"Think about the numbers: 9, 5, 7, 3. They don't end in 0 or 5 so we know Scale of 2 is clearer to show any number. Click 'Scale of 2.'\"",
  "prompt_2": "\"Click 'Scale of 2'\"",
  "student_action_2": "Click \"Scale of 2\" button.",
  "preview_displays_2": "All bars show ✓ indicator. Clean graph with 0-10 range.",
  "guide_5": "\"That's better! We can see the bars end at lines or exactly halfway. Scale of 2 could work. But when numbers are this small, you have another option. Try Scale of 1. What do you notice?\"",
  "prompt_3": "\"Click 'Scale of 1'\"",
  "student_action_3": "Click \"Scale of 1\" button",
  "preview_displays_3": "All bars land exactly on tick marks. ✓ indicator. Clean graph with 0-10 range.",
  "guide_6": "\"Every number lands right on a line. No halfway bars needed. We can read the graph accurately without having the data table.\"",
  "key_teaching_point": "\"For very small numbers, Scale of 1 can be a great choice—simple and exact.\"",
  "divider": "**→ SECTION 2 COMPLETE. PROCEED TO SECTION 3.**",
  "_generated_at": "2026-05-05T18:14:19.464347+00:00",
  "workspace_specs": {
    "toys": [
      "bar_graph",
      "data_table"
    ],
    "tools": [
      "click_scale_button"
    ]
  },
  "prior_section_summaries": "## s1_1_transition_warmup\n# Section Summary: s1_1_transition_warmup\n\n**VISUAL STATE:** Empty workspace. No tangible visualizations, graphs, or data displays are present on screen at section end.\n\n**CONTENT:** Transition dialogue acknowledging that in the Warmup section, all four scales (linear, log, square root, and reciprocal) were viable options for the student's dataset. The section introduces the concept that scale choice becomes more constrained when working with larger numbers, setting up the next investigation.\n\n**STUDENT ACTION:** No interactive action required. The student listened to dialogue explaining that scale flexibility depends on data magnitude, preparing them for the upcoming exploration of how larger numbers affect scale viability.\n\n---\n\n## s1_2_when_scale_needs_too_many\n# Section Summary: s1_2_when_scale_needs_too_many\n\n**VISUAL STATE AT SECTION END:**\nA data table and vertical bar graph are displayed side-by-side. The data table shows \"Books Read This Month\" with categories Aisha, Ben, Carlos, Dana and values 20, 35, 55, 80 respectively. The bar graph is vertical, in reading mode, with axis range 0–80, scale of 5, and all 17 tick marks highlighted (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80).\n\n**CONTENT:**\nThe section introduced the problem that when a scale is too small relative to data range, it creates too many tick marks on the axis, making the graph crowded and difficult to read. The key vocabulary introduced was the principle: \"When one scale needs too many tick marks, try a bigger scale.\" Students observed that a scale of 5 with axis 0–80 produces 17 tick marks, demonstrating visual clutter.\n\n**STUDENT ACTION:**\nThe student (via guided exploration) selected a scale of 5, observed the preview showing Dana's bar extending past the initial 0–50 boundary, then extended the axis to 0–80 to accommodate all data. This revealed the crowding problem, leading to the conceptual takeaway about choosing appropriate scales.\n\n---\n\n## s1_3_trying_bigger_scale\n# Section Summary: s1_3_trying_bigger_scale\n\n**VISUAL STATE AT SECTION END:**\nTwo tangibles are on screen: (1) a data table displaying \"Books Read This Month\" with categories Aisha, Ben, Carlos, Dana and values 20, 35, 55, 80 respectively; (2) a vertical bar graph in reading mode showing the same data with scale 10, axis range 0–80 containing 9 tick marks (0, 10, 20, 30, 40, 50, 60, 70, 80), all four bars fitting cleanly.\n\n**CONTENT:**\nThe section introduced the concept of adjusting graph scale to improve readability. Students learned that increasing the scale from 5 to 10 reduces the number of tick marks (from 17 to 9), making the graph cleaner and easier to interpret while still displaying all data accurately.\n\n**STUDENT ACTION:**\nThe student clicked the \"Scale of 10\" button on the interactive scale selector, triggering the graph to update and demonstrating the effect of a larger scale on axis tick mark density and overall visual clarity.\n\n---\n\n## s1_4_range_check_efficiency\n# Section Summary: s1_4_range_check_efficiency\n\n**VISUAL STATE AT SECTION END:**\n- **Data Table** (\"Books Read This Month\"): Categories—Aisha, Ben, Carlos, Dana; Values—20, 35, 55, 80 respectively; Dana's value (80) highlighted.\n- **Bar Graph** (vertical, reading mode): Same dataset; axis range 0–80; scale of 10; 9 tick marks (0, 10, 20, 30, 40, 50, 60, 70, 80); all four bars visible.\n\n**CONTENT:**\nIntroduced the \"range check\" strategy for selecting appropriate graph scales: identify the biggest number in the dataset first, then choose a scale that fits the maximum value without creating too many axis tick marks. Formally introduced the principle that larger scales (e.g., 10 vs. 5) produce cleaner, more readable graphs when multiple scales are viable. Compared efficiency: Scale of 5 requires 17 tick marks; Scale of 10 requires only 9 for the same data.\n\n**STUDENT ACTION:**\nAnswered a multiple-choice question identifying 80 as the largest value in the dataset, demonstrating understanding of the first step in scale selection.\n\n---\n\n## s2_1_all_scales_fit_small_data\n# Section Summary: s2_1_all_scales_fit_small_data\n\n**VISUAL STATE AT SECTION END:**\nA horizontal bar graph (dataset: Marbles in Jars) displays four bars for categories Jar A, Jar B, Jar C, and Jar D with values 7, 12, 19, and 23 respectively. The graph uses a scale of 1 with an axis range of 0–23 and 24 tick marks. A horizontal data table showing the same four categories and values appears alongside the graph.\n\n**CONTENT:**\nThe section introduced the concept that multiple scales can fit small datasets and demonstrated how to evaluate scale appropriateness by checking whether the maximum data value (23) fits within each scale option. Students learned that while all four scales (1, 2, 5, 10) are mathematically valid, scale choice affects readability—specifically, a scale of 1 produces many tick marks (24), which can clutter the axis.\n\n**STUDENT ACTION:**\nThe student clicked through all four scale buttons to explore which scales fit the data range, then selected Scale of 1 to observe the resulting graph with its dense tick-mark display.\n\n---\n\n## s2_2_but_which_is_best_efficiency\n# Section Summary: s2_2_but_which_is_best_efficiency\n\n**VISUAL STATE AT SECTION END:**\nA data table displays \"Marbles in Jars\" with four categories: Jar A=7, Jar B=12, Jar C=19, Jar D=23. A horizontal bar graph (reading mode) shows the same data with scale of 10, axis range 0–30 (4 tick marks), and warning indicators (⚠️) on Jar A and Jar C bars, signaling that values 7 and 19 do not land exactly on axis lines or midpoints.\n\n**CONTENT:**\nThe section introduced the concept of **scale efficiency**—balancing readability (fewer axis lines) against precision (exact value placement). Students learned that while larger scales (e.g., 10) reduce visual clutter for big datasets, they can create ambiguity for small data values. The vocabulary term **\"scale\"** was reinforced as a tool choice that affects graph clarity and accuracy.\n\n**STUDENT ACTION:**\nThe student clicked a \"Scale of 10\" button to switch the graph from scale 1 (24 tick marks, 0–23 range) to scale 10 (4 tick marks, 0–30 range), then observed warning indicators highlight precision problems with values that don't align to grid lines.\n\n---\n\n## s2_3_scale_2_works_non_multiples\n# Section Summary: s2_3_scale_2_works_non_multiples\n\n**VISUAL STATE AT SECTION END:**\n- **Data Table** (\"Marbles in Jars\"): 4 categories (Jar A, Jar B, Jar C, Jar D) with values 7, 12, 19, 23 respectively\n- **Horizontal Bar Graph** (\"bar_graph_marbles\"): reading mode, Scale of 2, axis range 0–24, categories Jar A, Jar B, Jar C, Jar D with values 7, 12, 19, 23; all bars land exactly on tick marks with checkmark indicator visible, no warning indicators\n\n**CONTENT:**\nThe section introduced the concept that **Scale of 2 works universally for whole numbers** because its half-interval (1) allows any integer to land exactly on a tick mark or midpoint. Students learned that Scale of 2 is effective for small datasets because it produces a manageable number of axis marks while ensuring precise value representation—contrasting with Scale of 10, which generated warnings for non-multiple values (7 and 19).\n\n**STUDENT ACTION:**\nThe student clicked the \"Scale of 2\" button to preview the graph transformation, observing how all data values (7, 12, 19, 23) aligned exactly with axis marks when the scale changed from 10 to 2.\n\n---\n\n## s2_4_digit_pattern_recognition_shortcut\n# Section Summary: s2_4_digit_pattern_recognition_shortcut\n\n**VISUAL STATE:** Two side-by-side image panels are displayed. Left panel (\"Data Set A\") shows values 20, 35, 55, 80 with annotation \"Ones digits: 0 or 5.\" Right panel (\"Data Set B\") shows values 7, 12, 19, 23 with annotation \"Ones digits: 7, 2, 9, 3.\" Both panels remain visible throughout; Data Set B becomes highlighted after student interaction.\n\n**CONTENT:** Students learned a shortcut for scale selection by examining the ones digit (last digit) of dataset values. The key pattern introduced: numbers ending in 0 or 5 are multiples of 5 (suitable for Scales of 5 and 10), while numbers with other ones digits (like 7, 2, 9, 3) signal that Scale of 2 may be the best choice. This digit-checking strategy provides a quick decision rule for scale selection.\n\n**STUDENT ACTION:** Student clicked on Data Set B to answer the prompt \"Which data set has last digits that are NOT 0 or 5?\" The correct selection (Data Set B) triggered a highlight animation and confirmatory dialogue reinforcing that ones digits 7, 2, 9, 3 indicate a Scale of 2 signal.\n\n---\n\n## s2_5_practice_with_non_multiples\n# Section Summary: Practice with Non-Multiples\n\n**VISUAL STATE:** At section end, the screen displays two tangibles: (1) a vertical data table titled \"Points Scored\" with categories Round 1, Round 2, Round 3, Round 4 and values 22, 15, 8, 31 respectively; (2) a vertical bar graph in reading mode with the same dataset, scale of 1, axis range 0–31, where all bars are visible and land on tick marks.\n\n**CONTENT:** Students practiced selecting appropriate scales for datasets containing non-multiples of common scale intervals. The lesson introduced the strategy of checking ones-place digits to determine divisibility by 5, then reasoned that a scale of 2 works well for this data (since all values are even) while a scale of 1, though accurate, requires many axis marks. The concept reinforced is that scale choice balances exactness with readability.\n\n**STUDENT ACTION:** The student answered a multiple-choice question selecting \"Scale of 2\" as the best scale to show all values exactly, then observed the resulting bar graph and compared it to a scale-of-1 version to evaluate trade-offs between precision and practicality."
}
</input>

======================================================================

## Prefill

{
