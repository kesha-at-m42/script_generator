# Godot Schema Specification

**Audience:** Developers and engineers  
**Purpose:** Standardize terminology and structure for Godot game engine integration


## Overview

The Godot schema uses **@type annotations** in JSON for deserialization, which are mapped to Godot classes during validation. The validator uses `.type(ClassName)` to specify the target class, while the JSON contains `"@type": "ClassName"` for serialization.

---

## Root Structure

```json
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
      "steps": [...]
    }
  ]
}
```

**Note:** The validator expects `{"steps": [...]}` at the Sequence level, but the JSON includes wrapping with @type annotations for proper deserialization. Each Sequence also includes @metadata with problem context.

---

## Example Step Structure

```json
{
  "@type": "Step",
  "dialogue": "Here's a bar. Click in the middle to make 2 equal parts.",
  "workspace": {
    "@type": "WorkspaceData",
    "tangibles": [...]
  },
  "prompt": {
    "@type": "Prompt",
    "text": "Click once in the middle to make 2 equal parts.",
    "tool": "click_sections",
    "validator": {
      "@type": "SelectSectionsValidator",
      "answer": [1]
    },
    "choices": null,
    "remediations": [
      {"@type": "Remediation", "id": "light", ...},
      {"@type": "Remediation", "id": "medium", ...},
      {"@type": "Remediation", "id": "heavy", ...}
    ],
    "on_correct": null
  },
  "scene": null
}
```

---

## Schema Field Reference

### Step Fields (from sequence_schema.gd)

Required fields:
- `@type`: "Step"

Optional fields:
- `dialogue`: string - What the guide says (can include [event:...] tags)
- `workspace`: WorkspaceData - Visual setup with tangibles
- `prompt`: Prompt - Learner interaction request
- `scene`: string - Scene change (e.g., "Classroom", "Workspace", or null)
- `@metadata`: object - Documentation for visual effects/events (optional)
  - `events`: Array<{name: string, description: string}> - Describes each animation event

### Workspace Structure

```json
{
  "@type": "WorkspaceData",
  "tangibles": [
    {
      "@type": "<TangibleType>",
      "id": "unique_id",
      ...properties...
    }
  ]
}
```

**Important:** Use `"@type": "WorkspaceData"` (not "Workspace")

### Prompt Structure

```json
{
  "@type": "Prompt",
  "text": "Problem statement or instruction",
  "tool": "interaction_tool_name",
  "validator": {
    "@type": "ValidatorType",
    "answer": ...
  },
  "choices": {
    "@type": "WorkspaceChoices",
    "allow_multiple": false,
    "options": ["option1", "option2", ...]
  } | null,
  "remediations": [
    {
      "@type": "Remediation",
      "id": "light" | "medium" | "heavy",
      "step": {
        "@type": "Step",
        "dialogue": "..."
      }
    }
  ],
  "on_correct": {
    "@type": "Step",
    "dialogue": "Success message"
  } | null
}
```

### Remediation Structure

```json
{
  "@type": "Remediation",
  "id": "light" | "medium" | "heavy",
  "step": {
    "@type": "Step",
    "dialogue": "Remediation text with optional [event:tags]",
    "@metadata": {
      "events": [
        {
          "name": "pulse_sections",
          "description": "All three sections pulse to show they are separate parts"
        }
      ]
    }
  }
}
```

The `step` field uses partial_step schema (dialogue only). The optional `@metadata` field can document what visual effects occur:

**Light Remediation** (no events):
```json
{
  "@type": "Remediation",
  "id": "light",
  "step": {
    "@type": "Step",
    "dialogue": "Think about how many parts you need."
  }
}
```

**Medium Remediation** (1-2 events):
```json
{
  "@type": "Remediation",
  "id": "medium",
  "step": {
    "@type": "Step",
    "@metadata": {
      "events": [
        {
          "name": "pulse_sections",
          "description": "All three sections pulse to show they are separate parts"
        }
      ]
    },
    "dialogue": "[event:pulse_sections]Let's count the parts together."
  }
}
```

**Heavy Remediation** (2+ events):
```json
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
          "description": "One section becomes shaded as a demonstration"
        }
      ]
    },
    "dialogue": "[event:label_sections][event:shade_one_section]Here's an example."
  }
}
```

---

## Component Definitions

### Sequence
A list of **Steps** triggered in order. Each Sequence represents one problem or learning interaction.

**Structure:**
```json
{
  "@type": "Sequence",
  "@metadata": {
    "problem_id": 1,
    "difficulty": 0,
    "verb": "partition",
    "goal": "Students can partition shapes into equal parts"
  },
  "steps": [...]
}
```

**@metadata Fields:**
- `problem_id`: Integer - Unique identifier for the problem
- `difficulty`: Integer - Problem difficulty level (0=easy, 1=medium, 2=hard)
- `verb`: String - Learning action/skill (e.g., "partition", "compare", "identify")
- `goal`: String - Learning objective description

### Step
A collection of one or more **Components** that trigger simultaneously:
- **Dialogue** - Guide speech
- **Workspace** - Visual setup
- **Prompt** - Learner interaction
- **Scene** - Camera/environment change

A step is "completed" when all components finish running.

### Tool
An interaction method the learner uses to respond:
- `"cut"` - Cut/divide tangibles into parts
- `"paint"` - Shade/color sections of tangibles
- `"select"` - Select a single tangible from workspace
- `"multi_select"` - Select multiple tangibles from workspace
- `"compare"` - Compare tangibles or match representations
- `"highlight"` - Highlight specific tick marks or positions
- `"place_tick"` - Place tick marks on number line
- (no tool) - Multiple choice questions use workspace.choices instead of a tool

**Rule:** Only one tool active at a time per prompt. MCQs don't use tools.

### Tangible Types

Physical interactable objects in the workspace.

**FracShape** - Unified type for all fraction shapes (rectangles, circles, squares)

The `visual` property determines the shape type:
- `0` = Bar (horizontal)
- `1` = Pie
- `2` = Grid
- (other values for additional shapes)

**Uniform FracShape** (equal parts):
```json
{
  "@type": "FracShape",
  "fractions": "1/4",
  "visual": 0,
  "shaded": [0, 1],
  "lcm": 24
}
```
When `fractions` is a single fraction string, creates uniform shape with that many equal parts.

**Non-uniform FracShape** (different-sized parts):
```json
{
  "@type": "FracShape",
  "fractions": ["1/4", "1/4", "1/2"],
  "visual": 0,
  "shaded": [],
  "frac_label_visible": [0, 1, 2],
  "lcm": 24
}
```
When `fractions` is an array, each element represents one part's fraction value.

**FracShape Properties:**
- `@type`: Always "FracShape"
- `fractions`: String ("1/4") for uniform OR Array<String> (["1/4", "1/2"]) for non-uniform OR null for whole
  * **Fraction format:** Pattern `^[1-9]+/[1-9]+$` (e.g., "1/4", "2/9")
  * **Maximum denominator:** 9 (smallest supported fraction is 1/9)
- `visual`: Integer (0=bar, 1=pie, 2=grid, etc.) - Optional, default 0
- `shaded`: Array<Integer> - Indices of shaded parts - Optional, default []
- `missing`: Array<Integer> - Indices of missing/hidden parts - Optional, default []
- `frac_label_visible`: Array<Integer> - Indices where fraction labels show - Optional, default []
- `lcm`: Integer - Least common multiple for rendering calculations - Optional, default 24
  * **For cut/partition tasks**: Set to `sections × 2` (e.g., 3 sections → lcm = 6)
  * **For other tasks**: Use default 24

**NumberLine:**
```json
{
  "@type": "NumberLine",
  "lcd": 6,
  "tick_marks": [0, "1/6", "2/6", "3/6", "4/6", "5/6", 1],
  "labelled": [true, false, false, false, false, false, true],
  "dots": [2]
}
```

**NumberLine Properties:**
- `@type`: Always "NumberLine"
- `lcd`: Integer - Least common denominator (required, maximum value: 9)
- `tick_marks`: Array - Mix of integers (0, 1) and fraction strings ("1/6") for tick positions (required)
  * **Fraction format:** Pattern `^[1-9]+/[1-9]+$` (e.g., "1/6", "2/9")
  * **Maximum denominator:** 9 (smallest supported fraction is 1/9)
- `labelled`: Array<Boolean> - Whether each tick shows label - Optional
- `dots`: Array<Integer> - Indices of tick marks with dots/markers - Optional

### Validator Types

Maps to interaction tools to validate learner responses.

**EqualShadedValidator**
```json
{
  "@type": "EqualShadedValidator",
  "answer": "1/4"
}
```
**Answer Type:** Fraction string (e.g., "1/4", "2/3") or null
**Required Tangibles:** At least one non-read-only FracShape
**Required Properties:** FracShape.shaded array
**Key Behavior:** Validates all shapes have equal shaded proportions (within 0.001 tolerance). When answer provided, first shape must match target proportion.
**Use case:** Ensuring equivalent shaded amounts across multiple representations ("shade 1/4 on all bars")

**ShadedPartsValidator**
```json
{
  "@type": "ShadedPartsValidator",
  "answer": 3
}
```
**Answer Type:** Integer (count) or null
**Required Tangibles:** At least one non-read-only FracShape
**Required Properties:** FracShape.shaded array
**Key Behavior:** Validates all shapes have same count of shaded parts. When answer provided, checks for exact count match.
**Use case:** Tasks requiring specific number of parts shaded, regardless of size ("shade 3 parts")

**FractionShapePartsValidator** 
```json
{
  "@type": "FractionShapePartsValidator",
  "answer": "1/4"
}
```
or explicit array form (equivalent):
```json
{
  "@type": "FractionShapePartsValidator",
  "answer": ["1/4", "1/4", "1/4", "1/4"]
}
```
or for non-uniform parts:
```json
{
  "@type": "FractionShapePartsValidator",
  "answer": ["1/4", "1/4", "1/2"]
}
```
**Answer Type:** Single fraction string (e.g., "1/4") or array of fraction strings (e.g., ["1/4", "1/4", "1/2"])
  - Single fraction string: Shorthand for uniform parts (e.g., "1/4" means all parts are fourths)
  - Array of fractions: Explicit form where each element represents one part's size. Array elements must have same denominator and sum to 1. Can represent uniform parts ["1/2", "1/2"] or non-uniform parts ["1/4", "1/4", "1/2"]
**Required Tangibles:** At least one non-read-only FracShape
**Required Properties:** FracShape.fractions (string or array)
**Key Behavior:** Validates each part's exact fraction value. If array, checks part[i] == answer[i]. If string, all parts must equal that value.
**Use case:** Partition/cut tasks where specific part sizes matter ("cut into thirds", "cut into 1/4 and 1/2")

**SelectionValidator**
```json
{
  "@type": "SelectionValidator",
  "answer": 2
}
```
or for multiple selections:
```json
{
  "@type": "SelectionValidator",
  "answer": [0, 2]
}
```
**Answer Type:** Integer (e.g., 2) for single selection or array of integers (e.g., [0, 2]) for multiple selections
**Required Tangibles:** At least one tangible model in workspace
**Required Properties:** Tangible.is_selected property
**Key Behavior:** Validates is_selected property on tangibles by 0-based index. Multi-select ensures only items in answer array are selected.
**Use case:** Select specific shapes/objects from multiple options ("select the shape showing 1/2")

**MultipleChoiceValidator**
```json
{
  "@type": "MultipleChoiceValidator",
  "answer": [2]
}
```
**Answer Type:** Array of integers (e.g., [2] for single choice, [0, 2] for multiple)
**Required Tangibles:** None (uses button interface)
**Required Fields:** Prompt.choices (WorkspaceChoices object with options array)
**Key Behavior:** Validates selected button indices match answer array (order-independent, uses sorting). Requires exact match.
**Use case:** Multiple choice questions where learner clicks button(s) to select answer

**PlaceTicksValidator**
```json
{
  "@type": "PlaceTicksValidator",
  "answer": [2, 4]
}
```
**Answer Type:** Array of integers (numerator values, e.g., [2, 4] for 2/6 and 4/6)
**Required Tangibles:** One NumberLine
**Required Properties:** NumberLine.tick_marks array, tick numerator property
**Key Behavior:** Validates count and numerator values of user-placed ticks (excludes start/end ticks). Each tick's numerator must match answer[i].
**Use case:** Tasks where learner places tick marks at specific positions ("place ticks at 2/6 and 4/6")

**SelectTicksValidator**
```json
{
  "@type": "SelectTicksValidator",
  "answer": [3]
}
```
**Answer Type:** Array of integers (numerator values, e.g., [3] for 3/6)
**Required Tangibles:** One NumberLine with existing tick marks
**Required Properties:** NumberLine.tick_marks array, tick is_shaded and numerator properties
**Key Behavior:** Validates numerators of shaded ticks match answer array (order-independent). Rejects if end tick selected.
**Use case:** Tasks where learner highlights/selects existing tick marks ("select the tick at 3/6")

### WorkspaceChoices

Used with MultipleChoiceValidator for displaying options.

```json
{
  "@type": "WorkspaceChoices",
  "allow_multiple": false,
  "options": ["1/2", "1/3", "1/4", "1/5"]
}
```

- `allow_multiple`: boolean - Whether multiple selections allowed
- `options`: array of strings - Text for each choice button

---

## Scaffolding Levels

Remediations use progressive scaffolding with 3 required levels:

**Light Remediation:**
- ID: `"light"`
- No visual effects (no @metadata.events)
- Example: `{"@type": "Remediation", "id": "light", "step": {"@type": "Step", "dialogue": "..."}}`

**Medium Remediation:**
- ID: `"medium"`
- May include 1-2 visual effects in @metadata.events
- Example: `{"@type": "Remediation", "id": "medium", "step": {"@type": "Step", "@metadata": {"events": [...]}, "dialogue": "..."}}`

**Heavy Remediation:**
- ID: `"heavy"`
- May include 2+ visual effects in @metadata.events
- Example: `{"@type": "Remediation", "id": "heavy", "step": {"@type": "Step", "@metadata": {"events": [...]}, "dialogue": "..."}}`

---

## Complete Working Example

**Full sequence from problem_pool.json:**

```json
{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "@metadata": {
        "problem_id": 101,
        "difficulty": 0,
        "verb": "partition",
        "goal": "Create thirds on a number line"
      },
      "steps": [
        {
          "@type": "Step",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [
              {
                "@type": "NumberLine",
                "range": [0, 1],
                "lcd": 6,
                "tick_marks": [0, 1]
              }
            ]
          }
        },
        {
          "@type": "Step",
          "dialogue": "[event:show_lines]Create thirds on this number line. Click to place marks that make three equal intervals."
        },
        {
          "@type": "Step",
          "prompt": {
            "@type": "Prompt",
            "text": "Place marks to create three equal intervals.",
            "tool": "place_tick",
            "validator": {
              "@type": "PlaceTicksValidator",
              "answer": [2, 4]
            },
            "remediations": [
              {
                "@type": "Remediation",
                "id": "light",
                "step": {
                  "@type": "Step",
                  "dialogue": "Here's a hint: Check your spacing - Thirds need three equal intervals."
                }
              },
              {
                "@type": "Remediation",
                "id": "medium",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:practice_1_md]Not quite. For thirds, place marks at one third and two thirds to create three equal spaces between 0 and 1."
                }
              },
              {
                "@type": "Remediation",
                "id": "heavy",
                "step": {
                  "@type": "Step",
                  "dialogue": "[event:practice_1_hv]Let me show you. For three equal intervals, I place marks at one third and two thirds. Now I have thirds."
                }
              }
            ]
          }
        },
        {
          "@type": "Step",
          "dialogue": "Perfect! Three equal intervals - that's thirds."
        }
      ]
    }
  ]
}
```

**Step Breakdown:**
1. **Workspace Setup** - Display NumberLine with tick marks at 0 and 1
2. **Dialogue** - Instruct learner with [event:show_lines] trigger
3. **Prompt** - Request interaction with tool, validator, and 3 remediations (L/M/H)
4. **Success Dialogue** - Positive feedback when correct

---

## Key Rules & Best Practices

### Required @type Fields
Every object must have `@type` for proper deserialization:
- Root: `"@type": "SequencePool"`
- Sequence: `"@type": "Sequence"` + `"@metadata": {...}` (problem context)
- Step: `"@type": "Step"`
- Workspace: `"@type": "WorkspaceData"` ⚠️ (not "Workspace")
- Prompt: `"@type": "Prompt"`
- Validator: `"@type": "<ValidatorType>"` (see validator types above)
- Remediation: `"@type": "Remediation"`
- Choices: `"@type": "WorkspaceChoices"`
- Tangibles: `"@type": "FracShape"` or `"@type": "NumberLine"`

### Field Requirements
- **@metadata**: Required in Sequence. Contains problem_id, difficulty, verb, goal
- **dialogue**: Optional in Steps. Contains guide speech and [event:...] tags.
- **workspace**, **prompt**, **scene**: All optional in Steps. At least one should be present.
- **remediations**: Must have exactly 3 items with id "light", "medium", "heavy" (in that order)
- **tool**: Required in Prompt (use appropriate tool from list). Exception: MCQs have no tool (omit or null)
- **validator**: Required in Prompt
- **choices**: Required for MultipleChoiceValidator (workspace.choices), null for other validators

### Common Usage Patterns

**Pattern 1: Combined Workspace + Dialogue**
```json
{
  "@type": "Step",
  "dialogue": "Look at this...",
  "workspace": {...}
}
```

**Pattern 2: Dialogue + Prompt in Same Step**
```json
{
  "@type": "Step",
  "dialogue": "Instructions here.",
  "prompt": {
    "@type": "Prompt",
    "text": "Button text",
    ...
  }
}
