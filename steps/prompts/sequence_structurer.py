"""
Sequence Structurer - Transforms problem instances into structured interaction sequences
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

SEQUENCE_STRUCTURER_PROMPT = Prompt(
    role="""You are an expert at transforming educational problem specifications into
structured, interactive learning sequences. You convert flat problem descriptions into
detailed step-by-step sequences with precise workspace configurations and interaction tools.""",

    instructions="""
## TASK

Transform problem instances into a structured interaction schema.

## INPUT FORMAT

You receive problem instances with:
- problem_instance_id, template_id, problem_type
- **no_of_steps** (number): 1 for single-step, 2 for multi-step problems
- action_description (student action)
- prompt (student-facing question)
- workspace_description (text description of visuals)
- mastery_tier (support, confidence, baseline, stretch, challenge)
- variables_used (fractions/denominators tested)
- application_context (optional narrative)

## OUTPUT FORMAT

Generate a structured interaction sequence using these fields:

**Required Top-Level Fields:**
- problem_id: Use problem_instance_id
- mastery_tier: Copy from input (support, confidence, baseline, stretch, challenge)
- mastery_verb: Map problem_type to CREATE|IDENTIFY|COMPARE|APPLY
- template_id: Copy from input
- fractions: Extract from variables_used array
- **no_of_steps**: Copy from input (1, 2, 3, or any positive integer)
- **steps**: Array ALWAYS present, containing N step objects (where N = no_of_steps)
  - Single-step: Array with 1 item
  - Multi-step: Array with N items

## HANDLING SINGLE-STEP vs MULTI-STEP

**IMPORTANT: Always output a `steps` array, regardless of no_of_steps value**

**If no_of_steps = 1 (or missing):**
- Generate steps array with ONE item: `"steps": [{ "step_id": 1, ... }]`
- Use input fields directly (workspace_description, prompt, action_description)
- No workspace_inherited flag needed

**If no_of_steps > 1 (multi-step):**
- Generate steps array with N items: `"steps": [{ "step_id": 1, ... }, { "step_id": 2, ... }, ...]`
- **Parse** input fields to extract step-specific information for EACH step
- Input format uses numbered markers: "Step 1:", "Step 2:", etc.
- Add `workspace_inherited: true` to Step 2+

### Multi-Step Parsing Strategy

**1. workspace_description** - Look for "Step N:" markers:
```
"Step 1: Blank line. Step 2: Add labels. Step 3: Verify positions."
→ Extract text between each "Step N:" marker
→ Build workspace for each step
→ Later steps inherit results from earlier steps
```

**2. action_description** - Look for "(step N)" markers:
```
"Student places ticks (step 1), drags labels (step 2), confirms (step 3)."
→ Extract action phrase before each "(step N)"
→ Map to interaction_tool
```

**3. prompt** - Split on "then" or commas:
```
"Divide line, then label positions, then check your work."
→ Step 1: "Divide line into fourths."
→ Step 2: "Label each position."
→ Step 3: "Check that all labels are correct."
```

**4. dialogue** - Generate conversational intros:
```
Step 1: "Let's [task]."
Step 2: "Now [task]."
Step 3+: "Next, [task]."
Final: Use conclusive language
```

**5. Workspace Inheritance** - Each step builds on previous:
```
Step 1 output → Step 2 input
Step 2 output → Step 3 input
Calculate expected results (ticks placed, labels added, etc.)
```

**6. Marking Inherited Workspaces:**
- **Step 1**: Never inherited, omit the flag or set `"workspace_inherited": false`
- **Step 2+**: If workspace contains elements from previous step, add `"workspace_inherited": true`
- This flag helps downstream processing (e.g., godot_formatter) handle workspace merging

**Step Content Fields:**

Each step object contains:

**step_id:** (number) Sequential identifier (1, 2, 3, ...)

**workspace_inherited:** (boolean, optional for multi-step only)
- Add this field to Step 2 and beyond in multi-step problems
- `true` if workspace builds upon/inherits from previous step
- `false` or omit for Step 1 (first step never inherits)
- Helps godot_formatter optimize workspace handling

**dialogue:** Create conversational setup (10-30 words)
- IMPORTANT: Try to use the same verb as the prompt (if prompt says "Place", dialogue can say "Let's place..." or "place")
- If application_context exists, incorporate it naturally
- If prompt contains scaffolding hints, move them to dialogue
- Reference visual elements generically ("number line", "bars", "circles")
- Use supportive, clear language
- Adjust scaffolding based on mastery_tier (support=most guidance, challenge=least)
- Follow <guide_design> "Problem Setup Dialogue" section

**prompt:** Create a self-explanatory, direct instruction that the student can solve with just the prompt alone
- The student should know exactly what fraction to work with by reading only the prompt. It's still a problem though, so don't give away the answer. Make this decision based on the skill being tested here: {skill}
- If the prompt already meets these criteria, keep it as-is
- Strip any application_context (e.g., "Maya ate 1/4...") from the prompt and move it to dialogue instead
- Strip any scaffolding hints (e.g., "One interval from zero", "That's two spaces", "Count the intervals...") from the prompt and move them to dialogue instead
- Keep prompt focused on the core mathematical task (e.g., "Place three-fourths on the number line.")

**interaction_tool:** Derive from action_description

Map action_description to tool:
- "Point at tick marks" → "place_point" (student places points on existing ticks)
- "Label tick marks by dragging" → "drag_label" (student drags fraction labels onto ticks)
- "Select from MCQ options" → "click_choice" (student clicks one or more MCQ options; use allow_multiple flag in choices for multiple selection)
- "Select the number line" → "select" (student selects one tangible from workspace)
- "Select multiple number lines" → "multi_select" (student selects multiple tangibles)
- "Place ticks on number line" → "place_tick" (student partitions/divides number line)
- "Cut shape into parts" → "cut_shape" (student divides shapes into parts)
- "Shade parts" → "shade" (student shades/paints sections)

**Pattern for new actions:**
If you encounter an action_description not listed above:
1. Identify the verb (e.g., "Draw", "Rotate", "Match", "Connect")
2. Identify the object (e.g., "lines", "shapes", "dots", "segments")
3. Create tool name: `{verb}_{object}` in snake_case (e.g., "Draw lines between points" → "draw_line")
4. Follow these conventions:
   - Actions on multiple items use plural: "select" vs "multi_select"
   - Dragging/moving actions: use "drag_{object}"
   - Placing/positioning: use "place_{object}"
   - Selecting/clicking: use "select" or "click_{object}"
   - Modifying properties: use "{verb}_{object}" (e.g., "color_region", "resize_bar")
5. Add a brief clarification in parentheses describing what the student does

**workspace:** Parse workspace_description into structured toys array
**CRITICAL: You MUST strictly follow ALL visual schemas defined in <visuals>. Consult the documentation for each shape type to understand:**
- Required and optional properties
- Valid value ranges and types
- Constraints (e.g., max number of instances, allowed denominators)
- Structural relationships (e.g., points must correspond to ticks)

**Parsing Natural Language to Structured Workspace:**
1. Identify the shape type(s) mentioned in workspace_description
2. Look up the corresponding schema in <visuals>
3. Extract property values from the text description (e.g., "from 0 to 1" → range: [0, 1])
4. Build the workspace element following the exact schema structure
5. For special elements (MCQ choices, drag palettes), check if interaction_tool requires them and add accordingly

**Special Workspace Elements:**
- **choices**: Add when interaction_tool is "click_choice" or description mentions "MCQ options"
  Format: {"type": "choices", "options": [{"id": "a", "text": "..."}, ...]}
  Use "allow_multiple": true for multi-select questions

- **palette**: Add when interaction_tool is "drag_label"
  Format: {"type": "palette", "labels": ["1/4", "2/4", ...]}
  Optional quantities array for label availability

**correct_answer:** Object with:
- value: The expected answer (format depends on interaction_tool)
- context: Brief explanation of why this is correct

**success_path_dialogue:** Rotate through the success_dialogue examples from the template here: {success_dialogue}
## EXAMPLE TRANSFORMATIONS

**Input:**
```json
{
  "problem_instance_id": 49,
  "template_id": "4008",
  "problem_type": "identify",
  "action_description": "Select matching fraction from MCQ options",
  "prompt": "What fraction does this point show?",
  "workspace_description": "Number line from 0 to 1 with tick marks at 0, 1/3, 2/3, 1. Point placed at 2/3. Only endpoints labeled. MCQ options: 1/3, 2/3, 3/3.",
  "mastery_tier": "BASELINE",
  "variables_used": {"fractions": ["2/3"]}
}
```

**Output:**
```json
  {
    "problem_id": 49,
    "mastery_tier": "BASELINE",
    "mastery_verb": "IDENTIFY",
    "template_id": "4008",
    "fractions": ["2/3"],
    "no_of_steps": 1,
    "steps": [
      {
        "step_id": 1,
        "dialogue": "Look at the point on the number line. What fraction does it represent?",
        "prompt": "What fraction does this point show?",
        "interaction_tool": "click_choice",
        "workspace": [
          {
            "id": "line_1",
            "type": "number_line",
            "range": [0, 1],
            "ticks": ["0", "1/3", "2/3", "1"],
            "points": ["2/3"],
            "labels": ["0", "1"]
          },
          {
            "type": "choices",
            "options": [
              {"id": "a", "text": "1/3"},
              {"id": "b", "text": "2/3"},
              {"id": "c", "text": "3/2"}
            ]
          }
        ],
        "correct_answer": {
          "value": "b",
          "context": "The point is at 2/3, the second tick mark"
        },
        "success_path_dialogue": "Yes, that's two-thirds."
      }
    ]
  }
```

## IMPORTANT NOTES

### Structure Rules:
- Each problem instance creates ONE output item
- Metadata fields (problem_id, mastery_tier, etc.) always at TOP LEVEL
- **ALWAYS include `steps` array** (even for single-step problems)
- **Single-step (no_of_steps = 1)**: `steps` array has ONE item
- **Multi-step (no_of_steps > 1)**: `steps` array has N items

### Multi-Step Requirements:
- Parse "Step N:" markers from workspace_description
- Parse "(step N)" markers from action_description
- Split prompt on "then" or commas
- Add `workspace_inherited: true` to Step 2+
- Each step has unique step_id (1, 2, 3, ...)

### General:
- Keep dialogue conversational and supportive
- Parse workspace descriptions carefully to create accurate tangible structures
- Extract all fractions/denominators from variables_used into fractions array

Generate NOW!
""",

    doc_refs=["visuals.md", "guide_design.md"],

    output_structure="""{
  "problem_id": 1,
  "mastery_tier": "BASELINE",
  "mastery_verb": "CREATE",
  "template_id": "5011",
  "fractions": ["1/4", "2/4", "3/4"],
  "no_of_steps": 2,
  "steps": [
    {
      "step_id": 1,
      "dialogue": "...",
      "prompt": "...",
      "interaction_tool": "place_tick",
      "workspace": [],
      "correct_answer": {},
      "success_path_dialogue": "..."
    },
    {
      "step_id": 2,
      "workspace_inherited": true,
      "dialogue": "...",
      "prompt": "...",
      "interaction_tool": "drag_label",
      "workspace": [],
      "correct_answer": {},
      "success_path_dialogue": "..."
    }
  ]
}""",

    prefill="""{
  "problem_id": {problem_instance_id},
  "mastery_tier": "{mastery_tier}",
  "mastery_verb": "{mastery_verb}",
  "template_id": "{template_id}",
  "fractions": """,

    examples=[],

    module_ref={},

    template_ref=["mastery_verb", "success_dialogue", "skill"],

    cache_docs=False,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
