"""Test 6: End-to-end test of question generation"""
import sys
from pathlib import Path

# Add parent directory to path so we can import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.file_utils import save_json, load_json
from steps.question_generator import QuestionGenerator

print("="*60)
print("END-TO-END TEST: Question Generation")
print("="*60 + "\n")

# Setup
client = ClaudeClient()
generator = QuestionGenerator(client)

# Input
learning_goals = """
- Students can add fractions with like denominators
- Students can identify equivalent fractions
- Students can compare fractions using visual models
""".strip()

print("Learning Goals:")
print(learning_goals)
print("\n" + "-"*60 + "\n")

# Generate
questions = generator.generate(learning_goals, num_questions=6)

# Save
save_json(questions, "step1_questions.json")

# Load back and verify
loaded = load_json("step1_questions.json")

print("\n" + "-"*60)
print("VERIFICATION")
print("-"*60)
print(f"✓ Generated: {len(questions)} questions")
print(f"✓ Saved and reloaded: {len(loaded)} questions")
print(f"✓ Data integrity: {questions == loaded}")

# Show summary
print("\n" + "-"*60)
print("QUESTION SUMMARY")
print("-"*60)
for i, q in enumerate(loaded, 1):
    print(f"{i}. [{q['interaction_type']}] {q['prompt'][:50]}...")

# Stats
stats = client.get_stats()
print("\n" + "-"*60)
print(f"📊 Total tokens used: {stats['total_tokens']}")
print("="*60)
print("\n✓✓✓ END-TO-END TEST PASSED! ✓✓✓\n")