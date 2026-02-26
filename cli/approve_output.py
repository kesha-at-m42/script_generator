"""
Approve Output CLI - Copy a pipeline output version into good_outputs/ (git-tracked)

Usage:
    # Approve latest version
    python approve_output.py problem_pool_generator --module 4 --path b

    # Approve specific version
    python approve_output.py problem_pool_generator --module 4 --path b --version v15

    # Approve with a note
    python approve_output.py problem_pool_generator --module 4 --path b --note "Final approved version"
"""

import sys
import argparse
import shutil
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.version_manager import get_latest_version
from core.path_manager import get_project_paths


def main():
    parser = argparse.ArgumentParser(
        description="Copy a pipeline output version to good_outputs/ (git-tracked)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python approve_output.py problem_pool_generator --module 4 --path b
  python approve_output.py problem_pool_generator --module 4 --path b --version v15
  python approve_output.py problem_pool_generator --module 4 --path b --note "Approved after review"
        """
    )

    parser.add_argument("pipeline_name", help="Name of the pipeline")
    parser.add_argument("--module", type=int, help="Module number")
    parser.add_argument("--path", choices=['a', 'b', 'c'], help="Path letter")
    parser.add_argument("--version", default=None, help="Version to approve (default: latest)")
    parser.add_argument("--note", nargs="+", default=[], help="Optional note about this version (no quotes needed)")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")

    args = parser.parse_args()
    args.note = " ".join(args.note)

    paths = get_project_paths()
    outputs_dir = paths['outputs']
    good_outputs_dir = project_root / "good_outputs"

    # Build full pipeline name (same convention as rerun.py)
    full_pipeline_name = args.pipeline_name
    if args.module is not None:
        full_pipeline_name += f"_module_{args.module}"
    if args.path is not None:
        full_pipeline_name += f"_path_{args.path.lower()}"

    pipeline_dir = outputs_dir / full_pipeline_name

    if not pipeline_dir.exists():
        print(f"Error: No outputs found for '{full_pipeline_name}'")
        print(f"  Expected: {pipeline_dir}")
        sys.exit(1)

    # Resolve version
    version = args.version
    if version is None:
        version = get_latest_version(pipeline_dir)
        if version is None:
            print(f"Error: No versions found in {pipeline_dir}")
            sys.exit(1)
        print(f"Using latest version: {version}")

    source_dir = pipeline_dir / version

    if not source_dir.exists():
        print(f"Error: Version '{version}' not found in {pipeline_dir}")
        sys.exit(1)

    dest_dir = good_outputs_dir / full_pipeline_name / version

    print(f"\nAPPROVE OUTPUT: {full_pipeline_name} / {version}")
    print(f"  From: {source_dir}")
    print(f"  To:   {dest_dir}")
    if args.note:
        print(f"  Note: {args.note}")

    if dest_dir.exists():
        print(f"\nWarning: {dest_dir} already exists and will be overwritten.")

    if not args.yes:
        response = input("\nProceed? [y/N] ").strip().lower()
        if response != 'y':
            print("Aborted.")
            sys.exit(0)

    # Copy
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)

    # Write note file if provided
    if args.note:
        (dest_dir / "KEEP_NOTE.txt").write_text(args.note)

    print(f"\nDone. Copied to good_outputs/{full_pipeline_name}/{version}/")
    print(f"  Run: git add good_outputs/ && git commit")


if __name__ == "__main__":
    main()
