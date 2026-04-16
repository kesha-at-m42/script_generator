# UX/Script Terminology Drift Report

Generated: 2026-04-07 13:22  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 11

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Split screen` | `s1_3_equal_groups_vs_rectangular` | Split screen. Left side: The 3 bags of 5 from W.1 remain (clustered equal groups |
| `Same objects` | `s1_3_equal_groups_vs_rectangular` | ...lly and vertically. Same objects, different arrangement. |

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
| `template` | `Toys` | `visual` | `s1_2_equation_building_callback` | ...with full equation template: `[___] × [___] = [___]`. Til |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_2_equation_building_callback`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...with full equation template: `[___] × [___] = [___]`. Tile palette: 2, 3, 4, 5, 6, 8, 12, 14, 15, 16.

### `s1_3_equal_groups_vs_rectangular`

- **Unresolved:** `Split screen` in `visual`
  > Split screen. Left side: The 3 bags of 5 from W.1 remain (clustered equal groups). Right sid...
- **Unresolved:** `Same objects` in `visual`
  > ...lly and vertically. Same objects, different arrangement.
