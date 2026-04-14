# UX/Script Terminology Drift Report

Generated: 2026-04-10 11:50  
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
| `Clean transition` | `s1_1_opening_frame` | Clean transition. Practice clears. |
| `Practice clears` | `s1_1_opening_frame` | Clean transition. Practice clears. |
| `Split screen` | `s1_2_real_world_array_to_dot` | Split screen. Left: Photo/illustration of a muffin tin (2 rows, 4 columns — 2×4  |
| `Then fades` | `s3_3_identity_building_closure` | ...and `5 × 3 = 15`). Then fades. A new array appears (4×3) with only a question |

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

### `s1_1_opening_frame`

- **Unresolved:** `Clean transition` in `visual`
  > Clean transition. Practice clears.
- **Unresolved:** `Practice clears` in `visual`
  > Clean transition. Practice clears.

### `s1_2_real_world_array_to_dot`

- **Unresolved:** `Split screen` in `visual`
  > Split screen. Left: Photo/illustration of a muffin tin (2 rows, 4 columns — 2×4 arrangement)...

### `s3_3_identity_building_closure`

- **Unresolved:** `Then fades` in `visual`
  > ...and `5 × 3 = 15`). Then fades. A new array appears (4×3) with only a question mark where the equations would...
