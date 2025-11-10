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
- Workspace: `"@type": "WorkspaceData"` 
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
- `select_tick` → `single_paint` (you can select only one tick at a time)
- `click_choice` → omit tool (MCQs don't use tools, only workspace.choices)

**Validator Selection:**

Read `correct_answer.context` to understand what's being validated, then determine appropriate validator:

- **Shading a proportion** (e.g., "shade 3/4") → `EqualShadedValidator` with fraction string answer
- **Shading a count** (e.g., "shade exactly 2 parts") → `ShadedPartsValidator` with integer answer
- **Part sizes after cutting** (e.g., "cut into thirds") → `FractionShapePartsValidator` with fraction string/array
- **Selecting tangible(s)** (e.g., "select the shape showing 1/2") → `SelectionValidator` with integer/array
- **Multiple choice** (e.g., "which represents 3/4?") → `MultipleChoiceValidator` with array of indices
- **Placing tick marks** (e.g., "place ticks at 1/3 and 2/3") → `PlaceTicksValidator` with numerator array **scaled to LCD**
  - **Selecting tick marks** (e.g., "select the tick at 2/6") → `SelectTicksValidator` with numerator array **scaled to LCD**

  **CRITICAL: LCD-Based Validator Answer Calculation**

  For `PlaceTicksValidator` and `SelectTicksValidator`, the answer array must be expressed as numerators on the LCD scale, NOT as sequential indices.

  **Formula for partitioning tasks:**
  - If partitioning into N equal parts (creating N intervals):
    - LCD = N × 2
    - Each tick position = (tick_index × 2) where tick_index goes from 1 to (N-1)
    - Answer array = [2, 4, 6, 8, ..., (N-1)×2]

  **Examples:**
  - **Sixths** (partition into 6 equal parts):
    - LCD = 12
    - Tick positions: 1/6, 2/6, 3/6, 4/6, 5/6
    - Answer = [2, 4, 6, 8, 10] (NOT [1, 2, 3, 4, 5])

  - **Eighths** (partition into 8 equal parts):
    - LCD = 16
    - Tick positions: 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8
    - Answer = [2, 4, 6, 8, 10, 12, 14] (NOT [1, 2, 3, 4, 5, 6, 7])

  - **Thirds** (partition into 3 equal parts):
    - LCD = 6
    - Tick positions: 1/3, 2/3
    - Answer = [2, 4] (NOT [1, 2])

  **For selecting specific ticks:**
  - Convert the fraction to LCD scale: tick at 3/6 with LCD=12 → numerator = 6
  - Answer = [6] (NOT [3])

See schema for validator field requirements and answer formats.

### 4. Tangible Conversions

**Common fields to remove from all tangibles:**
- `id`, `type`, `state`, `intervals`, `interval_pattern`, `description` (parse, then discard)

**FracShape (@type: "FracShape"):**
- `visual`: 0=rectangle/bar, 1=circle/pie, 2=grid
- `fractions`: Based on state + intervals:
  * `state="undivided"` → omit field (whole shape)
  * `state="divided_equal"` → single string `"1/N"` where N = intervals
  * `state="divided_unequal"` → array summing to 1, parse `interval_pattern`/`description`:
    - `"middle_larger"` + intervals=3 → `["1/4", "1/2", "1/4"]`
    - `"first_larger"` + intervals=3 → `["1/2", "1/4", "1/4"]`
    - Use denominators: 6, 8, 10, 12
- `shaded`: Array of section indices (e.g., `[0, 1]`)
- `lcm`: For cut tasks: intervals×2; others: 24

**NumberLine (@type: "NumberLine"):**
- `is_visible`: Always set to `true`
- `range`: Keep (e.g., `[0, 1]`)
- `tick_marks`: Generate based on state + intervals (like fractions for FracShape):
  * `state="undivided"` → `[0, 1]` (only endpoints)
  * `state="divided_equal"` → array with N+1 ticks where N = intervals
    - intervals=3 → `[0, "1/3", "2/3", 1]`
    - intervals=4 → `[0, "1/4", "2/4", "3/4", 1]`
  * `state="divided_unequal"` → array based on `interval_pattern`/`description`:
    - Parse pattern to determine tick positions (must match intervals count)
    - Example: `"middle_larger"` + intervals=3 → `[0, "1/4", "3/4", 1]`
 - `labelled`: Boolean array matching tick_marks length. **IMPORTANT: Omit this field entirely if using default behavior** (start and end ticks labeled, middle ticks unlabeled). Only include when you need custom label.
 - `shaded`: **Boolean array** matching tick_marks length (e.g., `[false, false, true, false]`). **IMPORTANT: Omit this field entirely if no ticks are highlighted** (don't include `"shaded": []`)
- `lcd`: For place_tick/select_tick tasks: intervals×2 (e.g., thirds → intervals=3 → lcd=6); others: 12


### 5. Example Transformations

**Example A: Multi-select interaction (verb="IDENTIFY", tool="multi_select")**

Input (from remediation generator - all in ONE step):
```json
{
  "problem_id": 2,
  "verb": "IDENTIFY",
  "goal": "The student can distinguish unit fractions from non-unit fractions",
  "goal_id": 4,
  "fractions": ["1/3", "1/4"],
  "steps": [
    {
      "dialogue": "Unit fractions have exactly one part shaded. Which of these bars show unit fractions?",
      "prompt": "Select all bars showing unit fractions.",
      "interaction_tool": "multi_select",
      "workspace": [
        {
          "id": "bar_1",
          "type": "rectangle_bar",
          "state": "divided_equal",
          "intervals": 3,
          "shaded": [0]
        },
        {
          "id": "bar_2",
          "type": "rectangle_bar",
          "state": "divided_equal",
          "intervals": 3,
          "shaded": [0, 1]
        }
      ],
      "correct_answer": {
        "value": ["bar_1"],
        "context": "Bar 1 is a unit fraction (1/3) with exactly one part shaded"
      },
      "student_attempts": {
        "success_path": {
          "dialogue": "You identified the unit fraction!"
        },
        "error_path_generic": {
          "steps": [
            {
              "scaffolding_level": "light",
              "dialogue": "Not quite. Look for bars with exactly one part shaded."
            },
            {
              "scaffolding_level": "medium",
              "dialogue": "Let's think about this together.",
              "visual": {
                "effects": [
                  {
                    "animation": "pulse_shaded_section",
                    "description": "The single shaded section in bar 1 pulses"
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ]
}
```

Output:
```json
{
  "@type": "Step",
  "dialogue": "Unit fractions have exactly one part shaded. Which of these bars show unit fractions?",
  "workspace": {
    "@type": "WorkspaceData",
    "tangibles": [
      {
        "@type": "FracShape",
        "visual": 0,
        "fractions": "1/3",
        "shaded": [0],
        "lcm": 24
      },
      {
        "@type": "FracShape",
        "visual": 0,
        "fractions": "1/3",
        "shaded": [0, 1],
        "lcm": 24
      }
    ]
  },
  "prompt": {
    "@type": "Prompt",
    "text": "Select all bars showing unit fractions",
    "tool": "multi_select",
    "validator": {
      "@type": "SelectionValidator",
      "answer": [0]
    },
    "remediations": [
      {
        "@type": "Remediation",
        "id": "light",
        "step": {
          "@type": "Step",
          "dialogue": "Not quite. Look for bars with exactly one part shaded."
        }
      },
      {
        "@type": "Remediation",
        "id": "medium",
        "step": {
          "@type": "Step",
          "metadata": {
            "events": [
              {"name": "pulse_shaded_section", "description": "The single shaded section in bar 1 pulses"}
            ]
          },
          "dialogue": "Let's think about this together."
        }
      }
    ],
    "on_correct": {
      "@type": "Step",
      "dialogue": "You identified the unit fraction!"
    }
  }
}
```

**Example B: Selection interaction with choices (verb="COMPARE", tool="click_choice")**

Input (from remediation generator):
```json
{
  "problem_id": 3,
  "verb": "COMPARE",
  "goal": "The student can distinguish unit fractions from non-unit fractions",
  "goal_id": 4,
  "fractions": ["1/4"],
  "steps": [
    {
      "dialogue": "Look at this bar. What makes it different from a unit fraction?",
      "prompt": "Explain why this is not a unit fraction.",
      "interaction_tool": "click_choice",
      "workspace": [
        {
          "id": "bar_center",
          "type": "rectangle_bar",
          "state": "divided_equal",
          "intervals": 4,
          "shaded": [0, 1, 2]
        }
      ],
      "choices": [
        {"id": "a", "text": "It has unequal parts"},
        {"id": "b", "text": "More than one part is shaded"},
        {"id": "c", "text": "It has too many parts"}
      ],
      "correct_answer": {
        "value": "b",
        "context": "This bar has 3 parts shaded, making it 3/4, not a unit fraction"
      },
      "student_attempts": {
        "success_path": {
          "dialogue": "That's right. Unit fractions have only one part shaded."
        }
      }
    }
  ]
}
```

Output (keep all components together in ONE step):
```json
{
  "@type": "Step",
  "dialogue": "Look at this bar. What makes it different from a unit fraction?",
  "workspace": {
    "@type": "WorkspaceData",
    "tangibles": [
      {
        "@type": "FracShape",
        "visual": 0,
        "fractions": "1/4",
        "shaded": [0, 1, 2],
        "lcm": 24
      }
    ]
  },
  "prompt": {
    "@type": "Prompt",
    "text": "Explain why this is not a unit fraction",
    "validator": {
      "@type": "MultipleChoiceValidator",
      "answer": [1]
    },
    "choices": {
      "@type": "WorkspaceChoices",
      "allow_multiple": false,
      "options": ["It has unequal parts", "More than one part is shaded", "It has too many parts"]
    },
    "remediations": [],
    "on_correct": {
      "@type": "Step",
      "dialogue": "That's right. Unit fractions have only one part shaded."
    }
  }
}
```

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

1. **STEP CONSOLIDATION (CRITICAL)**: The input already has dialogue, workspace, and prompt all in ONE step. KEEP THEM TOGETHER in the output.

   Each step can contain one of all interaction components:
   - dialogue (teacher instruction)
   - workspace (tangibles the student sees)
   - prompt (the student's task, including tool, validator, remediations, on_correct)

   ```json
   {
     "@type": "Step",
     "dialogue": "Here's a bar. Divide it into 2 parts.",
     "workspace": {...},
     "prompt": {...}
   }
   ```
2. **metadata in Sequence**: Include all fields from section 1 (problem_id, goal_id, goal_text, verb, variables_covered, plus placeholder mastery fields)
3. **Workspace structure**: Change workspace array → workspace object with tangibles array
4. **FracShape conversion**: state + sections → fractions field (see section 4)
5. **LCM calculation**: partition tasks use sections*2, others use 24
6. **Remove input fields**: id, type, state, position (not in Godot schema)
7. **Event metadata**: Extract animation name + description to metadata.events
8. **Remediation order**: Must be light, medium, heavy
9. **Tool mapping**: Use section 3 mappings (shade→paint, etc.)
10. **Validator selection**: Read correct_answer.context to determine type
11. **MCQ structure**: No tool field, use choices in prompt
12. **Answer extraction**: Use correct_answer.value only (context is for understanding)
13. **Text formatting**: Leave all text AS-IS (fractions like "3/4", vocabulary words unchanged). BBCode formatting will be applied in post-processing.

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