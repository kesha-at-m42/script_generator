"""
dialogue_extractor - Formatting Step

Pre-extracts dialogue beats from each section into a flat list with context
labels, ready for the dialogue_rewriter AI step.

This makes extraction deterministic so the AI never needs to traverse the
section JSON itself — it only rewrites the pre-extracted list.

Context labels:
  "lesson"     — regular dialogue beat in section steps
  "on_correct" — dialogue beat inside an is_correct: true validator state

Output per section:
  {
    "id": "<section_id>",
    "dialogues": [
      {"text": "...", "context": "lesson"},
      {"text": "...", "context": "on_correct"},
      ...
    ],
    "section": { ...original section JSON... }
  }
"""

import copy


def _extract(steps, in_correct_state=False):
    beats = []
    for step_group in steps:
        for beat in step_group:
            if beat.get("type") == "dialogue":
                context = "on_correct" if in_correct_state else "lesson"
                beats.append({"text": beat["text"], "context": context})
            elif beat.get("type") == "prompt":
                for state in beat.get("validator", []):
                    if state.get("is_correct"):
                        beats.extend(_extract(state.get("steps", []), in_correct_state=True))
    return beats


def extract_dialogues(data, **_kwargs):
    """Extract dialogue beats with context labels from each section."""
    result = []
    for section in data:
        result.append({
            "id": section["id"],
            "dialogues": _extract(section.get("steps", [])),
            "section": copy.deepcopy(section),
        })
    return result
