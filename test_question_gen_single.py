"""
Test question generation for a single goal
"""
from steps.module_loader import ModuleLoader
from steps.question_generator import QuestionGenerator
from core.claude_client import ClaudeClient
import json

# Load module
loader = ModuleLoader()
module_result = loader.execute({"module_number": 1})

# Get goal 9 (the one with good examples)
goal_9 = [g for g in module_result['goals'] if g['id'] == 9][0]

print("=" * 80)
print(f"Testing Question Generation for Goal {goal_9['id']}")
print("=" * 80)
print(f"\nGoal: {goal_9['text']}")
print(f"\nVocabulary: {', '.join(goal_9['vocabulary_used'])}")
print(f"\nExample Questions:")
for i, ex in enumerate(goal_9['example_questions'], 1):
    print(f"  {i}. {ex}")

print("\n" + "=" * 80)
print("Generating 3 questions...")
print("=" * 80 + "\n")

# Generate questions for just this goal
claude = ClaudeClient()
generator = QuestionGenerator(claude)

# Create minimal input with just goal 9
test_input = {
    "goals": [goal_9],
    "grade_level": 3,
    "full_module_data": module_result['full_module_data']
}

result = generator.execute(test_input, questions_per_goal=3)

# Display results
print("\n" + "=" * 80)
print("GENERATED QUESTIONS")
print("=" * 80)

for goal_group in result['goals']:
    for i, q in enumerate(goal_group['questions'], 1):
        print(f"\n{'='*80}")
        print(f"Question {i}")
        print(f"{'='*80}")
        print(f"Text: {q['question_text']}")
        print(f"Type: {q['interaction_type']} | Difficulty: {q['difficulty_level']} | {q['question_type']}")
        print(f"\nVisual: {q['visual_context']}")
        print(f"\nAnswer: {q['correct_answer']}")
        print(f"\nExplanation: {q['explanation']}")
        print(f"\nVocabulary: {', '.join(q['vocabulary_reinforced'])}")

# Save to file
with open("outputs/test_goal_9_questions.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print("✓ Saved to: outputs/test_goal_9_questions.json")
print("=" * 80)

# Show stats
stats = claude.get_stats()
print(f"\n📊 Tokens used: {stats['total_tokens']}")
print(f"   Input: {stats['input_tokens']} | Output: {stats['output_tokens']}")
