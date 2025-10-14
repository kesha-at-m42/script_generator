"""Test the 3-step pipeline: Questions → Sequences → Scripts"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.question_generator import QuestionGenerator
from steps.sequence_generator import SequenceGenerator
from steps.script_formatter import ScriptFormatter

print("Testing 3-Step Pipeline: Questions → Sequences → Scripts\n")
print("Step 1: Question Generator (AI)")
print("Step 2: Sequence Generator (AI)")
print("Step 3: Script Formatter (No AI - Pure formatting)\n")

client = ClaudeClient()

# Create pipeline with all 3 steps
pipeline = Pipeline("questions_sequences_scripts", save_intermediate=True)
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(SequenceGenerator(client))
pipeline.add_step(ScriptFormatter())

# Input: Learning goals
learning_goals = """
- Students can partition shapes into equal parts
- Students can identify unit fractions
""".strip()

# Execute full pipeline
print("=" * 70)
results = pipeline.execute(
    {
        "learning_goals": learning_goals,
        "num_questions": 3,
        "grade_level": 3,
        "questions_per_goal": 3  # For step 2
    }
)
print("=" * 70)

# Get outputs from each step
all_results = pipeline.results
step1_output = all_results[0]['output'] if len(all_results) > 0 else {}
step2_output = all_results[1]['output'] if len(all_results) > 1 else {}
step3_output = all_results[2]['output'] if len(all_results) > 2 else {}

print(f"\n✨ Complete pipeline finished!")
print(f"\n📁 All files saved in: {pipeline.run_folder}")
print(f"  • question_generator_*.json")
print(f"  • sequence_generator_*.json")
print(f"  • script_formatter_*.json")
print(f"  • script_*.md (combined readable script)")

print(f"\n📊 Pipeline Summary:")
if step1_output.get('questions'):
    print(f"  • Generated {len(step1_output['questions'])} questions")
if step2_output.get('sequences'):
    print(f"  • Converted to {len(step2_output['sequences'])} interactive sequences")
if step3_output.get('combined_script'):
    total_problems = step3_output.get('total_problems', 0)
    print(f"  • Formatted as 1 combined script with {total_problems} problems")

# Show preview of combined script
combined_script = step3_output.get('combined_script', '')
if combined_script:
    print(f"\n🎯 Script Preview:")
    print("=" * 70)
    print(combined_script[:800])
    print("...")
    print("=" * 70)

stats = client.get_stats()
print(f"\n💰 Token Usage: {stats['total_tokens']} tokens")
print(f"  • Step 1 (Questions): ~1,500-2,000 tokens")
print(f"  • Step 2 (Sequences): ~6,000-8,000 tokens")
print(f"  • Step 3 (Scripts):   0 tokens (no AI)")

print(f"\n✅ Complete! Check outputs/scripts/ folder for readable markdown scripts.")
