"""
Process sequences individually through remediation
This avoids token limit issues by processing one sequence at a time
"""

import json
import os
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder
from steps.script_formatter import ScriptFormatter

# Specify the output directory from the previous run
output_dir = "outputs/flow_test_module1_20251016_172640"

print("=" * 70)
print("INDIVIDUAL SEQUENCE PROCESSING")
print("=" * 70)
print(f"Using output directory: {output_dir}\n")

# Load the sequences from step 2
sequences_file = f"{output_dir}/2_sequences.json"
with open(sequences_file, 'r', encoding='utf-8') as f:
    sequences_data = json.load(f)

sequences = sequences_data.get('sequences', [])
print(f"✓ Loaded {len(sequences)} sequences from Step 2\n")

# Initialize
client = ClaudeClient()
builder = PromptBuilder()

# Process each sequence individually
all_remediated_sequences = []

for i, sequence in enumerate(sequences, 1):
    print("=" * 70)
    print(f"PROCESSING SEQUENCE {i}/{len(sequences)}")
    print("=" * 70)
    print(f"Problem ID: {sequence.get('problem_id')}")
    print(f"Verb: {sequence.get('verb')}")
    print(f"Goal: {sequence.get('goal')}")
    print("")
    
    # Create single-sequence input
    single_sequence_input = {
        "sequences": [sequence]
    }
    
    # Build prompt for this one sequence
    remediation_prompt = builder.build_prompt(
        prompt_id="remediation_generator",
        variables={"interactions_context": json.dumps(single_sequence_input, indent=2)}
    )
    
    print(f"Prompt length: {len(remediation_prompt)} characters")
    print("Calling Claude API...")
    
    # Call Claude with high token limit for single sequence
    remediation_response = client.generate(remediation_prompt, max_tokens=4096, temperature=0.7)
    
    # Save individual raw response
    with open(f"{output_dir}/3_remediation_seq{i}_raw.txt", "w", encoding="utf-8") as f:
        f.write(remediation_response)
    
    # Extract JSON
    if "```json" in remediation_response:
        json_start = remediation_response.find("```json") + 7
        json_end = remediation_response.find("```", json_start)
        if json_end == -1:
            print("⚠️ Warning: No closing fence, using entire response")
            remediation_json = remediation_response[json_start:].strip()
        else:
            remediation_json = remediation_response[json_start:json_end].strip()
    else:
        remediation_json = remediation_response.strip()
    
    try:
        remediation_result = json.loads(remediation_json)
        
        # Extract the remediated sequence
        remediated_seqs = remediation_result.get('sequences', [])
        if remediated_seqs:
            remediated_seq = remediated_seqs[0]
            all_remediated_sequences.append(remediated_seq)
            
            # Validate
            student_attempts = remediated_seq.get('student_attempts', {})
            error_paths = [k for k in student_attempts.keys() if k.startswith('error_path')]
            
            print(f"✓ Success path: {'Yes' if 'success_path' in student_attempts else 'No'}")
            print(f"✓ Error paths added: {len(error_paths)}")
            
            if error_paths:
                for ep_name in error_paths:
                    ep = student_attempts[ep_name]
                    steps = ep.get('steps', [])
                    print(f"  - {ep_name}: {len(steps)} steps")
                    
                    if len(steps) == 3:
                        for j, step in enumerate(steps, 1):
                            word_count = len(step.get('dialogue', '').split())
                            visuals = len(step.get('visual', []))
                            print(f"    Step {j}: {word_count} words, {visuals} visuals")
            
            print(f"✓ Saved to {output_dir}/3_remediation_seq{i}_raw.txt")
        else:
            print("✗ No sequences in response")
            
    except json.JSONDecodeError as e:
        print(f"✗ JSON Error: {e}")
        print(f"Saved raw response to {output_dir}/3_remediation_seq{i}_raw.txt")
        print("\nSkipping this sequence...")
    
    print("")

# ============================================================================
# COMBINE ALL REMEDIATED SEQUENCES
# ============================================================================
print("=" * 70)
print("COMBINING RESULTS")
print("=" * 70)

combined_result = {
    "sequences": all_remediated_sequences
}

# Save combined result
with open(f"{output_dir}/3_remediation_combined.json", "w", encoding="utf-8") as f:
    json.dump(combined_result, f, indent=2)

print(f"✓ Combined {len(all_remediated_sequences)} remediated sequences")
print(f"✓ Saved to {output_dir}/3_remediation_combined.json")

# ============================================================================
# STEP 4: FORMATTER
# ============================================================================
print("\n" + "=" * 70)
print("STEP 4: FORMATTER (DETERMINISTIC)")
print("=" * 70)

if all_remediated_sequences:
    formatter = ScriptFormatter()
    
    # Format the sequences
    result = formatter.execute(combined_result, run_folder=output_dir)
    
    # Save the combined script
    combined_script = result.get("combined_script", "")
    script_path = f"{output_dir}/4_script_final.md"
    
    header = f"""# Interactive Learning Script

**Module:** Introduction to Fractions
**Grade:** 3

{'=' * 80}

"""
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(header + combined_script)
    
    print(f"✓ Generated markdown script")
    print(f"✓ Saved to {output_dir}/4_script_final.md")
else:
    print("⚠️ No sequences to format")

print("\n" + "=" * 70)
print("PROCESSING COMPLETE")
print("=" * 70)
print(f"\nFiles generated:")
print(f"  Individual raw responses: 3_remediation_seq1_raw.txt, seq2_raw.txt, seq3_raw.txt")
print(f"  Combined JSON: 3_remediation_combined.json")
print(f"  Final script: 4_script_final.md")
