"""
script_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

SCRIPT_GENERATOR_PROMPT = Prompt(
    role="""You are converting a detailed lesson specification into structured JSON format. This is TRANSLATION work, not creative work. The pedagogical decisions have already been made—your job is faithful conversion.""",

    instructions="""

## INPUT DOCUMENTS

 Read and fully understand the <Module 1 Starter Pack VPSS - AI Ready.md>. Here's how to use each section:

| Section | Purpose | How You Use It |
|---------|---------|----------------|
| 1.0 Learning Goals | Module objectives | Reference only—verify interactions serve these goals |
| 1.1 The One Thing | Core concept | Reference only—informs success criteria |
| 1.2 Scope Boundaries | What to include/exclude | CONSTRAINT—never add content outside these boundaries |
| 1.3 Vocabulary Architecture | Term staging order | CONSTRAINT—verify vocabulary appears at correct interaction |
| 1.4 Misconceptions | Error patterns | Reference for remediation context (Stage 3 uses fully) |
| 1.5 Tool Specifications | Workspace definitions | PRIMARY SOURCE for workspace arrays |
| 1.7 Lesson Phase | Interaction sequence | PRIMARY SOURCE—follow exactly |
| 1.8 Script Requirements | Required/forbidden phrases | CONSTRAINT—verify compliance |
| 1.9 Verification Checklist | Completeness check | Use after generation to verify |

---

## YOUR TASK

Convert each interaction from **Section 1.7** into JSON format.

**Critical principle:** Section 1.7 IS your script. You are reformatting, not rewriting.

For each numbered interaction (1.1, 1.2, 1.3, etc.):
1. Parse the prose specification
2. Extract dialogue, prompts, visual descriptions
3. Build workspace array from visual description + Section 1.5 tool specs
4. Determine interaction_tool from the student action
5. Set correct_answer based on expected response
6. Output structured JSON

---

## OUTPUT SCHEMA
```json
{
  "module_id": "M01",
  "path": "C",
  "phase": "lesson",
  "interactions": [
    {
      "interaction_id": "1.1",
      "interaction_name": "string (3-6 word summary)",
      "section": "string (e.g., 'Section 1: Grid Mastery')",
      "fractions_addressed": ["1/2", "1/4"],
      "vocabulary_introduced": ["term"] or [],
      "misconception_addressed": "M1.1" or null,
      
      "steps": [
        {
          "step_id": "1.1.1",
          "step_type": "demonstration" | "practice" | "observation",
          
          "workspace": [
            { /* tangible object */ }
          ],
          
          "dialogue": "Guide speech with [event:name] tags if demonstrating",
          "prompt": "Student-facing instruction (5-15 words)",
          
          "interaction_tool": "none" | "cut" | "shade" | "select" | "click_choice",
          
          "correct_answer": {
            "value": "varies by tool type",
            "context": "Why this is correct"
          },
          
          "success_dialogue": "Brief positive feedback (5-12 words)",
          
          "remediation_placeholder": true
        }
      ]
    }
  ]
}
```

---

## WORKSPACE TANGIBLE SCHEMA

Build workspace arrays using Section 1.5 Tool Specifications. Every tangible follows this structure:
```json
{
  "id": "unique_string",
  "type": "rectangle_bar" | "hexagon" | "grid",
  "state": "undivided" | "divided_equal" | "divided_unequal", 
  "intervals": number,
  "shaded": [indices] or [],
  "description": "optional context"
}
```

**Mapping Section 1.5 to Workspace:**

| Section 1.5 Tool | type value | intervals | Notes |
|------------------|------------|-----------|-------|
| Grid Arrays (1x2) | "rectangle_bar" | 2 | state: "undivided" before cut, "divided_equal" after |
| Grid Arrays (1x4) | "rectangle_bar" | 4 | |
| Grid Arrays (2x3) | "grid" | 6 | For sixths shown as 2D grid |
| Hexagons | "hexagon" | 2, 3, or 6 only | Per Section 1.5.2 |

**State Transitions:**
- Before student cuts: `"state": "undivided", "intervals": 1`
- After successful cut into 4 parts: `"state": "divided_equal", "intervals": 4`
- After shading 1 of 4 parts: `"shaded": [0]` (index of shaded section)

---

## INTERACTION_TOOL MAPPING

Determine from Section 1.7's prompt what action the student takes:

| Section 1.7 Language | interaction_tool | correct_answer format |
|---------------------|------------------|----------------------|
| "Click once in the middle to split..." | "cut" | "1/2" (each part created) |
| "Click X times to partition into Y parts" | "cut" | "1/Y" |
| "Click on 1 of the X parts to shade it" | "shade" | "1/X" |
| "Select the bar that shows..." | "select" | tangible id |
| "Match each bar to its fraction" | "select" or "drag" | mapping object |
| "[click_choice: yes/no]" | "click_choice" | "yes" or "no" |
| No student action (demo only) | "none" | omit correct_answer |

---

## ANIMATION EVENTS

When Section 1.7 indicates the Guide demonstrates something, embed animation events in dialogue:

**Syntax:** `[event:event_name]` placed immediately after the action verb

**Available Events:**
- `automatic_cuts` - Guide cuts shape automatically
- `cutting_guides` - Visual hints appear for where to cut
- `shading_support` - Guide shades sections
- `counting_support` - Guide counts and labels parts
- `comparison_support` - Guide highlights parts for comparison

**Example from Section 1.7:**
> "Here's one way we can split the bar into four equal parts: first split the bar in half, then split each half in half again." [DEMONSTRATE visually]

**Converts to:**
```json
"dialogue": "Here's one way we can split the bar into four equal parts. Watch as I divide [event:automatic_cuts] it in half, then split [event:automatic_cuts] each half in half again."
```

---

## MULTI-STEP SEQUENCES

Some interactions require multiple steps. Indicators in Section 1.7:

| Section 1.7 Pattern | Steps Needed |
|--------------------|--------------|
| Tool demo + student practice | 2 steps: demo (tool: "none"), then practice |
| Guide demonstrates [DEMONSTRATE] + "Your turn" | 2 steps |
| Partition prompt + Shade prompt (separate interactions) | Already separate—keep as separate interactions |
| Verification prompt embedded in interaction | Include as step within same interaction |

**Workspace Continuity Rule:**
If Step 1 shows guide cutting a bar, Step 2's workspace must show the CUT bar:
- Step 1: `"state": "undivided"` → Guide demonstrates cutting
- Step 2: `"state": "divided_equal", "intervals": 4` → Student sees result, takes action

---

## DIALOGUE HANDLING

**Transfer dialogue from Section 1.7 directly.** Do not rewrite for style—voice polish happens in Stage 2.

| Section 1.7 Element | Where It Goes |
|--------------------|---------------|
| **Guide:** "text" | `dialogue` field |
| **Prompt:** "text" | `prompt` field |
| **On Correct:** "text" | `success_dialogue` field |
| **Vocabulary:** Introduce "term" | `vocabulary_introduced` array + embed in dialogue |
| [DEMONSTRATE visually] | Add animation events to dialogue |

**Example Conversion:**

Section 1.7 Interaction 1.3:
> **Visual:** Bar partitioned into halves from 1.2
> **Guide:** "Now, please click one of those parts to shade it."
> **Prompt:** "Click on 1 of the 2 parts to shade it."
> **Remediation:** Full L-M-H (shade focus)
> **On Correct:** "Yes. You selected one part out of two equal parts."
> **Vocabulary:** After shading, introduce "partition"

Converts to:
```json
{
  "interaction_id": "1.3",
  "interaction_name": "Shade One Half",
  "section": "Section 1: Grid Mastery",
  "fractions_addressed": ["1/2"],
  "vocabulary_introduced": ["partition"],
  "misconception_addressed": null,
  
  "steps": [
    {
      "step_id": "1.3.1",
      "step_type": "practice",
      
      "workspace": [
        {
          "id": "bar_halves",
          "type": "rectangle_bar",
          "state": "divided_equal",
          "intervals": 2,
          "shaded": [],
          "description": "Bar partitioned into halves from previous interaction"
        }
      ],
      
      "dialogue": "Now, please click one of those parts to shade it.",
      "prompt": "Click on 1 of the 2 parts to shade it.",
      
      "interaction_tool": "shade",
      
      "correct_answer": {
        "value": "1/2",
        "context": "Student shades one of two equal parts"
      },
      
      "success_dialogue": "Yes. You selected one part out of two equal parts. When mathematicians divide something into equal parts like you just did, they call it PARTITIONING.",
      
      "remediation_placeholder": true
    }
  ]
}
```

---

## SECTION TRANSITIONS

Section 1.7 contains embedded transitions marked with ⚡ symbols. Convert these as observation steps:
```json
{
  "interaction_id": "1.11.transition",
  "interaction_name": "Section 1 Synthesis",
  "section": "Section 1: Grid Mastery",
  "fractions_addressed": ["1/2", "1/3", "1/4", "1/6", "1/8"],
  "vocabulary_introduced": [],
  "misconception_addressed": null,
  
  "steps": [
    {
      "step_id": "1.11.t.1",
      "step_type": "observation",
      
      "workspace": [
        {"id": "bar_halves", "type": "rectangle_bar", "state": "divided_equal", "intervals": 2, "shaded": [0]},
        {"id": "bar_thirds", "type": "rectangle_bar", "state": "divided_equal", "intervals": 3, "shaded": [0]},
        {"id": "bar_fourths", "type": "rectangle_bar", "state": "divided_equal", "intervals": 4, "shaded": [0]},
        {"id": "bar_sixths", "type": "rectangle_bar", "state": "divided_equal", "intervals": 6, "shaded": [0]},
        {"id": "bar_eighths", "type": "rectangle_bar", "state": "divided_equal", "intervals": 8, "shaded": [0]}
      ],
      
      "dialogue": "Look at all the fractions you've made: 1/2, 1/4, 1/3, 1/6, and 1/8. Each fraction shows one part of a whole that's been partitioned into equal parts.",
      "prompt": "Observe the fractions you created.",
      
      "interaction_tool": "none",
      "success_dialogue": null,
      "remediation_placeholder": false
    }
  ]
}
```

---

## CONSTRAINTS (from Sections 1.2, 1.3, 1.8)

**Before outputting, verify:**

☐ **Scope boundaries (Section 1.2):** No circles, no comparison, no equivalent fractions
☐ **Vocabulary staging (Section 1.3):** Terms appear at correct interaction
☐ **Required phrases (Section 1.8):** All five appear somewhere in script
☐ **Forbidden phrases (Section 1.8):** None appear
☐ **Interaction count:** Matches Section 1.7 (18-20 total, max 22)
☐ **All five fractions:** 1/2, 1/3, 1/4, 1/6, 1/8 all appear

**If any constraint would be violated, STOP and note the issue.**

---

## OUTPUT FORMAT

Return valid JSON only. Structure:
```json
{
  "metadata": {
    "module_id": "M01",
    "path": "C", 
    "phase": "lesson",
    "total_interactions": number,
    "sections": ["Section 1: Grid Mastery", "Section 2: Notation Bridge", "Section 3: Hexagon Extension"],
    "fractions_covered": ["1/2", "1/3", "1/4", "1/6", "1/8"],
    "vocabulary_introduced": ["whole", "partition", "equal parts", "fraction"],
    "generation_notes": "Any issues or flags"
  },
  "interactions": [
    // All interactions in sequence
  ]
}
```

---

## WHAT NOT TO DO

- ❌ Do NOT rewrite dialogue for style (Stage 2 handles voice)
- ❌ Do NOT add interactions beyond Section 1.7
- ❌ Do NOT skip interactions marked "optional" (include with `"optional": true` flag)
- ❌ Do NOT write full remediation (add `"remediation_placeholder": true` instead)
- ❌ Do NOT invent visual contexts—derive from Section 1.7 + Section 1.5 only
- ❌ Do NOT add warmth markers not already in Section 1.7 dialogue

---

## VERIFICATION (Run After Generation)

Use Section 1.9 Verification Checklist to confirm:

1. All Section 1 interactions (1.1-1.11) present
2. Notation intro embedded after 1.5
3. All Section 2 interactions (2.1-2.2) present
4. Section 3 interactions (3.0-3.6) present
5. All transitions/synthesis moments captured
6. Interaction count within range
7. All five fraction types appear
8. Vocabulary staging matches Section 1.3

**Output any verification failures in `metadata.generation_notes`.**

""",

    doc_refs=['Module 1 Starter Pack VPSS - AI Ready.md'],

    output_structure="""







""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
