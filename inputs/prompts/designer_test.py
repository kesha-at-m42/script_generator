"""
Designer Test Prompt - Example for experimentation and learning

This is a simplified prompt you can use to understand how the system works.
Feel free to modify any part of this to experiment!
"""

# =============================================================================
# ROLE - Define who Claude is and what expertise they have
# =============================================================================

DESIGNER_TEST_ROLE = """
You are a helpful assistant that transforms simple prompts into structured educational content.

Your task is to take a learning goal and create a simple question with feedback.
"""


# =============================================================================
# DOCUMENTATION - Reference materials to include (optional)
# =============================================================================

DESIGNER_TEST_DOCS = [
    # Add documentation files here if needed
    # Example: "<cognitive_types>"
]


# =============================================================================
# MODULE REFERENCES - Fields from modules.py to include (optional)
# =============================================================================

DESIGNER_TEST_MODULE_REF = [
    # Add module fields here if needed
    # Example: "vocabulary"
]


# =============================================================================
# EXAMPLES - Show Claude what good output looks like
# =============================================================================

DESIGNER_TEST_EXAMPLES = []


# =============================================================================
# INSTRUCTIONS - Tell Claude exactly what to do
# =============================================================================

DESIGNER_TEST_INSTRUCTIONS = """
## YOUR TASK

Transform the learning goal into a simple question with correct answer and feedback.

**Input Variables:**
- `{goal}`: The learning goal text
- `{goal_id}`: The goal ID number

**Output Format:**
Return a JSON object with:
- `test_id`: Use the goal_id
- `goal`: Copy the learning goal
- `question`: A simple question testing this goal
- `correct_answer`: The correct answer
- `feedback`: Encouraging feedback when correct

**Example Output:**
```json
{
  "test_items": [
    {
      "test_id": 1,
      "goal": "Students can identify colors",
      "question": "What color is the sky on a clear day?",
      "correct_answer": "blue",
      "feedback": "That's right! The sky is blue on a clear day."
    }
  ]
}
```

Return valid JSON only. No markdown, no explanation.
"""


# =============================================================================
# PREFILL - Guide Claude's response structure (optional)
# =============================================================================

DESIGNER_TEST_PREFILL = """{{
  "test_items": [
    {{
      "test_id": {goal_id},
      "goal": "{goal}","""


# =============================================================================
# NOTES FOR DESIGNERS
# =============================================================================

"""
HOW TO EXPERIMENT WITH THIS PROMPT:

1. ✅ SAFE TO CHANGE:
   - ROLE: Change the persona or expertise
   - INSTRUCTIONS: Add more guidance, change requirements
   - EXAMPLES: Add example inputs/outputs
   - PREFILL: Change the JSON structure

2. ⚠️ BE CAREFUL:
   - Variable names like {goal} and {goal_id} must match pipeline config
   - Keep PREFILL indentation consistent (2 spaces)
   - Use {{ and }} for literal braces in PREFILL

3. ❌ DON'T CHANGE:
   - The constant names (DESIGNER_TEST_ROLE, etc.)
   - The file structure

TO TEST YOUR CHANGES:
   python tests/designer_test_example.py
"""
