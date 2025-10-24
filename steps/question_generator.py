import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from utils.json_utils import parse_json
from core.pipeline import Step
from core.prompt_builder import PromptBuilder


class QuestionGenerator(Step):
    """Generates questions from learning goals"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Question Generator", prompt_id="question_generator")
        self.claude = claude_client
        self.prompt_builder = PromptBuilder()
    
    def execute(self, input_data, **kwargs):
        """Execute step - generates questions from learning goals, going goal by goal"""
        # Handle both dict and string inputs
        if isinstance(input_data, dict):
            goals = input_data.get("goals", [])
            grade_level = input_data.get("grade_level", 3)
            vocabulary = input_data.get("full_module_data", {}).get("vocabulary", [])
            # Generate more questions to get good distribution across difficulty levels
            # Default: 6 questions per goal (can be filtered later by validator)
            questions_per_goal = kwargs.get("questions_per_goal", 6)
        else:
            goals = kwargs.get("goals", [])
            grade_level = kwargs.get("grade_level", 3)
            vocabulary = kwargs.get("vocabulary", [])
            questions_per_goal = kwargs.get("questions_per_goal", 6)
        
        if not goals:
            raise ValueError("No goals provided for question generation")
        
        # Process each goal deterministically
        all_goal_groups = []
        total_questions = 0
        
        print(f"  🎯 Generating {questions_per_goal} questions per goal for {len(goals)} goals...")
        
        for goal in goals:
            print(f"\n  📍 Processing Goal {goal['id']}: {goal['text'][:60]}...")
            
            # Generate questions for this specific goal
            goal_questions = self._generate_questions_for_goal(
                goal, 
                vocabulary, 
                grade_level, 
                questions_per_goal
            )
            
            all_goal_groups.append({
                "goal_id": goal['id'],
                "goal_text": goal['text'],
                "vocabulary_used": goal.get('vocabulary_used', []),
                "questions": goal_questions
            })
            
            total_questions += len(goal_questions)
            print(f"     ✓ Generated {len(goal_questions)} questions for Goal {goal['id']}")
        
        # Build final result
        result = {
            "metadata": {
                "total_questions": total_questions,
                "total_goals": len(goals),
                "questions_per_goal": questions_per_goal
            },
            "goals": all_goal_groups
        }
        
        print(f"\n  ✓ Total: {total_questions} questions across {len(goals)} goals")
        
        return result
    
    def _generate_questions_for_goal(self, goal, vocabulary, grade_level, num_questions):
        """Generate questions for a single goal"""
        # Format vocabulary relevant to this goal
        vocab_text = self._format_vocabulary_for_goal(vocabulary, goal.get('vocabulary_used', []))
        
        # Format example questions
        examples_text = ""
        if goal.get('example_questions'):
            examples_text = ""
            for i, ex in enumerate(goal['example_questions'], 1):
                examples_text += f"{i}. {ex}\n"
        
        # Get visual constraints from module data (passed through in kwargs or from parent)
        visuals_text = "Rectangle bars (horizontal or vertical), can be divided into 2, 3, 4, 6, or 8 equal or unequal parts"
        
        # Build prompt for this specific goal
        prompt = self.prompt_builder.build_prompt(
            "question_generator",
            {
                "goal_id": goal['id'],
                "goal_text": goal['text'],
                "vocabulary": vocab_text,
                "visuals": visuals_text,
                "examples": examples_text,
                "num_questions": num_questions,
                "grade_level": grade_level
            }
        )
        
        # Generate with reduced temperature for more consistent, example-following output
        # Increased token limit to handle multiple detailed questions with explanations
        response = self.claude.generate(prompt, max_tokens=16000, temperature=0.7)
        
        # Parse
        result = parse_json(response)
        questions = result.get("questions", []) if isinstance(result, dict) else result
        
        # Validate and add goal_id
        for q in questions:
            q['goal_id'] = goal['id']
            self._validate_question(q)
        
        return questions
    
    def _format_vocabulary_for_goal(self, all_vocabulary, goal_vocab_used):
        """Format vocabulary terms relevant to this goal"""
        if not all_vocabulary or not goal_vocab_used:
            return ""
        
        vocab_lines = []
        for term in all_vocabulary:
            if isinstance(term, dict):
                # Only include vocabulary used in this goal
                if term['term'] in goal_vocab_used:
                    line = f"- {term['term']}: {term['definition']}"
                    if 'values' in term:
                        line += f" (values: {term['values']})"
                    vocab_lines.append(line)
        
        return "\n".join(vocab_lines) if vocab_lines else ""
    
    def _validate_question(self, question):
        """Validate a single question and fix any hallucinated values"""
        VALID_DIFFICULTY_LEVELS = {0, 1, 2, 3, 4}
        VALID_QUESTION_TYPES = {"procedural", "conceptual", "transfer"}
        
        # Validate difficulty_level
        if "difficulty_level" in question:
            level = question["difficulty_level"]
            if level not in VALID_DIFFICULTY_LEVELS:
                print(f"  ⚠️  Invalid difficulty_level {level}, defaulting to 2")
                question["difficulty_level"] = 2
        
        # Validate question_type
        if "question_type" in question:
            q_type = question["question_type"]
            if q_type not in VALID_QUESTION_TYPES:
                print(f"  ⚠️  Invalid question_type '{q_type}', defaulting to 'conceptual'")
                question["question_type"] = "conceptual"
    
    def _validate_and_fix_questions(self, questions: list):
        """Validate questions and fix any hallucinated metadata values (DEPRECATED - use _validate_question)"""
        for q in questions:
            self._validate_question(q)

# Test it
if __name__ == "__main__":
    from core.claude_client import ClaudeClient
    from core.pipeline import Pipeline
    
    print("Testing QuestionGenerator with PromptBuilder...\n")
    
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