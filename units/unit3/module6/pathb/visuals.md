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
