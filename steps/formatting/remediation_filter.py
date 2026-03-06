"""
remediation_filter - Formatting Step

Returns a list of section IDs that contain at least one prompt with a real
validator (i.e. not a single any-response-advances state).

Used as the batch_only_items_file source for remediation_generator — sections
not in this list are passed through unchanged in the collated output.
"""


def _has_real_prompt(section):
    for step in section.get("steps", []):
        for beat in step:
            if beat.get("type") != "prompt":
                continue
            validator = beat.get("validator", [])
            is_ara = len(validator) == 1 and validator[0].get("condition") == {}
            if not is_ara:
                return True
    return False


def filter_sections(data):
    return {
        "batch_only_items": [section["id"] for section in data if _has_real_prompt(section)],
        "data": data,
    }
