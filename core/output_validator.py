"""
Output Validator - Validates AI output structure using schemas from prompts

Focuses on structural validation to catch common AI generation errors:
- Bare arrays instead of objects (or vice versa)
- Missing required fields
- Invalid types
- Incorrect nested structure

Uses the prompt's output_structure to derive the expected schema.
Does NOT validate content (prompts, dialogue, etc.) - only structure.
"""
from typing import Any, Dict, Optional, Union, List
import json


def parse_schema_from_example(output_structure: str) -> Dict[str, Any]:
    """Parse the output_structure JSON example to extract schema information

    Args:
        output_structure: JSON string or example from prompt.output_structure

    Returns:
        Dict with schema info: {
            "is_array": bool,
            "required_fields": List[str],
            "field_types": Dict[str, type],
            "nested_structure": Dict
        }
    """
    try:
        example = json.loads(output_structure.strip())
    except json.JSONDecodeError:
        # If it's not valid JSON, return minimal schema
        return {
            "is_array": False,
            "required_fields": [],
            "field_types": {},
            "nested_structure": {}
        }

    schema = {
        "is_array": isinstance(example, list),
        "required_fields": [],
        "field_types": {},
        "nested_structure": {}
    }

    # If it's an array, extract schema from first element
    sample_obj = example[0] if isinstance(example, list) and len(example) > 0 else example

    if isinstance(sample_obj, dict):
        # Extract required fields and their types
        for key, value in sample_obj.items():
            schema["required_fields"].append(key)

            # Determine expected type
            if isinstance(value, str):
                schema["field_types"][key] = str
            elif isinstance(value, int):
                schema["field_types"][key] = int
            elif isinstance(value, float):
                schema["field_types"][key] = (int, float)  # Accept both
            elif isinstance(value, bool):
                schema["field_types"][key] = bool
            elif isinstance(value, list):
                schema["field_types"][key] = list
            elif isinstance(value, dict):
                schema["field_types"][key] = dict
            else:
                schema["field_types"][key] = type(value)

    return schema


def validate_ai_output_structure(
    result: Any,
    input_item: Dict,
    batch_id_field: Optional[str] = None,
    output_structure: Optional[str] = None
) -> Optional[str]:
    """Validate AI output structure to catch malformed responses

    Uses the prompt's output_structure to validate the actual output.

    Args:
        result: The parsed AI output
        input_item: The input item that was processed
        batch_id_field: Expected ID field (e.g., "problem_id", "template_id")
        output_structure: JSON string from prompt.output_structure (schema example)

    Returns:
        Error message if validation fails, None if valid

    Examples:
        >>> schema = '[{"problem_id": 1, "text": "..."}]'
        >>> validate_ai_output_structure([{"problem_id": 1}], {}, "problem_id", schema)
        None  # Valid

        >>> validate_ai_output_structure({"problem_id": 1}, {}, "problem_id", schema)
        "AI returned object but expected array..."  # Invalid
    """

    # Check 0: Should not be a raw_output wrapper (indicates parse failure)
    if isinstance(result, dict) and 'raw_output' in result and len(result) == 1:
        return "AI output could not be parsed as JSON (raw_output wrapper)"

    # If we have an output_structure, use it for validation
    if output_structure:
        schema = parse_schema_from_example(output_structure)

        # Check 1: Array vs Object structure
        if schema["is_array"] and not isinstance(result, list):
            return (
                f"AI returned {type(result).__name__} but expected array. "
                f"Schema expects: array of objects. "
                f"Got keys: {list(result.keys()) if isinstance(result, dict) else 'N/A'}"
            )

        if not schema["is_array"] and isinstance(result, list):
            return (
                f"AI returned array with {len(result)} elements but expected object. "
                f"Schema expects: single object. "
                f"First element: {result[0] if result else 'empty'}"
            )

        # Check 2: Required fields (for object or first array element)
        sample = result[0] if isinstance(result, list) and len(result) > 0 else result

        if isinstance(sample, dict) and schema["required_fields"]:
            missing_fields = [f for f in schema["required_fields"] if f not in sample]
            if missing_fields:
                return (
                    f"AI output missing required fields: {missing_fields}. "
                    f"Expected fields: {schema['required_fields']}. "
                    f"Got fields: {list(sample.keys())}"
                )

            # Check 3: Field types
            for field, expected_type in schema["field_types"].items():
                if field in sample:
                    actual_value = sample[field]
                    # Handle None values (optional fields)
                    if actual_value is None:
                        continue

                    # Check type
                    if isinstance(expected_type, tuple):
                        # Multiple acceptable types (e.g., int or float)
                        if not isinstance(actual_value, expected_type):
                            return (
                                f"Field '{field}' has wrong type. "
                                f"Expected one of: {expected_type}, "
                                f"Got: {type(actual_value).__name__}"
                            )
                    else:
                        if not isinstance(actual_value, expected_type):
                            return (
                                f"Field '{field}' has wrong type. "
                                f"Expected: {expected_type.__name__}, "
                                f"Got: {type(actual_value).__name__}"
                            )

    else:
        # Fallback to basic validation if no schema provided
        # Check 1: Must be a dict or list, not primitive
        if not isinstance(result, (dict, list)):
            return f"AI returned {type(result).__name__} instead of object or array"

        # Check 2: If array, should not be empty
        if isinstance(result, list) and len(result) == 0:
            return "AI returned empty array"

    # Check: If batch_id_field specified, verify it exists
    if batch_id_field:
        # For arrays, check first element
        check_item = result[0] if isinstance(result, list) and len(result) > 0 else result

        if isinstance(check_item, dict):
            # Check in result (top-level or in metadata)
            result_has_id = (
                batch_id_field in check_item or
                (isinstance(check_item.get('metadata'), dict) and
                 batch_id_field in check_item.get('metadata', {}))
            )

            # Check if input had it (to determine if it should be inherited)
            input_has_id = (
                batch_id_field in input_item or
                (isinstance(input_item.get('metadata'), dict) and
                 batch_id_field in input_item.get('metadata', {}))
            )

            if not result_has_id and input_has_id:
                return (
                    f"AI output missing '{batch_id_field}' field. "
                    f"Input had this field but output doesn't. "
                    f"Output keys: {list(check_item.keys())}"
                )

    return None  # Valid


def get_validation_stats(errors: list) -> Dict[str, int]:
    """Analyze validation errors to identify patterns

    Args:
        errors: List of error messages

    Returns:
        Dict with error type counts
    """
    stats = {
        'bare_array': 0,
        'wrong_structure': 0,
        'missing_fields': 0,
        'wrong_type': 0,
        'parse_failure': 0,
        'other': 0
    }

    for error in errors:
        error_lower = error.lower()
        if 'array' in error_lower and 'expected' in error_lower:
            stats['wrong_structure'] += 1
        elif 'missing required fields' in error_lower or 'missing' in error_lower:
            stats['missing_fields'] += 1
        elif 'wrong type' in error_lower or 'type' in error_lower:
            stats['wrong_type'] += 1
        elif 'raw_output' in error_lower or 'parse' in error_lower:
            stats['parse_failure'] += 1
        else:
            stats['other'] += 1

    return stats
