# Prompt: section_structurer_v3
# Generated: 2026-04-29T16:17:38.929157
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 32000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are translating a lesson specification into structured section JSON. Your job is faithful, precise translation: every interaction in the spec becomes a correctly structured section object with the right beats, tools, validators, and scene state. Dialogue is functional. Preserve the pedagogical intent from the spec without embellishment.

----------------------------------------------------------------------

### Block 2: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

<input> is a single structured section object produced by starterpack_parser_v3.

It may contain a `prior_section_summaries` field — a running document summarising every section processed so far, newest at the bottom. Use it to:
- Resolve under-specified visual references ("Same data", "Full data visible", "remains visible", "picture graph from Section 1") — look up the most recent matching tangible in the summaries and use its exact dataset, categories, values, scale, and orientation.
- Understand what concepts and vocabulary have already been introduced so you don't contradict prior content.
- Know the current screen state so `add`, `update`, and `remove` beats are consistent with what has been established.
When `prior_section_summaries` is absent (first section), treat the screen as empty.

It contains key-value fields extracted from the original spec
(visual, guide, prompt, correct_answer, on_correct, on_incorrect, purpose, etc.)
and a `workspace_specs` field: `{ "toys": ["picture_graph", "data_table"], "tools": ["click_category"] }`.

**Map all fields by meaning, not by name.** The input object may present
information in various field names and formats — interpret every field and
map it to the appropriate schema context:
- `student_action: "MC (2, 6, 8, 12)"` → `multiple_choice` prompt with
  options `[2, 6, 8, 12]`
- `student_action: "Multi-select: Dogs, Cats, Fish"` → `multi_select` with
  those options
- `guide_2`, `prompt_2`, `on_correct_2` etc. → a second step in the section. When `prompt_2` (or any numbered prompt field) exists without a corresponding `guide_2`, you must still generate a dialogue beat before that prompt — infer it from `visual_N`, the prompt text itself, or surrounding context. A missing `guide_N` is never a reason to omit the required dialogue beat.
- `divider` fields are contextual labels only — they describe what is happening at that point in the spec. Do not use them to determine step boundaries and do not output them as beats. Use the surrounding prompt, student_action, and guide fields to determine structure.
- A `student_action` field that contains two actions joined by "and" (e.g. "selects X or Y and fills two number slots") represents two sequential prompts — split them into separate steps
- A `student_action` that uses "OR" to offer two equivalent click targets for the same interaction (e.g. "Click on the bar OR the symbols for that category") is a **single prompt with a multi-target** — use `"target": ["tangible_id_1", "tangible_id_2"]`. A `correct_answer` of "Either correct location accepted" confirms this pattern. Do NOT split it into two sequential prompts.
- Inline annotations in any text field (e.g. `[System highlights rows
  sequentially]`, `[3 tile places into first slot]`) → `scene` beats at
  that point in the step
- `task` describing a build/click/drag action → infer the tool type from it
- Any beat in the outer `beats` array that only applies on a specific branch gets a `"branch_name": "<condition_id>"` field — referencing the `condition_id` of the validator state that established the branch (e.g. `"branch_name": "selected_rows"`). Omit the field when the beat is unconditional. When pushed to Notion, beats with the same `branch_name` are grouped under an H3 heading `🔀 <branch_name>`.
- **Once a branch is established, output ALL beats for one branch consecutively before writing ANY beat for the other branch.** Do not interleave. Wrong: rows-step-1, cols-step-1, rows-step-2. Correct: rows-step-1, rows-step-2 … then cols-step-1, cols-step-2. Complete one branch entirely, then the other.
- Fields whose value begins with a `[branch_name]` or `(qualifier)` prefix — e.g. `visual_2: "[selected_rows] Rows buttons activate."`, `on_correct_2: "(example: 4 × 5 = 20) "4 times 5...""` — carry inline context about which branch or condition the content belongs to. Strip the prefix when using the content; use `[branch_name]` values to assign `branch_name` to the corresponding beats, and use `(qualifier)` values to generate named validator states with `condition_id` matching the qualifier.

Do not ignore fields because their name is unfamiliar. Read every field in
the input object and decide where it belongs in the output structure.

**Canonical names:** `workspace_specs.toys` lists the only valid `tangible_type` values for this section.
`workspace_specs.tools` lists the only valid `tool` values. Use these exact strings verbatim — they have already been resolved to their canonical forms.

When `workspace_specs.tools` contains multiple tools, the section has multiple prompt beats — one per tool. Map each tool to the step it belongs to using the dividers and numbered fields as context.


Convert this section object into a single section JSON object following the lesson script schema.
Output only that one section object (not an array).

Scripts are static. Use concrete values throughout. Values are defined
in the spec. Do not invent values; do not use placeholders like [X].

**Dialogue:** carry the spec's dialogue intent directly into the text field.
Keep it clear and functional. Do not add warmth, personality, or flair.
A separate pass handles dialogue enhancement. Do not use em dashes (—).

Include all required phrases from <input>. Avoid all forbidden phrases.

---

## WHAT IS A STEP GROUP

A step group is one **teaching moment** — one idea, paired with its visual. Everything in the group serves that moment. The student presses Next once to advance past it.

**Scene and dialogue are partners.** A step is usually the guide teaching something using a visual: the scene beat shows what appears or changes on screen; the dialogue beat says what it means. They co-narrate the same moment and belong together in the same step.

**Scene beat ordering depends on method.** `add`, `update`, `show`, and `hide` beats set up state — place them before the dialogue they establish. `animate` beats play concurrently with dialogue — place them in the same step alongside the dialogue they accompany.

**Dialogue is animation-agnostic.** Scene beats own the visual description — what highlights, pulses, or animates. Guide dialogue stays at the level of meaning. Prefer dialogue that says what something means ("That bar shows the total for the week.") over dialogue that narrates the animation ("notice the highlighted bar"). Where the spec dialogue already does this well, keep it.

A step group contains at most one prompt beat, always contains dialogue, and always ends with `current_scene`. Multiple dialogue beats are allowed — they collapse into a single block of text for the student.

**Step sizing** — the question for every step boundary is: is this one teaching moment, or two?

- **One moment: keep together.** When beats co-narrate the same thing — a visual and the narration explaining it, an animation and the dialogue it plays alongside — they belong in one step. Splitting them breaks the student's understanding of what's being shown.
- **Two moments: split.** When the section is naming something, introducing a property, or making a distinct conceptual point, each idea belongs in its own step. Two unrelated explanations in one step mean the student is absorbing different things before they can advance.
- **Scene setup is never its own step.** Setup beats (`add`, `update`, `show`, `hide`) always belong to the step whose dialogue they establish. Never end a step immediately after setup beats with no dialogue.

The same principle drives both: if removing one beat would leave the other incomplete or out of context, they belong together. If each beat could stand on its own as a distinct moment, split them.

Valid step group compositions:
- Scene setup beat(s) → Dialogue → `current_scene`  ← default
- Scene setup beat(s) → Dialogue → Prompt → `current_scene`
- Dialogue → Prompt → `current_scene`

**Every prompt is preceded by a dialogue beat.** Dialogue is heard; prompt text is read. The dialogue beat is the guide's narrated setup — the same CTA in spoken register. The prompt text is the concise written instruction the student reads on screen. Both are required; they are not redundant. Consequently, a `student_action` that describes multiple interactions means multiple step groups — one per interaction, each with its own preceding dialogue and ending with `current_scene`. When interactions are closely related, additional dialogue beats may appear within a step group to narrate the transition between them.

`current_scene` is always the last beat in every step group. All step groups are in the flat `beats` array — do not wrap them in a `steps` array.

---

## SECTION STRUCTURE

```json
{
  "id": "s{group}_{seq}_{slug}",
  "beats": [ ... ]
}
```

- `id`: copy verbatim from the input section's `id` field. Do not modify or re-derive it.
- `beats`: flat array of all beats for the entire section. Do **not** nest beats inside steps — put everything in one flat list.

Step groups are implicit: a new step begins after each `current_scene` beat. Every step group ends with a `current_scene` beat.

Every section begins with an empty screen. Everything visible must be put on screen explicitly by `scene` beats in the first step group. Nothing carries over from the previous section.

**Visual clearing phrases** — phrases like "Clean transition", "Practice clears", "Lesson graph clears", "Equation Builder clears", "Lesson visualization fades", and any similar `[thing] clears/fades` form in a `visual` field describe the empty starting state of the section, not an animation to generate. Do **not** create any `scene` or `animate` beat for these. The section already starts with an empty screen; these phrases confirm that and carry no actionable information.

**Transition sections** use `"type": "transition"` on the section object.
They have scene and dialogue beats. No prompts.

---

## BEAT TYPES

### Scene: things happen on screen

```json
{ "type": "scene", "method": "add", "tangible_id": "picture_graph_fruits", "tangible_type": "picture_graph",
  "params": { "mode": "reading", "orientation": "horizontal",
              "categories": ["Apples", "Bananas", "Oranges", "Grapes"],
              "description": "Horizontal picture graph appears. Favorite Fruits data. Each fruit symbol = 1 vote." } }
```
```json
{ "type": "scene", "method": "animate", "tangible_id": "bg_animals",
  "params": { "event": "draw_bar_guideline", "status": "confirmed",
              "description": "Horizontal line draws from top of Monkeys bar to vertical axis, 7 highlights" } }
```
```json
{ "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
  "params": { "highlight_categories": ["Blue", "Yellow"],
              "description": "Blue and Yellow bars highlight." } }
```

Methods: `add` `show` `hide` `animate` `update` `remove`

- Use **`add`** when a tangible appears for the first time. Always include
  `tangible_type` and a `params.description` of what the student sees.
  Include all relevant state fields in `params` (mode, orientation,
  categories, axis range, etc.) drawn from <toy_specs>.
- Use **`animate`** for named animation events: `event` (snake_case),
  `status` (`proposed` = setup in progress / `confirmed` = complete),
  `description` (plain English).
- Use **`update`** when a toy's state changes (highlighting, mode switch,
  template change, button state, expression value, etc.). Always include a
  `params.description` — plain English of what visually changes as a result.
- Use **`show`** / **`hide`** to toggle visibility of a tangible that
  already exists.

For the section-to-section transition (picture graph → bar graph), use
`animate` with `event: "transform_to_bar_graph"` on the picture graph
tangible, then treat subsequent sections as having the bar graph on screen.

### Dialogue: guide speaks

```json
{ "type": "dialogue", "text": "Every part of a graph has a job." }
```
```json
{ "type": "dialogue", "text": "The KEY shows the SCALE." }
```

Translate the spec's dialogue intent directly. Keep it clear and on-point.
Do not embellish. Voice enhancement happens in a later step.

Never use letter labels (A, B, C) in dialogue even if the spec uses them as identifiers. Those labels are system-level placeholders; the visual narration handles what they refer to. Use the actual name, value, or a plain description instead.

### Prompt: student interacts

```json
{
  "type": "prompt",
  "text": "Click on the category that got the MOST votes.",
  "tool": "click_category",
  "target": "picture_graph_fruits",
  "validator": [ ... ]
}
```

Every prompt requires `tool` and `validator`. The tangible in `target` must
already exist in the scene at this point in the step.

**Tool and target usage:**

| `tool` | `target` | `options` |
|---|---|---|
| `click_category` | tangible ID string | — |
| `click_component` | `"tangible_id.component"` string | — |
| `click_tangible` | array of IDs or `{ "type": "..." }` | — |
| `multiple_choice` | — | array of numbers or strings |
| `multi_select` | — | array of strings |

For all other tools (`place_tile`, `add_row`, `add_column`, `select_fill_option`, etc.) — refer to the **Canonical Tools** table in <glossary.md> for the correct `target` and validator condition shape.

`target` shapes:
- Single tangible: `"target": "picture_graph_fruits"`
- Specific component: `"target": "picture_graph_animals.key"`
- Multiple tangibles: `"target": ["pg_fruits", "pg_animals"]`
- All of a type: `"target": { "type": "picture_graph" }`

For `multiple_choice`, include the exact options from the spec:
`"tool": "multiple_choice", "options": [5, 6, 7, 8]`

**Options must be taken verbatim from the `student_action` field.** If `student_action` does not list options explicitly, draw them only from values that appear in the spec's dataset. Never invent, approximate, or calculate distractor values — even plausible-looking ones. An invented distractor may violate module-level constraints (e.g. "all values are multiples of 5") that the spec author enforced but did not repeat in every field.

For `multi_select`, include the category names:
`"tool": "multi_select", "options": ["Dogs", "Cats", "Fish", "Birds", "Lizards"]`

### current_scene: snapshot of the resulting scene

**Must be the last beat in every step** (and the last beat in every
validator state's inner step). It is a pure derived snapshot: reflect
only what `scene` beats have established. Tangibles carry forward
within a section — a tangible stays on screen until a `scene` beat
removes or hides it. Never introduce a tangible or state that no
`scene` beat has declared.

```json
{
  "type": "current_scene",
  "elements": [
    {
      "tangible_id": "picture_graph_fruits",
      "description": "Horizontal picture graph. Favorite Fruits data. Apples row highlighted. Data table alongside.",
      "tangible_type": "picture_graph",
      "mode": "reading",
      "orientation": "horizontal",
      "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
    },
    {
      "tangible_id": "data_table",
      "description": "Data table showing Favorite Fruits values.",
      "tangible_type": "data_table"
    }
  ]
}
```

Each element includes:
- `tangible_id`: the instance ID
- `description`: plain English of what's visible and its current state
- `tangible_type`: canonical type from <toy_specs>
- Relevant state fields from <toy_specs> (mode, orientation, categories, etc.)

If the scene is empty at the end of a step, write `"elements": []`.

---

## VALIDATOR STRUCTURE

Define only the correct state. The remediation generator adds incorrect
states later. Always include `"is_correct": true` on every validator state
you generate.

Every validator state requires a `condition_id` — a short, semantic, stable
identifier (e.g. `"correct"`, `"selected_rows"`, `"placed_3x4"`). Use snake_case.

```json
"validator": [
  {
    "condition_id": "correct",
    "condition": { "selected": "Apples" },
    "description": "Student clicked Apples, correct, 6 votes",
    "is_correct": true,
    "beats": [
      { "type": "scene", "method": "animate", "tangible_id": "picture_graph_fruits",
        "params": { "event": "highlight_category", "status": "confirmed",
                    "description": "Apples row highlights to confirm selection.", "category": "Apples" } },
      { "type": "dialogue", "text": "Apples got the most. 6 people chose it. You read that from the graph." }
    ]
  }
]
```

**Validator beats are feedback only.** They contain the immediate response to
the student's answer: a confirmation scene animation and/or dialogue. They do
NOT contain `current_scene`, do NOT set up the next step's scene, and do NOT
advance the interaction. After the validator fires, execution returns to the
outer beats and the next outer beat runs.

This means:
- Scene setup for the NEXT step goes in outer beats, not in validator beats.
- `current_scene` belongs in the outer beats array, not inside validators.
- Remediation (incorrect) states added later follow the same rule: feedback only.

**On-correct beats must only contain feedback directly about acknowledging
the correct answer.** Do not add beats that narrate the student's specific
path, set up the next scene, or make assumptions about what the student chose.

**When there is a way to be wrong — when the condition specifies a concrete
required answer (any condition that is not `{}` and is not a branching prompt) —
the correct state must have substantive on_correct dialogue.** Name the answer and
close with the principle. `{ "type": "empty" }` is only for interactions where the
student cannot be wrong: branching prompts (both choices are valid) and
any-response-advances (`condition: {}`). Even in two-step interactions, each step
with a concrete correct answer needs its own acknowledgment beat — it may be brief
("4 boxes.") but it must exist.

- For concrete answers (MC, click_category): name the answer, then close by
  naming what the answer demonstrates — the principle or structural insight
  the student just proved. The closing sentence should be transferable to the
  next problem.
  "Apples got the most votes: 6." is the answer. "That's how you read the
  tallest bar." is the principle. Together: "Apples got the most votes: 6.
  That's how you read the tallest bar."
- For open-ended interactions (`variable_answer: true`): simple achievement
  acknowledgment only. Do not narrate the specific values the student may
  have used. You may still close with a transferable principle that does not
  reference the student's specific values. "You got to 20. Any combination
  of equal groups that reaches the total works."
- For branching prompts or any-response-advances where there is no meaningful
  feedback to give: use `{ "type": "empty" }` to signal intentional silence.
  Prefer this over an empty array.

**Never embed a CTA inside on-correct dialogue.** If the feedback text trails
into a lead-in for the next prompt ("5 in each box. So what do you have?"),
split it: the acknowledgment stays in the validator beat ("5 in each box."),
and the CTA ("So what do you have?") goes as a top-level `dialogue` beat
immediately after the prompt in the outer beats array.

**Flag variable-answer interactions.** When a prompt has no fixed correct
answer (`product_equals`, `sum_equals`, or any condition that does not check
a fixed `selected` value), add `"variable_answer": true` to the prompt beat.
This applies to all feedback for that prompt — on_correct and all remediation
states. Downstream steps use this flag to avoid generating language that
assumes a specific answer.

For `multiple_choice`: `{ "condition": { "selected": 7 } }`

For `multi_select` requiring multiple selections:
```json
{ "condition": { "and": [ { "selected": "Dogs" }, { "selected": "Fish" } ] } }
```

**Any-response-advances** (no wrong answer): `"condition": {}`

Use `"condition": {}` only when every response leads to the exact same next scene and step. If the choice determines what the student sees or does next, use a branching prompt instead (see **Branching prompts** above).

Use `condition` for answer-checking (one correct answer, remediation possible). Use `branch: true` for path-taking (both options valid, different beat sequences follow).

### Branching prompts

A **branching prompt** occurs when a student's choice leads to fundamentally
different sequences of interactions — only one path is followed, paths do not
reconverge. Both choices are valid; they lead to different beat sequences.

Use branching when the student picks between options and each choice leads to
different tools, different scene setup, or different follow-up prompts. Do NOT
use branching for standard correct/incorrect validation.

Set `"branching": true` on the prompt beat. Each validator state that
establishes a branch gets `"branch": true` and a short stable `condition_id`
(e.g. `"selected_rows"`, `"selected_columns"`). Both states have `"is_correct": true`.
Branch validator beats must not contain scene setup. Scene setup for each
branch goes in the outer beats with `branch_name`. Branch validator beats
may contain a dialogue beat acknowledging the choice, or `{ "type": "empty" }`
if there is nothing to say. No `current_scene`.

```json
{
  "type": "prompt",
  "text": "Choose rows or columns.",
  "tool": "multiple_choice",
  "options": ["Rows", "Columns"],
  "branching": true,
  "validator": [
    {
      "condition_id": "selected_rows",
      "branch": true,
      "description": "Student chose rows",
      "is_correct": true,
      "beats": [ { "type": "empty" } ]
    },
    {
      "condition_id": "selected_columns",
      "branch": true,
      "description": "Student chose columns",
      "is_correct": true,
      "beats": [ { "type": "empty" } ]
    }
  ]
}
```

All outer beats that belong to a specific branch get `"branch_name": "<condition_id>"`.
Output ALL beats for one branch together before any beats for the other branch.
The unconditional `current_scene` right after the branching prompt captures
the pending-choice state; each branch's own `current_scene` carries `branch_name`.

```json
{ "type": "current_scene", "elements": [ ... ] },

{ "type": "scene", "method": "add", ..., "branch_name": "branch_a" },
{ "type": "prompt", ..., "branch_name": "branch_a",
  "validator": [ { "condition_id": "correct", "condition": { ... }, ... } ] },
{ "type": "current_scene", "elements": [ ... ], "branch_name": "branch_a" },

{ "type": "scene", "method": "add", ..., "branch_name": "branch_b" },
{ "type": "prompt", ..., "branch_name": "branch_b",
  "validator": [ { "condition_id": "correct", "condition": { ... }, ... } ] },
{ "type": "current_scene", "elements": [ ... ], "branch_name": "branch_b" }
```

---

## TWO-STEP INTERACTIONS

Two-step sections have two separate steps, each ending with `current_scene`
in the outer beats. Scene setup for step 2 goes in the outer beats after
step 1's `current_scene` — not inside step 1's validator.

```json
"beats": [
  { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
    "params": { "highlight_categories": ["Yellow", "Red"] } },
  { "type": "dialogue", "text": "Step 1: Find how many chose Yellow or Red in all." },
  { "type": "prompt", "text": "How many liked Yellow or Red in all?",
    "tool": "multiple_choice", "options": [5, 6, 11, 14],
    "validator": [
      {
        "condition_id": "correct",
        "condition": { "selected": 11 },
        "description": "Student answered 11, correct",
        "is_correct": true,
        "beats": [
          { "type": "dialogue", "text": "11 in all. Yellow has 6, Red has 5. 6 plus 5 equals 11." }
        ]
      }
    ]
  },
  { "type": "current_scene", "elements": [ ... ] },
  { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
    "params": { "highlight_categories": ["Green"], "description": "Green bar highlights for step 2." } },
  { "type": "dialogue", "text": "Step 2: Now compare that total to Green." },
  { "type": "prompt", "text": "How many MORE is 11 than Green's 4?",
    "tool": "multiple_choice", "options": [4, 7, 11, 15],
    "validator": [
      {
        "condition_id": "correct",
        "condition": { "selected": 7 },
        "description": "Student answered 7, correct",
        "is_correct": true,
        "beats": [
          { "type": "dialogue", "text": "7 more. You used TWO steps: first added, then compared." }
        ]
      }
    ]
  },
  { "type": "current_scene", "elements": [ ... ] }
]
```

---

## TANGIBLE IDs

| Visual described | ID convention | Examples |
|---|---|---|
| Picture graph | `picture_graph_{slug}` | `picture_graph_fruits`, `picture_graph_animals`, `picture_graph_pets` |
| Bar graph | `bar_graph_{slug}` | `bar_graph_animals`, `bar_graph_books`, `bar_graph_colors` |
| Data table | `data_table` | `data_table` |

Use the same ID consistently. When the spec says "NEW graph," assign a new ID.
`tangible_type` must match the canonical name in <toy_specs> exactly.

---

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Do not reference concepts from <advanced_concepts>. Ground the section's teaching in <the_one_thing>. Include <required_phrases> where genuinely appropriate in dialogue.

These constraints define what this module's students have been taught and what they have not. Values, counts, and data points in scene descriptions, dialogue, and prompt options must be consistent with the module's dataset. Never construct values (e.g. distractor counts, made-up quantities) that fall outside the numerical patterns established by the module's data — even plausible-looking values can violate constraints the spec author enforced implicitly.

---

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Output a single section object starting with `{` and ending with `}`
- Use double quotes throughout



----------------------------------------------------------------------

### Block 3: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>

{
  "id": "s1_1_most_votes",
  "beats": [
    {
      "type": "scene",
      "method": "add",
      "tangible_id": "picture_graph_fruits",
      "tangible_type": "picture_graph",
      "params": {
        "mode": "reading",
        "orientation": "horizontal",
        "categories": ["Apples", "Bananas", "Oranges", "Grapes"],
        "description": "Horizontal picture graph appears. Favorite Fruits data. Apples=6, Bananas=4, Oranges=5, Grapes=3. Key: each fruit symbol = 1 vote."
      }
    },
    {
      "type": "scene",
      "method": "add",
      "tangible_id": "data_table",
      "tangible_type": "data_table",
      "params": {
        "description": "Data table appears alongside graph, showing same Favorite Fruits values."
      }
    },
    {
      "type": "dialogue",
      "text": "Now let's read some other graphs. Every part gives us information to READ. Look at this Favorite Fruits graph."
    },
    {
      "type": "prompt",
      "text": "Click on the category that got the MOST votes.",
      "tool": { "name": "click_category", "tangible_id": "picture_graph_fruits" },
      "validator": [
        {
          "condition": { "selected": "Apples" },
          "description": "Student clicked Apples, correct, 6 votes",
          "is_correct": true,
          "beats": [
            { "type": "dialogue", "text": "Apples got the most votes: 6." },
            {
              "type": "current_scene",
              "elements": [
                {
                  "tangible_id": "picture_graph_fruits",
                  "description": "Horizontal picture graph. Apples row highlighted. Favorite Fruits data.",
                  "tangible_type": "picture_graph",
                  "mode": "reading",
                  "orientation": "horizontal",
                  "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
                },
                {
                  "tangible_id": "data_table",
                  "description": "Data table showing Favorite Fruits values.",
                  "tangible_type": "data_table"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "current_scene",
      "elements": [
        {
          "tangible_id": "picture_graph_fruits",
          "description": "Horizontal picture graph in reading mode. Favorite Fruits data. click_category tool active.",
          "tangible_type": "picture_graph",
          "mode": "reading",
          "orientation": "horizontal",
          "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
        },
        {
          "tangible_id": "data_table",
          "description": "Data table showing Favorite Fruits values alongside the graph.",
          "tangible_type": "data_table"
        }
      ]
    }
  ]
}

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
{
  "id": "s2_1_read_built_rectangle_with_concrete",
  "setup": "The checked rectangle remains visible. The concrete stem appears via §2.10 Drop Down: `___ tiles fill ___ rows of ___, so the area is ___ square units`. Numeric label reveals are paused at this beat — only the row count and row size are referenced.",
  "student_action": "Student uses the checked rectangle to fill the stem, selecting or entering the total tiles, number of rows, row size, and area. Student reads the completed stem aloud or silently with the visible rectangle in view.",
  "teacher_move": "Say: \"Use the checked rectangle to fill the sentence. How many rows do you see? How many squares are in each row?\" Keep the row count and row size separate in the prompts (defeats #M01-2 collapse).",
  "key_observation": "Student ties the built object to a structured sentence and distinguishes row count from row size. This separation is the M01-2 prevention move — never combine row count and row size into a single prompt.",
  "common_detour": "Student reverses the row count and row size (puts row count where row size goes), or fills the total slot from memory without referencing the picture.",
  "intervention": "Point back to the image verbally: \"Count the rows first. Then tell how many squares are in each row.\" Do not advance until the two values are entered in the right slots.",
  "next_move": "Proceed to L.3 (Snap-On Transition / Beat 3).",
  "duration": "~2 minutes.",
  "_generated_at": "2026-04-29T21:16:42.578231+00:00",
  "workspace_specs": {
    "toys": [],
    "student_interactions": [
      "fill_in_blank"
    ]
  },
  "prior_section_summaries": "## s1_0_purpose_frame\n# Section Summary: s1_0_purpose_frame\n\n**VISUAL STATE:**\nNo tangible visual elements are displayed on screen at section end—the current scene contains no rendered objects, graphs, or interactive components.\n\n**CONTENT:**\nThis section introduces the lesson's overarching purpose: students will construct rectangles on a grid to explore the relationship between area, factors, and multiples. The core learning objective is framed as completing the sentence: \"___ is a multiple of ___ because ___ × ___ = ___.\" Students are told they will build rectangles one row at a time and receive feedback on the total number of squares (area) used.\n\n**STUDENT ACTION:**\nNo interaction has occurred yet. This is a framing/setup beat where the teacher explains the task structure and learning goal before students begin building their first rectangle.\n\n---\n\n## s1_1_free_tile_build_find_rectangle\n# Section Summary: s1_1_free_tile_build_find_rectangle\n\n**VISUAL STATE AT SECTION END:**\nThree tangibles are on screen: (1) Hundred Grid in Mode B with grid-snap off, numeric labels hidden, side handles not exposed, displaying 12 tiles arranged in a rectangular formation; (2) Tile Bank (empty, 0 tiles remaining); (3) Sentence Builder displaying the template \"My rectangle has ___ tiles in ___ rows.\" with both number slots completed by the student.\n\n**CONTENT:**\nStudents were introduced to the concept of rectangles as arrangements of equal-length rows. The vocabulary term \"rectangle\" was formally introduced in the context of describing a shape formed by tiles arranged in rows of equal length. The lesson emphasized that rectangles have rows with the same number of tiles in each row.\n\n**STUDENT ACTION:**\nThe student placed 12 tiles on the hundred grid to form a valid rectangle (variable arrangement, but all configurations with equal-length rows were accepted), then filled two number slots in a sentence builder to describe their rectangle's dimensions—specifying the total tile count and the number of rows in their specific arrangement."
}
</input>

======================================================================

## Prefill

{

