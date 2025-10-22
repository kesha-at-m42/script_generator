"""
Stepwise Test 3: Godot Formatter
Takes remediation JSON and transforms it to Godot-processable schema using AI
Uses Claude to intelligently transform schema with proper @type annotations and structure
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
from utils.vocabulary_helper import format_vocabulary_list_for_prompt


def transform_to_godot_schema_OLD(remediation_data):
    """
    Transform remediation schema to Godot-processable format
    
    Current schema:
    - Part 1: workspace (array of tangibles)
    - Part 2: workspace_context + interaction_tool + correct_answer
    - Error paths: scaffolding_level + workspace_context + visual (effects array)
    
    Godot schema:
    - Flat steps[] array
    - @type annotations for Godot type system
    - Consistent structure for parsing
    """
    
    godot_sequences = []
    
    for seq in remediation_data.get('sequences', []):
        godot_seq = {
            "@type": "Sequence",
            "problem_id": seq.get('problem_id'),
            "difficulty": seq.get('difficulty'),
            "verb": seq.get('verb'),
            "goal": seq.get('goal'),
            "steps": []
        }
        
        # Transform main steps
        main_steps = seq.get('steps', [])
        for step_idx, step in enumerate(main_steps):
            
            # Check if this is Part 1 (workspace setup) or Part 2 (interaction)
            has_workspace = 'workspace' in step
            has_interaction = 'interaction_tool' in step
            
            if has_workspace:
                # Part 1: Setup step with workspace tangibles
                godot_step = {
                    "@type": "Step",
                    "workspace": {
                        "@type": "WorkspaceData",
                        "tangibles": transform_tangibles(step['workspace'])
                    }
                }
                
                # Add dialogue if present
                if step.get('dialogue'):
                    godot_step['dialogue'] = step['dialogue']
                
                godot_seq['steps'].append(godot_step)
            
            elif has_interaction:
                # Part 2: Interaction step
                # Split into dialogue + prompt steps
                
                # Dialogue step
                if step.get('dialogue'):
                    godot_seq['steps'].append({
                        "@type": "Step",
                        "dialogue": step['dialogue']
                    })
                
                # Prompt step with validator and remediations
                prompt_step = {
                    "@type": "Step",
                    "prompt": {
                        "@type": "Prompt",
                        "text": step.get('prompt', ''),
                        "tool": step.get('interaction_tool'),
                        "validator": create_validator(step),
                        "remediations": []
                    }
                }
                
                # Add choices if present
                if 'choices' in step:
                    prompt_step['prompt']['choices'] = {
                        "@type": "WorkspaceChoices",
                        "allow_multiple": False,
                        "options": [choice['text'] for choice in step['choices']]
                    }
                
                # Transform error paths to remediations
                student_attempts = seq.get('student_attempts', {})
                
                # Add all error paths
                for error_path_name, error_path in student_attempts.items():
                    if error_path_name.startswith('error_path'):
                        remediations = transform_error_path_to_remediations(error_path)
                        prompt_step['prompt']['remediations'].extend(remediations)
                
                godot_seq['steps'].append(prompt_step)
                
                # Success step
                success_path = student_attempts.get('success_path', {})
                success_steps = success_path.get('steps', [])
                if success_steps:
                    godot_seq['steps'].append({
                        "@type": "Step",
                        "dialogue": success_steps[0].get('dialogue', '')
                    })
        
        godot_sequences.append(godot_seq)
    
    return {
        "@type": "SequencePool",
        "sequences": godot_sequences
    }


def transform_tangibles(workspace_array):
    """Transform workspace array to Godot tangibles format"""
    tangibles = []
    
    for tangible in workspace_array:
        godot_tangible = {
            "@type": map_type_to_godot(tangible.get('type', ''))
        }
        
        # Copy all properties except 'type' (already mapped to @type)
        for key, value in tangible.items():
            if key != 'type':
                godot_tangible[key] = value
        
        tangibles.append(godot_tangible)
    
    return tangibles


def map_type_to_godot(type_name):
    """Map our type names to Godot class names"""
    type_map = {
        'rectangle_bar': 'RectangleBar',
        'square': 'Square',
        'circle': 'Circle',
        'number_line': 'NumberLine',
        'fraction_bar': 'FractionBar'
    }
    
    return type_map.get(type_name, 'Shape')


def create_validator(step):
    """Create validator object from step data"""
    interaction_tool = step.get('interaction_tool', '')
    correct_answer = step.get('correct_answer')
    
    # Map interaction tools to validator types
    if interaction_tool == 'click_sections':
        return {
            "@type": "SelectSectionsValidator",
            "answer": correct_answer if isinstance(correct_answer, list) else [correct_answer]
        }
    elif interaction_tool == 'click_choice':
        return {
            "@type": "MultipleChoiceValidator",
            "answer": [get_choice_index(step, correct_answer)]
        }
    elif interaction_tool == 'drag_fraction':
        return {
            "@type": "DragFractionValidator",
            "answer": correct_answer
        }
    else:
        # Generic validator
        return {
            "@type": "GenericValidator",
            "answer": correct_answer
        }


def get_choice_index(step, correct_answer):
    """Get the index of the correct answer from choices"""
    choices = step.get('choices', [])
    for idx, choice in enumerate(choices):
        if choice.get('id') == correct_answer:
            return idx
    return 0


def transform_error_path_to_remediations(error_path):
    """Transform error path (L/M/H steps) to Godot remediation format"""
    remediations = []
    
    steps = error_path.get('steps', [])
    
    for step in steps:
        scaffolding = step.get('scaffolding_level', 'light')
        
        # Map scaffolding levels to Godot IDs
        remediation_id_map = {
            'light': 'light',
            'medium': 'medium',
            'heavy': 'heavy'
        }
        
        remediation = {
            "@type": "Remediation",
            "id": remediation_id_map.get(scaffolding, 'light'),
            "step": {
                "@type": "Step",
                "dialogue": step.get('dialogue', '')
            }
        }
        
        # Add visual effects if present
        visual = step.get('visual')
        if visual and visual.get('effects'):
            # Transform effects to Godot events
            effects = visual['effects']
            events = []
            
            for effect in effects:
                event_name = f"{effect.get('type', 'animation')}_{effect.get('animation', 'default')}"
                events.append(f"[event:{event_name}]")
            
            # Prepend events to dialogue
            if events:
                event_str = ' '.join(events)
                remediation['step']['dialogue'] = f"{event_str} {remediation['step']['dialogue']}"
        
        remediations.append(remediation)
    
    return remediations


def test_godot_formatter(remediation_path, output_dir=None, limit=None):
    """
    Test Godot formatter with remediation JSON file
    
    Args:
        remediation_path: Path to remediation JSON file (output from remediation generator)
        output_dir: Optional output directory (auto-generated if not provided)
        limit: Optional limit on number of sequences to process (for testing)
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
        response = input(f"\nProcess all {num_sequences} sequences? (y/n) or enter a number: ").strip().lower()
        
        if response == 'n':
            print("Cancelled by user.")
            return None
        elif response != 'y':
            try:
                custom_limit = int(response)
                if custom_limit > 0 and custom_limit < num_sequences:
                    print(f"⚠️  Processing first {custom_limit} sequences")
                    remediation_data['sequences'] = remediation_data['sequences'][:custom_limit]
                    num_sequences = custom_limit
                elif custom_limit > num_sequences:
                    print(f"⚠️  Requested {custom_limit} but only {num_sequences} available. Processing all.")
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
    # TRANSFORM TO GODOT SCHEMA (using AI)
    # ========================================================================
    print("=" * 70)
    print("TRANSFORMING TO GODOT SCHEMA")
    print("=" * 70)
    
    print(f"\nTransforming {num_sequences} sequences to Godot format (one at a time)...")
    print("  - Adding @type annotations")
    print("  - Flattening steps structure")
    print("  - Mapping validators and remediations")
    print("  - Embedding visual effects as [event:...] tags")
    print("  - Formatting fractions with [fraction] tags")
    print("  - Formatting vocabulary with [vocab] tags\n")
    
    # Get vocabulary terms for formatting
    vocabulary_list = format_vocabulary_list_for_prompt()
    
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
        
        # Build prompt
        godot_prompt = builder.build_prompt(
            prompt_id="godot_formatter",
            variables={
                "remediation_context": json.dumps(single_sequence_data, indent=2),
                "vocabulary_terms": vocabulary_list
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
        with open(f"{output_dir}/godot_{sequence.get('problem_id')}_raw.txt", "w", encoding="utf-8") as f:
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
            "problem_id": seq.get('problem_id'),
            "steps": [],
            "issues": []
        }
        
        print(f"\n  Sequence {idx} (Problem ID: {seq.get('problem_id')}):")
        
        steps = seq.get('steps', [])
        print(f"    - Total steps: {len(steps)}")
        
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
                    if 'id' not in rem or rem['id'] not in ['light', 'medium', 'heavy']:
                        seq_validation['issues'].append(f"Step {step_idx}, Remediation {rem_idx}: Invalid id")
            
            elif has_dialogue:
                dialogue_steps += 1
                print(f"      Step {step_idx}: Dialogue only ✓")
        
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
    print(f"  - {output_dir}/godot_raw.txt")
    print(f"  - {output_dir}/godot_sequences.json ← Godot-processable format")
    print(f"  - {output_dir}/validation_report.json")
    
    print("\n📊 Godot Schema Features:")
    print("  ✓ @type annotations for all objects (Godot type system)")
    print("  ✓ Flattened steps[] array (no nesting)")
    print("  ✓ Workspace with tangibles array")
    print("  ✓ Prompt with validator and remediations")
    print("  ✓ Remediations with id: light/medium/heavy")
    print("  ✓ Visual effects embedded in dialogue as [event:...] tags")
    print("  ✓ Fractions formatted with [fraction numerator=N denominator=D] BBCode")
    print("  ✓ Vocabulary terms wrapped with [vocab][/vocab] tags")
    
    print("\n" + "=" * 70)
    
    return godot_output_path


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Godot Formatter with remediation JSON')
    parser.add_argument('remediation_path', help='Path to remediation JSON file (from remediation generator)')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    parser.add_argument('-n', '--limit', type=int, help='Limit number of sequences to process (for testing)', default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.remediation_path):
        print(f"✗ Error: Remediation file not found: {args.remediation_path}")
        sys.exit(1)
    
    test_godot_formatter(args.remediation_path, args.output, args.limit)


if __name__ == "__main__":
    main()
