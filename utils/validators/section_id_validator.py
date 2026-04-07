"""Validator that checks every beat in a sections list has a stable ID.

Called by the pipeline executor after any formatting step that returns a
sections list, to catch formatting steps that accidentally drop IDs.
"""

from __future__ import annotations

from typing import Any


def validate_section_ids(data: Any) -> list[str]:
    """Return a list of violation messages, empty if all beats have IDs.

    Checks:
    - Every section has a "beats" key (not "steps" — legacy format is an error
      post-migration).
    - Every beat has an "id" field.
    - Every validator state has "beats" (not "steps").
    - Every validator beat has an "id" field.

    Args:
        data: Pipeline step output. Only validated if it is a list of section
            dicts (i.e. has "id" and "beats" on the first element).

    Returns:
        List of human-readable violation strings. Empty means valid.
    """
    if not isinstance(data, list) or not data:
        return []
    first = data[0]
    if not isinstance(first, dict) or "id" not in first:
        return []
    # Only validate if it looks like a sections list
    if "beats" not in first and "steps" not in first:
        return []

    violations: list[str] = []

    for section in data:
        if not isinstance(section, dict):
            continue
        sid = section.get("id", "?")

        if "steps" in section and "beats" not in section:
            violations.append(
                f"{sid}: has 'steps' key — id_stamper must run before this step"
            )
            continue

        beats = section.get("beats", [])
        for bi, beat in enumerate(beats):
            if not isinstance(beat, dict):
                continue
            if "id" not in beat:
                violations.append(f"{sid} beat[{bi}] (type={beat.get('type')}): missing 'id'")

            if beat.get("type") == "prompt":
                for vi, state in enumerate(beat.get("validator", [])):
                    if not isinstance(state, dict):
                        continue
                    if "steps" in state and "beats" not in state:
                        violations.append(
                            f"{sid} beat[{bi}] validator[{vi}]: has 'steps' — not flattened"
                        )
                        continue
                    for vbi, vbeat in enumerate(state.get("beats", [])):
                        if not isinstance(vbeat, dict):
                            continue
                        if "id" not in vbeat:
                            violations.append(
                                f"{sid} beat[{bi}] validator[{vi}] beat[{vbi}] "
                                f"(type={vbeat.get('type')}): missing 'id'"
                            )

    return violations
