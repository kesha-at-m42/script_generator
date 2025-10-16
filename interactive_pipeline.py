"""
Interactive Pipeline - Generate content with review at each stage
"""
import json
from steps.module_loader import ModuleLoader
from steps.question_generator import QuestionGenerator
from steps.question_validator import QuestionValidator
from steps.interaction_designer import InteractionDesigner
from steps.validation_designer import ValidationDesigner
from steps.dialogue_writer import DialogueWriter
from steps.script_formatter import ScriptFormatter


def print_separator():
    """Print a visual separator"""
    print("\n" + "=" * 80 + "\n")


def save_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved to: {filename}")


def load_json(filename):
    """Load data from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_user_approval(stage_name):
    """Ask user if they want to proceed to next stage"""
    print_separator()
    print(f"REVIEW STAGE: {stage_name}")
    print("Options:")
    print("  [y] Approve and continue to next stage")
    print("  [n] Stop pipeline")
    print("  [r] Regenerate this stage")
    print("  [e] Edit the output file manually, then continue")
    
    while True:
        choice = input("\nYour choice: ").lower().strip()
        if choice in ['y', 'n', 'r', 'e']:
            return choice
        print("Invalid choice. Please enter y, n, r, or e")


def run_interactive_pipeline(module_number=1):
    """
    Run the full pipeline with review stages
    
    Args:
        module_number: The module number to process
    """
    print_separator()
    print(f"INTERACTIVE PIPELINE - MODULE {module_number}")
    print_separator()
    
    # Stage 0: Load Module
    print("STAGE 0: Loading Module Data...")
    module_loader = ModuleLoader()
    module_result = module_loader.execute({"module_number": module_number})
    print(f"✓ Module loaded: {module_result['module_name']}")
    print(f"  Learning goals: {len(module_result['goals'])} goals")
    print(f"  Vocabulary terms: {len(module_result['full_module_data']['vocabulary'])} terms")
    
    # Stage 1: Generate Questions
    print_separator()
    print("STAGE 1: Generating Questions...")
    from core.claude_client import ClaudeClient
    claude_client = ClaudeClient()
    question_generator = QuestionGenerator(claude_client)
    
    while True:
        questions_result = question_generator.execute(module_result, questions_per_goal=3)
        output_file = f"outputs/questions_module_{module_number}.json"
        save_json(questions_result, output_file)
        
        # Count total questions
        total_qs = sum(len(goal['questions']) for goal in questions_result['goals'])
        print(f"\n📊 Generated {total_qs} questions across {len(questions_result['goals'])} goals")
        
        # Show first few questions
        shown = 0
        for goal in questions_result['goals'][:2]:
            print(f"\n  Goal {goal['goal_id']}: {goal['goal_text'][:50]}...")
            for q in goal['questions'][:2]:
                shown += 1
                print(f"    {shown}. {q.get('question_text', 'N/A')[:60]}...")
        
        # VALIDATE QUESTIONS
        print("\n  🔍 Running validation...")
        validator = QuestionValidator()
        validated_result = validator.execute(questions_result)
        
        # Update output with validation report
        output_file_validated = f"outputs/questions_module_{module_number}_validated.json"
        save_json(validated_result, output_file_validated)
        
        choice = get_user_approval("Questions Generated & Validated")
        
        if choice == 'y':
            questions_result = validated_result  # Use validated version
            break
        elif choice == 'n':
            print("Pipeline stopped by user.")
            return
        elif choice == 'e':
            input(f"\nEdit {output_file_validated} now, then press Enter to continue...")
            questions_result = load_json(output_file_validated)
            break
        elif choice == 'r':
            print("Regenerating questions...")
            continue
    
    # Stage 2: Design Interactions
    print_separator()
    print("STAGE 2: Designing Interactions...")
    interaction_designer = InteractionDesigner(claude_client)
    
    while True:
        interactions = interaction_designer.execute(questions_result, **module_result)
        output_file = f"outputs/interactions_module_{module_number}.json"
        save_json(interactions, output_file)
        
        print(f"\n📊 Generated {len(interactions)} interaction sequences")
        for i, seq in enumerate(interactions[:2], 1):
            print(f"  {i}. Question {seq.get('question_id')}: {len(seq.get('sequence', []))} steps")
        if len(interactions) > 2:
            print(f"  ... and {len(interactions) - 2} more")
        
        choice = get_user_approval("Interactions Designed")
        
        if choice == 'y':
            break
        elif choice == 'n':
            print("Pipeline stopped by user.")
            return
        elif choice == 'e':
            input(f"\nEdit {output_file} now, then press Enter to continue...")
            interactions = load_json(output_file)
            break
        elif choice == 'r':
            print("Regenerating interactions...")
            continue
    
    # Stage 3: Design Validation
    print_separator()
    print("STAGE 3: Designing Validation...")
    validation_designer = ValidationDesigner(claude_client)
    
    while True:
        validations = validation_designer.execute(interactions, **module_result)
        output_file = f"outputs/validations_module_{module_number}.json"
        save_json(validations, output_file)
        
        print(f"\n📊 Added validation to {len(validations)} sequences")
        for i, seq in enumerate(validations[:2], 1):
            validation_count = sum(1 for step in seq.get('sequence', []) 
                                 if step.get('type') == 'validation')
            print(f"  {i}. Question {seq.get('question_id')}: {validation_count} validation steps")
        if len(validations) > 2:
            print(f"  ... and {len(validations) - 2} more")
        
        choice = get_user_approval("Validation Designed")
        
        if choice == 'y':
            break
        elif choice == 'n':
            print("Pipeline stopped by user.")
            return
        elif choice == 'e':
            input(f"\nEdit {output_file} now, then press Enter to continue...")
            validations = load_json(output_file)
            break
        elif choice == 'r':
            print("Regenerating validation...")
            continue
    
    # Stage 4: Write Dialogue
    print_separator()
    print("STAGE 4: Writing Dialogue...")
    dialogue_writer = DialogueWriter(claude_client)
    
    while True:
        dialogues = dialogue_writer.execute(validations, **module_result)
        output_file = f"outputs/dialogues_module_{module_number}.json"
        save_json(dialogues, output_file)
        
        print(f"\n📊 Added dialogue to {len(dialogues)} sequences")
        for i, seq in enumerate(dialogues[:2], 1):
            dialogue_count = sum(1 for step in seq.get('sequence', []) 
                               if 'guide_says' in step)
            print(f"  {i}. Question {seq.get('question_id')}: {dialogue_count} dialogue steps")
        if len(dialogues) > 2:
            print(f"  ... and {len(dialogues) - 2} more")
        
        choice = get_user_approval("Dialogue Written")
        
        if choice == 'y':
            break
        elif choice == 'n':
            print("Pipeline stopped by user.")
            return
        elif choice == 'e':
            input(f"\nEdit {output_file} now, then press Enter to continue...")
            dialogues = load_json(output_file)
            break
        elif choice == 'r':
            print("Regenerating dialogue...")
            continue
    
    # Stage 5: Generate Scripts
    print_separator()
    print("STAGE 5: Generating Scripts...")
    script_formatter = ScriptFormatter(claude_client)
    
    while True:
        scripts = script_formatter.execute(dialogues, **module_result)
        output_file = f"outputs/scripts_module_{module_number}.json"
        save_json(scripts, output_file)
        
        print(f"\n📊 Generated {len(scripts)} scripts")
        for i, script in enumerate(scripts[:2], 1):
            print(f"  {i}. Question {script.get('question_id')}: {script.get('script_type', 'N/A')}")
        if len(scripts) > 2:
            print(f"  ... and {len(scripts) - 2} more")
        
        choice = get_user_approval("Scripts Generated")
        
        if choice == 'y':
            break
        elif choice == 'n':
            print("Pipeline stopped by user.")
            return
        elif choice == 'e':
            input(f"\nEdit {output_file} now, then press Enter to continue...")
            scripts = load_json(output_file)
            break
        elif choice == 'r':
            print("Regenerating scripts...")
            continue
    
    # Pipeline Complete
    print_separator()
    print("✅ PIPELINE COMPLETE!")
    print(f"\nAll outputs saved to outputs/ directory:")
    print(f"  - questions_module_{module_number}.json")
    print(f"  - interactions_module_{module_number}.json")
    print(f"  - validations_module_{module_number}.json")
    print(f"  - dialogues_module_{module_number}.json")
    print(f"  - scripts_module_{module_number}.json")
    print_separator()


if __name__ == "__main__":
    import sys
    
    # Get module number from command line or use default
    module_number = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    
    run_interactive_pipeline(module_number)
