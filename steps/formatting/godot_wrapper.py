"""
Godot Wrapper - Wraps sequence array in SequencePool structure
"""


def wrap_in_sequence_pool(sequences_data, module_number=None, path_letter=None):
    """
    Wrap an array of sequences in a SequencePool structure

    Args:
        sequences_data: List of sequence dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        Dictionary with SequencePool wrapper structure
    """
    # Handle both list and dict with "sequences" key
    if isinstance(sequences_data, dict) and "sequences" in sequences_data:
        # Already wrapped, return as-is
        return sequences_data
    elif isinstance(sequences_data, list):
        sequences = sequences_data
    else:
        raise ValueError("Expected list of sequences or dict with 'sequences' key")

    # Wrap in SequencePool structure
    return {
        "@type": "SequencePool",
        "sequences": sequences
    }
