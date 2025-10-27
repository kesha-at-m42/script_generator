"""
Question Generator Prompt Configuration
Brainstorms diverse questions exploring different narratives, contexts, and cognitive demands
"""

QUESTION_GENERATOR_ROLE = """
You are an expert educational content designer creating practice questions for grade 3 students.
Generate diverse, clear question variations using the module's available visuals and vocabulary, with age-appropriate language and relatable contexts.
"""

QUESTION_GENERATOR_DOCS = [
    "difficulty_levels.md",
    "question_types.md"
]

QUESTION_GENERATOR_INPUTS = ["goal", "goal_id", "difficulty_level", "example_questions", "variables"]

QUESTION_GENERATOR_EXAMPLES = []

QUESTION_GENERATOR_MODULE_REF = ["available_visuals", "vocabulary"]

QUESTION_GENERATOR_PREFILL = """{{
  "questions": [
    {{
      "goal_id": {goal_id},
      "goal_text": "{goal}","""

QUESTION_GENERATOR_INSTRUCTIONS = """
## TASK

Generate meaningfully different question variations for independent practice of the learning goal:
- ID: {goal_id}
- Text: {goal}
- Difficulty Range: {difficulty_level}
- Example Questions: {example_questions}
- Variables to Swap: {variables}

**IMPORTANT:** Each example question represents a DIFFERENT question structure or approach. For EACH example template, create variations by swapping variable values systematically.

**HANDLING INTERCHANGEABLE VARIABLES:**
When multiple variables represent the same concept (e.g., "2" and "halves", "3" and "thirds"):
- These are EQUIVALENT - they represent the same value with different vocabulary
- Generate ONE question per unique value, choosing either numeric or name form
- Example: "Divide into 2 equal parts" and "Divide into halves" = SAME question, generate only once
- Coverage goal: Each unique value (2/halves, 3/thirds, 4/fourths, 6/sixths, 8/eighths) appears once per template

**GENERATION STRATEGY:**
- If 4 example templates * 5 unique values = aim for ~20 questions total
- Each template should appear with each unique value once
- Focus on structural variety (different templates), not vocabulary swaps of the same structure

## LESSON COVERAGE CONSTRAINTS

Ensure comprehensive coverage across the full lesson scope:
- **All unique variable values must be covered within a goal**: Every distinct value listed in {variables} (treating "2" = "halves" as one if both are listed) appears at least once
- **Balance across difficulty levels**: Spread questions across the full difficulty range {difficulty_level}
- **Appropriate question types**: Use CREATE, IDENTIFY, COMPARE, APPLY, CONNECT based on each template's structure
- Track coverage in variables_used field

## CREATING VARIATIONS

For each question variation, fill these fields:

1. **goal_id**: Will be prefilled for the first question, copy for all subsequent questions

2. **goal_text**: Will be prefilled for the first question, copy for all subsequent questions

3. **question_id**: Sequential number (1, 2, 3, ...)

4. **question_prompt**: 
  - A concise, task-focused instruction telling the student exactly what to do. 
  - Stay very close to the example questions - keep almost everything the same. 
  - Only make minimal variations like swapping specific numbers/fractions from {variables} (e.g., "1/2" → "1/3", "thirds" → "fourths", "2" → "4"). 


5. **question_type**: Assign an appropriate cognitive question type - see question_types.md

6. **difficulty_level**: Choose 0-4 based on cognitive complexity, variable used, context familiarity, and steps required - see difficulty_levels.md

8. **variables_used**: Track only the exact variable value that appears in the question_prompt:
   - If the prompt uses "halves", record "fraction_names": "halves"
   - If the prompt uses "2", record "total_parts": 2
   - Only include the variable field that was actually used in this variation
   - This allows systematic tracking of coverage

9. **application_context** (ONLY for APPLY/CONNECT question types):
   - Provide a brief real-world scenario or context that frames the problem, 10-20 words
   - Use {available_visuals} for inspiration on situations
   - Incorporate vocabulary from {vocabulary}
   - Create fun, relatable and age-appropriate scenarios
   - This field should be omitted for CREATE, IDENTIFY, and COMPARE question types

10. **visual_context**: 
  - Describe what appears on screen to support the question. 
  - Specify the visual shape/format (from {available_visuals}) and any additional layout details needed.
"""

QUESTION_GENERATOR_STRUCTURE = """
{
  "questions": [
    {
      "goal_id": <from prefill>,
      "goal_text": <from prefill>,
      "question_id": 1,
      "question_prompt": "Variation of example 1 with variable swapped",
      "visual_context": "Description of what appears on screen",
      "question_type": "CREATE|IDENTIFY|COMPARE|APPLY|CONNECT",
      "difficulty_level": 0-4,
      "variables_used": {
        "total_parts": 2
      },
      "application_context": "Only include for APPLY/CONNECT types"
    }
  ]
}
"""
