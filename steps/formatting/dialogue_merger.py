"""
dialogue_merger - Formatting Step

Merges {id, dialogues} items produced by dialogue_rewriter back into
full section objects, replacing dialogue beat texts positionally.

Input: collated output from dialogue_rewriter step — an array of:
  {"id": "...", "dialogues": ["text 0", "text 1", ...]}

Traversal order (must match dialogue_rewriter):
  for each step_group in section.steps:
    for each beat in step_group:
      if type == "dialogue": replace text
      if type == "prompt": recurse into each validator state's steps

Output: complete sections array with dialogue texts replaced.
"""

import copy
import json
from pathlib import Path


def _walk_and_replace(steps, texts, idx):
    """Walk steps depth-first, replacing dialogue texts from the texts list."""
    for step_group in steps:
        for beat in step_group:
            if beat.get("type") == "dialogue":
                if idx[0] < len(texts):
                    beat["text"] = texts[idx[0]]
                    idx[0] += 1
            elif beat.get("type") == "prompt":
                for state in beat.get("validator", []):
                    _walk_and_replace(state.get("steps", []), texts, idx)


def _replace_dialogues(section, new_texts):
    """Return a deep copy of section with all dialogue texts replaced positionally."""
    section = copy.deepcopy(section)
    idx = [0]
    _walk_and_replace(section.get("steps", []), new_texts, idx)
    return section


def merge_dialogues(data, output_file_path=None):
    """Merge rewritten dialogue texts back into full section objects.

    Args:
        data: collated output from dialogue_rewriter — list of {id, dialogues} dicts
        output_file_path: path where this step's output will be saved; used to
                          locate the original lesson_generator output from step 1
    """
    original_by_id = {}
    if output_file_path is not None:
        version_dir = Path(output_file_path).parent.parent
        for step1_dir in sorted(version_dir.glob("step_01_*")):
            step_name = step1_dir.name.split("_", 2)[2]
            lesson_file = step1_dir / f"{step_name}.json"
            if lesson_file.exists():
                originals = json.loads(lesson_file.read_text(encoding="utf-8"))
                original_by_id = {s["id"]: s for s in originals}
                break

    result = []
    for item in data:
        if isinstance(item, dict) and "dialogues" in item:
            section_id = item["id"]
            original = original_by_id.get(section_id)
            if original is None:
                raise RuntimeError(
                    f"dialogue_merger: original section '{section_id}' not found in step 1 output"
                )
            result.append(_replace_dialogues(original, item["dialogues"]))
        else:
            result.append(item)

    return result
