"""
Benchmark Label Hider - Formatting Step

Sets is_label_visible: false on every Benchmark tangible found in any
workspace across all sequences. This suppresses the benchmark label
in-game without removing the benchmark itself.
"""


def _process_step(step, verbose, location=""):
    """Set is_label_visible: false on all Benchmark tangibles in a step's workspace."""
    workspace = step.get("workspace")
    if not isinstance(workspace, dict):
        return 0

    tangibles = workspace.get("tangibles", [])
    if not isinstance(tangibles, list):
        return 0

    count = 0
    for tangible in tangibles:
        if not isinstance(tangible, dict):
            continue
        if tangible.get("@type") != "Benchmark":
            continue
        if tangible.get("is_label_visible") is False:
            continue  # already set
        tangible["is_label_visible"] = False
        count += 1
        if verbose:
            loc = tangible.get("location", "1/2")
            print(f"  [BENCHMARK] {location}: set is_label_visible=false (location={loc})")

    return count


def _process_sequences(data, verbose):
    """Walk all sequences and hide benchmark labels."""
    if isinstance(data, dict) and data.get("@type") == "SequencePool":
        sequences = data.get("sequences", [])
    elif isinstance(data, list):
        sequences = data
    else:
        return data

    total = 0
    for seq_idx, item in enumerate(sequences, 1):
        if not isinstance(item, dict):
            continue
        steps = item.get("steps", [])
        if not isinstance(steps, list):
            continue
        for step_idx, step in enumerate(steps, 1):
            if not isinstance(step, dict):
                continue
            location = f"Seq{seq_idx}/Step{step_idx}"
            total += _process_step(step, verbose, location)

            # Also process remediations
            prompt = step.get("prompt", {})
            if not isinstance(prompt, dict):
                continue
            for remediation in prompt.get("remediations", []):
                if not isinstance(remediation, dict):
                    continue
                rem_step = remediation.get("step", {})
                if isinstance(rem_step, dict):
                    total += _process_step(rem_step, verbose, f"{location}/remediation")

    if verbose:
        print(f"\n[BENCHMARK LABEL HIDER] Set is_label_visible=false on {total} benchmark(s)")

    return data


def main(input_data, verbose=False, **kwargs):
    """
    Main entry point for pipeline execution.

    Args:
        input_data: List of sequences or SequencePool dict
        verbose: Enable logging (default: False)
        **kwargs: Additional arguments (unused)

    Returns:
        Same structure with is_label_visible=false on all Benchmark tangibles
    """
    return _process_sequences(input_data, verbose)
