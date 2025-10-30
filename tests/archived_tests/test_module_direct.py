"""Pipeline using module data - no parser needed!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from inputs.modules.modules import module_1
from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from core.file_utils import save_to_file
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from archive.steps.quiz_formatter import QuizFormatter

print("="*60)
print("MODULE-DRIVEN PIPELINE: Direct Data Access")
print("="*60 + "\n")

# Display module info - direct access!
print(f"📚 Module: {module_1['module_name']}")
print(f"   Grade: {module_1['grade_level']}")
print(f"   Module Number: {module_1['module_number']}")
print(f"   Variant: {module_1['path_variant']}\n")

# Show learning goals
print("🎯 Learning Goals:")
for goal in module_1['learning_goals']:
    print(f"  - {goal}")
print()

# Show vocabulary
print("📖 Key Vocabulary:")
print(f"  {', '.join(module_1['vocabulary'])}")
print()

# Show standards
print("📊 Standards:")
standards = module_1['standards']
print(f"  Building On: {', '.join(standards['building_on'])}")
print(f"  Addressing: {', '.join(standards['addressing'])}")
print(f"  Building Toward: {', '.join(standards['building_toward'])}")
print()

# Show detailed goals
print(f"🎓 Detailed Goals ({len(module_1['goals'])} total):")
for goal in module_1['goals']:
    print(f"  {goal['id']}. {goal['text']}")
print()

# Interactive: Select goals
print("Which goals would you like to target?")
print("  1. All goals")
print("  2. Goals 1-2")
print("  3. Goal 3 only")
choice = input("\nYour choice (1-3): ").strip()

if choice == "2":
    selected_goals = module_1['goals'][:2]
elif choice == "3":
    selected_goals = [module_1['goals'][2]]
else:
    selected_goals = module_1['goals']

print(f"\n✓ Selected {len(selected_goals)} goal(s)")

# Format for pipeline
learning_goals_text = '\n'.join(f"- {goal['text']}" for goal in selected_goals)

# Add context
context = f"""Module: {module_1['module_name']} (Grade {module_1['grade_level']})

Learning Goals:
{learning_goals_text}

Key Vocabulary: {', '.join(module_1['vocabulary'])}
"""

# Get number of questions
num_questions = input("How many questions would you like to generate? (default: 4): ").strip()
num_questions = int(num_questions) if num_questions else 4

print(f"\n{'='*60}")
print(f"GENERATING {num_questions} QUESTIONS")
print(f"{'='*60}\n")

# Create pipeline
client = ClaudeClient()
pipeline = Pipeline(f"module_{module_1['module_number']}_quiz")

pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(AnswerGenerator(client))
pipeline.add_step(QuizFormatter(format_type="html"))

# Execute
pipeline_input = {
    "learning_goals": learning_goals_text,
    "full_context": context,
    "module_name": module_1['module_name'],
    "grade_level": module_1['grade_level'],
    "num_questions": num_questions
}

results = pipeline.execute(pipeline_input)

# Save results
pipeline_file = pipeline.save_results()
print(f"\n📄 Pipeline results: {pipeline_file}")

# Save HTML output
module_name_clean = module_1['module_name'].replace(' ', '_').lower()
html_file = save_to_file(
    pipeline.get_final_output(),
    f"{module_name_clean}_quiz.html",
    "output"
)
print(f"🌐 HTML quiz: {html_file}")

# Stats
stats = client.get_stats()
print(f"\n📊 Statistics:")
print(f"   Total Tokens: {stats['total_tokens']}")
print(f"   Input Tokens: {stats['input_tokens']}")
print(f"   Output Tokens: {stats['output_tokens']}")

print(f"\n✅ Done! Open {html_file} in your browser to view the quiz.")
