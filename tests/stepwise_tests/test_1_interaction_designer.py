"""
Stepwise Test 1: Interaction Designer
Takes a questions JSON file and generates sequences with workspace + visual schema
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

def test_interaction_designer(questions_path, output_dir=None):
    """
    Test interaction designer with questions from a JSON file
    
    Args:
        questions_path: Path to questions JSON file
        output_dir: Optional output directory (auto-generated if not provided)
    """
    print("=" * 70)
    print("STEPWISE TEST 1: INTERACTION DESIGNER")
    print("=" * 70)
    
    # Load questions
    print(f"\nLoading questions from: {questions_path}")
    with open(questions_path, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)
    
    num_questions = len(questions_data.get('questions', []))
    print(f"✓ Loaded {num_questions} questions")
    
    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_interaction_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder()
    
    # ========================================================================
    # INTERACTION DESIGNER
    # ========================================================================
    print("=" * 70)
    print("GENERATING SEQUENCES")
    print("=" * 70)
    
    print("\nGenerating sequences with workspace + visual schema...")
    
    sequences_prompt = builder.build_prompt(
        prompt_id="interaction_designer",
        variables={"learning_goals_data": json.dumps(questions_data, indent=2)}
    )
    
    print(f"Prompt length: {len(sequences_prompt)} characters")
    print("Calling Claude API...")
    
    sequences_response = client.generate(sequences_prompt, max_tokens=8000, temperature=0.7)
    
    # Save raw response
    with open(f"{output_dir}/sequences_raw.txt", "w", encoding="utf-8") as f:
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
        
        sequences_output_path = f"{output_dir}/sequences.json"
        with open(sequences_output_path, "w", encoding="utf-8") as f:
            json.dump(sequences_data, f, indent=2)
        
        print(f"✓ Generated {len(sequences_data.get('sequences', []))} sequences")
        print(f"✓ Saved to {sequences_output_path}")
        
        # ====================================================================
        # VALIDATE SCHEMA
        # ====================================================================
        print("\n" + "=" * 70)
        print("SCHEMA VALIDATION")
        print("=" * 70)
        
        validation_results = {
            "total_sequences": len(sequences_data.get('sequences', [])),
            "sequences": []
        }
        
        for idx, seq in enumerate(sequences_data.get('sequences', []), 1):
            seq_validation = {
                "sequence_id": idx,
                "problem_id": seq.get('problem_id'),
                "num_steps": len(seq.get('steps', [])),
                "issues": []
            }
            
            print(f"\n  Sequence {idx} (Problem ID: {seq.get('problem_id')}):")
            print(f"    - Steps: {seq_validation['num_steps']}")
            
            # Check Part 1 steps (should have workspace)
            part1_steps = [step for step in seq.get('steps', []) if 'workspace' in step]
            part1_count = len(part1_steps)
            print(f"    - Part 1 steps (with workspace): {part1_count} {'✓' if part1_count > 0 else '✗'}")
            if part1_count == 0:
                seq_validation['issues'].append("No Part 1 steps with workspace field")
            
            # Check Part 2 steps (should have workspace_context + interaction_tool)
            part2_steps = [step for step in seq.get('steps', []) if 'workspace_context' in step and 'interaction_tool' in step]
            part2_count = len(part2_steps)
            print(f"    - Part 2 steps (with workspace_context + interaction_tool): {part2_count} {'✓' if part2_count > 0 else '✗'}")
            if part2_count == 0:
                seq_validation['issues'].append("No Part 2 steps with workspace_context and interaction_tool")
            
            # Check that Part 2 steps have correct_answer
            part2_with_answer = sum(1 for step in part2_steps if 'correct_answer' in step)
            print(f"    - Part 2 steps with correct_answer: {part2_with_answer}/{part2_count} {'✓' if part2_with_answer == part2_count else '✗'}")
            if part2_with_answer != part2_count:
                seq_validation['issues'].append("Some Part 2 steps missing correct_answer")
            
            # Check visual field (should be omitted/not present in main flow)
            steps_with_visual = sum(1 for step in seq.get('steps', []) if 'visual' in step)
            print(f"    - Steps with visual field: {steps_with_visual}/{seq_validation['num_steps']} {'✓ (should be 0)' if steps_with_visual == 0 else '⚠️'}")
            if steps_with_visual > 0:
                seq_validation['issues'].append("Visual field present in main flow steps (should be omitted)")
            
            # Check success_path
            has_success = 'success_path' in seq.get('student_attempts', {})
            print(f"    - Has success_path: {has_success} {'✓' if has_success else '✗'}")
            if not has_success:
                seq_validation['issues'].append("Missing success_path in student_attempts")
            
            # Check for error paths (should be NONE at this stage)
            error_paths = [k for k in seq.get('student_attempts', {}).keys() if k.startswith('error_path')]
            has_error_paths = len(error_paths) > 0
            print(f"    - Has error paths: {len(error_paths)} {'✗ (should be 0)' if has_error_paths else '✓'}")
            if has_error_paths:
                seq_validation['issues'].append(f"Unexpected error paths: {error_paths}")
            
            validation_results['sequences'].append(seq_validation)
        
        # Save validation report
        validation_path = f"{output_dir}/validation_report.json"
        with open(validation_path, "w", encoding="utf-8") as f:
            json.dump(validation_results, f, indent=2)
        
        print(f"\n✓ Validation report saved to {validation_path}")
        
        # ====================================================================
        # SUMMARY
        # ====================================================================
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        
        total_issues = sum(len(s['issues']) for s in validation_results['sequences'])
        
        print(f"\n✓ Generated {validation_results['total_sequences']} sequences")
        print(f"{'✓' if total_issues == 0 else '⚠️'} Total validation issues: {total_issues}")
        
        if total_issues > 0:
            print("\nIssues found:")
            for seq in validation_results['sequences']:
                if seq['issues']:
                    print(f"  Sequence {seq['sequence_id']}:")
                    for issue in seq['issues']:
                        print(f"    - {issue}")
        
        print(f"\nOutput files:")
        print(f"  - {output_dir}/sequences_raw.txt")
        print(f"  - {output_dir}/sequences.json ← Use this for remediation test")
        print(f"  - {output_dir}/validation_report.json")
        
        print("\n📊 Expected Schema:")
        print("  ✓ Part 1 steps: dialogue + workspace")
        print("  ✓ Part 2 steps: dialogue + prompt + interaction_tool + workspace_context + correct_answer")
        print("  ✓ Optional Part 2 fields: choices, input_config")
        print("  ✓ Visual field: omitted (not present) in main flow steps")
        print("  ✓ success_path: In student_attempts")
        print("  ✓ No error_path_* (added in remediation step)")
        
        print("\n" + "=" * 70)
        
        return sequences_output_path
        
    except json.JSONDecodeError as e:
        print(f"\n✗ JSON parsing error: {e}")
        print(f"✗ Raw response saved to {output_dir}/sequences_raw.txt")
        print(f"✗ Check the raw response for syntax errors")
        return None

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Interaction Designer with questions JSON')
    parser.add_argument('questions_path', help='Path to questions JSON file')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.questions_path):
        print(f"✗ Error: Questions file not found: {args.questions_path}")
        sys.exit(1)
    
    test_interaction_designer(args.questions_path, args.output)

if __name__ == "__main__":
    main()
