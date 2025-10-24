"""
Test Question Generator with Difficulty Levels and Question Types
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from steps.question_generator import QuestionGenerator
from inputs.modules.modules import module_1
from inputs.difficulty_levels import DIFFICULTY_LEVELS
from inputs.question_types import QUESTION_TYPES

def print_question_details(questions):
    """Print detailed information about each question"""
    print("\n" + "="*80)
    print("GENERATED QUESTIONS - DETAILED VIEW")
    print("="*80)
    
    for i, q in enumerate(questions, 1):
        difficulty_level = q.get('difficulty_level', '?')
        question_type = q.get('question_type', '?')
        cognitive_verb = q.get('cognitive_verb', '?')
        
        # Get difficulty name
        if isinstance(difficulty_level, int) and difficulty_level in DIFFICULTY_LEVELS:
            diff_name = DIFFICULTY_LEVELS[difficulty_level]['name']
            diff_desc = DIFFICULTY_LEVELS[difficulty_level]['description']
        else:
            diff_name = "Unknown"
            diff_desc = ""
        
        # Get question type description
        if question_type in QUESTION_TYPES:
            type_focus = QUESTION_TYPES[question_type]['cognitive_focus']
        else:
            type_focus = "Unknown"
        
        print(f"\n{'─'*80}")
        print(f"Question {i}")
        print(f"{'─'*80}")
        print(f"PROMPT: {q.get('prompt', 'N/A')}")
        print(f"\nMETADATA:")
        print(f"  • Difficulty: Level {difficulty_level} - {diff_name}")
        print(f"    → {diff_desc}")
        print(f"  • Question Type: {question_type.upper()} ({type_focus})")
        print(f"  • Cognitive Verb: {cognitive_verb}")
        print(f"  • Interaction: {q.get('interaction_type', 'N/A')}")
        print(f"  • Learning Goal: {q.get('goal', 'N/A')}")
        if q.get('context'):
            print(f"  • Context: {q['context']}")

def main():
    print("="*80)
    print("TESTING QUESTION GENERATOR WITH DIFFICULTY & TYPE METADATA")
    print("="*80)
    
    # Initialize
    client = ClaudeClient()
    generator = QuestionGenerator(client)
    
    # Use first module's data
    print(f"\nModule: {module_1['module_name']} (Grade {module_1['grade_level']})")
    print(f"Using {len(module_1['goals'])} learning goals")
    
    # Format learning goals for input
    learning_goals_text = "\n".join([f"- {goal['text']}" for goal in module_1['goals']])
    
    # Prepare pipeline input
    pipeline_input = {
        "learning_goals": learning_goals_text,
        "num_questions": 8,  # Generate 8 questions to get good variety
        "module_name": module_1['module_name'],
        "grade_level": module_1['grade_level']
    }
    
    print(f"\nGenerating {pipeline_input['num_questions']} questions...")
    print("─"*80)
    
    # Execute
    result = generator.execute(pipeline_input)
    
    # Handle structured output
    if isinstance(result, dict) and "questions" in result:
        questions = result["questions"]
        metadata = result.get("metadata", {})
        print("\n  ✓ Received structured output with metadata")
    else:
        questions = result if isinstance(result, list) else []
        metadata = {}
    
    # Print detailed view
    print_question_details(questions)
    
    # Print token usage
    print("\n" + "="*80)
    print("TOKEN USAGE")
    print("="*80)
    stats = client.get_stats()
    print(f"Input tokens:  {stats['input_tokens']}")
    print(f"Output tokens: {stats['output_tokens']}")
    print(f"Total tokens:  {stats['total_tokens']}")
    
    # Validate distribution
    print("\n" + "="*80)
    print("VALIDATION")
    print("="*80)
    
    # Check for variety
    difficulty_levels = set(q.get('difficulty_level') for q in questions)
    question_types = set(q.get('question_type') for q in questions)
    interaction_types = set(q.get('interaction_type') for q in questions)
    
    print(f"✓ Unique difficulty levels: {len(difficulty_levels)} (Goal: 3+)")
    print(f"  Levels present: {sorted(difficulty_levels)}")
    
    print(f"✓ Unique question types: {len(question_types)} (Goal: 2+)")
    print(f"  Types present: {question_types}")
    
    print(f"✓ Unique interaction types: {len(interaction_types)} (Goal: 3+)")
    print(f"  Types present: {interaction_types}")
    
    # Count mastery vs support questions
    mastery_count = sum(1 for q in questions if q.get('difficulty_level', 0) >= 2)
    support_count = sum(1 for q in questions if q.get('difficulty_level', 0) < 2)
    
    print(f"\n✓ Mastery questions (Levels 2-4): {mastery_count}")
    print(f"✓ Support questions (Levels 0-1): {support_count}")
    
    print("\n" + "="*80)
    print("TEST COMPLETE!")
    print("="*80)

if __name__ == "__main__":
    main()
