"""
Pipelines - Define and run your pipelines here

Usage:
    python pipelines.py
"""

import sys
from pathlib import Path

# Add core directory to path
sys.path.insert(0, str(Path(__file__).parent / "core"))

from pipeline import Step, run_pipeline


# =============================================================================
# DEFINE YOUR PIPELINES HERE
# =============================================================================

PIPELINES = {
    "test": [
        Step(
            prompt_name='test',
            variables={'name': 'Alice'},
            output_key='greeting'
        ),
    ],

    # Example multi-step pipeline:
    # "my_pipeline": [
    #     Step(
    #         prompt_name='step1_prompt',
    #         variables={'input': 'data'},
    #         output_key='step1_result'
    #     ),
    #     Step(
    #         prompt_name='step2_prompt',
    #         variables={},  # Can use {step1_result} in the prompt
    #         output_key='step2_result'
    #     ),
    # ],
}


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Pipeline Runner")
    print("="*70)

    # Show available pipelines
    print("\nAvailable pipelines:")
    for i, name in enumerate(PIPELINES.keys(), 1):
        print(f"  {i}. {name}")

    # Get user choice
    choice = input(f"\nSelect pipeline [1-{len(PIPELINES)}]: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(PIPELINES):
        pipeline_name = list(PIPELINES.keys())[int(choice) - 1]
    elif choice in PIPELINES:
        pipeline_name = choice
    else:
        print(f"Invalid choice")
        sys.exit(1)

    # Get module/path (optional)
    module_input = input("Module number (or Enter to skip): ").strip()
    module_number = int(module_input) if module_input else None

    path_letter = None
    if module_number:
        path_input = input("Path letter (a/b/c): ").strip().lower()
        path_letter = path_input if path_input in ['a', 'b', 'c'] else None

    # Run pipeline
    try:
        print(f"\nRunning pipeline: {pipeline_name}")

        results = run_pipeline(
            steps=PIPELINES[pipeline_name],
            module_number=module_number,
            path_letter=path_letter,
            verbose=True
        )

        print("\n" + "="*70)
        print("RESULTS:")
        print("="*70)
        for key, value in results.items():
            print(f"\n{key}:")
            preview = value[:200] if len(value) > 200 else value
            print(preview)
            if len(value) > 200:
                print("...")

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
