"""Test InteractionDesigner + DialogueWriter with questions.json"""
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from datetime import datetime
from core.claude_client import ClaudeClient
from steps.interaction_designer import InteractionDesigner
from steps.dialogue_writer import DialogueWriter


def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def test_interaction_designer_and_dialogue_writer():
    """Test the split Step 2: InteractionDesigner → DialogueWriter"""
    
    # Load questions
    inputs_dir = Path(__file__).parent.parent / "inputs" / "examples"
    questions_path = inputs_dir / "questions.json"
    questions_list = load_json(questions_path)
    
    # Use only first 2 questions for testing
    questions_list = questions_list[:2]
    
    # Wrap in expected format
    questions_data = {"questions": questions_list}
    
    print(f"\n📊 Loaded {len(questions_list)} questions")
    
    # Setup
    claude = ClaudeClient()
    interaction_designer = InteractionDesigner(claude)
    dialogue_writer = DialogueWriter(claude)
    
    # Create test output folder
    outputs_dir = Path(__file__).parent.parent / "outputs"
    test_folder = outputs_dir / datetime.now().strftime("%Y-%m-%d") / "test_split"
    test_folder.mkdir(parents=True, exist_ok=True)
    
    # Step 2a: InteractionDesigner
    print("\n" + "="*60)
    print("STEP 2a: INTERACTION DESIGNER")
    print("="*60)
    
    interactions = interaction_designer.execute(questions_data)
    
    # Save intermediate
    interactions_path = test_folder / "interactions_without_dialogue.json"
    save_json(interactions, interactions_path)
    print(f"\n💾 Saved interactions to: {interactions_path}")
    
    # Step 2b: DialogueWriter
    print("\n" + "="*60)
    print("STEP 2b: DIALOGUE WRITER")
    print("="*60)
    
    sequences = dialogue_writer.execute(interactions)
    
    # Save final
    sequences_path = test_folder / "sequences_with_dialogue.json"
    save_json(sequences, sequences_path)
    print(f"\n💾 Saved sequences to: {sequences_path}")
    
    # Summary
    print("\n" + "="*60)
    print("✅ TEST COMPLETE")
    print("="*60)
    print(f"Questions:    {len(questions_data['questions'])}")
    print(f"Interactions: {len(interactions.get('sequences', []))}")
    print(f"Sequences:    {len(sequences.get('sequences', []))}")
    print(f"\nOutput folder: {test_folder}")
    

if __name__ == "__main__":
    test_interaction_designer_and_dialogue_writer()
