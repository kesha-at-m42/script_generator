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
        
        # OPTIMIZATION: Strip unnecessary fields to reduce token count
        # DialogueWriter only needs: problem_id, goal, and dialogue_placeholder fields
        # It doesn't need full visual descriptions or animation details
        compact_sequences = self._create_compact_sequences(sequences)
        
        # Format sequences as JSON string
        import json
        interaction_sequences = json.dumps({"sequences": compact_sequences}, indent=2)
        
        print(f"  🔧 Compacted input from {len(json.dumps({'sequences': sequences})):,} to {len(interaction_sequences):,} chars")
        
        # Build prompt using PromptBuilder
        prompt = self.prompt_builder.build_prompt(
            "dialogue_writer",
            {
                "interaction_sequences": interaction_sequences
            }
        )
        
        # Generate
        print(f"  🎯 Writing dialogue for {len(sequences)} sequences...")
        response = self.claude.generate(prompt, max_tokens=12000)  # Reduced - dialogue is shorter than validation logic
        
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
        compact_with_dialogue = result if isinstance(result, list) else result.get("sequences", [])
        
        # Merge dialogue back into original full sequences
        sequences_with_dialogue = self._merge_dialogue(sequences, compact_with_dialogue)
        
        # Validate
        self._validate_dialogue(sequences_with_dialogue)
        
        # Summary
        print(f"  ✓ Added dialogue to {len(sequences_with_dialogue)} sequences")
        
        return {"sequences": sequences_with_dialogue}
    
    def _create_compact_sequences(self, sequences: list) -> list:
        """Create compact version with only fields needed for dialogue writing"""
        compact = []
        
        for seq in sequences:
            compact_seq = {
                "problem_id": seq.get("problem_id"),
                "goal": seq.get("goal"),
                "verb": seq.get("verb"),
                "difficulty": seq.get("difficulty"),
                "main_sequence": []
            }
            
            for step in seq.get("main_sequence", []):
                compact_step = {
                    "step_id": step.get("step_id"),
                    "dialogue_placeholder": step.get("dialogue_placeholder")
                }
                
                # Include student_action if present (for validation placeholders)
                if step.get("student_action"):
                    compact_step["student_action"] = self._compact_student_action(step["student_action"])
                
                compact_seq["main_sequence"].append(compact_step)
            
            compact.append(compact_seq)
        
        return compact
    
    def _compact_student_action(self, student_action: dict) -> dict:
        """Compact student action to only include dialogue placeholders"""
        if not student_action:
            return None
        
        compact = {
            "description": student_action.get("description")
        }
        
        validation = student_action.get("validation", {})
        if validation:
            compact_validation = {}
            
            # Success paths - only keep dialogue_placeholder
            if "success_first_attempt" in validation:
                compact_validation["success_first_attempt"] = {
                    "dialogue_placeholder": validation["success_first_attempt"].get("dialogue_placeholder")
                }
            
            if "success_after_error" in validation:
                compact_validation["success_after_error"] = {
                    "dialogue_placeholder": validation["success_after_error"].get("dialogue_placeholder")
                }
            
            # Error paths - only keep dialogue_placeholders from remediations
            if "errors" in validation:
                compact_errors = {}
                for error_name, error_data in validation["errors"].items():
                    compact_remediations = []
                    for rem in error_data.get("remediations", []):
                        compact_remediations.append({
                            "attempt": rem.get("attempt"),
                            "dialogue_placeholder": rem.get("dialogue_placeholder")
                        })
                    compact_errors[error_name] = {
                        "remediations": compact_remediations
                    }
                compact_validation["errors"] = compact_errors
            
            compact["validation"] = compact_validation
        
        return compact
    
    def _merge_dialogue(self, original_sequences: list, dialogue_sequences: list) -> list:
        """Merge dialogue from compact sequences back into original full sequences"""
        merged = []
        
        for orig_seq, dialogue_seq in zip(original_sequences, dialogue_sequences):
            merged_seq = orig_seq.copy()
            merged_seq["main_sequence"] = []
            
            for orig_step, dialogue_step in zip(orig_seq.get("main_sequence", []), dialogue_seq.get("main_sequence", [])):
                merged_step = orig_step.copy()
                
                # Replace dialogue_placeholder with guide_says
                if "guide_says" in dialogue_step:
                    merged_step["guide_says"] = dialogue_step["guide_says"]
                    if "dialogue_placeholder" in merged_step:
                        del merged_step["dialogue_placeholder"]
                
                # Merge student_action dialogue if present
                if "student_action" in merged_step and "student_action" in dialogue_step:
                    merged_step["student_action"] = self._merge_student_action_dialogue(
                        merged_step["student_action"],
                        dialogue_step["student_action"]
                    )
                
                merged_seq["main_sequence"].append(merged_step)
            
            merged.append(merged_seq)
        
        return merged
    
    def _merge_student_action_dialogue(self, original: dict, dialogue: dict) -> dict:
        """Merge dialogue into original student_action"""
        if not original or not dialogue:
            return original
        
        merged = original.copy()
        
        if "validation" in merged and "validation" in dialogue:
            orig_val = merged["validation"]
            dial_val = dialogue["validation"]
            
            # Merge success paths
            if "success_first_attempt" in orig_val and "success_first_attempt" in dial_val:
                if "guide_says" in dial_val["success_first_attempt"]:
                    orig_val["success_first_attempt"]["guide_says"] = dial_val["success_first_attempt"]["guide_says"]
                    if "dialogue_placeholder" in orig_val["success_first_attempt"]:
                        del orig_val["success_first_attempt"]["dialogue_placeholder"]
            
            if "success_after_error" in orig_val and "success_after_error" in dial_val:
                if "guide_says" in dial_val["success_after_error"]:
                    orig_val["success_after_error"]["guide_says"] = dial_val["success_after_error"]["guide_says"]
                    if "dialogue_placeholder" in orig_val["success_after_error"]:
                        del orig_val["success_after_error"]["dialogue_placeholder"]
            
            # Merge error remediations
            if "errors" in orig_val and "errors" in dial_val:
                for error_name in orig_val["errors"]:
                    if error_name in dial_val["errors"]:
                        orig_rems = orig_val["errors"][error_name].get("remediations", [])
                        dial_rems = dial_val["errors"][error_name].get("remediations", [])
                        
                        for orig_rem, dial_rem in zip(orig_rems, dial_rems):
                            if "guide_says" in dial_rem:
                                orig_rem["guide_says"] = dial_rem["guide_says"]
                                if "dialogue_placeholder" in orig_rem:
                                    del orig_rem["dialogue_placeholder"]
        
        return merged
    
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
