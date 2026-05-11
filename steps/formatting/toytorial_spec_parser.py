"""
toytorial_spec_parser - Formatting Step

Parses a visuals.md file into a flat list of spec items for the toytorial_generator
AI step. For each toy shape found in the file it produces:
  - One "intro" item (generates the transition section that first shows the toy)
  - One "action" item per Allowed Student Action (generates a teaching/practice section)

Input (input_data): raw visuals.md content as a string
Output: [{id, index, type, toy_name, ...}, ...]
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


def _parse_shapes(content: str) -> list:
    """Split visuals.md on ## Shape: boundaries and parse each block."""
    shapes = []
    blocks = re.split(r"(?m)^\s*##\s+Shape:\s*", content)

    for block in blocks[1:]:  # blocks[0] is the preamble
        lines = block.splitlines()
        if not lines:
            continue

        shape_name = lines[0].strip()
        body = "\n".join(lines[1:])

        # First non-empty, non-heading, non-separator line is the description
        description = ""
        for line in lines[1:]:
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and stripped != "---":
                description = stripped
                break

        shapes.append(
            {
                "name": shape_name,
                "description": description,
                "spec": block.strip(),
                "actions": _parse_actions(body),
            }
        )

    return shapes


def _parse_actions(block_text: str) -> list:
    """Extract Allowed Student Actions from one shape block."""
    m = re.search(
        r"^\s*###\s+Allowed Student Actions\s*\n(.*?)(?:\n\s*###|\n\s*##|\Z)",
        block_text,
        re.DOTALL | re.MULTILINE,
    )
    if not m:
        return []

    actions = []
    for match in re.finditer(r"-\s+\*\*([^*]+)\*\*:\s*(.+)", m.group(1)):
        name = match.group(1).strip()
        full = match.group(2).strip()

        # Split on ". For example," to separate description from examples+undo
        ex_match = re.search(r"\.\s+For example,\s*", full, re.IGNORECASE)
        if ex_match:
            description = full[: ex_match.start()].strip()
            remainder = full[ex_match.end() :]
        else:
            description = full
            remainder = ""

        # Split remainder on ". Undo:" to separate examples from undo mechanic
        undo_match = re.search(r"\.\s+Undo:\s*", remainder, re.IGNORECASE)
        if undo_match:
            examples = remainder[: undo_match.start()].strip()
            undo = remainder[undo_match.end() :].strip().rstrip(".")
        else:
            examples = remainder.strip().rstrip(".")
            undo = ""

        # If no "For example," block, check if description itself has "Undo:"
        if not ex_match:
            undo_match2 = re.search(r"\.\s+Undo:\s*", description, re.IGNORECASE)
            if undo_match2:
                undo = description[undo_match2.end() :].strip().rstrip(".")
                description = description[: undo_match2.start()].strip()
            else:
                description = description.rstrip(".")

        actions.append(
            {"name": name, "description": description, "examples": examples, "undo": undo}
        )

    return actions


def _to_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def parse_spec(input_data, **kwargs) -> list:
    """
    Entry point for the pipeline formatting step.

    Args:
        input_data: Raw visuals.md content (string)

    Returns:
        Flat list of spec items ordered: intro → actions for each shape.
    """
    if not isinstance(input_data, str):
        raise ValueError(
            "toytorial_spec_parser expects raw markdown (string) as input_data; "
            f"got {type(input_data).__name__}"
        )

    shapes = _parse_shapes(input_data)
    if not shapes:
        raise ValueError(
            "No toy shapes found in visuals.md — check that ## Shape: headings are present"
        )

    items = []
    for shape in shapes:
        toy_slug = _to_slug(shape["name"])

        items.append(
            {
                "id": f"t0_{toy_slug}_intro",
                "index": len(items),
                "type": "intro",
                "toy_name": shape["name"],
                "toy_description": shape["description"],
                "toy_spec": shape["spec"],
            }
        )

        for i, action in enumerate(shape["actions"], start=1):
            action_slug = _to_slug(action["name"])
            items.append(
                {
                    "id": f"t{i}_{toy_slug}_{action_slug}",
                    "index": len(items),
                    "type": "action",
                    "toy_name": shape["name"],
                    "toy_description": shape["description"],
                    "action_name": action["name"],
                    "action_description": action["description"],
                    "action_examples": action["examples"],
                    "action_undo": action["undo"],
                    "toy_spec": shape["spec"],
                }
            )

        bridge_index = len(shape["actions"]) + 1
        items.append(
            {
                "id": f"t{bridge_index}_{toy_slug}_bridge",
                "index": len(items),
                "type": "bridge",
                "toy_name": shape["name"],
                "toy_description": shape["description"],
                "toy_spec": shape["spec"],
            }
        )

    return items
