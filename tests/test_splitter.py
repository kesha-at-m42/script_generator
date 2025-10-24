import json
from steps.difficulty_splitter import DifficultySplitter
from pathlib import Path

# Load godot sequences
with open('outputs/test_godot_20251021_202555/godot_sequences.json') as f:
    data = json.load(f)

sequences = data.get('sequences', [])
print(f"Loaded {len(sequences)} sequences")

# Create output dir
output_dir = Path('outputs/test_difficulty_split')
output_dir.mkdir(exist_ok=True)

# Run splitter
splitter = DifficultySplitter()
result = splitter.execute(data, run_folder=output_dir)

print(f"\n✓ Split complete! Check {output_dir}/ for the split files")
print(f"Created {len(result.get('difficulty_files', {}))} files:")
for filename, info in result.get('difficulty_files', {}).items():
    print(f"  {filename}: {info['count']} sequences")

