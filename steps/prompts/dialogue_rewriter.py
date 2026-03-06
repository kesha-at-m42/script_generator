"""
dialogue_rewriter - AI Prompt

Rewrites all dialogue beats in a lesson section to improve voice, warmth,
and naturalness while preserving pedagogical intent.

Runs in batch mode — one call per section.

Input per call: full section JSON auto-wrapped as <input> by the pipeline.
Output per call:
  {
    "id": "<section_id>",
    "dialogues": ["rewritten text 1", "rewritten text 2", ...]
  }

The dialogues array contains one string per dialogue beat, in the order
they appear when walking the section depth-first:
  - for each step_group in section.steps:
      - for each beat in step_group:
          - if type == "dialogue": include
          - if type == "prompt": recurse into each validator state's steps

A downstream formatter (dialogue_merger) reinserts these texts positionally
into the original section.
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt  # noqa: E402

DIALOGUE_REWRITER_PROMPT = Prompt(
    role="""You are a dialogue writer for an interactive math lesson. The input dialogue is pedagogically approved placeholder text -- it captures WHAT the Guide needs to communicate. Your job is to transform HOW the Guide says it: rewrite every line to sound like a real person talking to an 8-year-old, using the voice defined in <guide_design>.""",
    instructions="""
## TASK

Walk the section in `<input>` and collect every dialogue beat in depth-first order, following this traversal:

```
for each step_group in section.steps:
  for each beat in step_group:
    if beat.type == "dialogue" -- include it
    if beat.type == "prompt" -- recurse:
      for each state in beat.validator:
        for each step_group in state.steps:
          (same walk)
```

Rewrite every dialogue line. Output one string per beat, in the same order.

---

## THE CORE TASK

The input dialogue is competent placeholder text -- clear, purposeful, pedagogically correct. It is NOT the final voice. It reads like a curriculum document. Your job is to make it sound like a real tutor sitting next to a kid.

**Every Guide line must be rewritten.** If your output contains lines unchanged from the input, you have not completed the task.

The transformation is not about adding warmth on top of what is there. It is about finding the human register -- the rhythm, the casual phrasing, the dry observations, the thinking-out-loud quality that makes the guide feel present and unscripted.

**Example of the transformation:**

Input (placeholder register):
"You made a graph with your Minis. Now let's read some other graphs. A graph isn't just a picture -- every part tells us something. Look at this Favorite Fruits graph."

Rewritten (Guide voice):
"You made a graph with your Minis. Each picture graph is more than just a picture -- every part of the graph gives us something to READ. Let's explore this by looking closer at this Favorite Fruits graph."

Same pedagogical content. Same required concept. More specific, more present, more purposeful.

---

## VOICE GOAL

The rewritten dialogue should sound like a real teacher talking -- not a curriculum document, not a voiceover script, not a well-written teacher's guide. A real teacher, speaking out loud, to a kid.

Read each line aloud before finalizing it. If it sounds like something you would read, not say, rewrite it.

Refer to <guide_design> for the specific voice patterns, register, and examples.

---

## CONSTRAINTS

**Preserve:**
- All factual content: numbers, category names, graph data, correct answers
- Pedagogical intent: what is being taught, what the student just did
- Required vocabulary from <vocabulary>
- Any phrases from <required_phrases> where they appear
- Approximate beat length -- do not expand a short beat into a long one

**Never:**
- Change numbers, category names, or factual values
- Add instructional content not in the original
- Use phrases from <forbidden_phrases>
- Use em dashes (use "..." or restructure instead)
- Use hollow praise: "Great job!", "Excellent!", "Perfect!" unless specifically earned and specific

---

## OUTPUT FORMAT

```json
{
  "id": "<section_id>",
  "dialogues": [
    "rewritten text for beat 0",
    "rewritten text for beat 1",
    ...
  ]
}
```

- One string per dialogue beat, in traversal order
- Strings only -- no beat metadata, no type fields
- The count MUST match the number of dialogue beats in the input section

---

## OUTPUT RULES

- Output ONLY the JSON object -- no explanation, no markdown fences
- The prefill already opens `{"id": "...", "dialogues": [` -- complete from that point
- Use double quotes throughout

""",
    doc_refs=[
        "guide_design.md",
    ],
    module_ref={
        "forbidden_phrases": "scope_fence.forbidden_phrases",
        "required_phrases": "scope_fence.required_phrases",
        "vocabulary": "vocabulary",
        "the_one_thing": "the_one_thing.statement",
    },
    output_structure="""
{
  "id": "s1_1_most_votes",
  "dialogues": [
    "You made your own graph. Nice. Now let's look at some graphs other people made. Here's the thing about graphs... they're not just pictures. Every part is actually telling you something. Let's figure out what.",
    "Apples got 6 votes. You read that right from the graph."
  ]
}
""",
    prefill='{"id": "{id}", "dialogues": [',
    examples=[],
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=4000,
    stop_sequences=[],
)
