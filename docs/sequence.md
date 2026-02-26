# Sequence Schema

> Reference for sequence structure based on Godot SequenceSchema.

---

## Overview

A sequence represents a complete learning interaction with metadata, steps, workspace configuration, prompts, and validation.

### @type Field Usage

The `@type` field is used throughout sequence JSON to indicate the schema type for deserialization. While the GDScript may not strictly require it in all cases, **it is good practice to include @type for all objects**.

**Where to use @type:**
- Sequence level: `"@type": "Sequence"`
- Every Step: `"@type": "Step"`
- Prompts: `"@type": "Prompt"`
- Tools: `"@type": "Move"`, `"@type": "Place"`, `"@type": "Select"`, etc.
- Validators: `"@type": "LabelValidator"`, `"@type": "TickValidator"`, etc.
- Workspace elements: `"@type": "WorkspaceData"`, `"@type": "WorkspaceChoices"`
- Tangibles: `"@type": "NumLine"`, etc.
- Palette: `"@type": "Palette"`
- Stacks: `"@type": "FracLabelStack"`, `"@type": "PointStack"`
- Remediations: `"@type": "Remediation"`

**Best practice:** Always include @type when creating sequence JSON to ensure proper deserialization and type safety.

---

## Top-Level Structure

### Sequence
**Schema type**: `Sequence`

**Fields**:
- `@type` (required, string): Must be "Sequence"
- `metadata` (optional, SequenceMetadata): Learning context and mastery information
- `steps` (required, array of Step): Ordered steps in the sequence

**Example**:
```json
{
  "@type": "Sequence",
  "metadata": {
    "mastery_tier": "baseline",
    "mastery_component": "fractions",
    "mastery_verbs": ["identify"]
  },
  "steps": [...]
}
```

---

## Metadata

### SequenceMetadata
**Schema type**: `SequenceMetadata`

**Purpose**: Provides learning context and mastery tracking information.

**Fields**:
- `mastery_tier` (optional, string): Learning difficulty level
  - Valid values: support, confidence, baseline, stretch, challenge
- `mastery_component` (optional, string): Subject area or topic
- `mastery_verbs` (optional, array of strings): Learning objectives

**Example**:
```json
{
  "mastery_tier": "baseline",
  "mastery_component": "fractions",
  "mastery_verbs": ["identify", "compare"]
}
```

---

## Step Structure

### Step
**Schema type**: `Step`

**Purpose**: Represents a single interaction or moment in the learning sequence.

**Fields**:
- `@type` (required, string): Must be "Step"
- `metadata` (optional, dictionary): Additional step-level metadata
- `dialogue` (optional, string): Conversational text shown to student
- `audio_dir` (optional, string): Audio file directory path
- `workspace` (optional, Workspace): Visual elements and tangibles
- `prompt` (optional, Prompt): Student-facing question and interaction configuration
- `scene` (optional, string): Classroom scene setting
- `pool` (optional, Pool): Problem pool reference

**Example**:
```json
{
  "@type": "Step",
  "dialogue": "Look at the number line. What fraction does the point show?",
  "workspace": {...},
  "prompt": {...}
}
```

---

## Prompt Structure

### Prompt
**Schema type**: `Prompt`

**Purpose**: Defines the student-facing question, interaction tool, validation, and feedback.

**Fields**:
- `@type` (required, string): Must be "Prompt"
- `text` (required, string): The question or instruction shown to student
- `tool` (optional, Tool): Interaction tool (Move, Place, Paint, Select, Drag, etc.)
- `validator` (optional, Validator): Answer validation logic
- `choices` (optional, WorkspaceChoices): MCQ options for click_choice interactions
- `palette` (optional, Palette): Draggable items for drag interactions
- `remediations` (optional, array of Remediation): Incorrect answer feedback
- `on_correct` (optional, Step): Step to show on correct answer

**Example**:
```json
{
  "@type": "Prompt",
  "text": "What fraction does this point show?",
  "tool": {
    "@type": "Move"
  },
  "validator": {...},
  "choices": {
    "options": ["1/3", "2/3", "3/3"]
  }
}
```

**Note**: When `tool` is a `Move` (Drag) tool, palette information can be specified either in the tool itself or at the prompt level. The schema automatically migrates prompt-level palette to the Move tool during deserialization.

---

## Workspace Elements

### WorkspaceChoices
**Schema type**: `WorkspaceChoices`

**Purpose**: Multiple choice options for click_choice interaction tool.

**Fields**:
- `@type` (required, string): Must be "WorkspaceChoices"
- `allow_multiple` (optional, boolean): Whether multiple options can be selected. Default: false
- `options` (required, array of strings): The choice options

**Example**:
```json
{
  "@type": "WorkspaceChoices",
  "allow_multiple": false,
  "options": ["1/4", "2/4", "3/4", "4/4"]
}
```

**Usage**:
- For single-answer MCQ: Omit `allow_multiple` or set to `false`
- For multi-answer MCQ: Set `allow_multiple` to `true`
- Serializes to `null` if options array is empty

---

### Palette
**Schema type**: `Palette`

**Purpose**: Contains draggable items (labels, points, etc.) for drag interactions.

**Fields**:
- `stacks` (required, array of PartStack): Draggable items available in the palette

**Stacks can be**:
- `FracLabelStack`: Fraction labels with quantity
- `PointStack`: Points with quantity

**Example**:
```json
{
  "@type": "Palette",
  "stacks": [
    {
      "@type": "FracLabelStack",
      "label": "1/4",
      "quantity": 2
    },
    {
      "@type": "FracLabelStack",
      "label": "2/4"
    }
  ]
}
```

**Usage Notes**:
- Labels can only be dragged to pre-placed tick marks with `is_read_only: false` (default)
- Non-interactable tick marks (endpoints, pre-labeled ticks) should be marked `is_read_only: true`
- Quantity defaults to 1 if not specified

---

### FracLabelStack
**Schema type**: `FracLabelStack`

**Purpose**: A stack of draggable fraction labels.

**Fields**:
- `@type` (required, string): Must be "FracLabelStack"
- `label` (required, fraction): The fraction label (e.g., "1/4")
- `quantity` (optional, integer): How many labels are available. Default: 1
- `capacity` (optional, integer): Advanced - maximum capacity. Rarely used. Default: same as quantity

**Example**:
```json
{
  "@type": "FracLabelStack",
  "label": "3/4",
  "quantity": 2
}
```

**Serialization**: Omits `quantity` if 1, omits `capacity` if equal to quantity

---

### PointStack
**Schema type**: `PointStack`

**Purpose**: A stack of draggable points.

**Fields**:
- `@type` (required, string): Must be "PointStack"
- `quantity` (optional, integer): How many points are available. Default: -1 (unlimited)
- `capacity` (optional, integer): Advanced - maximum capacity. Rarely used. Default: -1 (unlimited)

**Example**:
```json
{
  "@type": "PointStack",
  "quantity": 3
}
```

**Serialization**: Omits fields if -1 (unlimited) or if capacity equals quantity

---

## Remediation

### Remediation
**Schema type**: `Remediation`

**Purpose**: Provides feedback and guidance for incorrect answers.

**Fields**:
- `@type` (required, string): Must be "Remediation"
- `id` (required, string): Unique identifier for this remediation
- `step` (required, Step): Partial step containing feedback dialogue or guidance

**Example**:
```json
{
  "@type": "Remediation",
  "id": "incorrect_third",
  "step": {
    "@type": "Step",
    "dialogue": "That's actually one-third. Two-thirds is further along the line."
  }
}
```

---

## Common Patterns

### MCQ Question with Single Answer
```json
{
  "@type": "Step",
  "dialogue": "What fraction does the point represent?",
  "prompt": {
    "@type": "Prompt",
    "text": "What fraction does this point show?",
    "choices": {
      "@type": "WorkspaceChoices",
      "options": ["1/3", "2/3", "3/3"]
    }
  }
}
```

### MCQ Question with Multiple Answers
```json
{
  "@type": "Step",
  "prompt": {
    "@type": "Prompt",
    "text": "Select all equivalent fractions to 1/2.",
    "choices": {
      "@type": "WorkspaceChoices",
      "allow_multiple": true,
      "options": ["2/4", "3/6", "1/3", "4/8"]
    }
  }
}
```

### Drag Label Question
```json
{
  "@type": "Step",
  "dialogue": "Let's label the tick marks on this number line.",
  "prompt": {
    "@type": "Prompt",
    "text": "Drag the correct label to the marked tick.",
    "tool": {
      "@type": "Move",
      "mode": "frac_labels",
      "palette": {
        "@type": "Palette",
        "stacks": [
          {"@type": "FracLabelStack", "label": "1/4"},
          {"@type": "FracLabelStack", "label": "2/4"},
          {"@type": "FracLabelStack", "label": "3/4"}
        ]
      }
    }
  }
}
```

### Point Placement Question with Limited Points
```json
{
  "@type": "Step",
  "dialogue": "Place three points on the number line.",
  "prompt": {
    "@type": "Prompt",
    "text": "Place points at 1/4, 2/4, and 3/4.",
    "tool": {
      "@type": "Move",
      "mode": "points",
      "palette": {
        "@type": "Palette",
        "stacks": [
          {"@type": "PointStack", "quantity": 3}
        ]
      }
    }
  }
}
```

### Point Placement Question with Unlimited Points
```json
{
  "@type": "Step",
  "dialogue": "Place points on the number line.",
  "prompt": {
    "@type": "Prompt",
    "text": "Place a point at 2/3.",
    "tool": {
      "@type": "Move",
      "mode": "points",
      "palette": {
        "@type": "Palette",
        "stacks": [
          {"@type": "PointStack"}
        ]
      }
    }
  }
}
```

### Drag with Multiple Label Types
```json
{
  "@type": "Step",
  "prompt": {
    "@type": "Prompt",
    "text": "Label all the tick marks.",
    "tool": {
      "@type": "Move",
      "mode": "frac_labels",
      "palette": {
        "@type": "Palette",
        "stacks": [
          {"@type": "FracLabelStack", "label": "1/4", "quantity": 2},
          {"@type": "FracLabelStack", "label": "2/4"},
          {"@type": "FracLabelStack", "label": "3/4", "quantity": 2}
        ]
      }
    }
  }
}
```
