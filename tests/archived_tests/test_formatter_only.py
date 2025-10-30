"""Test just the ScriptFormatter step"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from steps.script_formatter import ScriptFormatter

print("Testing ScriptFormatter only...\n")

# Load sample sequence data from previous run
sequence_file = Path("outputs/test_dialogue_only.json")

if not sequence_file.exists():
    print(f"❌ Sequence file not found: {sequence_file}")
    print("Please run test_dialogue_writer_only.py first to generate sequence data.")
    sys.exit(1)

with open(sequence_file, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

sequences = input_data.get('sequences', [])
print(f"📖 Loaded {len(sequences)} sequences from {sequence_file}\n")

# Test formatter
formatter = ScriptFormatter()

# Create a mock run folder for testing
test_folder = Path("outputs/test_formatter")
test_folder.mkdir(parents=True, exist_ok=True)

# Execute with run_folder
result = formatter.execute(input_data, run_folder=test_folder)

print(f"\n✅ Formatted {result['total_problems']} problems")
print(f"📁 Output saved to: {test_folder}\n")

# Show preview
print("=" * 70)
print("Preview:")
print("=" * 70)
print(result['combined_script'][:1000])
print("...")
print("=" * 70)
