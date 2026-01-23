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

Transform problem instances into structured interactive sequences.

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

Generate sequences with structured steps containing:

**1. Metadata:**
- problem_id: Use problem_instance_id
- difficulty: Map mastery_tier to 0-4 (support=0, confidence=1, baseline=2, stretch=3, challenge=4)
- verb: Map problem_type to CREATE|IDENTIFY|COMPARE|APPLY
- template_id: Copy from input
- fractions: Extract from variables_used

**2. Step Structure:**

Each step includes:

**a. prompt:** Use the input prompt as-is

**b. dialogue:** Create conversational setup (10-30 words)
- If application_context exists, incorporate it naturally
- Reference visual elements generically ("number line", "bars", "circles")
- Use supportive, clear language
- Adjust scaffolding based on difficulty (lower=more guidance)

**c. interaction_tool:** Map action_description to tool (refer to visuals.md allowed actions)

Based on visuals.md allowed student actions:
- "Point at tick marks" → "place_point" (student places points on ticks)
- "Label tick marks by dragging" → "drag_label" (student drags fraction labels onto ticks)
- "Select from MCQ options" OR "Select matching fraction from MCQ options" → "click_choice"
- "Select the number line" OR "Select" → "select" (choose one or more number lines/shapes)
- "Select multiple" → "multi_select"

Additional tools from lesson_generator.py:
- "cut", "shade", "none" (for future use with other shapes)


**d. workspace:** Parse workspace_description into structured toys

Refer to <visuals> for the precise structure of number line elements.

**Number Line Parsing Rules (based on visuals.md):**
- "Number line from X to Y" → range: [X, Y]
- "tick marks at 0, 1/3, 2/3, 1" → ticks: ["0", "1/3", "2/3", "1"]
- "Point placed at 2/3" → points: ["2/3"]
- "Only endpoints labeled" OR "Only 0 and 1 are labeled" → labels: ["0", "1"] (or labels: true/false)
- "with tick marks dividing it into X equal intervals" → calculate ticks array based on X
- "MCQ options below: A, B, C" → add choices element to workspace

**Number Line Structure:**
```json
{
  "id": "line_1",
  "type": "number_line",
  "range": [0, 1],
  "ticks": ["0", "1/3", "2/3", "1"],
  "points": ["2/3"],  // Optional: highlighted ticks
  "labels": ["0", "1"]  // Optional: which ticks show labels
}
```

**For comparison sets (multiple number lines):**
- Parse "Line A:", "Line B:", "Line C:" as separate toys with unique ids
- Each gets its own ticks configuration
- Use description field to explain distinguishing characteristics

**MCQ Handling:**
- When workspace_description mentions "MCQ options:", add a choices element to workspace
- Choices is a workspace element with type: "choices" and options array
- Format: {"type": "choices", "options": [{"id": "a", "text": "1/2"}, {"id": "b", "text": "1/3"}, ...]}
- If fractions are listed like "1/3, 2/3, 3/3", create sequential ids (a, b, c, etc.)

**e. correct_answer:**
- value: The expected answer (fraction like "2/3", tick index like [2], choice id like "b", tangible id like "line_equal")
- context: Brief explanation of why this is correct

**f. student_attempts.success_path.dialogue:** Brief positive feedback (5-10 words)
- Examples: "Yes, that's two-thirds.", "Correct! You found fourths.", "Good work."

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
  "mastery_tier": "baseline",
  "variables_used": {"fractions": ["2/3"]}
}
```

**Output:**
```json
{
  "problem_id": 49,
  "difficulty": 2,
  "verb": "IDENTIFY",
  "template_id": "4008",
  "fractions": ["2/3"],
  "steps": [{
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
          {"id": "c", "text": "3/3"}
        ]
      }
    ],
    "correct_answer": {
      "value": "b",
      "context": "The point is at 2/3, the second tick mark"
    },
    "student_attempts": {
      "success_path": {
        "dialogue": "Yes, that's two-thirds."
      }
    }
  }]
}
```

## IMPORTANT NOTES

- Each problem instance creates ONE sequence with ONE step (unless template specifies multi-step)
- Keep dialogue conversational and supportive
- Parse workspace descriptions carefully to create accurate tangible structures
- Use description field in tangibles when workspace mentions specific characteristics
- Map mastery tiers consistently to difficulty levels
- Extract all fractions/denominators from variables_used into fractions array

Generate structured sequences NOW!
""",

    doc_refs=["visuals.md"],

    output_structure="""
{
  "sequences": [
    {
      "problem_id": 1,
      "difficulty": 2,
      "verb": "IDENTIFY",
      "template_id": "4001",
      "fractions": ["1/3"],
      "steps": [{
        "dialogue": "...",
        "prompt": "...",
        "interaction_tool": "place_point|drag_label|click_choice|select|multi_select",
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
        "correct_answer": {...},
        "student_attempts": {
          "success_path": {
            "dialogue": "..."
          }
        }
      }]
    }
  ]
}
""",

    prefill="""{"sequences":[{"problem_id":""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=False,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
