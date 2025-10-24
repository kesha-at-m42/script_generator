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

For each question, create a SEQUENCE (1-3 steps).

## HOW TO USE THE QUESTION DATA

Each question includes rich metadata. Use it to design the sequence:

**Design Process:**
1. **Generate dialogue first** using difficulty level, goal, question_text and guide_design.md (Kim's warm, encouraging voice)
2. **Design the interaction** (prompt, tool, workspace) using interaction_type and visual_context
3. **Validate**: Check that dialogue matches the visual workspace you created, and use vocabulary_reinforced terms naturally in dialogue

**Key fields:**
- **question_text**: The scenario/context - use for dialogue content
- **interaction_type**: Inspires the type of interaction/tool to use
- **visual_context**: Inspires the workspace setup
- **goal**: The learning objective - understand what concept the student is practicing
- **difficulty_level** (0-4): Consider for appropriate complexity in dialogue scaffolding and tone
- **cognitive_verb**: The thinking skill (identify, apply, compare, etc.)
- **correct_answer**: Use this to set the correct_answer.value field
- **explanation**: Background on what the question assesses
- **vocabulary_reinforced**: Key terms that might appear in dialogue

**Example mapping:**
```
Question data:
  "question_text": "A chocolate is cut into 8 equal pieces. Shade the bar to show what fraction one piece represents."
  "interaction_type": "Shade"
  "visual_context": "A horizontal rectangle bar divided into 8 equal parts, all unshaded, with a small chocolate icon above it"
  "correct_answer": "Shade one of the eight equal parts"

Becomes sequence:
  "dialogue": "A chocolate is cut into 8 equal pieces. Shade the bar to show what fraction one piece represents."
  "prompt": "Shade one-eighth"
  "interaction_tool": "shade"
  "workspace": [{"id": "bar_1", "type": "rectangle_bar", "sections": 8, "state": "divided", "shaded": []}]
  "correct_answer": {"value": "1/8", "context": "Shade 1 out of 8 sections to represent one piece"}
  "student_attempts": {"success_path": {"dialogue": "That's correct. You shaded one-eighth of the chocolate bar."}}
```

## SEQUENCE STRUCTURE

Generally, each sequence has 1 step. Each step can include the following fields:

**dialogue** (required)
- Use Kim's conversational voice from the guide design document
- Length: 10-30 words
- Clear, friendly practice instructions
- These are practice problems for concepts already taught - guide students through applying what they know

**prompt** (required)
- Clear mathematical action language focused on the concept
- Examples: "Shade three-fourths", "Partition the bar into halves", "Select bars with equal parts"

**interaction_tool** (required)
Choose from these options:
- `"shade"` - Student shades/colors sections of shapes
- `"cut"` - Student divides/partitions shapes into parts
- `"select"` - Student selects one shape from multiple options
- `"multi_select"` - Student selects multiple shapes
- `"place_tick"` - Student places marks on a number line
- `"click_choice"` - Student picks from multiple choice answers

**workspace** (required)
Array of tangible objects with these required fields:
- `id`: Unique identifier string
- `type`: Shape type (rectangle_bar, circle, grid, number_line, etc.)
- `sections`: Number of equal parts (1 = undivided/whole, 2+ = divided)
- `state`: Visual state - "undivided", "divided", or "divided_unequal"
- `shaded`: Array of integers for shaded section indices (empty array [] means none shaded)
- `position`: Location on screen (center, top, bottom, etc.)

**correct_answer** (required)
Object with two fields:
- `value`: The answer value (format depends on interaction_tool):
  - shade: Fraction string like "3/4"
  - cut: Fraction string like "1/4" 
  - select: Tangible ID string like "shape_b"
  - multi_select: Array of tangible IDs like ["shape_a", "shape_c"]
  - place_tick: Array of decimals like [0.5]
  - click_choice: Choice ID string like "c"
- `context`: Human-readable explanation of what the value means

**choices** (optional)
Only for click_choice interactions - array of choice objects with id and text fields

**student_attempts** (required)
Object with feedback for successful completion:
- `success_path`: Object containing dialogue
  - `dialogue`: Brief positive feedback (5-10 words, warm tone from guide_design.md)

**Example step:**
```json
{{
  "dialogue": "Here's a rectangle bar divided into 4 equal parts. Shade three of them.",
  "prompt": "Shade three-fourths",
  "interaction_tool": "shade",
  "workspace": [
    {{
      "id": "bar_1",
      "type": "rectangle_bar",
      "sections": 4,
      "state": "divided",
      "shaded": [],
      "position": "center"
    }}
  ],
  "correct_answer": {{
    "value": "3/4",
    "context": "Shade 3 out of 4 sections"
  }}
}}
```

**Example 1: Shading interaction**
   ```json
   {{
     "dialogue": "Here's a bar with 4 equal parts. Shade three of them to show three-fourths.",
     "prompt": "Shade three-fourths",
     "interaction_tool": "shade",
     "workspace": [
       {{
         "id": "bar_1",
         "type": "rectangle_bar",
         "sections": 4,
         "state": "divided",
         "shaded": []
       }}
     ],
     "correct_answer": {{
       "value": "3/4",
       "context": "The value 3/4 represents shading 3 out of 4 sections - the numerator is the number of sections to shade, denominator is total sections"
     }}
   }}
   ```
   
   **Example 1b: Dividing/partitioning interaction**
   ```json
   {{
     "dialogue": "Here's a whole bar. Divide it into 4 equal parts.",
     "prompt": "Partition the bar into fourths",
     "interaction_tool": "cut",
     "workspace": [
       {{
         "id": "bar_1",
         "type": "rectangle_bar",
         "sections": 1,
         "state": "undivided",
         "shaded": []
       }}
     ],
     "correct_answer": {{
       "value": "1/4",
       "context": "The value 1/4 represents the size of each part created - the denominator indicates how many equal parts to create the bar into"
     }}
   }}
   ```
   
   **Example 2: Multiple choice**
   ```json
   {{
     "dialogue": "Look at this rectangle. What fraction is shaded?",
     "prompt": "Select the correct fraction",
     "interaction_tool": "click_choice",
     "workspace": [
       {{
         "id": "bar_1",
         "type": "rectangle_bar",
         "sections": 4,
         "state": "divided",
         "shaded": [0, 1, 2]
       }}
     ],
     "choices": [
       {{"id": "a", "text": "1/4"}},
       {{"id": "b", "text": "2/4"}},
       {{"id": "c", "text": "3/4"}},
       {{"id": "d", "text": "4/4"}}
     ],
     "correct_answer": {{
       "value": "c"
     }}
   }}
   ```
   
   **Example 3: Number line interaction**
   ```json
   {{
     "dialogue": "Here's a number line from 0 to 1. Mark one-half on it.",
     "prompt": "Mark one-half on the number line",
     "interaction_tool": "place_tick",
     "workspace": [
       {{
         "id": "number_line_1",
         "type": "number_line",
         "start": 0,
         "end": 1,
         "marks": []
       }}
     ],
     "correct_answer": {{
       "value": [0.5],
       "context": "The value 0.5 is the decimal position on the number line representing one-half - array contains positions where ticks should be placed"
     }}
   }}
   ```
   
   **Example 4: Selection interaction**
   ```json
   {{
     "dialogue": "Look at these bars. Which one shows one-third shaded?",
     "prompt": "Select the bar showing one-third",
     "interaction_tool": "select",
     "workspace": [
       {{"id": "bar_top", "type": "rectangle_bar", "sections": 3, "state": "divided", "shaded": [0, 1]}},
       {{"id": "bar_bottom", "type": "rectangle_bar", "sections": 3, "state": "divided", "shaded": [0]}}
     ],
     "correct_answer": {{
       "value": "bar_bottom",
       "context": "The bottom bar has exactly 1 out of 3 parts shaded, representing one-third"
     }}
   }}
   ```

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
        // Every step has workspace, dialogue, prompt, interaction_tool, correct_answer, and student_attempts
        {{
          "dialogue": "Here's a rectangle divided into 4 equal parts. Shade three of them.",
          "prompt": "Shade three-fourths",
          "interaction_tool": "shade",
          "workspace": [
            {{
              "id": "bar_1",
              "type": "rectangle_bar",
              "sections": 4,
              "state": "divided",
              "shaded": []
            }}
          ],
          "correct_answer": {{
            "value": "3/4",
            "context": "Shade 3 out of 4 sections to show three-fourths"
          }},
          "student_attempts": {{
            "success_path": {{
              "dialogue": "Perfect! You shaded exactly three-fourths."
            }}
          }}
        }},
        
        // Multiple choice example
        {{
          "dialogue": "Take a look at this bar. Count the shaded parts and see what fraction they make.",
          "prompt": "Which fraction represents the shaded parts?",
          "interaction_tool": "click_choice",
          "workspace": [
            {{
              "id": "bar_1",
              "type": "rectangle_bar",
              "sections": 4,
              "state": "divided",
              "shaded": [0, 1, 2]
            }}
          ],
          "choices": [
            {{"id": "a", "text": "1/4"}},
            {{"id": "b", "text": "2/4"}},
            {{"id": "c", "text": "3/4"}},
            {{"id": "d", "text": "4/4"}}
          ],
          "correct_answer": {{
            "value": "c",
            "context": "The value 'c' is the choice id - it corresponds to 3/4, which represents 3 out of 4 sections shaded"
          }},
          "student_attempts": {{
            "success_path": {{
              "dialogue": "You counted the shaded parts and identified the fraction correctly."
            }}
          }}
        }}
    }}
  ]
}}

Key points:
- Every step requires: dialogue, prompt, interaction_tool, workspace, correct_answer, student_attempts
- workspace defines the tangibles for each step
- Add choices field for click_choice interactions
- student_attempts.success_path.dialogue provides feedback for successful completion of that step
- Omit optional fields that aren't needed (don't set to null)
- Each dialogue is 10-30 words
"""
