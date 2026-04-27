# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:54  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 9

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Warmup` | `s1_1_extend_accumulation_5_10_concrete` | ...ing) 5 circles from Warmup visible (or re-displayed). Products Strip shows: ` |
| `Products Strip still` | `s1_3_bridge_pattern_check_concrete_relational` | Products Strip still visible. Equation Builder resets to show: `5 × 2 = 10`. Con |
| `Highlighting shown of the ones digit of all numbers on the Products Strip` | `s2_3_5s_discovery_partial_worked_example` | Highlighting shown of the ones digit of all numbers on the Products Strip. |
| `No Context Visualization` | `s2_4_student_builds_full_equation_5s` | ...11, 20, 25, 30, 35. No Context Visualization. Products Strip from 2.3 may rem |
| `UX decision` | `s2_4_student_builds_full_equation_5s` | ...visible or fade per UX decision. |
| `Products Strip` | `s3_1_10s_discovery_computation_application_new` | ...all numbers on the Products Strip. |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

_None found._

---

## Tools Inferred but Not in Glossary

These `tool` values were inferred but have no canonical entry in the glossary.
They may need a new glossary entry.

_None found._

---

## Deprecated Spec Aliases Used

These terms appeared in raw spec text and match a renamed or superseded alias.
The spec writer used an older name — the canonical replacement is shown.

| Spec term | Canonical name | Field | Section | Snippet |
| ---|---|---|---|--- |
| `template` | `Toys` | `visual` | `s2_1_worked_example_first_full_equation` | ...pears with expanded template: `[___] × [___] = [___]`. Th |
| `methods c/d` | `place_tile` | `visual` | `s2_4_student_builds_full_equation_5s` | ...[___] = [___]` with Methods C/D active. Tile palette: 4,  |
| `methods c/d` | `place_tile` | `visual` | `s3_2_graph_scale_callback_10_application` | ...actors pre-filled). Methods C/D active. |
| `methods c/d` | `place_tile` | `visual` | `s3_3_10_independent_computation_application_reinforcement` | ...Factors pre-filled. Methods C/D active. Tile palette: 10, |
| `methods c/d` | `place_tile` | `visual` | `s3_4_independent_equation_building_full_construction` | ...three slots empty). Methods C/D active. Tile palette: 5,  |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

| Assigned tool | Section | Snippet |
| ---|---|--- |
| `multiple_choice` | `s1_3_bridge_pattern_check_concrete_relational` | "When you multiply any number by 2, is the product even or odd?" |

---

## Section Detail

### `s1_1_extend_accumulation_5_10_concrete`

- **Unresolved:** `Warmup` in `visual`
  > ...ing) 5 circles from Warmup visible (or re-displayed). Products Strip shows: `[2] [4] [6] [8] [10]`. Equati...

### `s1_3_bridge_pattern_check_concrete_relational`

- **Unresolved:** `Products Strip still` in `visual`
  > Products Strip still visible. Equation Builder resets to show: `5 × 2 = 10`. Context Visualization s...
- **Tool fallback:** defaulted to `multiple_choice` — no rule matched
  > "When you multiply any number by 2, is the product even or odd?"

### `s2_1_worked_example_first_full_equation`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...pears with expanded template: `[___] × [___] = [___]`. Three slots visible. = sign is fixed (not a tile). Fi...

### `s2_3_5s_discovery_partial_worked_example`

- **Unresolved:** `Highlighting shown of the ones digit of all numbers on the Products Strip` in `visual`
  > Highlighting shown of the ones digit of all numbers on the Products Strip.

### `s2_4_student_builds_full_equation_5s`

- **Unresolved:** `No Context Visualization` in `visual`
  > ...11, 20, 25, 30, 35. No Context Visualization. Products Strip from 2.3 may remain visible or fade per UX decision.
- **Unresolved:** `UX decision` in `visual`
  > ...visible or fade per UX decision.
- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...[___] = [___]` with Methods C/D active. Tile palette: 4, 5, 6, 11, 20, 25, 30, 35. No Context Visualization. Pr...

### `s3_1_10s_discovery_computation_application_new`

- **Unresolved:** `Products Strip` in `visual`
  > ...all numbers on the Products Strip.

### `s3_2_graph_scale_callback_10_application`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...actors pre-filled). Methods C/D active.

### `s3_3_10_independent_computation_application_reinforcement`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...Factors pre-filled. Methods C/D active. Tile palette: 10, 16, 30, 50, 60, 70.

### `s3_4_independent_equation_building_full_construction`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...three slots empty). Methods C/D active. Tile palette: 5, 9, 10, 14, 45, 50, 90, 95.
