"""Shared pipeline utility functions."""

from __future__ import annotations

import json
from pathlib import Path


def find_prior_sections_file(output_file_path: Path) -> Path | None:
    """Find the most recent sections JSON file in steps before output_file_path.

    Walks step directories in reverse order (highest step number first) and
    returns the first JSON file that looks like a flat-beats sections array:
    a list where every element is a dict with both "id" and "beats" keys.

    Also accepts the legacy "steps" key so this works during migration.

    Args:
        output_file_path: The current step's output file path. Only steps
            with a lower step number are considered.

    Returns:
        Path to the sections file, or None if not found.
    """
    try:
        version_dir = output_file_path.parent.parent
        own_step_num = int(output_file_path.parent.name.split("_")[1])
    except (IndexError, ValueError):
        return None

    for step_dir in sorted(version_dir.glob("step_*"), reverse=True):
        try:
            step_num = int(step_dir.name.split("_")[1])
        except (IndexError, ValueError):
            continue
        if step_num >= own_step_num:
            continue
        for json_file in sorted(step_dir.glob("*.json")):
            try:
                candidate = json.loads(json_file.read_text(encoding="utf-8"))
                if _is_sections_list(candidate):
                    return json_file
            except Exception:
                continue
    return None


def _is_sections_list(data: object) -> bool:
    """Return True if data looks like a sections array."""
    if not isinstance(data, list) or not data:
        return False
    return all(
        isinstance(s, dict)
        and "id" in s
        and ("beats" in s or "steps" in s)  # accept both during migration
        for s in data
    )
