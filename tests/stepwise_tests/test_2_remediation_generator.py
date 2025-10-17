"""
Stepwise Test 2: Remediation Generator
Takes a sequences JSON file and adds error paths with scaffolding_level, workspace_context, visual schema
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

def test_remediation_generator(sequences_path, output_dir=None):
    """
    Test remediation generator with sequences from a JSON file
    
    Args:
        sequences_path: Path to sequences JSON file (output from interaction designer)
        output_dir: Optional output directory (auto-generated if not provided)
    """
    print("=" * 70)
    print("STEPWISE TEST 2: REMEDIATION GENERATOR")
    print("=" * 70)
    
    # Load sequences
    print(f"\nLoading sequences from: {sequences_path}")
    with open(sequences_path, 'r', encoding='utf-8') as f:
        sequences_data = json.load(f)
    
    num_sequences = len(sequences_data.get('sequences', []))
    print(f"✓ Loaded {num_sequences} sequences")
    
    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_remediation_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder()
    
    # ========================================================================
    # REMEDIATION GENERATOR
    # ========================================================================
    print("=" * 70)
    print("ADDING ERROR PATHS")
    print("=" * 70)
    
    print("\nAdding error paths with scaffolding_level, workspace_context, visual schema...")
    
    remediation_prompt = builder.build_prompt(
        prompt_id="remediation_generator",
        variables={"interactions_context": json.dumps(sequences_data, indent=2)}
    )
    
    print(f"Prompt length: {len(remediation_prompt)} characters")
    print("Calling Claude API...")
    
    remediation_response = client.generate(remediation_prompt, max_tokens=16000, temperature=0.3)
    
    # Save raw response
    with open(f"{output_dir}/remediation_raw.txt", "w", encoding="utf-8") as f:
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
        
        remediation_output_path = f"{output_dir}/remediation.json"
        with open(remediation_output_path, "w", encoding="utf-8") as f:
            json.dump(remediation_data, f, indent=2)
        
        print(f"✓ Added error paths to {len(remediation_data.get('sequences', []))} sequences")
        print(f"✓ Saved to {remediation_output_path}")
        
        # ====================================================================
        # VALIDATE SCHEMA
        # ====================================================================
        print("\n" + "=" * 70)
        print("SCHEMA VALIDATION")
        print("=" * 70)
        
        validation_results = {
            "total_sequences": len(remediation_data.get('sequences', [])),
            "sequences": []
        }
        
        for idx, seq in enumerate(remediation_data.get('sequences', []), 1):
            seq_validation = {
                "sequence_id": idx,
                "problem_id": seq.get('problem_id'),
                "error_paths": [],
                "issues": []
            }
            
            print(f"\n  Sequence {idx} (Problem ID: {seq.get('problem_id')}):")
            
            attempts = seq.get('student_attempts', {})
            error_paths = [k for k in attempts.keys() if k.startswith('error_path')]
            
            print(f"    - Error paths: {len(error_paths)}")
            
            if len(error_paths) == 0:
                seq_validation['issues'].append("No error paths added")
            
            # Check each error path
            for error_path_name in error_paths:
                path_validation = {
                    "name": error_path_name,
                    "num_steps": 0,
                    "step_issues": []
                }
                
                error_path = attempts[error_path_name]
                steps = error_path.get('steps', [])
                path_validation['num_steps'] = len(steps)
                
                print(f"\n    {error_path_name}: {len(steps)} steps")
                
                if len(steps) != 3:
                    path_validation['step_issues'].append(f"Expected 3 steps (L/M/H), got {len(steps)}")
                
                for step_idx, step in enumerate(steps, 1):
                    step_issues = []
                    
                    # Check scaffolding_level
                    has_scaffolding = 'scaffolding_level' in step
                    scaffolding = step.get('scaffolding_level', 'MISSING')
                    expected_scaffolding = ['light', 'medium', 'heavy'][step_idx - 1] if step_idx <= 3 else 'unknown'
                    
                    scaffolding_match = scaffolding == expected_scaffolding
                    print(f"      Step {step_idx}: scaffolding_level={scaffolding} {'✓' if has_scaffolding and scaffolding_match else '✗'}")
                    
                    if not has_scaffolding:
                        step_issues.append("Missing scaffolding_level field")
                    elif not scaffolding_match:
                        step_issues.append(f"Expected {expected_scaffolding}, got {scaffolding}")
                    
                    # Check workspace_context
                    has_context = 'workspace_context' in step
                    print(f"        - workspace_context: {'present' if has_context else 'MISSING'} {'✓' if has_context else '✗'}")
                    
                    if not has_context:
                        step_issues.append("Missing workspace_context field")
                    else:
                        context = step['workspace_context']
                        has_tangibles = 'tangibles_present' in context
                        if not has_tangibles:
                            step_issues.append("workspace_context missing tangibles_present")
                    
                    # Check visual based on scaffolding level
                    visual = step.get('visual')
                    
                    if scaffolding == 'light':
                        correct_visual = visual is None
                        print(f"        - visual is null (light): {correct_visual} {'✓' if correct_visual else '✗'}")
                        if not correct_visual:
                            step_issues.append("Light step should have visual=null")
                    
                    elif scaffolding in ['medium', 'heavy']:
                        has_visual = visual is not None
                        has_effects = has_visual and isinstance(visual, dict) and 'effects' in visual
                        print(f"        - visual has effects: {has_effects} {'✓' if has_effects else '✗'}")
                        
                        if not has_visual:
                            step_issues.append(f"{scaffolding.capitalize()} step should have visual object")
                        elif not has_effects:
                            step_issues.append(f"{scaffolding.capitalize()} visual should have effects array")
                        else:
                            num_effects = len(visual['effects'])
                            print(f"          - {num_effects} effect(s) defined")
                    
                    if step_issues:
                        path_validation['step_issues'].extend([f"Step {step_idx}: {issue}" for issue in step_issues])
                
                if path_validation['step_issues']:
                    seq_validation['issues'].extend(path_validation['step_issues'])
                
                seq_validation['error_paths'].append(path_validation)
            
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
        total_error_paths = sum(len(s['error_paths']) for s in validation_results['sequences'])
        
        print(f"\n✓ Processed {validation_results['total_sequences']} sequences")
        print(f"✓ Added {total_error_paths} error paths")
        print(f"{'✓' if total_issues == 0 else '⚠️'} Total validation issues: {total_issues}")
        
        if total_issues > 0:
            print("\nIssues found:")
            for seq in validation_results['sequences']:
                if seq['issues']:
                    print(f"  Sequence {seq['sequence_id']}:")
                    for issue in seq['issues']:
                        print(f"    - {issue}")
        
        print(f"\nOutput files:")
        print(f"  - {output_dir}/remediation_raw.txt")
        print(f"  - {output_dir}/remediation.json ← Final output with error paths")
        print(f"  - {output_dir}/validation_report.json")
        
        print("\n📊 Expected Schema:")
        print("  ✓ scaffolding_level: 'light'|'medium'|'heavy' at step level")
        print("  ✓ workspace_context: Metadata with tangibles_present array")
        print("  ✓ visual: null for light, object with effects for medium/heavy")
        print("  ✓ visual.effects: Array of effect objects (target, type, animation, description)")
        print("  ✓ 3 steps per error path: light → medium → heavy")
        
        print("\n" + "=" * 70)
        
        return remediation_output_path
        
    except json.JSONDecodeError as e:
        print(f"\n✗ JSON parsing error: {e}")
        print(f"✗ Raw response saved to {output_dir}/remediation_raw.txt")
        print(f"✗ Check the raw response for syntax errors")
        return None

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Remediation Generator with sequences JSON')
    parser.add_argument('sequences_path', help='Path to sequences JSON file (from interaction designer)')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.sequences_path):
        print(f"✗ Error: Sequences file not found: {args.sequences_path}")
        sys.exit(1)
    
    test_remediation_generator(args.sequences_path, args.output)

if __name__ == "__main__":
    main()
