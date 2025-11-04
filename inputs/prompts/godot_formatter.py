"""
Godot Formatter Prompt Configuration
Transforms remediation sequences to Godot-processable schema

This is an AI-powered transformation that understands the semantic structure
and produces properly formatted Godot sequences.
"""

GODOT_FORMATTER_ROLE = """You are an expert in transforming educational content schemas into Godot game engine format.

Your task: Transform remediation sequences into Godot-processable format that matches the exact specification with @type annotations and proper component structure."""

GODOT_FORMATTER_EXAMPLES = []
GODOT_FORMATTER_DOCS = ["godot_schema_spec.md"]

GODOT_FORMATTER_INSTRUCTIONS = """
## YOUR TASK

Transform these interaction sequences to Godot-processable format:

<interaction_sequences>
{complete_interaction_sequences}
</interaction_sequences>

See godot_schema_spec.md for complete structure documentation.

## TRANSFORMATION RULES

### 1. Sequence Metadata Structure

Each Sequence must include a metadata object with these fields:

**Input fields (copy directly from source):**
- `problem_id`: Integer - unique identifier for this problem
- `goal_id`: Integer - learning goal this sequence addresses
- `goal_text`: String - human-readable description of the learning goal
- `verb`: String - primary interaction verb (e.g., "shade", "partition", "select")
- `variables_covered`: Object - maps variable types to their values
  - Format: `{"fractions": ["1/4", "1/3"], "whole_numbers": [2, 3]}`
  - Common keys: "fractions", "whole_numbers", "mixed_numbers"

**Mastery fields (will be auto-generated, use placeholders):**
- `mastery_tier`: String - set to `"2"` (placeholder, will be mapped from goal_id)
- `mastery_component`: String - set to `"PROCEDURAL"` (placeholder)
- `mastery_verbs`: Array - set to `["APPLY"]` (placeholder)

**Complete metadata structure:**
```json
{
  "@type": "SequenceMetadata",
  "problem_id": 123,
  "goal_id": 5,
  "goal_text": "The student can partition shapes into equal parts",
  "verb": "partition",
  "variables_covered": {"fractions": ["1/4"]},
  "mastery_tier": "2",
  "mastery_component": "PROCEDURAL",
  "mastery_verbs": ["APPLY"]
}
```

Note: Mastery fields will be automatically corrected by metadata_mapper utility in post-processing. Use the placeholder values shown above.

### 2. Add @type Annotations

Every object needs a @type field for deserialization (see schema for complete list):
- Root: `"@type": "SequencePool"`
- Sequence: `"@type": "Sequence"` (with metadata object as shown above)
- Step: `"@type": "Step"`
- Workspace: `"@type": "WorkspaceData"` (NOT "Workspace")
- Tangibles: `"@type": "FracShape"` or `"@type": "NumberLine"`
- Prompt, Validator, Remediation, Choices: Use appropriate @type (see schema)

### 3. Type Mappings

**Tangible Types (input → output):**
ALL fraction shapes use unified `FracShape` type:
- `rectangle_bar` → `"@type": "FracShape"` with `"visual": 0`
- `square` → `"@type": "FracShape"` with `"visual": 0`
- `grid` → `"@type": "FracShape"` with `"visual": 2`
- `circle` → `"@type": "FracShape"` with `"visual": 1`
- `fraction_bar` → `"@type": "FracShape"` with `"visual": 0`
- `number_line` → `"@type": "NumberLine"` (unchanged)

**Tool Mapping (interaction_tool → Godot tool):**
- `shade` → `"paint"` (for shading interactions)
- `cut` → `"cut"` (for dividing/partitioning shapes)
- `select` → `"select"` (for selecting single tangible)
- `multi_select` → `"multi_select"` (for selecting multiple tangibles)
- `place_tick` → `"place_tick"` (unchanged)
- `click_choice` → omit tool (MCQs don't use tools, only workspace.choices)

**Validator Selection:**

Read `correct_answer.context` to understand what's being validated, then determine appropriate validator:

- **Shading a proportion** (e.g., "shade 3/4") → `EqualShadedValidator` with fraction string answer
- **Shading a count** (e.g., "shade exactly 2 parts") → `ShadedPartsValidator` with integer answer
- **Part sizes after cutting** (e.g., "cut into thirds") → `FractionShapePartsValidator` with fraction string/array
- **Selecting tangible(s)** (e.g., "select the shape showing 1/2") → `SelectionValidator` with integer/array
- **Multiple choice** (e.g., "which represents 3/4?") → `MultipleChoiceValidator` with array of indices
- **Placing tick marks** (e.g., "place ticks at 1/3 and 2/3") → `PlaceTicksValidator` with numerator array
- **Selecting tick marks** (e.g., "select the tick at 2/6") → `SelectTicksValidator` with numerator array

See schema for validator field requirements and answer formats.

### 4. FracShape State Conversion

**Input fields (standardized schema):**
- `type`: Shape type (rectangle_bar, circle, grid, etc.)
- `sections`: Integer count (1 = undivided, 2+ = divided)
- `state`: Visual state ("undivided", "divided", "divided_unequal")
- `shaded`: Array of 0-based indices
- `position`: Screen location (not used in Godot)

**Output FracShape fields:**
- `@type`: "FracShape"
- `visual`: 0=rectangle/bar, 1=circle/pie, 2=grid (from type mapping)
- `fractions`: Determined by state + sections:
  * `state="undivided"` (sections=1) → omit fractions field (whole shape)
  * `state="divided"` (equal parts) → single fraction string `"1/N"` where N = sections
    - sections=2 → `"1/2"`
    - sections=3 → `"1/3"`
  * `state="divided_unequal"` → array of fractions (must sum to 1)
    - sections=3 → `["1/2", "1/4", "1/4"]`
    - sections=4 → `["1/8", "4/8", "3/8"]`
- `shaded`: Keep as-is (array of 0-based indices)
- `lcm`: LCM calculation:
  * **For partition/cut tasks** (tool="cut" OR verb="partition"/"divide"/"cut"):
    - If shape undivided (sections=1), use correct_answer to get target: answer="1/N" → lcm = N * 2
    - If shape already divided, use existing sections: lcm = sections * 2
  * **For all other interactions**: lcm = 24 (default)

**Remove these fields** (not in Godot schema):
- `id`, `type`, `state`, `position`

### 5. Example Transformations

**Example A: Partition/cut interaction (verb="partition", tool="cut")**

Input:
```json
{
  "verb": "partition",
  "steps": [
    {
      "workspace": [
        {
          "type": "rectangle_bar",
          "sections": 1,
          "state": "undivided",
          "shaded": []
        }
      ]
    },
    {
      "prompt": "Click to cut",
      "interaction_tool": "cut",
      "correct_answer": {
        "value": "1/4",
        "context": "Divide into fourths"
      }
    }
  ]
}
```

Output:
```json
{
  "@type": "Step",
  "workspace": {
    "@type": "WorkspaceData",
    "tangibles": [
      {
        "@type": "FracShape",
        "visual": 0,
        "shaded": [],
        "lcm": 8
      }
    ]
  }
}
```
*Note: state="undivided" → fractions omitted. lcm=8 because answer="1/4" means 4 sections → 4*2=8

**Example B: Shading interaction (verb="shade")**

Input:
```json
{
  "verb": "shade",
  "workspace": [
    {
      "type": "rectangle_bar",
      "sections": 3,
      "state": "divided",
      "shaded": []
    }
  ]
}
```

Output:
```json
{
  "@type": "Step",
  "workspace": {
    "@type": "WorkspaceData",
    "tangibles": [
      {
        "@type": "FracShape",
        "fractions": "1/3",
        "visual": 0,
        "shaded": [],
        "lcm": 24
      }
    ]
  }
}
```
*Note: sections=3 + state="divided" → fractions="1/3". lcm=24 (default for non-partition)*

### 6. Error Paths → Remediations with metadata

Transform error_path_generic steps into remediations array. Extract visual effects to metadata.events:

Input:
```json
"error_path_generic": {
  "steps": [
    {
      "scaffolding_level": "light",
      "dialogue": "Not quite..."
    },
    {
      "scaffolding_level": "medium",
      "dialogue": "Let's think...",
      "visual": {
        "effects": [
          {
            "animation": "pulse_sections",
            "description": "All sections pulse"
          }
        ]
      }
    },
    {
      "scaffolding_level": "heavy",
      "dialogue": "This is tricky...",
      "visual": {
        "effects": [
          {"animation": "label_sections", "description": "Labels appear"},
          {"animation": "shade_one", "description": "One section shades"}
        ]
      }
    }
  ]
}
```

Output:
```json
"remediations": [
  {
    "@type": "Remediation",
    "id": "light",
    "step": {
      "@type": "Step",
      "dialogue": "Not quite..."
    }
  },
  {
    "@type": "Remediation",
    "id": "medium",
    "step": {
      "@type": "Step",
      "metadata": {
        "events": [
          {"name": "pulse_sections", "description": "All sections pulse"}
        ]
      },
      "dialogue": "Let's think..."
    }
  },
  {
    "@type": "Remediation",
    "id": "heavy",
    "step": {
      "@type": "Step",
      "metadata": {
        "events": [
          {"name": "label_sections", "description": "Labels appear"},
          {"name": "shade_one", "description": "One section shades"}
        ]
      },
      "dialogue": "This is tricky..."
    }
  }
]
```

**Rules:**
- Extract event name from `animation` field, description stays as-is
- metadata is OPTIONAL - only add if visual effects exist
- Remediation IDs: "light", "medium", "heavy" (lowercase, in order)

### 7. Success Path → on_correct

Add success_path dialogue to prompt as `on_correct` field:

Input:
```json
"success_path": {
  "steps": [{"dialogue": "Perfect! You got it right."}]
}
```

Output (in prompt object):
```json
"on_correct": {
  "@type": "Step",
  "dialogue": "Perfect! You got it right."
}
```

If no success_path or empty, set `on_correct: null`.

### 8. Multiple Choice → choices

If input has `choices` array, add to prompt:

```json
"prompt": {
  "@type": "Prompt",
  "text": "...",
  "validator": {
    "@type": "MultipleChoiceValidator",
    "answer": [2]
  },
  "choices": {
    "@type": "WorkspaceChoices",
    "allow_multiple": false,
    "options": ["1/2", "1/3", "1/4"]
  }
}
```

**Note**: MCQs do NOT have a "tool" field.

## KEY TRANSFORMATION POINTS

1. **metadata in Sequence**: Include all fields from section 1 (problem_id, goal_id, goal_text, verb, variables_covered, plus placeholder mastery fields)
2. **Workspace structure**: Change workspace array → workspace object with tangibles array
3. **FracShape conversion**: state + sections → fractions field (see section 4)
4. **LCM calculation**: partition tasks use sections*2, others use 24
5. **Remove input fields**: id, type, state, position (not in Godot schema)
6. **Event metadata**: Extract animation name + description to metadata.events
7. **Remediation order**: Must be light, medium, heavy
8. **Tool mapping**: Use section 3 mappings (shade→paint, etc.)
9. **Validator selection**: Read correct_answer.context to determine type
10. **MCQ structure**: No tool field, use choices in prompt
11. **Answer extraction**: Use correct_answer.value only (context is for understanding)
12. **Text formatting**: Leave all text AS-IS (fractions like "3/4", vocabulary words unchanged). BBCode formatting will be applied in post-processing.

Return ONLY valid JSON with Godot schema structure.
"""

GODOT_FORMATTER_STRUCTURE = """
{
  "@type": "SequencePool",
  "metadata": {
    "goal_ids": [5],
    "variables_covered": [
      {"fractions": ["1/2", "1/3", "1/4", "1/6", "1/8"]}
    ]
  },
  "sequences": [
    {
      "@type": "Sequence",
      "metadata": {
        "@type": "SequenceMetadata",
        "problem_id": 123,
        "goal_id": 5,
        "goal_text": "The student can partition shapes into equal parts",
        "verb": "partition",
        "variables_covered": {"fractions": ["1/4"]},
        "mastery_tier": "2",
        "mastery_component": "PROCEDURAL",
        "mastery_verbs": ["APPLY"]
      },
      "steps": [
        {
          "@type": "Step",
          "dialogue": "...",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {"@type": "FracShape", "fractions": "1/4", "shaded": [], "lcm": 24}
            ]
          },
          "prompt": {
            "@type": "Prompt",
            "text": "...",
            "tool": "paint",
            "validator": {"@type": "ShadedPartsValidator", "answer": 2},
            "remediations": [
              {"@type": "Remediation", "id": "light", "step": {"@type": "Step", "dialogue": "..."}},
              {"@type": "Remediation", "id": "medium", "step": {"@type": "Step", "metadata": {"events": [{"name": "pulse", "description": "..."}]}, "dialogue": "..."}},
              {"@type": "Remediation", "id": "heavy", "step": {"@type": "Step", "metadata": {"events": [{"name": "label", "description": "..."}]}, "dialogue": "..."}}
            ],
            "on_correct": {"@type": "Step", "dialogue": "Success!"}
          }
        }
      ]
    }
  ]
}
"""