"""
dialogue_extractor - Formatting Step

Pre-extracts dialogue beats from each section into a flat list with context
labels, ready for the dialogue_rewriter AI step.

This makes extraction deterministic so the AI never needs to traverse the
section JSON itself — it only rewrites the pre-extracted list.

Context labels:
  "lesson"     — regular dialogue beat in section beats
  "on_correct" — dialogue beat inside an is_correct: true validator state

Output per section:
  {
    "id": "<section_id>",
    "dialogues": [
      {"text": "...", "context": "lesson"},
      {"text": "...", "context": "on_correct"},
      ...
    ]
  }
"""


def _extract(beats, in_correct_state=False):
    result = []
    for beat in beats:
        if beat.get("type") == "dialogue":
            context = "on_correct" if in_correct_state else "lesson"
            result.append({"text": beat["text"], "context": context})
        elif beat.get("type") == "prompt":
            for state in beat.get("validator", []):
                if state.get("is_correct"):
                    result.extend(_extract(state.get("beats", []), in_correct_state=True))
    return result


def extract_dialogues(data, **_kwargs):
    """Extract dialogue beats with context labels from each section."""
    return [
        {
            "id": section["id"],
            "dialogues": _extract(section.get("beats", [])),
        }
        for section in data
    ]
