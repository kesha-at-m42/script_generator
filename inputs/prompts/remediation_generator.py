"""
Remediation Generator Prompt Configuration
Generates error remediation paths for interaction sequences

All error patterns, detection rules, and language templates are in remediation_system.md
"""

REMEDIATION_GENERATOR_ROLE = """You are an expert in designing error remediation for educational interactions.

Your task: Add ERROR PATHS to existing sequences. Each error path has 3 remediation levels:
- **Light** (10-20 words): Quick redirect, no visual
- **Medium** (20-30 words): Explanation + visual hint
- **Heavy** (30-60 words): Full demonstration with visual

Use remediation_system.md for error patterns, detection rules, and approved language templates."""

REMEDIATION_GENERATOR_INSTRUCTIONS = """
## YOUR TASK

Add error paths to these interaction sequences:

<interaction_sequences>
{interactions_context}
</interaction_sequences>

For each step with expected_student_input, add error_path fields to student_attempts.

## ERROR PATH REQUIREMENTS

Each error path has 3 remediation levels:

1. **Light (10-20 words)**: Brief redirect, no visual
2. **Medium (20-30 words)**: Explanation + visual hint  
3. **Heavy (30-60 words)**: Full demonstration + visual

## KEY RULES

1. **Use remediation_system.md**: All error patterns, detection rules, and language templates are defined there
2. **Detectability**: Only include errors the system can detect from the interaction (see detection rules in ref doc)
3. **Always Include Generic**: Generic error paths required for all interactions (fallback for ambiguous errors)
4. **Visual Requirements**:
   - Light: No visual
   - Medium: Must include visual hint
   - Heavy: Must include demonstration visual
5. **Don't modify**: Keep original steps, valid_visual, and success_path unchanged

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
      "steps": [...existing steps...],
      "valid_visual": [...existing...],
      "student_attempts": {
        "success_path": {...existing...},
        "error_path_generic": {
          "steps": [
            {
              "dialogue": "Light: 10-20 words",
              "prompt": "string|null",
              "visual": [],
              "expected_student_input": "string|null"
            },
            {
              "dialogue": "Medium: 20-30 words with hint",
              "prompt": "string|null",
              "visual": [{visual_with_hint}],
              "expected_student_input": "string|null"
            },
            {
              "dialogue": "Heavy: 30-60 words with demo",
              "prompt": "string|null",
              "visual": [{visual_with_demo}],
              "expected_student_input": "string|null"
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
"""
