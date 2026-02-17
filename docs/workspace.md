# Workspace Structure

> Reference for workspace tangibles based on Godot WorkspaceSchema.

---

## Workspace Structure

**Schema type**: `WorkspaceData`

**Fields**:
- `tangibles` (array): Array of tangible objects (NumLine, Vocab, Benchmark, MathExpression, Grid)

**Example**:
```json
{
  "@type": "WorkspaceData",
  "tangibles": [
    {"@type": "NumLine", ...}
  ]
}
```

---

## Common Tangible Fields

All tangibles support these optional layout fields:

- `@col` (integer): Column position in layout
- `@layout` (string): Layout mode - `"underlay"`, `"default"`, or `"overlay"`

---

## Tangible Types

### NumLine (Number Line)
**Schema type**: `NumLine`

**Purpose**: 1D visual representation showing intervals, tick marks, and fraction positions.

**Required Fields**:
- Must have either `ticks` OR `intervals` (but not both)

**Optional Fields**:

**visual** (string): Visual representation type. Default: `"line"`
- Valid values: `"bar"`, `"pie"`, `"line"`, `"equation"`, `"bar_sm"`, `"composite_bar_equation"`, `"polygon"`

**sum_is_visible** (boolean): Show sum of intervals. Default: `false`

**lcm** (integer): Least common multiple for calculations. Default: `24`

**range** (array of 2 integers): Start and end bounds. Default: `[0, 1]`

**ticks** (Fraction or array of Fractions): Tick mark positions

**intervals** (Fraction or array of Fractions): Interval sizes (auto-generates ticks)

**points** (array of Fractions): Highlighted point positions. Must be fraction strings like "1/4", "2/3", not floats. Default: `[]`

**labels** (boolean or array of Fractions): Which ticks show fraction labels (positioned below number line). INTERACTIVE - can be dragged with Move tool (mode="frac_labels"). Default: `true`

**alt_labels** (boolean or array of Fractions): Alternative labels for ticks (positioned on top of number line). NON-INTERACTIVE - cannot be dragged into or out of. Used for fixed reference labels. Default: `false`

**invert_labels** (boolean): Flips the position of labels and alt_labels. When `true`, labels appear on top (interactive) and alt_labels appear below (non-interactive). Use this to allow dragging labels to the top position. Default: `false`

**intervals_is_frac_label_visible** (boolean or array of integers): Show labels on intervals. Default: `false`

**ticks_is_read_only** (boolean or array of Fractions): Make ticks non-interactive. Default: `false`
- Valid: `true` (all ticks), `false` (no ticks), or `["0", "1/3", "2/3"]` (specific fraction strings)
- INVALID: `[true, true, false, ...]` (arrays of booleans are not supported)

**intervals_is_read_only** (boolean or array of integers): Make intervals non-interactive. Default: `false`
- Valid: `true` (all intervals), `false` (no intervals), or `[0, 1, 2]` (specific interval indices)
- INVALID: `[true, false, true, ...]` (arrays of booleans are not supported)

**is_read_only** (boolean): Make entire number line read-only. Default: `false`

**sum_location** (string): Position of sum display. Options: `"top"`, `"bottom"`, `"left"`, `"right"`. Default: `"right"`

**intervals_is_shaded** (boolean or array of integers): Which intervals are shaded. Default: `false`

**Important**: Cannot specify both `ticks` and `intervals` - use one or the other

**Tick Specification**:

**IMPORTANT**: Ticks must be specified as **fraction strings** (e.g., "1/4", "2/4"), **NOT** as float arrays (e.g., 0.25, 0.5). Floats are not supported.

Single fraction (uniform spacing):
```json
"ticks": "1/3"
// Generates: [0, "1/3", "2/3", 1] within the range
```

Array of fractions (explicit positions):
```json
"ticks": ["0", "1/3", "2/3", "1"]
// ✓ CORRECT: Fraction strings
// ✗ WRONG: [0, 0.333, 0.666, 1] - floats not supported
```

**Interval Specification**:

**IMPORTANT**: Intervals must be specified as **fraction strings**, **NOT** floats.

Single fraction (uniform intervals):
```json
"intervals": "1/4"
// Generates ticks at: [0, "1/4", "1/2", "3/4", 1]
```

Array of fractions (explicit interval sizes):
```json
"intervals": ["1/4", "1/4", "1/2"]
// Generates ticks at: [0, "1/4", "1/2", 1]
// ✓ CORRECT: Fraction strings
// ✗ WRONG: [0.25, 0.25, 0.5] - floats not supported
```

**Labels Specification**:

**labels** (interactive, positioned below by default):

Boolean (all or none):
```json
"labels": true   // All ticks labeled below (can be dragged)
"labels": false  // No ticks labeled
```

Array (specific ticks to label - must match tick fraction strings):
```json
"labels": ["0", "1/2", "1"]  // Only these ticks labeled below
// ✓ CORRECT: Fraction strings matching tick positions
// ✗ WRONG: [0, 0.5, 1] - floats not supported
```

**alt_labels** (non-interactive, positioned on top by default):

Same format as labels but NON-DRAGGABLE, displays on top:
```json
"alt_labels": true              // All ticks labeled on top (fixed, cannot drag)
"alt_labels": ["0", "1"]        // Only these ticks labeled on top (fixed)
```

**invert_labels** (swaps positions):

```json
"invert_labels": false  // Default: labels below (draggable), alt_labels on top (fixed)
"invert_labels": true   // Inverted: labels on top (draggable), alt_labels below (fixed)
```

**Use case for invert_labels:** When you want students to drag labels to the TOP position, set `"invert_labels": true`. This places the interactive labels on top while keeping fixed reference labels below.

**Note:** Both `labels` and `alt_labels` can be used simultaneously. Only `labels` can be dragged; `alt_labels` are always fixed display-only.

**Example - Basic Number Line**:
```json
{
  "@type": "NumLine",
  "visual": "line",
  "range": [0, 1],
  "ticks": "1/3",
  "points": ["2/3"],
  "labels": ["0", "1"],
  "lcm": 12
}
```

**Example - Number Line with Intervals**:
```json
{
  "@type": "NumLine",
  "visual": "bar",
  "range": [0, 1],
  "intervals": "1/4",
  "intervals_is_shaded": [0, 2],
  "lcm": 24
}
```

**Example - Draggable Labels with Fixed Reference Labels**:
```json
{
  "@type": "NumLine",
  "visual": "line",
  "range": [0, 1],
  "ticks": "1/4",
  "labels": false,           // No draggable labels initially (student will drag them)
  "alt_labels": ["0", "1"],  // Fixed reference labels on top
  "lcm": 24
}
```

**Example - Drag Labels to Top Position**:
```json
{
  "@type": "NumLine",
  "visual": "line",
  "range": [0, 1],
  "ticks": "1/3",
  "labels": false,           // No draggable labels initially
  "alt_labels": ["0", "1"],  // Fixed labels that will appear below when inverted
  "invert_labels": true,     // Swap positions: draggable on top, fixed below
  "lcm": 12
}
```

---

### Vocab (Vocabulary Label)
**Schema type**: `Vocab`

**Purpose**: Text label or vocabulary term displayed in workspace.

**Required Fields**:
- `label` (string): The text to display

**Optional Fields**:
- `is_highlighted` (boolean): Whether label is emphasized. Default: `false`

**Example**:
```json
{
  "@type": "Vocab",
  "label": "unit fraction",
  "is_highlighted": false,
  "@col": 0,
  "@layout": "default"
}
```

---

### Benchmark
**Schema type**: `Benchmark`

**Purpose**: Reference line or marker (often at 1/2 for comparison).

**Optional Fields**:
- `location` (Fraction): Position of benchmark. Default: `"1/2"`

**Example**:
```json
{
  "@type": "Benchmark",
  "location": "1/2",
  "@col": 0,
  "@layout": "underlay"
}
```

**Note**: Benchmarks typically use `@layout: "underlay"` to appear behind other tangibles.

---

### MathExpression (Mathematical Expression)
**Schema type**: `MathExpression`

**Purpose**: Displays mathematical expressions with fractions and operators.

**Optional Fields**:
- `terms` (array): Array of Fractions or Term objects representing the expression

**Example**:
```json
{
  "@type": "MathExpression",
  "terms": ["1/4", "+", "2/4", "=", "3/4"],
  "@col": 0,
  "@layout": "default"
}
```

**Note**: Terms can be either Fraction objects or Term objects (operators, symbols, etc.). Fraction terms automatically have their labels set to visible.

---

### Grid
**Schema type**: `Grid`

**Purpose**: 2D grid representation for area models and fraction visualization.

**Optional Fields**:
- `h_lcm` (integer): Horizontal divisions (columns). Default: `8`
- `v_lcm` (integer): Vertical divisions (rows). Default: `4`

**Example**:
```json
{
  "@type": "Grid",
  "h_lcm": 8,
  "v_lcm": 4,
}
```

**Note**: Grid automatically generates parts based on h_lcm × v_lcm dimensions, with each part representing `1/(h_lcm × v_lcm)`.

---

## Fraction Format

Fractions are specified as **strings** in "numerator/denominator" format:

**Valid formats**:
- `"1/3"` - proper fraction
- `"2/3"` - proper fraction
- `"4/4"` - whole number as fraction
- `"3"` or `"1"` or `"0"` - whole numbers (equivalent to "3/1", "1/1", "0/1")

**Invalid formats** (will cause errors):
- `0.25` - float/decimal (use `"1/4"` instead)
- `[0.25, 0.5, 0.75]` - array of floats (use `["1/4", "2/4", "3/4"]` instead)
- `1/4` - unquoted (use `"1/4"` with quotes)

**Schema handling**:
- Deserializer: Parses string to `Fraction` object with `numerator` and `denominator` fields
- Serializer: Converts `Fraction` object back to string format
  - If denominator is 1: outputs `"3"` (not `"3/1"`)
  - Otherwise: outputs `"3/4"` format

---

## Field Behaviors

### Boolean vs Array Fields

Several fields accept both boolean and array values:

**Boolean mode** (applies to all):
```json
"labels": true          // All ticks labeled
"labels": false         // No ticks labeled
"ticks_is_read_only": true   // All ticks read-only
```

**Array mode** (applies to specific items):
```json
"labels": ["0", "1"]              // Only these ticks labeled
"ticks_is_read_only": ["1/3", "2/3"]  // Only these ticks read-only
"intervals_is_shaded": [0, 2]         // Only intervals at index 0 and 2 shaded
```

### Read-Only Behavior

Multiple levels of read-only controls:

1. **Entire tangible**: `is_read_only: true` - Nothing can be modified
2. **Specific ticks**: `ticks_is_read_only: ["1/3"]` - Only certain ticks locked
3. **Specific intervals/parts**: `read_only_parts: [0, 2]` - Only certain sections locked

---

## Serialization/Deserialization Notes

The schema handles conversion between JSON and internal Godot objects:

**Deserialization** (JSON → Godot):
- String fractions → `Fraction` objects
- Single fraction → Array of ticks/intervals
- Boolean flags → Configured internal state

**Serialization** (Godot → JSON):
- Omits default values for cleaner JSON
- Converts uniform ticks back to single fraction
- Converts boolean arrays back to boolean if all true/false
- Example: All ticks labeled → `"labels": true` instead of array

**Validation errors** are returned for:
- Using deprecated GRID visual (value 2)
- Specifying both `ticks` and `intervals`
- Invalid fraction formats
- References to non-existent ticks

---

## Layout System

Tangibles can be positioned using layout fields:

**Column positioning**:
```json
"@col": 0  // First column
"@col": 1  // Second column
```

**Layer positioning**:
```json
"@layout": "underlay"   // Behind other elements
"@layout": "default"    // Normal layer
"@layout": "overlay"    // In front of other elements
```

**Typical usage**:
- Benchmarks: `@layout: "underlay"`
- Main tangibles: `@layout: "default"` (or omit)
- Highlights: `@layout: "overlay"`

---

## Module 4 Path B Usage

For number line focused activities:

**Primary tangible**: `NumLine` with `visual: "line"`

**Common patterns**:

**Single number line with point**:
```json
{
  "@type": "NumLine",
  "visual": "line",
  "ticks": "1/3",
  "points": ["2/3"],
  "labels": ["0", "1"]
}
```

**Comparison set (multiple lines)**:
```json
{
  "tangibles": [
    {"@type": "NumLine", "ticks": "1/3", ...},
    {"@type": "NumLine", "ticks": "1/4", ...}
  ]
}
```

**Benchmark reference**:
```json
{
  "tangibles": [
    {"@type": "Benchmark", "location": "1/2", "@layout": "underlay"},
    {"@type": "NumLine", ...}
  ]
}
```

**Not typically used in Module 4 Path B**:
- Interval shading (focuses on tick positions)
