"""
Prefill Generator Utilities
Generates dynamic prefills for Claude API calls to guide JSON structure
"""

import json
from typing import Dict, Any, Optional, List


def truncate_at_key(data: Dict[str, Any], path: List[str], add_opening: str = None) -> str:
    """
    Truncate a JSON structure at a specific nested key path and optionally add an opening.

    This is useful for generating prefills that guide Claude to continue from a specific point.

    Args:
        data: The complete data structure to truncate
        path: List of keys forming the path to truncate at (e.g., ["sequences", 0, "student_attempts"])
        add_opening: Optional string to add after truncation (e.g., '"error_path_generic": {')

    Returns:
        JSON string truncated at the specified location

    Example:
        data = {"sequences": [{"id": 1, "student_attempts": {"success_path": {...}}}]}
        path = ["sequences", 0, "student_attempts"]
        add_opening = '"error_path_generic": {'

        Result: JSON up to student_attempts with error_path_generic opening added
    """
    # Convert to JSON string first
    json_str = json.dumps(data, indent=2)

    # Build the search pattern for the path
    # Navigate through the structure to find where to truncate
    current = data
    keys_processed = []

    for key in path:
        keys_processed.append(key)
        if isinstance(key, int):
            # Array index
            current = current[key]
        else:
            # Dict key
            if key not in current:
                raise KeyError(f"Key '{key}' not found at path {keys_processed}")
            current = current[key]

    # Now we need to find this location in the JSON string
    # Convert the partial path back to JSON to find the location
    partial_data = data
    for i, key in enumerate(path[:-1]):
        if isinstance(key, int):
            partial_data = partial_data[key]
        else:
            partial_data = partial_data[key]

    # Get the JSON representation of the parent and target
    parent_json = json.dumps({path[-1]: current}, indent=2)

    # Find where this appears in the full JSON
    last_key = path[-1]
    if isinstance(last_key, str):
        search_pattern = f'"{last_key}":'
    else:
        # For array indices, this is trickier - might need different approach
        raise ValueError("Cannot truncate at array index - provide dict key instead")

    # Find the last occurrence of the pattern (in case of nested structures)
    # We'll use a more robust approach: serialize up to the parent, then add the key

    # Actually, simpler approach: just find the closing braces and truncate there
    # Let's rebuild this more carefully

    # Serialize the data up to the truncation point
    truncated_data = {}
    current_level = truncated_data
    source_level = data

    for i, key in enumerate(path):
        if isinstance(key, int):
            if i == len(path) - 1:
                # Last item - this is where we truncate
                current_level = source_level[:key+1]  # Include up to this index
            else:
                source_level = source_level[key]
        else:
            if i == len(path) - 1:
                # Last key - include it but make it empty
                current_level[key] = {}
            else:
                current_level[key] = {}
                current_level = current_level[key]
                source_level = source_level[key]

    # This is getting complex. Let me use a simpler string-based approach
    # Convert to JSON, then use string manipulation

    json_str = json.dumps(data, indent=2)

    # Find the location of the target key
    lines = json_str.split('\n')
    target_line_idx = None
    indent_level = None

    # Search for the key pattern
    search_str = f'"{last_key}":'
    for idx, line in enumerate(lines):
        if search_str in line:
            target_line_idx = idx
            indent_level = len(line) - len(line.lstrip())
            break

    if target_line_idx is None:
        raise ValueError(f"Could not find key '{last_key}' in JSON structure")

    # Truncate at this line and rebuild
    truncated_lines = lines[:target_line_idx + 1]

    # Remove the value part after the colon on the last line
    last_line = truncated_lines[-1]
    if ':{' in last_line or ':[' in last_line:
        # It's an object or array, keep the opening
        truncated_lines[-1] = last_line.split(':', 1)[0] + ': {'
    else:
        # It's a simple value, replace with opening brace
        truncated_lines[-1] = last_line.split(':', 1)[0] + ': {'

    result = '\n'.join(truncated_lines)

    # Add custom opening if provided
    if add_opening:
        # Remove the trailing brace we just added
        result = result.rstrip().rstrip('{').rstrip()
        # Add comma and the custom opening
        result += ',\n' + ' ' * (indent_level + 2) + add_opening

    return result


def truncate_for_remediation(sequence: Dict[str, Any]) -> str:
    """
    Generate a prefill for remediation generator that includes the sequence structure
    up to the opening of error_path_generic.

    This is a specialized truncation for the pp_remediation_generator prompt that:
    1. Includes the entire sequence with success_path
    2. Opens student_attempts for adding error_path_generic

    Args:
        sequence: The interaction sequence dict with student_attempts.success_path

    Returns:
        String containing the prefill JSON (incomplete, ready for Claude to continue)

    Example Input:
        {
          "problem_id": 1,
          "steps": [...],
          "student_attempts": {
            "success_path": {...}
          }
        }

    Example Output (string):
        {
          "sequences": [
            {
              "problem_id": 1,
              "steps": [...],
              "student_attempts": {
                "success_path": {...},
                "error_path_generic": {
    """
    # Create a copy to avoid modifying original
    prefill_seq = sequence.copy()

    # Ensure student_attempts exists
    if 'student_attempts' not in prefill_seq:
        prefill_seq['student_attempts'] = {}

    # Build prefill dict wrapping the sequence
    prefill_dict = {"sequences": [prefill_seq]}

    # Convert to formatted JSON
    prefill_json = json.dumps(prefill_dict, indent=2)

    # Find the student_attempts at sequence level (not step level)
    # and insert error_path_generic inside it
    import re

    # Look for the sequence-level student_attempts (it should be empty: {})
    # Pattern: "student_attempts": {} or "student_attempts": {...}
    # We want to find this at the sequence level (near the end)

    # Find the last occurrence of "student_attempts":
    lines = prefill_json.split('\n')
    target_line_idx = None

    for idx in reversed(range(len(lines))):
        if '"student_attempts":' in lines[idx]:
            target_line_idx = idx
            break

    if target_line_idx is None:
        # Fallback: student_attempts doesn't exist, add it
        prefill_parts = prefill_json.rsplit('}', 2)
        prefill_text = prefill_parts[0] + '},\n      "student_attempts": {\n        "error_path_generic": {'
        return prefill_text

    # Check if student_attempts is empty or has content
    student_attempts_line = lines[target_line_idx]

    if '{}' in student_attempts_line:
        # Empty student_attempts - replace {} with { and add error_path_generic
        lines[target_line_idx] = student_attempts_line.replace('{}', '{')
        # Add error_path_generic opening on next line
        indent = '        '  # 8 spaces for nested field
        lines.insert(target_line_idx + 1, indent + '"error_path_generic": {')
        prefill_text = '\n'.join(lines[:target_line_idx + 2])
    else:
        # student_attempts has content - need to find its closing brace and add comma + error_path_generic
        # Find the closing brace for this student_attempts
        indent_level = len(student_attempts_line) - len(student_attempts_line.lstrip())
        closing_brace_idx = None

        for idx in range(target_line_idx + 1, len(lines)):
            line = lines[idx]
            line_indent = len(line) - len(line.lstrip())
            if line.strip() == '}' or line.strip() == '},' or line.strip() == '},':
                if line_indent == indent_level:
                    closing_brace_idx = idx
                    break

        if closing_brace_idx:
            # Insert before the closing brace
            indent = ' ' * (indent_level + 2)
            lines.insert(closing_brace_idx, indent + '"error_path_generic": {')
            # Add comma to previous line if needed
            prev_line = lines[closing_brace_idx - 1]
            if not prev_line.rstrip().endswith(','):
                lines[closing_brace_idx - 1] = prev_line.rstrip() + ','
            prefill_text = '\n'.join(lines[:closing_brace_idx + 1])
        else:
            # Couldn't find closing brace, use fallback
            prefill_parts = prefill_json.rsplit('}', 3)
            prefill_text = prefill_parts[0] + '},\n        "error_path_generic": {'

    return prefill_text


def truncate_for_interaction(question_data: Dict[str, Any]) -> str:
    """
    Generate a prefill for interaction designer that includes question metadata.

    Args:
        question_data: Question dict with goal_id, question_prompt, etc.

    Returns:
        String containing the prefill JSON with metadata (incomplete, ready for Claude to continue)

    Example Output:
        {
          "sequences": [
            {
              "problem_id": 5,
              "difficulty": 2,
              "verb": "IDENTIFY",
              "goal": "The student can identify unit fractions",
              "goal_id": 1,
    """
    prefill = f"""{{
  "sequences": [
    {{
      "problem_id": {question_data.get('goal_id', 1)}_{question_data.get('question_id', 1)},
      "difficulty": {question_data.get('difficulty_level', 0)},
      "verb": "{question_data.get('cognitive_type', 'IDENTIFY')}",
      "goal": "{question_data.get('goal_text', '')}",
      "goal_id": {question_data.get('goal_id', 1)},"""

    return prefill


def truncate_for_question(goal_id: int, goal_text: str) -> str:
    """
    Generate a prefill for question generator that includes goal metadata.

    Args:
        goal_id: The learning goal ID
        goal_text: The learning goal text

    Returns:
        String containing the prefill JSON (incomplete, ready for Claude to continue)

    Example Output:
        {
          "questions": [
            {
              "goal_id": 1,
              "goal_text": "The student can...",
    """
    prefill = f"""{{
  "questions": [
    {{
      "goal_id": {goal_id},
      "goal_text": "{goal_text}","""

    return prefill


def generate_prefill(prompt_id: str, item: Dict[str, Any]) -> Optional[str]:
    """
    Generate appropriate prefill based on prompt type.

    This is the main entry point for the pipeline to generate prefills dynamically.

    Args:
        prompt_id: The prompt identifier (e.g., "question_generator", "pp_remediation_generator")
        item: The data item being processed

    Returns:
        Prefill string or None if no dynamic prefill needed

    Example Usage (in pipeline_runner.py):
        from utils.prefill_generator import generate_prefill

        prefill_text = generate_prefill(prompt_id, item)
        if prefill_text:
            prompt_variables["prefill_sequence"] = prefill_text
    """
    if prompt_id == "pp_remediation_generator":
        return truncate_for_remediation(item)

    elif prompt_id == "interaction_designer":
        return truncate_for_interaction(item)

    elif prompt_id == "question_generator":
        # Note: question_generator uses template-based prefill in the prompt config
        # But we can still generate it here if needed
        goal_id = item.get('id', item.get('goal_id', 1))
        goal_text = item.get('text', item.get('goal_text', ''))
        return truncate_for_question(goal_id, goal_text)

    # No dynamic prefill for other prompts
    return None


def escape_for_json_string(text: str) -> str:
    """
    Escape a string to be safe inside a JSON string value.

    Handles quotes, newlines, and other special characters.

    Args:
        text: Raw text to escape

    Returns:
        Escaped text safe for JSON
    """
    # Replace special characters
    text = text.replace('\\', '\\\\')  # Backslashes first
    text = text.replace('"', '\\"')    # Quotes
    text = text.replace('\n', '\\n')   # Newlines
    text = text.replace('\r', '\\r')   # Carriage returns
    text = text.replace('\t', '\\t')   # Tabs
    return text


if __name__ == "__main__":
    # Test the functions
    print("Testing Prefill Generator")
    print("=" * 70)

    # Test 1: Question prefill
    print("\n1. Question Prefill:")
    question_prefill = truncate_for_question(
        goal_id=1,
        goal_text="The student can identify unit fractions"
    )
    print(question_prefill)

    # Test 2: Interaction prefill
    print("\n2. Interaction Prefill:")
    test_question = {
        "question_id": 5,
        "goal_id": 2,
        "goal_text": "The student can create unit fractions",
        "cognitive_type": "CREATE",
        "difficulty_level": 1,
        "question_prompt": "Shade 1/4 of the bar"
    }
    interaction_prefill = truncate_for_interaction(test_question)
    print(interaction_prefill)

    # Test 3: Remediation prefill
    print("\n3. Remediation Prefill:")
    test_sequence = {
      "problem_id": 1,
      "difficulty": 0,
      "verb": "divide",
      "goal": "The student can partition shapes into equal parts",
      "steps": [
        {
          "dialogue": "Here's a bar. We're going to split it into two equal parts.",
          "workspace": [
            {
              "id": "bar_1",
              "type": "rectangle_bar",
              "sections": 1,
              "state": "undivided",
              "shaded": [],
              "position": "center"
            }
          ]
        },
        {
          "dialogue": "Click once in the middle to divide the bar into 2 equal parts.",
          "prompt": "Click in the center to divide",
          "interaction_tool": "cut",
          "workspace_context": {
            "tangibles_present": [
              "bar_1"
            ],
            "note": "Undivided horizontal rectangle bar"
          },
          "correct_answer": {
            "value": "1/2",
            "context": "One click in the center divides the bar into 2 equal halves"
          }
        }
      ],
      "student_attempts": {
        "success_path": {
          "steps": [
            {
              "dialogue": "Perfect! You found the exact midpoint."
            }
          ]
        }
      }
    }
    remediation_prefill = truncate_for_remediation(test_sequence)
    print(remediation_prefill[:300] + "...")

    # Test 4: Auto-generate based on prompt_id
    print("\n4. Auto-generation:")
    auto_prefill = generate_prefill("pp_remediation_generator", test_sequence)
    print(f"Generated {len(auto_prefill)} characters for pp_remediation_generator")

    print("\n" + "=" * 70)
    print("All tests completed successfully!")
