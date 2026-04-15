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


def _all_branch(validator):
    """Return True if every state in the validator is a branch state.

    Branch states (branch: true) are choice points where both options are
    correct — there is no wrong answer, so no remediations should be merged.
    """
    return bool(validator) and all(v.get("branch") is True for v in validator)


def _merge_incorrects_into_section(section, incorrects):
    """Append incorrect states from incorrects queue into matching prompt beats."""
    section = copy.deepcopy(section)
    queue = list(incorrects)  # one inner array per qualifying prompt, in order

    for beat in section.get("beats", []):
        if beat.get("type") != "prompt":
            continue
        validator = beat.get("validator", [])
        if _is_ara(validator) or _all_branch(validator):
            # Generator may have produced a placeholder empty group for this
            # prompt — consume and discard it to keep the queue aligned.
            if queue and not queue[0]:
                queue.pop(0)
            continue
        if queue:
            beat["validator"] = [s for s in beat["validator"] if s.get("is_correct", False)]
            beat["validator"].extend(queue.pop(0))

    return section


def merge_remediation(data, output_file_path=None):
    """Merge incorrect validator states back into full section objects.

    Args:
        data: collated output from remediation_generator (list of sections or
              {id, incorrects} dicts)
        output_file_path: path where this step's output will be saved; used to
                          locate the original sections from a prior step
    """
    from utils.pipeline_utils import find_prior_sections_file

    original_by_id = {}
    if output_file_path is not None:
        # Skip at least 3 steps back to avoid picking up the filter output
        version_dir = Path(output_file_path).parent.parent
        own_step_num = int(Path(output_file_path).parent.name.split("_")[1])

        source_file = None
        for step_dir in sorted(version_dir.glob("step_*"), reverse=True):
            try:
                step_num = int(step_dir.name.split("_")[1])
            except (IndexError, ValueError):
                continue
            if step_num > own_step_num - 3:
                continue
            for json_file in sorted(step_dir.glob("*.json")):
                try:
                    candidate = json.loads(json_file.read_text(encoding="utf-8"))
                    if (
                        isinstance(candidate, list)
                        and candidate
                        and isinstance(candidate[0], dict)
                        and "id" in candidate[0]
                        and ("beats" in candidate[0] or "steps" in candidate[0])
                    ):
                        source_file = json_file
                        break
                except Exception:
                    continue
            if source_file:
                break

        if source_file is not None:
            originals = json.loads(source_file.read_text(encoding="utf-8"))
            original_by_id = {s["id"]: s for s in originals}

    result = []
    for item in data:
        if isinstance(item, dict) and "incorrects" in item:
            section_id = item["id"]
            original = original_by_id.get(section_id)
            if original is None:
                raise RuntimeError(
                    f"remediation_merger: original section '{section_id}' not found in prior steps"
                )
            result.append(_merge_incorrects_into_section(original, item["incorrects"]))
        else:
            result.append(item)

    # Stamp IDs on any validator-state beats that remediation_generator left in
    # legacy steps format (arrays-of-arrays). id_stamper is idempotent so this
    # is safe even if beats were already stamped by an earlier pipeline step.
    from steps.formatting.id_stamper import stamp_ids
    return stamp_ids(result, output_file_path=output_file_path)
