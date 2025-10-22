"""
Godot Formatter Prompt Configuration
Transforms remediation sequences to Godot-processable schema

This is an AI-powered transformation that understands the semantic structure
and produces properly formatted Godot sequences.
"""

GODOT_FORMATTER_ROLE = """You are an expert in transforming educational content schemas into Godot game engine format.

Your task: Transform remediation sequences into Godot-processable format that matches the exact specification with @type annotations, proper component structure, and Event tags."""

GODOT_FORMATTER_DOCS = ["godot_schema_spec.md"]

GODOT_FORMATTER_EXAMPLES = [
    {
        "description": "Example transformation from remediation schema to Godot schema",
        "input": """{
  "sequences": [
    {
      "problem_id": 1,
      "difficulty": 0,
      "verb": "partition",
      "goal": "Students can partition shapes into equal parts",
      "steps": [
        {
          "dialogue": "Here's a rectangle divided into 3 equal parts.",
          "workspace": [
            {
              "id": "rect_1",
              "type": "rectangle_bar",
              "sections": 3,
              "state": "divided",
              "shaded": [],
              "position": "center"
            }
          ]
        },
        {
          "dialogue": "Shade 1 part to show one-third.",
          "prompt": "Click to shade 1 part",
          "interaction_tool": "shade",
          "workspace_context": {
            "tangibles_present": ["rect_1"],
            "note": "Rectangle with 3 equal horizontal sections, all unshaded"
          },
          "correct_answer": {
            "value": "1/3",
            "context": "Shade 1 out of 3 parts to represent one-third"
          }
        }
      ],
      "student_attempts": {
        "success_path": {
          "steps": [
            {
              "dialogue": "That's it! You showed one-third perfectly."
            }
          ]
        },
        "error_path_generic": {
          "steps": [
            {
              "scaffolding_level": "light",
              "dialogue": "Not quite. We need to shade exactly 1 part.",
              "workspace_context": {
                "tangibles_present": ["rect_1"]
              },
              "visual": null
            },
            {
              "scaffolding_level": "medium",
              "dialogue": "Let's think about this together. We want to show one-third, which means 1 part out of 3 total parts.",
              "workspace_context": {
                "tangibles_present": ["rect_1"]
              },
              "visual": {
                "effects": [
                  {
                    "target": "rect_1",
                    "type": "highlight",
                    "animation": "pulse_sections",
                    "description": "All three sections pulse to show they are separate parts"
                  }
                ]
              }
            },
            {
              "scaffolding_level": "heavy",
              "dialogue": "This is tricky, so let's work through it together. One-third means 1 part out of 3. See these three parts? Click any one of them to shade it. There we go.",
              "workspace_context": {
                "tangibles_present": ["rect_1"]
              },
              "visual": {
                "effects": [
                  {
                    "target": "rect_1",
                    "type": "annotation",
                    "animation": "label_sections",
                    "description": "Labels appear showing '1', '2', '3' on each section"
                  },
                  {
                    "target": "rect_1",
                    "type": "demonstration",
                    "animation": "shade_one_section",
                    "description": "One section shades automatically to demonstrate"
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ]
}""",
        "output": """{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "@metadata": {
        "problem_id": 1,
        "difficulty": 0,
        "verb": "partition",
        "goal": "Students can partition shapes into equal parts"
      },
      "steps": [
        {
          "@type": "Step",
          "dialogue": "Here's a rectangle divided into 3 equal parts.",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {
                "@type": "FracShape",
                "fractions": "1/3",
                "visual": 0,
                "shaded": [],
                "lcm": 6,
                "is_read_only": false
              }
            ]
          }
        },
        {
          "@type": "Step",
          "dialogue": "Shade 1 part to show [fraction numerator=1 denominator=3]one third[/fraction].",
          "prompt": {
            "@type": "Prompt",
            "text": "Click to shade 1 part",
            "tool": "paint",
            "validator": {
              "@type": "EqualShadedValidator",
              "answer": "1/3"
            },
            "remediations": [
              {
                "@type": "Remediation",
                "id": "light",
                "step": {
                  "@type": "Step",
                  "dialogue": "Not quite. We need to shade exactly 1 part."
                }
              },
              {
                "@type": "Remediation",
                "id": "medium",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:pulse_sections]Let's think about this together. We want to show [fraction numerator=1 denominator=3]one third[/fraction], which means 1 part out of 3 total parts."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:label_sections][event:shade_one_section]This is tricky, so let's work through it together. [fraction numerator=1 denominator=3]One third[/fraction] means 1 part out of 3. See these three parts? Click any one of them to shade it. There we go."
                }
              }
            ],
            "on_correct": {
              "@type": "Step",
              "dialogue": "That's it! You showed [fraction numerator=1 denominator=3]one third[/fraction] perfectly."
            }
          }
        }
      ]
    }
  ]
}"""
    }
]

GODOT_FORMATTER_INSTRUCTIONS = """
## YOUR TASK

Transform these remediation sequences to Godot-processable format:

<remediation_sequences>
{remediation_context}
</remediation_sequences>

## TRANSFORMATION RULES

### 1. Add @type Annotations
Every object needs a @type field:
- Root: `"@type": "SequencePool"`
- Sequence: `"@type": "Sequence"`
- Sequence @metadata: `"@metadata": {{"problem_id": ..., "difficulty": ..., "verb": "...", "goal": "..."}}`
- Step: `"@type": "Step"`
- Workspace: `"@type": "WorkspaceData"` (NOT "Workspace")
- Prompt: `"@type": "Prompt"`
- Validator: `"@type": "<ValidatorType>"` (see Type Mappings below)
- Remediation: `"@type": "Remediation"`
- Tangibles: `"@type": "FracShape"` or `"@type": "NumberLine"`
- Choices: `"@type": "WorkspaceChoices"` (when used in prompt.choices)

### 2. Type Mappings

**Tangible Types:**
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

Read `correct_answer.context` to understand what's being validated, then use the schema to determine the appropriate validator based on:

**What's being checked:**
- **Shading a proportion** (e.g., "shade 3/4") → Answer: fraction string → Requires: FracShape.shaded
- **Shading a count** (e.g., "shade exactly 2 parts") → Answer: integer → Requires: FracShape.shaded
- **Part sizes after cutting** (e.g., "cut into thirds") → Answer: fraction string or array → Requires: FracShape.fractions
- **Selecting tangible(s)** (e.g., "select the shape showing 1/2") → Answer: integer or array → Requires: multiple tangibles
- **Clicking choice buttons** (e.g., "which represents 3/4?") → Answer: array of indices → Requires: choices array in input
- **Placing tick marks** (e.g., "place ticks at 1/3 and 2/3") → Answer: array of numerators → Requires: NumberLine
- **Selecting tick marks** (e.g., "select the tick at 2/6") → Answer: array of numerators → Requires: NumberLine with existing ticks

**Key principle:** The context describes the action. The answer type + tangible properties determine which validator to use. Refer to godot_schema_spec.md for complete validator details.

### 3. Structure Transformation

**FracShape Conversion Rules:**

Input tangible fields (standardized schema):
- `type`: Shape type (rectangle_bar, circle, grid, etc.)
- `sections`: Integer count (1 = undivided, 2+ = divided)
- `state`: Visual state ("undivided", "divided", "divided_unequal")
- `shaded`: Array of 0-based indices for shaded sections
- `position`: Screen location (center, top, bottom, etc.)

Output FracShape fields:
- `@type`: Always "FracShape" for fraction shapes
- `visual`: Shape rendering (0=rectangle/bar, 1=circle/pie, 2=grid)
- `fractions`: Determined by state and sections:
  * state="undivided" (sections=1) → `"1/1"`
  * state="divided" (equal parts) → `"1/N"` where N = sections
    - sections=2 → `"1/2"`
    - sections=3 → `"1/3"`
    - sections=4 → `"1/4"`
    - sections=6 → `"1/6"`
  * state="divided_unequal" → array of fractions (must sum to 1)
    - sections=3 → `["1/2", "1/4", "1/4"]` (unequal thirds)
    - sections=4 → `["1/8", "4/8", "3/8"]` (unequal fourths)
    - sections=5 → `["2/8", "2/8", "1/8", "1/8", "2/8"]` (unequal fifths)
- `shaded`: Keep as-is (array of 0-based indices)
- `is_read_only`: Typically false for interactive tangibles
- `lcm`: LCM calculation:
  * For "cut" tool OR if verb is "partition"/"divide"/"cut": 
    - If shape is undivided (sections=1), look at correct_answer to determine target sections
    - Example: answer="1/2" means creating 2 sections → lcm = 2 × 2 = 4
    - Example: answer="1/3" means creating 3 sections → lcm = 3 × 2 = 6
    - If shape is already divided, use existing sections count → lcm = sections × 2
  * For all other interactions: lcm = 24 (default)

Fields to remove (not in Godot schema):
- `type` (replaced by @type)
- `id` (not needed)
- `state` (used to determine fractions, then removed)
- `position` (not in Godot schema)

**Example Transformations:**

**Example A: Partition/cut interaction (verb="partition", tool="cut")**

Input:
```json
{{
  "verb": "partition",
  "steps": [
    {{
      "dialogue": "Here's a rectangle.",
      "workspace": [
        {{
          "id": "rect_1",
          "type": "rectangle_bar",
          "sections": 1,
          "state": "undivided",
          "shaded": [],
          "position": "center"
        }}
      ]
    }},
    {{
      "dialogue": "Divide it into 4 equal parts.",
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
  "steps": [
    {{
      "@type": "Step",
      "workspace": {{
        "@type": "WorkspaceData",
        "tangibles": [
          {{
            "@type": "FracShape",
            "visual": 0,
            "shaded": [],
            "lcm": 8,
            "is_read_only": false
          }}
        ]
      }},
      "dialogue": "Here's a rectangle."
    }}
  ]
}}
```
Note: 
- state="undivided" (sections=1) → fractions omitted (whole shape)
- lcm=8 because verb="partition" AND correct_answer="1/4" indicates creating 4 sections, so lcm = 4 × 2 = 8

**Example B: Shading interaction (no partition verb)**

Input:
```json
{{
  "verb": "shade",
  "steps": [
    {{
      "dialogue": "Here's a rectangle divided into 3 equal parts.",
      "workspace": [
        {{
          "id": "rect_1",
          "type": "rectangle_bar",
          "sections": 3,
          "state": "divided",
          "shaded": [],
          "position": "center"
        }}
      ]
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
        "lcm": 24,
        "is_read_only": false
      }}
    ]
  }},
  "dialogue": "Here's a rectangle divided into 3 equal parts."
}}
```
Note: 
- type="rectangle_bar" → @type="FracShape" with visual=0
- sections=3 + state="divided" → fractions="1/3" (equal thirds)
- lcm=24 (default for non-partition interactions - verb is "shade", not "partition")
- Removed fields: id, type, state, position

**Input Part 2 (interaction):**
```json
{{
  "dialogue": "Shade 3 out of 4 parts...",
  "prompt": "Click to shade 3 parts",
  "interaction_tool": "shade",
  "workspace_context": {{...}},
  "correct_answer": {{
    "value": "3/4",
    "context": "Shade 3 out of 4 parts to show three-fourths"
  }}
}}
```

**Output:**
```json
{{
  "@type": "Step",
  "dialogue": "Shade 3 out of 4 parts...",
  "prompt": {{
    "@type": "Prompt",
    "text": "Click to shade 3 parts",
    "tool": "paint",
    "validator": {{
      "@type": "EqualShadedValidator",
      "answer": "3/4"
    }},
    "remediations": [...]
  }}
}}
```

**Note:** The validator type (EqualShadedValidator) was chosen by reading the context "Shade 3 out of 4 parts" which indicates a shading action, not by looking at the interaction_tool field.

### 4. Error Paths → Remediations with Event Tags + @metadata

Transform error_path_generic steps into remediations array with event tags and optional @metadata:

**Input error path:**
```json
"error_path_generic": {{
  "steps": [
    {{
      "scaffolding_level": "light",
      "dialogue": "Not quite...",
      "visual": null
    }},
    {{
      "scaffolding_level": "medium",
      "dialogue": "Let's think...",
      "visual": {{
        "effects": [
          {{
            "type": "highlight",
            "animation": "pulse_sections",
            "description": "All three sections pulse to show they are separate parts"
          }}
        ]
      }}
    }},
    {{
      "scaffolding_level": "heavy",
      "dialogue": "This is tricky...",
      "visual": {{
        "effects": [
          {{
            "type": "annotation",
            "animation": "label_sections",
            "description": "Labels appear showing '1', '2', '3' on each section"
          }},
          {{
            "type": "demonstration",
            "animation": "shade_one_section",
            "description": "One section shades automatically to demonstrate"
          }}
        ]
      }}
    }}
  ]
}}
```

**Output remediations array:**
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
          {{
            "name": "pulse_sections",
            "description": "All three sections pulse to show they are separate parts"
          }}
        ]
      }},
      "dialogue": "[event:pulse_sections]Let's think..."
    }}
  }},
  {{
    "@type": "Remediation",
    "id": "heavy",
    "step": {{
      "@type": "Step",
      "@metadata": {{
        "events": [
          {{
            "name": "label_sections",
            "description": "Labels appear showing '1', '2', '3' on each section"
          }},
          {{
            "name": "shade_one_section",
            "description": "One section shades automatically to demonstrate"
          }}
        ]
      }},
      "dialogue": "[event:label_sections][event:shade_one_section]This is tricky..."
    }}
  }}
]
```

**Rules:**
- Extract animation name from each effect → prepend as [event:...] tag to dialogue
- Extract description from each effect → add to @metadata.events array
- @metadata is OPTIONAL - only add if visual effects exist (medium/heavy)
- Light remediations have no visual effects, so no @metadata needed
- Remediation IDs must be "light", "medium", "heavy" (lowercase, in that order)

### 5. Success Path → on_correct

The success path should be added to the prompt as `on_correct` field:

Input:
```json
"success_path": {{
  "steps": [{{"dialogue": "Perfect! You got it right."}}]
}}
```

Output (add to prompt):
```json
{{
  "@type": "Step",
  "dialogue": "Shade 1 part...",
  "prompt": {{
    "@type": "Prompt",
    "text": "Click to shade 1 part",
    "tool": "paint",
    "validator": {{...}},
    "remediations": [...],
    "on_correct": {{
      "@type": "Step",
      "dialogue": "Perfect! You got it right."
    }}
  }}
}}
```

**Important:** If success_path has only dialogue, include it in `on_correct`. If no success_path, set `on_correct` to null.

### 6. Choices (Multiple Choice)

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
    "options": ["1/2", "1/3", "1/4", "1/8"]
  }},
  "remediations": [...]
}}
```
**Note**: MCQs do NOT have a "tool" field. Choices are part of the prompt object for rendering.

### 7. Fraction Formatting in Dialogue

ALL fractions in dialogue text must use the special BBCode format for proper rendering:

**Format:** `[fraction numerator=N denominator=D]text representation[/fraction]`

**Examples:**
- `3/4` → `[fraction numerator=3 denominator=4]three fourths[/fraction]`
- `1/2` → `[fraction numerator=1 denominator=2]one half[/fraction]`
- `2/3` → `[fraction numerator=2 denominator=3]two thirds[/fraction]`
- `1/4` → `[fraction numerator=1 denominator=4]one fourth[/fraction]`

**Rules:**
- Replace ALL fraction notation (like "1/3", "2/4") with the BBCode format
- Use the spelled-out text version between the tags (e.g., "three fourths")
- Apply this to dialogue in ALL steps, remediations, and on_correct messages

**Example transformation:**
- Input: `"dialogue": "Shade 1/3 of the rectangle"`
- Output: `"dialogue": "Shade [fraction numerator=1 denominator=3]one third[/fraction] of the rectangle"`

- Input: `"dialogue": "That's it! You showed 1/3 perfectly."`
- Output: `"dialogue": "That's it! You showed [fraction numerator=1 denominator=3]one third[/fraction] perfectly."`

## KEY POINTS

1. **@metadata field**: Each Sequence must have @metadata with problem_id, difficulty, verb, and goal from input
2. **Workspace rename**: Change "workspace" array → "workspace" object with "tangibles" array and optional "choices"
3. **FracShape conversion**: ALL fraction shapes become FracShape with visual property (0=rectangle/bar, 1=circle/pie, 2=grid). See Structure Transformation section for complete conversion rules (sections + state → fractions, lcm calculation)
4. **Field removal**: Remove "type", "id", "state", "position" from input tangibles (not in Godot schema)
5. **Success path handling**: Add success_path dialogue to prompt.on_correct (not as separate step)
6. **Event tags + @metadata**: Extract event names for [event:...] tags AND descriptions for @metadata.events array (optional, only if visual effects exist)
7. **Fraction formatting**: ALL fractions in dialogue must use `[fraction numerator=N denominator=D]text[/fraction]` BBCode format
8. **Remediation IDs**: Must be "light", "medium", or "heavy" (lowercase)
9. **Tool mapping**: Use interaction_tool to map Godot tool (shade→paint, cut→cut, select→select, multi_select→multi_select, place_tick→place_tick, click_choice→(no tool))
10. **Validator selection**: Analyze workspace_context.tangibles_present and correct_answer.context to choose validator
11. **MCQ choices**: Choices go ONLY in prompt.choices
12. **Answer object structure**: Input has correct_answer.value (the actual answer) and correct_answer.context (explanation). Use context to understand what validator is needed, then use only the value in the output validator

Return ONLY valid JSON with the Godot schema structure.
"""

GODOT_FORMATTER_STRUCTURE = """
{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "@metadata": {
        "problem_id": 1,
        "difficulty": 0,
        "verb": "partition",
        "goal": "Students can partition shapes into equal parts"
      },
      "steps": [
        {
          "@type": "Step",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {
                "@type": "FracShape",
                "fractions": "1/4",
                "shaded": [],
                "lcm": 24,
                "is_read_only": false
              },
              {
                "@type": "NumberLine",
                "lcd": 6,
                "tick_marks": [0, "1/6", "2/6", 1],
                "labelled": [true, false, false, true],
                "is_read_only": [true, false, false, true]
              }
            ]
          },
          "dialogue": "..."
        },
        {
          "@type": "Step",
          "dialogue": "...",
          "prompt": {
            "@type": "Prompt",
            "text": "...",
            "tool": "paint",
            "validator": {
              "@type": "ShadedPartsValidator",
              "answer": 2
            },
            "choices": {
              "@type": "WorkspaceChoices",
              "allow_multiple": false,
              "options": ["1/2", "1/3", "1/4"]
            },
            "remediations": [
              {
                "@type": "Remediation",
                "id": "light",
                "step": {
                  "@type": "Step",
                  "dialogue": "..."
                }
              },
              {
                "@type": "Remediation",
                "id": "medium",
                "step": {
                  "@type": "Step",
                  "@metadata": {
                    "events": [
                      {
                        "name": "pulse_sections",
                        "description": "All sections pulse to show they are separate parts"
                      }
                    ]
                  },
                  "dialogue": "[event:pulse_sections]..."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "@metadata": {
                    "events": [
                      {
                        "name": "label_sections",
                        "description": "Labels appear on each section"
                      },
                      {
                        "name": "shade_one_section",
                        "description": "One section becomes shaded to demonstrate"
                      }
                    ]
                  },
                  "dialogue": "[event:label_sections][event:shade_one_section]..."
                }
              }
            ],
            "on_correct": {
              "@type": "Step",
              "dialogue": "Success message"
            }
          }
        }
      ]
    }
  ]
}
"""
