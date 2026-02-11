"""
Output Validator - Validates AI output structure using schemas from prompts

Focuses on structural validation to catch common AI generation errors:
- Bare arrays instead of objects (or vice versa)
- Missing required fields
- Invalid types
- Incorrect nested structure

Uses the prompt's output_structure to derive the expected schema.
Does NOT validate content (prompts, dialogue, etc.) - only structure.

Includes Godot-specific schema validation for known problematic patterns.
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

    # Check 0a: Godot-specific schema validation (runs for Godot Sequences)
    if isinstance(result, dict):
        godot_error = validate_godot_schema(result)
        if godot_error:
            return f"Godot schema error: {godot_error}"

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


def are_fractions_equivalent(frac1: str, frac2: str) -> bool:
    """Check if two fraction strings are mathematically equivalent

    Args:
        frac1: First fraction (e.g., "2/3", "4/6")
        frac2: Second fraction (e.g., "4/6", "2/3")

    Returns:
        True if fractions are equivalent
    """
    try:
        def parse_frac(f):
            if '/' in str(f):
                parts = str(f).split('/')
                return int(parts[0]) / int(parts[1])
            return float(f)

        val1 = parse_frac(frac1)
        val2 = parse_frac(frac2)
        return abs(val1 - val2) < 0.0001
    except:
        return False


def validate_godot_schema(result: Dict[str, Any]) -> Optional[str]:
    """Validate Godot-specific schema patterns

    Catches common Godot schema errors like:
    - labels/alt_labels as object instead of array/boolean
    - points as object instead of array
    - Invalid nested tangible structures
    - Multiple equivalent correct answers in MCQ/Selection

    Args:
        result: Parsed result (should be a Godot Sequence)

    Returns:
        Error message if validation fails, None if valid
    """
    # Only validate if this looks like a Godot Sequence
    if not isinstance(result, dict) or result.get("@type") != "Sequence":
        return None

    # Validate steps array
    steps = result.get("steps", [])
    if not isinstance(steps, list):
        return None

    # Check each step's workspace
    for step_idx, step in enumerate(steps):
        if not isinstance(step, dict):
            continue

        workspace = step.get("workspace")
        if not isinstance(workspace, dict):
            continue

        # Validate workspace_choices - should be array of strings
        if "workspace_choices" in workspace:
            workspace_choices = workspace["workspace_choices"]
            if not isinstance(workspace_choices, list):
                return (
                    f"steps[{step_idx}].workspace.workspace_choices has invalid type. "
                    f"Expected: array of strings, "
                    f"Got: {type(workspace_choices).__name__}"
                )
            # Check that all elements are strings
            if isinstance(workspace_choices, list):
                for choice_idx, choice in enumerate(workspace_choices):
                    if not isinstance(choice, str):
                        return (
                            f"steps[{step_idx}].workspace.workspace_choices[{choice_idx}] has invalid type. "
                            f"Expected: string, "
                            f"Got: {type(choice).__name__} ({choice})"
                        )

        tangibles = workspace.get("tangibles")
        if not isinstance(tangibles, list):
            continue

        # Validate each tangible
        for tangible_idx, tangible in enumerate(tangibles):
            if not isinstance(tangible, dict):
                continue

            tangible_type = tangible.get("@type")
            location = f"steps[{step_idx}].workspace.tangibles[{tangible_idx}]"

            # NumLine validation
            if tangible_type == "NumLine":
                # Check labels - should be boolean or array, NOT object
                if "labels" in tangible:
                    labels = tangible["labels"]
                    if isinstance(labels, dict):
                        return (
                            f"{location}.labels has invalid type. "
                            f"Expected: boolean or array (e.g., [\"0\", \"1/3\"]), "
                            f"Got: object with keys {list(labels.keys())}. "
                            f"Note: labels cannot be an object with key-value pairs like {{\"0\": \"0\", \"1/3\": \"1/3 is here\"}}."
                        )
                    if not isinstance(labels, (bool, list)):
                        return (
                            f"{location}.labels has invalid type. "
                            f"Expected: boolean or array, "
                            f"Got: {type(labels).__name__}"
                        )

                # Check alt_labels - should be boolean or array, NOT object
                if "alt_labels" in tangible:
                    alt_labels = tangible["alt_labels"]
                    if isinstance(alt_labels, dict):
                        return (
                            f"{location}.alt_labels has invalid type. "
                            f"Expected: boolean or array, "
                            f"Got: object with keys {list(alt_labels.keys())}"
                        )
                    if not isinstance(alt_labels, (bool, list)):
                        return (
                            f"{location}.alt_labels has invalid type. "
                            f"Expected: boolean or array, "
                            f"Got: {type(alt_labels).__name__}"
                        )

                # Check points - should be array, NOT object
                if "points" in tangible:
                    points = tangible["points"]
                    if isinstance(points, dict):
                        return (
                            f"{location}.points has invalid type. "
                            f"Expected: array (e.g., [\"1/4\", \"2/3\"]), "
                            f"Got: object"
                        )
                    if not isinstance(points, list):
                        return (
                            f"{location}.points has invalid type. "
                            f"Expected: array, "
                            f"Got: {type(points).__name__}"
                        )

                # Check range - should be array of 2 numbers
                if "range" in tangible:
                    range_val = tangible["range"]
                    if not isinstance(range_val, list):
                        return (
                            f"{location}.range has invalid type. "
                            f"Expected: array [start, end], "
                            f"Got: {type(range_val).__name__}"
                        )
                    if isinstance(range_val, list) and len(range_val) != 2:
                        return (
                            f"{location}.range should have exactly 2 elements [start, end], "
                            f"got {len(range_val)} elements"
                        )

                # Check ticks_is_read_only - should be boolean OR array of fraction strings (NOT array of booleans)
                if "ticks_is_read_only" in tangible:
                    ticks_readonly = tangible["ticks_is_read_only"]
                    if isinstance(ticks_readonly, list) and len(ticks_readonly) > 0:
                        # Check if array contains booleans (invalid)
                        if any(isinstance(x, bool) for x in ticks_readonly):
                            return (
                                f"{location}.ticks_is_read_only has invalid format. "
                                f"Should be: boolean (true/false) OR array of fraction strings ([\"0\", \"1/3\"]), "
                                f"Got: array with booleans {ticks_readonly}. "
                                f"Note: Use single boolean to mark all ticks readonly, or array of strings for specific ticks."
                            )

                # Check intervals_is_read_only - should be boolean OR array of integers (NOT array of booleans)
                if "intervals_is_read_only" in tangible:
                    intervals_readonly = tangible["intervals_is_read_only"]
                    if isinstance(intervals_readonly, list) and len(intervals_readonly) > 0:
                        if any(isinstance(x, bool) for x in intervals_readonly):
                            return (
                                f"{location}.intervals_is_read_only has invalid format. "
                                f"Should be: boolean OR array of integers ([0, 1, 2]), "
                                f"Got: array with booleans."
                            )

        # Check for multiple equivalent correct answers
        prompt = step.get("prompt")
        if isinstance(prompt, dict):
            validator = prompt.get("validator")
            if isinstance(validator, dict):
                validator_type = validator.get("@type")

                # Check for empty answer (applies to all validator types)
                answer = validator.get("answer")
                if answer is None or answer == [] or answer == "":
                    return (
                        f"steps[{step_idx}].prompt.validator: answer field is empty or missing. "
                        f"All validators require a valid answer field."
                    )

                # Check MultipleChoiceValidator with WorkspaceChoices
                if validator_type == "MultipleChoiceValidator":
                    answer = validator.get("answer", [])
                    choices = prompt.get("choices", {})

                    if isinstance(choices, dict) and isinstance(answer, list):
                        choice_options = choices.get("options", [])
                        allow_multiple = choices.get("allow_multiple", False)

                        # Flag if answer has 1 item but there are equivalent fractions
                        if len(answer) == 1 and not allow_multiple and len(choice_options) > 1:
                            answer_idx = answer[0]
                            if 0 <= answer_idx < len(choice_options):
                                answer_text = choice_options[answer_idx]

                                # Check if any other option is equivalent
                                equivalent_indices = []
                                for idx, option in enumerate(choice_options):
                                    if idx != answer_idx and are_fractions_equivalent(answer_text, option):
                                        equivalent_indices.append(idx)

                                if equivalent_indices:
                                    return (
                                        f"steps[{step_idx}].prompt.validator: Multiple equivalent correct answers detected. "
                                        f"Answer is [{answer_idx}] (\"{answer_text}\") but option(s) {equivalent_indices} "
                                        f"({[choice_options[i] for i in equivalent_indices]}) are also equivalent. "
                                        f"Either: (1) set allow_multiple: true and answer: {[answer_idx] + equivalent_indices}, "
                                        f"or (2) remove equivalent options from choices."
                                    )

                # Check SelectionValidator with equivalent tangibles
                if validator_type == "SelectionValidator":
                    answer = validator.get("answer")

                    # Normalize answer to list
                    if isinstance(answer, int):
                        answer = [answer]

                    if isinstance(answer, list) and len(answer) == 1 and isinstance(workspace, dict):
                        tangibles = workspace.get("tangibles", [])
                        answer_idx = answer[0]

                        if 0 <= answer_idx < len(tangibles):
                            answer_tangible = tangibles[answer_idx]

                            # Check for equivalent fraction strips/bars
                            if answer_tangible.get("@type") in ["NumLine", "FracShape"]:
                                # Extract the shaded amount from answer tangible
                                answer_amount = _extract_shaded_amount(answer_tangible)

                                if answer_amount:
                                    # Check other tangibles for equivalence
                                    equivalent_indices = []
                                    for idx, tangible in enumerate(tangibles):
                                        if idx != answer_idx and tangible.get("@type") == answer_tangible.get("@type"):
                                            # Skip reference tangibles
                                            if tangible.get("is_read_only"):
                                                continue

                                            tangible_amount = _extract_shaded_amount(tangible)
                                            if tangible_amount and are_fractions_equivalent(answer_amount, tangible_amount):
                                                equivalent_indices.append(idx)

                                    if equivalent_indices:
                                        return (
                                            f"steps[{step_idx}].prompt.validator: Multiple equivalent selectable tangibles detected. "
                                            f"Answer is [{answer_idx}] (showing {answer_amount}) but tangible(s) {equivalent_indices} "
                                            f"are also equivalent. This creates ambiguity - student could select any equivalent tangible. "
                                            f"Consider: (1) marking non-answer equivalents as is_read_only: true (reference), "
                                            f"or (2) using MultipleChoiceValidator if multiple selections are valid."
                                        )

    return None


def _extract_shaded_amount(tangible: Dict[str, Any]) -> Optional[str]:
    """Extract the shaded fraction amount from a tangible

    Args:
        tangible: NumLine or FracShape tangible

    Returns:
        Fraction string (e.g., "2/4") or None
    """
    tangible_type = tangible.get("@type")

    if tangible_type == "NumLine":
        # For bars with intervals, count shaded intervals
        intervals_shaded = tangible.get("intervals_is_shaded")
        intervals = tangible.get("intervals")

        if isinstance(intervals_shaded, list) and isinstance(intervals, str):
            # intervals is a string like "1/4"
            shaded_count = len(intervals_shaded)
            return f"{shaded_count * int(intervals.split('/')[0])}/{intervals.split('/')[1]}"

    elif tangible_type == "FracShape":
        # Similar logic for FracShape
        intervals_shaded = tangible.get("intervals_is_shaded")
        intervals = tangible.get("intervals")

        if isinstance(intervals_shaded, list) and isinstance(intervals, str):
            shaded_count = len(intervals_shaded)
            return f"{shaded_count * int(intervals.split('/')[0])}/{intervals.split('/')[1]}"

    return None


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


# ============================================================================
# COMMAND-LINE INTERFACE
# ============================================================================

if __name__ == "__main__":
    import sys
    import argparse
    from pathlib import Path
    import importlib.util

    def load_prompt_output_structure(prompt_name: str, project_root: Path) -> Optional[str]:
        """Load output_structure from a prompt file

        Args:
            prompt_name: Name of the prompt (e.g., "godot_formatter")
            project_root: Project root directory

        Returns:
            output_structure string or None if not found
        """
        prompt_file = project_root / "steps" / "prompts" / f"{prompt_name}.py"

        if not prompt_file.exists():
            return None

        try:
            # Load the module
            spec = importlib.util.spec_from_file_location(prompt_name, prompt_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Find the Prompt object (usually uppercased prompt name)
            prompt_obj = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if hasattr(attr, 'output_structure'):
                    prompt_obj = attr
                    break

            if prompt_obj and hasattr(prompt_obj, 'output_structure'):
                return prompt_obj.output_structure

        except Exception as e:
            print(f"Warning: Could not load prompt '{prompt_name}': {e}")

        return None

    def detect_prompt_from_path(file_path: Path) -> Optional[str]:
        """Detect prompt name from output file path

        Args:
            file_path: Path to the output file

        Returns:
            Prompt name or None

        Examples:
            output/module_4/godot_formatter/collated.json → "godot_formatter"
            output/m4/problem_generator/items/1.json → "problem_generator"
        """
        parts = file_path.parts

        # Look for common prompt names in path
        known_prompts = [
            'godot_formatter',
            'problem_generator',
            'bbcode_formatter',
            'sequence_generator'
        ]

        for part in parts:
            if part in known_prompts:
                return part

        return None

    parser = argparse.ArgumentParser(
        description="Validate AI output for schema errors",
        epilog="""
Examples:
  # Auto-detect prompt from path
  python core/output_validator.py output/module_4/godot_formatter/collated.json

  # Specify prompt manually
  python core/output_validator.py output.json --prompt godot_formatter

  # Save validated output
  python core/output_validator.py input.json -o validated.json
        """
    )
    parser.add_argument(
        "input_file",
        help="Path to JSON file to validate"
    )
    parser.add_argument(
        "-p", "--prompt",
        help="Prompt name to load output_structure from (auto-detected if not specified)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Save validated output to file (adds _validation_status fields)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed error messages"
    )

    args = parser.parse_args()

    # Determine project root
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent

    # Load input file
    input_path = Path(args.input_file).resolve()
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_path}: {e}")
        sys.exit(1)

    # Detect or use prompt name
    prompt_name = args.prompt
    if not prompt_name:
        prompt_name = detect_prompt_from_path(input_path)
        if prompt_name and args.verbose:
            print(f"Auto-detected prompt: {prompt_name}")

    # Load output_structure if prompt name available
    output_structure = None
    if prompt_name:
        output_structure = load_prompt_output_structure(prompt_name, project_root)
        if output_structure and args.verbose:
            print(f"Loaded output_structure from prompt: {prompt_name}")
        elif not output_structure and args.verbose:
            print(f"Warning: Could not load output_structure from prompt: {prompt_name}")

    # Determine format
    if isinstance(data, dict) and data.get('@type') == 'SequencePool':
        sequences = data.get('sequences', [])
        is_pool = True
    elif isinstance(data, list):
        sequences = data
        is_pool = False
    elif isinstance(data, dict) and data.get('@type') == 'Sequence':
        sequences = [data]
        is_pool = False
    else:
        sequences = [data]  # Treat as single item
        is_pool = False

    # Validate each sequence
    print(f"\nValidating {len(sequences)} item(s)...")
    print("=" * 70)

    validation_errors = []
    for idx, sequence in enumerate(sequences):
        seq_id = None
        if isinstance(sequence, dict):
            seq_id = sequence.get('metadata', {}).get('problem_id') or sequence.get('problem_id', idx)
        else:
            seq_id = idx

        # Run full validation (both basic + Godot)
        error = validate_ai_output_structure(
            sequence,
            {},  # No input item for standalone validation
            batch_id_field=None,
            output_structure=output_structure
        )

        if error:
            if isinstance(sequence, dict):
                sequence['_validation_status'] = 'invalid'
                sequence['_validation_error'] = error
            validation_errors.append({
                'item_id': seq_id,
                'item_index': idx,
                'error': error
            })
            print(f"Item {seq_id}: [INVALID]")
            if args.verbose:
                print(f"  Error: {error}")
        else:
            if isinstance(sequence, dict):
                sequence['_validation_status'] = 'valid'
            print(f"Item {seq_id}: [VALID]")

    # Print summary
    print("=" * 70)
    print(f"Total: {len(sequences)}")
    print(f"Valid: {len(sequences) - len(validation_errors)}")
    print(f"Invalid: {len(validation_errors)}")

    if validation_errors:
        print(f"\nSchema errors found in {len(validation_errors)} item(s):")
        for err in validation_errors[:10]:  # Show first 10
            error_preview = err['error'][:100] + "..." if len(err['error']) > 100 else err['error']
            print(f"  - ID {err['item_id']}: {error_preview}")
        if len(validation_errors) > 10:
            print(f"  ... and {len(validation_errors) - 10} more")

    # Save validation errors to separate file
    if validation_errors:
        # Save to same directory as input file (or output file if specified)
        base_path = Path(args.output).parent if args.output else input_path.parent
        errors_file = base_path / 'validation_errors.json'

        with open(errors_file, 'w', encoding='utf-8') as f:
            json.dump(validation_errors, f, indent=2, ensure_ascii=False)

        print(f"\nValidation errors saved to: {errors_file}")

    # Save output if requested
    if args.output:
        output_path = Path(args.output)

        # Reconstruct output in same format as input
        if is_pool:
            output_data = data  # SequencePool with updated sequences
        elif isinstance(data, list):
            output_data = sequences
        else:
            output_data = sequences[0] if len(sequences) == 1 else sequences

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"\nValidated output saved to: {output_path}")

    # Exit with error code if validation failed
    sys.exit(1 if validation_errors else 0)
