"""
Rerun CLI - Rerun specific items or steps from a pipeline

Supports two rerun modes:
1. Item-level reruns: Rerun specific items within batch steps
2. Step-level reruns: Rerun specific step ranges

Usage:
    # Rerun specific items (existing functionality)
    python rerun.py problem_generator 4001 4005 4012 --base v2

    # Rerun from step 3 onwards
    python rerun.py problem_generator --start-from 3 --module 4 --path a

    # Rerun only step 3
    python rerun.py problem_generator --start-from 3 --end-at 3 --module 4

    # Combine: rerun items 4001, 4005 within step range 2-4
    python rerun.py problem_generator 4001 4005 --start-from 2 --end-at 4
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))

from core.pipeline import run_pipeline
from core.version_manager import get_latest_version
from core.path_manager import get_project_paths
from config.pipelines import PIPELINES
import json


def main():
    parser = argparse.ArgumentParser(
        description="Rerun specific items or steps from a pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Item-level reruns (rerun specific batch items)
  python rerun.py problem_generator 4001 4005 4012
  python rerun.py problem_generator 4001 --base v2 --note "Fixed prompt"

  # Step-level reruns (skip to step N)
  python rerun.py problem_generator --start-from 3 --module 4 --path a
  python rerun.py problem_generator --start-from 3 --end-at 3 --module 4
  python rerun.py problem_generator --start-from sequence_structurer --module 4

  # Combined (rerun items within step range)
  python rerun.py problem_generator 4001 4005 --start-from 2 --end-at 4
        """
    )
    parser.add_argument("pipeline_name", help="Name of the pipeline")
    parser.add_argument("item_ids", nargs="*", help="Item IDs to rerun (for batch steps)")

    # Rerun options
    parser.add_argument("--base", default=None, help="Base version to rerun from (default: latest)")
    parser.add_argument("--note", default="", help="Optional note about this rerun")

    # Step range options
    parser.add_argument("--start-from", help="Start from step N (int or name)")
    parser.add_argument("--end-at", help="End at step N (int or name)")

    # Module/path context (required for step-level reruns)
    parser.add_argument("--module", type=int, help="Module number")
    parser.add_argument("--path", choices=['a', 'b', 'c'], help="Path letter")

    # Other
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--status", help="Pipeline status (alpha/beta/rc/final)")

    args = parser.parse_args()

    # Validate pipeline exists
    if args.pipeline_name not in PIPELINES:
        print(f"Error: Pipeline '{args.pipeline_name}' not found")
        print(f"Available pipelines:")
        for p in PIPELINES.keys():
            print(f"  - {p}")
        sys.exit(1)

    # Get pipeline steps
    steps = PIPELINES[args.pipeline_name]

    # Build full pipeline name for path resolution
    full_pipeline_name = args.pipeline_name
    if args.module:
        full_pipeline_name += f"_module_{args.module}"
    if args.path:
        full_pipeline_name += f"_path_{args.path.lower()}"

    # Get base version
    base_version = args.base
    if base_version is None:
        outputs_dir = get_project_paths()['outputs']
        pipeline_dir = outputs_dir / full_pipeline_name
        base_version = get_latest_version(pipeline_dir)

        if base_version is None:
            print(f"Error: No versions found for '{full_pipeline_name}'")
            print(f"Run the full pipeline first before attempting a rerun.")
            sys.exit(1)

    # Determine rerun mode
    has_item_ids = len(args.item_ids) > 0
    has_step_range = args.start_from is not None or args.end_at is not None

    # Validate combinations
    if has_step_range and not args.module:
        print("Error: --module required when using --start-from or --end-at")
        sys.exit(1)

    # Convert numeric step references to int
    start_from = args.start_from
    if start_from and start_from.isdigit():
        start_from = int(start_from)

    end_at = args.end_at
    if end_at and end_at.isdigit():
        end_at = int(end_at)

    # Show confirmation
    print(f"\n{'='*70}")
    print(f"RERUN: {full_pipeline_name}")
    print(f"{'='*70}")
    print(f"Base version: {base_version}")

    if has_step_range:
        if start_from:
            print(f"Start from: {start_from}")
        if end_at:
            print(f"End at: {end_at}")
        if not start_from and not end_at:
            print(f"Steps: All (full pipeline)")
    else:
        print(f"Steps: All (full pipeline)")

    if has_item_ids:
        print(f"Items: {', '.join(args.item_ids)}")
    else:
        print(f"Items: All (full rerun)")

    if args.note:
        print(f"Note: {args.note}")
    print(f"{'='*70}\n")

    response = input("Proceed with rerun? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)

    # Run pipeline with rerun parameters
    try:
        results = run_pipeline(
            steps=steps,
            pipeline_name=args.pipeline_name,
            module_number=args.module,
            path_letter=args.path,
            base_version=base_version,
            rerun_items=args.item_ids if has_item_ids else None,
            start_from_step=start_from,
            end_at_step=end_at,
            notes=args.note,
            pipeline_status=args.status,
            verbose=True
        )

        print("\n" + "="*70)
        print("RERUN COMPLETE")
        print("="*70)

        if 'metadata' in results:
            meta = results['metadata']
            print(f"\nNew version: {meta.get('version')}")
            print(f"Mode: {meta.get('mode')}")
            if meta.get('step_range'):
                print(f"Steps executed: {meta.get('step_range')}")
            print(f"Duration: {meta.get('duration_seconds', 0):.1f}s")

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
