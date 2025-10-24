"""Split godot_first_50.json by difficulty level"""
import json
from pathlib import Path
from collections import defaultdict

# Load the file
input_file = Path('examples/godot_first_50.json')
with open(input_file) as f:
    data = json.load(f)

sequences = data.get('sequences', [])
print(f"Loaded {len(sequences)} sequences\n")

# Group by difficulty
difficulty_groups = defaultdict.fromkeys(range(5), [])
for i in range(5):
    difficulty_groups[i] = []

for seq in sequences:
    difficulty = seq.get('@metadata', {}).get('difficulty', 0)
    difficulty_groups[difficulty].append(seq)

# Print summary
difficulty_names = {
    0: "support",
    1: "confidence", 
    2: "baseline",
    3: "stretch",
    4: "challenge"
}

print("Difficulty distribution:")
for level in range(5):
    count = len(difficulty_groups[level])
    name = difficulty_names[level].capitalize()
    print(f"  Level {level} ({name}): {count} sequences")

# Save split files
output_dir = Path('examples')
for level in range(5):
    if difficulty_groups[level]:
        name = difficulty_names[level]
        filename = f"godot_{name}.json"
        filepath = output_dir / filename
        
        output = {
            "@type": "SequencePool",
            "sequences": difficulty_groups[level]
        }
        
        with open(filepath, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"\n✓ Saved {len(difficulty_groups[level])} sequences to {filename}")

print("\n✓ Split complete!")
