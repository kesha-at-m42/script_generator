import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.json_utils import parse_json
from core.pipeline import Step
from core.prompt_builder import PromptBuilder


class DialogueWriter(Step):
    """Adds character dialogue to interaction sequences"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Dialogue Writer", prompt_id="dialogue_writer")
        self.claude = claude_client
        self.prompt_builder = PromptBuilder()
    
    def _get_prompt_template(self) -> str:
        """Prompt for writing dialogue"""
        return """Add character dialogue to these interaction sequences.

<interaction_sequences>
{interaction_sequences}
</interaction_sequences>

<character_voice>
{character_template}
</character_voice>

For each sequence, replace all `dialogue_placeholder` fields with actual dialogue in the character voice. 

The placeholders use **standard response types** defined in the character guide:
- `BREAKTHROUGH` - First try success
- `BREAKTHROUGH_AFTER_STRUGGLE` - Success after hints
- `STRUGGLE_GENTLE` - First remediation attempt
- `STRUGGLE_EXPLICIT` - Second remediation attempt
- `STRUGGLE_DEMONSTRATE` - Third remediation (show solution)
- `OPENING` - Introduce new step/visual
- `PATTERN_DISCOVERY` - Student found a pattern
- `STRATEGIC_THINKING` - Note student's approach

Each placeholder also has `[visuals: ...]` or `[context: ...]` showing what students will see.

**CRITICAL - Visual/Dialogue Consistency:**
- ONLY reference visuals/animations that are listed in the `[visuals: ...]` brackets
- If placeholder says `[visuals: circle highlights, counter shows parts]`, your dialogue can reference the circle and counter
- If placeholder says `[context: verbal feedback only]`, do NOT say "look at this" or "watch this"
- Match dialogue timing to animations: "Watch as each section lights up" only if animation exists

Guidelines:
- Follow the character guide's examples for each response type
- Keep language age-appropriate and encouraging
- Use Kim's voice: professionally warm, authentically invested
- For STRUGGLE types, acknowledge difficulty without dismissing it
- For BREAKTHROUGH types, mark the moment as significant but stay grounded
- Keep dialogue concise (1-2 sentences per step)
- **Only reference visuals that are specified in the [visuals: ...] context**

**Output structure:**
Replace each `dialogue_placeholder` with `guide_says` containing actual dialogue.

Example transformation:
```
"dialogue_placeholder": "STRUGGLE_GENTLE [visuals: circle highlights each section, counter shows '1 of 4 parts']"
```
becomes:
```
"guide_says": "This is genuinely tricky. Watch as we count the sections together."
```

**DO NOT reference visuals that aren't listed:**
```
"dialogue_placeholder": "BREAKTHROUGH_AFTER_STRUGGLE [context: verbal feedback only]"
```
becomes:
```
"guide_says": "You stuck with it. That's how learning works."
```
NOT: "Look at the circle" (no circle mentioned in context)

**Use the character guide examples for each response type:**
- BREAKTHROUGH → "Right there – you got it."
- STRUGGLE_GENTLE → "This is genuinely tricky. Let's work through it."
- STRUGGLE_DEMONSTRATE → "Watch this: [explain solution with visual reference]"

Return the COMPLETE sequences with all dialogue_placeholder fields replaced by guide_says fields. Return ONLY valid JSON array."""
    
    def execute(self, input_data, **kwargs):
        """Execute step - adds dialogue to sequences"""
        # Extract sequences from step 2 output
        if isinstance(input_data, dict):
            sequences = input_data.get("sequences", [])
        elif isinstance(input_data, list):
            sequences = input_data
        else:
            sequences = []
        
        print(f"  📖 Loaded character template")
        
        # Format sequences as JSON string
        import json
        interaction_sequences = json.dumps({"sequences": sequences}, indent=2)
        
        # Build prompt using PromptBuilder
        prompt = self.prompt_builder.build_prompt(
            "dialogue_writer",
            {
                "interaction_sequences": interaction_sequences
            }
        )
        
        # Generate
        print(f"  🎯 Writing dialogue for {len(sequences)} sequences...")
        response = self.claude.generate(prompt, max_tokens=16000)  # Increased for large sequences
        
        # Debug
        print(f"  📋 API Response length: {len(response)} chars")
        if len(response) < 500:
            print(f"  ⚠️  Short response: {response[:200]}")
        
        # Parse
        try:
            result = parse_json(response)
        except Exception as e:
            # Save raw response for debugging
            debug_path = Path("outputs") / "debug_dialogue_response.txt"
            debug_path.parent.mkdir(exist_ok=True)
            with open(debug_path, "w", encoding="utf-8") as f:
                f.write(response)
            print(f"  ❌ Failed to parse JSON. Raw response saved to: {debug_path}")
            print(f"  ❌ Error: {e}")
            print(f"  📄 Last 1000 chars of response:")
            print(response[-1000:])
            raise
        
        # Extract sequences
        sequences_with_dialogue = result if isinstance(result, list) else result.get("sequences", [])
        
        # Validate
        self._validate_dialogue(sequences_with_dialogue)
        
        # Summary
        print(f"  ✓ Added dialogue to {len(sequences_with_dialogue)} sequences")
        
        return {"sequences": sequences_with_dialogue}
    
    def _validate_dialogue(self, sequences: list):
        """Check that dialogue was added"""
        for i, seq in enumerate(sequences, 1):
            main_seq = seq.get('main_sequence', [])
            for step in main_seq:
                # Check main dialogue
                if 'dialogue_placeholder' in step:
                    print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}: Still has dialogue_placeholder instead of guide_says")
                
                # Check validation dialogue
                if step.get('student_action'):
                    validation = step.get('student_action', {}).get('validation', {})
                    
                    # Check success paths
                    for key in ['success_first_attempt', 'success_after_error']:
                        if key in validation and 'dialogue_placeholder' in validation[key]:
                            print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}: {key} still has dialogue_placeholder")
                    
                    # Check error remediations
                    errors = validation.get('errors', {})
                    for error_name, error_data in errors.items():
                        remediations = error_data.get('remediations', [])
                        for rem in remediations:
                            if 'dialogue_placeholder' in rem:
                                print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}, Error {error_name}: Remediation still has dialogue_placeholder")
