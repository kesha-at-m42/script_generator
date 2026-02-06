"""
NumLine Fixer - Formatting Step

Fixes NumLine issues:
1. Ensures all labels are strings, not numeric values
2. Adds alt_labels for whole number positions when using frac_labels mode
3. Ensures whole number ticks and labels exist when range extends beyond 2
4. Removes ticks from ticks_is_read_only if they're in LabelValidator answer
"""

from fractions import Fraction


def parse_fraction(frac_str):
    """
    Parse a fraction string to get its decimal value.

    Args:
        frac_str: Fraction string like "3/4", "2/2", or "3"

    Returns:
        tuple: (numerator, denominator, decimal_value)
    """
    if '/' in str(frac_str):
        parts = frac_str.split('/')
        num, denom = int(parts[0]), int(parts[1])
        return num, denom, num / denom
    else:
        # Whole number
        val = int(frac_str)
        return val, 1, float(val)


def is_whole_number(frac_str):
    """Check if a fraction string represents a whole number."""
    try:
        num, denom, decimal = parse_fraction(frac_str)
        return num % denom == 0
    except:
        return False


def simplify_to_whole(frac_str):
    """Convert a whole number fraction to its whole number string."""
    try:
        num, denom, decimal = parse_fraction(frac_str)
        if num % denom == 0:
            return str(num // denom)
    except:
        pass
    return frac_str


def get_whole_numbers_in_range(range_list):
    """
    Get all whole number positions within a range.

    Args:
        range_list: [start, end] like [0, 3]

    Returns:
        list: Whole number strings like ["0", "1", "2", "3"]
    """
    if not isinstance(range_list, list) or len(range_list) != 2:
        return []

    start, end = range_list
    whole_numbers = []
    for i in range(int(start), int(end) + 1):
        whole_numbers.append(str(i))
    return whole_numbers


def fix_numline_labels(data):
    """
    Recursively fix NumLine labels to ensure they are strings.

    Converts numeric values in labels arrays to strings while preserving
    string values. Handles boolean labels (true/false) without modification.

    Args:
        data: Any data structure (dict, list, or primitive)

    Returns:
        Fixed data structure with string labels
    """
    if isinstance(data, dict):
        # Check if this is a NumLine with labels array
        if data.get("@type") == "NumLine" and "labels" in data:
            labels = data["labels"]

            # Only fix if labels is an array (not boolean)
            if isinstance(labels, list):
                fixed_labels = []
                for label in labels:
                    if isinstance(label, (int, float)):
                        # Convert numeric to string
                        if isinstance(label, int) or label.is_integer():
                            fixed_labels.append(str(int(label)))
                        else:
                            fixed_labels.append(str(label))
                    else:
                        # Keep strings as-is
                        fixed_labels.append(label)

                data["labels"] = fixed_labels

        # Recursively process all dict values
        return {key: fix_numline_labels(value) for key, value in data.items()}

    elif isinstance(data, list):
        # Recursively process all list items
        return [fix_numline_labels(item) for item in data]

    else:
        # Primitive value, return as-is
        return data


def add_alt_labels_for_whole_numbers(step):
    """
    Add alt_labels to NumLine when frac_labels mode has whole number fractions.

    When a Move tool with mode="frac_labels" has whole number fractions in the
    palette (like "2/2", "3/3", "6/3"), add alt_labels to show the simplified
    whole numbers ("1", "2") as fixed reference labels.

    Args:
        step: Step dictionary

    Returns:
        Modified step dictionary
    """
    prompt = step.get('prompt', {})
    if not isinstance(prompt, dict):
        return step

    tool = prompt.get('tool', {})
    if not isinstance(tool, dict):
        return step

    # Check if this is frac_labels mode
    if tool.get('mode') != 'frac_labels':
        return step

    # Get palette labels
    palette = tool.get('palette', {})
    stacks = palette.get('stacks', [])
    palette_labels = [stack.get('label') for stack in stacks]

    # Find whole number fractions in palette
    whole_number_positions = set()
    for label in palette_labels:
        if label and is_whole_number(label):
            simplified = simplify_to_whole(label)
            whole_number_positions.add(simplified)

    # If no whole numbers in palette, nothing to do
    if not whole_number_positions:
        return step

    # Add alt_labels to NumLine tangibles
    workspace = step.get('workspace', {})
    if not isinstance(workspace, dict):
        return step

    tangibles = workspace.get('tangibles', [])
    for tangible in tangibles:
        if tangible.get('@type') == 'NumLine':
            # Don't override existing alt_labels
            if tangible.get('alt_labels') is None:
                # Get the range to determine which whole numbers to show
                range_list = tangible.get('range', [0, 1])
                whole_numbers_in_range = get_whole_numbers_in_range(range_list)

                # Only add alt_labels for whole numbers in the palette that are in range
                alt_labels = [wn for wn in whole_numbers_in_range
                             if wn in whole_number_positions]

                if alt_labels:
                    tangible['alt_labels'] = alt_labels

    return step


def ensure_whole_number_ticks_and_labels(tangible):
    """
    Ensure NumLine has ticks and labels at all whole number positions when range > 2.

    When a number line extends beyond 2 (like [0, 3] or [0, 4]), ensure there are
    ticks and labels at all whole number positions (0, 1, 2, 3, etc.).

    Args:
        tangible: NumLine tangible dictionary

    Returns:
        Modified tangible dictionary
    """
    if tangible.get('@type') != 'NumLine':
        return tangible

    range_list = tangible.get('range', [0, 1])
    if not isinstance(range_list, list) or len(range_list) != 2:
        return tangible

    start, end = range_list

    # Only apply if range extends beyond 2
    if end <= 2:
        return tangible

    # Get all whole numbers in range
    whole_numbers = get_whole_numbers_in_range(range_list)

    # Ensure ticks includes all whole numbers (if ticks is an array)
    ticks = tangible.get('ticks')
    if isinstance(ticks, list):
        # Add any missing whole numbers to ticks
        ticks_set = set(ticks)
        for wn in whole_numbers:
            if wn not in ticks_set:
                ticks.append(wn)
        # Sort ticks by their numeric value
        try:
            ticks.sort(key=lambda x: parse_fraction(x)[2])
        except:
            pass  # If sorting fails, keep original order

    # Ensure labels includes all whole numbers
    labels = tangible.get('labels')
    if isinstance(labels, list):
        # Add any missing whole numbers to labels
        labels_set = set(labels)
        for wn in whole_numbers:
            if wn not in labels_set:
                labels.append(wn)
        # Sort labels by their numeric value
        try:
            labels.sort(key=lambda x: parse_fraction(x)[2])
        except:
            pass  # If sorting fails, keep original order

    return tangible


def are_fractions_equal(frac1, frac2):
    """
    Check if two fraction strings are mathematically equal.

    Args:
        frac1: First fraction string (e.g., "6/3", "2")
        frac2: Second fraction string (e.g., "2", "6/3")

    Returns:
        bool: True if fractions are equal
    """
    try:
        _, _, decimal1 = parse_fraction(frac1)
        _, _, decimal2 = parse_fraction(frac2)
        return abs(decimal1 - decimal2) < 0.0001  # Allow for floating point errors
    except:
        return False


def fix_ticks_readonly_for_label_validator(step):
    """
    Remove ticks from ticks_is_read_only if they are in the LabelValidator answer.

    When a LabelValidator expects a label to be placed at a tick position,
    that tick should not be read-only. This function removes any tick positions
    from ticks_is_read_only that appear in the validator's answer array.

    Handles equivalent fractions: if answer has "6/3" and ticks_is_read_only has "2",
    removes "2" since 6/3 = 2.

    Args:
        step: Step dictionary

    Returns:
        Modified step dictionary
    """
    prompt = step.get('prompt', {})
    if not isinstance(prompt, dict):
        return step

    validator = prompt.get('validator', {})
    if not isinstance(validator, dict):
        return step

    # Check if this is a LabelValidator
    if validator.get('@type') != 'LabelValidator':
        return step

    # Get the answer array
    answer = validator.get('answer', [])
    if not isinstance(answer, list) or not answer:
        return step

    # Fix ticks_is_read_only in NumLine tangibles
    workspace = step.get('workspace', {})
    if not isinstance(workspace, dict):
        return step

    tangibles = workspace.get('tangibles', [])
    for tangible in tangibles:
        if tangible.get('@type') == 'NumLine':
            ticks_readonly = tangible.get('ticks_is_read_only')

            # Only process if ticks_is_read_only is an array
            if isinstance(ticks_readonly, list):
                # Remove any ticks that match an answer position (including equivalent fractions)
                updated_readonly = []
                for tick in ticks_readonly:
                    # Check if this tick is equivalent to any answer position
                    is_answer_position = False
                    for answer_frac in answer:
                        if are_fractions_equal(tick, answer_frac):
                            is_answer_position = True
                            break

                    if not is_answer_position:
                        updated_readonly.append(tick)

                # Update the field if changes were made
                if len(updated_readonly) != len(ticks_readonly):
                    tangible['ticks_is_read_only'] = updated_readonly

    return step


def process_sequences(input_data):
    """
    Process input data to fix NumLine issues.

    Handles both formats:
    1. List of sequences with steps arrays
    2. List of flattened step items

    Args:
        input_data: List of sequences or flattened items

    Returns:
        List with fixed NumLine labels and alt_labels
    """
    # First pass: Fix numeric labels to strings
    data = fix_numline_labels(input_data)

    # Second pass: Add alt_labels for whole numbers and ensure whole number ticks
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                # Check if this is a sequence with steps
                if 'steps' in item:
                    for step in item.get('steps', []):
                        # Add alt_labels for whole numbers
                        add_alt_labels_for_whole_numbers(step)

                        # Fix ticks_is_read_only for LabelValidator
                        fix_ticks_readonly_for_label_validator(step)

                        # Ensure whole number ticks/labels
                        workspace = step.get('workspace', {})
                        if isinstance(workspace, dict):
                            tangibles = workspace.get('tangibles', [])
                            for tangible in tangibles:
                                ensure_whole_number_ticks_and_labels(tangible)

                # Or flattened step item
                elif 'workspace' in item or 'prompt' in item:
                    # Add alt_labels for whole numbers
                    add_alt_labels_for_whole_numbers(item)

                    # Fix ticks_is_read_only for LabelValidator
                    fix_ticks_readonly_for_label_validator(item)

                    # Ensure whole number ticks/labels
                    workspace = item.get('workspace', {})
                    if isinstance(workspace, dict):
                        tangibles = workspace.get('tangibles', [])
                        for tangible in tangibles:
                            ensure_whole_number_ticks_and_labels(tangible)

    return data


# Entry point for pipeline
def main(input_data, **kwargs):
    """
    Main entry point for pipeline execution

    Args:
        input_data: List of sequences or flattened items
        **kwargs: Additional arguments (unused)

    Returns:
        List with fixed NumLine labels and alt_labels
    """
    return process_sequences(input_data)


if __name__ == "__main__":
    # Test with sample data
    sample_input = [
        # Test 1: Numeric labels (needs fixing)
        {
            "problem_id": 36,
            "template_id": "5004",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Look at the point.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 1],
                                "ticks": "1/6",
                                "points": ["4/6"],
                                "labels": [0, "1/2", 1],  # NUMERIC - needs fixing
                                "lcm": 18
                            }
                        ]
                    }
                }
            ]
        },
        # Test 2: frac_labels with whole number fraction (needs alt_labels)
        {
            "problem_id": 45,
            "template_id": "5011",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Drag labels.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 1],
                                "ticks": "1/2",
                                "labels": ["0", "1"],
                                "lcm": 12
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Drag the label.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "2/2"}
                                ]
                            }
                        }
                    }
                }
            ]
        },
        # Test 3: Extended range beyond 2 (needs whole number labels)
        {
            "problem_id": 57,
            "template_id": "5015",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Drag labels.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 3],
                                "ticks": "1/3",
                                "labels": ["0", "1/3"],  # Missing "1", "2", "3"
                                "lcm": 12
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Drag labels.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "4/3"},
                                    {"@type": "FracLabelStack", "label": "6/3"}
                                ]
                            }
                        }
                    }
                }
            ]
        },
        # Test 4: ticks_is_read_only should exclude answer positions
        {
            "problem_id": 60,
            "template_id": "5020",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Place fractions.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 2],
                                "ticks": ["0", "1/3", "2/3", "1", "4/3", "5/3", "2"],
                                "labels": ["0", "1", "2"],
                                "ticks_is_read_only": ["0", "1", "2"],  # "2" should be removed (6/3 = 2)
                                "lcm": 9
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Place the fractions.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "4/3"},
                                    {"@type": "FracLabelStack", "label": "5/3"},
                                    {"@type": "FracLabelStack", "label": "6/3"}
                                ]
                            }
                        },
                        "validator": {
                            "@type": "LabelValidator",
                            "answer": ["4/3", "5/3", "6/3"]
                        }
                    }
                }
            ]
        }
    ]

    result = process_sequences(sample_input)

    print("Testing NumLine Fixer")
    print("=" * 70)

    # Test 1: Numeric labels should be fixed
    print("\nTest 1 - Numeric labels fixed:")
    labels_1 = result[0]["steps"][0]["workspace"]["tangibles"][0]["labels"]
    print(f"  Input:  [0, '1/2', 1]")
    print(f"  Output: {labels_1}")
    assert labels_1 == ["0", "1/2", "1"], f"Expected ['0', '1/2', '1'], got {labels_1}"
    assert all(isinstance(label, str) for label in labels_1), "All labels should be strings"
    print("  PASS - All labels are now strings")

    # Test 2: alt_labels should be added for whole number fractions
    print("\nTest 2 - alt_labels added for whole number fractions:")
    tangible_2 = result[1]["steps"][0]["workspace"]["tangibles"][0]
    alt_labels_2 = tangible_2.get("alt_labels")
    print(f"  Palette has: ['2/2'] (equals 1)")
    print(f"  Alt_labels added: {alt_labels_2}")
    assert alt_labels_2 == ["1"], f"Expected ['1'], got {alt_labels_2}"
    print("  PASS - alt_labels correctly shows whole number")

    # Test 3: Whole number labels should be added when range > 2
    print("\nTest 3 - Whole number labels added for extended range:")
    labels_3 = result[2]["steps"][0]["workspace"]["tangibles"][0]["labels"]
    print(f"  Range: [0, 3]")
    print(f"  Input labels:  ['0', '1/3']")
    print(f"  Output labels: {labels_3}")
    for wn in ["0", "1", "2", "3"]:
        assert wn in labels_3, f"Expected '{wn}' in labels"
    print("  PASS - All whole numbers (0, 1, 2, 3) are in labels")

    # Also check alt_labels for Test 3
    tangible_3 = result[2]["steps"][0]["workspace"]["tangibles"][0]
    alt_labels_3 = tangible_3.get("alt_labels")
    print(f"  Alt_labels added: {alt_labels_3}")
    assert "2" in alt_labels_3, "Expected '2' in alt_labels (from 6/3)"
    print("  PASS - alt_labels shows whole number from palette")

    # Test 4: ticks_is_read_only should exclude answer positions
    print("\nTest 4 - ticks_is_read_only excludes answer positions:")
    tangible_4 = result[3]["steps"][0]["workspace"]["tangibles"][0]
    ticks_readonly_4 = tangible_4.get("ticks_is_read_only")
    print(f"  Input ticks_is_read_only:  ['0', '1', '2']")
    print(f"  Validator answer: ['4/3', '5/3', '6/3'] (6/3 = 2)")
    print(f"  Output ticks_is_read_only: {ticks_readonly_4}")
    assert "2" not in ticks_readonly_4, "Expected '2' to be removed (6/3 = 2 is in answer)"
    assert "0" in ticks_readonly_4, "Expected '0' to remain (not in answer)"
    assert "1" in ticks_readonly_4, "Expected '1' to remain (not in answer)"
    print("  PASS - '2' removed from read-only (matches 6/3 in answer)")

    print("\n" + "=" * 70)
    print("All tests passed!")
