"""
Example: Using the reusable step functions in different flows

This demonstrates how to use the core step functions from steps/ 
in various contexts (pipelines, APIs, dashboards, etc.)
"""

import json
from steps.run_interaction_designer import run_interaction_designer
from steps.run_remediation_generator import run_remediation_generator
from steps.run_godot_formatter import run_godot_formatter


# ============================================================================
# EXAMPLE 1: Full Pipeline (like test_5_full_pipeline.py)
# ============================================================================
def example_full_pipeline(questions_data, module_number, path_letter):
    """Run all steps in sequence"""
    
    print("Step 1: Interaction Designer")
    sequences_data = run_interaction_designer(
        questions_data=questions_data,
        module_number=module_number,
        path_letter=path_letter
    )
    
    print("\nStep 2: Remediation Generator")
    remediation_data = run_remediation_generator(
        sequences_data=sequences_data,
        module_number=module_number,
        path_letter=path_letter
    )
    
    print("\nStep 3: Godot Formatter")
    godot_data = run_godot_formatter(
        remediation_data=remediation_data,
        module_number=module_number
    )
    
    return godot_data


# ============================================================================
# EXAMPLE 2: Custom Flow - Only Interaction Designer + Godot (skip remediation)
# ============================================================================
def example_quick_flow(questions_data, module_number):
    """Generate sequences and format for Godot without remediation"""
    
    sequences_data = run_interaction_designer(
        questions_data=questions_data,
        module_number=module_number,
        verbose=False  # Quiet mode
    )
    
    # Add a dummy success_path for Godot formatter
    for seq in sequences_data['sequences']:
        if 'student_attempts' not in seq:
            seq['student_attempts'] = {
                'success_path': {'steps': seq.get('steps', [])}
            }
    
    godot_data = run_godot_formatter(
        remediation_data=sequences_data,
        module_number=module_number,
        verbose=False
    )
    
    return godot_data


# ============================================================================
# EXAMPLE 3: Batch Processing - Process from saved files
# ============================================================================
def example_batch_processing(questions_file, module_number, path_letter):
    """Load questions from file and process"""
    
    # Load questions
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)
    
    # Run pipeline
    result = example_full_pipeline(questions_data, module_number, path_letter)
    
    # Save result
    output_file = questions_file.replace('questions', 'godot_output')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nSaved to: {output_file}")
    return result


# ============================================================================
# EXAMPLE 4: API Endpoint - Function that could be called from Flask/FastAPI
# ============================================================================
def api_generate_sequences(request_data):
    """
    Example API endpoint handler
    
    Expected request_data:
    {
        "questions": [...],
        "module_number": 1,
        "path_letter": "b",
        "steps": ["interaction", "remediation", "godot"]  # optional
    }
    """
    questions = request_data.get('questions', [])
    module_number = request_data.get('module_number')
    path_letter = request_data.get('path_letter')
    steps_to_run = request_data.get('steps', ['interaction', 'remediation', 'godot'])
    
    result = {"questions": questions}
    
    # Run requested steps
    if 'interaction' in steps_to_run:
        result['sequences'] = run_interaction_designer(
            questions_data=questions,
            module_number=module_number,
            path_letter=path_letter,
            verbose=False
        )
    
    if 'remediation' in steps_to_run:
        result['remediation'] = run_remediation_generator(
            sequences_data=result.get('sequences', questions),
            module_number=module_number,
            path_letter=path_letter,
            verbose=False
        )
    
    if 'godot' in steps_to_run:
        result['godot'] = run_godot_formatter(
            remediation_data=result.get('remediation', result.get('sequences', questions)),
            module_number=module_number,
            verbose=False
        )
    
    return result


# ============================================================================
# EXAMPLE 5: Partial Processing - Only add remediation to existing sequences
# ============================================================================
def example_add_remediation_only(sequences_file, module_number, path_letter):
    """Add remediation to already-generated sequences"""
    
    # Load existing sequences
    with open(sequences_file, 'r', encoding='utf-8') as f:
        sequences_data = json.load(f)
    
    # Only run remediation step
    remediation_data = run_remediation_generator(
        sequences_data=sequences_data,
        module_number=module_number,
        path_letter=path_letter,
        limit=5  # Only process first 5 sequences
    )
    
    # Save
    output_file = sequences_file.replace('sequences', 'remediation')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(remediation_data, f, indent=2)
    
    return remediation_data


# ============================================================================
# Usage Examples
# ============================================================================
if __name__ == "__main__":
    
    # Example questions data
    sample_questions = {
        "questions": [
            {
                "question_id": 1,
                "goal": "Understand addition",
                "prompt": "What is 2 + 3?",
                "context": "basic arithmetic"
            }
        ]
    }
    
    print("Example 1: Full Pipeline")
    print("=" * 70)
    # result = example_full_pipeline(sample_questions, module_number=1, path_letter='b')
    
    print("\n\nExample 2: Quick Flow (no remediation)")
    print("=" * 70)
    # result = example_quick_flow(sample_questions, module_number=1)
    
    print("\n\nExample 3: Batch from file")
    print("=" * 70)
    # result = example_batch_processing('inputs/questions.json', module_number=1, path_letter='b')
    
    print("\n\nExample 4: API Request")
    print("=" * 70)
    # api_request = {
    #     "questions": sample_questions["questions"],
    #     "module_number": 1,
    #     "path_letter": "b",
    #     "steps": ["interaction", "godot"]  # Skip remediation
    # }
    # result = api_generate_sequences(api_request)
    
    print("\n\nExample 5: Add remediation only")
    print("=" * 70)
    # result = example_add_remediation_only('outputs/sequences.json', module_number=1, path_letter='b')
    
    print("\nAll examples defined! Uncomment to run.")
