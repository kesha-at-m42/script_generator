"""Complete 6-Step Pipeline: Module → Questions → Interactions → Validation → Dialogue → Scripts"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.module_loader import ModuleLoader
from steps.question_generator import QuestionGenerator
from steps.interaction_designer import InteractionDesigner
from steps.validation_designer import ValidationDesigner
from steps.dialogue_writer import DialogueWriter
from steps.script_formatter import ScriptFormatter

print("Testing Complete 6-Step Pipeline:\n")
print("Step 1: Module Loader (loads learning goals from module number)")
print("Step 2: Question Generator (AI)")
print("Step 3: Interaction Designer (AI - visuals/mechanics)")
print("Step 4: Validation Designer (AI - error types/scaffolding)")
print("Step 5: Dialogue Writer (AI - character voice)")
print("Step 6: Script Formatter (No AI - Pure formatting)\n")

client = ClaudeClient()

# Create pipeline with all 6 steps
pipeline = Pipeline("module_to_script", save_intermediate=True)
pipeline.add_step(ModuleLoader())
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(InteractionDesigner(client))
pipeline.add_step(ValidationDesigner(client))
pipeline.add_step(DialogueWriter(client))
pipeline.add_step(ScriptFormatter())

# Input: Just a module number!
module_number = 1
num_questions = 5

print("=" * 70)
results = pipeline.execute(
    {
        "module_number": module_number,
        "num_questions": num_questions
    }
)
print("=" * 70)

# Get outputs from each step
all_results = pipeline.results
step1_output = all_results[0]['output'] if len(all_results) > 0 else {}
step2_output = all_results[1]['output'] if len(all_results) > 1 else {}
step3_output = all_results[2]['output'] if len(all_results) > 2 else {}
step4_output = all_results[3]['output'] if len(all_results) > 3 else {}
step5_output = all_results[4]['output'] if len(all_results) > 4 else {}
step6_output = all_results[5]['output'] if len(all_results) > 5 else {}

print(f"\n✨ Complete pipeline finished!")
print(f"\n📁 All files saved in: {pipeline.run_folder}")
print(f"  • module_loader_*.json")
print(f"  • question_generator_*.json")
print(f"  • interaction_designer_*.json")
print(f"  • validation_designer_*.json")
print(f"  • dialogue_writer_*.json")
print(f"  • script_formatter_*.json")
print(f"  • script_*.md (combined readable script)")

print(f"\n📊 Pipeline Summary:")
print(f"  • Module: {step1_output.get('module_name', 'N/A')}")
print(f"  • Grade Level: {step1_output.get('grade_level', 'N/A')}")
print(f"  • Learning Goals: {len(step1_output.get('learning_goals_list', []))}")
if step2_output.get('questions'):
    print(f"  • Generated {len(step2_output['questions'])} questions")
if step3_output.get('sequences'):
    print(f"  • Designed {len(step3_output['sequences'])} interaction flows")
if step4_output.get('sequences'):
    print(f"  • Added validation to {len(step4_output['sequences'])} sequences")
if step5_output.get('sequences'):
    print(f"  • Added dialogue to {len(step5_output['sequences'])} sequences")
if step6_output.get('combined_script'):
    total_problems = step6_output.get('total_problems', 0)
    print(f"  • Formatted as 1 combined script with {total_problems} problems")

# Show preview of combined script
combined_script = step6_output.get('combined_script', '')
if combined_script:
    print(f"\n🎯 Script Preview:")
    print("=" * 70)
    print(combined_script[:800])
    print("...")
    print("=" * 70)

stats = client.get_stats()
print(f"\n💰 Token Usage: {stats['total_tokens']} tokens")
print(f"  • Step 1 (Module Loader):        0 tokens (no AI)")
print(f"  • Step 2 (Questions):            ~1,750 tokens")
print(f"  • Step 3 (Interaction Designer): ~5,000 tokens")
print(f"  • Step 4 (Validation Designer):  ~6,000 tokens")
print(f"  • Step 5 (Dialogue Writer):      ~5,000 tokens")
print(f"  • Step 6 (Scripts):              0 tokens (no AI)")

print(f"\n✅ Complete! Check {pipeline.run_folder} for all outputs.")
