"""
Test prompt_builder to see why module_utils isn't working
"""

from core.prompt_builder import PromptBuilderV2

# Create a builder with module_number set
builder = PromptBuilderV2(module_number=1, path_letter='a', verbose=True)

# Try to fetch module data
print("Testing module data fetch...")
print("=" * 60)

try:
    # Test the _fetch_module_data method directly
    variables = {}
    result = builder._fetch_module_data(["phases.0"], variables)
    print("\nSuccess!")
    print(f"Variables: {result}")
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
