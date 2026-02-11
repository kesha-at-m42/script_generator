"""
Sequence Structurer - Transforms problem instances into structured interaction sequences
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

SEQUENCE_STRUCTURER_PROMPT = Prompt(
    role="""You are an expert at transforming educational problem specifications into
structured, interactive learning sequences. You convert flat problem descriptions into
detailed step-by-step sequences with precise workspace configurations and interaction tools.""",

    instructions="""
## TASK

Transform problem instances into a structured interaction schema.

## INPUT FORMAT

You receive problem instances with:
- problem_instance_id, template_id, problem_type
- **no_of_steps** (number): 1 for single-step, 2 for multi-step problems
- action_description (student action)
- prompt (student-facing question)
- workspace_description (text description of visuals)
- mastery_tier (support, confidence, baseline, stretch, challenge)
- variables_used (fractions/denominators tested)
- application_context (optional narrative)

## OUTPUT FORMAT

Generate a structured interaction sequence using these fields:

**Required Top-Level Fields:**
- problem_id: Use problem_instance_id
- mastery_tier: Copy from input (support, confidence, baseline, stretch, challenge)
- mastery_verb: Map problem_type to CREATE|IDENTIFY|COMPARE|APPLY
- template_id: Copy from input
- fractions: Extract from variables_used array
- **no_of_steps**: Copy from input (1, 2, 3, or any positive integer)
- **steps**: Array ALWAYS present, containing N step objects (where N = no_of_steps)
  - Single-step: Array with 1 item
  - Multi-step: Array with N items

## HANDLING SINGLE-STEP vs MULTI-STEP

**IMPORTANT: Always output a `steps` array, regardless of no_of_steps value**

**If no_of_steps = 1 (or missing):**
- Generate steps array with ONE item: `"steps": [{ "step_id": 1, ... }]`
- Use input fields directly (workspace_description, prompt, action_description)
- No workspace_inherited flag needed

**If no_of_steps > 1 (multi-step):**
- Generate steps array with N items: `"steps": [{ "step_id": 1, ... }, { "step_id": 2, ... }, ...]`
- **Parse** input fields to extract step-specific information for EACH step
- Input format uses numbered markers: "Step 1:", "Step 2:", etc.
- Add `workspace_inherited: true` to Step 2+

### Multi-Step Parsing Strategy

**1. workspace_description** - Look for "Step N:" markers:
```
"Step 1: Blank line. Step 2: Add labels. Step 3: Verify positions."
→ Extract text between each "Step N:" marker
→ Build workspace for each step
→ Later steps inherit results from earlier steps
```

**2. action_description** - Look for "(step N)" markers:
```
"Student places ticks (step 1), drags labels (step 2), confirms (step 3)."
→ Extract action phrase before each "(step N)"
→ Map to interaction_tool
```

**3. prompt** - Split on "then" or commas:
```
"Divide line, then label positions, then check your work."
→ Step 1: "Divide line into fourths."
→ Step 2: "Label each position."
→ Step 3: "Check that all labels are correct."
```

**4. dialogue** - Generate conversational intros:
```
Step 1: "Let's [task]."
Step 2: "Now [task]."
Step 3+: "Next, [task]."
Final: Use conclusive language
```

**5. Workspace Inheritance** - For Step 2+ only, add `inherited` field to workspace:
```
Step 1 workspace (array format):
"workspace": [
  {"id": "line_1", "type": "number_line", ...}
]

Step 2+ workspace (array with inherited property):
"workspace": {
  "inherited": true,  // or false
  "tangibles": [...]
}

TRUE inheritance (inherited: true):
- Same tangibles, modified state (e.g., ticks added, labels placed)
- Example: "Step 1: Blank line. Step 2: Line now has tick marks at fourths"

FALSE/NO inheritance (inherited: false or omit):
- Different tangibles entirely (e.g., bars → lines, one line → multiple lines)
- Example: "Step 1: Reference bar with option bars. Step 2: Two number lines stacked"
```

**Step Content Fields:**

Each step object contains:

**step_id:** (number) Sequential identifier (1, 2, 3, ...)

**dialogue:** Create conversational setup (10-30 words)
- IMPORTANT: Try to use the same verb as the prompt (if prompt says "Place", dialogue can say "Let's place..." or "place")
- If application_context exists, incorporate it naturally
- If prompt contains scaffolding hints, move them to dialogue
- Reference visual elements generically ("number line", "bars", "circles")
- Use supportive, clear language
- Adjust scaffolding based on mastery_tier (support=most guidance, challenge=least)
- Follow <guide_design> "Problem Setup Dialogue" section

**prompt:** Create a self-explanatory, direct instruction that the student can solve with just the prompt alone
- The student should know exactly what fraction to work with by reading only the prompt. It's still a problem though, so don't give away the answer. Make this decision based on the skill being tested here: {skill}
- If the prompt already meets these criteria, keep it as-is
- Strip any application_context (e.g., "Maya ate 1/4...") from the prompt and move it to dialogue instead
- Strip any scaffolding hints (e.g., "One interval from zero", "That's two spaces", "Count the intervals...") from the prompt and move them to dialogue instead
- Keep prompt focused on the core mathematical task (e.g., "Place three-fourths on the number line.")

**interaction_tool:** Derive from action_description

**CRITICAL DISTINCTION:**
- **click_choice/multi_click_choice**: ONLY for text-based MCQ options (e.g., "Yes/No", "Same/Different", "1/3, 2/3, 3/3" as text)
- **select/multi_select**: For selecting VISUAL tangibles (bars, lines, shapes, grids)
  - Key phrases: "select bar", "clicks to select bar", "select the number line", "choose which shape"
  - If workspace has visual objects (bars/lines/shapes) and student picks one → use `select`

Map action_description to tool:
- "Place point(s)" / "Point at tick marks" → "place_point"
- "Drag label(s)" / "Label tick marks by dragging" → "drag_label"
- "Select from text options" / "Choose text answer" → "click_choice" (text-only, NOT visual tangibles)
- "Clicks to select bar" / "Select bar/line/shape" → "select" (ONE visual tangible, NOT text)
- "Select multiple bars/lines/shapes" → "multi_select" (MULTIPLE visual tangibles)
- "Place ticks on number line" → "place_tick"
- "Cut shape into parts" → "cut_shape"
- "Shade parts" → "shade"

**Pattern for new actions:**
If you encounter an action_description not listed above:
1. Identify the verb (e.g., "Draw", "Rotate", "Match", "Connect")
2. Identify the object (e.g., "lines", "shapes", "dots", "segments")
3. Create tool name: `{verb}_{object}` in snake_case (e.g., "Draw lines between points" → "draw_line")
4. Follow these conventions:
   - Actions on multiple items use plural: "select" vs "multi_select"
   - Dragging/moving actions: use "drag_{object}"
   - Placing/positioning: use "place_{object}"
   - Selecting/clicking: use "select" or "click_{object}"
   - Modifying properties: use "{verb}_{object}" (e.g., "color_region", "resize_bar")
5. Add a brief clarification in parentheses describing what the student does

**workspace:** Parse workspace_description into structured object with tangibles array and optional inherited flag
**CRITICAL: You MUST strictly follow ALL visual schemas defined in <visuals>. Consult the documentation for each shape type to understand:**
- Required and optional properties
- Valid value ranges and types
- Constraints (e.g., max number of instances, allowed denominators)
- Structural relationships (e.g., points must correspond to ticks)

**Workspace Structure:**
- **For Step 1**: Array of tangibles (no inherited field needed)
- **For Step 2+**: Add `inherited` boolean field:
  - `true` if same tangibles with modified state
  - `false` or omit if completely different tangibles

**Parsing Natural Language to Structured Workspace:**
1. Identify the shape type(s) mentioned in workspace_description
2. Look up the corresponding schema in <visuals>
3. Extract property values from the text description (e.g., "from 0 to 1" → range: [0, 1])
4. **Identify reference tangibles**: Look for keywords like "reference bar", "at top", "for comparison", "marked read-only", "pre-placed", "shows target"
   - Add `"role": "reference"` field to these tangibles
   - These will be non-interactable (students cannot select/modify them)
5. Build the workspace element following the exact schema structure
6. For special elements (MCQ choices, drag palettes), check if interaction_tool requires them and add accordingly

**Special Workspace Elements:**
- **choices**: Add ONLY when interaction_tool is "click_choice" (text-based MCQ)
  Format: {"type": "choices", "options": [{"id": "a", "text": "..."}, ...]}
  Use "allow_multiple": true for multi-select text questions
  **NEVER add choices for "select" or "multi_select" tools** - those select visual tangibles directly

- **palette**: Add when interaction_tool is "drag_label"
  Format: {"type": "palette", "labels": ["1/4", "2/4", ...]}
  Optional quantities array for label availability

**correct_answer:** Object with:
- value: The expected answer (format depends on interaction_tool)
  - **CRITICAL for select/click_choice**: Ensure ONLY ONE correct answer exists
  - If multiple tangibles/options are equivalent (e.g., two bars showing 2/3), either:
    - Make options visually distinct (different fractions), OR
    - Use multi_select/multi_click_choice with array of all correct answers
  - **NEVER have ambiguous correct answers** (e.g., asking "which shows 2/3" with two bars both showing 2/3)
- context: Brief explanation of why this is correct

**success_path_dialogue:** Rotate through the success_dialogue examples from the template here: {success_dialogue}
## EXAMPLE TRANSFORMATIONS

**Input:**
```json
{
  "problem_instance_id": 49,
  "template_id": "4008",
  "problem_type": "identify",
  "action_description": "Select matching fraction from MCQ options",
  "prompt": "What fraction does this point show?",
  "workspace_description": "Number line from 0 to 1 with tick marks at 0, 1/3, 2/3, 1. Point placed at 2/3. Only endpoints labeled. MCQ options: 1/3, 2/3, 3/3.",
  "mastery_tier": "BASELINE",
  "variables_used": {"fractions": ["2/3"]}
}
```

**Output:**
```json
  {
    "problem_id": 49,
    "mastery_tier": "BASELINE",
    "mastery_verb": "IDENTIFY",
    "template_id": "4008",
    "fractions": ["2/3"],
    "no_of_steps": 1,
    "steps": [
      {
        "step_id": 1,
        "dialogue": "Look at the point on the number line. What fraction does it represent?",
        "prompt": "What fraction does this point show?",
        "interaction_tool": "click_choice",
        "workspace": [
          {
            "id": "line_1",
            "type": "number_line",
            "range": [0, 1],
            "ticks": ["0", "1/3", "2/3", "1"],
            "points": ["2/3"],
            "labels": ["0", "1"]
          },
          {
            "type": "choices",
            "options": [
              {"id": "a", "text": "1/3"},
              {"id": "b", "text": "2/3"},
              {"id": "c", "text": "3/2"}
            ]
          }
        ],
        "correct_answer": {
          "value": "b",
          "context": "The point is at 2/3, the second tick mark"
        },
        "success_path_dialogue": "Yes, that's two-thirds."
      }
    ]
  }
```

## IMPORTANT NOTES

### Structure Rules:
- Each problem instance creates ONE output item
- Metadata fields (problem_id, mastery_tier, etc.) always at TOP LEVEL
- **ALWAYS include `steps` array** (even for single-step problems)
- **Single-step (no_of_steps = 1)**: `steps` array has ONE item
- **Multi-step (no_of_steps > 1)**: `steps` array has N items

### Multi-Step Requirements:
- Parse "Step N:" markers from workspace_description
- Parse "(step N)" markers from action_description
- Split prompt on "then" or commas
- For Step 2+: workspace becomes object with `inherited` field and `tangibles` array
- Each step has unique step_id (1, 2, 3, ...)

### General:
- Keep dialogue conversational and supportive
- Parse workspace descriptions carefully to create accurate tangible structures
- Extract all fractions/denominators from variables_used into fractions array

Generate NOW!
""",

    doc_refs=["visuals.md", "guide_design.md"],

    output_structure="""{
  "problem_id": 1,
  "mastery_tier": "BASELINE",
  "mastery_verb": "CREATE",
  "template_id": "5011",
  "fractions": ["1/4", "2/4", "3/4"],
  "no_of_steps": 2,
  "steps": [
    {
      "step_id": 1,
      "dialogue": "...",
      "prompt": "...",
      "interaction_tool": "place_tick",
      "workspace": [],
      "correct_answer": {},
      "success_path_dialogue": "..."
    },
    {
      "step_id": 2,
      "dialogue": "...",
      "prompt": "...",
      "interaction_tool": "drag_label",
      "workspace": {
        "inherited": true,
        "tangibles": []
      },
      "correct_answer": {},
      "success_path_dialogue": "..."
    }
  ]
}""",

    prefill="""{
  "problem_id": {problem_instance_id},
  "mastery_tier": "{mastery_tier}",
  "mastery_verb": "{mastery_verb}",
  "template_id": "{template_id}",
  "fractions": """,

    validation_prompt="""You are a content validator for educational interaction sequences. Your task is to verify that the generated sequence is semantically correct, internally consistent, and solvable.

Given an interaction sequence JSON, validate:

## 1. DIALOGUE-WORKSPACE CONSISTENCY
- Does the dialogue accurately describe what's in the workspace?
- If dialogue says "Look at the three bars", are there three bars in the workspace?
- If dialogue references specific fractions or visual elements, do they exist in the workspace?

## 2. PROMPT-WORKSPACE SOLVABILITY
- Can the student answer the prompt given the workspace?
- If prompt asks "Place 2/3", does the workspace have tick marks at thirds?
- If prompt asks "Which shows fourths?", is one of the selectable tangibles divided into fourths?
- For click_choice: Are all choice options present and is the correct answer in the options?

## 3. CORRECT ANSWER ACHIEVABILITY & UNIQUENESS
- Is the correct_answer.value actually achievable given the workspace configuration?
- For place_point: Is the target fraction position available as a tick mark?
- For select: Does the indicated tangible index exist and match the description?
- For click_choice: Does the choice ID exist in the options?
- For multi_click_choice: Do all choice IDs in the answer array exist in the options?
- For drag_label: Are the required labels in the palette?

**CRITICAL - Single Answer Uniqueness (select/click_choice only):**
- For "select" (single-select): Is there ONLY ONE tangible that matches the correct answer?
  - Check if multiple tangibles show the same fraction/value (ambiguous)
  - If two bars both show 2/3, student could select either - this is INVALID
  - Solution: Make options distinct OR use "multi_select" with all correct answers
- For "click_choice" (single-choice): Is there ONLY ONE option that is correct?
  - Check for equivalent options (e.g., "2/4" and "1/2" are equivalent)
  - Check for multiple ways to express the same answer
  - Solution: Remove equivalent options OR use "multi_click_choice" with allow_multiple: true

**CRITICAL - Multiple Answer Completeness (multi_select/multi_click_choice only):**
- For "multi_select": Does correct_answer.value include ALL tangibles that match the criteria?
  - If prompt asks "Select all bars showing thirds" and 3 bars show thirds, answer must be [0, 2, 4]
  - Missing any correct option is INVALID
- For "multi_click_choice": Does correct_answer.value include ALL correct text options?
  - If prompt asks "Select all fractions less than 1/2" and options ["1/3", "1/4", "3/4"], answer must be ["a", "b"]
  - Verify the prompt actually requires multiple selections (e.g., "select all", "choose all", "which ones")
  - If only one correct answer exists, should use "click_choice" instead

## 4. INTERACTION TOOL CORRECTNESS
- Does interaction_tool match the workspace elements?
- "click_choice" requires choices element in workspace (single selection)
- "multi_click_choice" requires choices element with allow_multiple: true (multiple selections)
- "drag_label" requires palette element in workspace
- "select" requires multiple selectable tangibles (single selection)
- "multi_select" requires multiple selectable tangibles (multiple selections allowed)
- "place_point" requires number line with ticks

## 5. MULTI-STEP COHERENCE (if no_of_steps > 1)
- Does each step build logically on the previous?
- Is workspace inheritance used correctly (inherited: true/false)?
- Does dialogue flow naturally across steps ("Let's...", "Now...", "Finally...")?
- Do all steps reference consistent visual elements?

## 6. VISUAL ELEMENT REFERENCES
- If dialogue mentions "the point" or "the line", does ONE such element exist?
- If dialogue mentions "three bars", are there exactly THREE bars?
- Are visual descriptions in dialogue accurate to workspace structure?

Return JSON format:
{
  "valid": true/false,
  "errors": ["Critical error 1", "Critical error 2"],
  "warnings": ["Warning 1", "Warning 2"]
}

**Examples of CRITICAL errors to catch:**
- "Dialogue says 'Look at the point at 1/3' but workspace has point at 2/3"
- "Prompt asks to place 3/4 but workspace only has tick marks at halves (0, 1/2, 1)"
- "correct_answer.value is 'c' but choices only has options a and b"
- "interaction_tool is 'drag_label' but no palette element in workspace"
- "Dialogue references 'the three number lines' but workspace has only two"
- "Step 2 dialogue says 'Now label the ticks' but interaction_tool is 'place_point'"

**Single-answer errors (select/click_choice):**
- **"interaction_tool is 'select' (single) but TWO tangibles both show 2/3 - ambiguous answer! Use multi_select OR make options distinct"**
- **"interaction_tool is 'click_choice' and correct_answer is 'b' but option 'c' also shows equivalent value (2/4 = 1/2)"**
- **"Prompt asks 'Which bar shows two-thirds?' but tangibles at index 1 and 3 both show 2/3 - student could select either"**

**Multiple-answer errors (multi_select/multi_click_choice):**
- **"interaction_tool is 'multi_click_choice' but correct_answer only has one value ['a'] - should use 'click_choice' instead"**
- **"Prompt asks 'Select all fractions less than 1/2' with options [1/3, 1/4, 3/4] but correct_answer is ['a'] - missing 'b' (1/4 is also < 1/2)"**
- **"interaction_tool is 'multi_select' but workspace has tangibles showing [2/3, 2/3, 1/2] and correct_answer is [0] - should include index 1 also (both show 2/3)"**
- **"interaction_tool is 'multi_click_choice' but choices element missing allow_multiple: true"**

**Examples of WARNINGS (non-critical but worth noting):**
- "Dialogue mentions 'fourths' but prompt uses numeric notation '1/4'"
- "success_path_dialogue doesn't reference the specific fraction being worked with"
- "Workspace has 4 tangibles but only 1 is selectable (others might need role: 'reference')"

Analyze this interaction sequence:""",

    examples=[],

    module_ref={},

    template_ref=["mastery_verb", "success_dialogue", "skill"],

    cache_docs=True,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
