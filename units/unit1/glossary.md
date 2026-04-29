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
