"""
dialogue_merger - Formatting Step

Merges {id, dialogues} items produced by dialogue_rewriter back into
full section objects, replacing dialogue beat texts positionally.

Input: collated output from dialogue_rewriter step — an array of:
  {"id": "...", "dialogues": ["text 0", "text 1", ...]}

Traversal order (must match dialogue_rewriter / dialogue_extractor):
  for each beat in section.beats:
    if type == "dialogue": replace text
    if type == "prompt": recurse into each is_correct validator state's beats

Output: complete sections array with dialogue texts replaced.
"""

import copy
import json
from pathlib import Path


def _count_dialogues(beats):
    count = 0
    for beat in beats:
        if beat.get("type") == "dialogue":
            count += 1
        elif beat.get("type") == "prompt":
            for state in beat.get("validator", []):
                if state.get("is_correct"):
                    count += _count_dialogues(state.get("beats", []))
    return count


def _walk_and_replace(beats, texts, idx):
    for beat in beats:
        if beat.get("type") == "dialogue":
            beat["text"] = texts[idx[0]]
            idx[0] += 1
        elif beat.get("type") == "prompt":
            for state in beat.get("validator", []):
                if state.get("is_correct"):
                    _walk_and_replace(state.get("beats", []), texts, idx)


def _replace_dialogues(section, new_texts):
    """Return a deep copy of section with all dialogue texts replaced positionally."""
    expected = _count_dialogues(section.get("beats", []))
    if len(new_texts) != expected:
        raise RuntimeError(
            f"dialogue_merger: section '{section.get('id')}' has {expected} dialogue beats "
            f"but rewriter returned {len(new_texts)}"
        )
    section = copy.deepcopy(section)
    idx = [0]
    _walk_and_replace(section.get("beats", []), new_texts, idx)
    return section


def merge_dialogues(data, output_file_path=None):
    """Merge rewritten dialogue texts back into full section objects.

    Args:
        data: collated output from dialogue_rewriter — list of {id, dialogues} dicts
        output_file_path: path where this step's output will be saved; used to
                          locate the id-stamped sections from earlier in the pipeline
    """
    from steps.formatting.id_stamper import stamp_ids
    from utils.pipeline_utils import find_prior_sections_file

    original_by_id = {}
    if output_file_path is not None:
        source_file = find_prior_sections_file(Path(output_file_path))
        if source_file is not None:
            originals = json.loads(source_file.read_text(encoding="utf-8"))
            originals = stamp_ids(originals)
            original_by_id = {s["id"]: s for s in originals}

    result = []
    for item in data:
        if isinstance(item, dict) and "dialogues" in item:
            section_id = item["id"]
            original = original_by_id.get(section_id)
            if original is None:
                raise RuntimeError(
                    f"dialogue_merger: original section '{section_id}' not found in prior steps"
                )
            result.append(_replace_dialogues(original, item["dialogues"]))
        else:
            result.append(item)

    return result
