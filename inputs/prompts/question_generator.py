"""
Question Generator Prompt Configuration
Brainstorms diverse questions exploring different narratives, contexts, and cognitive demands
"""

QUESTION_GENERATOR_ROLE = """You are an expert educational content designer who takes the learning goals and their example questions from the module, then creates fresh narrative variations. Your role is to generate creative, engaging question variations that use the module's available visuals and vocabulary."""

QUESTION_GENERATOR_DOCS = [
    "difficulty_levels.md",
    "question_types.md",
]

QUESTION_GENERATOR_EXAMPLES = []

QUESTION_GENERATOR_MODULE_REF = ["variables", "available_visuals", "vocabulary"]

QUESTION_GENERATOR_PREFILL = '{"questions": ['

QUESTION_GENERATOR_EXPECTED_INPUT = {
    "id": 3,
    "text": "The student can shade one part to represent a unit fraction",
    "difficulty_level": "0-2",
    "example_questions": [
        "Shade a part of the bar to represent 1/2.",
        "Which bar correctly shows 1/3 shaded?",
        "Select a fraction that matches the shaded part of the bar."
    ]
}

QUESTION_GENERATOR_INSTRUCTIONS = """
## TASK

For each learning goal provided, generate diverse question variations using the input **example_questions as templates**.

**Your process:**
1. You receive a learning goal with their example_questions and difficulty_level range
2. For EACH value in example_questions you generate:
   - Pick a difficulty level within the goal's range (vary across 0-4 based on goal's difficulty_level)
   - Assign a question_type from the 5 cognitive actions (refer to question_types.md)
   - Create a unique narrative context that matches the visual shape from {available_visuals}
   - Pick different variable values from {variables} (e.g., halves vs thirds vs fourths)
   - Use vocabulary terms from {vocabulary} appropriately in your question text

**IMPORTANT:** 
- Generate multiple questions for the input goal
- VARY difficulty levels across the questions (use the full range from the goal's difficulty_level)
- VARY question types (don't repeat the same cognitive action)
- VARY variable values (use different denominators, different partition types, etc.)

## STEP 1: UNDERSTAND THE VISUAL

Check {available_visuals} to know what shape you're working with. This guides your narrative choice.

## STEP 2: CREATING NARRATIVE VARIATIONS

Take the example_question template and add a real-world context **that matches the visual_context**:

**Key principle:** The narrative shape should match the visual_context shape. Student should intuitively picture the context as the visual.

## STEP 3: VARY YOUR QUESTIONS

Generate diverse questions by systematically varying:

**1. Difficulty Levels:**
- Use the goal's difficulty_level range (e.g., "0-2" means generate questions at levels 0, 1, and 2)
- Distribute evenly: if generating 6 questions for a "0-2" goal, make 2 at level 0, 2 at level 1, 2 at level 2
- Refer to difficulty_levels.md for what each level means

**2. Question Types (Cognitive Actions):**
- Rotate through: CREATE → IDENTIFY → COMPARE → APPLY → CONNECT
- Each type tests different skills (procedural vs conceptual vs transfer)
- Refer to question_types.md for guidance on each type

**3. Variable Values:**
- Use different values from the module's variables for each question
- Example: If variables includes denominators [2, 3, 4, 6, 8], cycle through them
- Question 1: halves (denominator 2)
- Question 2: thirds (denominator 3)  
- Question 3: fourths (denominator 4)
- etc.

**4. Narrative Contexts:**
- Don't repeat the same context (e.g., don't use "chocolate bar" for every question)
- Mix food, objects, and spaces from the narrative ideas below

## STEP 4: NARRATIVE IDEAS BY SHAPE

**For rectangle_bar:**
- **Linear Food**: Candy bar, licorice, granola bar, chocolate bar, toast, sandwich, hotdog, baguette
- **Materials/Strips**: Ribbon, fabric strip, rope, paper strip, tape, beam
- **Spaces/Lanes**: Parking lanes, swimming lanes, rows in a garden bed, sections of fence
- **Groups in Lines**: People in a line, books on a shelf, seats in a row, plants in a row

**For circle:**
- **Circular Food**: Pizza, pie, cake, donut, tart, pancake
- **Circular Objects**: Wheel, clock, plate, coin, target
- **Circular Spaces**: Garden plot, pond, field, stage

**For other shapes:**
- Match the narrative to the visual (hexagon → honeycomb, diamond → tiles, triangle → roof sections, etc.)
"""

QUESTION_GENERATOR_STRUCTURE = """
{
  "questions": [
    {
      "question_id": 1,
      "goal_id": "From learning goals",
      "goal": "Learning goal text here",
      "question_prompt": "The example_question template from the module",
      "question_type": "CREATE|IDENTIFY|COMPARE|APPLY|CONNECT",
      "visual_context": "From module's available_visuals (e.g., 'rectangle_bar')",
      "question_text": "Your creative narrative variation matching the visual shape",
      "difficulty_level": 0-4,
    }
  ]
}
"""
