"""
Test script for prompt builder metadata refactoring
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import PromptBuilderV2

# Create output directory relative to tests folder
output_dir = Path(__file__).parent / "test_outputs"
output_dir.mkdir(exist_ok=True)

# Test with lesson_generator prompt
print("="*70)
print("Testing Prompt Builder with Metadata")
print("="*70)

# Create builder with verbose mode
builder = PromptBuilderV2(module_number=1, path_letter='a', verbose=True)

# Build the prompt and save to file
save_path = output_dir / "lesson_generator_test.md"
print(f"\nBuilding prompt and saving to: {save_path}\n")

try:
    result = builder.build(
        prompt_name='lesson_generator',
        variables={},
        input_content="""<lesson>
Test lesson content here.
This is just a test to verify the metadata works.
</lesson>""",
        save_prompt_to=str(save_path)
    )

    print("\n" + "="*70)
    print("SUCCESS: Prompt built successfully!")
    print("="*70)
    print(f"\n[OK] System blocks created: {len(result['system'])}")
    print(f"[OK] User message length: {len(result['user_message'])} chars")
    print(f"[OK] Saved prompt to: {save_path}")

    # Check metadata
    print("\n" + "-"*70)
    print("Block Metadata Summary:")
    print("-"*70)
    for i, block in enumerate(result['system'], 1):
        metadata = block.get('metadata', {})
        block_type = metadata.get('block_type', 'unknown')
        block_name = metadata.get('block_name', '')
        cached = '[CACHED]' if 'cache_control' in block else ''

        print(f"Block {i}: {block_type:20s} {block_name:30s} {cached}")

    print("\n[OK] Please check the saved file to see the enhanced format!")
    print(f"  Open: {save_path}")

except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
