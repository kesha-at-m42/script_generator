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

**Step Content Fields:**

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
    "dialogue": "Look at the point on the number line. What fraction does it represent?",
    "prompt": "What fraction does this point show?",
    "interaction_tool": "select",
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
          {"id": "a", "text": "1/3"},   // Distractor (adjacent fraction on line)
          {"id": "b", "text": "2/3"},   // Correct answer
          {"id": "c", "text": "3/2"}    // Obviously incorrect (reversed, > 1)
        ]
      }
    ],
    "correct_answer": {
      "value": "b",
      "context": "The point is at 2/3, the second tick mark"
    },
    "success_path_dialogue": "Yes, that's two-thirds."
  }
```

## IMPORTANT NOTES

- Each problem instance creates ONE item
- All metadata fields (problem_id, mastery_tier, mastery_verb, etc.) are at the TOP LEVEL of each item
- Keep dialogue conversational and supportive
- Parse workspace descriptions carefully to create accurate tangible structures
- Use description field in tangibles when workspace mentions specific characteristics
- Extract all fractions/denominators from variables_used into fractions array

Generate NOW!
""",

    doc_refs=["visuals.md", "guide_design.md"],

    output_structure="""
  {
    "problem_id": 1,
    "mastery_tier": "BASELINE",
    "mastery_verb": "IDENTIFY",
    "template_id": "4001",
    "fractions": ["1/3"],
    "dialogue": "...",
    "prompt": "...",
    "interaction_tool": "place_point|drag_label|click_choice|select|multi_select|place_tick|cut_shape|shade",
    "workspace": [
      {
        "id": "line_1",
        "type": "number_line",
        "range": [0, 1],
        "ticks": ["0", "1/3", "2/3", "1"],
        "points": [],
        "labels": ["0", "1"]
      },
      {"type": "choices", "options": [{...}]}
    ],
    "correct_answer": {
      "value": "...",
      "context": "..."
    },
    "success_path_dialogue": "Great work!"
  }
""",

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
