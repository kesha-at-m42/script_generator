import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from utils.json_utils import parse_json
from core.pipeline import Step
from core.prompt_builder import PromptBuilder


class ValidationDesigner(Step):
    """Designs validation logic and error remediation strategies"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Validation Designer", prompt_id="validation_designer")
        self.claude = claude_client
        self.prompt_builder = PromptBuilder()
    
    def _get_prompt_template(self) -> str:
        """Prompt for designing validation and error handling"""
        return """Design validation and error handling for these interaction sequences.

<interaction_sequences>
{interaction_sequences}
</interaction_sequences>

<visual_interaction_guide>
{visual_guide}
</visual_interaction_guide>

For each sequence, design the validation logic for student actions:

1. **Identify possible error types** - What mistakes might students make?
2. **Design progressive scaffolding** - 3 attempts with increasing support
3. **Select remediation animations** - Use animations from the visual guide
4. **Plan success paths** - Different feedback for first try vs after hints

**Output structure for each student_action:**
```json
"student_action": {{
  "type": "<interaction type>",
  "expected": "<expected outcome>",
  "description": "<what student should do>",
  "validation": {{
    "success_first_attempt": {{
      "dialogue_placeholder": "BREAKTHROUGH [context: first try success]",
      "next": <next_step_id or "complete">
    }},
    "success_after_error": {{
      "dialogue_placeholder": "BREAKTHROUGH_AFTER_STRUGGLE [context: success after hints]",
      "next": <next_step_id or "complete">
    }},
    "errors": {{
      "<error_name>": {{
        "condition": "<what makes this error>",
        "remediations": [
          {{
            "attempt": 1,
            "dialogue_placeholder": "STRUGGLE_GENTLE [visuals: <list animations here>]",
            "animations": [
              {{
                "visual_id": "<id of visual to animate>",
                "type": "<animation from guide>",
                "description": "<what it shows>"
              }}
            ]
          }},
          {{
            "attempt": 2,
            "dialogue_placeholder": "STRUGGLE_EXPLICIT [visuals: <list animations here>]",
            "animations": [
              {{
                "visual_id": "<id>",
                "type": "<stronger animation>",
                "description": "<clearer demonstration>"
              }}
            ]
          }},
          {{
            "attempt": 3,
            "dialogue_placeholder": "STRUGGLE_DEMONSTRATE [visuals: <list animations here>]",
            "animations": [
              {{
                "visual_id": "<id>",
                "type": "<show answer animation>",
                "description": "<complete solution>"
              }}
            ]
          }}
        ]
      }}
    }}
  }}
}}
```

**Standard dialogue_placeholder types:**
- `BREAKTHROUGH` - Student got it right on first try (Case 2: Breakthrough Moments)
- `BREAKTHROUGH_AFTER_STRUGGLE` - Student succeeded after errors (Case 2 + Case 1 combined)
- `STRUGGLE_GENTLE` - First remediation attempt, acknowledge difficulty (Case 1: Struggle Moments)
- `STRUGGLE_EXPLICIT` - Second attempt, more direct guidance (Case 1: Struggle Moments)
- `STRUGGLE_DEMONSTRATE` - Third attempt, show the solution (Case 1: Struggle Moments + showing)
- `OPENING` - Introduce a new step or visual (Case 5: Opening/Transitioning)
- `PATTERN_DISCOVERY` - Student found a pattern (Case 3: Pattern Discovery)
- `STRATEGIC_THINKING` - Note student's approach (Case 4: Strategic Thinking)

**CRITICAL for dialogue_placeholder:**
- Use ONLY the standard types above
- Always include `[visuals: ...]` or `[context: ...]` after the type
- List ALL animations that will appear for that remediation
- Be specific: `[visuals: circle highlights sections 1-4, counter shows '1 of 4 parts']`
- If no visuals/animations: `[context: verbal feedback only]`
- This ensures DialogueWriter knows what visuals exist to reference

**Guidelines:**
- Consider difficulty level when designing error types (harder = more error types)
- Progressive scaffolding: gentle → explicit → demonstrate
- Use animations from visual guide (highlighting, pulsing, counting, etc.)
- Error names should be descriptive (e.g., "wrong_numerator", "shaded_too_many")
- Each remediation attempt should increase scaffolding
- **ALWAYS include visual context in dialogue_placeholder: `[visuals: ...]` or `[context: ...]`**
- List specific animations so DialogueWriter knows what students will see

Return the COMPLETE sequences with validation added to each student_action. Return ONLY valid JSON array."""
    
    def execute(self, input_data, **kwargs):
        """Execute step - designs validation logic"""
        # Extract sequences from interaction designer output
        if isinstance(input_data, dict):
            sequences = input_data.get("sequences", [])
        elif isinstance(input_data, list):
            sequences = input_data
        else:
            sequences = []
        
        print(f"  🎯 Loaded visual guide for animation reference")
        
        # Format sequences as JSON string
        import json
        interaction_sequences = json.dumps({"sequences": sequences}, indent=2)
        
        # Build prompt using PromptBuilder
        prompt = self.prompt_builder.build_prompt(
            "validation_designer",
            {
                "interaction_sequences": interaction_sequences
            }
        )
        
        # Generate
        print(f"  🎯 Designing validation logic for {len(sequences)} sequences...")
        response = self.claude.generate(prompt, max_tokens=20000)  # Increased for complex validation logic
        
        # Debug
        print(f"  📋 API Response length: {len(response)} chars")
        if len(response) < 500:
            print(f"  ⚠️  Short response: {response[:200]}")
        
        # Parse
        try:
            result = parse_json(response)
        except Exception as e:
            # Save raw response for debugging
            debug_path = Path("outputs") / "debug_validation_response.txt"
            debug_path.parent.mkdir(exist_ok=True)
            with open(debug_path, "w", encoding="utf-8") as f:
                f.write(response)
            print(f"  ❌ Failed to parse JSON. Raw response saved to: {debug_path}")
            print(f"  ❌ Error: {e}")
            print(f"  📄 Last 1000 chars of response:")
            print(response[-1000:])
            raise
        
        # Extract sequences
        sequences_with_validation = result if isinstance(result, list) else result.get("sequences", [])
        
        # Validate
        self._validate_validation(sequences_with_validation)
        
        # Summary
        print(f"  ✓ Designed validation for {len(sequences_with_validation)} sequences")
        
        return {"sequences": sequences_with_validation}
    
    def _validate_validation(self, sequences: list):
        """Check that validation was added"""
        for i, seq in enumerate(sequences, 1):
            main_seq = seq.get('main_sequence', [])
            for step in main_seq:
                student_action = step.get('student_action')
                if student_action:
                    validation = student_action.get('validation')
                    if not validation:
                        print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}: Missing validation for student_action")
                    elif not validation.get('errors'):
                        print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}: No error types defined")
