"""
Stepwise Test 5: Full Pipeline
Chains all 4 stepwise tests together automatically:
  Test 1: Question Generator (Module → Questions)
  Test 2: Interaction Designer (Questions → Sequences)
  Test 3: Remediation Generator (Sequences → Remediation)
  Test 4: Godot Formatter (Remediation → Godot JSON)
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import individual test functions
from tests.stepwise_tests.test_1_question_generator import test_question_generator
from tests.stepwise_tests.test_2_interaction_designer import test_interaction_designer
from tests.stepwise_tests.test_3_remediation_generator import test_remediation_generator
from tests.stepwise_tests.test_4_godot_formatter import test_godot_formatter


def test_full_pipeline(
    module_number=None,
    path_letter=None,
    num_questions=8,
    limit_sequences=None,
    output_dir=None
):
    """
    Run complete pipeline from module to Godot-ready JSON
    
    Args:
        module_number: Module number to load (if None, will prompt user)
        path_letter: Optional path letter (e.g., 'a', 'b') for module-specific docs (if None, will prompt user)
        num_questions: Number of questions to generate per learning goal
        limit_sequences: Optional limit on sequences to process in remediation/Godot steps
        output_dir: Optional output directory (auto-generated if not provided)
    
    Returns:
        Dict with paths to all outputs
    """
    print("=" * 70)
    print("STEPWISE TEST 5: FULL PIPELINE")
    print("=" * 70)
    print("\nChaining Tests:")
    print("  1. Question Generator (Module → Questions)")
    print("  2. Interaction Designer (Questions → Sequences)")
    print("  3. Remediation Generator (Sequences → Remediation)")
    print("  4. Godot Formatter (Remediation → Godot JSON)")
    print("=" * 70)
    
    # Get module configuration if not provided
    if module_number is None:
        print("\nModule Configuration:")
        try:
            module_input = input("Enter module number (e.g., 1): ").strip()
            module_number = int(module_input)
            path_letter = input("Enter path letter (e.g., a, b, c): ").strip().lower()
            print(f"✓ Using module {module_number}, path {path_letter}")
        except ValueError:
            print("❌ Invalid module number")
            return None
    
    print(f"\n📋 Pipeline Configuration:")
    print(f"  • Module: {module_number}")
    print(f"  • Path: {path_letter}")
    print(f"  • Questions per goal: {num_questions}")
    if limit_sequences:
        print(f"  • Sequence limit: {limit_sequences}")
    
    # Create main output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/test_full_pipeline_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n📁 Main output directory: {output_dir}\n")
    
    # Track outputs
    outputs = {
        "output_dir": output_dir,
        "module_number": module_number,
        "path_letter": path_letter,
        "num_questions": num_questions,
        "limit_sequences": limit_sequences,
        "steps": {}
    }
    
    # ========================================================================
    # STEP 1: QUESTION GENERATOR
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 1/4: QUESTION GENERATOR")
    print("=" * 70)
    
    step1_dir = os.path.join(output_dir, "step1_questions")
    
    try:
        questions_path = test_question_generator(
            module_number=module_number,
            num_questions=num_questions,
            path_letter=path_letter,
            output_dir=step1_dir
        )
        
        if questions_path is None:
            print("\n✗ Step 1 failed - cannot continue pipeline")
            return None
        
        outputs["steps"]["step1_questions"] = {
            "status": "success",
            "output_path": questions_path,
            "output_dir": step1_dir
        }
        
        # Load questions to check count
        with open(questions_path, 'r', encoding='utf-8') as f:
            questions_data = json.load(f)
        
        num_generated = len(questions_data.get('questions', []))
        print(f"\n✓ Step 1 Complete: {num_generated} questions generated")
        print(f"  → Output: {questions_path}")
        
    except Exception as e:
        print(f"\n✗ Step 1 Error: {e}")
        outputs["steps"]["step1_questions"] = {
            "status": "failed",
            "error": str(e)
        }
        return outputs
    
    # ========================================================================
    # STEP 2: INTERACTION DESIGNER
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 2/4: INTERACTION DESIGNER")
    print("=" * 70)
    
    step2_dir = os.path.join(output_dir, "step2_sequences")
    
    try:
        sequences_path = test_interaction_designer(
            questions_path=questions_path,
            output_dir=step2_dir,
            module_number=module_number,
            path_letter=path_letter
        )
        
        if sequences_path is None:
            print("\n✗ Step 2 failed - cannot continue pipeline")
            outputs["steps"]["step2_sequences"] = {
                "status": "failed",
                "error": "test_interaction_designer returned None"
            }
            return outputs
        
        outputs["steps"]["step2_sequences"] = {
            "status": "success",
            "output_path": sequences_path,
            "output_dir": step2_dir
        }
        
        # Load sequences to check count
        with open(sequences_path, 'r', encoding='utf-8') as f:
            sequences_data = json.load(f)
        
        num_sequences = len(sequences_data.get('sequences', []))
        print(f"\n✓ Step 2 Complete: {num_sequences} sequences designed")
        print(f"  → Output: {sequences_path}")
        
    except Exception as e:
        print(f"\n✗ Step 2 Error: {e}")
        outputs["steps"]["step2_sequences"] = {
            "status": "failed",
            "error": str(e)
        }
        return outputs
    
    # ========================================================================
    # STEP 3: REMEDIATION GENERATOR
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 3/4: REMEDIATION GENERATOR")
    print("=" * 70)
    
    step3_dir = os.path.join(output_dir, "step3_remediation")
    
    try:
        remediation_path = test_remediation_generator(
            sequences_path=sequences_path,
            output_dir=step3_dir,
            limit=limit_sequences,
            module_number=module_number,
            path_letter=path_letter
        )
        
        if remediation_path is None:
            print("\n✗ Step 3 failed - cannot continue pipeline")
            outputs["steps"]["step3_remediation"] = {
                "status": "failed",
                "error": "test_remediation_generator returned None"
            }
            return outputs
        
        outputs["steps"]["step3_remediation"] = {
            "status": "success",
            "output_path": remediation_path,
            "output_dir": step3_dir
        }
        
        # Load remediation to check count
        with open(remediation_path, 'r', encoding='utf-8') as f:
            remediation_data = json.load(f)
        
        num_remediation = len(remediation_data.get('sequences', []))
        
        # Count error paths
        total_error_paths = 0
        for seq in remediation_data.get('sequences', []):
            attempts = seq.get('student_attempts', {})
            error_paths = [k for k in attempts.keys() if k.startswith('error_path')]
            total_error_paths += len(error_paths)
        
        print(f"\n✓ Step 3 Complete: {num_remediation} sequences with error paths")
        print(f"  → Total error paths added: {total_error_paths}")
        print(f"  → Output: {remediation_path}")
        
    except Exception as e:
        print(f"\n✗ Step 3 Error: {e}")
        outputs["steps"]["step3_remediation"] = {
            "status": "failed",
            "error": str(e)
        }
        return outputs
    
    # ========================================================================
    # STEP 4: GODOT FORMATTER
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 4/4: GODOT FORMATTER")
    print("=" * 70)
    
    step4_dir = os.path.join(output_dir, "step4_godot")
    
    try:
        godot_path = test_godot_formatter(
            remediation_path=remediation_path,
            output_dir=step4_dir,
            limit=limit_sequences,
            module_number=module_number
        )
        
        if godot_path is None:
            print("\n✗ Step 4 failed")
            outputs["steps"]["step4_godot"] = {
                "status": "failed",
                "error": "test_godot_formatter returned None"
            }
            return outputs
        
        outputs["steps"]["step4_godot"] = {
            "status": "success",
            "output_path": godot_path,
            "output_dir": step4_dir
        }
        
        # Load Godot data to check count
        with open(godot_path, 'r', encoding='utf-8') as f:
            godot_data = json.load(f)
        
        num_godot = len(godot_data.get('sequences', []))
        print(f"\n✓ Step 4 Complete: {num_godot} Godot-ready sequences")
        print(f"  → Output: {godot_path}")
        
    except Exception as e:
        print(f"\n✗ Step 4 Error: {e}")
        outputs["steps"]["step4_godot"] = {
            "status": "failed",
            "error": str(e)
        }
        return outputs
    
    # ========================================================================
    # PIPELINE SUMMARY
    # ========================================================================
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)
    
    print(f"\n✅ All 4 steps completed successfully!")
    print(f"\n📁 Output Directory: {output_dir}")
    print(f"\n📊 Pipeline Results:")
    print(f"  • Module {module_number}{f' (Path {path_letter})' if path_letter else ''}")
    print(f"  • {num_generated} questions generated")
    print(f"  • {num_sequences} sequences designed")
    print(f"  • {total_error_paths} error paths added")
    print(f"  • {num_godot} Godot sequences formatted")
    
    print(f"\n📂 Output Files:")
    print(f"  Step 1: {outputs['steps']['step1_questions']['output_path']}")
    print(f"  Step 2: {outputs['steps']['step2_sequences']['output_path']}")
    print(f"  Step 3: {outputs['steps']['step3_remediation']['output_path']}")
    print(f"  Step 4: {outputs['steps']['step4_godot']['output_path']}")
    
    print(f"\n🎮 Final Output (Ready for Godot):")
    print(f"  → {godot_path}")
    
    # Save pipeline summary
    summary_path = os.path.join(output_dir, "pipeline_summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(outputs, f, indent=2)
    
    print(f"\n📄 Pipeline summary saved to: {summary_path}")
    
    print("\n" + "=" * 70)
    
    return outputs


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Run full pipeline from module to Godot-ready JSON')
    parser.add_argument('-m', '--module', type=int, default=1, help='Module number to load (default: 1)')
    parser.add_argument('-p', '--path', help='Path letter (e.g., a, b) for module-specific docs')
    parser.add_argument('-n', '--num-questions', type=int, default=8, help='Number of questions per goal (default: 8)')
    parser.add_argument('-l', '--limit', type=int, help='Limit sequences in remediation/Godot steps (for testing)')
    parser.add_argument('-o', '--output', help='Output directory (optional)', default=None)
    
    args = parser.parse_args()
    
    print("\n🚀 Starting Full Pipeline...")
    print(f"   Module: {args.module}")
    if args.path:
        print(f"   Path: {args.path}")
    print(f"   Questions per goal: {args.num_questions}")
    if args.limit:
        print(f"   Sequence limit: {args.limit}")
    print()
    
    result = test_full_pipeline(
        module_number=args.module,
        path_letter=args.path,
        num_questions=args.num_questions,
        limit_sequences=args.limit,
        output_dir=args.output
    )
    
    if result is None:
        print("\n❌ Pipeline failed")
        sys.exit(1)
    else:
        print("\n✅ Pipeline completed successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
