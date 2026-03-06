"""
remediation_merger - Formatting Step

Merges {id, incorrects} items produced by remediation_generator back into
full section objects.

Input: collated output from remediation_generator step — an array where:
  - Passthrough items are full section objects (no real prompts, unchanged)
  - Processed items are {"id": "...", "incorrects": [[states...], ...]} dicts

Output: complete lesson_sections.json array with incorrect validator states
appended to each prompt beat's validator array.
"""

import copy
import json
from pathlib import Path


def _is_ara(validator):
    """Return True if validator is a single any-response-advances state."""
    return len(validator) == 1 and validator[0].get("condition") == {}


def _merge_incorrects_into_section(section, incorrects):
    """Append incorrect states from incorrects queue into matching prompt beats."""
    section = copy.deepcopy(section)
    queue = list(incorrects)  # one inner array per qualifying prompt, in order

    for step_beats in section.get("steps", []):
        for beat in step_beats:
            if beat.get("type") != "prompt":
                continue
            validator = beat.get("validator", [])
            if _is_ara(validator):
                continue
            if queue:
                beat["validator"].extend(queue.pop(0))

    return section


def merge_remediation(data, output_file_path=None):
    """Merge incorrect validator states back into full section objects.

    Args:
        data: collated output from remediation_generator (list of sections or
              {id, incorrects} dicts)
        output_file_path: path where this step's output will be saved; used to
                          locate the original lesson_generator output from step 1
    """
    # Load original sections from step 1 to reconstruct processed items
    original_by_id = {}
    if output_file_path is not None:
        version_dir = Path(output_file_path).parent.parent
        for step1_dir in sorted(version_dir.glob("step_01_*")):
            # Derive filename from directory name: "step_01_script_generator" → "script_generator.json"
            step_name = step1_dir.name.split("_", 2)[2]
            lesson_file = step1_dir / f"{step_name}.json"
            if lesson_file.exists():
                originals = json.loads(lesson_file.read_text(encoding="utf-8"))
                original_by_id = {s["id"]: s for s in originals}
                break

    result = []
    for item in data:
        if isinstance(item, dict) and "incorrects" in item:
            section_id = item["id"]
            original = original_by_id.get(section_id)
            if original is None:
                raise RuntimeError(
                    f"remediation_merger: original section '{section_id}' not found in step 1 output"
                )
            result.append(_merge_incorrects_into_section(original, item["incorrects"]))
        else:
            result.append(item)

    return result
