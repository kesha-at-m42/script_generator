"""
Interaction Designer - Core Function
Generates interaction sequences from questions with workspace and visual schema
"""

import json
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder


def run_interaction_designer(
    questions_data,
    module_number=None,
    path_letter=None,
    limit=None,
    verbose=True
):
    """
    Generate interaction sequences from questions
    
    Args:
        questions_data: Dict with 'questions' key or list of questions
        module_number: Module number for module-specific docs (optional)
        path_letter: Path letter for module-specific docs (optional)
        limit: Limit number of questions to process (optional)
        verbose: Print progress messages (default: True)
    
    Returns:
        Dict with 'sequences' key containing generated sequences
    """
    # Normalize input
    if isinstance(questions_data, list):
        questions_data = {"questions": questions_data}
    
    questions_list = questions_data.get('questions', [])
    num_questions = len(questions_list)
    
    if verbose:
        print(f"  📋 Processing {num_questions} question(s)")
        if module_number:
            print(f"  📂 Module {module_number}, Path {path_letter}")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder(module_number=module_number, path_letter=path_letter)
    
    # Apply limit if specified
    num_to_process = min(limit, num_questions) if limit else num_questions
    
    all_sequences = []
    
    for idx in range(num_to_process):
        question = questions_list[idx]
        question_id = question.get('question_id', question.get('id', idx + 1))
        
        if verbose:
            print(f"  [{idx+1}/{num_to_process}] Processing Question {question_id}...")
        
        # Pass the entire question object as a formatted JSON string
        question_json = json.dumps(question, indent=2)
        
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
        
        # Extract JSON
        if "```json" in sequences_response:
            json_start = sequences_response.find("```json") + 7
            json_end = sequences_response.find("```", json_start)
            sequences_json = sequences_response[json_start:json_end].strip()
        else:
            sequences_json = sequences_response.strip()
        
        try:
            sequence_data = json.loads(sequences_json)
            sequences = sequence_data.get('sequences', [])
            all_sequences.extend(sequences)
            
            if verbose:
                print(f"      ✓ Generated {len(sequences)} sequence(s)")
        except json.JSONDecodeError as e:
            if verbose:
                print(f"      ✗ JSON parsing error: {e}")
                print(f"      ✗ Skipping question {question_id}")
            continue
    
    if verbose:
        print(f"\n  ✓ Total sequences generated: {len(all_sequences)}")
    
    return {"sequences": all_sequences}
