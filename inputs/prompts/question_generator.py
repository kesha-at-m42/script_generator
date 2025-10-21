"""
Question Generator Prompt Configuration
"""

QUESTION_GENERATOR_ROLE = """You are an expert educational content designer specializing in elementary mathematics. You create questions that are developmentally appropriate, clear, and aligned with learning objectives."""

QUESTION_GENERATOR_DOCS = [
    "difficulty_levels.md",
    "question_types.md",
]

QUESTION_GENERATOR_EXAMPLES = [
    {
        "description": "Sample questions for Goal: Students can partition shapes into equal parts (showing good variety)",
        "output": """{
  "questions": [
    {
      "id": 1,
      "question_text": "Click once in the middle to divide the bar into 2 equal parts.",
      "interaction_type": "Click",
      "difficulty_level": 0,
      "question_type": "procedural",
      "cognitive_verb": "divide",
      "visual_context": "A horizontal rectangular bar, unpartitioned, solid color",
      "correct_answer": "Click once in the center to create 2 equal sections",
      "explanation": "This question teaches the most basic partitioning skill - creating two equal parts by finding the midpoint. It's procedural and concrete, requiring only one action to successfully partition a whole into halves.",
      "vocabulary_reinforced": ["partition", "equal parts"]
    },
    {
      "id": 2,
      "question_text": "Which circle shows 4 equal parts?",
      "interaction_type": "Multiple Choice",
      "difficulty_level": 2,
      "question_type": "conceptual",
      "cognitive_verb": "identify",
      "visual_context": "Three circles displayed: Circle A divided into 4 equal wedges, Circle B divided into 4 unequal wedges, Circle C divided into 3 equal parts",
      "correct_answer": "Circle A (the one with 4 equal wedges)",
      "explanation": "This question builds conceptual understanding by requiring students to distinguish between equal and unequal partitioning while also verifying the correct count. The circle shape adds complexity compared to rectangles, and the multiple distractors require careful visual discrimination.",
      "vocabulary_reinforced": ["equal parts"],
      "answer_choices": ["Circle A", "Circle B", "Circle C"]
    },
    {
      "id": 3,
      "question_text": "A rectangular garden needs to be divided into 6 equal sections for planting different vegetables. Show how you would divide it.",
      "interaction_type": "Drag and Drop",
      "difficulty_level": 4,
      "question_type": "transfer",
      "cognitive_verb": "apply",
      "visual_context": "A large rectangle representing a garden, with draggable dividing lines (5 lines available) that can be positioned horizontally or vertically",
      "correct_answer": "Position 5 lines to create 6 equal sections (e.g., 2 rows × 3 columns or 3 rows × 2 columns)",
      "explanation": "This transfer question applies partitioning to a real-world scenario requiring spatial reasoning and strategic planning. Students must determine that creating 6 equal parts requires 5 dividing lines and discover that multiple valid arrangements exist (2×3 or 3×2 or 6×1), promoting flexible thinking about equal partitioning in context.",
      "vocabulary_reinforced": ["equal parts", "partition", "whole"]
    }
  ]
}"""
    }
]

QUESTION_GENERATOR_INSTRUCTIONS = """
## TASK

Generate {num_questions} questions **PER LEARNING GOAL** for the following:

{learning_goals}

**IMPORTANT:** If multiple learning goals are provided, generate {num_questions} questions for EACH goal (not {num_questions} total).

## REQUIREMENTS

### DIFFICULTY DISTRIBUTION

Generate questions across difficulty levels (see difficulty_levels.md for details):
- 1-2 questions at Level 0-1 (support/confidence building)
- 2-3 questions at Level 2 (baseline mastery) ← FOCUS HERE
- 2-3 questions at Level 3 (stretch/deeper) ← FOCUS HERE  
- 1-2 questions at Level 4 (challenge/enrichment)

Target distribution: Level 0-1 (25%), Level 2 (30%), Level 3 (25%), Level 4 (20%)

### QUESTION TYPE DISTRIBUTION

See question_types.md for definitions. Target:
- ~25% Procedural (create, construct, partition, divide)
- ~45% Conceptual (identify, compare, explain, recognize)
- ~30% Transfer (apply, connect, predict, extend)

### INTERACTION VARIETY

Vary interaction types as much as possible. Available types:
- Click
- Multiple Choice
- Multiple Select
- Shade
- True/False

**IMPORTANT:** For Multiple Choice and Multiple Select questions, include the `answer_choices` field with an array of all options.

### VISUAL CONSTRAINTS

Use ONLY rectangle bars:
- 2-8 parts
- Equal or unequal divisions

Example visual descriptions:
- "Rectangle bar divided into 4 equal parts, 1 shaded"
- "Rectangle bar with 6 equal sections, 3 shaded"
- "Two rectangle bars: one divided into halves, one into fourths"

For Multiple Choice questions with visual answer options, describe all options in visual_context.

### ENSURE VARIETY

- Use different interaction types where possible
- Vary visual contexts (different partition counts, orientations)
- Different cognitive verbs from the learning goal
- Progress from simpler to more complex scenarios

### VOCABULARY

Reinforce vocabulary from the learning goal. Use terms like:
- partition, equal parts, whole
- halves, thirds, fourths, etc.
- numerator, denominator
- unit fraction

## OUTPUT STRUCTURE

Return valid JSON with this structure:

{{
  "questions": [
    {{
      "id": 1,
      "goal_id": "ID from learning goals (if provided)",
      "goal": "Learning goal text here",
      "difficulty_level": 0-4,
      "question_type": "procedural|conceptual|transfer",
      "cognitive_verb": "identify|partition|compare|etc.",
      "question_text": "Clear, specific instruction or question",
      "interaction_type": "string",
      "visual_context": "Detailed description of what student sees",
      "correct_answer": "Expected student response or action",
      "explanation": "Why this question targets the learning goal (30+ words)",
      "vocabulary_reinforced": ["term1", "term2"]
    }}
  ]
}}

Note: answer_choices is only required for Multiple Choice and Multiple Select questions.

## FOLLOW THE EXAMPLES CLOSELY

The example shows good variety in:
- Interaction types (Click → Multiple Choice → Drag and Drop)
- Difficulty levels (0 → 2 → 4)  
- Question types (procedural → conceptual → transfer)
- Visual complexity (simple bar → multiple circles → complex garden)

Match this level of variety and quality.
"""

QUESTION_GENERATOR_STRUCTURE = """
{
  "questions": [
    {
      "id": 1,
      "goal_id": "ID from learning goals (if provided)",
      "goal": "Learning goal text here",
      "difficulty_level": 0-4,
      "question_type": "procedural|conceptual|transfer",
      "cognitive_verb": "identify|partition|compare|etc.",
      "question_text": "Clear, specific instruction or question",
      "interaction_type": "string",
      "visual_context": "Detailed description of what student sees",
      "correct_answer": "Expected student response or action",
      "explanation": "Why this question targets the learning goal (30+ words)",
      "vocabulary_reinforced": ["term1", "term2"]
    }
  ]
}
"""
