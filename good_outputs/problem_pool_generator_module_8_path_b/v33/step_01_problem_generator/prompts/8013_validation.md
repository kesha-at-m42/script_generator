# Validation Prompt for 8013

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
    "template_id": "8013",
    "problem_type": "Two-step problem: Student first selects equivalent bar, then verifies by placing both fractions on a number line",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Reference bar at top showing 1/2 (divided into halves with first half shaded). Three option bars below: Bar A shows 2/4 (divided into fourths with first two shaded), Bar B shows 3/6 (divided into sixths with first three shaded), Bar C shows 1/3 (divided into thirds with first third shaded). Step 2 (after correct selection): Two number lines stacked vertically, both 0-1 range. Top line has tick marks at 0, 1/2, 1 with point at 1/2. Bottom line has tick marks at 0, 1/4, 2/4, 3/4, 1 (unlabeled except endpoints).",
    "action_description": "Step 1: Student selects Bar A (2/4) as the equivalent fraction. Step 2: Student places point at 2/4 on bottom number line to verify it matches the 1/2 position.",
    "prompt": "Step 1: Which bar is equivalent to one half? Step 2: One half is marked on top. Place two fourths below to check.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "1/2",
        "2/4"
      ]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "8013",
    "problem_type": "Two-step problem: Student first selects equivalent bar, then verifies by placing both fractions on a number line",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Reference bar at top showing 2/4 (divided into fourths with first two shaded). Three option bars below: Bar A shows 1/2 (divided into halves with first half shaded), Bar B shows 2/6 (divided into sixths with first two shaded), Bar C shows 1/4 (divided into fourths with first fourth shaded). Step 2 (after correct selection): Two number lines stacked vertically, both 0-1 range. Top line has tick marks at 0, 1/4, 2/4, 3/4, 1 with point at 2/4. Bottom line has tick marks at 0, 1/2, 1 (unlabeled except endpoints).",
    "action_description": "Step 1: Student selects Bar A (1/2) as the equivalent fraction. Step 2: Student places point at 1/2 on bottom number line to verify it matches the 2/4 position.",
    "prompt": "First, find the equivalent bar. Then place it on a number line to compare positions.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "fractions": [
        "2/4",
        "1/2"
      ]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8013",
    "problem_type": "Two-step problem: Student first selects equivalent bar, then verifies by placing both fractions on a number line",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Reference bar at top showing 3/6 (divided into sixths with first three shaded). Three option bars below: Bar A shows 1/2 (divided into halves with first half shaded), Bar B shows 3/8 (divided into eighths with first three shaded), Bar C shows 2/4 (divided into fourths with first two shaded). Step 2 (after correct selection): Two number lines stacked vertically, both 0-1 range. Top line has tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1 with point at 3/6. Bottom line has tick marks at 0, 1/2, 1 (unlabeled except endpoints).",
    "action_description": "Step 1: Student selects Bar A (1/2) as the equivalent fraction. Step 2: Student places point at 1/2 on bottom number line to verify it matches the 3/6 position.",
    "prompt": "Select the matching bar, then place it below the reference to verify.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "3/6",
        "1/2"
      ]
    }
  },
  {
    "problem_instance_id": 4,
    "template_id": "8013",
    "problem_type": "Two-step problem: Student first selects equivalent bar, then verifies by placing both fractions on a number line",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Reference bar at top showing 1/2 (divided into halves with first half shaded). Three option bars below: Bar A shows 4/8 (divided into eighths with first four shaded), Bar B shows 3/6 (divided into sixths with first three shaded), Bar C shows 2/6 (divided into sixths with first two shaded). Step 2 (after correct selection): Two number lines stacked vertically, both 0-1 range. Top line has tick marks at 0, 1/2, 1 with point at 1/2. Bottom line has tick marks at 0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1 (unlabeled except endpoints).",
    "action_description": "Step 1: Student selects Bar A (4/8) as the equivalent fraction. Step 2: Student places point at 4/8 on bottom number line to verify it matches the 1/2 position.",
    "prompt": "Which bar equals two fourths? After you choose, place the equivalent on the bottom line.",
    "mastery_tier": "CHALLENGE",
    "variables_used": {
      "fractions": [
        "1/2",
        "4/8"
      ]
    }
  },
  {
    "problem_instance_id": 5,
    "template_id": "8013",
    "problem_type": "Two-step problem: Student first selects equivalent bar, then verifies by placing both fractions on a number line",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Reference bar at top showing 2/4 (divided into fourths with first two shaded). Three option bars below: Bar A shows 3/6 (divided into sixths with first three shaded), Bar B shows 4/8 (divided into eighths with first four shaded), Bar C shows 2/8 (divided into eighths with first two shaded). Step 2 (after correct selection): Two number lines stacked vertically, both 0-1 range. Top line has tick marks at 0, 1/4, 2/4, 3/4, 1 with point at 2/4. Bottom line has tick marks at 0, 1/6, 2/6, 3/6, 4/6, 5/6, 1 (unlabeled except endpoints).",
    "action_description": "Step 1: Student selects Bar A (3/6) as the equivalent fraction. Step 2: Student places point at 3/6 on bottom number line to verify it matches the 2/4 position.",
    "prompt": "Find the equivalent. Then show it lands at the same position as the reference.",
    "mastery_tier": "STRETCH",
    "variables_used": {
      "fractions": [
        "2/4",
        "3/6"
      ]
    }
  }
]