# Validators

> Reference for validator types based on Godot ValidatorSchema.

---

## Validator Types

### ShadedValidator
**Schema type**: `ShadedValidator`

**Purpose**: Validates that shapes/intervals are shaded to match a target fraction.

**Fields**:
- `answer` (Fraction): The target fraction that should be shaded (e.g., `"3/4"`)

**Example**:
```json
{
  "@type": "ShadedValidator",
  "answer": "3/4"
}
```

---

### ShadedPartsValidator
**Schema type**: `ShadedPartsValidator`

**Purpose**: Validates that an exact count of parts are shaded (integer validation).

**Fields**:
- `answer` (optional, integer, min: 0): Number of parts that should be shaded

**Example**:
```json
{
  "@type": "ShadedPartsValidator",
  "answer": 3
}
```

---

### SameShadedValidator
**Schema type**: `SameShadedValidator`

**Purpose**: Validates that multiple tangibles have the same amount shaded (comparison validation).

**Fields**: None

**Example**:
```json
{
  "@type": "SameShadedValidator"
}
```

---

### SelectionValidator
**Schema type**: `SelectionValidator`

**Purpose**: Validates that correct tangible(s) are selected from workspace.

**Fields**:
- `answer` (integer OR array of integers): Index/indices of correct tangible(s)
  - Single selection: `0` or `[0]`
  - Multiple selection: `[0, 2]`

**Index Counting**:
- Indices count **ALL tangibles in the tangibles array** (0-based)
- This **includes read-only tangibles** (reference bars, etc.)
- Example workspace:
  ```json
  "tangibles": [
    { "@type": "NumLine", "is_read_only": true, "intervals": "1/4" },  // Index 0
    { "@type": "NumLine", "intervals": "1/2" },                        // Index 1
    { "@type": "NumLine", "intervals": "1/3" },                        // Index 2
    { "@type": "NumLine", "intervals": "1/6" }                         // Index 3
  ]
  ```
  - To select the "1/2" bar: `answer: 1`
  - To select the "1/3" bar: `answer: 2`
  - To select both "1/2" and "1/6": `answer: [1, 3]`

**Examples**:

Single selection:
```json
{
  "@type": "SelectionValidator",
  "answer": 0
}
```

Multiple selection:
```json
{
  "@type": "SelectionValidator",
  "answer": [0, 2]
}
```

---

### MultipleChoiceValidator
**Schema type**: `MultipleChoiceValidator`

**Purpose**: Validates selection from multiple choice options.

**Fields**:
- `answer` (array of integers, min: 0): Indices of correct choice(s)
  - 0-based indexing
  - Can contain multiple indices for multi-select questions

**Example**:
```json
{
  "@type": "MultipleChoiceValidator",
  "answer": [1]
}
```

**Conversion notes**:
- Choice id "a" → index `[0]`
- Choice id "b" → index `[1]`
- Choice id "c" → index `[2]`

---

### TickValidator
**Schema type**: `TickValidator`

**Purpose**: Validates the fraction size of parts (e.g., after cutting/dividing) and tick placement on number lines.

**Fields**:
- `answer` (Fraction OR array of Fractions): Expected tick position(s) or fraction size of parts

**Answer Format**:
- **Shorthand (string)**: A single fraction like `"1/3"` validates all tick marks for that denominator (scales to any range: 0-1, 0-2, etc.)
  - `"1/3"` → validates all ticks for thirds (1/3, 2/3 on 0-1; or 1/3, 2/3, 4/3, 5/3 on 0-2)
  - `"1/4"` → validates all ticks for fourths
  - `"1/8"` → validates all ticks for eighths
- **Array (explicit)**: Validates specific tick positions; MUST include endpoints
  - `["0", "1/3", "2/3", "1"]` for thirds
  - `["0", "1/4", "2/4", "3/4", "1"]` for fourths

**Examples**:

Shorthand for thirds (validates all ticks for thirds):
```json
{
  "@type": "TickValidator",
  "answer": "1/3"
}
```

Explicit array (validates these specific ticks):
```json
{
  "@type": "TickValidator",
  "answer": ["0", "1/3", "2/3", "1"]
}
```

**Note**: A single position like `"2/3"` is not meaningful as shorthand. Use `"1/3"` to validate all thirds, or use explicit array format.

---

### PointValidator
**Schema type**: `PointValidator`

**Purpose**: Validates that points are placed at correct positions on number line. Used with Move tool (mode="points").

**Fields**:
- `answer` (array of Fractions): Expected point positions

**Example**:
```json
{
  "@type": "PointValidator",
  "answer": ["2/7"]
}
```

---

### LabelValidator
**Schema type**: `LabelValidator`

**Purpose**: Validates dragged fraction labels placed on number line ticks. Used with Move tool (mode="frac_labels" with palette).

**Fields**:
- `answer` (array of Fractions): The labels that should be dragged from the palette to correct positions

**Example**:
```json
{
  "@type": "LabelValidator",
  "answer": ["1/4"]
}
```

**Important**: Answer array should ONLY include the labels being validated from the palette, NOT all tick marks or pre-existing labels.
- If palette has `["1/6"]` → answer: `["1/6"]`
- If palette has `["1/3", "2/3"]` → answer: `["1/3", "2/3"]`
- Do NOT include all possible tick positions

---

## Validator Selection Guide

**For Move tool (placing points, mode="points")**:
- Use: `PointValidator`
- Answer format: `["2/7"]` (array of fractions)

**For Move tool (dragging labels, mode="frac_labels" with palette)**:
- Use: `LabelValidator`
- Answer format: Labels from palette `["1/3"]` or `["1/3", "2/3"]`

**For Place tool (placing ticks)**:
- Use: `TickValidator`
- Answer format (shorthand): `"1/3"` (validates all ticks for thirds, scales to any range)
- Answer format (explicit): `["0", "1/3", "2/3", "1"]` (validates specific ticks, must include endpoints)

**For Select tool (single)**:
- Use: `SelectionValidator`
- Answer format: `0` or `[0]`

**For Select tool (multi)**:
- Use: `SelectionValidator`
- Answer format: `[0, 2]`

**For MCQ (choices)**:
- Use: `MultipleChoiceValidator`
- Answer format: `[1]`

**For Paint tool (proportion)**:
- Use: `ShadedValidator`
- Answer format: `"3/4"`

**For Paint tool (count)**:
- Use: `ShadedPartsValidator`
- Answer format: `3`

---

## Answer Format Reference

### Fraction Format
Fractions are specified as strings:
- Format: `"numerator/denominator"` (e.g., `"2/3"`, `"1/4"`)
- Whole numbers: `"3"` or `"3/1"`
- Always use strings, not numeric types

### Index Format
Tangible and choice indices are 0-based integers:
- First item: `0`
- Second item: `1`
- Third item: `2`

### Single vs Array
- `SelectionValidator` accepts both single integer and array
- `MultipleChoiceValidator` requires array (even for single choice)
- `TickValidator` accepts both single fraction and array
- `LabelValidator` requires array

