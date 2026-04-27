# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:53  
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
| `Animation is smooth` | `s2_1_grouping_animation_reveal` | ...containing 5 items. Animation is smooth, visual continuation ("Those symbols  |
| `Simple text screen` | `s4_1_bridge_lesson` | Simple text screen. Reference to the three contexts just experienced. |
| `Reference to the three contexts just experienced` | `s4_1_bridge_lesson` | Simple text screen. Reference to the three contexts just experienced. |

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

### `s2_1_grouping_animation_reveal`

- **Unresolved:** `Animation is smooth` in `visual`
  > ...containing 5 items. Animation is smooth, visual continuation ("Those symbols were hiding groups inside").

### `s4_1_bridge_lesson`

- **Unresolved:** `Simple text screen` in `visual`
  > Simple text screen. Reference to the three contexts just experienced.
- **Unresolved:** `Reference to the three contexts just experienced` in `visual`
  > Simple text screen. Reference to the three contexts just experienced.
