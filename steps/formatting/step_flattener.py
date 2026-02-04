"""
Step Flattener - Formatting Step
Expands sequences with steps arrays into individual step items for batch processing
"""


def flatten_steps(input_data):
    """
    Flatten sequences with steps arrays into individual step items.

    Each sequence becomes N separate items (one per step), with metadata
    fields duplicated to each item.

    Args:
        input_data: List of sequences, each with a steps array

    Returns:
        List of flattened step items

    Example:
        Input: [
            {
                "problem_id": 75,
                "template_id": "5011",
                "no_of_steps": 2,
                "steps": [
                    {"step_id": 1, "dialogue": "...", ...},
                    {"step_id": 2, "dialogue": "...", ...}
                ]
            }
        ]

        Output: [
            {"problem_id": 75, "step_id": 1, "template_id": "5011", "no_of_steps": 2, "dialogue": "...", ...},
            {"problem_id": 75, "step_id": 2, "template_id": "5011", "no_of_steps": 2, "dialogue": "...", ...}
        ]
    """
    flattened = []

    for sequence in input_data:
        # Extract metadata fields (everything except steps)
        metadata = {
            key: value
            for key, value in sequence.items()
            if key != "steps"
        }

        # Flatten each step
        for step in sequence.get("steps", []):
            # Merge metadata with step fields
            flattened_item = {
                **metadata,  # problem_id, template_id, mastery_tier, etc.
                **step       # step_id, dialogue, prompt, workspace, etc.
            }

            flattened.append(flattened_item)

    return flattened


# Entry point for pipeline
def main(input_data, **kwargs):
    """
    Main entry point for pipeline execution

    Args:
        input_data: List of sequences from sequence_structurer
        **kwargs: Additional arguments (unused)

    Returns:
        List of flattened step items
    """
    return flatten_steps(input_data)


if __name__ == "__main__":
    # Test with sample data
    sample_input = [
        {
            "problem_id": 1,
            "template_id": "4001",
            "mastery_tier": "BASELINE",
            "mastery_verb": "IDENTIFY",
            "fractions": ["1/3"],
            "no_of_steps": 1,
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Look at the point.",
                    "prompt": "What fraction?",
                    "interaction_tool": "click_choice",
                    "workspace": [],
                    "correct_answer": {"value": "a", "context": "..."},
                    "success_path_dialogue": "Yes!"
                }
            ]
        },
        {
            "problem_id": 75,
            "template_id": "5011",
            "mastery_tier": "BASELINE",
            "mastery_verb": "create",
            "fractions": ["1/4", "2/4", "3/4"],
            "no_of_steps": 2,
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Divide the line.",
                    "prompt": "Divide into fourths.",
                    "interaction_tool": "place_tick",
                    "workspace": [],
                    "correct_answer": {"value": ["0", "1/4", "2/4", "3/4", "1"], "context": "..."},
                    "success_path_dialogue": "Right."
                },
                {
                    "step_id": 2,
                    "workspace_inherited": True,
                    "dialogue": "Label positions.",
                    "prompt": "Label each tick.",
                    "interaction_tool": "drag_label",
                    "workspace": [],
                    "correct_answer": {"value": {}, "context": "..."},
                    "success_path_dialogue": "Good!"
                }
            ]
        }
    ]

    result = flatten_steps(sample_input)

    print(f"Input: {len(sample_input)} sequences")
    print(f"Output: {len(result)} flattened items")
    print("\nFlattened items:")
    for item in result:
        print(f"  - problem_id={item['problem_id']}, step_id={item['step_id']}, no_of_steps={item['no_of_steps']}")

    # Verify structure
    assert len(result) == 3  # 1 step from first + 2 steps from second
    assert result[0]["problem_id"] == 1
    assert result[0]["step_id"] == 1
    assert result[1]["problem_id"] == 75
    assert result[1]["step_id"] == 1
    assert result[2]["problem_id"] == 75
    assert result[2]["step_id"] == 2
    assert result[2]["workspace_inherited"] == True

    print("\nAll tests passed!")
