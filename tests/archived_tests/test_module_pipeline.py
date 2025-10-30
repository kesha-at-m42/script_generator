"""Pipeline using structured module JSON input"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from core.input_parsers import ModuleInputParser
from core.file_utils import save_to_file
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from archive.steps.quiz_formatter import QuizFormatter

print("="*60)
print("MODULE-DRIVEN PIPELINE: Using Structured Input")
print("="*60 + "\n")

# Load module data
module_file = "inputs/module_1_fractions.json"
parser = ModuleInputParser(module_file)

# Display module info
module_info = parser.get_module_info()
print(f"📚 Module: {module_info['name']}")
print(f"   Grade: {module_info['grade']}")
print(f"   Module Number: {module_info['number']}")
print(f"   Variant: {module_info['variant']}\n")

# Show learning goals
print("🎯 Learning Goals:")
learning_goals = parser.get_learning_goals()
print(learning_goals)
print()

# Show vocabulary
print("📖 Key Vocabulary:")
print(", ".join(parser.get_vocabulary()))
print()

# Show standards
print("📋 Standards:")
standards = parser.get_standards()
print(f"  Building On: {', '.join(standards.get('buildingOn', []))}")
print(f"  Addressing: {', '.join(standards.get('addressing', []))}")
print(f"  Building Toward: {', '.join(standards.get('buildingToward', []))}")
print()

# Option 1: Use specific goals
print("Choose which goals to target:")
print("1. All goals")
print("2. Specific goals (1-3)")
print("3. Specific goals (4-6)")
choice = input("Enter choice (1-3): ").strip()

if choice == "2":
    goal_ids = [1, 2, 3]
elif choice == "3":
    goal_ids = [4, 5, 6]
else:
    goal_ids = None

# Format input for pipeline
pipeline_input = parser.format_for_question_generation(goal_ids)

# How many questions?
num_questions = int(input("Number of questions to generate: ").strip() or "5")
pipeline_input["num_questions"] = num_questions

print("\n" + "="*60)
print("EXECUTING PIPELINE")
print("="*60 + "\n")

# Initialize client and pipeline
client = ClaudeClient()
pipeline = Pipeline(f"module_{module_info['number']}_quiz")

# Add steps
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(AnswerGenerator(client))
pipeline.add_step(QuizFormatter(format_type="html"))

# Execute
try:
    results = pipeline.execute(pipeline_input)
    
    # Save results
    pipeline.save_results()
    
    # Save final output
    final_output = pipeline.get_final_output()
    module_name_clean = module_info['name'].replace(' ', '_').lower()
    html_file = save_to_file(
        final_output, 
        f"{module_name_clean}_quiz.html",
        "output"
    )
    
    print(f"\n💾 Quiz saved to: {html_file}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Module: {module_info['name']}")
    print(f"Grade: {module_info['grade']}")
    print(f"Questions Generated: {num_questions}")
    print(f"Goals Targeted: {len(goal_ids) if goal_ids else 'All'}")
    
    stats = client.get_stats()
    print(f"\n📊 Tokens: {stats['total_tokens']} total")
    print(f"   Input: {stats['input_tokens']}")
    print(f"   Output: {stats['output_tokens']}")
    
    print("\n✓✓✓ PIPELINE COMPLETED! ✓✓✓")
    print(f"\nOpen in browser: start {html_file}")
    
except Exception as e:
    print(f"\n✗ Pipeline failed: {e}")
    raise
