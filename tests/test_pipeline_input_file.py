"""
Test that pipeline properly loads input_file from pipelines.json
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config.pipelines import PIPELINES

print("="*70)
print("Testing Pipeline Input File Loading")
print("="*70)

# Check new_warmup_generator pipeline
pipeline_name = "new_warmup_generator"
if pipeline_name in PIPELINES:
    pipeline = PIPELINES[pipeline_name]

    print(f"\nPipeline: {pipeline_name}")
    print(f"Number of steps: {len(pipeline)}")

    for i, step in enumerate(pipeline, 1):
        print(f"\n--- Step {i} ---")
        print(f"  Prompt name: {step.prompt_name}")
        print(f"  Input file: {step.input_file}")
        print(f"  Output file: {step.output_file}")

        if step.input_file:
            print(f"  [OK] Input file is configured!")
        else:
            print(f"  [WARN] No input file configured")
else:
    print(f"[ERROR] Pipeline '{pipeline_name}' not found")

print("\n" + "="*70)
