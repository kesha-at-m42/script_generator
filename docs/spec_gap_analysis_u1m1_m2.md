# Spec Gap Analysis — Unit 1, Modules 1 & 2

**What this document covers:** Features and schema properties used in generated scripts (lesson, warmup, synthesis) that are not defined in the toy specs (`units/unit1/toy_specs.md`). Animations are excluded.

**Specs reviewed:** Picture Graph, Bar Graph, Data Table, Equation Builder  
**Scripts reviewed:**
- `outputs/unit1/lesson_generator_module_1/v21/step_04_merge_remediation/merge_remediation.json`
- `outputs/unit1/warmup_generator_module_1/v4/step_04_merge_remediation/merge_remediation.json`
- `outputs/unit1/synthesis_generator_module_1/v1/step_04_merge_remediation/merge_remediation.json`
- `outputs/unit1/lesson_generator_module_2/v1/step_04_merge_remediation/merge_remediation.json`
- `outputs/unit1/warmup_generator_module_2/v2/step_04_merge_remediation/merge_remediation.json`
- `outputs/unit1/synthesis_generator_module_2/v7/step_04_merge_remediation/merge_remediation.json`

---

## 1. Tangible Types — No Spec Exists

These `tangible_type` values appear in scripts but have no corresponding spec section.

| `tangible_type` | First seen | Description in script |
|---|---|---|
| `interactive_game` | M1 warmup `w1_data_collection` | Minis counting game with up/down counter buttons |
| `text_display` | M1 warmup `w2_symbol_selection`, `w3a–c` | Reference text displayed alongside graph |
| `data_collection_game` | M2 warmup `w1_data_collection` | Mario Party-style counting game (variant of M1 `interactive_game`) |
| `data_display` | M2 warmup `w2_prediction` | Results screen showing category/value pairs after counting game |
| `animation_canvas` | M2 warmup `w3_grouping_animation` | Workspace for the grouping → scaled graph transformation |
| `animation` | M2 synthesis `s5_4_closure` | Static frame from warmup grouping animation |

**Impact:** Engineering has no spec to build from for any of these. The grouping animation (`animation_canvas`) is pedagogically critical for M2's core concept introduction.

---

## 2. Student Interaction Tools — Not in Any Spec

These `tool` values appear in prompts but are not defined in any toy spec.

| Tool | First seen | Used for |
|---|---|---|
| `counter_input` | M1 warmup `w1` | Tracking counts in the Minis counting game (up/down buttons) |
| `multi_select` | M1 synthesis `s4_1`, `s4_3`; M2 synthesis `s5_2` | "Select all that apply" questions |
| `click_symbol` | M1 warmup `w2` | Selecting a symbol from the palette in creating mode |
| `click_component` | M1 lesson `s1_3`; M1 synthesis `s4_2`; M2 synthesis `s5_1` | Clicking named graph components (key, title, scale_toggle) |
| `click_to_place` | M2 lesson `s1_4`, `s1_5` | Placing symbols in creating mode (replaces `click_symbol` for M1) |
| `counting_game` | M2 warmup `w1` | Completing the data collection counting game |

**Note on `click_component`:** The Picture Graph spec describes a "Highlight" teaching action and a constraint that "Click categories (Mode 1): Any 1–2 categories." It does not define a student-facing interaction for clicking labeled components (key, title, A/B/C labels, scale_toggle). These are distinct interactions that need spec definitions.

**Note on `multi_select`:** The Equation Builder spec defines "Method A: Multiple Choice" (single select). `multi_select` is a different interaction type with no spec backing anywhere.

---

## 3. Schema Params — Not in Spec Vocab Tables

These params appear on defined tangible types but are absent from the spec's "Tool to Schema Vocab Translation" tables.

### 3a. `picture_graph` params

| Param | First seen | Notes |
|---|---|---|
| `key_visible` | M1 lesson, M1 warmup, M2 warmup | Spec says key is always visible when scale > 1, but `key_visible` is not in schema vocab |
| `title` | M1 lesson, synthesis | Not in picture graph schema vocab (mentioned contextually but never as a property) |
| `component_labels` | M1 synthesis `s4_2` | `{"A": "title", "B": "key", "C": "category_labels"}` overlay — not in spec |
| `selected_symbol` | M1 warmup `w2` | Set to `"student_choice"` after palette selection — not in schema vocab |
| `highlight_component` | M2 lesson `s1_2`, `s1_3`; M2 synthesis `s5_3` | Used as both an initial `params` field and an `update` params field; not in schema vocab |
| `highlight_categories` | M1 synthesis; M2 lesson; M2 synthesis | Update param for highlighting category rows — not in schema vocab |
| `highlight_categories: []` | M2 synthesis `s5_2` | Empty array used to clear highlighting — not in schema vocab |
| `key_text` | M2 warmup `w4` | Explicit string like `"Each ⭐ = 2"` — spec only references `scale_text` |
| `symbol_counts` | M2 warmup `w4` | Array of per-category symbol counts alongside `values` — not in schema vocab (spec has `placed_counts`) |
| `prefilled` | M2 lesson `s1_4` | Dict of pre-filled category → symbol count (e.g., `{"Pretzels": 5}`) — spec describes scaffolding levels conceptually but defines no schema param |

### 3b. `bar_graph` params

| Param | First seen | Notes |
|---|---|---|
| `axis_min` / `axis_max` | M1 lesson `s2_transition` onwards | Scripts use these; spec schema vocab defines `tick_marks: [0, 5, 10, ...]` instead |
| `axis_range` | M1 synthesis `s4_1` | `[0, 8]` — not in schema vocab |
| `axis_labels_visible` | M1 synthesis `s4_1` | Not in schema vocab |
| `highlight_categories` | M1 synthesis `s4_1` | Same issue as picture graph — not in schema vocab |

### 3c. `data_table` params

| Param | First seen | Notes |
|---|---|---|
| `display_mode` | M2 lesson (`"numeric"`) | Not in data table schema vocab (though Numeric vs Symbol Display modes are described in prose) |
| `orientation` | M2 lesson `s1_4` (`"vertical"`) | Not in data table schema vocab |
| `highlight_categories` | M2 lesson `s1_5` | Update param for highlighting rows — not in schema vocab |

---

## 4. New M2-Specific Features Without Spec Backing

### Scale toggle control on `picture_graph`

In M2 synthesis `s5_1`, the picture graph has a live **scale toggle** — a UI control letting the student switch between scale 1 and scale 2 while watching the graph update in real time.

```json
{
  "tool": "click_component",
  "target": "picture_graph_pets.scale_toggle"
}
```

The Picture Graph spec discusses scale as a fixed property and mentions scale comparison as a teaching action, but defines no interactive scale toggle control within the graph itself.

### Two simultaneous picture graphs

M2 synthesis `s5_3` places two picture graphs on screen at once (`picture_graph_pets_scale1` and `picture_graph_pets_scale2`) for side-by-side scale comparison.

**This directly conflicts with the Picture Graph spec's Layout Constraints:**

> Cannot appear with: Multiple picture graphs simultaneously | Only one at a time

The M3-M4 comparison layout defined in the spec pairs a picture graph with a **bar graph** — not two picture graphs.

---

## 5. Scene-Level Properties — Not Defined

| Property | Where | Notes |
|---|---|---|
| `type: "transition"` on scene objects | M1 synthesis `s4_opening`, `s4_closure`; M1 lesson `s2_transition`; M2 synthesis `s5_opening_frame`, `s5_4_closure` | No spec or schema doc defines scene types |

---

## Summary Table

| Category | Gap count | Highest priority |
|---|---|---|
| Tangible types with no spec | 6 | `interactive_game` / `data_collection_game`, `animation_canvas` |
| Student interaction tools not defined | 6 | `multi_select`, `click_to_place`, `click_component` |
| `picture_graph` params not in schema vocab | 10 | `prefilled`, `highlight_component`, `highlight_categories` |
| `bar_graph` params not in schema vocab | 4 | `axis_min`/`axis_max` vs. spec's `tick_marks` |
| `data_table` params not in schema vocab | 3 | `display_mode`, `orientation` |
| M2-specific unspecced features | 2 | Scale toggle control, two-simultaneous-picture-graph layout |
| Scene-level properties undefined | 1 | `type: "transition"` |
| **Spec constraint violations** | **1** | Two simultaneous picture graphs (M2 synthesis) |
