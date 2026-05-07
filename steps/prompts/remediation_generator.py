"""
remediation_generator - AI Prompt

Generates incorrect validator states (L/M/H for Non-MC, per-distractor for
single-select MC, per-branch for multiselect MC) for each prompt in a lesson
section.

Runs in batch mode. Input is pre-filtered to sections that have at least one
prompt with a real validator (not any-response-advances).

Input per call: section JSON auto-wrapped as <input> by the pipeline.
Lesson context: the lesson_generator step output (lesson_sections.json) is passed
as <lesson_sections> by the pipeline so the generator can align correction language
with the lesson's teaching vocabulary and arc. Wired in lesson_generator_dialogue_pass
and exitcheck_generator_dialogue_pass via context_files.

Section context: the section_structurer step output (section_context.md) is passed
as <section_context> by the pipeline. It is a running document of section summaries
(visual state, content taught, student action) built up in section order. The
remediation generator uses it to identify the most recently taught strategy for the
current section and align remediation with that approach rather than introducing
shortcuts or patterns not yet covered.

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

**Do NOT skip a `multiple_choice` prompt just because its validator only contains the correct state.** A `multiple_choice` validator that has only one `is_correct: true` state with `condition: { "selected": "..." }` means the wrong-answer states haven't been written yet — that is exactly what you are here to generate. The absence of pre-existing `is_correct: false` states is normal, not a signal to skip.

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

The design track is determined by **coverage**, not by tool name. For each qualifying prompt:

**A. Enumerate the wrong-answer space:**
- `multiple_choice`: all values in `tool.options` except the correct one
- `multi_select`: all option subsets not matching the correct condition
- `click_tangible`: all tangible IDs added by `scene add` beats in this section, minus the correct one
- `click_category`: all category values visible in the scene, minus the correct one
- Build tools / numeric / open inputs: problem space is **open** (cannot be enumerated)

**B. Count pre-defined specific conditions:** `is_correct: false` states in the input validator with a non-empty, non-catch-all condition (i.e. condition is not `{}`).

**C. Choose design track:**

| Coverage | Correct answer type | Track |
|---|---|---|
| All wrong inputs covered by specific conditions | Single correct value | **Single-Select MC** → Per-condition Mediums + Heavy |
| All wrong inputs covered by specific conditions | Multiple correct values | **Multiselect MC** → Per-branch Medium + Heavy |
| Specific conditions exist but do NOT cover all wrong inputs | Any | **Non-MC** → Specific Mediums + Generic L/M/H |
| No specific conditions, or open problem space | Any | **Non-MC** → Generic L/M/H only |

This means `click_tangible` with 2 wrong tangibles and both covered → Single-Select MC. `click_category` with 4 categories and all covered → Single-Select MC. `multiple_choice` always has full coverage → always Single-Select MC.

---

## STEP 2A: NON-MC: STATES

Use this track only when specific conditions do **not** cover the entire wrong-answer space (see STEP 1). Follow `<remediation_design_ref>` Sections 2.4–2.5 for state structure and order. Always emit generic L/M/H after any specific-condition states. Follow length, visual, and language rules from `<remediation_design_ref>` Sections 4–6.

**Two parallel tracks run simultaneously:**
- **Specific condition track:** fires when the student's answer matches a known wrong answer. Attempt-agnostic — fires regardless of attempt number.
- **Generic L/M/H track:** purely attempt-count driven (`incorrect_count: 1` → Light, `incorrect_count: 2` → Medium, `{}` → Heavy on third attempt). Catches any wrong answer not matched by a specific condition.

**Specific conditions** are pre-defined in the input — do not invent them. Inspect the existing `validator` for `is_correct: false` states with non-empty conditions (not just `{}`). Each such state has:
- `condition`: the base condition (e.g. `{ "container_count": 3 }`) — use it exactly as-is
- `description`: a plain-English label for what wrong answer this represents
- `beats`: placeholder dialogue already written — use as inspiration when writing Medium-quality content (visual scaffold + 20–30 words)

For each specific condition, emit **one state** using the base condition unchanged. **Never include `incorrect_count` in a specific condition** — the condition fires any time that answer is given, regardless of attempt number. Write or rewrite the dialogue and scene beats to Medium standard — do not just copy the placeholder beats verbatim.

**Two effective patterns for specific condition dialogue:**

- **Pattern A — Credit + narrow:** When the student got part right, acknowledge it, then narrow to the specific error. Close with a pointed question.
  > "You're right that there are 4 columns. But count how many dots are in each column. Are there 4?"

- **Pattern B — Name + redirect + point:** Name what the student did in one phrase, redirect to the correct concept, give one concrete action or question.
  > "You counted the Dogs. When we ask how many fewer, we need to find the difference. Count how far apart Dogs and Fish are."

In both patterns: the Medium answer rule applies — do not give the correct counts or values. The student still has to execute.

**Light** (`incorrect_count: 1`): dialogue only.
```json
{
  "condition": { "incorrect_count": 1 },
  "description": "Student answered incorrectly on first attempt",
  "is_correct": false,
  "remediation_level": "light",
  "steps": [
    [ { "type": "dialogue", "text": "..." } ]
  ]
}
```

**Medium** (`incorrect_count: 2`): scene beat required. Dialogue teaches the method — name what to look at and in what order. Close with a pointed question or specific imperative.
```json
{
  "condition": { "incorrect_count": 2 },
  "description": "Student answered incorrectly on second attempt",
  "is_correct": false,
  "remediation_level": "medium",
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

**Scenario image prompts (`click_tangible` on `image` tangibles):** When the prompt targets scenario images (real-world connection sections), never reference images by letter label in any state. For each state that needs to draw attention to a specific image, emit a `scene animate` beat with `event: "highlight"` on that tangible ID, then say "this image" in the dialogue. Apply this in Medium states (highlight the specific wrong or correct image) and Heavy states (highlight each relevant image in sequence as the guide narrates).

```json
{ "type": "scene", "method": "animate", "tangible_id": "scenario_image_counting",
  "params": { "event": "highlight", "status": "confirmed", "description": "Counting money scenario image highlights." } },
{ "type": "dialogue", "text": "Look at this image. Does this situation use groups of 10?" }
```

**Heavy** (catch-all `{}`): `scene animate` beat required (system demonstrates the answer). For Non-MC, fires on the third wrong attempt — whether that is an unenumerated answer, a repeated specific condition, or simply a third incorrect try. Never fires when the student clicks the correct answer — that is handled by the correct validator. Dialogue narrates the thinking, not just the mechanics — name the structure being demonstrated and connect each step to what it means. End with the underlying principle: why the answer has to be what it is, not just what the answer is.

**For the on_correct beat:** use it only to identify what concept the answer demonstrates and what the closing principle should be. Do not treat it as a template for which tangibles to animate — it only shows the confirmation step, not the reasoning.

**For the Heavy's animate beats:** read the section's `scene add` beats and the dialogue beat that introduces the prompt. These tell you which tangibles are part of the reasoning and what each one contributes (line counts, axis values, etc.). The Heavy must animate every tangible involved in the reasoning — in the order the section presents them — and narrate what the guide observes about each one, arriving at the correct answer as the conclusion.

**Use `<section_context>` to confirm the teaching strategy and align vocabulary.** If the section context shows that the guide's teaching walked through multiple visuals in sequence, the Heavy's animate beats must follow that same sequence.
```json
{
  "condition": {},
  "description": "Student has been incorrect three or more times. System models the correct answer.",
  "is_correct": false,
  "remediation_level": "heavy",
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

Also add `"remediation_level": "medium"` to every specific-condition state (the pre-defined `is_correct: false` states with non-empty conditions).

---

## STEP 2B: SINGLE-SELECT MC: PER-CONDITION STATES

Use this track when all possible wrong answers are covered by specific conditions — regardless of tool. This includes `multiple_choice` prompts (always fully enumerated), and non-MC prompts like `click_tangible` or `click_category` when every wrong target has a pre-defined specific condition.

**Derive wrong conditions explicitly:**
- For `multiple_choice`: take the full `options` array and remove any value that appears as `condition.selected` in an `is_correct: true` validator state
- For `click_tangible` / `click_category`: use the pre-defined specific conditions from the input validator — these are the wrong answers

Every wrong answer/condition requires a Medium state. Do this even if no `is_correct: false` states exist yet in the validator.

See `<remediation_design_ref>` Section 3.2 for this structure (no Light state; per-condition Mediums + one Heavy). The condition for each Medium is the base wrong-answer condition only — e.g. `{ "selected": <distractor> }`. Do not add `incorrect_count` — per-condition and LMH are separate branching dimensions and must never be combined.

One **Medium** per distractor: scene beat required. Dialogue names the error and redirects to the correct concept or tool. Close with a pointed question or specific imperative.
```json
{
  "condition": { "selected": <distractor> },
  "description": "Student selected <distractor>: <why this is wrong>",
  "is_correct": false,
  "remediation_level": "medium",
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required. Fires when the student selects any option they have already tried — all distractors are enumerated as Mediums, so a repeat on any of them escalates to Heavy.
```json
{
  "condition": {},
  "description": "Student repeated a previously tried option. System models the correct answer.",
  "is_correct": false,
  "remediation_level": "heavy",
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

Identify **correct answers** from the success/correct validator state condition — these are the values listed under `selected` clauses. **Incorrect answers** are values listed under `not_selected` clauses in that same condition.

**First, detect the no-wrong-options variant:** Count `not_selected` clauses in the correct validator condition. If there are **none**, all options are correct — no wrong options exist. Follow Section 3B.9 of `<remediation_design_ref>` and emit only Branch 2 + Heavy. Do NOT invent phantom wrong option values.

For the **no-wrong-options variant**, every possible error is an under-selecting error — so use `incorrect_count` conditions (same as Non-MC L/M/H). Do NOT use Branch 2/3/4 conditions.

**Light** (`incorrect_count: 1`) — dialogue only:
```json
{
  "condition": { "incorrect_count": 1 },
  "description": "Student has not selected all correct answers (first attempt)",
  "is_correct": false,
  "remediation_level": "light",
  "steps": [
    [ { "type": "dialogue", "text": "..." } ]
  ]
}
```
Use a short nudge (10–20 words) pointing toward completeness — e.g. "Read the scenarios carefully. Did you select ALL?" Adapt to the content.

**Medium** (`incorrect_count: 2`) — scene beat required:
```json
{
  "condition": { "incorrect_count": 2 },
  "description": "Student has not selected all correct answers (second attempt)",
  "is_correct": false,
  "remediation_level": "medium",
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

**Heavy** (`condition: {}`) — `scene animate` beat required. Models all correct answers.

For the **standard variant** (has at least one `not_selected` clause = has wrong options), identify all options not listed as `selected` in the correct condition as incorrect answers. See `<remediation_design_ref>` Section 3B for structure, branch definitions, language requirements, and condition patterns (no Light; Branches 2/3/4 Mediums + one Heavy).

One **Medium per branch**: scene beat required.
```json
{
  "condition": { <see Section 3B.7 for correct condition logic per branch> },
  "description": "Branch <N>: <description of student's selection state>",
  "is_correct": false,
  "remediation_level": "medium",
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required. Shared fallback for all branches. Fires when the student cannot find the correct answer after 3 tries.
```json
{
  "condition": {},
  "description": "Student could not find the correct answer after 3 tries. System models all correct answers.",
  "is_correct": false,
  "remediation_level": "heavy",
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

**Multiselect MC inner array (standard — has wrong options):**
1. Branch 2 Medium — under-selecting
2. Branch 3 Medium — all-wrong
3. Branch 4 Medium — mixed
4. Heavy (`condition: {}`): always last

**Multiselect MC inner array (no-wrong-options variant — zero `not_selected` in correct condition):**
1. Light — `{ "incorrect_count": 1 }` — dialogue only
2. Medium — `{ "incorrect_count": 2 }` — scene beat required
3. Heavy — `condition: {}` — always last

---

## LANGUAGE RULES

Follow all language patterns, word counts, visual requirements, and prohibited constructs from `<remediation_design_ref>` Sections 4–8 and 12.4.

**Light:** Use openers from Sections 4.1–4.2. Cycle — do not reuse the same phrase within a section.

**Medium:** Use a starter from Section 5.1. Cycle — do not reuse within a section.

**Medium — universal answer rule (applies to all tracks and specific conditions):** Never state the correct answer, value, or count in a Medium. This applies even when the answer is visible on screen (e.g. a key showing "Each ⭐ = 5", a label, a highlighted number). Redirect the student to the right place and let them read it. A Medium that names the answer removes the work the student needs to do. If you find yourself writing the correct value in a Medium, rewrite it as a question or imperative that sends the student to look.

**Heavy:** Choose an opener from Section 6.1. Rotate across the full range of available openers — "Let me show you", "Let me help you think through this", "Let's work together", "I'll walk us through this", "Here's what matters" — treating each as equally valid. Cycle — do not reuse the same opener within a section. Refer to <remediations.md> for opener variety and the principle-ending pattern. End with closure per Section 7.

---

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Do not reference concepts from <advanced_concepts>. Reference <required_phrases> in Medium/Heavy where genuinely appropriate. Ground explanations in <the_one_thing>. Keep tangible references consistent with the section's `scene` array and existing scene beats. **Do not fabricate game data values** — specific quantities, scale-key values, or item counts that come from live game content are not available at script-writing time unless they appear explicitly in the input section JSON or `<lesson_sections>`. Do not invent them. In Light and Medium states, redirect the student to look at the relevant element rather than stating a value. In Heavy states, narrate the structural pattern being animated without naming specific quantities that aren't grounded in the input.

When <lesson_sections> is available, use it to align correction language with how the lesson taught the concept — match the vocabulary the guide used in earlier sections and frame corrections in terms the student has already encountered.

When <section_context> is available, read every section summary whose `## section_id` appears before the current section's id. Identify the most recently taught strategy: what approach did the guide use to explain the concept, what scaffold did it provide, what vocabulary did it lean on? Use that strategy — and only that strategy — to frame remediation. Do not introduce a shortcut, pattern, or reasoning method that does not appear in any prior section summary. If a student is stuck on `s2_5`, the remediation should teach using the same scaffold introduced in `s2_1`–`s2_4`, not a rule the lesson hasn't covered yet.

For prompts with `"variable_answer": true`: do not assume the student's specific attempt in Light or Medium dialogue. For Heavy, model one specific valid example but frame it as one way, not the only answer.

---

## OUTPUT RULES

- Output ONLY the `incorrects` array content. No explanation, no markdown fences.
- **Flag placeholders and uncertain content:** When a beat or validator state contains content that could not be grounded in the input — game data values not present in the section JSON or `<section_context>`, unresolved visual elements, invented quantities — add `"flag": "placeholder — <brief reason>"` to that beat or state object. This makes uncertain content findable for human review without blocking output. Example: `"flag": "placeholder — scale key values not in input"`.
- The prefill already opens `{"id": "...", "incorrects": [`. Complete from that point.
- Use double quotes throughout
- `is_correct: false` on every state
- Do not use em dashes (—) or double hyphens (--) in any text field; to create a pause or connect two thoughts, use a period or comma instead

""",
    doc_refs=[
        "remediation_design_ref.md",
        "references/lesson_script_schema_guide.md",
        "dialogue_examples/remediations.md",
    ],
    module_ref={
        "misconceptions": "misconceptions",
        "forbidden_phrases": "scope_fence.forbidden_phrases",
        "required_phrases": "scope_fence.required_phrases",
        "advanced_concepts": "scope_fence.advanced_concepts",
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
