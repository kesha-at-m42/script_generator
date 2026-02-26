# Validation Prompt for 10010

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

**CHECK 9: No Duplicate Problems in This Batch**
- This check applies to the FULL array of problems, not just one problem
- For each pair of problems, extract their parameter values by flattening all values in `variables_used` into a sorted list
- ERROR: Two problems share the same `mastery_tier` AND same `variables_used` values → ERROR: "Duplicate parameters in problems #ID1 and #ID2: same tier ({tier}), same parameters ({params})"

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
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 2/6 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 2/6 (top) and 5/6 (bottom). MathExpression shows '2/6 ? 5/6' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 2/6 on the top number line to place a point. Step 2: Student clicks the tick mark at 5/6 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Place two-sixths on the top line. Step 2: Now place five-sixths on the bottom line. Step 3: Which symbol correctly compares these fractions?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/6",
        "5/6"
      ],
      "denominators": [
        6
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 2/7 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 2/7 (top) and 4/7 (bottom). MathExpression shows '2/7 ? 4/7' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 2/7 on the top number line to place a point. Step 2: Student clicks the tick mark at 4/7 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Mark two-sevenths on the top number line. Step 2: Mark four-sevenths on the bottom line. Step 3: Select the correct symbol.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/7",
        "4/7"
      ],
      "denominators": [
        7
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 3/8 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 3/8 (top) and 5/8 (bottom). MathExpression shows '3/8 ? 5/8' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 3/8 on the top number line to place a point. Step 2: Student clicks the tick mark at 5/8 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Place three-eighths on the top line. Step 2: Place five-eighths on the bottom line. Step 3: Which symbol makes this comparison true?",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "3/8",
        "5/8"
      ],
      "denominators": [
        8
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/4, 2/4, 3/4, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 1/4 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 1/4 (top) and 3/4 (bottom). MathExpression shows '1/4 ? 3/4' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 1/4 on the top number line to place a point. Step 2: Student clicks the tick mark at 3/4 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Place one-fourth on the top line. Step 2: Now place three-fourths on the bottom line. Step 3: Which symbol correctly compares these fractions?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/4",
        "3/4"
      ],
      "denominators": [
        4
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 1/6 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 1/6 (top) and 4/6 (bottom). MathExpression shows '1/6 ? 4/6' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 1/6 on the top number line to place a point. Step 2: Student clicks the tick mark at 4/6 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Mark one-sixth on the top number line. Step 2: Mark four-sixths on the bottom line. Step 3: Select the correct symbol.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/6",
        "4/6"
      ],
      "denominators": [
        6
      ]
    }
  },
  {
    "problem_instance_id": 6,
    "template_id": "10010",
    "problem_type": "Student places a point on each of two stacked number lines (one fraction each), then selects the correct comparison symbol",
    "no_of_steps": 3,
    "workspace_description": "Three sequential workspaces. Step 1: Two number lines visible, both 0-1 range with tick marks at 0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1. Endpoints labeled. Top line is active (student places point). Bottom line is read-only reference with no point yet. Step 2: Top line is now read-only showing placed point at 1/8 from Step 1. Bottom line becomes active (student places point). Step 3: Both lines read-only with points at 1/8 (top) and 6/8 (bottom). MathExpression shows '1/8 ? 6/8' with symbol placeholder. Three symbol choices: <, =, >.",
    "action_description": "Step 1: Student clicks the tick mark at 1/8 on the top number line to place a point. Step 2: Student clicks the tick mark at 6/8 on the bottom number line to place a point. Step 3: Student clicks the < symbol from three choices.",
    "prompt": "Step 1: Place one-eighth on the top line. Step 2: Place six-eighths on the bottom line. Step 3: Which symbol makes this comparison true?",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/8",
        "6/8"
      ],
      "denominators": [
        8
      ]
    }
  }
]