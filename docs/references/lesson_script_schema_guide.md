# Lesson Script Schema Guide

Reference for the `lesson.json` script format. Covers every field, beat type, condition shape, and naming convention.

---

## Design Requirements

Two goals shape this schema.

### 1. Readability and Notion Portability

The format is human-readable first and machine-processed second. This makes it suitable for collaborative review in Notion, where non-engineers can read, comment on, and edit lesson content without touching raw JSON.

Key choices that serve this goal:

- **Plain-text content fields** — `dialogue.text` and `prompt.text` contain natural language, not markup or encoded content
- **Notion callout mapping** — each beat type maps to a specific Notion callout emoji (💬 dialogue, ❓ prompt, 🎬/🎞️ scene), so the JSON can round-trip to/from Notion without losing information on the editable fields
- **Selective editability** — only `dialogue.text` and `prompt.text` are editable in Notion; `scene` beats are display-only, so reviewers cannot inadvertently break structural logic
- **Human-readable IDs and slugs** — section IDs include a slug (e.g. `s1_1_most_votes`) so a reviewer can follow the navigation flow without reading code
- **`description` on validator states** — every validator state carries a plain-English description of the student condition it captures, making branching logic readable without interpreting condition syntax

### 2. Translatable Structured Data

The schema is an authored intermediate representation — not the final runtime format. It must be structured enough to be mechanically translated to a downstream schema (a runtime engine, a CMS, or a future schema revision).

Key choices that serve this goal:

- **Typed beats** — `type` is always explicit (`"dialogue"`, `"scene"`, `"prompt"`), enabling switch-based translation with no ambiguity
- **Explicit targeting** — tangibles are always referenced by `tangible_id` or `tangible_type`, never by position or implicit state
- **No logic embedded in text** — conditions and branching live exclusively in `validator`; dialogue strings carry no conditional content
- **Flat, predictable field shapes** — each beat type has a fixed, documented field set; the only open-ended field is `params`, which is scoped to a specific `method` and documented
- **Validator as a declarative state machine** — validator states are a portable condition/goto structure with no runtime-specific implementation details, making them translatable to any branching execution model
- **IDs as the only coupling between sections** — sections reference each other only via `goto` section IDs; the schema makes no assumptions about execution order beyond what those references specify

These two goals can create tension: fully specified structured data tends toward verbosity, while readability pushes toward concision. The schema resolves this by separating concerns — structural and logic fields are fully specified for translation fidelity, while human-facing fields (`text`, `description`, ID slugs) carry the readability load.

---

## Top-Level Structure

```json
{
  "id": "u3_m4_lesson",
  "sections": [ ... ]
}
```

| Field | Type | Description |
|---|---|---|
| `id` | string | Sequence identifier — see format below |
| `sections` | array | Ordered list of all sections (main, transition, remediation) |

### Lesson ID Format

```
u{unit}_m{module}_{phase}

u3_m4_lesson
u3_m4_warmup
u3_m4_synthesis
u3_m4_practice
u3_m4_exitcheck
```

| Segment | Description |
|---|---|
| `u{n}` | Unit number |
| `m{n}` | Module number within the unit |
| `{phase}` | One of: `lesson`, `warmup`, `synthesis`, `practice`, `exitcheck` |

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
s{group}_{seq}_{slug}              →  s1_1_most_votes
s{group}_{seq}{variant}_{slug}     →  s2_2a_fewest_books
s{group}_transition                →  s2_transition
```

| Segment | Description |
|---|---|
| `s` | Fixed prefix |
| `{group}` | Concept group number — local to the unit/module, not the phase |
| `{seq}` | Sequence position within the group |
| `{variant}` | Optional letter suffix for sub-problems, e.g. `a`, `b`, `c` |
| `{slug}` | Human-readable label for the problem |

**Key rules:**
- Section IDs are **unit/module specific** — they belong to a content area, not a phase
- The same section can appear in multiple phases (lesson, warmup, synthesis, practice, exitcheck)
- Some sections are **misconception specific** — written to address a known error pattern
  rather than advancing the main concept sequence
- Some sections are **validator-state dependent child sections** — they only execute
  when a specific validator state is triggered. Remediation sections (`_light`, `_medium`,
  `_heavy`) are the current example of this pattern, but other branching types will exist
  (e.g. sections addressing a specific wrong answer, or sections unlocked by a correct
  answer to a prerequisite prompt). These are always referenced via `child_section` in a
  validator state, never appear in the main sequence directly.

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

Manipulates a tangible on screen. Display-only in Notion (method emoji callout). Basic workspace changes use 🎬; elaborate animation events use 🎞️.

Three targeting levels — omit fields to broaden scope:

| Target | Fields present |
|---|---|
| Specific instance | `tangible_id` |
| All instances of a type | `tangible_type` |
| All instances on workspace | neither |

`add` is the exception — it always requires both `tangible_id` and `tangible_type`.

Interactivity is **implicit** — a tangible becomes interactive when a prompt's `tool` targets it, and resets automatically when the prompt resolves. Use `lock`/`unlock` only for edge cases that need explicit control.

| Method | Notion icon | `params` fields | Description |
|---|---|---|---|
| `show` | 🎬 | — | Make tangible visible |
| `hide` | 🎬 | — | Remove tangible from view |
| `animate` | 🎞️ | `event`, `status`, `description`, ...tangible-specific | Trigger a named animation |
| `update` | 🎬 | `highlight_categories: string[]` | Highlight specific categories |
| `add` | 🎬 | tangible-specific config (optional) | Add a new instance to the workspace |
| `remove` | 🎬 | — | Remove a tangible instance from the workspace |
| `lock` | 🎬 | — | Prevent student interaction regardless of active prompt |
| `unlock` | 🎬 | — | Re-enable student interaction on a locked tangible |

**show / hide**
```json
{ "type": "scene", "method": "show", "tangible_id": "pg_fruits" }
{ "type": "scene", "method": "hide", "tangible_id": "data_table" }
```

**animate — specific instance**
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_id": "bg_animals",
  "params": {
    "event": "draw_bar_guideline",
    "status": "proposed",
    "description": "Guideline draws from top of Monkeys bar to axis",
    "category": "Monkeys"
  }
}
```

**animate — all instances of a type**
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_type": "picture_graph",
  "params": {
    "event": "transform_to_bar_graph",
    "status": "proposed",
    "description": "All picture graphs collapse into bar graphs"
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
  "tangible_id": "numline_a",
  "tangible_type": "number_line",
  "params": { "min": 0, "max": 2 }
}
```

**remove**
```json
{ "type": "scene", "method": "remove", "tangible_id": "numline_a" }
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"scene"` | yes | |
| `method` | string | yes | `show` `hide` `animate` `update` `add` `remove` |
| `tangible_id` | string | conditional | Instance ID. Required for `add`. Omit to broaden scope to type or all. |
| `tangible_type` | string | conditional | Required for `add`. Omit to broaden scope to all instances on workspace. |
| `params` | object | no | Method-specific configuration; omit when not needed |

---

### Prompt

Student interaction point. Text is editable in Notion (❓ callout).

**Workspace tool** — activates interaction on a specific tangible:
```json
{
  "type": "prompt",
  "text": "Which fruit got the most votes? Click it.",
  "tool": { "name": "click_category", "tangible_id": "pg_fruits" },
  "validator": { "states": [...] }
}
```

**Workspace tool — tangibles as options (explicit list)**
```json
{
  "type": "prompt",
  "text": "Which graph shows the most cats?",
  "tool": { "name": "click_tangible", "tangible_ids": ["pg_fruits", "pg_animals", "pg_pets"] },
  "validator": { "states": [...] }
}
```

**Workspace tool — tangibles as options (all of a type)**
```json
{
  "type": "prompt",
  "text": "Which graph shows the most cats?",
  "tool": { "name": "click_tangible", "tangible_type": "picture_graph" },
  "validator": { "states": [...] }
}
```

**Overlay tool** — generates its own UI, not tied to a tangible:
```json
{
  "type": "prompt",
  "text": "How many monkeys are at the zoo?",
  "tool": { "name": "multiple_choice", "options": [5, 6, 7, 8] },
  "validator": { "states": [...] }
}
```

```json
{
  "type": "prompt",
  "text": "Select all the categories you need to answer this question.",
  "tool": { "name": "multi_select", "options": ["Dogs", "Cats", "Fish", "Birds", "Lizards"] },
  "validator": { "states": [...] }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"prompt"` | yes | |
| `text` | string | yes | Question or instruction shown to student |
| `tool` | object | yes | See tool fields below |
| `validator` | object | yes | See [Validator](#validator) |

**`tool` fields:**

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | `click_category` · `click_tangible` · `multiple_choice` · `multi_select` |
| `tangible_id` | string | conditional | Workspace tool targeting a single tangible |
| `tangible_ids` | string[] | conditional | `click_tangible` — explicit list of selectable tangible instances |
| `tangible_type` | string | conditional | `click_tangible` — all instances of a type are selectable |
| `options` | array | conditional | Overlay tools — `multiple_choice` and `multi_select`. Numbers or strings. |
| `config` | object | no | Tool-specific configuration (e.g. `{ "max_cells": 3 }` for `shade`) |

---

## Validator

An array of states evaluated **in order**; the first match wins. The final state is always an empty condition (`{}`) catch-all. `goto` is always required — every state has a feedback section.

States have no inherent correct/incorrect meaning — they are just defined states. `incorrect_count` is the one system parameter; all other condition keys are tangible-specific fields.

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student selected Apples",
    "goto": "s1_1_chose_apples"
  },
  {
    "condition": { "selected": "Bananas", "incorrect_count": 1 },
    "description": "Student selected Bananas on first attempt",
    "goto": "s1_1_chose_bananas_1"
  },
  {
    "condition": { "selected": "Bananas", "incorrect_count": 2 },
    "description": "Student selected Bananas on second attempt",
    "goto": "s1_1_chose_bananas_2"
  },
  {
    "condition": { "incorrect_count": 1 },
    "description": "Student selected any other wrong answer on first attempt",
    "goto": "s1_1_fallback_1"
  },
  {
    "condition": {},
    "description": "Catch-all — any remaining state",
    "goto": "s1_1_fallback_3"
  }
]
```

| Field | Type | Description |
|---|---|---|
| `condition` | object | Matching condition. Multiple keys implicitly ANDed. Use `or`/`and` arrays for explicit logic. |
| `description` | string | Precise plain-English description of exactly what student state this condition captures. |
| `goto` | string | Section ID to branch to. Always required. |

### Condition Parameters

| Parameter | Type | Description |
|---|---|---|
| `selected` | string \| number | What the student selected from the tool's available options |
| `incorrect_count` | number | System counter — how many times the student has triggered a non-first-match state on this prompt. Max 3. |
| `tangible_id` | string | Scopes remaining keys to a specific tangible instance. Used when checking tangible state fields directly. |
| *(tangible fields)* | any | State fields exposed by the scoped tangible — used alongside `tangible_id` |

### Condition Logic

**Single tangible check:**
```json
{ "condition": { "selected": "Bananas", "incorrect_count": 1 } }
```

**Specific tangible field check:**
```json
{ "condition": { "tangible_id": "numline_a", "shaded_interval_count": 3 } }
```

**Multiple tangibles (AND):**
```json
{
  "condition": {
    "and": [
      { "tangible_id": "bar_a", "points": [1, 2] },
      { "tangible_id": "numline_a", "shaded_interval_count": 3 }
    ]
  }
}
```

**OR across values:**
```json
{ "condition": { "or": [{ "selected": "Oranges" }, { "selected": "Grapes" }] } }
```

**Fallback — empty object; always matches:**
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
