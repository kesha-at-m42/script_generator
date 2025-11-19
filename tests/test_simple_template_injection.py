import sys
import os
from pathlib import Path

# Add paths relative to script_generator root
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir / "utils"))
sys.path.insert(0, str(root_dir / "core"))

from problem_template_utils import get_fields_by_reference
import traceback
from prompt_builder_old import PromptBuilder

"""
Simple test for problem template field injection
"""


# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

# Add necessary paths
sys.path.insert(0, str(Path(__file__).parent / "core"))
sys.path.insert(0, str(Path(__file__).parent / "utils"))


def test_get_fields_by_reference():
    """Test the get_fields_by_reference function directly"""

    print("\n" + "=" * 70)
    print("TEST 1: Direct field fetching from problem_templates.json")
    print("=" * 70)

    # Test with INTERACTION_DESIGNER_TEMPLATE_REF = ["tools_available"]
    INTERACTION_DESIGNER_TEMPLATE_REF = ["tools_available"]

    print(f"\nFetching fields: {INTERACTION_DESIGNER_TEMPLATE_REF}")
    print(f"From: Module 1, Goal 1")

    try:
        fields = get_fields_by_reference(1, 1, INTERACTION_DESIGNER_TEMPLATE_REF)
        print(f"\nResult: {fields}")

        if "tools_available" in fields:
            print(f"SUCCESS: 'tools' field fetched: {fields['tools']}")
        else:
            print("FAIL: 'tools' field not in result")

    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        return False

    return True


def test_multiple_goals():
    """Test with different goals to see different tools"""

    print("\n" + "=" * 70)
    print("TEST 2: Fetching tools for different goals")
    print("=" * 70)

    TEMPLATE_REF = ["tools_available", "cognitive_type"]

    for goal_id in [1, 2, 3, 4, 5, 6]:
        try:
            fields = get_fields_by_reference(1, goal_id, TEMPLATE_REF)
            print(f"\nGoal {goal_id}:")
            print(f"  Tools: {fields.get('tools')}")
            print(f"  Cognitive Type: {fields.get('cognitive_type')}")
        except Exception as e:
            print(f"\nGoal {goal_id}: ERROR - {e}")


def test_prompt_builder_old_integration():
    """Test that prompt builder can load the config with problem_template_ref"""

    print("\n" + "=" * 70)
    print("TEST 3: Prompt Builder Integration")
    print("=" * 70)

    try:

        # Create builder with verbose=False to avoid emoji issues
        builder = PromptBuilder(module_number=1, path_letter="a", verbose=False)

        print("\nChecking if interaction_designer config has problem_template_ref...")

        # Get the config
        config = builder._get_prompt_config("interaction_designer")

        if "problem_template_ref" in config:
            print(f"SUCCESS: problem_template_ref found in config")
            print(f"  Value: {config['problem_template_ref']}")
        else:
            print("FAIL: problem_template_ref not in config")
            print(f"  Available keys: {list(config.keys())}")

    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        return False

    return True


def test_full_integration():
    """Test the full integration with prompt building"""

    print("\n" + "=" * 70)
    print("TEST 4: Full Integration - Build Prompt with Auto-Fetch")
    print("=" * 70)

    try:

        # Check if _auto_fetch_problem_template_data method exists
        builder = PromptBuilder(module_number=1, path_letter="a", verbose=False)

        if hasattr(builder, '_auto_fetch_problem_template_data'):
            print("SUCCESS: _auto_fetch_problem_template_data method exists")

            # Test calling it directly
            print("\nTesting direct call to _auto_fetch_problem_template_data...")
            variables = {}
            result = builder._auto_fetch_problem_template_data(
                ["tools_available", "remediations_per_step.0.0.scaffolding_level"],
                1,
                variables
            )

            print(f"Result variables: {result}")

            if "tools_available" in result:
                print(f"SUCCESS: tools auto-fetched: {result['tools']}")
            if "remediations_per_step.0.0.scaffolding_level" in result:
                print(f"SUCCESS: remediations_per_step.0.0.scaffolding_level auto-fetched: {result['remediations_per_step.0.0.scaffolding_level']}")

        else:
            print("FAIL: _auto_fetch_problem_template_data method not found")
            return False

    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        return False

    return True


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("         PROBLEM TEMPLATE INJECTION - SIMPLE TEST")
    print("=" * 70)

    # Run all tests
    test1 = test_get_fields_by_reference()
    test2 = test_multiple_goals()
    test3 = test_prompt_builder_old_integration()
    test4 = test_full_integration()

    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Test 1 (Field Fetching): {'PASS' if test1 else 'FAIL'}")
    print(f"Test 3 (Config Integration): {'PASS' if test3 else 'FAIL'}")
    print(f"Test 4 (Full Integration): {'PASS' if test4 else 'FAIL'}")
    print("=" * 70)
