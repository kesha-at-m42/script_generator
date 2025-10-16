"""
Retry Remediation - Process One Sequence at a Time
To avoid token limits, processes each sequence individually
"""

import json
import os
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder
from steps.script_formatter import ScriptFormatter

# Specify the output directory from the previous run
output_dir = "outputs/flow_test_module1_20251016_172640"

print("=" * 70)
print("RETRY: REMEDIATION (ONE AT A TIME) + FORMATTER")
print("=" * 70)
print(f"Using output directory: {output_dir}\n")

# Load the sequences from step 2
sequences_file = f"{output_dir}/2_sequences.json"
with open(sequences_file, 'r', encoding='utf-8') as f:
    sequences_data = json.load(f)

sequences = sequences_data.get('sequences', [])
print(f"✓ Loaded {len(sequences)} sequences from Step 2")

# Initialize
client = ClaudeClient()
builder = PromptBuilder()

# ============================================================================
# STEP 3: REMEDIATION GENERATOR (ONE AT A TIME)
# ============================================================================
print("\n" + "=" * 70)
print("STEP 3: REMEDIATION GENERATOR (PROCESSING INDIVIDUALLY)")
print("=" * 70)

processed_sequences = []

for i, sequence in enumerate(sequences, 1):
    print(f"\nProcessing sequence {i}/{len(sequences)} (Problem {sequence.get('problem_id')})...")
    
    # Create input with just this one sequence
    single_sequence_input = {"sequences": [sequence]}
    
    remediation_prompt = builder.build_prompt(
        prompt_id="remediation_generator",
        variables={"interactions_context": json.dumps(single_sequence_input, indent=2)}
    )
    
    print(f"  Prompt length: {len(remediation_prompt)} characters")
    print(f"  Calling Claude API...")
    
    remediation_response = client.generate(remediation_prompt, max_tokens=8192, temperature=0.7)
    
    # Extract JSON
    if "```json" in remediation_response:
        json_start = remediation_response.find("```json") + 7
        json_end = remediation_response.find("```", json_start)
        if json_end == -1:
            remediation_json = remediation_response[json_start:].strip()
        else:
            remediation_json = remediation_response[json_start:json_end].strip()
    else:
        remediation_json = remediation_response.strip()
    
    try:
        remediation_result = json.loads(remediation_json)
        
        # Extract the sequence (should be in a 'sequences' array)
        if 'sequences' in remediation_result and len(remediation_result['sequences']) > 0:
            processed_sequence = remediation_result['sequences'][0]
            processed_sequences.append(processed_sequence)
            
            # Validate
            student_attempts = processed_sequence.get('student_attempts', {})
            error_paths = [k for k in student_attempts.keys() if k.startswith('error_path')]
            
            print(f"  ✓ Success! Added {len(error_paths)} error paths")
        else:
            print(f"  ✗ Error: No sequences in result")
            processed_sequences.append(sequence)  # Keep original
    
    except json.JSONDecodeError as e:
        print(f"  ✗ Invalid JSON: {e}")
        print(f"  Keeping original sequence without error paths")
        processed_sequences.append(sequence)  # Keep original

# Combine all processed sequences
remediation_data = {"sequences": processed_sequences}

# Save combined result
with open(f"{output_dir}/3_remediation_individual.json", "w", encoding="utf-8") as f:
    json.dump(remediation_data, f, indent=2)

print(f"\n✓ Processed all {len(processed_sequences)} sequences")
print(f"✓ Saved to {output_dir}/3_remediation_individual.json")

# Show summary
total_error_paths = 0
for seq in processed_sequences:
    error_paths = [k for k in seq.get('student_attempts', {}).keys() if k.startswith('error_path')]
    total_error_paths += len(error_paths)

print(f"\nSummary:")
print(f"  Total sequences: {len(processed_sequences)}")
print(f"  Total error paths: {total_error_paths}")

# ============================================================================
# STEP 4: FORMATTER (Deterministic)
# ============================================================================
print("\n" + "=" * 70)
print("STEP 4: FORMATTER (DETERMINISTIC)")
print("=" * 70)

# Use the ScriptFormatter class
formatter = ScriptFormatter()

# Format the sequences
result = formatter.execute(remediation_data, run_folder=output_dir)

# Save the combined script with header
combined_script = result.get("combined_script", "")
script_path = f"{output_dir}/4_script_individual.md"

# Add module header
header = f"""# Interactive Learning Script

**Module:** Introduction to Fractions
**Grade:** 3

{'=' * 80}

"""

with open(script_path, "w", encoding="utf-8") as f:
    f.write(header + combined_script)

print(f"✓ Saved markdown script to {output_dir}/4_script_individual.md")

# Show token usage
stats = client.get_stats()
print(f"\n📊 API Usage:")
print(f"  Input tokens: {stats['total_input_tokens']:,}")
print(f"  Output tokens: {stats['total_output_tokens']:,}")
print(f"  Total tokens: {stats['total_input_tokens'] + stats['total_output_tokens']:,}")

print("\n" + "=" * 70)
print("RETRY COMPLETE")
print("=" * 70)
print(f"\nFiles generated:")
print(f"  1. 3_remediation_individual.json - Remediation JSON (processed individually)")
print(f"  2. 4_script_individual.md - Final markdown script ✨")
