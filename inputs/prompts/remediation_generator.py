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
For each scaffolding level (light, medium, heavy), generate appropriate "dialogue" and "events" based on the following guidelines:

1. **Follow {remediations_per_step} and refer to the <remediation_events> documentation** to understand the visual scaffolds that will appear on screen at each remediation level. Use this create an array of "events" for medium and heavy remediation levels.
  **Reference existing workspace**: Don't redefine tangibles; use the workspace field to understand what is present on the screen.
        "events":
          [
            {
              "name": from {remediation_per_step} matching the scaffolding_level,
              "target": from workspace,
              "description": from <remediation_events> documentation
            },
            {
              "name": from {remediation_per_step} matching the scaffolding_level,
              "target": from workspace,
              "description": from <remediation_events> documentation
            }
          ]
  

2. **Progressing from step 1, use the "events" generate corresponding and matching "dialogue". Refer <remediation_system> documentation**, especially for the language guidance.

3. **Don't modify**: Keep original steps and success_path unchanged (success_path already exists from interaction designer)

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
