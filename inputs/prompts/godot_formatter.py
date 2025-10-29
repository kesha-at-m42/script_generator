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

### 1. Add @type Annotations
Every object needs a @type field for deserialization (see schema for complete list):
- Root: `"@type": "SequencePool"`
- Sequence: `"@type": "Sequence"` + metadata object
- Step: `"@type": "Step"`
- Workspace: `"@type": "WorkspaceData"` (NOT "Workspace")
- Tangibles: `"@type": "FracShape"` or `"@type": "NumberLine"`
- Prompt, Validator, Remediation, Choices: Use appropriate @type (see schema)

### 2. Type Mappings

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

### 3. FracShape State Conversion

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

### 4. Example Transformations

**Example A: Partition/cut interaction (verb="partition", tool="cut")**

Input:
```json
{{
  "verb": "partition",
  "steps": [
    {{
      "workspace": [
        {{
          "type": "rectangle_bar",
          "sections": 1,
          "state": "undivided",
          "shaded": []
        }}
      ]
    }},
    {{
      "prompt": "Click to cut",
      "interaction_tool": "cut",
      "correct_answer": {{
        "value": "1/4",
        "context": "Divide into fourths"
      }}
    }}
  ]
}}
```

Output:
```json
{{
  "@type": "Step",
  "workspace": {{
    "@type": "WorkspaceData",
    "tangibles": [
      {{
        "@type": "FracShape",
        "visual": 0,
        "shaded": [],
        "lcm": 8
      }}
    ]
  }}
}}
```
*Note: state="undivided" → fractions omitted. lcm=8 because answer="1/4" means 4 sections → 4*2=8

**Example B: Shading interaction (verb="shade")**

Input:
```json
{{
  "verb": "shade",
  "workspace": [
    {{
      "type": "rectangle_bar",
      "sections": 3,
      "state": "divided",
      "shaded": []
    }}
  ]
}}
```

Output:
```json
{{
  "@type": "Step",
  "workspace": {{
    "@type": "WorkspaceData",
    "tangibles": [
      {{
        "@type": "FracShape",
        "fractions": "1/3",
        "visual": 0,
        "shaded": [],
        "lcm": 24
      }}
    ]
  }}
}}
```
*Note: sections=3 + state="divided" → fractions="1/3". lcm=24 (default for non-partition)*

### 5. Error Paths → Remediations with @metadata

Transform error_path_generic steps into remediations array. Extract visual effects to @metadata.events:

Input:
```json
"error_path_generic": {{
  "steps": [
    {{
      "scaffolding_level": "light",
      "dialogue": "Not quite..."
    }},
    {{
      "scaffolding_level": "medium",
      "dialogue": "Let's think...",
      "visual": {{
        "effects": [
          {{
            "animation": "pulse_sections",
            "description": "All sections pulse"
          }}
        ]
      }}
    }},
    {{
      "scaffolding_level": "heavy",
      "dialogue": "This is tricky...",
      "visual": {{
        "effects": [
          {{"animation": "label_sections", "description": "Labels appear"}},
          {{"animation": "shade_one", "description": "One section shades"}}
        ]
      }}
    }}
  ]
}}
```

Output:
```json
"remediations": [
  {{
    "@type": "Remediation",
    "id": "light",
    "step": {{
      "@type": "Step",
      "dialogue": "Not quite..."
    }}
  }},
  {{
    "@type": "Remediation",
    "id": "medium",
    "step": {{
      "@type": "Step",
      "@metadata": {{
        "events": [
          {{"name": "pulse_sections", "description": "All sections pulse"}}
        ]
      }},
      "dialogue": "Let's think..."
    }}
  }},
  {{
    "@type": "Remediation",
    "id": "heavy",
    "step": {{
      "@type": "Step",
      "@metadata": {{
        "events": [
          {{"name": "label_sections", "description": "Labels appear"}},
          {{"name": "shade_one", "description": "One section shades"}}
        ]
      }},
      "dialogue": "This is tricky..."
    }}
  }}
]
```

**Rules:**
- Extract event name from `animation` field, description stays as-is
- @metadata is OPTIONAL - only add if visual effects exist
- Remediation IDs: "light", "medium", "heavy" (lowercase, in order)

### 6. Success Path → on_correct

Add success_path dialogue to prompt as `on_correct` field:

Input:
```json
"success_path": {{
  "steps": [{{"dialogue": "Perfect! You got it right."}}]
}}
```

Output (in prompt object):
```json
"on_correct": {{
  "@type": "Step",
  "dialogue": "Perfect! You got it right."
}}
```

If no success_path or empty, set `on_correct: null`.

### 7. Multiple Choice → choices

If input has `choices` array, add to prompt:

```json
"prompt": {{
  "@type": "Prompt",
  "text": "...",
  "validator": {{
    "@type": "MultipleChoiceValidator",
    "answer": [2]
  }},
  "choices": {{
    "@type": "WorkspaceChoices",
    "allow_multiple": false,
    "options": ["1/2", "1/3", "1/4"]
  }}
}}
```

**Note**: MCQs do NOT have a "tool" field.

### 8. Fraction Formatting in Dialogue

ALL fractions in dialogue must use BBCode format for rendering:

**Format:** `[fraction numerator=N denominator=D]text[/fraction]`

**Examples:**
- `3/4` → `[fraction numerator=3 denominator=4]three fourths[/fraction]`
- `1/2` → `[fraction numerator=1 denominator=2]one half[/fraction]`
- `2/3` → `[fraction numerator=2 denominator=3]two thirds[/fraction]`

Apply to ALL dialogue in steps, remediations, and on_correct.

### 9. Vocabulary Tag Formatting

Wrap vocabulary terms with `[vocab]...[/vocab]` tags for emphasis and tracking.

**Vocabulary terms to wrap:** {vocabulary_terms}

**Rules:**
- Only wrap terms that appear in the provided vocabulary list
- Wrap the exact term as it appears (case-sensitive)
- Don't wrap if already inside another tag (e.g., inside [fraction])
- Apply to ALL dialogue in steps, remediations, and on_correct

**Examples:**
- "equal parts" → `[vocab]equal parts[/vocab]`
- "partition the bar" → `[vocab]partition[/vocab] the bar`
- "shade one half" → `[vocab]shade[/vocab] [fraction numerator=1 denominator=2]one half[/fraction]`

## KEY TRANSFORMATION POINTS

1. **@metadata in Sequence**: Add problem_id, difficulty, verb, goal from input
2. **Workspace structure**: Change workspace array → workspace object with tangibles array
3. **FracShape conversion**: state + sections → fractions field (see section 3)
4. **LCM calculation**: partition tasks use sections*2, others use 24
5. **Remove input fields**: id, type, state, position (not in Godot schema)
6. **Event metadata**: Extract animation name + description to @metadata.events
7. **Fraction BBCode**: Replace all "N/D" with BBCode format in dialogue
8. **Vocabulary tags**: Wrap vocabulary terms with [vocab]...[/vocab] tags
9. **Remediation order**: Must be light, medium, heavy
10. **Tool mapping**: Use section 2 mappings (shade→paint, etc.)
11. **Validator selection**: Read correct_answer.context to determine type
12. **MCQ structure**: No tool field, use choices in prompt
13. **Answer extraction**: Use correct_answer.value only (context is for understanding)

Return ONLY valid JSON with Godot schema structure.
"""

GODOT_FORMATTER_STRUCTURE = """
{
  "@type": "SequencePool",
  "@metadata": {
  "goal_ids": 5,
  "variables_covered": [
    {"fractions": ["1/2", "1/3", "1/4", "1/6", "1/8"]}
  ],
  "sequences": [
    {
      "@type": "Sequence",
      "@metadata": {
        "problem_id": 1,
        "difficulty": 0,
        "verb": "partition",
        "goal": "Students can partition shapes",
        "goal_id": 1,
        "fractions": []
      },
      "steps": [
        {
          "@type": "Step",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {"@type": "FracShape", "fractions": "1/4", "shaded": [], "lcm": 24}
            ]
          }
        },
        {
          "@type": "Step",
          "dialogue": "...",
          "prompt": {
            "@type": "Prompt",
            "text": "...",
            "tool": "paint",
            "validator": {"@type": "ShadedPartsValidator", "answer": 2},
            "remediations": [
              {"@type": "Remediation", "id": "light", "step": {"@type": "Step", "dialogue": "..."}},
              {"@type": "Remediation", "id": "medium", "step": {"@type": "Step", "@metadata": {"events": [{"name": "pulse", "description": "..."}]}, "dialogue": "..."}},
              {"@type": "Remediation", "id": "heavy", "step": {"@type": "Step", "@metadata": {"events": [{"name": "label", "description": "..."}]}, "dialogue": "..."}}
            ],
            "on_correct": {"@type": "Step", "dialogue": "Success!"}
          }
        }
      ]
    }
  ]
}
"""
