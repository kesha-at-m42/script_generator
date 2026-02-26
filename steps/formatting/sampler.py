"""
Sampler - Creates test samples from generated content
"""

import random


def sample_per_template(data, sample_size=3, module_number=None, path_letter=None):
    """
    Sample N random sequences per template for testing

    Works with SequencePool structure where sequences have metadata.template_id

    Args:
        data: SequencePool dict with sequences array
        sample_size: Number of sequences to keep per template (default: 3)
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        SequencePool dict with randomly sampled sequences
    """
    # Validate input structure
    if not isinstance(data, dict) or "@type" not in data or data["@type"] != "SequencePool":
        raise ValueError("Expected SequencePool structure with @type and sequences")

    sequences = data.get("sequences", [])

    # Group by template_id from metadata
    by_template = {}
    for seq in sequences:
        template_id = seq.get("metadata", {}).get("template_id")
        if template_id:
            if template_id not in by_template:
                by_template[template_id] = []
            by_template[template_id].append(seq)

    # Take random sample_size from each template
    sampled = []
    for template_id in sorted(by_template.keys()):
        template_sequences = by_template[template_id]
        # Use random.sample if there are more sequences than sample_size
        if len(template_sequences) <= sample_size:
            sampled.extend(template_sequences)
        else:
            sampled.extend(random.sample(template_sequences, sample_size))

    # Return same structure with sampled sequences
    return {
        "@type": "SequencePool",
        "sequences": sampled
    }
