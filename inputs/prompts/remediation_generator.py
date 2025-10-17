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

REMEDIATION_GENERATOR_INSTRUCTIONS = """
## YOUR TASK

Add error paths to these interaction sequences:

<interaction_sequences>
{interactions_context}
</interaction_sequences>

For each step with expected_student_input, add error paths to the existing student_attempts:
- **error_path_generic**: Generic fallback (always required)
- **error_path_[name]**: Specific detectable errors

The success_path already exists - DO NOT modify it.

## ERROR PATH REQUIREMENTS

Each error path has 3 remediation levels:

1. **Light (10-20 words)**: Brief redirect, no visual effects (visual = null)
2. **Medium (20-30 words)**: Explanation + visual hint effects (highlights, pulses, arrows on workspace tangibles)
3. **Heavy (30-60 words)**: Full demonstration with visual animations (measurements, overlays, step-by-step demos)

## KEY RULES

1. **Use remediation_system.md**: All error patterns, detection rules, and language templates are defined there
2. **Detectability**: Only include errors the system can detect from the interaction (see detection rules in ref doc)
3. **Always Include Generic**: Generic error paths required for all interactions (fallback for ambiguous errors)
4. **Scaffolding Level at Step Level**: Each remediation step must have scaffolding_level field at the top level:
   - "light": Brief redirect, visual = null
   - "medium": Explanation + hint, visual has highlight/pulse effects
   - "heavy": Full demo, visual has measurement/overlay animations
5. **Workspace Context vs Visual Effects**:
   - **workspace_context**: Metadata indicating which tangibles from main flow are present (for reference only)
   - **visual**: Dynamic effects/animations applied TO those tangibles (or null for light)
6. **Don't modify**: Keep original steps, valid_visual, and success_path unchanged (success_path already exists from interaction designer)
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
        },
        "error_path_specific_error": {
          "steps": [...]
        }
      }
    }
  ]
}

Notes:
- scaffolding_level = "light" | "medium" | "heavy" at step level (describes overall approach)
- workspace_context = Metadata indicating which tangibles from main flow are present
- visual = Dynamic effects/animations applied to those tangibles
- Light: visual is null (no dynamic changes)
- Medium: visual has hint effects (pulses, highlights, arrows)
- Heavy: visual has demonstration effects (measurements, overlays, comparisons)
"""
