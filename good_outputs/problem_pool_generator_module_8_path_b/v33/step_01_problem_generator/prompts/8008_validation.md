# Validation Prompt for 8008

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
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 1/2 with tick marks at 0, 1/2, 1. Bottom line has tick marks at 0, 1/4, 2/4, 3/4, 1 for student interaction.",
    "action_description": "Student places a point at 2/4 on the bottom number line, which aligns with the 1/2 reference point on the top line.",
    "prompt": "Place two fourths on the line. Where does it land compared to one half?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/2",
        "2/4"
      ],
      "denominators": [
        2,
        4
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 2/3 with tick marks at 0, 1/3, 2/3, 1. Bottom line has tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1 for student interaction.",
    "action_description": "Student places a point at 4/6 on the bottom number line, which aligns with the 2/3 reference point on the top line.",
    "prompt": "Place four sixths on the line. Where does it land compared to two thirds?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ],
      "denominators": [
        3,
        6
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 1/3 with tick marks at 0, 1/3, 2/3, 1. Bottom line has tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1 for student interaction.",
    "action_description": "Student places a point at 2/6 on the bottom number line, which aligns with the 1/3 reference point on the top line.",
    "prompt": "Show where two sixths goes.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/3",
        "2/6"
      ],
      "denominators": [
        3,
        6
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 1/2 with tick marks at 0, 1/2, 1. Bottom line has tick marks at 0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1 for student interaction.",
    "action_description": "Student places a point at 4/8 on the bottom number line, which aligns with the 1/2 reference point on the top line.",
    "prompt": "Place the marker at four eighths.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/2",
        "4/8"
      ],
      "denominators": [
        2,
        8
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 2/6 with tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1. Bottom line has tick marks at 0, 1/3, 2/3, 1 for student interaction.",
    "action_description": "Student places a point at 1/3 on the bottom number line, which aligns with the 2/6 reference point on the top line.",
    "prompt": "Put one third on the number line. Is it at the same spot as two sixths?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/6",
        "1/3"
      ],
      "denominators": [
        6,
        3
      ]
    }
  },
  {
    "problem_instance_id": 6,
    "template_id": "8008",
    "problem_type": "Student places varied fractions on a number line to verify equivalence with a marked reference point",
    "no_of_steps": 1,
    "workspace_description": "Two number lines stacked vertically, both ranging from 0 to 1. Top line (reference, non-interactable) has a labeled point at 2/3 with tick marks at 0, 1/3, 2/3, 1. Bottom line has tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1 for student interaction.",
    "action_description": "Student places a point at 3/6 on the bottom number line, which aligns with the 2/3 reference point on the top line. Note: This is different from problem 2 which used 4/6 with the same prompt structure.",
    "prompt": "Find where three sixths belongs.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "2/3",
        "3/6"
      ],
      "denominators": [
        3,
        6
      ]
    }
  }
]