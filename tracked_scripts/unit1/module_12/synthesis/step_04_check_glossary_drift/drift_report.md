# UX/Script Terminology Drift Report

Generated: 2026-04-10 16:06  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 12

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Split screen` | `s1_2_strategy_consolidation_two_proofs` | Split screen. Left side: A 4×5 array with highlighting demo — rows highlighted ( |
| `Both sides display their equations` | `s1_2_strategy_consolidation_two_proofs` | ...dates (5 × 4 = 20). Both sides display their equations. |
| `Reflection moment` | `s4_1_key_takeaway_metacognitive` | ...display — no array. Reflection moment. |

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

### `s1_2_strategy_consolidation_two_proofs`

- **Unresolved:** `Split screen` in `visual`
  > Split screen. Left side: A 4×5 array with highlighting demo — rows highlighted (4 × 5 = 20),...
- **Unresolved:** `Both sides display their equations` in `visual`
  > ...dates (5 × 4 = 20). Both sides display their equations.

### `s4_1_key_takeaway_metacognitive`

- **Unresolved:** `Reflection moment` in `visual`
  > ...display — no array. Reflection moment.
