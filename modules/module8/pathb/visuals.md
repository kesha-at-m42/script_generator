# Visuals

> A designer reference for different shapes, their division methods, and available student actions for the given module and path.

---
  ## Shape: Number Line

  A 1D visual representation showing equal intervals with tick marks and fraction positions.

  ### Properties
  - **State**: Can be whole (showing only endpoints) or divided with tick marks
  - **Range**: The numerical bounds [start, end], typically [0, 1] but can extend to show fractions greater than 1

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

  ### Intervals
  The distinct sections (parts) created by dividing the strip.

  #### intervals
  Interval sizes defining how the strip is divided.

  - **Type**: Fraction OR array of fractions
  - **Description**: Defines the size of each section in the strip
  - **Uniform spacing**: Use single fraction (e.g., "1/3" creates 3 equal sections)
  - **Non-uniform spacing**: Use array of fractions (e.g., ["1/4", "1/4", "1/2"])

  #### intervals_is_shaded
  Which sections are shaded.

  - **Type**: Boolean OR array of integers (indices)
  - **Description**: Specifies which sections should be shaded
  - **Boolean**: `true` shades all sections, `false` shades none
  - **Array**: Indices of sections to shade (e.g., [0, 2] shades first and third sections)

  #### intervals_is_read_only
  Which sections are non-interactable.

  - **Type**: Boolean OR array of integers (indices)
  - **Description**: Makes specific sections non-interactable
  - **Default**: `false`

  ### Example Configurations

  **Basic fraction strip with thirds:**
  ```
  range: [0, 1]
  intervals: "1/3"
  // Creates: Strip divided into 3 equal sections
  ```

  **Fraction strip with shaded sections:**
  ```
  range: [0, 1]
  intervals: "1/4"
  intervals_is_shaded: [0, 2]
  // Creates: Strip with fourths, first and third sections shaded
  ```

  ### Constraints
  - Denominators are commonly limited to: 2, 3, 4, 5, 6, or 8
  - Maximum of 3 fraction strips can be shown for comparison

  ### Allowed Student Actions
  - **Cut**: Divide the whole strip into intervals. For example, divide this strip into thirds.
  - **Select**: Select fraction strips (1 or more) that match the question requirements. For example, select the strip showing fifths.
  - **Shade**: Select sections to shade or unshade. For example, shade 2/3 of the strip.
