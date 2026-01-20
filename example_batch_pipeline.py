"""
Example: Batch Processing Pipeline with Versioning

This example demonstrates how to use the new batch processing features:
- Process templates one-by-one with separate API calls
- Version-based output structure
- Automatic collation
- Rerun specific items

Workflow:
1. Initial run: Process all 14 templates → outputs/problem_generator/v0/
2. Review outputs, find issues with template 4002
3. Rerun: Process only 4002 → outputs/problem_generator/v1/
4. Result: v1 merges v0 items + new 4002
"""

from core.pipeline import run_pipeline, Step


def example_initial_run():
    """Example: Initial pipeline run with batch processing"""

    print("\n" + "="*70)
    print("EXAMPLE: Initial Batch Pipeline Run")
    print("="*70 + "\n")

    result = run_pipeline(
        steps=[
            Step(
                prompt_name="generate_interaction",
                input_file="inputs/modules/module4/problem_templates.json",
                batch_mode=True,                     # Enable batch processing
                batch_id_field="template_id",        # Use template_id for tracking
                batch_output_id_field="interaction_id",  # Add sequential IDs
                batch_id_start=1,                    # Start from 1
                output_file="interactions.json"      # Collated output
            ),
            Step(
                prompt_name="format_interaction",
                # Auto-chains from previous step
                batch_mode=True,                     # Process interactions one-by-one
                batch_id_field="interaction_id",
                output_file="formatted.json"
            )
        ],
        pipeline_name="problem_generator",  # Enables versioning
        module_number=4,
        pipeline_status="alpha",            # Mark as alpha/beta/rc/final
        notes="Initial test run with new prompt",  # Optional notes
        verbose=True
    )

    print(f"\n✓ Pipeline complete!")
    print(f"  Output: {result['output_dir']}")
    print(f"  Version: {result['metadata']['version']}")
    print(f"\nStructure:")
    print(f"  outputs/problem_generator_module_4/")
    print(f"  ├─ v0/                         # First version")
    print(f"  │  ├─ items/                   # Individual results")
    print(f"  │  │  ├─ 4001/")
    print(f"  │  │  │  ├─ 01_output.json")
    print(f"  │  │  │  └─ 02_output.json")
    print(f"  │  │  ├─ 4002/")
    print(f"  │  │  └─ ...")
    print(f"  │  ├─ collated/                # Collated arrays")
    print(f"  │  │  ├─ 01_interactions.json")
    print(f"  │  │  └─ 02_formatted.json")
    print(f"  │  ├─ prompts/                 # Saved prompts")
    print(f"  │  └─ metadata.json            # Pipeline metadata")
    print(f"  └─ latest -> v0                # Symlink to latest")


def example_rerun():
    """Example: Rerun specific items"""

    print("\n" + "="*70)
    print("EXAMPLE: Rerun Specific Items")
    print("="*70 + "\n")

    result = run_pipeline(
        steps=[
            Step(
                prompt_name="generate_interaction",
                input_file="inputs/modules/module4/problem_templates.json",
                batch_mode=True,
                batch_id_field="template_id",
                batch_output_id_field="interaction_id",
                output_file="interactions.json"
            ),
            Step(
                prompt_name="format_interaction",
                batch_mode=True,
                batch_id_field="interaction_id",
                output_file="formatted.json"
            )
        ],
        pipeline_name="problem_generator",
        module_number=4,
        rerun_items=["4002", "4007"],  # Only process these items
        verbose=True
    )

    print(f"\n✓ Rerun complete!")
    print(f"  New version: {result['metadata']['version']}")
    print(f"  Base version: {result['metadata']['base_version']}")
    print(f"\nWhat happened:")
    print(f"  1. Created v1 directory")
    print(f"  2. Processed only items 4002 and 4007")
    print(f"  3. Collated outputs merge v0 + v1 items")
    print(f"  4. Updated latest -> v1")


def example_with_filters():
    """Example: Using batch filters"""

    print("\n" + "="*70)
    print("EXAMPLE: Batch Filters")
    print("="*70 + "\n")

    result = run_pipeline(
        steps=[
            Step(
                prompt_name="generate_interaction",
                input_file="inputs/modules/module4/problem_templates.json",
                batch_mode=True,
                batch_id_field="template_id",
                batch_skip_existing=True,     # Skip items that already have outputs
                batch_only_items=["4001", "4002", "4003"],  # Only these
                # OR
                # batch_skip_items=["4010", "4011"],  # Skip these
                batch_stop_on_error=False,    # Continue on errors
                output_file="interactions.json"
            )
        ],
        pipeline_name="problem_generator_filtered",
        module_number=4,
        verbose=True
    )

    print(f"\n✓ Complete with filters!")


def example_cli_usage():
    """Example: CLI tools usage"""

    print("\n" + "="*70)
    print("EXAMPLE: CLI Tools")
    print("="*70 + "\n")

    print("After running pipelines, use these CLI tools:\n")

    print("1. List all pipelines:")
    print("   python list.py")
    print()

    print("2. List versions of a pipeline:")
    print("   python list.py problem_generator")
    print()

    print("3. Compare two versions:")
    print("   python compare.py problem_generator v0 v1")
    print("   python compare.py problem_generator v0 v1 --detail")
    print()

    print("4. Rerun specific items (currently shows instructions):")
    print("   python rerun.py problem_generator 4002")
    print("   python rerun.py problem_generator 4002 4007 --note 'Fixed prompt'")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("BATCH PROCESSING EXAMPLES")
    print("="*70)
    print("\nThis file shows examples of the new batch processing features.")
    print("Uncomment the examples you want to run.\n")

    # Uncomment to run examples:
    # example_initial_run()
    # example_rerun()
    # example_with_filters()
    example_cli_usage()

    print("\n" + "="*70)
    print("For more information, see:")
    print("  - core/pipeline.py (Step class documentation)")
    print("  - Documentation on batch_mode parameters")
    print("="*70 + "\n")
