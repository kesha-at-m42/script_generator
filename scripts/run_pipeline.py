"""
Pipelines - Define and run your pipelines here

Usage:
    python pipeline_runner.py
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.pipeline import Step, run_pipeline


# =============================================================================
# DEFINE YOUR PIPELINES HERE
# =============================================================================

PIPELINES = {
    "test": [
        Step(
            prompt_name='test',
            variables={'name': 'Kesha'},
            output_file='greeting.txt'
        ),
        Step(
            prompt_name='test_2',
            # No input_file specified - auto-chains from greeting.txt
            # Content will be available in <input> section of system prompt
            output_file='response.txt'
        )
    ],
    "warmupscript_generator": [
        Step(
            prompt_name='warmup_generator',
            output_file='warmup.json'
        ),
        Step(
            prompt_name='interaction_generator',
            output_file='interactions.json'
        ),
        Step(
          function="script_formatter.format_interactions_to_markdown",
          output_file="script.md"
      )
    ],
    "lessonscript_generator": [
        Step(
            prompt_name='lesson_generator',
            output_file='lesson.json'
        ),
        Step(
            prompt_name='interaction_generator',
            output_file='interactions.json'
        ),
        Step(
          function="script_formatter.format_interactions_to_markdown",
          output_file="script.md"
      )
    ],

    # Example: Human-in-loop workflow with auto-chaining
    # "draft_refine": [
    #     Step(
    #         prompt_name='generate_draft',
    #         variables={'topic': 'AI safety'},
    #         output_file='draft.txt'
    #     ),
    #     # PAUSE HERE: Human can edit draft.txt before continuing
    #     Step(
    #         prompt_name='refine_draft',
    #         # No input_file - auto-chains from draft.txt
    #         # Edited content available in <input> section
    #         output_file='refined.txt'
    #     ),
    # ],

    # Example: Explicit input file (override auto-chain)
    # "from_existing": [
    #     Step(
    #         prompt_name='analyze',
    #         input_file='inputs/docs/existing_doc.txt',
    #         output_file='analysis.txt'
    #     ),
    # ],

    # Example: Three-step chain
    # "multi_step": [
    #     Step(
    #         prompt_name='step1',
    #         variables={'seed': 'robots'},
    #         output_file='step1.txt'
    #     ),
    #     Step(
    #         prompt_name='step2',
    #         # Auto-chains from step1.txt
    #         output_file='step2.txt'
    #     ),
    #     Step(
    #         prompt_name='step3',
    #         # Auto-chains from step2.txt
    #         output_file='final.txt'
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

    # Ask for interactive mode
    interactive_input = input("Enable interactive mode (step-by-step confirmation)? (y/n): ").strip().lower()
    interactive = interactive_input == 'y'

    # Run pipeline
    try:
        print(f"\nRunning pipeline: {pipeline_name}")

        results = run_pipeline(
            steps=PIPELINES[pipeline_name],
            pipeline_name=pipeline_name,
            module_number=module_number,
            path_letter=path_letter,
            verbose=True,
            interactive=interactive
        )

        print("\n" + "="*70)
        print("RESULTS:")
        print("="*70)
        for key, value in results.items():
            print(f"\n{key}:")
            if isinstance(value, str):
                preview = value[:200] if len(value) > 200 else value
                print(preview)
                if len(value) > 200:
                    print("...")
            else:
                print(value)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)