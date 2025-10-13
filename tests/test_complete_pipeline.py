"""Complete end-to-end pipeline example"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from core.file_utils import save_to_file
from steps.question_generator import QuestionGenerator
from steps.answer_generator import AnswerGenerator
from steps.quiz_formatter import QuizFormatter

print("="*60)
print("COMPLETE PIPELINE: Question → Answer → Format")
print("="*60 + "\n")

# Initialize client
client = ClaudeClient()

# Create pipeline
pipeline = Pipeline("educational_quiz_generator")

# Add steps
pipeline.add_step(QuestionGenerator(client))
pipeline.add_step(AnswerGenerator(client))
pipeline.add_step(QuizFormatter(format_type="html"))

# Define initial input
initial_input = {
    "learning_goals": """
- Students can add fractions with like denominators
- Students can subtract fractions with like denominators
- Students can identify equivalent fractions
    """.strip(),
    "num_questions": 4
}

print("Initial Input:")
print(f"  Learning Goals: {initial_input['learning_goals'][:50]}...")
print(f"  Number of Questions: {initial_input['num_questions']}\n")

# Execute pipeline
try:
    results = pipeline.execute(initial_input)
    
    # Save results
    pipeline.save_results()
    
    # Save final HTML output
    final_output = pipeline.get_final_output()
    html_file = save_to_file(final_output, "quiz_output.html")
    print(f"💾 HTML quiz saved to: {html_file}")
    
    # Print summary
    print("\n" + "="*60)
    print("PIPELINE SUMMARY")
    print("="*60)
    
    for i, result in enumerate(results, 1):
        print(f"\nStep {i}: {result['name']}")
        print(f"  Input Type: {type(result['input']).__name__}")
        print(f"  Output Type: {type(result['output']).__name__}")
        
        if isinstance(result['output'], list):
            print(f"  Items Generated: {len(result['output'])}")
        elif isinstance(result['output'], str):
            print(f"  Output Length: {len(result['output'])} characters")
    
    # Stats
    stats = client.get_stats()
    print("\n" + "="*60)
    print(f"📊 Total tokens used: {stats['total_tokens']}")
    print(f"   Input: {stats['input_tokens']}")
    print(f"   Output: {stats['output_tokens']}")
    print("="*60)
    print("\n✓✓✓ PIPELINE COMPLETED SUCCESSFULLY! ✓✓✓\n")
    
except Exception as e:
    print(f"\n✗ Pipeline failed: {e}")
    raise
