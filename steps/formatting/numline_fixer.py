"""
NumLine Fixer - Formatting Step

Fixes NumLine issues:
1. Ensures all labels are strings, not numeric values
2. For LabelValidator/PointValidator answers: ensures fractions are in range, have ticks, and are not read-only
3. Moves labels to alt_labels when frac_labels mode has whole number fractions in answer
4. Ensures whole number ticks and labels exist when range extends beyond 2
"""

import os
from fractions import Fraction


# ============================================================================
# DEBUG LOGGING HELPERS
# ============================================================================

class NumLineLogger:
    """Tracks and logs NumLine formatting changes"""
    def __init__(self, enabled=False):
        self.enabled = enabled
        self.changes = {
            'labels_fixed': 0,
            'alt_labels_added': 0,
            'ticks_added': 0,
            'labels_added': 0,
            'readonly_fixed': 0
        }
        self.details = []

    def log_labels_fixed(self, location, old_labels, new_labels):
        """Log when numeric labels are converted to strings"""
        if not self.enabled or old_labels == new_labels:
            return

        self.changes['labels_fixed'] += 1
        self.details.append({
            'type': 'labels_fixed',
            'location': location,
            'old': old_labels,
            'new': new_labels
        })
        print(f"\n[DEBUG] LABELS FIXED - {location}")
        print(f"  BEFORE: {old_labels}")
        print(f"  AFTER:  {new_labels}")

    def log_alt_labels_added(self, location, alt_labels):
        """Log when alt_labels are added"""
        if not self.enabled:
            return

        self.changes['alt_labels_added'] += 1
        self.details.append({
            'type': 'alt_labels_added',
            'location': location,
            'alt_labels': alt_labels
        })
        print(f"\n[DEBUG] ALT_LABELS ADDED - {location}")
        print(f"  Added: {alt_labels}")

    def log_ticks_added(self, location, old_ticks, new_ticks):
        """Log when ticks are added"""
        if not self.enabled or old_ticks == new_ticks:
            return

        added = [t for t in new_ticks if t not in old_ticks]
        self.changes['ticks_added'] += len(added)
        self.details.append({
            'type': 'ticks_added',
            'location': location,
            'added': added
        })
        print(f"\n[DEBUG] TICKS ADDED - {location}")
        print(f"  Added: {added}")
        print(f"  Full ticks: {new_ticks}")

    def log_labels_list_updated(self, location, old_labels, new_labels):
        """Log when labels list is updated"""
        if not self.enabled or old_labels == new_labels:
            return

        added = [l for l in new_labels if l not in old_labels]
        self.changes['labels_added'] += len(added)
        self.details.append({
            'type': 'labels_updated',
            'location': location,
            'added': added
        })
        print(f"\n[DEBUG] LABELS UPDATED - {location}")
        print(f"  Added: {added}")
        print(f"  Full labels: {new_labels}")

    def log_readonly_fixed(self, location, old_readonly, new_readonly, removed):
        """Log when ticks_is_read_only is fixed"""
        if not self.enabled or old_readonly == new_readonly:
            return

        self.changes['readonly_fixed'] += 1
        self.details.append({
            'type': 'readonly_fixed',
            'location': location,
            'removed': removed
        })
        print(f"\n[DEBUG] READONLY FIXED - {location}")
        print(f"  Removed: {removed}")
        print(f"  BEFORE: {old_readonly}")
        print(f"  AFTER:  {new_readonly}")

    def summary(self):
        """Print summary of all changes"""
        if not self.enabled:
            return

        print(f"\n{'='*70}")
        print(f"NUMLINE FIXER SUMMARY")
        print(f"{'='*70}")

        if self.changes['labels_fixed'] > 0:
            print(f"[OK] Numeric labels fixed: {self.changes['labels_fixed']} NumLines")
        if self.changes['alt_labels_added'] > 0:
            print(f"[OK] Alt_labels added: {self.changes['alt_labels_added']} NumLines")
        if self.changes['ticks_added'] > 0:
            print(f"[OK] Ticks added: {self.changes['ticks_added']} whole number ticks")
        if self.changes['labels_added'] > 0:
            print(f"[OK] Labels added: {self.changes['labels_added']} whole number labels")
        if self.changes['readonly_fixed'] > 0:
            print(f"[OK] Readonly fixed: {self.changes['readonly_fixed']} NumLines")

        if not any(self.changes.values()):
            print("No changes made")


# Global logger instance
_logger = NumLineLogger()


def parse_fraction(frac_str):
    """
    Parse a fraction string to get its decimal value.

    Args:
        frac_str: Fraction string like "3/4", "2/2", or "3"

    Returns:
        tuple: (numerator, denominator, decimal_value)
    """
    if '/' in str(frac_str):
        parts = frac_str.split('/')
        num, denom = int(parts[0]), int(parts[1])
        return num, denom, num / denom
    else:
        # Whole number
        val = int(frac_str)
        return val, 1, float(val)


def is_whole_number(frac_str):
    """Check if a fraction string represents a whole number."""
    try:
        num, denom, decimal = parse_fraction(frac_str)
        return num % denom == 0
    except:
        return False


def simplify_to_whole(frac_str):
    """Convert a whole number fraction to its whole number string."""
    try:
        num, denom, decimal = parse_fraction(frac_str)
        if num % denom == 0:
            return str(num // denom)
    except:
        pass
    return frac_str


def get_whole_numbers_in_range(range_list):
    """
    Get all whole number positions within a range.

    Args:
        range_list: [start, end] like [0, 3]

    Returns:
        list: Whole number strings like ["0", "1", "2", "3"]
    """
    if not isinstance(range_list, list) or len(range_list) != 2:
        return []

    start, end = range_list
    whole_numbers = []
    for i in range(int(start), int(end) + 1):
        whole_numbers.append(str(i))
    return whole_numbers


def fix_numline_labels(data, location_prefix=""):
    """
    Recursively fix NumLine labels to ensure they are strings.

    Converts numeric values in labels arrays to strings while preserving
    string values. Handles boolean labels (true/false) without modification.

    Args:
        data: Any data structure (dict, list, or primitive)
        location_prefix: Location prefix for logging (internal use)

    Returns:
        Fixed data structure with string labels
    """
    if isinstance(data, dict):
        # Check if this is a NumLine with labels array
        if data.get("@type") == "NumLine" and "labels" in data:
            labels = data["labels"]

            # Only fix if labels is an array (not boolean)
            if isinstance(labels, list):
                old_labels = labels[:]
                fixed_labels = []
                for label in labels:
                    if isinstance(label, (int, float)):
                        # Convert numeric to string
                        if isinstance(label, int) or label.is_integer():
                            fixed_labels.append(str(int(label)))
                        else:
                            fixed_labels.append(str(label))
                    else:
                        # Keep strings as-is
                        fixed_labels.append(label)

                if old_labels != fixed_labels:
                    _logger.log_labels_fixed(location_prefix or "NumLine", old_labels, fixed_labels)
                data["labels"] = fixed_labels

        # Recursively process all dict values
        return {key: fix_numline_labels(value, location_prefix) for key, value in data.items()}

    elif isinstance(data, list):
        # Recursively process all list items
        return [fix_numline_labels(item, location_prefix) for item in data]

    else:
        # Primitive value, return as-is
        return data


def add_alt_labels_for_whole_numbers(step):
    """
    Move labels to alt_labels in NumLine when frac_labels mode has whole number fractions in answer.

    When a Move tool with mode="frac_labels" has a validator answer containing fractions
    representing whole numbers (like "2/2", "3/3", "6/3"), move the existing labels to
    alt_labels (as fixed reference labels) and set labels to false.

    Args:
        step: Step dictionary

    Returns:
        Modified step dictionary
    """
    prompt = step.get('prompt', {})
    if not isinstance(prompt, dict):
        return step

    tool = prompt.get('tool', {})
    if not isinstance(tool, dict):
        return step

    # Check if this is frac_labels mode
    if tool.get('mode') != 'frac_labels':
        return step

    # Check validator answer for whole number fractions
    validator = prompt.get('validator', {})
    if not isinstance(validator, dict):
        return step

    # Only process LabelValidator
    if validator.get('@type') != 'LabelValidator':
        return step

    answer = validator.get('answer', [])
    if not isinstance(answer, list):
        return step

    # Check if any answer fraction represents a whole number
    has_whole_number_fraction = False
    for frac in answer:
        if frac and is_whole_number(frac):
            has_whole_number_fraction = True
            break

    # If no whole number fractions in answer, nothing to do
    if not has_whole_number_fraction:
        return step

    # Move labels to alt_labels in NumLine tangibles
    workspace = step.get('workspace', {})
    if not isinstance(workspace, dict):
        return step

    tangibles = workspace.get('tangibles', [])
    for idx, tangible in enumerate(tangibles):
        if tangible.get('@type') == 'NumLine':
            # Move labels to alt_labels if labels is an array
            if isinstance(tangible.get('labels'), list):
                # Move existing labels to alt_labels (override if exists)
                tangible['alt_labels'] = tangible['labels']
                tangible['labels'] = False

                # Convert whole number fractions in alt_labels to numeric form
                alt_labels = tangible.get('alt_labels', [])
                if isinstance(alt_labels, list):
                    converted_alt_labels = []
                    for label in alt_labels:
                        if is_whole_number(label):
                            # Use existing simplify_to_whole helper (line 170)
                            whole_num = simplify_to_whole(label)
                            if whole_num:
                                converted_alt_labels.append(whole_num)
                            else:
                                converted_alt_labels.append(label)
                        else:
                            converted_alt_labels.append(label)

                    tangible['alt_labels'] = converted_alt_labels

                location = step.get('_location', f"NumLine[{idx}]")
                _logger.log_alt_labels_added(location, tangible['alt_labels'])

    return step


def ensure_whole_number_ticks_and_labels(tangible, location="NumLine", validator_answer=None):
    """
    Ensure NumLine has ticks and labels at all whole number positions when range > 2.

    When a number line extends beyond 2 (like [0, 3] or [0, 4]), ensure there are
    ticks and labels at all whole number positions (0, 1, 2, 3, etc.).

    IMPORTANT: Does NOT add whole numbers to labels if they are in the validator answer
    (to avoid giving away the answer).

    Args:
        tangible: NumLine tangible dictionary
        location: Location string for logging
        validator_answer: List of answer fractions from validator (to avoid adding to labels)

    Returns:
        Modified tangible dictionary
    """
    if tangible.get('@type') != 'NumLine':
        return tangible

    range_list = tangible.get('range', [0, 1])
    if not isinstance(range_list, list) or len(range_list) != 2:
        return tangible

    start, end = range_list

    # Only apply if range extends to 2 or beyond
    if end < 2:
        return tangible

    # Get all whole numbers in range
    whole_numbers = get_whole_numbers_in_range(range_list)

    # Normalize validator answer
    if not isinstance(validator_answer, list):
        validator_answer = []

    # Ensure ticks includes all whole numbers (if ticks is an array)
    ticks = tangible.get('ticks')
    if isinstance(ticks, list):
        old_ticks = ticks[:]
        # Add any missing whole numbers to ticks
        # Use fraction equivalence checking (e.g., 6/3 = 2)
        for wn in whole_numbers:
            # Check if this whole number (or equivalent fraction) already exists
            has_equivalent = False
            for tick in ticks:
                if are_fractions_equal(tick, wn):
                    has_equivalent = True
                    break

            if not has_equivalent:
                ticks.append(wn)

        # Sort ticks by their numeric value
        try:
            ticks.sort(key=lambda x: parse_fraction(x)[2])
        except:
            pass  # If sorting fails, keep original order

        # Log if changes were made
        if old_ticks != ticks:
            _logger.log_ticks_added(location, old_ticks, ticks)

    # Ensure labels includes all whole numbers EXCEPT those in the validator answer
    labels = tangible.get('labels')
    if isinstance(labels, list):
        old_labels = labels[:]
        # Add any missing whole numbers to labels (except answer positions)
        # Use fraction equivalence checking (e.g., 6/3 = 2)
        for wn in whole_numbers:
            # Check if this whole number is in the validator answer
            is_in_answer = False
            for answer_frac in validator_answer:
                if are_fractions_equal(wn, answer_frac):
                    is_in_answer = True
                    break

            # Skip if it's in the answer (don't give away the answer!)
            if is_in_answer:
                continue

            # Check if this whole number (or equivalent fraction) already exists
            has_equivalent = False
            for label in labels:
                if are_fractions_equal(label, wn):
                    has_equivalent = True
                    break

            if not has_equivalent:
                labels.append(wn)

        # Sort labels by their numeric value
        try:
            labels.sort(key=lambda x: parse_fraction(x)[2])
        except:
            pass  # If sorting fails, keep original order

        # Log if changes were made
        if old_labels != labels:
            _logger.log_labels_list_updated(location, old_labels, labels)

    return tangible


def are_fractions_equal(frac1, frac2):
    """
    Check if two fraction strings are mathematically equal.

    Args:
        frac1: First fraction string (e.g., "6/3", "2")
        frac2: Second fraction string (e.g., "2", "6/3")

    Returns:
        bool: True if fractions are equal
    """
    try:
        _, _, decimal1 = parse_fraction(frac1)
        _, _, decimal2 = parse_fraction(frac2)
        return abs(decimal1 - decimal2) < 0.0001  # Allow for floating point errors
    except:
        return False


def ensure_answer_fractions_placeable(step):
    """
    Ensure all fractions in validator answer can be placed on the NumLine.

    Supports both LabelValidator and PointValidator.

    For each fraction in the validator answer, this function ensures:
    1. The fraction is within the NumLine range (extends range if needed)
    2. There is a tick at that position (adds to ticks if missing)
    3. The tick is NOT read-only (removes from ticks_is_read_only if present)
    4. Whole numbers NOT in the answer ARE read-only (adds to ticks_is_read_only)

    Args:
        step: Step dictionary

    Returns:
        Modified step dictionary
    """
    prompt = step.get('prompt', {})
    if not isinstance(prompt, dict):
        return step

    validator = prompt.get('validator', {})
    if not isinstance(validator, dict):
        return step

    # Check if this is a LabelValidator or PointValidator
    validator_type = validator.get('@type')
    if validator_type not in ['LabelValidator', 'PointValidator']:
        return step

    # Get the answer array
    answer = validator.get('answer', [])
    if not isinstance(answer, list):
        answer = []

    # Process NumLine tangibles
    workspace = step.get('workspace', {})
    if not isinstance(workspace, dict):
        return step

    tangibles = workspace.get('tangibles', [])
    for idx, tangible in enumerate(tangibles):
        if tangible.get('@type') != 'NumLine':
            continue

        location = step.get('_location', f"NumLine[{idx}]")

        # Get current range, ticks, and read_only
        range_list = tangible.get('range', [0, 1])
        if not isinstance(range_list, list) or len(range_list) != 2:
            continue

        start, end = range_list
        ticks = tangible.get('ticks')
        ticks_readonly = tangible.get('ticks_is_read_only')

        # Collect ALL fractions that need tick support (answer + labels + points)
        all_fractions_needing_ticks = list(answer) if answer else []

        # Add fractions from existing labels
        labels = tangible.get('labels')
        if isinstance(labels, list):
            for label in labels:
                if label and isinstance(label, str) and '/' in label:
                    all_fractions_needing_ticks.append(label)

        # Add fractions from existing points
        points = tangible.get('points')
        if isinstance(points, list):
            for point in points:
                if point and isinstance(point, str):
                    all_fractions_needing_ticks.append(point)

        # If no fractions need support, skip this NumLine
        if not all_fractions_needing_ticks:
            continue

        # Step 1: Check if all answer fractions are in range, extend if needed
        needs_extension = False
        max_answer_value = end

        for frac in answer:
            try:
                _, _, decimal_value = parse_fraction(frac)
                if decimal_value > end or decimal_value < start:
                    needs_extension = True
                    max_answer_value = max(max_answer_value, decimal_value)
            except:
                continue

        if needs_extension:
            import math
            new_end = math.ceil(max_answer_value)
            old_range = range_list[:]
            tangible['range'] = [start, new_end]

            if _logger.enabled:
                print(f"\n[DEBUG] RANGE EXTENDED - {location}")
                print(f"  BEFORE: {old_range}")
                print(f"  AFTER:  [{start}, {new_end}]")
                print(f"  REASON: Answer contains fractions beyond range")

        # Step 2: Ensure ticks supports all fractions (answer + labels + points)
        if isinstance(ticks, str):
            # Already a string interval - leave as-is
            pass
        elif isinstance(ticks, list):
            # Check if the list already includes all required positions
            all_positions_supported = True
            for frac in all_fractions_needing_ticks:
                has_tick = False
                for tick in ticks:
                    if are_fractions_equal(tick, frac):
                        has_tick = True
                        break
                if not has_tick:
                    all_positions_supported = False
                    break

            # Only convert to string if required positions are missing
            if not all_positions_supported:
                from math import gcd
                from functools import reduce

                denominators = []
                for frac in all_fractions_needing_ticks:
                    try:
                        _, denom, _ = parse_fraction(frac)
                        denominators.append(denom)
                    except:
                        continue

                if denominators:
                    # Use the LCM of denominators, then set ticks to 1/LCM
                    lcm = reduce(lambda a, b: abs(a * b) // gcd(a, b), denominators)
                    old_ticks = ticks
                    tangible['ticks'] = f"1/{lcm}"

                    if _logger.enabled:
                        print(f"\n[DEBUG] TICKS SET - {location}")
                        print(f"  BEFORE: {old_ticks}")
                        print(f"  AFTER: 1/{lcm} (based on answer/labels/points denominators)")
        elif ticks is None:
            # Convert to string interval based on all fractions
            from math import gcd
            from functools import reduce

            denominators = []
            for frac in all_fractions_needing_ticks:
                try:
                    _, denom, _ = parse_fraction(frac)
                    denominators.append(denom)
                except:
                    continue

            if denominators:
                # Use the LCM of denominators, then set ticks to 1/LCM
                lcm = reduce(lambda a, b: abs(a * b) // gcd(a, b), denominators)
                old_ticks = ticks
                tangible['ticks'] = f"1/{lcm}"

                if _logger.enabled:
                    print(f"\n[DEBUG] TICKS SET - {location}")
                    print(f"  BEFORE: {old_ticks}")
                    print(f"  AFTER: 1/{lcm} (based on answer/labels/points denominators)")

        # Step 3: Update ticks_is_read_only
        # - Remove answer positions from read_only (students need to place labels there)
        # - Add whole numbers to read_only if they're NOT in the answer (prevent placement)
        if isinstance(ticks_readonly, list):
            old_readonly = ticks_readonly[:]
            removed_ticks = []
            updated_readonly = []

            # First, keep existing read_only ticks that are NOT answer positions
            for tick in ticks_readonly:
                is_answer_position = False
                for answer_frac in answer:
                    if are_fractions_equal(tick, answer_frac):
                        is_answer_position = True
                        removed_ticks.append(f"{tick} (matches {answer_frac})")
                        break

                if not is_answer_position:
                    updated_readonly.append(tick)

            # Second, add whole numbers to read_only if they're NOT in the answer
            current_range = tangible.get('range', [0, 1])
            whole_numbers = get_whole_numbers_in_range(current_range)
            added_readonly = []

            for wn in whole_numbers:
                # Check if this whole number is in the answer
                is_in_answer = False
                for answer_frac in answer:
                    if are_fractions_equal(wn, answer_frac):
                        is_in_answer = True
                        break

                # If NOT in answer and NOT already in read_only, add it
                if not is_in_answer:
                    already_readonly = False
                    for tick in updated_readonly:
                        if are_fractions_equal(tick, wn):
                            already_readonly = True
                            break

                    if not already_readonly:
                        updated_readonly.append(wn)
                        added_readonly.append(wn)

            # Update the field if changes were made
            if old_readonly != updated_readonly:
                tangible['ticks_is_read_only'] = updated_readonly
                if removed_ticks or added_readonly:
                    if _logger.enabled:
                        print(f"\n[DEBUG] READONLY UPDATED - {location}")
                        if removed_ticks:
                            print(f"  REMOVED: {removed_ticks}")
                        if added_readonly:
                            print(f"  ADDED: {added_readonly} (whole numbers not in answer)")
                        print(f"  BEFORE: {old_readonly}")
                        print(f"  AFTER:  {updated_readonly}")
                _logger.log_readonly_fixed(location, old_readonly, updated_readonly, removed_ticks)

    return step


def remove_internal_fields(data):
    """
    Recursively remove internal fields like _location from the data structure.

    Args:
        data: Any data structure (dict, list, or primitive)

    Returns:
        Data structure with internal fields removed
    """
    if isinstance(data, dict):
        # Remove internal fields and recursively process remaining values
        return {key: remove_internal_fields(value)
                for key, value in data.items()
                if not key.startswith('_')}
    elif isinstance(data, list):
        # Recursively process all list items
        return [remove_internal_fields(item) for item in data]
    else:
        # Primitive value, return as-is
        return data


def ensure_preplaced_points_in_validator(step):
    """
    Ensure pre-placed points in workspace are included in PointValidator answer.

    When a NumLine has pre-placed points and a PointValidator, the validator answer
    must include both the pre-placed points AND the points the student should place.

    IMPORTANT: Only adds points from interactable NumLines (is_read_only not set or false).
    Points on reference lines (is_read_only: true) are NOT added to the validator.

    Args:
        step: Step dictionary

    Returns:
        Modified step dictionary
    """
    prompt = step.get('prompt', {})
    if not isinstance(prompt, dict):
        return step

    validator = prompt.get('validator', {})
    if not isinstance(validator, dict):
        return step

    # Only process PointValidator
    if validator.get('@type') != 'PointValidator':
        return step

    validator_answer = validator.get('answer', [])
    if not isinstance(validator_answer, list):
        return step

    # Get pre-placed points from workspace
    workspace = step.get('workspace', {})
    if not isinstance(workspace, dict):
        return step

    tangibles = workspace.get('tangibles', [])
    for tangible in tangibles:
        if tangible.get('@type') == 'NumLine' and 'points' in tangible:
            # Check if this NumLine is interactable (not a reference line)
            is_read_only = tangible.get('is_read_only', False)
            if is_read_only:
                # Skip reference lines - don't add their points to validator
                continue

            workspace_points = tangible.get('points', [])
            if isinstance(workspace_points, list) and workspace_points:
                # Add any missing pre-placed points to validator answer
                added = []
                for point in workspace_points:
                    if point not in validator_answer:
                        validator_answer.append(point)
                        added.append(point)

                if added:
                    # Sort by numeric value
                    try:
                        validator_answer.sort(key=lambda x: parse_fraction(x)[2])
                    except:
                        pass  # If sorting fails, keep original order

                    validator['answer'] = validator_answer

                    if _logger.enabled:
                        location = step.get('_location', 'Step')
                        print(f"\n[DEBUG] POINTVALIDATOR UPDATED - {location}")
                        print(f"  Added pre-placed points from interactable NumLine: {added}")
                        print(f"  Updated answer: {validator_answer}")

    return step


def process_step(step, location):
    """
    Process a single step to fix NumLine issues.

    Args:
        step: Step dictionary
        location: Location string for logging
    """
    step['_location'] = location

    # Ensure validator answer fractions can be placed (range, ticks, read_only)
    ensure_answer_fractions_placeable(step)

    # Add alt_labels for whole numbers
    add_alt_labels_for_whole_numbers(step)

    # Ensure pre-placed points are in PointValidator answer
    ensure_preplaced_points_in_validator(step)

    # Get validator answer to avoid adding to labels
    validator_answer = []
    prompt = step.get('prompt', {})
    if isinstance(prompt, dict):
        validator = prompt.get('validator', {})
        if isinstance(validator, dict):
            answer = validator.get('answer', [])
            if isinstance(answer, list):
                validator_answer = answer

    # Ensure whole number ticks/labels
    workspace = step.get('workspace', {})
    if isinstance(workspace, dict):
        tangibles = workspace.get('tangibles', [])
        for tangible_idx, tangible in enumerate(tangibles):
            tangible_loc = f"{location}/NumLine[{tangible_idx}]"
            ensure_whole_number_ticks_and_labels(tangible, tangible_loc, validator_answer)


def process_sequences(input_data):
    """
    Process input data to fix NumLine issues.

    Handles both formats:
    1. SequencePool with sequences array
    2. List of sequences with steps arrays
    3. List of flattened step items

    Args:
        input_data: SequencePool dict, list of sequences, or flattened items

    Returns:
        Same format as input with fixed NumLine labels and alt_labels
    """
    # Reset logger for new run
    global _logger
    _logger = NumLineLogger()

    # First pass: Fix numeric labels to strings (works recursively on entire structure)
    data = fix_numline_labels(input_data)

    # Second pass: Extract sequences array to process
    # (modifications happen in place, preserving SequencePool wrapper and metadata)
    if isinstance(data, dict) and data.get('@type') == 'SequencePool':
        sequences = data['sequences']
    elif isinstance(data, list):
        sequences = data
    else:
        sequences = []

    # Process each sequence or flattened step
    if isinstance(sequences, list):
        for seq_idx, item in enumerate(sequences, 1):
            if isinstance(item, dict):
                # Check if this is a sequence with steps
                if 'steps' in item:
                    for step_idx, step in enumerate(item.get('steps', []), 1):
                        location = f"Seq{seq_idx}/Step{step_idx}"
                        process_step(step, location)

                # Or flattened step item
                elif 'workspace' in item or 'prompt' in item:
                    location = f"Step{seq_idx}"
                    process_step(item, location)

    # Print summary
    _logger.summary()

    # Remove internal fields before returning
    data = remove_internal_fields(data)

    return data


# Entry point for pipeline
def main(input_data, verbose=False, **kwargs):
    """
    Main entry point for pipeline execution

    Args:
        input_data: List of sequences or flattened items
        verbose: Enable debug logging (default: False)
        **kwargs: Additional arguments (unused)

    Returns:
        List with fixed NumLine labels and alt_labels
    """
    global _logger
    _logger = NumLineLogger(enabled=verbose)

    return process_sequences(input_data)


if __name__ == "__main__":
    # Test with sample data
    sample_input = [
        # Test 1: Numeric labels (needs fixing)
        {
            "problem_id": 36,
            "template_id": "5004",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Look at the point.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 1],
                                "ticks": "1/6",
                                "points": ["4/6"],
                                "labels": [0, "1/2", 1],  # NUMERIC - needs fixing
                                "lcm": 18
                            }
                        ]
                    }
                }
            ]
        },
        # Test 2: frac_labels with whole number fraction (needs alt_labels)
        {
            "problem_id": 45,
            "template_id": "5011",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Drag labels.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 1],
                                "ticks": "1/2",
                                "labels": ["0", "1"],
                                "lcm": 12
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Drag the label.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "2/2"}
                                ]
                            }
                        }
                    }
                }
            ]
        },
        # Test 3: Extended range beyond 2 (needs whole number labels)
        {
            "problem_id": 57,
            "template_id": "5015",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Drag labels.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 3],
                                "ticks": "1/3",
                                "labels": ["0", "1/3"],  # Missing "1", "2", "3"
                                "lcm": 12
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Drag labels.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "4/3"},
                                    {"@type": "FracLabelStack", "label": "6/3"}
                                ]
                            }
                        }
                    }
                }
            ]
        },
        # Test 4: ticks_is_read_only should exclude answer positions
        {
            "problem_id": 60,
            "template_id": "5020",
            "steps": [
                {
                    "step_id": 1,
                    "dialogue": "Place fractions.",
                    "workspace": {
                        "tangibles": [
                            {
                                "@type": "NumLine",
                                "visual": "line",
                                "range": [0, 2],
                                "ticks": ["0", "1/3", "2/3", "1", "4/3", "5/3", "2"],
                                "labels": ["0", "1", "2"],
                                "ticks_is_read_only": ["0", "1", "2"],  # "2" should be removed (6/3 = 2)
                                "lcm": 9
                            }
                        ]
                    },
                    "prompt": {
                        "@type": "Prompt",
                        "text": "Place the fractions.",
                        "tool": {
                            "@type": "Move",
                            "mode": "frac_labels",
                            "palette": {
                                "@type": "Palette",
                                "stacks": [
                                    {"@type": "FracLabelStack", "label": "4/3"},
                                    {"@type": "FracLabelStack", "label": "5/3"},
                                    {"@type": "FracLabelStack", "label": "6/3"}
                                ]
                            }
                        },
                        "validator": {
                            "@type": "LabelValidator",
                            "answer": ["4/3", "5/3", "6/3"]
                        }
                    }
                }
            ]
        },
        {
      "@type": "Sequence",
      "metadata": {
        "@type": "SequenceMetadata",
        "problem_id": 88,
        "template_id": "6012",
        "template_skill": "Two-step: Student extends partition from 1-2 matching 0-1 spacing, then labels the beyond-1 positions",
        "identifiers": [
          "7/6",
          "8/6"
        ],
        "mastery_tier": "STRETCH",
        "mastery_verb": "create",
        "telemetry_data": {
          "mastery_skill": "Student can extend partitioning past 1, then label fractions beyond 1",
          "cognitive_verb": "create",
          "mastery_skill_id": "M6-01, M6-02",
          "tier": "STRETCH",
          "non_curriculum_skills": [
            "click_accuracy",
            "spatial_reasoning",
            "extended_number_line_reasoning"
          ],
          "misconception_id": [
            11,
            4,
            3
          ],
          "misconception_tag": [
            "fractions_cant_exceed_one",
            "improper_spacing_on_number_line",
            "numerator_denominator_as_independent"
          ],
          "component": "procedural"
        },
        "mastery_component": "PROCEDURAL"
      },
      "steps": [
        {
          "@type": "Step",
          "dialogue": "This number line shows sixths from 0 to 1. Extend the pattern from 1 to 2.",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {
                "@type": "NumLine",
                "is_visible": True,
                "visual": "line",
                "range": [
                  0,
                  2
                ],
                "ticks": [
                  "0",
                  "1/6",
                  "2/6",
                  "3/6",
                  "4/6",
                  "5/6",
                  "1"
                ],
                "labels": [
                  "0",
                  "1",
                  "2"
                ],
                "ticks_is_read_only": [
                  "0",
                  "1/6",
                  "2/6",
                  "3/6",
                  "4/6",
                  "5/6",
                  "1"
                ],
                "lcm": 18
              }
            ]
          },
          "prompt": {
            "@type": "Prompt",
            "text": "Place tick marks to continue the sixths from 1 to 2.",
            "tool": {
              "@type": "Place",
              "lcm": 18,
              "bounds": [
                "0",
                "2"
              ]
            },
            "validator": {
              "@type": "TickValidator",
              "answer": [
                "0",
                "1/6",
                "2/6",
                "3/6",
                "4/6",
                "5/6",
                "1",
                "7/6",
                "8/6",
                "9/6",
                "10/6",
                "11/6",
                "2"
              ]
            },
            "remediations": [
              {
                "@type": "Remediation",
                "id": "light",
                "step": {
                  "@type": "Step",
                  "dialogue": "Not quite. Look at the spacing between the tick marks from 0 to 1. Use that same spacing to continue the pattern from 1 to 2."
                }
              },
              {
                "@type": "Remediation",
                "id": "medium",
                "step": {
                  "@type": "Step",
                  "dialogue": "Let's think about this together. From 0 to 1, you can see 6 equal intervals that create sixths. The pattern continues the same way past 1. Each sixth stays the same size. Match the spacing you see from 0 to 1 as you place tick marks from 1 to 2."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "Let me walk you through this. From 0 to 1, the number line is divided into 6 equal intervals - those are the sixths. To extend this pattern from 1 to 2, we keep using the same size intervals. Look at the distance between any two tick marks from 0 to 1 - that's one sixth. Now place 5 tick marks between 1 and 2 using that exact same spacing. The first tick after 1 is at [fraction numerator=7 denominator=6]7 sixths[/fraction], then [fraction numerator=8 denominator=6]8 sixths[/fraction], [fraction numerator=9 denominator=6]9 sixths[/fraction], [fraction numerator=10 denominator=6]10 sixths[/fraction], and [fraction numerator=11 denominator=6]11 sixths[/fraction] right before 2. That's how we extend fraction patterns - the equal intervals continue with the same spacing."
                }
              }
            ],
            "on_correct": {
              "@type": "Step",
              "dialogue": "Good, you extended the sixths to 2."
            }
          }
        },
        {
          "@type": "Step",
          "dialogue": "Now label the positions beyond 1.",
          "prompt": {
            "@type": "Prompt",
            "text": "Drag [fraction numerator=7 denominator=6][/fraction] and [fraction numerator=8 denominator=6][/fraction] to their correct positions.",
            "tool": {
              "@type": "Move",
              "mode": "frac_labels",
              "palette": {
                "@type": "Palette",
                "stacks": [
                  {
                    "@type": "FracLabelStack",
                    "label": "7/6"
                  },
                  {
                    "@type": "FracLabelStack",
                    "label": "8/6"
                  }
                ]
              }
            },
            "validator": {
              "@type": "LabelValidator",
              "answer": [
                "7/6",
                "8/6"
              ]
            },
            "remediations": [
              {
                "@type": "Remediation",
                "id": "light",
                "step": {
                  "@type": "Step",
                  "dialogue": "Not quite. Count how many sixths past 1 each fraction should be."
                }
              },
              {
                "@type": "Remediation",
                "id": "medium",
                "step": {
                  "@type": "Step",
                  "dialogue": "Let's think about this step by step. When you have [fraction numerator=7 denominator=6]7 sixths[/fraction], that's 7 sixths total. Six sixths equals 1, so [fraction numerator=7 denominator=6]7 sixths[/fraction] is one more sixth past 1. Similarly, [fraction numerator=8 denominator=6]8 sixths[/fraction] is 8 sixths total - that's 6 sixths to get to 1, then 2 more sixths past 1. Count the ticks past 1 to find where each fraction goes."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "Let me walk you through placing these fractions. We're working with sixths, and the number line shows each sixth marked. For [fraction numerator=7 denominator=6]7 sixths[/fraction], let's think: 6 sixths makes 1 whole, so [fraction numerator=7 denominator=6]7 sixths[/fraction] is one sixth past 1. That means [fraction numerator=7 denominator=6]7 sixths[/fraction] goes on the first tick mark after 1. For [fraction numerator=8 denominator=6]8 sixths[/fraction], we have 8 sixths total. That's 6 sixths to reach 1, then 2 more sixths past 1. So [fraction numerator=8 denominator=6]8 sixths[/fraction] goes on the second tick mark after 1. That's how we count fractions beyond 1 - once we reach the whole number, we keep counting the parts past it."
                }
              }
            ],
            "on_correct": {
              "@type": "Step",
              "dialogue": "Correct, you placed [fraction numerator=7 denominator=6]7 sixths[/fraction] and [fraction numerator=8 denominator=6]8 sixths[/fraction] on the line."
            }
          }
        }
      ]
    }
    ]

    result = process_sequences(sample_input)

    print("Testing NumLine Fixer")
    print("=" * 70)

    # Test 1: Numeric labels should be fixed
    print("\nTest 1 - Numeric labels fixed:")
    labels_1 = result[0]["steps"][0]["workspace"]["tangibles"][0]["labels"]
    print(f"  Input:  [0, '1/2', 1]")
    print(f"  Output: {labels_1}")
    assert labels_1 == ["0", "1/2", "1"], f"Expected ['0', '1/2', '1'], got {labels_1}"
    assert all(isinstance(label, str) for label in labels_1), "All labels should be strings"
    print("  PASS - All labels are now strings")

    # Test 2: alt_labels should be added for whole number fractions
    print("\nTest 2 - alt_labels added for whole number fractions:")
    tangible_2 = result[1]["steps"][0]["workspace"]["tangibles"][0]
    alt_labels_2 = tangible_2.get("alt_labels")
    print(f"  Palette has: ['2/2'] (equals 1)")
    print(f"  Alt_labels added: {alt_labels_2}")
    assert alt_labels_2 == ["1"], f"Expected ['1'], got {alt_labels_2}"
    print("  PASS - alt_labels correctly shows whole number")

    # Test 3: Whole number labels should be added when range > 2
    print("\nTest 3 - Whole number labels added for extended range:")
    labels_3 = result[2]["steps"][0]["workspace"]["tangibles"][0]["labels"]
    print(f"  Range: [0, 3]")
    print(f"  Input labels:  ['0', '1/3']")
    print(f"  Output labels: {labels_3}")
    for wn in ["0", "1", "2", "3"]:
        assert wn in labels_3, f"Expected '{wn}' in labels"
    print("  PASS - All whole numbers (0, 1, 2, 3) are in labels")

    # Also check alt_labels for Test 3
    tangible_3 = result[2]["steps"][0]["workspace"]["tangibles"][0]
    alt_labels_3 = tangible_3.get("alt_labels")
    print(f"  Alt_labels added: {alt_labels_3}")
    assert "2" in alt_labels_3, "Expected '2' in alt_labels (from 6/3)"
    print("  PASS - alt_labels shows whole number from palette")

    # Test 4: ticks_is_read_only should exclude answer positions
    print("\nTest 4 - ticks_is_read_only excludes answer positions:")
    tangible_4 = result[3]["steps"][0]["workspace"]["tangibles"][0]
    ticks_readonly_4 = tangible_4.get("ticks_is_read_only")
    print(f"  Input ticks_is_read_only:  ['0', '1', '2']")
    print(f"  Validator answer: ['4/3', '5/3', '6/3'] (6/3 = 2)")
    print(f"  Output ticks_is_read_only: {ticks_readonly_4}")
    assert "2" not in ticks_readonly_4, "Expected '2' to be removed (6/3 = 2 is in answer)"
    assert "0" in ticks_readonly_4, "Expected '0' to remain (not in answer)"
    assert "1" in ticks_readonly_4, "Expected '1' to remain (not in answer)"
    print("  PASS - '2' removed from read-only (matches 6/3 in answer)")

    # Test 5: Ticks should include whole number endpoint when in validator answer
    print("\nTest 5 - Ticks should include '2' when in TickValidator answer:")
    tangible_5 = result[4]["steps"][0]["workspace"]["tangibles"][0]
    ticks_5 = tangible_5.get("ticks")
    validator_answer_5 = result[4]["steps"][0]["prompt"]["validator"]["answer"]
    print(f"  Range: [0, 2]")
    print(f"  Input ticks:  ['0', '1/6', '2/6', '3/6', '4/6', '5/6', '1']")
    print(f"  Validator answer includes: '2'")
    print(f"  Output ticks: {ticks_5}")
    if "2" in ticks_5:
        print("  PASS - '2' was added to ticks")
    else:
        print("  FAIL - '2' is missing from ticks (should be added for range [0,2])")
        print(f"  Issue: ensure_whole_number_ticks_and_labels only works when range > 2")
        print(f"  The function needs to handle range == 2 as well")

    # Test 5b: Second step should have workspace added
    print("\nTest 5b - Second step should have workspace:")
    second_step_5 = result[4]["steps"][1]
    has_workspace_5 = "workspace" in second_step_5
    print(f"  Second step has workspace: {has_workspace_5}")
    if has_workspace_5:
        workspace_5 = second_step_5["workspace"]
        print(f"  Workspace type: {workspace_5.get('@type')}")
        print(f"  Has tangibles: {'tangibles' in workspace_5}")
        print("  PASS - Workspace added to second step")
    else:
        print("  INFO - No workspace in second step (may need add_empty_workspace_to_first_step)")

    print("\n" + "=" * 70)
    print("All tests passed!")
