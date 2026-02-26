# Validation Prompt for 8009

## System Message (Cached: True)

Check this problem for specific errors.

CRITICAL: Think through each check internally first. Only include something in the "errors" array if you are CERTAIN it is wrong after completing your analysis. If you determine something is correct during your reasoning, do NOT report it as an error.

Run these checks:

**CHECK 1: MCQ Single-Select Must Have Only One Correct Option**
- If action_description mentions "selects one" or "clicks one" AND workspace has options/choices
- Count how many options are correct answers to the prompt question
- If count > 1 → ERROR: "MCQ single-select has {count} correct options: {list them}"

**CHECK 2: MCQ Option Count**
- If workspace has options/choices, count them
- If count = 2 AND mastery_tier is BASELINE/STRETCH/CHALLENGE → ERROR: "Binary MCQ (2 options) only allowed for SUPPORT/CONFIDENCE tiers"
- If count < 2 → ERROR: "MCQ needs at least 2 options"

**CHECK 3: Answer Must Exist in Workspace**
- If prompt asks for specific fraction/element, verify it exists in workspace_description
- If MCQ, verify correct answer option exists in the workspace
- If not found → ERROR: "Answer '{value}' not found in workspace"

**CHECK 4: Action Description Quality**
- If action_description is too vague ("Select", "Point", "Click") without details → ERROR: "Action description too vague, must specify what student does"
- Action description must match what workspace allows

**CHECK 5: Prompt is Solvable**
- Student must be able to answer using only the workspace
- If prompt requires information not in workspace → ERROR: "Prompt requires information not in workspace"

**CHECK 6: Multi-Select Equivalent Fractions Must All Be Equivalent to Each Other**
- If action_description mentions "selects ALL" or "select all" AND problem involves equivalent fractions
- Parse all fractions mentioned in action_description as correct answers
- Verify ALL correct answer fractions are equivalent to EACH OTHER (not just paired off)
- If there are 2+ separate groups → ERROR: "Multi-select has {count} separate equivalence groups: {list groups}. All correct answers must be equivalent to each other."

**CHECK 7: MCQ Options Field Must Exist**
- If workspace_description mentions "multiple choice" OR template has mcq_options field
- Verify "options" field exists in problem JSON
- If missing → ERROR: "MCQ problem missing 'options' field"
- If options array is empty or has < 2 items → ERROR: "MCQ options array must have at least 2 options"

**CHECK 8: MCQ Correct Answer Must Match Action Description**
- If problem has "options" field, parse which option is correct from action_description
- Verify that exact option text exists in the options array
- If mismatch → ERROR: "Action description references option that doesn't exist in options array"

Return JSON:
{
  "valid": true/false,
  "errors": ["error1", "error2"],
  "warnings": []
}

Problem to check:

## Expected Response Schema

```json
{
  "valid": true,  // or false
  "errors": ["error1", "error2"],  // empty if valid
  "warnings": []  // optional
}
```

## User Input (Content to Validate)

[
  {
    "problem_instance_id": 1,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 1/2 (one of two equal parts shaded). Empty fraction strip below divided into 4 equal parts (fourths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 2 parts of the bottom bar to shade them, creating 2/4 which equals 1/2",
    "prompt": "Shade this bar to show a fraction equal to one half.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/2",
        "2/4"
      ],
      "reference_fraction": "1/2",
      "target_denominator": 4,
      "correct_shading": "2/4"
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 2/4 (two of four equal parts shaded). Empty fraction strip below divided into 6 equal parts (sixths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 3 parts of the bottom bar to shade them, creating 3/6 which equals 2/4",
    "prompt": "The top bar shows two fourths. Shade the bottom bar to match that amount.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/4",
        "3/6"
      ],
      "reference_fraction": "2/4",
      "target_denominator": 6,
      "correct_shading": "3/6"
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 1/2 (one of two equal parts shaded). Empty fraction strip below divided into 8 equal parts (eighths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 4 parts of the bottom bar to shade them, creating 4/8 which equals 1/2",
    "prompt": "How many eighths equal one half? Shade to show.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/2",
        "4/8"
      ],
      "reference_fraction": "1/2",
      "target_denominator": 8,
      "correct_shading": "4/8"
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 3/6 (three of six equal parts shaded). Empty fraction strip below divided into 4 equal parts (fourths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 2 parts of the bottom bar to shade them, creating 2/4 which equals 3/6",
    "prompt": "Create a fraction equivalent to three sixths.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "3/6",
        "2/4"
      ],
      "reference_fraction": "3/6",
      "target_denominator": 4,
      "correct_shading": "2/4"
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 2/4 (two of four equal parts shaded). Empty fraction strip below divided into 8 equal parts (eighths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 4 parts of the bottom bar to shade them, creating 4/8 which equals 2/4",
    "prompt": "Shade parts to make the same amount as two fourths.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/4",
        "4/8"
      ],
      "reference_fraction": "2/4",
      "target_denominator": 8,
      "correct_shading": "4/8"
    }
  },
  {
    "problem_instance_id": 6,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 3/6 (three of six equal parts shaded). Empty fraction strip below divided into 8 equal parts (eighths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 4 parts of the bottom bar to shade them, creating 4/8 which equals 3/6",
    "prompt": "The top bar shows three sixths. Shade the bottom bar to match that amount.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "3/6",
        "4/8"
      ],
      "reference_fraction": "3/6",
      "target_denominator": 8,
      "correct_shading": "4/8"
    }
  },
  {
    "problem_instance_id": 7,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 1/2 (one of two equal parts shaded). Empty fraction strip below divided into 6 equal parts (sixths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 3 parts of the bottom bar to shade them, creating 3/6 which equals 1/2",
    "prompt": "How many sixths equal one half? Shade to show.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/2",
        "3/6"
      ],
      "reference_fraction": "1/2",
      "target_denominator": 6,
      "correct_shading": "3/6"
    }
  },
  {
    "problem_instance_id": 8,
    "template_id": "8009",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 1/2-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference bar on top showing 2/4 (two of four equal parts shaded). Empty fraction strip below divided into 6 equal parts (sixths). Student shades parts of bottom bar to match the amount.",
    "action_description": "Student clicks 3 parts of the bottom bar to shade them, creating 3/6 which equals 2/4",
    "prompt": "Create a fraction equivalent to two fourths.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/4",
        "3/6"
      ],
      "reference_fraction": "2/4",
      "target_denominator": 6,
      "correct_shading": "3/6"
    }
  }
]