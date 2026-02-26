"""
Remediation Generator - AI Prompt
Generates error remediation paths for interaction sequences
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

REMEDIATION_GENERATOR_PROMPT = Prompt(
    role="""You are an expert in designing error remediation for educational interactions.

Your task: Add ERROR PATHS to existing interaction sequences. Each error path has 3 remediation levels:
- **Light**: Quick redirect, no visual changes
- **Medium**: Explanation + visual hint (animations/highlights on workspace tangibles)
- **Heavy**: Full demonstration with visual animations and annotations

Follow the <remediation_system> documentation for error patterns, detection rules, and approved language templates.""",

    instructions="""
## YOUR TASK

Add error paths to these interaction sequences from the voice.json input:

<interaction_sequences>
{input}
</interaction_sequences>

For each step with a `correct_answer` field, add error paths to the existing `student_attempts`:
- **error_path_generic**: Generic fallback (REQUIRED - only error path to add for now)

The `success_path` already exists - DO NOT modify it.

**Note on Workspace Tangibles:** Tangibles may include a `visual_description` field (especially in comparison sets) that describes the visual characteristics of that specific tangible. This field helps maintain context about features like equal vs unequal spacing, segment sizes, etc.

## ERROR PATH REQUIREMENTS

**IMPORTANT DESIGN FLOW**: Events drive dialogue, not the other way around. Follow this process:

### STEP 1: Identify Remediation Strategy

For each step with `correct_answer`:
1. Understand what the student is being asked to do (check the `prompt` field)
2. Understand what the correct answer should be (check `correct_answer` field)
3. Consider what common errors might occur
4. Refer to <remediation_system> for appropriate scaffolding strategies

### STEP 2: Design Events for Each Scaffolding Level

**Event Levels:**
- **Light remediation**: Usually NO events (empty array [])
- **Medium remediation**: 1-2 events (subtle hints/guides)
- **Heavy remediation**: 2+ events (full demonstrations)

**Event Prefixes for Multiple Tangibles:**
The workspace may have multiple tangibles. Use appropriate event prefixes:
- Events with "A_" prefix operate on the FIRST/TOP tangible
- Events with "B_" prefix operate on the SECOND tangible
- Events with "C_" prefix operate on the THIRD tangible
- Events with "D_" prefix operate on the FOURTH tangible

Refer to <animation_events> documentation for available event names and their descriptions.

**Design Process:**
1. Look at the workspace to see what tangibles are available
2. Consult <remediation_system> to understand what remediation is pedagogically needed
3. Select appropriate events from <animation_events> that match the pedagogical need
4. Use the appropriate event prefixes (A_, B_, C_, D_) for the tangibles that need to be part of the remediation

**Example Event Selection:**
```json
"events": [
  {
    "name": "A_cut_hint_1_2",
    "description": "Show visual guide for cutting bar at 1/2 mark"
  }
]
```

### STEP 3: Design Dialogue Around Events with [event: name] Markers

**After selecting events**, write dialogue that integrates naturally with these animations and insert event markers at appropriate locations:

**Event Marker Format:** `[event: event_name]`

**Placement Guidelines:**
- Place [event: name] markers immediately before the noun/object being animated
- Pattern: "verb + [event: marker] + object"
- Multiple events use consecutive markers: `[event: A_cut_1_3][event: A_cut_2_3]`
- Events appear in logical pedagogical order

**Placement Examples:**
"Look at [event: C_pulse] this bar"
"Let's divide [event: A_cut_1_2] the line in half"
"Notice [event: A_measure] these sections"

**Examples by Level:**

1. **Light (no events)**: Simple redirect using <remediation_system> language templates
   ```json
   {
     "scaffolding_level": "light",
     "dialogue": "Not quite. Try dividing the bar into 2 equal parts.",
     "events": []
   }
   ```

2. **Medium (1-2 events)**: Insert markers before the object being animated
   ```json
   {
     "scaffolding_level": "medium",
     "dialogue": "Let's think about this together. To make two equal parts, we need to cut [event: A_cut_hint_1_2] the bar right in the middle.",
     "events": [
       {
         "name": "A_cut_hint_1_2",
         "description": "Show visual guide for cutting bar at 1/2 mark"
       }
     ]
   }
   ```

3. **Heavy (2+ events)**: Narrate events in pedagogical groups
   ```json
   {
     "scaffolding_level": "heavy",
     "dialogue": "Let me show you how to make sixths. First, let's divide [event: A_cut_1_2] the line in half. Now let's divide [event: A_cut_1_6][event: A_cut_2_6] the left half into thirds. And let's divide [event: A_cut_4_6][event: A_cut_5_6] the right half into thirds too. See how that creates 6 equal intervals?",
     "events": [
       {
         "name": "A_cut_1_2",
         "description": "Partition at 1/2 mark"
       },
       {
         "name": "A_cut_1_6",
         "description": "Make a cut at 1/6 mark"
       },
       {
         "name": "A_cut_2_6",
         "description": "Make a cut at 2/6 mark"
       },
       {
         "name": "A_cut_4_6",
         "description": "Make a cut at 4/6 mark"
       },
       {
         "name": "A_cut_5_6",
         "description": "Make a cut at 5/6 mark"
       }
     ]
   }
   ```

**Key Principles:**
- Insert [event: name] markers at the point where each animation should trigger
- Write dialogue that flows naturally with the animations
- Use <remediation_system> language templates and vocabulary guidelines
- Don't explicitly say "watch this animation" - describe the action naturally
- Group event markers to match the pedagogical sequence

### STEP 4: Keep Original Content Unchanged

- Don't modify existing fields (dialogue, prompt, workspace, correct_answer, success_path)
- Only ADD error_path_generic to student_attempts
- Preserve all [event:tags] that already exist in dialogue
- Maintain the exact same JSON structure

Return valid JSON only (see structure below).
""",

    doc_refs=[
        'remediation_system.md',
        'animation_events.json'
    ],

    output_structure="""
[
  {
    "interaction_id": 1,
    "interaction_name": "string",
    "fractions": [],
    "vocabulary_introduced": [],
    "steps": [
      {
        "dialogue": "existing dialogue",
        "prompt": "existing prompt",
        "interaction_tool": "cut|shade|select|etc",
        "workspace": [...existing workspace...],
        "correct_answer": {
          "value": "expected_value",
          "context": "explanation"
        },
        "student_attempts": {
          "success_path": {
            "dialogue": "existing success feedback"
          },
          "error_path_generic": {
            "steps": [
              {
                "scaffolding_level": "light",
                "dialogue": "Follow <remediation_system> for appropriate light dialogue",
                "events": []
              },
              {
                "scaffolding_level": "medium",
                "dialogue": "Follow <remediation_system> for appropriate medium dialogue with [event:name] markers",
                "events": [
                  {
                    "name": "A_hint_example",
                    "description": "Description of what this event does"
                  }
                ]
              },
              {
                "scaffolding_level": "heavy",
                "dialogue": "Follow <remediation_system> for appropriate heavy dialogue with [event:name] markers showing full demonstration",
                "events": [
                  {
                    "name": "A_demo_step1",
                    "description": "First demonstration step"
                  },
                  {
                    "name": "A_demo_step2",
                    "description": "Second demonstration step"
                  }
                ]
              }
            ]
          }
        }
      }
    ]
  }
]
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
