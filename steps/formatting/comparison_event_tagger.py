"""
Comparison Event Tagger - Formatting Step

Prepends a Godot event tag to `on_correct.dialogue` for any step that:
1. Has a MathExpression tangible with " ? " in its terms (comparison placeholder)
2. Has choices.options == ["<", "=", ">"]
3. Has a validator.answer with at least one index

Event tag mapping (based on correct answer index into options):
  0 → "<"  → [event:Change_sign_to_less]
  1 → "="  → [event:Change_sign_to_equals]
  2 → ">"  → [event:Change_sign_to_greater]
"""

_EVENT_TAGS = {
    "<": "[event:Change_sign_to_less]",
    "=": "[event:Change_sign_to_equals]",
    ">": "[event:Change_sign_to_greater]",
}

_COMPARISON_OPTIONS = {"<", "=", ">"}


def _has_comparison_placeholder(tangibles):
    """Return True if any MathExpression tangible contains ' ? ' in its terms."""
    if not isinstance(tangibles, list):
        return False
    for tangible in tangibles:
        if not isinstance(tangible, dict):
            continue
        if tangible.get("@type") != "MathExpression":
            continue
        terms = tangible.get("terms", [])
        if isinstance(terms, list) and " ? " in terms:
            return True
    return False


def _process_step(step, seq_idx, step_idx, verbose):
    """Tag on_correct.dialogue for a single step if it meets the criteria."""
    workspace = step.get("workspace", {})
    tangibles = workspace.get("tangibles", []) if isinstance(workspace, dict) else []

    if not _has_comparison_placeholder(tangibles):
        return

    prompt = step.get("prompt", {})
    if not isinstance(prompt, dict):
        return

    # Check choices.options contains exactly {"<", "=", ">"}
    choices = prompt.get("choices", {})
    if not isinstance(choices, dict):
        return
    options = choices.get("options", [])
    if set(options) != _COMPARISON_OPTIONS:
        return

    # Get correct answer index
    validator = prompt.get("validator", {})
    if not isinstance(validator, dict):
        return
    answer = validator.get("answer", [])
    if not isinstance(answer, list) or not answer:
        return

    answer_idx = answer[0]
    correct_symbol = options[answer_idx] if answer_idx < len(options) else None
    event_tag = _EVENT_TAGS.get(correct_symbol)
    if event_tag is None:
        if verbose:
            print(f"  [WARN] Seq{seq_idx}/Step{step_idx}: answer symbol '{correct_symbol}' (index {answer_idx}) not in event map")
        return

    # Prepend to on_correct.dialogue
    on_correct = prompt.get("on_correct", {})
    if not isinstance(on_correct, dict):
        return

    dialogue = on_correct.get("dialogue", "")
    if not isinstance(dialogue, str):
        return

    # Skip if tag is already present
    if dialogue.startswith(event_tag):
        return

    on_correct["dialogue"] = f"{event_tag} {dialogue}"

    if verbose:
        print(f"  [TAG] Seq{seq_idx}/Step{step_idx}: prepended {event_tag}")


def _process_sequences(data, verbose):
    """Walk all sequences and tag qualifying steps."""
    if isinstance(data, dict) and data.get("@type") == "SequencePool":
        sequences = data.get("sequences", [])
    elif isinstance(data, list):
        sequences = data
    else:
        return data

    tagged = 0
    for seq_idx, item in enumerate(sequences, 1):
        if not isinstance(item, dict):
            continue
        steps = item.get("steps", [])
        if not isinstance(steps, list):
            continue
        for step_idx, step in enumerate(steps, 1):
            if not isinstance(step, dict):
                continue
            before = step.get("prompt", {}).get("on_correct", {}).get("dialogue", "")
            _process_step(step, seq_idx, step_idx, verbose)
            after = step.get("prompt", {}).get("on_correct", {}).get("dialogue", "")
            if before != after:
                tagged += 1

    if verbose:
        print(f"\n[COMPARISON EVENT TAGGER] Tagged {tagged} on_correct dialogue(s)")

    return data


def main(input_data, verbose=False, **kwargs):
    """
    Main entry point for pipeline execution.

    Args:
        input_data: List of sequences or SequencePool dict
        verbose: Enable logging (default: False)
        **kwargs: Additional arguments (unused)

    Returns:
        Same structure with event tags prepended to qualifying on_correct dialogues
    """
    return _process_sequences(input_data, verbose)


if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(
        description="Prepend Godot event tags to on_correct.dialogue for comparison steps."
    )
    parser.add_argument("files", nargs="+", metavar="FILE", help="JSON file(s) to fix in place")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    for path in args.files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            result = main(data, verbose=args.verbose)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"[OK] {path}")
        except Exception as e:
            print(f"[ERROR] {path}: {e}", file=sys.stderr)
