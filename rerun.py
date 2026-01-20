"""
Rerun CLI - Rerun specific items from a pipeline

Usage:
    python rerun.py <pipeline_name> <item_ids> [--note "reason"]

Examples:
    python rerun.py problem_generator 4002
    python rerun.py problem_generator 4002 4007 4012
    python rerun.py problem_generator 4002 --note "Fixed prompt"
"""

import sys
import argparse
from pathlib import Path

# Add core directory to path
core_dir = Path(__file__).parent / "core"
if str(core_dir) not in sys.path:
    sys.path.insert(0, str(core_dir))

from pipeline import run_pipeline, Step, _get_latest_version
import json


def main():
    parser = argparse.ArgumentParser(
        description="Rerun specific items from a pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python rerun.py problem_generator 4002
  python rerun.py problem_generator 4002 4007 4012
  python rerun.py problem_generator 4002 --note "Fixed prompt issue"
  python rerun.py problem_generator 4002 --base v0
        """
    )
    parser.add_argument("pipeline_name", help="Name of the pipeline")
    parser.add_argument("item_ids", nargs="+", help="Item IDs to rerun (space-separated)")
    parser.add_argument("--note", default="", help="Optional note about this rerun")
    parser.add_argument("--base", default=None, help="Base version to rerun from (default: latest)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    # Get pipeline directory
    outputs_dir = Path(__file__).parent / "outputs"
    pipeline_dir = outputs_dir / args.pipeline_name

    if not pipeline_dir.exists():
        print(f"Error: Pipeline '{args.pipeline_name}' not found in outputs/")
        print(f"Available pipelines:")
        for p in outputs_dir.iterdir():
            if p.is_dir():
                print(f"  - {p.name}")
        sys.exit(1)

    # Get base version
    base_version = args.base
    if base_version is None:
        base_version = _get_latest_version(pipeline_dir)
        if base_version is None:
            print(f"Error: No versions found for pipeline '{args.pipeline_name}'")
            sys.exit(1)

    print(f"\n{'='*70}")
    print(f"RERUN: {args.pipeline_name}")
    print(f"Base version: {base_version}")
    print(f"Items: {', '.join(args.item_ids)}")
    if args.note:
        print(f"Note: {args.note}")
    print(f"{'='*70}\n")

    # Load metadata from base version to get pipeline config
    base_metadata_path = pipeline_dir / base_version / "metadata.json"
    if not base_metadata_path.exists():
        print(f"Error: metadata.json not found in {base_version}/")
        print(f"Cannot determine pipeline configuration.")
        sys.exit(1)

    with open(base_metadata_path, 'r', encoding='utf-8') as f:
        base_metadata = json.load(f)

    # Reconstruct steps from metadata (if available)
    # Note: For now, user needs to provide steps manually or we need to save step config
    print(f"Error: Automatic step reconstruction not yet implemented.")
    print(f"\nTo rerun items, you need to:")
    print(f"1. Load your pipeline configuration")
    print(f"2. Call run_pipeline with:")
    print(f"   - pipeline_name='{args.pipeline_name}'")
    print(f"   - base_version='{base_version}'")
    print(f"   - rerun_items={args.item_ids}")
    print(f"\nExample code:")
    print(f"""
from core.pipeline import run_pipeline, Step

# Define your steps
steps = [
    Step(prompt_name="your_prompt", batch_mode=True, batch_id_field="template_id", ...),
    ...
]

# Run with rerun
result = run_pipeline(
    steps=steps,
    pipeline_name='{args.pipeline_name}',
    base_version='{base_version}',
    rerun_items={args.item_ids},
    module_number={base_metadata.get('module_number')},
    verbose=True
)
    """)


if __name__ == "__main__":
    main()
