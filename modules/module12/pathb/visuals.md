# Visuals

> A designer reference for different shapes, their division methods, and available student actions for the given module and path.

---
  ## Shape: Number Line

  A 1D visual representation showing equal intervals with tick marks and fraction positions.

  ### Properties
  - **State**: Can be whole (showing only endpoints) or divided with tick marks
  - **Range**: The numerical bounds [start, end], typically [0, 1] but can extend to show fractions greater than 1
  - **Role**: Determines if this is a reference visual (non-interactable) or an option/target (interactable)
    - **Reference**: For display only - cannot be selected, clicked, or modified (e.g., reference bar at top for comparison)
    - **Option/Target**: Default - can be selected, clicked, or modified by student (e.g., selectable answer choices)
    - Mark reference tangibles in workspace descriptions as "reference bar" or "for comparison only"

  ### Ticks
  Marks at specific positions on the number line.

  #### ticks
  Vertical marks indicating specific positions.
  - **Type**: Fraction OR array of fractions
  - **Description**: Marks at fraction positions on the number line
  - **Always includes**: Ticks at start and end points (e.g., 0 and 1)
  - **is_read_only**: Boolean indicating whether the tick is interactable (default: `false`). Set to `true` for tick marks that should not accept dragged labels (e.g., endpoints, already labeled ticks)

  #### points
  Additional visual emphasis by placing dots or points on specific ticks.

  - **Type**: Array of fractions (must correspond to tick positions)
  - **Description**: Highlights specific ticks with dots

  #### labels
  Text annotations on specific ticks.

  - **Type**: Array of fractions (must correspond to tick positions)
  - **Description**: Display fraction values as text at tick positions
  - **Boolean**: Enable/disable labels for all ticks

  ### Example Configurations

  **Basic number line with sevenths:**
  ```
  range: [0, 1]
  ticks: 1/7
  // Creates: Number line from 0 to 1 with tick marks at sevenths
  ```

  **Number line with pre-placed point:**
  ```
  range: [0, 1]
  ticks: 1/7
  points: [2/7]
  labels: [0, 1]
  // Creates: Number line with sevenths, point placed at 2/7, endpoints labeled
  ```

  **Two stacked number lines with benchmark:**
  ```
  Benchmark at 1/2 (underlay, spans both lines)
  Line 1: range [0,1], ticks 1/4, points [3/4], labels [0, 1]
  Line 2: range [0,1], ticks 1/6, points [1/6], labels [0, 1]
  // Creates: Stacked lines with a vertical 1/2 reference line visible across both
  ```

  ### Constraints
  - Number lines are always labeled with start and end values (typically 0 and 1)
  - Denominators used in this module: 3, 4, 5, 6, 7, 8, 9, or 10
  - Maximum of 2 number lines can be shown for comparison (stacked vertically)
  - Points and labels can only be attached to existing ticks
  - A Benchmark tangible in the same column will render as a vertical line crossing all stacked number lines

  ### Allowed Student Actions
  - **Select**: Select number lines (1 or more) that match the question requirements. For example, select the fraction above the benchmark.
  - **Place point**: Place points at specific tick marks (1 or more). For example, place a point at 2/7 or place 3/8 on the line.

---
  ## Shape: Fraction Strip

  A 1D rectangular bar representing a whole, shown as a horizontal strip that can be divided into equal sections.

  ### Properties
  - **State**: Can be whole (undivided) or divided into equal sections
  - **Range**: The numerical bounds [start, end], typically [0, 1] but can extend to show fractions greater than 1
  - **Role**: Determines if this is a reference visual (non-interactable) or an option/target (interactable)
    - **Reference**: For display only - cannot be selected, clicked, or modified (e.g., reference bar at top showing target fraction)
    - **Option/Target**: Default - can be selected, clicked, or modified by student (e.g., bars to shade, option bars to select from)
    - Mark reference tangibles in workspace descriptions as "reference bar" or "for comparison only"

  ### Intervals
  The equal parts created by dividing the strip.

  #### intervals
  How the strip is divided into equal parts.

  - **Type**: Single fraction (uniform) OR array of fractions (non-uniform)
  - **Description**: Defines the size of each interval. A single fraction like "1/6" creates 6 equal sections.
  - **Uniform**: Use single fraction (e.g., "1/6" → sixths bar with 6 equal intervals)
  - **Non-uniform**: Use array of fractions (e.g., ["1/4", "1/4", "1/2"])

  #### shaded_intervals
  Which intervals are filled to represent the numerator.

  - **Type**: Count, Boolean, or array of interval indices (0-based)
  - **Count**: First N intervals are shaded — the most common case, where N is the numerator (e.g., 1 shades the first interval of a fourths bar → shows 1/4)
  - **Boolean**: `true` shades all intervals, `false` shades none
  - **Array**: Specific indices to shade for non-consecutive shading (e.g., [0, 2] shades first and third)

  #### missing_intervals
  Which intervals are visually highlighted as "missing" (unshaded and emphasized).

  - **Type**: Array of interval indices (0-based)
  - **Description**: Used in close-to-1 problems where the unshaded remainder is the focus. Highlights the gap visually so students can compare missing pieces across bars.
  - **Example**: A 7/8 bar with `missing_intervals: [7]` highlights the last interval as the missing piece

  ### Labels

  #### interval_labels
  A unit fraction label on each individual interval.

  - **Type**: Boolean OR array of interval indices
  - **Description**: Shows the unit fraction on each piece (e.g., "1/4" on every interval of a fourths bar). Use when reinforcing what each individual piece represents.
  - **Boolean**: `true` labels all intervals, `false` labels none
  - **Array**: Indices of intervals to label

  ### Example Configurations

  **Single shaded bar with benchmark:**
  ```
  Benchmark at 1/2 (underlay)
  Bar: intervals 1/4, shaded_intervals: 3
  // Shows 3/4 with a vertical 1/2 reference line crossing the bar
  ```

  **Close-to-1 comparison (missing piece focus):**
  ```
  Bar 1: intervals 1/8, shaded_intervals: 7, missing_intervals: [7]
  Bar 2: intervals 1/6, shaded_intervals: 5, missing_intervals: [5]
  // Both bars mostly filled; unshaded pieces highlighted for comparison
  ```

  **Same-numerator comparison (different denominators):**
  ```
  Bar 1: intervals 1/5, shaded_intervals: 3
  Bar 2: intervals 1/7, shaded_intervals: 3
  // Same count shaded; fifths pieces visibly wider than sevenths pieces
  ```

  ### Constraints
  - Denominators used in this module: 3, 4, 5, 6, 7, 8, 9, or 10
  - Maximum of 2 fraction strips can be shown for comparison
  - A Benchmark tangible in the same column will render as a vertical line crossing all strips
  - `missing_intervals` should only be used when the unshaded remainder is the explicit focus of the question

  ### Allowed Student Actions
  - **Select**: Select fraction strips (1 or more) that match the question requirements. For example, click the bar that shows the bigger piece.

---
  ## Shape: Math Expression

  A horizontal mathematical expression displayed as text. Used to show fraction notation, comparison statements, and symbols alongside or independent of visual shapes.

  ### Terms
  The content of the expression is defined as an ordered list of terms. Each term is one of:

  - **Fraction** — a fraction value, displayed as a formatted fraction (e.g., 3/5 renders as stacked numerator/denominator)
  - **Symbol** — a comparison operator: `>`, `<`, `=`
  - **Placeholder** — `" ? "` indicates where the student's selected symbol will appear

  ### Common Patterns

  #### fraction_label
  A single fraction shown beside a bar to name it.
  ```
  terms: [3/5]
  ```

  #### comparison_with_placeholder
  Shows the full comparison with an unknown symbol for the student to fill in.
  ```
  terms: [3/5, " ? ", 3/7]
  ```

  #### benchmark_comparison_with_placeholder
  Shows a fraction compared to the benchmark with an unknown symbol.
  ```
  terms: [3/5, " ? ", 1/2]
  ```

  #### complete_comparison_statement
  Shows a resolved comparison, typically after a correct answer or during explanation.
  ```
  terms: [3/5, >, 3/7]
  ```

  ### Constraints
  - Terms are rendered left to right in a single line
  - Fractions render as stacked notation (numerator over denominator), not inline (3/5)

---
  ## Shape: Benchmark

  A vertical reference line that spans across all visuals in the same column. Used to help students compare fractions against a known value (typically 1/2).

  ### Properties
  - **Location**: The fraction position where the line is drawn. Defaults to `1/2`.
  - **Label**: A fraction label displayed at the line's position. Visible by default — shows the benchmark value (e.g., "1/2") so students can read it.
  - **Layout**: Always renders as an underlay — behind all bars and number lines in the same column, so the shapes remain in the foreground.

  ### Behaviour
  - The benchmark is a **separate tangible** placed in the workspace alongside bars and number lines — it is not a property of a bar or line
  - It spans vertically across the full height of its column, crossing all stacked shapes
  - Students cannot interact with it (always read-only)
  - When used with stacked number lines, the line crosses both lines simultaneously at the same horizontal position
  - When used with fraction strips, the line crosses the bar at the proportional position (e.g., 1/2 falls at the midpoint of the bar)

  ### Configuration

  **Minimal (benchmark at 1/2 with label — most common):**
  ```
  Benchmark (all defaults)
  // Draws a vertical line at 1/2 with a "1/2" label
  ```

  **Without label:**
  ```
  Benchmark
  is_label_visible: false
  // Draws a vertical line at 1/2 with no text label
  ```

  **At a different position:**
  ```
  Benchmark
  location: 3/4
  // Draws a vertical line at 3/4 with a "3/4" label
  ```

  ### Constraints
  - Only one benchmark per column
  - Benchmark module 12 always uses location `1/2` (the default) — no need to specify
  - The label is on by default; hide it only if the position is visually obvious from context
