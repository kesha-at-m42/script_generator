"""
Remediation Generator Prompt Configuration
Generates error remediation paths for interaction sequences

All error patterns, detection rules, and language templates are in remediation_system.md
"""

REMEDIATION_GENERATOR_ROLE = """You are an expert in designing error remediation for educational interactions.

Your task: Add ERROR PATHS to existing sequences. Each error path has 3 remediation levels:
- **Light** (10-20 words): Quick redirect, no visual changes
- **Medium** (20-30 words): Explanation + visual hint (animations/highlights on workspace tangibles)
- **Heavy** (30-60 words): Full demonstration with visual animations and annotations

Use remediation_system.md for error patterns, detection rules, and approved language templates."""

REMEDIATION_GENERATOR_DOCS = [
  "remediation_system.md",  # Error patterns, detection rules, language templates
  "visual_guide.md"         # Visual scaffolds and animation types
]

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

1. **ALWAYS consult remediation_system.md**: 
   - For approved language templates at each scaffolding level
   - For scaffolding progression strategies
   - For dialogue tone and student support approaches
   
2. **ALWAYS consult visual_guide.md**:
   - For available visual effect types (highlight, pulse, arrow, measurement, overlay, demonstration)
   - For animation specifications and tangible interactions
   - For visual scaffolding best practices

3. **Scaffolding Level at Step Level**: Each remediation step must have scaffolding_level field at the top level:
   - "light": Brief redirect following remediation_system.md templates, visual = null
   - "medium": Explanation + hint following remediation_system.md patterns, visual has effects from visual_guide.md
   - "heavy": Full demo following remediation_system.md teaching strategies, visual has animations from visual_guide.md

5. **Workspace Context vs Visual Effects**:
   - **workspace_context**: Metadata indicating which tangibles from main flow are present (for reference only)
   - **visual**: Dynamic effects/animations applied TO those tangibles per visual_guide.md (or null for light)

6. **Don't modify**: Keep original steps and success_path unchanged (success_path already exists from interaction designer)

7. **Reference existing workspace**: Don't redefine tangibles; use workspace_context to indicate which ones from main flow are present

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
      "fractions_covered": [],
      "steps": [...existing steps with workspace tangibles...],
      "valid_visual": [...existing...],
      "student_attempts": {
        "success_path": {...existing...},
        "error_path_generic": {
          "steps": [
            {
              "scaffolding_level": "light",
              "dialogue": "Light: 10-20 words",
              "workspace_context": {
                "tangibles_present": ["bar_a", "bar_b", "button_choice_1"],
                "note": "Uses existing workspace from main flow"
              },
              "visual": null,
            },
            {
              "scaffolding_level": "medium",
              "dialogue": "Medium: 20-30 words with hint",
              "workspace_context": {
                "tangibles_present": ["bar_a", "bar_b", "button_choice_1"],
                "note": "Uses existing workspace from main flow"
              },
              "visual": {
                "effects": [
                  {
                    "target": "bar_a",
                    "type": "highlight",
                    "animation": "pulse",
                    "description": "Bar A sections pulse to draw attention"
                  }
                ]
              },
            },
            {
              "scaffolding_level": "heavy",
              "dialogue": "Heavy: 30-60 words with demo",
              "workspace_context": {
                "tangibles_present": ["bar_a", "bar_b", "button_choice_1"],
                "note": "Uses existing workspace from main flow"
              },
              "visual": {
                "effects": [
                  {
                    "target": "bar_a",
                    "type": "measurement",
                    "animation": "measure_sections_equal",
                    "description": "Animated overlay showing measurement lines confirming all sections are equal width"
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
