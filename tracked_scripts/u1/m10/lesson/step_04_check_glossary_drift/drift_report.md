# UX/Script Terminology Drift Report

Generated: 2026-04-27 10:54  
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
| `Construction area starts empty` | `s3_2_first_factor_unknown_student_constructs` | ...0 equals 40 total." Construction area starts empty. \+/- group control availa |

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
| `template` | `Toys` | `visual` | `s1_1_quick_equation_build_setup_sign` | ...uation Builder with template `[___] × [___] = [___]`. Til |
| `template` | `Toys` | `visual` | `s1_3_guided_practice_reversed_form` | ...ilder with REVERSED template: `[___] = [___] × [___]`. Ti |
| `template` | `Toys` | `guide` | `s1_3_guided_practice_reversed_form` | ...hing different. The template is flipped — product comes F |
| `template` | `Toys` | `visual` | `s1_4_independent_practice_standard_reversed` | ...uation Builder with template `[___] × [___] = [___]`. Til |
| `template` | `Toys` | `visual` | `s2_1_context_variety_announcement_worked_example` | ...uation Builder with template `[___] × [___] = [___]`. Til |
| `template` | `Toys` | `visual` | `s2_4_product_unknown_reversed_form` | ...ilder with REVERSED template, pre-filled: `☐ = 5 × 7`. Pa |
| `template` | `Toys` | `visual` | `s3_1_first_factor_unknown_skip_counting` | ...der with pre-filled template: `☐ × 5 = 20`. Language prom |
| `template` | `Toys` | `visual` | `s3_2_first_factor_unknown_student_constructs` | ...der with pre-filled template: `☐ × 10 = 40`. Language pro |

---

## Tool Inferred by Fallback

No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.
Review these sections: the correct tool may be something else.

_None found._

---

## Section Detail

### `s1_1_quick_equation_build_setup_sign`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...uation Builder with template `[___] × [___] = [___]`. Tile palette: `2, 3, 4, 5, 6, 7, 8, 10, 12, 14`.

### `s1_3_guided_practice_reversed_form`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...ilder with REVERSED template: `[___] = [___] × [___]`. Tile palette: 3, 4, `6`, `7`, 8, 11, 16, 20, 21, 24.
- **Deprecated alias:** `template` → `Toys` (in `guide`)
  > ...hing different. The template is flipped — product comes FIRST this time. Remember, equals means same value a...

### `s1_4_independent_practice_standard_reversed`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...uation Builder with template `[___] × [___] = [___]`. Tile palette: `3, 4, 5, 6, 7, 10, 16, 18, 24, 28`.

### `s2_1_context_variety_announcement_worked_example`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...uation Builder with template `[___] × [___] = [___]`. Tile palette: `3`, `4, 8, 9, 10, 12, 24, 27, 30, 36`.

### `s2_4_product_unknown_reversed_form`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...ilder with REVERSED template, pre-filled: `☐ = 5 × 7`. Palette: `12, 30, 35, 42`.

### `s3_1_first_factor_unknown_skip_counting`

- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...der with pre-filled template: `☐ × 5 = 20`. Language prompt displayed above Equation Builder: "\*\*\_ groups...

### `s3_2_first_factor_unknown_student_constructs`

- **Unresolved:** `Construction area starts empty` in `visual`
  > ...0 equals 40 total." Construction area starts empty. \+/- group control available (each new group pre-set to 10 items per the equat...
- **Deprecated alias:** `template` → `Toys` (in `visual`)
  > ...der with pre-filled template: `☐ × 10 = 40`. Language prompt: "\*\*\_ groups of 10 equals 40 total." Constru...
