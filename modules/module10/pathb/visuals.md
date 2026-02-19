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

  **Basic number line with thirds:**
  ```
  range: [0, 1]
  ticks: [0, 1/3, 2/3, 1]
  // Creates: Number line from 0 to 1 with tick marks at thirds
  ```

  **Number line with partly labeled and emphasized points:**
  ```
  range: [0, 1]
  ticks: [0, 1/4, 1/2, 3/4, 1]
  points: [1/4, 3/4]
  labels: [1/4, 3/4]
  // Creates: Number line with fourths, highlighting and labeling 1/4 and 3/4
  ```

  ### Constraints
  - Number lines are always labeled with start and end values (typically 0 and 1)
  - Denominators are commonly limited to: 2, 3, 4, 6, or 8
  - Maximum of 3 number lines can be shown for comparison
  - Points and labels can only be attached to existing ticks

  ### Allowed Student Actions
  - **Place tick**: Place ticks on an unpartitioned or partially partitioned number bar. For example, divide this line into thirds or place a tick at 3/5.
  - **Select**: Select number lines (1 or more) that match the question requirements. For example, select the number line showing fifths.
  - **Place point**: Place points at specific tick marks (1 or more). For example, place a point at 3/5 or place 3/5 on the line.
  - **Label**: Label tick marks (1 or more) by dragging fraction labels (1 or more) to them. For example, place/drag the correct label on the given tick mark or place/drag the given fraction on the correct number line.

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
  - **Count**: First N intervals are shaded — the most common case, where N is the numerator (e.g., 4 shades the first four intervals of a sixths bar → shows 4/6)
  - **Boolean**: `true` shades all intervals, `false` shades none
  - **Array**: Specific indices to shade for non-consecutive shading (e.g., [0, 2] shades first and third)

  ### Labels

  #### interval_labels
  A unit fraction label on each individual interval.

  - **Type**: Boolean OR array of interval indices
  - **Description**: Shows the unit fraction on each piece (e.g., "1/6" on every interval of a sixths bar). Use when reinforcing what each individual piece represents.
  - **Boolean**: `true` labels all intervals, `false` labels none
  - **Array**: Indices of intervals to label

  ### Example Configurations

  **Basic sixths strip:**
  ```
  intervals: 1/6
  // Creates: Strip divided into 6 equal sections, none shaded
  ```

  **Strip with shading:**
  ```
  intervals: 1/4
  shaded_intervals: 3
  // Creates: Fourths strip with first 3 intervals shaded (shows 3/4)
  ```

  ### Constraints
  - Denominators used in this module: 4, 5, 6, 7, 8, 10, 12
  - Maximum of 3 fraction strips can be shown for comparison
  - All strips in a comparison group must share the same denominator

  ### Allowed Student Actions
  - **Select**: Select fraction strips (1 or more) that match the question requirements. For example, click the bar that has more parts shaded.
  - **Shade**: Select intervals to shade or unshade. For example, shade 2/3 of the strip.

---
  ## Shape: Math Expression

  A horizontal mathematical expression displayed as text. Used to show fraction notation, comparison statements, and symbols alongside or independent of visual shapes.

  ### Terms
  The content of the expression is defined as an ordered list of terms. Each term is one of:

  - **Fraction** — a fraction value, displayed as a formatted fraction (e.g., 2/6 renders as stacked numerator/denominator)
  - **Symbol** — a comparison operator: `>`, `<`, `=`
  - **Placeholder** — `" ? "` indicates where the student's selected symbol will appear

  ### Common Patterns

  #### fraction_label
  A single fraction shown beside a bar to name it.
  ```
  terms: [4/6]
  ```

  #### comparison_with_placeholder
  Shows the full comparison with an unknown symbol for the student to fill in.
  ```
  terms: [4/6, " ? ", 2/6]
  ```

  #### complete_comparison_statement
  Shows a resolved comparison, typically after a correct answer or during explanation.
  ```
  terms: [4/6, >, 2/6]
  ```

  #### symbol_only
  Displays a single comparison symbol in isolation, used during symbol introduction or explanation steps.
  ```
  terms: [>]
  ```

  ### Constraints
  - Terms are rendered left to right in a single line
  - Fractions render as stacked notation (numerator over denominator), not inline (2/6)
