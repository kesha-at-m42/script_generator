"""Interactive console script - Generate educational problems from module number"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.claude_client import ClaudeClient
from core.pipeline import Pipeline
from steps.module_loader import ModuleLoader
from steps.question_generator import QuestionGenerator
from steps.interaction_designer import InteractionDesigner
from steps.validation_designer import ValidationDesigner
from steps.dialogue_writer import DialogueWriter
from steps.script_formatter import ScriptFormatter


def main():
    print("\n" + "="*70)
    print("  EDUCATIONAL PROBLEM GENERATOR")
    print("="*70)
    print("\nThis will generate interactive educational problems from a module.\n")
    
    # Get module number from user
    while True:
        try:
            module_num = input("Enter module number: ").strip()
            module_num = int(module_num)
            if module_num in [1, 2]:
                break
            else:
                print("❌ Please enter 1 or 2")
        except ValueError:
            print("❌ Please enter a valid number")
    
    # Get number of questions
    while True:
        try:
            num_questions = input("How many questions? (1-10): ").strip()
            num_questions = int(num_questions)
            if 1 <= num_questions <= 10:
                break
            else:
                print("❌ Please enter a number between 1 and 10")
        except ValueError:
            print("❌ Please enter a valid number")
    
    print("\n" + "="*70)
    print(f"Generating {num_questions} problems from Module {module_num}")
    print("="*70)
    
    # Setup pipeline
    client = ClaudeClient()
    pipeline = Pipeline("module_to_script", save_intermediate=True)
    
    # Add all 6 steps
    pipeline.add_step(ModuleLoader())
    pipeline.add_step(QuestionGenerator(client))
    pipeline.add_step(InteractionDesigner(client))
    pipeline.add_step(ValidationDesigner(client))
    pipeline.add_step(DialogueWriter(client))
    pipeline.add_step(ScriptFormatter())
    
    print("\nPipeline Steps:")
    print("  1. Module Loader - Load learning goals")
    print("  2. Question Generator - Generate questions (AI)")
    print("  3. Interaction Designer - Design visuals/mechanics (AI)")
    print("  4. Validation Designer - Design error handling (AI)")
    print("  5. Dialogue Writer - Add character voice (AI)")
    print("  6. Script Formatter - Format as readable script")
    print()
    
    # Execute pipeline
    try:
        results = pipeline.execute({
            "module_number": module_num,
            "num_questions": num_questions
        })
        
        # Get final output
        final_output = pipeline.get_final_output()
        
        print("\n" + "="*70)
        print("✅ GENERATION COMPLETE!")
        print("="*70)
        
        # Show summary
        all_results = pipeline.results
        step1 = all_results[0]['output'] if len(all_results) > 0 else {}
        step2 = all_results[1]['output'] if len(all_results) > 1 else {}
        step6 = all_results[5]['output'] if len(all_results) > 5 else {}
        
        print(f"\n📊 Summary:")
        print(f"  Module: {step1.get('module_name', 'N/A')}")
        print(f"  Grade Level: {step1.get('grade_level', 'N/A')}")
        print(f"  Questions Generated: {len(step2.get('questions', []))}")
        print(f"  Total Problems: {step6.get('total_problems', 0)}")
        
        # Show output location
        print(f"\n📁 Output Location:")
        print(f"  {pipeline.run_folder}")
        print(f"\n📄 Files Generated:")
        print(f"  • module_loader_*.json")
        print(f"  • question_generator_*.json")
        print(f"  • interaction_designer_*.json")
        print(f"  • validation_designer_*.json")
        print(f"  • dialogue_writer_*.json")
        print(f"  • script_formatter_*.json")
        print(f"  • script_*.md (readable script)")
        
        # Show token usage
        stats = client.get_stats()
        print(f"\n💰 API Usage:")
        print(f"  Total Tokens: {stats['total_tokens']:,}")
        print(f"  Estimated Cost: ${stats['total_tokens'] * 0.000003:.4f} (at $3/1M tokens)")
        
        # Show script preview
        combined_script = step6.get('combined_script', '')
        if combined_script:
            print(f"\n📖 Script Preview (first 1000 chars):")
            print("="*70)
            print(combined_script[:1000])
            print("...")
            print("="*70)
        
        # Ask if user wants to generate more
        print()
        another = input("Generate another set? (y/n): ").strip().lower()
        if another == 'y':
            print("\n" + "="*70)
            main()  # Recursive call to start over
        else:
            print("\n👋 Thanks for using the Problem Generator!")
            
    except KeyboardInterrupt:
        print("\n\n❌ Generation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error during generation:")
        print(f"  {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
