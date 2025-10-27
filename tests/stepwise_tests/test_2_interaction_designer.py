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

def test_interaction_designer(questions_path, output_dir=None, limit=None, module_number=None, path_letter=None):
    """
    Test interaction designer with questions from a JSON file
    
    Args:
        questions_path: Path to questions JSON file
        output_dir: Optional output directory (auto-generated if not provided)
        limit: Optional limit on number of questions to process
        module_number: Module number (if None, will prompt user)
        path_letter: Path letter (if None, will prompt user)
    """
    print("=" * 70)
    print("STEPWISE TEST 1: INTERACTION DESIGNER")
    print("=" * 70)
    
    # Load questions
    print(f"\nLoading questions from: {questions_path}")
    with open(questions_path, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    # Handle both formats: list or dict with 'questions' key
    if isinstance(loaded_data, list):
        questions_data = {"questions": loaded_data}
    else:
        questions_data = loaded_data
    
    num_questions = len(questions_data.get('questions', []))
    print(f"✓ Loaded {num_questions} questions")
    
    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_interaction_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # Get module information for accessing module-specific docs (if not provided)
    if module_number is None:
        print("\nModule Configuration:")
        try:
            module_input = input("Enter module number (e.g., 1) or press Enter to skip: ").strip()
            if module_input:
                module_number = int(module_input)
                path_letter = input("Enter path letter (e.g., a, b, c): ").strip().lower()
                print(f"✓ Using module {module_number}, path {path_letter}")
            else:
                module_number = None
                path_letter = None
                print("⚠️  No module specified - module-specific docs won't be loaded")
        except ValueError:
            print("⚠️  Invalid module number - skipping module configuration")
            module_number = None
            path_letter = None
    else:
        print(f"\n✓ Using module {module_number}, path {path_letter}")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder(module_number=module_number, path_letter=path_letter)
    
    # ========================================================================
    # INTERACTION DESIGNER
    # ========================================================================
    print("=" * 70)
    print("GENERATING SEQUENCES")
    print("=" * 70)
    
    # Determine how many questions to process
    questions_list = questions_data.get('questions', [])
    print(f"\nTotal questions available: {num_questions}")
    
    if limit is not None:
        num_to_process = min(limit, num_questions)
        print(f"⚠️  Processing only first {num_to_process} questions (limit specified)")
    else:
        try:
            user_input = input("How many questions would you like to process? (press Enter for all): ").strip()
            if user_input == "":
                num_to_process = num_questions
            else:
                num_to_process = int(user_input)
                num_to_process = min(num_to_process, num_questions)  # Cap at total available
        except ValueError:
            print("Invalid input, processing all questions")
            num_to_process = num_questions
    
    print(f"\nProcessing {num_to_process} question(s) (one at a time)...\n")
    
    all_sequences = []
    
    for idx in range(num_to_process):
        question = questions_list[idx]
        question_id = question.get('question_id', question.get('id', idx + 1))  # Use question_id, id, or index
        print(f"  [{idx+1}/{num_to_process}] Processing Question {question_id}...")
        
        # Pass the entire question object as a formatted JSON string
        # The prompt will parse fields like goal, prompt, context, question_type, etc.
        question_json = json.dumps(question, indent=2)
        
        print(f"\n  📋 Question data being passed to prompt:")
        print(f"  {question_json}")
        print()
        
        sequences_prompt = builder.build_prompt(
            prompt_id="interaction_designer",
            variables={
                "question_data": question_json,
                "questions_data": question_json,
                "learning_goals_data": question_json,
            }
        )
        
        # Generate sequence for this question
        sequences_response = client.generate(sequences_prompt, max_tokens=8000, temperature=0.7)
        
        # Save individual raw response - use index-based filename
        with open(f"{output_dir}/sequence_{idx + 1}_raw.txt", "w", encoding="utf-8") as f:
            f.write(sequences_response)
        
        # Extract JSON
        if "```json" in sequences_response:
            json_start = sequences_response.find("```json") + 7
            json_end = sequences_response.find("```", json_start)
            sequences_json = sequences_response[json_start:json_end].strip()
        else:
            sequences_json = sequences_response.strip()
        
        try:
            sequence_data = json.loads(sequences_json)
            # Extract sequences from response and add to collection
            sequences = sequence_data.get('sequences', [])
            all_sequences.extend(sequences)
            print(f"      ✓ Generated {len(sequences)} sequence(s)")
        except json.JSONDecodeError as e:
            print(f"      ✗ JSON parsing error: {e}")
            print(f"      ✗ Skipping question {question.get('id')}")
            continue
    
    print(f"\n  ✓ Total sequences generated: {len(all_sequences)}")
    
    # Combine all sequences into final output
    sequences_data = {"sequences": all_sequences}
    
    try:
        
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
        };
        
        for idx, seq in enumerate(sequences_data.get('sequences', []), 1):
            seq_validation = {
                "sequence_id": idx,
                "problem_id": seq.get('problem_id'),
                "num_steps": len(seq.get('steps', [])),
                "issues": []
            }
            
            print(f"\n  Sequence {idx} (Problem ID: {seq.get('problem_id')}):")
            print(f"    - Steps: {seq_validation['num_steps']}")
            
            # Check steps have required fields
            steps_with_workspace = [step for step in seq.get('steps', []) if 'workspace' in step]
            steps_with_interaction = [step for step in seq.get('steps', []) if 'interaction_tool' in step]
            steps_with_answer = [step for step in seq.get('steps', []) if 'correct_answer' in step]
            
            print(f"    - Steps with workspace: {len(steps_with_workspace)} {'✓' if len(steps_with_workspace) > 0 else '✗'}")
            if len(steps_with_workspace) == 0:
                seq_validation['issues'].append("No steps with workspace field")
            
            print(f"    - Steps with interaction_tool: {len(steps_with_interaction)} {'✓' if len(steps_with_interaction) > 0 else '✗'}")
            if len(steps_with_interaction) == 0:
                seq_validation['issues'].append("No steps with interaction_tool")
            
            print(f"    - Steps with correct_answer: {len(steps_with_answer)} {'✓' if len(steps_with_answer) > 0 else '✗'}")
            if len(steps_with_answer) == 0:
                seq_validation['issues'].append("No steps with correct_answer")
            
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
        print("  ✓ Steps should have: dialogue, prompt, interaction_tool, workspace, correct_answer")
        print("  ✓ Optional step fields: choices (for MCQs)")
        print("  ✓ workspace: Array of tangible objects with id, type, sections, state, shaded")
        print("  ✓ student_attempts.success_path: Success dialogue")
        print("  ✓ No error_path_* at this stage (added in remediation step)")
        print("  ✓ Visual effects: Not in main flow steps (added in remediation)")
        
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
