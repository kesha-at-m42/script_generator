"""Filter Godot sequences by one or more difficulty levels"""
import json
import sys
from pathlib import Path

def filter_by_difficulties(input_file, target_difficulties):
    """Filter godot sequences for specified difficulty levels"""
    
    # Map difficulty names to numbers
    difficulty_map = {
        "support": 0,
        "confidence": 1,
        "baseline": 2,
        "stretch": 3,
        "challenge": 4,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4
    }
    
    difficulty_names = {
        0: "support",
        1: "confidence",
        2: "baseline",
        3: "stretch",
        4: "challenge"
    }
    
    # Convert all target difficulties to numbers
    difficulty_levels = []
    for target in target_difficulties:
        target_lower = str(target).lower()
        if target_lower not in difficulty_map:
            print(f"❌ Error: Invalid difficulty '{target}'")
            print(f"   Valid options: {', '.join(sorted(set(difficulty_map.keys())))}")
            sys.exit(1)
        difficulty_levels.append(difficulty_map[target_lower])
    
    # Remove duplicates and sort
    difficulty_levels = sorted(set(difficulty_levels))
    
    print(f"Loading: {input_file}")
    print(f"Filtering for difficulty levels:")
    for level in difficulty_levels:
        print(f"  • Level {level} ({difficulty_names[level].capitalize()})")
    print()
    
    # Load data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    print(f"Total sequences: {len(sequences)}")
    
    # Filter for target difficulties
    filtered = []
    level_counts = {level: 0 for level in difficulty_levels}
    
    for seq in sequences:
        # Check if difficulty is in metadata (Godot format) or directly on sequence
        if 'metadata' in seq:
            difficulty = seq['metadata'].get('tier')
        else:
            difficulty = seq.get("tier")
        
        if difficulty in difficulty_levels:
            filtered.append(seq)
            level_counts[difficulty] += 1
    
    print(f"Matching sequences: {len(filtered)}")
    for level in difficulty_levels:
        print(f"  • {difficulty_names[level].capitalize()}: {level_counts[level]}")
    
    if not filtered:
        print(f"\n⚠️  No sequences found for specified difficulty levels")
        sys.exit(0)
    
    # Create output filename based on difficulties
    input_path = Path(input_file)
    if len(difficulty_levels) == 1:
        output_name = f"godot_{difficulty_names[difficulty_levels[0]]}.json"
    else:
        # Create a combined name
        names = [difficulty_names[level] for level in difficulty_levels]
        output_name = f"godot_{'_'.join(names)}.json"
    
    output_file = input_path.parent / output_name
    
    output_data = {
        "@type": "SequencePool",
        "sequences": filtered
    }
    
    # Save filtered data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n✅ Saved to: {output_file}")
    print(f"   Contains: {len(filtered)} sequences total")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python filter_godot_difficulty.py <input.json> <difficulty1> [difficulty2] [difficulty3] ...")
        print("\nDifficulty options:")
        print("  0 or support     - Support level")
        print("  1 or confidence  - Confidence level")
        print("  2 or baseline    - Baseline level")
        print("  3 or stretch     - Stretch level")
        print("  4 or challenge   - Challenge level")
        print("\nExamples:")
        print("  # Single difficulty:")
        print("  python filter_godot_difficulty.py godot.json baseline")
        print()
        print("  # Multiple difficulties:")
        print("  python filter_godot_difficulty.py godot.json support confidence")
        print("  python filter_godot_difficulty.py godot.json 0 1 2")
        print("  python filter_godot_difficulty.py godot.json baseline stretch challenge")
        sys.exit(1)
    
    input_file = sys.argv[1]
    target_difficulties = sys.argv[2:]  # Get all arguments after the input file
    
    filter_by_difficulties(input_file, target_difficulties)