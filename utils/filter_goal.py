"""Filter Godot sequences by one or more goal IDs"""
import json
import sys
from pathlib import Path

def filter_by_goals(input_file, target_goals):
    """Filter godot sequences for specified goal IDs"""
    # Convert all target goals to integers (if possible)
    goal_ids = []
    for goal in target_goals:
        try:
            goal_ids.append(int(goal))
        except ValueError:
            print(f"❌ Error: Invalid goal ID '{goal}' (must be integer)")
            sys.exit(1)
    goal_ids = sorted(set(goal_ids))
    print(f"Loading: {input_file}")
    print(f"Filtering for goal IDs:")
    for gid in goal_ids:
        print(f"  • Goal ID {gid}")
    print()
    # Load data
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    sequences = data.get('sequences', [])
    print(f"Total sequences: {len(sequences)}")
    # Filter for target goals
    filtered = []
    goal_counts = {gid: 0 for gid in goal_ids}
    for seq in sequences:
        # Check if goal_id is in metadata or directly on sequence
        if 'metadata' in seq:
            goal_id = seq['metadata'].get('goal_id')
        else:
            goal_id = seq.get("goal_id")
        if goal_id in goal_ids:
            filtered.append(seq)
            goal_counts[goal_id] += 1
    print(f"Matching sequences: {len(filtered)}")
    for gid in goal_ids:
        print(f"  • Goal {gid}: {goal_counts[gid]}")
    if not filtered:
        print(f"\n⚠️  No sequences found for specified goal IDs")
        sys.exit(0)
    # Create output filename based on goals
    input_path = Path(input_file)
    if len(goal_ids) == 1:
        output_name = f"godot_goal{goal_ids[0]}.json"
    else:
        output_name = f"godot_goal_{'_'.join(str(gid) for gid in goal_ids)}.json"
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
        print("Usage: python filter_goal.py <input.json> <goal_id1> [goal_id2] [goal_id3] ...")
        print("\nExamples:")
        print("  # Single goal:")
        print("  python filter_goal.py godot.json 1")
        print()
        print("  # Multiple goals:")
        print("  python filter_goal.py godot.json 1 2 3")
        sys.exit(1)
    input_file = sys.argv[1]
    target_goals = sys.argv[2:]  # Get all arguments after the input file
    filter_by_goals(input_file, target_goals)
