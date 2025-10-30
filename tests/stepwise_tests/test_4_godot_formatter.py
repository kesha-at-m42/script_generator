"""
Stepwise Test 3: Godot Formatter
Takes remediation JSON and transforms it to Godot-processable schema using AI
Uses Claude for structural transformation + deterministic BBCode formatting
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder
from utils.module_utils import get_module_field
from utils.metadata_mapper import map_to_mastery_metadata
from utils.bbcode_formatter import process_godot_sequences


def test_godot_formatter(remediation_path, output_dir=None, limit=None, module_number=None, metadata_type="SequenceMetadata"):
    """
    Test Godot formatter with remediation JSON file
    
    Args:
        remediation_path: Path to remediation JSON file (output from remediation generator)
        output_dir: Optional output directory (auto-generated if not provided)
        limit: Optional limit on number of sequences to process (for testing)
        module_number: Module number to fetch vocabulary (if None, will prompt user)
        metadata_type: Expected @type value for metadata validation

    Returns:
        str: Path to the generated Godot sequences JSON file.
    """
    print("=" * 70)
    print("STEPWISE TEST 3: GODOT FORMATTER")
    print("=" * 70)
    
    # Load remediation data
    print(f"\nLoading remediation from: {remediation_path}")
    with open(remediation_path, 'r', encoding='utf-8') as f:
        remediation_data = json.load(f)
    
    num_sequences = len(remediation_data.get('sequences', []))
    print(f"✓ Loaded {num_sequences} sequences")
    
    # Apply limit if specified
    if limit and limit < num_sequences:
        print(f"⚠️  Processing only first {limit} sequences (limit specified)")
        remediation_data['sequences'] = remediation_data['sequences'][:limit]
        num_sequences = limit
    elif limit is None:
        # Interactive mode - ask user how many to process
        print(f"\n{'='*70}")
        print(f"INTERACTIVE MODE")
        print(f"{'='*70}")
        response = input(f"\nProcess all {num_sequences} sequences? (y/n or Enter for yes, or enter a number): ").strip().lower()
        
        if response == 'n':
            print("Cancelled by user.")
            return None
        elif response == '' or response == 'y':
            # Explicitly treat empty input or 'y' as confirmation to process all
            pass
        else:
            try:
                custom_limit = int(response)
                if custom_limit > 0 and custom_limit < num_sequences:
                    remediation_data['sequences'] = remediation_data['sequences'][:custom_limit]
                    num_sequences = custom_limit
                elif custom_limit > num_sequences:
                    print(f"⚠️  Requested {custom_limit} but only {num_sequences} available. Processing all.")
                    remediation_data['sequences'] = remediation_data['sequences'][:num_sequences]
                    # num_sequences remains unchanged, as we process all available
            except ValueError:
                print(f"Invalid input. Processing all {num_sequences} sequences.")
    
    # Strip non-generic error paths to ensure 1-to-1 mapping
    print(f"\n⚠️  Stripping non-generic error paths (keeping only error_path_generic)...")
    for sequence in remediation_data['sequences']:
        if 'student_attempts' in sequence:
            attempts = sequence['student_attempts']
            # Keep only success_path and error_path_generic
            filtered_attempts = {}
            if 'success_path' in attempts:
                filtered_attempts['success_path'] = attempts['success_path']
            if 'error_path_generic' in attempts:
                filtered_attempts['error_path_generic'] = attempts['error_path_generic']
            sequence['student_attempts'] = filtered_attempts
    
    print(f"✓ Stripped non-generic error paths. Each sequence will generate exactly 1 Godot sequence.\n")
    
    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_godot_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # ========================================================================
    # GET VOCABULARY FOR FORMATTING
    # ========================================================================
    
    # Ask user for module number to fetch vocabulary (if not provided)
    if module_number is None:
        try:
            module_input = input("Enter module number to fetch vocabulary (e.g., 1) or press Enter to skip: ").strip()
            if module_input:
                module_number = int(module_input)
            else:
                print("⚠️  No module specified - vocabulary formatting will be skipped")
        except ValueError:
            print("⚠️  Invalid module number - vocabulary formatting will be skipped")
            module_number = None
    
    # Fetch vocabulary if module_number is set
    vocabulary_list = None
    if module_number is not None:
        vocabulary = get_module_field(module_number, 'vocabulary', required=False)
        if vocabulary:
            vocabulary_list = vocabulary  # Keep as list
            print(f"✓ Loaded vocabulary from module {module_number}: {', '.join(vocabulary)}")
        else:
            print("⚠️  No vocabulary found in module")
    
    # ========================================================================
    # TRANSFORM TO GODOT SCHEMA (using AI)
    # ========================================================================
    print("\n" + "=" * 70)
    print("TRANSFORMING TO GODOT SCHEMA")
    print("=" * 70)
    
    print(f"\nTransforming {num_sequences} sequences to Godot format (one at a time)...")
    print("  - AI: Structural transformation + @type annotations")
    print("  - AI: Flattening steps structure")
    print("  - AI: Mapping validators and remediations")
    print("  - AI: Embedding visual effects as metadata.events")
    print("  - Post: Correcting metadata with metadata_mapper (deterministic)")
    print("  - Post: Formatting fractions with [fraction] BBCode (deterministic)")
    print("  - Post: Formatting vocabulary with [vocab] tags (deterministic)\n")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder()
    
    all_godot_sequences = []
    sequences_list = remediation_data.get('sequences', [])
    
    for idx, sequence in enumerate(sequences_list, 1):
        print(f"  [{idx}/{num_sequences}] Processing Sequence {sequence.get('problem_id')}...")
        
        # Create single-sequence data for this iteration
        single_sequence_data = {
            "sequences": [sequence]
        }
        
        # Build prompt (note: vocabulary is NOT passed to AI anymore)
        godot_prompt = builder.build_prompt(
            prompt_id="godot_formatter",
            variables={
                "complete_interaction_sequences": json.dumps(single_sequence_data, indent=2)
            }
        )
        
        # Generate Godot format for this sequence with retry logic
        max_retries = 3
        retry_delay = 5  # seconds
        
        for attempt in range(max_retries):
            try:
                godot_response = client.generate(godot_prompt, max_tokens=16000, temperature=0.3)
                break  # Success, exit retry loop
            except Exception as e:
                if "Overloaded" in str(e) and attempt < max_retries - 1:
                    print(f"      ⚠️  API overloaded, retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    print(f"      ✗ Error: {e}")
                    print(f"      ✗ Skipping sequence {sequence.get('problem_id')}")
                    godot_response = None
                    break
        
        if godot_response is None:
            continue
        
        # Add small delay between requests
        time.sleep(1)
        
        # Save individual raw response
        with open(f"{output_dir}/godot_{idx:03d}_problem{sequence.get('problem_id')}_goal{sequence.get('goal_id')}_raw.txt", "w", encoding="utf-8") as f:
            f.write(godot_response)
        
        # Extract JSON
        if "```json" in godot_response:
            json_start = godot_response.find("```json") + 7
            json_end = godot_response.find("```", json_start)
            godot_json = godot_response[json_start:json_end].strip()
        else:
            godot_json = godot_response.strip()
        
        try:
            godot_seq_data = json.loads(godot_json)
            
            # ================================================================
            # STEP 1: Fix metadata using metadata_mapper
            # ================================================================
            print(f"      ⚙️  Correcting metadata fields...")
            for godot_seq in godot_seq_data.get('sequences', []):
                # Extract fields from original input sequence for mapping
                input_fields = {
                    'difficulty': sequence.get('difficulty', 2),
                    'verb': sequence.get('verb', 'CREATE'),
                    'goal_id': sequence.get('goal_id', 1),
                    'goal': sequence.get('goal', ''),
                    'fractions': sequence.get('fractions', []),
                    'problem_id': sequence.get('problem_id', 0)
                }
                
                # Generate correct metadata
                correct_metadata = map_to_mastery_metadata(input_fields)
                
                # Preserve problem_id from input (not in mapper output)
                correct_metadata['problem_id'] = input_fields['problem_id']
                
                # Update the sequence metadata
                if 'metadata' not in godot_seq:
                    godot_seq['metadata'] = {}
                godot_seq['metadata'].update(correct_metadata)
            
            # ================================================================
            # STEP 2: BBCode formatting
            # ================================================================
            print(f"      ⚙️  Applying BBCode formatting...")
            godot_seq_data = process_godot_sequences(godot_seq_data, vocabulary_list)
            
            # Extract sequences from response and add to collection
            sequences = godot_seq_data.get('sequences', [])
            all_godot_sequences.extend(sequences)
            print(f"      ✓ Transformed successfully")
            
        except json.JSONDecodeError as e:
            print(f"      ✗ JSON parsing error: {e}")
            print(f"      ✗ Skipping sequence {sequence.get('problem_id')}")
            continue
    
    print(f"\n  ✓ Total sequences transformed: {len(all_godot_sequences)}")
    
    # Combine all sequences into final output
    godot_data = {
        "@type": "SequencePool",
        "sequences": all_godot_sequences
    }
    
    # Save Godot schema
    godot_output_path = f"{output_dir}/godot_sequences.json"
    with open(godot_output_path, "w", encoding="utf-8") as f:
        json.dump(godot_data, f, indent=2)
    
    print(f"\n✓ Transformed {len(godot_data.get('sequences', []))} sequences")
    print(f"✓ Saved to {godot_output_path}")
    
    # ========================================================================
    # VALIDATE GODOT SCHEMA
    # ========================================================================
    print("\n" + "=" * 70)
    print("SCHEMA VALIDATION")
    print("=" * 70)
    
    validation_results = {
        "total_sequences": len(godot_data.get('sequences', [])),
        "sequences": []
    }
    
    for idx, seq in enumerate(godot_data.get('sequences', []), 1):
        seq_validation = {
            "sequence_id": idx,
            "problem_id": seq.get('metadata', {}).get('problem_id'),
            "steps": [],
            "issues": []
        }
        
        print(f"\n  Sequence {idx} (Problem ID: {seq_validation['problem_id']}):")
        
        steps = seq.get('steps', [])
        print(f"    - Total steps: {len(steps)}")
        
        # Check metadata structure
        metadata = seq.get('metadata', {})
        if '@type' not in metadata or metadata['@type'] != metadata_type:
            seq_validation['issues'].append(f"Metadata missing @type or not '{metadata_type}'")
        
        required_metadata_fields = ['mastery_tier', 'mastery_component', 'mastery_verbs', 
                                    'goal_id', 'goal_text', 'problem_id', 'variables_covered']
        for field in required_metadata_fields:
            if field not in metadata:
                seq_validation['issues'].append(f"Metadata missing required field: {field}")
        
        # Check each step
        workspace_steps = 0
        prompt_steps = 0
        dialogue_steps = 0
        
        for step_idx, step in enumerate(steps, 1):
            step_type = step.get('@type')
            has_workspace = 'workspace' in step
            has_prompt = 'prompt' in step
            has_dialogue = 'dialogue' in step
            
            if step_type != 'Step':
                seq_validation['issues'].append(f"Step {step_idx}: Missing @type or not 'Step'")
            
            if has_workspace:
                workspace_steps += 1
                tangibles = step.get('workspace', {}).get('tangibles', [])
                print(f"      Step {step_idx}: Workspace with {len(tangibles)} tangible(s) ✓")
                
                # Check tangibles have @type
                for tangible in tangibles:
                    if '@type' not in tangible:
                        seq_validation['issues'].append(f"Step {step_idx}: Tangible missing @type")
            
            elif has_prompt:
                prompt_steps += 1
                prompt = step['prompt']
                validator = prompt.get('validator', {})
                remediations = prompt.get('remediations', [])
                
                print(f"      Step {step_idx}: Prompt with validator and {len(remediations)} remediation(s) ✓")
                
                # Check validator has @type
                if '@type' not in validator:
                    seq_validation['issues'].append(f"Step {step_idx}: Validator missing @type")
                
                # Check remediations structure
                for rem_idx, rem in enumerate(remediations):
                    if '@type' not in rem:
                        seq_validation['issues'].append(f"Step {step_idx}, Remediation {rem_idx}: Missing @type")
                    if 'id' not in rem or not isinstance(rem['id'], str) or not rem['id'].strip():
                        seq_validation['issues'].append(f"Step {step_idx}, Remediation {rem_idx}: Invalid or missing id")
                
                # Check BBCode formatting
                if 'text' in prompt and '/' in prompt['text'] and '[fraction' not in prompt['text']:
                    seq_validation['issues'].append(f"Step {step_idx}: Prompt text may have unformatted fractions")
            
            elif has_dialogue:
                dialogue_steps += 1
                print(f"      Step {step_idx}: Dialogue only ✓")
                
                # Check BBCode formatting in dialogue
                if '/' in step['dialogue'] and '[fraction' not in step['dialogue']:
                    seq_validation['issues'].append(f"Step {step_idx}: Dialogue may have unformatted fractions")
        
        print(f"    - Workspace steps: {workspace_steps}")
        print(f"    - Prompt steps: {prompt_steps}")
        print(f"    - Dialogue steps: {dialogue_steps}")
        
        validation_results['sequences'].append(seq_validation)
    
    # Save validation report
    validation_path = f"{output_dir}/validation_report.json"
    with open(validation_path, "w", encoding="utf-8") as f:
        json.dump(validation_results, f, indent=2)
    
    print(f"\n✓ Validation report saved to {validation_path}")
    
    # ========================================================================
    # METADATA VERIFICATION
    # ========================================================================
    print("\n" + "=" * 70)
    print("METADATA VERIFICATION")
    print("=" * 70)
    
    print("\nChecking corrected metadata fields:")
    for idx, seq in enumerate(godot_data.get('sequences', [])[:3], 1):  # Show first 3
        metadata = seq.get('metadata', {})
        print(f"\n  Sequence {idx}:")
        print(f"    - problem_id: {metadata.get('problem_id')}")
        print(f"    - goal_id: {metadata.get('goal_id')}")
        print(f"    - mastery_tier: {metadata.get('mastery_tier')}")
        print(f"    - mastery_component: {metadata.get('mastery_component')}")
        print(f"    - mastery_verbs: {metadata.get('mastery_verbs')}")
        print(f"    - variables_covered: {metadata.get('variables_covered')}")
    
    if len(godot_data.get('sequences', [])) > 3:
        print(f"\n  ... and {len(godot_data.get('sequences', [])) - 3} more sequences")
    
    # ========================================================================
    # BBCODE FORMATTING CHECK
    # ========================================================================
    print("\n" + "=" * 70)
    print("BBCODE FORMATTING VERIFICATION")
    print("=" * 70)
    
    fraction_count = 0
    vocab_count = 0
    
    for seq in godot_data.get('sequences', []):
        for step in seq.get('steps', []):
            # Check dialogue
            if 'dialogue' in step:
                fraction_count += step['dialogue'].count('[fraction')
                vocab_count += step['dialogue'].count('[vocab')
            
            # Check prompt
            if 'prompt' in step:
                prompt = step['prompt']
                if 'text' in prompt:
                    fraction_count += prompt['text'].count('[fraction')
                
                # Check remediations
                for rem in prompt.get('remediations', []):
                    rem_dialogue = rem.get('step', {}).get('dialogue', '')
                    fraction_count += rem_dialogue.count('[fraction')
                    vocab_count += rem_dialogue.count('[vocab')
                
                # Check on_correct
                if 'on_correct' in prompt and prompt['on_correct']:
                    on_correct_dialogue = prompt['on_correct'].get('dialogue', '')
                    fraction_count += on_correct_dialogue.count('[fraction')
                    vocab_count += on_correct_dialogue.count('[vocab')
    
    print(f"\n  ✓ Fraction BBCode tags found: {fraction_count}")
    print(f"  ✓ Vocabulary tags found: {vocab_count}")
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    total_issues = sum(len(s['issues']) for s in validation_results['sequences'])
    
    print(f"\n✓ Transformed {validation_results['total_sequences']} sequences")
    print(f"{'✓' if total_issues == 0 else '⚠️'} Total validation issues: {total_issues}")
    
    if total_issues > 0:
        print("\nIssues found:")
        for seq in validation_results['sequences']:
            if seq['issues']:
                print(f"  Sequence {seq['sequence_id']}:")
                for issue in seq['issues']:
                    print(f"    - {issue}")
    
    print(f"\nOutput files:")
    print(f"  - {output_dir}/godot_NNN_*.txt (raw AI responses)")
    print(f"  - {output_dir}/godot_sequences.json ← Godot-processable format")
    print(f"  - {output_dir}/validation_report.json")
    
    print("\n📊 Godot Schema Features:")
    print("  ✓ @type annotations for all objects (Godot type system)")
    print("  ✓ Flattened steps[] array (no nesting)")
    print("  ✓ Workspace with tangibles array")
    print("  ✓ Prompt with validator and remediations")
    print("  ✓ Remediations with id: light/medium/heavy")
    print("  ✓ Visual effects in metadata.events")
    print("  ✓ Metadata with corrected mastery fields (via metadata_mapper)")
    print("  ✓ Fractions formatted with [fraction] BBCode (deterministic)")
    print("  ✓ Vocabulary wrapped with [vocab] tags (deterministic)")
    
    print("\n" + "=" * 70)
    
    return godot_output_path


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Godot Formatter with remediation JSON')
    parser.add_argument('remediation_path', help='Path to remediation JSON file (from remediation generator)')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    parser.add_argument('-n', '--limit', type=int, help='Limit number of sequences to process (for testing)', default=None)
    parser.add_argument('-m', '--module', type=int, help='Module number to fetch vocabulary', default=None)
    parser.add_argument('--metadata-type', type=str, help='Expected @type value for metadata validation', default="SequenceMetadata")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.remediation_path):
        print(f"✗ Error: Remediation file not found: {args.remediation_path}")
        sys.exit(1)
    
    test_godot_formatter(args.remediation_path, args.output, args.limit, args.module, args.metadata_type)


if __name__ == "__main__":
    main()