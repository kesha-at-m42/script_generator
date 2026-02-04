# Interaction Tools

> Reference for available student interaction tools based on Godot ToolSchema.

---

## Tool Types

### move
**Schema type**: `Move`

**Purpose**: Student moves/places points or fraction labels on tick marks of a number line.

**Fields**:
- `mode` (required, string): Interaction mode - "points" for placing points, "frac_labels" for dragging fraction labels
- `palette` (optional, Palette object): Available items to drag (required when mode is "frac_labels"). See [Palette documentation](sequence.md#palette) for full details.

**Example (points mode)**:
```json
{
  "@type": "Move",
  "mode": "points"
}
```

**Example (fraction labels mode)**:
```json
{
  "@type": "Move",
  "mode": "frac_labels",
  "palette": {
    "@type": "Palette",
    "stacks": [
      {"@type": "FracLabelStack", "label": "1/3", "quantity": 2},
      {"@type": "FracLabelStack", "label": "2/3"}
    ]
  }
}
```

**Example (point placement with limited quantity)**:
```json
{
  "@type": "Move",
  "mode": "points",
  "palette": {
    "@type": "Palette",
    "stacks": [
      {"@type": "PointStack", "quantity": 3}
    ]
  }
}
```

---

### place
**Schema type**: `Place`

**Purpose**: Student places tick marks to partition/divide a number line (cutting task).

**Fields**:
- `lcm` (required, integer): Least common multiple for tick calculations
- `is_single` (optional, boolean): Whether student can place only one tick. Default: false
- `bounds` (optional, array of fractions): Valid range for placement (e.g., `["0", "1"]`)

**Example**:
```json
{
  "@type": "Place",
  "lcm": 12,
  "is_single": true,
  "bounds": ["0", "1"]
}
```

---

### paint
**Schema type**: `Paint`

**Purpose**: Student shades/paints sections of shapes or number line intervals.

**Fields**:
- `is_single` (optional, boolean): Whether only one section can be painted at a time. Default: false

**Example**:
```json
{
  "@type": "Paint",
  "is_single": false
}
```

---

### select
**Schema type**: `Select`

**Purpose**: Student selects tangible(s) from workspace.

**Fields**:
- `is_single` (optional, boolean): Whether only one tangible can be selected. Default: true

**Example**:
```json
{
  "@type": "Select",
  "is_single": true
}
```

---

### comp_frame
**Schema type**: `CompFrame`

**Purpose**: Composition frame tool.

**Fields**: None

**Example**:
```json
{
  "@type": "CompFrame"
}
```

---

### highlight
**Schema type**: `Highlight`

**Purpose**: Student highlights elements.

**Fields**: None

**Example**:
```json
{
  "@type": "Highlight"
}
```

---

### cut_grid
**Schema type**: `CutGrid`

**Purpose**: Grid cutting tool for dividing 2D grids.

**Fields**: None

**Example**:
```json
{
  "@type": "CutGrid"
}
```

---

## Tool Selection Guide for Module 4 Path B

**Place points on existing ticks**:
- Tool: `Move` with `mode: "points"`
- Use for: Student places points at specific tick positions
- Validated with: `PointValidator`

**Drag fraction labels onto ticks**:
- Tool: `Move` with `mode: "frac_labels"` and `palette`
- Use for: Student drags labels from palette onto ticks
- Requires palette with FracLabelStack items (see [Palette docs](sequence.md#palette))
- Validated with: `LabelValidator`

**Partition/divide number line (create new ticks)**:
- Tool: `Place`
- Use for: Student divides line into equal intervals
- Validated with: `TickValidator`

**Select one number line**:
- Tool: `Select`
- Configuration: Single selection
- Validated with: `SelectionValidator`

**Select multiple number lines**:
- Tool: `Select` with `is_single: false`
- Validated with: `SelectionValidator`

**Paint/shade intervals**:
- Tool: `Paint`
- Configuration: Multi or single
- Validated with: `ShadedValidator` or `ShadedPartsValidator`
