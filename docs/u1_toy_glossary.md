# U1 Toy Glossary — Design Requirements

Consolidated from 48 scripts across U1 (12 modules × lesson / warmup / exitcheck / synthesis).
Organized by toy type. Each section covers: what the toy is, how it behaves, what interactions students have with it, and what the guide can animate on it.

**Coverage so far:** m1–m12 (all 48 files)

---

## picture_graph

A graph where each category is represented by symbols. The number of symbols per category depends on the scale: at scale 1, each symbol = 1 item; at scale 2, each symbol = 2 items; at scale 5, each symbol = 5 items. Values that don't divide evenly produce a **half-symbol** (e.g. 7 items at scale 2 = 3 full symbols + 1 half-symbol). Can appear in **reading** mode (pre-filled) or **creation** mode (student builds it). Orientation can be **vertical** or **horizontal**.

**Scales seen:** 1, 2, 5

---

### Student Interactions

#### `click_category`
Student clicks a category to answer a question about the graph (most popular, least popular, matches a condition).
- Validator checks: `{ "selected": "<category_name>" }`
- Examples: "Select the category with the most votes" → Apples; "Which animal has fewer than 4?" → Elephants; "Select the category with the most books" → James

#### `click_categories`
Student clicks all categories that apply to answer a question about the graph (all that qualify, all needed for a calculation).
- Validator checks: `{ "and": [{ "selected": "A" }, { "selected": "B" }] }`
- Example: "Which categories do you need to answer this question?" → Dogs + Fish

#### `click_component`
Student clicks on a named sub-part of the graph rather than a category. Used to teach graph anatomy.
- Target uses dot notation: `picture_graph_id.component_name`
- Validator checks: `{ "selected": "<component_name>" }` — component is identified by name (e.g. `key`) or by letter label (e.g. `A`, `B`, `C`) when the scene overlays lettered markers on parts
- Components seen: `key` · `scale_toggle` (interactive control; validator is `{}` — any click completes it) · letter labels `A`/`B`/`C` (when the scene overlays lettered markers)
- Examples:
  - "Click on the part that tells us what each symbol means" → key
  - "Which component is the key?" (labeled A/B/C) → B
  - "Toggle the scale" → scale_toggle (no specific value; action itself is the answer)

#### `build_category`
Student builds a category by setting its symbol count to represent a data value. Reinforces the translation from number → symbols. Supports half-symbols for odd values at scale 2 (e.g. 9 items = 4.5 symbols).
- Tool field aliases seen: `click_to_place` · `click_place_symbols` · `click_to_set_height`
- Validator checks: `{ "symbols_placed": <number> }` or `{ "category": "<name>", "symbols_placed": <number> }` or `{ "and": [...] }` for multi-category prompts
- Examples:
  - "Place 4 symbols for Popcorn" → symbols_placed: 4
  - "Place symbols for Maya's 9 books" → symbols_placed: 4.5 (half-symbol)
  - "Set the number of symbols for Liam" (35 books, scale 5) → symbols_placed: 7
  - "Set lengths for all remaining categories" → Emma: 4, Noah: 5, Olivia: 8

#### `select_scale`
Student chooses a scale to see how it changes the graph representation. Selecting a different scale triggers an animation that updates all symbol counts while keeping the underlying data constant — building the concept that scale affects display, not data.
- Validator checks: `{ "selected": <scale_number> }`
- Example: "Toggle to scale 1" → 1; "Toggle to scale 2" → 2; "Toggle back to 5" → 5

---

### Guide Animations

> **Design principle:** animations are atomic and can fire simultaneously. Compound effects are expressed as two events triggered at the same time (e.g. `highlight_key` + `annotate_key`) rather than as a single compound event name.

---
**Highlight**

#### `highlight`
Pulses and holds a specific element. Valid targets:

- **`title`** — graph title text. Often sequenced with `labels` and `key` when teaching graph anatomy.
- **`labels`** — category labels along the axis or side.
- **`key`** — the key/legend element. Almost always fires simultaneously with `annotate_key`.
- **`scale_value`** — the scale number inside the key; zooms and pulses to emphasize the current scale.
- **`category`** — one or more category columns/rows stay highlighted. Often paired with `count(symbols)` to show a running count inside the highlight.
- **`symbol`** — one symbol, all symbols in one category, or all symbols across the graph. **Sequential variant:** `highlight_symbol_sequentially` — symbols light up one at a time; use when counting through a category before a value question.
- **`component`** — a named or letter-labeled sub-part of the graph (e.g. `key`, `A`, `B`). General-purpose; subsumes `highlight_key` when the target is identified by label rather than role.

---
**Annotate**

#### `annotate_key`
**Animation:** A callout text bubble appears on or beside the key, explicitly stating what one symbol represents (e.g. "Each star = 5"). Distinct from the key itself, which only shows the symbol icon — `annotate_key` adds a spoken-aloud-style text overlay that makes the scale value explicit as a sentence.

**Example use:** Always fires simultaneously with `highlight_key` — "Key highlights while annotation reads: Each star = 5."

---
**Demonstrate**

#### `demonstrate_half_symbol`
**Animation:** Inside or beside the key, a full symbol appears with label "2" and a half-symbol appears with label "1" — teaching that half a symbol equals half the scale value.

**Example use:** Teaching half-symbol concept: `demonstrate_half_symbol` — "Key animates: full symbol labeled '2', half-symbol labeled '1'." Fires after `highlight_key` + `annotate_key` to deepen understanding.

#### `demonstrate_scale`
**Animation:** One symbol expands to reveal the individual items it represents inside it.

**Example use:** Introducing scale of 2: `highlight_key` + `demonstrate_scale` — "Key pulses, then one star expands to show 2 items inside it — making the scale concrete."

#### `demonstrate_skip_counting`
**Animation:** Groups (or symbols) highlight sequentially with running skip-count labels, teaching the pattern before asking a value question. Distinct from `count(symbols_by_scale)` in that the emphasis is on the count pattern itself rather than reading a specific category's total.

**Example use:** Introducing scale-5 reading: `demonstrate_skip_counting` — "5 groups highlight one by one: 5, 10, 15, 20, 25."

---
**Count**

#### `count`
Illuminates symbols in a category one at a time with a running label. Options:

- **`symbols`** — count by 1s (1, 2, 3…). Use for scale-1 graphs or when counting raw symbol count.
- **`symbols_by_scale`** — skip-count by the scale value (2, 4, 6… or 5, 10, 15…). Use when reading a scaled graph where each symbol represents more than 1.

---
**Show**

#### `show_scale_multiplication`
**Animation:** After symbols in a category are counted, a multiplication equation appears as an overlay on the graph showing: symbol count × scale = real total. This is an annotation on the picture_graph itself — not the equation_builder widget — and fires in context of reading a specific category.

**Example use:** Reading a scale-2 graph: `count(symbols)` → `show_scale_multiplication` — "Bus row: 4 symbols counted, then 4 × 2 = 8 appears."

#### `show_addition`
**Animation:** Two highlighted values are combined and their sum appears as an equation. Same animation as bar_graph `show_addition`.

**Example use:** Combining two category totals: `show_addition` — "Birds: 7, Deer: 6, then 7 + 6 = 13 appears." Used as the final step of `count_and_combine_categories` and `demonstrate_addition`.

#### `show_difference`
**Animation:** Two categories highlight and a subtraction equation labels the difference between them. Same animation as bar_graph `show_difference`.

**Example use:** Unscaled compare: `highlight_category` (both) + `show_difference` — "Fish (4) and Dogs (7) highlighted; 7 - 4 = 3 shown."

#### `show_comparison`
**Animation:** A reference value (from a prior step) visually extends to align with another category, with the gap between them labeled. Same animation as bar_graph `show_comparison`. Distinct from `show_difference` — use `show_comparison` in two-step problems where a step-1 total is being compared against a new category; use `show_difference` for direct category-to-category comparisons.

**Example use:** Two-step problem step 2: `show_comparison` — "Step-1 result (11) extends against Green bar (4), gap of 7 labeled."

---
**Compare**

#### `compare`
Spreads targets apart so value labels can appear on each group. Valid targets:

- **`symbols`** — full symbols and half-symbol in a category spread apart; full symbols labeled with their combined count (e.g. "6"), half-symbol labeled with its value (e.g. "1"). Used before a sum to make mixed-symbol composition visible. Usually fires simultaneously with `annotate_key`.

---
**Place / Confirm**

#### `place_symbols`
**Animation:** Guide places symbols one at a time into a category, each placement highlighted as it lands.

**Example use:** Modeling correct placement after wrong answer: `place_symbols` — "4 symbols placed in Popcorn column one at a time." Followed by `confirm_placement`.

#### `place_remaining_symbols`
**Animation:** Guide fills all remaining empty categories simultaneously in one event, including half-symbols where needed. Distinct from `place_symbols` (which fills one category at a time) — use this when the guide demonstrates completing the whole graph at once, not one category.

**Example use:** Modeling full graph completion: `place_remaining_symbols` — "James: 6 full, Sofia: 3 full + 1 half, Aiden: 5 full + 1 half."

#### `confirm_placement`
**Animation:** Symbols lock into place in a category with a confirm visual after correct student placement. Same animation as bar_graph `confirm_placement` and equation_builder `confirm_placement`.

> These are guide animations fired *after* the validator has already confirmed correctness — they provide student-facing visual acknowledgment of a right answer. Separate from validation logic.

**Example use:** After correct `build_category` response: `confirm_placement` — "3 symbols lock into Slides column." See also `confirm_all` for full-graph confirmation.

#### `confirm_all`
**Animation:** All symbols across the entire graph lock into place, confirming a completed build. Same animation as bar_graph `confirm_all`.

**Example use:** After student completes the last category: `confirm_all` — "7 symbols lock into Liam row, completing the graph."

---
**Scale / Transform**

#### `scale_toggle_transform`
**Animation:** All symbol counts across the graph animate simultaneously to reflect the new scale — columns multiply or shrink while data stays constant. Key updates to show the new scale value.

**Example use:** After `select_scale`: `scale_toggle_transform` — "Olivia goes from 8 symbols (scale 5) to 40 symbols (scale 1). Key updates to Each star = 1."

#### `transform_to_bar_graph`
**Animation:** The picture graph morphs into a bar graph — symbol columns become bars, axis appears with numeric labels.

**Example use:** Transitioning between graph types in the same lesson: `transform_to_bar_graph` — "Same Animals at the Zoo data; bars replace symbol columns, axis 0–8 appears."

---
**Compound Sequences**

#### `count_and_scale_symbols`
**Compound sequence:**
1. `count(symbols)` — symbols illuminate one at a time with a running count
2. `demonstrate_scale` (per symbol) — each symbol splits open to reveal the items inside, arriving at the real total

**Example use:** Bridging symbol count to real value on a scale-2 graph: `count_and_scale_symbols` — "7 Crackers symbols counted, then each splits into 2 votes: total 14."

#### `introduce_scale`
**Compound sequence:** Shows how individual items group into symbols, making scale concrete.
1. Items appear in a category one at a time (raw count, before any grouping)
2. `items_group_by_scale` — items self-organize into equal groups matching the scale value
3. `groups_transform_to_symbols` — each group morphs into a single symbol icon; symbols stack into the column

**Example use:** Introducing scale-of-5 for the first time: `introduce_scale(scale=5)` — "20 individual items appear for Swings, organize into 4 groups of 5, then 4 star symbols stack in the column."

#### `introduce_half_symbol`
**Compound sequence:** Shows what happens when items don't divide evenly, motivating the half-symbol.
1. `items_group_by_scale_with_remainder` — items group into equal pairs, leaving one leftover visibly unpaired. Text: "3 groups of 2, but 1 more — what do we do with that 1?"
2. The leftover item pulses to draw attention to it
3. `demonstrate_half_symbol_solution` — leftover transforms into a half-symbol with a text overlay explaining the conversion. Text: "3 full symbols + 1 half-symbol = 7 total"
4. `show_half_symbol_solution` + `highlight_key` + `annotate_key` — completed category with full symbols + half-symbol; key highlights with annotation. Text: "Half of 2 is 1. 7 = [3 full] + [1 half]"

**Example use:** Introducing half-symbols at scale 2: `introduce_half_symbol` — "7 items: 3 groups of 2 with 1 leftover. Leftover pulses, transforms into half-star. Key shows Each star = 2; 3 full symbols + half-symbol = 7."

#### `comparison_demonstration`
**Compound sequence:**
1. `count(symbols)` — count symbols in category A one by one
2. `count(symbols)` — count symbols in category B one by one
3. `show_difference` — highlight both categories and show the subtraction equation

For scaled graphs, replace steps 1–2 with `count(symbols_by_scale)` (skip-counts by the scale value instead).

**Example use:** Full walkthrough of a scaled comparison: "Emma counted (5,10,15,20), Olivia counted (5…40), difference of 20 displayed."

#### `show_comparison_calculation`
**Compound sequence:** Full workflow for a "how many more/fewer" problem on a scaled graph — reads both category values through the scale, then shows the difference. The distinguishing feature vs. `count(symbols_by_scale)` alone: it also resolves the multiplication and ends with an explicit difference equation.
1. `count(symbols_by_scale)` — skip-count symbols in category A
2. `show_scale_multiplication` — show symbol count × scale = real total for A
3. `count(symbols_by_scale)` — skip-count symbols in category B
4. `show_scale_multiplication` — show symbol count × scale = real total for B
5. `show_difference` — highlight both totals and show the subtraction equation

**Example use:** Modeling a scaled "how many fewer" answer: "Birds: 3.5 × 2 = 7; Squirrels: 5 × 2 = 10; 10 - 7 = 3." Also: "Crackers: 7 × 2 = 14; Popcorn: 4 × 2 = 8; 14 - 8 = 6."

#### `count_and_combine_categories`
**Compound sequence:**
1. `count(symbols)` — count symbols in category A one by one
2. `count(symbols)` — count symbols in category B one by one
3. `show_addition` — display the sum of both counts

For scaled graphs, replace steps 1–2 with `count(symbols_by_scale)` (skip-counts by scale value instead).

**Example use:** Unscaled combine: "Birds: 7 symbols counted, Deer: 6 counted, then 7 + 6 = 13." Scaled: "Maya: 9 symbols, Sofia: 7 symbols, 9 + 7 = 16."

#### `demonstrate_addition`
**Compound sequence:**
1. `count(symbols_by_scale)` — skip-count symbols in category A
2. `show_scale_multiplication` — show symbol count × scale = real total for A
3. `count(symbols_by_scale)` — skip-count symbols in category B
4. `show_scale_multiplication` — show symbol count × scale = real total for B
5. `show_addition` — display the sum of both scaled totals

**Example use:** Scaled "in all" question: "James: 6 × 2 = 12; Aiden: 5.5 × 2 = 11; 12 + 11 = 23."

---

## bar_graph

A graph where each data value is represented by a solid bar. The bar's height (vertical) or length (horizontal) is read against a numbered axis. The axis itself encodes the scale — for scale-of-5 graphs, the axis counts by 5s (0, 5, 10, 15…); for scale-of-1 graphs, the axis counts by 1s. Can appear in **reading** mode (pre-filled) or **creation** mode (student builds it). Orientation can be **vertical** or **horizontal**.

**Scales seen:** 1 (axis by 1s), 5 (axis by 5s), 10 (axis by 10s)

---

### Student Interactions

#### `click_category`
Student clicks on a bar to identify it as the answer. Used for "most," "least," or "find this bar" prompts.
- Validator checks: `{ "selected": "<category_name>" }`
- Examples: "Click on the Monkeys bar" → Monkeys; "Who read the fewest books?" → Maya; "Which color is most popular?" → Blue

#### `select_scale`
Student selects a scale from the bar graph's scale selector (same semantics as picture_graph `select_scale`).
- Tool field: `click_scale_button`
- Validator checks: `{ "selected": <scale_number> }`
- Example: "Which scale should we use?" → 10

#### `build_bar`
Student builds a bar by setting its height (vertical) or length (horizontal) to represent a data value. Reinforces the translation from number → bar height against the axis. Can cover one or multiple bars in a single prompt.
- Tool field aliases seen: `click_to_set_height`
- Validator checks:
  - Single bar: `{ "bar": "<category>", "height": <number> }` or `{ "bar_height": <number>, "category": "<name>" }`
  - Multi-bar: `{ "bars": { "Cat1": v1, "Cat2": v2 } }` or `{ "and": [{ "bar_height": { "category": "X", "value": n } }, ...] }` or `{ "bars_set": { "Cat1": v1, "Cat2": v2 } }`
- Examples:
  - "Set the height for Pizza to show 20" → bar: Pizza, height: 20
  - "Set Salad and Pasta bars" → Salad: 15, Pasta: 25
  - "Set all four bars" → Saturday: 35, Sunday: 30, Monday: 40, Tuesday: 25

---

### Guide Animations

---
**Highlight**

#### `highlight_axis_numbers`
Axis numbers highlight in sequence from 0 upward, showing the skip-counting pattern.
> *"Axis numbers highlight in sequence: 0, 5, 10, 15, 20, 25, 30, tracing the skip-counting pattern."*

**Targeted variant:** `highlight_axis_sequence` — same animation but stops at a specific target value. Use when directing attention to a particular bar's value: "Highlights from 0 to 25, pausing at each interval."

**Alias:** `highlight_axis_intervals`, `highlight_skip_counting_sequence` — same animation; use `highlight_axis_numbers` as the canonical name.

#### `highlight_bar`
One bar pulses and stays highlighted — used to direct attention to a specific category before or after a question.
> *"Monkeys bar highlights."*

**Example use:** Directing attention to an answer: `highlight_bar` — "Monkeys bar highlights as the answer to 'which has the most?'" `highlight_shortest_bar` is a specific variant of this.

#### `highlight_shortest_bar`
The shortest bar pulses and highlights as the answer to a "fewest" question. Specific variant of `highlight_bar`.
> *"Maya's bar pulses and is highlighted as the shortest bar on the graph."*

#### `highlight_gap`
The portion of the taller bar that extends above the shorter bar is highlighted, making the difference visible as a region.
> *"Ava's bar at 50 and Noah's bar at 25 — the upper 25-unit region of Ava's bar highlights."*

**Example use:** Atomic pair for difference questions: `highlight_gap` + `show_difference` — "Gap region highlights, then label '25' appears."

#### `highlight_bars_at_lines`
Bars whose tops align exactly with a gridline highlight to draw attention to the "easy-to-read" bars.
> *"Markers (30) and Paintbrushes (20) bars highlight — both tops land exactly on gridlines."*

**Example use:** Always followed immediately by `highlight_bars_between_lines` — "Easy bars first, then harder ones." These two always fire as a pedagogical pair: show what's easy, then show what requires estimation. If there's no need to contrast the two types, use `highlight_bar` instead.

#### `highlight_bars_between_lines`
Bars whose tops fall between two gridlines highlight, making the point that these require estimation.
> *"Crayons (45) and Glue Sticks (55) bars highlight — both tops land between gridlines."*

**Example use:** Always immediately follows `highlight_bars_at_lines` — see above.

---
**Draw**

#### `draw_bar_guideline`
A horizontal (or vertical) line draws from the top of a bar to the axis, landing on the value to show how to read bar height.
> *"Horizontal line draws from top of Monkeys bar perpendicular to vertical axis. Value 7 highlights on axis."*

#### `draw_bar_guidelines`
Draws guidelines for multiple bars simultaneously.
> *"Horizontal guidelines draw from the end of each bar to the axis, confirming Saturday 35, Sunday 30, Monday 40, Tuesday 25."*

#### `draw_all_bars`
All bars draw to their correct heights at once, with guidelines from each bar end to the axis.
> *"All four bars draw to their correct heights: Saturday to 35, Sunday to 30, Monday to 40, Tuesday to 25. Guidelines draw from each bar end to the axis value."*

---
**Show**

#### `show_difference`
Labels the numeric difference between two bars. Same animation as picture_graph `show_difference`.
> *"Animation shows Blue bar at 8 and Yellow bar at 6, then '2' appears between them."*

**Example use:** Fires simultaneously with `highlight_gap` — gap region visible + difference labeled together.

#### `show_addition`
Two bars are highlighted in sequence and their combined total is displayed. Same animation as picture_graph `show_addition`.
> *"Yellow bar shows 6, Red bar shows 5, visual addition 6+5=11 appears."*

#### `show_comparison`
A reference value (often a prior-step result) is visually extended against a bar to show the gap between them. Same animation as picture_graph `show_comparison`. Distinct from `show_difference` (which labels the gap between two co-present values) — `show_comparison` is used in two-step problems where step-1 produced a total that is now being placed against a new bar.
> *"Green bar (4) extends to match against the total 11, showing difference of 7."*

#### `show_halfway_gridline`
A ghost (dashed or faint) gridline appears between two axis marks at the midpoint, marking the half-interval value.
> *"A ghost gridline appears at 45, halfway between the 40 and 50 marks."*

**Example use:** Reading a between-lines bar: `show_halfway_gridline` — "Ghost gridline at 45 pulses, showing 40 + 5 = 45."

---
**Label**

#### `label_bar_values`
Value labels appear on each highlighted bar, showing their numeric amounts.
> *"Ben's bar labeled 5, Cara's bar labeled 6."*

**Example use:** Simultaneously with `show_addition` — "Ben (5) and Cara (6) bars labeled, then 5 + 6 = 11 appears."

---
**Fill / Confirm**

#### `fill_bar`
Guide fills a bar from 0 to a target height, demonstrating correct placement. The bar-fill animation makes it clear how height maps to value.
> *"System demonstrates: Swings bar fills from 0 up to 30, then stops."*

**Example use:** After wrong answer or as modeling: `fill_bar` — "Nonfiction bar fills from 0 to 60, endpoint aligns with the 60 gridline." Followed by `confirm_placement`.

#### `confirm_placement`
A single bar locks into place with a confirm visual after correct student placement. Same animation as picture_graph `confirm_placement` and equation_builder `confirm_placement`.
> *"Swings bar confirms at height 30 — bar pulses and locks."*

> Fired *after* the validator has confirmed correctness — provides student-facing visual acknowledgment. Separate from validation logic.

**Example use:** After correct `build_bar` response: `confirm_placement`. See also `confirm_all` for full-graph confirmation.

#### `confirm_all`
All bars across the graph confirm simultaneously after completing the last placement. Same animation as picture_graph `confirm_all`.
> *"All four bars confirm simultaneously: Monday 40, Tuesday 35, Wednesday 50, Thursday 25."*

---
**Scale & Axis**

#### `populate_bars_with_overflow`
All bars draw to their correct heights, but at least one bar extends beyond the axis top boundary, with a warning indicator showing the data cannot be fully read.
> *"Aisha (20), Ben (35), Carlos (55) bars draw. Dana's bar (80) extends past the top at 50 — warning indicator appears."*

**Example use:** Teaching why scale matters: `populate_bars_with_overflow` → `extend_axis_upward` — "First show the problem, then solve it."

#### `extend_axis_upward`
The axis grows upward, new tick marks appearing sequentially to accommodate data that exceeded the previous range.
> *"Axis extends: 55, 60, 65, 70, 75, 80 tick marks appear. Axis now shows 0 to 80."*

#### `compare_all_scales`
A preview panel animates through all scale options, showing tick mark density for each, to illustrate efficiency trade-offs.
> *"Scale 1: 60 tick marks. Scale 2: 30 marks. Scale 5: 12 marks. Scale 10: 6 marks — fewest and most readable."*

**Example use:** Choosing a scale: `compare_all_scales` — "All four scales compared side by side by tick-mark count."

#### `demonstrate_scale_exploration`
Guide clicks each scale button in sequence, each showing the graph state briefly, demonstrating how to evaluate options before committing. Distinct from `scale_toggle_transform` (PG): that is the graph-update animation that fires on a single scale selection; this is the guide-driven walkthrough of all options before one is chosen.
> *"System clicks Scale 1, 2, 5, 10 in order — each displays briefly with a checkmark."*

---
**Compound Sequences**

#### `demonstrate_halfway_reading`
**Compound sequence:**
1. `highlight_axis_numbers` — the two adjacent axis marks around the target value glow in sequence
2. `show_halfway_gridline` — a ghost gridline appears at the midpoint between them, making the half-interval readable

> *"30 mark glows, 40 mark glows, then ghost gridline appears at 35. Leo's bar endpoint aligns with the 35 mark."*

---

## equal_groups

A visual grouping toy displaying N identical containers (circles, bags, boxes, a shelf), each holding the same number of items. Used in m7–m10 to make equal groups concrete before connecting to multiplication. The student can build it interactively (setting container count and items-per-container) or the guide can populate it.

**Variants seen:** `equal_groups_circles` · `equal_groups_bags` · `equal_groups_boxes` · `equal_groups_shelf` · `equal_groups_build` (interactive build target) · `equal_groups_builder`

---

### Student Interactions

#### `set_container_count`
Student sets how many groups (containers) to display.
- Validator checks: `{ "container_count": <number> }`
- Example: "Make 3 groups" → container_count: 3

#### `set_items_per_container`
Student sets how many items go in each group.
- Validator checks: `{ "items_per_container": <number> }`
- Example: "Put 4 items in each group" → items_per_container: 4

---

### Guide Animations

> **Atomic pairs:** most count/highlight animations combine `highlight_containers_sequentially` + `count_items_in_container`. Compound sequence events are just these atomics fired in order.

#### `containers_appear`
Empty containers appear one at a time, ready to be filled.
> *"3 bags appear on screen, empty."*

#### `items_populate`
Items appear inside each container simultaneously.
> *"4 items appear in each of the 3 bags."*

**Example use:** After `containers_appear`: `containers_appear` → `items_populate` — "Empty bags appear, then fill."

#### `highlight_containers_sequentially`
Containers highlight one at a time in sequence, counting through the number of groups.
> *"Bags highlight: 1, 2, 3, 4."*

#### `zoom_container` / `focus_container`
One container zooms in or highlights so the items inside are visible and countable.
> *"First bag zooms in. Items inside are visible."*

#### `count_items_in_container`
Items inside one container highlight one at a time with a running count label.
> *"Items in one box highlight sequentially: 1, 2, 3, 4, 5."*

#### `open_one_container`
One container opens, revealing its items which then highlight sequentially.
> *"One box opens. Items inside highlight one by one as they are counted."*

#### `count_containers_then_items`
**Compound sequence:**
1. `highlight_containers_sequentially` — containers highlight one at a time, counting the number of groups
2. `count_items_in_container` — items inside one container highlight one at a time, counting items per group

> *"5 circles highlight: 1, 2, 3, 4, 5. Then one circle's 3 dots count: 1, 2, 3."*

#### `demonstrate_expression`
**Compound sequence:**
1. `highlight_containers_sequentially` — containers highlight to show the group count
2. `count_items_in_container` — items in one container highlight to show items per group
3. Multiplication expression appears (e.g., `2 × 5`)

> *"2 boxes highlight. One box's 5 items highlight. Expression '2 × 5' appears."*

#### `demonstrate_equal_groups`
Shows that each group contains the same count by highlighting containers in sequence, each labeled with its item count.
> *"Each bag highlights in turn: showing 4, 4, 4."*

#### `set_containers_with_narration`
Guide places containers one at a time with count narration.
> *"System sets container count to 2. Two bags appear one at a time."*

#### `fill_containers_with_narration`
Guide fills each container with items one at a time, narrating as it goes.
> *"Each bag fills: items appear one at a time until all bags contain 3."*

#### `transform_from_symbols`
Picture graph symbols transform into equal-group containers, each revealing the items inside. Bridges graph scale to multiplication.
> *"4 picture graph symbols morph into 4 bags, each revealing 5 items — showing 4 × 5."*

#### `build_groups_sequentially`
Groups appear one at a time, each adding to a running cumulative total counter.
> *"3 stacks of 5: first stack appears (total: 5), second (total: 10), third (total: 15)."*

**Example use:** Skip-counting through groups: `build_groups_sequentially` — "Each new group appears as the running count increments."

#### `reveal_cluster`
One cluster of items appears and highlights, with a running count label showing the cumulative total so far.
> *"First cluster of 5 birds reveals and highlights. Running count: 5."*

**Example use:** Building towards a total incrementally: `reveal_cluster` fired N times — "Each cluster reveals in turn: 5, 10, 15, 20, 25."

#### `count_items_sequentially`
Items are counted continuously across all groups in order — the count does not reset between groups.
> *"First shelf items count 1–8, then second shelf continues 9–16."*

---

## equation_builder

An interactive equation widget with slots for the two factors and the product (e.g., `___ × ___ = ___`). Students drag number tiles from a palette into the correct slots. Used in m8–m9 to connect equal-groups representations to multiplication notation.

**Tangible IDs seen:** `equation_builder` · `equation_builder_pencils` · `equation_builder_6x2` · `equation_builder_5s` · `equation_builder_warmup`

---

### Student Interactions

#### `place_tile`
Student drags number tiles into factor/product slots.
- Validator checks: `{ "placed": { "groups": n, "items": m } }` for factor-only, or `{ "placed": { "groups": n, "items": m, "total": p } }` for all three slots, or `{ "placed": { "total": p } }` for product slot only
- Examples:
  - "Place the two factors" → groups: 2, items: 4
  - "Complete the equation" → groups: 6, items: 2, total: 12
  - "Place the product" → total: 15

---

### Guide Animations

#### `highlight_slot`
A slot in the equation builder glows, directing attention to where the next tile goes.
> *"First slot glows with subtle 'groups' label."*

#### `highlight_first_number` / `highlight_second_number`
First or second factor in the built equation highlights.
> *"Factor 4 highlights in '4 × 5'."*

#### `demonstrate_tile_placement`
Guide drags a tile from the palette to the correct slot, demonstrating the placement action.
> *"Guide drags 5 tile from palette to first slot. Tile snaps into position."*

#### `confirm_all`
Full equation confirms after all slots are filled correctly. Same animation as picture_graph `confirm_all` and bar_graph `confirm_all`. Also seen as `confirm_equation` (same event).
> *"Equation 6 × 2 = 12 confirms with a brief pulse."*

#### `model_placement`
**Compound sequence:**
1. `demonstrate_tile_placement` — guide places factor 1 tile into its slot
2. `demonstrate_tile_placement` — guide places factor 2 tile into its slot
3. `demonstrate_tile_placement` — guide places product tile into its slot

Each step pauses briefly before the next. Also known as `place_tiles_sequentially`.

> *"6 in first slot, 5 in second slot, 30 in product slot — each pauses before the next."*

#### `display_labels`
"Factor / Factor / Product" labels briefly appear above the respective slots or tiles.
> *"Labels appear: 'factor' under 7, 'factor' under 2, 'product' under 14."*

#### `model_skip_counting`
**Compound sequence:**
1. Skip-count animation — increments by the items-per-group value N times (one beat per group)
2. `confirm_placement` — product slot fills with the final result

> *"Skip-counting by 10s six times: 10, 20, 30, 40, 50, 60. Product slot fills with 60."*

#### `confirm_placement`
A single tile locks into its slot with a confirmation pulse. Same animation as picture_graph `confirm_placement` and bar_graph `confirm_placement`.
> *"Tile 32 locks into the product slot. Equation reads 8 × 4 = 32."*

#### `rearrange_to_reversed`
The equation animates from A × B = C format to C = A × B, teaching that the equals sign means both sides are the same value.
> *"Equation rearranges: 3 × 4 = 12 fades, 12 = 3 × 4 appears."*

---

## arrays

A rectangular grid of dots (or objects) arranged in rows and columns. Used in m11–m12 to introduce and explore the commutative property: rotating the array shows that N rows of M = M rows of N. Can be pre-built (reading mode) or student-built via `row_builder` or `column_builder`.

**Tangible IDs seen:** `arrays_dots` · `array_5x4` · `arrays_3x5` · `row_builder`

---

### Student Interactions

#### `add_row`
Student adds rows one at a time to build the array (via `row_builder` tangible).
- Validator checks: `{ "rows": <number> }`
- Example: "Make an array with 4 rows" → rows: 4

#### `add_item_per_row`
Student sets the number of items in each row.
- Validator checks: `{ "items_per_row": <number> }`
- Example: "Put 6 in each row" → items_per_row: 6

#### `add_row_and_item_per_row`
Both Row + and Items per Row + buttons are active; student may tap either in any order.
- Validator checks: `{ "rows": <number>, "items_per_row": <number> }`
- Example: "Build an array with 3 rows of 5" → rows: 3, items_per_row: 5

#### `add_column`
Student adds columns one at a time to build the array (via `column_builder` tangible).
- Validator checks: `{ "columns": <number> }`
- Example: "Make an array with 4 columns" → columns: 4

#### `add_item_per_column`
Student sets the number of items in each column.
- Validator checks: `{ "items_per_column": <number> }`
- Example: "Put 3 in each column" → items_per_column: 3

#### `add_column_and_item_per_column`
Both Column + and Items per Column + buttons are active; student may tap either in any order.
- Validator checks: `{ "columns": <number>, "items_per_column": <number> }`
- Example: "Build an array with 5 columns of 4" → columns: 5, items_per_column: 4

---

### Guide Animations

#### `highlight_rows`
Rows highlight one at a time (horizontally) to draw attention to the row structure.
> *"4 rows highlight sequentially."*

**Sequential variant:** `highlight_rows_sequentially` — each row highlights and holds before the next, for stronger emphasis.

#### `highlight_columns`
Columns highlight one at a time (vertically) to draw attention to the column structure.
> *"5 columns highlight sequentially."*

**Sequential variant:** `highlight_columns_sequentially` — each column highlights and holds before the next, for stronger emphasis.

#### `count_rows`
Rows count sequentially with a running label.
> *"System counts rows: 1, 2. Then counts dots in one row: 1 … 7."*

**Example use:** Reading array dimensions: `count_rows` → `count_by_rows` — "Count how many rows, then count per row."

#### `count_by_rows`
Highlights each row in sequence while a cumulative count increments by the row length.
> *"Row 1 highlights: 3. Row 2: 6. Row 3: 9. Row 4: 12. Row 5: 15. Row 6: 18."*

#### `trace_alignment`
Traces horizontal lines across rows and vertical lines down columns to reveal the grid structure.
> *"Horizontal lines trace across each row, then vertical lines trace down each column — showing perfect alignment."*

#### `rotate_array`
The entire array rotates 90° to show the same dots in a transposed orientation, demonstrating commutativity.
> *"4×3 array rotates 90° — becomes 3×4. Same dots, different orientation."*

**Example use:** Teaching commutativity: `rotate_array` — "5 rows of 6 rotates to 6 rows of 5 — product stays 30."

#### `count_all_dots`
All dots in the array pulse simultaneously to emphasize the total count.
> *"All 20 dots pulse — total stays 20 after rotation."*

#### `highlight_rows_and_columns`
Both rows and columns highlight with grid lines to show the 2D structure simultaneously.
> *"Image A highlights with visible row and column lines showing a 2×6 structure."*

---

## equation

A static, read-only display — no student interaction, no tool. Used in three ways:

- **Single equation** — one expression on screen (e.g. `4 × 2 = 8`)
- **Step-1 result** (alias: `text_display`) — a floating equation placed by the guide to hold a prior result visible while the student solves a follow-up (e.g. "Yellow + Red = 11" stays on screen for the "how many more?" step)
- **Products strip** — a horizontal row of multiple `equation` instances showing a skip-count sequence (e.g. 1×5=5, 2×5=10, 3×5=15…)

No student interactions. Single equation and step-1 result variants have no guide animations.

---

### Guide Animations (products strip only)

#### `skip_count_sequence`
Equations in the strip highlight one at a time in order.
> *"5 pulses, then 10, then 15 — each product highlighted in turn."*

#### `group_by_twos`
Each product splits to show it forms equal groups of 2 with no remainder.
> *"Each product animates into pairs of 2."*

#### `show_factors`
Factor pair labels appear above each product.
> *"Each product labeled: 1×10, 2×10, 3×10… 10×10."*

---

## data_table

A simple table showing category names and their raw numeric values. Displayed alongside graphs as a read-only reference so students can cross-check symbols or bars against the source data.

No student interactions.

---

### Guide Animations

#### `highlight_value`
**Animation:** A specific value cell in the data table highlights.

**Example use:** Connecting table value to graph in remediation: `highlight_value` — "Value 7 for Birds highlights in the data table."

---

#### `demonstrate_symbol_calculation`
**Animation:** Highlights a value in the table and shows inline how many symbols it requires — full symbols for the even part, plus a half-symbol for any remainder.

**Example use:** Teaching half-symbols: `demonstrate_symbol_calculation` — "Emma collected 9 stickers: 4 full symbols show 8, plus half-symbol shows 1 more." Fires before or alongside the student's `build_category` prompt.

---

## sorting_area

A drag-and-drop sorting surface divided into labeled zones. Students drag word problems, scenarios, or examples into the correct zone to categorize them. Used for conceptual classification tasks — e.g., sorting problems into "JUST COMPARE" vs. "COMBINE FIRST."

**Appears in:** m6/synthesis

---

### Student Interactions

#### `drag_to_sort`
Student drags one or more items into labeled zones. Each item is dragged independently; the validator checks the final placement of each.
- Validator checks: `{ "placed": { "zone_a": ["item_1"], "zone_b": ["item_2", "item_3"] } }`
- Example: "Sort these problems: which ones compare and which combine first?" → problem_1 → JUST COMPARE; problem_2, problem_3 → COMBINE FIRST

---

### Guide Animations

#### `demonstrate_sort`
Guide drags items one at a time to demonstrate the correct sorting before asking the student to try.
> *"System drags problem_1 to JUST COMPARE zone, then problem_2 and problem_3 to COMBINE FIRST zone."*

---

## dropdown_fillin

A sentence-frame response widget with one or more inline fill blanks. Each blank is linked to an option palette; the student selects an option to fill it in. Used for structured short-answer responses embedded in a sentence stem.

No guide animations.

---

### Student Interactions

#### `select_fill_option`
Student selects an option from the palette to fill a blank in the sentence frame.
- Validator checks: `{ "selected": "<option_text>" }`
- Example: "The graph with fewer symbols uses scale ___" → selected: "5"

---

## image

A static image displayed for real-world connection or context. No student interactions and no guide animations — display only.

---

## Cross-toy Interactions

#### `select_one_option`
Student picks one answer from a list of numbers or short strings. Appears on any toy. Used for reading a value off a graph, answering compare (how many more/fewer) questions, answering combine (in all/together) questions, and conceptual questions about scale or graph structure.
- Validator checks: `{ "selected": <number_or_string> }`
- Examples on picture_graph:
  - "How many monkeys at the zoo?" → 7
  - "How many votes did Crackers get?" → 14 (scale 2, 7 symbols × 2)
  - "How many sightings does 3 and a half symbols show?" → 7
  - "How many animals were Birds and Deer in all?" → 13
  - "Which scale uses the fewest symbols?" → Scale of 5
- Examples on bar_graph:
  - "How many books did Sofia read?" → 5
  - "How many more Blue than Yellow?" → 2
  - "Yellow + Red in all?" → 11
  - "What's the height of the Slides bar?" → 15
  - "What comes after 20 on this axis?" → 25

---

#### `drag_to_sort`
Student drags items into labeled zones to classify them. See `sorting_area` toy section for full details.

---

#### `select_all_options`
Student selects all options from a text list that apply. Used for conceptual/reflection questions — "which of these statements is true?", "which scenarios would use a graph?". Not tied to a specific toy; the options are text, not graph categories.
- Validator checks: `{ "and": [{ "selected": "option text A" }, { "selected": "option text B" }, { "not_selected": "wrong option" }] }`
- Examples:
  - "Which statements about these two graphs are true?" → "They have the same title" + "They show the same categories" + "Soccer has the most in both"
  - "Which scenarios would a graph help organize?" → three real-world scenarios

---

#### `select_toy`
Student selects one toy from 2–4 displayed side-by-side based on a criterion. Used when the reasoning targets the toy as a whole rather than something within it. Applies to any toy type. Tool field alias: `click_tangible`.
- Target: array of tangible_ids `["toy_a", "toy_b"]` or up to 4
- Validator checks: `{ "selected": "<tangible_id>" }`
- Examples:
  - "Which graph uses fewer symbols to show the same data?" → picture_graph_books (scale-2 over scale-1)
  - "Which graph has scale of 10?" → bar_graph_scale_10 (from 4 bar graphs at scales 1/2/5/10)

---

#### `click_category (multi-target)`
A derivative of `click_category` used when two side-by-side graphs show the same data and the student must locate the same category on either one. The student's click counts as correct regardless of which toy they clicked.

- **Applies to:** `picture_graph` and `bar_graph` only (the two toys that share category-based interaction)
- **Target:** array of two tangible IDs — `"target": ["tangible_id_1", "tangible_id_2"]`
- **Validator:** `{ "selected": "<category_name>" }` — condition checks only the category name, not which toy was clicked
- **Example:** "Both graphs show 40 for Yellow Items. Can you find where?" → target: `["picture_graph_scale_10", "bar_graph_scale_10"]`, correct condition: `{ "selected": "Yellow Items" }`
- **Seen in:** m4/warmup `s3_1_picture_bar_bridge_1_10` — picture graph and bar graph displayed side-by-side, student locates the same category on either

---

## Tool Taxonomy (quick reference)

| Tool | Interaction | Validator condition shape |
|---|---|---|
| `select_one_option` | Pick one from a list — cross-toy | `{ "selected": value }` |
| `select_all_options` | Select all that apply from a text list — cross-toy, conceptual questions | `{ "and": [{ "selected": A }, { "not_selected": wrong }] }` |
| `click_categories` | Select multiple categories that apply | `{ "and": [{ "selected": A }, { "selected": B }] }` |
| `click_category` | Click a column or row on a graph | `{ "selected": "category_name" }` |
| `click_category (multi-target)` | Click the named category on either of two side-by-side graphs — picture_graph and bar_graph only | `{ "selected": "category_name" }` with `"target": ["id1", "id2"]` |
| `click_component` | Click a named sub-part of a toy (e.g. key) | `{ "selected": "component_name" }` |
| `select_toy` | Select one of 2–4 toys displayed side-by-side based on a criterion — cross-toy | `{ "selected": "tangible_id" }` |
| `drag_to_sort` | Drag items into labeled zones — on `sorting_area` toy | `{ "placed": { "zone": ["item"] } }` |
| `build_category` | Build a picture graph category by setting its symbol count | `{ "symbols_placed": n }` or `{ "category": "x", "symbols_placed": n }` |
| `build_bar` | Build a bar graph category by setting its height or length | `{ "bar": "x", "height": n }` or `{ "bars": { ... } }` |
| `select_scale` | Choose a scale to explore how it changes the graph representation | `{ "selected": scale_number }` |
| `set_container_count` | Set how many groups in an equal_groups toy | `{ "container_count": n }` |
| `set_items_per_container` | Set items per group in an equal_groups toy | `{ "items_per_container": n }` |
| `place_tile` | Drag number tiles into equation_builder factor/product slots | `{ "placed": { "groups": n, "items": m, "total": p } }` |
| `add_row` | Add rows to a row_builder (arrays) | `{ "rows": n }` |
| `add_item_per_row` | Set items per row in a row_builder | `{ "items_per_row": n }` |
| `add_row_and_item_per_row` | Both row and items-per-row buttons active — either tap completes | `{ "rows": n, "items_per_row": m }` |
| `add_column` | Add columns to a column_builder (arrays) | `{ "columns": n }` |
| `add_item_per_column` | Set items per column in a column_builder | `{ "items_per_column": n }` |
| `add_column_and_item_per_column` | Both column and items-per-column buttons active — either tap completes | `{ "columns": n, "items_per_column": m }` |
| `select_fill_option` | Select an option to fill a blank in a `dropdown_fillin` sentence frame | `{ "selected": "option_text" }` |
