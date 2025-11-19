"""
Test to verify prefill is being generated and used
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "core"))
sys.path.insert(0, str(Path(__file__).parent / "utils"))

from prompt_builder_old import PromptBuilder
from prefill_generator import generate_prefill

# Test data
test_question = {
    "goal_id": 1,
    "goal_text": "The student can partition shapes into equal parts",
    "question_id": 1,
    "question_prompt": "Divide the bar into 2 equal parts.",
    "cognitive_type": "CREATE",
    "difficulty_level": 0,
    "variables_used": {"fractions": "1/2"}
}

print("=" * 70)
print("TEST: Prefill Generation for Interaction Designer")
print("=" * 70)

# Test 1: Check if generate_prefill works
print("\n1. Testing generate_prefill function directly:")
prefill_from_generator = generate_prefill("interaction_designer", test_question)
print(f"Generated prefill:\n{prefill_from_generator}")

# Test 2: Check prompt builder
print("\n" + "=" * 70)
print("2. Testing PromptBuilder with interaction_designer:")
print("=" * 70)

builder = PromptBuilder(module_number=1, path_letter="a", verbose=True)

result = builder.build_prompt(
    prompt_id="interaction_designer",
    variables={
        "question_data": test_question,
        "goal_id": 1
    }
)

if isinstance(result, tuple):
    prompt, prefill = result
    print(f"\n✓ Prompt builder returned a tuple (prompt, prefill)")
    print(f"  Prompt length: {len(prompt)} chars")
    print(f"  Prefill: {prefill if prefill else 'None'}")

    if prefill:
        print(f"\n  Prefill content (first 300 chars):")
        print(f"  {prefill[:300]}")
        print("\n✓ PREFILL IS WORKING!")
    else:
        print("\n✗ PREFILL IS NONE - Not working")
else:
    print(f"\n✗ Prompt builder returned only prompt, no prefill")
    print(f"  Result type: {type(result)}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
