import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from utils.json_utils import parse_json
from core.pipeline import Step
from core.prompt_builder import PromptBuilder


class InteractionDesigner(Step):
    """Designs visual interactions and flow without dialogue"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Interaction Designer", prompt_id="interaction_designer")
        self.claude = claude_client
        self.prompt_builder = PromptBuilder()
    
    def execute(self, input_data, **kwargs):
        """Execute step - designs interaction flow"""
        # Extract questions from step 1 output
        if isinstance(input_data, dict):
            questions_data = input_data
        else:
            questions_data = input_data
        
        print(f"  🎨 Loaded visual interaction guide")
        
        # Format learning goals data as JSON string if it's a dict
        if isinstance(questions_data, dict):
            import json
            questions_data = json.dumps(questions_data, indent=2)
        
        # Build prompt using PromptBuilder
        prompt = self.prompt_builder.build_prompt(
            "interaction_designer",
            {
                "learning_goals_data": questions_data
            }
        )
        
        # Generate
        print(f"  🎯 Designing interaction sequences...")
        response = self.claude.generate(prompt, max_tokens=16000)  # Increased for complex sequences
        
        # Debug: show response
        print(f"  📋 API Response length: {len(response)} chars")
        if len(response) < 500:
            print(f"  ⚠️  Short response: {response[:200]}")
        
        # Parse
        try:
            result = parse_json(response)
        except Exception as e:
            # Save raw response for debugging
            debug_path = Path("outputs") / "debug_response.txt"
            debug_path.parent.mkdir(exist_ok=True)
            with open(debug_path, "w", encoding="utf-8") as f:
                f.write(response)
            print(f"  ❌ Failed to parse JSON. Raw response saved to: {debug_path}")
            print(f"  ❌ Error: {e}")
            print(f"  📄 First 500 chars of response:")
            print(response[:500])
            print(f"  📄 Last 500 chars of response:")
            print(response[-500:])
            raise
        
        # Validate sequences
        sequences = result if isinstance(result, list) else result.get("sequences", [])
        self._validate_sequences(sequences)
        
        # Summary
        print(f"  ✓ Designed {len(sequences)} interaction sequences")
        
        return {"sequences": sequences}
    
    def _validate_sequences(self, sequences: list):
        """Basic validation of sequence structure"""
        for i, seq in enumerate(sequences, 1):
            # Check required fields only
            if 'problem_id' not in seq:
                print(f"  ⚠️  Sequence {i}: Missing problem_id")
            if 'main_sequence' not in seq or not seq['main_sequence']:
                print(f"  ⚠️  Sequence {i}: Missing or empty main_sequence array")
