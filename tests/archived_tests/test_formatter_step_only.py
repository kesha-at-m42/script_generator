"""
Test just the ScriptFormatter step using existing dialogue_writer output
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from steps.script_formatter import ScriptFormatter
import json

def main():
    print("=" * 70)
    print("Testing ScriptFormatter Only")
    print("=" * 70)
    
    # Use the dialogue_writer output from previous run
    dialogue_file = Path("outputs/test_steps_3-6/dialogue_writer_112332.json")
    
    if not dialogue_file.exists():
        print(f"✗ Dialogue file not found: {dialogue_file}")
        return
    
    print(f"\n📂 Loading dialogue from: {dialogue_file.name}")
    with open(dialogue_file, 'r', encoding='utf-8') as f:
        dialogue_data = json.load(f)
    
    print(f"✓ Loaded dialogue data ({len(json.dumps(dialogue_data)):,} chars)")
    
    # Run ScriptFormatter
    print("\n" + "=" * 70)
    print("STEP: ScriptFormatter")
    print("=" * 70)
    try:
        script_formatter = ScriptFormatter()
        script_result = script_formatter.execute(dialogue_data)
        
        # Handle dict or string result
        if isinstance(script_result, dict):
            script_text = script_result.get('combined_script', script_result.get('script', ''))
            print(f"  ℹ️ Result is dict with keys: {list(script_result.keys())}")
        else:
            script_text = script_result
        
        # Save to file
        output_file = Path("outputs/test_steps_3-6/script_formatter_test.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script_text)
        
        print(f"✓ ScriptFormatter complete")
        print(f"  Output: {output_file}")
        print(f"  Size: {len(script_text):,} chars")
        
        # Show preview
        print("\n" + "=" * 70)
        print("PREVIEW (first 1000 chars):")
        print("=" * 70)
        print(script_text[:1000])
        
    except Exception as e:
        print(f"✗ ScriptFormatter failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n" + "=" * 70)
    print("✓ COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
