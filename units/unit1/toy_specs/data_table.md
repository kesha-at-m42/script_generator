# Data Tables

Category: Unit 1
Created: February 3, 2026 4:28 PM
Status: Ready for UX
Target Audience: Grade 3 Unit 1

---

> **WHAT:** A two-column display system for organizing categorical data in table format with category labels and corresponding numerical or symbolic values.

**WHY:** Data Tables provide the foundational structure for students to read, reference, and extract information when creating graphs. They establish the relationship between categories and quantities in a structured format that supports both reading comprehension and graph construction. The table format helps students understand data organization before translating it into visual representations. In early modules (M2-M3), symbol display mode provides explicit scaffolding for the grouping concept (each symbol = multiple items) before students work with pure numeric abstraction. This supports the critical transition from concrete counting to scaled representation.
>

## Shape:

- UX to provide visuals

### Data Table Structure

A simple two-column table displaying categorical data:

- **Column 1:** Category labels (text)
- **Column 2:** Values (numbers or grouped symbols)
- **Rows:** 4-6 maximum (no scrolling required)

📷 *Placeholder for standard numeric table image*

**Example - Numeric Display:**

`| Category  | Value |
|-----------|-------|
| Dogs      | 8     |
| Cats      | 12    |
| Birds     | 6     |
| Fish      | 10    |`

📷 *Placeholder for symbol display table image*

**Example - Symbol Display (M2-M3 only):**

`| Category  | Symbols (Each 🐕 = 2) |
|-----------|------------------------|
| Dogs      | 🐕🐕🐕🐕               |
| Cats      | 🐕🐕🐕🐕🐕🐕           |
| Birds     | 🐕🐕🐕                 |
| Fish      | 🐕🐕🐕🐕🐕             |`

## Properties

### Display Modes

- UX to provide visuals for each mode

| Mode | Description | Visual Treatment | When Used |
| --- | --- | --- | --- |
| **Numeric Display** | Value column shows numbers only | Standard table with clean typography | M1, M4-M12, and late M2-M3 activities |
| **Symbol Display** | Value column shows grouped symbols representing values | Symbols arranged in groups with scale indicator | Early/mid M2-M3 only (scaffolding) |

### State Properties

- UX to provide visuals for each state

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Default** | Table displayed, no interaction | Standard readable format |
| **Row Hover** | Mouse over a row | Subtle highlight of entire row |
| **Single Row Selected** | One row clicked | Row highlighted, comparison inactive |
| **Two Rows Selected** | Two rows clicked | Both rows highlighted, triggers comparison display |

### Symbol Display Properties (M2-M3 Only)

- UX to finalize

When in Symbol Display mode:

- **Scale indicator** appears above or below table
- **Format:** "Each [symbol] = [number]"
- **Example:** "Each 🐕 = 2"
- **Symbol arrangement:** Grouped visually to show scale relationship
- **Purpose:** Help students visualize grouping before numeric abstraction

### Typography & Readability

- UX to specify
- **Font size:** Large enough for Grade 3 readability
- **Row height:** Comfortable spacing between rows
- **Column width:** Auto-adjusts to content
- **Alignment:** Left-aligned text, right-aligned numbers (standard table conventions)

---

## Allowed Student Actions

### Hover (Debatable if we need this, Jon thinks no)

- UX to provide interaction visual

**Description:** Mouse hovers over any row.

**Behavior:**

- Subtle highlight of the entire row
- No tooltip or additional information needed (values already visible)

**Purpose:** Indicate interactive element, help with visual tracking.

## Additional Teaching/Remediation Actions

### Highlight

- UX to provide visual

**Description:** Guide draws attention to specific row(s) or the scale indicator.

**Purpose:** Direct student attention during instruction; emphasize key information.

**Triggers:**

- Guide narration referencing specific category
- Teaching moment about scale meaning
- Error correction (student using wrong data)

### Comparison Display

- UX to provide visual

**Description:** When student clicks two rows, system displays the comparison.

**Behavior:**

- Appears adjacent to table (not blocking view)
- Shows operation: "12 - 8 = 4" or "12 + 8 = 20"
- May include visual representation (bars, number line)

**Purpose:** Support problem-solving by making mathematical relationship explicit.

**Note:** This may be part of a separate Comparison Tool that works across multiple toys (Tables, Picture Graphs, Bar Graphs).

### Scale Indicator Emphasis (Symbol Display Only)

- UX to provide visual

**Description:** Highlight or animate the scale indicator ("Each 🐕 = 2").

**Purpose:** Ensure students understand the grouping relationship; prevent "symbol counting" misconception.

## Division Properties

- Data Tables do not divide or partition

## Constraints

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| Read-only display | Students cannot edit table values |
| No scrolling | Maximum 4-6 rows to fit on screen |
| Two-column structure only | No multi-column support needed |
| Static after display | Table contents do not change during activity |

### Question Constraints (What We ASK Students to Do)

| Question Type | Constraint | Notes |
| --- | --- | --- |
| Read values | Students extract specific values | "How many dogs?" |
| Compare two values | Students click two rows, read comparison | "How many more X than Y?" |
| Find totals | Students click two rows, read sum | "How many X and Y altogether?" |
| NO: Multi-category operations | Never ask to compare 3+ categories | Too complex for Grade 3 |
| NO: Complex calculations | Never ask for percentages, averages | Beyond grade level |

### Visual/Teaching Constraints (What Remediation Tools Support)

| Feature | Constraint | Notes |
| --- | --- | --- |
| Comparison display | Supports 2 rows only | Not 3+ row comparisons |
| Symbol display scaffolding | M2-M3 only, removed by M4 | Intentional fade-out |
| Highlight animation | Any single row or scale indicator | For guide instruction |

## Layout Constraints

- UX to determine positioning

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum rows | 4-6 rows | Avoid scrolling |
| Minimum rows | 2 rows | Need at least two categories for comparison |
| Can appear with | Picture Graphs, Bar Graphs, Comparison Tool | Common pairings |
| Typical position | Left side or top of screen | Reference position while student works with graph on right/bottom |
| Cannot appear with | Multiple tables simultaneously | Only one data source at a time |

**Common Layout Patterns:**

- **M2-M5:** Table (left) + Graph (right) for creation activities
- **M6:** Graph (center) + Table (appears on demand) for problem-solving
- **M1:** Table + Graph side-by-side for reading/comparison

## Tool to Schema Vocab Translation

- Engineering to complete

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
| "numeric display" | `display_mode: "numeric"` | Default mode |
| "symbol display" | `display_mode: "symbol"` | M2-M3 scaffolding mode |
| "scale indicator" | `scale: 2` (example) | Only relevant when display_mode = "symbol" |
| "row highlighted" | `selected_rows: [0]` or `[0, 2]` | Array of row indices |
| "show comparison" | `comparison_active: true` | Triggers comparison display |
| "category label" | `categories: ["Dogs", "Cats", ...]` | Array of strings |
| "values" | `values: [8, 12, 6, 10]` | Array of numbers |

## Curriculum Animators Techs

- Waiting on engineering implementation

## Open Questions

- [ ]  **Symbol Display transition:** Exactly which activities in M2-M3 use symbol display vs numeric display? Need activity-level specification.
- [ ]  **Comparison display:** Is this part of Data Table or a separate Comparison Tool that works across all toys?
- [ ]  **Hover behavior:** Should hovering show highlight?
- [ ]  **Scale indicator position:** Above table, below table, or inline with header?
- [ ]  **Symbol variety:** Does symbol display need multiple symbol options (🐕, 🐈, 🐦) or always use one consistent symbol per table?
- [ ]  **Maximum value size:** What's the largest value we'll display? (determines column width needs)
---

