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
      "state": "divided",
      "shaded": [],
      "position": "center"
    }}
  ]
}}
```

**Required tangible fields:**
- `type`: String - Shape type (rectangle_bar, circle, grid, number_line, etc.)
- `sections`: Integer - Number of equal parts (1 = undivided/whole, 2+ = divided)
- `state`: String - Visual state of the tangible:
  * `"undivided"` - Whole shape, no divisions (sections = 1)
  * `"divided"` - Shape divided into equal parts (sections = 2+)
  * `"divided_unequal"` - Shape divided into unequal parts (for distractor/incorrect examples)
- `shaded`: Array of integers - Indices of shaded sections (e.g., `[0, 2]` means first and third sections are shaded, `[]` means none shaded)
- `position`: String - Location on screen (center, top, bottom, etc.)

**Fields to omit:**
- ~~`orientation`~~ - Not needed, inferred from shape type
- ~~`section_widths`~~ - Not needed, use `state: "divided_unequal"` for unequal divisions
- ~~`shaded_sections`~~ - Use `shaded` array instead
- ~~`filled_sections`~~ - Use `shaded` array instead
- ~~`shading_colors`~~ - Not needed for basic interactions

### Part 2: Action Steps (1-3 steps)
**Purpose**: Student interacts with the workspace to solve the problem

**Fields (in order):**
- **dialogue**: Kim's guidance (10-30 words)
- **prompt**: Screen instruction/button text
- **interaction_tool**: Choose based on the interaction type:
  - `"shade"` - Student shades/colors sections of shapes
  - `"cut"` - Student divides/partitions shapes into parts
  - `"select"` - Student selects one shape from multiple options
  - `"multi_select"` - Student selects multiple shapes
  - `"place_tick"` - Student places marks on a number line
  - `"click_choice"` - Student picks from multiple choice answers
- **workspace_context**: What's visible `{{"tangibles_present": ["bar_1"], "note": "description"}}`
- **choices** (optional): For multiple choice `[{{"id": "a", "text": "1/4"}}]`
- **correct_answer**: Object with two fields:
  - **value**: The answer value (format depends on interaction_tool):
    - `shade`: Fraction string like `"3/4"` (shade 3 out of 4 parts)
    - `cut`: Fraction string like `"1/4"` (divide into 4 equal parts)
    - `select`: Tangible ID string like `"shape_b"`
    - `multi_select`: Array of tangible IDs like `["shape_a", "shape_c"]`
    - `place_tick`: Array of decimals like `[0.5]` or `[0.25, 0.75]`
    - `click_choice`: Choice ID string like `"c"`
  - **context**: Human-readable explanation of what the value means (e.g., "Shade 3 out of 4 parts to represent three-fourths" or "Place tick at 0.5 which represents one-half")

**Example 1: Shading interaction**
   ```json
   {{
     "dialogue": "Now shade 3 out of 4 parts to show three-fourths.",
     "prompt": "Click to shade 3 parts",
     "interaction_tool": "shade",
     "workspace_context": {{
       "tangibles_present": ["bar_1"],
       "note": "Rectangle bar with 4 sections visible"
     }},
     "correct_answer": {{
       "value": "3/4",
       "context": "Shade 3 out of 4 sections to represent three-fourths of the bar"
     }}
   }}
   ```
   
   **Example 1b: Dividing/partitioning interaction**
   ```json
   {{
     "dialogue": "Click to divide this bar into 4 equal parts.",
     "prompt": "Click 3 times to make 4 parts",
     "interaction_tool": "cut",
     "workspace_context": {{
       "tangibles_present": ["bar_1"],
       "note": "Undivided rectangle bar"
     }},
     "correct_answer": {{
       "value": "1/4",
       "context": "Divide the bar into fourths (4 equal parts), requiring 3 cuts"
     }}
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
     "correct_answer": {{
       "value": "c",
       "context": "Choice 'c' (3/4) correctly identifies that 3 out of 4 parts are shaded"
     }}
   }}
   ```
   
   **Example 3: Number line interaction**
   ```json
   {{
     "dialogue": "Place a tick mark at one-half on the number line.",
     "prompt": "Click to place the tick mark",
     "interaction_tool": "place_tick",
     "workspace_context": {{
       "tangibles_present": ["number_line_1"],
       "note": "Number line from 0 to 1"
     }},
     "correct_answer": {{
       "value": [0.5],
       "context": "Position 0.5 represents the halfway point between 0 and 1, which is one-half"
     }}
   }}
   ```
   
   **Example 4: Selection interaction**
   ```json
   {{
     "dialogue": "Which shape shows one-third shaded?",
     "prompt": "Click the shape that shows 1/3",
     "interaction_tool": "select",
     "workspace_context": {{
       "tangibles_present": ["shape_a", "shape_b", "shape_c"],
       "note": "Three shapes with different shaded amounts"
     }},
     "correct_answer": {{
       "value": "shape_b",
       "context": "shape_b has exactly 1 out of 3 parts shaded, representing one-third"
     }}
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
              "state": "divided",
              "shaded": []
            }}
          ]
        }},
        
        // PART 2: Action (1-3 steps) - Shading interaction example
        {{
          "dialogue": "Shade 3 parts to show three-fourths.",
          "prompt": "Click to shade 3 parts",
          "interaction_tool": "paint",
          "workspace_context": {{
            "tangibles_present": ["bar_1"],
            "note": "Rectangle bar with 4 equal sections"
          }},
          "correct_answer": {{
            "value": "3/4",
            "context": "Shade 3 out of 4 sections to show three-fourths"
          }}
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
          "correct_answer": {{
            "value": "c",
            "context": "Choice 'c' represents three-fourths, matching the shaded amount"
          }}
        }}
            "context": "Choice 'c' represents three-fourths, matching the shaded amount"
          }}
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
