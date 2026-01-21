"""
Test FINAL structure: Task in system, Input in user message
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
print("Testing FINAL Structure: Task in System, Input in User")
print("="*70)

builder = PromptBuilderV2(module_number=1, path_letter='c', verbose=True)

test_input = """# Warmup Specs

## Interaction 1: Identify Equal Parts
Student sees 3 rectangles...
"""

save_path = output_dir / "final_structure.md"
print(f"\nBuilding warmup_generator with FINAL structure...")
print(f"Saving to: {save_path}\n")

try:
    result = builder.build(
        prompt_name='warmup_generator',
        variables={},
        input_content=test_input,
        save_prompt_to=str(save_path)
    )

    print("\n" + "="*70)
    print("FINAL STRUCTURE")
    print("="*70)

    # Check system blocks
    print("\n[SYSTEM BLOCKS - All static, fully cacheable]")
    print("-"*70)
    for i, block in enumerate(result['system'], 1):
        metadata = block.get('metadata', {})
        block_type = metadata.get('block_type', 'unknown')
        block_name = metadata.get('block_name', '')
        cached = '[CACHED]' if 'cache_control' in block else ''

        name_str = f" ({block_name})" if block_name else ""
        print(f"  {i}. {block_type:20s}{name_str:30s} {cached}")

    # Check user message
    print("\n[USER MESSAGE - Dynamic, changes per request]")
    print("-"*70)
    has_input = '<input>' in result['user_message']
    has_instructions = 'Convert each of the interactions' in result['user_message']

    if has_input:
        print("  [OK] Contains <input> tag")
    else:
        print("  [FAIL] Missing <input> tag")

    if has_instructions:
        print("  [FAIL] Contains instructions (SHOULD BE IN SYSTEM!)")
    else:
        print("  [OK] Does NOT contain instructions (correct!)")

    # Verify instructions are in system
    instructions_in_system = any(
        metadata.get('block_type') == 'instructions'
        for block in result['system']
        for metadata in [block.get('metadata', {})]
    )

    print("\n[VERIFICATION]")
    print("-"*70)
    if instructions_in_system:
        print("  [OK] Task instructions are in SYSTEM blocks")
    else:
        print("  [FAIL] Task instructions NOT in system blocks")

    if has_input and not has_instructions and instructions_in_system:
        print("\n" + "="*70)
        print("  SUCCESS! PERFECT STRUCTURE!")
        print("="*70)
        print("  System: Role -> Docs -> TASK -> Examples -> Output [CACHED]")
        print("  User:   Just the input data")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("  FAIL! STRUCTURE INCORRECT")
        print("="*70)

    print(f"\nCheck saved file: {save_path}")

except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
