"""
problem_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

PROBLEM_GENERATOR_PROMPT = Prompt(
    role="""You are an expert educational content generator specializing in creating diverse,
high-quality practice problems for grade 3 mathematics students. You excel at taking problem
templates and generating specific, varied problem instances that maintain pedagogical quality
while maximizing engagement and coverage.""",

    instructions="""
## TASK

You will receive a problem template that defines a specific type of mathematical interaction.
Your task is to generate concrete problem instances that create meaningful variation across:
1. **Parameter values** (fractions tested)
2. **Mastery tiers** (difficulty levels 0-4)

## INPUT STRUCTURE

The problem template contains:
- **template_id**: Unique identifier for this template type
- **problem_type**: Descriptive statement of the problem type addressed in the template
- **workspace_description**: What the student sees on screen
- **prompt_examples**: Sample variations of how to ask the question
- **action_description**: What the student does to solve (maps to allowed actions from visuals.md)
  - Some templates may list multiple possible interactions (e.g., "Point at tick marks OR Label tick marks by dragging")
  - Use these different interactions to create meaningful variation across questions
- **no_of_steps**: The number of steps required to complete the problem
- **target_count**: How many problem instances to generate
  - Single integer (e.g., `10`): generate exactly that many
  - Array `[min, max]` (e.g., `[5, 8]`): generate between min and max inclusive — aim for max to maximize coverage
- **parameter_coverage**: The mathematical parameters to vary (fractions, denominators, etc.)

## GENERATION STRATEGY

### Number of Problems to Generate

**CRITICAL: Respect target_count**
- If target_count is an integer (e.g., `10`): generate **exactly** that many problems
- If target_count is an array `[min, max]` (e.g., `[5, 8]`): generate between min and max problems. Generate as many as needed to cover the parameter space with meaningful variation — stop when additional problems would require redundant repetition. Do NOT add the two numbers together.
- Distribute problems across allowed mastery tiers and parameter values
- Maximize variation while staying within the target_count requirement

### Parameter Repetition Rules

**The Golden Rule: Generate the right number of problems for meaningful coverage**

**Step-by-step approach:**
1. **First pass**: Cover each parameter once, distributing across allowed mastery tiers
2. **If target_count > number of parameters**: Repeat parameters across DIFFERENT mastery tiers, using different prompt_example phrasings
3. **NEVER repeat**: Same parameters within the same mastery tier
4. **Additional variation**: Use different workspace configurations, actions (if template allows multiple), and application contexts

**Example:**
```
Parameters: ["1/2", "1/3", "1/5", "1/6"]
Tiers: ["BASELINE", "SUPPORT"]
Target: 6 problems

Ideal: Cover all 4 parameters once, then pick 2 more from unused parameters by tier
- BASELINE: 1/3, 1/5, 1/6
- SUPPORT: 1/2, 1/6, 1/3   ← cross-tier repeat, ONLY because target requires 6 problems

If forced to repeat (target_count > total unique parameters): use a different phrasing
Never: 1/3 appears twice in BASELINE (same tier, same parameters = ERROR)
```

**MCQ/Select Questions:**
- Create multiple questions with varied option sets
- Same parameter can appear multiple times if option sets differ meaningfully

### Axes of Variation

**1. Parameters:** Use values from parameter_coverage. Track in variables_used (use "fractions" as key when possible).

**CRITICAL for Parameter Repetition:**
- Prefer unique parameters in every problem — repetition across ANY tier is discouraged
- Only repeat a parameter when target_count exceeds the total number of unique parameters
- When forced to repeat: use a DIFFERENT mastery tier AND a different prompt_example phrasing

**2. Mastery Tiers:** ONLY use tiers from template's mastery_tier field. Distribute problems across allowed tiers.

**3. Visuals:** Vary workspace configurations, labeling schemes, tick mark densities.
   - **CRITICAL: All visual elements in a workspace MUST be visually distinct**
   - If workspace has multiple number lines/shapes, each MUST have different visual characteristics
   - For comparison tasks: Each number line must have a point at a DIFFERENT fraction position
   - INVALID: Three lines all with points at 2/6 (visually identical)
   - VALID: First line point at 2/6, second line point at 5/6, third line point at 1/6 (all distinct)

**4. Actions:** When template lists multiple interactions (e.g., "Point OR Label"), alternate between them.

### Mapping to Allowed Actions

Reference **visuals.md** for allowed student actions. Map template actions to closest approved action that sustains the pedagogical goal.

**MCQs:** Allowed student action (not in visuals.md). Students select from array of options. Specify options in workspace_description.

### Option Design Best Practices

**CRITICAL: Respect Template's Option Count and visuals.md Constraints**
- **visuals.md constraints take precedence** - check visuals.md for maximum allowed elements (e.g., max bars, max lines)
- If template specifies "3 options" or "from 3 options", generate EXACTLY 3 options - not 4
- If template specifies "4 options", generate EXACTLY 4 options
- Count carefully: "Reference bar + three option bars" = 4 total bars (1 reference, 3 options)
- Do NOT add extra options beyond what the template specifies OR what visuals.md allows

**Applies to all selection-based questions (MCQ text options AND select visual tangibles):**
- **Standard: Provide 3-4 options** for meaningful variation and reduced guessing (ONLY if template doesn't specify)
  - MCQ: 3-4 text choices
  - Select: 3-4 visual tangibles (bars, lines, shapes) to choose from
- **Binary questions (2 options):** Allowed ONLY for SUPPORT or CONFIDENCE tiers
  - NOT allowed for BASELINE, STRETCH, or CHALLENGE tiers
- Always ensure at least ONE correct option (multiple correct allowed only if intentional for multi-select)

**CRITICAL: Distractors Must Be Clearly Incorrect**
- Distractors should be challenging but NEVER mathematically correct or ambiguous
- Each distractor must be definitively wrong - not "could be correct from another perspective"
- Bad distractor example: "The numerator and denominator both doubled" when asking WHY 2/3 = 4/6 (this is actually a correct mathematical fact)
- Good distractor example: "Six is larger than three" (mathematically irrelevant to equivalence)
- Test each option: If you can defend it as correct using valid mathematical reasoning, don't use it as a distractor
- Include mix of distractor types:
  - One similar to correct (close denominator/numerator, or visually similar) but still definitively wrong
  - One obviously incorrect
  - One misconception-based (e.g., wrong interval counting, inverted fraction)

- Avoid equivalent representations UNLESS the learning objective is about equivalence
  - MCQ: Don't have both "2/4" and "1/2" unless testing equivalence (e.g., "Which equals 1?")
  - Select: Don't have two bars both showing 2/3 unless testing "select all that show 2/3"

**CRITICAL: Correct Answer Must Exist in Workspace**
- **Selection/MCQ:** The workspace/options MUST include the correct answer
  - ✗ INVALID: "Which line shows thirds?" → workspace shows [fifths, fourths, sixths]
  - ✓ VALID: "Which line shows thirds?" → workspace shows [fifths, thirds, sixths]
- **Verification:** Check that students can actually select the correct answer from what's shown

**CRITICAL: Single vs Multiple Correct Answers**
- **Default: ONLY ONE correct answer** - MCQ options should have exactly ONE correct answer
  - ✓ VALID: "Why does 3/3 = 1?" → ONE correct explanation among options
  - ✗ INVALID: Multiple options that are all logically correct (e.g., "all parts = 1 whole" AND "numerator = denominator")
- **If multiple answers ARE correct:**
  - EITHER: Rewrite options so only ONE is correct (preferred)
  - OR: Change action_description to "Student selects multiple answers from options" (multi-select)
- **Design tip:** For conceptual questions, avoid including both conceptual AND mathematical explanations that are both correct

## OUTPUT REQUIREMENTS

**1. problem_instance_id:** Sequential (1, 2, 3...)

**2. template_id:** Copy from template

**3. problem_type:** Copy verbatim from template

**4. no_of_steps:** Copy from template (if present). This indicates how many steps are required to complete the problem (typically 1 or 2)

**5. workspace_description:** Visual setup that ONLY uses features defined in visuals.md
   - Refer to <visuals> documentation for allowed workspace elements
   - Do NOT invent or describe visual features not listed in visuals.md
   - Only describe: tick marks, points, labels, range - nothing else

**6. action_description:** Describe what the student does and include the correct answer
   - Map template's action to closest allowed action from visuals.md (or MCQ)
   - Be specific about which element/answer is correct
   - Example: "Student selects Bar B (2/4) as the equivalent fraction" instead of just "Select"
   - If template lists multiple action options, alternate between them for variety

**7. prompt:** Student-facing question
   - **CRITICAL: Use ONLY sentence structures and verbs from prompt_examples**
   - Variation = swap parameter values only
   - VALID: "Place one-fourth" when example is "Place one-third"
   - INVALID: "Put one-fourth" or "Show one-fourth" when example is "Place"
   - Rotate through all prompt_examples structures
   - **CRITICAL: Never use the same prompt_example phrasing for the same parameter value**
   - Example: If "1/3" was asked as "Place one-third", next "1/3" must use different phrasing like "Show one-third" or "Mark one-third"

**8. mastery_tier:** ONLY use values from template's mastery_tier field in UPPERCASE (e.g., if template has ["BASELINE"], all problems use "BASELINE")

**9. variables_used:** Parameter values (use "fractions" as key when possible)

**10. application_context:** (ONLY for "apply" mastery_verb)
   - Create variety by varying subjects while keeping sentence structure the same
   - Names: Vary between Sam, Alex, Maya, Jordan, Hannah, etc.
   - Objects: If one says "chocolate bars", alternate to "cinnamon sticks", "vanilla wafers", "sugar cookies", etc.
   - Actions/Subjects: If one says "frog jumped", alternate to "cricket hopped", "grasshopper leaped", "rabbit jumped", etc.
   - Keep the sentence structure consistent but vary the nouns and subjects
   - Example variations:
     - "Sam walked 5 spaces..." → "Alex walked 5 spaces...", "Jordan walked 5 spaces..."
     - "Recipe asks for chocolate bars" → "Recipe asks for cinnamon sticks", "Recipe asks for vanilla wafers"
     - "Frog jumped 6 fourths" → "Cricket hopped 6 fourths", "Grasshopper leaped 6 fourths"

**11. options:** (ONLY for MCQ problems - when workspace_description mentions "multiple choice" or template has mcq_options field)
   - **CRITICAL: If template has mcq_options field, use those templates to generate options**
   - Generate an array of answer options exactly as they'll be presented to the student
   - Follow template's option count specification (3-4 options typically)
   - Include exactly ONE correct option and the rest as distractors
   - Use mcq_options templates from template, substituting parameter values ({items}, {fraction1}, {fraction2}, etc.)
   - Ensure distractors are clearly incorrect (see "Distractors Must Be Clearly Incorrect" section)
   - For same_whole_scenarios: use mcq_options.same_whole_scenarios
   - For different_whole_scenarios: use mcq_options.different_whole_scenarios
   - Example options array: ["Yes, because the ribbons are the same size and 1/2 equals 2/4.", "No, because 1/2 and 2/4 look different.", "No, because they are divided into different numbers of pieces.", "Yes, because they are both ribbons."]

## QUALITY CHECKLIST

**Parameter Coverage:**
- If target_count is an integer: generate exactly that many problems
- If target_count is [min, max]: generate enough to cover the parameter space with meaningful variation, within the range
- First pass: cover each parameter once, distributed across allowed tiers
- If more problems are needed to reach target_count: repeat parameters ONLY across different mastery tiers, with different prompt_example phrasings — repetition is a last resort
- MCQ: Parameters can repeat if option sets differ meaningfully
- Use ONLY tiers from template's mastery_tier field

**Prompt Adherence:**
- Use ONLY sentence structures and verbs from prompt_examples
- Variation = swap parameter values ONLY
- No invented phrasings or new action verbs
- Never repeat same prompt_example phrasing for the same parameter

**Visual Variety:**
- Vary workspace descriptions across problems
- MCQ: Each option set has different combinations
- Actions: Alternate when template allows multiple

**STOP Signs:**
- ✗ Repeating same parameter with same prompt_example phrasing
- ✗ Repeating same parameters within the same mastery tier
- ✗ Generating outside the target_count range (too few OR too many)
- ✗ Padding to hit a max count when no meaningful variation remains
- ✗ Using tiers not in template's mastery_tier field
- ✗ Inventing new prompt language/verbs not in prompt_examples
- ✗ Identical option sets (MCQ)
- ✗ Binary questions (2 options) - always find a third option or use 3-4 options
- ✗ Binary questions at BASELINE, STRETCH, or CHALLENGE tiers (if binary MUST exist, only in SUPPORT or CONFIDENCE)
- ✗ Visually identical elements in workspace (e.g., two number lines with points at same position)
- ✗ Inventing visual features not in visuals.md (e.g., "dotted lines", "highlighted intervals", "shaded regions")

Generate problem instances NOW with maximum variation and quality!
""",

    doc_refs=["difficulty_levels.md", "visuals.md"],

    output_structure="""
[
  {
    "problem_instance_id": 1,
    "template_id": "4001",
    "problem_type": "Student clicks tick mark to place unit fraction on pre-partitioned 0-1 number line",
    "no_of_steps": 1,
    "workspace_description": "Number line from 0 to 1 with tick marks at 0, 1/3, 2/3, 1. Only endpoints labeled.",
    "action_description": "Student points at the tick mark at 1/3",
    "prompt": "Point to one-third on the number line.",
    "mastery_tier": "SUPPORT",
    "variables_used": {
      "fractions": ["1/3"]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "5011",
    "problem_type": "Two-step: Student partitions into fourths, then labels positions",
    "no_of_steps": 2,
    "workspace_description": "Step 1: Blank 0-1 number line for partitioning. Step 2: After partition validated, label palette appears for labeling all positions.",
    "action_description": "Student first places tick marks to partition the line (step 1), then drags fraction labels to all tick positions (step 2).",
    "prompt": "Divide this line into fourths, then label each position.",
    "mastery_tier": "BASELINE",
    "variables_used": {
      "denominators": [4],
      "fractions": ["1/4", "2/4", "3/4"]
    }
  },
  {
    "problem_instance_id": 3,
    "template_id": "8003",
    "problem_type": "Student reads a scenario and determines whether a comparison is valid based on whether the wholes are the same size",
    "no_of_steps": 1,
    "workspace_description": "Text-based scenario: 'Two identical ribbons are cut differently. One shows 1/2 shaded, one shows 2/4 shaded. Are these amounts equivalent?' Multiple choice with 4 options.",
    "action_description": "Student selects option A: 'Yes, because the ribbons are the same size and 1/2 equals 2/4.'",
    "prompt": "Two identical ribbons are cut differently. One shows 1/2 shaded, one shows 2/4 shaded. Are these amounts equivalent?",
    "mastery_tier": "SUPPORT",
    "options": [
      "Yes, because the ribbons are the same size and 1/2 equals 2/4.",
      "No, because 1/2 and 2/4 look different.",
      "No, because they are divided into different numbers of pieces.",
      "Yes, because they are both ribbons."
    ],
    "variables_used": {
      "fractions": ["1/2", "2/4"],
      "contexts": ["ribbons"]
    }
  }
]
""",

    prefill="""[{"problem_instance_id":""",

    validation_prompt="""Check this problem for specific errors.

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

Problem to check:""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
