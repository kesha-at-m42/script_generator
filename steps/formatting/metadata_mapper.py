"""
Metadata Mapper
Maps input sequence fields to Godot mastery metadata structure
"""

def infer_component(verb):
    """
    Infer mastery component from cognitive verb

    Args:
        verb: Cognitive verb (e.g., "CREATE", "IDENTIFY", "COMPARE", "APPLY")

    Returns:
        str: Component type ("PROCEDURAL", "CONCEPTUAL", or "TRANSFER")

    Examples:
        >>> infer_component("CREATE")
        'PROCEDURAL'
        >>> infer_component("IDENTIFY")
        'CONCEPTUAL'
        >>> infer_component("APPLY")
        'TRANSFER'
    """
    # Map verb → mastery_component
    procedural_verbs = ['CREATE']
    conceptual_verbs = ['IDENTIFY', 'COMPARE']
    transfer_verbs = ['APPLY', 'TRANSFER', 'CONNECT']

    verb_upper = str(verb).upper()

    if verb_upper in procedural_verbs:
        return "PROCEDURAL"
    elif verb_upper in conceptual_verbs:
        return "CONCEPTUAL"
    elif verb_upper in transfer_verbs:
        return "TRANSFER"
    else:
        return "PROCEDURAL"  # default


def add_component_to_metadata(data):
    """
    Add mastery_component to both metadata level and telemetry_data

    Args:
        data: Either a single sequence dict or a list of sequences

    Returns:
        Updated data (same type as input)
    """
    def process_sequence(sequence):
        """Process a single sequence"""
        # Get the verb from metadata
        if 'metadata' in sequence:
            metadata = sequence['metadata']
            verb = metadata.get('mastery_verb') or metadata.get('verb', 'CREATE')

            # Infer component
            component = infer_component(verb)

            # Add to metadata level
            metadata['mastery_component'] = component

            # Add to telemetry_data
            if 'telemetry_data' not in metadata:
                metadata['telemetry_data'] = {}
            metadata['telemetry_data']['component'] = component.lower()

        return sequence

    # Handle both single sequence and list of sequences
    if isinstance(data, list):
        return [process_sequence(seq) for seq in data]
    else:
        return process_sequence(data)