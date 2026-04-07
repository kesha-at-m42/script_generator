"""
id_stamper - Formatting Step

Converts any legacy section format to the canonical flat-beats schema and
stamps stable, deterministic IDs on every beat.

Handles three input formats transparently:
  1. Old array-of-arrays:  "steps": [[beat, ...], [beat, ...]]
  2. Step-objects:         "steps": [{"id": ..., "beats": [...]}, ...]
  3. New flat format:      "beats": [beat, ...]

Output: sections with a flat "beats" list and stable "id" on every beat and
        validator-state beat.

ID scheme:
  - Section beat:    {section_id}_b{index}          e.g. s1_1_b0
  - Validator beat:  {prompt_beat_id}_v{vi}_b{bi}   e.g. s1_1_b2_v0_b0

Reconciliation (when output_file_path is supplied by the pipeline runner):
  Loads the previous run's sections file (same output filename, previous
  version directory).
  - Structure unchanged → copy IDs and _notion_block_id from previous run
    positionally.
  - Structure changed → assign fresh positional IDs, strip _notion_block_id,
    print a warning so the team knows Notion sync links were cleared.

Idempotent — running twice on already-stamped data produces identical output.
"""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Format detection & flattening
# ---------------------------------------------------------------------------


def _flatten_beats(section: dict) -> list[dict]:
    """Return a flat list of beats from any legacy or current section format."""
    if "beats" in section:
        return list(section["beats"])
    steps = section.get("steps", [])
    beats: list[dict] = []
    for step in steps:
        if isinstance(step, dict):
            beats.extend(step.get("beats", []))
        elif isinstance(step, list):
            beats.extend(step)
    return beats


def _flatten_validator_beats(state: dict) -> list[dict]:
    """Return a flat list of beats from any legacy or current validator state."""
    if "beats" in state:
        return list(state["beats"])
    steps = state.get("steps", [])
    beats: list[dict] = []
    for step in steps:
        if isinstance(step, dict):
            beats.extend(step.get("beats", []))
        elif isinstance(step, list):
            beats.extend(step)
    return beats


def _normalize_prev_section(section: dict) -> dict:
    """Flatten a previous-run section (any format) for reconciliation comparison."""
    flat = _flatten_beats(section)
    normalized: list[dict] = []
    for beat in flat:
        beat = dict(beat)
        if beat.get("type") == "prompt":
            new_validator = []
            for state in beat.get("validator", []):
                state = dict(state)
                state["beats"] = _flatten_validator_beats(state)
                state.pop("steps", None)
                new_validator.append(state)
            beat["validator"] = new_validator
        normalized.append(beat)
    norm = dict(section)
    norm["beats"] = normalized
    norm.pop("steps", None)
    return norm


# ---------------------------------------------------------------------------
# ID stamping
# ---------------------------------------------------------------------------


def _stamp_validator_beats(beats: list[dict], prompt_beat_id: str, vi: int) -> list[dict]:
    result = []
    for bi, beat in enumerate(beats):
        beat = copy.deepcopy(beat)
        beat.setdefault("id", f"{prompt_beat_id}_v{vi}_b{bi}")
        result.append(beat)
    return result


def _stamp_beats(beats: list[dict], section_id: str) -> list[dict]:
    """Stamp IDs on a flat beats list, recursing into validator states."""
    result = []
    for i, beat in enumerate(beats):
        beat = copy.deepcopy(beat)
        beat.setdefault("id", f"{section_id}_b{i}")
        if beat.get("type") == "prompt":
            new_validator = []
            for vi, state in enumerate(beat.get("validator", [])):
                state = dict(state)
                vbeats = _flatten_validator_beats(state)
                state["beats"] = _stamp_validator_beats(vbeats, beat["id"], vi)
                state.pop("steps", None)
                new_validator.append(state)
            beat["validator"] = new_validator
        result.append(beat)
    return result


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------


def _beat_type_seq(beats: list[dict]) -> tuple:
    return tuple(b.get("type", "") for b in beats)


def _copy_ids_from_prev(new_beats: list[dict], prev_beats: list[dict]) -> None:
    """Overwrite IDs and _notion_block_id on new_beats from prev_beats positionally."""
    for nb, pb in zip(new_beats, prev_beats):
        nb["id"] = pb["id"]
        if "_notion_block_id" in pb:
            nb["_notion_block_id"] = pb["_notion_block_id"]


def _find_prev_sections_file(output_file_path: Path) -> Path | None:
    """Find the same-named output file in the immediately preceding version dir."""
    try:
        version_dir = output_file_path.parent.parent
        m = re.match(r"^v(\d+)$", version_dir.name)
        if not m:
            return None
        prev_v = int(m.group(1)) - 1
        if prev_v < 0:
            return None
        prev_path = (
            version_dir.parent
            / f"v{prev_v}"
            / output_file_path.parent.name
            / output_file_path.name
        )
        return prev_path if prev_path.exists() else None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def stamp_ids(data: Any, output_file_path: Path | None = None, **_kwargs) -> list[dict]:
    """Convert all sections to flat-beats format and stamp stable IDs.

    Args:
        data: list of section dicts (any legacy format accepted).
        output_file_path: injected by the pipeline runner; used to locate
            the previous run's sections file for ID reconciliation.

    Returns:
        New list of section dicts with flat "beats" and IDs on every beat.
    """
    # Load and normalise previous run for reconciliation (best-effort)
    prev_by_id: dict[str, dict] = {}
    if output_file_path is not None:
        prev_file = _find_prev_sections_file(Path(output_file_path))
        if prev_file is not None:
            try:
                prev_raw = json.loads(prev_file.read_text(encoding="utf-8"))
                prev_by_id = {
                    s["id"]: _normalize_prev_section(s)
                    for s in prev_raw
                    if isinstance(s, dict) and "id" in s
                }
            except Exception:
                pass

    result = []
    for section in data:
        section = dict(section)
        section_id = section.get("id", "")

        raw_beats = _flatten_beats(section)
        section.pop("steps", None)
        stamped = _stamp_beats(raw_beats, section_id)
        section["beats"] = stamped

        prev_section = prev_by_id.get(section_id)
        if prev_section is not None:
            prev_beats = prev_section.get("beats", [])
            if _beat_type_seq(stamped) == _beat_type_seq(prev_beats):
                _copy_ids_from_prev(stamped, prev_beats)
            else:
                print(
                    f"  [ID RECONCILER] {section_id}: structure changed "
                    f"(was {len(prev_beats)} beats, now {len(stamped)} beats) "
                    f"— Notion sync links cleared"
                )

        result.append(section)

    return result
