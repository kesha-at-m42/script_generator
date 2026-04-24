# UX/Script Terminology Drift Report

Generated: 2026-04-20 11:59  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 8

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

_None found._

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
| `methods c/d` | `place_tile` | `visual` | `s1_1_build_expression_boxes` | ...+ Equation Builder (Methods C/D). Concrete context (boxes |
| `methods c/d` | `place_tile` | `visual` | `s1_3_build_expression_circles` | ...+ Equation Builder (Methods C/D). Semi-abstract context ( |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_1_build_expression_boxes`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Concrete context (boxes with cookies/markers). 3 boxes with 4 items each. Til...

### `s1_3_build_expression_circles`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...+ Equation Builder (Methods C/D). Semi-abstract context (circles with dots). 5 circles with 3 dots each. Tile p...
