"""
Test that prompts are restructured correctly with input in user message
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import PromptBuilderV2

# Create output directory
output_dir = Path(__file__).parent / "test_outputs"
output_dir.mkdir(exist_ok=True)

print("="*70)
print("Testing Prompt Restructure: Input in User Message")
print("="*70)

# Test warmup_generator
builder = PromptBuilderV2(module_number=1, path_letter='c', verbose=True)

test_input = """# Warmup Specs

## Interaction 1
Test interaction content here.
"""

save_path = output_dir / "warmup_generator_restructured.md"
print(f"\nBuilding warmup_generator prompt with input_content...")
print(f"Saving to: {save_path}\n")

try:
    result = builder.build(
        prompt_name='warmup_generator',
        variables={},
        input_content=test_input,
        save_prompt_to=str(save_path)
    )

    print("\n" + "="*70)
    print("SUCCESS: Prompt built successfully!")
    print("="*70)
    print(f"\n[OK] System blocks created: {len(result['system'])}")
    print(f"[OK] User message length: {len(result['user_message'])} chars")

    # Check structure
    print("\n" + "-"*70)
    print("System Block Structure (should all be static):")
    print("-"*70)
    for i, block in enumerate(result['system'], 1):
        metadata = block.get('metadata', {})
        block_type = metadata.get('block_type', 'unknown')
        block_name = metadata.get('block_name', '')
        cacheable = metadata.get('cacheable', True)
        cached = '[CACHED]' if 'cache_control' in block else ''

        name_str = f" ({block_name})" if block_name else ""
        print(f"Block {i}: {block_type:20s}{name_str:35s} cacheable={cacheable} {cached}")

    # Check user message structure
    print("\n" + "-"*70)
    print("User Message Structure:")
    print("-"*70)
    has_input = '<input>' in result['user_message']
    has_instructions = 'Convert each of the interactions' in result['user_message']

    print(f"[{'OK' if has_input else 'FAIL'}] Contains <input> tag")
    print(f"[{'OK' if has_instructions else 'FAIL'}] Contains task instructions")

    if has_input and has_instructions:
        input_before_instructions = result['user_message'].index('<input>') < result['user_message'].index('Convert')
        print(f"[{'OK' if input_before_instructions else 'FAIL'}] Input comes before instructions")

    # Verify no warmup_specs in system blocks
    print("\n" + "-"*70)
    print("Verification:")
    print("-"*70)

    warmup_specs_in_system = any('warmup_specs' in block.get('text', '') for block in result['system'])
    print(f"[{'FAIL' if warmup_specs_in_system else 'OK'}] warmup_specs NOT in system blocks")

    visuals_in_system = any('visuals' in block.get('text', '') for block in result['system'])
    print(f"[{'OK' if visuals_in_system else 'FAIL'}] visuals IS in system blocks (reference doc)")

    print("\n" + "="*70)
    print("Check the saved file to see the restructured format!")
    print(f"Open: {save_path}")
    print("="*70)

except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
