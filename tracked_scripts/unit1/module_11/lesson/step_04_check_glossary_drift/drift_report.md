# UX/Script Terminology Drift Report

Generated: 2026-04-10 13:07  
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
| `Brief visual of the word specification template appearing` | `s2_5_section_transition` | ...ion Builder clears. Brief visual of the word specification template appearing |

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
| `template` | `Toys` | `visual` | `s2_5_section_transition` | ...word specification template appearing. |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

| Assigned tool | Section | Snippet |
| ---|---|--- |
| `multiple_choice` | `s1_2_introduce_row_column_vocabulary` | "How many rows? (Rows go across.)" |

---

## Section Detail

### `s1_2_introduce_row_column_vocabulary`

- **Tool fallback:** defaulted to `multiple_choice` — no rule matched
  > "How many rows? (Rows go across.)"

### `s2_5_section_transition`

- **Unresolved:** `Brief visual of the word specification template appearing` in `visual`
  > ...ion Builder clears. Brief visual of the word specification template appearing.
- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...word specification template appearing.
