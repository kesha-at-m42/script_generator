"""
Pipelines - CLI runner for pipelines

Usage:
    python cli/run_pipeline.py [OPTIONS]

Options:
    -p, --pipeline <name|number>  Pipeline name or number to run
    -u, --unit <number>           Unit number (optional)
    -m, --module <number>         Module number (optional)
    --path <letter>               Path letter (a/b/c) (optional)
    -i, --interactive             Enable interactive mode (step-by-step confirmation)
    --start-from <step>           Start from this step (number or name)
    --end-at <step>               Stop after this step (number or name)
    --batch-ids <ids>             Only run these batch IDs (comma-separated)
    --skip-batch-ids <ids>        Skip these batch IDs (comma-separated)
    -y, --yes                     Skip all confirmation prompts
    --note <text>                 Note about this run
    --status <label>              Pipeline status (alpha/beta/rc/final)
    --test-push                   Push to a temporary Notion page (registry not updated)
    -h, --help                    Show this help message

Examples:
    python cli/run_pipeline.py -p 1 -m 5 --path a -i
    python cli/run_pipeline.py --pipeline "GODOT Formatter" --module 3
    python cli/run_pipeline.py -p 2

Note: Pipelines are centralized in ui/saved_pipelines.json.
      Edit pipelines through the UI or directly in the JSON file.
"""

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))

from core.pipeline import (  # noqa: E402
    add_common_pipeline_args,
    apply_yes_flag,
    parse_batch_filter_arg,
    parse_step_ref_arg,
    prompt_for_pipeline,
    prompt_for_run_context,
    resolve_pipeline_name,
)
from core.pipelines import PIPELINES, run_pipeline_from_config  # noqa: E402

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run pipelines with optional parameters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli/run_pipeline.py -p 1 -m 5 --path a -i
  python cli/run_pipeline.py --pipeline "GODOT Formatter" --module 3
  python cli/run_pipeline.py -p 2
        """,
    )

    add_common_pipeline_args(parser)
    parser.add_argument(
        "--batch-ids",
        type=str,
        help='Only run these batch IDs (comma-separated, e.g. "1,3,5" or "template_001")',
    )
    parser.add_argument(
        "--skip-batch-ids",
        type=str,
        help='Skip these batch IDs (comma-separated, e.g. "2,4")',
    )
    parser.add_argument(
        "--test-push",
        action="store_true",
        help="Push to a new temporary Notion page without updating the registry",
    )

    args = parser.parse_args()

    apply_yes_flag(args)

    print("Pipeline Runner")
    print("=" * 70)

    # Resolve pipeline name
    if args.pipeline:
        pipeline_name = resolve_pipeline_name(args.pipeline, PIPELINES)
    else:
        pipeline_name = prompt_for_pipeline(PIPELINES)

    # Fill in unit / module / path / interactive interactively if not provided
    prompt_for_run_context(args)

    # Parse batch ID filters
    batch_only_items = parse_batch_filter_arg(args.batch_ids)
    batch_skip_items = parse_batch_filter_arg(args.skip_batch_ids)

    if batch_only_items:
        print(f"  [BATCH FILTER] Only running IDs: {batch_only_items}")
    if batch_skip_items:
        print(f"  [BATCH FILTER] Skipping IDs: {batch_skip_items}")

    # Run pipeline
    try:
        print(f"\nRunning pipeline: {pipeline_name}")
        if args.unit:
            print(f"Unit: {args.unit}")
        if args.module:
            print(f"Module: {args.module}")
        if args.path:
            print(f"Path: {args.path}")
        if batch_only_items:
            print(f"Batch filter (only): {', '.join(batch_only_items)}")
        if batch_skip_items:
            print(f"Batch filter (skip): {', '.join(batch_skip_items)}")
        print(f"Interactive mode: {'enabled' if args.interactive else 'disabled'}")

        start_at = parse_step_ref_arg(args.start_from)
        end_at = parse_step_ref_arg(args.end_at)

        steps_config = list(PIPELINES[pipeline_name])
        if args.test_push:
            import copy
            steps_config = copy.deepcopy(steps_config)
            for s in steps_config:
                fn = str(getattr(s, "function", "") or "")
                if "notion_push" in fn:
                    s.function_args = {**getattr(s, "function_args", {}), "test_push": True}
            print("  [TEST PUSH] Will create a temporary Notion page (registry not updated)")

        results = run_pipeline_from_config(
            steps_config=steps_config,
            pipeline_name=pipeline_name,
            unit_number=args.unit,
            module_number=args.module,
            path_letter=args.path,
            verbose=True,
            interactive=args.interactive,
            rerun_items=batch_only_items,
            start_from_step=start_at,
            end_at_step=end_at,
        )

        print("\n" + "=" * 70)
        print("RESULTS:")
        print("=" * 70)
        for key, value in results.items():
            # Skip printing final_output to avoid console clutter (it's saved to file)
            if key == "final_output":
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
