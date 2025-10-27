"""
Remediation Generator - Core Function
Adds error paths with scaffolding levels (light, medium, heavy) to interaction sequences
"""

import json
import time
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder


def run_remediation_generator(
    sequences_data,
    module_number=None,
    path_letter=None,
    limit=None,
    verbose=True
):
    """
    Add error paths with remediation scaffolding to sequences
    
    Args:
        sequences_data: Dict with 'sequences' key or list of sequences
        module_number: Module number for module-specific docs (optional)
        path_letter: Path letter for module-specific docs (optional)
        limit: Limit number of sequences to process (optional)
        verbose: Print progress messages (default: True)
    
    Returns:
        Dict with 'sequences' key containing sequences with error paths added
    """
    # Normalize input
    if isinstance(sequences_data, list):
        sequences_data = {"sequences": sequences_data}
    
    sequences_list = sequences_data.get('sequences', [])
    num_sequences = len(sequences_list)
    
    if verbose:
        print(f"  📋 Adding error paths to {num_sequences} sequence(s)")
        if module_number:
            print(f"  📂 Module {module_number}, Path {path_letter}")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder(module_number=module_number, path_letter=path_letter)
    
    # Apply limit if specified
    num_to_process = min(limit, num_sequences) if limit else num_sequences
    
    all_sequences = []
    
    for idx in range(num_to_process):
        sequence = sequences_list[idx]
        problem_id = sequence.get('problem_id', idx + 1)
        
        if verbose:
            print(f"  [{idx+1}/{num_to_process}] Processing Sequence {problem_id}...")
        
        # Create single-sequence data for this iteration
        single_sequence_data = {
            "sequences": [sequence]
        }
        
        # Build dynamic prefill - copy sequence up to error_path_generic
        prefill_seq = sequence.copy()
        # Ensure student_attempts exists
        if 'student_attempts' not in prefill_seq:
            prefill_seq['student_attempts'] = {}
        
        # Build prefill JSON stopping at error_path_generic opening
        prefill_dict = {"sequences": [prefill_seq]}
        prefill_json = json.dumps(prefill_dict, indent=2)
        
        # Truncate at the end of success_path and add error_path_generic opening
        prefill_parts = prefill_json.rsplit('}', 2)  # Split at last 2 closing braces
        prefill_text = prefill_parts[0] + '},\n            "error_path_generic": {'
        
        remediation_prompt = builder.build_prompt(
            prompt_id="remediation_generator",
            variables={
                "interactions_context": json.dumps(single_sequence_data, indent=2),
                "prefill_sequence": prefill_text
            }
        )
        
        # Generate remediation with retry logic
        max_retries = 3
        retry_delay = 5  # seconds
        
        for attempt in range(max_retries):
            try:
                remediation_response = client.generate(remediation_prompt, max_tokens=16000, temperature=0.3)
                break  # Success, exit retry loop
            except Exception as e:
                if "Overloaded" in str(e) and attempt < max_retries - 1:
                    if verbose:
                        print(f"      ⚠️  API overloaded, retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    if verbose:
                        print(f"      ✗ Error: {e}")
                        print(f"      ✗ Skipping sequence {problem_id}")
                    remediation_response = None
                    break
        
        if remediation_response is None:
            continue
        
        # Small delay between requests to avoid overwhelming API
        time.sleep(1)
        
        # Extract JSON
        if "```json" in remediation_response:
            json_start = remediation_response.find("```json") + 7
            json_end = remediation_response.find("```", json_start)
            remediation_json = remediation_response[json_start:json_end].strip()
        else:
            remediation_json = remediation_response.strip()
        
        try:
            remediation_seq_data = json.loads(remediation_json)
            sequences = remediation_seq_data.get('sequences', [])
            all_sequences.extend(sequences)
            
            # Count error paths added
            error_paths = 0
            if sequences:
                attempts = sequences[0].get('student_attempts', {})
                error_paths = len([k for k in attempts.keys() if k.startswith('error_path')])
            
            if verbose:
                print(f"      ✓ Added {error_paths} error path(s)")
        except json.JSONDecodeError as e:
            if verbose:
                print(f"      ✗ JSON parsing error: {e}")
                print(f"      ✗ Skipping sequence {problem_id}")
            continue
    
    if verbose:
        print(f"\n  ✓ Total sequences processed: {len(all_sequences)}")
    
    return {"sequences": all_sequences}
