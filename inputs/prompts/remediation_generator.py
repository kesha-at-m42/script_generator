"""
Remediation Generator Prompt Configuration
Generates error remediation paths for interaction sequences

All error patterns, detection rules, and language templates are in remediation_system.md
"""
# ============================================================================
# PROMPT COMPONENTS
# ============================================================================

REMEDIATION_GENERATOR_ROLE = """You are an expert in designing error remediation for educational interactions.

Your task: Add ERROR PATHS to existing sequences. Each error path has 3 remediation levels:
- **Light**: Quick redirect, no visual changes
- **Medium**: Explanation + visual hint (animations/highlights on workspace tangibles)
- **Heavy**: Full demonstration with visual animations and annotations

Follow the <remediation_system> documentation for error patterns, detection rules, and approved language templates."""

REMEDIATION_GENERATOR_DOCS = [
  "remediation_system.md",  # Language quidelines
 "remediation_events.json" # Event names and their visual animation descriptions
    ]

REMEDIATION_GENERATOR_TEMPLATE_REF = ["remediations_per_step"]

REMEDIATION_GENERATOR_EXAMPLES = []

REMEDIATION_GENERATOR_PREFILL = """{prefill_sequence}"""

REMEDIATION_GENERATOR_INSTRUCTIONS = """
## YOUR TASK

Add error paths to these interaction sequences:

<interaction_sequences>
{interactions_context}
</interaction_sequences>

For each step with expected_student_input, add error paths to the existing student_attempts:
- **error_path_generic**: Generic fallback (REQUIRED - only error path to add for now)

The success_path already exists - DO NOT modify it.
## ERROR PATH REQUIREMENTS

**IMPORTANT DESIGN FLOW**: Events drive dialogue, not the other way around. Follow this process:

### STEP 1: Extract Events from {remediations_per_step}

The {remediations_per_step} template field provides events IN ORDER for each scaffolding level. This is your authoritative guide.

For each remediation level:
1. Look up the events in {remediations_per_step} for the current scaffolding level (light/medium/heavy)
2. The events are listed IN THE ORDER they should occur
3. Find each event in <remediation_events> documentation to understand what it does
4. Build the events array using the EXACT event names and order from {remediations_per_step}:

```json
"events": [
  {
    "name": "A_cut_hint_1_2",
    "description": "Show visual guide for cutting bar at 1/2 mark"
  }
]
```

**Notes:**
- Light remediation: Usually NO events (empty array or not specified in {remediations_per_step})
- Medium remediation: 1-2 events (subtle hints/guides)
- Heavy remediation: 2+ events (full demonstrations)
- Use event names from {remediations_per_step} as a starting point
- Preserve the ORDER of events from {remediations_per_step}

**IMPORTANT - Adapting Events for Multiple Tangibles:**

The {remediations_per_step} provides baseline events, but you should adapt them based on what's pedagogically appropriate for the remediation:

**Event Prefixes for Multiple Tangibles:**
- Events with "A_" prefix operate on the FIRST/TOP bar
- Events with "B_" prefix operate on the SECOND bar
- Events with "C_" prefix operate on the THIRD bar
- Events with "D_" prefix operate on the FOURTH bar

**Design Process:**
1. Start with events from {remediations_per_step} (e.g., "A_compare")
2. Consult <remediation_system> to understand what remediation is pedagogically needed
3. Look at the workspace to see what tangibles are available
4. Use the appropriate event prefixes (A_, B_, C_, D_) for the tangibles that need to be part of the remediation

**Example:** If {remediations_per_step} suggests "A_compare" for medium remediation:
- **Scenario 1**: Student needs to understand one bar has equal parts → Use only "A_compare"
- **Scenario 2**: Student needs to compare two bars (one equal, one unequal) → Use "A_compare" and "B_compare"
- **Scenario 3**: Student selected wrong bar from 3 options → Use event for the correct bar (could be A_, B_, or C_)

**Key Principle:** Select events based on **what the student needs to learn**, not just how many tangibles exist. Refer to <remediation_system> for pedagogical guidance on error patterns and appropriate scaffolding.

### STEP 2: Design Dialogue Around Events with [event: name] Markers

**After extracting events from {remediations_per_step}**, write dialogue that integrates naturally with these animations and insert event markers at appropriate locations:

**Event Marker Format:** `[event: event_name]`

**Placement Guidelines:**
- Place the [event: name] marker RIGHT BEFORE the dialogue text that describes or references that animation
- The event triggers the animation, then the dialogue describes what's happening
- Multiple events should each have their own marker: `[event: A_cut_1_3][event: A_cut_2_3]`
- Events should appear in the SAME ORDER as listed in {remediations_per_step}

**Examples by Level:**

1. **Light (no events)**: Simple redirect using <remediation_system> language templates
   ```
   "dialogue": "Not quite. Try dividing the bar into 2 equal parts."
   ```

2. **Medium (1-2 events)**: Insert markers before describing the visual hints
   ```
   "events": [{"name": "A_cut_hint_1_2", "description": "Show visual guide for cutting bar at 1/2 mark"}]
   "dialogue": "Let's think about this together. To make two equal parts, we need to cut [event: A_cut_hint_1_2] right in the middle of the bar."
   ```

3. **Heavy (2+ events)**: Insert markers in order before describing each demonstration step
   ```
   "events": [
     {"name": "A_cut_1_2", "description": "Partition the bar in half (1/2)"}
   ]
   "dialogue": "Let me show you how to do this. To divide the bar into two equal parts, we need to cut [event: A_cut_1_2] right at the middle. See how this creates two parts that are exactly the same size?"
   ```

   **Multiple events example:**
   ```
   "events": [
     {"name": "A_cut_1_3", "description": "Make a cut at 1/3 mark"},
     {"name": "A_cut_2_3", "description": "Make a cut at 2/3 mark"}
   ]
   "dialogue": "Let me show you how to make three equal parts. To make thirds, we need to cut [event: A_cut_1_3][event: A_cut_2_3] at the one third mark and the two thirds mark. See how each part is exactly the same size?"
   ```

**Key Principles:**
- Follow the EVENT ORDER from {remediations_per_step} exactly
- Insert [event: name] markers at the point where each animation should trigger
- Write dialogue that flows naturally with the animations
- Use <remediation_system> language templates and vocabulary guidelines
- Don't explicitly say "watch this animation" - describe the action naturally

### STEP 3: Keep Original Content Unchanged

- Don't modify existing steps or success_path
- Only add error_path_generic to student_attempts

Return valid JSON only (see structure below).
"""

REMEDIATION_GENERATOR_STRUCTURE = """
{
  "sequences": [
    {
      "problem_id": 1,
      "difficulty": 0-4,
      "verb": "string",
      "goal": "string",
      "goal_id": 1,
      "fractions": [],
      "steps": [...existing steps with workspace tangibles...],
      "correct_answer": [...existing...],
      "student_attempts": {
        "success_path": {...existing...},
        "error_path_generic": {
          "steps": [
            {
              "scaffolding_level": "light",
              "dialogue": "Follow <remediation_system> for appropriate light dialogue",
              "events": [],
            },
            {
              "scaffolding_level": "medium",
              "dialogue": "Follow <remediation_system> for appropriate medium dialogue",
              "events":
                [
                    {
                      "target": "bar_a",
                      "type": "highlight",
                      "description": "Bar A sections pulse to draw attention"
                    }
                ]
                },
            },
            {
              "scaffolding_level": "heavy",
              "dialogue": "Follow <remediation_system> for appropriate heavy dialogue with modeling",
              "workspace_context": {
                "tangibles_present": ["bar_a", "bar_b", "button_choice_1"],
                "note": "Uses existing workspace from main flow"
              },
              "events": [
                  {
                    "target": "bar_a",
                    "type": "measurement",
                    "animation": "measure_sections_equal",
                    "description": "Animated overlay showing measurement lines confirming all sections are equal parts"
                  },
                  {
                    "target": "bar_b",
                    "type": "measurement",
                    "animation": "measure_sections_unequal",
                    "description": "Animated overlay showing measurement lines highlighting size differences"
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ]
}
"""
