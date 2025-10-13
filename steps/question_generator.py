import sys
from pathlib import Path
import json

# Add parent directory to path so we can import core modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from core.pipeline import Step

class QuestionGenerator(Step):
    """Generates questions from learning goals"""
    
    def __init__(self, claude_client: ClaudeClient, prompt_template: str = None):
        super().__init__(name="Question Generator", prompt_id="question_generator")
        self.claude = claude_client
        
        # Load prompt from saved prompts file or use provided template
        if prompt_template is None:
            prompt_template = self._load_prompt_template()
        
        self.prompt_template = prompt_template
    
    def _load_prompt_template(self) -> str:
        """Load prompt template from dashboard's saved prompts"""
        prompts_file = Path("prompts/saved_prompts.json")
        
        if prompts_file.exists():
            with open(prompts_file, 'r') as f:
                prompts = json.load(f)
                if "question_generator" in prompts:
                    return prompts["question_generator"]["template"]
        
        # Fallback to default if file doesn't exist
        return """Generate {num_questions} educational questions based on these learning goals:

{learning_goals}

Return as a JSON array where each item has:
- "goal": the specific learning goal being addressed
- "prompt": the question text
- "interaction_type": one of ["Click", "Shade", "Multiple Choice", "Drag and Drop"]

Example:
[
  {{
    "goal": "Students can identify fractions",
    "prompt": "Click on the shape that shows 1/2",
    "interaction_type": "Click"
  }}
]"""
    
    def generate(self, learning_goals: str, num_questions: int = 5) -> list:
        """Generate questions from learning goals (legacy method)"""
        return self.execute({"learning_goals": learning_goals, "num_questions": num_questions})
    
    def execute(self, input_data, **kwargs):
        """Execute step - generates questions from learning goals"""
        # Handle both dict and string inputs
        if isinstance(input_data, dict):
            learning_goals = input_data.get("learning_goals", "")
            num_questions = input_data.get("num_questions", 5)
        else:
            learning_goals = str(input_data)
            num_questions = kwargs.get("num_questions", 5)
        
        # Format the prompt with provided variables
        prompt = self.prompt_template.format(
            num_questions=num_questions,
            learning_goals=learning_goals
        )
        
        print("  🎯 Generating questions...")
        response = self.claude.generate(prompt, max_tokens=2000)
        
        print("  ✓ Response received, parsing JSON...")
        questions = parse_json(response)
        
        print(f"  ✓ Generated {len(questions)} questions")
        return questions

# Test it
if __name__ == "__main__":
    print("Testing QuestionGenerator...\n")
    
    client = ClaudeClient()
    generator = QuestionGenerator(client)
    
    learning_goals = """
- Students can partition shapes into equal parts
- Students can identify unit fractions
    """.strip()
    
    questions = generator.generate(learning_goals, num_questions=3)
    
    print("\nGenerated questions:")
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['prompt']}")
        print(f"   Goal: {q['goal']}")
        print(f"   Type: {q['interaction_type']}")
    
    stats = client.get_stats()
    print(f"\n✓ Used {stats['total_tokens']} tokens")