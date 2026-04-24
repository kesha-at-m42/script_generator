# UX/Script Terminology Drift Report

Generated: 2026-04-20 12:00  
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
| `Four real-world scenario illustrations` | `s1_2_real_world_bridge_where_do` | Four real-world scenario illustrations. A: Egg carton (2 rows, 6 eggs each). B:  |
| `Clean screen` | `s1_4_identity_building_closure` | Clean screen. Brief display of an expression `4 × 3`. |

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

### `s1_2_real_world_bridge_where_do`

- **Unresolved:** `Four real-world scenario illustrations` in `visual`
  > Four real-world scenario illustrations. A: Egg carton (2 rows, 6 eggs each). B: Parking lot (3 rows, 4 cars each). C:...

### `s1_4_identity_building_closure`

- **Unresolved:** `Clean screen` in `visual`
  > Clean screen. Brief display of an expression `4 × 3`.
