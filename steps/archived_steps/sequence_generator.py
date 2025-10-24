import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from utils.json_utils import parse_json
from core.pipeline import Step


class SequenceGenerator(Step):
    """Converts questions into guided step-by-step interactive learning sequences"""
    
    def __init__(self, claude_client: ClaudeClient):
        super().__init__(name="Sequence Generator", prompt_id="sequence_generator")
        self.claude = claude_client
        self.prompt_template = self._get_prompt_template()
    
    def _get_prompt_template(self) -> str:
        """Simplified prompt template for converting questions to sequences"""
        return """Convert these educational questions into guided, step-by-step interactive learning sequences.

<questions>
{learning_goals_data}
</questions>

<character_voice>
{character_template}
</character_voice>

<visual_interaction_guide>
{visual_guide}
</visual_interaction_guide>

For each question, create a sequence with 3-6 interaction steps. Use the character voice for all dialogue. Use the visual guide to design appropriate visuals, interactions, and scaffolding based on the difficulty level.

**Output structure for each sequence:**
```json
{{
  "problem_id": <question_id>,
  "difficulty": <0-4>,
  "verb": "<action verb>",
  "goal": "<learning objective>",
  
  "main_sequence": [
    {{
      "step_id": <sequential number>,
      "guide_says": "<what tutor says in character voice>",
      "visuals": [
        {{
          "id": "<unique_id>",
          "type": "<type from visual guide>",
          "state": "<state description>",
          "description": "<human-readable description>",
          "animation": "<animation type from visual guide>" or null
        }}
      ],
      "student_action": {{
        "type": "<interaction type from visual guide>",
        "expected": "<expected outcome>",
        "validation": {{
          "success_first_attempt": {{
            "guide_says": "<encouraging feedback>",
            "next": <next_step_id or "complete">
          }},
          "success_after_error": {{
            "guide_says": "<positive reinforcement feedback>",
            "next": <next_step_id or "complete">
          }},
          "errors": {{
            "<error_type>": {{
              "condition": "<what makes this error>",
              "remediations": [
                {{
                  "attempt": 1,
                  "guide_says": "<corrective feedback>",
                  "visuals": [
                    {{
                      "id": "<visual_id>",
                      "animation": "<animation from visual guide>",
                      "description": "<what animation shows>"
                    }}
                  ],
                  "retry": true
                }},
                {{
                  "attempt": 2,
                  "guide_says": "<more explicit hint>",
                  "visuals": [
                    {{
                      "id": "<visual_id>",
                      "animation": "<stronger scaffolding animation>",
                      "description": "<what animation shows>"
                    }}
                  ],
                  "retry": true
                }},
                {{
                  "attempt": 3,
                  "guide_says": "<demonstration>",
                  "visuals": [
                    {{
                      "id": "<visual_id>",
                      "animation": "<show solution animation>",
                      "description": "<complete demonstration>"
                    }}
                  ],
                  "retry": false
                }}
              ]
            }}
          }}
        }}
      }} or null,
      "next": <next_step_id or "complete">
    }}
  ]
}}
```

Return ONLY valid JSON array. Process all questions."""
    
    def execute(self, input_data, **kwargs):
        """Execute step - converts questions to interactive sequences"""
        # Input data should be the output from QuestionGenerator (step 1)
        # which contains {"metadata": {...}, "questions": [...]}
        
        # Extract questions from step 1 output
        if isinstance(input_data, dict):
            learning_goals_data = input_data  # Use entire output from step 1
            questions_per_goal = kwargs.get("questions_per_goal", 3)
        else:
            learning_goals_data = input_data
            questions_per_goal = kwargs.get("questions_per_goal", 3)
        
        # Load character template from guide_design.md (required)
        docs_dir = Path(__file__).parent.parent / "inputs" / "docs"
        character_template_path = docs_dir / "guide_design.md"
        visual_guide_path = docs_dir / "visual_guide.md"
        
        with open(character_template_path, "r", encoding="utf-8") as f:
            character_template = f.read()
        
        with open(visual_guide_path, "r", encoding="utf-8") as f:
            visual_guide = f.read()
        
        print(f"  📖 Loaded character template")
        print(f"  🎨 Loaded visual interaction guide")
        
        # Format learning goals data as JSON string if it's a dict
        if isinstance(learning_goals_data, dict):
            import json
            learning_goals_data = json.dumps(learning_goals_data, indent=2)
        
        # Build the prompt
        prompt = self.prompt_template.format(
            learning_goals_data=learning_goals_data,
            character_template=character_template,
            visual_guide=visual_guide
        )
        
        # Generate
        print(f"  🎯 Converting questions to interactive sequences...")
        response = self.claude.generate(prompt, max_tokens=8000)
        
        # Parse
        result = parse_json(response)
        
        # Validate sequences
        sequences = result if isinstance(result, list) else result.get("sequences", [])
        self._validate_sequences(sequences)
        
        # Summary
        print(f"  ✓ Generated {len(sequences)} interactive sequences")
        
        return {"sequences": sequences}
    
    def _validate_sequences(self, sequences: list):
        """Basic validation of sequence structure"""
        for i, seq in enumerate(sequences, 1):
            # Check required fields only
            if 'problem_id' not in seq:
                print(f"  ⚠️  Sequence {i}: Missing problem_id")
            if 'main_sequence' not in seq or not seq['main_sequence']:
                print(f"  ⚠️  Sequence {i}: Missing or empty main_sequence array")
            
            # Validate steps have proper validation structure if they have student actions
            main_seq = seq.get('main_sequence', [])
            for step in main_seq:
                if step.get('student_action') and not step.get('student_action', {}).get('validation'):
                    print(f"  ⚠️  Sequence {i}, Step {step.get('step_id')}: Has student_action but missing validation")

# Test it
if __name__ == "__main__":
    from core.pipeline import Pipeline
    
    print("Testing SequenceGenerator (Step 2 only)...\n")
    print("Note: For full pipeline test (Step 1 → Step 2), run tests/test_full_pipeline.py\n")
    
    client = ClaudeClient()
    generator = SequenceGenerator(client)
    
    # Sample question data (simulating output from QuestionGenerator - Step 1)
    sample_questions = {
        "metadata": {
            "total_questions": 3,
            "distribution": {
                "by_difficulty": {"0": 0, "1": 1, "2": 2, "3": 0, "4": 0},
                "by_question_type": {"procedural": 1, "conceptual": 1, "transfer": 1}
            }
        },
        "questions": [
            {
                "id": 1,
                "goal": "Students can partition shapes into equal parts",
                "prompt": "Divide the rectangle into 4 equal parts",
                "interaction_type": "Shade",
                "difficulty_level": 1,
                "question_type": "procedural",
                "cognitive_verb": "partition"
            },
            {
                "id": 2,
                "goal": "Students can identify unit fractions",
                "prompt": "Which fraction shows 1 out of 3 equal parts?",
                "interaction_type": "Multiple Choice",
                "difficulty_level": 2,
                "question_type": "conceptual",
                "cognitive_verb": "identify"
            },
            {
                "id": 3,
                "goal": "Students can partition shapes into equal parts",
                "prompt": "Share a pizza equally among 6 friends. How many slices should each person get?",
                "interaction_type": "Input",
                "difficulty_level": 2,
                "question_type": "transfer",
                "cognitive_verb": "apply"
            }
        ]
    }
    
    print("Input: Sample question data (from Step 1)")
    print(f"  • {len(sample_questions['questions'])} questions")
    print(f"  • Will load character template from inputs/docs/guide_design.md\n")
    
    # Test with pipeline (auto-save enabled)
    pipeline = Pipeline("test_sequence_generation", save_intermediate=True)
    pipeline.add_step(generator)
    
    results = pipeline.execute(sample_questions, questions_per_goal=3)
    
    # Display results
    result = pipeline.get_final_output()
    sequences = result.get("sequences", [])
    
    print(f"\n✨ Generated {len(sequences)} interactive sequences:")
    for i, seq in enumerate(sequences, 1):
        print(f"\n{i}. Problem ID: {seq.get('problem_id')}")
        print(f"   Goal: {seq.get('goal')}")
        print(f"   Steps: {len(seq.get('steps', []))}")
        print(f"   Difficulty: {seq.get('difficulty', 'N/A')}")
        if seq.get('steps'):
            print(f"   First dialogue: \"{seq['steps'][0].get('dialogue', 'N/A')[:60]}...\"")
    
    stats = client.get_stats()
    print(f"\n✓ Used {stats['total_tokens']} tokens")
