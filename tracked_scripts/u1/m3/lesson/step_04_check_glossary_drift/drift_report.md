# UX/Script Terminology Drift Report

Generated: 2026-04-20 11:59  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 3

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Data Table and picture graph NOT` | `s2_7_comparison_question_bars_work_too` | ...) bars highlighted. Data Table and picture graph NOT visible. |
| `Emma` | `s3_2_complete_picture_graph` | ...filled (7 symbols). Emma, Noah, Olivia rows empty. |
| `Noah` | `s3_2_complete_picture_graph` | ...(7 symbols). Emma, Noah, Olivia rows empty. |
| `Olivia rows empty` | `s3_2_complete_picture_graph` | ...mbols). Emma, Noah, Olivia rows empty. |
| `Horizontal layout` | `s3_5_reading_axis_horizontal` | ...y=25. 4 categories. Horizontal layout. |
| `Both completed horizontal graphs` | `s3_8_final_check_what_s_same` | Both completed horizontal graphs visible (Books picture graph, Screen Time bar g |

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
| `template` | `Toys` | `visual` | `s3_6_bar_graph_independent_creation_horizontal` | ...orizontal bar graph template. Scale marked 0, 5, 10... up |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

| Assigned tool | Section | Snippet |
| ---|---|--- |
| `multiple_choice` | `s2_1_two_ways_show_scale_5` | "Where do you see the 5s on the bar graph?" |

---

## Section Detail

### `s2_1_two_ways_show_scale_5`

- **Tool fallback:** defaulted to `multiple_choice` — no rule matched
  > "Where do you see the 5s on the bar graph?"

### `s2_7_comparison_question_bars_work_too`

- **Unresolved:** `Data Table and picture graph NOT` in `visual`
  > ...) bars highlighted. Data Table and picture graph NOT visible.

### `s3_2_complete_picture_graph`

- **Unresolved:** `Emma` in `visual`
  > ...filled (7 symbols). Emma, Noah, Olivia rows empty.
- **Unresolved:** `Noah` in `visual`
  > ...(7 symbols). Emma, Noah, Olivia rows empty.
- **Unresolved:** `Olivia rows empty` in `visual`
  > ...mbols). Emma, Noah, Olivia rows empty.

### `s3_5_reading_axis_horizontal`

- **Unresolved:** `Horizontal layout` in `visual`
  > ...y=25. 4 categories. Horizontal layout.

### `s3_6_bar_graph_independent_creation_horizontal`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...orizontal bar graph template. Scale marked 0, 5, 10... up to 45.

### `s3_8_final_check_what_s_same`

- **Unresolved:** `Both completed horizontal graphs` in `visual`
  > Both completed horizontal graphs visible (Books picture graph, Screen Time bar graph).
