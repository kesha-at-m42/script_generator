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

Transform interaction sequences from sequence_structurer output to Godot-processable format.

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
  "difficulty": 2,
  "verb": "IDENTIFY",
  "template_id": "4008",
  "fractions": ["2/3"]
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

### 8. Success Path
Convert `student_attempts.success_path.dialogue` to:
```json
"on_correct": {
  "@type": "Step",
  "dialogue": "..."
}
```

### 9. Choices Extraction
Move choices from workspace to prompt and flatten:
```json
"choices": {
  "allow_multiple": false,
  "options": ["1/3", "2/3", "3/3"]
}
```

### 10. Palette Structure
Palette objects do NOT have @type field:
```json
"palette": {
  "labels": ["1/3", "2/3"],
  "quantities": [1, 1]
}
```

## EXAMPLE TRANSFORMATION

**Input (from sequence_structurer)**:
```json
{
  "problem_id": 49,
  "difficulty": 2,
  "verb": "IDENTIFY",
  "template_id": "4008",
  "fractions": ["2/3"],
  "steps": [{
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
    "student_attempts": {
      "success_path": {
        "dialogue": "Yes, that's two-thirds."
      }
    }
  }]
}
```

**Output (Godot format)**:
```json
{
  "@type": "Sequence",
  "metadata": {
    "@type": "SequenceMetadata",
    "problem_id": 49,
    "difficulty": 2,
    "verb": "IDENTIFY",
    "template_id": "4008",
    "fractions": ["2/3"]
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
        "allow_multiple": false,
        "options": ["1/3", "2/3"]
      },
      "remediations": [],
      "on_correct": {
        "@type": "Step",
        "dialogue": "Yes, that's two-thirds."
      }
    }
  }]
}
```

**Key transformations in this example**:
1. Metadata extracted into separate object with @type
2. All objects have @type annotations
3. Workspace: array → object with tangibles array
4. NumLine: Added visual, is_visible, lcm fields
5. NumLine: ticks simplified to "1/3" (uniform spacing)
6. NumLine: labels kept as array (workspace.md allows this)
7. Choices: moved from workspace to prompt.choices
8. Choices: options simplified from objects to strings
9. Answer: "b" converted to index [1]
10. Success path: converted to on_correct Step
11. Removed: id and type fields from tangibles

## IMPORTANT NOTES

- Refer to tools.md, validators.md, and workspace.md for complete specifications
- NumLine can use either `ticks` (array or single fraction) or `intervals` - see workspace.md
- Tools can be strings ("select") or objects ({"@type": "Select"}) - see tools.md
- Validator answer formats vary by type - see validators.md
- Always include @type for objects EXCEPT: palette and choices (these have no @type)
- Palette structure: {"labels": [...], "quantities": [...]} - NO @type field
- Choices structure: {"allow_multiple": bool, "options": [...]} - NO @type field
- Remove id, type fields from input tangibles
- Set remediations to [] if no error paths provided

Return ONLY valid JSON with Godot schema structure.
""",

    doc_refs=["tools.md", "validators.md", "workspace.md"],

    output_structure="""
{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "metadata": {
        "@type": "SequenceMetadata",
        "problem_id": 1,
        "difficulty": 2,
        "verb": "IDENTIFY",
        "template_id": "4001",
        "fractions": ["1/3"]
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
  ]
}
""",

    prefill="""{"@type":"SequencePool","sequences":[{"@type":"Sequence","metadata":{"@type":"SequenceMetadata","problem_id":""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=False,
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
