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
    "question_types.md",
]

QUESTION_GENERATOR_INPUTS = ["goal", "goal_id", "difficulty_level", "example_questions"]

QUESTION_GENERATOR_EXAMPLES = []

QUESTION_GENERATOR_MODULE_REF = ["variables", "available_visuals", "vocabulary"]

QUESTION_GENERATOR_PREFILL = """{{
  "questions": [
    {{
      "goal_id": {goal_id},
      "goal_text": "{goal}","""

QUESTION_GENERATOR_INSTRUCTIONS = """
## TASK

Generate diverse question variations for independent practice of the learning goal:
- ID: {goal_id}
- Text: {goal}
- Difficulty Range: {difficulty_level}
- Example Questions: {example_questions}

Create a pool of varied questions to support repeated application and consolidation of the concept. For EACH example question, create MULTIPLE variations exploring natural combinations of difficulty levels, question types, variables, and narrative contexts. Focus on meaningful variation that allows independent application across different scenarios.

## CREATING VARIATIONS

For each question variation, fill these 8 fields:

1. **goal_id**: Will be prefilled for the first question, copy for all subsequent questions

2. **goal_text**: Will be prefilled for the first question, copy for all subsequent questions

3. **question_id**: Sequential number (1, 2, 3, ...)

4. **question_prompt**: 
A concise, task-focused instruction telling the student exactly what to do. 
Stay very close to the example questions - keep almost everything the same. 
Only make minimal variations like swapping specific numbers/fractions from {variables} (e.g., "1/2" → "1/3", "thirds" → "fourths", "2" → "4"). 
The core action and phrasing should remain nearly identical to the examples.

5. **question_type**: Assign an appropriate cognitive question type - see question_types.md

6. **difficulty_level**: Choose 0-4 based on cognitive complexity, context familiarity, and steps required - see difficulty_levels.md

7. **question_text**: Design the main question narrative for independent practice, 15-30 words:
   - Uses question_prompt as the instructional template
   - Use question_type and difficulty_level to guide complexity and the design
   - Uses {available_visuals} for inspiration on shapes and contexts
   - Incorporates vocabulary from {vocabulary}
   - Creates fun, relatable and age-appropriate scenarios that allow concept application

8. **visual_context**: 
Describe what appears on screen to support the question. 
Based on the question_text you wrote, specify the visual shape/format (from {available_visuals}) and any additional layout details needed. 

"""

QUESTION_GENERATOR_STRUCTURE = """
{
  "questions": [
    {
      "goal_id": <from prefill>,
      "goal_text": <from prefill>,
      "question_id": 1,
      "question_prompt": "Template-based variation of example",
      "question_type": "CREATE|IDENTIFY|COMPARE|APPLY|CONNECT",
      "difficulty_level": 0-4,
      "question_text": "Creative narrative variation",
      "visual_context": "rectangle bar|circle|etc"
    }
  ]
}
"""
