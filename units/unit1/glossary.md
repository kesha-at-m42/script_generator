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
| `text_display` | Persistent on-screen text — running totals, strategy labels, equations. | Needs spec |
| `text_overlay` | Temporary overlay text used to name or annotate mid-interaction. | Needs spec |
| `scale_preview_system` | Interactive scale selector with preview pane (M5 only). Replaces `scale_selector`, `scale_toggle`, `scale_preview`. | Needs spec |
| `sorting_area` | Workspace for drag-to-sort activities. | Needs spec |
| `image` | Static image displayed for real-world connection or context. | Needs spec |

**Forbidden aliases** — use the canonical name above instead:

| Do NOT use | Use instead |
|---|---|
| `counting_game` | `data_collection_game` |
| `interactive_game` | `data_collection_game` |
| `data_collection_game` (varies) | `data_collection_game` |
| `scale_selector` | `scale_preview_system` |
| `scale_toggle` | `scale_preview_system` |
| `scale_preview` | `scale_preview_system` |
| `data_display` | `text_display` |
| `animation` | — (animations are not standalone toys; use `animate` scene beats) |
| `animation_canvas` | — (same as above) |

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
| `multiple_choice` | Student picks one answer from a fixed list | standalone | `{ "selected": value }` |
| `multi_select` | Student picks multiple items from a list | standalone | `{ "and": [{ "selected": "A" }, { "selected": "B" }] }` |

### Creating / Building Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_to_place` | Student clicks to place symbols one at a time on a picture graph | `picture_graph` (mode: creating) | `{ "symbols_placed": 3 }` |
| `click_to_set_height` | Student clicks or drags to set a bar to a specific height | `bar_graph` (mode: creating) | `{ "bar_height": 30 }` |
| `click_symbol` | Student selects a symbol from the symbol palette | `picture_graph` (mode: creating) | `{ "selected": "symbol_name" }` |

### Scale Tools

| Tool | What it does | Applies to | Validator shape |
|---|---|---|---|
| `click_scale_button` | Student selects a scale option from the scale preview system | `scale_preview_system` | `{ "selected": 2 }` (the scale value chosen) |

**Forbidden aliases** — use the canonical name above instead:

| Do NOT use | Use instead |
|---|---|
| `click_to_set_bars` | `click_to_set_height` |
| `bar_graph_creator` | `click_to_set_height` |
| `click_place_symbols` | `click_to_place` |
| `click_to_set_height` used for picture graph | `click_to_place` |
| `click_component` used to set a bar height | `click_to_set_height` |
| `click_component` used to place symbols | `click_to_place` |
| `explore_scales` | `click_scale_button` |
| `counter_input` | `click_scale_button` (for scale) or leave as `counter_input` pending spec |
| `drag_to_sort` | pending spec — do not use yet |

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
