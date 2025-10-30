"""
Test optimized DialogueWriter with compaction
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from steps.dialogue_writer import DialogueWriter
from core.claude_client import ClaudeClient
import json

def main():
    print("=" * 70)
    print("Testing Optimized DialogueWriter")
    print("=" * 70)
    
    # Load validation_designer output
    validation_file = Path("outputs/test_steps_3-6/validation_designer_154329.json")
    
    if not validation_file.exists():
        print(f"✗ Validation file not found: {validation_file}")
        return
    
    print(f"\n📂 Loading validation from: {validation_file.name}")
    with open(validation_file, 'r', encoding='utf-8') as f:
        validation_data = json.load(f)
    
    sequences = validation_data.get("sequences", [])
    print(f"✓ Loaded {len(sequences)} sequences")
    print(f"  Original size: {len(json.dumps(validation_data)):,} chars")
    
    # Test DialogueWriter
    print("\n" + "=" * 70)
    print("STEP: DialogueWriter (Optimized)")
    print("=" * 70)
    
    claude_client = ClaudeClient()
    dialogue_writer = DialogueWriter(claude_client)
    
    try:
        dialogue_result = dialogue_writer.execute(validation_data)
        
        # Save output
        output_file = Path("outputs/test_steps_3-6/dialogue_writer_optimized.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dialogue_result, f, indent=2)
        
        print(f"\n✓ DialogueWriter complete")
        print(f"  Output: {output_file}")
        print(f"  Size: {len(json.dumps(dialogue_result)):,} chars")
        
        # Check token usage
        stats = claude_client.get_stats()
        print(f"\n💰 API Usage:")
        print(f"  Input tokens: {stats['input_tokens']:,}")
        print(f"  Output tokens: {stats['output_tokens']:,}")
        print(f"  Total tokens: {stats['total_tokens']:,}")
        
    except Exception as e:
        print(f"\n✗ DialogueWriter failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n" + "=" * 70)
    print("✓ COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
