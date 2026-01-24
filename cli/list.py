"""
List CLI - List all versions of a pipeline

Usage:
    python list.py [pipeline_name]

Examples:
    python list.py                    # List all pipelines
    python list.py problem_generator  # List all versions of a specific pipeline
"""

import sys
import argparse
from pathlib import Path
import json


def format_duration(seconds):
    """Format duration in human-readable format"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"


def main():
    parser = argparse.ArgumentParser(
        description="List pipeline versions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Status Filtering Examples:
  python list.py problem_generator                    # Default: show beta, rc, final only
  python list.py problem_generator --all              # Show all statuses
  python list.py problem_generator --status final     # Show only final
  python list.py problem_generator --status beta rc   # Show beta and rc
        """
    )
    parser.add_argument("pipeline_name", nargs="?", help="Pipeline name (optional)")
    parser.add_argument("--all", action="store_true",
                       help="Show all versions (including draft and deprecated)")
    parser.add_argument("--status", nargs="+",
                       help="Filter by specific status(es): draft, alpha, beta, rc, final, deprecated")

    args = parser.parse_args()

    # Default statuses to show (excludes draft and deprecated by default)
    default_statuses = {"beta", "rc", "final"}

    if args.all:
        filter_statuses = None  # Show all
    elif args.status:
        filter_statuses = set(args.status)
    else:
        filter_statuses = default_statuses

    # Add project root to path
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(project_root / "core"))

    from path_manager import get_project_paths

    paths = get_project_paths()
    outputs_dir = paths['outputs']

    if not outputs_dir.exists():
        print("No outputs directory found")
        sys.exit(1)

    if args.pipeline_name:
        # List versions for specific pipeline
        pipeline_dir = outputs_dir / args.pipeline_name

        if not pipeline_dir.exists():
            print(f"Error: Pipeline '{args.pipeline_name}' not found")
            print(f"\nAvailable pipelines:")
            for p in outputs_dir.iterdir():
                if p.is_dir():
                    print(f"  - {p.name}")
            sys.exit(1)

        # Get all versions
        versions = []
        for item in pipeline_dir.iterdir():
            if item.is_dir() and item.name.startswith('v') and item.name[1:].isdigit():
                version_num = int(item.name[1:])
                metadata_path = item / "metadata.json"

                metadata = {}
                if metadata_path.exists():
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)

                versions.append({
                    "version": item.name,
                    "version_num": version_num,
                    "metadata": metadata
                })

        # Sort by version number
        versions.sort(key=lambda x: x["version_num"])

        # Filter by status if needed
        if filter_statuses is not None:
            filtered_versions = [
                v for v in versions
                if v["metadata"].get("pipeline_status", "draft") in filter_statuses
            ]
            hidden_count = len(versions) - len(filtered_versions)
        else:
            filtered_versions = versions
            hidden_count = 0

        # Get latest version
        latest_file = pipeline_dir / "latest.txt"
        latest_link = pipeline_dir / "latest"
        latest_version = None

        if latest_link.is_symlink():
            try:
                latest_version = latest_link.readlink().name
            except:
                pass
        elif latest_file.exists():
            with open(latest_file, 'r') as f:
                latest_version = f.read().strip()

        # Print versions
        print(f"\n{'='*70}")
        print(f"PIPELINE: {args.pipeline_name}")
        print(f"Versions: {len(filtered_versions)}" + (f" (hiding {hidden_count})" if hidden_count > 0 else ""))
        if latest_version:
            print(f"Latest: {latest_version}")
        if filter_statuses:
            print(f"Showing: {', '.join(sorted(filter_statuses))}")
            print(f"Tip: Use --all to show all versions, or --status <status> to filter")
        print(f"{'='*70}\n")

        for v in filtered_versions:
            meta = v["metadata"]
            is_latest = v["version"] == latest_version

            print(f"{v['version']}" + (" (latest)" if is_latest else ""))
            print(f"  Created: {meta.get('timestamp', 'N/A')}")
            print(f"  Status: {meta.get('pipeline_status', 'N/A')}")
            if meta.get('notes'):
                print(f"  Notes: {meta['notes']}")
            print(f"  Mode: {meta.get('mode', 'N/A')}")
            if meta.get('base_version'):
                print(f"  Base: {meta['base_version']}")
            if meta.get('duration_seconds'):
                print(f"  Duration: {format_duration(meta['duration_seconds'])}")

            # Count items
            items_dir = pipeline_dir / v["version"] / "items"
            if items_dir.exists():
                item_count = len([d for d in items_dir.iterdir() if d.is_dir()])
                print(f"  Items: {item_count}")

            # Show errors if any
            for i in range(1, 10):  # Check up to 10 steps
                errors_file = pipeline_dir / v["version"] / f"{i:02d}_errors.json"
                if errors_file.exists():
                    with open(errors_file, 'r', encoding='utf-8') as f:
                        errors = json.load(f)
                    if errors:
                        print(f"  Errors (step {i}): {len(errors)}")

            print()

    else:
        # List all pipelines
        pipelines = []
        for p in outputs_dir.iterdir():
            if p.is_dir():
                # Get all versions and filter by status
                all_versions = []
                for item in p.iterdir():
                    if item.is_dir() and item.name.startswith('v') and item.name[1:].isdigit():
                        metadata_path = item / "metadata.json"
                        if metadata_path.exists():
                            with open(metadata_path, 'r', encoding='utf-8') as f:
                                metadata = json.load(f)
                                status = metadata.get('pipeline_status', 'draft')
                                # Apply filter
                                if filter_statuses is None or status in filter_statuses:
                                    all_versions.append(item.name)

                if len(all_versions) > 0:
                    pipelines.append({
                        "name": p.name,
                        "versions": len(all_versions)
                    })

        if not pipelines:
            print("No pipelines found with the specified status filter")
            if filter_statuses:
                print(f"Showing: {', '.join(sorted(filter_statuses))}")
                print("Tip: Use --all to show all pipelines")
            sys.exit(0)

        print(f"\n{'='*70}")
        print(f"ALL PIPELINES")
        if filter_statuses:
            print(f"Showing: {', '.join(sorted(filter_statuses))}")
            print(f"Tip: Use --all to show all pipelines, or --status <status> to filter")
        print(f"{'='*70}\n")

        for p in sorted(pipelines, key=lambda x: x["name"]):
            print(f"{p['name']}")
            print(f"  Versions: {p['versions']}")
            print()


if __name__ == "__main__":
    main()
