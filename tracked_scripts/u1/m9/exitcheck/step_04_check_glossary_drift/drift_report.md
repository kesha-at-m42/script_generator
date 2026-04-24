# UX/Script Terminology Drift Report

Generated: 2026-04-20 12:00  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 9

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
| `methods c/d` | `place_tile` | `visual` | `s1_2_build_full_visual_2_create` | ...three slots empty). Methods C/D active. Tile palette: 2,  |
| `methods c/d` | `place_tile` | `visual` | `s1_3_build_full_10_equation_create` | ...three slots empty). Methods C/D active. Tile palette: 4,  |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_2_build_full_visual_2_create`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...three slots empty). Methods C/D active. Tile palette: 2, 4, 5, 6, 8, 10, 12, 14.

### `s1_3_build_full_10_equation_create`

- **Deprecated alias:** `methods c/d` → `place_tile` (in `visual`)
  > ...three slots empty). Methods C/D active. Tile palette: 4, 5, 10, 14, 20, 30, 40, 50.
