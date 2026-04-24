# UX/Script Terminology Drift Report

Generated: 2026-04-20 12:00  
Source: `check_glossary_drift.json`  
Scope: Unit 1, Module 6

Discovery document — surfaces spec terminology that needs a glossary decision.
This does not block generation.

---

## Unresolved Visual Phrases

Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.
These likely represent concepts not yet in the glossary or toy_specs directory.

| Phrase | Section | Snippet |
| ---|---|--- |
| `Guide avatar` | `s2_2_worked_example_with_think_aloud` | ...ad 10, Burgers 15). Guide avatar appears. Question displayed: "How many more  |
| `Strategy statement` | `s2_3_strategy_naming` | Strategy statement appears on screen: **"Find the combined total first, then com |
| `Find the combined total first` | `s2_3_strategy_naming` | ...pears on screen: **"Find the combined total first, then compare."** |
| `Strategy statement re` | `s3_5_bridge_exit_check` | Graph clears. Strategy statement reappears: **"Find the combined total first, th |
| `Find the combined total first` | `s3_5_bridge_exit_check` | ...ement reappears: **"Find the combined total first, then compare."** |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

| Toy type | Section |
| ---|--- |
| `word_problems` | `s1_2_single_step_activation` |

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

### `s1_2_single_step_activation`

- **Toy not in glossary:** `word_problems`

### `s2_2_worked_example_with_think_aloud`

- **Unresolved:** `Guide avatar` in `visual`
  > ...ad 10, Burgers 15). Guide avatar appears. Question displayed: "How many more students chose pizza than tacos and...

### `s2_3_strategy_naming`

- **Unresolved:** `Strategy statement` in `visual`
  > Strategy statement appears on screen: **"Find the combined total first, then compare."**
- **Unresolved:** `Find the combined total first` in `visual`
  > ...pears on screen: **"Find the combined total first, then compare."**

### `s3_5_bridge_exit_check`

- **Unresolved:** `Strategy statement re` in `visual`
  > Graph clears. Strategy statement reappears: **"Find the combined total first, then compare."**
- **Unresolved:** `Find the combined total first` in `visual`
  > ...ement reappears: **"Find the combined total first, then compare."**
