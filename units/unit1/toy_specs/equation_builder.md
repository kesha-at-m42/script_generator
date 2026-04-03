# Equation Builder

Category: Unit 1
Created: February 3, 2026 5:13 PM
Target Audience: Grade 3 Unit 1, Grade 3 Unit 2, Grade 3 Unit 4

---

> **WHAT:** A multi-method system for assembling multiplication expressions and equations using different input interfaces—multiple choice selection, dropdown menus, draggable tiles, or click-to-place tiles—to accommodate diverse learning styles and device capabilities.

**WHY:** Equation Builder serves as the critical bridge between visual multiplication representations (equal groups, arrays) and symbolic mathematical notation. Providing multiple input methods addresses two essential needs: (1) **Pedagogical differentiation** - some students learn best by selecting complete equations (recognition), while others benefit from constructing expressions piece-by-piece (assembly), and (2) **Technical accessibility** - touch devices, trackpads, and mice each have different interaction strengths, so offering multiple methods ensures all students can effectively demonstrate understanding regardless of device. The progressive unlocking strategy (Method A only → Methods A+C/D → All methods) provides scaffolding as students transition from recognition to construction. By M10, when unknowns and equation flexibility (20 = 4 × 5) are introduced, students have fluency with the interface and can focus cognitive energy on mathematical concepts rather than interface mechanics. Supporting both numeric notation (3 × 4 = 12) and word-based expressions ("3 groups of 4 = 12") helps students maintain the conceptual connection between symbolic and verbal mathematical language.
>

**Scope:** Equation Builder is used across multiple units. This spec is organized as:

- **Core** — Universal capabilities shared by all units
- **Unit 1: Data & Scaled Graphs** — Capabilities specific to Unit 1's multiplication contexts (equal groups, arrays)
- **Unit 2: Area & Multiplication** — Additional capabilities needed for area expressions, composite figures, and reverse reasoning
- Unit 4:  Division operator tile, division content types, fact family display mode, letter unknown tiles, place value decomposition display, two-step equation template, division word expressions, expanded factor range

Each unit's UX team should read Core + their unit section. Later unit sections build on earlier ones.

## Shape:

### Equation/Expression Structure

The assembled mathematical statement showing multiplication relationships.

📷 *UX: Add equation structure examples*

**Expression:**

- Structure: `[factor] × [factor]`
- Example: `3 × 4`
- No equals sign; shows multiplication relationship only

**Equation:**

- Structure: `[factor] × [factor] = [product]` OR `[product] = [factor] × [factor]`
- Example: `3 × 4 = 12` OR `12 = 3 × 4`
- Complete mathematical sentence with equals sign

**With Unknowns:**

- Unknown factor: `___ × 5 = 20` OR `4 × ___ = 20`
- Unknown product: `4 × 5 = ___`
- Unknowns represented by boxes (☐), question marks (?), or blank spaces (___)

### Tile Types (Methods C & D)

Individual draggable or clickable components for building equations.

📷 *UX: Add tile types visual*

**Number Tiles:** Range 0-12+ (contextual based on activity). Large, clear numerals. Minimum 44×44px (touch-friendly).

**Operation Tiles:** Multiplication symbol (×), equals sign (=). Clear symbol, same size as number tiles.

**Unknown Tiles:** Representations: ☐ (box), ? (question mark), ___ (blank). Distinct from number tiles.

**Addition Tiles (Occasional):** Plus sign (+). For repeated addition connection (3 + 3 + 3 + 3 = 12).

### Slots/Assembly Area (Methods C & D)

Designated spaces where tiles are placed to form equations.

📷 *UX: Add assembly area visual*

**Visual Design:** Outlined boxes or underscores. May show structure hints ("groups × items per group = total"). Highlights when tile hovers over or is placed.

**Structure Templates:**

- Expression: `[___] × [___]`
- Equation: `[___] × [___] = [___]`
- Equation (reversed): `[___] = [___] × [___]`
- With unknown: `[___] × [5] = [20]` (student fills one blank)

## Properties

### Core: Input Methods

📷 *UX: Add visuals for each method*

| Method | Description | Interaction Type | Cognitive Demand | Device Optimization | When Introduced |
| --- | --- | --- | --- | --- | --- |
| **A: Multiple Choice** | Complete equations shown as options; student selects correct one | Click to select | Lowest (recognition) | All devices | M8 Early |
| **C: Drag-Drop Tiles** | Draggable number/operation tiles; student drags into assembly slots | Click-drag-release | Medium-High (spatial + construction) | Best for mouse/touch | M8 Mid |
| **D: Click-Pickup-Place** | Same tiles as Method C; click tile to lift, click slot to place | Click-click (no drag) | Medium-High (construction) | Best for trackpad | M8 Mid |

**Note:** Method B (Dropdown Selectors) was considered but deprecated. If needed in future, it can be re-added.

**Progressive Unlocking:**

**Requirement:** Methods unlock in order: Method A (recognition) first, then Methods C/D (construction) added later. Students must demonstrate recognition before being asked to construct. The specific unlock timing per module is defined in each unit's Tool Flow.

**Reference Design:** Method A alone initially → Methods A + C/D together → all methods available. UX determines how method selection is presented to students (e.g., tabs, toggle, automatic based on device).

### Core: Content Types

These content types are available across units. Each unit uses a subset.

| Type | Description | Structure | Example |
| --- | --- | --- | --- |
| **Numeric Expression** | Numbers only, no equals | `3 × 4` | `5 × 2` |
| **Numeric Equation** | Numbers with equals | `3 × 4 = 12` | `5 × 2 = 10` |

### Equation Orientation

| Orientation | Structure | Example | Purpose |
| --- | --- | --- | --- |
| **Standard** | `factor × factor = product` | `4 × 5 = 20` | Traditional format |
| **Reversed** | `product = factor × factor` | `20 = 4 × 5` | Emphasizes equality flexibility |

**Important:** M10 introduces both orientations from the start to prevent rigid thinking about equals sign placement.

### Unit 1: Additional Content Types

| Type | Description | Structure | Example |
| --- | --- | --- | --- |
| **Word Expression** | Descriptive language | "3 groups of 4" | "5 groups of 2" |
| **Word Equation** | Descriptive with equals | "3 groups of 4 = 12" | "5 groups of 2 = 10" |
| **Repeated Addition** | Additive form | `3 + 3 + 3 + 3` | `2 + 2 + 2 + 2 + 2` |

### Unit 2: Additional Content Types

| Type | Description | Structure | Example |
| --- | --- | --- | --- |
| **Parenthesized Addition (2-term)** | Two multiplication terms added | `(a × b) + (c × d) = total` | `(4 × 3) + (5 × 2) = 22` |
| **Parenthesized Addition (3-term)** | Three multiplication terms | `(a × b) + (c × d) + (e × f) = total` | `(2 × 7) + (3 × 4) + (2 × 3) = 32` |

**Note:** Unit 2 does NOT use Word Expressions, Word Equations, or Repeated Addition content types. Unit 2 uses Numeric Expressions and Numeric Equations (from Core) plus the Parenthesized types above.

## Unit 4: Additional Content Types

| Type | Description | Structure | Example |
| --- | --- | --- | --- |
| **Division Expression** | Numbers only, no equals, division | `a ÷ b` | `12 ÷ 3` |
| **Division Equation** | Numbers with equals, division | `a ÷ b = c` | `12 ÷ 3 = 4` |
| **Division Word Expression (Partitive)** | Sharing language | "a shared among b" | "12 shared among 3" |
| **Division Word Expression (Quotitive)** | Grouping/measurement language | "How many groups of b in a?" | "How many groups of 3 in 12?" |
| **Fact Family Set** | All 4 related equations displayed together | See Fact Family mode below | `3 × 4 = 12`, `4 × 3 = 12`, `12 ÷ 3 = 4`, `12 ÷ 4 = 3` |
| **Place Value Decomposition** | Multi-step equation chain showing associative property | `a × (b × 10) = (a × b) × 10 = product` | `4 × 30 = 4 × (3 × 10) = 12 × 10 = 120` |
| **Two-Step Equation Pair** | Two linked equations solving a multi-step problem | `equation 1` → `equation 2` | `6 × 4 = 24` → `24 + 3 = 27` |

**Note:** Unit 4 uses Word Expressions for division only (partitive and quotitive phrasing). Multiplication word expressions ("groups of") from Unit 1 may appear in mixed contexts but are not new to Unit 4.

### Core: Modes

| Mode | Description | Student Interaction |
| --- | --- | --- |
| **Observation** | Guide displays equations; students observe notation | None — display only |
| **Construction** | Students build equations using available input methods | Methods A, C, D (progressive unlock) |

### Unit 2: Additional Modes

| Mode | Description | Student Interaction |
| --- | --- | --- |
| **Blank-Slot** | Template with area (product) given, factor(s) missing. Student selects missing value(s) from MC options. | MC selection to fill blanks |
| **Parenthesized Addition** | Multi-term addition of area calculations, color-coded to match decomposed rectangles | MC selection per term; system auto-populates structure |

### Unit 2: Blank-Slot Mode

A reverse-reasoning mode where the area (product) is given and one factor is missing.

**Structure:** `___ × 5 = 30` (one blank slot, one factor given, product given)

**Behavior:**

- Template displayed with area value and one factor pre-filled
- Student selects missing factor from MC options (not from tile palette)
- On correct selection: system fills the blank, expression completes
- For open-ended reverse problems: `___ × ___ = [area]` with both factors blank. Student selects a factor pair from MC options showing unique pairs only.

**Unit labels:** When used for area problems (M4-M9), the product should include the unit label: "= 28 sq ft" not just "= 28". Available units: sq units (generic), sq cm, sq in, sq ft, sq m. Unit label appears after the product, not as a separate tile.

### Unit 2: Design Exploration Mode (Blank-Slot + Number Palette)

**Description:** Both factor slots are blank with the target area (product) given. Student selects factors freely from a number palette (0–12), not from curated MC options. The system validates whether the product matches the target.

**Structure:** `___ × ___ = [target area]`

**Behavior:**

- Number palette displays digits 0–12 (or contextually scoped subset)
- Student selects first factor, then second factor from palette
- System computes product in real time
- If product ≠ target: neutral feedback — "That gives an area of [product], not [target]. Try different numbers!" No penalty. Exploration IS the learning.
- If product = target: confirmation — Grid Rectangles displays the resulting rectangle to scale
- System prompts: "Can you find a DIFFERENT rectangle with the same area?" (encourages multiple solutions)
- After 2–3 failed attempts: guide may hint — "Try starting with a number that goes into [target]."

**When used:** M9 Mid/Late design problems. Follows MC-scaffolded design problems (which use standard Blank-Slot with factor-pair MC) to ensure students can identify valid pairs before producing them independently.

### Unit 2: Unknown Position

| Position | Structure | Example | Problem Type |
| --- | --- | --- | --- |
| **Unknown Product** | `factor × factor = ___` | `4 × 5 = ___` | Find the total |
| **Unknown Factor (1st)** | `___ × factor = product` | `___ × 5 = 20` | "How many groups?" |
| **Unknown Factor (2nd)** | `factor × ___ = product` | `4 × ___ = 20` | "How many in each group?" |

**Pedagogical Note:** All three unknown positions introduced in M10; prepares for division in later units.

### Unit 2: Semantic Slot Labels

Slots can display semantic labels that scaffold the visual-to-symbolic connection:

| Scaffolding Level | Slot Display | Example | When Used |
| --- | --- | --- | --- |
| **Labeled** | Slots show role labels | `[Rows] × [In each row] = [Area]` | M4 Early: first exposure to multiplication notation for area |
| **Unlabeled** | Empty slots, no labels | `[___] × [___] = [___]` | M4 Mid: labels removed, structure maintained |
| **Independent** | No slots at all | Free-form tile placement | M4 Late: full construction independence |

**Requirement:** Slot labels must fade over time — students should transition from labeled slots to unlabeled slots within a single concept introduction. Labels are a temporary scaffold, not a permanent feature.

**Reference Design:** The three scaffolding levels above (Labeled → Unlabeled → Independent) represent one approach. UX may find a different fading pattern that achieves the same goal.

**Label placement — UX decision, two options:**

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| **In-slot** | Label text inside the slot; student's tile replaces it | Clean — one element per slot | Label disappears once filled |
| **Above-slot** | Label as caption above; slot itself is empty | Label persists after placement — student can check | More visual clutter |

### Unit 2: Color-Coded Rectangle Integration

When Equation Builder is used alongside Composite Figures, each parenthesized term must visually match the color of its corresponding decomposed rectangle.

**Requirement:** When Equation Builder displays a parenthesized addition expression alongside a decomposed composite figure, each term in the expression must be visually linked to its corresponding rectangle. This color correspondence is what makes the connection between visual decomposition and arithmetic expression concrete — without it, students cannot track which sub-calculation maps to which region.

**Behavior:**

- Blue rectangle → blue-highlighted term `(4 × 3)` in the expression
- Orange rectangle → orange-highlighted term `(5 × 2)` in the expression
- Color correspondence is automatic after decomposition
- If a rectangle is selected/active in the figure, its corresponding term highlights in the expression (and vice versa)

**Why this matters:** Without grids (M12+), the color link is the primary visual connection between the abstract expression and the ungridded figure.

**Display format:** The full expression shows the intermediate step:
`(4 × 3) + (5 × 2) = 12 + 10 = 22`
The intermediate products (12, 10) help students track the calculation. The final sum (22) is the total area.

**Interaction:** The Equation Builder auto-populates as students calculate each rectangle's area via MC. Student calculates blue rectangle area → system fills `(4 × 3) = 12` in blue → student calculates orange rectangle area → system fills `(5 × 2) = 10` in orange → student adds → system shows `= 22`.

### Unit 4: Additional Tile Types

| Tile | Display | Notes |
| --- | --- | --- |
| **Division Tile** | ÷ | Same size as × tile. Added to operation tile set. |
| **Letter Unknown Tiles** | `n`, `a`, `b` (lowercase) | Distinct styling from number tiles — e.g., italic or different background color. Represent the same concept as ☐ and ? but at a higher abstraction level. |

**Unknown representation progression (cumulative across units):**

| Stage | Representation | When Introduced | Example |
| --- | --- | --- | --- |
| 1 | Question mark (?) | Unit 1 (M10) | `? × 5 = 20` |
| 2 | Box (☐) | Unit 2 (M8) | `☐ × 5 = 20` |
| 3 | Letter (n, a) | Unit 4 (Section C–D) | `n × 5 = 20` |

**Requirement:** All three representations should be recognized by the system as equivalent unknowns. Once letters are introduced, all three may appear across activities — the specific representation is configured per problem. Letters are NOT introduced abruptly; the transition is scaffolded through Observation mode first (guide shows `n × 5 = 20` alongside `☐ × 5 = 20` and explains they mean the same thing).

**Cumulative flexibility model (D7 revised per SME):** These stages represent when each representation is INTRODUCED, not when prior representations are retired. From the point each new representation appears, all previously introduced representations continue to appear in practice problems interchangeably. By Unit 4 M10, students should be comfortable seeing ?, □, and letters in any activity. This prepares students for state assessments that use varied unknown formats without warning.

## Allowed Student Actions

**NOT allowed: Edit products / Change table size / Free-form typing.** All student interaction goes through the defined methods (MC, drag-drop, click-place) or MC selection within templates.

## Core Actions (All Units)

### Mode 1: Observation

**Description:** Guide displays multiplication notation for observation only. Students do not interact with the tool.

**Behavior:** Display only — guide shows and explains equations.

**Purpose:** Build conceptual understanding of notation before any student interaction.

---

### Method A: Select from Multiple Choice

**Description:** Student sees 3-4 complete equations/expressions as options and clicks the correct one.

**Behavior:** View options → click correct match → submit/confirm selection. Correct: checkmark or confirmation message. Incorrect: "Try again" with option to re-attempt or see correct answer.

**Purpose:** Build recognition skills; lowest cognitive demand; ideal for introduction.

📷 *UX: Add MC interaction visual*

---

### Method C: Drag-Drop Tiles

**Description:** Student drags number/operation tiles from palette into assembly slots.

**Behavior:**

1. View tile palette (available numbers and operations)
2. Click-hold on tile (tile lifts/highlights)
3. Drag toward slot (ghost preview shows position)
4. Hover over slot (slot highlights to indicate valid drop zone)
5. Release (tile snaps into slot)
6. Repeat for remaining slots
7. Submit when equation complete

**Tile Behavior:** Snap-to-slot alignment. Placing new tile in occupied slot replaces previous. Tile returns to palette if dropped outside valid slot.

**Purpose:** Most tactile/spatial method; works best with mouse or touch screens.

📷 *UX: Add drag-drop interaction visual*

---

### Method D: Click-Pickup-Place

**Description:** Same tiles as Method C, but uses click-click interaction instead of drag.

**Behavior:**

1. View tile palette
2. Click tile (tile lifts and highlights; cursor changes or tile "sticks" to cursor)
3. Click destination slot (tile places in slot)
4. Repeat for remaining slots
5. Submit when equation complete

**Purpose:** Alternative to drag-drop for trackpads; eliminates hold-and-drag challenge.

📷 *UX: Add click-place interaction visual*

---

### Rearrange/Modify Placed Tiles (Methods C & D)

**Description:** Students pick up already-placed tiles and reposition them.

**Behavior:** Method C: Click-drag placed tile to new slot. Method D: Click placed tile (lifts), click new destination slot.

**Purpose:** Correct mistakes without full reset; explore turn-around facts (swap 3 × 4 to 4 × 3) in M9+.

**Note:** Not a separate feature — inherent to tile-based methods C & D.

---

### Reset/Clear

**Description:** Remove all placed tiles and start over.

**Behavior:** Click "Clear" or "Reset" button. All slots empty. Tiles return to palette.

**Purpose:** Allow fresh start without penalty; support iterative thinking.

---

### Unit 2 Additional Mode E: Parenthesized Addition

**Description:** System displays the parenthesized expression template. Student fills in each term's result via MC, then the sum via MC. System auto-populates the structure.

**Why NOT tile-based:** The expression `(4 × 3) + (5 × 2) = 12 + 10 = 22` has too many components for tile assembly at Grade 3. System provides the structure; students provide the calculations.

**Behavior (interaction sequence):**

1. Student decomposes composite figure → rectangles color-coded
2. System generates expression template: `(__ × __) + (__ × __) = ___`
3. System highlights blue rectangle → student sees "The blue rectangle is 4 by 3. What's its area?" → MC: 12 / 15 / 7 / 10
4. Student selects 12 → system fills: `(4 × 3) + (__ × __) = 12 + ___ = ___`
5. System highlights orange rectangle → same process → student selects 10
6. System fills: `(4 × 3) + (5 × 2) = 12 + 10 = ___`
7. Student adds: "What's 12 + 10?" → MC: 22 / 20 / 32 / 14
8. System fills: `(4 × 3) + (5 × 2) = 12 + 10 = 22`

**For 3-component figures:** Same sequence with a third term.

**Scaffolding levels:**

- M11 Early: System pre-fills dimensions in the expression (student only calculates products and sum)
- M11 Mid-Late: Student calculates via MC; expression builds incrementally
- M12+: Same as M11 Mid-Late (no additional scaffolding change)

**Display requirements:**

- Each parenthesized term matches rectangle color
- Intermediate products shown (12 + 10, not just 22)
- Expression updates in real time as student provides each answer
- If student gets a component area wrong, the expression shows the wrong value — the error propagates. Guide catches the downstream error and traces it back to the source.

**Purpose:** Make explicit connection between visual decomposition and arithmetic expression for composite area.

**⚠️ Engineering requirement — reactive term generation:** The Equation Builder must dynamically generate the parenthesized expression based on the number of component rectangles the student's decomposition produces — NOT from a pre-configured 2-term or 3-term template. If the student draws one decomposition line (2 rectangles), the expression has 2 terms. If the student draws two lines (3 rectangles), the expression has 3 terms. The Equation Builder is reactive to the Composite Figures decomposition output, not prescriptive.

**Interaction flow:** Student places decomposition line(s) → Composite Figures identifies resulting rectangles and color-codes them → Equation Builder populates with the matching number of color-coded parenthesized terms → student fills in values via MC per term → system completes the expression.

## Unit 4: Additional Modes

### Fact Family Mode

**Description:** Displays all four related equations for a given set of three numbers (two factors + product). Used alongside an Array visual to show WHY four facts exist from one arrangement.

**Display structure:**

`3 × 4 = 12
4 × 3 = 12
12 ÷ 3 = 4
12 ÷ 4 = 3`

**Behavior options (scaffolding levels):**

| Level | Student Action | Display |
| --- | --- | --- |
| **Observation** | None — all 4 equations displayed by guide | System shows all 4 facts; guide explains relationships |
| **Guided Construction** | Student builds one equation at a time via MC or tiles; system reveals each as completed | Equations appear one at a time as student provides them |
| **Prompted Construction** | System shows first fact (e.g., `3 × 4 = 12`); student provides remaining 3 via MC | "What other equations can you write with 3, 4, and 12?" |
| **Independent Construction** | System provides the three numbers; student builds all 4 equations | Numbers shown in a fact family triangle or simply listed |

**Visual pairing:** Fact Family Mode should appear alongside an Array showing the same arrangement. The array visual reinforces WHY these four facts are related — same objects, different questions.

**Key interaction:** When a multiplication equation is highlighted, the corresponding array reading is shown (e.g., highlight `3 × 4 = 12` → array shows "3 rows of 4"). When a division equation is highlighted, the corresponding division interpretation is shown (e.g., highlight `12 ÷ 3 = 4` → "12 arranged in 3 rows → 4 in each row").

**Pedagogical note:** Research on fact families is practitioner-consensus based (MEDIUM confidence — see Research Summary). The critical design requirement is that fact families always connect to a visual referent (array), not appear as abstract symbol shuffling. If a student can produce all 4 equations but cannot explain why they're related using an array, the teaching has failed.

---

### Unit 4:  Place Value Decomposition Display Mode

**Description:** Shows a multi-step equation chain that breaks down multiplication by multiples of 10 using the associative property and unit language.

**Display structure (example for 4 × 30):**

`4 × 30 = 4 × (3 × 10) = (4 × 3) × 10 = 12 × 10 = 120`

**This is an Observation/Teaching mode** — students do NOT assemble this chain via tiles. The cognitive demand of the full chain is too high for Grade 3 tile assembly. Instead:

**Behavior:**

1. Guide shows `4 × 30` and asks "What's 4 groups of 30?" — students may attempt via MC
2. Guide reveals decomposition step by step, with each segment highlighting as it appears:
    - `4 × 30` (original)
    - `= 4 × (3 × 10)` (decompose 30 into 3 × 10)
    - `= (4 × 3) × 10` (regroup — "multiply the 3 first")
    - `= 12 × 10` (compute 4 × 3)
    - `= 120` (compute 12 × 10)
3. Student then solves similar problems via MC or Blank-Slot mode with simpler scaffolding:
    - `6 × 40 = 6 × ___ tens = ___ tens = ___`

**Visual pairing:** Should appear alongside Base 10 Blocks showing the same calculation concretely — 4 groups of 3 ten-rods = 12 ten-rods = 120 unit cubes.

**Unit language requirement:** The display should support a "tens language" annotation layer where applicable:

- `4 × 3 tens = 12 tens = 120`
- This is separate from the full associative chain — a simpler intermediate representation

**Pedagogical note:** The full associative property chain (`4 × (3 × 10) = (4 × 3) × 10`) is for teaching/observation. Student practice uses the simpler unit language frame or Blank-Slot problems. Never teach "add a zero." (Research Summary, Commitment #6; Misconception U4.5)

---

### Unit 4: Two-Step Equation Template Mode

**Description:** Displays two linked equations showing the steps of a multi-step word problem. Students fill in values via MC, one step at a time.

**Display structure (example):**

`Step 1: 6 × 4 = ___
Step 2: ___ + 3 = ___`

**Behavior:**

1. Problem presented alongside a Bar/Tape Diagram (if available) showing the structure
2. System highlights Step 1 → student solves via MC → system fills result (24)
3. System carries Step 1 answer into Step 2 → highlights Step 2 → student solves → system fills
4. Final answer confirmed

**Scaffolding levels:**

| Level | What System Provides | What Student Does |
| --- | --- | --- |
| **High** | Both equations pre-structured with operations shown; one blank per step | Fill in the results via MC |
| **Medium** | Equation structure shown but operations blank | Select the operation AND the result via MC |
| **Low** | Only the word problem shown; student identifies both steps | Select equations from MC options representing each step |

**Unknown representations in two-step problems:**

- At HIGH scaffolding: blanks (___) in result positions
- At MEDIUM: blanks in operation AND result positions
- At LOW: letter unknowns may appear (`n × 4 = 24; 24 + 3 = n`)

**Pedagogical note:** Two-step problems should be presented as two connected single-step problems before requiring students to see them as integrated. (Research Summary, Commitment #11; Powell et al., 2022)

---

## Unit 4: Division Unknown Positions

Extends the Unit 2 unknown position table to include division:

| Position | Structure | Example | Problem Type | Division Interpretation |
| --- | --- | --- | --- | --- |
| **Unknown Quotient** | `a ÷ b = ___` | `12 ÷ 3 = ___` | "What's the result?" | Both partitive and quotitive |
| **Unknown Divisor** | `a ÷ ___ = c` | `12 ÷ ___ = 4` | "How many groups?" or "How many in each group?" | Depends on context |
| **Unknown Dividend** | `___ ÷ b = c` | `___ ÷ 3 = 4` | "What was the total?" | Inverse of both types |

**Critical design requirement — unknown-factor bridge:**
The primary Unit 4 strategy for division is to reframe it as unknown-factor multiplication (3.OA.B.6). The Equation Builder must support showing the equivalence:

`12 ÷ 3 = ?    is the same as    ? × 3 = 12`

**Behavior:** When a division equation with an unknown quotient is displayed, the system can (on guide trigger) show the equivalent multiplication equation alongside or below it. This should be a teaching action, not automatic — students need to see the connection made explicit.

**Teaching Action: Show Division-Multiplication Equivalence**

- Trigger: Guide-directed
- Display: Division equation on left, equivalent unknown-factor multiplication on right, with visual connector (arrow, "same as" label, or animation transitioning between the two)
- Example: `56 ÷ 8 = ?` ↔ `? × 8 = 56`
- Purpose: Operationalizes the inverse relationship (Commitment #4; Misconception U4.3)

---

## Unit 4: Equation Orientation (Division)

| Orientation | Structure | Example | Purpose |
| --- | --- | --- | --- |
| **Standard** | `dividend ÷ divisor = quotient` | `12 ÷ 3 = 4` | Traditional format |
| **Reversed** | `quotient = dividend ÷ divisor` | `4 = 12 ÷ 3` | Equals sign flexibility |

**Requirement:** Both orientations should appear from the start of division instruction (not introduced separately). This continues the equals-sign flexibility practice from Units 1–2 and directly addresses Misconception A2 (equals sign as "do something"). Non-standard equation formats (e.g., `4 = 12 ÷ 3`) should be normalized, not treated as special cases.

**Additional nonstandard formats for Unit 4:**

- `8 = 8` (identity — equality without operations)
- `3 × 4 = 12 = 4 × 3` (chained equality showing commutativity)
- `☐ × 5 = 40 = 8 × 5` (unknown with equivalent expression)

These formats are for Observation mode primarily. Not all need MC/tile construction support.

## Additional Teaching/Remediation Actions

## Core Teaching Actions

### Highlight Equation Component

**Description:** Guide draws attention to specific part of equation (first factor, second factor, product, equals sign). Example: Guide explains "The first number shows HOW MANY groups" → first factor highlights.

**Purpose:** Direct focus during instruction; reinforce positional meaning.

**Triggers:** Guide-directed during instruction.

📷 *UX: Add highlighting visual*

---

### Show Connection to Visual

**Description:** Display equal groups/array/area visual alongside equation with connecting lines. Example: 3 bags with 4 apples → `3 × 4 = 12` → lines connecting 3 to bags count, 4 to apples per bag, 12 to total.

**Purpose:** Maintain visual-symbolic connection; prevent abstract notation from losing meaning.

**Triggers:** Guide-directed; always when visual is also displayed.

📷 *UX: Add connection visual*

---

### Show Repeated Addition Connection

**Description:** Display multiplication expression alongside repeated addition equivalent. Example: `5 × 2` alongside `2 + 2 + 2 + 2 + 2`, both evaluating to `10`.

**Purpose:** Reinforce that multiplication is shorthand for repeated addition.

**Triggers:** Guide-directed; used strategically in M8-M9.

---

### Pre-Fill Slots (Scaffolding)

**Description:** Some slots already filled; student completes remaining slots.

**Purpose:** Graduated difficulty; focus attention on specific concept.

**Triggers:** System-configured per activity.

**Scaffolding Levels:**

- **High:** Only one blank (student fills one value)
- **Medium:** Two blanks (student fills two values)
- **Low:** All blanks (student builds complete equation)

📷 *UX: Add pre-fill visual*

---

### TPP (Teacher's Purple Pen)

**Description:** Guide can circle, underline, or annotate specific parts of equations.

**Purpose:** Direct student attention during instruction.

**Triggers:** Remediation; emphasis during instruction; error correction.

## Constraints

### Core: Behavior Constraints

| Constraint | Description |
| --- | --- |
| Progressive method unlock | Methods unlock in order: A (recognition) before C/D (construction) |
| Contextual tile sets | Only relevant numbers available per problem (not always full 0-12 range) |
| Not draggable as a whole | Individual tiles drag; the Equation Builder itself is a fixed display |

### Unit 1: Behavior Constraints

| Constraint | Description |
| --- | --- |
| Expressions before equations | Expressions (no equals sign) introduced before full equations |
| Unknown introduction timing | Unknowns only after students have equation fluency |
| Equals sign flexibility | Both orientations (standard and reversed) introduced together |

### Unit 2: Behavior Constraints

| Constraint | Description |
| --- | --- |
| Parenthesized expressions are system-structured | Students fill in calculation results via MC; they do NOT assemble the parenthesized structure via tiles |
| Color coding requires Composite Figures | Color-coded equation terms only appear alongside the decomposed composite figure |
| No word notation | Unit 2 does not use word-based expressions or equations |
| No repeated addition | Unit 2 does not use repeated addition notation |
| Guide-activated conditional display  | Equation Builder can be configured as initially hidden, appearing only when guide activates it (e.g., after incorrect first attempt or extended inactivity) |

## Unit 4: Behavior Constraints

| Constraint | Description |
| --- | --- |
| Division tiles available only after division is introduced | ÷ tile not in palette during multiplication-only activities |
| Letter unknowns only after box unknowns are fluent | Letters appear Section C–D, not Section A |
| Fact family mode always paired with Array visual | Never display 4 related equations without a visual referent |
| Place value decomposition is Observation only | Students do NOT tile-assemble the full associative chain |
| Two-step templates scaffold from high to low | Never start with low scaffolding for two-step problems |
| Division word expressions label the type | System (or guide) explicitly identifies partitive vs. quotitive contexts |

### Core: Question Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| Factor range | 0-12 (contextual per problem) | Grade 3 scope |
| MC options | 3-4 maximum | Reduce cognitive load |
| **NOT:** Free-form typing | Never | All interaction through defined methods |

### Unit 1: Question Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| **NOT:** Equations before expressions | Never — expressions first | Recognition before construction |
| **NOT:** Unknowns before equation fluency | Never | Requires comfort with full equations first |
| **NOT:** Methods C/D before Method A | Never | Recognition before construction |

### Unit 2: Question Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| Parenthesized terms | Maximum 3 | Max 3-component composite figures |
| Parenthesized sums | ≤ 100 | Manageable addition for Grade 3 |
| **NOT:** Reversed orientation for composite expressions | Never | `22 = (4 × 3) + (5 × 2)` not introduced |
| **NOT:** Student-constructed parenthesized expressions via tiles | Never | Structure too complex for tile assembly at Grade 3 |
| **NOT:** Color-coded equations without Composite Figures display | Never | Color correspondence requires visual reference |

## Unit 4: Question Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| Division factor range | Dividends 0–100; Divisors 1–10 | 3.OA.C.7: divide within 100 |
| Multiples of 10 range | Factors: single digit × multiple of 10, products to 100 (or slightly beyond for 9 × 20 = 180) | 3.NBT.A.3 |
| Fact family number sets | Products ≤ 100 using factors 1–10 | Aligned with multiplication table scope |
| Two-step problems | Maximum 2 operations | Grade 3 scope per 3.OA.D.8 |
| **NOT:** Division with remainders in Equation Builder | Never | Remainders are contextual, not equation-based in this unit |
| **NOT:** Letter unknowns in Section A–B | Never | Build comfort with ☐/? first |
| **NOT:** Full associative chain as tile construction | Never | Display/observation only — too many components |

### Core: Interaction Constraints

| Action | Constraint | Notes |
| --- | --- | --- |
| Select from multiple choice | 3-4 options maximum | Avoid overwhelming choices |
| Drag tiles (Method C) | One tile at a time | Cannot multi-select |
| Click tiles (Method D) | One tile at a time | Sequential placement |
| Edit products directly | **NOT ALLOWED** | Must use defined input methods |
| Free-form typing | **NOT ALLOWED** | All interaction through methods A/C/D or MC |

### Unit 1: Interaction Constraints

| Action | Constraint | Notes |
| --- | --- | --- |
| Rearrange factors | Only after commutative property is introduced | Explore turn-around facts (3 × 4 ↔ 4 × 3) |
| Use unknowns | Only after equation fluency established | Requires comfort with complete equations first |
| Reverse equation orientation | Only after equals-sign flexibility introduced | Both directions taught together |

### Unit 2: Interaction Constraints

| Action | Constraint | Notes |
| --- | --- | --- |
| Parenthesized addition: fill terms | Via MC only (not tiles) | System provides structure; student provides calculations |
| Blank-slot: fill missing factor | Via MC only (not tiles) | Reverse reasoning with constrained input |

## Unit 4: Interaction Constraints

| Action | Constraint | Notes |
| --- | --- | --- |
| Division-multiplication equivalence display | Guide-triggered only | Not automatic — explicit teaching action |
| Fact family: rearrange equations | Only after all 4 are generated | Student can reorder displayed equations |
| Two-step template: carry answer forward | Automatic after Step 1 correct | System fills Step 1 result into Step 2 |
| Letter unknown entry | Via MC only (select from options) | Students do NOT type letters |

### Visual / Teaching Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| Visual-to-equation connection lines | Only when visual is also displayed | Requires equal groups, array, or area visual |
| Repeated addition display | Only for expressions with reasonable length | Keep additions manageable |
| Pre-filled slots | Minimum 1 blank required | Cannot have all slots pre-filled |
| Highlighting | One component at a time | First factor, second factor, product, or operation |
| Color-coded terms | Must match Composite Figures rectangle colors | M11-M14 only |

## Layout Constraints

| Constraint | Value | Notes |
| --- | --- | --- |
| Tile palette size | 8-15 tiles visible | Avoid scrolling if possible |
| Assembly area position | Center or top-center | Primary focus area |
| Tile size | Minimum 44×44px | Touch-friendly; accessibility standard |
| MC options | 3-4 maximum | Reduce cognitive load |
| Can appear with (Unit 1) | Equal groups visuals, arrays, picture graphs, bar graphs | Unit 1 pairings |
| Can appear with (Unit 2)  | Grid Rectangles, Composite Figures | Composite Figures pairing requires color-coded synchronization. |
| Can appear with (Unit 2) | Word Problem container | M9: contextual area problems with Equation Builder scaffold |
| Cannot appear with | Multiple Equation Builders simultaneously | Focus on one problem at a time |
| Can appear with (Unit 4) | Equal Groups, Arrays, Multiplication Table, Base 10 Blocks, Composite Figures (rectangle mode) | All Unit 4 toys |
|  Cannot appear with | Multiplication Table Grid |  |
| Fact Family display | Vertical stack of 4 equations, alongside Array |  |
| Place Value display | Horizontal chain OR stepped vertical display | UX decision — chain may be too wide for single line |
| Two-Step display | Vertically stacked with Step 1/Step 2 labels | Visual connector between steps |

📷 *UX: Add layout diagram(s)*

## Tool to Schema Vocab Translation

- Engineering to complete

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
| "expression" | `equation_type: "expression"` | No equals sign |
| "equation" | `equation_type: "equation"` | Includes equals sign |
| "unknown" | `has_unknown: true, unknown_position: "factor1" | "factor2" |
| "standard orientation" | `equation_format: "standard"` | factor × factor = product |
| "reversed orientation" | `equation_format: "reversed"` | product = factor × factor |
| "Method A" | `input_method: "multiple_choice"` | Selection interface |
| "Method B" | `input_method: "dropdown"` | Dropdown menus |
| "Method C" | `input_method: "drag_drop"` | Draggable tiles |
| "Method D" | `input_method: "click_place"` | Click-click tiles |
| "numeric notation" | `notation_type: "numeric"` | 3 × 4 = 12 |
| "word notation" | `notation_type: "words"` | "3 groups of 4" |
| "repeated addition" | `notation_type: "addition"` | 4 + 4 + 4 |
| "available tiles" | `tile_palette: [2, 3, 4, 5, "×", "="]` | Contextual set |
| "pre-filled slots" | `pre_filled: {position_0: 3, position_2: 12}` | Scaffolding |

## Curriculum Animators Techs

 - Waiting on engineering implementation

## Open Questions

**Unresolved:**

- [ ]  **[UX]** Tile palette organization: Grouped (numbers | operations | unknowns) or mixed?
- [ ]  **[UX]** Haptic feedback: Vibration on mobile when tile snaps to slot?
- [ ]  **[UX]** Keyboard navigation: Tab order for accessibility — tile palette → slots → submit?
- [ ]  **[UX]** Undo vs Reset: Granular "undo last tile" vs full "clear all"?
- [ ]  **[UX]** Audio feedback: Sound effects for placement, completion, errors?
- [ ]  **[UX]** Pre-fill visual distinction: How do pre-filled slots look different from student-filled slots?
- [ ]  **[UX - Unit 1]** Unknown representation preference: Box (☐), question mark (?), or underscore (___)?
- [ ]  **[UX - Unit 1]** Equals sign teaching: Should = sign be clickable/moveable to practice both orientations?
- [ ]  **[UX - Unit 2]** Semantic slot label placement: In-slot or above-slot? (See Unit 2: Semantic Slot Labels)
- [ ]  **[Engineering]** Unit labels: Display-only suffix after product, or selectable component?

## Unit 4: Open Questions

- [ ]  **[UX]** Fact Family layout: Vertical stack (all 4 equations listed) vs. triangle organizer with equations radiating from vertices? Triangle is visually compact but may be harder to read.
- [ ]  **[UX]** Place value decomposition chain: Single horizontal line (may overflow) vs. stepped/waterfall layout vs. animated sequential reveal?
- [ ]  **[UX]** Letter unknown styling: Italic? Different background color? How to visually distinguish `n` from number tiles while keeping it clear this is "a number we don't know yet"?
- [ ]  **[UX]** Division-multiplication equivalence display: Side-by-side with arrow? Animated morph from one to the other? Stacked with "is the same as" connector?
- [ ]  **[UX]** Two-step template: How to visually show the "carry forward" from Step 1 result to Step 2 input? Animation? Color-matching?
- [ ]  **[Engineering]** ÷ tile: Same tile palette slot as × (toggle?) or separate tile? Impacts palette size.
- [ ]  **[Cross-Unit - Andrea]** Tape Diagram integration: If Tape Diagrams are introduced in Unit 3, two-step template mode should be able to display alongside a Tape Diagram. Layout implications?

**Resolved:**

- [x]  **[Resolved — Tool Flow M4]** Tile palette organization? → Contextual — only relevant numbers available per problem. Grouped or mixed is UX decision.
- [x]  **[Resolved — Tool Flow M8, M11]** MC distractors? → Diagnostically designed per problem type. Forward: near-miss products. Reverse: plausible but wrong factor pairs. Composite: addition errors, partial calculations.
- [x]  **[Resolved — Tool Flow Unit 2]** Word notation frequency? → Unit 2 doesn't use word notation in Equation Builder. Unit 1 decision.
- [x]  **[Resolved — Tool Flow Unit 2]** Repeated addition display? → Unit 2 doesn't use repeated addition. Unit 1 decision.
- [x]  **[Resolved — Tool Flow M4]** Rearrange availability? → Both orientations accepted (4×6 and 6×4 both valid) but no explicit rearrange action in Unit 2. Commutative property shown through guide demonstration.
- [x]  **[Deprecated]** Method B (Dropdown Selectors)? → Removed from spec. Can be re-added from original if needed in future.

## JSON Schema Formatting

