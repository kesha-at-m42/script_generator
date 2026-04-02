"""
section_structurer - AI Prompt

Converts a structured spec (output of spec_parser) into section JSON objects
following the lesson script schema (sections / steps / beats).

Input is a flat JSON array of section objects, each with:
  - key-value fields extracted from the original markdown spec
  - workspace_specs: { toys: [...], tools: [...] } declaring what's on screen

Dialogue voice and enhancement are handled downstream by dialogue_rewriter.
This step focuses on structural correctness and faithful spec translation.

Input (user message):
    <input>   - structured_spec.json (array of parsed section objects)
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

SECTION_STRUCTURER_PROMPT = Prompt(
    role="""You are translating a lesson specification into structured section JSON. Your job is faithful, precise translation: every interaction in the spec becomes a correctly structured section object with the right beats, tools, validators, and scene state. Dialogue is functional. Preserve the pedagogical intent from the spec without embellishment.""",
    instructions="""
## TASK

<input> is a single structured section object produced by starterpack_parser.

It contains key-value fields extracted from the original spec
(visual, guide, prompt, correct_answer, on_correct, on_incorrect, purpose, etc.)
and a `workspace_specs` field: `{ "toys": ["picture_graph", "data_table"], "tools": ["click_category"] }`.

**Canonical names:** `workspace_specs.toys` lists the only valid `tangible_type` values for this section.
`workspace_specs.tools` lists the only valid `tool` values. Use these exact strings verbatim — they have
already been resolved to their canonical forms.

Convert this section object into a single section JSON object following the lesson script schema.
Output only that one section object (not an array).

Scripts are static. Use concrete values throughout. Values are defined
in the spec. Do not invent values; do not use placeholders like [X].

**Dialogue:** carry the spec's dialogue intent directly into the text field.
Keep it clear and functional. Do not add warmth, personality, or flair.
A separate pass handles dialogue enhancement. Do not use em dashes (—).

Include all required phrases from <input>. Avoid all forbidden phrases.

---

## WHAT IS A STEP

A step is a **do-together block**: all beats in a step play together without pausing. The step ends, and the system pauses, when student input is required.

Student input is required when:
1. **Dialogue plays** (animations happen alongside dialogue): the student must act or respond after the guide speaks
2. **A prompt beat**: the student explicitly interacts with a tangible or overlay tool

Everything before that pause belongs in the same step. Beat order within a step:

1. Scene beats (`add`, `show`, `animate`, `update`): things appear or change on screen
2. Dialogue beats: the guide speaks (animations play alongside)
3. Prompt beat: student interacts (only one prompt per step; always the last non-snapshot beat)
4. `current_scene`: snapshot of what is on screen after all beats in this step

---

## SECTION STRUCTURE

```json
{
  "id": "s{group}_{seq}_{slug}",
  "steps": [ [...], [...] ]
}
```

- `id`: derive from the spec's section numbering. Group = lesson section
  (1, 2, 3). Seq = interaction number within that section. Slug = purpose.
  Every section **must** have a unique `major.minor` combination — no two
  sections may share the same number. When one interaction spans multiple
  sections (e.g. build rows → add columns → write equation), use letter
  suffixes to keep them distinct: `s3_2a_build_rows`, `s3_2b_add_columns`,
  `s3_2c_write_equation`.
  Examples: `s1_1_most_votes`, `s2_2_reading_independently`,
  `s3_3b_two_step_total`, `s2_transition`
- `steps`: array of arrays; each inner array is one step (do-together block ending when student input is required)

Every section begins with an empty screen. Everything visible must be put on screen explicitly by `scene` beats in the first step. Nothing carries over from the previous section.

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

`target` shapes:
- Single tangible: `"target": "picture_graph_fruits"`
- Specific component: `"target": "picture_graph_animals.key"`
- Multiple tangibles: `"target": ["pg_fruits", "pg_animals"]`
- All of a type: `"target": { "type": "picture_graph" }`

For `multiple_choice`, include the exact options from the spec:
`"tool": "multiple_choice", "options": [5, 6, 7, 8]`

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

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student clicked Apples, correct, 6 votes",
    "is_correct": true,
    "steps": [
      [
        { "type": "scene", "method": "animate", "tangible_id": "picture_graph_fruits",
          "params": { "event": "highlight_category", "status": "confirmed",
                      "description": "Apples row highlights to confirm selection", "category": "Apples" } },
        { "type": "dialogue", "text": "Apples got the most. 6 people chose it. You read that from the graph." },
        { "type": "current_scene", "elements": [ ... ] }
      ]
    ]
  }
]
```

Validator state `steps` follow the same beat ordering and also end with
`current_scene`. **Scene beats are allowed and expected in correct validator
states whenever a visual change accompanies the feedback.**

**`current_scene` in validator states must follow the same rule as everywhere
else: it only mirrors what `scene` beats have declared. If the correct response
requires no visual change, the `current_scene` must describe the tangibles in
exactly the same state as before — no new adjectives, no "confirmed", no added
state. Do not use the description field to imply a change that no `scene` beat
produced.**

```json
// WRONG — current_scene inventing a visual state:
[
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Red items confirmed as 40." }] }
]

// RIGHT — if no visual change, description is identical to prior state:
[
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Minis counting scene. Red, Blue, Yellow items visible." }] }
]

// RIGHT — if a visual change is needed, declare it with a scene beat first:
[
  { "type": "scene", "method": "animate", "tangible_id": "minis_counting_scene",
    "params": { "event": "mark_counted", "status": "confirmed",
                "description": "Red items highlight as counted, count of 40 appears", "category": "Red" } },
  { "type": "dialogue", "text": "That's right, 40." },
  { "type": "current_scene", "elements": [{ ..., "description": "Minis counting scene. Red items highlighted as counted." }] }
]
```

For `multiple_choice`: `{ "condition": { "selected": 7 } }`

For `multi_select` requiring multiple selections:
```json
{ "condition": { "and": [ { "selected": "Dogs" }, { "selected": "Fish" } ] } }
```

**Any-response-advances** (no wrong answer): `"condition": {}`

---

## TWO-STEP INTERACTIONS

Two-step sections have two separate steps, each ending with `current_scene`.
The correct validator state of step 1 sets up the visual state for step 2
(highlight the next target, display the running total, etc.), then step 2
begins with those scene changes already reflected.

```json
"steps": [
  [
    { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
      "params": { "highlight_categories": ["Yellow", "Red"] } },
    { "type": "dialogue", "text": "Step 1: Find how many chose Yellow or Red in all." },
    { "type": "prompt", "text": "How many liked Yellow or Red in all?",
      "tool": { "name": "multiple_choice", "options": [5, 6, 11, 14] },
      "validator": [
        {
          "condition": { "selected": 11 },
          "description": "Student answered 11, correct",
          "steps": [
            [
              { "type": "dialogue", "text": "11 in all. Yellow has 6, Red has 5. 6 plus 5 equals 11." },
              { "type": "scene", "method": "update", "tangible_id": "bar_graph_colors",
                "params": { "highlight_categories": ["Green"] } },
              { "type": "current_scene", "elements": [ ... ] }
            ]
          ]
        }
      ]
    },
    { "type": "current_scene", "elements": [ ... ] }
  ],
  [
    { "type": "dialogue", "text": "Step 2: Now compare that total to Green." },
    { "type": "prompt", "text": "How many MORE is 11 than Green's 4?",
      "tool": { "name": "multiple_choice", "options": [4, 7, 11, 15] },
      "validator": [
        {
          "condition": { "selected": 7 },
          "description": "Student answered 7, correct",
          "steps": [
            [
              { "type": "dialogue", "text": "7 more. You used TWO steps: first added, then subtracted to compare." },
              { "type": "current_scene", "elements": [ ... ] }
            ]
          ]
        }
      ]
    },
    { "type": "current_scene", "elements": [ ... ] }
  ]
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

## OUTPUT RULES

- Output ONLY valid JSON. No explanation, no markdown fences.
- Output a single section object starting with `{` and ending with `}`
- Use double quotes throughout

""",
    doc_refs=[
        "glossary.md",
    ],
    output_structure="""
{
    "id": "s1_1_most_votes",
    "steps": [
      [
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
              "steps": [
                [
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
    ]
  }
}
""",
    prefill="{",
    examples=[],
    module_ref={},
    template_ref={},
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=32000,
    stop_sequences=[],
)
