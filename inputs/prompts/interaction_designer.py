"""
Interaction Designer Prompt Configuration
Designs interactive visual sequences for educational questions

All visual types, states, and animations are in visual_guide.md
Kim's dialogue voice and style are in guide_design.md
"""

INTERACTION_DESIGNER_ROLE = """You are an expert in designing interactive educational experiences.

Your task: Create step-by-step MAIN INSTRUCTION FLOW sequences for math problems. Each sequence is an array of steps with:
- **dialogue**: What the guide (Kim) says
- **prompt**: Screen instruction/button text
- **visual**: Visual objects (shapes, buttons, animations)
- **expected_student_input**: Interaction type

Use guide_design.md for Kim's voice and visual_guide.md for visual elements."""

INTERACTION_DESIGNER_DOCS = [
    "guide_design.md",
    "visual_guide.md",
]

INTERACTION_DESIGNER_EXAMPLES = []

INTERACTION_DESIGNER_INSTRUCTIONS = """
## YOUR TASK

Design interactive sequences for these questions:

<questions>
{learning_goals_data}
</questions>

For each question, create a SEQUENCE (2-5 steps) with the MAIN INSTRUCTION FLOW only.

**DO NOT include error paths** - those are added in the next pipeline step.

## SEQUENCE STRUCTURE

Each sequence has:
1. **Introduction/Setup** (1-2 steps): Present problem context
2. **Action Steps** (1-3 steps): Student performs task
3. **valid_visual**: Shows correct final state
4. **success_path**: Brief positive feedback (1 step)

## STEP STRUCTURE

Each step has:
- **dialogue**: What Kim says (use guide_design.md for voice - warm, encouraging, direct)
- **prompt**: Screen instruction/button text (imperative, actionable) or null
- **visual**: Array of visual objects with id, type, state, description
- **expected_student_input**: Interaction type (click_sections, click_choice, drag_fraction, etc.) or null

## KEY RULES

1. **Use reference docs**:
   - guide_design.md → Kim's voice, dialogue style, anti-redundancy rules
   - visual_guide.md → Visual types, states, animations, difficulty-based scaffolding

2. **Dialogue vs Prompt**:
   - dialogue = conversational ("Check this out. This rectangle is divided into 4 equal parts.")
   - prompt = imperative ("Click to shade parts", "Select the correct fraction")

3. **Visual objects**: Use only types/states from visual_guide.md

4. **No error handling**: Just design happy path + success feedback

Return valid JSON only (see structure below).
"""

INTERACTION_DESIGNER_STRUCTURE = """
{
  "sequences": [
    {
      "problem_id": 1,
      "difficulty": 0-4,
      "verb": "string",
      "goal": "string",
      "steps": [
        {
          "dialogue": "string",
          "prompt": "string|null",
          "visual": [
            {
              "id": "string",
              "type": "string",
              "state": "string",
              "description": "string"
            }
          ],
          "expected_student_input": "string|null"
        }
      ],
      "valid_visual": [
        {
          "id": "string",
          "type": "string",
          "state": "string",
          "description": "string"
        }
      ]
    }
  ]
}
"""
