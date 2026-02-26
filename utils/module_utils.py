"""
Utility functions for fetching data from modules.py
Supports nested field access with dot notation
"""

from modules.modules import MODULES


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