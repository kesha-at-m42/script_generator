"""
Compare CLI - Compare two versions of a pipeline

Usage:
    python compare.py <pipeline_name> <version1> <version2>

Examples:
    python compare.py problem_generator v0 v1
    python compare.py problem_generator v1 v2 --detail
"""

import sys
import argparse
from pathlib import Path
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compare two versions of a pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("pipeline_name", help="Name of the pipeline")
    parser.add_argument("version1", help="First version (e.g., v0)")
    parser.add_argument("version2", help="Second version (e.g., v1)")
    parser.add_argument("--detail", action="store_true", help="Show detailed diffs")

    args = parser.parse_args()

    # Get pipeline directory
    outputs_dir = Path(__file__).parent / "outputs"
    pipeline_dir = outputs_dir / args.pipeline_name

    if not pipeline_dir.exists():
        print(f"Error: Pipeline '{args.pipeline_name}' not found")
        sys.exit(1)

    v1_dir = pipeline_dir / args.version1
    v2_dir = pipeline_dir / args.version2

    if not v1_dir.exists():
        print(f"Error: Version '{args.version1}' not found")
        sys.exit(1)

    if not v2_dir.exists():
        print(f"Error: Version '{args.version2}' not found")
        sys.exit(1)

    # Load metadata
    v1_metadata_path = v1_dir / "metadata.json"
    v2_metadata_path = v2_dir / "metadata.json"

    v1_meta = {}
    v2_meta = {}

    if v1_metadata_path.exists():
        with open(v1_metadata_path, 'r', encoding='utf-8') as f:
            v1_meta = json.load(f)

    if v2_metadata_path.exists():
        with open(v2_metadata_path, 'r', encoding='utf-8') as f:
            v2_meta = json.load(f)

    # Print comparison
    print(f"\n{'='*70}")
    print(f"COMPARING: {args.pipeline_name}")
    print(f"{args.version1} vs {args.version2}")
    print(f"{'='*70}\n")

    # Compare metadata
    print(f"Version Info:")
    print(f"  {args.version1}:")
    print(f"    Created: {v1_meta.get('timestamp', 'N/A')}")
    print(f"    Status: {v1_meta.get('pipeline_status', 'N/A')}")
    if v1_meta.get('notes'):
        print(f"    Notes: {v1_meta['notes']}")
    print(f"    Mode: {v1_meta.get('mode', 'N/A')}")
    print(f"    Duration: {v1_meta.get('duration_seconds', 0):.1f}s")

    print(f"  {args.version2}:")
    print(f"    Created: {v2_meta.get('timestamp', 'N/A')}")
    print(f"    Status: {v2_meta.get('pipeline_status', 'N/A')}")
    if v2_meta.get('notes'):
        print(f"    Notes: {v2_meta['notes']}")
    print(f"    Mode: {v2_meta.get('mode', 'N/A')}")
    print(f"    Duration: {v2_meta.get('duration_seconds', 0):.1f}s")
    if v2_meta.get('base_version'):
        print(f"    Base: {v2_meta['base_version']}")

    # Compare items
    v1_items_dir = v1_dir / "items"
    v2_items_dir = v2_dir / "items"

    v1_items = set()
    v2_items = set()

    if v1_items_dir.exists():
        v1_items = {item.name for item in v1_items_dir.iterdir() if item.is_dir()}

    if v2_items_dir.exists():
        v2_items = {item.name for item in v2_items_dir.iterdir() if item.is_dir()}

    only_in_v1 = v1_items - v2_items
    only_in_v2 = v2_items - v1_items
    in_both = v1_items & v2_items

    print(f"\nItems:")
    print(f"  Total in {args.version1}: {len(v1_items)}")
    print(f"  Total in {args.version2}: {len(v2_items)}")
    print(f"  In both: {len(in_both)}")

    if only_in_v1:
        print(f"  Only in {args.version1}: {sorted(only_in_v1)}")
    if only_in_v2:
        print(f"  Only in {args.version2}: {sorted(only_in_v2)}")

    # Show changed items if detail mode
    if args.detail and in_both:
        print(f"\nDetailed Comparison:")
        for item_id in sorted(in_both):
            # Compare outputs for this item
            v1_item_dir = v1_items_dir / item_id
            v2_item_dir = v2_items_dir / item_id

            v1_outputs = {f.name for f in v1_item_dir.iterdir() if f.is_file()}
            v2_outputs = {f.name for f in v2_item_dir.iterdir() if f.is_file()}

            if v1_outputs != v2_outputs:
                print(f"\n  Item {item_id}:")
                print(f"    Different output files")
                print(f"    {args.version1}: {sorted(v1_outputs)}")
                print(f"    {args.version2}: {sorted(v2_outputs)}")

    print(f"\n{'='*70}")


if __name__ == "__main__":
    main()
