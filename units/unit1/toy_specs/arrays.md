# Arrays

Category: Unit 1
Created: February 4, 2026 10:36 AM
Status: Ready for UX
Target Audience: Grade 3 Unit 2, Grade 3 Unit 4

---

> **WHAT:** Rectangular grid arrangements of objects or dots where items are organized in clear rows and columns, progressing from concrete objects (egg cartons, muffin tins) through mixed representations (concrete + dots side-by-side) to abstract dot grids, with interactive features that allow students to toggle between row and column interpretations and see the same array structure in multiple ways.

**WHY:** Arrays are the critical second model of multiplication (after equal groups) and serve a fundamentally different pedagogical purpose: they make the **commutative property** visible and provable rather than merely stated. The system must support demonstrating that the same 3×4 array can be read as "3 rows of 4" OR "4 columns of 3," making it visually undeniable that 3×4 = 4×3 (same physical arrangement, different reading). This **representational duality** is a sophisticated mathematical concept that prepares students for algebraic thinking. The abstraction progression (concrete objects → mixed → dots) follows CRA principles but is compressed into M11-M12 because students already have multiplication fluency from M7-M10. Research shows that explicit instruction on both row and column interpretations (rather than defaulting to rows only) increases student performance on commutative property tasks by 0.45-0.62 effect sizes. Arrays are used for **property discovery**, not repetitive practice—the focus is helping students see and prove mathematical relationships through visual structure.
>

## Shape:

- UX to provide visuals

### Rectangular Array Structure

The defining characteristic: items organized in aligned rows and aligned columns forming a rectangle.

📷 *Placeholder for array structure diagram showing rows and columns labeled*

**Key Properties:**

- **Rows:** Horizontal lines of items (extend left-right)
- **Columns:** Vertical lines of items (extend top-bottom)
- **Rectangular:** All rows have same number of items; all columns have same number of items
- **Aligned:** Items line up both horizontally and vertically
- **No gaps:** Every position in the grid is filled

**Example - 3×4 Array:**

`● ● ● ●
● ● ● ●
● ● ● ●`

- 3 rows (3 horizontal lines)
- 4 columns (4 vertical lines)
- 12 total items

**Critical Distinction from Equal Groups:**

- Equal groups: Items clustered (3 bags of 4 apples)
- Arrays: Items aligned in grid (3 rows of 4 apples)

---

### Abstraction Progression: Three Stages

The pedagogical sequence from concrete to abstract array representations.

📷 *Placeholder for abstraction progression visual showing all three stages*

**Stage 1: Concrete Objects (M11 Early)**

📷 *Placeholder for concrete array examples (egg cartons, muffin tins)*

**Visual Design:**

- **Egg cartons:** Real-looking egg carton with eggs in rectangular grid
- **Muffin tins:** Muffin pan with muffins in rectangular array
- **Ice cube trays:** Ice tray with ice cubes in grid
- **Chocolate boxes:** Box with chocolates arranged in rows and columns

**Purpose:** Introduction to rectangular structure using familiar objects; rows and columns are visible but feel natural

**Examples:**

- 2×6 egg carton (2 rows of 6 eggs)
- 3×4 muffin tin (3 rows of 4 muffins)
- 4×5 chocolate box (4 rows of 5 chocolates)

**Pedagogical Note:** Concrete objects make the grid structure feel "real" and purposeful. Students encounter these in daily life, so the rectangular organization makes sense.

---

**Stage 2: Mixed Concrete/Abstract (M11 Mid)**

📷 *Placeholder for side-by-side comparison: concrete + dots*

**Visual Design:**

- **Side-by-side display:** Concrete array (left) + Dot array (right)
- **Same dimensions:** 3×4 muffin tin shows same structure as 3×4 dot grid
- **Visual connection:** Arrows or alignment lines showing equivalence

**Purpose:** Bridge from concrete to abstract; students see that dots can represent any objects; same structure, different representation

**Examples:**

- Muffin tin (3×4) paired with dot grid (3×4)
- Egg carton (2×6) paired with dot grid (2×6)
- Ice cube tray (4×5) paired with dot grid (4×5)

**Pedagogical Note:** This explicit comparison is crucial—students need to see that the dot grid is NOT a different problem, but the SAME array in abstract form.

---

**Stage 3: Dot Arrays (M11 Late, M12 Primary)**

📷 *Placeholder for dot array examples with various dimensions*

**Visual Design:**

- **Simple dots:** Uniform size (8-12px diameter), evenly spaced
- **Grid structure:** Clear row and column alignment
- **Grid overlay (optional):** Faint gridlines between rows/columns (toggleable)
- **Color coding (optional):** Can highlight rows OR columns

**Purpose:** Pure mathematical representation; focus on structure without object distractions; standard format for property exploration

**Examples:**

- 3×4 dot array
- 4×3 dot array (same dots, different dimensions—THIS IS THE CRITICAL COMPARISON)
- 5×2 dot array
- 2×5 dot array

**Pedagogical Note:** Dot arrays are the **workhorse for M12 property discovery**. They're clean, abstract, and allow students to focus on structure and mathematical relationships.

---

### Row Emphasis vs Column Emphasis

Visual and symbolic representations must support showing the same array with different interpretations.

📷 *Placeholder for same array shown with row emphasis vs column emphasis*

**Row Emphasis Requirements:**

- **Visual:** Rows visually emphasized (color-coding, highlighting, or other distinction)
- **Language:** "3 rows of 4" or "3 rows with 4 items each"
- **Equation requirement:** Must display/support equation showing first factor as rows (e.g., 3 × 4 = 12)

**Column Emphasis Requirements:**

- **Visual:** Columns visually emphasized (color-coding, highlighting, or other distinction)
- **Language:** "4 columns of 3" or "4 columns with 3 items each"
- **Equation requirement:** Must display/support equation showing first factor as columns (e.g., 4 × 3 = 12)

**The Critical Teaching Need:**

- System must support switching between row and column emphasis for the same array
- When emphasis changes, equation must update to match the interpretation
- **Purpose:** Demonstrate that same array = same total, therefore 3 × 4 = 4 × 3 (commutative property)

**Implementation Note:** Emphasis switching may be guide-controlled demonstration, student-interactive toggle, or combination. Equations may be displayed via integrated text, Equation Builder toy, or other method. Requirements focus on **what must be shown**, not **how it's implemented**.

---

### Grid Overlay (Scaffolding Feature)

Optional gridlines that make structure more visible.

📷 *Placeholder for array with grid overlay on vs off*

**Visual Design:**

- **Faint lines** between rows and columns
- **Does not obscure items/dots**
- **Toggleable:** Can be shown or hidden

**Purpose:**

- Help students who struggle to see rows/columns in early M11
- Scaffolding that fades as proficiency increases
- Makes alignment explicit

**Default State:**

- **M11 Early:** ON by default (help students see structure)
- **M11 Late / M12:** OFF by default (students can toggle if needed)

## Properties

### Abstraction Level

- UX to provide visual examples

| Level | Visual Treatment | When Used | Purpose |
| --- | --- | --- | --- |
| **Concrete Objects** | Egg cartons, muffin tins, ice trays | M11 Early | Familiar rectangular structure; real-world connection |
| **Mixed (Concrete + Dots)** | Side-by-side comparison | M11 Mid | Bridge to abstraction; show equivalence |
| **Dot Arrays** | Pure dot grids | M11 Late, M12 | Mathematical representation; property exploration |

### Emphasis Mode (Interactive State)

- UX to provide visuals for each mode

| Mode | Description | Visual Treatment | Equation Form |
| --- | --- | --- | --- |
| **Neutral** | No emphasis | Standard dot grid | Can write either way |
| **Row Emphasis** | Rows highlighted | Horizontal color-coding or highlighting | 3 × 4 = 12 ("3 rows of 4") |
| **Column Emphasis** | Columns highlighted | Vertical color-coding or highlighting | 4 × 3 = 12 ("4 columns of 3") |

### Grid Overlay State

| State | Description | When |
| --- | --- | --- |
| **Grid On** | Gridlines visible | M11 Early (default), student-requested later |
| **Grid Off** | No gridlines | M11 Late / M12 (default) |

### Array Dimensions

| Property | Typical Range | Notes |
| --- | --- | --- |
| Minimum size | 2×2 | Smallest meaningful array |
| Maximum size | 10×10 | Grade 3 factor range is 0-12; 10×10 provides adequate coverage while maintaining visibility |
| Common sizes | 2×3, 3×4, 2×5, 4×5, 3×6, 5×8, 4×9, 6×7, 10×2, 2×10 | Based on Grade 3 multiplication focus and products within 100 |

### Fact Family View (Unit 4)

An integrated display mode showing one array with all four related equations visible simultaneously.

📷 *Placeholder for array with fact family equations arranged around it*

| Component | Description |
| --- | --- |
| **Array** | Standard dot array (M3–M5 use dot arrays, not concrete objects) |
| **Equation set** | All four equations displayed: 2 multiplication + 2 division |
| **Visual connection** | Each equation is visually linked to the array (e.g., positioned near the corresponding reading — row equations near rows, column equations near columns) |
| **Highlight sync** | When an equation is in focus, the corresponding array emphasis activates (e.g., focusing on "3 × 5 = 15" triggers row emphasis) |

**Equation Arrangement Options (UX to decide):**

- **Around the array:** Row equations left/right, column equations above/below
- **Below the array:** All four in a grid, with active equation highlighted
- **Sequential reveal:** Show one equation at a time, building to all four

**Scaffolding States:**

| State | What's Shown | When Used |
| --- | --- | --- |
| **Full display** | Array + all 4 equations | M4 Late — confirm understanding |
| **Partial display** | Array + 1-2 given equations; student generates the rest | M4 Mid — practice generating related facts |
| **Array only** | Array shown; student generates all 4 equations independently | M4 Exit Check / Practice |
| **Equation only** | One equation given; student identifies or builds the array | M3-M4 — reverse direction (equation → visual) |

**Implementation Note:** Fact family equations may be rendered by the Equation Builder toy displayed alongside the array, by integrated text labels, or by another method. The requirement is that all four equations are **simultaneously visible** and **visually connected to the array** in the full display state.

### Division Question Frame (Unit 4)

Controls whether the array is presented as a multiplication or division context.

| Frame | Prompt Pattern | Equation Format | Visual Treatment |
| --- | --- | --- | --- |
| **Multiplication** | "How many total?" | ___ × ___ = ? | Standard (Unit 1 behavior) |
| **Division (partitive)** | "___ items in ___ equal rows. How many in each row?" | ___ ÷ ___ = ? | Row emphasis; row count labeled, items-per-row is unknown |
| **Division (quotitive)** | "___ items with ___ in each column. How many columns?" | ___ ÷ ___ = ? | Column emphasis; column size labeled, column count is unknown |
| **Inverse/Unknown factor** | "___ × ? = ___" | ? × ___ = ___ | One dimension labeled, one shown as ? / □ / letter |

**Key Design Principle:** The array itself looks the same regardless of frame. What changes is the question text, equation format, emphasis mode, and which dimension is labeled vs. unknown. This reinforces the inverse relationship — students see that multiplication and division are two ways of reading the same structure.

## Allowed Student Actions

### Observe Array Structure

- UX to provide interaction visual/video

**Description:** Student views array to identify rows and columns.

**Interaction:**

- View array (concrete, mixed, or dots)
- Visually identify: "How many rows?"
- Visually identify: "How many columns?"

**Purpose:** Build recognition of rectangular structure; distinguish rows from columns.

### Specify Array Dimensions (Structured Question)

- UX to provide interaction visual/video

**Description:** Student indicates rows and columns after viewing array.

**Interaction:**

- **View array** (concrete, mixed, or dots)
- **Answer question:** "How many rows?" (multiple choice, number input, or other method)
- **Answer question:** "How many columns?" (multiple choice, number input, or other method)

**Feedback:**

- **Correct:** Confirmation message
- **Incorrect:** System provides correction (may include highlighting rows/columns sequentially to help counting)

**Purpose:** Explicit identification of array dimensions; practice distinguishing rows from columns.

### Match Array to Equations (Both Interpretations)

- UX to provide interaction visual/video

**Description:** Student recognizes that array matches BOTH row and column equations.

**Interaction:**

- **View array** (e.g., 3×4 dot grid)
- **Question format varies:**
    - "Which equations describe this array?" (select all that apply)
    - Separate questions for row and column interpretations
    - Other formats as determined by UX

**Expected outcome:** Student recognizes both 3 × 4 and 4 × 3 are valid for same array

**Purpose:** Reinforce that BOTH interpretations are valid; commutative property foundation.

**Note:** Equation display/building may be handled by Equation Builder toy appearing alongside, integrated display, or other method.

### Specify and Build Array (Interactive Construction)

- UX to provide interaction visual/video

**Description:** Student specifies array dimensions and system builds the array.

**Interaction:**

1. **Student receives prompt** (e.g., "Make an array with 20 items")
2. **Student chooses interpretation:** "Rows" or "Columns"
3. **Student specifies structure:**
    - "Making  ***rows of*** " (e.g., 4 rows of 5)
    - OR "Making  ***columns of*** " (e.g., 5 columns of 4)
4. **System builds array** based on specification
5. **Student writes matching expression** using Equation Builder
6. **System validates:** Language matches expression?

**Variations:**

- **Given total, student chooses structure:** "Make an array with 20 items" → Student decides 4×5, 5×4, 2×10, etc.
- **Given partial structure:** "Make 3 rows of ___" → Student completes specification

**Purpose:** Active construction; connect language to structure; practice translating between verbal description and visual array.

**Note:** Student specifies STRUCTURE; system generates the visual. NOT dragging individual dots.

### Unit 4: Identify Division Equation from Array

- UX to provide interaction visual/video

**Description:** Student views an array and writes or selects the corresponding division equation.

**Interaction:**

- **View array** with one dimension emphasized and labeled (e.g., "3 rows" highlighted)
- **Question:** "There are 15 dots in 3 equal rows. How many in each row?"
- **Student action:** Select/build the equation 15 ÷ 3 = ? (via MC or Equation Builder)
- **Verify:** Student confirms answer (5) matches the visible column count

**Variations:**

- Given row emphasis → write partitive division equation
- Given column emphasis → write quotitive division equation
- Given array with NO emphasis → student chooses which division equation to write

**Purpose:** Connect array visual to division notation; distinguish partitive and quotitive division from the same representation.

---

### Unit 4: Generate Fact Family from Array

- UX to provide interaction visual/video

**Description:** Student produces all four related equations from a single array.

**Interaction:**

1. **View array** (e.g., 4×6 dot grid = 24 total)
2. **System prompts sequentially or all-at-once** (scaffolding-dependent):
    - "Write a multiplication equation for the rows" → 4 × 6 = 24
    - "Write a multiplication equation for the columns" → 6 × 4 = 24
    - "Write a division equation" → 24 ÷ 4 = 6
    - "Write another division equation" → 24 ÷ 6 = 4
3. **System displays all four** in fact family view

**Scaffolding Progression:**

| Level | Support | Student Does |
| --- | --- | --- |
| **M3 Early** | Array shown + 2 multiplication equations given → student writes 1 division equation | Generate one related division fact |
| **M3 Late** | Array shown + 1 multiplication equation given → student generates remaining 3 | Generate three related facts |
| **M4 Early** | Array shown → student generates all 4 equations with sequential prompts | Generate full fact family with guidance |
| **M4 Mid** | Array shown → student generates all 4 equations independently | Full independent fact family production |
| **M4 Late** | One equation given (no array) → student generates remaining 3 | Abstract fact family production (array available as optional scaffold) |

**Purpose:** Build understanding of WHY four facts exist from one arrangement; transition from visual grounding to abstract fact family fluency.

---

### Unit 4: Solve Unknown Factor Using Array

- UX to provide interaction visual/video

**Description:** Student uses an array to find the missing factor in a division/multiplication equation.

**Interaction:**

- **View equation with unknown:** ? × 4 = 20 (or equivalently: 20 ÷ 4 = ?)
- **View array:** 4 columns visible, dots visible, row count is the unknown
- **Student counts/identifies:** 5 rows → ? = 5
- **Student confirms:** 5 × 4 = 20 ✓

**Variations:**

- Unknown in first position: ? × 4 = 20 (find number of rows)
- Unknown in second position: 5 × ? = 20 (find number of columns)
- Division format: 20 ÷ 4 = ? (same array, different equation frame)

**Purpose:** Ground the unknown-factor strategy (3.OA.B.6) in visual evidence; make "think multiplication to solve division" concrete and verifiable.

---

### Unit 4: Match Division Expression to Array (Select Correct Array)

- UX to provide interaction visual/video

**Description:** Given a division expression, student selects the array that represents it from 2-4 options.

**Interaction:**

- **View expression:** 18 ÷ 3 = ?
- **View 2-4 array options** (e.g., 3×6, 6×3, 2×9, 3×5)
- **Student selects** the correct array(s)
- **Follow-up:** "How does this array show 18 ÷ 3?" (MC: "3 rows with 6 in each" / "6 groups of 3" / etc.)

**Key Design Consideration:** Both a 3×6 and a 6×3 array are valid for 18 ÷ 3 — but they represent different division interpretations (partitive vs. quotitive). Whether both are accepted or a specific interpretation is required depends on the module and learning goal.

**Purpose:** Strengthen connection between symbolic division and visual array representation; assess whether students understand what division "looks like."

## Additional Teaching/Remediation Actions

These are system capabilities for guide-led demonstrations and instruction.

### Switch Row/Column Emphasis

- UX to provide visual/video

**Description:** System switches visual emphasis between row and column interpretations.

**Requirements:**

- Must support showing same array with row emphasis, then switching to column emphasis (or vice versa)
- Visual treatment changes to match emphasis (row highlighting vs column highlighting)
- Equation display must update to match interpretation
    - Row emphasis → equation like "3 × 4 = 12" or "3 rows of 4"
    - Column emphasis → equation like "4 × 3 = 12" or "4 columns of 3"

**Purpose:** Guide demonstrates "Look, same array, but we can read it two ways!"

**Implementation Note:** May be guide-controlled only, student-interactive, or combination. Equation display may use Equation Builder toy, integrated text, or other method.

**Control:** Guide-controlled demonstration only. NOT student-interactive. Students explore both interpretations through "Match Array to Equations" tasks, not by toggling emphasis themselves.

### Highlight Single Row or Column

- UX to provide visual/video

**Description:** Guide draws attention to specific row or column during instruction.

**Example:**

- Guide says "Look at this row" → That row highlights
- Guide says "Look at this column" → That column highlights

**Purpose:** Direct focus; model row vs column distinction.

### Sequential Row Highlighting

- UX to provide visual/video

**Description:** Rows highlight one at a time in sequence.

**Example - 3 rows of 4:**

- Highlight row 1: "4 items"
- Highlight row 2: "4 items"
- Highlight row 3: "4 items"
- Guide: "3 rows, each with 4 items. That's 3 × 4."

**Purpose:** Model counting rows; connect to row equation format.

### Sequential Column Highlighting

- UX to provide visual/video

**Description:** Columns highlight one at a time in sequence.

**Example - 4 columns of 3:**

- Highlight column 1: "3 items"
- Highlight column 2: "3 items"
- Highlight column 3: "3 items"
- Highlight column 4: "3 items"
- Guide: "4 columns, each with 3 items. That's 4 × 3."

**Purpose:** Model counting columns; connect to column equation format.

### Side-by-Side Array Comparison

- UX to provide visual/video

**Description:** Display two arrays side-by-side for comparison (e.g., 3×4 and 4×3).

**Example:**

- **Left:** 3×4 array (3 rows of 4)
- **Right:** 4×3 array (4 rows of 3)
- **Both highlighted to show they're different arrangements**
- Guide: "These look different, but do they have the same total?"

**Purpose:** Visual comparison for commutative property; show that 3×4 ≠ same visual as 4×3, but both = 12 total.

**Critical Pedagogical Note:** This is DIFFERENT from toggling row/column emphasis. This shows two ACTUALLY DIFFERENT arrays (rotated 90°) that happen to have the same total.

### Array Rotation Animation (M12 Property Discovery)

- UX to provide visual/video

**Description:** Physically rotate array 90° to show how 3×4 becomes 4×3.

**Example:**

- Start with 3×4 array (3 rows of 4, horizontal orientation)
- Animation: Array rotates 90° clockwise
- Result: Now 4×3 array (4 rows of 3, vertical orientation)
- Guide: "Look! When we rotate the array, the rows become columns and the columns become rows. But we didn't add or remove any items. So the total stays the same!"

**Purpose:**

- **THE CRITICAL PROOF** of commutative property
- Visual demonstration that 3×4 and 4×3 are related by rotation
- Make abstract property concrete and undeniable

**Note:** This is different from switching emphasis (same array, different reading) vs rotation (physically different arrangement).

### Grid Overlay Control

- UX to provide visual/video

**Description:** System can show/hide gridlines on arrays.

**Requirements:**

- Gridlines between rows and columns
- Faint enough not to obscure items
- Can be toggled on/off

**Purpose:** Scaffolding tool—helps students see structure early in M11, can be removed as proficiency increases.

**Implementation Note:** May be guide-controlled, student-controlled, or both.

### Unit 4: Division Reading Demonstration

- UX to provide visual/video

**Description:** Guide demonstrates reading the same array as both multiplication AND division.

**Sequence:**

1. Display 3×5 array (neutral, no emphasis)
2. Activate row emphasis: "Look — 3 rows of 5. That's 3 × 5 = 15."
3. Pause. Return to neutral.
4. Re-activate row emphasis with division frame: "Now think about it this way: 15 dots, arranged in 3 equal rows. How many in each row? 15 ÷ 3 = 5."
5. Display both equations side by side: 3 × 5 = 15 AND 15 ÷ 3 = 5
6. Guide: "Same array. Same numbers. Two different questions."

**Purpose:** THE critical teaching moment for the inverse relationship. Students see that multiplication and division are not separate operations but different readings of the same structure.

**When used:** M3 Lesson — first introduction of multiplication-division connection.

---

### Unit 4: Non-Commutativity of Division Discovery

- UX to provide visual/video

**Description:** Guide leads students through discovering that while multiplication IS commutative, division is NOT.

**Sequence:**

1. **Multiplication test:** Show 3×5 array. "3 × 5 = 15."
2. **Rotate 90°** (existing rotation animation). "5 × 3 = 15."
3. **Confirm:** "Same total! Multiplication: order doesn't change the answer." ✓
4. **Division test — set up:** "Let's try division."
5. **Show 12 ÷ 4:** Display 3×4 array with row emphasis. "12 in 4 columns → 3 per column. 12 ÷ 4 = 3."
6. **Swap:** "What about 4 ÷ 12? Can we put 4 items into 12 equal groups?"
7. **Visual evidence:** Try to show — there aren't enough items. Each group would get less than 1. "That doesn't give us a whole number."
8. **Conclusion:** "Multiplication: order doesn't matter. Division: order DOES matter. 12 ÷ 4 ≠ 4 ÷ 12."

**Purpose:** Explicitly address Misconception A3 (overgeneralizing commutativity to division). This is a DISCOVERY experience — the student should feel the surprise of division behaving differently.

**When used:** M5 — immediately after commutativity confirmation, while the comparison is fresh.

**Implementation Note:** Steps 6-7 require showing that 4 ÷ 12 doesn't work with whole numbers. This could be a concrete demonstration (trying to deal 4 objects into 12 groups), a visual comparison (arrays of different sizes), or a discussion prompt. The specific mechanism is flexible; the pedagogical requirement is that students experience the failure, not just hear about it.

---

### Unit 4: Quick Images Flash (Optional — Research-Supported Enhancement)

- UX to provide visual/video

**Description:** Array is displayed briefly (2-3 seconds), then hidden. Student identifies dimensions or total from memory.

**Interaction:**

1. Array flashes on screen for 2-3 seconds
2. Array disappears (or is covered)
3. Student answers: "How many rows?" / "How many columns?" / "How many total?"
4. Array reappears for verification

**Research basis:** Kosko (2020) found that when all units are visible, students can bypass multiplicative reasoning by counting. Quick Images force students to attend to row-by-column structure rather than individual dots. This pushes beyond additive counting toward genuine multiplicative reasoning.

**Purpose:** Push students from "I can count all the dots" (additive) to "I saw 3 rows of 5" (multiplicative). Assessment of whether students truly perceive array structure.

**When used:** M3 Warm-Up or M5 Warm-Up — brief engagement activity, not a core instructional tool.

**Scaffolding:**

- **Longer display (3-4 sec):** Early use, smaller arrays (2×3, 2×5)
- **Shorter display (1-2 sec):** Later use, requires genuine structural perception
- **Partial reveal:** Show array briefly, then reveal only rows OR only columns as a hint

**Note:** This is an OPTIONAL enhancement supported by research. It is not required for core instruction. Include only if development capacity allows.

## Unit 4: Division Properties

The same array that shows multiplication simultaneously encodes division. This is the critical pedagogical insight that makes arrays the primary bridging representation between the two operations.

**How Arrays Show Division:**

A 3×5 array (3 rows of 5 dots = 15 total) simultaneously represents:

- **Multiplication:** 3 × 5 = 15 and 5 × 3 = 15
- **Partitive division:** 15 ÷ 3 = 5 ("15 items arranged in 3 rows → 5 in each row")
- **Quotitive division:** 15 ÷ 5 = 3 ("15 items arranged in columns of 5 → 3 columns")

**This means one array image encodes all four fact family equations.** Students do not need separate "multiplication arrays" and "division arrays" — the representation is identical; only the question changes.

📷 *Placeholder for annotated array showing all four equations derived from one arrangement*

**Division Reading Modes:**

| Mode | Question Frame | Visual Emphasis | Equation Generated |
| --- | --- | --- | --- |
| **Partitive (row reading)** | "15 in 3 equal rows. How many in each row?" | Rows emphasized; row count given, items-per-row is the unknown | 15 ÷ 3 = ? |
| **Quotitive (column reading)** | "15 with 5 in each column. How many columns?" | Columns emphasized; column size given, column count is the unknown | 15 ÷ 5 = ? |

**Unknown Dimension Display:**

- **Known dimension:** Labeled with numeral (e.g., "3 rows" or "5 per column")
- **Unknown dimension:** Displayed as `?` (M3), `□` (M4), or letter (M10+) per the unknown scaffold progression (Decision D7)
- The array itself is fully visible — the unknown applies to the *label/equation*, not the visual. Students can count to verify.

📷 *Placeholder for array with one dimension labeled "3 rows" and the other showing "?" with equation 15 ÷ 3 = ?*

**Relationship to Existing Emphasis Modes:**

The Unit 1 Row Emphasis and Column Emphasis modes serve double duty in Unit 4:

- **Row Emphasis + multiplication frame** → "3 rows of 5 → 3 × 5 = 15"
- **Row Emphasis + division frame** → "15 in 3 rows → 15 ÷ 3 = 5"
- **Column Emphasis + multiplication frame** → "5 columns of 3 → 5 × 3 = 15"
- **Column Emphasis + division frame** → "15 in columns of 5 → 15 ÷ 5 = 3"

The visual treatment is the same; what changes is the **question frame** and **equation format** displayed alongside. This is the key architectural insight: no new visual rendering is needed for division reading — only new equation/label overlays.

## Constraints

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| Arrays always rectangular | All rows same length; all columns same height; every grid position filled |
| Both interpretations valid | ALWAYS teach both row AND column interpretations; never default to rows only |
| Abstraction progression sequential | Concrete → Mixed → Dots (in that order) |
| Row/column emphasis mutually exclusive | Can show rows OR columns emphasized, not both simultaneously |

### Unit 4: Behavior Constraints

| Constraint | Description |
| --- | --- |
| Division and multiplication use identical arrays | The same array visual represents both operations. Division is a different QUESTION about the same PICTURE — never render a separate "division array." |
| Fact family equations must be grounded in visible array | When displaying fact families, the array should remain visible so students can verify each equation against the visual structure. |
| Unknown dimension labels match scaffold stage | M3: ? (question mark), M4: □ (box), M10+: letter (per Decision D7 unknown scaffold) |

### Interaction Constraints (What Students CAN Do)

| Action | Constraint | Notes |
| --- | --- | --- |
| Observe arrays | All modules (M11-M12) | Basic viewing capability |
| Specify dimensions | Must identify both rows AND columns | Can't answer just one |
| Match to equations | Must recognize both row and column equations as valid | Commutative property foundation |
| See emphasis demonstrations | System must support showing row vs column emphasis | Implementation method flexible |

**Note:** Whether emphasis switching is student-controlled or guide-controlled is an implementation decision. Requirements focus on **what must be shown**, not **who controls it**.

### Question Constraints (What We ASK Students to Do)

**By Module & Abstraction Level:**

| Module | Abstraction Level | Primary Visual | Questions Asked | System Capabilities Needed |
| --- | --- | --- | --- | --- |
| **M11 Early** | Concrete objects | Egg cartons, muffin tins | "How many rows?" "How many columns?" | Basic display, dimension questions |
| **M11 Mid** | Mixed (concrete + dots) | Side-by-side comparison | Same + "Do these show the same array?" | Comparison display |
| **M11 Late** | Dot arrays | Dot grids | Fluent dimension identification; both equations | Emphasis demonstrations, equation display |
| **M12** | Dot arrays (primary) | Dot grids | Property discovery; both interpretations | Emphasis switching, rotation animation, equation updates |

**Never Ask:**

- Identify non-rectangular arrays (all arrays are rectangular by design)
- Build arrays in Unit 1 (observation and interpretation only; construction may come in later units)
- Work with arrays larger than 10×10 (exceeds reasonable screen visibility)
- Work with arrays where product exceeds 100 (per standard 3.OA.A.3)

**By Module & Abstraction Level (Unit 4 Addition):**

| Module | Context | Primary Visual | Questions Asked | System Capabilities Needed |
| --- | --- | --- | --- | --- |
| **M3** | Inverse relationship discovery | Dot arrays (students already fluent from M11-M12) | "What multiplication AND division equations match this array?" "Find ? × 4 = 20 using the array." | Division reading demonstration, unknown dimension display, equation display for both operations |
| **M4 Early** | Fact families with visual support | Dot arrays + fact family view | "Write all four facts for this array." Given 1 fact, generate remaining 3. | Fact family view (full and partial display), sequential equation generation |
| **M4 Mid-Late** | Fact families transitioning to abstract | Dot arrays available but optional | Given one equation, generate remaining 3 (array available as scaffold if needed). | Fact family view, array-on-demand toggle |
| **M5** | Commutativity + non-commutativity discovery | Dot arrays + rotation animation | "Does 3 × 5 = 5 × 3? Does 12 ÷ 4 = 4 ÷ 12? How do you know?" | Rotation animation (existing), non-commutativity demonstration |

**Never Ask (Unit 4 additions):**

- Write a division equation without first establishing the division reading of an array (in M3)
- Generate a complete fact family before understanding the inverse relationship (fact families come AFTER inverse relationship, not before)
- Claim that division is commutative or leave the question unaddressed after teaching commutativity

### Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Row/column highlighting | One mode at a time | Cannot show both simultaneously |
| Sequential highlighting | One row/column at a time | For counting demonstrations |
| Side-by-side comparison | Two arrays maximum | More than two becomes overwhelming |
| Rotation animation | Demonstration/teaching only | Not student-controlled |
| Grid overlay | Can be on or off | Scaffolding tool |

## Layout Constraints

- UX to determine positioning

| Constraint | Value | Notes |
| --- | --- | --- |
| Minimum array size | 2×2 | Smaller doesn't demonstrate structure well |
| Maximum array size typical | 6×6 | Larger exceeds screen space and Grade 3 factor range |
| Common array sizes | 2×3, 3×4, 2×5, 4×5, 3×6 | Based on Grade 3 multiplication focus |
| Can appear with | Equation Builder, word problems, side-by-side comparisons | Common pairings |
| Cannot appear with | Equal groups visuals (different model) | Separate representations |
| Toggle buttons position | Below or beside array | Accessible but not obtrusive |

**Common Layout Patterns:**

- **M11 Early:** Concrete array (center) + Questions (below)
- **M11 Mid:** Concrete array (left) + Dot array (right) for comparison
- **M11 Late:** Dot array (center) + Equation Builder (below) + Row/Column toggle (bottom)
- **M12:** Dot array (center) + Row emphasis view (left) + Column emphasis view (right) + Rotation animation (center) for property discovery

## Unit 4 Additions

- **M3:** Dot array (center) + Equation Builder showing BOTH multiplication and division equations (below/beside) — the visual emphasis toggles between row and column reading as equations are discussed
- **M4 Early:** Dot array (center) + Fact Family equation display (all 4 equations arranged around or below array)
- **M4 Late:** Fact Family equation display (primary) + Array available as optional scaffold (toggleable)
- **M5:** Side-by-side arrays for commutativity comparison (existing capability) + Rotation animation + Equation comparisons for non-commutativity discovery

## Tool to Schema Vocab Translation

- Engineering to complete

## Curriculum Animators Techs

- Waiting on engineering implementation

*CAT team will document workflow once array visual implementation is complete.*

## Open Questions

- [ ]  **Equation display method:** Integrated in array toy, Equation Builder toy alongside, or other?
- [ ]  **Grid overlay control:** Guide-controlled, student-controlled, or both?
- [ ]  **Grid overlay default:** ON by default in M11 Early then fade, or OFF with option to enable?
- [ ]  **Row/column visual treatment:** Color-coding, highlighting, outlines? Colorblind-accessible options?
- [ ]  **Rotation animation trigger:** Guide-controlled demonstration only, or student-triggerable?
- [ ]  **Side-by-side comparison alignment:** Vertical alignment (top edges) or center-align?
- [ ]  **Dot size and spacing:** Optimal dimensions? (8-12px diameter, 15-20px spacing?)
- [ ]  **Grid line visual style:** Faint gray, dashed, dotted? How faint?
- [ ]  **Concrete object variety:** How many types (eggs, muffins, ice, chocolates)? Standardize on 2-3?
- [ ]  **Emphasis persistence:** If emphasis switches to columns, stay there or auto-reset?

### Unit 4 Open Questions:

- [ ]  **Fact family equation arrangement:** Positioned around the array (spatially mapped to row/column readings) or grouped below (simpler layout)? Spatial mapping is pedagogically stronger but potentially cluttered.
- [ ]  **Division reading transition:** When guide demonstrates reading an array as division (M3), should the equation update live as emphasis changes, or appear after the verbal explanation?
- [ ]  **Quick Images implementation:** If included, what is the minimum reliable display time for this age group on screen? (Physical Quick Images use ~3 seconds; digital may need adjustment.)
- [ ]  **Non-commutativity demonstration:** How do we visually show that "4 ÷ 12" doesn't produce a whole number? Options: attempted dealing animation that "fails," a visual comparison of array sizes, or a text/discussion-based approach.
- [ ]  **Array availability in M4 Late/Practice:** Should arrays be always visible, available on request (tap to show), or hidden? Research says abstract symbols should work alongside visuals, not replace them — but M4 Late is deliberately pushing toward abstraction.

## JSON Schema Formatting

### Fact Family View (Unit 4: M3–M5)

An integrated display mode showing one array with all four related equations visible simultaneously.

📷 *Placeholder for array with fact family equations arranged around it*

| Component | Description |
| --- | --- |
| **Array** | Standard dot array (M3–M5 use dot arrays, not concrete objects) |
| **Equation set** | All four equations displayed: 2 multiplication + 2 division |
| **Visual connection** | Each equation is visually linked to the array (e.g., positioned near the corresponding reading — row equations near rows, column equations near columns) |
| **Highlight sync** | When an equation is in focus, the corresponding array emphasis activates (e.g., focusing on "3 × 5 = 15" triggers row emphasis) |

**Equation Arrangement Options (UX to decide):**

- **Around the array:** Row equations left/right, column equations above/below
- **Below the array:** All four in a grid, with active equation highlighted
- **Sequential reveal:** Show one equation at a time, building to all four

**Scaffolding States:**

| State | What's Shown | When Used |
| --- | --- | --- |
| **Full display** | Array + all 4 equations | M4 Late — confirm understanding |
| **Partial display** | Array + 1-2 given equations; student generates the rest | M4 Mid — practice generating related facts |
| **Array only** | Array shown; student generates all 4 equations independently | M4 Exit Check / Practice |
| **Equation only** | One equation given; student identifies or builds the array | M3-M4 — reverse direction (equation → visual) |

**Implementation Note:** Fact family equations may be rendered by the Equation Builder toy displayed alongside the array, by integrated text labels, or by another method. The requirement is that all four equations are **simultaneously visible** and **visually connected to the array** in the full display state.
---

