# Bar Graphs

Category: Unit 1
Created: February 3, 2026 4:45 PM
Status: UX in Process
Target Audience: Grade 3 Unit 1

---

> **WHAT:** A visual data display system using continuous horizontal or vertical bars where the height or length of each bar represents a quantitative value on a scaled axis with tick marks.

**WHY:** Bar Graphs provide the critical transition from discrete (countable symbols) to continuous (measured lengths) representation of scaled data. This is a foundational shift in mathematical abstraction—students move from counting individual symbols to reading values from positions on an axis. The continuous nature of bars eliminates the cognitive load of counting and instead requires interpolation skills (reading between tick marks), which is essential for later work with measurement, number lines, and coordinate systems. Bar graphs also introduce the concept that data can be represented without individual countable units, preparing students for more abstract mathematical representations. The format is universally used in real-world contexts (newspapers, reports, scientific data), making this a critical life skill. Research on visual-to-numeric bridging shows that the explicit transition from picture graphs (discrete symbols) to bar graphs (continuous) has effect sizes of 0.50-0.77 for data literacy in elementary students. In M5, bar graphs uniquely support scale selection decision-making—students must evaluate data characteristics and choose appropriate scales, developing metacognitive skills about representation efficiency.
>

## Shape:

- UX to provide visuals

### Bar (Continuous Rectangle)

A solid, continuous rectangle extending from the zero baseline to a value on the scaled axis.

📷 *Placeholder for bar examples (horizontal and vertical)*

**Key Visual Properties:**

- **Continuous fill** (no gaps or segments within the bar)
- **Uniform width** (all bars same width within a graph)
- **Clean edges** (precise alignment with axis)
- **Extends from zero** (baseline at 0, not floating)
- **Color/shading** (distinct but not distracting)

### Axis System

The framework that gives bars their measurable meaning.

📷 *Placeholder for axis system diagram*

**Components:**

**Scaled Axis (Numeric Axis):**

- Perpendicular to bar direction
- **Tick marks** at regular intervals based on scale
- **Numeric labels** at major tick marks
- **Zero baseline** clearly marked
- **Scale indicator** (may appear as "Scale: 1:5" or implicit from labels)

**Category Axis (Qualitative Axis):**

- Parallel to bar direction (or perpendicular in horizontal orientation)
- **Category labels** for each bar
- **Even spacing** between categories
- **No numeric values** (categorical, not quantitative)

**Example - Vertical Orientation:**

`Numeric axis (left side, vertical):
   40 |
   30 |
   20 |
   10 |
    0 |_______________
       Dogs Cats Birds
       Category axis (bottom, horizontal)`

**Example - Horizontal Orientation:**

`Category axis (left, vertical)    Numeric axis (bottom, horizontal)
Dogs    |========>                 0  10  20  30  40
Cats    |============>
Birds   |======>`

### Ghost Gridlines (Mode 2: Creating Only)

Subtle horizontal or vertical lines extending from tick marks across the graph area.

📷 *Placeholder for ghost gridlines visual*

**Purpose:** Help students align bars precisely during creation; provide visual reference for reading values.

**Behavior:**

- Appear during bar adjustment (Mode 2)
- Semi-transparent, not dominating
- Can be toggled on/off (scaffolding control)
- Disappear or become very subtle in final display

## Properties

### Orientation

- UX to provide visuals for each orientation

| Orientation | Description | Bar Direction | Axis Configuration | When Used |
| --- | --- | --- | --- | --- |
| **Horizontal** | Bars extend rightward | Left → Right | Numeric axis on bottom/top; Category labels on left | All modules (mixed) |
| **Vertical** | Bars extend upward | Bottom → Top | Numeric axis on left/right; Category labels on bottom | All modules (mixed) |

**Note:** Both orientations used throughout Unit 1. No pedagogical preference; students should be flexible with both.

### Scale (Axis Increment)

- UX to provide scale indicator visuals

| Scale | Tick Mark Spacing | When Introduced | Halfway Points (Interpolation) |
| --- | --- | --- | --- |
| **1:1** | Every unit (1, 2, 3, 4...) | M1 (review, rarely used) | Not needed (every value has tick) |
| **1:2** | Every 2 units (2, 4, 6, 8...) | M3 (brief, mainly picture graphs) | Yes (odd numbers = halfway) |
| **1:5** | Every 5 units (5, 10, 15, 20...) | M3 (introduction of bars) | Introduced in M4 (halfway = 2.5, but we use multiples of 5) |
| **1:10** | Every 10 units (10, 20, 30, 40...) | M4 (primary focus) | Yes (multiples of 5 not 10 = halfway) |

**Scale Indicator Display:**

- May appear as text above/near graph: "Scale: 1:10" or "Each tick mark = 10"
- Or implicit from axis labels (if labeled 0, 10, 20, 30..., scale is clearly 10)
- Always clear to students; no guessing required

### Mode

- UX to provide visuals for each mode

| Mode | Description | Student Interaction | When Used |
| --- | --- | --- | --- |
| **Mode 1: Reading** | Pre-made bar graphs for interpretation | Click bars, hover for values, compare | All modules |
| **Mode 2: Creating** | Student adjusts bar heights to match data | Hover-to-preview, click-to-set, confirm | M3-M5 |

**Critical Distinction:** Unlike picture graphs where students "place" discrete symbols, bar creation is about "adjusting height" of continuous bars.

### Bar States (Mode 2 Only)

- UX to provide visuals for each state

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Unset (default)** | Bar at zero or minimal height, awaiting adjustment | Faint outline or minimal bar |
| **Hover-Preview** | Student hovering to adjust; bar follows cursor | Translucent bar showing potential height |
| **Active-Adjustment** | Bar height changes as student moves cursor | Highlight border; ghost gridlines visible |
| **Set-Awaiting-Confirm** | Bar positioned but not locked in | Solid color; may show value label |
| **Confirmed** | Bar finalized, cannot be changed without reset | Standard bar appearance |
| **Selected-for-Comparison** | Bar clicked for reading comparison | Highlight/glow effect |

### Pre-Completion Scaffolding (Mode 2)

- UX to determine visual treatment

**Scaffolding Levels:**

- **High scaffold:** 3 of 4 bars pre-set (student adjusts 1)
- **Medium scaffold:** 2 of 4 bars pre-set (student adjusts 2)
- **Low scaffold:** All bars empty (student adjusts all 4-5)

**Progression:** High scaffold in M3-M4 early → Low scaffold by M4 late → No scaffold in M5-M6

**Visual Distinction:** Pre-set bars may appear in different color/shade or with checkmark to indicate "already correct."

## Allowed Student Actions

### Mode 1: Reading

- Bar Graphs in reading mode are display-only. Students view graphs but do not interact. Any highlighting or comparison is system-driven for instruction/remediation.

###

### Hover to Preview Bar Height (Mode 2: Creating)

- UX to provide interaction visual/video

**Description:** Student hovers cursor over bar adjustment area to see potential bar height.

**Interaction Flow:**

1. **Student reads value from data table** (e.g., "Dogs: 25")
2. **Student positions cursor** near where bar should end
3. **Ghost bar appears** following cursor, showing potential height
4. **Ghost gridlines activate** (if enabled) showing alignment
5. **Value preview may display** showing current height

**Visual Feedback:**

- Translucent bar extending from zero to cursor position
- Snap-to-scale indicators (bar "pulls" toward valid tick marks)
- Numerical value preview (optional)

**Purpose:** Allow precise positioning before committing; reduce errors; build understanding of scale.

### Click to Confirm Bar Height (Mode 2: Creating)

- UX to provide interaction visual/video

**Description:** Student clicks to set bar height at previewed position.

**Behavior:**

- Bar solidifies at clicked height
- Snaps to nearest valid value (tick mark or halfway point)
- Value confirmation displays briefly
- Bar changes to "confirmed" state

**Error Prevention:**

- If value doesn't match data table target (creating mode), subtle indication "Check the data table"
- System may require match before allowing progression

###

## Additional Teaching/Remediation Actions

### Highlight Bar or Axis Element

- UX to provide visual/video

**Description:** Guide draws attention to specific bar, tick mark, or axis label.

**Purpose:** Direct student focus during instruction; emphasize specific values or comparisons.

### Tick Mark Emphasis

- UX to provide visual/video

**Description:** Highlight specific tick marks or the spacing between them.

**Example:** Guide explains "See how each tick mark represents 10? Count by tens..."

**Purpose:** Teach scale reading; reinforce skip-counting connection.

### Interpolation Demonstration

- UX to provide visual/video

**Description:** Show how to read values between tick marks (halfway points).

**Visual Example:**

- Highlight two adjacent tick marks (e.g., 20 and 30)
- Show bar ending halfway between them
- Guide: "This bar is halfway between 20 and 30, so the value is 25."

**Purpose:** Critical skill for scales of 5 and 10; addresses common student error of only reading tick mark values.

### Comparison Display

- UX to provide visual/video

**Description:** When student clicks two bars, system displays mathematical comparison.

**Behavior:**

- Appears adjacent to graph
- Shows operation: "30 - 20 = 10" or "30 + 20 = 50"
- May include visual representation (difference bar, number line)

**Purpose:** Make mathematical relationships explicit; support problem-solving.

**Note:** May be part of a separate **Comparison Tool** that works across Data Tables, Picture Graphs, and Bar Graphs.

### Ghost Gridline Toggle

- UX to provide visual/video

**Description:** Guide or student can show/hide ghost gridlines.

**Purpose:** Scaffolding control—gridlines help in early creation, then are removed as students gain proficiency.

## Division Properties

- Bar Graphs do not divide internally (though they represent scaled values conceptually)

## Constraints

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| Continuous bars only | No segmentation or gaps within bars |
| Extends from zero | All bars start at baseline (not floating) |
| Uniform bar width | All bars within graph have same width |
| Snap-to-valid-values | Bars land on tick marks or halfway points only |
| No negative values | Grade 3 works with positive values only |
| Axis starts at zero | No "broken axis" or non-zero starting points |

### Interaction Constraints (What Students CAN Do)

| Action | Constraint | Notes |
| --- | --- | --- |
| Set bar heights (Mode 2) | Up to data table target value | Snap-to-scale |
| Click bars (Mode 1) | Any 1-2 bars | For reading/comparison |
| Toggle gridlines (Mode 2) | On/off based on scaffolding level | Teacher or student control |
| Interpolate values | Read halfway points (multiples of 5 at scale 10) | Critical skill |
| Maximum categories per graph | 4-6 categories | Fits screen without scrolling |
| Maximum value displayed | ~100 at scale 10, ~50 at scale 5 | Readability limit |

### Question Constraints (What We ASK Students to Do)

**By Module:**

| Module | Creating | Reading | Interpolation | Scale | Question Types |
| --- | --- | --- | --- | --- | --- |
| **M1** | ❌ | ✅ | No | 1:1 | Direct reading (rare—mostly picture graphs) |
| **M3 Late** | ✅ | ✅ | No (multiples only) | 1:5 | Creating, reading; comparison to picture graphs |
| **M4 Early-Mid** | ✅ | ✅ | No (multiples of 10 only) | 1:10 | Creating with high scaffold; direct reading |
| **M4 Late** | ✅ | ✅ | Yes (multiples of 5) | 1:10 | Creating with low scaffold; interpolation introduced |
| **M5** | ✅ | ✅ | Yes | Student selects (1, 2, 5, or 10) | Scale selection + creation + reading |
| **M6** | ❌ | ✅ | Yes | Mixed (5 or 10) | Problem-solving with pre-made graphs |

**Value Constraints (All Modules):**

- **All values are multiples of 5** (maintains no-estimation principle)
- Students can read values **precisely** from axis (no approximation)
- Example valid values: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
- Example invalid values: 7, 13, 22, 38 (would require estimation)

**Never Ask:**

- Estimate values between non-halfway points (e.g., "about 23")
- Create bars with scale of 1 (too tedious; picture graphs better)
- Read values from poorly-designed scales (always provide clear scales)
- Compare more than 2 bars simultaneously

### Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Comparison display | 2 bars only | Not 3+ bar comparisons |
| Ghost gridlines | Can be toggled on/off | Scaffolding tool |
| Interpolation teaching | Halfway points only (multiples of 5) | Not arbitrary points |
| Scale selector (M5) | 4 options: 1, 2, 5, 10 | No other scales |
| Preview pane (M5) | Shows one scale at a time | Student can switch freely |

## Layout Constraints

- UX to determine positioning

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum categories | 4-6 per graph | Avoid scrolling |
| Minimum categories | 2 categories | Need at least two for comparison |
| Can appear with | Data Tables, Picture Graphs, Comparison Tool, Scale Selector (M5) | Common pairings |
| Typical position | Center (Mode 1), Right side (Mode 2 with table on left) | Activity-dependent |
| Cannot appear with | Multiple bar graphs simultaneously (except M3-M4 transformation) | Focus on one at a time |
| Axis label clarity | Large enough for Grade 3 readability | Font size critical |

**Common Layout Patterns:**

- **M3-M4 Creating:** Data Table (left) + Bar Graph (right, editable)
- **M3-M4 Comparison:** Picture Graph (left) + Bar Graph (right, same data)
- **M5 Scale Selection:** Data Table (top/left) + Scale Selector (top/center) + Preview Pane (center) + Final Graph (center after confirm)
- **M6 Problem-Solving:** Bar Graph (center) + Questions (below or right)

---

## Scale Selection Feature (M5 Only)

- UX to design complete interface

### Overview

In M5, students choose which scale to use before creating a bar graph. This develops metacognitive skills about representation efficiency and data-to-scale matching.

### Interface Components

📷 *Placeholder for complete scale selection interface mockup*

**1. Data Table (Reference)**

- Displays the dataset to be graphed
- Always visible during scale selection
- Student references this to evaluate options

**2. Scale Selector (Four Options)**

- Clickable buttons or tabs: **Scale of 1** | **Scale of 2** | **Scale of 5** | **Scale of 10**
- Student can freely switch between options
- Selected scale highlights

**3. Preview Pane (Live Update)**

- Shows what the bar graph WOULD look like with selected scale
- Updates immediately when student selects different scale
- **Validation feedback:**
    - ✅ "All data fits!" (green indicator)
    - ⚠️ "Tallest bar won't fit - try a bigger scale" (warning indicator, problematic value highlighted)
- Displays actual bars at potential heights (not just empty axes)

**4. Confirm Button**

- "Use This Scale" or "Create Graph"
- Locks in scale choice
- Transitions to standard bar creation mode (hover-to-preview, click-to-set)

### Behavior

**Exploration Phase:**

- Student clicks different scales
- Preview updates in real-time
- Student evaluates: "Does it fit?" "Is it easy to read?" "Is it efficient?"
- Can switch unlimited times before confirming

**Validation:**

- System checks if maximum data value fits within graph bounds for selected scale
- If scale too small: Warning displays, problematic bar(s) highlighted in preview
- If scale works: Green checkmark or "All data fits!" message

**Confirmation:**

- Student clicks "Confirm" or "Use This Scale"
- Scale is locked in
- Interface switches to creation mode with that scale
- **Scale cannot be changed** after confirmation (would require restart)

### Pedagogical Goals

- Develop scale-selection strategy: Small data range → smaller scale; Large data range → larger scale
- Understand tradeoffs: Efficiency (fewer tick marks) vs. Precision (more detail)
- Practice metacognition: "Does my choice make sense for THIS data?"

### Constraints (M5 Scale Selection)

| Constraint | Value | Notes |
| --- | --- | --- |
| Available scales | 1, 2, 5, 10 only | No custom scales |
| Data values | All multiples of 5 | Maintains no-estimation principle |
| Preview accuracy | Must show actual bar heights | Not just empty axes |
| Validation timing | Real-time as student switches | Not after confirmation |
| Confirmation requirement | Cannot proceed without confirming | Prevents accidental scale use |

## Tool to Schema Vocab Translation

- Engineering to complete

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
| "horizontal orientation" | `orientation: "horizontal"` | Bars extend right |
| "vertical orientation" | `orientation: "vertical"` | Bars extend up |
| "scale of 5" | `scale: 5` | Each tick mark = 5 units |
| "tick marks" | `tick_marks: [0, 5, 10, 15, ...]` | Array of labeled positions |
| "ghost gridlines on" | `show_gridlines: true` | Scaffolding enabled |
| "reading mode" | `mode: "reading"` | Pre-made, non-editable |
| "creating mode" | `mode: "creating"` | Student adjusts bars |
| "categories" | `categories: ["Dogs", "Cats", ...]` | Array of category labels |
| "values" | `values: [25, 30, 15, 20]` | Target values (for creating mode) |
| "bar heights" | `bar_heights: [25, 30, 0, 0]` | Current bar positions |
| "snap-to-scale enabled" | `snap_to_valid_values: true` | Bars land on tick marks/halfway |
| "scale selection mode" | `scale_selection: {available: [1,2,5,10], selected: 5, confirmed: false}` | M5 feature |
| "preview graph" | `preview_mode: true` | Showing potential graph |
| "interpolation values" | `allow_halfway_points: true` | For scales 2, 5, 10 |

## Curriculum Animators Techs

- Waiting on engineering implementation

## Open Questions

- [ ]  **Value display timing:** When does exact numeric value show? Continuously? On hover? On confirm only?
- [ ]  **Ghost gridline default:** On by default in early M3-M4, off by default in late M4-M5?
- [ ]  **Scale selection preview:** How prominent? Full-size preview or thumbnail comparison?
- [ ]  **Problematic value highlighting:** How does system show "this value won't fit with this scale"? Red bar? Warning icon?
- [ ]  **Confirmation lock:** Once scale confirmed in M5, can student request a restart/reset, or is it permanent?
- [ ]  **Interpolation teaching:** How does system explain halfway points? Tooltip? Guide narration? Visual demonstration?
- [ ]  **Comparison display:** Confirmed as separate tool across toys, or integrated per toy?
- [ ]  **Maximum value guidance:** Should system suggest scale based on data range, or let student discover?
- [ ]  **Tick mark label density:** How many numeric labels show? Every tick? Every other? Strategic points only?
- [ ]  **Bar color/shading:** Single color? Category-specific colors? Student-selectable?
- [ ]  **Horizontal vs vertical default:** Any pedagogical reason to prefer one orientation for certain activities?

## JSON Schema Formatting


