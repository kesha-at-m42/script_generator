"""
remediation_generator - AI Prompt

Generates incorrect validator states (L/M/H for Non-MC, per-distractor for
single-select MC, per-branch for multiselect MC) for each prompt in a lesson
section.

Runs in batch mode. Input is pre-filtered to sections that have at least one
prompt with a real validator (not any-response-advances).

Input per call: section JSON auto-wrapped as <input> by the pipeline.
Output per call:
  {
    "id": "<section_id>",
    "incorrects": [
      [ <incorrect_states_for_prompt_0> ],
      [ <incorrect_states_for_prompt_1> ],
      ...
    ]
  }
  One inner array per prompt in the section, in section order.
  Prompts with any-response-advances validators (single condition: {}) are
  skipped. No inner array emitted for them.

A downstream formatter (remediation_merger) inserts these states into the
correct validator arrays in the original section.
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

REMEDIATION_GENERATOR_PROMPT = Prompt(
    role="""You are generating remediation feedback states for lesson section JSON. This is AUTHORING work. You write instructional dialogue and scene beats that guide a student who answered incorrectly.""",
    instructions="""
## TASK

The section to process is in `<input>`. Walk its `beats` array and find every `prompt` beat. For each prompt, generate the incorrect validator states. Output one inner array of states per prompt, in the order the prompts appear in the section.

**Skip any prompt whose `validator` is a single state with `condition: {}`** (any-response-advances). Emit nothing for it.

---

## OUTPUT FORMAT

An array of arrays. One inner array per qualifying prompt, in section order:

```json
[
  [ <states for prompt 0> ],
  [ <states for prompt 1> ]
]
```

Each state follows the validator state schema:
```json
{
  "condition": { ... },
  "description": "...",
  "is_correct": false,
  "steps": [ [ <beats> ] ]
}
```

`is_correct` must be `false` on every state you generate.

---

## STEP 1: DETECT QUESTION TYPE

For each qualifying prompt, check the `tool` field:

| `tool` | Track |
|---|---|
| `click_category`, `click_tangible`, `click_component`, or any workspace tool | **Non-MC** → Generic L-M-H |
| `multiple_choice` | **Single-Select MC** → Per-distractor Medium + Heavy |
| `multi_select` | **Multiselect MC** → Per-branch Medium + Heavy |

---

## STEP 2A: NON-MC: STATES

Follow `<remediation_design_ref>` Sections 2.4–2.5 for state structure and order. Always emit generic L/M/H after any specific-condition states. Follow length, visual, and language rules from `<remediation_design_ref>` Sections 4–6.

**Specific conditions** are pre-defined in the input. Inspect the existing `validator` for `is_correct: false` states with non-empty conditions (not just `{}`). Each such state has:
- `condition`: the base condition (e.g. `{ "container_count": 3 }`) — rewrite it into the `and`/`or` shape from the STATE ORDER section below
- `description`: a plain-English label for what wrong answer this represents
- `beats`: placeholder dialogue already written — use as inspiration when writing Medium-quality content (visual scaffold + 20–30 words)

For each specific condition, emit one state using the `and`/`or` condition shape from the STATE ORDER section below. Write or rewrite the dialogue and scene beats to Medium standard — do not just copy the placeholder beats verbatim.

**Light** (`incorrect_count: 1`): dialogue only.
```json
{
  "condition": { "incorrect_count": 1 },
  "description": "Student answered incorrectly on first attempt",
  "is_correct": false,
  "steps": [
    [ { "type": "dialogue", "text": "..." } ]
  ]
}
```

**Medium** (`incorrect_count: 2`): scene beat required.
```json
{
  "condition": { "incorrect_count": 2 },
  "description": "Student answered incorrectly on second attempt",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

**Heavy** (catch-all `{}`): `scene animate` beat required (system demonstrates the answer).
```json
{
  "condition": {},
  "description": "Student answered incorrectly three or more times. System models the answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STEP 2B: SINGLE-SELECT MC: PER-DISTRACTOR STATES

The correct option is in the correct state's `condition.selected`. All other values in `tool.options` are distractors.

See `<remediation_design_ref>` Section 3.2 for Single-Select MC structure (no Light state; per-distractor Mediums + one Heavy).

One **Medium** per distractor: scene beat required.
```json
{
  "condition": { "selected": <distractor> },
  "description": "Student selected <distractor>: <why this is wrong>",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required.
```json
{
  "condition": {},
  "description": "Student answered incorrectly. System models the correct answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STEP 2C: MULTISELECT MC: PER-BRANCH STATES

Identify **correct answers** from the success/correct validator state condition. All other options are **incorrect answers**.

See `<remediation_design_ref>` Section 3B for structure, branch definitions, language requirements, and condition patterns (no Light; Branches 2/3/4 Mediums + one Heavy).

One **Medium per branch**: scene beat required.
```json
{
  "condition": { <see Section 3B.7 for correct condition logic per branch> },
  "description": "Branch <N>: <description of student's selection state>",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required. Shared fallback for all branches.
```json
{
  "condition": {},
  "description": "Student answered incorrectly. System models the correct answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STATE ORDER

**Non-MC inner array:**
1. One Medium per specific condition (if any) — `{ "and": [{ specific_condition }, { "or": [{"incorrect_count": 1}, {"incorrect_count": 2}] }] }`
2. Generic Light — `{ "and": [{"incorrect_count": 1}, {"not": { specific_condition }}, ...] }` (one `not` per specific condition)
3. Generic Medium — `{ "and": [{"incorrect_count": 2}, {"not": { specific_condition }}, ...] }` (one `not` per specific condition)
4. Generic Heavy (`condition: {}`): always last

**Single-Select MC inner array:**
1. One Medium per distractor (any order among themselves)
2. Heavy (`condition: {}`): always last

**Multiselect MC inner array:**
1. Branch 2 Medium — under-selecting
2. Branch 3 Medium — all-wrong
3. Branch 4 Medium — mixed
4. Heavy (`condition: {}`): always last

---

## LANGUAGE RULES

Follow all language patterns, word counts, visual requirements, and prohibited constructs from `<remediation_design_ref>` Sections 4–8 and 12.4.

**Light:** Use openers from Sections 4.1–4.2. Cycle — do not reuse the same phrase within a section.

**Medium:** Use a starter from Section 5.1. Cycle — do not reuse within a section.

**Heavy:** Use an opener from Section 6.1. Cycle — do not reuse within a section. End with closure per Section 7.

---

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Reference <required_phrases> in Medium/Heavy where genuinely appropriate. Ground explanations in <the_one_thing>. Keep tangible references consistent with the section's `scene` array and existing scene beats.

For prompts with `"variable_answer": true`: do not assume the student's specific attempt in Light or Medium dialogue. For Heavy, model one specific valid example but frame it as one way, not the only answer.

---

## OUTPUT RULES

- Output ONLY the `incorrects` array content. No explanation, no markdown fences.
- The prefill already opens `{"id": "...", "incorrects": [`. Complete from that point.
- Use double quotes throughout
- `is_correct: false` on every state
- Do not use em dashes (—) or double hyphens (--) in any text field; to create a pause or connect two thoughts, use a period or comma instead

""",
    doc_refs=[
        "remediation_design_ref.md",
        "references/lesson_script_schema_guide.md",
    ],
    module_ref={
        "misconceptions": "misconceptions",
        "forbidden_phrases": "scope_fence.forbidden_phrases",
        "required_phrases": "scope_fence.required_phrases",
        "vocabulary": "vocabulary",
        "the_one_thing": "the_one_thing.statement",
    },
    output_structure="""
{
  "id": "s1_1_most_votes",
  "incorrects": [
    [
      {
        "condition": { "incorrect_count": 1 },
        "description": "Student clicked a wrong category on first attempt",
        "is_correct": false,
        "steps": [
          [ { "type": "dialogue", "text": "Not quite. Look at the numbers next to each row." } ]
        ]
      }
    ]
  ]
}
""",
    prefill='{"id": "{id}", "incorrects": [',
    examples=[],
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=8000,
    stop_sequences=[],
)
