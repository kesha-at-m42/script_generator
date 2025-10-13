"""Step 2: Answer Generator - Generates solutions for questions"""
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from core.pipeline import Step

class AnswerGenerator(Step):
    """Generates detailed answers/solutions for questions"""
    
    def __init__(self, claude_client: ClaudeClient, prompt_template: str = None):
        super().__init__(name="Answer Generator", prompt_id="answer_generator")
        self.claude = claude_client
        
        if prompt_template is None:
            prompt_template = self._load_prompt_template()
        
        self.prompt_template = prompt_template
    
    def _load_prompt_template(self) -> str:
        """Load prompt template from saved prompts"""
        prompts_file = Path("prompts/saved_prompts.json")
        
        if prompts_file.exists():
            with open(prompts_file, 'r') as f:
                prompts = json.load(f)
                if "answer_generator" in prompts:
                    return prompts["answer_generator"]["template"]
        
        # Fallback default
        return """Given these educational questions, generate detailed answers with explanations:

{questions}

Return as a JSON array where each item has:
- "question": the original question text
- "answer": the correct answer
- "explanation": step-by-step explanation
- "hints": array of helpful hints for students

Example:
[
  {{
    "question": "What is 1/2 + 1/4?",
    "answer": "3/4",
    "explanation": "First find common denominator (4), convert 1/2 to 2/4, then add: 2/4 + 1/4 = 3/4",
    "hints": ["Find a common denominator", "Convert fractions", "Add numerators"]
  }}
]"""
    
    def execute(self, input_data, **kwargs):
        """Generate answers for questions"""
        print("  🎯 Generating answers...")
        
        # Format questions for prompt
        if isinstance(input_data, list):
            questions_text = json.dumps(input_data, indent=2)
        else:
            questions_text = str(input_data)
        
        prompt = self.prompt_template.format(questions=questions_text)
        
        # Generate
        response = self.claude.generate(prompt, max_tokens=3000)
        
        print("  ✓ Response received, parsing...")
        answers = parse_json(response)
        
        print(f"  ✓ Generated {len(answers)} answers")
        return answers


# Test
if __name__ == "__main__":
    from core.claude_client import ClaudeClient
    
    print("Testing AnswerGenerator...\n")
    
    client = ClaudeClient()
    generator = AnswerGenerator(client)
    
    test_questions = [
        {"question": "What is 1/2 + 1/4?", "goal": "Add fractions"},
        {"question": "What is 3/4 - 1/4?", "goal": "Subtract fractions"}
    ]
    
    answers = generator.execute(test_questions)
    
    print("\nGenerated answers:")
    for ans in answers:
        print(f"\n Q: {ans['question']}")
        print(f" A: {ans['answer']}")
        print(f" Explanation: {ans['explanation'][:50]}...")
