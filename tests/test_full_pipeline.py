"""Test the full pipeline: Question Generator → Sequence Generator"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.question_generator import QuestionGenerator
from steps.sequence_generator import SequenceGenerator

print("Testing Full Pipeline: Questions → Sequences\n")

client = ClaudeClient()

# Create pipeline with both steps
pipeline = Pipeline("question_to_sequence_pipeline", save_intermediate=True)
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(SequenceGenerator(client))

# Input: Learning goals
learning_goals = """
- Students can partition shapes into equal parts
- Students can identify unit fractions
""".strip()

# Execute full pipeline
print("=" * 60)
results = pipeline.execute(
    {
        "learning_goals": learning_goals,
        "num_questions": 3,
        "grade_level": 3,
        "questions_per_goal": 3  # For step 2
    }
)
print("=" * 60)

# Get final output (sequences)
final_output = pipeline.get_final_output()
sequences = final_output.get("sequences", [])

print(f"\n✨ Pipeline completed successfully!")
print(f"\nStep 1 (Question Generator) output saved to: outputs/question_generator_*.json")
print(f"Step 2 (Sequence Generator) output saved to: outputs/sequence_generator_*.json")

print(f"\n📊 Results Summary:")
print(f"  • Generated {len(sequences)} interactive sequences")

print(f"\n🎯 Sample Sequence:")
if sequences:
    seq = sequences[0]
    print(f"  Problem ID: {seq.get('problem_id')}")
    print(f"  Goal: {seq.get('goal')}")
    print(f"  Difficulty: {seq.get('difficulty', 'N/A')}")
    print(f"  Steps: {len(seq.get('steps', []))}")
    
    if seq.get('steps'):
        print(f"\n  First step dialogue:")
        print(f"  '{seq['steps'][0].get('dialogue', 'N/A')}'")

stats = client.get_stats()
print(f"\n💰 Token Usage: {stats['total_tokens']} tokens")
print(f"  • Step 1 (Questions): ~1500-2000 tokens")
print(f"  • Step 2 (Sequences): ~{stats['total_tokens'] - 1750} tokens")
