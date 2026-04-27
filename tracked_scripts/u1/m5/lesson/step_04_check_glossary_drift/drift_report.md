# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:54  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 5

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Scale Preview System with all four buttons` | `s2_1_all_scales_fit_small_data` | ...: 19, Jar D: 23   * Scale Preview System with all four buttons. Horizontal ba |
| `Initially no graph showing` | `s2_1_all_scales_fit_small_data` | ...izontal bar graphs. Initially no graph showing. |

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

### `s2_1_all_scales_fit_small_data`

- **Unresolved:** `Scale Preview System with all four buttons` in `visual`
  > ...: 19, Jar D: 23
  * Scale Preview System with all four buttons. Horizontal bar graphs. Initially no graph showing.
- **Unresolved:** `Initially no graph showing` in `visual`
  > ...izontal bar graphs. Initially no graph showing.
