"""
Question Generator Prompt Configuration
Generates diverse, engaging questions with maximum structured creativity while ensuring systematic variable coverage
"""

QUESTION_GENERATOR_ROLE = """
You are an expert educational content designer creating practice questions for grade 3 students.
Generate diverse, clear question variations using the module's available visuals and vocabulary, with age-appropriate contexts within the constraints of one question per variable.
"""

QUESTION_GENERATOR_DOCS = [
    "difficulty_levels.md",
    "cognitive_types.md",
    "visuals.md",
]

QUESTION_GENERATOR_INPUTS = ["goal", "goal_id", "difficulty_level", "example_questions", "variables_used", "cognitive_type"]

QUESTION_GENERATOR_TEMPLATE_REF = ["visual_context"]

QUESTION_GENERATOR_EXAMPLES = []

QUESTION_GENERATOR_MODULE_REF = ["vocabulary"]

QUESTION_GENERATOR_PREFILL = """{{
  "questions": [
    {{
      "goal_id": {goal_id},
      "goal": "{goal}","""

QUESTION_GENERATOR_INSTRUCTIONS = """
## TASK

Generate diverse, engaging questions for independent practice of the learning goal:
- **Goal ID:** {goal_id}
- **Goal Text:** {goal}
- **Difficulty Range:** {difficulty_level}
- **Variables to Cover:** {variables}
- **Example Questions:** {example_questions}
- **Question Type:** {cognitive_type}

## GENERATION STRATEGY

**Core Rule: One Question Per Variable Per Goal**
- For each unique value in {variables}, create exactly ONE question. In general, each goal will have 4-8 questions.
- Only use variable values explicitly listed in {variables} - do not add new values
- Meaningfully different questions - different cognitive_type, visual context, or variable.
- If meaningful differentiation is not possible for a particular variable combination, skip that combination rather than force repetition
- Maximize variation across multiple dimensions to ensure questions feel distinct, not template-based

- For each unique variable value in {variables} for the goal, create only ONE question.
- For example, if the variable is "fractions" with values [1/2, 1/3, 1/6], generate one question using 1/2, another using 1/3, and another using 1/6. Don't make 1/5 if not listed. Only use listed variable values.
- If a meaningfully different question cannot be created for an example_question, difficulty_level and variable set, it is okay to skip that variable at that level.
- A meaningfully different question is one that differs significantly in visual context, cognitive demand, or variable used.
Since you'll create one question per variable value, differentiate questions through:

## CREATIVITY DIMENSIONS TO VARY

### 1. Visual Dimension
- Rotate through available visual types from <visuals> and adhere to {visual_context} requirements.
- Mix visual states: blank shapes, partially shaded, fully labeled, partially labelled, comparison sets
- Alternate between single shapes and multi-shape comparisons
- Use number lines with different tick configurations when applicable

### 2. Cognitive Dimension
- Distribute across difficulty levels {difficulty_level} (see difficulty_levels.md)
- Vary cognitive types within the constraints of example questions and available {cognitive_type} (see <cognitive_types>)
- Include age-appropriate real-world contexts when using APPLY/CONNECT


## CREATING EACH QUESTION

For each question variation, construct these fields thoughtfully:

**1. goal_id & goal:** Copy from prefill (will auto-populate)

**2. question_id:** Sequential number (1, 2, 3, ...)

**3. question_prompt:** The student-facing question text
   - **CRITICAL:** Stick to the task structure from {example_questions} - don't invent new tasks or actions
   - Create variations by swapping variable values while keeping the task/action the same
   - Word variations (synonyms, word order) must be inspired ONLY from {example_questions}
   - If examples say "Shade", use "Shade" - don't introduce "Color" or "Fill" unless they appear in examples
   - If examples say "Click", use "Click" - don't introduce "Select" or "Tap" unless they appear in examples
   - Age-appropriate vocabulary from {vocabulary}
   - Examples of correct variation:
     * Example: "Partition the bar into halves" → Variations: "Partition the bar into thirds", "Partition the bar into fourths"
     * Example: "Click on the circle showing 1/2" → Variations: "Click on the circle showing 1/3", "Click on the bar showing 1/4"

**4. visual_context:** Detailed description of what appears on screen
   - Only use visuals defined in <visuals> and adhere to {visual_context} requirements.
   - Vary the visual based on variables used (different shapes, states, configurations)
   - Be creative with which visual you choose and how you configure it
   - Use the variable values to determine visual parameters (number of parts, shading, etc.)
   - Format: "{shape_type} ({state}, {parts} equal/unequal parts, {shading})" or follow <visuals> spec
   - **For comparison sets:** Ensure each shape in the set is DIFFERENT - no two visuals should have the same configuration
      - 1 circle, 1 number line, 1 bar, each divided into 3 equal parts (different shapes)
      - 2 bars (1 has 4 equal parts, 1 has 6 unequal parts) (different configurations)
      - 2 circles (1 has 2 equal parts with 1 part shaded, 1 has 2 equal parts with no parts shaded) (different configurations)
   - Examples within constraints:
     * "horizontal_bar (blank, 4 equal parts)"
     * "circle (1 of 3 equal sectors shaded)"
     * "comparison_set: 3 circles (first has 2 equal parts, second has 3 equal parts, third has 4 equal parts)"
     * "number_line (0 to 1, with tick marks at 0, 1/4, 1/2, 3/4, 1)"

**Variable Placement Strategy - Be Creative:**

   **Pattern A - Variables in question_prompt (Creation/Action tasks):**
   - question_prompt: "Partition into halves" or "Shade 3 parts" (variable specifies the action)
   - visual_context: "horizontal_bar (blank)" (generic visual)
   
   **Pattern B - Variables in visual_context (Identification/Selection tasks):**
   - question_prompt: "Click the shape with equal parts" (generic question)
   - visual_context: "comparison_set: 3 bars (first has 2 equal parts, second has 3 unequal parts, third has 4 equal parts)" (variables define options)
   
   **Pattern C - Variables in both (Comparison tasks):**
   - question_prompt: "Which shows thirds?" (variable in question)
   - visual_context: "2 circles and 1 horizontal_bar, each divided into 3 equal parts" (variable in visual)

**5. cognitive_type:** Choose based on cognitive demand (see <cognitive_types>)

**6. difficulty_level:** Assign 0-4 based on (see difficulty_levels.md):

**7. variables_used:** Track ONLY the variable listed in the {variables} input that determines the mathematical content
   - Record the value from question_prompt OR visual_context (whatever defines the math, and record the answerable value in case of multiple variables)
   - Should be a single key-value pair, e.g., {"fractions": "1/2"} or {"parts": "4"}

**8. application_context:** (ONLY for APPLY/CONNECT cognitive types)
   - Brief real-world scenario or context, 10-20 words
   - Draw from contexts in {variables} when available
   - Age-appropriate, relatable, and fun

## QUALITY CHECKLIST

Before submitting, verify maximum creativity:

**Coverage Requirements:**
- Every value in {variables} appears at least once
- The same visual context is never repeated for the same variable value
- Difficulty spread across full range {difficulty_level}, never forced
- Cognitive types balanced appropriately

**Quality Requirements:**
- All questions aligned to goal: {goal}
- Age-appropriate language from {vocabulary}
- Clear, actionable instructions
- Precise visual descriptions

Generate questions NOW with maximum structured creativity!
"""

QUESTION_GENERATOR_STRUCTURE = """
{
  "questions": [
    {
      "goal_id": <from prefill>,
      "goal": <from prefill>,
      "question_id": 1,
      "question_prompt": "Variation of example 1 with variable swapped",
      "visual_context": "Description of what appears on screen",
      "cognitive_type": "CREATE|IDENTIFY|COMPARE|APPLY|CONNECT",
      "difficulty_level": 0-4,
      "variables_used": {
        "fractions": "1/2"
      },
      "application_context": "Only include for APPLY/CONNECT types"
    }
  ]
}
"""
