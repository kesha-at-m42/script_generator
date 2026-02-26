# Validation Prompt for 11009

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
    "template_id": "11009",
    "problem_type": "Student views a fraction pair with the same numerator and selects two correct answers from four strategy options",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips: Bar A divided into sixths with 2 intervals shaded (showing 2/6), Bar B divided into fourths with 2 intervals shaded (showing 2/4). MathExpression shows: 2/6 < 2/4. Four multiple choice options displayed.",
    "action_description": "Student selects two options: 'Check for same numerator' and 'Compare the sizes of parts'",
    "prompt": "Which TWO can help you compare these fractions?",
    "mastery_tier": "BASELINE",
    "options": [
      "Check for same numerator",
      "Compare the sizes of parts",
      "Check for same denominator",
      "Count the equal parts"
    ],
    "variables_used": {
      "fractions": [
        "2/6",
        "2/4"
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "11009",
    "problem_type": "Student views a fraction pair with the same numerator and selects two correct answers from four strategy options",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips: Bar A divided into fifths with 3 intervals shaded (showing 3/5), Bar B divided into sevenths with 3 intervals shaded (showing 3/7). MathExpression shows: 3/5 > 3/7. Four multiple choice options displayed.",
    "action_description": "Student selects two options: 'Check for same numerator' and 'Compare the sizes of parts'",
    "prompt": "How would you compare these fractions? Select TWO options.",
    "mastery_tier": "BASELINE",
    "options": [
      "Check for same numerator",
      "Compare the sizes of parts",
      "Check for same denominator",
      "Count the total intervals"
    ],
    "variables_used": {
      "fractions": [
        "3/5",
        "3/7"
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "11009",
    "problem_type": "Student views a fraction pair with the same numerator and selects two correct answers from four strategy options",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips: Bar A divided into thirds with 2 intervals shaded (showing 2/3), Bar B divided into sixths with 2 intervals shaded (showing 2/6). MathExpression shows: 2/3 > 2/6. Four multiple choice options displayed.",
    "action_description": "Student selects two options: 'Check for same numerator' and 'Compare the sizes of parts'",
    "prompt": "Which TWO steps of the strategy apply here?",
    "mastery_tier": "STRETCH",
    "options": [
      "Check for same numerator",
      "Compare the sizes of parts",
      "Check for same denominator",
      "Add the denominators"
    ],
    "variables_used": {
      "fractions": [
        "2/3",
        "2/6"
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "11009",
    "problem_type": "Student views a fraction pair with the same numerator and selects two correct answers from four strategy options",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips: Bar A divided into fourths with 3 intervals shaded (showing 3/4), Bar B divided into ninths with 3 intervals shaded (showing 3/9). MathExpression shows: 3/4 > 3/9. Four multiple choice options displayed.",
    "action_description": "Student selects two options: 'Check for same numerator' and 'Compare the sizes of parts'",
    "prompt": "Which TWO can help you compare these fractions?",
    "mastery_tier": "STRETCH",
    "options": [
      "Check for same numerator",
      "Compare the sizes of parts",
      "Look at the denominators only",
      "Count how many pieces are shaded"
    ],
    "variables_used": {
      "fractions": [
        "3/4",
        "3/9"
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "11009",
    "problem_type": "Student views a fraction pair with the same numerator and selects two correct answers from four strategy options",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips: Bar A divided into sixths with 4 intervals shaded (showing 4/6), Bar B divided into tenths with 4 intervals shaded (showing 4/10). MathExpression shows: 4/6 > 4/10. Four multiple choice options displayed.",
    "action_description": "Student selects two options: 'Check for same numerator' and 'Compare the sizes of parts'",
    "prompt": "How would you compare these fractions? Select TWO options.",
    "mastery_tier": "BASELINE",
    "options": [
      "Check for same numerator",
      "Compare the sizes of parts",
      "Multiply the numerators",
      "Find the smaller denominator"
    ],
    "variables_used": {
      "fractions": [
        "4/6",
        "4/10"
      ]
    }
  }
]