# MODULE 6: Multiplication Strategies — Area Models

**Version:** 2026-04-16 (Gate 4 fixes applied; ready for SME review)

```
---
module_id: M06
unit: 4
domain: operations_algebraic_thinking
primary_toys:
  - name: "Grid Rectangles"
    notion_url: "https://www.notion.so/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca"
  - name: "Equation Builder"
    notion_url: "https://www.notion.so/Equation-Builder-2fc5917eac52803f8604f47c62304ee7"
secondary_toys:
  - name: "Multiplication Tables Grid"
    notion_url: "https://www.notion.so/Multiplication-Tables-Grid-1395917eac52801da8e3d35eb2e6ca3e"
interaction_tools:
  - "Select (single) (MC selection, partition point confirmation)"
  - "Drag to build (Equation Builder partial-product expression construction)"
  - "Place tick (partition line placement on gridded/ungridded rectangles)"
---
```

---

# BACKBONE

---

## 1.0 THE ONE THING

**[REQUIRED]**

Breaking apart a factor into simpler parts creates two smaller multiplication problems. When you add those partial products together, they equal the original product — every time, no matter where you choose to break. The area model makes this principle VISIBLE: both sub-rectangles are right there on screen, each with its own dimensions and its own multiplication, so you can SEE why the parts sum to the whole. Different students can choose different decomposition points and still get the same answer — the strategy is the choice, not the specific partition.

**CRA Stage:** Representational → Abstract. Gridded area models (Early/Mid — students can count squares to verify) transition to ungridded/open area models (Late — dimensions only, no counting fallback). This mirrors Unit 2's progression but compressed because students have already made this transition once for area measurement. The Equation Builder appears alongside the area model from the start (D4 — simultaneous connections), making the expression-to-diagram link explicit from the first interaction.

**Critical Misconception:** U4.6 — Distributive property applied incorrectly. Students who decompose 7 × 14 as 7 × 10 + 4 (forgetting to multiply the second part by 7) are caught by the area model: both sub-rectangles visually require their own multiplication. The model makes the error impossible to miss — both pieces are on screen simultaneously.

**Biggest Risk:** Students learn the decomposition procedure without understanding WHY it works — they mechanically partition and compute without connecting the sub-rectangles to the original product. If the area model feels like an extra step rather than a meaning-making tool, students will abandon it for mental math shortcuts that don't scale to larger numbers. The strategic choice element is essential: if every student decomposes the same way, it becomes a procedure; when students choose their own partition point, it becomes a strategy.

**Success Indicator (Core):** Given an ungridded rectangle (e.g., 7 × 13), the student can choose a benchmark decomposition point, write the matching partial-product expression with parentheses, and compute the total — without counting individual squares.

**Success Indicator (Extended):** The student can also produce an alternative decomposition of the same rectangle and verify that it produces the same product. This strategic flexibility is the full learning target, but some students will develop it in Practice rather than by end of Lesson — EC.3 tests it as the highest-demand item.

---

## 1.1 LEARNING GOALS

**[REQUIRED]**

*Verbatim — Script Must Achieve These*

**L10:** Use area diagrams to explore strategies based on properties of multiplication.

**L11:** Apply associative and distributive properties of multiplication to find products within 100. Recognize that multiplication is associative and can be distributed over addition.

> **D5 Constraint:** Students experience both properties through the area model but do NOT name them as "distributive property" or "associative property." Strategy language is "breaking apart" and "decompose." The L11 goal is achieved through the strategy, not through formal property naming.

**Module Goal (Student-Facing):** "You'll discover how breaking a rectangle into parts turns one hard multiplication problem into two easier ones — and YOU get to choose where to break."

**Exit Check Tests:** (1) Connect a gridded decomposition to the matching partial-product expression, (2) Decompose an ungridded rectangle, write the expression, and find the product, (3) Produce an alternative decomposition of the same rectangle.

### Standards Cascade

| Role | Standard | Description |
| :---- | :---- | :---- |
| **Addressing** | 3.OA.B.5 | Apply properties of operations as strategies to multiply and divide. |
| **Addressing** | 3.MD.C.7c | Use tiling to show in a concrete case that the area of a rectangle with whole-number side lengths a and b + c is the sum of a × b and a × c. Use area models to represent the distributive property. |
| **Building On** | M5 | Commutativity — students know order doesn't matter for multiplication. Multiplication table patterns. |
| **Building On** | Unit 2 | Area concepts, Grid Rectangles tool, gridded → ungridded progression. |
| **Building Toward** | 3.NBT.A.3 | Multiply one-digit whole numbers by multiples of 10. |
| **Building Toward** | M8 | Teen number multiplication strategies — area model decomposition applied to two-digit × one-digit. |

### Module Bridges

| Direction | Content |
| :---- | :---- |
| **From M5** | Students arrive with commutativity proven through arrays and table symmetry. They know order doesn't matter for multiplication and that it DOES matter for division. The multiplication table is a familiar reference. They have been writing commutative pairs and fact families since M4. All three unknown representations (?, □, letter) are used interchangeably. Grid Rectangles are familiar from Unit 2 area measurement work. |
| **This Module (M6)** | Reintroduce Grid Rectangles in a new role — not measuring area, but using the area model as a multiplication STRATEGY. Guide demonstrates that partitioning a rectangle creates two simpler sub-problems whose products sum to the original. Students progress from guided decomposition on gridded models (Early) to student-chosen decomposition (Mid) to ungridded rectangles where counting isn't possible (Late). The expression-to-diagram link is explicit throughout: each decomposition maps to a partial-product expression with parentheses. Students discover that different decompositions produce the same total — the choice of where to break is strategic, not prescribed. |
| **To M7** | Students leave with the "breaking apart" strategy fully operational on both gridded and ungridded rectangles. They can write partial-product expressions, choose decomposition points strategically, and understand why the strategy works (the area model makes both parts visible). M7 introduces a DIFFERENT strategy — place value reasoning for multiples of 10 — with a tool switch from Grid Rectangles to Base-10 Blocks that signals the strategy shift. The distributive property understanding from M6 continues to support all subsequent multiplication modules. |

### OUR Lesson Sources

| OUR Lesson | Scope | Transformation |
| :---- | :---- | :---- |
| L10 | Gridded area model decomposition — strategies based on properties of multiplication | Combined with L11 into single module. Confirmed per SME: "totally doable" because students know area and decomposition from Unit 2. What's NEW: connecting expressions to diagrams. |
| L11 | Ungridded/open area models — associative and distributive properties applied to products within 100 | Late section of combined module. Progressive formalization: same strategies on rectangles without grid support. |

---

## 1.2 SCOPE BOUNDARIES

**[REQUIRED]**

### ✅ Must Teach

* Area model decomposition: partitioning a rectangle into two sub-rectangles creates two simpler multiplication problems
* "Breaking apart" as the primary strategy language — students learn to decompose one factor into convenient parts
* Partial-product expressions with parentheses: (5 × 10) + (5 × 3) = 65 — explicit visual-to-notation connection
* Parentheses introduced: "These curved lines, called parentheses, are like a box around each part" — descriptive grouping, NOT order of operations
* Guided decomposition at benchmark numbers (2, 5, or 10) in Early activities
* Student-chosen decomposition in Mid activities — multiple valid partitions for the same rectangle, all producing the same product
* Progressive formalization: gridded rectangles (count to verify) → ungridded rectangles (dimension labels only, no counting fallback)
* Strategic choice: "Where would YOU choose to break apart this rectangle? Why?" — different decomposition points are valid strategy choices, not errors
* Both sub-rectangles visible simultaneously — this IS the U4.6 prevention design
* Expression-to-diagram connection as the new emphasis vs. Unit 2 (Unit 2 = measuring area; Unit 4 = multiplication strategy)
* Vocabulary: decompose, area model (as strategy — reinforced from Unit 2 as measurement), partial products (informal: "the parts"), breaking apart
* Notation convention: parentheses — introduced as "a box around each part," descriptive grouping only
* Reinforced vocabulary: area, square units, multiply, factor, product, expression, equation

### ❌ Must Not Include

* "Distributive property" or "associative property" as named terms (D5 — properties used but not named at this grade level)
* Order of operations or formal precedence rules (parentheses are descriptive grouping only)
* Multiples of 10 as a specific strategy (M7 — different approach using place value)
* Division decomposition or reverse operations (not in scope)
* Decomposition of both factors simultaneously in a single problem (one factor decomposed per problem — author-inferred cognitive load constraint for Grade 3; TVP examples consistently show single-factor decomposition only)
* Free-form partition choices during Late Lesson (constrained to benchmark numbers — 2, 5, or 10 — per AF3 resolution; fully open in Practice only)
* Think-multiplication strategy assessment (M12)
* Two-step word problems (M10+)
* New unknown representations (all three already introduced by M4)

### Scope Confirmation Checklist

- [x] Concepts IN scope: area model decomposition (gridded → ungridded), partial-product expressions, strategic decomposition choice, expression-to-diagram connection
- [x] Concepts deferred: formal property naming (D5), multiples of 10 (M7), division decomposition, two-step problems (M10+)
- [x] Vocabulary introduced: decompose, area model (as strategy), partial products / "the parts", breaking apart, parentheses
- [x] Vocabulary reinforced: area, square units, multiply, factor, product, expression, equation (precision note: "expression" = the left side without =; "equation" = full statement with =. Guide dialogue should use terms precisely per P-4)
- [x] Vocabulary forbidden: distributive property, associative property, "add a zero"
- [x] Value constraints: one single-digit factor (2-9), second factor single-digit or up to 14 (Late), products within 100
- [x] L10 + L11 = sole lesson sources, combined per SME
- [x] Scope boundaries: M5 covers commutativity/table patterns; M6 covers area models/decomposition; M7 covers multiples of 10

---

## 1.3 VOCABULARY ARCHITECTURE

**[REQUIRED]**

**Assessment Vocabulary (appears on state test):** area model, decompose, partial products (per 3.MD.C.7c required vocabulary)

### Vocabulary Staging by Phase

| Phase | Terms | Introduction Approach |
| :---- | :---- | :---- |
| **Warmup** | area, square units, rectangle, multiply, factor, product (all established from Unit 2 / M1–M5) | Activation only — no formal introduction. All terms established in prior modules/units. Grid Rectangles tool reactivates Unit 2 vocabulary naturally. |
| **Lesson S1 (Early)** | [vocab]breaking apart[/vocab] (NEW — strategy name), parentheses (notation convention — introduced but not formal vocabulary), [vocab]decompose[/vocab] (NEW — mathematical synonym for breaking apart) | "Breaking apart" introduced as the strategy name during first guided decomposition. "Parentheses" introduced via explicit visual-to-notation unpacking: "These curved lines, called parentheses, are like a box around each part" — this is a notation convention, not a vocabulary term requiring `[vocab]` tags. "Decompose" introduced as the mathematical word for "breaking apart" — after students have used the strategy. All follow vocab-after-grounding rule. |
| **Lesson S2 (Mid)** | [vocab]partial products[/vocab] (NEW — informal: "the parts") | Introduced after students experience multiple decompositions producing the same total. "Each part you multiplied is called a partial product — a part of the whole product. We've been calling them 'the parts.'" |
| **Lesson S3 (Late)** | [vocab]area model[/vocab] (STATUS CHANGE — from Unit 2 measurement meaning to Unit 4 strategy meaning) | "Area model" was a measurement tool in Unit 2. Now it's a multiplication strategy tool. The status change happens when the grid is removed: "This rectangle without the grid is called an open area model. You know the dimensions — you don't need to count every square." |
| **EC** | (all terms — assessment context) | Students use decomposition vocabulary to write expressions and explain strategy choices. |
| **Practice** | (all terms) | Used in problem contexts with fully open decomposition choices. |
| **Synthesis** | (all terms — consolidation) | Strategy summary. Bridge to M7 uses "breaking apart" to contrast with upcoming place value approach. |

### Vocabulary Reinforcement Plan (NEW/status-change terms only)

| Term | Introduction Interaction | Reinforcement Target (≥50% of remaining) |
| :---- | :---- | :---- |
| breaking apart | S1 Early (~Interaction 1.1–1.2) | Guide dialogue in S1, S2, S3, EC, Synthesis |
| decompose | S1 Early (~Interaction 1.3) | Guide dialogue in S2, S3, EC, Synthesis |
| partial products | S2 Mid (~Interaction 2.2) | Guide dialogue in S2, S3, EC, Synthesis |
| area model (as strategy) | S3 Late (~Interaction 3.1) | EC, Synthesis |

> **Vocab Tag Policy (v4.7):** Only the 4 terms above get `[vocab]` markup as NEW or STATUS-CHANGE terms. "Parentheses" is a notation convention introduced in Guide dialogue but does not receive `[vocab]` tags — it's not a mathematical concept term. All other terms (area, square units, rectangle, multiply, factor, product, expression, equation, array, multiplication table, row, column, pattern, commutative) are ESTABLISHED from prior modules/units and appear untagged.

### Terms to Avoid (Save for Later Modules)

* distributive property (D5 — used but not named; students say "breaking apart")
* associative property (D5 — implicit in some decompositions; not named)
* "add a zero" (NEVER — per D6)

---

## 1.4 MISCONCEPTIONS

**[REQUIRED]**

### 1.4.1 U4.6: Distributive Property Applied Incorrectly (PRIMARY)

**Trigger Behavior:** When decomposing 7 × 14, student writes 7 × 10 + 4 (multiplies only the first part, adds the second part raw). Or computes partial products correctly but adds wrong: 7 × 10 + 7 × 4 = 70 + 28 = 88 (addition error under cognitive load). On area models, may label one sub-rectangle correctly but forget dimensions on the other.

**Why It Happens:** "Breaking apart" creates two simultaneous cognitive demands: (1) remembering that BOTH parts need to be multiplied by the same factor, and (2) holding two partial products in working memory for addition. The most common error is (1) — students decompose the factor and then treat the second piece as already-multiplied. This is a "losing track" error under cognitive load, not a conceptual misunderstanding of area.

**Visual Cue:** The area model directly prevents this error when both sub-rectangles are visible simultaneously. Each sub-rectangle clearly has two dimensions — students can SEE that both parts require their own multiplication. The error primarily occurs when students work symbolically without the visual support (i.e., on ungridded models or when rushing through expressions).

**Prevention Strategy:** Both sub-rectangles are on screen simultaneously throughout Early and Mid activities — the visual makes "forgetting to multiply both parts" impossible because both pieces are right there with labeled dimensions. When transitioning to ungridded models in Late, the Guide explicitly draws attention to both sub-rectangle dimensions before expression writing. The Equation Builder shows the full partial-product expression (5 × 10) + (5 × 3) with the common factor (5) visible in both terms. Error-pattern monitoring in Practice: flag any expression where only one term contains two factors (e.g., "7 × 10 + 4" instead of "7 × 10 + 7 × 4").

---

### 1.4.2 A2: Equals Sign Treated as "Do Something" (SECONDARY — Monitoring)

**Trigger Behavior:** Student hesitates at or rejects partial-product expressions in nonstandard format (e.g., 42 = (5 × 6) + (2 × 6)). May insist "the answer should be on the right."

**Why It Happens:** Relational equals sign understanding (A2) is an ongoing concern across the unit (global misconception ID from misconceptions database — applies to all modules involving equation notation). Partial-product expressions introduce a new format challenge specific to M6: the product is the SUM of two sub-products, written with parentheses. Nonstandard presentation (e.g., 42 = (5 × 6) + (2 × 6), product on left) can trigger A2 for students with operational equals-sign understanding who expect "answer on the right."

**Prevention Strategy:** Per D8 (presentation pattern), nonstandard equation formats are woven throughout. At least 30% of partial-product expressions presented in nonstandard format (product on left). The Guide models reading these naturally: "42 equals 5 times 6 plus 2 times 6." No standalone true/false activities — exposure-based normalization.

---

## 1.5 TOY SPECIFICATIONS

**[REQUIRED]**

### 1.5.1 Grid Rectangles (Primary)

**Notion Spec:** [Grid Rectangles](https://www.notion.so/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca)

**Changes from Unit 2:** In Unit 2, Grid Rectangles were used for area measurement — counting squares, labeling dimensions, computing area. In M6, the SAME tool returns in a new role: the area model as a multiplication STRATEGY. New capabilities needed for M6: partition line (system-placed in Early, student-placed in Mid), sub-rectangle color coding, dimension labels on sub-rectangles, and ungridded mode (outline + dimensions only, no grid squares).

**Engineering Note (AF2 — Resolved):** Grid Rectangles were mocked up and shown alongside the Multiplication Tables Grid in Unit 2. The gridded rectangle display is an existing capability. Student-placed partition lines and sub-rectangle display may still require engineering confirmation for the interactive (student-placed) mode — the Unit 2 implementation shows system-controlled decomposition. Flag for engineering: confirm student-initiated partition placement is feasible on the existing Grid Rectangles component.

### Module Configuration (M6)

| Property | Value |
| :---- | :---- |
| **Display Modes** | Gridded (full grid with squares visible), Ungridded (outline + dimension labels only) |
| **Partition Line** | System-placed (Early), Student-placed (Mid), Student-placed (Late) |
| **Sub-Rectangle Display** | Color-coded (two distinct colors), dimension labels on both sub-rectangles |
| **Dimension Labels** | Always visible: row count and column count on each sub-rectangle |
| **Grid Squares** | Visible in gridded mode (countable), absent in ungridded mode |
| **Orientation** | Rows × Columns (consistent with array convention from M1–M5) |

### M6 Guardrails

* Both sub-rectangles must be visible simultaneously at all times after partition — never show one sub-rectangle without the other
* Dimension labels must appear on BOTH sub-rectangles after partition (not just the original rectangle dimensions)
* In ungridded mode, no grid lines or individual squares visible — only the outline and dimension labels
* The partition line must be perpendicular to one dimension (horizontal OR vertical split, not diagonal)
* Color coding must be perceptually distinct (not red/green — accessibility)

### Progression Within M6

| Phase | Grid State | Partition Control | Verification |
| :---- | :---- | :---- | :---- |
| Warmup | Gridded (display) | Guide-drawn (demonstration) | Guide narrates count |
| Early (S1) | Gridded | System-placed | Student can count squares to verify |
| Mid (S2) | Gridded | Student-placed | Student counts to verify |
| Late (S3) | Ungridded | Student-placed (benchmark 2, 5, or 10 only) | Must compute from dimensions (no counting) |
| EC | Both gridded (EC.1) and ungridded (EC.2, EC.3) | Shown (EC.1), Student-placed (EC.2, EC.3) | Varies by problem |

### 1.5.2 Equation Builder (Primary)

**Notion Spec:** [Equation Builder](https://www.notion.so/Equation-Builder-2fc5917eac52803f8604f47c62304ee7)

**Changes from M5:** M5 used Equation Builder for equation construction (fact families). M6 uses it for partial-product expression construction, a new format with parentheses, displayed simultaneously alongside Grid Rectangles. Students build expressions using tiles: factor tiles, operation tiles (×, +), parentheses tiles, = tile, and product tiles.

### Module Configuration (M6) — Equation Builder

| Property | Value |
| :---- | :---- |
| **Mode** | Interactive — expression construction (Early: guided; Mid/Late: independent) |
| **Tile Set** | Number tiles (0–9, composable for multi-digit), ×, +, (, ), = |
| **Expression Format** | Partial-product: (a × b) + (a × c) = product |
| **Nonstandard Formats** | ≥30% of expressions in nonstandard format per D8 (e.g., 42 = (5 × 6) + (2 × 6)) |
| **Display alongside** | Grid Rectangles — Equation Builder visible simultaneously with area model |
| **Unknown symbols** | ? and □ interchangeable in Practice per D7 — not primary in Lesson |

### M6 Guardrails — Equation Builder

* Equation Builder always visible alongside Grid Rectangles — the expression-to-diagram connection is the core pedagogical move
* Parentheses required around each partial product in the expression
* Partial-product expression must match the sub-rectangle decomposition shown in Grid Rectangles (system validates correspondence)
* No order-of-operations instruction — parentheses are descriptive grouping only

### 1.5.3 Multiplication Tables Grid (Secondary — Synthesis Only)

**Notion Spec:** [Multiplication Tables Grid](https://www.notion.so/Multiplication-Tables-Grid-1395917eac52801da8e3d35eb2e6ca3e)

**Changes from M5:** M5 used the Multiplication Tables Grid as a primary tool for commutativity discovery. In M6, it appears in a single Synthesis connection task — display-only, showing how the multiplication table IS a gridded area model from the upper left corner. Per AF1 resolution: this beat is placed in Synthesis as a connection task, not in the Lesson.

**Unit 2 precedent:** Grid Rectangles were shown alongside the Multiplication Tables Grid in Unit 2 (see app screenshot — the table displays as a gridded rectangle with row/column headers). This existing visual capability supports the table-as-area-model connection without new engineering work.

### 1.5.4 Data Constraints by Section

| Phase | Factor 1 | Factor 2 | Product Range | Decomposition Constraint | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Warmup** | 2–4 | 4–12 | 8–48 | Guide-demonstrated | 3×12 chosen for benchmark-10 foreshadowing (DN-2); second factor extended to accommodate natural benchmark-10 partition |
| **Early (S1)** | 2–4 | 5–12 | 10–48 | At benchmark (2, 5, or 10) | Gridded; first factor kept small (2–4) per TVP for visual clarity |
| **Mid (S2)** | 2–5 | 5–12 | 10–60 | Student choice (any valid point) | Gridded; grid visible for verification; first factor ≤5 keeps grid countable |
| **Late (S3)** | 2–9 | 7–14 | 14–100 | Benchmark numbers only (2, 5, or 10) | Ungridded; products ≤ 100; constrained per AF3 resolution |
| **EC** | 2–9 | 5–14 | 10–100 | EC.1 shown; EC.2-3 student choice (benchmark) | Mixed gridded/ungridded; fresh values |
| **Practice** | 2–9 | 5–14 | 10–100 | BASELINE: ~50% offer suggested partition points (2, 5, 10); ~50% fully open. Above-baseline: all fully open. | Full range; student strategic choice |

**Problem count per phase (from TVP):** Early 3–4 interactions, Mid 3–4 interactions, Late 3–4 interactions, EC 3 problems, Practice variable per tier (Baseline ~50% with suggested partitions; Stretch fully open).

**Cross-phase constraints:**
* All products within 100
* Gridded rectangles: first factor kept small (2–4 in Early, ≤5 in Mid) for visual clarity; second factor may extend to low double digits (e.g., 3 × 12)
* Per SME: do NOT artificially cap second factor at ≤ 10 for gridded — gridded rectangles with larger second dimension are valuable for showing decomposition at benchmark 10
* Avoid decompositions that create sub-problems harder than the original
* Sub-problems from benchmark decomposition should use facts students are fluent with (from Units 1–2)
* **Benchmark partition rationale (AF3):** 2, 5, and 10 are the benchmark options. With factors up to 14, "break at 10" works for 11–14 but not 7–9. "Break at 5" works for most single-digit factors. "Break at 2" provides a third option for smaller factors where 5 and 10 aren't natural (e.g., 7 × 6 → break 6 at 2: (7 × 4) + (7 × 2)). The three benchmarks together ensure students always have a genuine choice, not a forced "the only option is 5." Per SME Andrea: "5s and 10s are great go-to breaks" but 2s needed as additional option given factor ranges.

### Interaction Constraints (All Toys)

* Grid Rectangles and Equation Builder visible simultaneously for all decomposition interactions
* Visual: lines follow format — Toy Name (Mode). Orientation. Data. Scaffold state. Interaction type. Visibility flags.
* Partition line always perpendicular to one dimension
* Sub-rectangle dimension labels always shown after partition
* Partial-product expressions always use parentheses around each term
* Equation Builder tiles are the primary response mechanism for expression writing (not free-text entry)

---

## 1.6 WARMUP

**[REQUIRED]**

### Core Purpose

**Purpose:** Reactivate the area model from Unit 2 and reframe it as a multiplication STRATEGY — demonstrating that partitioning a rectangle into parts turns one hard multiplication into two easier ones.

**Key Function:** Students last used Grid Rectangles for area measurement in Unit 2. The Warmup must explicitly bridge from "counting square units" to "breaking apart to make multiplication easier." The Guide demonstrates a single partition on a familiar gridded rectangle, shows both partial products, and adds them — revealing that breaking apart WORKS. This positions S1 to have students write the matching expression and discover WHY it works (both parts are visible in the area model).

**Why this serves the concept:**

* Reframes a familiar tool (Grid Rectangles) in a new role — from measurement to strategy — which is the module's core cognitive move
* Demonstrates the "breaking apart" procedure ONCE with full narration so students see the end-to-end process before they try it
* Creates the driving question for the Lesson: "Can we use this trick to make ANY hard multiplication easier?"

**Test:** If we removed this Warmup, would students lose mathematical preparation for the Lesson? YES — students would enter S1 without (1) reactivation of the Grid Rectangles tool from Unit 2, (2) the critical reframing from "area measurement" to "multiplication strategy," and (3) the visible demonstration that partitioning creates two easier problems whose products sum to the original.

### Parameters

| Parameter | Value |
| :---- | :---- |
| **Time** | ~2–3 minutes |
| **Interactions** | 3 (1 activation, 1 with student action, 1 bridge) |
| **Warmup Type** | Activation (Unit 2 Callback + Strategic Reframing) |
| **Cognitive Load** | 20–30% — familiar tool, familiar values, one new idea (breaking apart) shown by Guide |
| **Remediation** | Pipeline (light) |
| **Vocabulary** | NEW terms: forbidden. ESTABLISHED terms activated: area, rectangle, multiply, factor, product, square units. No `[vocab]` tags in Warmup — all terms are established. |
| **Visual States** | 2 max: [DISPLAY] gridded rectangle, [MODIFY] partition line + sub-rectangle highlighting |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Explicitly reframe Grid Rectangles: "You measured area with these. Now we're using the SAME rectangles as a trick for multiplication." (PE-03 non-negotiable) | Introduce "breaking apart," "decompose," "partial products," or any NEW vocabulary |
| Use familiar Unit 2 values (3 × 12, benchmark-10 partition) per Data Constraints | Teach the expression-to-diagram connection (that's S1's job) |
| Show ONE complete partition demonstration — Guide narrates the entire process | Have students place a partition line (that's S2's job) |
| Create anticipation: "What if we could do this with HARDER numbers?" | Explain WHY partial products sum to the original (that's the module's Big Insight) |
| Use session-relative language ("last time" / "this time") | Use temporal language ("yesterday" / "today") |
| Include 2+ engagement anchors from approved list | Exceed 2 visual states |

> **Warmup Type Rationale:** Activation (Unit 2 Callback + Strategic Reframing) is the right type because M6 repurposes a familiar tool (Grid Rectangles from Unit 2) for a new role (multiplication strategy). The warmup's job is retrieval (reactivate the grid) + reframing (same tool, different purpose) + demonstration (one example of breaking apart). Binary Choice or WODB would work for comparing partitions, but students haven't done ANY partitioning as strategy yet — they need to SEE one demonstration before they could make meaningful choices. Activation with strategic reframing positions S1 to build on a demonstration rather than starting cold.

> **Design Note — Cross-module hook differentiation (Pattern #40):** M5's warmup opened with "Remember this fact family?" (M4 callback via Equation Builder display). M6's warmup opens with a different frame: starting from the Grid Rectangles tool itself, reframing its purpose from Unit 2 measurement to Unit 4 strategy. The hook is about SEEING A FAMILIAR TOOL IN A NEW ROLE, not recalling a prior pattern. Different tool, different cognitive move, different framing.

---

### Interaction W.1: The Grid Returns [ACTIVATION]

* **Purpose:** Reactivate Grid Rectangles from Unit 2. Student identifies the total area of a familiar gridded rectangle — grounding in known territory before any new content.
* **Visual:** Grid Rectangles (gridded, display). 3 × 12 rectangle with full grid visible.
* **Guide:** "Look what's back: the rectangle grid from when you measured area. Here's a 3-by-12 rectangle. You know how to figure out the area: 3 rows of 12. But here's the thing: 3 × 12 might take a moment to figure out. What if there's a way to make it easier? First, though, how many squares are in this rectangle? You can count or multiply."
* **Prompt:** "How many squares are in the 3 × 12 rectangle?"
* **Student Action:** Select (single)
  * **Options:**
  A. 36
  B. 30
  C. 15
  D. 24
* **Correct Answer:** A (36)
* **Answer Rationale:**
  - A (36): Correct — 3 × 12 = 36 square units
  - B (30): 3 × 10 — may have computed partial product without finishing
  - C (15): 3 + 12 — added instead of multiplied
  - D (24): 2 × 12 — miscounted rows
* **On Correct:** "36 squares. 3 rows of 12."
* **Remediation:** Pipeline

> **Design Note — Engagement Anchors:** Anchor 1 (Personalization): "the rectangle grid from when you measured area" — callbacks to student's own Unit 2 experience. Anchor 2 (Choice/Agency): "You can count or multiply" — student chooses their approach to finding the total.

> **Scaffolding Note:** 3 × 12 is chosen because (a) first factor 2–4 per Early data constraints for grid clarity, (b) second factor 12 allows a natural benchmark-10 partition, (c) product 36 is within fluent facts range, and (d) 3 × 12 is NOT an M5 reused value (fresh for M6). Distractor B (30 = 3 × 10) foreshadows the partial product that will appear in the demonstration.

---

### Interaction W.2: Breaking It Apart [DEMONSTRATION — No Student Action]

* **Purpose:** Guide demonstrates a single partition of the 3 × 12 rectangle at benchmark 10, computing both partial products and adding them. This is the module's core idea shown ONCE — students watch, then the Lesson has them do it.
* **Visual:** Grid Rectangles (gridded, display → modify). Same 3 × 12 rectangle. [MODIFY] Guide draws partition line at column 10, splitting into 3 × 10 (left, color A) and 3 × 2 (right, color B). Both sub-rectangles labeled with dimensions. Sub-rectangle areas visible.
* **Guide:** "Watch this. A line splits the rectangle into two parts. Now there's a 3-by-10 piece and a 3-by-2 piece. The 3-by-10 part is 30 squares. The 3-by-2 part is 6 squares. 30 plus 6 is... 36. Same area! But instead of figuring out 3 × 12 all at once, it turned into 3 × 10 and 3 × 2. Two easier problems."
* **No student action.**

> **Design Note — Strategic Reframing (PE-03):** This interaction is the non-negotiable reframing moment. The Guide explicitly bridges from "measuring area" to "making multiplication easier" by narrating the partition, the partial products, and the sum. The key phrase "two easier problems" is the conceptual hook for the entire module. No formal vocabulary is introduced — "breaking apart," "decompose," and "partial products" are all saved for S1.

> **Voice Note:** Tone is medium-high energy (Warmup), conversational, genuinely interested in showing the trick. "Watch this" is an informal attention-getter — not instructional. The narration moves briskly: partition → two parts → compute each → add → same total. No pausing for reflection — this is activation, not teaching.

---

### Interaction W.3: The Bridge [ANTICIPATION — No Student Action]

* **Purpose:** Create anticipation for the Lesson without teaching. The question "Can we use this trick with HARDER numbers?" sets up S1's guided decomposition work.
* **Visual:** Grid Rectangles (gridded, display). Same 3 × 12 rectangle still showing the partition from W.2. Both sub-rectangles and their products visible.
* **Guide:** "I turned one hard problem into two easy ones, and got the same answer. Last time, we said area models could help with bigger multiplication. Now you've seen how. What about even harder ones, like 7 × 13? Let's find out."
* **No student action.**

> **Bridge Note:** The bridge acknowledges M5's "area models" preview ("Last time, we said area models could help") before pushing forward with the new question ("What about even harder ones, like 7 × 13?"). This resolves the M5→M6 bridge asymmetry (XB1.1): M5's Identity Closure explicitly names "area models," so M6's bridge honors that preview rather than reopening discovery framing. The actual discovery in M6 is HOW breaking apart works as a strategy, not THAT area models exist. The specific mention of "7 × 13" previews the kind of Late-section values students will encounter, creating curiosity without intimidation.

---

### Warmup Verification Checklist

**Structure:**

- [x] Hook appears in first 15–20 seconds (W.1: "Look what's back — the rectangle grid")
- [x] 2+ engagement anchors from approved list (Personalization: Unit 2 callback; Choice/Agency: "count or multiply")
- [x] 2+ meaningful visual interactions (W.1: student identifies area; W.2: Guide demonstrates partition)
- [x] 1+ judgment/noticing task requiring thought (W.1: identify total area of 3 × 12)
- [x] Zero formal vocabulary introduced (no "breaking apart," "decompose," "partial products," or "parentheses")
- [x] Maximum 2 visual states used ([DISPLAY] rectangle, [MODIFY] partition + highlights)
- [x] Clear bridge to Lesson at end (W.3: "What about even harder ones, like 7 × 13?")
- [x] Total time stays under 5 minutes (~2–3 min)
- [x] Cognitive load feels light (20–30%) — familiar tool, familiar operation, Guide does the new work
- [x] Strategic reframing explicitly present (PE-03: "You measured area... now we're using the SAME rectangles as a trick")
- [x] Cross-module hook differentiation verified (Pattern #40: M5 = "Remember this fact family?"; M6 = "Look what's back — the rectangle grid" — different tool, different frame)

**Boundary Checks:**

- [x] No teaching of new content (partition demonstration is SHOWING, not explaining WHY it works)
- [x] No vocabulary front-loading (informal language only: "two parts," "two easier problems")
- [x] No multi-step instructions (W.1 is one action; W.2 and W.3 have no student action)
- [x] Warmup bridge creates anticipation without teaching

---

## 1.7 LESSON

**[REQUIRED]**

### Lesson Requirements Checklist

- [ ] CRA sequence: Representational (S1 gridded) → Relational (S2 comparing decompositions) → Abstract (S3 ungridded) — with D4 simultaneous Equation Builder throughout
- [ ] Worked examples: Full → Partial → Independent fading (1.1 full, 1.2 partial, 1.3 independent)
- [ ] Think-aloud: 1–2 with tagged elements ([PLANNING], [ATTENTION], [SELF-CHECK])
- [ ] Example-problem pair structure in S1
- [ ] Vocabulary staging matches §1.3 exactly: "breaking apart" + "decompose" in S1, "partial products" in S2, "area model" status-change in S3
- [ ] Purpose Frame present at Lesson opening
- [ ] Required Phrases section present
- [ ] Forbidden Phrases section present with ❌ prefix
- [ ] Misconception Prevention section present
- [ ] Guide/Prompt independence verified on 3+ interactions
- [ ] Section transition markers between S1, S2, S3
- [ ] Every interaction has a type label
- [ ] All interactions use toys/modes documented in §1.5
- [ ] Dimension Tracking updated in Working Notes

### Core Purpose

**Purpose:** Teach the "breaking apart" strategy using area models — from guided decomposition on gridded rectangles (S1) through student-chosen decomposition with multiple valid solutions (S2) to ungridded rectangles where counting is impossible (S3). The Equation Builder appears alongside the area model from the start (D4), making the expression-to-diagram connection explicit.

### Pedagogical Flow

| CRA Phase | Module Implementation | Key Pedagogical Move |
| :---- | :---- | :---- |
| **Representational (S1)** | Gridded area model with system-placed partition + Equation Builder | Guide demonstrates expression-to-diagram connection with parentheses; student replicates |
| **Relational (S2)** | Multiple decompositions of same gridded rectangle, sequential reveal | Student discovers: different partitions → same product. "Partial products" named after experience. |
| **Abstract (S3)** | Ungridded rectangle (outline + dimensions only) + Equation Builder | No counting fallback — student must compute from dimensions. "Area model" reframed as strategy. |

### Lesson Structure

| Section | Focus | Time | Interactions |
| :---- | :---- | :---- | :---- |
| **Purpose Frame** | Orient students: what they'll learn and why | ~15 sec | 0 (Guide only) |
| **S1 — Early (Guided Decomposition)** | Expression-to-diagram connection, parentheses introduction, benchmark decomposition | ~3–4 min | 3 (1 worked example + 1 partial + 1 independent) |
| **S2 — Mid (Student-Chosen Decomposition)** | Multiple valid decompositions → same product, "partial products" vocabulary | ~3–4 min | 4 (student choice + relational reveal + comparison + independent) |
| **S3 — Late (Ungridded Area Models)** | Progressive formalization, no counting fallback, "area model" as strategy | ~3–4 min | 3 (1 guided transition + 2 independent) |
| **Bridge to EC** | Transition to assessment | ~15 sec | 0 (Guide only) |

### Required Phrases

These vocabulary words and key phrases MUST appear in script:

* "breaking apart" — introduced in S1, used throughout (S1, S2, S3, EC bridge)
* "decompose" — introduced in S1 as mathematical synonym, reinforced in S2, S3
* "partial products" / "the parts" — introduced in S2 after experiencing multiple decompositions
* "area model" — status-change in S3 from "measurement tool" to "strategy tool"
* "parentheses" — notation convention, introduced in S1 via visual unpacking ("like a box around each part")
* Assessment language stems: "break [factor] into...", "write the expression that matches...", "where would YOU choose to break apart...?"

### Forbidden Phrases

* ❌ "distributive property" — D5 HARD CONSTRAINT. Students experience the property; they never name it. Use "breaking apart" instead.
* ❌ "associative property" — D5. Implicit in some decompositions; never named.
* ❌ "order of operations" — parentheses are descriptive grouping only, NOT precedence rules.
* ❌ "add a zero" — D6, NEVER. Not in M6 scope (that's M7).
* ❌ "your friend" — DN-1. Inauthentic in 1:1 app context. Use "another student might do it this way" or sequential reveal.
* ❌ "Let me show you the answer" — discovery language. Guide shows strategy, student discovers it works.
* ❌ "This is called the distributive property but we won't use that name" — meta-commentary about omitted terms is worse than omission.

### Misconception Prevention

**U4.6 (PRIMARY) — Distributive property applied incorrectly:**

Prevention is embedded in the toy design and interaction structure:
* Both sub-rectangles visible simultaneously after every partition (§1.5.1 Guardrail) — prevents "forgetting to multiply both parts" because both pieces are on screen with labeled dimensions
* Equation Builder shows the full partial-product expression (a × b) + (a × c) with the common factor visible in both terms — makes the error pattern (e.g., "7 × 10 + 4" instead of "7 × 10 + 7 × 4") visually apparent
* S1 Interaction 1.1 (worked example) explicitly narrates BOTH parts: "THIS part is [factor] × [part]. THAT part is [factor] × [other part]."
* **MC distractor design (DN-7):** When expression-matching appears, include distractors missing the common factor in one term (diagnostic of the core error)

**A2 (SECONDARY — Monitoring) — Equals sign as "do something":**

Prevention via normalization:
* Per D8, ≥30% of partial-product expressions in nonstandard format (product on left)
* Guide models reading nonstandard format naturally: "36 equals 3 times 10 plus 3 times 2"
* No explicit discussion of equals-sign meaning — exposure-based normalization only

---

### Purpose Frame [No Student Action]

* **Purpose:** Orient students to what they'll learn (breaking apart rectangles to make multiplication easier) and why it's useful (works for numbers that are hard to multiply in your head).
* **Visual:** Grid Rectangles (gridded, display). Fresh rectangle — not the Warmup rectangle. Clear screen.
* **Guide:** "You just saw how splitting a rectangle into two parts turned one hard multiplication into two easy ones. Now you're going to learn how to do that yourself, and you'll discover that it works every time, no matter where you choose to break. Ready?"
* **No student action.**

> **Design Note — Purpose Frame vs Warmup Bridge:** The bridge acknowledged M5's "area models" preview and asked "What about even harder ones, like 7 × 13?" (curiosity). The Purpose Frame answers: "You're going to learn how to do that yourself" (orientation). Bridge = emotional; Purpose Frame = cognitive. No overlap.

---

### SECTION 1: GUIDED DECOMPOSITION ON GRIDDED AREA MODELS (Early)

**CRA Stage:** Representational (gridded — students can count squares to verify)
**Scaffolding Level:** Full → Partial → Independent (fading across 3 interactions)
**Toys:** Grid Rectangles (gridded, system-placed partition) + Equation Builder (interactive)

---

### Interaction 1.1: Watch How I Think About This [WORKED EXAMPLE — Type A]

* **Purpose:** Full worked example — Guide demonstrates the complete decomposition-to-expression process with think-aloud. Student observes. Introduces "breaking apart" and parentheses notation.
* **Visual:** Grid Rectangles (gridded, system-placed partition). 4 × 7 rectangle. System places partition at column 5: left sub-rectangle 4 × 5 (color A), right sub-rectangle 4 × 2 (color B). Dimensions labeled on both sub-rectangles. Equation Builder (display — Guide demonstrates expression construction). Expression builds on screen as Guide narrates; student observes. Interactive mode begins in 1.2.
* **Guide:** "Let me show you how I think about this. Here's a 4-by-7 rectangle. 4 × 7... I'd have to think about that. But look: I've split it into two parts. [PLANNING] First, I ask myself: what are my two easier problems? [ATTENTION] I look at the left part. 4 rows of 5. That's 4 × 5, which is 20. Easy. [ATTENTION] Now the right part. 4 rows of 2. That's 4 × 2, which is 8. Also easy. [ACTION] 20 plus 8 is 28. So 4 × 7 equals 28. I just [vocab]broke apart[/vocab] the 7 into 5 and 2, and solved two easier problems instead of one harder one. [SELF-CHECK] And look: I can count the squares to check. 28. Same answer. Now I'll write it as math. These curved lines are called parentheses. They're like a box around each part. (4 × 5) plus (4 × 2) equals 28."
* **No student action.** (Type A — teaching only)

> **Scaffolding Note:** This is a FULL worked example. Guide does everything: identifies sub-rectangles, computes both partial products, adds them, introduces the notation. Student's job is to watch and listen. The next interaction (1.2) will have the student write the expression for a similar problem.

> **Voice Note:** Think-aloud tags ([PLANNING], [ATTENTION], [SELF-CHECK]) are authoring annotations — strip before Notion publish. The dialogue reads as natural speech without them.

> **Vocabulary Note:** "Breaking apart" / [vocab]broke apart[/vocab] is the first NEW term introduction, per §1.3 staging. "Parentheses" introduced as notation convention (no [vocab] tag per policy). "Decompose" will be introduced in 1.2 as mathematical synonym.

---

### Interaction 1.2: Your Turn — Write the Expression [GUIDED PRACTICE — Type C]

* **Purpose:** Partial worked example — system places the partition, Guide identifies the sub-rectangles, but student writes the matching expression in Equation Builder. Introduces "decompose" as synonym for "breaking apart."
* **Visual:** Grid Rectangles (gridded, system-placed partition). 3 × 8 rectangle. System places partition at column 5: left 3 × 5 (color A), right 3 × 3 (color B). Dimensions labeled. Equation Builder (interactive) — empty, ready for student input.
* **Guide:** "Here's a 3-by-8 rectangle, already split into two parts. The left part is 3 × 5 and the right part is 3 × 3. Mathematicians call this [vocab]decomposing[/vocab]. It means breaking apart a number into smaller pieces. You just saw me write the expression with parentheses. Now you try: build the expression that matches these two parts."
* **Prompt:** "Use the tiles to build the partial-product expression: (3 × 5) + (3 × 3) = ?"
* **Student Action:** Drag to build — Equation Builder tile manipulation
* **Correct Answer:** (3 × 5) + (3 × 3) = 24
* **On Correct:** "You decomposed 8 into 5 and 3. 15 plus 9 is 24."
* **Remediation:** Pipeline

> **Scaffolding Note:** PARTIAL worked example — system provides the partition and sub-rectangle identification, student writes the expression. This is the middle step in the fading sequence (Full → Partial → Independent). The Guide's dialogue includes complete instruction for independence test: "build the expression that matches these two parts."

> **Dimension Note:** 3 × 8 = 24. Partition at 5: (3 × 5) + (3 × 3) = 15 + 9 = 24. Fresh values (not reused from Warmup or M5).

---

### Interaction 1.3: Now Without the Hint [INDEPENDENT CHECK — Type B]

* **Purpose:** Independent — system places the partition, but Guide provides only brief context. Student identifies the sub-rectangle dimensions AND writes the expression.
* **Visual:** Grid Rectangles (gridded, system-placed partition). 2 × 11 rectangle. System places partition at column 10: left 2 × 10 (color A), right 2 × 1 (color B). Dimensions labeled. Equation Builder (interactive) — empty.
* **Guide:** "Here's a 2-by-11 rectangle, broken apart at 10. Build the expression."
* **Prompt:** "Build the partial-product expression for this decomposition."
* **Student Action:** Drag to build — Equation Builder tile manipulation
* **Correct Answer:** (2 × 10) + (2 × 1) = 22
* **On Correct:** "20 plus 2 is 22. The benchmark 10 made that one quick."
* **Remediation:** Pipeline

> **Scaffolding Note:** INDEPENDENT — minimal Guide context, student does the cognitive work. Still system-placed partition (student choice comes in S2). Benchmark 10 is a natural partition for 11.

> **Dimension Note:** 2 × 11 = 22. Partition at 10: (2 × 10) + (2 × 1) = 20 + 2 = 22. Smallest factor in Early range for maximum grid clarity.

→ **SECTION 1 COMPLETE. PROCEED TO SECTION 2.**

---

### SECTION 2: STUDENT-CHOSEN DECOMPOSITION (Mid)

**CRA Stage:** Relational (comparing decompositions — discovering that different partitions produce the same total)
**Scaffolding Level:** Partial → Independent (student places partition)
**Toys:** Grid Rectangles (gridded, student-placed partition) + Equation Builder (interactive)

> **Section Design Note (PE-02):** The "three decompositions, same total" discovery is the relational peak of the module. Three decompositions are shown SEQUENTIALLY with comparison prompts after each reveal, NOT simultaneously. Grade 3 working memory (5–7 items max) cannot hold three decompositions at once for meaningful comparison. See DN-4.

---

### Interaction 2.1: You Choose Where to Break [STUDENT CHOICE — Type C]

* **Purpose:** First student-placed partition. Student chooses where to decompose, writes the expression, and computes. Any valid partition point is correct.
* **Visual:** Grid Rectangles (gridded, student-placed partition). 4 × 9 rectangle. Full grid visible. Student places partition line. After placement: both sub-rectangles color-coded with dimensions labeled. Equation Builder (interactive) — empty.
* **Guide:** "Here's a 4-by-9 rectangle. This time, YOU choose where to break it apart. Where would you split the 9 to make two easier problems? Place the line, then build your expression."
* **Prompt:** "Place the partition line where you want to break apart the 9. Then build the expression and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Any valid partition. Examples: (4 × 5) + (4 × 4) = 36, (4 × 2) + (4 × 7) = 36, (4 × 4) + (4 × 5) = 36. System validates that expression matches partition placement and total = 36.
* **On Correct:** (varies by partition choice) "You broke the 9 into [a] and [b]. [4 × a] plus [4 × b] is 36."
* **Remediation:** Pipeline

> **Design Note:** This is the first time the student places the partition. The Guide's language ("where would you split it to make two easier problems?") frames this as a strategic choice, not a right/wrong answer. Any valid partition that produces a correct expression and total of 36 is accepted.

> **Dimension Note:** 4 × 9 = 36. Factor 1 within Mid range (2–5). Product within 100. Multiple valid partitions possible (at 2, 3, 4, 5, 6, 7).

---

### Interaction 2.2: Different Decomposition, Same Answer [RELATIONAL DISCOVERY — Type A]

* **Purpose:** Sequential reveal — Guide shows a DIFFERENT decomposition of the same rectangle (4 × 9) than what the student chose. Student discovers same product. [vocab]Partial products[/vocab] named.
* **Visual:** Grid Rectangles (gridded, display). Same 4 × 9 rectangle shown with a DIFFERENT partition than the student used in 2.1. E.g., if student broke at 5 (showing (4 × 5) + (4 × 4)), now show broken at 2: 4 × 2 (color A) + 4 × 7 (color B). Dimensions and products labeled on both sub-rectangles. Equation Builder displays the matching expression.
* **Guide:** "Look: here's a different way to break apart the same rectangle. This time it's split at 2: (4 × 2) plus (4 × 7). 8 plus 28 is... still 36! Look at your expression and this one. What do you notice? Both have two multiplications that add to 36. Same rectangle, different split, same answer. Each of those multiplications, the 8 and the 28, those are called [vocab]partial products[/vocab]. Partial means 'part of.' They're parts of the whole product. Which split felt easier to you: yours or this one?"
* **No student action.** (Type A — teaching + reflection prompt)

> **Design Note (DN-4, Sequential Reveal):** This is the first of the sequential reveals. The student sees their OWN decomposition from 2.1, then the Guide shows an alternative. One comparison at a time. The question "Which split felt easier?" invites metacognitive reflection without requiring a formal response — it plants the seed of strategic thinking.

> **Vocabulary Note:** "Partial products" is the third NEW term, per §1.3 staging (S2 Mid). Introduced AFTER students have experienced multiple decompositions producing the same total — the term names what they've already seen.

---

### Interaction 2.3: One More Way — Breaking the Other Factor [RELATIONAL EXTENSION — Type C]

* **Purpose:** Third decomposition shown — this time decomposing the OTHER factor (4 instead of 9). Student writes the matching expression. Cements the discovery: ANY valid decomposition produces the same total.
* **Visual:** Grid Rectangles (gridded, display → student build). Same 4 × 9 rectangle, but now partition is HORIZONTAL (splitting the 4): top 2 × 9 (color A), bottom 2 × 9 (color B). Dimensions labeled. Equation Builder (interactive) — empty.
* **Guide:** "Here's one more way. This time I broke the OTHER number. Instead of splitting the 9, I split the 4 into 2 and 2. Two groups of 9. Can you build the expression?"
* **Prompt:** "Build the expression for this decomposition: the 4 split into 2 and 2."
* **Student Action:** Drag to build — Equation Builder tile manipulation
* **Correct Answer:** (2 × 9) + (2 × 9) = 36
* **On Correct:** "18 plus 18 is 36. Two partial products, same total. Three different ways to break apart, same answer every time."
* **Remediation:** Pipeline

> **Design Note:** This third decomposition completes the "different decompositions, same total" discovery. The On Correct line explicitly names the relational pattern: "Three different ways... same answer every time." This is the module's relational insight.

> **D8 Note:** Expression (2 × 9) + (2 × 9) = 36 is in standard format. The nonstandard format (36 = (2 × 9) + (2 × 9)) will appear in later interactions per the ≥30% target.

---

### Interaction 2.4: A Bigger Rectangle — Your Strategy [INDEPENDENT — Type B]

* **Purpose:** Second independent partition choice on gridded rectangle before grid disappears. Fresh values reinforce that decomposition works on any rectangle, not just 4 × 9. Student applies strategy without Guide scaffolding.
* **Visual:** Grid Rectangles (gridded, student-placed partition). 5 × 8 rectangle. Full grid visible. Student places partition line. After placement: both sub-rectangles color-coded with dimensions labeled. Equation Builder (interactive) — empty.
* **Guide:** "New rectangle: 5 by 8. Break it apart and find the product."
* **Prompt:** "Place the partition, build the expression, and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Benchmark partition producing correct total. E.g., at 5: (5 × 5) + (5 × 3) = 40. At 2: (5 × 2) + (5 × 6) = 40. System validates benchmark constraint (2, 5, or 10) and expression-partition match.
* **On Correct:** "40. You're choosing smart places to break. That's the whole strategy."
* **Remediation:** Pipeline

> **Design Note (P-9):** Added per Gate 2 review. Without this interaction, students place their own partition only ONCE (2.1) before the grid disappears in S3. This gives a second independent practice with gridded support — a stronger base before the abstraction leap. The Guide is minimal ("Break it apart and find the product") to confirm independence. Values: 5 × 8 = 40 is solidly within Mid constraints (Factor 1 at Mid ceiling, Factor 2 within 5–12), fresh (not reused), and affords benchmarks 5 and 2. Factor 1 = 5 adds variety — all prior S2 interactions used Factor 1 = 4 or 2.

> **Dimension Note:** 5 × 8 = 40. Factor 1: 5 (Mid range 2–5, at ceiling). Factor 2: 8 (Mid range 5–12). Product within 100. Valid partitions: at 5 (5×5=25, 5×3=15), at 2 (5×2=10, 5×6=30). Benchmark 10 not available (8 < 10).

→ **SECTION 2 COMPLETE. PROCEED TO SECTION 3.**

---

### SECTION 3: UNGRIDDED/OPEN AREA MODELS (Late)

**CRA Stage:** Abstract (no counting fallback — students compute from dimensions only)
**Scaffolding Level:** Guided transition → Independent
**Toys:** Grid Rectangles (ungridded — outline + dimension labels only) + Equation Builder (interactive)

---

### Interaction 3.1: The Grid Disappears [TRANSITION — Type C]

* **Purpose:** Guide the transition from gridded to ungridded. Show the same rectangle first WITH grid, then remove the grid. Student sees that the dimensions are enough — they don't need to count.
* **Visual:** Grid Rectangles (transition display). First: 5 × 12 rectangle shown gridded with partition at 10 — both sub-rectangles visible with dimensions. Then: [MODIFY] grid fades, leaving only outline + dimension labels + partition line. Equation Builder (interactive) — empty.
* **Guide:** "You've been using the grid to count and check. But you don't really need every square, do you? Watch: same rectangle, same partition, but now the grid disappears. You've still got the numbers: 5 × 10 on this side, 5 × 2 on that side. This is called an [vocab]area model[/vocab], a rectangle you use as a strategy for multiplication, even without the grid. Build the expression."
* **Prompt:** "Build the partial-product expression for this area model."
* **Student Action:** Drag to build — Equation Builder tile manipulation
* **Correct Answer:** (5 × 10) + (5 × 2) = 60
* **On Correct:** "50 plus 10 is 60. No grid needed. The area model gives you everything."
* **Remediation:** Pipeline

> **Vocabulary Note:** "Area model" status-change happens here per §1.3 staging (S3 Late). In Unit 2 it meant "measuring area." Now it means "using a rectangle as a multiplication strategy." The Guide's language makes this explicit: "a rectangle you use as a strategy for multiplication, even without the grid."

> **Scaffolding Note:** This is a GUIDED TRANSITION — the grid-to-ungridded shift is shown explicitly with the same rectangle. Student's cognitive load is managed: familiar partition (at 10), familiar values, only the visual support changes. Subsequent interactions (3.2, 3.3) will use ungridded from the start.

> **Dimension Note:** 5 × 12 = 60. Factor 1 at boundary of Mid/Late ranges. Partition at benchmark 10. Product within 100.

---

### Interaction 3.2: Ungridded — You Choose [INDEPENDENT — Type B]

* **Purpose:** Fully independent on ungridded rectangle. Student chooses partition point (benchmark 2, 5, or 10), writes expression, computes total.
* **Visual:** Grid Rectangles (ungridded). 7 × 13 rectangle — outline only with dimension labels "7" and "13." No grid squares. Student places partition line. After placement: sub-rectangle dimensions appear. Equation Builder (interactive) — empty.
* **Guide:** "A 7-by-13 area model. No grid, just the dimensions. Stick with 2, 5, or 10. Where would you break the 13?"
* **Prompt:** "Decompose the 7 × 13 area model. Place the partition, build the expression, and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Benchmark partition producing correct total. E.g., at 10: (7 × 10) + (7 × 3) = 91. At 5: (7 × 5) + (7 × 8) = 91. System validates benchmark constraint (2, 5, or 10) and expression-partition match.
* **On Correct:** (varies by partition) "91 = (7 × 10) + (7 × 3). No grid needed." [D8: nonstandard format, product on left]
* **Remediation:** Pipeline

> **Dimension Note:** 7 × 13 = 91. Late range (Factor 1: 2–9, Factor 2: 7–14). This is a TVP example value. Benchmark 10 is the natural choice (7 × 10 = 70, 7 × 3 = 21 — both within fluent facts).

> **D8 Note — Nonstandard format:** On Correct for this interaction uses nonstandard format (product on left: "91 = ..."). Equation Builder displays the expression in nonstandard format. Combined with 3.3 (also nonstandard display), this achieves 2 of 3 Late interactions = 67% nonstandard, exceeding the ≥30% D8 target. Engineering note: Equation Builder tile arrangement defaults to product-on-left for these interactions.

---

### Interaction 3.3: One More — Benchmark Choice [INDEPENDENT — Type B]

* **Purpose:** Final independent Late interaction. Student continues independent decomposition with benchmark constraint on a fresh ungridded rectangle.
* **Visual:** Grid Rectangles (ungridded). 6 × 14 rectangle — outline only with dimension labels. Student places partition line. Equation Builder (interactive) — empty.
* **Guide:** "A 6-by-14 area model. Break it apart and find the product."
* **Prompt:** "Decompose the 6 × 14 area model. Place the partition, build the expression, and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Benchmark partition. E.g., at 10: (6 × 10) + (6 × 4) = 84. At 2: (6 × 2) + (6 × 12) = 84. System validates.
* **On Correct:** "84. Your area model turned 6 × 14 into two problems you already know." [D8: Equation Builder displays nonstandard: 84 = (6 × 10) + (6 × 4)]
* **Remediation:** Pipeline

> **Dimension Note:** 6 × 14 = 84. Late range. TVP example value. Multiple valid benchmark partitions: at 10 (most natural), at 2, at 5.

> **D8 Note:** Equation Builder displays expression in nonstandard format (product on left) for this interaction. Combined with 3.2 nonstandard On Correct, 2 of 3 Late interactions use nonstandard format (67%), exceeding ≥30% D8 target.

---

### Bridge to Exit Check [No Student Action]

* **Purpose:** Transition from Lesson to Exit Check. Signal shift from learning to demonstrating.
* **Visual:** Clear screen.
* **Guide:** "You've been breaking apart rectangles and writing expressions, on grids and without them. Let's see what you know."
* **No student action.**

---

### Lesson Verification Checklist

**CRA Structure:**

- [x] Representational phase (S1): Gridded rectangles with system-placed partition, expression-to-diagram connection (1.1, 1.2, 1.3)
- [x] Relational phase (S2): DEDICATED section — comparing decompositions, "same total" discovery (2.1, 2.2, 2.3), plus independent practice on fresh rectangle (2.4). NOT folded into vocabulary introduction.
- [x] Abstract phase (S3): Ungridded rectangles, no counting fallback (3.1, 3.2, 3.3)
- [x] D4 simultaneous connections: Equation Builder alongside Grid Rectangles in every decomposition interaction

**Worked Examples & Fading:**

- [x] Full worked example: 1.1 (Guide demonstrates entire process with think-aloud)
- [x] Partial worked example: 1.2 (system partitions, student writes expression)
- [x] Independent: 1.3 (minimal Guide context, student does cognitive work)
- [x] Fading structure documented: Full → Partial → Independent across S1

**Think-Aloud:**

- [x] 1 think-aloud with tagged elements (1.1: [PLANNING], [ATTENTION], [SELF-CHECK])
- [x] In Representational phase (S1), not Abstract
- [x] Guide models, doesn't ask student to metacognate

**Vocabulary Staging (matches §1.3):**

- [x] "breaking apart" / "broke apart" — S1, Interaction 1.1 (first use in worked example)
- [x] "decompose" / "decomposing" — S1, Interaction 1.2 (mathematical synonym)
- [x] "partial products" — S2, Interaction 2.2 (after experiencing multiple decompositions)
- [x] "area model" (status-change) — S3, Interaction 3.1 (grid-to-ungridded transition)
- [x] "parentheses" — S1, Interaction 1.1 (notation convention, no [vocab] tag)
- [x] No forbidden vocabulary in any Guide or Prompt line

**Guide/Prompt Independence (spot-check 3 interactions):**

- [x] 1.2: Guide says "build the expression that matches these two parts" → complete instruction. Prompt says "Use the tiles to build the partial-product expression: (3 × 5) + (3 × 3) = ?" → complete instruction. Both work independently. ✓
- [x] 2.1: Guide says "Place the line, then build your expression" → complete instruction. Prompt says "Place the partition line... Then build the expression and find the total." → complete instruction. Both work independently. ✓
- [x] 3.2: Guide says "Where would you break the 13... Place your line and build the expression." → complete instruction. Prompt says "Decompose the 7 × 13 area model. Place the partition, build the expression, and find the total." → complete instruction. Both work independently. ✓

**Structure:**

- [x] Purpose Frame present (connects backward to Warmup, forward to "do that yourself")
- [x] Section transition markers present (→ SECTION 1 COMPLETE, → SECTION 2 COMPLETE)
- [x] Every interaction has a type label ([WORKED EXAMPLE], [GUIDED PRACTICE], [INDEPENDENT CHECK], [STUDENT CHOICE], [RELATIONAL DISCOVERY], [RELATIONAL EXTENSION], [TRANSITION])
- [x] All interactions use toys/modes documented in §1.5

**Cross-Module Checks:**

- [x] On Correct lines differ from M5 (Pattern #41): M5 used commutativity language; M6 uses decomposition/partial product language. No identical phrasing.
- [x] Hook/opening different from M5 Warmup (Pattern #40): Verified in Warmup checklist.

**Interaction Count:** 10 Lesson interactions + Purpose Frame + Bridge = 12 total elements. Minimum 6 required. ✓

---

---

## 1.8 EXIT CHECK (~3-5 minutes)

**[REQUIRED]**

### EC Requirements Checklist (from EC Playbook)

- [ ] 3 problems testing SAME core concept from Lesson
- [ ] Cognitive types from M4-6 range: CREATE and/or IDENTIFY; add COMPARE if comparison was taught
- [ ] Sequencing: simple to complex cognitively
- [ ] All problems use ONLY visual models, orientations, and interaction types from Lesson
- [ ] Values differ from Lesson and Warmup (fresh factor-product triples)
- [ ] No new vocabulary, visual models, or interaction types introduced
- [ ] Brief, specific feedback (5-10 words per On Correct)
- [ ] No new information in On Correct
- [ ] Clear, objective, binary success criteria on each problem
- [ ] Appropriate difficulty: representative middle (not too easy, not too hard)
- [ ] Transition frame from Lesson present (Bridge to EC interaction)

### Purpose

Verify Lesson understanding before Practice. Tests whether students can (1) identify the correct partial-product expression for a shown decomposition (recognition of expression-to-diagram connection), (2) independently decompose an ungridded rectangle, write the expression, and compute the product, and (3) produce an alternative decomposition of a rectangle (creative application of the "different decompositions, same total" insight).

### Parameters

| Element | Specification |
| :---- | :---- |
| **Problems** | 3 |
| **Cognitive Types** | IDENTIFY (EC.1 — expression recognition from shown partition); CREATE (EC.2 — independent decomposition + expression + computation); CREATE (EC.3 — produce alternative decomposition). See Design Note below for COMPARE discussion. |
| **Time** | 3-5 minutes |
| **Tone** | Calm, low-stakes |
| **Toys Used** | Grid Rectangles (gridded, system-placed partition — EC.1), Grid Rectangles (ungridded — EC.2, EC.3), Equation Builder (interactive — EC.2, EC.3; display — EC.1 options) |
| **Remediation** | Pipeline |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Use Grid Rectangles + Equation Builder (same configurations as Lesson) | Introduce new tools or interaction types |
| Use values NOT identical to any Lesson, Warmup, or Synthesis interaction | Reuse exact Lesson/Warmup factor-product triples |
| Stay within data constraints (factors 2-9, products ≤ 100) | Exceed Lesson complexity range |
| Test the decomposition-to-expression connection (S1), independent decomposition (S2/S3), AND alternative decomposition production | Test skills not explicitly taught in Lesson |
| Include U4.6 distractor (missing common factor) in EC.1 MC options | Omit the primary misconception from assessment |
| Enforce benchmark constraint on EC.2 (student decomposes at 2, 5, or 10) | Allow open-ended decomposition in EC (that's Practice) |

### Alignment Check

| Problem | Tests | Lesson Source | Cognitive Type |
| :---- | :---- | :---- | :---- |
| EC.1 | Expression-to-diagram connection — select correct expression for shown partition | Section 1: guided decomposition (1.1–1.3) | IDENTIFY |
| EC.2 | Independent decomposition on ungridded — choose partition, write expression, compute | Section 3: ungridded independent (3.2–3.3) | CREATE |
| EC.3 | Alternative decomposition — given one decomposition, produce a DIFFERENT one | Section 2: relational discovery (2.1–2.3) — multiple valid decompositions | CREATE |

> **Design Note — Cognitive Type Selection:** M6's core skill is procedural (decompose → write expression → compute), which maps to CREATE. The relational insight (different decompositions → same product) was experienced in S2 but not as a comparison task — students discovered it through sequential reveals, not by comparing and selecting. COMPARE would require testing a skill (selecting which of two decompositions is "better" or "correct") that the lesson deliberately avoided — the lesson's message is "all valid decompositions are equal." EC.1 is reframed as IDENTIFY (select from options) to provide cognitive type variety. EC.3 tests the relational insight through production (CREATE an alternative), not comparison. This is documented as KDD.

---

### Transition Frame [Bridge to EC — from Lesson]

The Bridge to Exit Check interaction at the end of §1.7 Lesson serves as the transition frame:
* **Guide:** "You've been breaking apart rectangles and writing expressions, on grids and without them. Let's see what you know."

---

### Interaction EC.1: Match the Expression [IDENTIFY]

* **Purpose:** Student identifies which partial-product expression matches a shown gridded decomposition. Tests S1's expression-to-diagram connection — the core skill from guided decomposition. MC format with U4.6 distractor.
* **Visual:** Grid Rectangles (gridded, system-placed partition). 2 × 9 rectangle with full grid. Partition at column 5: left sub-rectangle 2 × 5 (color A), right sub-rectangle 2 × 4 (color B). Dimensions labeled on both.
* **Guide:** "Here's a rectangle that's been broken apart. Which expression matches these two parts?"
* **Prompt:** "Select the expression that matches this decomposition."
* **Student Action:** Select (single)
  * **Options:**
  A. (2 × 5) + (2 × 4)
  B. (2 × 5) + 4
  C. (2 × 9)
  D. (2 × 5) × (2 × 4)
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct: matches left sub-rectangle (2 × 5) and right sub-rectangle (2 × 4)
  - B = U4.6 distractor: forgot to multiply the common factor (2) by the right part — wrote "4" instead of "2 × 4"
  - C = Didn't decompose — wrote the whole-rectangle expression
  - D = Operation error: used multiplication instead of addition to combine the partial products — confused "putting parts together" with multiplying
* **On Correct:** "That matches. Two parts, two multiplications, one addition."
* **Remediation:** Pipeline

> **Value Selection:** 2 × 9 = 18. Factor 1: 2 (Early range). Factor 2: 9. Product 18 — fresh (not used in any Lesson, Warmup, or other EC interaction). Partition at 5: (2 × 5) + (2 × 4) = 10 + 8 = 18. Sub-problems within fluent facts. U4.6 distractor B directly targets "forgetting to multiply both parts" per DN-7.

> **D8 Note:** Expression displayed in standard format (partial-product expression on left). EC does not need to meet the ≥30% nonstandard target (that applies to Lesson Late interactions).

---

### Interaction EC.2: Ungridded — You Decompose [CREATE]

* **Purpose:** Student independently decomposes an ungridded rectangle: chooses partition point (benchmark), writes the expression, and computes the total. Tests S3's independent ungridded decomposition skill. Highest-demand single-rectangle problem.
* **Visual:** Grid Rectangles (ungridded). 8 × 12 rectangle — outline only with dimension labels "8" and "12." No grid squares. Student places partition line. After placement: sub-rectangle dimensions appear. Equation Builder (interactive) — empty.
* **Guide:** "An 8-by-12 area model. Decompose it and find the product."
* **Prompt:** "Place the partition, build the expression, and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Benchmark partition producing correct total. E.g., at 10: (8 × 10) + (8 × 2) = 96. At 5: (8 × 5) + (8 × 7) = 96. At 2: (8 × 2) + (8 × 10) = 96. System validates benchmark constraint (2, 5, or 10) and expression-partition match.
* **On Correct:** "96. Two partial products, no grid needed."
* **Remediation:** Pipeline

> **Value Selection:** 8 × 12 = 96. Factor 1: 8 (Late range). Factor 2: 12. Product 96 — fresh. Benchmark 10 is the natural choice (8 × 10 = 80, 8 × 2 = 16 — both fluent facts). Larger factors than Lesson Late values (7 × 13, 6 × 14) to confirm transfer, but still within data constraints.

---

### Interaction EC.3: A Different Way [CREATE]

* **Purpose:** One decomposition shown with expression. Student produces a DIFFERENT decomposition of the same rectangle. Tests the relational insight from S2: multiple valid decompositions produce the same total. Highest cognitive demand in the EC — student must produce an alternative, not just verify one.
* **Visual:** Grid Rectangles (ungridded). 4 × 11 rectangle — outline only with dimension labels "4" and "11." Partition line shown at 10: left sub-rectangle labeled "4 × 10," right sub-rectangle labeled "4 × 1." Equation displayed below: "(4 × 10) + (4 × 1) = 44." Below: same rectangle, unpartitioned, with "Your turn" label. Equation Builder (interactive) — empty.
* **Guide:** "Here's one way to decompose 4 × 11. Can you find a DIFFERENT way?"
* **Prompt:** "Decompose the 4 × 11 rectangle a different way. Place a new partition, build the expression, and find the total."
* **Student Action:** Place tick (partition line) + Drag to build (Equation Builder)
* **Correct Answer:** Any benchmark partition DIFFERENT from the shown one (at 10). Valid alternatives: at 5: (4 × 5) + (4 × 6) = 20 + 24 = 44. At 2: (4 × 2) + (4 × 9) = 8 + 36 = 44. System validates: different partition point, benchmark constraint, expression-partition match, total = 44.
* **On Correct:** "44. Same product, different decomposition. Two ways work."
* **Remediation:** Pipeline

> **Value Selection:** 4 × 11 = 44. Factor 1: 4 (Mid range). Factor 2: 11. Product 44 — fresh. The shown decomposition at 10 is the "easy" choice; student must find an alternative (at 5 or at 2). Both alternatives produce fluent sub-problems. This directly tests the S2 relational insight: "different decompositions, same total."

> **Design Note — EC.3 and TVP Version B:** Per DN-5 (Gate 1), EC.3 follows TVP Version B: student PRODUCES an alternative decomposition (CREATE), not merely verifies that two shown decompositions match (IDENTIFY). This is the higher-demand option, testing strategic flexibility.

---

### EC Closure [No Student Action]

* **Purpose:** Transition from Exit Check to Practice. Signal that the assessment phase is complete and the student is ready for independent work.
* **Visual:** Clear screen.
* **Guide:** "You're ready. Let's practice."
* **No student action.**

---

### EC Verification Checklist

**Structure:**

- [x] 3 problems testing the decomposition-to-expression core concept
- [x] Each problem maps to a Lesson section (see Alignment Check): EC.1 → S1, EC.2 → S3, EC.3 → S2
- [x] Transition frame present (Bridge to Exit Check at end of Lesson)
- [x] Total time 3-5 minutes
- [x] Simple → complex sequencing: IDENTIFY (MC select) → CREATE (independent decomposition) → CREATE (produce alternative)

**Alignment:**

- [x] All visual models appeared in Lesson (Grid Rectangles gridded — S1; Grid Rectangles ungridded — S3; Equation Builder — all sections)
- [x] All interaction types appeared in Lesson (Select single — not directly, but MC is lower-demand version of Lesson's expression-building; Place tick + Drag to build — S2, S3)
- [x] Values differ from all Lesson and Warmup values:
  - EC.1: 2 × 9 = 18 (fresh product)
  - EC.2: 8 × 12 = 96 (fresh product)
  - EC.3: 4 × 11 = 44 (fresh product)
- [x] No skill tested that wasn't explicitly taught
- [x] Two cognitive types: IDENTIFY (EC.1) and CREATE (EC.2, EC.3)

**Constraints:**

- [x] No new vocabulary introduced
- [x] No new visual models introduced
- [x] No complexity increase beyond Lesson (Lesson used factors 2-7 first factor, 7-14 second factor; EC uses 2, 4, 8 first factor; 9, 11, 12 second factor — within Late range)
- [x] U4.6 distractor present in EC.1 (option B: missing common factor)
- [x] Every interaction has both Guide: and Prompt:
- [x] On Correct follows EC Playbook §3E: brief, specific, ≤10 words, no new information
- [x] M5 EC values (30, 42, 18÷6) — product 18 overlaps with EC.1 but M5 EC.1 product is 30, M5 EC.3 dividend is 18. EC.1 here tests a completely different skill (expression matching vs array rotation). No meaningful cross-module collision.

---

## 1.8.5 PRACTICE PHASE INPUTS

**[REQUIRED]**

### Skill Tracking

| Skill ID | Description | Lesson Source | Cognitive Type |
| :---- | :---- | :---- | :---- |
| SK1 | Write matching partial-product expression — given a gridded rectangle with partition shown, write the expression that matches the two sub-rectangles | Section 1 (1.1–1.3) | CREATE |
| SK2 | Decompose gridded rectangle at benchmark — student places partition (2, 5, or 10), writes expression, computes total. Grid visible for verification | Section 2 (2.1, 2.4) | CREATE |
| SK3 | Decompose ungridded rectangle at benchmark — student places partition on open area model, writes expression, computes total. No counting fallback | Section 3 (3.2–3.3) | CREATE |
| SK4 | Produce alternative decomposition — given one decomposition, student generates a different valid one for the same rectangle | Section 2 (2.1–2.3 relational insight) | CREATE |
| SK5 | Identify correct expression from options — given a decomposition visual, select the matching expression (MC). Includes U4.6 distractors | Section 1 (1.1–1.2) | IDENTIFY |

### Distribution Targets

* **SK1 (Expression writing from shown partition):** 20% of problems — foundational skill. Gridded rectangles with system-placed partitions. Student writes the matching expression. Early-range values (Factor 1: 2-4, Factor 2: 5-12). Gateway to SK2-SK4.
* **SK2 (Student-chosen decomposition, gridded):** 25% of problems — core procedural skill with grid support. Student chooses partition point (benchmark 2, 5, or 10), writes expression, computes total. Mid-range values (Factor 1: 2-5, Factor 2: 5-12). Any valid benchmark partition accepted. Grid visible for verification.
* **SK3 (Student-chosen decomposition, ungridded):** 25% of problems — highest-demand procedural skill. Same as SK2 but on ungridded/open rectangles (outline + dimensions only). Late-range values (Factor 1: 2-9, Factor 2: 7-14, products ≤100). Benchmark constraint enforced.
* **SK4 (Alternative decomposition production):** 15% of problems — relational skill. Given one decomposition with expression, produce a different valid one. Tests "different decompositions, same total" insight. Mix of gridded and ungridded. Rectangle shown with one partition; student must produce alternative at a different benchmark.
* **SK5 (Expression identification, MC):** 15% of problems — conceptual recognition. MC format with U4.6 distractors (missing common factor). Gridded rectangles. Lower demand than SK1-SK4 — use for interleaved assessment and A3 monitoring.

**Tier Classification:**

* **BASELINE:** SK1, SK2, SK3, SK5 — core decomposition and expression skills, counts toward mastery
* **STRETCH:** SK3 with larger factors (e.g., 9 × 14) + SK4 (alternative decomposition production), counts toward mastery
* **SUPPORT:** SK1 reduced — gridded rectangle with partition shown AND sub-rectangle products labeled. Student writes expression only (products given). Factors ≤ 5, products ≤ 30. Does not count toward mastery.
* **CONFIDENCE:** Single gridded rectangle with partition and expression both shown. Student confirms total by selecting from MC. Familiar facts only (products ≤ 20). Does not count toward mastery.

### Toy Constraints for Practice

Same as Lesson with the following notes:

* **Grid Rectangles (gridded):** Used for SK1, SK2, SK5 problems. Full grid visible. System-placed partition for SK1/SK5; student-placed for SK2. Color-coded sub-rectangles with dimensions labeled after partition.
* **Grid Rectangles (ungridded):** Used for SK3, SK4 problems (and some SK4 gridded variants). Outline + dimension labels only. Student places partition line. After placement: sub-rectangle dimensions appear.
* **Equation Builder:** Interactive for SK1, SK2, SK3, SK4 (tile-based expression construction). Display for SK5 (MC options shown as formatted expressions).
* **Data ranges:** Factor 1: 2-9, Factor 2: 5-14, products ≤ 100. All exact multiplication. Sub-problems from benchmark decomposition within fluent facts range.
* **Benchmark constraint:** BASELINE problems constrain partition to benchmark 2, 5, or 10. Above-baseline (STRETCH): fully open decomposition — any valid partition accepted.
* **U4.6 monitoring:** System should track SK5 responses. If student selects the U4.6 distractor (missing common factor) on 2+ SK5 problems, flag misconception and route to SUPPORT with explicit visual: highlight both sub-rectangles and their two dimensions.

### Dimensions Used Tracking (EC + Practice)

| Interaction | Factors | Product | Decomposition | Notes |
|-------------|---------|---------|---------------|-------|
| EC.1 | 2, 9 | 18 | At 5: (2×5)+(2×4) = 10+8 | Gridded, IDENTIFY (MC) |
| EC.2 | 8, 12 | 96 | Student choice (benchmark) | Ungridded, CREATE |
| EC.3 | 4, 11 | 44 | Shown at 10; student produces alternative | Ungridded, CREATE |

**Non-overlap verification:** No EC product matches any Lesson or Warmup product (18, 96, 44 vs. 36, 28, 24, 22, 40, 60, 91, 84). No EC product matches M5 EC products (vs. 30, 42). ✓

**Note:** This table covers EC values only. Practice values are Pipeline-generated at runtime per the Distribution Targets and Toy Constraints above; no pre-specified dimensions. Full authored-content dimension tracking (Warmup + Lesson + EC + Synthesis) is in Working Notes.

### Cross-Module Skill References

M6 Practice does NOT include M5 content as spiral review. M5's commutativity is a property the student now applies implicitly when choosing which factor to decompose (e.g., 7 × 8 can be decomposed by breaking the 8 OR the 7 — commutativity makes both approaches valid). The area model framework from Unit 2 is familiar context, not spiral content.

### Error-Pattern Monitoring

The following error patterns should trigger diagnostic flags in the Practice pipeline:

* **U4.6 — Forgetting to multiply both parts (PRIMARY):** Student writes partial-product expression with one term missing the common factor (e.g., "(5 × 10) + 3" instead of "(5 × 10) + (5 × 3)" for a 5 × 13 rectangle). Detected via SK5 MC responses and SK1-SK4 expression validation. Intervention: route to SUPPORT with explicit visual — highlight both sub-rectangles with BOTH dimensions labeled, narrate "this part is [factor] × [piece], that part is [factor] × [other piece]."
* **Additive decomposition error:** Student decomposes factors additively instead of multiplicatively (e.g., 7 × 14 → "7 × 10 + 4" instead of "7 × 10 + 7 × 4" — splitting 14 into 10 + 4 but applying the factor 7 only once). This is a variant of U4.6. Intervention: same as above.
* **Non-benchmark partition:** Student partitions at a non-benchmark number in BASELINE problems (e.g., breaking 13 at 3 instead of 10, 5, or 2). Intervention: system prompts "Try breaking at 2, 5, or 10 — those create the easiest sub-problems." Route to SK2 (gridded) for visual verification.
* **Arithmetic error in partial products:** Student writes correct expression but computes incorrect partial products or incorrect total. Intervention: on gridded problems, prompt student to count grid squares for verification. On ungridded, reduce to gridded SUPPORT for visual check.
* **Forgetting to add partial products:** Student writes "(3 × 10) + (3 × 4)" but reports only one partial product as the total (e.g., "30" instead of "42"). Intervention: highlight the addition sign and both products: "You've got two parts — now add them."

> **Note:** Distribution targets are starting proportions for the Practice pipeline. The system adjusts based on student performance data — increasing weight on skills where errors are detected and decreasing weight on mastered skills.

---

## 1.9 SYNTHESIS (~6-8 minutes)

**[REQUIRED]**

### Synthesis Requirements Checklist (from Synthesis Playbook)

- [ ] Opening Frame (30-45 sec): signal shift from practice to reflection
- [ ] Connection Tasks (4-5 min): 3-5 diverse discovery activities, each cognitively distinct
- [ ] Metacognitive Reflection (1-2 min): student reflects on strategies — prefer Type 1 or Type 3 for M4-6
- [ ] Identity-Building Closure (30 sec): specific, growth-oriented affirmation + M7 bridge
- [ ] At least 2 different task types from Types A-D
- [ ] At least one task involves pattern recognition or transfer
- [ ] Visual support for every task
- [ ] Zero new teaching or procedures
- [ ] Light remediation only (mastery assumed)
- [ ] At least one task requires placement, matching, or creation (not all MC)
- [ ] Consolidation check: module taught one core strategy (decomposition) applied multiple ways — no explicit side-by-side strategy review needed (single strategy, not multiple)

### Purpose

Students step back from decomposition practice to see the BIGGER PICTURE: the area model makes the distributive property (unnamed) VISIBLE — both parts are right there, and it works no matter where you break. They connect the gridded-to-ungridded progression (representation transfer), recognize the pattern that any decomposition of the same rectangle produces the same product (pattern recognition), briefly connect the multiplication table to the area model framework (per AF1), and reflect on which strategy choices felt easiest (metacognitive reflection). Per TVP: vocabulary consolidation — decompose, area model, partial products, breaking apart. Bridge to M7: place value strategy for multiples of 10.

### Parameters

| Element | Specification |
| :---- | :---- |
| **Duration** | 6-8 minutes |
| **Toys Used** | Grid Rectangles (gridded + ungridded, display), Equation Builder (display), Multiplication Tables Grid (display — for table-as-area-model connection per AF1) |
| **Interaction Count** | 4 student-action moments (S.1 representation transfer, S.2 table-as-area-model connection, S.3 pattern discovery, S.4 metacognitive reflection) + Opening Frame + Identity-Building Closure |
| **Task Types** | Type D: Representation Transfer (S.1 — gridded vs ungridded same decomposition), Type D: Representation Transfer (S.2 — multiplication table as area model), Type A: Pattern Discovery (S.3 — three decompositions same total), Metacognitive Reflection Type 3: Tool/Approach Preference (S.4) |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Use a fresh value set not seen in Lesson, EC, or Warmup | Reuse Lesson/EC/Warmup factor-product triples |
| Connect across representations (gridded ↔ ungridded ↔ table) | Present more practice problems disguised as Synthesis |
| Include at least 2 different task types (Type D + Type A) | Use only one task type |
| Include metacognitive reflection before closure | Skip reflection |
| Identity-building closure references specific student achievements | Use generic praise ("Great job!") |
| Bridge to M7 mentions "multiples of 10" and "place value" per TVP transition | Bridge to content beyond M7 |
| Include table-as-area-model connection task per AF1 | Skip the table connection |
| Vocabulary consolidation: decompose, area model, partial products, breaking apart | Introduce new vocabulary |
| Light remediation only (mastery assumed) | Extended reteaching |

---

### Opening Frame [No Student Action]

* **Purpose:** Signal shift from practice to reflection. Connect backward to the Lesson progression (gridded → ungridded, different decompositions → same product) and set up the consolidation work.
* **Visual:** Grid Rectangles (gridded, display). A 3 × 7 rectangle shown with partition at 5: left 3 × 5 (color A), right 3 × 2 (color B). Expression below: "(3 × 5) + (3 × 2) = 21." Adjacent: same 3 × 7 rectangle shown ungridded with same partition — outline only, dimension labels, expression below.
* **Guide:** "You started with grids and ended without them. You broke apart rectangles at 5, at 10, at 2, and every time, the total came out the same. Let's look at what you've been doing from a bigger picture."
* **No student action.**

> **Design Note:** Opening uses 3 × 7 = 21 — fresh value (not used in Lesson, EC, or Warmup). The simultaneous gridded/ungridded display of the same decomposition immediately establishes the progressive formalization theme that S.1 will develop.

---

### Interaction S.1: Grid vs No Grid — Same Math [REPRESENTATION TRANSFER — Type D]

* **Purpose:** Students see the same decomposition on a gridded rectangle and an ungridded rectangle simultaneously. They identify what stayed the same and what changed. Tests understanding that the area model strategy works regardless of visual support.
* **Visual:** Two panels side by side:
  - Panel A: Grid Rectangles (gridded). 3 × 7 rectangle with partition at 5. Full grid visible. Left: 3 × 5 = 15 (color A). Right: 3 × 2 = 6 (color B). Expression: "(3 × 5) + (3 × 2) = 21."
  - Panel B: Grid Rectangles (ungridded). Same 3 × 7 rectangle with same partition at 5. Outline only, dimension labels. Expression: "(3 × 5) + (3 × 2) = 21."
* **Guide:** "Look at both rectangles. One has a grid, one doesn't. What stayed the same?"
* **Prompt:** "What's the same about both decompositions?"
* **Student Action:** Select (single)
  * **Options:**
  A. The expression and the total
  B. The number of squares
  C. The colors
* **Correct Answer:** A
* **Answer Rationale:**
  - A (The expression and the total): Correct — the mathematical content (expression, partial products, total) is identical across representations. The grid is a visual aid, not a mathematical requirement.
  - B (The number of squares): Incorrect — the ungridded version has no visible squares. Students choosing this are fixated on the grid's visual features rather than the mathematical information.
  - C (The colors): Incorrect — surface-level observation. Colors are a visual distinction tool, not a mathematical property.
* **On Correct:** "Same expression, same total. The grid helps you count, but the math works either way."
* **Remediation:** Pipeline

> **Design Note:** This is the simplest Synthesis task — recognition that the mathematics is invariant across representations. The wrong answers (B, C) are concrete/surface-level observations that a student fixated on the visual might choose. Option B is tricky: the ungridded version has no visible squares, so "number of squares" can't be verified there — testing whether students understand that the dimensions carry the information, not the grid.

---

### Interaction S.2: The Table IS an Area Model [REPRESENTATION TRANSFER — Type D]

* **Purpose:** Brief connection task per AF1 (Gate 1). Students see a small section of the multiplication table and recognize it as a gridded area model with the origin at upper-left. They identify a product in the table as the area of the corresponding rectangle. This is exposure, not mastery — one task, not a full lesson.
* **Visual:** Multiplication Tables Grid (display). 5 × 5 corner of the table shown (rows 1-5, columns 1-5). Cell at row 3, column 4 highlighted (value: 12). Adjacent: Grid Rectangles (gridded, display). A 3 × 4 rectangle with full grid and no partition, dimensions labeled.
* **Guide:** "Look at the table corner. See the 12 at row 3, column 4? Now look at the rectangle: 3 rows, 4 columns, 12 squares. The multiplication table IS a grid of rectangles starting from the corner."
* **Prompt:** "Where in the table would you find the area of a 2 × 5 rectangle?"
* **Student Action:** Select (single) — click cell at row 2, column 5 in the table
* **Correct Answer:** Cell (2, 5) = 10
* **On Correct:** "10. Row 2, column 5. The table holds every rectangle's area."
* **Remediation:** Pipeline

> **Design Note (AF1 Resolution):** Per Conflict #4 and AF1 (Gate 1), the table-as-area-model connection is placed in Synthesis, not Lesson. This is a brief exposure task (~60 seconds) — students see the connection but aren't tested on it rigorously. The multiplication table IS a gridded area model is a conceptual insight that enriches understanding of both tools; full exploration happens if/when table-based strategies appear in later units.

> **Value Selection:** 3 × 4 = 12 (highlighted) and 2 × 5 = 10 (prompted) — both small values for immediate recognition. Neither product collides with Lesson, EC, or other Synthesis values.

---

### Interaction S.3: Three Ways, Same Answer [PATTERN DISCOVERY — Type B]

* **Purpose:** Students see three decompositions of the same rectangle and identify the common pattern: all produce the same total. This consolidates the relational insight from S2 (Lesson) — "different decompositions, same total" — through explicit pattern recognition rather than discovery.
* **Visual:** Three panels showing 6 × 8 = 48 decomposed three ways:
  - Panel A: Grid Rectangles (ungridded). Partition at 5: "(6 × 5) + (6 × 3) = 30 + 18 = 48"
  - Panel B: Grid Rectangles (ungridded). Partition at 2: "(6 × 2) + (6 × 6) = 12 + 36 = 48"
  - Panel C: Grid Rectangles (ungridded). Horizontal partition at 3 (splitting the 6): "(3 × 8) + (3 × 8) = 24 + 24 = 48"
* **Guide:** "Three different ways to decompose 6 × 8. Look at all three."
* **Prompt:** "What's the same about all three decompositions?"
* **Student Action:** Select (single)
  * **Options:**
  A. All three break the rectangle into exactly two parts
  B. All three produce the same total: 48
  C. All three break at the same number
* **Correct Answer:** B
* **Answer Rationale:**
  - A (All three break the rectangle into exactly two parts): Technically true but misses the mathematical point — the insight is about the PRODUCT being invariant, not the number of pieces.
  - B (All three produce the same total: 48): Correct — this is the relational insight: any valid decomposition of the same rectangle produces the same product. The partition point is a strategic choice, not a determinant of the answer.
  - C (All three break at the same number): False — they break at 5, 2, and horizontal-at-3 respectively. Students choosing this haven't attended to the different partition points shown.
* **On Correct:** "48 every time. Breaking apart works, no matter where you break."
* **Remediation:** Pipeline

> **Design Note:** Option A is technically true but misses the mathematical point. Option C is false (5, 2, and horizontal-at-3 are different). The target insight is B: invariance of the product across decompositions. Fresh value: 6 × 8 = 48, not used elsewhere.

---

### Interaction S.4: Your Strategy [METACOGNITIVE REFLECTION — Type 3]

* **Purpose:** Students reflect on which decomposition strategy felt most useful to them. Planning-focused (Type 3 per Synthesis Playbook) — concrete and accessible for Grade 3.
* **Visual:** Clear screen. Three benchmark options displayed as icons: "Break at 10," "Break at 5," "Break at 2."
* **Guide:** "You've been choosing where to break apart rectangles. Which benchmark worked best for you?"
* **Prompt:** "Which strategy felt easiest to use?"
* **Student Action:** Select (single)
  * **Options:**
  A. Breaking at 10
  B. Breaking at 5
  C. Breaking at 2
  D. It depended on the numbers
* **Correct Answer:** Any — all valid (no wrong answers in reflection)
* **Answer Rationale:**
  - A (Breaking at 10): Valid preference — 10 creates multiples-of-10 sub-problems, which are the easiest mental computations. Most common choice for factors 11-14.
  - B (Breaking at 5): Valid preference — fives facts are among the earliest fluent facts. Reliable across most factor ranges.
  - C (Breaking at 2): Valid preference — doubles are simple and accessible. Good for smaller second factors where 5 and 10 aren't natural.
  - D (It depended on the numbers): Most sophisticated response — demonstrates strategic flexibility and awareness that benchmark choice should be driven by the specific factors in the problem.
* **On Correct:**
  - A: "10 is a strong benchmark. Multiples of 10 are facts you know."
  - B: "5 is reliable. Fives facts come easily."
  - C: "2 keeps the pieces simple. Good eye."
  - D: "Choosing based on the numbers. That's strategic thinking."
* **Remediation:** Pipeline (light only — redirect to selection if no response)

> **Design Note:** Type 3 reflection (Tool/Approach Preference) is preferred for M4-6 per Synthesis Playbook §3E. The question surfaces students' developing strategic awareness without requiring abstract self-assessment. Option D ("it depended") is the most sophisticated response and gets the warmest validation.

---

### Identity-Building Closure + M7 Bridge [No Student Action]

* **Purpose:** Specific, growth-oriented affirmation referencing what the student demonstrated. Bridge to M7 per TVP Transition Out.
* **Visual:** Grid Rectangles (ungridded, display). A rectangle with a partition line and expression — the student's most recent successful decomposition from Practice (system selects). If unavailable, display 6 × 8 from S.3.
* **Guide:** "You decomposed rectangles, wrote expressions with partial products, and proved that breaking apart works, on grids and without them. You chose where to break based on what made the problem easiest. That's a multiplication strategy you own now. Next time, you'll look at what happens when one factor is a multiple of 10, like 4 × 30. That's a different kind of strategy. It uses place value instead of breaking apart."
* **No student action.**

> **Design Note — M7 Bridge:** Matches TVP Transition Out verbatim: "You've been breaking apart one factor to make multiplication easier. Next time: a DIFFERENT strategy for multiples of 10 — using place value." The distinction between M6 (breaking-apart strategy via area models) and M7 (place value strategy for multiples of 10) is explicit. Tool switch (Grid Rectangles → Base-10 Blocks) is not mentioned here — that's M7's job to introduce.

> **Voice Note:** Closure follows Synthesis Playbook §3F: specific behavioral observations ("You decomposed rectangles, wrote expressions... chose where to break"), growth framing ("a multiplication strategy you own now"), and forward bridge. No generic praise.

---

### Synthesis Verification Checklist

**Structure:**

- [x] Opening Frame present (connects backward to Lesson progression)
- [x] 4 connection tasks (S.1 through S.4), cognitively distinct
- [x] At least 2 different task types: Type D (S.1, S.2) + Type A (S.3) + Metacognitive Reflection (S.4)
- [x] Metacognitive reflection moment present (S.4 — Type 3: Tool/Approach Preference)
- [x] Identity-building closure with specific behavioral observations (not generic praise)
- [x] M7 bridge matches TVP Transition Out
- [x] Total time ~6-8 minutes

**Content:**

- [x] Visual support for every task
- [x] Zero new teaching or procedures — all tasks consolidate Lesson content
- [x] Vocabulary consolidation: "decompose" (S.1 Guide, S.3 Guide), "area model" (S.2 Guide, Closure), "partial products" (Closure), "breaking apart" (S.3 On Correct, Closure)
- [x] Table-as-area-model connection present (S.2 — per AF1)
- [x] Light remediation only (all interactions use Pipeline with light redirect)
- [x] At least one task requires placement/creation: S.2 requires cell selection in table
- [x] No new vocabulary introduced
- [x] Fresh values: 3 × 7 = 21 (Opening + S.1), 3 × 4 = 12 and 2 × 5 = 10 (S.2), 6 × 8 = 48 (S.3)

**Alignment:**

- [x] S.1 connects to S1/S3 progression (gridded → ungridded)
- [x] S.2 connects to M5 multiplication table + M6 area models (cross-module synthesis)
- [x] S.3 connects to S2 relational discovery (different decompositions, same total)
- [x] S.4 connects to Late benchmark choice (3.2, 3.3, 2.4)
- [x] Closure references student's own work, not hypothetical achievements

---

## 1.10 KEY DESIGN DECISIONS

**[REQUIRED]**

### KDD-1: Vocabulary Staging

"Breaking apart" and "decompose" are introduced in S1 (Early), "partial products" in S2 (Mid), "area model" status-change in S3 (Late). This staging follows the CRA arc: students need the action language first ("breaking apart" while they're doing it on gridded models), the output language second ("partial products" after they've seen multiple decompositions produce partial results), and the tool language last ("area model" when the grid disappears and the rectangle IS the strategy). Introducing all terms in S1 would overload working memory during the expression-to-diagram connection, which is already the hardest cognitive beat of the guided phase.

### KDD-2: Benchmark Constraint (2, 5, or 10)

Late Lesson interactions and EC constrain decomposition to benchmarks 2, 5, or 10; fully open-ended choice is reserved for Practice. The TVP originally specified "multiples of 5" (5 and 10 only). AF3 (Gate 1) extended to include 2, based on Andrea's rationale: with second factors up to 14, "break at 10" works for 11-14 and "break at 5" works for most, but smaller factors (e.g., 6, 7, 8) benefit from a "break at 2" option. Three benchmarks ensure genuine student choice in every problem, not a forced "the only option is 5." Practice removes the constraint because students have proven the strategy works and should explore freely.

### KDD-3: Sequential Reveal in S2

The three decompositions of 4 × 9 in Section 2 are revealed one at a time with comparison prompts, not simultaneously. Grade 3 working memory (5-7 items max) cannot hold three decompositions at once for meaningful comparison. The TVP showed three decompositions "side by side" for a single comparison moment; the SP spreads them across interactions (2.1: student's own, 2.2: Guide's alternative, 2.3: horizontal split) so each comparison is fresh and manageable.

### KDD-4: Warmup Uses 3 × 12, Not TVP's 4 × 6

The TVP Warmup used 4 × 6 = 24 with partition at 4. The SP uses 3 × 12 = 36 with partition at 10. Rationale: the module's benchmark strategy message is "break at 2, 5, or 10," and the Warmup should foreshadow this. 4 × 6 partitioned at 4 doesn't exemplify any benchmark. 3 × 12 partitioned at 10 demonstrates the most natural benchmark decomposition (3 × 10 + 3 × 2 = 30 + 6) and sets up the Lesson's guided phase with familiar benchmark-10 language.

### KDD-5: No COMPARE in Exit Check

The EC Playbook allows COMPARE for M4-6. M6's EC uses IDENTIFY + CREATE instead. The relational insight (different decompositions → same product) IS a comparison concept, but students experienced it through sequential reveals and discovery in S2 — they were never asked to compare decompositions as an assessment action. Forcing COMPARE (e.g., "which decomposition is better?") would either (a) have no single correct answer (they're all valid — that's the module's message) or (b) test a preference that the lesson deliberately didn't teach. EC.3's "produce an alternative" tests the relational insight through creation — asking students to generate a different valid decomposition is more authentic to S2's discovery approach than selecting between shown decompositions. CREATE also carries higher cognitive demand than COMPARE here, making EC.3 a stronger assessment of strategic flexibility.

### KDD-6: Table-as-Area-Model Placement in Synthesis

Per AF1 (Gate 1, Conflict #4), the table-as-area-model connection task is placed in Synthesis, not Lesson. The Module Mapping described it as a "synthesis beat"; the TVP's phase-by-phase Lesson description didn't include it. Synthesis placement is correct: students have just finished Practice and have the area model framework fully established. The connection ("the multiplication table IS a gridded area model starting from the corner") is a one-task exposure, not a taught skill. Full exploration deferred to later units if needed.

### KDD-7: Worked Example Fading Across S1

Section 1 uses a full → partial → independent fading sequence: 1.1 is a full worked example (Guide demonstrates entire process with think-aloud), 1.2 is a partial worked example (system provides partition, student writes expression), 1.3 is independent (minimal Guide, student does cognitive work). This is a single fading pass, not repeated. The fading ensures students see the complete process before attempting it, then get scaffolded support, then prove independence — all within the gridded representational phase before moving to student choice (S2) or ungridded models (S3).

### KDD-8: Parentheses as Notation Convention

Parentheses are introduced visually in 1.1 ("These curved lines, called parentheses, are like a box around each part") but are NOT tagged as [vocab]. Per D5, properties of operations are taught as strategies, not named. Parentheses are notation — they group terms visually — not mathematical vocabulary at the Grade 3 level. Students use them throughout but are never assessed on the word "parentheses" itself.

### KDD-9: Grid-to-Ungridded Transition via Explicit Fade (3.1)

Interaction 3.1 shows the same rectangle first WITH grid, then removes the grid while keeping dimensions and partition. This explicit visual fade (rather than simply presenting an ungridded rectangle) manages the abstraction leap by letting students see that the dimensions carry all the information the grid provided. The TVP specified "gridded → ungridded" progression; the SP implements this as a single interaction where students watch the transformation, then prove they can work without the grid in 3.2 and 3.3.

### KDD-10: Second Independent Partition in S2 (Interaction 2.4)

Interaction 2.4 (5 × 8) was added per Gate 2 review (P-9). Without it, students place their own partition only once (2.1) before the grid disappears in S3. A single student-placed partition is insufficient practice before the abstraction leap to ungridded models. 2.4 gives a second independent choice on a fresh gridded rectangle with a different Factor 1 (5, vs 4 in 2.1), confirming the strategy generalizes before removing visual support.

### KDD-11: Horizontal Partition in S2 (Interaction 2.3)

Interaction 2.3 introduces decomposing the OTHER factor (splitting the 4 into 2 + 2, rather than the 9). This is qualitatively different from the vertical partitions in 2.1 and 2.2, where students break the second factor. The design choice broadens the decomposition concept: either factor can be broken apart, and the strategy still works. This is not documented in the Section Plan's S2 description ("student chooses decomposition") because the Section Plan focuses on the relational insight (multiple valid decompositions → same product). The horizontal partition is a specific instance of that insight, but it crosses a conceptual boundary — splitting Factor 1 vs Factor 2 — that merits explicit documentation. The move is Guide-demonstrated (Type A), not student-discovered, to manage cognitive load: students see it works, then apply it independently in later modules.

---

## 1.11 FINAL FORMATTING AUDIT

- [x] All `[vocab]` tags on NEW/status-change terms only; established terms untagged
- [x] All interaction headers include descriptive label + Type classification in brackets
- [x] Type labels match student action presence (Type A = no action, Type B = independent action, Type C = scaffolded action)
- [x] CRA Stage line present after each §1.7 section header (S1 Representational, S2 Relational, S3 Abstract)
- [x] No development tags remaining in student-facing content ([PLANNING]/[ATTENTION]/[ACTION]/[SELF-CHECK] are authoring annotations, strip before Notion)
- [x] All Prompts are Guide-independent (tested on 1.2, 2.1, 3.2)
- [x] No em dashes (—) in Guide, Prompt, or On Correct dialogue lines (VO13 resolved)
- [x] All MC interactions have Answer Rationale blocks (W.1, EC.1, S.1, S.3, S.4)
- [x] KDD entries use `### KDD-N:` heading format (KDD-1 through KDD-10)
- [x] EC Closure interaction present between EC.3 and Practice Inputs
- [x] "partial products" vocabulary reinforced in EC (EC.2 On Correct)
- [x] Dimension Tracking table in Working Notes matches SP values
- [x] Version date updated to reflect final edit date
- [x] END OF MODULE marker present
- [x] No placeholder text remaining (searched for bracket-wrapped stubs)

---

# END OF MODULE 6 STARTER PACK
