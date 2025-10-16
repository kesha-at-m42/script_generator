"""
Retry Remediation and Formatter Steps
Uses existing sequences from a previous run
"""

import json
import os
from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder
from steps.script_formatter import ScriptFormatter

# Specify the output directory from the previous run
output_dir = "outputs/flow_test_module1_20251016_172640"

print("=" * 70)
print("RETRY: REMEDIATION + FORMATTER")
print("=" * 70)
print(f"Using output directory: {output_dir}\n")

# Load the sequences from step 2
sequences_file = f"{output_dir}/2_sequences.json"
with open(sequences_file, 'r', encoding='utf-8') as f:
    sequences_data = json.load(f)

print(f"✓ Loaded {len(sequences_data.get('sequences', []))} sequences from Step 2")

# Initialize
client = ClaudeClient()
builder = PromptBuilder()

# ============================================================================
# STEP 3: REMEDIATION GENERATOR
# ============================================================================
print("\n" + "=" * 70)
print("STEP 3: REMEDIATION GENERATOR (RETRY)")
print("=" * 70)

remediation_prompt = builder.build_prompt(
    prompt_id="remediation_generator",
    variables={"interactions_context": json.dumps(sequences_data, indent=2)}
)

print(f"Prompt length: {len(remediation_prompt)} characters")
print("\nCalling Claude API for remediation generation...")
print("Using max_tokens=64000 (actual model maximum)")

remediation_response = client.generate(remediation_prompt, max_tokens=64000, temperature=0.7)

# Print token usage
stats = client.get_stats()
print(f"\n📊 Token Usage:")
print(f"   Input:  {stats['input_tokens']:,} tokens")
print(f"   Output: {stats['output_tokens']:,} tokens")
print(f"   Total:  {stats['total_tokens']:,} tokens")

# Save raw response
with open(f"{output_dir}/3_remediation_raw_retry.txt", "w", encoding="utf-8") as f:
    f.write(remediation_response)

# Extract and save JSON
if "```json" in remediation_response:
    json_start = remediation_response.find("```json") + 7
    json_end = remediation_response.find("```", json_start)
    if json_end == -1:
        print("⚠️ Warning: No closing markdown fence found, using entire response")
        remediation_json = remediation_response[json_start:].strip()
    else:
        remediation_json = remediation_response[json_start:json_end].strip()
else:
    remediation_json = remediation_response.strip()

try:
    remediation_data = json.loads(remediation_json)
    
    with open(f"{output_dir}/3_remediation_retry.json", "w", encoding="utf-8") as f:
        json.dump(remediation_data, f, indent=2)
    
    print(f"✓ Added error paths to {len(remediation_data.get('sequences', []))} sequences")
    print(f"✓ Saved to {output_dir}/3_remediation_retry.json")
    
    # Validate structure
    if remediation_data.get('sequences'):
        sample = remediation_data['sequences'][0]
        student_attempts = sample.get('student_attempts', {})
        error_paths = [k for k in student_attempts.keys() if k.startswith('error_path')]
        
        print(f"\nValidation:")
        print(f"  Problem ID: {sample.get('problem_id')}")
        print(f"  Success path: {'✓' if 'success_path' in student_attempts else '✗'}")
        print(f"  Error paths: {len(error_paths)} ({', '.join(error_paths)})")
        
        if error_paths:
            first_error = student_attempts[error_paths[0]]
            steps = first_error.get('steps', [])
            print(f"  First error path: {len(steps)} steps")
            
            if len(steps) == 3:
                print(f"  ✓ Correct: 3 steps (Light/Medium/Heavy)")
                for i, step in enumerate(steps, 1):
                    dialogue = step.get('dialogue', '')
                    word_count = len(dialogue.split())
                    visuals = len(step.get('visual', []))
                    print(f"    Step {i}: {word_count} words, {visuals} visuals")

except json.JSONDecodeError as e:
    print(f"✗ Invalid JSON: {e}")
    print(f"Saved raw response to {output_dir}/3_remediation_raw_retry.txt")
    print("\nShowing error location:")
    
    # Show the error location
    lines = remediation_json.split('\n')
    error_line = int(str(e).split('line ')[1].split(' ')[0]) if 'line' in str(e) else 0
    
    if error_line > 0:
        start = max(0, error_line - 3)
        end = min(len(lines), error_line + 2)
        print(f"\nLines {start+1}-{end+1}:")
        for i in range(start, end):
            marker = ">>>" if i == error_line - 1 else "   "
            print(f"{marker} {i+1}: {lines[i]}")
    
    remediation_data = None
    print("\nExiting...")
    exit(1)

# ============================================================================
# STEP 4: FORMATTER (Deterministic)
# ============================================================================
print("\n" + "=" * 70)
print("STEP 4: FORMATTER (DETERMINISTIC)")
print("=" * 70)

if remediation_data:
    # Use the ScriptFormatter class
    formatter = ScriptFormatter()
    
    # Format the sequences
    result = formatter.execute(remediation_data, run_folder=output_dir)
    
    # Save the combined script with header
    combined_script = result.get("combined_script", "")
    script_path = f"{output_dir}/4_script_retry.md"
    
    # Add module header
    header = f"""# Interactive Learning Script

**Module:** Introduction to Fractions
**Grade:** 3

{'=' * 80}

"""
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(header + combined_script)
    
    print(f"✓ Saved markdown script to {output_dir}/4_script_retry.md")
else:
    print("⚠️ Skipping formatter - no remediation data available")

print("\n" + "=" * 70)
print("RETRY COMPLETE")
print("=" * 70)
print(f"\nFiles generated:")
print(f"  1. 3_remediation_raw_retry.txt - Raw Claude response")
print(f"  2. 3_remediation_retry.json - Parsed remediation JSON")
print(f"  3. 4_script_retry.md - Final markdown script")
