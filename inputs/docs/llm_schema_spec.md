**Audience:** AI Content Generators and Developers  
**Purpose:** Define the input schema structure for the Godot Formatter transformation step

## Overview

This document specifies the **input schema** that the Godot Formatter accepts. This is the output from the Remediation Generator (Step 2) and input to the Godot Formatter (Step 3).

The Godot Formatter transforms this remediation schema into Godot-processable format with @type annotations and proper structure.

---

## Root Structure

```json
{
  "sequences": [
    {
      "problem_id": integer,
      "difficulty": integer,
      "verb": string,
      "goal": string,
      "steps": [...],
      "student_attempts": {
        "success_path": {...},
        "error_path_generic": {...}
      }
    }
  ]
}
```

---

## Sequence Object

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `problem_id` | Integer | Unique identifier for the problem | `1` |
| `difficulty` | Integer | Problem difficulty (0=easy, 1=medium, 2=hard) | `0` |
| `verb` | String | Learning action/skill being practiced | `"partition"`, `"identify"`, `"compare"` |
| `goal` | String | Learning objective description | `"Students can partition shapes into equal parts"` |
| `steps` | Array | Main instruction and interaction steps | See [Step Types](#step-types) |
| `student_attempts` | Object | Success and error path definitions | See [Student Attempts](#student-attempts) |

### Example

```json
{
  "problem_id": 1,
  "difficulty": 0,
  "verb": "partition",
  "goal": "Students can partition shapes into equal parts",
  "steps": [...],
  "student_attempts": {...}
}
```

---

## Step Types

There are two main types of steps in the `steps` array:

### 1. Workspace Setup Step

Shows visual tangibles to the learner.

```json
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
}
```

**Fields:**
- `dialogue`: (Optional) What the guide says when showing the workspace
- `workspace`: Array of tangible objects to display

### 2. Interaction Step

Prompts learner to interact with tangibles.

```json
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
```

**Fields:**
- `dialogue`: (Optional) Instructions for the learner
- `prompt`: Button text or interaction prompt
- `interaction_tool`: Tool used for interaction (see [Interaction Tools](#interaction-tools))
- `workspace_context`: Context about what's in the workspace
- `correct_answer`: Expected answer format (varies by tool)
- `choices`: (Optional) Array of choice options for MCQs

---

## Tangible Types

### Rectangle Bar

```json
{
  "id": "rect_1",
  "type": "rectangle_bar",
  "sections": 3,
  "orientation": "horizontal",
  "state": "divided",
  "shaded": [0, 1],
  "position": "center"
}
```

**Properties:**
- `id`: Unique identifier for this tangible
- `type`: `"rectangle_bar"` or `"fraction_bar"`
- `sections`: Number of equal parts
- `orientation`: `"horizontal"` or `"vertical"`
- `state`: `"divided"`, `"empty"`, `"partitioned"`
- `shaded`: Array of shaded section indices (0-based)
- `position`: `"center"`, `"top"`, `"bottom"`, `"left"`, `"right"`

### Square

```json
{
  "id": "square_1",
  "type": "square",
  "sections": 4,
  "layout": "grid_2x2",
  "shaded": [1],
  "position": "center"
}
```

**Properties:**
- `id`: Unique identifier
- `type`: `"square"`
- `sections`: Number of parts (must be perfect square for grid)
- `layout`: `"grid_2x2"`, `"grid_3x3"`, etc.
- `shaded`: Array of shaded indices
- `position`: Placement on screen

### Circle

```json
{
  "id": "circle_1",
  "type": "circle",
  "sections": 8,
  "shaded": [0, 1, 2],
  "position": "center"
}
```

**Properties:**
- `id`: Unique identifier
- `type`: `"circle"`
- `sections`: Number of pie slices
- `shaded`: Array of shaded indices
- `position`: Placement on screen

### Number Line

```json
{
  "id": "numberline_1",
  "type": "number_line",
  "min": 0,
  "max": 1,
  "divisions": 6,
  "marked_positions": [0, 1],
  "labels_visible": true
}
```

**Properties:**
- `id`: Unique identifier
- `type`: `"number_line"`
- `min`: Starting value
- `max`: Ending value
- `divisions`: Number of equal divisions
- `marked_positions`: Existing tick marks
- `labels_visible`: Whether to show labels

---

## Interaction Tools

### Tool Types

| Tool | Description | Answer Format | Use Case |
|------|-------------|---------------|----------|
| `click_sections` | Click to shade/select sections | Array of indices `[1, 2]` | Shading fractions |
| `click_choice` | Select from multiple choices | Array with single index `[2]` | Multiple choice questions |
| `place_tick` | Place tick marks on number line | Array of positions `[2, 4]` | Number line partitioning |
| `highlight` | Highlight specific positions | Array of indices `[3]` | Selecting ticks |
| `drag_fraction` | Drag fraction representations | Fraction string `"1/4"` | Fraction matching |
| `select` | Select tangibles | Integer or array `2` or `[0, 2]` | Tangible selection |

### Examples

**Click Sections:**
```json
{
  "interaction_tool": "click_sections",
  "correct_answer": [1, 2]  // Indices of sections to shade
}
```

**Multiple Choice:**
```json
{
  "interaction_tool": "click_choice",
  "choices": ["1/2", "1/3", "1/4", "1/5"],
  "correct_answer": [2]  // Index 2 = "1/4"
}
```

**Place Ticks:**
```json
{
  "interaction_tool": "place_tick",
  "correct_answer": [2, 4]  // Positions for tick marks
}
```

---

## Student Attempts

Defines success and error paths with progressive scaffolding.

### Success Path

```json
"success_path": {
  "steps": [
    {
      "dialogue": "That's it! You showed one-third perfectly."
    }
  ]
}
```

**Fields:**
- `steps`: Array with single step containing success dialogue

### Error Path (Generic)

Progressive scaffolding with 3 levels: light, medium, heavy

```json
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
```

### Scaffolding Levels

| Level | Word Count | Visual Effects | Purpose |
|-------|-----------|----------------|---------|
| `light` | 10-20 words | None (`visual: null`) | Minimal hint, gentle redirect |
| `medium` | 20-30 words | 1-2 effects | Explanation + visual feedback |
| `heavy` | 30-60 words | 2-3 effects | Full demonstration with step-by-step |

### Visual Effects

```json
{
  "target": "rect_1",
  "type": "highlight",
  "animation": "pulse_sections",
  "description": "All three sections pulse to show they are separate parts"
}
```

**Fields:**
- `target`: ID of tangible to animate
- `type`: Effect category (`highlight`, `annotation`, `demonstration`)
- `animation`: Animation name (becomes `[event:animation_name]` in Godot)
- `description`: Human-readable description of the effect

**Common Animations:**
- `pulse_sections` - Sections pulse/flash
- `label_sections` - Add number labels
- `highlight_shaded` - Highlight shaded areas
- `shade_one_section` - Auto-shade demonstration
- `show_lines` - Display number lines
- `count_sections_sequentially` - Count with animation
- `highlight_shaded_vs_total` - Compare shaded to total

---

## Complete Example

```json
{
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
}
```

---

## Validation Rules

### Required Fields

1. **Sequence Level:**
   - `problem_id`, `difficulty`, `verb`, `goal` - Required
   - `steps` - Must have at least 1 step
   - `student_attempts` - Must have both success and error paths

2. **Step Level:**
   - Either `workspace` OR `prompt` must be present (can have both)
   - If interaction step, must have: `interaction_tool`, `correct_answer`

3. **Error Path:**
   - Must have exactly 3 remediation steps
   - Must have `scaffolding_level`: "light", "medium", "heavy" (in order)
   - Light: `visual: null`
   - Medium/Heavy: Can have visual effects array

### Best Practices

1. **Dialogue Guidelines:**
   - Keep focused on the learning objective
   - Use clear, age-appropriate language
   - Reference specific tangibles by type/position

2. **Workspace Context:**
   - Always include `tangibles_present` array
   - Add `note` for clarification when helpful
   - Describe current state of tangibles

3. **Visual Effects:**
   - Use 0 effects for light (just text)
   - Use 1-2 effects for medium (highlight/guide)
   - Use 2-3 effects for heavy (demonstrate solution)

4. **Progressive Scaffolding:**
   - Light: Minimal hint, ask leading question
   - Medium: Explain concept, show visual cue
   - Heavy: Full walkthrough with demonstration

---

## Transformation to Godot Schema

The Godot Formatter will transform this schema into the Godot-processable format:

### Key Transformations:

1. **@type annotations** added to all objects
2. **workspace** array → **workspace** object with **tangibles** array
3. **Tangible types** mapped to FracShape with visual property
4. **interaction_tool** → **tool** (with name mapping)
5. **correct_answer** → **validator.answer**
6. **error_path_generic** → **prompt.remediations** array
7. **visual.effects** → **[event:...]** tags in dialogue
8. **success_path** → **prompt.on_correct**
9. **@metadata** added with problem_id, difficulty, verb, goal

See `godot_schema_spec.md` for the output schema specification.
