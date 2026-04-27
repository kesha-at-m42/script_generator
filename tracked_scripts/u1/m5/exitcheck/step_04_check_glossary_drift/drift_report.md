# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:52  
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
| `No Scale Preview System` | `s1_3_select_appropriate_scale_compare` | ...Cara: 90, Dan: 50. No Scale Preview System. No bar graph shown. |
| `No bar graph shown` | `s1_3_select_appropriate_scale_compare` | ...ale Preview System. No bar graph shown. |

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
| `toy` | `Mode value` | `visual` | `s1_1_scale_too_small_identify` | ...a Table displayed: "Toys Collected" — Amy: 45, Ben: 70, C |
| `toy` | `Mode value` | `guide` | `s1_1_scale_too_small_identify` | ...r friends collected toys for a donation drive. Ben collec |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_1_scale_too_small_identify`

- **Deprecated alias:** `toy` → `Mode value` (in `visual`)
  > ...a Table displayed: "Toys Collected" — Amy: 45, Ben: 70, Cora: 15, Dan: 30. Below it, four scale options...
- **Deprecated alias:** `toy` → `Mode value` (in `guide`)
  > ...r friends collected toys for a donation drive. Ben collected the most with 70 toys. Which scale works b...

### `s1_3_select_appropriate_scale_compare`

- **Unresolved:** `No Scale Preview System` in `visual`
  > ...Cara: 90, Dan: 50. No Scale Preview System. No bar graph shown.
- **Unresolved:** `No bar graph shown` in `visual`
  > ...ale Preview System. No bar graph shown.
