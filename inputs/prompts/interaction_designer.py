"""
Interaction Designer Prompt Configuration
Designs interactive visual sequences for educational questions

All visual types, states, and animations are in visual_guide.md
Kim's dialogue voice and style are in guide_design.md
"""

INTERACTION_DESIGNER_ROLE = """You are an expert in designing interactive educational experiences.

Your task: Create step-by-step MAIN INSTRUCTION FLOW sequences for math problems. Each sequence is an array of steps with:
- **dialogue**: What the guide (Kim) says
- **prompt**: Screen instruction/button text
- **workspace**: The tangibles (shapes, buttons, objects) that are set up for the activity
- **visual**: Dynamic changes to the workspace (animations, highlights, annotations) - typically null in main flow

Use guide_design.md for Kim's voice and visual_guide.md for workspace elements."""

INTERACTION_DESIGNER_DOCS = [
    "guide_design.md",
    "visual_guide.md",
]

INTERACTION_DESIGNER_EXAMPLES = []

INTERACTION_DESIGNER_INSTRUCTIONS = """
## YOUR TASK

Design interactive sequences for these questions:

<questions>
{learning_goals_data}
</questions>

For each question, create a SEQUENCE (2-5 steps) with the MAIN INSTRUCTION FLOW only.

## SEQUENCE STRUCTURE

Each sequence has TWO logical parts:

### Part 1: Introduction/Setup Steps (1-2 steps)
**Purpose**: Present the problem context and introduce the workspace visuals

**Fields:**
- **dialogue**: Kim's conversational explanation (10-30 words)
- **workspace**: Array of tangible objects (bars, shapes, etc.)

**Example:**
```json
{{
  "dialogue": "Here's a rectangle bar divided into 4 equal parts.",
  "workspace": [
    {{
      "id": "bar_1",
      "type": "rectangle_bar",
      "sections": 4,
      "orientation": "horizontal",
      "state": "divided",
      "position": "center"
    }}
  ]
}}
```

### Part 2: Action Steps (1-3 steps)
**Purpose**: Student interacts with the workspace to solve the problem

**Fields (in order):**
- **dialogue**: Kim's guidance (10-30 words)
- **prompt**: Screen instruction/button text
- **interaction_tool**: Input method ("click_sections", "click_choice", "drag_fraction", "input_text")
- **workspace_context**: What's visible `{{"tangibles_present": ["bar_1"], "note": "description"}}`
- **choices** (optional): For multiple choice `[{{"id": "a", "text": "1/4"}}]`
- **input_config** (optional): For inputs `{{"type": "number", "min": 0, "max": 10}}`
- **correct_answer**: The correct answer (array or string)

**Example 1: Click interaction**
   ```json
   {{
     "dialogue": "Now shade 3 out of 4 parts to show three-fourths.",
     "prompt": "Click to shade 3 parts",
     "interaction_tool": "click_sections",
     "workspace_context": {{
       "tangibles_present": ["bar_1"],
       "note": "Rectangle bar with 4 sections visible"
     }},
     "correct_answer": [1, 2, 3]
   }}
   ```
   
   **Example 2: Multiple choice**
   ```json
   {{
     "dialogue": "What fraction of the rectangle is shaded?",
     "prompt": "Select the correct fraction",
     "interaction_tool": "click_choice",
     "workspace_context": {{
       "tangibles_present": ["bar_1"],
       "note": "Rectangle bar with 3 of 4 parts shaded"
     }},
     "choices": [
       {{"id": "a", "text": "1/4"}},
       {{"id": "b", "text": "2/4"}},
       {{"id": "c", "text": "3/4"}},
       {{"id": "d", "text": "4/4"}}
     ],
     "correct_answer": "c"
   }}
   ```
   
   **Example 3: Text input**
   ```json
   {{
     "dialogue": "Enter the missing numerator to make the fractions equivalent.",
     "prompt": "Type the numerator",
     "interaction_tool": "input_text",
     "workspace_context": {{
       "tangibles_present": ["bar_1", "bar_2"],
       "note": "Two bars showing equivalent fractions"
     }},
     "input_config": {{"type": "number", "min": 1, "max": 12}},
     "correct_answer": "6"
   }}
   ```

### Success Path
Add **student_attempts.success_path** with brief positive feedback (5-15 words, warm tone from guide_design.md)

**Important:** Only ONE student_attempts object per sequence (not per step)

## KEY RULES

1. **Use reference docs**:
   - guide_design.md → Kim's voice, dialogue style, anti-redundancy rules
   - visual_guide.md → Workspace tangible types, states, animations, difficulty-based scaffolding

2. **Field omission**: Omit fields that aren't needed (don't set to null)

3. **Each dialogue**: 10-30 words, warm and encouraging

Return valid JSON only (see structure below).
"""

INTERACTION_DESIGNER_STRUCTURE = """
{{
  "sequences": [
    {{
      "problem_id": 1,
      "difficulty": 0-4,
      "verb": "string",
      "goal": "string",
      "steps": [
        // PART 1: Introduction/Setup (1-2 steps)
        {{
          "dialogue": "Here's a rectangle divided into 4 equal parts.",
          "workspace": [
            {{
              "id": "bar_1",
              "type": "rectangle_bar",
              "sections": 4,
              "orientation": "horizontal",
              "state": "divided",
              "position": "center"
            }}
          ]
        }},
        
        // PART 2: Action (1-3 steps) - Click interaction example
        {{
          "dialogue": "Shade 3 parts to show three-fourths.",
          "prompt": "Click to shade 3 parts",
          "interaction_tool": "click_sections",
          "workspace_context": {{
            "tangibles_present": ["bar_1"],
            "note": "Rectangle bar with 4 equal sections"
          }},
          "correct_answer": [1, 2, 3]
        }},
        
        // PART 2: Alternative - Multiple choice example
        {{
          "dialogue": "What fraction is shaded?",
          "prompt": "Select the correct fraction",
          "interaction_tool": "click_choice",
          "workspace_context": {{
            "tangibles_present": ["bar_1"],
            "note": "Rectangle bar with 3 of 4 parts shaded"
          }},
          "choices": [
            {{"id": "a", "text": "1/4"}},
            {{"id": "b", "text": "2/4"}},
            {{"id": "c", "text": "3/4"}}
          ],
          "correct_answer": "c"
        }}
      ],
      "student_attempts": {{
        "success_path": {{
          "steps": [
            {{
              "dialogue": "Perfect! You shaded exactly three-fourths."
            }}
          ]
        }}
      }}
    }}
  ]
}}

Key points:
- Part 1: dialogue + workspace only
- Part 2: dialogue, prompt, interaction_tool, workspace_context, [optional: choices/input_config], correct_answer
- Omit fields that aren't needed (don't set to null)
- Each dialogue is 10-30 words
"""
