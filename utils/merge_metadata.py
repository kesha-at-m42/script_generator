import json
import sys
from typing import Dict, List, Optional, Tuple

def copy_metadata_to_remediations(step1: Dict, step2: Dict):
    """Copy @metadata from step2 remediations to step1 remediations."""
    prompt1 = step1.get('prompt', {})
    prompt2 = step2.get('prompt', {})
    
    remediations1 = prompt1.get('remediations', [])
    remediations2 = prompt2.get('remediations', [])
    
    # Create a map of remediation id to metadata
    remediation_metadata_map = {}
    for rem2 in remediations2:
        rem_id = rem2.get('id')
        rem_step = rem2.get('step', {})
        if '@metadata' in rem_step:
            remediation_metadata_map[rem_id] = rem_step['@metadata']
    
    # Apply metadata to matching remediations in step1
    for rem1 in remediations1:
        rem_id = rem1.get('id')
        if rem_id in remediation_metadata_map:
            rem_step = rem1.get('step', {})
            if rem_step:
                rem_step['@metadata'] = remediation_metadata_map[rem_id].copy()

def get_goal_text(goal_id: int) -> str:
    """Return the goal description for a given goal_id."""
    goals = {
        1: "The student can partition shapes into equal parts",
        2: "The student can recognize and identify equal versus unequal parts",
        3: "The student can shade one part to represent a unit fraction",
        4: "The student can identify and maintain the whole when working with fractions",
        5: "The student can understand that all parts must be equal for fractions"
    }
    return goals.get(goal_id, "Unknown goal")

def extract_fractions(tangibles: List[Dict]) -> List[str]:
    """Extract unique fractions from workspace tangibles."""
    fractions = set()
    for t in tangibles:
        if 'fractions' in t:
            if isinstance(t['fractions'], str):
                fractions.add(t['fractions'])
            elif isinstance(t['fractions'], list):
                fractions.update(t['fractions'])
    return sorted(list(fractions))

def find_matching_metadata(seq: Dict, file2_sequences: List[Dict]) -> Optional[Tuple[Dict, Dict]]:
    """Find matching metadata from file2 sequences."""
    
    # Get characteristics of the sequence we're trying to match
    first_step = seq['steps'][0]
    dialogue1 = first_step.get('dialogue', '').lower()
    prompt1 = first_step.get('prompt', {})
    tool1 = prompt1.get('tool', '')
    validator1 = prompt1.get('validator', {}).get('@type', '')
    num_steps1 = len(seq['steps'])
    
    tangibles1 = first_step.get('workspace', {}).get('tangibles', [])
    num_tangibles1 = len(tangibles1)
    fractions1 = extract_fractions(tangibles1)
    
    # Try to find exact or close match in file2
    best_match = None
    best_match_seq = None
    best_score = 0
    
    for seq2 in file2_sequences:
        if '@metadata' not in seq2:
            continue
            
        first_step2 = seq2['steps'][0]
        dialogue2 = first_step2.get('dialogue', '').lower()
        prompt2 = first_step2.get('prompt', {})
        tool2 = prompt2.get('tool', '')
        validator2 = prompt2.get('validator', {}).get('@type', '')
        num_steps2 = len(seq2['steps'])
        
        tangibles2 = first_step2.get('workspace', {}).get('tangibles', [])
        num_tangibles2 = len(tangibles2)
        fractions2 = extract_fractions(tangibles2)
        
        # Calculate match score
        score = 0
        
        # Same tool is very important
        if tool1 == tool2:
            score += 10
        
        # Same validator type
        if validator1 == validator2:
            score += 8
        
        # Same number of steps
        if num_steps1 == num_steps2:
            score += 5
        
        # Same number of tangibles
        if num_tangibles1 == num_tangibles2:
            score += 3
        
        # Matching fractions
        if set(fractions1) == set(fractions2):
            score += 15
        elif len(set(fractions1) & set(fractions2)) > 0:
            score += 5
        
        # Similar dialogue (check for key phrases)
        key_phrases = ['equal parts', 'divide', 'shade', 'select', 'whole', 'thirds', 'fourths', 'halves', 'sixths', 'eighths']
        phrases1 = [p for p in key_phrases if p in dialogue1]
        phrases2 = [p for p in key_phrases if p in dialogue2]
        
        matching_phrases = len(set(phrases1) & set(phrases2))
        score += matching_phrases * 2
        
        # Update best match if this is better
        if score > best_score and score >= 20:  # Minimum threshold of 20
            best_score = score
            best_match = seq2['@metadata']
            best_match_seq = seq2
    
    # Return both the metadata and the full matching sequence
    return (best_match, best_match_seq) if best_match else (None, None)

def merge_metadata(file1_path: str, file2_path: str, output_path: str):
    """Merge metadata from file2 into file1 sequences."""
    
    # Load both files
    print(f"Loading {file1_path}...")
    with open(file1_path, 'r', encoding='utf-8') as f:
        file1_data = json.load(f)
    
    print(f"Loading {file2_path}...")
    with open(file2_path, 'r', encoding='utf-8') as f:
        file2_data = json.load(f)
    
    file2_sequences = file2_data.get('sequences', [])
    print(f"\nFound {len(file2_sequences)} sequences in file2")
    
    # Process file1 sequences
    print(f"Processing {len(file1_data['sequences'])} sequences from file1...\n")
    
    matched_count = 0
    unmatched_count = 0
    
    for index, seq in enumerate(file1_data['sequences']):
        # Try to find matching metadata from file2
        matched_metadata, matched_seq = find_matching_metadata(seq, file2_sequences)
        
        # Add metadata directly to existing sequence
        if matched_metadata:
            seq['@metadata'] = matched_metadata.copy()
            seq['@metadata']['problem_id'] = index + 1  # Update problem_id sequentially
            matched_count += 1
            print(f"  ✓ Sequence {index + 1}: MATCHED - {seq['@metadata']['verb']} - Goal {seq['@metadata']['goal_id']} - Difficulty {seq['@metadata']['difficulty']}")
            
            # Copy metadata from remediations if we found a matching sequence
            if matched_seq:
                for step_idx, step1 in enumerate(seq['steps']):
                    if step_idx < len(matched_seq['steps']):
                        step2 = matched_seq['steps'][step_idx]
                        copy_metadata_to_remediations(step1, step2)
        else:
            seq['@metadata'] = None
            unmatched_count += 1
            print(f"  ✗ Sequence {index + 1}: NO MATCH - metadata set to null")
    
    # Save merged file
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total sequences: {len(file1_data['sequences'])}")
    print(f"  Matched: {matched_count}")
    print(f"  Unmatched (null): {unmatched_count}")
    print(f"{'='*60}")
    
    print(f"\nSaving to {output_path}...")
    
    # Custom JSON encoder to ensure @metadata appears after @type
    def order_keys(obj):
        if isinstance(obj, dict):
            # If dict has both @type and @metadata, order them correctly
            if '@type' in obj and '@metadata' in obj:
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
    
    ordered_data = order_keys(file1_data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Output saved to: {output_path}")

def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python merge_metadata.py <file1.json> <file2.json>")
        print("\nExample:")
        print("  python merge_metadata.py sequences_no_metadata.json sequences_with_metadata.json")
        print("\nThis script will:")
        print("  - Match sequences from file1 with sequences in file2")
        print("  - Copy metadata from file2 when a match is found")
        print("  - Set @metadata to null for sequences with no match")
        print("  - Save output as <file1>_metadata_merged.json")
        sys.exit(1)
    
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    
    # Generate output path with _metadata_merged suffix
    import os
    file1_dir = os.path.dirname(file1_path)
    file1_name = os.path.basename(file1_path)
    file1_base, file1_ext = os.path.splitext(file1_name)
    output_name = f"{file1_base}_metadata_merged{file1_ext}"
    output_path = os.path.join(file1_dir, output_name) if file1_dir else output_name
    
    try:
        merge_metadata(file1_path, file2_path, output_path)
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