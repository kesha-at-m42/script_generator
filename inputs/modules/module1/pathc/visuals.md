# Visuals

> A designer reference for different shapes, their division methods, and available student actions for the given module and path.

---
  ## Shape: Rectangle

  A 2D rectangle with one longer side and one shorter side.

  ### Properties
  - **Orientation**: Can be horizontal (default) or vertical
  - **State**: Can be whole (undivided) or divided into parts
  - **Available cut types**: Horizontal, Vertical

  ### Division Properties
  - **Total intervals**: The number of distinct sections created by all cuts

  - **Equal or unequal intervals**: Intervals can be equally or unequally sized
    - **Equal intervals examples** (achieving 12 total intervals):
      - 3 equally-spaced vertical cuts (4 equal columns) + 2 equally-spaced horizontal cuts (3 equal rows) = 12 equal parts
      - 5 equally-spaced vertical cuts (6 equal columns) + 1 equally-spaced horizontal cut (2 equal rows) = 12 equal parts

    - **Unequal intervals examples** (achieving 12 total intervals):
      - 5 unequally-spaced vertical cuts + 1 partial horizontal cut spanning only columns 1-5 = 12 unequal parts
      - 3 equally-spaced vertical cuts (4 equal columns) + 2 unequally-spaced horizontal cuts = 12 unequal parts

  - **Vertical cuts**: Cut across the width to create columns
    - Example: 3 vertical cuts = 4 columns
    - Can be equally or unequally spaced
    - Can be full cuts (spanning entire height) or partial cuts (spanning specific rows only)

  - **Horizontal cuts**: Cut across the height to create rows
    - Example: 2 horizontal cuts = 3 rows
    - Can be equally or unequally spaced
    - Can be full cuts (spanning entire width) or partial cuts (spanning specific columns only)

  - **Shaded intervals**: Which parts are shaded in the default layout
    - Example: "2 out of 4 parts shaded" or "row 2 in column 1 and row 5 in column 3 shaded"

  ### Constraints
  - Cuts across longer side: maximum 7 (creates up to 8 intervals)
    - Longer side = width when horizontal orientation, height when vertical orientation
  - Cuts across shorter side: maximum 5 (creates up to 6 intervals)
    - Shorter side = height when horizontal orientation, width when vertical orientation

  ### Allowed Student Actions
  - **Cut**: Divide the whole into parts using available cut types
  - **Shade**: Select parts to shade or unshade
  - **Select**: Select the whole shape for interaction
---

  ## Shape: Hexagon

  A 2D hexagon (6-sided polygon) with natural symmetry.

  ### Properties
  - **Orientation**: Can be flat-top (default) or pointy-top
  - **State**: Can be whole (undivided) or divided into parts
  - **Available cut types**: Radial

  ### Division Properties
  - **Total intervals**: The number of distinct sections created by all cuts

  - **Equal or unequal intervals**: Intervals can be equally or unequally sized depending on cut placement
    - **Equal intervals examples** (cuts along symmetry axes):
      - 2 radial cuts along symmetry axes = 2 equal parts (halves)
      - 3 radial cuts along symmetry axes = 3 equal parts (thirds)
      - 6 radial cuts along symmetry axes = 6 equal parts (sixths)
    - **Unequal intervals examples** (cuts not along symmetry axes):
      - 2 radial cuts at non-symmetrical angles = 2 unequal parts
      - 3 radial cuts at non-symmetrical angles = 3 unequal parts
      - Up to 5 radial cuts can create up to 5 unequal parts

  - **Radial cuts**: Cuts from center outward (toward vertices or edges)
    - Example: 2 radial cuts = 2 parts
    - Can follow symmetry axes (creating equal parts) or be placed freely (creating unequal parts)

  - **Shaded intervals**: Which parts are shaded in the default layout
    - Example: "1 of 3 parts shaded"

  ### Constraints
  - Maximum radial cuts: 6 (creates up to 6 parts)
  - Symmetrical divisions only allow: 2, 3, or 6 equal parts
  - Unequal divisions allow: 2 to 5 unequal parts

  ### Allowed Student Actions
  - **Cut**: Divide the whole into parts using radial cuts from center
  - **Shade**: Select parts to shade or unshade
  - **Select**: Select the whole shape for interaction