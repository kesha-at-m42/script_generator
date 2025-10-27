"""
Godot Formatter - Core Function
Transforms remediation sequences into Godot-processable schema with @type annotations
"""

import json
import time
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder
from utils.module_utils import get_module_field


def run_godot_formatter(
    remediation_data,
    module_number=None,
    limit=None,
    verbose=True
):
    """
    Transform remediation sequences to Godot-processable format
    
    Args:
        remediation_data: Dict with 'sequences' key or list of sequences
        module_number: Module number to fetch vocabulary (optional)
        limit: Limit number of sequences to process (optional)
        verbose: Print progress messages (default: True)
    
    Returns:
        Dict with '@type': 'SequencePool' and 'sequences' key containing Godot-formatted sequences
    """
    # Normalize input
    if isinstance(remediation_data, list):
        remediation_data = {"sequences": remediation_data}
    
    sequences_list = remediation_data.get('sequences', [])
    num_sequences = len(sequences_list)
    
    if verbose:
        print(f"  📋 Transforming {num_sequences} sequence(s) to Godot format")
        if module_number:
            print(f"  📂 Module {module_number}")
    
    # Fetch vocabulary if module_number is set
    vocabulary_list = ""
    if module_number is not None:
        vocabulary = get_module_field(module_number, 'vocabulary', required=False)
        if vocabulary:
            vocabulary_list = ', '.join(vocabulary)
            if verbose:
                print(f"  ✓ Loaded vocabulary: {vocabulary_list}")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder()
    
    # Apply limit if specified
    num_to_process = min(limit, num_sequences) if limit else num_sequences
    
    # Strip non-generic error paths to ensure 1-to-1 mapping
    if verbose:
        print(f"\n  ⚠️  Stripping non-generic error paths (keeping only error_path_generic)...")
    
    for sequence in sequences_list:
        if 'student_attempts' in sequence:
            attempts = sequence['student_attempts']
            # Keep only success_path and error_path_generic
            filtered_attempts = {}
            if 'success_path' in attempts:
                filtered_attempts['success_path'] = attempts['success_path']
            if 'error_path_generic' in attempts:
                filtered_attempts['error_path_generic'] = attempts['error_path_generic']
            sequence['student_attempts'] = filtered_attempts
    
    if verbose:
        print(f"  ✓ Stripped non-generic error paths\n")
    
    all_godot_sequences = []
    
    for idx in range(num_to_process):
        sequence = sequences_list[idx]
        problem_id = sequence.get('problem_id', idx + 1)
        
        if verbose:
            print(f"  [{idx+1}/{num_to_process}] Processing Sequence {problem_id}...")
        
        # Create single-sequence data for this iteration
        single_sequence_data = {
            "sequences": [sequence]
        }
        
        # Build prompt
        godot_prompt = builder.build_prompt(
            prompt_id="godot_formatter",
            variables={
                "remediation_context": json.dumps(single_sequence_data, indent=2),
                "vocabulary_terms": vocabulary_list
            }
        )
        
        # Generate Godot format with retry logic
        max_retries = 3
        retry_delay = 5  # seconds
        
        for attempt in range(max_retries):
            try:
                godot_response = client.generate(godot_prompt, max_tokens=16000, temperature=0.3)
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
                    godot_response = None
                    break
        
        if godot_response is None:
            continue
        
        # Small delay between requests
        time.sleep(1)
        
        # Extract JSON
        if "```json" in godot_response:
            json_start = godot_response.find("```json") + 7
            json_end = godot_response.find("```", json_start)
            godot_json = godot_response[json_start:json_end].strip()
        else:
            godot_json = godot_response.strip()
        
        try:
            godot_seq_data = json.loads(godot_json)
            sequences = godot_seq_data.get('sequences', [])
            all_godot_sequences.extend(sequences)
            
            if verbose:
                print(f"      ✓ Transformed successfully")
        except json.JSONDecodeError as e:
            if verbose:
                print(f"      ✗ JSON parsing error: {e}")
                print(f"      ✗ Skipping sequence {problem_id}")
            continue
    
    if verbose:
        print(f"\n  ✓ Total sequences transformed: {len(all_godot_sequences)}")
    
    return {
        "@type": "SequencePool",
        "sequences": all_godot_sequences
    }
