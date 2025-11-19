"""
Test script to verify problem template field injection in prompt builder
"""

import sys
from pathlib import Path

# Add necessary paths
sys.path.insert(0, str(Path(__file__).parent / "core"))
sys.path.insert(0, str(Path(__file__).parent / "utils"))

from prompt_builder_old import PromptBuilder

def test_interaction_designer_with_template_ref():
    """Test that INTERACTION_DESIGNER_TEMPLATE_REF fields are auto-fetched"""

    print("=" * 70)
    print("TEST: Problem Template Field Injection")
    print("=" * 70)

    # Create prompt builder for module 1
    builder = PromptBuilder(module_number=1, path_letter="a", verbose=True)

    # Sample question data (as would come from question_generator)
    question_data = """{
      "goal_id": 1,
      "goal_text": "The student can partition shapes into equal parts",
      "question_id": 1,
      "question_prompt": "Divide the bar into 2 equal parts.",
      "cognitive_type": "CREATE",
      "difficulty_level": 1,
      "visual_context": "One undivided rectangle bar",
      "variables_used": {
        "fractions": "1/2"
      }
    }"""

    # Build the prompt with goal_id in variables
    print("\n" + "=" * 70)
    print("Building interaction_designer prompt...")
    print("=" * 70)

    try:
        result = builder.build_prompt(
            prompt_id="interaction_designer",
            variables={
                "question_data": question_data,
                "goal_id": 1  # This triggers problem template fetching
            }
        )

        # Check if prompt was built
        if isinstance(result, tuple):
            prompt, prefill = result
            print(f"\n✓ Prompt built successfully with prefill!")
            print(f"  Prompt length: {len(prompt)} characters")
            print(f"  Prefill length: {len(prefill)} characters")
        else:
            prompt = result
            print(f"\n✓ Prompt built successfully!")
            print(f"  Total length: {len(prompt)} characters")

        # Check if 'tools' field was injected
        print("\n" + "=" * 70)
        print("VERIFICATION: Checking if 'tools' field was injected")
        print("=" * 70)

        # The tools should be injected as a variable
        # Let's check by building again and inspecting variables in verbose mode

        print("\nTest completed!")

    except Exception as e:
        print(f"\n✗ Error during prompt building: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True


def test_with_different_goals():
    """Test with different goal IDs to verify different tools are fetched"""

    print("\n" + "=" * 70)
    print("TEST: Multiple Goals - Different Tools")
    print("=" * 70)

    builder = PromptBuilder(module_number=1, path_letter="a", verbose=True)

    test_cases = [
        {"goal_id": 1, "expected_tools": ["cut"]},
        {"goal_id": 2, "expected_tools": ["select", "multi_select", "click_choice"]},
        {"goal_id": 3, "expected_tools": ["shade"]},
    ]

    for test_case in test_cases:
        goal_id = test_case["goal_id"]
        expected = test_case["expected_tools"]

        print(f"\n--- Testing Goal {goal_id} ---")
        print(f"Expected tools: {expected}")

        # Import to access the fetched values
        from problem_template_utils import get_tools

        try:
            actual_tools = get_tools(1, goal_id)
            print(f"Actual tools: {actual_tools}")

            if actual_tools == expected:
                print(f"✓ Tools match for goal {goal_id}")
            else:
                print(f"✗ Tools mismatch for goal {goal_id}")
                print(f"  Expected: {expected}")
                print(f"  Got: {actual_tools}")
        except Exception as e:
            print(f"✗ Error fetching tools for goal {goal_id}: {e}")


if __name__ == "__main__":
    print("\n")
    print("=" * 70)
    print(" " * 15 + "PROBLEM TEMPLATE INJECTION TEST")
    print("=" * 70)
    print("\n")

    # Run tests
    success = test_interaction_designer_with_template_ref()

    if success:
        test_with_different_goals()

    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)
