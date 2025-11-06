"""
Event Name Injector Utility
Injects event names into dialogue text for remediation steps
"""

from typing import Dict, List, Any


def inject_event_names_into_dialogue(sequences: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Inject event names into dialogue text for steps that have metadata.events.

    Prepends [event: event_name] to the dialogue for each event in the step's metadata.

    Args:
        sequences: List of sequence dicts from final.json

    Returns:
        Modified sequences with event names injected into dialogue

    Example:
        Input dialogue: "Let's think about this together..."
        Input events: [{"name": "A_cut_hint_1_2", ...}]
        Output dialogue: "[event: A_cut_hint_1_2] Let's think about this together..."
    """
    for sequence in sequences:
        # Process main steps
        if 'steps' in sequence:
            for step in sequence['steps']:
                _inject_into_step(step)

                # Process remediation steps
                if 'prompt' in step and 'remediations' in step['prompt']:
                    for remediation in step['prompt']['remediations']:
                        if 'step' in remediation:
                            _inject_into_step(remediation['step'])

    return sequences


def _inject_into_step(step: Dict[str, Any]) -> None:
    """
    Helper to inject event names into a single step's dialogue.
    Modifies the step in-place.
    """
    # Check if step has metadata.events
    if 'metadata' not in step:
        return

    metadata = step['metadata']
    if 'events' not in metadata or not metadata['events']:
        return

    # Check if step has dialogue
    if 'dialogue' not in step:
        return

    # Extract event names
    event_names = [event['name'] for event in metadata['events'] if 'name' in event]

    if not event_names:
        return

    # Build event prefix - separate [event: name] for each event
    event_prefix = "".join(f"[event: {name}]" for name in event_names)

    # Prepend to dialogue (avoid double-adding if already present)
    dialogue = step['dialogue']
    if not dialogue.startswith('[event'):
        step['dialogue'] = event_prefix + dialogue


def process_godot_sequences_with_events(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main entry point for processing godot formatter output to inject event names.

    Args:
        data: The complete data structure from godot_formatter (SequencePool)

    Returns:
        Modified data with event names injected into dialogue
    """
    if 'sequences' in data:
        data['sequences'] = inject_event_names_into_dialogue(data['sequences'])

    return data


if __name__ == "__main__":
    # Test the function
    import json

    test_step = {
        "@type": "Step",
        "metadata": {
            "events": [
                {
                    "name": "A_cut_hint_1_2",
                    "description": "Show visual guide for cutting bar at 1/2 mark"
                }
            ]
        },
        "dialogue": "Let's think about this together. You need to make a cut..."
    }

    print("Testing event injection:")
    print(f"Before: {test_step['dialogue']}")

    _inject_into_step(test_step)

    print(f"After: {test_step['dialogue']}")

    # Test with multiple events
    test_step_multi = {
        "@type": "Step",
        "metadata": {
            "events": [
                {"name": "A_cut_1_2"},
                {"name": "A_highlight_0"}
            ]
        },
        "dialogue": "Watch as I show you..."
    }

    print(f"\nMultiple events before: {test_step_multi['dialogue']}")
    _inject_into_step(test_step_multi)
    print(f"Multiple events after: {test_step_multi['dialogue']}")

    print("\n✓ Event injection test completed!")
