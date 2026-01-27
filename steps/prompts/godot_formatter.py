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
  "identifiers": {
    "fractions": ["2/3"]
  },
  "mastery_tier": "BASELINE",  // Keep original: SUPPORT, CONFIDENCE, BASELINE, STRETCH, CHALLENGE
  "mastery_component": "CONCEPTUAL",
  "mastery_verb": "IDENTIFY",
  "telemetry_data": {}
}
```

### 3. Tool Mapping
Map `interaction_tool` to Godot tool (see tools.md):
- `place_point` → Move tool
- `drag_label` → Drag tool with labels/quantities
- `click_choice` → no tool (uses choices)
- `select` / `multi_select` → Select tool

### 4. Validator Mapping
Choose validator based on interaction_tool (see validators.md):
- Move tool → PointValidator
- Drag tool → LabelValidator
- MCQ → MultipleChoiceValidator
- Select → SelectionValidator

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
    "identifiers": {
      "fractions": ["2/3"]
    },
    "mastery_tier": "BASELINE",
    "mastery_component": "CONCEPTUAL",
    "mastery_verb": "IDENTIFY",
    "telemetry_data": {}
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
- Metadata must include: problem_id, template_id, template_skill, identifiers, mastery_tier, mastery_component, mastery_verb, telemetry_data
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
    "identifiers": {
      "fractions": ["1/3"]
    },
    "mastery_tier": "BASELINE",
    "mastery_component": "CONCEPTUAL",
    "mastery_verb": "IDENTIFY",
    "telemetry_data": {}
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
      "tool": "move",
      "validator": {"@type": "TickValidator", "answer": ["2/3"]},
      "remediations": [],
      "on_correct": {"@type": "Step", "dialogue": "..."}
    }
  }]
}
""",

    # Prefill forces proper Godot structure with @types
    # Batch mode: processes one item at a time, outputs one Sequence
    # Minimal prefill avoids variable substitution issues
    prefill="""{"@type":"Sequence",""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=False,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
