"""
Test Complete Pipeline Flow
Tests: Questions → Sequences → Remediation → Formatter

This tests the entire pipeline with actual Claude API calls to verify:
1. Question generation from learning goals
2. Sequence generation (main flow + success path, NO error paths)
3. Remediation generation (ADDS error paths to sequences)
4. Final formatting
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder

# Add inputs directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'inputs'))
from modules import MODULES

print("=" * 70)
print("COMPLETE PIPELINE FLOW TEST")
print("=" * 70)

# ============================================================================
# USER INPUT: SELECT MODULE
# ============================================================================
print("\nAvailable Modules:")
for module_id, module in MODULES.items():
    print(f"  {module_id}. {module['module_name']} (Grade {module['grade_level']})")

print("\nSelect module number:")
module_choice = int(input("> ").strip())

if module_choice not in MODULES:
    print(f"Invalid choice. Defaulting to Module 1")
    module_choice = 1

selected_module = MODULES[module_choice]
print(f"\n✓ Selected: Module {module_choice} - {selected_module['module_name']}")

# Show learning goals
print("\nLearning Goals:")
for i, goal in enumerate(selected_module['learning_goals'], 1):
    print(f"  {i}. {goal}")

print("\nHow many questions per learning goal? (1-5)")
print("Enter a single number or range (e.g., '2' or '2-3'):")
num_questions_input = input("> ").strip()
if not num_questions_input:
    num_questions_input = "2-3"
    print(f"Using default: {num_questions_input}")

# Create output directory
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"outputs/flow_test_module{module_choice}_{timestamp}"
os.makedirs(output_dir, exist_ok=True)
print(f"\nOutput directory: {output_dir}\n")

# Initialize
client = ClaudeClient()
builder = PromptBuilder()

# ============================================================================
# BUILD LEARNING GOALS FROM SELECTED MODULE
# ============================================================================
print("\n" + "=" * 70)
print("BUILDING LEARNING GOALS CONTEXT")
print("=" * 70)

# Build learning goals context from selected module
learning_goals = f"""
Module: {selected_module['module_name']}
Grade: {selected_module['grade_level']}
Path Variant: {selected_module['path_variant']}

Learning Goals:
"""
for i, goal in enumerate(selected_module['learning_goals'], 1):
    learning_goals += f"{i}. {goal}\n"

learning_goals += f"\nVocabulary: {', '.join([v['term'] if isinstance(v, dict) else v for v in selected_module['vocabulary']])}\n"

learning_goals += f"\nCore Concepts: {', '.join(selected_module['core_concepts'])}\n"

if 'goals' in selected_module and selected_module['goals']:
    learning_goals += "\nDetailed Goals:\n"
    for goal in selected_module['goals']:
        learning_goals += f"- {goal['text']}\n"

print(f"✓ Generated learning goals context ({len(learning_goals)} characters)")
print(f"\nPreview:")
print(learning_goals[:500])
if len(learning_goals) > 500:
    print(f"... ({len(learning_goals) - 500} more characters)")

# ============================================================================
# STEP 1: QUESTION GENERATOR
# ============================================================================
print("\n" + "=" * 70)
print("STEP 1: QUESTION GENERATOR")
print("=" * 70)

questions_prompt = builder.build_prompt(
    prompt_id="question_generator",
    variables={
        "learning_goals": learning_goals,
        "num_questions": num_questions_input
    }
)

print(f"Prompt length: {len(questions_prompt)} characters")
print("\nCalling Claude API for question generation...")

questions_response = client.generate(questions_prompt, max_tokens=4000, temperature=0.7)

# Save raw response
with open(f"{output_dir}/1_questions_raw.txt", "w", encoding="utf-8") as f:
    f.write(questions_response)

# Extract and save JSON
if "```json" in questions_response:
    json_start = questions_response.find("```json") + 7
    json_end = questions_response.find("```", json_start)
    if json_end == -1:  # No closing fence found
        print("⚠️ Warning: No closing markdown fence found, using entire response")
        questions_json = questions_response[json_start:].strip()
    else:
        questions_json = questions_response[json_start:json_end].strip()
else:
    questions_json = questions_response.strip()

try:
    questions_data = json.loads(questions_json)
    
    with open(f"{output_dir}/1_questions.json", "w", encoding="utf-8") as f:
        json.dump(questions_data, f, indent=2)
    
    print(f"✓ Generated {len(questions_data.get('questions', []))} questions")
    print(f"✓ Saved to {output_dir}/1_questions.json")
except json.JSONDecodeError as e:
    print(f"✗ JSON parsing error: {e}")
    print(f"✗ Raw response saved to {output_dir}/1_questions_raw.txt")
    print(f"✗ Cannot continue to next steps without valid JSON")
    print("\nExiting...")
    exit(1)

with open(f"{output_dir}/1_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions_data, f, indent=2)

print(f"✓ Generated {len(questions_data.get('questions', []))} questions")
print(f"✓ Saved to {output_dir}/1_questions.json")

# Show sample question
if questions_data.get('questions'):
    sample = questions_data['questions'][0]
    print(f"\nSample Question:")
    print(f"  ID: {sample.get('id')}")
    print(f"  Difficulty: {sample.get('difficulty')}")
    print(f"  Verb: {sample.get('verb')}")
    print(f"  Goal: {sample.get('goal')}")

# ============================================================================
# STEP 2: INTERACTION DESIGNER (Sequence Generator)
# ============================================================================
print("\n" + "=" * 70)
print("STEP 2: INTERACTION DESIGNER (SEQUENCE GENERATOR)")
print("=" * 70)

# Use the generated questions as input
sequences_prompt = builder.build_prompt(
    prompt_id="interaction_designer",
    variables={"learning_goals_data": json.dumps(questions_data, indent=2)}
)

print(f"Prompt length: {len(sequences_prompt)} characters")
print("\nCalling Claude API for sequence generation...")

sequences_response = client.generate(sequences_prompt, max_tokens=8000, temperature=0.7)

# Save raw response
with open(f"{output_dir}/2_sequences_raw.txt", "w", encoding="utf-8") as f:
    f.write(sequences_response)

# Extract and save JSON
if "```json" in sequences_response:
    json_start = sequences_response.find("```json") + 7
    json_end = sequences_response.find("```", json_start)
    sequences_json = sequences_response[json_start:json_end].strip()
else:
    sequences_json = sequences_response.strip()

sequences_data = json.loads(sequences_json)

with open(f"{output_dir}/2_sequences.json", "w", encoding="utf-8") as f:
    json.dump(sequences_data, f, indent=2)

print(f"✓ Generated {len(sequences_data.get('sequences', []))} sequences")
print(f"✓ Saved to {output_dir}/2_sequences.json")

# Validate sequence structure
if sequences_data.get('sequences'):
    sample_seq = sequences_data['sequences'][0]
    print(f"\nSample Sequence:")
    print(f"  Problem ID: {sample_seq.get('problem_id')}")
    print(f"  Verb: {sample_seq.get('verb')}")
    print(f"  Steps: {len(sample_seq.get('steps', []))} steps")
    print(f"  Valid Visual: {len(sample_seq.get('valid_visual', []))} visuals")
    
    # Check for error paths (should be NONE at this stage)
    student_attempts = sample_seq.get('student_attempts', {})
    has_success = 'success_path' in student_attempts
    error_paths = [k for k in student_attempts.keys() if k.startswith('error_path')]
    
    print(f"  Has success_path: {has_success} ✓" if has_success else "  Has success_path: False ✗")
    print(f"  Error paths: {len(error_paths)} (should be 0 at this stage)")
    
    if error_paths:
        print("  ⚠️ WARNING: Sequence generator added error paths (should NOT)")
    else:
        print("  ✓ Sequence generator correctly did NOT add error paths")

# ============================================================================
# STEP 3: REMEDIATION GENERATOR
# ============================================================================
print("\n" + "=" * 70)
print("STEP 3: REMEDIATION GENERATOR")
print("=" * 70)

# Use the generated sequences as input
remediation_prompt = builder.build_prompt(
    prompt_id="remediation_generator",
    variables={"interactions_context": json.dumps(sequences_data, indent=2)}
)

print(f"Prompt length: {len(remediation_prompt)} characters")
print("\nCalling Claude API for remediation generation...")

remediation_response = client.generate(remediation_prompt, max_tokens=8000, temperature=0.7)

# Save raw response
with open(f"{output_dir}/3_remediation_raw.txt", "w", encoding="utf-8") as f:
    f.write(remediation_response)

# Extract and save JSON
if "```json" in remediation_response:
    json_start = remediation_response.find("```json") + 7
    json_end = remediation_response.find("```", json_start)
    remediation_json = remediation_response[json_start:json_end].strip()
else:
    remediation_json = remediation_response.strip()

try:
    remediation_data = json.loads(remediation_json)
    
    with open(f"{output_dir}/3_remediation.json", "w", encoding="utf-8") as f:
        json.dump(remediation_data, f, indent=2)
    
    print(f"✓ Added error paths to {len(remediation_data.get('sequences', []))} sequences")
    print(f"✓ Saved to {output_dir}/3_remediation.json")
    
    # Validate remediation structure
    if remediation_data.get('sequences'):
        sample_rem = remediation_data['sequences'][0]
        print(f"\nSample Remediation:")
        print(f"  Problem ID: {sample_rem.get('problem_id')}")
        print(f"  Verb: {sample_rem.get('verb')}")
        
        student_attempts = sample_rem.get('student_attempts', {})
        has_success = 'success_path' in student_attempts
        error_paths = [k for k in student_attempts.keys() if k.startswith('error_path')]
        
        print(f"  Has success_path: {has_success} ✓" if has_success else "  Has success_path: False ✗")
        print(f"  Error paths: {len(error_paths)}")
        
        if error_paths:
            print(f"  ✓ Error paths added: {', '.join(error_paths)}")
            
            # Check first error path structure
            first_error = student_attempts[error_paths[0]]
            if 'steps' in first_error:
                steps = first_error['steps']
                print(f"  ✓ Error path has 'steps' array with {len(steps)} steps")
                
                if len(steps) == 3:
                    print(f"  ✓ Correct: 3 steps (Light/Medium/Heavy)")
                    
                    # Check each step
                    for i, step in enumerate(steps, 1):
                        has_dialogue = 'dialogue' in step
                        has_visual = 'visual' in step
                        visual_count = len(step.get('visual', []))
                        
                        print(f"    Step {i}: dialogue={has_dialogue}, visual={visual_count} items")
                        
                        # Word count check
                        if has_dialogue:
                            word_count = len(step['dialogue'].split())
                            if i == 1:
                                status = "✓" if 10 <= word_count <= 20 else "⚠️"
                                print(f"      {status} Light: {word_count} words (target: 10-20)")
                            elif i == 2:
                                status = "✓" if 20 <= word_count <= 30 else "⚠️"
                                print(f"      {status} Medium: {word_count} words (target: 20-30)")
                            elif i == 3:
                                status = "✓" if 30 <= word_count <= 60 else "⚠️"
                                print(f"      {status} Heavy: {word_count} words (target: 30-60)")
                else:
                    print(f"  ⚠️ WARNING: Error path has {len(steps)} steps, expected 3")
            else:
                print(f"  ✗ ERROR: Error path missing 'steps' array")
        else:
            print(f"  ✗ ERROR: No error paths added")

except json.JSONDecodeError as e:
    print(f"✗ Invalid JSON: {e}")
    print(f"Saved raw response to {output_dir}/3_remediation_raw.txt")
    remediation_data = None

# ============================================================================
# STEP 4: FORMATTER (Deterministic - converts JSON to Markdown)
# ============================================================================
print("\n" + "=" * 70)
print("STEP 4: FORMATTER (DETERMINISTIC)")
print("=" * 70)

if remediation_data:
    # Use the ScriptFormatter class
    from steps.script_formatter import ScriptFormatter
    
    formatter = ScriptFormatter()
    
    # Format the sequences
    result = formatter.execute(remediation_data, run_folder=output_dir)
    
    # Save the combined script
    combined_script = result.get("combined_script", "")
    script_path = f"{output_dir}/4_script.md"
    
    # Add module header
    header = f"""# Interactive Learning Script

**Module:** {selected_module['module_name']}
**Grade:** {selected_module['grade_level']}

{'=' * 80}

"""
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(header + combined_script)
    
    print(f"✓ Saved to {output_dir}/4_script.md")
else:
    print("⚠️ Skipping formatter - no remediation data available")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("FLOW TEST SUMMARY")
print("=" * 70)
print(f"\nAll outputs saved to: {output_dir}/")
print("\nFiles generated:")
print("  1. 1_questions_raw.txt - Raw Claude response for questions")
print("  2. 1_questions.json - Parsed questions JSON (with goal_id)")
print("  3. 2_sequences_raw.txt - Raw Claude response for sequences")
print("  4. 2_sequences.json - Parsed sequences JSON (NO error paths)")
print("  5. 3_remediation_raw.txt - Raw Claude response for remediation")
print("  6. 3_remediation.json - Parsed remediation JSON (WITH error paths)")
print("  7. 4_script.md - Human-readable markdown script (FINAL OUTPUT)")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
