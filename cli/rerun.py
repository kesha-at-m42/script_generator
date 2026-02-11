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
from glob import glob
import shutil

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "core"))

from core.pipeline import run_pipeline
from core.version_manager import get_latest_version
from core.path_manager import get_project_paths, get_step_directory, get_step_output_paths
from core.pipeline_executor import run_formatting_step
from config.pipelines import PIPELINES
import json
import re


def parse_output_path(path_str):
    """Parse output file/directory path to extract pipeline info

    Args:
        path_str: Path to output file or directory

    Returns:
        Dict with pipeline_name, module_number, path_letter, base_version,
        item_ids, template_ids, step_number, version_dir
    """
    path = Path(path_str).resolve()

    if not path.exists():
        return None

    # Find outputs directory in path
    parts = path.parts
    if 'outputs' not in parts:
        return None

    outputs_idx = parts.index('outputs')

    # Next: pipeline directory (e.g., problem_pool_generator_module_4_path_b)
    if len(parts) <= outputs_idx + 1:
        return None

    pipeline_dir_name = parts[outputs_idx + 1]

    # Next: version (e.g., v8)
    if len(parts) <= outputs_idx + 2:
        return None

    version = parts[outputs_idx + 2]
    if not version.startswith('v'):
        return None

    # Parse pipeline directory name: {name}_module_{N}_path_{letter}
    match = re.match(r'(.+?)(?:_module_(\d+))?(?:_path_([abc]))?$', pipeline_dir_name)
    if not match:
        return None

    pipeline_name, module_str, path_letter = match.groups()
    module_number = int(module_str) if module_str else None

    # Load metadata
    version_dir = Path(project_root) / 'outputs' / pipeline_dir_name / version
    metadata_file = version_dir / 'metadata.json'
    base_version = None

    if metadata_file.exists():
        try:
            metadata = load_json(metadata_file)
            base_version = metadata.get('base_version')
        except:
            pass

    # Extract step number from path (e.g., "step_02_sequence_structurer")
    step_number = None
    for part in parts:
        if part.startswith('step_'):
            match = re.match(r'step_(\d+)_', part)
            if match:
                step_number = int(match.group(1))
                break

    result = {
        'pipeline_name': pipeline_name,
        'module_number': module_number,
        'path_letter': path_letter,
        'version': version,
        'base_version': base_version,
        'step_number': step_number,
        'version_dir': version_dir
    }

    # Extract item IDs from path
    if path.is_file() and path.suffix == '.json' and path.parent.name == 'items':
        # Single item file
        item_id = path.stem
        result['item_ids'] = [item_id]

        # For step 1: filename IS the template ID (no mapping needed)
        if step_number == 1 and pipeline_name == 'problem_pool_generator':
            result['template_ids'] = [item_id]
        # For step 2+: use item IDs directly (no template mapping)
        elif step_number and step_number >= 2:
            result['template_ids'] = None

    elif path.is_dir() and path.name == 'items':
        # Items directory - get all items
        item_files = sorted(path.glob('[0-9]*.json'))
        item_ids = [f.stem for f in item_files]
        result['item_ids'] = item_ids

        # For step 1: filenames ARE the template IDs (no mapping needed)
        if step_number == 1 and pipeline_name == 'problem_pool_generator':
            result['template_ids'] = item_ids
        # For step 2+: use item IDs directly (no template mapping)
        elif step_number and step_number >= 2:
            result['template_ids'] = None

    # Extract item IDs from collated files (step 2+)
    elif path.is_file() and path.suffix == '.json' and step_number and step_number >= 2:
        try:
            data = load_json(path)
            if isinstance(data, list):
                # Extract problem_id or problem_instance_id from each item
                item_ids = set()
                for item in data:
                    # Try multiple ID paths
                    pid = (
                        item.get('problem_id') or
                        item.get('problem_instance_id') or
                        (item.get('metadata', {}).get('problem_id') if isinstance(item.get('metadata'), dict) else None)
                    )
                    if pid:
                        item_ids.add(str(pid))

                if item_ids:
                    result['item_ids'] = sorted(item_ids, key=int)
                    result['template_ids'] = None
        except:
            pass

    return result


def map_items_to_templates(item_ids, version_dir):
    """Map problem IDs to template IDs

    Args:
        item_ids: List of problem_instance_id strings
        version_dir: Version directory path

    Returns:
        Set of template IDs or None
    """
    # Find step 1 output
    step_1_dir = None
    for d in version_dir.iterdir():
        if d.is_dir() and 'step_01' in d.name and 'problem_generator' in d.name:
            step_1_dir = d
            break

    if not step_1_dir:
        return None

    collated_file = step_1_dir / 'problem_generator.json'
    if not collated_file.exists():
        return None

    try:
        data = load_json(collated_file)
        template_ids = set()

        for item in data:
            pid = str(item.get('problem_instance_id'))
            if pid in item_ids:
                tid = item.get('template_id')
                if tid:
                    template_ids.add(str(tid))

        return template_ids if template_ids else None
    except:
        return None


def filter_ai_step_outputs(new_version_dir, exclude_template_ids=None, exclude_item_ids=None, verbose=True):
    """
    Filter items from AI step outputs in the new version directory.
    Removes files and items with matching template_id or item_id.

    Args:
        new_version_dir: Path to new version directory
        exclude_template_ids: List of template IDs to exclude
        exclude_item_ids: List of item/problem IDs to exclude
        verbose: Print filtering details
    """
    if not exclude_template_ids and not exclude_item_ids:
        return

    if verbose:
        print(f"\n{'='*70}")
        print("FILTERING AI STEP OUTPUTS")
        print(f"{'='*70}")

    # Find all AI step directories
    for step_dir in sorted(new_version_dir.glob("step_*")):
        if not step_dir.is_dir():
            continue

        step_name = step_dir.name

        # Check items directory (batch mode)
        items_dir = step_dir / "items"
        if items_dir.exists():
            removed_count = 0
            for item_file in items_dir.glob("*.json"):
                try:
                    with open(item_file, 'r', encoding='utf-8') as f:
                        item_data = json.load(f)

                    should_remove = False

                    # Check template_id
                    if exclude_template_ids:
                        template_id = item_data.get('template_id') or item_data.get('metadata', {}).get('template_id')
                        if template_id in exclude_template_ids:
                            should_remove = True

                    # Check item_id
                    if exclude_item_ids and not should_remove:
                        item_id = item_data.get('problem_id') or item_data.get('problem_instance_id') or item_data.get('metadata', {}).get('problem_id')
                        if str(item_id) in exclude_item_ids or item_id in exclude_item_ids:
                            should_remove = True

                    if should_remove:
                        item_file.unlink()
                        removed_count += 1
                except:
                    pass

            if removed_count > 0 and verbose:
                print(f"  [FILTER] {step_name}: Removed {removed_count} items")

        # Check collated file
        for json_file in step_dir.glob("*.json"):
            if json_file.name == "errors.json":
                continue

            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                original_count = 0
                filtered_data = data

                # Filter array
                if isinstance(data, list):
                    original_count = len(data)
                    filtered_data = []
                    for item in data:
                        should_remove = False

                        # Check template_id
                        if exclude_template_ids:
                            template_id = item.get('template_id') or item.get('metadata', {}).get('template_id')
                            if template_id in exclude_template_ids:
                                should_remove = True

                        # Check item_id
                        if exclude_item_ids and not should_remove:
                            item_id = item.get('problem_id') or item.get('problem_instance_id') or item.get('metadata', {}).get('problem_id')
                            if str(item_id) in exclude_item_ids or item_id in exclude_item_ids:
                                should_remove = True

                        if not should_remove:
                            filtered_data.append(item)

                # Filter SequencePool
                elif isinstance(data, dict) and 'sequences' in data:
                    original_count = len(data.get('sequences', []))
                    sequences = data.get('sequences', [])
                    filtered_sequences = []

                    for seq in sequences:
                        should_remove = False

                        # Check template_id
                        if exclude_template_ids:
                            template_id = seq.get('metadata', {}).get('template_id')
                            if template_id in exclude_template_ids:
                                should_remove = True

                        # Check item_id
                        if exclude_item_ids and not should_remove:
                            item_id = seq.get('metadata', {}).get('problem_id')
                            if str(item_id) in exclude_item_ids or item_id in exclude_item_ids:
                                should_remove = True

                        if not should_remove:
                            filtered_sequences.append(seq)

                    filtered_data = {**data, 'sequences': filtered_sequences}

                # Save if changed
                if original_count > 0:
                    new_count = len(filtered_data) if isinstance(filtered_data, list) else len(filtered_data.get('sequences', []))
                    if new_count < original_count:
                        with open(json_file, 'w', encoding='utf-8') as f:
                            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
                        if verbose:
                            print(f"  [FILTER] {step_name}/{json_file.name}: {original_count} → {new_count} items")
            except:
                pass


def main():
    parser = argparse.ArgumentParser(
        description="Rerun specific items or steps from a pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Point at any output and rerun it (auto-detects everything)
  python rerun.py --from-output outputs/.../v8/step_03/.../items/48.json
  python rerun.py --from-output outputs/.../v8/step_03/.../items/

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
    parser.add_argument("pipeline_name", nargs="?", help="Name of the pipeline (optional if using --from-output)")
    parser.add_argument("item_ids", nargs="*", help="Item IDs to rerun (for batch steps)")

    # Rerun from output
    parser.add_argument("--from-output", help="Point at any output file to rerun it (auto-detects pipeline/module/items)")

    # Rerun options
    parser.add_argument("--base", default=None, help="Base version to rerun from (default: latest or auto-detected)")
    parser.add_argument("--note", default="", help="Optional note about this rerun")
    parser.add_argument("--templates", action="store_true", help="Treat item_ids as template IDs (enables template rerun mode)")

    # Step range options
    parser.add_argument("--start-from", help="Start from step N (int or name)")
    parser.add_argument("--end-at", help="End at step N (int or name)")

    # Module/path context (required for step-level reruns)
    parser.add_argument("--module", type=int, help="Module number")
    parser.add_argument("--path", choices=['a', 'b', 'c'], help="Path letter")

    # Exclusion filters
    parser.add_argument("--exclude-template-ids", type=str, help="Exclude items with these template IDs from ALL steps (comma-separated, e.g., '7006,7010')")
    parser.add_argument("--exclude-item-ids", type=str, help="Exclude items with these problem/item IDs from ALL steps (comma-separated, e.g., '73,74,75')")

    # Other
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--status", help="Pipeline status (alpha/beta/rc/final)")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")

    args = parser.parse_args()

    # Parse exclusion filters
    exclude_template_ids = None
    if args.exclude_template_ids:
        exclude_template_ids = [id.strip() for id in args.exclude_template_ids.split(',')]
        print(f"  [EXCLUDE] Template IDs: {exclude_template_ids}")

    exclude_item_ids = None
    if args.exclude_item_ids:
        exclude_item_ids = [id.strip() for id in args.exclude_item_ids.split(',')]
        print(f"  [EXCLUDE] Item/Problem IDs: {exclude_item_ids}")

    # Handle --from-output mode
    if args.from_output:
        output_info = parse_output_path(args.from_output)
        if not output_info:
            print(f"Error: Could not parse output path: {args.from_output}")
            print("Expected format: outputs/{pipeline}/v{N}/.../items/123.json")
            sys.exit(1)

        # Override args with detected values
        args.pipeline_name = output_info['pipeline_name']
        args.module = output_info.get('module_number')
        args.path = output_info.get('path_letter')
        if not args.base and output_info.get('base_version'):
            args.base = output_info['base_version']

        step_number = output_info.get('step_number')

        # Auto-select rerun mode based on step number
        if step_number == 1:
            # Step 1: Template rerun mode (full pipeline from step 1)
            if output_info.get('template_ids'):
                args.item_ids = list(output_info['template_ids'])
                args.templates = True
                args.start_from = None
                if args.verbose:
                    print(f"[FROM-OUTPUT] Detected step 1 -> Template rerun mode")
            else:
                # Fallback: no template IDs found, use item IDs
                args.item_ids = list(output_info.get('item_ids', []))

        elif step_number and step_number >= 2:
            # Step 2+: Item rerun mode (partial pipeline from this step)
            args.templates = False
            args.item_ids = list(output_info.get('item_ids', []))
            args.start_from = str(step_number)
            if args.verbose:
                print(f"[FROM-OUTPUT] Detected step {step_number} -> Item rerun mode (starting from step {step_number})")

        else:
            # Fallback: No step number detected, infer from IDs
            if output_info.get('template_ids'):
                args.item_ids = list(output_info['template_ids'])
                args.templates = True
            elif output_info.get('item_ids'):
                args.item_ids = list(output_info['item_ids'])

        print(f"\n[AUTO-DETECTED FROM OUTPUT]")
        print(f"  Pipeline: {args.pipeline_name}")
        if args.module:
            print(f"  Module: {args.module}")
        if args.path:
            print(f"  Path: {args.path}")
        if args.base:
            print(f"  Base: {args.base}")
        if step_number:
            print(f"  Step: {step_number}")
        if args.templates:
            print(f"  Mode: Template Rerun (full pipeline)")
            print(f"  Templates: {', '.join(args.item_ids)}")
        elif args.start_from:
            print(f"  Mode: Item Rerun (from step {args.start_from})")
            print(f"  Items: {', '.join(args.item_ids[:5])}{'...' if len(args.item_ids) > 5 else ''}")
        else:
            print(f"  Items: {', '.join(args.item_ids[:5])}{'...' if len(args.item_ids) > 5 else ''}")
        print()

    # Validate pipeline name is provided
    if not args.pipeline_name:
        print("Error: pipeline_name required (or use --from-output)")
        parser.print_help()
        sys.exit(1)

    # Validate pipeline exists
    if args.pipeline_name not in PIPELINES:
        print(f"Error: Pipeline '{args.pipeline_name}' not found")
        print(f"Available pipelines:")
        for p in PIPELINES.keys():
            print(f"  - {p}")
        sys.exit(1)

    # Get pipeline steps
    steps = PIPELINES[args.pipeline_name]

    # Detect exclude mode
    is_exclude_mode = bool(exclude_template_ids or exclude_item_ids)

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
    is_template_rerun = args.templates and has_item_ids

    # Validate combinations
    if is_exclude_mode and has_item_ids:
        print("Error: Exclude mode cannot be combined with item IDs")
        print("Exclude mode reruns formatting steps on the entire filtered dataset")
        sys.exit(1)

    if is_exclude_mode and has_step_range:
        print("Error: Exclude mode cannot be combined with --start-from or --end-at")
        print("Exclude mode automatically reruns all formatting steps")
        sys.exit(1)

    if is_exclude_mode and is_template_rerun:
        print("Error: Exclude mode cannot be combined with template rerun mode")
        sys.exit(1)

    if has_step_range and not args.module:
        print("Error: --module required when using --start-from or --end-at")
        sys.exit(1)

    if is_template_rerun and has_step_range:
        print("Error: Template rerun mode (--templates) cannot be combined with --start-from or --end-at")
        sys.exit(1)

    if is_template_rerun and not args.module:
        print("Error: Template rerun mode requires --module")
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

    if is_template_rerun:
        print(f"Mode: Template Rerun")
        print(f"Templates: {', '.join(args.item_ids)}")
    elif has_item_ids:
        print(f"Items: {', '.join(args.item_ids)}")
    else:
        print(f"Items: All (full rerun)")

    if args.note:
        print(f"Note: {args.note}")
    print(f"{'='*70}\n")

    if not args.yes:
        response = input("Proceed with rerun? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled.")
            sys.exit(0)

    # Run pipeline with rerun parameters
    try:
        if is_exclude_mode:
            # Exclude mode: copy all steps, filter AI outputs, rerun only formatting steps (no API calls)
            results = run_exclude_mode(
                steps=steps,
                pipeline_name=args.pipeline_name,
                module_number=args.module,
                path_letter=args.path,
                base_version=base_version,
                exclude_template_ids=exclude_template_ids,
                exclude_item_ids=exclude_item_ids,
                notes=args.note,
                verbose=True
            )
        elif is_template_rerun:
            # Template rerun mode: orchestrate with diff and cascade
            results = run_template_rerun_pipeline(
                steps=steps,
                pipeline_name=args.pipeline_name,
                module_number=args.module,
                path_letter=args.path,
                template_ids=args.item_ids,
                base_version=base_version,
                notes=args.note,
                verbose=True
            )
        else:
            # Standard rerun mode
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


def run_exclude_mode(steps, pipeline_name, module_number, path_letter, base_version,
                     exclude_template_ids=None, exclude_item_ids=None, notes="", verbose=True):
    """Run exclude mode: copy all steps from base, filter AI outputs, rerun only formatting steps

    Args:
        steps: Pipeline steps
        pipeline_name: Pipeline name
        module_number: Module number
        path_letter: Path letter
        base_version: Base version to copy from
        exclude_template_ids: Template IDs to exclude
        exclude_item_ids: Item IDs to exclude
        notes: Optional notes
        verbose: Enable verbose output

    Returns:
        Pipeline results
    """
    from core.version_manager import create_version_directory, save_metadata, update_latest_symlink
    from datetime import datetime
    import json

    # Get project root
    project_root = Path(__file__).parent.parent

    # Build full pipeline name
    full_pipeline_name = pipeline_name
    if module_number:
        full_pipeline_name += f"_module_{module_number}"
    if path_letter:
        full_pipeline_name += f"_path_{path_letter.lower()}"

    # Create new version directory
    version_dir, version_str, is_rerun, full_name = create_version_directory(
        pipeline_name, module_number, path_letter, base_version
    )

    if verbose:
        print(f"\n{'='*70}")
        print(f"EXCLUDE MODE: {full_pipeline_name}")
        print(f"{'='*70}")
        print(f"Base version: {base_version}")
        print(f"New version: {version_str}")
        if exclude_template_ids:
            print(f"Excluding template IDs: {', '.join(exclude_template_ids)}")
        if exclude_item_ids:
            print(f"Excluding item IDs: {', '.join(exclude_item_ids)}")
        print(f"{'='*70}\n")

    # Get base version directory
    outputs_dir = get_project_paths()['outputs']
    pipeline_dir = outputs_dir / full_pipeline_name
    base_version_dir = pipeline_dir / base_version

    if not base_version_dir.exists():
        raise ValueError(f"Base version not found: {base_version_dir}")

    # Step 1: Copy ALL steps from base version
    if verbose:
        print(f"{'='*70}")
        print(f"STEP 1: COPYING ALL STEPS FROM BASE VERSION")
        print(f"{'='*70}")

    for step_idx, step in enumerate(steps, 1):
        step_name = step.prompt_name if step.is_ai_step() else str(step.function).split('.')[-1]

        # Source: base version step directory
        base_step_dir = get_step_directory(base_version_dir, step_idx, step_name)

        # Destination: new version step directory
        new_step_dir = get_step_directory(version_dir, step_idx, step_name)

        # Copy entire step directory
        if base_step_dir.exists():
            if verbose:
                print(f"  [COPY] Step {step_idx} ({step_name})")
            shutil.copytree(base_step_dir, new_step_dir, dirs_exist_ok=True)
        else:
            print(f"  [WARNING] Base step directory not found: {base_step_dir}")

    # Step 2: Filter AI step outputs
    if verbose:
        print(f"\n{'='*70}")
        print(f"STEP 2: FILTERING AI STEP OUTPUTS")
        print(f"{'='*70}")

    filter_ai_step_outputs(
        version_dir,
        exclude_template_ids=exclude_template_ids,
        exclude_item_ids=exclude_item_ids,
        verbose=verbose
    )

    # Step 3: Rerun ONLY formatting steps
    if verbose:
        print(f"\n{'='*70}")
        print(f"STEP 3: RERUNNING FORMATTING STEPS")
        print(f"{'='*70}")

    for step_idx, step in enumerate(steps, 1):
        # Skip AI steps
        if step.is_ai_step():
            continue

        step_name = str(step.function).split('.')[-1]
        step_dir = get_step_directory(version_dir, step_idx, step_name)

        if verbose:
            print(f"\n  [STEP {step_idx}] {step_name}")

        # Get input from previous step's output
        prev_step = steps[step_idx - 2]  # 0-indexed
        prev_step_name = prev_step.prompt_name if prev_step.is_ai_step() else str(prev_step.function).split('.')[-1]
        prev_step_dir = get_step_directory(version_dir, step_idx - 1, prev_step_name)
        input_file = prev_step_dir / f"{prev_step_name}.json"

        # Load input data
        input_data = load_json(input_file)

        # Execute formatting function
        try:
            output_data = run_formatting_step(
                step=step,
                input_data=input_data,
                input_content=None,
                module_number=module_number,
                path_letter=path_letter,
                project_root=project_root,
                verbose=False
            )

            # Save output
            output_file = step_dir / f"{step_name}.json"
            save_json(output_file, output_data)

            if verbose:
                print(f"    [OK] Completed")
        except Exception as e:
            if verbose:
                print(f"    [ERROR] {e}")
            raise

    # Step 4: Save metadata
    start_time = datetime.now()
    metadata = {
        "timestamp": start_time.isoformat(),
        "pipeline_name": pipeline_name,
        "module_number": module_number,
        "path_letter": path_letter,
        "version": version_str,
        "base_version": base_version,
        "mode": "exclude",
        "exclude_template_ids": exclude_template_ids,
        "exclude_item_ids": exclude_item_ids,
        "notes": notes or "Exclude mode rerun",
        "pipeline_status": "draft",
        "full_pipeline_name": full_pipeline_name,
        "status": "completed",
        "output_dir": str(version_dir)
    }

    save_metadata(version_dir, metadata)
    update_latest_symlink(full_pipeline_name, version_str)

    if verbose:
        print(f"\n{'='*70}")
        print(f"EXCLUDE MODE COMPLETE")
        print(f"Version: {version_str}")
        print(f"Output: outputs/{full_pipeline_name}/latest/")
        print(f"{'='*70}")

    return {
        'final_output': None,
        'output_dir': str(version_dir),
        'metadata': metadata
    }


def run_template_rerun_pipeline(steps, pipeline_name, module_number, path_letter,
                                template_ids, base_version, notes="", verbose=True):
    """Run template-based rerun with automatic re-collation

    This function runs the FULL pipeline with batch_only_items set to the problem IDs
    from the specified templates. BatchProcessor automatically copies unchanged items
    from the base version. After the pipeline completes, all steps are re-collated to
    merge base + new items.

    Args:
        steps: Pipeline steps
        pipeline_name: Pipeline name
        module_number: Module number
        path_letter: Path letter
        template_ids: List of template IDs to rerun
        base_version: Base version to rerun from
        notes: Optional notes
        verbose: Enable verbose output

    Returns:
        Pipeline results
    """
    from core.path_manager import get_step_directory, get_step_output_paths

    # Get project root
    project_root = Path(__file__).parent.parent

    # Build full pipeline name
    full_pipeline_name = pipeline_name
    if module_number:
        full_pipeline_name += f"_module_{module_number}"
    if path_letter:
        full_pipeline_name += f"_path_{path_letter.lower()}"

    # Get base version directory
    outputs_dir = get_project_paths()['outputs']
    pipeline_dir = outputs_dir / full_pipeline_name
    base_version_dir = pipeline_dir / base_version

    if not base_version_dir.exists():
        raise ValueError(f"Base version not found: {base_version_dir}")

    # Step 1: Map template IDs to problem_instance_ids
    step_0_dir = None
    for subdir in sorted(base_version_dir.iterdir()):
        if subdir.is_dir() and ('step_00' in subdir.name or 'step_01' in subdir.name) and 'problem_generator' in subdir.name:
            step_0_dir = subdir
            break

    if not step_0_dir:
        raise ValueError(f"Could not find step_00_problem_generator or step_01_problem_generator in {base_version_dir}")

    # Load base step 0 to map template_id → problem_instance_ids
    base_step0_file = step_0_dir / "problem_generator.json"
    if not base_step0_file.exists():
        raise ValueError(f"Base step 0 output not found: {base_step0_file}")

    base_step0_items = load_json(base_step0_file)
    rerun_problem_ids = [
        str(item['problem_instance_id'])
        for item in base_step0_items
        if str(item.get('template_id')) in template_ids
    ]

    if not rerun_problem_ids:
        raise ValueError(f"No items found for templates {template_ids} in base version")

    if verbose:
        print(f"\n[TEMPLATE RERUN] Mapping {len(template_ids)} templates to {len(rerun_problem_ids)} problem instances")
        print(f"  Templates: {', '.join(template_ids)}")
        print(f"  Problem IDs: {', '.join(rerun_problem_ids[:5])}{'...' if len(rerun_problem_ids) > 5 else ''}")
        print(f"  BatchProcessor will copy unchanged items from base automatically")

    # Step 2: Run FULL pipeline with batch_only_items
    # For step 1 (problem_generator): use template_ids
    # For steps 2+: use problem_instance_ids
    # This is necessary because step 1 processes templates, not problem instances
    if verbose:
        print(f"\n[TEMPLATE RERUN] Running full pipeline ({len(steps)} steps)")

    # Set batch_only_items on step 1 ONLY to use template_ids
    # Steps 2+ will use rerun_items (problem_ids) for filtering
    if steps and hasattr(steps[0], 'batch_only_items'):
        steps[0].batch_only_items = template_ids
        if verbose:
            print(f"  [STEP 1] Will process templates: {', '.join(template_ids)}")
            # Debug: Check batch_only_items for all steps
            for idx, step in enumerate(steps, 1):
                print(f"  [DEBUG] Step {idx} batch_only_items: {step.batch_only_items}")

    # Run pipeline with rerun_items for steps 2+
    # This ensures steps 2-4 only process the problem_ids from the regenerated templates
    results = run_pipeline(
        steps=steps,  # ALL steps
        pipeline_name=pipeline_name,
        module_number=module_number,
        path_letter=path_letter,
        base_version=base_version,
        rerun_items=rerun_problem_ids,  # Filter steps 2+ by problem_id (28, 29, 30)
        notes=f"Template rerun: {', '.join(template_ids)}" + (f" - {notes}" if notes else ""),
        verbose=verbose
    )

    # Clear batch_only_items from step 1 to prevent contamination in formatting reruns
    if steps and hasattr(steps[0], 'batch_only_items'):
        steps[0].batch_only_items = None

    new_version = results['metadata']['version']
    new_version_dir = pipeline_dir / new_version

    if verbose:
        print(f"\n[TEMPLATE RERUN] Pipeline complete, re-collating all steps...")

    # Step 3: Re-collate all AI steps to merge base + new items
    for step_idx, step in enumerate(steps, 1):
        step_name = step.prompt_name if step.is_ai_step() else str(step.function).split('.')[-1]
        step_dir = get_step_directory(new_version_dir, step_idx, step_name)
        base_step_dir = get_step_directory(base_version_dir, step_idx, step_name)

        if step_idx == 1:
            # Step 1: Merge template files (preserve original IDs)
            merge_and_collate_templates(step_dir, base_step_dir, set(template_ids))
            if verbose:
                print(f"  [STEP {step_idx}] Re-collated {step_name} (merged {len(template_ids)} new templates + base)")
        elif step.is_ai_step():
            # AI steps: Merge new items + base items
            merge_and_collate_items(step_dir, step_name, base_step_dir, set(rerun_problem_ids))
            if verbose:
                print(f"  [STEP {step_idx}] Re-collated {step_name} (merged {len(rerun_problem_ids)} new + base)")
        # Formatting steps will be handled below

    # Step 4: Re-run formatting steps on merged data
    if verbose:
        print(f"\n[TEMPLATE RERUN] Re-running formatting steps on merged data...")

    # Find last AI step
    last_ai_step_idx = None
    for idx, step in enumerate(steps, 1):
        if step.is_ai_step():
            last_ai_step_idx = idx

    # Re-run each formatting step sequentially
    for step_idx, step in enumerate(steps, 1):
        # Skip AI steps and steps before the last AI step
        if step_idx <= last_ai_step_idx or step.is_ai_step():
            continue

        step_name = str(step.function).split('.')[-1]
        step_dir = get_step_directory(new_version_dir, step_idx, step_name)

        # Get input from previous step's collated output
        prev_step = steps[step_idx - 2]  # 0-indexed
        prev_step_name = prev_step.prompt_name if prev_step.is_ai_step() else str(prev_step.function).split('.')[-1]
        prev_step_dir = get_step_directory(new_version_dir, step_idx - 1, prev_step_name)
        input_file = prev_step_dir / f"{prev_step_name}.json"

        # Load input data
        input_data = load_json(input_file)

        # Execute formatting function
        try:
            # Get module context from pipeline name
            output_data = run_formatting_step(
                step=step,
                input_data=input_data,
                input_content=None,
                module_number=module_number,
                path_letter=path_letter,
                project_root=project_root,
                verbose=False  # Suppress detailed execution logs
            )

            # Save output
            output_file = step_dir / f"{step_name}.json"
            save_json(output_file, output_data)

            if verbose:
                print(f"  [STEP {step_idx}] Re-ran {step_name} on merged data")
        except Exception as e:
            if verbose:
                print(f"  [STEP {step_idx}] ERROR re-running {step_name}: {e}")
            raise

    if verbose:
        print(f"\n[TEMPLATE RERUN] Re-collation complete!")

    return results


def load_json(file_path):
    """Load JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(file_path, data):
    """Save JSON file"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def merge_and_collate_templates(step_dir, base_step_dir=None, rerun_template_ids=None):
    """Smart merge: NEW regenerated templates + ALL other templates from base

    For template reruns, this merges:
    1. NEW items from regenerated templates (e.g., 4004.json from new version)
    2. UNCHANGED items from all other templates (from base version's items directory)

    This ensures the final output has ALL 108 items (or however many), not just the
    regenerated ones.

    Args:
        step_dir: New version step directory path (e.g., v15/step_01_problem_generator)
        base_step_dir: Base version step directory (e.g., v8/step_01_problem_generator)
        rerun_template_ids: Set of template IDs that were regenerated (e.g., {'4004'})
    """
    step_path = Path(step_dir)
    all_items = []
    processed_template_ids = set()

    # Build mappings from base version
    base_template_start_ids = {}  # {template_id: first_id}
    base_template_counts = {}     # {template_id: item_count}
    max_base_id = 0

    if base_step_dir:
        base_items_file = Path(base_step_dir) / "problem_generator.json"
        if base_items_file.exists():
            base_items = load_json(base_items_file)

            for item in base_items:
                template_id = str(item.get('template_id', ''))
                item_id = item.get('problem_instance_id', 0)

                # Track first ID for each template
                if template_id not in base_template_start_ids:
                    base_template_start_ids[template_id] = item_id
                    base_template_counts[template_id] = 0

                # Count items per template
                base_template_counts[template_id] += 1

                # Track max ID for appending new items at the end
                max_base_id = max(max_base_id, item_id)

    # Counter for items that exceed original template count
    next_overflow_id = max_base_id + 1

    # 1. Load NEW template files from current version (only regenerated ones exist)
    template_files = sorted(glob(str(step_path / "items" / "[0-9]*.json")))

    for template_file in template_files:
        items = load_json(template_file)
        template_id = Path(template_file).stem
        processed_template_ids.add(template_id)

        # Convert to list if single item
        if not isinstance(items, list):
            items = [items]

        # Get original slot info for this template
        start_id = base_template_start_ids.get(template_id, 1)
        original_count = base_template_counts.get(template_id, 0)

        for idx, item in enumerate(items):
            if idx < original_count:
                # Within original count: assign to original slot
                # E.g., template 4004 items 0-2 get IDs 28, 29, 30
                item['problem_instance_id'] = start_id + idx
            else:
                # Beyond original count: append to end of dataset
                # E.g., template 4004 items 3-4 get IDs 112, 113 (if max was 111)
                item['problem_instance_id'] = next_overflow_id
                next_overflow_id += 1

            all_items.append(item)

    # 2. Load ALL other templates from BASE version's COLLATED file
    # (Individual template files have relative IDs, collated has absolute IDs)
    if base_step_dir:
        base_collated_file = Path(base_step_dir) / "problem_generator.json"
        if base_collated_file.exists():
            base_all_items = load_json(base_collated_file)

            for item in base_all_items:
                template_id = str(item.get('template_id', ''))

                # Skip if this template was regenerated (already processed above)
                if template_id in processed_template_ids:
                    continue

                # Add item with its original absolute ID
                all_items.append(item)

    # Sort by problem_instance_id to maintain stable ordering
    all_items.sort(key=lambda x: x.get('problem_instance_id', 0))

    # Save collated (IDs are already correct - don't renumber!)
    save_json(step_path / "problem_generator.json", all_items)


def merge_and_collate_items(step_dir, step_name, base_step_dir=None, rerun_ids=None):
    """Smart merge: NEW regenerated items + ALL unchanged items from base

    For steps 2+, this merges:
    1. NEW items from new version's items/ directory (only regenerated items)
    2. ALL other items from base version's items/ directory (unchanged items)

    This ensures the final output has ALL items, not just regenerated ones.

    Args:
        step_dir: New version step directory path
        step_name: Step name for output file
        base_step_dir: Base version step directory (for merging unchanged items)
        rerun_ids: Set of problem IDs that were regenerated (to skip from base)
    """
    step_path = Path(step_dir)
    all_items = []
    loaded_ids = set()

    # Check if items directory exists (AI steps have items/, formatting steps don't)
    items_dir = step_path / "items"
    if not items_dir.exists():
        # This is a formatting step - no items to collate
        return

    # 1. Load NEW items from current version (only regenerated items exist here)
    item_files = sorted(
        glob(str(items_dir / "[0-9]*.json")),
        key=lambda x: int(Path(x).stem)
    )

    for item_file in item_files:
        item = load_json(item_file)

        # Handle both single items and lists of items
        if isinstance(item, list):
            for single_item in item:
                # Track the actual item's ID (not filename)
                item_problem_id = str(
                    single_item.get('problem_id') or
                    single_item.get('problem_instance_id') or
                    (single_item.get('metadata', {}).get('problem_id') if isinstance(single_item.get('metadata'), dict) else None) or
                    ''
                )
                if item_problem_id:
                    loaded_ids.add(item_problem_id)
                all_items.append(single_item)
        else:
            # Track the actual item's ID (not filename)
            item_problem_id = str(
                item.get('problem_id') or
                item.get('problem_instance_id') or
                (item.get('metadata', {}).get('problem_id') if isinstance(item.get('metadata'), dict) else None) or
                ''
            )
            if item_problem_id:
                loaded_ids.add(item_problem_id)
            all_items.append(item)

    # 2. Load ALL items from BASE version's COLLATED file (not items directory!)
    # The items directory may be incomplete (for rerun versions), so use collated file
    if base_step_dir:
        base_collated_file = Path(base_step_dir) / f"{step_name}.json"
        if base_collated_file.exists():
            base_all_items = load_json(base_collated_file)

            for item in base_all_items:
                # Try multiple paths for ID (some steps nest it in metadata)
                item_problem_id = str(
                    item.get('problem_id') or
                    item.get('problem_instance_id') or
                    (item.get('metadata', {}).get('problem_id') if isinstance(item.get('metadata'), dict) else None) or
                    ''
                )

                # Skip if this item was regenerated (in rerun_ids)
                if rerun_ids and item_problem_id in rerun_ids:
                    continue

                # Skip if already loaded from new version
                if item_problem_id in loaded_ids:
                    continue

                # Add item with its original ID
                all_items.append(item)

    # Sort by problem_id or problem_instance_id
    all_items.sort(key=lambda x: x.get('problem_id', x.get('problem_instance_id', 0)))

    # Save collated with step name
    save_json(step_path / f"{step_name}.json", all_items)


if __name__ == "__main__":
    main()
