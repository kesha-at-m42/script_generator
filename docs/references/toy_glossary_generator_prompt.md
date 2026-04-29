# Toy Glossary — What It Is

A **Toy Glossary** is a design requirements document that catalogs every interactive component in a curriculum unit. It lives between curriculum design and engineering: it tells script authors what they can use and tells engineers what they need to build. It is synthesized from reading the actual lesson scripts — not written speculatively.

The document is organized by **toy type**. Each toy gets its own section covering three things: what the toy is, how students interact with it, and what the guide can animate on it.

---

## Key Concepts

**Toy** — a visual, interactive object placed on screen. Toys have state (mode, values, orientation) and are added, updated, animated, or removed across scenes. Examples: `picture_graph`, `equal_groups`, `arrays`. The specific instance of a toy in a script is its **tangible ID** (e.g. `picture_graph_books`, `row_builder`).

**Mode** — how the toy is currently configured. `"reading"` means it's pre-built and the student reads or identifies things on it. `"building"` means the student constructs it. Mode determines which tools apply.

**Tool** — the interaction mechanism a student uses on a toy. It describes *how* the student acts, not *what* they act on. Tools only appear in `prompt` beats and always have a **validator** — a JSON condition that defines what a correct response looks like (e.g. `{ "selected": "Dogs" }`, `{ "symbols_placed": 4 }`). Some tools are **cross-toy**: they appear on any toy and go in their own section rather than under a specific toy.

**Animation event** — something the guide fires on a toy: highlighting, counting, demonstrating, transforming. Animation events are scene beats, not student actions. The key design rule is that they are **atomic** — each event is one self-contained visual moment. Two atomics can fire simultaneously. When a multi-step effect is needed, it is a **compound sequence**: a named event that lists its constituent atomics as numbered steps in order.

**Sequential variant** — some atomic animations can run either all-at-once or one-item-at-a-time. The one-at-a-time version is the sequential variant. It is noted inline under the core event (not a separate entry).

---

## Document Structure

**Toy section** (`## toy_name`) — describes what the toy is: its purpose, behavioral modes, visual variants, tangible IDs seen in scripts, and which modules it appears in.

**Student Interactions** (`### Student Interactions`) — one entry per tool. Each entry gives the canonical tool name (and any aliases seen in scripts), one sentence on what the student does and why, the validator shape, and example prompts drawn from real scripts.

**Guide Animations** (`### Guide Animations`) — one entry per animation event. Opens with a callout: *"animations are atomic and can fire simultaneously; compound effects are two events fired at the same time rather than one compound name."* Atomic entries describe the visual and give an example of when and how the event fires (including any common pairings). Compound entries list their steps as a numbered sequence.

**Cross-toy Interactions** (`## Cross-toy Interactions`) — tools not bound to one toy: `select_one_option`, `select_all_options`, `select_toy`, `drag_to_sort`. Same entry format as toy-specific tools.

**Tool Taxonomy** (`## Tool Taxonomy (quick reference)`) — flat table at the end: every tool in the document, one row each, with a one-line description and validator shape.

---

## Naming Principles

**Same action, different cardinality — use the same verb, singular vs plural.**
When two tools perform the same student action but differ in how many correct answers exist, keep the verb identical and distinguish by pluralizing the noun:
- `select_category` — student selects one category as the answer
- `select_categories` — student selects all categories that apply

Do not use different verbs (e.g. `click_` vs `select_`) to signal this distinction — that implies the actions are fundamentally different when they are not.

**Ordering** — list cardinality variants adjacent to each other in the document. `select_category` immediately before `select_categories`, not separated by unrelated entries.

---

## Canonical Tool Names

Scripts often use older implementation names. Always normalize:

| Seen in scripts | Canonical |
|---|---|
| `click_to_place`, `click_place_symbols` | `build_category` |
| `click_to_set_height` | `build_bar` |
| `click_tangible` | `select_toy` |
| `click_scale_button`, `explore_scales` | `select_scale` |
| `multiple_choice` | `select_one_option` |
| `multi_select` | `select_all_options` |
| `drag_tile` | `place_tile` |
| `click_category` | `select_category` |

Note aliases you normalized in each tool entry under "Tool field aliases seen."

---

## Example Prompt

```
You are writing a Toy Glossary — Design Requirements document for [unit name].

A Toy Glossary catalogs every toy (interactive UI component), student interaction, and guide animation across the unit. It is organized by toy type. Each toy section covers: what the toy is and how it behaves, how students interact with it (tools and validators), and what the guide can animate on it (atomic events and compound sequences).

Key concepts:
- Toys have modes: "reading" (pre-built, student reads/identifies) or "building" (student constructs)
- Tools are student actions in prompt beats. Each has a validator — a JSON condition defining a correct response
- Animation events are guide actions. They are atomic by design: each is one visual moment that can fire simultaneously with others. Compound sequences are named events that list their constituent atomics as numbered steps
- Sequential variants (one-at-a-time vs all-at-once) are noted inline under the core event, not as separate entries
- Cross-toy tools (select_one_option, select_all_options, select_toy, drag_to_sort) go in their own section at the end

Normalize any deprecated tool names: click_to_place → build_category, click_to_set_height → build_bar, click_tangible → select_toy, click_scale_button → select_scale, multiple_choice → select_one_option, multi_select → select_all_options, click_category → select_category.

Naming principle: when two tools are the same action but differ in cardinality (one correct answer vs all that apply), use the same verb and distinguish via singular/plural — e.g. select_category vs select_categories. Do not use different verbs to signal this distinction.

Only document what appears in the scripts — do not invent entries.

See docs/u1_toy_glossary.md for a complete worked example covering picture_graph, bar_graph, equal_groups, equation_builder, arrays, equation, data_table, sorting_area, dropdown_fillin, and image.

Here are the scripts:
[paste scripts]
```
