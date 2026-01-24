# Interaction Tools

> Reference for available student interaction tools based on Godot ToolSchema.

---

## Tool Types

### move
**Schema type**: `Move`

**Purpose**: Student moves/places points on tick marks of a number line.

**Fields**:
- `palette` (optional, Palette object): Available items to move

**Backwards compatibility**: String `"move"` maps to `Move`

**Example**:
```json
{
  "@type": "Move",
  "palette": {}
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

**Backwards compatibility**: String `"cut"` maps to `Place`

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
- `is_single` (optional, boolean): Whether only one section can be painted at a time

**Backwards compatibility**:
- String `"paint"` maps to `Paint` (multi-select)
- String `"single_paint"` maps to `Paint` with `is_single: false`

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
- `is_single` (optional, boolean): Whether only one tangible can be selected

**Backwards compatibility**:
- String `"select"` maps to single selection
- String `"multi_select"` maps to `Select` with `is_single: false`

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

**Purpose**: Student drags labels/objects onto target positions.

**Fields**:
- `lcm` (optional, integer): For fraction-based dragging
- `palette` (optional, Palette object): Available items to drag
- `labels` (optional, array of fractions): **LEGACY** - Available fraction labels to drag
- `quantities` (optional, array of integers): **LEGACY** - Quantity of each label

**Note**: Legacy `labels` and `quantities` are automatically migrated to `palette` format.

**Example**:
```json
{
  "@type": "Drag",
  "palette": {
    "fractions": ["1/3", "2/3"],
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

## String Shortcuts (Backwards Compatibility)

For simpler JSON, tools can be specified as strings:

- `"cut"` → `Place` (place points)
- `"paint"` → `Paint` (multi-paint)
- `"single_paint"` → `Paint` with `is_single: false`
- `"select"` → `Select` (single selection)
- `"multi_select"` → `Select` with `is_single: false`
- `"comp_frame"` → `CompFrame`
- `"highlight"` → `Highlight`
- `"move"` → `Move`

---

## Tool Selection Guide for Module 4 Path B

**Place points on existing ticks**:
- Tool: `Move` or `"move"`
- Use for: Student places points at specific tick positions
- Validated with: `PointValidator`

**Partition/divide number line (create new ticks)**:
- Tool: `Place` or `"cut"`
- Use for: Student divides line into equal intervals
- Validated with: `TickValidator`

**Drag fraction labels onto ticks**:
- Tool: `Drag` with `labels` and `quantities`
- Use for: Student drags labels from palette onto ticks
- Validated with: `LabelValidator`

**Select one number line**:
- Tool: `Select` or `"select"`
- Configuration: Single selection
- Validated with: `SelectionValidator`

**Select multiple number lines**:
- Tool: `Select` with `is_single: false`
- Or use shortcut: `"multi_select"`
- Validated with: `SelectionValidator`

**Paint/shade intervals**:
- Tool: `Paint`
- Configuration: Multi or single
- Validated with: `ShadedValidator` or `ShadedPartsValidator`
