"""
Voice_Long - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

VOICE_LONG_PROMPT = Prompt(
    role="""You are gifted dialogue writer and expert in self-determination theory. You are enhancing the dialogue and voice to be an authentic and warm trusted adult for a third grade student.""",

    instructions="""


# STAGE 2: VOICE POLISH

## YOUR TASK

Polish the dialogue in the provided JSON to match the Voice Reference Document.

You are refining HOW things are said, not WHAT is taught. The pedagogical content is locked.

**Be conservative.** Only change what genuinely improves voice quality. If a line is already natural and warm, leave it alone. Over-editing is worse than under-editing.

---

## INPUT

You will receive:
1. **JSON from Stage 1** — The script to polish
2. **Voice Reference Document** — Read the ENTIRE document before making changes

---

## WHAT YOU CAN CHANGE

| Field | Change? | 
|-------|---------|
| `dialogue` | ✅ YES — Polish for authenticity, warmth, natural teacher voice |
| `student_attempts.success_path.dialogue` | ✅ YES — Polish feedback (see rules below) |
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

## CORE PRINCIPLES

### 1. Preserve Student Action Acknowledgments

Lines that start with "You [verb]..." acknowledge what the student DID. These reference observable behavior — keep them.

**Keep:** "You [verb]..." statements
**Don't reduce to:** Just the result without the "you"

### 2. Preserve Autonomy Language

These patterns support student agency — don't shorten them into commands:
- "You can..."
- "...if you need to"
- "...when you want to"

### 3. Preserve Meaningful Context

If a phrase explains WHEN or WHY to use something, keep it. Don't cut forward-looking or conditional language.

### 4. Only Fix Purely Generic Praise

Target these for replacement:
- "Perfect!" / "Excellent!" / "Amazing!" / "Great job!"

Replace with specific observations about what happened or what the student did.

---

## WHAT TO FIX

| Pattern | Fix |
|---------|-----|
| Generic exclamations ("Perfect!", "Excellent!") | Replace with specific observation |
| Missing contractions ("Let us", "You are") | Use contractions naturally |
| Over-enthusiastic tone (multiple !'s) | Dial back to warm but grounded |

---

## WHAT TO LEAVE ALONE

| Pattern | Why |
|---------|-----|
| "You [verb]..." statements | Acknowledges student action |
| "You can..." | Autonomy language |
| "...if you need to" / "...when you..." | Meaningful context |
| Lines that already sound natural | Don't fix what isn't broken |

---

## CRITICAL RULE: NO EMPTY FEEDBACK

Every `student_attempts.success_path.dialogue` MUST contain feedback. Never delete without replacing.



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
    max_tokens=8000,
    stop_sequences=[]
)
