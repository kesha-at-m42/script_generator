import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from core.pipeline import Step


class QuestionGenerator(Step):
    """Generates questions from learning goals"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Question Generator", prompt_id="question_generator")
        self.claude = claude_client
        self.prompt_template = self._get_prompt_template()
    
    def _get_prompt_template(self) -> str:
        """Hard-coded prompt structure with framework injection placeholders"""
        return """Generate {num_questions} educational questions for grade {grade_level} based on:

{learning_goals}

{difficulty_framework}

{question_type_framework}

=== INTERACTION TYPES ===
Multiple Choice | Multiple Select | Click | Shade | Drag and Drop | Input | True/False

=== REQUIREMENTS ===
1. Follow difficulty level targets and constraints
2. Follow question type distribution targets
3. Match cognitive verbs to question types
4. Vary interaction types (use 4-5 different)
5. Progress from simple (Level 0-1) to complex (Level 3-4)

=== REQUIRED OUTPUT FORMAT ===
Return a JSON object with this EXACT structure:

{{
  "metadata": {{
    "total_questions": <number>,
    "distribution": {{
      "by_difficulty": {{"0": <count>, "1": <count>, "2": <count>, "3": <count>, "4": <count>}},
      "by_question_type": {{"procedural": <count>, "conceptual": <count>, "transfer": <count>}},
      "by_interaction_type": {{"<type>": <count>, ...}}
    }}
  }},
  "questions": [
    {{
      "id": <sequential number starting at 1>,
      "goal": "<specific learning goal addressed>",
      "prompt": "<clear, age-appropriate question text>",
      "interaction_type": "<one of the interaction types above>",
      "difficulty_level": <integer 0-4>,
      "question_type": "<procedural|conceptual|transfer>",
      "cognitive_verb": "<main action verb from appropriate category>",
      "context": "<optional visual description or scenario setup>"
    }},
    ...
  ]
}}

Return ONLY valid JSON."""
    
    def execute(self, input_data, **kwargs):
        """Execute step - generates questions from learning goals"""
        # Handle both dict and string inputs
        if isinstance(input_data, dict):
            learning_goals = input_data.get("learning_goals", "")
            num_questions = input_data.get("num_questions", 5)
            grade_level = input_data.get("grade_level", 3)
        else:
            learning_goals = str(input_data)
            num_questions = kwargs.get("num_questions", 5)
            grade_level = kwargs.get("grade_level", 3)
        
        # Load framework text directly from markdown files
        docs_dir = Path(__file__).parent.parent / "inputs" / "docs"
        
        with open(docs_dir / "difficulty_levels.md", "r", encoding="utf-8") as f:
            difficulty_framework = f.read()
        
        with open(docs_dir / "question_types.md", "r", encoding="utf-8") as f:
            question_type_framework = f.read()
        
        # Format the prompt with all variables (structure + data)
        prompt = self.prompt_template.format(
            num_questions=num_questions,
            learning_goals=learning_goals,
            grade_level=grade_level,
            difficulty_framework=difficulty_framework,
            question_type_framework=question_type_framework
        )
        
        # Generate
        print(f"  🎯 Generating {num_questions} questions...")
        response = self.claude.generate(prompt, max_tokens=4000)
        
        # Parse
        result = parse_json(response)
        
        # Validate and fix any hallucinated values
        questions = result["questions"] if isinstance(result, dict) else result
        self._validate_and_fix_questions(questions)
        
        # Quick summary
        if isinstance(result, dict) and "questions" in result:
            print(f"  ✓ Generated {len(result['questions'])} questions")
        else:
            print(f"  ✓ Generated {len(result)} questions")
        
        return result
    
    def _validate_and_fix_questions(self, questions: list):
        """Validate questions and fix any hallucinated metadata values"""
        VALID_DIFFICULTY_LEVELS = {0, 1, 2, 3, 4}
        VALID_QUESTION_TYPES = {"procedural", "conceptual", "transfer"}
        
        for i, q in enumerate(questions, 1):
            # Validate difficulty_level
            if "difficulty_level" in q:
                level = q["difficulty_level"]
                if level not in VALID_DIFFICULTY_LEVELS:
                    print(f"  ⚠️  Question {i}: Invalid difficulty_level {level}, defaulting to 2")
                    q["difficulty_level"] = 2
            
            # Validate question_type
            if "question_type" in q:
                q_type = q["question_type"]
                if q_type not in VALID_QUESTION_TYPES:
                    print(f"  ⚠️  Question {i}: Invalid question_type '{q_type}', defaulting to 'conceptual'")
                    q["question_type"] = "conceptual"

# Test it
if __name__ == "__main__":
    from core.pipeline import Pipeline
    
    print("Testing QuestionGenerator with Pipeline...\n")
    
    client = ClaudeClient()
    generator = QuestionGenerator(client)
    
    learning_goals = """
- Students can partition shapes into equal parts
- Students can identify unit fractions
    """.strip()
    
    # Test with pipeline (auto-save enabled)
    pipeline = Pipeline("test_question_generation", save_intermediate=True)
    pipeline.add_step(generator)
    
    results = pipeline.execute(
        {"learning_goals": learning_goals, "num_questions": 3, "grade_level": 3}
    )
    
    # Display results
    result = pipeline.get_final_output()
    questions = result["questions"] if isinstance(result, dict) else result
    
    print("\nGenerated questions:")
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['prompt']}")
        print(f"   Goal: {q['goal']}")
        print(f"   Type: {q['interaction_type']}")
    
    stats = client.get_stats()
    print(f"\n✓ Used {stats['total_tokens']} tokens")