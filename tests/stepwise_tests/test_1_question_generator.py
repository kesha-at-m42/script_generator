"""
Stepwise Test 1: Question Generator
Takes learning goals and generates questions with proper schema
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.claude_client import ClaudeClient
from core.prompt_builder import PromptBuilder

def test_question_generator(module_number=2, num_questions=8, path_letter=None, output_dir=None, test_mode=False, goal_number=None):
    """
    Test question generator with learning goals
    
    Args:
        module_number: Module number to load
        num_questions: Number of questions to generate per goal
        path_letter: Optional path letter for module-specific docs
        output_dir: Optional output directory (auto-generated if not provided)
        test_mode: If True, only process first 2 goals for testing
        goal_number: If provided, only process this specific goal number
    """
    print("=" * 70)
    print("STEPWISE TEST 1: QUESTION GENERATOR")
    print("=" * 70)
    
    # Load learning goals from decomposed_goals.json
    goals_file = Path(__file__).parent.parent.parent / "inputs" / "modules" / f"module{module_number}" / "decomposed_goals.json"
    
    if not goals_file.exists():
        raise FileNotFoundError(f"Could not find decomposed goals file: {goals_file}")
    
    with open(goals_file, 'r', encoding='utf-8') as f:
        goals_data = json.load(f)
    
    learning_goals = goals_data["goals"]
    print(f"  📚 Loaded {len(learning_goals)} learning goals from {goals_file.name}")
    
    # Apply goal number filter if specified
    if goal_number is not None:
        learning_goals = [g for g in learning_goals if g['id'] == goal_number]
        if not learning_goals:
            raise ValueError(f"Goal {goal_number} not found in module {module_number}")
        print(f"\n🎯 SPECIFIC GOAL MODE: Processing only goal {goal_number}")
    # Otherwise apply test mode filter
    elif test_mode:
        learning_goals = learning_goals[:2]
        print(f"\n⚠️  TEST MODE: Processing only first 2 goals")
    
    print(f"\nModule: {module_number}")
    print(f"Goals to process: {len(learning_goals)}")
    
    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_questions_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nOutput directory: {output_dir}\n")
    
    # Initialize
    client = ClaudeClient()
    builder = PromptBuilder(module_number=module_number, path_letter=path_letter)
    
    # ========================================================================
    # QUESTION GENERATOR - PROCESS GOAL BY GOAL
    # ========================================================================
    print("=" * 70)
    print("GENERATING QUESTIONS")
    print("=" * 70)
    
    all_questions = []
    
    for idx, goal in enumerate(learning_goals, 1):
        print(f"\n{'=' * 70}")
        print(f"GOAL {idx}/{len(learning_goals)}")
        print(f"{'=' * 70}")
        
        # Extract goal text for display
        if isinstance(goal, dict):
            goal_display = goal.get('text', str(goal))
        else:
            goal_display = str(goal)
        
        print(f"Goal: {goal_display}")
        print(f"Generating questions...")
        
        # Extract goal data for prompt variables
        if isinstance(goal, dict):
            goal_id = goal.get('id', idx)
            goal_text = goal.get('text', str(goal))
            difficulty_level = goal.get('difficulty_level', '0-4')
            example_questions = goal.get('example_questions', [])
            question_type = goal.get('question_type', [])
            variables = goal.get('variables', {})
            
            # Format example questions as bullet list
            example_questions_text = '\n'.join([f"  - {ex}" for ex in example_questions])
            variables_text = json.dumps(variables, indent=2)  # ← ADD THIS
    
    # Format question types as comma-separated list
            question_types_text = ', '.join(question_type) 
        else:
            goal_id = idx
            goal_text = str(goal)
            difficulty_level = '0-4'
            example_questions_text = ''
        
        print(f"  Generating variations of example questions across difficulty range {difficulty_level}")
        
        # Build prompt (may return prefill)
        prompt_result = builder.build_prompt(
            prompt_id="question_generator",
            variables={
                "goal_id": goal_id,
                "goal": goal_text,
                "difficulty_level": difficulty_level,
                "example_questions": example_questions_text,
                "question_types": question_types_text,
                "variables": variables_text
            }
        )
        
        # Handle both tuple (prompt, prefill) and single string
        if isinstance(prompt_result, tuple):
            questions_prompt, prefill = prompt_result
        else:
            questions_prompt = prompt_result
            prefill = None
        
        print(f"Prompt length: {len(questions_prompt)} characters")
        print(f"Prefill: {prefill[:100]}..." if len(prefill) > 100 else f"Prefill: {prefill}")
        print("Calling Claude API...")
        
        # Higher temperature for more creative variation while maintaining structure
        questions_response = client.generate(
            questions_prompt, 
            max_tokens=16000, 
            temperature=1.0,
            prefill=prefill
        )
        
        # The response already includes the prefill, close the first question and questions array
        if not questions_response.strip().endswith('}'):
            questions_response = questions_response.rstrip().rstrip(',') + '\n    }\n  ]\n}'
        
        # Save raw response for this goal
        with open(f"{output_dir}/goal_{idx}_raw.txt", "w", encoding="utf-8") as f:
            f.write(questions_response)
        
        # Extract JSON
        if "```json" in questions_response:
            json_start = questions_response.find("```json") + 7
            json_end = questions_response.find("```", json_start)
            questions_json = questions_response[json_start:json_end].strip()
        else:
            questions_json = questions_response.strip()
        
        try:
            goal_questions_data = json.loads(questions_json)
            goal_questions = goal_questions_data.get('questions', [])
            
            # Questions already have goal_id and goal_text from prefill - no need to add them
            all_questions.extend(goal_questions)
            
            print(f"✓ Generated {len(goal_questions)} questions for goal {idx}")
            
            # Save individual goal output
            with open(f"{output_dir}/goal_{idx}_questions.json", "w", encoding="utf-8") as f:
                json.dump(goal_questions_data, f, indent=2)
            
        except json.JSONDecodeError as e:
            print(f"✗ JSON parsing error for goal {idx}: {e}")
            print(f"✗ Raw response saved to {output_dir}/goal_{idx}_raw.txt")
            continue
    
    # ====================================================================
    # GENERATE SUMMARY STATISTICS
    # ====================================================================
    summary = {
        "total_questions": len(all_questions),
        "by_goal": {},
        "by_variable_value": {},
        "by_difficulty_level": {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
        "by_question_type": {}
    }
    
    for q in all_questions:
        # Count by goal
        goal_id = q.get('goal_id', 'unknown')
        summary['by_goal'][goal_id] = summary['by_goal'].get(goal_id, 0) + 1
        
        # Count by variable value
        variables_used = q.get('variables_used', {})
        for var_name, var_value in variables_used.items():
            key = f"{var_name}: {var_value}"
            summary['by_variable_value'][key] = summary['by_variable_value'].get(key, 0) + 1
        
        # Count by difficulty level
        diff_level = q.get('difficulty_level')
        if diff_level in summary['by_difficulty_level']:
            summary['by_difficulty_level'][diff_level] += 1
        
        # Count by question type
        q_type = q.get('question_type', 'unknown')
        summary['by_question_type'][q_type] = summary['by_question_type'].get(q_type, 0) + 1
    
    # Combine all questions with summary
    questions_data = {
        "summary": summary,
        "questions": all_questions
    }
    
    # Save combined output
    questions_output_path = f"{output_dir}/questions.json"
    with open(questions_output_path, "w", encoding="utf-8") as f:
        json.dump(questions_data, f, indent=2)
    
    print(f"\n{'=' * 70}")
    print(f"✓ Generated {len(all_questions)} total questions across {len(learning_goals)} goals")
    print(f"✓ Saved combined output to {questions_output_path}")
    
    # Display summary statistics
    print("\n" + "=" * 70)
    print("SUMMARY STATISTICS")
    print("=" * 70)
    
    print("\nQuestions per Goal:")
    for goal_id in sorted(summary['by_goal'].keys()):
        count = summary['by_goal'][goal_id]
        print(f"  Goal {goal_id}: {count} questions")
    
    print("\nQuestions per Variable Value:")
    for var_key in sorted(summary['by_variable_value'].keys()):
        count = summary['by_variable_value'][var_key]
        print(f"  {var_key}: {count} questions")
    
    print("\nQuestions per Difficulty Level:")
    for level in sorted(summary['by_difficulty_level'].keys()):
        count = summary['by_difficulty_level'][level]
        pct = (count / len(all_questions) * 100) if len(all_questions) > 0 else 0
        print(f"  Level {level}: {count} questions ({pct:.1f}%)")
    
    print("\nQuestions per Question Type:")
    for q_type in sorted(summary['by_question_type'].keys()):
        count = summary['by_question_type'][q_type]
        pct = (count / len(all_questions) * 100) if len(all_questions) > 0 else 0
        print(f"  {q_type}: {count} questions ({pct:.1f}%)")
    
    # ====================================================================
    # VALIDATE SCHEMA
    # ====================================================================
    print("\n" + "=" * 70)
    print("SCHEMA VALIDATION")
    print("=" * 70)
    
    validation_results = {
        "total_questions": len(questions_data.get('questions', [])),
        "expected_total": num_questions * len(learning_goals),
        "questions": []
    }
    
    # Required fields for question generator output
    required_fields = [
        "goal_id", "goal_text", "question_id", "question_prompt", 
        "question_type", "difficulty_level", "visual_context", "variables_used"
    ]
    
    # Optional fields
    optional_fields = ["application_context"]
    
    # Track distributions
    difficulty_dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    question_type_dist = {"procedural": 0, "conceptual": 0, "transfer": 0}
    interaction_type_dist = {}
    
    for idx, q in enumerate(questions_data.get('questions', []), 1):
        q_validation = {
            "question_id": q.get('question_id'),
            "issues": []
        }
        
        print(f"\n  Question {idx} (ID: {q.get('question_id')}):")
        
        # Check required fields
        missing_fields = [field for field in required_fields if field not in q]
        if missing_fields:
            q_validation['issues'].append(f"Missing fields: {missing_fields}")
            print(f"    ✗ Missing fields: {missing_fields}")
        else:
            print(f"    ✓ All required fields present")
        
        # Check for extra fields
        all_valid_fields = required_fields + optional_fields
        extra_fields = [field for field in q.keys() if field not in all_valid_fields]
        if extra_fields:
            q_validation['issues'].append(f"Extra fields found: {extra_fields}")
            print(f"    ✗ Extra fields found: {extra_fields}")
        
        # Validate question_prompt is present with reasonable length
        question_prompt = q.get('question_prompt', '')
        if not question_prompt:
            q_validation['issues'].append("question_prompt is empty")
            print(f"    ✗ question_prompt is empty")
        else:
            prompt_length = len(question_prompt)
            if prompt_length > 50:
                print(f"    ✓ question_prompt present ({prompt_length} chars): \"{question_prompt[:50]}...\"")
            else:
                print(f"    ✓ question_prompt ({prompt_length} chars): \"{question_prompt}\"")
            # Warn if suspiciously short or long
            if prompt_length < 10:
                print(f"    ⚠️  question_prompt seems too short")
                q_validation['issues'].append("question_prompt too short")
            elif prompt_length > 200:
                print(f"    ⚠️  question_prompt seems too long")
                q_validation['issues'].append("question_prompt too long")
        
        # Track distributions
        diff_level = q.get('difficulty_level')
        if diff_level in difficulty_dist:
            difficulty_dist[diff_level] += 1
        
        q_type = q.get('question_type', '').upper()
        # Question types are CREATE, IDENTIFY, COMPARE, APPLY, CONNECT (not procedural/conceptual/transfer)
        
        i_type = q.get('interaction_type', 'N/A')
        interaction_type_dist[i_type] = interaction_type_dist.get(i_type, 0) + 1
        
        # Check variables_used (required field)
        variables_used = q.get('variables_used', {})
        if not variables_used:
            q_validation['issues'].append("Missing variables_used field")
            print(f"    ✗ Missing variables_used")
        else:
            print(f"    ✓ Variables used: {list(variables_used.keys())}")
        
        # Check visual context
        visual = q.get('visual_context', '')
        if 'rectangle' not in visual.lower() and 'bar' not in visual.lower():
            q_validation['issues'].append("Visual context doesn't mention rectangles/bars")
            print(f"    ⚠️  Visual context may not follow constraints")
        else:
            print(f"    ✓ Visual context uses rectangles/bars")
        
        validation_results['questions'].append(q_validation)
    
    # ====================================================================
    # DISTRIBUTION ANALYSIS
    # ====================================================================
    print("\n" + "=" * 70)
    print("DISTRIBUTION ANALYSIS")
    print("=" * 70)
    
    total = validation_results['total_questions']
    
    print("\nDifficulty Distribution:")
    target_diff = {0: "15%", 1: "10%", 2: "30%", 3: "25%", 4: "20%"}
    for level in range(5):
        count = difficulty_dist[level]
        pct = (count / total * 100) if total > 0 else 0
        target = target_diff[level]
        print(f"  Level {level}: {count} ({pct:.1f}%) - Target: {target}")
    
    print("\nQuestion Type Distribution:")
    target_qtype = {"procedural": "25%", "conceptual": "45%", "transfer": "30%"}
    for qtype in ["procedural", "conceptual", "transfer"]:
        count = question_type_dist[qtype]
        pct = (count / total * 100) if total > 0 else 0
        target = target_qtype[qtype]
        status = "✓" if pct >= 20 else "⚠️"
        print(f"  {qtype.capitalize()}: {count} ({pct:.1f}%) - Target: {target} {status}")
    
    print("\nInteraction Type Distribution:")
    for itype, count in sorted(interaction_type_dist.items()):
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {itype}: {count} ({pct:.1f}%)")
    
    # Save validation report
    validation_results['difficulty_distribution'] = difficulty_dist
    validation_results['question_type_distribution'] = question_type_dist
    validation_results['interaction_type_distribution'] = interaction_type_dist
    
    validation_path = f"{output_dir}/validation_report.json"
    with open(validation_path, "w", encoding="utf-8") as f:
        json.dump(validation_results, f, indent=2)
    
    print(f"\n✓ Validation report saved to {validation_path}")
    
    # ====================================================================
    # SUMMARY
    # ====================================================================
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    total_issues = sum(len(q['issues']) for q in validation_results['questions'])
    
    print(f"\n✓ Generated {validation_results['total_questions']} questions")
    print(f"  Expected: {validation_results['expected_total']}")
    print(f"{'✓' if total_issues == 0 else '⚠️'} Total validation issues: {total_issues}")
    
    if total_issues > 0:
        print("\nIssues found:")
        for q in validation_results['questions']:
            if q['issues']:
                print(f"  Question {q['question_id']}:")
                for issue in q['issues']:
                    print(f"    - {issue}")
    
    print(f"\nOutput files:")
    print(f"  - {output_dir}/goal_*_raw.txt (individual goal raw responses)")
    print(f"  - {output_dir}/goal_*_questions.json (individual goal outputs)")
    print(f"  - {output_dir}/questions.json ← Combined output for test 2 (interaction designer)")
    print(f"  - {output_dir}/validation_report.json")
    
    print("\n📊 Expected Schema:")
    print("  ✓ Required fields: goal_id, goal_text, question_id, question_prompt")
    print("  ✓ question_type, difficulty_level, visual_context, variables_used")
    print("  ✓ Optional fields: application_context (for APPLY/CONNECT types)")
    print("  ✓ Question types: CREATE, IDENTIFY, COMPARE, APPLY, CONNECT")
    print("  ✓ question_prompt should be close to example with variables swapped")
    
    print("\n" + "=" * 70)
    print("NEXT STEP")
    print("=" * 70)
    print(f"\nTo run Test 2 (Interaction Designer) with this output:")
    print(f"  python tests/stepwise/test_2_interaction_designer.py {questions_output_path}")
    
    return questions_output_path

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Test Question Generator with module loader')
    parser.add_argument('-m', '--module', type=int, default=1, help='Module number to load (default: 1)')
    parser.add_argument('-n', '--num-questions', type=int, default=8, help='Number of questions per goal (default: 8)')
    parser.add_argument('-p', '--path', help='Path letter (e.g., a, b) for module-specific docs')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    parser.add_argument('--test', action='store_true', help='Test mode: only process first 2 goals')
    parser.add_argument('-g', '--goal', type=int, help='Process only this specific goal number')

    args = parser.parse_args()

    test_question_generator(
        module_number=args.module,
        num_questions=args.num_questions,
        path_letter=args.path,
        output_dir=args.output,
        test_mode=args.test,
        goal_number=args.goal
    )

if __name__ == "__main__":
    main()