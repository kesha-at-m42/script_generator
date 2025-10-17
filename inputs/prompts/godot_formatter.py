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
              "orientation": "horizontal",
              "state": "divided",
              "shaded": [],
              "position": "center"
            }
          ]
        },
        {
          "dialogue": "Shade 1 part to show one-third.",
          "prompt": "Click to shade 1 part",
          "interaction_tool": "click_sections",
          "workspace_context": {
            "tangibles_present": ["rect_1"],
            "note": "Rectangle with 3 equal horizontal sections, all unshaded"
          },
          "correct_answer": [1]
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
          "dialogue": "Shade 1 part to show one-third.",
          "prompt": {
            "@type": "Prompt",
            "text": "Click to shade 1 part",
            "tool": "paint",
            "validator": {
              "@type": "ShadedPartsValidator",
              "answer": 1
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
                  "dialogue": "[event:pulse_sections]Let's think about this together. We want to show one-third, which means 1 part out of 3 total parts."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:label_sections][event:shade_one_section]This is tricky, so let's work through it together. One-third means 1 part out of 3. See these three parts? Click any one of them to shade it. There we go."
                }
              }
            ],
            "on_correct": {
              "@type": "Step",
              "dialogue": "That's it! You showed one-third perfectly."
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
- Choices: `"@type": "WorkspaceChoices"`

### 2. Type Mappings

**Tangible Types:**
ALL fraction shapes use unified `FracShape` type:
- `rectangle_bar` → `"@type": "FracShape"` with `"visual": 0`
- `square` → `"@type": "FracShape"` with `"visual": 2`
- `circle` → `"@type": "FracShape"` with `"visual": 1`
- `fraction_bar` → `"@type": "FracShape"` with `"visual": 0`
- `number_line` → `"@type": "NumberLine"` (unchanged)

**FracShape Conversion:**
- If tangible has uniform sections (e.g., 4 equal parts), use: `"fractions": "1/4"`
- If tangible has non-uniform sections, use array: `"fractions": ["1/4", "1/4", "1/2"]`
- visual: 0=rectangle/bar, 1=circle, 2=square
- Remove "type", "id", "orientation", "state", "position" fields
- Keep: shaded (array of indices)
- Add: is_read_only (typically false)
- Add: lcm - **IMPORTANT LCM CALCULATION:**
  * For "cut" tool OR if verb is "partition"/"divide"/"cut": lcm = sections × 2 (double the parts)
  * Example: 3 sections → lcm = 6, 4 sections → lcm = 8
  * For all other interactions: lcm = 24 (default)

**Validator Types (based on interaction_tool):**
- `click_sections` / `paint` → `"@type": "ShadedPartsValidator"` (answer: integer count)
- `click_sections` / `paint` → `"@type": "EqualShadedValidator"` (answer: fraction string like "1/4")
- `select` → `"@type": "SelectionValidator"` (answer: integer or array of integers)
- `click_choice` → `"@type": "MultipleChoiceValidator"` (answer: array with index)
- `place_tick` → `"@type": "PlaceTicksValidator"` (answer: array of positions)
- `highlight` → `"@type": "SelectTicksValidator"` (answer: array of indices)
- `compare` → `"@type": "FractionShapePartsValidator"` (answer: fraction or array of fractions)

**Tool Mapping:**
- `click_sections` → `"paint"` (for shading interactions)
- `click_choice` → omit tool (MCQs don't use tools, only workspace.choices)
- `drag_fraction` → `"compare"` (for fraction comparison)
- `place_tick` → `"place_tick"` (unchanged)
- `highlight` → `"highlight"` (unchanged)
- `select` / `multi_select` → use for tangible selection

### 3. Structure Transformation

**Input Part 1 (workspace setup):**
```json
{{
  "dialogue": "...",
  "workspace": [
    {{"id": "rect_1", "type": "rectangle_bar", ...}}
  ]
}}
```

**Output:**
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
        "lcm": 6,
        "is_read_only": false
      }}
    ]
  }},
  "dialogue": "..."
}}
```
Note: lcm = 6 because verb is "partition" and sections = 3, so lcm = 3 × 2 = 6

**Input Part 2 (interaction):**
```json
{{
  "dialogue": "Shade 1 part...",
  "prompt": "Click to shade 1 part",
  "interaction_tool": "click_sections",
  "workspace_context": {{...}},
  "correct_answer": [1]
}}
```

**Output:**
```json
{{
  "@type": "Step",
  "dialogue": "Shade 1 part...",
  "prompt": {{
    "@type": "Prompt",
    "text": "Click to shade 1 part",
    "tool": "paint",
    "validator": {{
      "@type": "ShadedPartsValidator",
      "answer": 1
    }},
    "remediations": [...]
  }}
}}
```

### 4. Error Paths → Remediations

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
          {{"type": "highlight", "animation": "pulse_sections", ...}}
        ]
      }}
    }},
    {{
      "scaffolding_level": "heavy",
      "dialogue": "This is tricky...",
      "visual": {{
        "effects": [
          {{"type": "annotation", "animation": "label_sections", ...}},
          {{"type": "demonstration", "animation": "shade_one_section", ...}}
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
      "dialogue": "[event:pulse_sections]Let's think..."
    }}
  }},
  {{
    "@type": "Remediation",
    "id": "heavy",
    "step": {{
      "@type": "Step",
      "dialogue": "[event:label_sections][event:shade_one_section]This is tricky..."
    }}
  }}
]
```

### 5. Visual Effects → Event Tags

Convert visual.effects array to [event:...] tags in dialogue:
- Extract animation name from each effect
- Prepend as [event:animation_name] before dialogue
- Multiple effects = multiple event tags

Example:
```json
"effects": [
  {{"animation": "pulse_sections"}},
  {{"animation": "highlight_shaded"}}
]
```
→ `"[event:pulse_sections][event:highlight_shaded]Original dialogue text"`

### 6. Success Path → on_correct

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

### 7. Choices (Multiple Choice)

If input has `choices` array, add to workspace AND prompt:
```json
"workspace": {{
  "@type": "WorkspaceData",
  "tangibles": [],
  "choices": {{
    "@type": "WorkspaceChoices",
    "allow_multiple": false,
    "options": ["1/2", "1/3", "1/4", "1/8"]
  }}
}},
"prompt": {{
  "@type": "Prompt",
  "text": "...",
  "validator": {{
    "@type": "MultipleChoiceValidator",
    "answer": [2]
  }},
  "remediations": [...]
}}
```
**Note**: MCQs do NOT have a "tool" field. They use workspace.choices for display.

## KEY POINTS

1. **@metadata field**: Each Sequence must have @metadata with problem_id, difficulty, verb, and goal from input
2. **Workspace rename**: Change "workspace" array → "workspace" object with "tangibles" array and optional "choices"
3. **Type field removal**: Remove "type", "id", "orientation", "state", "position" from tangibles after mapping to FracShape
4. **FracShape conversion**: ALL fraction shapes become FracShape with visual property (0/1/2)
5. **Uniform fractions**: Use string "1/4" for equal parts, not array ["1/4","1/4","1/4","1/4"]
6. **LCM calculation**: For cut/partition questions (verb="partition"/"divide"/"cut" OR tool="cut"), set lcm = sections × 2. Otherwise lcm = 24
7. **Success path handling**: Add success_path dialogue to prompt.on_correct (not as separate step)
8. **Event tag format**: Use animation name only (not full object)
9. **Remediation IDs**: Must be "light", "medium", or "heavy" (lowercase)
10. **Tool mapping**: click_sections→paint, click_choice→(no tool), drag_fraction→compare
11. **Validator selection**: Choose correct validator based on interaction type and answer format
12. **MCQ special case**: No tool field, choices go in workspace.choices

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
                "visual": 0,
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
            ],
            "choices": {
              "@type": "WorkspaceChoices",
              "allow_multiple": false,
              "options": ["1/2", "1/3", "1/4"]
            }
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
                  "dialogue": "[event:...]..."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:...][event:...]..."
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
