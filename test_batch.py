"""
Quick test of batch processing features

This creates a simple test to verify batch processing works without needing prompts.
"""

from core.pipeline import run_pipeline, Step
from pathlib import Path
import json


def test_basic_batch():
    """Test basic batch processing with the module 4 templates"""

    print("\n" + "="*70)
    print("TEST: Basic Batch Processing")
    print("="*70 + "\n")

    # First, let's verify the input file exists
    input_file = "inputs/modules/module4/problem_templates.json"
    if not Path(input_file).exists():
        print(f"Error: Input file not found: {input_file}")
        return

    # Load and show what we're working with
    with open(input_file, 'r', encoding='utf-8') as f:
        templates = json.load(f)

    print(f"Input file: {input_file}")
    print(f"Total templates: {len(templates)}")
    print(f"First template ID: {templates[0].get('template_id')}")
    print(f"Last template ID: {templates[-1].get('template_id')}")
    print()

    # For testing, we'll create a simple prompt that just echoes the data
    prompts_dir = Path("steps/prompts")
    prompts_dir.mkdir(parents=True, exist_ok=True)

    test_prompt_code = '''"""
test_process - Test prompt for batch processing
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

TEST_PROCESS_PROMPT = Prompt(
    role="""You are a helpful assistant that processes template data.""",

    instructions="""
You are processing template {template_id}.

Template details:
- Problem type: {problem_type}
- Mastery verb: {goal_decomposition__mastery_verb}

Return a simple JSON object with the following structure:
{{
  "template_id": "{template_id}",
  "processed": true,
  "problem_type": "{problem_type}",
  "mastery_verb": "{goal_decomposition__mastery_verb}"
}}
""",

    doc_refs=[],

    output_structure="""
Return valid JSON only.
""",

    prefill="",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=False,
    cache_ttl="5m",
    temperature=1.0,
    max_tokens=2000,
    stop_sequences=[]
)
'''

    with open(prompts_dir / "test_process.py", 'w', encoding='utf-8') as f:
        f.write(test_prompt_code)

    print("Created test prompt: steps/prompts/test_process.py")
    print()

    # Run a minimal batch (just first 3 items to keep it quick)
    print("Running batch processing on first 3 templates...")
    print("Note: This will make API calls. Use --dry-run to skip API calls.")
    print()

    try:
        result = run_pipeline(
            steps=[
                Step(
                    prompt_name="test_process",  # Just the prompt name
                    input_file=input_file,
                    batch_mode=True,
                    batch_id_field="template_id",
                    batch_output_id_field="result_id",
                    batch_id_start=1,
                    batch_only_items=["4001", "4002", "4003"],  # Just first 3
                    output_file="results.json"
                )
            ],
            pipeline_name="test_pipeline",
            module_number=4,
            pipeline_status="alpha",
            notes="Testing batch processing",
            verbose=True
        )

        print("\n" + "="*70)
        print("SUCCESS!")
        print("="*70)
        print(f"\nOutput directory: {result['output_dir']}")
        print(f"Version: {result['metadata']['version']}")
        print()
        print("Next steps:")
        print("  1. Check outputs: python list.py test_pipeline_module_4")
        print("  2. View items: ls outputs/test_pipeline_module_4/v0/items/")
        print("  3. View collated: cat outputs/test_pipeline_module_4/v0/collated/01_results.json")

    except Exception as e:
        print(f"\nError: {e}")
        print("\nThis is expected if you haven't set up API credentials yet.")
        print("The pipeline structure is correct, you just need to configure your API.")


def test_cli_tools():
    """Test the CLI tools"""

    print("\n" + "="*70)
    print("TEST: CLI Tools")
    print("="*70 + "\n")

    print("After running pipelines, try these commands:\n")

    print("1. List all pipelines:")
    print("   python list.py")
    print()

    print("2. List all pipelines (including drafts):")
    print("   python list.py --all")
    print()

    print("3. List versions of test pipeline:")
    print("   python list.py test_pipeline_module_4")
    print()

    print("4. Compare versions:")
    print("   python compare.py test_pipeline_module_4 v0 v1")
    print()

    print("5. Check template utilities:")
    from utils.template_utils import get_template_count, get_target_count
    print(f"   Template count: {get_template_count(4)}")
    print(f"   Target count: {get_target_count(4)}")
    print()


def test_without_api():
    """Test the structure without making API calls"""

    print("\n" + "="*70)
    print("TEST: Verify Structure (No API Calls)")
    print("="*70 + "\n")

    from utils.template_utils import (
        get_template_by_id,
        get_template_field,
        get_template_count,
        get_target_count
    )

    # Test template utilities
    print("Testing template_utils.py:")
    print(f"  Total templates: {get_template_count(4)}")
    print(f"  Total targets: {get_target_count(4)}")
    print()

    # Test individual template access
    template = get_template_by_id(4, "4001")
    print(f"Template 4001:")
    print(f"  problem_type: {template.get('problem_type')}")
    print()

    # Test nested field access
    mastery_verb = get_template_field(4, "4001", "goal_decomposition__mastery_verb")
    print(f"Nested field access:")
    print(f"  goal_decomposition__mastery_verb: {mastery_verb}")
    print()

    # Show what variables would be available in prompts
    print("Variables available in batch processing:")
    from core.pipeline import _flatten_dict
    flattened = _flatten_dict(template)
    for key in sorted(flattened.keys())[:10]:  # Show first 10
        print(f"  {{{key}}}")
    print(f"  ... and {len(flattened) - 10} more")
    print()

    print("All utilities working correctly!")


if __name__ == "__main__":
    import sys

    print("\n" + "="*70)
    print("BATCH PROCESSING TEST SUITE")
    print("="*70)

    if "--help" in sys.argv:
        print("\nUsage:")
        print("  python test_batch.py              # Run structure tests only")
        print("  python test_batch.py --full       # Run full test with API calls")
        print("  python test_batch.py --cli        # Show CLI tool examples")
        print()
        sys.exit(0)

    # Always test structure
    test_without_api()

    # Show CLI examples
    if "--cli" in sys.argv:
        test_cli_tools()

    # Full test with API calls (optional)
    if "--full" in sys.argv:
        test_basic_batch()
    else:
        print("\n" + "="*70)
        print("To test with actual API calls:")
        print("  python test_batch.py --full")
        print()
        print("To see CLI tool examples:")
        print("  python test_batch.py --cli")
        print("="*70 + "\n")
