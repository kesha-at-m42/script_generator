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

Transform interaction step (flat format) into Godot Sequence format (one step at a time).

You will receive ONE flat item representing ONE step. Transform it into a Godot Sequence with proper @type annotations.

Refer to documentation for complete specifications:
- **tools.md** - Tool types (Move, Place, Drag, Select, Paint, etc.)
- **validators.md** - Validator types and answer formats
- **workspace.md** - Tangible types (NumLine, FracShape, Vocab, etc.)

## KEY TRANSFORMATIONS

### 1. Add @type Annotations
Every object needs `@type`:
- Root: `SequencePool`
- Sequence: `Sequence` (with `SequenceMetadata`)
- Step: `Step`
- Workspace: `WorkspaceData`
- Tools, Validators, Tangibles: See respective docs

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
- `place_point` → Move
- `drag_label` → Drag (REQUIRES palette)
- `click_choice` → No tool (MCQ uses choices)
- `select` → Select (is_single: true)
- `multi_select` → Select (is_single: false)
- `place_tick` → Place (partition number line)
- `cut_shape` → Place (divide shape)
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
- Move tool does NOT use palette (places points directly)
- Drag tool REQUIRES palette (drags labels from palette)
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

### 6. NumLine Conversions
Key field changes (see workspace.md for details):
- Keep `ticks` or `intervals` as-is (schema handles both)
- Keep `labels` as-is (schema accepts array or boolean)
- Add `is_visible: true`
- Add `visual: "line"`
- Add `lcm` (typically 12)

### 7. Answer Conversions
- Choice IDs → indices: "a"→[0], "b"→[1], "c"→[2]
- Tangible IDs → indices: "line_1"→[0], "line_2"→[1]
- Fractions: Keep as strings "2/3"

### 8. Success and Error Paths
Convert flat fields to nested structure:
- `success_path_dialogue` → `"on_correct": {"@type": "Step", "dialogue": "..."}`
- `error_path_generic` → `"remediations": [array of 3 Remediation objects]`

For error paths, transform each scaffolding level into a separate Remediation object:
```json
"remediations": [
  {
    "@type": "Remediation",
    "id": "light",
    "step": {"@type": "Step", "dialogue": "..."}
  },
  {
    "@type": "Remediation",
    "id": "medium",
    "step": {"@type": "Step", "dialogue": "..."}
  },
  {
    "@type": "Remediation",
    "id": "heavy",
    "step": {"@type": "Step", "dialogue": "..."}
  }
]
```

### 9. Choices Extraction
Move choices from workspace to prompt and flatten:
```json
"choices": {
  "@type": "WorkspaceChoices",
  "allow_multiple": false,
  "options": ["1/3", "2/3", "3/3"]
}
```

### 10. Palette Structure
Palette objects MUST have @type field:
```json
"palette": {
  "@type": "Palette",
  "labels": ["1/3", "2/3"],
  "quantities": [1, 1]
}
```

## EXAMPLE TRANSFORMATION

**Input (one flat item with remediation)**:
```json
{
  "problem_id": 49,
  "mastery_tier": "BASELINE",
  "verb": "IDENTIFY",
  "template_id": "4008",
  "fractions": ["2/3"],
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
```

**Output (Godot Sequence format - NO SequencePool wrapper)**:
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
- Refer to tools.md, validators.md, and workspace.md for complete specifications
- NumLine can use either `ticks` (array or single fraction) or `intervals` - see workspace.md
- Tools can be strings ("select") or objects ({"@type": "Select"}) - see tools.md
- Validator answer formats vary by type - see validators.md
- Always include @type for ALL objects including palette and choices
- Palette structure: {"@type": "Palette", "labels": [...], "quantities": [...]}
- Choices structure: {"@type": "WorkspaceChoices", "allow_multiple": bool, "options": [...]}
- Remediation structure: Array of 3 objects: [{"@type": "Remediation", "id": "light", "step": {...}}, {"@type": "Remediation", "id": "medium", "step": {...}}, {"@type": "Remediation", "id": "heavy", "step": {...}}]
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

    doc_refs=["tools.md", "validators.md", "workspace.md"],

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
          "lcm": 12
        }
      ]
    },
    "prompt": {
      "@type": "Prompt",
      "text": "...",
      "tool": {"@type": "Move"},
      "validator": {"@type": "TickValidator", "answer": ["2/3"]},
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

    cache_docs=False,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
