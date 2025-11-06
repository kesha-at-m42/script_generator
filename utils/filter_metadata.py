"""Generic filter for Godot sequences by any metadata fields"""
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple


def parse_filter_args(args: List[str]) -> Dict[str, List[Any]]:
    """
    Parse command line arguments into field-value pairs.

    Format: field1=value1 field1=value2 field2=value3

    Returns dict like: {"field1": ["value1", "value2"], "field2": ["value3"]}
    """
    filters = {}

    for arg in args:
        if '=' not in arg:
            print(f"❌ Error: Invalid filter format '{arg}'")
            print(f"   Expected format: field=value")
            sys.exit(1)

        field, value = arg.split('=', 1)
        field = field.strip()
        value = value.strip()

        # Try to convert to int if possible (for numeric fields)
        try:
            value = int(value)
        except ValueError:
            pass  # Keep as string

        if field not in filters:
            filters[field] = []
        filters[field].append(value)

    return filters


def matches_filters(sequence: Dict[str, Any], filters: Dict[str, List[Any]]) -> bool:
    """
    Check if a sequence matches all filter criteria.

    A sequence matches if for each field in filters, the sequence's value
    for that field is in the list of acceptable values.
    """
    # Get metadata (could be nested or at top level)
    metadata = sequence.get('metadata', sequence)

    for field, acceptable_values in filters.items():
        # Get the field value from metadata
        field_value = metadata.get(field)

        # If field doesn't exist in this sequence, no match
        if field_value is None:
            return False

        # Check if the value matches any of the acceptable values
        if field_value not in acceptable_values:
            return False

    return True


def filter_by_metadata(input_file: str, filter_args: List[str]) -> None:
    """Filter sequences by arbitrary metadata fields"""

    if not filter_args:
        print("❌ Error: No filters specified")
        print("   Usage: python filter_metadata.py <input.json> field1=value1 [field2=value2] ...")
        sys.exit(1)

    # Parse filter arguments
    filters = parse_filter_args(filter_args)

    print(f"Loading: {input_file}")
    print(f"Filtering by:")
    for field, values in filters.items():
        values_str = ", ".join(str(v) for v in values)
        print(f"  • {field}: {values_str}")
    print()

    # Load data
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {input_file}")
        print(f"   {e}")
        sys.exit(1)

    sequences = data.get('sequences', [])
    print(f"Total sequences: {len(sequences)}")

    # Filter sequences
    filtered = []
    field_counts = {field: {v: 0 for v in values} for field, values in filters.items()}

    for seq in sequences:
        if matches_filters(seq, filters):
            filtered.append(seq)

            # Update counts for each field
            metadata = seq.get('metadata', seq)
            for field in filters.keys():
                value = metadata.get(field)
                if value in field_counts[field]:
                    field_counts[field][value] += 1

    print(f"Matching sequences: {len(filtered)}")

    # Print breakdown by each filter field
    for field, value_counts in field_counts.items():
        print(f"\n  {field}:")
        for value, count in value_counts.items():
            print(f"    • {value}: {count}")

    if not filtered:
        print(f"\n⚠️  No sequences found matching the specified filters")
        sys.exit(0)

    # Create output filename based on filters
    input_path = Path(input_file)

    # Build a descriptive filename
    filter_parts = []
    for field, values in filters.items():
        if len(values) == 1:
            filter_parts.append(f"{field}_{values[0]}")
        else:
            filter_parts.append(f"{field}_multiple")

    output_name = f"godot_{'_'.join(filter_parts)}.json"
    output_file = input_path.parent / output_name

    output_data = {
        "@type": "SequencePool",
        "sequences": filtered
    }

    # Save filtered data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)

    print(f"\n✅ Saved to: {output_file}")
    print(f"   Contains: {len(filtered)} sequences")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Generic Metadata Filter for Godot Sequences")
        print("=" * 50)
        print("\nUsage:")
        print("  python filter_metadata.py <input.json> field1=value1 [field2=value2] ...")
        print("\nExamples:")
        print("  # Filter by single field:")
        print("  python filter_metadata.py final.json goal_id=1")
        print()
        print("  # Filter by multiple values of same field:")
        print("  python filter_metadata.py final.json goal_id=1 goal_id=2")
        print()
        print("  # Filter by multiple fields (AND logic):")
        print("  python filter_metadata.py final.json goal_id=1 tier=2")
        print()
        print("  # Complex filter:")
        print("  python filter_metadata.py final.json goal_id=1 tier=2 verb=CREATE")
        print()
        print("  # Filter by mastery component:")
        print("  python filter_metadata.py final.json mastery_component=PROCEDURAL")
        print()
        print("Notes:")
        print("  • All filters use AND logic (sequence must match all criteria)")
        print("  • Multiple values for same field use OR logic")
        print("  • Numeric values are automatically detected")
        print("  • Searches in both 'metadata' object and top-level fields")
        sys.exit(1)

    input_file = sys.argv[1]
    filter_args = sys.argv[2:]

    filter_by_metadata(input_file, filter_args)
