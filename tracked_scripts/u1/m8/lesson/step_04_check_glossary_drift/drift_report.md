# UX/Script Terminology Drift Report

Generated: 2026-04-20 12:01  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 8

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Same structure in both` | `s2_1_show_pattern_bags_boxes` | ...ps of 5 items each. Same structure in both. [RELATIONAL COMPARISON] designati |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

| Toy type | Section |
| ---|--- |
| `multiple_choice` | `s1_2_student_builds_with_method` |

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
| `template` | `Toys` | `visual` | `s1_1_transition_warmup_worked_example` | ...AMPLE] designation. Template shows `[___] × [___]` empty. |
| `methods c/d` | `place_tile` | `visual` | `s2_3_introducing_methods_c_d_tile` | ...+ Equation Builder (Methods C/D). Concrete context (boxes |
| `methods c/d` | `place_tile` | `visual` | `s2_4_student_builds_with_tiles_decomposed` | ...+ Equation Builder (Methods C/D). Concrete context (bags  |
| `methods c/d` | `place_tile` | `visual` | `s3_1_independent_tile_building` | ...+ Equation Builder (Methods C/D). Concrete context (boxes |
| `methods c/d` | `place_tile` | `visual` | `s4_1_circles_introduction_build` | ...+ Equation Builder (Methods C/D). Semi-abstract context ( |
| `methods c/d` | `place_tile` | `visual` | `s4_2_circles_varied_values` | ...+ Equation Builder (Methods C/D). Semi-abstract context ( |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_1_transition_warmup_worked_example`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...AMPLE] designation. Template shows `[___] × [___]` empty.

### `s1_2_student_builds_with_method`

- **Toy not in glossary:** `multiple_choice`

### `s2_1_show_pattern_bags_boxes`

- **Unresolved:** `Same structure in both` in `visual`
  > ...ps of 5 items each. Same structure in both. [RELATIONAL COMPARISON] designation.

### `s2_3_introducing_methods_c_d_tile`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Concrete context (boxes with items). 5 boxes with 2 items each. Tile palette...

### `s2_4_student_builds_with_tiles_decomposed`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Concrete context (bags with items). 2 bags with 4 items each. Tile palette sh...

### `s3_1_independent_tile_building`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Concrete context (boxes with items). 3 boxes with 5 items each. Tile palette...

### `s4_1_circles_introduction_build`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Semi-abstract context (circles with dots). 2 circles with 3 dots each. Tile p...

### `s4_2_circles_varied_values`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Semi-abstract context (circles with dots). 4 circles with 4 dots each. Tile p...
