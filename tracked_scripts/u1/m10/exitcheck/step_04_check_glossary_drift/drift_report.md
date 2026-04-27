# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:53  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 10

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Construction area starts empty` | `s1_3_solve_1st_factor_unknown` | ...5 equals 15 total." Construction area starts empty. \+/- group control availa |

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
| `template` | `Toys` | `visual` | `s1_1_build_complete_equation_variety_visual` | ...uation Builder with template `[___] × [___] = [___]`. Til |
| `template` | `Toys` | `visual` | `s1_3_solve_1st_factor_unknown` | ...der with pre-filled template: `☐ × 5 = 15`. Language prom |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_1_build_complete_equation_variety_visual`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...uation Builder with template `[___] × [___] = [___]`. Tile palette: `2`, `3`, 4, `5`, `6`, 9, 12, 15, 18, 20...

### `s1_3_solve_1st_factor_unknown`

- **Unresolved:** `Construction area starts empty` in `visual`
  > ...5 equals 15 total." Construction area starts empty. \+/- group control available (each new group pre-set to 5 items per the equati...
- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...der with pre-filled template: `☐ × 5 = 15`. Language prompt: "\*\*\_ stacks of 5 equals 15 total." Construct...
