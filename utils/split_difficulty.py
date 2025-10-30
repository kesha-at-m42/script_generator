"""Split Godot sequences by difficulty level and/or verb"""
import json
import sys
from pathlib import Path
from datetime import datetime

def split_by_difficulty(input_file):
    """Split godot sequences by difficulty level"""
    
    print(f"Loading: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    print(f"Found {len(sequences)} sequences\n")
    
    # Group by difficulty
    difficulty_groups = {
        0: [],  # Support
        1: [],  # Confidence  
        2: [],  # Baseline
        3: [],  # Stretch
        4: []   # Challenge
    }
    
    difficulty_names = {
        0: "support",
        1: "confidence",
        2: "baseline",
        3: "stretch",
        4: "challenge"
    }
    
    # Group sequences by difficulty
    for seq in sequences:
        # Check if difficulty is in metadata (Godot format) or directly on sequence
        if 'metadata' in seq:
            difficulty = seq['metadata'].get('difficulty')
        else:
            difficulty = seq.get("difficulty")
        
        if difficulty in difficulty_groups:
            difficulty_groups[difficulty].append(seq)
        else:
            print(f"⚠️  Unknown difficulty: {difficulty} in problem_id {seq.get('metadata', {}).get('problem_id', seq.get('problem_id'))}")
    
    # Print summary
    print("Difficulty distribution:")
    for level in sorted(difficulty_groups.keys()):
        items = difficulty_groups[level]
        if items:
            name = difficulty_names[level].capitalize()
            print(f"  Level {level} ({name}): {len(items)} sequences")
    
    # Create output directory
    input_path = Path(input_file)
    output_dir = input_path.parent / "difficulty_split"
    output_dir.mkdir(exist_ok=True)
    
    # Save each difficulty level
    print(f"\nSaving to: {output_dir}")
    for level, items in difficulty_groups.items():
        if not items:
            continue
        
        name = difficulty_names[level]
        output_file = output_dir / f"godot_{name}.json"
        
        output_data = {
            "@type": "SequencePool",
            "sequences": items
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"  ✓ {output_file.name}: {len(items)} sequences")
    
    print(f"\n✅ Complete! Output in: {output_dir}")


def split_by_verb(input_file):
    """Split godot sequences by verb"""
    
    print(f"Loading: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    print(f"Found {len(sequences)} sequences\n")
    
    # Group by verb
    verb_groups = {}
    
    # Group sequences by verb
    for seq in sequences:
        # Check if verb is in metadata (Godot format) or directly on sequence
        if 'metadata' in seq:
            verb = seq['metadata'].get('verb')
        else:
            verb = seq.get("verb")
        
        if verb:
            verb_lower = verb.lower()
            if verb_lower not in verb_groups:
                verb_groups[verb_lower] = []
            verb_groups[verb_lower].append(seq)
        else:
            print(f"⚠️  No verb found in problem_id {seq.get('metadata', {}).get('problem_id', seq.get('problem_id'))}")
    
    # Print summary
    print("Verb distribution:")
    for verb in sorted(verb_groups.keys()):
        items = verb_groups[verb]
        print(f"  {verb.upper()}: {len(items)} sequences")
    
    # Create output directory
    input_path = Path(input_file)
    output_dir = input_path.parent / "verb_split"
    output_dir.mkdir(exist_ok=True)
    
    # Save each verb group
    print(f"\nSaving to: {output_dir}")
    for verb, items in verb_groups.items():
        if not items:
            continue
        
        output_file = output_dir / f"godot_{verb}.json"
        
        output_data = {
            "@type": "SequencePool",
            "sequences": items
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"  ✓ {output_file.name}: {len(items)} sequences")
    
    print(f"\n✅ Complete! Output in: {output_dir}")


def split_by_both(input_file):
    """Split godot sequences by both difficulty and verb"""
    
    print(f"Loading: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    print(f"Found {len(sequences)} sequences\n")
    
    # Group by difficulty + verb combination
    combo_groups = {}
    
    difficulty_names = {
        0: "support",
        1: "confidence",
        2: "baseline",
        3: "stretch",
        4: "challenge"
    }
    
    # Group sequences by difficulty + verb
    for seq in sequences:
        # Extract metadata
        if 'metadata' in seq:
            metadata = seq['metadata']
            difficulty = metadata.get('difficulty')
            verb = metadata.get('verb')
        else:
            difficulty = seq.get('difficulty')
            verb = seq.get('verb')
        
        if difficulty is not None and verb:
            diff_name = difficulty_names.get(difficulty, f"level{difficulty}")
            verb_lower = verb.lower()
            key = f"{diff_name}_{verb_lower}"
            
            if key not in combo_groups:
                combo_groups[key] = []
            combo_groups[key].append(seq)
    
    # Print summary
    print("Difficulty + Verb distribution:")
    for key in sorted(combo_groups.keys()):
        items = combo_groups[key]
        print(f"  {key}: {len(items)} sequences")
    
    # Create output directory
    input_path = Path(input_file)
    output_dir = input_path.parent / "difficulty_verb_split"
    output_dir.mkdir(exist_ok=True)
    
    # Save each combination
    print(f"\nSaving to: {output_dir}")
    for key, items in sorted(combo_groups.items()):
        if not items:
            continue
        
        output_file = output_dir / f"godot_{key}.json"
        
        output_data = {
            "@type": "SequencePool",
            "sequences": items
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"  ✓ {output_file.name}: {len(items)} sequences")
    
    print(f"\n✅ Complete! Output in: {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_godot.py <godot_sequences.json> [--by difficulty|verb|both]")
        print("\nExamples:")
        print("  python split_godot.py godot.json                  # Split by difficulty (default)")
        print("  python split_godot.py godot.json --by verb        # Split by verb")
        print("  python split_godot.py godot.json --by both        # Split by difficulty + verb")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check for --by argument
    split_type = "difficulty"  # default
    if len(sys.argv) >= 4 and sys.argv[2] == "--by":
        split_type = sys.argv[3].lower()
    
    if split_type == "verb":
        split_by_verb(input_file)
    elif split_type == "both":
        split_by_both(input_file)
    else:
        split_by_difficulty(input_file)
