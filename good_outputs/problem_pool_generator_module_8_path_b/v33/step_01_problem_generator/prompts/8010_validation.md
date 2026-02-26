# Validation Prompt for 8010

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
    "template_id": "8010",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 2/3-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference fraction strip at top showing 2/3 (2 out of 3 sections shaded, labeled '2/3') marked as reference bar for comparison only. Below is an empty fraction strip partitioned into 6 equal sections (sixths), no sections shaded initially.",
    "action_description": "Student clicks on 4 sections of the bottom bar to shade them, creating 4/6 which equals 2/3.",
    "prompt": "Shade this bar to show a fraction equal to two thirds.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ],
      "reference_fraction": "2/3",
      "target_denominator": 6,
      "correct_shading": "4/6"
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "8010",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 2/3-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference fraction strip at top showing 1/3 (1 out of 3 sections shaded, labeled '1/3') marked as reference bar for comparison only. Below is an empty fraction strip partitioned into 6 equal sections (sixths), no sections shaded initially.",
    "action_description": "Student clicks on 2 sections of the bottom bar to shade them, creating 2/6 which equals 1/3.",
    "prompt": "The top bar shows one third. Shade the bottom bar to match that amount.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "1/3",
        "2/6"
      ],
      "reference_fraction": "1/3",
      "target_denominator": 6,
      "correct_shading": "2/6"
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8010",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 2/3-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference fraction strip at top showing 2/3 (2 out of 3 sections shaded, labeled '2/3') marked as reference bar for comparison only. Below is an empty fraction strip partitioned into 6 equal sections (sixths), no sections shaded initially.",
    "action_description": "Student clicks on 4 sections of the bottom bar to shade them, creating 4/6 which equals 2/3.",
    "prompt": "How many sixths equal two thirds? Shade to show.",
    "mastery_tier": "CHALLENGE",
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ],
      "reference_fraction": "2/3",
      "target_denominator": 6,
      "correct_shading": "4/6"
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "8010",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 2/3-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference fraction strip at top showing 1/3 (1 out of 3 sections shaded, labeled '1/3') marked as reference bar for comparison only. Below is an empty fraction strip partitioned into 6 equal sections (sixths), no sections shaded initially.",
    "action_description": "Student clicks on 2 sections of the bottom bar to shade them, creating 2/6 which equals 1/3.",
    "prompt": "Create a fraction equivalent to one third using sixths.",
    "mastery_tier": "CHALLENGE",
    "variables_used": {
      "fractions": [
        "1/3",
        "2/6"
      ],
      "reference_fraction": "1/3",
      "target_denominator": 6,
      "correct_shading": "2/6"
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "8010",
    "problem_type": "Student shades parts of a bar to create a fraction equivalent to a 2/3-family reference",
    "no_of_steps": 1,
    "workspace_description": "Reference fraction strip at top showing 2/3 (2 out of 3 sections shaded, labeled '2/3') marked as reference bar for comparison only. Below is an empty fraction strip partitioned into 6 equal sections (sixths), no sections shaded initially.",
    "action_description": "Student clicks on 4 sections of the bottom bar to shade them, creating 4/6 which equals 2/3.",
    "prompt": "Each third splits into two sixths. Shade to show two thirds.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "2/3",
        "4/6"
      ],
      "reference_fraction": "2/3",
      "target_denominator": 6,
      "correct_shading": "4/6"
    }
  }
]