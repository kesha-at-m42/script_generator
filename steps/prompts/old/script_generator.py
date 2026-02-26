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
# STAGE 1: LESSON SCRIPT JSON CONVERSION

## YOUR TASK

Convert the Module Starter Pack Section 1.7 (Lesson Phase) from prose into structured JSON.

This is **TRANSLATION**, not creative writing. Every interaction, dialogue line, and prompt already exists in Section 1.7. You are reformatting, not inventing.

---

## BEFORE YOU GENERATE ANYTHING

**REQUIRED FIRST STEP:** Extract and list these constraints from the Starter Pack.

### From Section 1.2 (Scope Boundaries) — FORBIDDEN ITEMS
List everything under "NOT THIS" or "MUST NOT include":
```
FORBIDDEN:
- [item 1]
- [item 2]
- ...
```

### From Section 1.5 (Tool Specifications) — ALLOWED TOOLS
List every tool by its exact name as written in Section 1.5:
```
ALLOWED TOOLS:
- [tool name 1] — interactions: [how students interact]
- [tool name 2] — interactions: [how students interact]
- ...
```

### From Section 1.8 (Script Requirements) — LANGUAGE CONSTRAINTS
```
REQUIRED PHRASES:
- [phrase 1]
- ...

FORBIDDEN PHRASES:
- [phrase 1]
- ...
```

**Write these lists first. Then generate JSON. Do not skip this step.**

---

## DERIVING WORKSPACE TYPE

The `type` field in workspace tangibles MUST come from Section 1.5.

### Process:
1. Read Section 1.7's **Visual:** description for the interaction
2. Find the matching tool in your ALLOWED TOOLS list (from Section 1.5)
3. Use that **exact tool name** as the `type` value

### Rules:
- If Section 1.5 calls it "Grid Arrays" → use `"type": "grid_array"`
- If Section 1.5 calls it "Hexagons" → use `"type": "hexagon"`
- If a tool is NOT in Section 1.5, it does NOT exist for this module
- Do NOT use generic names like "rectangle", "bar", "circle", "number_line" unless Section 1.5 uses that exact term

### Validation:
Before outputting any workspace object, verify: "Is this type in my ALLOWED TOOLS list?"
If no → STOP. You are inventing a tool that doesn't exist.

---

## DERIVING INTERACTION_TOOL

The `interaction_tool` field MUST match how Section 1.5 says students interact with that tool.

### Process:
1. Read Section 1.7's **Prompt:** line
2. Identify which tool (from Section 1.5) the student acts on
3. Check Section 1.5's "Interaction:" description for that tool
4. Convert to interaction_tool value:

| Section 1.5 says... | Use interaction_tool: |
|---------------------|----------------------|
| "Click to partition" / "Click to divide" / "Click to split" | `"cut"` |
| "Click to shade" / "Tap to shade" | `"shade"` |
| "Click to select" / "Tap to select" | `"select"` |
| "Select multiple" / "Click multiple" | `"multi_select"` |
| "Match" / "Drag to match" | `"match"` |
| Multiple choice / Options shown | `"click_choice"` |
| No student action / Guide demonstrates | `"none"` |

### Validation:
If the prompt describes an interaction NOT supported by Section 1.5's tools → STOP and flag in generation_notes.

---

## TRANSFERRING CONTENT FROM SECTION 1.7

### Dialogue
- Transfer **Guide:** lines directly to `dialogue` field
- For demonstrations, add `[event:event_name]` after action verbs
- Do NOT rewrite for voice (Stage 2 handles voice polish)

### Prompts  
- Transfer **Prompt:** lines directly to `prompt` field
- If no Prompt line, use `"Watch the demonstration."` for demos or omit for observations

### Success Responses
- Transfer **On Correct:** or success lines to `success_dialogue`

### Vocabulary
- Check Section 1.3 for which terms are introduced at which interaction
- Include in `vocabulary_introduced` array when staged

---

## WORKSPACE STATE TRANSITIONS

| Event | State |
|-------|-------|
| Before any cuts | `"state": "undivided", "intervals": 1` |
| After cutting into N equal parts | `"state": "divided_equal", "intervals": N` |
| After shading X parts | Add indices to `"shaded": [0, 1, ...]` |

### Multi-Step Continuity
If Step 1 is demonstration and Step 2 is "your turn":
- Step 1 workspace: starting state
- Step 2 workspace: shows result of Step 1 OR fresh starting state (based on Section 1.7)

---

## ANIMATION EVENTS

When Section 1.7 indicates Guide demonstrates an action, embed event tags.

### Syntax
`[event:event_name]` immediately after the action verb

### Common Events
| When Guide... | Use event: |
|---------------|------------|
| Cuts/partitions | `automatic_cuts` |
| Shows where to cut | `cutting_guides` |
| Shades parts | `shading_support` |
| Counts/labels | `counting_support` |
| Compares items | `comparison_support` |
| Shows eraser tool | `eraser_demo` |

---

## WHAT NOT TO DO

❌ **Do NOT invent tools** — Only Section 1.5 tools exist  
❌ **Do NOT use forbidden items** — Section 1.2 is absolute  
❌ **Do NOT add interactions** — Follow Section 1.7 exactly  
❌ **Do NOT rewrite dialogue** — Transfer as-is (Stage 2 polishes)  
❌ **Do NOT write remediation** — Use `"remediation_placeholder": true`  
❌ **Do NOT use generic type names** — Derive from Section 1.5 exactly

---

## POST-GENERATION VERIFICATION

After generating, verify against Section 1.9 checklist:

- [ ] Interaction count within required range
- [ ] All required fractions from Section 1.8 appear
- [ ] Vocabulary staged per Section 1.3
- [ ] All required phrases present in dialogue
- [ ] No forbidden phrases appear
- [ ] Every workspace type is in ALLOWED TOOLS list
- [ ] Nothing from FORBIDDEN list appears anywhere

**Document any violations in `metadata.generation_notes`.**

---

## OUTPUT

Provide valid JSON matching the output structure schema.
""",

    doc_refs=['Module 1 Starter Pack VPSS - AI Ready.md'],

    output_structure="""
{
  "sequences": [
    {
      "interaction_id": 1,
      "interaction_name": "Pithy name (3-6 words)",
      "fractions": [],
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
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
