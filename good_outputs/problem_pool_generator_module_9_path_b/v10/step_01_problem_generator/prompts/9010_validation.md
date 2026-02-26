# Validation Prompt for 9010

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
    "template_id": "9010",
    "problem_type": "Student multi-selects all models (bars and number lines) that show fractions equivalent to target",
    "no_of_steps": 1,
    "workspace_description": "Reference: Bar showing 1/2 shaded (for comparison only). Options: Bar A showing 2/4 shaded, Bar B showing 1/3 shaded, Number Line C with labeled point at 4/8. All bars same size, line range 0-1.",
    "action_description": "Student selects Bar A (2/4 shaded) and Number Line C (point at 4/8) as both are equivalent to reference 1/2",
    "prompt": "Which models show fractions equivalent to 1/2? Click all that apply.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "reference_fractions": [
        "1/2"
      ],
      "equivalent_fractions": [
        "2/4",
        "4/8"
      ],
      "distractor_fractions": [
        "1/3"
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "9010",
    "problem_type": "Student multi-selects all models (bars and number lines) that show fractions equivalent to target",
    "no_of_steps": 1,
    "workspace_description": "Reference: Number Line with labeled point at 1/3 (for comparison only). Options: Bar A showing 1/4 shaded, Number Line B with labeled point at 2/6, Bar C showing 1/2 shaded. All bars same size, lines range 0-1.",
    "action_description": "Student selects Number Line B (point at 2/6) as the only equivalent to reference 1/3",
    "prompt": "Find all the models equal to 1/3. Select all correct ones.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "reference_fractions": [
        "1/3"
      ],
      "equivalent_fractions": [
        "2/6"
      ],
      "distractor_fractions": [
        "1/4",
        "1/2"
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "9010",
    "problem_type": "Student multi-selects all models (bars and number lines) that show fractions equivalent to target",
    "no_of_steps": 1,
    "workspace_description": "Reference: Bar showing 2/3 shaded (for comparison only). Options: Number Line A with labeled point at 4/6, Bar B showing 1/2 shaded, Number Line C with labeled point at 1/3. All bars same size, lines range 0-1.",
    "action_description": "Student selects Number Line A (point at 4/6) as the only equivalent to reference 2/3",
    "prompt": "Some are bars, some are lines. Which show 2/3?",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "reference_fractions": [
        "2/3"
      ],
      "equivalent_fractions": [
        "4/6"
      ],
      "distractor_fractions": [
        "1/2",
        "1/3"
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "9010",
    "problem_type": "Student multi-selects all models (bars and number lines) that show fractions equivalent to target",
    "no_of_steps": 1,
    "workspace_description": "Reference: Number Line with labeled point at 1/4 (for comparison only). Options: Bar A showing 2/8 shaded, Number Line B with labeled point at 1/2, Bar C showing 2/6 shaded. All bars same size, lines range 0-1.",
    "action_description": "Student selects Bar A (2/8 shaded) as the only equivalent to reference 1/4",
    "prompt": "Click every model that equals 1/4.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "reference_fractions": [
        "1/4"
      ],
      "equivalent_fractions": [
        "2/8"
      ],
      "distractor_fractions": [
        "1/2",
        "2/6"
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "9010",
    "problem_type": "Student multi-selects all models (bars and number lines) that show fractions equivalent to target",
    "no_of_steps": 1,
    "workspace_description": "Reference: Bar showing 1/2 shaded (for comparison only). Options: Number Line A with labeled point at 3/6, Bar B showing 1/3 shaded, Number Line C with labeled point at 1/4. All bars same size, lines range 0-1.",
    "action_description": "Student selects Number Line A (point at 3/6) as the only equivalent to reference 1/2",
    "prompt": "Find all the models equal to 1/2. Select all correct ones.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "reference_fractions": [
        "1/2"
      ],
      "equivalent_fractions": [
        "3/6"
      ],
      "distractor_fractions": [
        "1/3",
        "1/4"
      ]
    }
  }
]