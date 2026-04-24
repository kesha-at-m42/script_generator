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

| Phrase | Section | Snippet |
| ---|---|--- |
| `Side-by-side arrangement` | `s1_1_judgment_noticing_task` | ...lizations (Mode 2). Side-by-side arrangement. Concrete context (bags with ite |
| `Single visualization` | `s2_1_personalization_recognition` | ...lizations (Mode 2). Single visualization. Concrete context (boxes with items) |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

| Toy type | Section |
| ---|--- |
| `multiple_choice` | `s1_1_judgment_noticing_task` |
| `multiple_choice` | `s2_1_personalization_recognition` |

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

### `s1_1_judgment_noticing_task`

- **Unresolved:** `Side-by-side arrangement` in `visual`
  > ...lizations (Mode 2). Side-by-side arrangement. Concrete context (bags with items). [NEW] initialization. Multiple Choice inte...
- **Toy not in glossary:** `multiple_choice`

### `s2_1_personalization_recognition`

- **Unresolved:** `Single visualization` in `visual`
  > ...lizations (Mode 2). Single visualization. Concrete context (boxes with items). [NEW] initialization. Multiple Choice int...
- **Toy not in glossary:** `multiple_choice`
