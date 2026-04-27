# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:53  
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
| `Strategy statement` | `s1_0_opening_frame` | ...transition screen. Strategy statement appears: "Find the combined total first |
| `Find the combined total first` | `s1_0_opening_frame` | ...statement appears: "Find the combined total first, then compare." |
| `Maya` | `s3_1_real_world_bridge_type_c` | ...more stickers—just Maya, or Ben and Carlos put together?"   2. "Which team sc |
| `Red team alone` | `s3_1_real_world_bridge_type_c` | ...eam scored more—the Red team alone, or the Blue and Green teams combined?"    |
| `Strategy statement remains` | `s4_1_metacognitive_reflection_type_1_strategy` | Strategy statement remains visible: "Find the combined total first, then compare |
| `Find the combined total first` | `s4_1_metacognitive_reflection_type_1_strategy` | ...t remains visible: "Find the combined total first, then compare." |
| `Brief celebratory visual or clean screen` | `s4_2_identity_building_closure` | ...gy statement fades. Brief celebratory visual or clean screen. |

---

## Toys Resolved but Not in Glossary

`toy_spec_loader` matched these to a spec file, but they have no canonical entry
in the glossary's Canonical Toys table. They may need a new glossary entry.

| Toy type | Section |
| ---|--- |
| `word_problems` | `s3_1_real_world_bridge_type_c` |

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

### `s1_0_opening_frame`

- **Unresolved:** `Strategy statement` in `visual`
  > ...transition screen. Strategy statement appears: "Find the combined total first, then compare."
- **Unresolved:** `Find the combined total first` in `visual`
  > ...statement appears: "Find the combined total first, then compare."

### `s3_1_real_world_bridge_type_c`

- **Unresolved:** `Maya` in `visual`
  > ...more stickers—just Maya, or Ben and Carlos put together?"
  2. "Which team scored more—the Red team alo...
- **Unresolved:** `Red team alone` in `visual`
  > ...eam scored more—the Red team alone, or the Blue and Green teams combined?"
  3. "Did I spend more on only snacks,...
- **Toy not in glossary:** `word_problems`

### `s4_1_metacognitive_reflection_type_1_strategy`

- **Unresolved:** `Strategy statement remains` in `visual`
  > Strategy statement remains visible: "Find the combined total first, then compare."
- **Unresolved:** `Find the combined total first` in `visual`
  > ...t remains visible: "Find the combined total first, then compare."

### `s4_2_identity_building_closure`

- **Unresolved:** `Brief celebratory visual or clean screen` in `visual`
  > ...gy statement fades. Brief celebratory visual or clean screen.
