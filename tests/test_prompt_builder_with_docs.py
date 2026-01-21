"""
Test script for prompt builder with documentation references
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import PromptBuilderV2, Prompt

# Create output directory relative to tests folder
output_dir = Path(__file__).parent / "test_outputs"
output_dir.mkdir(exist_ok=True)

# Test with a simple prompt that has doc_refs
print("="*70)
print("Testing Prompt Builder with Documentation References")
print("="*70)

# Create builder with verbose mode for module 1 path b (which has visuals.md)
builder = PromptBuilderV2(module_number=1, path_letter='b', verbose=True)

# Create a test prompt with doc_refs
test_prompt = Prompt(
    role="You are a test assistant.",
    instructions="Process the input data.",
    doc_refs=['visuals.md', 'visual_guide.md'],  # These exist in module1/pathb
    examples=[
        {
            "description": "Example 1: Simple test",
            "output": "Test output"
        }
    ],
    output_structure="""Expected output format:
{
    "result": "value"
}""",
    cache_docs=True,
    cache_ttl="5m"
)

# Save it as a test prompt
import sys
sys.modules['test_doc_prompt'] = type(sys)('test_doc_prompt')
sys.modules['test_doc_prompt'].TEST_DOC_PROMPT_PROMPT = test_prompt

# Build the prompt and save to file
save_path = output_dir / "test_with_docs.md"
print(f"\nBuilding prompt and saving to: {save_path}\n")

try:
    result = builder.build(
        prompt_name='test_doc_prompt',
        variables={},
        input_content="""Test input content here.""",
        save_prompt_to=str(save_path)
    )

    print("\n" + "="*70)
    print("SUCCESS: Prompt built successfully!")
    print("="*70)
    print(f"\n[OK] System blocks created: {len(result['system'])}")

    # Check metadata
    print("\n" + "-"*70)
    print("Block Metadata Summary:")
    print("-"*70)
    for i, block in enumerate(result['system'], 1):
        metadata = block.get('metadata', {})
        block_type = metadata.get('block_type', 'unknown')
        block_name = metadata.get('block_name', '')
        purpose = metadata.get('purpose', '')
        cached = '[CACHED]' if 'cache_control' in block else ''

        display_name = f" ({block_name})" if block_name else ""
        print(f"Block {i}: {block_type:20s}{display_name:35s} {cached}")
        if purpose:
            print(f"         Purpose: {purpose}")

    print("\n[OK] Saved file shows enhanced format with doc metadata!")
    print(f"  Open: {save_path}")

except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
