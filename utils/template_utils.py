"""
Utility functions for fetching data from module 4 problem template JSON files.
Supports the template structure with template_id, goal_decomposition, etc.
Uses __ (double underscore) for nested field access.
"""

import json
import os


def get_template_by_id(module_number, template_id, required=True):
    """
    Fetch a specific template by its template_id.

    Args:
        module_number: The module number (4)
        template_id: The template ID to fetch (e.g., "4001")
        required: If True, raises error if template not found

    Returns:
        The template object, or None if not found and not required
    """
    template_path = os.path.join(
        "inputs", "modules", f"module{module_number}", "problem_templates.json"
    )

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"problem_templates.json not found at {template_path}"
        )

    with open(template_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)

    # Find template by ID
    for template in templates:
        if template.get("template_id") == template_id:
            return template

    if required:
        available_ids = [t.get("template_id") for t in templates]
        raise ValueError(
            f"Template {template_id} not found in {template_path}. "
            f"Available template IDs: {available_ids}"
        )
    return None


def get_template_field(module_number, template_id, field_path, required=True, default=None):
    """
    Fetch a field from a template, supporting nested access with __ (double underscore).

    Args:
        module_number: The module number (4)
        template_id: The template ID (e.g., "4001")
        field_path: Field to fetch, supports __ for nested fields
                   Examples: "problem_type", "goal_decomposition__mastery_verb"
        required: If True, raises error if field is missing
        default: Value to return if field not found and not required

    Returns:
        The requested field value, or default if not found and not required

    Examples:
        get_template_field(4, "4001", "problem_type")
        get_template_field(4, "4001", "goal_decomposition__mastery_verb")
        get_template_field(4, "4001", "parameter_coverage__fractions")
        get_template_field(4, "4001", "tier_constraints__baseline__fractions")
    """
    template = get_template_by_id(module_number, template_id, required=True)

    # Split the path by __ for nested access
    path_parts = field_path.split('__')
    current = template

    try:
        for i, part in enumerate(path_parts):
            # Handle array index
            if isinstance(current, list):
                try:
                    index = int(part)
                    current = current[index]
                except (ValueError, IndexError):
                    raise KeyError(f"Invalid array index '{part}' at '{'__'.join(path_parts[:i+1])}'")
            # Handle dict access
            elif isinstance(current, dict):
                if part not in current:
                    raise KeyError(f"Field '{part}' not found at '{'__'.join(path_parts[:i+1])}'")
                current = current[part]
            else:
                raise KeyError(f"Cannot access '{part}' on non-dict/non-list value")

        return current

    except KeyError as e:
        if required:
            available_fields = _get_available_fields(template)
            raise ValueError(
                f"Required field '{field_path}' not found in Module {module_number}, "
                f"Template {template_id}. Error: {e}. Available top-level fields: {available_fields}"
            )
        return default


def _get_available_fields(data):
    """Helper to list available fields"""
    if isinstance(data, dict):
        return ", ".join(data.keys())
    return str(type(data))


def get_all_fields(module_number, template_id):
    """Get all available top-level fields for a template."""
    template = get_template_by_id(module_number, template_id)
    return list(template.keys())


def get_all_templates(module_number):
    """Get all templates from a module's problem_templates.json."""
    template_path = os.path.join(
        "inputs", "modules", f"module{module_number}", "problem_templates.json"
    )

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"problem_templates.json not found at {template_path}"
        )

    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)


# Counting functions
def get_template_count(module_number, filter_field=None, filter_value=None):
    """
    Count templates, optionally filtered by a field value.

    Args:
        module_number: Module number
        filter_field: Optional field path to filter by (supports __ for nested)
        filter_value: Value to match (if list field, checks if value is IN the list)

    Returns:
        Count of matching templates

    Examples:
        get_template_count(4)  # Total count
        get_template_count(4, "goal_decomposition__mastery_tier", "baseline")  # Tier includes baseline
        get_template_count(4, "goal_decomposition__mastery_verb", "create")  # Verb is create
    """
    templates = get_all_templates(module_number)

    if filter_field is None:
        return len(templates)

    count = 0
    for template in templates:
        try:
            field_value = _get_nested_field(template, filter_field)
            # If field is a list, check if filter_value is in it
            if isinstance(field_value, list):
                if filter_value in field_value:
                    count += 1
            # Otherwise check for equality
            elif field_value == filter_value:
                count += 1
        except (KeyError, TypeError):
            # Skip templates that don't have this field
            continue

    return count


def get_target_count(module_number, tier=None, filter_field=None, filter_value=None):
    """
    Sum target_count values from tier_constraints.

    Args:
        module_number: Module number
        tier: Optional tier name (e.g., "baseline", "support"). If None, sums across ALL tiers.
        filter_field: Optional field path to filter templates (supports __)
        filter_value: Value to match for filtering

    Returns:
        Sum of target_count values

    Examples:
        get_target_count(4)  # Total target count for entire module (all tiers)
        get_target_count(4, "baseline")  # Total for baseline tier only
        get_target_count(4, None, "goal_decomposition__mastery_verb", "create")  # All tiers, create only
        get_target_count(4, "baseline", "goal_decomposition__mastery_verb", "create")  # Baseline + create
    """
    templates = get_all_templates(module_number)
    total = 0

    for template in templates:
        # Apply filter if specified
        if filter_field is not None:
            try:
                field_value = _get_nested_field(template, filter_field)
                # Check if filter matches
                if isinstance(field_value, list):
                    if filter_value not in field_value:
                        continue
                elif field_value != filter_value:
                    continue
            except (KeyError, TypeError):
                continue

        # Get target count
        try:
            tier_constraints = template.get("tier_constraints", {})

            if tier is None:
                # Sum across all tiers
                for tier_name, tier_data in tier_constraints.items():
                    if isinstance(tier_data, dict):
                        target_count = tier_data.get("target_count", 0)
                        total += target_count
            else:
                # Sum for specific tier
                if tier in tier_constraints:
                    target_count = tier_constraints[tier].get("target_count", 0)
                    total += target_count
        except (AttributeError, TypeError):
            continue

    return total


def _get_nested_field(template, field_path):
    """Helper to get nested field value using __ notation."""
    path_parts = field_path.split('__')
    current = template

    for part in path_parts:
        if isinstance(current, dict):
            current = current[part]
        elif isinstance(current, list):
            current = current[int(part)]
        else:
            raise KeyError(f"Cannot access '{part}'")

    return current


# Convenience functions
def get_problem_type(module_number, template_id):
    """Get the problem type for a template."""
    return get_template_field(module_number, template_id, "problem_type")


def get_mastery_verb(module_number, template_id):
    """Get the mastery verb (create, identify, compare, apply)."""
    return get_template_field(module_number, template_id, "goal_decomposition__mastery_verb")


def get_mastery_skill_id(module_number, template_id):
    """Get the mastery skill ID."""
    return get_template_field(module_number, template_id, "goal_decomposition__mastery_skill_id")


def get_prompt_examples(module_number, template_id):
    """Get example prompts for a template."""
    return get_template_field(module_number, template_id, "prompt_examples")


# Test it
if __name__ == "__main__":
    print("Testing template_utils with Module 4 templates...\n")

    print("=" * 70)
    print("TEMPLATE COUNTING")
    print("=" * 70)

    print("\n1. Total template count:")
    total = get_template_count(4)
    print(f"  {total} templates")

    print("\n2. Count templates where tier includes 'baseline':")
    baseline_count = get_template_count(4, "goal_decomposition__mastery_tier", "baseline")
    print(f"  {baseline_count} templates")

    print("\n3. Count templates where mastery_verb is 'create':")
    create_count = get_template_count(4, "goal_decomposition__mastery_verb", "create")
    print(f"  {create_count} templates")

    print("\n" + "=" * 70)
    print("TARGET COUNTING")
    print("=" * 70)

    print("\n4. Total target count for ENTIRE module (all tiers):")
    total_targets = get_target_count(4)
    print(f"  {total_targets} targets")

    print("\n5. Total target count for 'baseline' tier only:")
    baseline_targets = get_target_count(4, "baseline")
    print(f"  {baseline_targets} targets")

    print("\n6. Total target count for 'support' tier only:")
    support_targets = get_target_count(4, "support")
    print(f"  {support_targets} targets")

    print("\n7. Total target count for 'stretch' tier only:")
    stretch_targets = get_target_count(4, "stretch")
    print(f"  {stretch_targets} targets")

    print("\n8. Total targets (all tiers) where mastery_verb is 'create':")
    create_targets = get_target_count(4, None, "goal_decomposition__mastery_verb", "create")
    print(f"  {create_targets} targets")

    print("\n9. Baseline targets where mastery_verb is 'create':")
    baseline_create = get_target_count(4, "baseline", "goal_decomposition__mastery_verb", "create")
    print(f"  {baseline_create} targets")

    print("\n" + "=" * 70)
    print("FIELD ACCESS")
    print("=" * 70)

    print("\n10. Get mastery verb for template 4001:")
    verb = get_mastery_verb(4, "4001")
    print(f"  {verb}")

    print("\n11. Get nested field - baseline fractions for template 4001:")
    fractions = get_template_field(4, "4001", "tier_constraints__baseline__fractions")
    print(f"  {fractions}")

    print("\n" + "=" * 70)
    print("✅ All tests passed!")
    print("=" * 70)

    print("\n📖 Usage Examples:")
    print('  get_template_count(4)                                          # Total templates')
    print('  get_template_count(4, "goal_decomposition__mastery_tier", "baseline")  # Filter by tier')
    print('  get_target_count(4)                                            # ALL targets in module')
    print('  get_target_count(4, "baseline")                                # Baseline tier only')
    print('  get_target_count(4, None, "goal_decomposition__mastery_verb", "create")  # All tiers, create only')
    print('  get_template_field(4, "4001", "tier_constraints__baseline__fractions")  # Nested access')
