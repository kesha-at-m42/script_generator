# UX/Script Terminology Drift Report

Generated: 2026-04-15 14:20  
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
| `Side-by-side display` | `s1_2_representation_transfer` | ...(Mode 1: Reading). Side-by-side display. Same data: "Favorite Sports," 4 cate |
| `Favorite Sports` | `s1_2_representation_transfer` | ...isplay. Same data: "Favorite Sports," 4 categories, 1:1 scale. Picture graph  |
| `Both have` | `s1_2_representation_transfer` | ...bar graph on right. Both have visible keys/axis labels. Data Table not visibl |
| `Dogs` | `s2_1_pattern_discovery_type_a` | ...= Category labels (Dogs, Cats, Fish, Birds). Labels are display-only; student |
| `Cats` | `s2_1_pattern_discovery_type_a` | ...egory labels (Dogs, Cats, Fish, Birds). Labels are display-only; student clic |
| `Fish` | `s2_1_pattern_discovery_type_a` | ...labels (Dogs, Cats, Fish, Birds). Labels are display-only; student clicks to  |
| `Your class votes on a field trip destination` | `s3_1_real_world_bridge` | ...toy). Scenario 1: "Your class votes on a field trip destination." Scenario 2: |
| `Library tracks which book genre students check out most` | `s3_1_real_world_bridge` | ...tion." Scenario 2: "Library tracks which book genre students check out most." |
| `Cafeteria tracks which lunch is most popular` | `s3_1_real_world_bridge` | ...most." Scenario 3: "Cafeteria tracks which lunch is most popular." Multi-sele |
| `No graph toys active` | `s3_1_real_world_bridge` | ...Table not visible. No graph toys active. |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

| Toy type | Section |
| ---|--- |
| `multiple_choice` | `s3_1_real_world_bridge` |

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
| `toy` | `Mode value` | `visual` | `s3_1_real_world_bridge` | ...displayed (no graph toy). Scenario 1: "Your class votes o |
| `toy` | `Mode value` | `visual` | `s3_2_metacognitive_comparison_questions` | ...d as text (no graph toy active): "How many MORE students  |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_2_representation_transfer`

- **Unresolved:** `Side-by-side display` in `visual`
  > ...(Mode 1: Reading). Side-by-side display. Same data: "Favorite Sports," 4 categories, 1:1 scale. Picture graph on left,...
- **Unresolved:** `Favorite Sports` in `visual`
  > ...isplay. Same data: "Favorite Sports," 4 categories, 1:1 scale. Picture graph on left, bar graph on right. Both have...
- **Unresolved:** `Both have` in `visual`
  > ...bar graph on right. Both have visible keys/axis labels. Data Table not visible.

### `s2_1_pattern_discovery_type_a`

- **Unresolved:** `Dogs` in `visual`
  > ...= Category labels (Dogs, Cats, Fish, Birds). Labels are display-only; student clicks to select A, B, or...
- **Unresolved:** `Cats` in `visual`
  > ...egory labels (Dogs, Cats, Fish, Birds). Labels are display-only; student clicks to select A, B, or C. Da...
- **Unresolved:** `Fish` in `visual`
  > ...labels (Dogs, Cats, Fish, Birds). Labels are display-only; student clicks to select A, B, or C. Data Tab...

### `s3_1_real_world_bridge`

- **Unresolved:** `Your class votes on a field trip destination` in `visual`
  > ...toy). Scenario 1: "Your class votes on a field trip destination." Scenario 2: "Library tracks which book genre students check out most." Scenar...
- **Unresolved:** `Library tracks which book genre students check out most` in `visual`
  > ...tion." Scenario 2: "Library tracks which book genre students check out most." Scenario 3: "Cafeteria tracks which lunch is most popular." Multi-select enab...
- **Unresolved:** `Cafeteria tracks which lunch is most popular` in `visual`
  > ...most." Scenario 3: "Cafeteria tracks which lunch is most popular." Multi-select enabled. Data Table not visible. No graph toys active.
- **Unresolved:** `No graph toys active` in `visual`
  > ...Table not visible. No graph toys active.
- **Toy not in glossary:** `multiple_choice`
- **Deprecated alias:** `toy` → `Mode value` (in `visual`)
  > ...displayed (no graph toy). Scenario 1: "Your class votes on a field trip destination." Scenario 2: "Libr...

### `s3_2_metacognitive_comparison_questions`

- **Deprecated alias:** `toy` → `Mode value` (in `visual`)
  > ...d as text (no graph toy active): "How many MORE students chose dogs than cats?" and "How many FEWER stu...
