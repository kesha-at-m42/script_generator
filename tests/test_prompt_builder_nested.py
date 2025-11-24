"""
Test prompt_builder with various nested field patterns
"""

from core.prompt_builder import PromptBuilderV2

# Create a builder with module_number set
builder = PromptBuilderV2(module_number=1, path_letter='a', verbose=True)

print("Testing various nested field patterns...")
print("=" * 60)

# Test cases
test_cases = [
    ["phases.0"],
    ["phases.0.phase_name"],
    ["phases.0.purpose"],
    ["phases.1.vocabulary_introduced_in_order"],
    ["phases.*.phase_name"],
    ["standards.addressing"],
    ["misconceptions.0.misconception"],
]

for fields in test_cases:
    print(f"\n\nTest: {fields}")
    print("-" * 60)
    try:
        variables = {}
        result = builder._fetch_module_data(fields, variables)
        print(f"[OK] Success!")
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"[ERROR] Error: {e}")
