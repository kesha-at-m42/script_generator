"""
Batch Processing Test

Simple test for batch processing features using test_prompt.py.

Usage:
  python tests/test_batch_pipeline.py                    # Dry run (no API calls)
  python tests/test_batch_pipeline.py --run              # Run with first 3 items
  python tests/test_batch_pipeline.py --run --all        # Run all items
  python tests/test_batch_pipeline.py --rerun 4001 4002  # Rerun specific items
  python tests/test_batch_pipeline.py --cli              # Show CLI examples
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.pipeline import run_pipeline, Step
import json


def run_batch_test(only_items=None, rerun_items=None, verbose=True):
    """
    Run batch processing test with test_prompt

    Args:
        only_items: List of template IDs to process (e.g., ["4001", "4002", "4003"])
        rerun_items: List of template IDs to rerun
        verbose: Print detailed output
    """
    print("\n" + "="*70)
    print("BATCH PROCESSING TEST")
    print("="*70 + "\n")

    # Verify input file
    input_file = "modules/module4/problem_templates.json"
    if not Path(input_file).exists():
        print(f"ERROR: Input file not found: {input_file}")
        return None

    # Show what we're processing
    with open(input_file, 'r', encoding='utf-8') as f:
        templates = json.load(f)

    print(f"Input: {input_file}")
    print(f"Total templates: {len(templates)}")
    print(f"Prompt: steps/prompts/test_prompt.py")

    if only_items:
        print(f"Processing: {', '.join(only_items)}")
    elif rerun_items:
        print(f"Rerunning: {', '.join(rerun_items)}")
    else:
        print(f"Processing: All {len(templates)} items")
    print()

    # Configure step
    step_config = {
        "prompt_name": "test_prompt",
        "input_file": input_file,
        "batch_mode": True,
        "batch_id_field": "template_id",
        "batch_output_id_field": "result_id",
        "batch_id_start": 1,
        "output_file": "results.json"
    }

    if only_items:
        step_config["batch_only_items"] = only_items

    # Run pipeline
    try:
        result = run_pipeline(
            steps=[Step(**step_config)],
            pipeline_name="test_batch",
            module_number=4,
            pipeline_status="alpha",
            notes="Batch processing test",
            rerun_items=rerun_items,
            verbose=verbose
        )

        print("\n" + "="*70)
        print("SUCCESS!")
        print("="*70)
        print(f"\nOutput: {result['output_dir']}")
        print(f"Version: {result['metadata']['version']}")
        if result['metadata'].get('base_version'):
            print(f"Base version: {result['metadata']['base_version']}")
        print()
        print("Check results:")
        print(f"  Items:    {result['output_dir']}/items/")
        print(f"  Collated: {result['output_dir']}/collated/01_results.json")
        print()

        return result

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return None


def show_cli_tools():
    """Show CLI tool examples"""
    print("\n" + "="*70)
    print("CLI TOOLS")
    print("="*70 + "\n")

    print("List pipelines:")
    print("  python cli/list.py\n")

    print("List versions:")
    print("  python cli/list.py test_batch_module_4\n")

    print("Compare versions:")
    print("  python cli/compare.py test_batch_module_4 v0 v1")
    print("  python cli/compare.py test_batch_module_4 v0 v1 --detail\n")


def show_structure():
    """Show output structure"""
    print("\nOutput structure:")
    print("  outputs/test_batch_module_4/")
    print("    v0/")
    print("      items/4001/01_output.json")
    print("      collated/01_results.json")
    print("      prompts/01_test_prompt.md")
    print("      metadata.json")
    print("    latest -> v0")
    print()


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        show_structure()
        show_cli_tools()
        sys.exit(0)

    if "--cli" in sys.argv:
        show_cli_tools()
        sys.exit(0)

    # Parse run mode
    should_run = "--run" in sys.argv
    run_all = "--all" in sys.argv

    # Check for rerun
    if "--rerun" in sys.argv:
        try:
            idx = sys.argv.index("--rerun")
            rerun_items = [arg for arg in sys.argv[idx + 1:] if not arg.startswith("--")]

            if not rerun_items:
                print("\nERROR: --rerun requires item IDs")
                print("Example: python tests/test_batch_pipeline.py --rerun 4001 4002")
                sys.exit(1)

            run_batch_test(rerun_items=rerun_items)

        except ValueError:
            print("\nERROR: Invalid --rerun syntax")
            sys.exit(1)

    elif should_run:
        only_items = None if run_all else ["4001", "4002", "4003"]

        if only_items:
            print("\n> Running with first 3 items (use --all for all)")
        else:
            print("\n> Running with ALL items")

        run_batch_test(only_items=only_items)

    else:
        # Dry run
        print("\n> DRY RUN (no API calls)")
        show_structure()
        print("Run test:")
        print("  python tests/test_batch_pipeline.py --run")
        print("  python tests/test_batch_pipeline.py --run --all")
        print()
        print("Rerun items:")
        print("  python tests/test_batch_pipeline.py --rerun 4001 4002")
        print()
        print("CLI tools:")
        print("  python tests/test_batch_pipeline.py --cli")
        print()
