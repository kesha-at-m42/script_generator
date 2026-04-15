# Validator Use Cases — Taxonomy for System Design

Every prompt has exactly **one** `is_correct: true` condition. Wrong branches never have `is_correct: true`.

For canonical toy names, tool names, and aliases see `units/unit1/glossary.md`.

---

## Use Case 1 — Single-select: pick the right answer

**Tool:** `multiple_choice`
**Toy:** any (standalone panel, or hosted in `word_problem_area`)

> **Visual:** 3–5 answer options displayed as buttons
> **Guide:** "Which fruit got the most votes?"
> **Prompt:** Student taps one option

**Correct condition:** `{ selected: <value> }`
**Wrong branches:** one per distractor — `{ selected: <wrong_value> }` — misconception-targeted
**Fallback:** `{}`

**Design note:** We know exactly which wrong answer was chosen. No attempt counting needed. Feedback is per-distractor.

---

## Use Case 2 — Click to identify: tap a category or bar

**Tool:** `click_category`
**Toy:** `picture_graph`, `bar_graph`

> **Visual:** A graph on screen with labelled rows or bars
> **Guide:** "Which group has the fewest?"
> **Prompt:** Student taps a row or bar

**Correct condition:** `{ selected: "CategoryName" }`
**Wrong branches:** `incorrect_count: 1`, `incorrect_count: 2`, `{}`

**Design note:** The validator sees only that a wrong tap occurred — not which category. Remediation is generic. Suggested enhancement: support `{ selected: "CategoryName" }` on wrong branches too, mirroring Use Case 1.

---

## Use Case 3 — Click a structural part: no remediation

**Tool:** `click_component`
**Toy:** `picture_graph`, `bar_graph`

> **Visual:** A graph with labelled structural parts (key, title, axis)
> **Guide:** "Tap the key."
> **Prompt:** Student taps a named part

**Correct condition:** `{ selected: "component_name" }`
**Wrong branches:** none

**Design note:** Low-stakes identification. Valid as a single-state validator with no fallback.

---

## Use Case 4 — Place symbols: build a picture graph row

**Tool:** `click_to_place`
**Toy:** `picture_graph` (mode: building)

> **Visual:** An empty picture graph; student taps to place symbols into a row
> **Guide:** "Ava collected 7 stickers. Each symbol stands for 2. Place the symbols."
> **Prompt:** Student taps to place symbols (supports half-symbols, e.g. `3.5`)

**Correct condition:** `{ category: "Ava", symbols_placed: 3.5 }`
**Wrong branches:** `incorrect_count: 1`, `incorrect_count: 2`, `{}`

**Design note:** Condition is scoped to one row at a time. Wrong branches cannot see what was placed.

---

## Use Case 5 — Set bar heights: build a bar graph

**Tool:** `click_to_set_height`
**Toy:** `bar_graph` (mode: building)

> **Visual:** An empty bar graph; student taps or drags bars to set heights
> **Guide:** "Build the graph. Milk: 3. Water: 6."
> **Prompt:** Student sets all required bars

**Correct condition:** `{ and: [ { category: "Milk", symbols: 3 }, { category: "Water", symbols: 6 } ] }`
**Wrong branches:** `incorrect_count: 1`, `incorrect_count: 2`, `{}`

**Design note:** All bars must be correct simultaneously. Partial correctness falls through to attempt count — wrong branches have no visibility into which bars are off. Suggested enhancement: partial-match condition key in wrong branches.

---

## Use Case 6 — Place a tile: fill an equation

**Tool:** `place_tile`
**Toy:** `equation_builder`

> **Visual:** An equation frame with blank slots and a tile palette
> **Guide:** "6 groups of 7. Drag the tiles to fill in the equation."
> **Prompt:** Student drags number tiles into the slots

**Correct condition:** `{ placed: { groups: 6, items: 7, total: 42 } }`
**Wrong branches:** `incorrect_count: 1`, `incorrect_count: 2`, `{}`

**Design note:** All slots must be correct. Wrong branches cannot see which slots are wrong. Suggested enhancement: partial placed-match conditions (e.g. right total but swapped factors).

---

## Use Case 7 — Select all that apply: multi-select

**Tool:** `multi_select`
**Toy:** standalone

> **Visual:** A list of options; student selects all that apply
> **Guide:** "Which two categories does the question compare?"
> **Prompt:** Student selects multiple items and submits
 
**Correct condition:** `{ and: [ { selected: "Dogs" }, { selected: "Fish" }, { not: { selected: "Cats" } }, ... ] }`
**Wrong branches:** classified by selection pattern — `and`/`or`/`not` combinators:
- Under-selecting: picked some correct, not all
- All-wrong: no correct options chosen
- Over-selecting: correct + wrong item(s)

**Fallback:** `{}`

**Design note:** Wrong branches classify the *pattern* of the selection, not attempt count. Each branch must be self-sufficient — do not rely on evaluation order to exclude cases the condition itself does not rule out.

---

## Use Case 8 — Build equal groups: set containers and items

**Tools:** `set_container_count`, `set_items_per_container`
**Toy:** `equal_groups` (mode: building)

> **Visual:** An equal groups workspace; student sets the number of groups, then items per group
> **Guide:** "Show me 2 groups of 3."
> **Prompt (1):** "How many groups? Set the bags." → Student sets container count
> **Prompt (2):** "How many in each bag?" → Student sets items per container

**Correct condition:** `{ container_count: 2 }` / `{ items_per_container: 3 }`
**Wrong branches (when spec identifies a known wrong answer):** one Medium per specific condition (fires on attempt 1 or 2), then generic `incorrect_count: 1`, `incorrect_count: 2`, `{}`
**Wrong branches (generic only):** `incorrect_count: 1`, `incorrect_count: 2`, `{}`

**Design note:** Specific conditions (e.g. "student reverses the two numbers") are pre-defined in the spec. Generic states must use `not` to explicitly exclude specific conditions — do not rely on evaluation order.

---

## Summary

| Tool | Toy | Correct keys | Wrong keys |
|---|---|---|---|
| `multiple_choice` | any | `selected` | `selected` per-distractor, `{}` |
| `click_category` | `picture_graph`, `bar_graph` | `selected` | `incorrect_count`, `{}` |
| `click_component` | `picture_graph`, `bar_graph` | `selected` | — |
| `click_to_place` | `picture_graph` | `category` + `symbols_placed` | `incorrect_count`, `{}` |
| `click_to_set_height` | `bar_graph` | `and: [{category, symbols}...]` | `incorrect_count`, `{}` |
| `place_tile` | `equation_builder` | `placed: {groups, items, total}` | `incorrect_count`, `{}` |
| `multi_select` | standalone | `and/or/not selected` | `and/or/not` (semantic), `{}` |
| `set_container_count` / `set_items_per_container` | `equal_groups` | `{ field: value }` | specific + `incorrect_count`, `{}` |
