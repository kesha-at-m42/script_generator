"""
Utility functions for fetching data from problem_templates.json files
Supports nested field access with dot notation
"""

import json
import os


def get_problem_template_field(module_number, goal_id, field_path, required=True, default=None):
    """
    Fetch a field from a problem template for a specific goal, supporting nested access with dot notation.

    Args:
        module_number: The module number (1, 2, etc.)
        goal_id: The goal ID to fetch template for
        field_path: Field to fetch, supports dot notation for nested fields
                   Examples: "cognitive_type", "tools_available", "variables.0.fractions"
        required: If True, raises error if field is missing. If False, returns default.
        default: Value to return if field not found and not required

    Returns:
        The requested field value, or default if not found and not required.

    Examples:
        get_problem_template_field(1, 1, "cognitive_type")  # Top-level field
        get_problem_template_field(1, 1, "tools_available")  # Array field
        get_problem_template_field(1, 1, "variables.0.fractions")  # Nested access
        get_problem_template_field(1, 1, "remediations_per_step.0.0.scaffolding_level")  # Deep nesting

    Raises:
        FileNotFoundError: If problem_templates.json not found for module
        ValueError: If goal not found or required field is missing
    """
    # Construct path to problem_templates.json
    template_path = os.path.join(
        "inputs", "modules", f"module{module_number}", "problem_templates.json"
    )

    # Check if file exists
    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"problem_templates.json not found at {template_path}"
        )

    # Load the JSON file
    with open(template_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find the goal by ID
    goal = None
    if "goals" in data:
        for g in data["goals"]:
            if g.get("id") == goal_id:
                goal = g
                break

    if goal is None:
        available_ids = [g.get("id") for g in data.get("goals", [])]
        raise ValueError(
            f"Goal {goal_id} not found in {template_path}. "
            f"Available goal IDs: {available_ids}"
        )

    # Split the path by dots for nested access
    path_parts = field_path.split('.')
    current = goal

    try:
        for i, part in enumerate(path_parts):
            # Handle wildcard for arrays (e.g., "variables.*.fractions")
            if part == '*':
                if not isinstance(current, list):
                    raise ValueError(f"Wildcard used on non-list field at '{'.'.join(path_parts[:i])}'")
                # Get remaining path
                remaining_path = '.'.join(path_parts[i+1:])
                if remaining_path:
                    # Recursively get field from each item
                    return [_get_nested_value(item, remaining_path) for item in current]
                else:
                    return current

            # Handle array index (e.g., "variables.0")
            if isinstance(current, list):
                try:
                    index = int(part)
                    current = current[index]
                except (ValueError, IndexError):
                    raise KeyError(f"Invalid array index '{part}' at '{'.'.join(path_parts[:i+1])}'")
            # Handle dict access
            elif isinstance(current, dict):
                if part not in current:
                    raise KeyError(f"Field '{part}' not found at '{'.'.join(path_parts[:i+1])}'")
                current = current[part]
            else:
                raise KeyError(f"Cannot access '{part}' on non-dict/non-list value")

        return current

    except KeyError as e:
        if required:
            available_fields = _get_available_fields(goal)
            raise ValueError(
                f"Required field '{field_path}' not found in Module {module_number}, Goal {goal_id}. "
                f"Error: {e}. Available top-level fields: {available_fields}"
            )
        return default


def _get_nested_value(obj, path):
    """Helper to get nested value from object using dot notation"""
    parts = path.split('.')
    current = obj
    for part in parts:
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, list):
            current = current[int(part)]
        else:
            return None
        if current is None:
            return None
    return current


def _get_available_fields(data):
    """Helper to list available fields"""
    if isinstance(data, dict):
        return ", ".join(data.keys())
    return str(type(data))


# Convenience functions for common access patterns
def get_cognitive_type(module_number, goal_id):
    """Get the cognitive type for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "cognitive_type", required=True)


def get_tools(module_number, goal_id):
    """Get the tools list for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "tools_available", required=True)


def get_template_variables(module_number, goal_id):
    """Get the variables for a specific goal template."""
    return get_problem_template_field(module_number, goal_id, "variables", required=True)


def get_difficulty_level(module_number, goal_id):
    """Get the difficulty level for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "difficulty_level", required=True)


def get_example_questions(module_number, goal_id):
    """Get example questions for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "example_questions", required=True)


def get_remediations_per_step(module_number, goal_id):
    """Get remediation steps for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "remediations_per_step", required=False, default=[])


def get_no_of_steps(module_number, goal_id):
    """Get number of steps for a specific goal."""
    return get_problem_template_field(module_number, goal_id, "no_of_steps", required=False, default="1")


def get_all_goal_templates(module_number):
    """Get all goal templates from a module's problem_templates.json."""
    template_path = os.path.join(
        "inputs", "modules", f"module{module_number}", "problem_templates.json"
    )

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"problem_templates.json not found at {template_path}"
        )

    with open(template_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data.get("goals", [])


def get_goal_template_by_id(module_number, goal_id):
    """Get a specific goal template by ID."""
    goals = get_all_goal_templates(module_number)
    for goal in goals:
        if goal.get("id") == goal_id:
            return goal
    raise ValueError(f"Goal {goal_id} not found in Module {module_number} problem templates")


def get_fields_by_reference(module_number, goal_id, field_reference_list, required=True, default=None):
    """
    Fetch multiple fields from a problem template based on a reference list.
    Automatically handles nested fields with dot notation.

    Args:
        module_number: The module number (1, 2, etc.)
        goal_id: The goal ID to fetch template for
        field_reference_list: List of field names/paths to fetch (supports dot notation for nested)
        required: If True, raises error if any field is missing. If False, returns default for missing fields.
        default: Value to return for missing fields when not required

    Returns:
        Dictionary mapping field names to their values

    Examples:
        # Simple fields
        INTERACTION_DESIGNER_TEMPLATE_REF = ["tools_available", "cognitive_type", "difficulty_level"]
        fields = get_fields_by_reference(1, 1, INTERACTION_DESIGNER_TEMPLATE_REF)
        # Returns: {"tools_available": ["cut"], "cognitive_type": ["create"], "difficulty_level": "0-2"}

        # With nested fields (using dot notation)
        CUSTOM_REF = ["tools_available", "variables.0.fractions", "remediations_per_step.0.0.scaffolding_level"]
        fields = get_fields_by_reference(1, 1, CUSTOM_REF)
    """
    result = {}

    for field_path in field_reference_list:
        result[field_path] = get_problem_template_field(
            module_number,
            goal_id,
            field_path,
            required=required,
            default=default
        )

    return result


# Test it
if __name__ == "__main__":
    print("Testing problem_template_utils with nested field access...\n")

    print("=" * 70)
    print("BASIC FIELD ACCESS")
    print("=" * 70)

    # Test basic fields
    print("\n1. Cognitive type for Goal 1:")
    cognitive_type = get_cognitive_type(1, 1)
    print(f"  {cognitive_type}")

    print("\n2. Tools for Goal 2:")
    tools = get_tools(1, 2)
    print(f"  {tools}")

    print("\n3. Difficulty level for Goal 1:")
    difficulty = get_difficulty_level(1, 1)
    print(f"  {difficulty}")

    print("\n" + "=" * 70)
    print("NESTED FIELD ACCESS")
    print("=" * 70)

    # Test nested access
    print("\n4. Variables fractions (nested):")
    fractions = get_problem_template_field(1, 1, "variables.0.fractions")
    print(f"  {fractions}")

    print("\n5. First remediation scaffolding level (deep nested):")
    scaffolding = get_problem_template_field(1, 1, "remediations_per_step.0.0.scaffolding_level")
    print(f"  {scaffolding}")

    print("\n" + "=" * 70)
    print("CONVENIENCE FUNCTIONS")
    print("=" * 70)

    print("\n6. Example questions for Goal 3:")
    questions = get_example_questions(1, 3)
    for i, q in enumerate(questions, 1):
        print(f"  {i}. {q}")

    print("\n7. Number of steps for Goal 6:")
    steps = get_no_of_steps(1, 6)
    print(f"  {steps}")

    print("\n" + "=" * 70)
    print("GET ALL TEMPLATES")
    print("=" * 70)

    print("\n8. All goal templates from Module 1:")
    all_templates = get_all_goal_templates(1)
    for template in all_templates:
        print(f"  Goal {template['id']}: {template['text']}")

    print("\n9. Get specific goal template by ID:")
    goal_template = get_goal_template_by_id(1, 5)
    print(f"  Goal {goal_template['id']}: {goal_template['text']}")
    print(f"  Cognitive type: {goal_template.get('cognitive_type')}")
    print(f"  Tools: {goal_template.get('tools')}")

    print("\n" + "=" * 70)
    print("ERROR HANDLING")
    print("=" * 70)

    # Test optional field
    print("\n10. Optional field (doesn't exist, returns default):")
    optional = get_problem_template_field(1, 1, "nonexistent_field", required=False, default="N/A")
    print(f"  Result: {optional}")

    print("\n" + "=" * 70)
    print("✅ All tests passed!")
    print("=" * 70)

    print("\n📖 Usage Examples:")
    print('  get_problem_template_field(1, 1, "cognitive_type")  # Top-level')
    print('  get_problem_template_field(1, 1, "tools_available")           # Array field')
    print('  get_problem_template_field(1, 1, "variables.0.fractions")  # Nested')
    print('  get_cognitive_type(1, 1)                             # Convenience function')
    print('  get_all_goal_templates(1)                            # Get all templates')
