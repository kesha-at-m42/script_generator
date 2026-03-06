"""
warmup_generator - AI Prompt

Converts a warmup.md spec into section JSON objects following the
lesson script schema (sections / steps / beats).

Input (user message):
    <warmup_spec>   — full warmup.md content
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

WARMUP_GENERATOR_PROMPT = Prompt(
    role="""You are converting a warmup specification into structured JSON sections. This is TRANSLATION work — the pedagogical decisions have already been made. Your job is faithful conversion into the lesson script schema.""",
    instructions="""
## TASK

Convert every interaction in <warmup_spec> into a section JSON object.
Produce one section per interaction, in order. Output the full array.

Scripts are static. Use concrete values throughout — never write placeholders
like [X] or [category_A]. If the spec describes dynamic values (e.g. counting
results that vary per student), choose specific example values that fit the
spec's constraints and use those consistently across all sections.

---

## SECTION STRUCTURE

```json
{
  "id": "s{group}_{seq}_{slug}",
  "scene": ["tangible_id", ...],
  "steps": [ [...], [...] ]
}
```

- `id` — follow the naming convention from the schema guide. For warmup interactions
  use a slug that reflects the interaction's purpose (e.g. `s1_1_data_collection`,
  `s1_2_symbol_selection`, `s1_3_graph_creation`, `s1_4_bridge`)
- `scene` — tangible IDs **already on screen** when the section begins (carried
  in from a previous section). Omit or leave empty if the screen starts fresh.
- `steps` — array of arrays; each inner array is one step (all beats in a step
  play together before the lesson pauses)

---

## SCENE RULES

The section-level `scene` array is the **initial state** — tangibles present
on screen when the section begins. Every scene beat that adds, removes, shows, or
hides a tangible changes what is on screen.

A prompt may only reference tangibles that currently exist in the scene at
that point in the step sequence.

---

## BEAT TYPES

### current_scene
**Must be the first beat in every step.** Reflects the exact state of the
workspace at the start of that step — after all scene changes from previous steps.

```json
{
  "type": "current_scene",
  "elements": [
    {
      "tangible_id": "pg_warmup",
      "description": "Horizontal picture graph in creating mode. Cats row complete (5 symbols). Dogs and fish rows empty. Key shows selected symbol.",
      "tangible_type": "picture_graph",
      "mode": "creating",
      "orientation": "horizontal",
      "categories": ["cats", "dogs", "fish"],
      "completed_categories": ["cats"]
    }
  ]
}
```

Each element includes:
- `tangible_id` — the instance ID
- `description` — plain English of what's currently visible and its state
- `tangible_type` — canonical type from <toy_specs>
- Any relevant state fields drawn from <toy_specs> (mode, orientation, categories, etc.)

If the workspace is empty at the start of a step, write `"elements": []`.

---

### Dialogue
```json
{ "type": "dialogue", "text": "Let's count how many of each there are." }
```
Guide speech. Follow <guide_design> for all voice and language decisions —
tone calibration, praise language, conciseness limits, and anti-patterns.
For warmup: lean toward "Friendly Teacher" on the warmth spectrum; keep
pre-action dialogue to 1–3 sentences.

### Scene
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_id": "counting_game",
  "params": {
    "event": "reveal_counts",
    "status": "confirmed",
    "description": "Guide counts visually, confirming 5 cats, 3 dogs, 7 fish"
  }
}
```
Visual change on a tangible. Methods: `show` `hide` `animate` `update` `add` `remove`.
`animate` requires: `event` (snake_case), `status` (`proposed` for setup /
`confirmed` for completion), `description` (plain English of what happens on screen).
`add` requires both `tangible_id` and `tangible_type`.

For picture graph scenes, refer to <toy_specs> for available modes (Mode 1: Reading /
Mode 2: Creating), symbol states, allowed student actions, and animation types.
Include `"mode"` in `params` when adding or animating a picture graph tangible.

### Prompt
```json
{
  "type": "prompt",
  "text": "Which category had the most?",
  "tool": { "name": "click_category", "tangible_id": "pg_warmup" },
  "validator": [ ... ]
}
```
Student interaction point. Every prompt requires `tool` and `validator`.
Every tangible referenced in `tool` must exist in the current workspace.

---

## DERIVING TANGIBLE IDs FROM THE SPEC

Read the spec's visual descriptions to identify tangibles. Refer to <toy_specs>
for the full definition of each tangible type used in this unit. Use these
naming conventions:

| Visual described | ID convention | Examples |
|---|---|---|
| Picture graph | `pg_{slug}` | `pg_warmup` |
| Bar graph | `bg_{slug}` | `bg_warmup` |
| Counting / game widget | `{type}_game` | `counting_game` |
| Symbol / item palette | `{item}_palette` | `symbol_palette` |
| Number line | `nl_{slug}` | `nl_warmup` |
| Data table | `data_table` | `data_table` |

Use the same ID consistently across all sections that reference the same tangible.

---

## TOOL NAMES

Use the documented tool names from the schema guide where they fit. For
warmup-specific interactions not covered by the standard tools, use a
descriptive snake_case name that clearly communicates the action:

| Documented tools | Use for |
|---|---|
| `click_category` | Student clicks a category within a graph |
| `click_tangible` | Student selects one or more tangibles from the workspace |
| `multiple_choice` | Student picks from a list of options |
| `multi_select` | Student selects multiple options |

| Warmup-specific tools | Use for |
|---|---|
| `counter` | Student uses an up/down counter to track a count |
| `place_symbol` | Student clicks to add symbols to a graph row |
| `select_symbol` | Student selects a symbol from a palette |

For `place_symbol`, include a `config` with the target category and expected count:
`"config": { "category": "dogs", "correct_count": 3 }`

---

## VALIDATOR STRUCTURE

The validator is a flat array of states evaluated in order; first match wins.
Each state has `condition`, `description`, and `steps` (inline beats).

Define only the correct state. The remediation generator adds incorrect states later.

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student selected the correct category",
    "steps": [
      [
        { "type": "dialogue", "text": "Right — Apples had the most." }
      ]
    ]
  }
]
```

**Any-response-advances** (no wrong answer — e.g. open choice, game completion):
use `condition: {}` as the single state:

```json
"validator": [
  {
    "condition": {},
    "description": "Any response advances",
    "steps": [
      [
        { "type": "dialogue", "text": "Got it. Let's make a graph with that data." }
      ]
    ]
  }
]
```

---

## STEP GROUPING RULES

- Every step starts with a `current_scene` beat reflecting state at that point
- Each step ends at a student `prompt` beat OR a distinct scene transition
- Group setup dialogue + scene beats in the step before the prompt
- Post-interaction beats (guide success feedback, reveals) go in the correct
  validator state's `steps`, not as a separate section step
- If an interaction has sub-parts (e.g. "I do → You do → You do"),
  make each sub-part a separate step in the same section

---

## READING THE INTERACTION SPEC

For each interaction:

1. **Hook / visual setup** → `scene` beat(s) + opening `dialogue` beat(s)
2. **Guide framing** → `dialogue` beat(s)
3. **Student task** → `prompt` beat (derive tool from described action; define
   validator with the correct state only)
4. **On Complete / Guide reveal** → beats inside the correct validator state's
   `steps`, or as a follow-up step if it precedes the next interaction
5. **Sub-parts** → separate steps within the same section, scaffold fading
   exactly as described in the spec
6. **Bridge / no student task** → `dialogue` + `scene` beats only, no prompt

---

## TANGIBLE TYPES

`tangible_type` is required on `scene add` beats. Use the canonical type names
defined in <toy_specs> — do not invent type strings. For example, the type
for a picture graph tangible must match the name defined in toy_specs exactly.

---

## OUTPUT RULES

- Output ONLY valid JSON — no explanation, no markdown fences
- Entire response must be an array starting with `[` and ending with `]`
- One section object per interaction, in spec order
- Use double quotes throughout

""",
    doc_refs=[
        "guide_design.md",
        "toy_specs.md",
    ],
    output_structure="""
[
  {
    "id": "s1_1_data_collection",
    "scene": ["counting_game"],
    "steps": [
      [
        {
          "type": "scene",
          "method": "animate",
          "tangible_id": "counting_game",
          "params": {
            "event": "minis_appear",
            "status": "proposed",
            "description": "Minis characters appear in animated counting scenario"
          }
        },
        {
          "type": "dialogue",
          "text": "Check this out — the Minis are on the move! Let's count how many of each there are."
        },
        {
          "type": "prompt",
          "text": "Use the counter to count each type.",
          "tool": { "name": "counter", "tangible_id": "counting_game" },
          "validator": [
            {
              "condition": {},
              "description": "Any count recorded — game completes",
              "steps": [
                [
                  { "type": "dialogue", "text": "Let's see if you counted them all." },
                  {
                    "type": "scene",
                    "method": "animate",
                    "tangible_id": "counting_game",
                    "params": {
                      "event": "reveal_counts",
                      "status": "confirmed",
                      "description": "Guide counts visually, confirming 5 cats, 3 dogs, 7 fish"
                    }
                  },
                  { "type": "dialogue", "text": "There were 5 cats, 3 dogs, and 7 fish." }
                ]
              ]
            }
          ]
        }
      ]
    ]
  },
  {
    "id": "s1_3_graph_creation",
    "scene": ["pg_warmup"],
    "steps": [
      [
        { "type": "dialogue", "text": "Watch how I show our cats on the graph." },
        {
          "type": "scene",
          "method": "animate",
          "tangible_id": "pg_warmup",
          "params": {
            "event": "add_symbols_guided",
            "status": "proposed",
            "description": "5 symbols appear one at a time in the cats row as guide narrates",
            "category": "cats",
            "count": 5
          }
        },
        { "type": "dialogue", "text": "5 symbols. Each one means 1 cat." }
      ],
      [
        { "type": "dialogue", "text": "Your turn. You counted 3 dogs. Add 3 symbols — one for each dog you counted." },
        {
          "type": "prompt",
          "text": "Add 3 symbols to the dogs row.",
          "tool": {
            "name": "place_symbol",
            "tangible_id": "pg_warmup",
            "config": { "category": "dogs", "correct_count": 3 }
          },
          "validator": [
            {
              "condition": { "tangible_id": "pg_warmup", "symbol_count": 3, "category": "dogs" },
              "description": "Student placed exactly 3 symbols in the dogs row",
              "steps": [
                [
                  { "type": "dialogue", "text": "3 symbols. One for each dog." }
                ]
              ]
            },
          ]
        }
      ]
    ]
  }
]
""",
    prefill="[",
    examples=[],
    module_ref={},
    template_ref={},
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=8000,
    stop_sequences=[],
)
