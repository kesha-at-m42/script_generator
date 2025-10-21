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
from steps.module_loader import ModuleLoader

def test_question_generator(module_number=1, num_questions=8, path_letter=None, output_dir=None):
    """
    Test question generator with learning goals
    
    Args:
        module_number: Module number to load
        num_questions: Number of questions to generate per goal
        path_letter: Optional path letter for module-specific docs
        output_dir: Optional output directory (auto-generated if not provided)
    """
    print("=" * 70)
    print("STEPWISE TEST 1: QUESTION GENERATOR")
    print("=" * 70)
    # Load module data using ModuleLoader
    loader = ModuleLoader()
    module_data = loader.execute(module_number)
    learning_goals = module_data["learning_goals_list"]
    goals_text = module_data["learning_goals"]
    num_goals = len(learning_goals)
    print(f"\nLearning Goals ({num_goals}):")
    print(goals_text)
    print(goals_text)
    print(f"\nQuestions per goal: {num_questions}")
    print(f"Total questions to generate: {num_questions * num_goals}")
    
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
    # QUESTION GENERATOR
    # ========================================================================
    print("=" * 70)
    print("GENERATING QUESTIONS")
    print("=" * 70)
    
    print("\nGenerating questions from learning goals...")
    
    questions_prompt = builder.build_prompt(
        prompt_id="question_generator",
        variables={
            "learning_goals": goals_text,
            "num_questions": num_questions
        }
    )
    
    print(f"Prompt length: {len(questions_prompt)} characters")
    print("Calling Claude API...")
    
    questions_response = client.generate(questions_prompt, max_tokens=16000, temperature=0.7)
    
    # Save raw response
    with open(f"{output_dir}/questions_raw.txt", "w", encoding="utf-8") as f:
        f.write(questions_response)
    
    # Extract JSON
    if "```json" in questions_response:
        json_start = questions_response.find("```json") + 7
        json_end = questions_response.find("```", json_start)
        questions_json = questions_response[json_start:json_end].strip()
    else:
        questions_json = questions_response.strip()
    
    try:
        questions_data = json.loads(questions_json)
        
        questions_output_path = f"{output_dir}/questions.json"
        with open(questions_output_path, "w", encoding="utf-8") as f:
            json.dump(questions_data, f, indent=2)
        
        print(f"✓ Generated {len(questions_data.get('questions', []))} questions")
        print(f"✓ Saved to {questions_output_path}")
        
        # ====================================================================
        # VALIDATE SCHEMA
        # ====================================================================
        print("\n" + "=" * 70)
        print("SCHEMA VALIDATION")
        print("=" * 70)
        
        validation_results = {
            "total_questions": len(questions_data.get('questions', [])),
            "expected_total": num_questions * num_goals,
            "questions": []
        }
        
        # Required fields
        required_fields = [
            "id", "question_text", "interaction_type", "difficulty_level",
            "question_type", "cognitive_verb", "visual_context",
            "correct_answer", "explanation", "vocabulary_reinforced"
        ]
        
        # Track distributions
        difficulty_dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        question_type_dist = {"procedural": 0, "conceptual": 0, "transfer": 0}
        interaction_type_dist = {}
        
        for idx, q in enumerate(questions_data.get('questions', []), 1):
            q_validation = {
                "question_id": q.get('id'),
                "issues": []
            }
            
            print(f"\n  Question {idx} (ID: {q.get('id')}):")
            
            # Check required fields
            missing_fields = [field for field in required_fields if field not in q]
            if missing_fields:
                q_validation['issues'].append(f"Missing fields: {missing_fields}")
                print(f"    ✗ Missing fields: {missing_fields}")
            else:
                print(f"    ✓ All required fields present")
            
            # Check interaction_type specific fields
            interaction_type = q.get('interaction_type', '')
            if interaction_type in ['Multiple Choice', 'Multiple Select']:
                if 'answer_choices' not in q:
                    q_validation['issues'].append(f"Missing answer_choices for {interaction_type}")
                    print(f"    ✗ Missing answer_choices for {interaction_type}")
                else:
                    print(f"    ✓ answer_choices present ({len(q['answer_choices'])} options)")
            
            # Track distributions
            diff_level = q.get('difficulty_level')
            if diff_level in difficulty_dist:
                difficulty_dist[diff_level] += 1
            
            q_type = q.get('question_type', '').lower()
            if q_type in question_type_dist:
                question_type_dist[q_type] += 1
            
            i_type = q.get('interaction_type', '')
            interaction_type_dist[i_type] = interaction_type_dist.get(i_type, 0) + 1
            
            # Check explanation length
            explanation = q.get('explanation', '')
            word_count = len(explanation.split())
            if word_count < 30:
                q_validation['issues'].append(f"Explanation too short ({word_count} words, need 30+)")
                print(f"    ✗ Explanation too short ({word_count} words)")
            else:
                print(f"    ✓ Explanation adequate ({word_count} words)")
            
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
        print(f"  - {output_dir}/questions_raw.txt")
        print(f"  - {output_dir}/questions.json ← Use this for test 2 (interaction designer)")
        print(f"  - {output_dir}/validation_report.json")
        
        print("\n📊 Expected Schema:")
        print("  ✓ Required fields: id, question_text, interaction_type, difficulty_level")
        print("  ✓ question_type, cognitive_verb, visual_context, correct_answer")
        print("  ✓ explanation (30+ words), vocabulary_reinforced")
        print("  ✓ answer_choices (for Multiple Choice/Multiple Select only)")
        print("  ✓ Visual: Rectangle bars only, 2-8 parts")
        
        print("\n" + "=" * 70)
        print("NEXT STEP")
        print("=" * 70)
        print(f"\nTo run Test 2 (Interaction Designer) with this output:")
        print(f"  python tests/stepwise/test_2_interaction_designer.py {questions_output_path}")
        
        return questions_output_path
        
    except json.JSONDecodeError as e:
        print(f"\n✗ JSON parsing error: {e}")
        print(f"✗ Raw response saved to {output_dir}/questions_raw.txt")
        print(f"✗ Check the raw response for syntax errors")
        return None

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Test Question Generator with module loader')
    parser.add_argument('-m', '--module', type=int, default=1, help='Module number to load (default: 1)')
    parser.add_argument('-n', '--num-questions', type=int, default=8, help='Number of questions per goal (default: 8)')
    parser.add_argument('-p', '--path', help='Path letter (e.g., a, b) for module-specific docs')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)

    args = parser.parse_args()

    test_question_generator(
        module_number=args.module,
        num_questions=args.num_questions,
        path_letter=args.path,
        output_dir=args.output
    )

if __name__ == "__main__":
    main()