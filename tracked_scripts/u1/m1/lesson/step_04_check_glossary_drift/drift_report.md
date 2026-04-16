# UX/Script Terminology Drift Report

Generated: 2026-04-14 11:46  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 1

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `NEW graph` | `s2_4_horizontal_bar_graph` | ...(Mode 1: Reading). NEW graph. Horizontal orientation. Context: "Favorite Colo |
| `Favorite Colors` | `s2_4_horizontal_bar_graph` | ...entation. Context: "Favorite Colors," 4 categories. Axis 0–10 by 1s, labeled  |
| `Number of Votes` | `s2_4_horizontal_bar_graph` | ...–10 by 1s, labeled "Number of Votes." Values: Blue=8, Red=5, Green=4, Yellow= |
| `Guide speaks` | `s3_1_how_many_more_subtract` | ...Yellow (6) bars as Guide speaks. |
| `Data Table not` | `s3_5_what_information_needed` | ...Birds=6, Lizards=1. Data Table not visible. |
| `Cats` | `s3_6_solving_with_selected_data` | ...and Fish (4) only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not  |
| `Birds` | `s3_6_solving_with_selected_data` | ...ish (4) only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not visib |
| `Lizards dimmed/unhighlighted` | `s3_6_solving_with_selected_data` | ...only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not visible. |

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

_None found._

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s2_4_horizontal_bar_graph`

- **Unresolved:** `NEW graph` in `visual`
  > ...(Mode 1: Reading). NEW graph. Horizontal orientation. Context: "Favorite Colors," 4 categories. Axis 0–10 by...
- **Unresolved:** `Favorite Colors` in `visual`
  > ...entation. Context: "Favorite Colors," 4 categories. Axis 0–10 by 1s, labeled "Number of Votes." Values: Blue=8, Red...
- **Unresolved:** `Number of Votes` in `visual`
  > ...–10 by 1s, labeled "Number of Votes." Values: Blue=8, Red=5, Green=4, Yellow=6. Data Table visible.

### `s3_1_how_many_more_subtract`

- **Unresolved:** `Guide speaks` in `visual`
  > ...Yellow (6) bars as Guide speaks.

### `s3_5_what_information_needed`

- **Unresolved:** `Data Table not` in `visual`
  > ...Birds=6, Lizards=1. Data Table not visible.

### `s3_6_solving_with_selected_data`

- **Unresolved:** `Cats` in `visual`
  > ...and Fish (4) only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not visible.
- **Unresolved:** `Birds` in `visual`
  > ...ish (4) only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not visible.
- **Unresolved:** `Lizards dimmed/unhighlighted` in `visual`
  > ...only. Cats, Birds, Lizards dimmed/unhighlighted. Data Table not visible.
