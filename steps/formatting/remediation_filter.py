"""
remediation_filter - Formatting Step

Returns a list of section IDs that should receive AI-generated remediations.

Used as the batch_only_items_file source for remediation_generator — sections
not in this list are passed through unchanged in the collated output.

mode (via function_args in pipeline config):
  None (default) — any section with a real (non-ARA) prompt
  "single_select_mc" — sections containing a multiple_choice prompt
  "multiselect_mc"   — sections containing a multi_select prompt
  "mc"               — either of the above
"""

_SINGLE_SELECT_MC_TOOLS = {"multiple_choice"}
_MULTISELECT_MC_TOOLS = {"multi_select"}


def _has_real_prompt(section):
    for beat in section.get("beats", []):
        if beat.get("type") != "prompt":
            continue
        validator = beat.get("validator", [])
        is_ara = len(validator) == 1 and validator[0].get("condition") == {}
        if not is_ara:
            return True
    return False


def _has_mc_prompt(section, tools):
    for beat in section.get("beats", []):
        if beat.get("type") == "prompt" and beat.get("tool") in tools:
            return True
    return False


def filter_sections(data, mode=None):
    if mode == "single_select_mc":
        match = lambda s: _has_mc_prompt(s, _SINGLE_SELECT_MC_TOOLS)  # noqa: E731
    elif mode == "multiselect_mc":
        match = lambda s: _has_mc_prompt(s, _MULTISELECT_MC_TOOLS)  # noqa: E731
    elif mode == "mc":
        match = lambda s: _has_mc_prompt(s, _SINGLE_SELECT_MC_TOOLS | _MULTISELECT_MC_TOOLS)  # noqa: E731
    else:
        match = _has_real_prompt

    return {
        "batch_only_items": [section["id"] for section in data if match(section)],
        "data": data,
    }
