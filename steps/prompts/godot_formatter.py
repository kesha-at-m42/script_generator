"""
Godot Formatter - Transforms interaction sequences into Godot-processable format
"""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

GODOT_FORMATTER_PROMPT = Prompt(
    role="""You are an expert at transforming educational content schemas into Godot game engine format.

Your task: Transform interaction sequences into Godot-processable format with @type annotations and proper component structure.""",

    instructions="""
## TASK

Transform interaction sequence into Godot Sequence format.

You will receive ONE sequence with metadata and a `steps` array (may contain single or multiple steps). Transform it into ONE Godot Sequence with:
- Metadata at the top level
- All steps in the `steps` array
- Proper @type annotations throughout

**MULTI-STEP WORKSPACE HANDLING (CRITICAL):**
- **Step 1 (step_id: 1)**: Define workspace structure normally
- **Step 2+ (step_id: 2, 3, ...)**: DO NOT include workspace field at all
  - Steps automatically inherit workspace from step 1
  - Simply omit the workspace field entirely from steps 2+
  - The workspace evolves based on step 1's actions

**CRITICAL: Consult <sequence> for the complete Godot sequence structure. Every element you generate (Sequence, Step, Prompt, WorkspaceChoices, Palette, Remediation) must conform exactly to the schema specifications in sequence.md.**

Refer to documentation for complete specifications:
- **sequence.md** - Complete sequence structure with @type usage, Step, Prompt, WorkspaceChoices, Palette, Remediation schemas
- **tools.md** - Tool types (Move, Place, Drag, Select, Paint, etc.)
- **validators.md** - Validator types and answer formats
- **workspace.md** - Tangible types (NumLine, FracShape, Vocab, etc.)

## KEY TRANSFORMATIONS

### 1. Add @type Annotations
Consult <sequence> for @type field usage across all objects. Every object requires a @type field for proper deserialization.

### 2. Metadata Extraction
Move sequence-level fields into metadata object:
```json
"metadata": {
  "@type": "SequenceMetadata",
  "problem_id": 123,
  "template_id": "4008",
  "template_skill": "Description of the skill being practiced",
  "identifiers": ["2/3"],
  "mastery_tier": "BASELINE",  // Keep original: SUPPORT, CONFIDENCE, BASELINE, STRETCH, CHALLENGE
  "mastery_verb": "IDENTIFY",
  "telemetry_data": {
    "mastery_skill": "Place unit fraction on 0-1 number line",  // from template_ref
    "cognitive_verb": "CREATE",  // from template_ref
    "mastery_skill_id": "M4-01",  // from template_ref
    "tier": "baseline",  // from input mastery_tier variable
    "non_curriculum_skills": ["click_accuracy"],  // determined by interaction_tool (place_point)
    "misconception_id": [],
    "misconception_tag": []
  }
}
```

**Identifiers Array Format:**
- Copy the fractions array directly to identifiers
- Example: If input has `fractions: ["2/3"]`, output is `identifiers: ["2/3"]`
- Multiple fractions: `fractions: ["2/3", "1/4"]` → `identifiers: ["2/3", "1/4"]`

### 3. Tool Mapping
**CRITICAL: You MUST strictly follow ALL tool schemas defined in <tools>. Every tool must use the exact structure, @type, and required fields specified in tools.md. Validate your output against tools.md before finalizing.**

Map `interaction_tool` to Godot tool @type (refer to <tools> for complete schema):

**Point Placement:**
- `place_point` → Move with mode="points" and palette with PointStack
  - For unlimited points: PointStack with no quantity field (defaults to -1)
    ```json
    {
      "@type": "Move",
      "mode": "points",
      "palette": {
        "@type": "Palette",
        "stacks": [{"@type": "PointStack"}]
      }
    }
    ```
  - For limited points: PointStack with specific quantity
    ```json
    {
      "@type": "Move",
      "mode": "points",
      "palette": {
        "@type": "Palette",
        "stacks": [{"@type": "PointStack", "quantity": 3}]
      }
    }
    ```

**Label Dragging:**
- `drag_label` → Move with mode="frac_labels" and palette with FracLabelStack (ALWAYS required)
  ```json
  {
    "@type": "Move",
    "mode": "frac_labels",
    "palette": {
      "@type": "Palette",
      "stacks": [
        {"@type": "FracLabelStack", "label": "1/4"}
      ]
    }
  }
  ```

**Other Tools:**
- `click_choice` → No tool (MCQ uses choices)
- `select` → Select (is_single: true)
- `multi_select` → Select (is_single: false)
- `place_tick` → Place (partition number line, ALWAYS include lcm using 3× denominator rule)
- `cut_shape` → Place (divide shape, ALWAYS include lcm using 3× denominator rule)
- `shade` → Paint

### 4. Validator Mapping
Choose validator based on interaction_tool (see validators.md for complete specifications and answer formats):
- `place_point` → PointValidator
- `drag_label` → LabelValidator
- `click_choice` → MultipleChoiceValidator
- `select` or `multi_select` → SelectionValidator
- `place_tick` or `cut_shape` → TickValidator
- `shade` → ShadedValidator or ShadedPartsValidator

**Important**:
- Move tool with mode="points" ALWAYS uses palette with PointStack (even for unlimited points)
- Move tool with mode="frac_labels" ALWAYS uses palette with FracLabelStack
- PointStack quantity defaults to -1 (unlimited) when omitted
- FracLabelStack quantity defaults to 1 when omitted
- `click_choice` is for MCQ, `select` is for tangible selection (different use cases)
- See validators.md for correct answer format for each validator type

### 4a. Non-Curriculum Skills Mapping
Determine non_curriculum_skills array based on interaction_tool and question type:

**Interaction-based skills:**
- `place_point` → ["click_accuracy"]
- `drag_label` → ["drag_drop", "fine_motor_control"]
- `click_choice` → ["click_accuracy", "reading_comprehension"]
- `select` → ["click_accuracy", "visual_discrimination"]
- `multi_select` → ["click_accuracy", "visual_discrimination", "multiple_selection"]
- `place_tick` → ["click_accuracy", "spatial_reasoning"]
- `cut_shape` → ["click_accuracy", "spatial_reasoning"]
- `shade` → ["click_accuracy", "fine_motor_control"]

**Additional skills by question characteristics:**
- If workspace has 3+ tangibles for comparison → add "visual_comparison"
- If prompt mentions "count" or "how many" → add "counting"
- If question involves fractions beyond 1 → add "extended_number_line_reasoning"
- If MCQ has 4+ options → add "option_evaluation"
- If question involves application context → add "context_interpretation"

**Common non-curriculum skills:**
- click_accuracy - Ability to click/tap precisely on targets
- drag_drop - Ability to drag items to correct locations
- fine_motor_control - Precise cursor/finger control
- reading_comprehension - Understanding written instructions
- visual_discrimination - Distinguishing between similar visual elements
- visual_comparison - Comparing multiple visual representations
- spatial_reasoning - Understanding spatial relationships
- counting - Counting intervals, ticks, or spaces
- multiple_selection - Selecting multiple items correctly
- option_evaluation - Evaluating multiple choice options
- context_interpretation - Understanding story/application context
- extended_number_line_reasoning - Working with number lines beyond 1

Generate an appropriate array of 1-3 non_curriculum_skills for each question based on these mappings.

### 4b. Misconceptions Mapping
Determine misconception_id and misconception_tag arrays based on problem characteristics:

**Misconception Mappings:**

1. **equal_vs_unequal_parts** (ID: 1)
   - Problem involves identifying equal intervals vs unequal
   - Workspace shows comparison of equal/unequal partitions
   - Tags: ["Meta_Remediation", "Context_Framing_Issue"]

2. **misidentifying_the_whole** (ID: 2)
   - Multiple wholes or shapes in workspace
   - Comparison tasks with different-sized representations
   - Tags: ["Needs_DevAdapt", "Misconception_Spotlight"]

3. **numerator_denominator_as_independent** (ID: 3)
   - Identifying or placing non-unit fractions
   - Labeling tasks where numerator changes
   - Any task requiring understanding a/b relationship
   - Tags: ["Symbol_Link_Support", "Meta_Prompt"]

4. **improper_spacing_on_number_line** (ID: 4)
   - Partitioning number lines (place_tick)
   - Comparing equal vs unequal interval spacing
   - Tags: ["Meta_Remediation", "Visual_Anchor"]

5. **counting_tick_marks_instead_of_spaces** (ID: 5)
   - Counting intervals to identify denominator
   - Placing fractions by counting from zero
   - Any task emphasizing "count spaces not ticks"
   - Tags: ["Meta_Remediation", "AI_Peer_Opportunity"]

6. **reversing_numerator_and_denominator** (ID: 6)
   - Identifying fractions from points
   - Labeling tick marks with fractions
   - Reading or writing fraction notation
   - Tags: ["Symbol_Link_Support", "Needs_DevAdapt"]

7. **difficulty_recognizing_equivalence** (ID: 7)
   - Equivalent fraction tasks (2/4 = 1/2)
   - Comparing fractions with different denominators
   - Tags: ["Transfer_Thinking", "Meta_Prompt"]

8. **errors_comparing_unlike_fractions** (ID: 8)
   - Comparing fractions with different denominators
   - Ordering fractions by size
   - Tasks where "larger denominator = smaller pieces"
   - Tags: ["Benchmark_Anchor", "Meta_Remediation"]

9. **fractions_only_exist_in_shapes** (ID: 9)
   - Application contexts using number lines
   - Transfer from area models to linear models
   - Tags: ["Transfer_Thinking", "Symbol_Link_Support"]

10. **overgeneralizing_rules** (ID: 10)
    - Complex comparison or ordering tasks
    - Application problems requiring flexible thinking
    - Tags: ["Meta_Prompt", "Needs_DevAdapt"]

11. **fractions_cant_exceed_one** (ID: 11)
    - Any task involving fractions beyond 1 (numerator > denominator)
    - Extended number lines (0-2 range)
    - Tags: []

**Assignment Logic:**
- Identify 1-3 most relevant misconceptions for each question
- Include misconception_id as array of integers: [5, 11]
- Include misconception_tag as array of strings: ["counting_tick_marks_instead_of_spaces", "fractions_cant_exceed_one"]
- If no specific misconceptions apply, use empty arrays: [], []

### 5. Workspace Restructuring
Transform workspace (see workspace.md):
- Array → object with `tangibles` array
- Add `@type` to all tangibles
- Remove `id` and `type` fields
- Move `choices` from workspace to prompt.choices
- Add `shuffle_tangibles: true` for select questions (when interaction_tool is `select` or `multi_select`)

### 6. NumLine Conversions
Key field changes (see workspace.md for details):
- Keep `ticks` or `intervals` as-is (schema handles both)
- Keep `labels` as-is (schema accepts array or boolean)
- Add `is_visible: true`
- Add `visual` based on structure:
  - If NumLine has `ticks` → `"visual": "line"` (number line)
  - If NumLine has `intervals` → `"visual": "bar"` (fraction strip)
- Add `lcm` using 3× denominator rule:
  - Halves (1/2): lcm = 6
  - Thirds (1/3): lcm = 9
  - Fourths (1/4): lcm = 12
  - Sixths (1/6): lcm = 18
  - Eighths (1/8): lcm = 24

### 7. Answer Conversions
- Choice IDs → indices: "a"→[0], "b"→[1], "c"→[2]
- Tangible IDs → indices: "line_1"→[0], "line_2"→[1]
- Fractions: Keep as strings "2/3"

### 8. Success and Error Paths
Convert flat fields to nested structure:
- `success_path_dialogue` → `"on_correct": {"@type": "Step", "dialogue": "..."}`
- `error_path_generic` → `"remediations": [array of 3 Remediation objects]`

For error paths, transform each scaffolding level into a separate Remediation object with ids: "light", "medium", "heavy". Consult <sequence> "Remediation" section for complete schema structure.

### 9. Choices Extraction
Move choices from workspace to prompt. Consult <sequence> "WorkspaceChoices" section for complete schema structure.

### 10. Palette Structure
When interaction_tool is "drag_label", add palette with stacks. Consult <sequence> "Palette" and "FracLabelStack" sections for complete schema structure.

## EXAMPLE TRANSFORMATION

**Input (sequence with single step)**:
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
      "dialogue": "Look at the point on the number line.",
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
            {"id": "b", "text": "2/3"}
          ]
        }
      ],
      "correct_answer": {
        "value": "b",
        "context": "The point is at 2/3"
      },
      "success_path_dialogue": "Yes, that's two-thirds.",
      "error_path_generic": {
        "steps": [
          {"scaffolding_level": "light", "dialogue": "Not quite. Try again."},
          {"scaffolding_level": "medium", "dialogue": "Look at where the point is..."},
          {"scaffolding_level": "heavy", "dialogue": "The point is at 2 out of 3 parts..."}
        ]
      }
    }
  ]
}
```

**Input (sequence with multiple steps - note step 2 has workspace that should be IGNORED)**:
```json
{
  "problem_id": 75,
  "mastery_tier": "BASELINE",
  "mastery_verb": "create",
  "template_id": "5011",
  "fractions": ["1/4", "2/4", "3/4"],
  "no_of_steps": 2,
  "steps": [
    {
      "step_id": 1,
      "dialogue": "Let's divide this number line into fourths.",
      "prompt": "Divide this line into fourths.",
      "interaction_tool": "place_tick",
      "workspace": [
        {
          "id": "line_1",
          "type": "number_line",
          "range": [0, 1],
          "ticks": [0, 1],
          "labels": [0, 1]
        }
      ],
      "correct_answer": {
        "value": ["1/4", "2/4", "3/4"],
        "context": "Three tick marks placed"
      },
      "success_path_dialogue": "Good. You made four equal parts.",
      "error_path_generic": { "steps": [...] }
    },
    {
      "step_id": 2,
      "dialogue": "Now label each tick mark.",
      "prompt": "Label each position.",
      "interaction_tool": "drag_label",
      "workspace": [
        {
          "id": "line_1",
          "type": "number_line",
          "range": [0, 1],
          "ticks": [0, "1/4", "2/4", "3/4", 1],
          "labels": [0, 1]
        },
        {
          "type": "palette",
          "labels": ["1/4", "2/4", "3/4"]
        }
      ],
      "correct_answer": {
        "value": {"1/4": "1/4", "2/4": "2/4", "3/4": "3/4"},
        "context": "All labels placed correctly"
      },
      "success_path_dialogue": "Right. You labeled all the fourths.",
      "error_path_generic": { "steps": [...] }
    }
  ]
}
```

**Output (Godot Sequence format - NO SequencePool wrapper)**:

For single-step sequences:
```json
{
  "@type": "Sequence",
  "metadata": {
    "@type": "SequenceMetadata",
    "problem_id": 49,
    "template_id": "4008",
    "template_skill": "Student can identify fractions on number line",
    "identifiers": ["2/3"],
    "mastery_tier": "BASELINE",
    "mastery_verb": "IDENTIFY",
    "telemetry_data": {
      "mastery_skill": "Identify fractions on pre-partitioned number line",
      "cognitive_verb": "IDENTIFY",
      "mastery_skill_id": "M4-02",
      "tier": "baseline",
      "non_curriculum_skills": ["click_accuracy", "reading_comprehension"],
      "misconception_id": [3, 6],
      "misconception_tag": ["numerator_denominator_as_independent", "reversing_numerator_and_denominator"]
    }
  },
  "steps": [{
    "@type": "Step",
    "dialogue": "Look at the point on the number line.",
    "workspace": {
      "@type": "WorkspaceData",
      "tangibles": [{
        "@type": "NumLine",
        "is_visible": true,
        "visual": "line",
        "range": [0, 1],
        "ticks": "1/3",
        "points": ["2/3"],
        "labels": ["0", "1"],
        "lcm": 12
      }]
    },
    "prompt": {
      "@type": "Prompt",
      "text": "What fraction does this point show?",
      "validator": {
        "@type": "MultipleChoiceValidator",
        "answer": [1]
      },
      "choices": {
        "@type": "WorkspaceChoices",
        "allow_multiple": false,
        "options": ["1/3", "2/3"]
      },
      "remediations": [
        {
          "@type": "Remediation",
          "id": "light",
          "step": {"@type": "Step", "dialogue": "Not quite. Try again."}
        },
        {
          "@type": "Remediation",
          "id": "medium",
          "step": {"@type": "Step", "dialogue": "Look at where the point is..."}
        },
        {
          "@type": "Remediation",
          "id": "heavy",
          "step": {"@type": "Step", "dialogue": "The point is at 2 out of 3 parts..."}
        }
      ],
      "on_correct": {
        "@type": "Step",
        "dialogue": "Yes, that's two-thirds."
      }
    }
  }]
}
```

For multi-step sequences (NOTE: Step 2 does NOT have workspace field):
```json
{
  "@type": "Sequence",
  "metadata": {
    "@type": "SequenceMetadata",
    "problem_id": 75,
    "template_id": "5011",
    "template_skill": "Create and label fourths on number line",
    "identifiers": ["1/4", "2/4", "3/4"],
    "mastery_tier": "BASELINE",
    "mastery_verb": "create",
    "telemetry_data": { ... }
  },
  "steps": [
    {
      "@type": "Step",
      "dialogue": "Let's divide this number line into fourths.",
      "workspace": {
        "@type": "WorkspaceData",
        "tangibles": [{
          "@type": "NumLine",
          "is_visible": true,
          "visual": "line",
          "range": [0, 1],
          "ticks": [0, 1],
          "labels": [0, 1],
          "lcm": 12
        }]
      },
      "prompt": {
        "@type": "Prompt",
        "text": "Divide this line into fourths.",
        "tool": {
          "@type": "Place",
          "tangible_index": 0,
          "target": "ticks",
          "lcm": 12
        },
        "validator": {
          "@type": "TickValidator",
          "answer": ["1/4", "2/4", "3/4"]
        },
        "remediations": [...],
        "on_correct": {
          "@type": "Step",
          "dialogue": "Good. You made four equal parts."
        }
      }
    },
    {
      "@type": "Step",
      "dialogue": "Now label each tick mark.",
      "prompt": {
        "@type": "Prompt",
        "text": "Label each position.",
        "tool": {
          "@type": "Drag",
          "tangible_index": 0,
          "target": "labels",
          "palette": {
            "@type": "Palette",
            "stacks": [
              {"@type": "FracLabelStack", "label": "1/4"},
              {"@type": "FracLabelStack", "label": "2/4"},
              {"@type": "FracLabelStack", "label": "3/4"}
            ]
          }
        },
        "validator": {
          "@type": "LabelValidator",
          "answer": {"1/4": "1/4", "2/4": "2/4", "3/4": "3/4"}
        },
        "remediations": [...],
        "on_correct": {
          "@type": "Step",
          "dialogue": "Right. You labeled all the fourths."
        }
      }
    }
  ]
}
```

**KEY POINT**: Notice step 2 has NO `workspace` field - it automatically inherits the workspace from step 1.

**Key transformations in this example**:
1. Flat item → Sequence (no SequencePool wrapper)
2. Metadata extracted into separate object with @type
3. All objects have @type annotations
4. Workspace: array → object with tangibles array
5. NumLine: Added visual, is_visible, lcm fields
6. NumLine: ticks simplified to "1/3" (uniform spacing)
7. NumLine: labels kept as array (workspace.md allows this)
8. Choices: moved from workspace to prompt.choices
9. Choices: options simplified from objects to strings
10. Answer: "b" converted to index [1]
11. Success path: success_path_dialogue → on_correct Step
12. Error paths: error_path_generic.steps → remediations array with @type
13. Removed: id and type fields from tangibles
14. mastery_tier kept as original string value
15. non_curriculum_skills: auto-generated based on interaction_tool (click_choice → ["click_accuracy", "reading_comprehension"])
16. misconception_id and misconception_tag: auto-generated based on problem characteristics ([3, 6] for identifying fractions from points)

## IMPORTANT NOTES

- Input is ONE flat item - output is ONE Sequence (batch mode)
- DO NOT wrap output in SequencePool (that happens in a separate step)
- **Always consult documentation:**
  - <sequence> for Sequence, Step, Prompt, WorkspaceChoices, Palette, Remediation structures
  - <tools> for tool types and schemas
  - <validators> for validator types and answer formats
  - <workspace> for tangible types and properties
- For select questions (interaction_tool: `select` or `multi_select`), set `shuffle_tangibles: true` in workspace to randomize tangible order
- Metadata must include: problem_id, template_id, template_skill, identifiers, mastery_tier, mastery_verb, telemetry_data (with all required telemetry fields)
- Telemetry data sources:
  - mastery_skill (from template.skill)
  - cognitive_verb (from template.mastery_verb)
  - mastery_skill_id (from template.skill_id)
  - tier (from input mastery_tier)
  - non_curriculum_skills (AUTO-GENERATE based on interaction_tool using the mapping in section 4a)
  - misconception_id (AUTO-GENERATE based on problem characteristics using the mapping in section 4b, array of integers)
  - misconception_tag (AUTO-GENERATE based on problem characteristics using the mapping in section 4b, array of strings)
- Remove: id, type fields from input tangibles from steps
- Convert error_path_generic.steps array to remediations array with proper structure

Return ONLY valid JSON with Godot schema structure.
""",

    doc_refs=["sequence.md", "tools.md", "validators.md", "workspace.md"],

    output_structure="""
{
  "@type": "Sequence",
  "metadata": {
    "@type": "SequenceMetadata",
    "problem_id": 1,
    "template_id": "4001",
    "template_skill": "Student can place fractions on number line",
    "identifiers": ["1/3"],
    "mastery_tier": "BASELINE",
    "mastery_verb": "IDENTIFY",
    "telemetry_data": {
      "mastery_skill": "Place unit fraction on 0-1 number line",
      "cognitive_verb": "CREATE",
      "mastery_skill_id": "M4-01",
      "tier": "baseline",
      "non_curriculum_skills": ["click_accuracy"],
      "misconception_id": [5],
      "misconception_tag": ["counting_tick_marks_instead_of_spaces"]
    }
  },
  "steps": [{
    "@type": "Step",
    "dialogue": "...",
    "workspace": {
      "@type": "WorkspaceData",
      "tangibles": [
        {
          "@type": "NumLine",
          "is_visible": true,
          "visual": "line",
          "range": [0, 1],
          "ticks": "1/3",
          "labels": ["0", "1"],
          "lcm": 9
        }
      ]
    },
    "prompt": {
      "@type": "Prompt",
      "text": "...",
      "tool": {"@type": "Place", "lcm": 9, "bounds": ["0", "1"]},
      "validator": {"@type": "TickValidator", "answer": "1/3"},
      "remediations": [],
      "on_correct": {"@type": "Step", "dialogue": "..."}
    }
  }]
}
""",

    # Prefill forces proper Godot structure with @types
    # Batch mode: processes one item at a time, outputs one Sequence
    # Uses input variables and template_ref for metadata
    prefill="""{
  "@type": "Sequence",
  "metadata": {
    "@type": "SequenceMetadata",
    "problem_id": {problem_id},
    "template_id": "{template_id}",
    "template_skill": "{problem_type}",
    "identifiers": {fractions},
    "mastery_tier": "{mastery_tier}",
    "mastery_verb": "{mastery_verb}",
    "telemetry_data": {
      "mastery_skill": "{skill}",
      "cognitive_verb": "{mastery_verb}",
      "mastery_skill_id": "{skill_id}",
      "tier": "{mastery_tier}",
      "non_curriculum_skills": """,

    examples=[],

    module_ref={},

    template_ref=["problem_type", "skill", "mastery_verb", "skill_id"],

    cache_docs=True,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
