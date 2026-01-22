# Visuals

> A designer reference for different shapes, their division methods, and available student actions for the given module and path.

---
  ## Shape: Rectangle

  A 2D rectangle with one longer side and one shorter side.

  ### Properties
  - **Orientation**: Can be horizontal (default) or vertical
  - **State**: Can be whole (undivided) or divided into equal intervals or divided into unequal intervals

  ### Intervals
  The distinct parts (sections) of the rectangle. Intervals are created by dividing horizontally (rows), vertically (columns), or both (grid).

  #### horizontal_intervals
  Row divisions across the height of the rectangle.

  - **Type**: Array of fractions OR nested array of arrays of fractions
  - **Description**: Defines how the rectangle is divided into horizontal rows
  - **Simple array**: Creates full-width rows that span the entire width
    - Fractions represent the height of each row (must sum to 1)
    - Example: `[1/3, 1/3, 1/3]` creates 3 equal rows
  - **Nested array**: When vertical_intervals is a simple array, defines different column divisions within each row
    - Each element is an array of fractions for that row's columns
    - Example: `[[1/2, 1/2], [1], [1/3, 1/3, 1/3]]` = row 0 has 2 columns, row 1 is undivided, row 2 has 3 columns
  - **Undivided**: Use `[1]` for no horizontal divisions

  #### vertical_intervals
  Column divisions across the width of the rectangle.

  - **Type**: Array of fractions OR nested array of arrays of fractions
  - **Description**: Defines how the rectangle is divided into vertical columns
  - **Simple array**: Creates full-height columns that span the entire height
    - Fractions represent the width of each column (must sum to 1)
    - Example: `[1/4, 1/4, 1/2]` creates 3 unequal columns
  - **Nested array**: When horizontal_intervals is a simple array, defines different row divisions within each column
    - Each element is an array of fractions for that column's rows
    - Example: `[[1/2, 1/2], [1/3, 1/3, 1/3], [1]]` = column 0 has 2 rows, column 1 has 3 rows, column 2 is undivided
  - **Undivided**: Use `[1]` for no vertical divisions

  #### shaded_intervals
  Which intervals are filled in versus left empty.

  - **Type**: Array of integers (indices) OR position descriptor string
  - **Description**: Specifies which of the created intervals should be shaded
  - **Examples**:
    - `[0, 2, 5]` shades intervals at indices 0, 2, and 5
    - `"row 1, column 2"` shades the interval at that position

  ### Example Configurations

  **Full grid** (both simple arrays):
  ```
  horizontal_intervals: [1/3, 1/3, 1/3]
  vertical_intervals: [1/4, 1/4, 1/4, 1/4]
  // Creates: 3 × 4 = 12 intervals
  ```

  **Row-first with custom columns** (horizontal simple, vertical nested):
  ```
  horizontal_intervals: [1/3, 1/3, 1/3]
  vertical_intervals: [[1/2, 1/2], [1], [1/6, 2/6, 3/6]]
  // Creates: 2 + 1 + 3 = 6 intervals
  ```

  **Column-first with custom rows** (vertical simple, horizontal nested):
  ```
  vertical_intervals: [1/4, 1/4, 1/2]
  horizontal_intervals: [[1/2, 1/2], [1/3, 1/3, 1/3], [1]]
  // Creates: 2 + 3 + 1 = 6 intervals
  ```

  ### Constraints
  - Cuts across longer side: maximum 7 (creates up to 8 intervals)
    - Longer side = width when horizontal orientation, height when vertical orientation
  - Cuts across shorter side: maximum 5 (creates up to 6 intervals)
    - Shorter side = height when horizontal orientation, width when vertical orientation

  ### Allowed Student Actions
  - **Cut**: Divide the whole into intervals using available cut types
  - **Shade**: Select intervals to shade or unshade
  - **Select**: Select the whole shape for interaction
---

  ## Shape: Hexagon

  A 2D hexagon (6-sided polygon) with natural symmetry.

  ### Properties
  - **Orientation**: Can be flat-top (default) or pointy-top
  - **State**: Can be whole (undivided) or divided into intervals

  ### Intervals
  The distinct wedge-shaped parts (sections) of the hexagon. Intervals are created by radial cuts from the center outward.

  #### radial_intervals
  Wedge divisions radiating from the center to the edges.

  - **Type**: Array of fractions
  - **Description**: Defines how the hexagon is divided into wedge-shaped sections
  - **Simple array**: Each fraction represents the angular proportion of the whole (must sum to 1)
  - **Undivided**: Use `[1]` for no divisions

  #### shaded_intervals
  Which intervals are filled in versus left empty.

  - **Type**: Array of integers (indices) OR position descriptor string
  - **Description**: Specifies which of the created intervals should be shaded
  - **Examples**:
    - `[0, 2]` shades intervals at indices 0 and 2
    - `"wedge 1 of 3"` shades the interval at that position

  ### Example Configurations

  **Equal division - halves:**
  ```
  radial_intervals: [1/2, 1/2]
  // Creates: 2 equal wedges
  ```

  **Equal division - thirds:**
  ```
  radial_intervals: [1/3, 1/3, 1/3]
  // Creates: 3 equal wedges
  ```

  **Unequal division:**
  ```
  radial_intervals: [1/2, 1/4, 1/4]
  // Creates: 3 unequal wedges
  ```

  ### Constraints
  - Maximum intervals: 6 (array length ≤ 6)
  - Symmetrical equal divisions only allow: 2, 3, or 6 equal intervals
  - Unequal divisions allow: 2 to 5 intervals
  - All fractions must sum to 1

  ### Allowed Student Actions
  - **Cut**: Divide the whole into intervals using radial cuts from center
  - **Shade**: Select intervals to shade or unshade
  - **Select**: Select the whole shape for interaction