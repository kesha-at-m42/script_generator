# Prompt: warmup_generator
# Generated: 2026-01-21T16:45:20.293070
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 18000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are converting a detailed lesson specification into structured JSON format. This is TRANSLATION work, not creative work. The pedagogical decisions have already been made—your job is faithful conversion.

----------------------------------------------------------------------

### Block 2: Reference Doc (visuals.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: visuals.md

<visuals>
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
</visuals>

----------------------------------------------------------------------

### Block 3: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS




Convert each of the interactions listed in <warmup_specs> into the structured JSOn format.

For each interaction,
 #### Step 1: Understand Intent
 - What is the **educational purpose** of this interaction?
 - What **misconception** is it addressing or what **concept** is it activating?
 - What makes this interaction different from others?
 Using this, fill these fields of:
  "interaction_id": 1,
  "interaction_name": "Pithy name (3-6 words)"
 

 #### Step 2: Analyze Visual Description and refer to <visuals> to Set Up Workspace
 For each shape described:
 1. Determine **shape type** (rectangle or hexagon)
 2. Determine if **divided** or whole
 3. If divided, identify **cut type**:
    - Vertical cuts? How many columns?
    - Horizontal cuts? How many rows?
    - Radial cuts (hexagon)?
 4. Determine if parts are **equal or unequal**
 5. Express cuts as **part size fractions**:
    - Equal: all fractions identical (e.g., `[1/3, 1/3, 1/3]`)
    - Unequal: fractions differ (e.g., `[1/2, 1/4, 1/4]`)
 6. Determine **shading** (if any)

 Create workspace object:
 ```json
 {
   "toy_id": "descriptive_id",
   "toy_shape": "rectangle|hexagon",
   "toy_description": "Clear description from warmup_specs",
   "divided": true|false,
   "division_count": N,
   "is_divided_equal": true|false,
   "horizontal_cuts": [],
   "vertical_cuts": [],
   "radial_cuts": [],
   "shaded": []
 }
 ```

 #### Step 4: Determine Dialogue and Correct Answer
 Refer back to:
 - **Visual**: What student sees
 - **Purpose**: Why this interaction exists
 - **Content**: What warmup_specs says should happen

 Write:
 1. **dialogue**: Guide speaks (include [event:name] tags if demonstration)
    - Use only vocabulary from USE column
    - Match tone from specifications
    - Reference the visual purpose
 2. **prompt**: What student should do (clear action)
 3. **interaction_tool**: select, cut, shade, click_choice, or none
 4. **correct_answer**:
    - value: toy_id of correct choice OR expected input
    - context: Why this is correct (educational reasoning)

 ---

 ## CUT REPRESENTATION GUIDE:

 Cuts are **part sizes** (fractions that sum to 1).

 ### Simple divisions (1D array):
 ```
 ["1/2", "1/2"]           → 2 equal parts
 ["1/3", "1/3", "1/3"]      → 3 equal parts
 ["1/2", "1/4", "1/4"]      → 3 unequal parts
 ```

 ### Grids (both dimensions have 1D arrays):
 ```
 vertical_cuts: ["1/2", "1/2"]
 horizontal_cuts: ["1/2", "1/2"]
 → 2×2 grid = 4 equal parts
 ```

 ### Partial cuts (2D array for columns with different row divisions):
 ```
 vertical_cuts: ["1/2", "1/2"]           → 2 columns
 horizontal_cuts: [["1/2, "1/2"], ["1"]]  → column 1: 2 rows, column 2: whole
 → 3 total parts
 ```
 ---

  CRITICAL: Output ONLY valid JSON as described in <output_structure>. No explanations. No analysis. No verification.
  Your entire response must be ONLY the JSON object starting with { and ending with }.




----------------------------------------------------------------------

### Block 4: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>



{
  "sequences": [
    {
      "interaction_id": 1,
      "interaction_name": "Pithy name (3-6 words)",
      "fractions": [],
      "vocabulary_introduced": [],
      "steps": [
        {
          "dialogue": "Guide dialogue with [event:name] tags for demonstrations",
          "prompt": "Student action instruction",
          "interaction_tool": "cut|shade|select|multi_select|click_choice|none",
          "workspace": [
            {
            "toy_id": "rect_unequal_2",
            "toy_shape": "rectangle",
            "toy_description": "Rectangle divided into 2 unequal parts",
            "divided": true,
            "division_count": 2,
            "is_divided_equal": false,
            "horizontal_cuts": [],
            "vertical_cuts": ["1/3", "2/3"],
            "radial_cuts": [],
            "shaded": []
          }
          ],
          "correct_answer": {
            "value": "expected_answer",
            "context": "Why this is correct"
          },
          "student_attempts": {
            "success_path": {
              "dialogue": "Brief positive feedback"
            }
          }
        }
      ]
    }
  ]
}
  

</output_structure>

----------------------------------------------------------------------

## User Message

<input>
# Warmup Specs

## Interaction 1: Identify Equal Parts
Student sees 3 rectangles...

</input>

======================================================================

