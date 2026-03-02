# Lesson Script Schema Guide

Reference for the `lesson.json` script format. Covers every field, beat type, condition shape, and naming convention.

---

## Top-Level Structure

```json
{
  "id": "lesson_1_7",
  "sections": [ ... ]
}
```

| Field | Type | Description |
|---|---|---|
| `id` | string | Lesson identifier, e.g. `lesson_1_7` |
| `sections` | array | Ordered list of all sections (main, transition, remediation) |

---

## Section

```json
{
  "id": "s1_1_most_votes",
  "type": "remediation",
  "workspace": ["pg_fruits", "data_table"],
  "steps": [ [...], [...] ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique section ID — see [Naming Conventions](#section-id-naming-conventions) |
| `type` | string | no | `"transition"` or `"remediation"`. Omit for normal sections. |
| `workspace` | string[] | no | Tangible IDs visible on screen throughout this section |
| `steps` | array[] | yes | Array of steps; each step is an array of beats |

### Section ID Naming Conventions

```
s{major}_{minor}_{slug}            →  s1_1_most_votes
s{major}_{slug}                    →  s2_transition
{parent_id}_light/medium/heavy     →  s1_1_light
{parent_id}_step{n}_light/medium/heavy  →  s3_4c_step2_light
```

Remediation IDs always end in `_light`, `_medium`, or `_heavy` and mirror their parent section ID:

| Parent | Remediations |
|---|---|
| `s1_1_most_votes` | `s1_1_light`, `s1_1_medium`, `s1_1_heavy` |
| `s2_2_books_sofia` | `s2_2_books_sofia_light`, `s2_2_books_sofia_medium`, `s2_2_books_sofia_heavy` |
| `s3_4c_two_step` (multi-prompt) | `s3_4c_step1_light`, `s3_4c_step2_light`, `s3_4c_step2_medium`, `s3_4c_step2_heavy` |

---

## Steps

`steps` is an **array of arrays**. Each inner array is one step — a group of beats that play together before the lesson pauses for student interaction.

```json
"steps": [
  [beat, beat, beat],   // step 1 — scene setup + dialogue + prompt
  [beat, beat]          // step 2 — follow-up after correct answer
]
```

---

## Beat Types

### Dialogue

Narration or teacher speech. Editable in Notion (💬 callout).

```json
{
  "type": "dialogue",
  "text": "You made a graph with your Minis' votes. Each picture stands for one vote."
}
```

```json
{
  "type": "dialogue",
  "text": "Here's a graph: animals at the zoo. Every picture graph has a key that tells you what each symbol means.",
  "tags": ["vocabulary"]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"dialogue"` | yes | |
| `text` | string | yes | Spoken/displayed text |
| `tags` | string[] | no | Semantic labels, e.g. `["vocabulary"]` |

---

### Scene

Manipulates a tangible on screen. Display-only in Notion (method emoji callout).

| Method | Notion icon | Params | Description |
|---|---|---|---|
| `show` | 🎬 | none | Make tangible visible |
| `hide` | 🙈 | none | Remove tangible from view |
| `animate` | 🎞️ | `event`, `status`, `description?`, `category?` | Trigger a named animation |
| `update` | ✏️ | `highlight_categories: string[]` | Highlight specific categories |
| `add` | ➕ | `label`, `status` | Overlay a label annotation |

**show / hide**
```json
{ "type": "scene", "method": "show", "tangible_id": "pg_fruits" }
{ "type": "scene", "method": "hide", "tangible_id": "data_table" }
```

**animate**
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_id": "pg_animals",
  "params": {
    "event": "transform_to_bar_graph",
    "status": "proposed",
    "description": "Picture graph symbols collapse into solid bars"
  }
}
```
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_id": "bg_animals",
  "params": {
    "event": "draw_bar_guideline",
    "category": "Monkeys",
    "status": "proposed"
  }
}
```

**update**
```json
{
  "type": "scene",
  "method": "update",
  "tangible_id": "bg_colors",
  "params": { "highlight_categories": ["Blue", "Yellow"] }
}
```

**add**
```json
{
  "type": "scene",
  "method": "add",
  "tangible_id": "bg_colors",
  "params": { "label": "11 in all", "status": "proposed" }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"scene"` | yes | |
| `method` | string | yes | `show` `hide` `animate` `update` `add` |
| `tangible_id` | string | yes | Target tangible |
| `params` | object | conditional | Required for `animate`, `update`, `add`; omit for `show`/`hide` |

---

### Prompt

Student interaction point. Text is editable in Notion (❓ callout).

```json
{
  "type": "prompt",
  "text": "Which fruit got the most votes? Click it.",
  "tool": "click_category",
  "validator": { "states": [...] }
}
```

```json
{
  "type": "prompt",
  "text": "How many monkeys are at the zoo?",
  "tool": "multiple_choice",
  "options": [5, 6, 7, 8],
  "validator": { "states": [...] }
}
```

```json
{
  "type": "prompt",
  "text": "Select all the categories you need to answer this question.",
  "tool": "multi_select",
  "options": ["Dogs", "Cats", "Fish", "Birds", "Lizards"],
  "validator": { "states": [...] }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"prompt"` | yes | |
| `text` | string | yes | Question or instruction shown to student |
| `tool` | string | yes | `click_category` · `multiple_choice` · `multi_select` |
| `options` | array | conditional | Required for `multiple_choice` and `multi_select`. Numbers or strings. |
| `validator` | object | yes | See [Validator](#validator) |

---

## Validator

```json
{
  "states": [
    { "name": "correct",            "condition": { ... }, "child_section": null },
    { "name": "light_remediation",  "condition": { ... }, "child_section": "s1_1_light" },
    { "name": "medium_remediation", "condition": { ... }, "child_section": "s1_1_medium" },
    { "name": "heavy_remediation",  "condition": {},      "child_section": "s1_1_heavy" }
  ]
}
```

States are evaluated **in order**; the first match wins. The final state typically has an empty condition (`{}`) as a catch-all fallback.

| Field | Type | Description |
|---|---|---|
| `name` | string | `"correct"`, `"light_remediation"`, `"medium_remediation"`, `"heavy_remediation"` |
| `condition` | object | Matching condition — see shapes below |
| `child_section` | string \| null | Section to branch to, or `null` to continue forward |

### Condition Shapes

**Operator-based** — used for the `correct` state; compares a tangible expression to an expected value.

```json
{
  "operator": "eq",
  "left": { "tangible": "pg_fruits", "expr": "selected_category" },
  "right": { "value": "Apples" }
}
```
```json
{
  "operator": "eq",
  "left": { "tangible": "choice_input", "expr": "selected_value" },
  "right": { "value": 7 }
}
```

| Sub-field | Description |
|---|---|
| `operator` | `"eq"` (only value currently used) |
| `left.tangible` | Tangible ID to read from |
| `left.expr` | Expression on that tangible (`selected_category`, `selected_value`) |
| `right.value` | Expected value (string or number) |

---

**Evaluate-based** — used for remediation states; arbitrary JS predicate against attempt context.

```json
{
  "evaluate": "(p) => p.attempt_count === 1",
  "description": "First wrong attempt"
}
```
```json
{
  "evaluate": "(p) => p.selected.length === 2 && p.selected.includes('Dogs') && p.selected.includes('Fish')",
  "description": "Exactly Dogs and Fish selected"
}
```

| Sub-field | Description |
|---|---|
| `evaluate` | JS arrow function string; `p` is the attempt context |
| `description` | Human-readable label for this condition |

---

**Fallback** — empty object; always matches; used as the final catch-all state.

```json
{}
```

---

## Remediation Sections

Remediation sections are structurally identical to normal sections but:
- Have `"type": "remediation"`
- No `workspace` field (inherit parent's workspace)
- Contain simplified beats that scaffold the student toward the correct answer

Three levels, applied in order:

| Level | Hint style |
|---|---|
| `light` | Minimal nudge — direct attention without revealing the answer |
| `medium` | Partial reveal — show the key data, let the student conclude |
| `heavy` | Full scaffold — state the answer explicitly, prompt to confirm |

**light**
```json
{
  "id": "s1_1_light",
  "type": "remediation",
  "steps": [[
    { "type": "dialogue", "text": "Look at the numbers next to each row. Which one is biggest?" }
  ]]
}
```

**medium**
```json
{
  "id": "s1_1_medium",
  "type": "remediation",
  "steps": [[
    { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
      "params": { "highlight_categories": ["Apples"] } },
    { "type": "dialogue", "text": "Count the Apples row — 6 symbols. Count the others: Bananas 4, Oranges 5, Grapes 3. Which row has the most?" }
  ]]
}
```

**heavy**
```json
{
  "id": "s1_1_heavy",
  "type": "remediation",
  "steps": [[
    { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
      "params": { "highlight_categories": ["Apples"] } },
    { "type": "dialogue", "text": "Apples has 6 symbols — more than any other row. Click Apples." }
  ]]
}
```

---

## Multi-Step Prompt Sections

When a section contains two sequential prompts (e.g. a two-step math problem), each prompt's remediations use step-qualified IDs:

```
s3_4c_step1_light
s3_4c_step2_light, s3_4c_step2_medium, s3_4c_step2_heavy
```

The parent section is `s3_4c_two_step`. Validator `child_section` fields reference the step-qualified IDs. Not every step needs all three levels — `s3_4c_step1` only has `light`.

---

## Tangible ID Conventions

Tangibles are defined outside `lesson.json` but referenced by ID throughout. Observed prefixes:

| Prefix | Type | Examples |
|---|---|---|
| `pg_` | Picture graph | `pg_fruits`, `pg_animals`, `pg_pets` |
| `bg_` | Bar graph | `bg_animals`, `bg_books`, `bg_colors` |
| `data_table` | Data table UI component | `data_table` |
| `choice_input` | Answer input widget | `choice_input` |

---

## Beat Summary

| Type | Notion format | Editable | Fields |
|---|---|---|---|
| `dialogue` | 💬 callout | yes — `text` | `text`, `tags?` |
| `scene` | method-emoji callout | no | `method`, `tangible_id`, `params?` |
| `prompt` | ❓ callout | yes — `text` | `text`, `tool`, `options?`, `validator` |
