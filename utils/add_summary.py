import json
import sys
import os
from typing import Dict, List

def generate_summary(sequences: List[Dict]) -> Dict:
    """Generate a summary of sequences by type and difficulty."""
    summary = {
        'total_sequences': len(sequences),
        'by_verb': {},
        'by_goal': {},
        'by_difficulty': {},
        'by_verb_and_difficulty': {},
        'matched': 0,
        'unmatched': 0
    }
    
    for seq in sequences:
        metadata = seq.get('@metadata')
        
        if metadata is None:
            summary['unmatched'] += 1
            continue
        
        summary['matched'] += 1
        
        # Count by verb
        verb = metadata.get('verb', 'UNKNOWN')
        summary['by_verb'][verb] = summary['by_verb'].get(verb, 0) + 1
        
        # Count by goal
        goal_id = metadata.get('goal_id', 0)
        goal_text = metadata.get('goal', 'Unknown goal')
        goal_key = f"Goal {goal_id}: {goal_text}"
        summary['by_goal'][goal_key] = summary['by_goal'].get(goal_key, 0) + 1
        
        # Count by difficulty
        difficulty = metadata.get('difficulty', -1)
        summary['by_difficulty'][str(difficulty)] = summary['by_difficulty'].get(str(difficulty), 0) + 1
        
        # Count by verb and difficulty combination
        combo_key = f"{verb} - Difficulty {difficulty}"
        summary['by_verb_and_difficulty'][combo_key] = summary['by_verb_and_difficulty'].get(combo_key, 0) + 1
    
    return summary

def order_keys(obj):
    """Recursively order keys to put @type and @summary at the top."""
    if isinstance(obj, dict):
        # If dict has @type and @summary, order: @type, @summary, then rest
        if '@type' in obj and '@summary' in obj:
            ordered = {'@type': obj['@type'], '@summary': obj['@summary']}
            for key, value in obj.items():
                if key not in ('@type', '@summary'):
                    ordered[key] = order_keys(value)
            return ordered
        # If dict has both @type and @metadata, order them correctly
        elif '@type' in obj and '@metadata' in obj:
            ordered = {'@type': obj['@type'], '@metadata': obj['@metadata']}
            for key, value in obj.items():
                if key not in ('@type', '@metadata'):
                    ordered[key] = order_keys(value)
            return ordered
        # If dict only has @metadata (no @type), put it first
        elif '@metadata' in obj:
            ordered = {'@metadata': obj['@metadata']}
            for key, value in obj.items():
                if key != '@metadata':
                    ordered[key] = order_keys(value)
            return ordered
        else:
            return {k: order_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [order_keys(item) for item in obj]
    else:
        return obj

def add_summary_to_file(input_path: str, output_path: str):
    """Add summary metadata to a JSON file."""
    
    print(f"Loading {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    print(f"Found {len(sequences)} sequences")
    
    # Generate summary
    print("\nGenerating summary...")
    summary = generate_summary(sequences)
    
    # Print summary to console
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Total sequences: {summary['total_sequences']}")
    print(f"  Matched: {summary['matched']}")
    print(f"  Unmatched: {summary['unmatched']}")
    print(f"\nBy Verb:")
    for verb, count in summary['by_verb'].items():
        print(f"  {verb}: {count}")
    print(f"\nBy Difficulty:")
    for diff, count in sorted(summary['by_difficulty'].items()):
        print(f"  Difficulty {diff}: {count}")
    print(f"\nBy Goal:")
    for goal, count in summary['by_goal'].items():
        print(f"  {goal}: {count}")
    print(f"{'='*60}")
    
    # Add summary to data
    data['@summary'] = summary
    
    # Order keys and save
    print(f"\nSaving to {output_path}...")
    ordered_data = order_keys(data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Output saved to: {output_path}")

def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print("Usage: python add_summary.py <input.json>")
        print("\nExample:")
        print("  python add_summary.py sequences_with_metadata.json")
        print("\nThis script will:")
        print("  - Read the JSON file")
        print("  - Generate a summary of cognitive types and difficulties")
        print("  - Add @summary field after @type: SequencePool")
        print("  - Save output as <input>_with_summary.json")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Generate output path with _with_summary suffix
    input_dir = os.path.dirname(input_path)
    input_name = os.path.basename(input_path)
    input_base, input_ext = os.path.splitext(input_name)
    output_name = f"{input_base}_with_summary{input_ext}"
    output_path = os.path.join(input_dir, output_name) if input_dir else output_name
    
    try:
        add_summary_to_file(input_path, output_path)
    except FileNotFoundError as e:
        print(f"✗ Error: File not found - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()