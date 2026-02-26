"""
Pipelines - CLI runner for pipelines

Usage:
    python cli/run_pipeline.py [OPTIONS]

Options:
    -p, --pipeline <name|number>  Pipeline name or number to run
    -m, --module <number>         Module number (optional)
    --path <letter>               Path letter (a/b/c) (optional)
    -i, --interactive             Enable interactive mode (step-by-step confirmation)
    -h, --help                    Show this help message

Examples:
    python cli/run_pipeline.py -p 1 -m 5 --path a -i
    python cli/run_pipeline.py --pipeline "GODOT Formatter" --module 3
    python cli/run_pipeline.py -p 2

Note: Pipelines are now centralized in ui/saved_pipelines.json
      Edit pipelines through the UI or directly in the JSON file
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))

from core.pipeline import run_pipeline
from config.pipelines import PIPELINES


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Run pipelines with optional parameters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli/run_pipeline.py -p 1 -m 5 --path a -i
  python cli/run_pipeline.py --pipeline "GODOT Formatter" --module 3
  python cli/run_pipeline.py -p 2
        """
    )

    parser.add_argument(
        '-p', '--pipeline',
        type=str,
        help='Pipeline name or number to run'
    )
    parser.add_argument(
        '-m', '--module',
        type=int,
        help='Module number (optional)'
    )
    parser.add_argument(
        '--path',
        type=str,
        choices=['a', 'b', 'c'],
        help='Path letter: a, b, or c (optional)'
    )
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Enable interactive mode (step-by-step confirmation)'
    )
    parser.add_argument(
        '--batch-ids',
        type=str,
        help='Only run these batch IDs (comma-separated, e.g., "1,3,5" or "template_001,template_003")'
    )
    parser.add_argument(
        '--skip-batch-ids',
        type=str,
        help='Skip these batch IDs (comma-separated, e.g., "2,4" or "template_002,template_004")'
    )

    args = parser.parse_args()

    print("Pipeline Runner")
    print("="*70)

    # Determine pipeline name
    pipeline_name = None

    if args.pipeline:
        # Check if it's a number
        if args.pipeline.isdigit():
            pipeline_num = int(args.pipeline)
            if 1 <= pipeline_num <= len(PIPELINES):
                pipeline_name = list(PIPELINES.keys())[pipeline_num - 1]
            else:
                print(f"Invalid pipeline number: {args.pipeline}")
                print(f"Valid range: 1-{len(PIPELINES)}")
                sys.exit(1)
        # Check if it's a valid pipeline name
        elif args.pipeline in PIPELINES:
            pipeline_name = args.pipeline
        else:
            print(f"Invalid pipeline name: {args.pipeline}")
            print("\nAvailable pipelines:")
            for i, name in enumerate(PIPELINES.keys(), 1):
                print(f"  {i}. {name}")
            sys.exit(1)
    else:
        # No pipeline specified, show options and prompt
        print("\nAvailable pipelines:")
        for i, name in enumerate(PIPELINES.keys(), 1):
            print(f"  {i}. {name}")

        choice = input(f"\nSelect pipeline [1-{len(PIPELINES)}]: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(PIPELINES):
            pipeline_name = list(PIPELINES.keys())[int(choice) - 1]
        elif choice in PIPELINES:
            pipeline_name = choice
        else:
            print(f"Invalid choice")
            sys.exit(1)

    # Get module number
    module_number = args.module
    if module_number is None:
        module_input = input("Module number (or Enter to skip): ").strip()
        module_number = int(module_input) if module_input else None

    # Get path letter
    path_letter = args.path
    if path_letter is None and module_number:
        path_input = input("Path letter (a/b/c or Enter to skip): ").strip().lower()
        path_letter = path_input if path_input in ['a', 'b', 'c'] else None

    # Get interactive mode preference
    interactive = args.interactive
    if not interactive:
        interactive_input = input("Enable interactive mode (step-by-step confirmation)? (y/n): ").strip().lower()
        interactive = interactive_input == 'y'

    # Parse batch ID filters
    batch_only_items = None
    if args.batch_ids:
        batch_only_items = [id.strip() for id in args.batch_ids.split(',')]
        print(f"  [BATCH FILTER] Only running IDs: {batch_only_items}")

    batch_skip_items = None
    if args.skip_batch_ids:
        batch_skip_items = [id.strip() for id in args.skip_batch_ids.split(',')]
        print(f"  [BATCH FILTER] Skipping IDs: {batch_skip_items}")

    # Apply batch skip items to steps if specified
    steps = PIPELINES[pipeline_name].copy() if isinstance(PIPELINES[pipeline_name], list) else list(PIPELINES[pipeline_name])
    if batch_skip_items:
        for step in steps:
            if isinstance(step, dict) and step.get('batch_mode'):
                # Merge with existing skip items
                existing_skip = step.get('batch_skip_items', [])
                step['batch_skip_items'] = list(set(existing_skip + batch_skip_items))

    # Run pipeline
    try:
        print(f"\nRunning pipeline: {pipeline_name}")
        if module_number:
            print(f"Module: {module_number}")
        if path_letter:
            print(f"Path: {path_letter}")
        if batch_only_items:
            print(f"Batch filter (only): {', '.join(batch_only_items)}")
        if batch_skip_items:
            print(f"Batch filter (skip): {', '.join(batch_skip_items)}")
        print(f"Interactive mode: {'enabled' if interactive else 'disabled'}")

        results = run_pipeline(
            steps=steps,
            pipeline_name=pipeline_name,
            module_number=module_number,
            path_letter=path_letter,
            verbose=True,
            interactive=interactive,
            rerun_items=batch_only_items  # Use rerun_items for batch filtering
        )

        print("\n" + "="*70)
        print("RESULTS:")
        print("="*70)
        for key, value in results.items():
            # Skip printing final_output to avoid console clutter (it's saved to file)
            if key == 'final_output':
                continue

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