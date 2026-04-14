# UX/Script Terminology Drift Report

Generated: 2026-04-13 19:02  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 7

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Build Mode Interface` | `s1_3_student_builds_first_build_mode` | Build Mode Interface. Empty workspace. |
| `Empty workspace` | `s1_3_student_builds_first_build_mode` | ...ild Mode Interface. Empty workspace. |
| `Build Mode Interface` | `s1_4_build_with_notation` | Build Mode Interface. Empty workspace initially. |
| `Empty workspace initially` | `s1_4_build_with_notation` | ...ild Mode Interface. Empty workspace initially. |

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

| Assigned tool | Section | Snippet |
| ---|---|--- |
| `multiple_choice` | `s2_2_reduced_scaffolding_product_intro` | "How many groups? How many in each?" |

---

## Section Detail

### `s1_3_student_builds_first_build_mode`

- **Unresolved:** `Build Mode Interface` in `visual`
  > Build Mode Interface. Empty workspace.
- **Unresolved:** `Empty workspace` in `visual`
  > ...ild Mode Interface. Empty workspace.

### `s1_4_build_with_notation`

- **Unresolved:** `Build Mode Interface` in `visual`
  > Build Mode Interface. Empty workspace initially.
- **Unresolved:** `Empty workspace initially` in `visual`
  > ...ild Mode Interface. Empty workspace initially.

### `s2_2_reduced_scaffolding_product_intro`

- **Tool fallback:** defaulted to `multiple_choice` — no rule matched
  > "How many groups? How many in each?"
