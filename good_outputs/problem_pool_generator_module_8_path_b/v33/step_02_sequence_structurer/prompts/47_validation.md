# Validation Prompt for 47

## System Message (Cached: True)

Check this sequence for specific errors.

CRITICAL INSTRUCTIONS:
- For each check, FIRST write out your reasoning and analysis
- THEN determine if it's a pass or fail based on that reasoning
- Only add to "errors" array if you conclude it FAILED after analysis
- If your reasoning shows it PASSED, do NOT add it to errors
- Be mathematically consistent: 1/3 = 2/6, 2/4 = 1/2, 3/6 = 1/2 (these are facts, don't flip-flop)
- If original answer is mathematically correct, do NOT flag it as error

**IMPORTANT - Understanding Metadata vs Workspace:**
- Top-level fields like "fractions", "template_id", "mastery_tier" are METADATA - they describe what's being tested and the learning goal
- These metadata fields are NOT part of the student workspace and are NOT selectable options
- ONLY validate the actual workspace content (workspace.tangibles, workspace[0].options, etc.) - these are what students interact with
- Use metadata only to understand context (e.g., "fractions": ["1/2", "3/6"] tells you the problem tests equivalence between 1/2 and 3/6)
- Example: If prompt asks "Which equals 1/2?" and workspace has options ["2/6", "3/6", "4/6"], then only those 3 options are selectable - even if metadata "fractions" lists ["1/2", "3/6"]

**IMPORTANT - Using Tangible Descriptions:**
- Each tangible has a "description" field that clearly states what it shows
- **Use the description field as the primary source for understanding what fraction a tangible represents**
- Examples:
  - description: "Bar showing 2/4 shaded" → represents 2/4 (which equals 1/2)
  - description: "Number line with point at 1/2" → represents 1/2
  - description: "Fraction bar showing 1/2 shaded" → represents 1/2
- When checking if options are correct, compare the fractions in descriptions against the target fraction
- Only fall back to calculating from intervals/intervals_is_shaded if description is missing or unclear

Run these checks:

**CHECK 1: Tool/Answer Format**
- Single-select tool ("select", "click_choice") must have single answer, not array
- Multi-select tool ("multi_select", "multi_click_choice") must have array answer with 2+ items
- Error if mismatch: "Tool '{tool}' format doesn't match answer format"

**CHECK 2: Single-Select Correctness** (skip if multi-select tool)
- Count correct options in workspace (ignore top-level "fractions" metadata)
- Use tangible descriptions to understand what each shows
- Check mathematical equivalence: 1/2 = 2/4 = 3/6, etc.
- If multiple correct options exist → ERROR: "Single-select has {count} correct options: {ids}"

**CHECK 3: Multi-Select Completeness** (skip if single-select tool)
- Find all mathematically correct options in workspace
- Use tangible descriptions to understand what each shows
- Answer must include ALL correct options, no extras
- If incomplete → ERROR: "Missing correct option: {id}" or "Incorrect option included: {id}"

**CHECK 4: Answer Achievable**
- Verify answer IDs/values exist in workspace
- For ticks: check for exact match OR equivalent fraction
- Example: answer "2" is valid if ticks contains "2" OR "8/4" OR "6/3"
- Error if not found: "Answer '{value}' not in workspace"

**CHECK 5: Index Bounds**
- For intervals_is_shaded arrays: verify all indices < total sections
- Example: intervals="1/4" has 4 sections, valid indices are 0-3
- Error if out of bounds: "{id}: index {idx} > max {max}"

**CHECK 6: Language Match**
- Multi-select: use plural ("bars", "ALL")
- Single-select: use singular ("bar", "the")
- Error if mismatch: "Tool is {type} but language is {wrong}"

Return JSON:
{
  "valid": true/false,
  "errors": ["error1", "error2"],
  "warnings": []
}

Sequence to check:

## Expected Response Schema

```json
{
  "valid": true,  // or false
  "errors": ["error1", "error2"],  // empty if valid
  "warnings": []  // optional
}
```

## User Input (Content to Validate)

{
  "problem_id": 47,
  "mastery_tier": "STRETCH",
  "mastery_verb": "create",
  "template_id": "8009",
  "fractions": [
    "1/2",
    "4/8"
  ],
  "no_of_steps": 1,
  "steps": [
    {
      "step_id": 1,
      "dialogue": "Look at the top bar. It shows one half. Shade the bottom bar to show the same amount.",
      "prompt": "How many eighths equal one half? Shade to show.",
      "interaction_tool": "shade",
      "workspace": [
        {
          "id": "bar_reference",
          "type": "fraction_strip",
          "role": "reference",
          "description": "Reference bar showing 1/2 shaded",
          "range": [
            0,
            1
          ],
          "intervals": "1/2",
          "intervals_is_shaded": [
            0
          ]
        },
        {
          "id": "bar_target",
          "type": "fraction_strip",
          "role": "student_interaction",
          "description": "Empty fraction strip divided into eighths",
          "range": [
            0,
            1
          ],
          "intervals": "1/8",
          "intervals_is_shaded": false
        }
      ],
      "correct_answer": {
        "value": [
          0,
          1,
          2,
          3
        ],
        "context": "Four eighths equals one half - same amount as the reference bar"
      },
      "success_path_dialogue": "You made it. Four eighths equals one half."
    }
  ]
}