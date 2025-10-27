"""
Interaction Designer Prompt Configuration
Designs interactive visual sequences for educational questions

All visual types, states, and animations are in visual_guide.md
Kim's dialogue voice and style are in guide_design.md
"""

INTERACTION_DESIGNER_ROLE = """You are an expert in designing interactive educational experiences.

Your task: Create step-by-step MAIN INSTRUCTION FLOW sequences for math problems. Each sequence is an array of steps with:
- **dialogue**: What the guide (Kim) says
- **prompt**: A concise, task-focused instruction telling the student exactly what to do. 
- **workspace**: The interactive space where visuals appear and student interactions happen - defines what tangibles (shapes, buttons, objects) are present and their states

Use guide_design.md for Kim's voice and visual_guide.md for workspace elements."""

INTERACTION_DESIGNER_DOCS = [
    "guide_design.md",
    "visual_guide.md",
]

INTERACTION_DESIGNER_EXAMPLES = []

INTERACTION_DESIGNER_EXPECTED_INPUT="""
    {
      "goal_id": 6,
      "goal_text": "The student can understand that all parts must be equal for unit fractions",
      "question_id": 3,
      "question_prompt": "Select the bar that represents 1/6.",
      "question_type": "IDENTIFY",
      "difficulty_level": 2,
      "visual_context": "Three rectangle bars shown horizontally, each divided into 6 parts with one part shaded; only one bar has equal parts",
      "variables_used": {
        "total_parts": 6
      },
      "application_context": "Leo partitions a granola bar into 6 equal pieces."
    }
"""

INTERACTION_DESIGNER_PREFILL = """{
  "sequences": [
    {
"""

INTERACTION_DESIGNER_INSTRUCTIONS = """
## YOUR TASK

Design an interactive sequence for the given question idea:

<question>
{question_data}
</question>

Generally, each sequence has 1 step. Each step can include the following fields:

**Step 1: Write the prompt**
- Derive the `prompt` from `question_prompt`, and ensure it doesn't give away the answer.
- Clear mathematical action language focused on the concept in 5-15 words.
- Example: "Select the bar that represents 1/4" -> "Select the bar showing the correct fraction"

**Step 2: Map visual_context to workspace and choose interaction_tool**
- Read the `question_prompt`, `application_context` (if present) and `visual_context` to understand what should appear on screen
- Find matching tasks in visual_guide.md
- Select the appropriate interaction_tool based on the task requirements
  - `"shade"` - Student shades sections of shapes
  - `"cut"` - Student divides shapes into parts
  - `"select"` - Student selects one shape from multiple options
  - `"multi_select"` - Student selects multiple shapes
  - `"place_tick"` - Student places ticks on a number line
  - `"click_choice"` - Student picks from multiple choice answers
- Build workspace array with tangible objects:
  Array of tangible objects with these required fields:
  - `id`: Unique identifier string
  - `type`: Shape type (rectangle_bar, circle, grid, number_line, etc.)
  - `sections`: Number of parts, omit if not applicable
  - `state`: Visual state - "undivided", "divided_equal", or "divided_unequal"
There are two types of dialogue to write:

**3a. Main dialogue (setting up the question)**
- Use `question_prompt` and `application_context` (if available) as your narrative base.
- Refer to the "Problem Setup Dialogue" section in `guide_design.md` for Kim's conversational voice and tone.
- Keep the dialogue concise (10-30 words), clear, and supportive.
- Focus on guiding students to practice the `goal_text` without introducing new concepts.
- Adjust scaffolding and tone based on `difficulty_level` (0-4):
  - **Lower levels (0-1):** Provide more guidance.
  - **Higher levels (2-4):** Reduce scaffolding and encourage independent thinking.

**3b. Success dialogue (student_attempts.success_path.dialogue)**
- Provide brief, positive feedback when the student completes the task correctly.
- Refer to the "Success Dialogue" section in `guide_design.md` for Kim's conversational voice and tone.
- Keep the feedback concise (5-10 words).

**4. Map the fraction covered
- Use the `variables_used` field from question data to identify which fraction is being practiced in this question.
- For total_parts without numerators or fractions mentioned, 2-8 maps to "1/2" through "1/8" respectively.
- For fraction_names, "halves" maps to "1/2", "thirds" to "1/3", "fourths" to "1/4", "sixths" to "1/6", and "eighths" to "1/8".

**Example transformation:**
```
Input question data:
  "question_prompt": "Select the bar that represents 1/4.",
  "question_type": "IDENTIFY",
  "difficulty_level": 2,
  "application_context": "Maya is sharing a chocolate bar equally with 3 friends.",
  "visual_context": "Three rectangle bars shown horizontally, each divided into 4 parts with one part shaded; only one bar has equal parts",
  "variables_used": {"total_parts": 4}

Output sequence step:
  "prompt": "Select the bar showing the correct fraction.",
  "dialogue": "Maya wants to share a chocolate bar with three friends. Everyone will receive one part. How should she divide the bar so that everyone receives an equal part?" (based on guide_design.md),
  "interaction_tool": "select",
  "workspace": [
    {"id": "bar_top", "type": "rectangle_bar", "sections": 4, "state": "divided_unequal", "shaded": [0]},
    {"id": "bar_middle", "type": "rectangle_bar", "sections": 4, "state": "divided_unequal", "shaded": [0]},
    {"id": "bar_bottom", "type": "rectangle_bar", "sections": 4, "state": "divided_equal", "shaded": [0]}
  ],
  "correct_answer": {"value": "bar_bottom", "context": "It's the bar with equal parts."},
  "student_attempts": {"success_path": {"dialogue": "You selected the bar divided in fourths."}}}
```

**Example: Shading interaction:**
```json
{{
  "prompt": "Shade parts to show the correct fraction",
  "interaction_tool": "shade",
  "workspace": [
    {{
      "id": "bar_1",
      "type": "rectangle_bar",
      "sections": 4,
      "state": "divided_equal",
      "shaded": [],
      "position": "center"
    }}
  ],
  "correct_answer": {{
    "value": "3/4",
    "context": "3/4 parts should be shaded"
  }}
}}
```
   
**Example: Dividing/partitioning interaction**
   ```json
   {{
     "prompt": "Divide the bar into required parts",
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
       "context": "The value 1/4 represents the size of each part created"
     }}
   }}
   ```
   
   **Example: Multiple choice**
   {{
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
   
     
   **Example: Selection interaction**
   ```json
   {{
     "prompt": "Select the bar showing the correct fraction",
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
      "verb": "CREATE|IDENTIFY|COMPARE|APPLY|CONNECT",
      "goal": "learning goal text",
      "fractions_covered":[],
      "steps": [
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

"""
