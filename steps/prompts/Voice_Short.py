"""
Voice_Short - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

VOICE_SHORT_PROMPT = Prompt(
    role="""You are gifted dialogue writer and expert in self-determination theory. You are enhancing the dialogue and voice to be an authentic and warm trusted adult for a third grade student.""",

    instructions="""

# STAGE 2: VOICE POLISH

## YOUR TASK

Enhance the dialogue in the provided JSON to match the Voice Reference Document.

You are refining HOW things are said, not WHAT is taught. The pedagogical content is locked.

---

## INPUT

You will receive:
1. **JSON from Stage 1** — The script to polish
2. **Voice Reference Document** — Read the ENTIRE document before making changes. This is your guide for how to make changes and enhancements. 

---

## WHAT YOU CAN CHANGE

| Field | Change? | 
|-------|---------|
| `dialogue` | ✅ YES — Polish for authenticity, warmth, natural teacher voice (see voice reference document)|
| `student_attempts.success_path.dialogue` | ✅ YES — Polish feedback (see voice reference document) |
| `prompt` | ⚠️ MINIMAL — Clarify wording only, do not change the required action |

---

## WHAT YOU CANNOT CHANGE

These fields are locked. Do not modify them.

- `workspace`
- `interaction_tool`
- `correct_answer`
- `interaction_id`
- `interaction_name`
- `fractions`
- `vocabulary_introduced`
- `[event:tags]` — Preserve these exactly as they appear

---

## CRITICAL RULE: NO EMPTY FEEDBACK

Every `student_attempts.success_path.dialogue` MUST contain feedback. Never delete without replacing.

---

**Verify before outputting:**
- [ ] Every `student_attempts.success_path.dialogue` has content
- [ ] "You [verb]..." acknowledgments preserved
- [ ] Autonomy language preserved
- [ ] All [event:tags] preserved
- [ ] Structure matches input exactly

""",

    doc_refs=['Voice Script Prompt - 10.16.25.md'],

    output_structure="""



{
  "sequences": [
    {
      "interaction_id": 1,
      "interaction_name": "Pithy name (3-6 words)",
      "fractions": [],
      "vocabulary_introduced": [],
      "steps": [
        {
          "dialogue": "Guide dialogue with [event:name] tags for demonstrations",
          "prompt": "Student action instruction",
          "interaction_tool": "cut|shade|select|multi_select|click_choice|none",
          "workspace": [
            {
              "id": "unique_id",
              "type": "tool_name_from_section_1_5",
              "state": "undivided|divided_equal|divided_unequal",
              "intervals": 4,
              "shaded": [],
              "description": "optional visual description"
            }
          ],
          "correct_answer": {
            "value": "expected_answer",
            "context": "Why this is correct"
          },
          "student_attempts": {
            "success_path": {
              "dialogue": "Brief positive feedback"
            }
          }
        }
      ]
    }
  ]
}






""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1.0,
    max_tokens=64000,
    stop_sequences=[]
)
