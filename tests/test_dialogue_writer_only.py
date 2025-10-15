"""Test DialogueWriter only with pre-generated interactions"""
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.claude_client import ClaudeClient
from steps.dialogue_writer import DialogueWriter


def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def test_dialogue_writer():
    """Test DialogueWriter with pre-generated interactions"""
    
    # Load the interactions from the previous test
    # Try the full pipeline output first (5 sequences)
    interactions_path = Path("outputs/2025-10-14/interaction_designer_174312.json")
    
    if not interactions_path.exists():
        # Fall back to test split (2 sequences)
        interactions_path = Path("outputs/2025-10-14/test_split/interactions_without_dialogue.json")
    
    if not interactions_path.exists():
        print("❌ No interactions file found. Run test_steps_2_3_split.py first.")
        return
    
    interactions = load_json(interactions_path)
    
    print(f"\n📊 Loaded interactions from: {interactions_path}")
    sequences = interactions.get('sequences', [])
    print(f"   {len(sequences)} sequences to add dialogue to")
    
    # Setup
    claude = ClaudeClient()
    dialogue_writer = DialogueWriter(claude)
    
    # Test DialogueWriter
    print("\n" + "="*60)
    print("TESTING: DIALOGUE WRITER")
    print("="*60)
    
    result = dialogue_writer.execute(interactions)
    
    # Save output
    output_path = Path("outputs/test_dialogue_only.json")
    save_json(result, output_path)
    
    print(f"\n💾 Saved output to: {output_path}")
    
    # Summary
    print("\n" + "="*60)
    print("✅ TEST COMPLETE")
    print("="*60)
    print(f"Input sequences:  {len(sequences)}")
    print(f"Output sequences: {len(result.get('sequences', []))}")
    

if __name__ == "__main__":
    test_dialogue_writer()
