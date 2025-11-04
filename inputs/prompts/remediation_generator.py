"""
Remediation Generator Prompt Configuration
Generates error remediation paths for interaction sequences

All error patterns, detection rules, and language templates are in remediation_system.md
"""

# ============================================================================
# STANDARDIZED PROMPT CONFIG
# See PROMPT_STRUCTURE.md for documentation
# ============================================================================

REMEDIATION_GENERATOR_CONFIG = {
    "input_file": "interactions.json",           # From interaction_designer step
    "input_variable": "interactions_context",    # Variable name in template
    "docs": [
        "remediation_system.md",                 # Error patterns, detection rules, language templates
        "visual_guide.md"                        # Visual scaffolds and animation types
    ],
    "module_ref": [],                            # No module fields needed
    "role": "REMEDIATION_GENERATOR_ROLE",        # Defined below
    "instructions": "REMEDIATION_GENERATOR_INSTRUCTIONS",  # Defined below
    "structure": "REMEDIATION_GENERATOR_STRUCTURE",        # Defined below
    "examples": "REMEDIATION_GENERATOR_EXAMPLES",          # Defined below
    "prefill": "REMEDIATION_GENERATOR_PREFILL"             # Defined below
}

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

1. **Follow <remediation_system> documentation** for ALL remediation guidance:
   - Language templates and dialogue patterns
   - Visual effect specifications
   - Progressive scaffolding strategies

2. **Follow <visual_guide> documentation** for visual effects and animations

3. **Workspace Context vs Visual Effects**:
   - **workspace_context**: Metadata indicating which tangibles from main flow are present (for reference only)
   - **visual**: Dynamic effects/animations applied TO those tangibles (or null for light)

4. **Don't modify**: Keep original steps and success_path unchanged (success_path already exists from interaction designer)

5. **Reference existing workspace**: Don't redefine tangibles; use workspace_context to indicate which ones from main flow are present

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
      "valid_visual": [...existing...],
      "student_attempts": {
        "success_path": {...existing...},
        "error_path_generic": {
          "steps": [
            {
              "scaffolding_level": "light",
              "dialogue": "Follow <remediation_system> for appropriate light dialogue",
              "workspace_context": {
                "tangibles_present": ["bar_a", "bar_b", "button_choice_1"],
                "note": "Uses existing workspace from main flow"
              },
              "visual": null,
            },
            {
              "scaffolding_level": "medium",
              "dialogue": "Follow <remediation_system> for appropriate medium dialogue",
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
              "dialogue": "Follow <remediation_system> for appropriate heavy dialogue with modeling",
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
