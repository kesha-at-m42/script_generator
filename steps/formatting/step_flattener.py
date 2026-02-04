"""
Step Flattener - Formatting Step
Expands sequences with steps arrays into individual step items for batch processing
"""


def flatten_steps(input_data):
    """
    Flatten sequences into individual step items, handling both old and new formats.

    Supports two input formats:
    1. New format (problems 75+): Nested structure with "steps" array
    2. Old format (problems 1-74): Flat structure with fields at top level

    Each sequence becomes N separate items (one per step), with metadata
    fields duplicated to each item. Old flat structures are normalized to
    include step_id=1 and no_of_steps=1 if missing.

    Args:
        input_data: List of sequences (either format)

    Returns:
        List of flattened step items

    Example (new format):
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

    Example (old format):
        Input: [
            {
                "problem_id": 1,
                "template_id": "4001",
                "dialogue": "...",
                "prompt": "...",
                "workspace": []
            }
        ]

        Output: [
            {"problem_id": 1, "template_id": "4001", "step_id": 1, "no_of_steps": 1, "dialogue": "...", ...}
        ]
    """
    flattened = []

    for sequence in input_data:
        if "steps" in sequence:
            # New structure: flatten steps array
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
        else:
            # Old structure: already flat, normalize to match expected format
            # Add step_id and no_of_steps if missing
            normalized = {**sequence}
            if "step_id" not in normalized:
                normalized["step_id"] = 1
            if "no_of_steps" not in normalized:
                normalized["no_of_steps"] = 1

            flattened.append(normalized)

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
    # Test with sample data - mix of old and new formats
    sample_input = [
        # Old format (flat structure, no steps array)
        {
            "problem_id": 1,
            "template_id": "4001",
            "mastery_tier": "BASELINE",
            "mastery_verb": "IDENTIFY",
            "fractions": ["1/3"],
            "dialogue": "Look at the point.",
            "prompt": "What fraction?",
            "interaction_tool": "click_choice",
            "workspace": [],
            "correct_answer": {"value": "a", "context": "..."},
            "success_path_dialogue": "Yes!"
        },
        # New format (nested structure with steps array, single step)
        {
            "problem_id": 50,
            "template_id": "4010",
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
        # New format (nested structure with steps array, multiple steps)
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
    assert len(result) == 4  # 1 from old flat + 1 from new single-step + 2 from new multi-step

    # Test old flat format (problem 1)
    assert result[0]["problem_id"] == 1
    assert result[0]["step_id"] == 1  # Should be added
    assert result[0]["no_of_steps"] == 1  # Should be added
    assert result[0]["dialogue"] == "Look at the point."

    # Test new format single-step (problem 50)
    assert result[1]["problem_id"] == 50
    assert result[1]["step_id"] == 1
    assert result[1]["no_of_steps"] == 1

    # Test new format multi-step (problem 75)
    assert result[2]["problem_id"] == 75
    assert result[2]["step_id"] == 1
    assert result[2]["no_of_steps"] == 2
    assert result[3]["problem_id"] == 75
    assert result[3]["step_id"] == 2
    assert result[3]["no_of_steps"] == 2
    assert result[3]["workspace_inherited"] == True

    print("\nAll tests passed!")
