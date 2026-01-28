# Interaction Tools

> Reference for available student interaction tools based on Godot ToolSchema.

---

## Tool Types

### move
**Schema type**: `Move`

**Purpose**: Student moves/places points on tick marks of a number line.

**Fields**: None

**Example**:
```json
{
  "@type": "Move"
}
```

---

### place
**Schema type**: `Place`

**Purpose**: Student places tick marks to partition/divide a number line (cutting task).

**Fields**:
- `lcm` (optional, integer): Least common multiple for tick calculations. Default: 0
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

### drag
**Schema type**: `Drag`

**Purpose**: Student drags labels/objects from a palette onto target positions (e.g., tick marks on a number line).

**Fields**:
- `palette` (required, Palette object): Available items to drag
- `lcm` (optional, integer): For fraction-based dragging

**Important**: Drag tool REQUIRES palette. Use this when students drag labels from a palette onto number line ticks.

**Example**:
```json
{
  "@type": "Drag",
  "palette": {
    "@type": "Palette",
    "labels": ["1/3", "2/3"],
    "quantities": [1, 1]
  }
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

## Tool Selection Guide for Module 4 Path B

**Place points on existing ticks**:
- Tool: `Move`
- Use for: Student places points at specific tick positions
- No palette
- Validated with: `PointValidator`

**Drag fraction labels onto ticks**:
- Tool: `Drag` with `palette`
- Use for: Student drags labels from palette onto ticks
- Requires palette with labels and quantities
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
