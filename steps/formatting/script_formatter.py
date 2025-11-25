"""
Script Formatter - Deterministic formatting step
Converts interactions JSON into human-readable markdown scripts
"""


def format_interactions_to_markdown(interactions_data, module_number=None, path_letter=None):
    """
    Convert interactions JSON into human-readable markdown script

    Args:
        interactions_data: List of interaction dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        String containing markdown formatted script
    """
    # Handle both list and dict with "sequences" key
    if isinstance(interactions_data, dict) and "sequences" in interactions_data:
        interactions = interactions_data["sequences"]
    elif isinstance(interactions_data, list):
        interactions = interactions_data
    else:
        raise ValueError("Expected list of interactions or dict with 'sequences' key")

    markdown_lines = []

    # Format each interaction
    for interaction in interactions:
        interaction_md = _format_single_interaction(interaction)
        markdown_lines.append(interaction_md)
        markdown_lines.append("")
        markdown_lines.append("=" * 80)
        markdown_lines.append("")

    return "\n".join(markdown_lines)


def _format_single_interaction(interaction: dict) -> str:
    """Format a single interaction into markdown"""
    lines = []

    # Header
    interaction_id = interaction.get("interaction_id", "?")
    interaction_name = interaction.get("interaction_name", "Unnamed Interaction")

    lines.append(f"# Interaction {interaction_id}: {interaction_name}")
    lines.append("---")
    lines.append("")

    # Format steps (without step numbers, flows naturally)
    steps = interaction.get("steps", [])
    for step in steps:
        step_md = _format_step(step)
        lines.append(step_md)

    return "\n".join(lines)


def _format_step(step: dict) -> str:
    """Format a single step into markdown"""
    lines = []

    # Guide dialogue (⚫)
    dialogue = step.get("dialogue")
    if dialogue:
        lines.append(f"⚫ **Guide:** \"{dialogue}\"")
        lines.append("")
    
    # Screen prompt (⚪)
    prompt = step.get("prompt")
    if prompt:
        lines.append(f"⚪ **Prompt:** {prompt}")

    # Workspace / Visual (🔵)
    workspace = step.get("workspace", [])
    if workspace:
        lines.append(f"🔵 **Visual:**")
        for ws_item in workspace:
            ws_md = _format_workspace_item(ws_item)
            lines.append(ws_md)
        lines.append("")

    # Tool
    interaction_tool = step.get("interaction_tool")
    if interaction_tool:
        lines.append(f"   **Interaction Tool:** {interaction_tool}")

        # Answer inline
        correct_answer = step.get("correct_answer")
        if correct_answer:
            if isinstance(correct_answer, dict):
                answer_val = correct_answer.get("value", "N/A")
            else:
                answer_val = correct_answer
            lines.append(f"   **Answer:** {answer_val}")

        lines.append("")

    # Student attempts - success path
    student_attempts = step.get("student_attempts")
    if student_attempts:
        success_path = student_attempts.get("success_path")
        if success_path:
            success_dialogue = success_path.get("dialogue", "")
            if success_dialogue:
                lines.append(f"⚫ **Guide: (If student answers correctly)** \"{success_dialogue}\"")
                lines.append("")

    return "\n".join(lines)


def _format_workspace_item(ws_item: dict) -> str:
    """Format a workspace item into markdown (matching old format)"""
    ws_id = ws_item.get("id", "unknown")
    ws_type = ws_item.get("type", "unknown")
    state = ws_item.get("state", "")
    intervals = ws_item.get("intervals", 0)
    shaded = ws_item.get("shaded", [])
    description = ws_item.get("description", "")

    # Format: "  - id (type): intervals sections, state"
    parts = [f"  - {ws_id} ({ws_type})"]

    details = []
    if intervals:
        details.append(f"{intervals} sections")
    if state:
        details.append(state)

    if details:
        parts.append(f": {', '.join(details)}")

    result = "".join(parts)

    # Add description on next line if present
    if description:
        result += f"\n    *{description}*"

    return result


# Test function
if __name__ == "__main__":
    import json
    from pathlib import Path
    import sys

    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    print("Testing Script Formatter...")
    print("=" * 70)

    # Load sample data
    sample_file = Path(__file__).parent.parent / "outputs" / "pipeline_20251124_114427" / "interactions.json"

    if sample_file.exists():
        print(f"\nLoading: {sample_file}")
        with open(sample_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"Found {len(data)} interactions")
        print("\nFormatting to markdown...")

        # Format to markdown
        markdown = format_interactions_to_markdown(data, module_number=1, path_letter='c')

        print("\n[First 800 chars of output:]")
        print(markdown[:800])

        # Save to file
        output_file = sample_file.parent / "script.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"\n\n✓ Saved to: {output_file}")
    else:
        print(f"\n⚠️  Sample file not found: {sample_file}")
        print("\nUsing dummy data for testing...")

        dummy_data = [
            {
                "interaction_id": 1,
                "interaction_name": "Test Interaction",
                "fractions": ["1/2", "1/4"],
                "steps": [
                    {
                        "dialogue": "Let's look at this shape.",
                        "prompt": "What fraction is shaded?",
                        "interaction_tool": "click_choice",
                        "workspace": [
                            {
                                "id": "rect_1",
                                "type": "rectangle_bar",
                                "state": "divided_equal",
                                "intervals": 4,
                                "shaded": [0, 1]
                            }
                        ],
                        "correct_answer": {
                            "value": "1/2",
                            "context": "Two out of four parts are shaded"
                        },
                        "student_attempts": {
                            "success_path": {
                                "dialogue": "That's correct!"
                            }
                        }
                    }
                ]
            }
        ]

        markdown = format_interactions_to_markdown(dummy_data, module_number=1, path_letter='a')
        print(markdown)
