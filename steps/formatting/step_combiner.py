"""
Step Combiner - Formatting Step
Combines flattened step items back into sequences with steps arrays
"""

from collections import defaultdict


def combine_steps(input_data):
    """
    Combine flattened step items back into sequences with steps arrays.

    Groups items by problem_id and restructures into sequence format with
    metadata at top level and step-specific fields in steps array.

    Args:
        input_data: List of flattened items with step_id and no_of_steps

    Returns:
        List of sequences with steps arrays

    Example:
        Input: [
            {
                "problem_id": 75,
                "step_id": 1,
                "no_of_steps": 2,
                "template_id": "5011",
                "mastery_tier": "BASELINE",
                "dialogue": "Step 1 dialogue",
                "prompt": "Step 1 prompt",
                ...
            },
            {
                "problem_id": 75,
                "step_id": 2,
                "no_of_steps": 2,
                "template_id": "5011",
                "mastery_tier": "BASELINE",
                "dialogue": "Step 2 dialogue",
                "prompt": "Step 2 prompt",
                ...
            }
        ]

        Output: [
            {
                "problem_id": 75,
                "template_id": "5011",
                "mastery_tier": "BASELINE",
                "no_of_steps": 2,
                "steps": [
                    {
                        "step_id": 1,
                        "dialogue": "Step 1 dialogue",
                        "prompt": "Step 1 prompt",
                        ...
                    },
                    {
                        "step_id": 2,
                        "dialogue": "Step 2 dialogue",
                        "prompt": "Step 2 prompt",
                        ...
                    }
                ]
            }
        ]
    """
    # Define which fields belong to sequence metadata vs step data
    METADATA_FIELDS = {
        'problem_id',
        'template_id',
        'mastery_tier',
        'mastery_verb',
        'fractions',
        'no_of_steps'
    }

    # Group items by problem_id
    grouped = defaultdict(list)
    for item in input_data:
        problem_id = item.get('problem_id')
        grouped[problem_id].append(item)

    # Combine into sequences
    sequences = []
    for problem_id in sorted(grouped.keys()):
        items = grouped[problem_id]

        # Sort items by step_id
        items.sort(key=lambda x: x.get('step_id', 1))

        # Extract metadata from first item (should be same for all items)
        metadata = {
            field: items[0][field]
            for field in METADATA_FIELDS
            if field in items[0]
        }

        # Build steps array with step-specific fields
        steps = []
        for item in items:
            step = {
                key: value
                for key, value in item.items()
                if key not in METADATA_FIELDS
            }
            steps.append(step)

        # Create sequence
        sequence = {
            **metadata,
            'steps': steps
        }

        sequences.append(sequence)

    return sequences


# Entry point for pipeline
def main(input_data, **kwargs):
    """
    Main entry point for pipeline execution

    Args:
        input_data: List of flattened items from previous step
        **kwargs: Additional arguments (unused)

    Returns:
        List of sequences with steps arrays
    """
    return combine_steps(input_data)


if __name__ == "__main__":
    # Test with sample data
    sample_input = [
        # Single-step problem
        {
            "problem_id": 1,
            "step_id": 1,
            "no_of_steps": 1,
            "template_id": "4001",
            "mastery_tier": "BASELINE",
            "mastery_verb": "IDENTIFY",
            "fractions": ["1/3"],
            "dialogue": "Look at the point.",
            "prompt": "What fraction?",
            "interaction_tool": "click_choice",
            "workspace": [],
            "correct_answer": {"value": "a"},
            "success_path_dialogue": "Yes!",
            "error_path_generic": {"steps": []}
        },
        # Multi-step problem (step 1)
        {
            "problem_id": 75,
            "step_id": 1,
            "no_of_steps": 2,
            "template_id": "5011",
            "mastery_tier": "BASELINE",
            "mastery_verb": "create",
            "fractions": ["1/4", "2/4", "3/4"],
            "dialogue": "Divide the line.",
            "prompt": "Divide into fourths.",
            "interaction_tool": "place_tick",
            "workspace": [],
            "correct_answer": {"value": ["0", "1/4", "2/4", "3/4", "1"]},
            "success_path_dialogue": "Right.",
            "error_path_generic": {"steps": []}
        },
        # Multi-step problem (step 2)
        {
            "problem_id": 75,
            "step_id": 2,
            "no_of_steps": 2,
            "template_id": "5011",
            "mastery_tier": "BASELINE",
            "mastery_verb": "create",
            "fractions": ["1/4", "2/4", "3/4"],
            "dialogue": "Label positions.",
            "prompt": "Label each tick.",
            "interaction_tool": "drag_label",
            "workspace": [],
            "correct_answer": {"value": {}},
            "success_path_dialogue": "Good!",
            "error_path_generic": {"steps": []}
        }
    ]

    result = combine_steps(sample_input)

    print(f"Input: {len(sample_input)} flattened items")
    print(f"Output: {len(result)} sequences")
    print("\nSequences:")
    for seq in result:
        print(f"  - problem_id={seq['problem_id']}, no_of_steps={seq['no_of_steps']}, steps in array={len(seq['steps'])}")

    # Verify structure
    assert len(result) == 2  # 2 unique problem_ids

    # Check single-step problem
    assert result[0]["problem_id"] == 1
    assert result[0]["no_of_steps"] == 1
    assert len(result[0]["steps"]) == 1
    assert result[0]["steps"][0]["step_id"] == 1
    assert "dialogue" in result[0]["steps"][0]
    assert "template_id" not in result[0]["steps"][0]  # Should be in metadata, not step

    # Check multi-step problem
    assert result[1]["problem_id"] == 75
    assert result[1]["no_of_steps"] == 2
    assert len(result[1]["steps"]) == 2
    assert result[1]["steps"][0]["step_id"] == 1
    assert result[1]["steps"][1]["step_id"] == 2
    assert "template_id" not in result[1]["steps"][0]  # Should be in metadata, not step

    print("\nAll tests passed!")
