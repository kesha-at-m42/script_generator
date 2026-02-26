# Validation Prompt for 8011

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
    "template_id": "8011",
    "problem_type": "Student identifies or verifies equivalence between fractions in the 2/3 family",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips of equal size shown side by side for comparison. Left strip divided into thirds with 2 sections shaded. Right strip divided into sixths with 4 sections shaded.",
    "action_description": "Student selects option A: 'Yes, because both bars show the same amount shaded even though they are divided differently.'",
    "prompt": "Are two thirds and four sixths equivalent? How can you tell?",
    "mastery_tier": "BASELINE",
    "options": [
      "Yes, because both bars show the same amount shaded even though they are divided differently.",
      "No, because thirds and sixths are different sizes.",
      "No, because one has 2 parts shaded and the other has 4 parts.",
      "Yes, because 2 plus 4 equals 6."
    ],
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "8011",
    "problem_type": "Student identifies or verifies equivalence between fractions in the 2/3 family",
    "no_of_steps": 1,
    "workspace_description": "Reference bar at top showing thirds with 1 section shaded (for comparison only). Below are three option bars of equal size: Bar A divided into sixths with 2 sections shaded, Bar B divided into sixths with 3 sections shaded, Bar C divided into sixths with 1 section shaded.",
    "action_description": "Student selects Bar A, which shows 2/6 (equivalent to the reference bar showing 1/3).",
    "prompt": "Which bar shows a fraction equivalent to one third?",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/3",
        "2/6"
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8011",
    "problem_type": "Student identifies or verifies equivalence between fractions in the 2/3 family",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips of equal size shown side by side for comparison. Left strip divided into thirds with 1 section shaded. Right strip divided into sixths with 2 sections shaded.",
    "action_description": "Student selects option C: 'Yes, because the shaded amounts cover the same length on both bars.'",
    "prompt": "Compare one third and two sixths. Are they equivalent?",
    "mastery_tier": "STRETCH",
    "options": [
      "No, because six is larger than three.",
      "No, because you can't compare fractions with different denominators.",
      "Yes, because the shaded amounts cover the same length on both bars.",
      "Yes, because one third is always equal to two of something."
    ],
    "variables_used": {
      "fractions": [
        "1/3",
        "2/6"
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "8011",
    "problem_type": "Student identifies or verifies equivalence between fractions in the 2/3 family",
    "no_of_steps": 1,
    "workspace_description": "Reference bar at top showing sixths with 4 sections shaded (for comparison only). Below are three option bars of equal size: Bar A divided into thirds with 1 section shaded, Bar B divided into thirds with 2 sections shaded, Bar C divided into sixths with 3 sections shaded.",
    "action_description": "Student selects Bar B, which shows 2/3 (equivalent to the reference bar showing 4/6).",
    "prompt": "Find the bar that equals four sixths.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "8011",
    "problem_type": "Student identifies or verifies equivalence between fractions in the 2/3 family",
    "no_of_steps": 1,
    "workspace_description": "Two fraction strips of equal size shown side by side for comparison. Left strip divided into thirds with 2 sections shaded. Right strip divided into sixths with 4 sections shaded.",
    "action_description": "Student selects option A: 'Yes, the shaded portions are equal in size.'",
    "prompt": "Do these two bars show the same amount?",
    "mastery_tier": "BASELINE",
    "options": [
      "Yes, the shaded portions are equal in size.",
      "No, because one bar has more sections than the other.",
      "No, because 2 and 4 are different numbers.",
      "Yes, because both bars are the same length."
    ],
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ]
    }
  }
]