# Workspace Structure

> Reference for workspace tangibles based on Godot WorkspaceSchema.

---

## Workspace Structure

**Schema type**: `WorkspaceData`

**Fields**:
- `tangibles` (array): Array of tangible objects (NumLine, FracShape, Vocab, Benchmark)
- `shuffle_tangibles` (optional, boolean): Whether to randomize tangible order

**Example**:
```json
{
  "@type": "WorkspaceData",
  "tangibles": [
    {"@type": "NumLine", ...}
  ],
  "shuffle_tangibles": false
}
```

---

## Common Tangible Fields

All tangibles support these optional layout fields:

- `@col` (integer): Column position in layout
- `@layout` (string): Layout mode - `"underlay"`, `"default"`, or `"overlay"`
- `is_visible` (boolean): Whether tangible is visible. Default: `true`

---

## Tangible Types

### NumLine (Number Line)
**Schema type**: `NumLine`

**Type constant**: `TYPE_NUM_LINE = "num_line"`

**Purpose**: 1D visual representation showing intervals, tick marks, and fraction positions.

**Required Fields**:
- Must have either `ticks` OR `intervals` (but not both)

**Optional Fields**:

**visual** (integer or string): Visual representation type. Default: `LINE`
- String values (recommended): `"bar"`, `"pie"`, `"line"`, `"equation"`, `"bar_sm"`, `"composite_bar_equation"`, `"polygon"`
- Integer values (legacy): 0=BAR, 1=PIE, 2=GRID (DEPRECATED)

**sum_is_visible** (boolean): Show sum of intervals. Default: `false`

**lcm** (integer): Least common multiple for calculations. Default: `24`

**range** (array of 2 integers): Start and end bounds. Default: `[0, 1]`

**ticks** (Fraction or array of Fractions): Tick mark positions

**intervals** (Fraction or array of Fractions): Interval sizes (auto-generates ticks)

**points** (array of Fractions): Highlighted point positions. Default: `[]`

**labels** (boolean or array of Fractions): Which ticks show fraction labels. Default: `true`

**alt_labels** (boolean or array of Fractions): Alternative labels for ticks. Default: `false`

**invert_labels** (boolean): Invert label display. Default: `false`

**intervals_is_frac_label_visible** (boolean or array of integers): Show labels on intervals. Default: `false`

**ticks_is_read_only** (boolean or array of Fractions): Make ticks non-interactive. Default: `false`

**intervals_is_read_only** (boolean or array of integers): Make intervals non-interactive. Default: `false`

**is_read_only** (boolean): Make entire number line read-only. Default: `false`

**Important**:
- `visual: GRID` (2) is deprecated and will cause validation error
- Cannot specify both `ticks` and `intervals` - use one or the other

**Tick Specification**:

Single fraction (uniform spacing):
```json
"ticks": "1/3"
// Generates: [0, "1/3", "2/3", 1] within the range
```

Array of fractions (explicit positions):
```json
"ticks": ["0", "1/3", "2/3", "1"]
```

**Interval Specification**:

Single fraction (uniform intervals):
```json
"intervals": "1/4"
// Generates ticks at: [0, "1/4", "1/2", "3/4", 1]
```

Array of fractions (explicit interval sizes):
```json
"intervals": ["1/4", "1/4", "1/2"]
// Generates ticks at: [0, "1/4", "1/2", 1]
```

**Labels Specification**:

Boolean (all or none):
```json
"labels": true   // All ticks labeled
"labels": false  // No ticks labeled
```

Array (specific ticks):
```json
"labels": ["0", "1/2", "1"]  // Only these ticks labeled
```

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

---

### FracShape (Fraction Shape)
**Schema type**: `FracShape`

**Type constant**: `TYPE_FRACTION_SHAPE = "fraction_shape"`

**Purpose**: 2D shapes (bars, circles) for representing fractions visually.

**Optional Fields**:

**fractions** (Fraction or array of Fractions): Size of each part. Default: `["1/1"]`

**visual** (integer): Shape type. Default: `0` (BAR)
- 0 = BAR (rectangle)
- 1 = PIE (circle)
- 2 = GRID (DEPRECATED - will error)

**shaded** (array of integers): Indices of shaded parts. Default: `[]`

**missing** (array of integers): Indices of missing parts. Default: `[]`

**frac_label_visible** (array of integers): Which parts show labels. Default: `[]`

**read_only_parts** (array of integers): Non-interactive parts. Default: `[]`

**lcm** (integer): Least common multiple. Default: `24`

**num_rows** (integer): Number of rows (for grid layouts)

**is_read_only** (boolean): Make entire shape read-only. Default: `false`

**sum_is_visible** (boolean): Show sum of parts. Default: `false`

**Fractions Specification**:

Single fraction (uniform parts):
```json
"fractions": "1/4"
// Creates shape divided into fourths
```

Array (non-uniform parts):
```json
"fractions": ["1/4", "1/2", "1/4"]
// Creates shape with varying part sizes
```

Omitted (whole shape):
```json
// No "fractions" field = undivided whole
```

**Example - Shaded Fraction Bar**:
```json
{
  "@type": "FracShape",
  "visual": 0,
  "fractions": "1/4",
  "shaded": [0, 1, 2],
  "lcm": 24,
  "is_visible": true
}
```

**Note**: FracShape uses internal `NumLine` representation in Godot. Many properties mirror NumLine structure.

---

### Vocab (Vocabulary Label)
**Schema type**: `Vocab`

**Type constant**: `TYPE_VOCAB = "vocab"`

**Purpose**: Text label or vocabulary term displayed in workspace.

**Required Fields**:
- `label` (string): The text to display

**Optional Fields**:
- `is_visible` (boolean): Whether label is shown. Default: `true`
- `is_highlighted` (boolean): Whether label is emphasized. Default: `false`

**Example**:
```json
{
  "@type": "Vocab",
  "label": "unit fraction",
  "is_visible": true,
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

## Fraction Format

Fractions are specified as strings in "numerator/denominator" format:

**Valid formats**:
- `"1/3"` - proper fraction
- `"2/3"` - proper fraction
- `"4/4"` - whole number as fraction
- `"3"` - whole number (equivalent to "3/1")

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
- `FracShape` (focuses on number lines, not bars/circles)
- Interval shading (focuses on tick positions)
