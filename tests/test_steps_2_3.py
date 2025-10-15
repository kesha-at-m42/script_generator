"""Test Steps 2-3: Questions → Sequences → Scripts (using questions.json)"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.sequence_generator import SequenceGenerator
from steps.script_formatter import ScriptFormatter

print("Testing Steps 2-3 Pipeline: Questions → Sequences → Scripts\n")
print("Step 2: Sequence Generator (AI)")
print("Step 3: Script Formatter (No AI - Pure formatting)\n")

# Load questions from questions.json
questions_file = Path(__file__).parent.parent / "inputs" / "examples" / "questions.json"

if not questions_file.exists():
    print(f"❌ Questions file not found: {questions_file}")
    sys.exit(1)

with open(questions_file, 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"📖 Loaded {len(questions)} questions from {questions_file.name}\n")

# Format as input for SequenceGenerator (Step 2)
# Step 2 expects output from Step 1 which has {"metadata": {...}, "questions": [...]}
input_data = {
    "metadata": {
        "total_questions": len(questions),
        "source": "questions.json"
    },
    "questions": questions
}

client = ClaudeClient()

# Create pipeline with steps 2 and 3
pipeline = Pipeline("questions_to_script", save_intermediate=True)
pipeline.add_step(SequenceGenerator(client))
pipeline.add_step(ScriptFormatter())

# Execute pipeline
print("=" * 70)
results = pipeline.execute(input_data)
print("=" * 70)

# Get outputs from each step
all_results = pipeline.results
step2_output = all_results[0]['output'] if len(all_results) > 0 else {}
step3_output = all_results[1]['output'] if len(all_results) > 1 else {}

print(f"\n✨ Pipeline finished!")
print(f"\n📁 All files saved in: {pipeline.run_folder}")
print(f"  • sequence_generator_*.json")
print(f"  • script_formatter_*.json")
print(f"  • script_*.md (combined readable script)")

print(f"\n📊 Pipeline Summary:")
print(f"  • Input: {len(questions)} questions from questions.json")
if step2_output.get('sequences'):
    print(f"  • Generated {len(step2_output['sequences'])} interactive sequences")
if step3_output.get('combined_script'):
    total_problems = step3_output.get('total_problems', 0)
    print(f"  • Formatted as 1 combined script with {total_problems} problems")

# Show preview of combined script
combined_script = step3_output.get('combined_script', '')
if combined_script:
    print(f"\n🎯 Script Preview:")
    print("=" * 70)
    print(combined_script[:1000])
    print("...")
    print("=" * 70)

stats = client.get_stats()
print(f"\n💰 Token Usage: {stats['total_tokens']} tokens")
print(f"  • Step 2 (Sequences): ~{stats['total_tokens']} tokens")
print(f"  • Step 3 (Scripts):   0 tokens (no AI)")

print(f"\n✅ Complete! Check {pipeline.run_folder}/script_*.md for the full script.")
