"""
Test Steps 3-6: InteractionDesigner → ValidationDesigner → DialogueWriter → ScriptFormatter
Uses existing question_generator output as starting point.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from steps.interaction_designer import InteractionDesigner
from steps.validation_designer import ValidationDesigner
from steps.dialogue_writer import DialogueWriter
from steps.script_formatter import ScriptFormatter
from core.claude_client import ClaudeClient
from datetime import datetime
import json
from dotenv import load_dotenv

# Load environment
load_dotenv()

def main():
    print("=" * 70)
    print("Testing Steps 3-6: Interactions → Validation → Dialogue → Scripts")
    print("=" * 70)
    
    # Initialize Claude client
    claude_client = ClaudeClient()
    print("✓ Claude client initialized")
    
    # Use most recent question generator output
    question_file = Path("outputs/2025-10-14/question_generator_173952.json")
    
    if not question_file.exists():
        print(f"✗ Question file not found: {question_file}")
        return
    
    print(f"\n📂 Loading questions from: {question_file.name}")
    with open(question_file, 'r', encoding='utf-8') as f:
        question_data = json.load(f)
    
    print(f"✓ Loaded {len(question_data['questions'])} questions")
    
    # Create output folder
    timestamp = datetime.now().strftime("%H%M%S")
    output_dir = Path(f"outputs/test_steps_3-6")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 3: InteractionDesigner
    print("\n" + "=" * 70)
    print("STEP 3: InteractionDesigner")
    print("=" * 70)
    try:
        interaction_designer = InteractionDesigner(claude_client)
        interaction_result = interaction_designer.execute(question_data)
        
        interaction_file = output_dir / f"interaction_designer_{timestamp}.json"
        with open(interaction_file, 'w', encoding='utf-8') as f:
            json.dump(interaction_result, f, indent=2)
        
        print(f"✓ InteractionDesigner complete")
        print(f"  Output: {interaction_file.name}")
        print(f"  Size: {len(json.dumps(interaction_result)):,} chars")
    except Exception as e:
        print(f"✗ InteractionDesigner failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Step 4: ValidationDesigner
    print("\n" + "=" * 70)
    print("STEP 4: ValidationDesigner")
    print("=" * 70)
    try:
        validation_designer = ValidationDesigner(claude_client)
        validation_result = validation_designer.execute(interaction_result)
        
        validation_file = output_dir / f"validation_designer_{timestamp}.json"
        with open(validation_file, 'w', encoding='utf-8') as f:
            json.dump(validation_result, f, indent=2)
        
        print(f"✓ ValidationDesigner complete")
        print(f"  Output: {validation_file.name}")
        print(f"  Size: {len(json.dumps(validation_result)):,} chars")
    except Exception as e:
        print(f"✗ ValidationDesigner failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Step 5: DialogueWriter
    print("\n" + "=" * 70)
    print("STEP 5: DialogueWriter")
    print("=" * 70)
    try:
        dialogue_writer = DialogueWriter(claude_client)
        dialogue_result = dialogue_writer.execute(validation_result)
        
        dialogue_file = output_dir / f"dialogue_writer_{timestamp}.json"
        with open(dialogue_file, 'w', encoding='utf-8') as f:
            json.dump(dialogue_result, f, indent=2)
        
        print(f"✓ DialogueWriter complete")
        print(f"  Output: {dialogue_file.name}")
        print(f"  Size: {len(json.dumps(dialogue_result)):,} chars")
    except Exception as e:
        print(f"✗ DialogueWriter failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Step 6: ScriptFormatter
    print("\n" + "=" * 70)
    print("STEP 6: ScriptFormatter")
    print("=" * 70)
    try:
        script_formatter = ScriptFormatter()
        script_result = script_formatter.execute(dialogue_result)
        
        # ScriptFormatter returns a dict with 'script' key
        script_text = script_result.get('script', script_result) if isinstance(script_result, dict) else script_result
        
        script_file = output_dir / f"script_{timestamp}.md"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_text)
        
        print(f"✓ ScriptFormatter complete")
        print(f"  Output: {script_file.name}")
        print(f"  Size: {len(script_text):,} chars")
    except Exception as e:
        print(f"✗ ScriptFormatter failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Summary
    print("\n" + "=" * 70)
    print("✓ ALL STEPS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\nOutputs saved to: {output_dir}/")
    print(f"  - {interaction_file.name}")
    print(f"  - {validation_file.name}")
    print(f"  - {dialogue_file.name}")
    print(f"  - {script_file.name}")
    print(f"\n📄 View final script: {script_file}")

if __name__ == "__main__":
    main()
