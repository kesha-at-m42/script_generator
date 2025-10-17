"""
Stepwise Test: Interaction Designer + Remediation Generator
Tests the new schema with workspace and visual fields
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder

# Sample questions for testing
SAMPLE_QUESTIONS = {
    "questions": [
        {
            "id": 1,
            "question_text": "Click on a bar where all parts are the same size.",
            "interaction_type": "Click",
            "difficulty_level": 1,
            "question_type": "conceptual",
            "cognitive_verb": "identify",
            "visual_context": "Three horizontal bars: Bar A divided into 4 equal parts, Bar B divided into 4 unequal parts, Bar C divided into 2 equal parts",
            "correct_answer": "Bar A or Bar C",
            "explanation": "This tests recognition of equal versus unequal parts",
            "vocabulary_reinforced": ["equal parts"]
        },
        {
            "id": 2,
            "question_text": "Click 2 times on the bar to divide it into 3 equal parts.",
            "interaction_type": "Click",
            "difficulty_level": 0,
            "question_type": "procedural",
            "cognitive_verb": "partition",
            "visual_context": "A horizontal rectangular bar, unpartitioned, solid color",
            "correct_answer": "Two click positions at 1/3 and 2/3 of the bar width",
            "explanation": "Basic partitioning skill - creating three equal parts",
            "vocabulary_reinforced": ["partition", "equal parts"]
        },
        {
            "id": 3,
            "question_text": "A baker cuts a rectangular cake. Are these equal parts or unequal parts?",
            "interaction_type": "Multiple Choice",
            "difficulty_level": 3,
            "question_type": "transfer",
            "cognitive_verb": "apply",
            "visual_context": "A rectangular cake divided into 5 pieces with varying widths (2 narrow, 1 very wide, 2 medium)",
            "correct_answer": "Unequal parts",
            "explanation": "Applies equal/unequal concept to real-world context",
            "vocabulary_reinforced": ["equal parts"],
            "answer_choices": ["Equal parts", "Unequal parts"]
        }
    ]
}

def main():
    print("=" * 70)
    print("STEPWISE TEST: INTERACTION DESIGNER + REMEDIATION GENERATOR")
    print("=" * 70)
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"outputs/stepwise_test_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder()
    
    # Save sample questions
    with open(f"{output_dir}/0_questions.json", "w", encoding="utf-8") as f:
        json.dump(SAMPLE_QUESTIONS, f, indent=2)
    
    print(f"✓ Using {len(SAMPLE_QUESTIONS['questions'])} sample questions")
    
    # ========================================================================
    # STEP 1: INTERACTION DESIGNER
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 1: INTERACTION DESIGNER")
    print("=" * 70)
    
    print("\nGenerating sequences with new schema (workspace + visual fields)...")
    
    sequences_prompt = builder.build_prompt(
        prompt_id="interaction_designer",
        variables={"learning_goals_data": json.dumps(SAMPLE_QUESTIONS, indent=2)}
    )
    
    print(f"Prompt length: {len(sequences_prompt)} characters")
    print("Calling Claude API...")
    
    sequences_response = client.generate(sequences_prompt, max_tokens=8000, temperature=0.7)
    
    # Save raw response
    with open(f"{output_dir}/1_sequences_raw.txt", "w", encoding="utf-8") as f:
        f.write(sequences_response)
    
    # Extract JSON
    if "```json" in sequences_response:
        json_start = sequences_response.find("```json") + 7
        json_end = sequences_response.find("```", json_start)
        sequences_json = sequences_response[json_start:json_end].strip()
    else:
        sequences_json = sequences_response.strip()
    
    try:
        sequences_data = json.loads(sequences_json)
        
        with open(f"{output_dir}/1_sequences.json", "w", encoding="utf-8") as f:
            json.dump(sequences_data, f, indent=2)
        
        print(f"✓ Generated {len(sequences_data.get('sequences', []))} sequences")
        
        # Validate schema
        print("\n📋 Validating schema:")
        for idx, seq in enumerate(sequences_data.get('sequences', []), 1):
            print(f"\n  Sequence {idx}:")
            print(f"    - Steps: {len(seq.get('steps', []))}")
            
            # Check workspace field
            has_workspace = all('workspace' in step for step in seq.get('steps', []))
            print(f"    - Has workspace field in all steps: {has_workspace} {'✓' if has_workspace else '✗'}")
            
            # Check visual field (should be null in main flow)
            all_visual_null = all(step.get('visual') is None for step in seq.get('steps', []))
            print(f"    - Visual is null in all steps: {all_visual_null} {'✓' if all_visual_null else '✗'}")
            
            # Check valid_workspace
            has_valid_workspace = 'valid_workspace' in seq or 'valid_visual' in seq
            print(f"    - Has valid_workspace/valid_visual: {has_valid_workspace} {'✓' if has_valid_workspace else '⚠️'}")
            
            # Check success_path
            has_success = 'success_path' in seq.get('student_attempts', {})
            print(f"    - Has success_path: {has_success} {'✓' if has_success else '✗'}")
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {e}")
        print(f"Raw response saved to {output_dir}/1_sequences_raw.txt")
        return
    
    # ========================================================================
    # STEP 2: REMEDIATION GENERATOR
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 2: REMEDIATION GENERATOR")
    print("=" * 70)
    
    print("\nAdding error paths with new schema (scaffolding_level, workspace_context, visual)...")
    
    remediation_prompt = builder.build_prompt(
        prompt_id="remediation_generator",
        variables={"interactions_context": json.dumps(sequences_data, indent=2)}
    )
    
    print(f"Prompt length: {len(remediation_prompt)} characters")
    print("Calling Claude API...")
    
    remediation_response = client.generate(remediation_prompt, max_tokens=16000, temperature=0.3)
    
    # Save raw response
    with open(f"{output_dir}/2_remediation_raw.txt", "w", encoding="utf-8") as f:
        f.write(remediation_response)
    
    # Extract JSON
    if "```json" in remediation_response:
        json_start = remediation_response.find("```json") + 7
        json_end = remediation_response.find("```", json_start)
        remediation_json = remediation_response[json_start:json_end].strip()
    else:
        remediation_json = remediation_response.strip()
    
    try:
        remediation_data = json.loads(remediation_json)
        
        with open(f"{output_dir}/2_remediation.json", "w", encoding="utf-8") as f:
            json.dump(remediation_data, f, indent=2)
        
        print(f"✓ Added error paths to {len(remediation_data.get('sequences', []))} sequences")
        
        # Validate schema
        print("\n📋 Validating remediation schema:")
        for idx, seq in enumerate(remediation_data.get('sequences', []), 1):
            print(f"\n  Sequence {idx}:")
            
            attempts = seq.get('student_attempts', {})
            error_paths = [k for k in attempts.keys() if k.startswith('error_path')]
            
            print(f"    - Error paths: {len(error_paths)}")
            
            # Check each error path
            for error_path_name in error_paths:
                error_path = attempts[error_path_name]
                steps = error_path.get('steps', [])
                print(f"\n    - {error_path_name}: {len(steps)} steps")
                
                for step_idx, step in enumerate(steps, 1):
                    # Check scaffolding_level
                    has_scaffolding = 'scaffolding_level' in step
                    scaffolding = step.get('scaffolding_level', 'MISSING')
                    print(f"      Step {step_idx}: scaffolding_level={scaffolding} {'✓' if has_scaffolding else '✗'}")
                    
                    # Check workspace_context
                    has_context = 'workspace_context' in step
                    print(f"        - workspace_context: {has_context} {'✓' if has_context else '✗'}")
                    
                    # Check visual (should be null for light, object for medium/heavy)
                    visual = step.get('visual')
                    if scaffolding == 'light':
                        correct_visual = visual is None
                        print(f"        - visual is null (light): {correct_visual} {'✓' if correct_visual else '✗'}")
                    elif scaffolding in ['medium', 'heavy']:
                        has_visual_effects = visual is not None and 'effects' in visual
                        print(f"        - visual has effects: {has_visual_effects} {'✓' if has_visual_effects else '✗'}")
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {e}")
        print(f"Raw response saved to {output_dir}/2_remediation_raw.txt")
        return
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    print(f"\n✓ Test completed successfully")
    print(f"\nOutput files:")
    print(f"  - {output_dir}/0_questions.json")
    print(f"  - {output_dir}/1_sequences.json (with workspace + visual schema)")
    print(f"  - {output_dir}/2_remediation.json (with scaffolding_level, workspace_context, visual)")
    
    print("\n📊 Schema Validation:")
    print("  - workspace: Array of tangibles in main flow steps")
    print("  - visual: null in main flow, populated in remediation")
    print("  - scaffolding_level: light/medium/heavy at remediation step level")
    print("  - workspace_context: References to existing tangibles in remediation")
    print("  - visual.effects: Animation/highlight effects in medium/heavy remediation")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
