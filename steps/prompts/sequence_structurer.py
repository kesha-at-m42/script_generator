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

**5. Workspace Setup** - Default is always fresh; inherit only when explicitly stated:
```
DEFAULT — all steps (fresh workspace, array format):
"workspace": [
  {"id": "line_1", "type": "number_line", ...}
]

EXCEPTION — inherited workspace (object format):
"workspace": {
  "inherited": true,
  "tangibles": [...]
}
```

**Decision rule:**

TRUE inheritance (`inherited: true`) — ONLY when workspace_description EXPLICITLY says "same workspace" for that step (e.g., "Step 2: Same workspace as Step 1"):
- Use the object format with `inherited: true`
- Still describe the full tangible state as it appears entering this step

DEFAULT (everything else) — always re-describe the workspace fully as an array:
- Each step gets a complete, fresh workspace array
- Re-describe every tangible with its exact state for that step (active/read-only, points placed, labels shown, etc.)
- Example: "Step 2: Top line read-only with point at 2/7. Bottom line active." → fresh array, not inherited

**For ALL Step 2+ workspaces (inherited or fresh):** Map the previous step's correct_answer result onto the relevant tangible — the workspace must reflect what the student completed in the prior step (e.g., if Step 1's correct_answer placed a point at 2/7, the Step 2 workspace shows that tangible with `"points": ["2/7"]` already present)

**Step Content Fields:**

Each step object contains:

**step_id:** (number) Sequential identifier (1, 2, 3, ...)

**dialogue:** Create conversational setup (10-30 words)
- IMPORTANT: Try to use the same verb as the prompt (if prompt says "Place", dialogue can say "Let's place..." or "place")
- If application_context exists, incorporate it naturally
- If prompt contains scaffolding hints, move them to dialogue
- Reference visual elements generically ("number line", "bars", "circles")
- **CRITICAL - Singular vs Plural**: Use plural language if multiple correct answers exist
  - Multiple correct answers → "Which bars show..." (not "Which bar shows...")
  - Single correct answer → "Which bar shows..." (not "Which bars show...")
- Use supportive, clear language
- Adjust scaffolding based on mastery_tier (support=most guidance, challenge=least)
- Follow <guide_design> "Problem Setup Dialogue" section

**prompt:** Create a self-explanatory, direct instruction that the student can solve with just the prompt alone
- The student should know exactly what fraction to work with by reading only the prompt. It's still a problem though, so don't give away the answer. Make this decision based on the skill being tested here: {skill}
- If the prompt already meets these criteria, keep it as-is
- Strip any application_context (e.g., "Maya ate 1/4...") from the prompt and move it to dialogue instead
- Strip any scaffolding hints (e.g., "One interval from zero", "That's two spaces", "Count the intervals...") from the prompt and move them to dialogue instead
- **CRITICAL - Singular vs Plural**: Use plural language if multiple correct answers exist
  - Multiple correct answers → "Select ALL bars that..." (not "Select the bar that...")
  - Single correct answer → "Select the bar that..." (not "Select ALL bars")
- Keep prompt focused on the core mathematical task (e.g., "Place three-fourths on the number line.")

**interaction_tool:** Derive from action_description

**CRITICAL DISTINCTION:**
- **click_choice/multi_click_choice**: ONLY for text-based MCQ options (e.g., "Yes/No", "Same/Different", "1/3, 2/3, 3/3" as text)
- **select/multi_select**: For selecting VISUAL tangibles (bars, lines, shapes, grids)
  - Key phrases: "select bar", "clicks to select bar", "select the number line", "choose which shape"
  - If workspace has visual objects (bars/lines/shapes) and student picks one → use `select`

**CRITICAL: Single vs Multi Selection Tools:**
- **Before choosing tool**: Check how many correct answers exist in the workspace
- **Multiple correct answers** (e.g., two bars both show equivalent fractions):
  - Use "multi_select" or "multi_click_choice"
  - Dialogue and prompt should already use plural language (see sections above)
- **Single correct answer**:
  - Use "select" or "click_choice"
  - Dialogue and prompt should use singular language
- **Example ERROR**: workspace has bar_a (3/6) and bar_b (1/2), both equivalent to 2/4
  - WRONG: tool="select", dialogue="Which bar shows...", prompt="Select the equivalent bar", answer=["bar_a", "bar_b"]
  - RIGHT: tool="multi_select", dialogue="Which bars show...", prompt="Select ALL equivalent bars", answer=["bar_a", "bar_b"]

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
- **ONLY use fields defined in visuals.md for each toy type** - do NOT add fields that aren't documented in visuals.md
- The ONLY exceptions are the universal fields: `id`, `type`, and `role` (defined below)

**Workspace Structure:**
- **For Step 1**: Array of tangibles (no inherited field needed)
- **For Step 2+**: Add `inherited` boolean field:
  - `true` if same tangibles with modified state
  - `false` or omit if completely different tangibles

**Universal Tangible Fields:**

ALL tangible types (number_line, fraction_strip, etc.) support these universal fields IN ADDITION to their toy-specific properties:

- **id**: Unique identifier (e.g., "line_1", "bar_a", "bar_b")
- **type**: Toy type matching visuals.md (e.g., "number_line", "fraction_strip")
- **role**: (REQUIRED) Workspace context marker indicating how this tangible is used
  - `"reference"` - Non-interactable, for display/comparison only (student cannot select or modify)
  - `"student_interaction"` - Interactable, student can select/modify this tangible
  - **Keywords to identify reference tangibles**: "reference bar", "at top", "for comparison", "marked read-only", "pre-placed", "shows target", "for display only"
  - **Default**: If unclear, most tangibles are `"student_interaction"` unless explicitly marked as reference
  - **IMPORTANT**: Always add the `role` field to ALL tangibles. This field is REQUIRED for proper transformation to Godot format.
- **description**: (REQUIRED) Natural language description directly derived from workspace_description
  - Extract the phrase from workspace_description that describes this specific tangible
  - Examples from workspace_description:
    - "A fraction bar to show 1/2 shaded" → description: "Fraction bar showing 1/2 shaded"
    - "Number line with point marked at 2/3" → description: "Number line with point at 2/3"
    - "Bar with 2 out of 4 sections shaded" → description: "Bar with 2/4 shaded"
    - "Blank number line from 0 to 1" → description: "Blank number line 0-1"
  - **This field is the SOURCE OF TRUTH** - all technical fields must match this description

**Parsing Natural Language to Structured Workspace:**
1. Identify the shape type(s) mentioned in workspace_description
2. **For each tangible, extract its description from workspace_description and write the `description` field FIRST**
   - This captures what the workspace_description says this tangible should show
   - Example: workspace_description says "Bar A shows 2/4, Bar B shows 1/2" → Bar A gets description: "Bar showing 2/4 shaded"
3. Look up the corresponding schema in <visuals> to see what fields are valid for this toy type
4. **Use the description to determine ALL technical field values**:
   - "Bar showing 2/4 shaded" → intervals: "1/4", intervals_is_shaded: [0, 1]
   - "Number line with point at 1/2" → points: ["1/2"]
   - This ensures the technical fields exactly match what the description says
5. Extract other property values from the text description (e.g., "from 0 to 1" → range: [0, 1])
6. **Add universal fields**: `id`, `type`, `role`, and `description` (for ALL tangibles)
7. **Add ONLY toy-specific fields defined in visuals.md** - do NOT add any other fields
8. Build the workspace element following the exact schema structure from visuals.md
9. For special elements (MCQ choices, drag palettes), check if interaction_tool requires them and add accordingly

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
  - **Count correct answers first**: This determines tool choice (see interaction_tool section)
  - **Single correct answer**: value is string or single-item array; tool should be "select" or "click_choice"
  - **Multiple correct answers**: value is array with 2+ items; tool MUST be "multi_select" or "multi_click_choice"
  - If multiple tangibles/options are equivalent (e.g., two bars showing 2/3), either:
    - Make options visually distinct (different fractions) to keep single correct answer, OR
    - Use multi_select/multi_click_choice with array of ALL correct answers (and plural language in dialogue/prompt)
  - **NEVER have ambiguous correct answers** (e.g., single-select tool with multiple equivalent options)
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
            "role": "student_interaction",
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

    validation_prompt="""Check this sequence for specific errors.

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

Sequence to check:""",

    examples=[],

    module_ref={},

    template_ref=["mastery_verb", "success_dialogue", "skill"],

    cache_docs=True,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
