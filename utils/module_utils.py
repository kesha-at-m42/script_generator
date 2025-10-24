"""
Utility functions for fetching data from modules.py
Supports nested field access with dot notation
"""

from inputs.modules.modules import MODULES


def get_module_field(module_number, field_path, required=True, default=None):
    """
    Fetch a field from a module, supporting nested access with dot notation.
    
    Args:
        module_number: The module number (1, 2, etc.)
        field_path: Field to fetch, supports dot notation for nested fields
                   Examples: "vocabulary", "standards.addressing", "goals.0.text"
        required: If True, raises error if field is missing. If False, returns default.
        default: Value to return if field not found and not required
    
    Returns:
        The requested field value, or default if not found and not required.
    
    Examples:
        get_module_field(1, "vocabulary")  # Top-level field
        get_module_field(1, "standards.addressing")  # Nested dict
        get_module_field(1, "goals.0.text")  # Array index
        get_module_field(1, "goals.*.id")  # All IDs from goals array
    
    Raises:
        ValueError: If module not found or required field is missing.
    """
    # Check module exists
    if module_number not in MODULES:
        available = ", ".join(str(k) for k in MODULES.keys())
        raise ValueError(f"Module {module_number} not found. Available: {available}")
    
    module_data = MODULES[module_number]
    
    # Split the path by dots for nested access
    path_parts = field_path.split('.')
    current = module_data
    
    try:
        for i, part in enumerate(path_parts):
            # Handle wildcard for arrays (e.g., "goals.*.id")
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
            
            # Handle array index (e.g., "goals.0")
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
            available_fields = _get_available_fields(module_data)
            raise ValueError(
                f"Required field '{field_path}' not found in Module {module_number}. "
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
def get_variables(module_number):
    """Get the variables section from a module."""
    return get_module_field(module_number, "variables", required=True)


def get_vocabulary(module_number):
    """Get the vocabulary list from a module."""
    return get_module_field(module_number, "vocabulary", required=True)


def get_goals(module_number):
    """Get the learning goals (detailed) from a module."""
    return get_module_field(module_number, "goals", required=False, default=[])


def get_learning_goals(module_number):
    """Get the simple learning goals list from a module."""
    return get_module_field(module_number, "learning_goals", required=True)


def get_available_visuals(module_number):
    """Get the available visuals from a module."""
    return get_module_field(module_number, "available_visuals", required=True)


def get_standards(module_number):
    """Get all standards from a module."""
    return get_module_field(module_number, "standards", required=True)


def get_misconceptions(module_number):
    """Get misconceptions from a module."""
    return get_module_field(module_number, "misconceptions", required=False, default=[])


def get_goal_by_id(module_number, goal_id):
    """Get a specific goal by ID from a module."""
    goals = get_goals(module_number)
    for goal in goals:
        if goal.get("id") == goal_id:
            return goal
    raise ValueError(f"Goal {goal_id} not found in Module {module_number}")


def get_all_goal_ids(module_number):
    """Get all goal IDs from a module using wildcard."""
    return get_module_field(module_number, "goals.*.id", required=False, default=[])


def get_all_goal_texts(module_number):
    """Get all goal text descriptions using wildcard."""
    return get_module_field(module_number, "goals.*.text", required=False, default=[])


# Test it
if __name__ == "__main__":
    print("Testing module_utils with nested field access...\n")
    
    print("=" * 70)
    print("BASIC FIELD ACCESS")
    print("=" * 70)
    
    # Test get_variables
    print("\n1. Variables from Module 1:")
    vars_m1 = get_variables(1)
    for var_name, values in vars_m1.items():
        print(f"  {var_name}: {values}")
    
    # Test get_vocabulary
    print("\n2. Vocabulary from Module 1:")
    vocab_m1 = get_vocabulary(1)
    print(f"  {vocab_m1}")
    
    print("\n" + "=" * 70)
    print("NESTED FIELD ACCESS")
    print("=" * 70)
    
    # Test nested dict access
    print("\n3. Standards - Addressing (nested dict):")
    standards_addressing = get_module_field(1, "standards.addressing")
    print(f"  {standards_addressing}")
    
    # Test nested dict access - another level
    print("\n4. Visual shapes (nested dict):")
    visual_shapes = get_module_field(1, "available_visuals.shapes")
    print(f"  {visual_shapes}")
    
    print("\n" + "=" * 70)
    print("ARRAY ACCESS (Module 2 has 'goals' array)")
    print("=" * 70)
    
    # Test array index access
    print("\n5. First goal text (array index):")
    first_goal = get_module_field(2, "goals.0.text")
    print(f"  {first_goal}")
    
    # Test wildcard for all IDs
    print("\n6. All goal IDs (wildcard):")
    all_ids = get_module_field(2, "goals.*.id")
    print(f"  {all_ids}")
    
    # Test wildcard for all texts
    print("\n7. All goal texts (wildcard):")
    all_texts = get_module_field(2, "goals.*.text")
    for i, text in enumerate(all_texts, 1):
        print(f"  {i}. {text}")
    
    print("\n" + "=" * 70)
    print("HELPER FUNCTIONS")
    print("=" * 70)
    
    # Test convenience functions
    print("\n8. Using get_all_goal_ids():")
    goal_ids = get_all_goal_ids(2)
    print(f"  {goal_ids}")
    
    print("\n9. Using get_misconceptions():")
    misconceptions = get_misconceptions(1)
    for i, m in enumerate(misconceptions, 1):
        print(f"  {i}. {m['misconception']}")
    
    print("\n" + "=" * 70)
    print("ERROR HANDLING")
    print("=" * 70)
    
    # Test optional field
    print("\n10. Optional field (doesn't exist, returns default):")
    optional = get_module_field(1, "nonexistent_field", required=False, default="N/A")
    print(f"  Result: {optional}")
    
    print("\n" + "=" * 70)
    print("✅ All tests passed!")
    print("=" * 70)
    
    print("\n📖 Usage Examples:")
    print('  get_module_field(1, "vocabulary")              # Top-level')
    print('  get_module_field(1, "standards.addressing")    # Nested dict')
    print('  get_module_field(2, "goals.0.text")            # Array index')
    print('  get_module_field(2, "goals.*.id")              # Wildcard for all IDs')
    print('  get_module_field(1, "optional", required=False, default=[])  # Optional with default')
