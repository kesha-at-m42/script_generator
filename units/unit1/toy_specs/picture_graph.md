# Picture Graphs

Category: Unit 1
Created: February 3, 2026 4:38 PM
Status: UX in Process
Target Audience: Grade 3 Unit 1

---

> **WHAT:** A visual data display system using symbols or pictures where each symbol represents one or more data points, arranged in rows (horizontal) or columns (vertical) to show categorical data.

**WHY:** Picture Graphs provide concrete visual representation of scaled data, bridging the gap between counting individual items (1:1) and abstract numeric representation. The use of discrete, countable symbols allows students to see the grouping structure explicitly—each symbol represents multiple items—while maintaining visual clarity. This representation is pedagogically essential for introducing the concept of scale (1:2, 1:5, 1:10) because students can physically count symbols and verify by skip-counting. Picture graphs also introduce half-symbols, which provide precise mathematical scaffolding for odd numbers and prepare students for fraction concepts. The discrete nature of symbols makes the "each symbol = X items" relationship visually concrete before transitioning to continuous bar representations. Research shows that visual-to-numeric bridging (moving from picture graphs to bar graphs) has effect sizes of 0.50-0.77 for elementary students' data literacy.
>

## Shape:

- UX to provide visuals

### Full Symbols

Emoji-style pictographic symbols representing complete scale multiples.

📷 *Placeholder for full symbol examples*

**Symbol Library Categories:**

- **Animals:** paw prints, bones, pet icons (dogs, cats, birds, fish)
- **Foods:** plates, utensils, generic food icons (pizza, apples, sandwiches)
- **Objects:** stars, circles, squares, hearts, generic shapes
- **Activities:** sports equipment, instruments, books

**Library Size:** 20-30 distinct symbols across categories

**Critical Design Rule:** ONE symbol per graph (not one per category). For example, if graphing favorite pets, all categories (dogs, cats, birds, fish) use the same paw print symbol, not dog icons for dogs, cat icons for cats, etc.

### Half Symbols

Partial symbols representing values that are not complete scale multiples.

📷 *Placeholder for half symbol examples (horizontal and vertical cuts)*

**Two Cut Types:**

**Horizontal Cut:**

- Symbol divided left-to-right
- Used primarily in horizontal orientation graphs
- Left half filled, right half empty (or vice versa)

**Vertical Cut:**

- Symbol divided top-to-bottom
- Used primarily in vertical orientation graphs
- Top half filled, bottom half empty (or vice versa)

**Half-Symbol Value:**

- M2 (Scale of 2): Half symbol = 1 item
- M3 (Scale of 5): NO HALF-SYMBOLS USED (multiples only)
- M4+ (Scale of 10): Half symbol = 5 items

**Mathematical Precision:**

- Half of 2 = 1 (clean, intuitive for Grade 3)
- Half of 10 = 5 (also clean, builds on familiar benchmark)
- Half of 5 = 2.5 (NOT used—too complex for Grade 3)

## Properties

### Orientation

- UX to provide visuals for each orientation

| Orientation | Description | Visual Layout | When Used |
| --- | --- | --- | --- |
| **Horizontal** | Symbols extend rightward from category labels | Labels on left, symbols arranged in rows moving right | All modules (mixed with vertical) |
| **Vertical** | Symbols stack upward from category labels | Labels on bottom, symbols arranged in columns moving up | All modules (mixed with horizontal) |

**Note:** Both orientations are used throughout Unit 1. Students should already be familiar with both from Grades 1-2, so introducing both simultaneously activates prior knowledge.

### Scale (How Many Items Each Symbol Represents)

- UX to provide scale indicator visuals

| Scale | Description | When Introduced | Half-Symbol Support |
| --- | --- | --- | --- |
| **1:1** | Each symbol = 1 item | M1 (review from Grade 2) | No half-symbols needed |
| **1:2** | Each symbol = 2 items | M2 (critical leap) | Yes (half = 1) |
| **1:5** | Each symbol = 5 items | M3 | No (multiples only in M3) |
| **1:10** | Each symbol = 10 items | M4+ (observation only) | Yes (half = 5, for reading) |

**Scale Indicator:** Text appears above or near graph stating "Each [symbol] = [number]"

- Example: "Each 🐾 = 2"
- Always visible when scale > 1
- Font size: prominent but not dominating

### State (Mode)

- UX to provide visuals for each mode

| Mode | Description | Student Interaction | When Used |
| --- | --- | --- | --- |
| **Mode 1: Reading** | Pre-made graphs displayed for interpretation | Hover, click, compare | All modules |
| **Mode 2: Creating** | Student places symbols to build graph | Click-to-place, preview | M2-M3 |

**Important:** M4+ uses picture graphs for READING only (observation and comparison to bar graphs). Students do NOT create picture graphs with scale of 10.

### Symbol States (Mode 2 Only)

- UX to provide visuals for each state

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Available (in palette)** | Symbol ready to be placed | Standard appearance |
| **Hover/Preview** | Student hovering over placement position | Ghost/translucent preview at position |
| **Placed** | Symbol successfully positioned on graph | Solid, snapped to grid position |
| **Selected for comparison** | Category clicked for comparison | Highlight row/column |

### Pre-Completion Scaffolding (Mode 2)

- UX to determine visual treatment

**Scaffolding Levels:**

- **High scaffold:** 3 of 4 categories pre-filled (student completes 1)
- **Medium scaffold:** 2 of 4 categories pre-filled (student completes 2)
- **Low scaffold:** 1 of 4 categories pre-filled (student completes 3)
- **No scaffold:** All categories empty (student completes all)

**Progression:** High scaffold in early M2 → No scaffold by late M3

## Allowed Student Actions

### Mode 1: Reading

- Picture Graphs in reading mode are display-only. Students view graphs but do not interact. Any highlighting or comparison is system-driven for instruction/remediation.

### Click-to-Set (Mode 2: Creating)

**Interaction Flow:**

1. Student hovers over category position → Ghost preview appears showing symbol count at that position
2. Preview updates as hover moves (including half-symbol increments where applicable)
3. Student clicks → Symbols lock in at previewed count
4. Repeat for remaining categories

**Half-Symbol Increments:** Preview system shows both full and half-symbol positions (e.g., for scale of 2: 1, 1.5, 2, 2.5, 3... where .5 positions show half-symbols)

## Additional Teaching/Remediation Actions

### Highlight

- UX to provide visual/video

**Description:** Guide draws attention to specific category, symbols, or scale indicator.

**Purpose:** Direct student focus during instruction.

**Triggers:**

- Guide narration about specific data
- Teaching scale meaning
- Error correction (student miscounting symbols)

### Scale Indicator Emphasis

- UX to provide visual/video

**Description:** Highlight or animate the scale indicator text.

**Example:** "Each 🐾 = 2" pulses or is highlighted

**Purpose:**

- Reinforce scale meaning
- Prevent "symbol counting" misconception (counting symbols instead of skip-counting by scale value)
- Draw attention when students need to interpret value

### Comparison Display

- UX to provide visual/video

**Description:** System shows mathematical comparisons between categories for instruction

**Behavior:**

- Appears adjacent to graph (not blocking view)
- Shows operation: "12 - 8 = 4" or "12 + 8 = 20"
- May include visual representation

**Purpose:** Make mathematical relationships explicit; support problem-solving.

**Note:** This may be part of a separate **Comparison Tool** that works across Data Tables, Picture Graphs, and Bar Graphs.

### Grouping Animation Connection

- Coordinate with Animation toy specs

**Description:** Animation showing items → groups → symbols on picture graph.

**Example Flow:**

- 10 individual items displayed
- Items group into 5 groups of 2
- Each group transforms into one symbol
- Symbols arrange on picture graph

**Purpose:** Make scale relationship concrete; show that symbols represent groups, not individual items.

**Used In:** M2 introduction of 1:2 scale

## Division Properties

- Picture Graphs do not divide internally (though symbols represent divided quantities conceptually)

## Constraints

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| One symbol per graph | All categories use the same symbol type (not different symbols per category) |
| Snap-to-position | Symbols align to grid positions (no free placement) |
| Symbol integrity | Symbols cannot be edited, rotated, or resized by students |
| Directional consistency | Horizontal graphs extend right; vertical graphs stack up (no reverse) |
| Half-symbol cuts only | Cannot create quarter-symbols or other fractions |

### Interaction Constraints (What Students CAN Do)

| Action | Constraint | Notes |
| --- | --- | --- |
| Place symbols (Mode 2) | Up to value in data table | Cannot over-place |
| Click categories (Mode 1) | Any 1-2 categories | For reading/comparison |
| Use half-symbols | When needed for odd numbers | Except M3 (multiples only) |
| Count symbols | Any completed graph | Core skill |
| Maximum categories per graph | 4-6 categories | Fits screen without scrolling |
| Maximum symbols per category | ~20 symbols | Countability limit |

### Question Constraints (What We ASK Students to Do)

**By Module:**

| Module | Creating | Reading | Half-Symbols | Scale | Question Types |
| --- | --- | --- | --- | --- | --- |
| **M1** | ❌ | ✅ | No | 1:1 | Direct reading ("How many X?") |
| **M2** | ✅ | ✅ | Yes (half = 1) | 1:2 | Creating, reading, comparison ("How many more?") |
| **M3** | ✅ | ✅ | No (multiples only) | 1:5 | Creating, reading, comparison, side-by-side with bar graphs |
| **M4** | ❌ | ✅ | Yes (half = 5) | 1:10 | Observation only (format comparison to bars) |
| **M5-M6** | ❌ | ✅ | Yes | Mixed | Scale comparison across 1:2, 1:5, 1:10 |
| **M9** | ❌ | ✅ | Varies | Mixed | Connection to multiplication (scales as factors) |

**Never Ask:**

- Create picture graphs with scale of 10 (observation only)
- Use half-symbols with scale of 5 (M3 constraint)
- Compare more than 2 categories simultaneously
- Calculate averages or percentages from picture graphs

### Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Grouping animation | Supports up to 20 items → 10 groups | For scales 2 and 5 |
| Comparison display | 2 categories only | Not 3+ category comparisons |
| Scale indicator | Always visible when scale > 1 | Cannot be hidden |
| Symbol clarity at scale | Symbols readable up to scale of 10 | Visual design must remain clear |
| Half-symbol support | Horizontal and vertical cuts only | No diagonal or other cuts |

## Layout Constraints

- UX to determine positioning

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum categories | 4-6 per graph | Avoid scrolling |
| Minimum categories | 2 categories | Need at least two for comparison |
| Can appear with | Data Tables, Bar Graphs, Comparison Tool, Scale Selector | Common pairings |
| Typical position | Center (Mode 1), Right side (Mode 2 with table on left) | Activity-dependent |
| Cannot appear with | Multiple picture graphs simultaneously | Only one at a time |
| Symbol spacing | Consistent within graph | UX to define grid |

**Common Layout Patterns:**

- **M2-M3 Creating:** Data Table (left) + Picture Graph (right, editable)
- **M1, M5-M6 Reading:** Picture Graph (center) + Questions (below)
- **M3-M4 Comparison:** Picture Graph (left) + Bar Graph (right, same data)

## Tool to Schema Vocab Translation

- Engineering to complete

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
| "horizontal orientation" | `orientation: "horizontal"` | Symbols extend right |
| "vertical orientation" | `orientation: "vertical"` | Symbols stack up |
| "scale of 2" | `scale: 2` | Each symbol = 2 items |
| "full symbol" | `symbol_type: "full"` | Complete symbol |
| "half symbol" | `symbol_type: "half"` | Partial symbol |
| "horizontal cut" | `half_cut_type: "horizontal"` | Left-right division |
| "vertical cut" | `half_cut_type: "vertical"` | Top-bottom division |
| "reading mode" | `mode: "reading"` | Pre-made, non-editable |
| "creating mode" | `mode: "creating"` | Student places symbols |
| "symbol library" | `available_symbols: [...]` | Array of symbol options |
| "categories" | `categories: ["Dogs", "Cats", ...]` | Array of category labels |
| "values" | `values: [8, 12, 6, 10]` | Target values (for creating mode) |
| "placed symbols" | `placed_counts: [4, 6, 3, 5]` | Current symbol counts per category |
| "scale indicator text" | `scale_text: "Each 🐾 = 2"` | Displayed scale label |

## Curriculum Animators Techs

- Waiting on engineering implementation

## Open Questions

- [ ]  **Symbol library size:** Is 20-30 symbols sufficient? Should certain contexts have more variety?
- [ ]  **Scale indicator interaction:** Can students click scale indicator for explanation/reminder, or is it static text?
- [ ]  **Comparison display:** Confirmed as separate tool across toys, or integrated per toy?
- [ ]  **Pre-filled symbol visual:** How do pre-filled categories appear differently from student-placed symbols?
- [ ]  **M3 scale of 5 design decision:** Why no half-symbols in M3? Document pedagogical rationale for UX team.
- [ ]  **Ghost preview behavior:** How prominent? Does it show full vs half symbol automatically?
- [ ]  **Maximum value design:** What's the largest value we'll ever display? (impacts symbol spacing and graph size)
- [ ]  **Multi-orientation switch:** Can students toggle between horizontal/vertical for same data, or is orientation fixed per activity?

## JSON Schema Formatting

