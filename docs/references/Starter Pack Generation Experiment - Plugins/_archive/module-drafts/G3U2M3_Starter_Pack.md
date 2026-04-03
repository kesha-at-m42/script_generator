# MODULE 3: Structured Counting — Rows and Columns

**Version:** 03.16.26

```
---
module_id: M03
unit: 2
domain: measurement_area
primary_toys:
  - name: "Grid Rectangles"
    notion_url: "https://www.notion.so/ocpgg/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca"
secondary_toys: none
interaction_tools: MC, Tap-to-Highlight
our_lessons: L4
---
```

---

# BACKBONE

---

## 1.0 THE ONE THING

**[REQUIRED]**

A rectangle's area can be found by seeing its tiles as equal rows (or equal columns) and skip-counting — instead of counting every tile one by one.

**Critical Misconception:** #2.0 — Counting One-by-One. Students count every tile individually instead of using row/column structure, preventing them from developing the efficient strategies that lead to multiplication.

**Success Indicator:** Given a tiled rectangle with no highlighting, the student identifies the number of rows and the number in each row (or columns and number in each column), skip-counts to determine the area, and can describe the structure using "___ rows of ___" or "___ columns of ___" language.

**CRA Stage:** Concrete → Representational transition. Students work with pre-tiled rectangles (concrete) but the cognitive work is representational — seeing and describing organizational structure rather than manipulating physical objects.

**Biggest Risk:** Students learn to PRODUCE the correct area total (by counting one-by-one) without ever SEEING the row/column structure. If the connection between spatial structure and efficient counting isn't made explicit — with dedicated interactions that force structure identification BEFORE area calculation — students may pass M3 through brute-force counting and hit a wall in M4 when multiplication requires structural understanding. The four-problem EC design addresses this by requiring structure identification as a separate, assessed step.

---

## 1.1 LEARNING GOALS

**[REQUIRED]**

*Verbatim from OUR Curriculum — Script Must Achieve These*

**L1:** "Describe and represent the area of a rectangle as the total number of unit squares arranged in equal groups of rows and columns."

**L2:** "Find the area of rectangles (within 60 square units) by counting unit squares."

**Module Goal (Student-Facing):** "Today you'll find a faster way to count all those tiles — by looking at how they're organized."

**Exit Check Tests:**
* Can the student identify the row/column structure of a tiled rectangle without highlighting support? (Structure identification MC — must select correct description BEFORE calculating area)
* Can the student use skip-counting (not one-by-one counting) to determine area? (Skip-counting validation)
* Can the student describe the same rectangle's area using BOTH rows and columns? (Flexible structure-seeing)

**Question/Test Language Stems (from Module Mapping):**
* "How many rows? How many in each row?" → Maps to Lesson Section 1 (row discovery) and EC Problems 1-2
* "How many columns? How many in each column?" → Maps to Lesson Section 2 (column discovery) and EC Problem 4
* "What is the area?" → Maps to EC Problems 1-3 and all Lesson practice interactions

### 1.1.1 Standards Cascade

| Building On | 3.MD.C.5.b (tiling with no gaps/overlaps — from M2) |
| :---- | :---- |
| **Addressing** | 3.MD.C.6 (counting unit squares with structure) |
| **Building Toward** | 3.MD.C.7.b (multiply side lengths — M4+) |

**Standards Note:** M3 advances 3.MD.C.6 from M2's introduction (accurate tiling → accurate counting) to structured counting (row/column organization → skip-counting). M3 does NOT fully satisfy 3.MD.C.6 — standard unit vocabulary (sq cm, sq in, etc.) is deferred to M5-M6, and the multiplication connection (counting structure → multiplication formula) is deferred to M4. M3's specific contribution to 3.MD.C.6 is establishing that unit squares in a rectangle are organized in equal rows and equal columns, enabling efficient counting via skip-counting.

### 1.1.2 Module Bridges

**From M2 (Tiling Rectangles — No Gaps, No Overlaps):** Students can tile rectangles accurately with no gaps and no overlaps. They count every tile one by one to determine area and can state it in square units. They identify gaps and overlaps as errors (too few / too many). M2 Synthesis bridge: a correctly tiled 3×4 rectangle with one highlighted row — "You can tile perfectly now! But counting every single tile takes time. Look at this row. Is there a faster way to count? That's what we'll figure out next time." Students arrive with accurate tiling skills, gap/overlap rules internalized, and the question "Is there a faster way?" as motivation.

**This Module:** Students discover that tiles in a rectangle form equal rows and equal columns. They learn to identify the structure ("___ rows of ___"), skip-count by rows or columns to find area efficiently, and confirm that both directions give the same answer. "Row" and "column" vocabulary is formalized through concrete experience. "Array" vocabulary is introduced as a naming term for the row-column arrangement. This is the critical bridge from counting to multiplying — students must SEE structure before they can USE multiplication. (⚠️ CRITICAL MODULE — Decision #2)

**To M4 (Area as Multiplication):** Students leave M3 able to describe rectangles as "___ rows of ___" and skip-count to find area. M4 opens with the explicit bridge: "Last time you found 6 rows of 4 = 24 by skip-counting. Watch this: 6 × 4 = 24. Same thing — but faster!" The M3→M4 transition converts structure-description language to multiplication notation. No M4 content is previewed in M3 — the multiplication bridge is M4's responsibility (resolved SME decision).

### 1.1.3 OUR Lesson Sources

| OUR Lesson | Content Used | Adaptation Notes |
| :---- | :---- | :---- |
| L4 | Row/column structure identification; finding area by counting rows/columns; skip-counting to find area; describing rectangles as "rows of" | Adapted from physical tile manipulation and partner activities to digital Grid Rectangles with progressive highlighting (auto → tap → off). OUR's partner activity ("What Did I Create") replaced with individual tap-to-highlight interactions. OUR's large area rectangles (within 60 sq units) constrained to max 50 (5×10) per TVP dimension restrictions. Skip-counting by 2, 3, 4, 5, 10 only — no 6-9 skip-counting (Grade 2 prior knowledge boundary). |

---

## 1.2 SCOPE BOUNDARIES

**[REQUIRED]**

### ✅ Must Teach

* Row/column structure in tiled rectangles — every row has the SAME number of tiles; every column has the SAME number
* Skip-counting by rows to find area (replacing one-by-one counting)
* Skip-counting by columns to find area — same answer as rows
* "How many rows? How many in each row?" as the key structural question
* Structure-description language: "___ rows of ___" / "___ columns of ___"
* Vocabulary: row, column, array
* Vocabulary definitions: Row = horizontal line of squares; Column = vertical line of squares; Array = an arrangement of objects in equal rows and columns
* The efficiency advantage of structured counting over one-by-one counting
* Both horizontal (row-based) and vertical (column-based) structure-seeing
* Rectangle structure reinforcement (continues from M2 — 4 sides, 4 right angles)

### ❌ Must Not Include

* Multiplication notation (×, times, product, factor) — M4
* Multiplication as a strategy for finding area — M4
* "Length × width" formula — M7+
* Dimensions-only rectangles (no visible tiles) — M7+
* Partial grids, tick marks, grid fading — M7+
* Standard units (square centimeters, square inches, etc.) — M5-M6
* Perimeter or "distance around" — NOT in Unit 2 (Decision #5)
* Skip-counting by 6, 7, 8, or 9 — NOT Grade 2 prior knowledge; belongs to M4+ when multiplication replaces skip-counting
* Tiling activities (drag-to-place) — M2 skill, not M3's focus. M3 uses pre-tiled rectangles.
* Composite figures or non-rectangular shapes — M11+
* Commutative property of multiplication — M4+ (though M3 builds toward it by showing rows and columns give the same total)

⚠️ **CRITICAL MODULE (Decision #2):** Research shows only 31% of 3rd graders can spatially structure arrays without explicit instruction. M3 MUST include dedicated activities targeting row-column seeing — this is an explicit instructional target, not an assumed skill. Delay multiplication formula until M4. Use highlighting/animation to make structure visible. This constraint drives every interaction in M3.

### Scope Confirmation Checklist

- [x] What concepts are IN scope vs. deferred? — Row/column structure IN; multiplication OUT (M4)
- [x] What vocabulary is introduced vs. just used vs. forbidden? — row, column, array INTRODUCED; area, square unit, rectangle USED; multiply, times, factor, length, width FORBIDDEN
- [x] What specific values/parameters are required? — Dimensions from {2, 3, 4, 5, 10} only; areas 6-50
- [x] What value constraints apply? — Products within 60; never both dimensions outside {2,3,4,5,10}; skip-counting limited to 2, 3, 4, 5, 10
- [x] Are there any "both X and Y" situations? — Students must describe structure BOTH ways (rows AND columns) for some problems
- [x] What OUR lessons does this module combine? — L4 only
- [x] What are the scope boundaries with adjacent modules? — M2 establishes tiling rules; M3 adds structure; M4 adds multiplication. No overlap in instructional targets.

---

## 1.3 VOCABULARY ARCHITECTURE

**[REQUIRED]**

**Assessment Vocabulary (appears on state test):** area, unit square, square unit (continuing from M1-M2) + row, column (new for 3.MD.C.6)

### Vocabulary Staging by Phase

| Phase | Terms | Introduction Approach |
| :---- | :---- | :---- |
| **Warm-Up** | area, square unit, tile/tiles, rectangle | Continue from M1-M2 — use naturally. No new formal vocabulary in Warmup. "Counting every tile" reinforces M2 language. |
| **Lesson Section 1 (Row Discovery)** | row, "rows of" | Introduced DURING concrete observation of highlighted rows. Students see rows highlighted → count per row → discover equal count → term "row" formalized. "Rows of" structure language practiced immediately. |
| **Lesson Section 2 (Column Discovery — Early)** | column, "columns of" | Introduced DURING system auto-highlight column experience (first column exposure). Same grounding pattern as "row." Students discover columns also equal, also produce same area. |
| **Lesson Section 2 (Transfer)** | (row, column practiced) | Tap-to-highlight practice with both-direction descriptions. Students actively use tool to find structure. No new vocabulary — practice existing terms. |
| **Lesson Section 2 (Capstone)** | array | CALLBACK from Unit 1. Activated AFTER students have practiced both row and column descriptions through tap-to-highlight: "You've been working with these the whole time — rows and columns together. That's called an array." Placed at Section 2 capstone so students absorb "column" and practice both-direction descriptions BEFORE a third term lands. |
| **Lesson Section 3 (Independent)** | (all terms) | Used in structure descriptions. Student applies vocabulary independently without highlighting support. |
| **Exit Check** | row, column, area, square unit | Used in prompts and structure descriptions. |
| **Synthesis** | (all terms) | Used in consolidation tasks. "Rows" / "columns" / "array" expected in student structure descriptions. |

### Vocabulary Note: "Array"

Module Mapping lists "array" in Vocabulary to Teach. TVP does not explicitly mention "array" in M3 vocabulary sections but consistently uses row/column structure language. Per hierarchy rule #3, Module Mapping is authoritative for vocabulary. "Array" is staged as the Section 2 capstone (interaction 2.5) — after both row and column are established AND students have practiced both-direction descriptions through tap-to-highlight — as a CALLBACK from Unit 1. Students will have encountered "array" in Unit 1 (arrays and multiplication). M3 activates this term in the area context: "You've seen arrangements like this before — rows and columns. That's called an array." Per Decision #4: leverage array knowledge if students have it (callback), teach it if they don't (grounding through row/column experience makes the term concrete). The key definition for M3: "An array is an arrangement of objects in equal rows and equal columns." This is NOT multiplication-via-arrays — it's naming the spatial structure students have already discovered through highlighting.

### Terms to Avoid (Save for Later Modules)

* multiply / multiplication / times (M4)
* product / factor (M4-M5)
* equation / expression (M5)
* formula (M7+)
* length / width / dimensions (M7+)
* perimeter (NOT in Unit 2 — Decision #5)
* square centimeters / square inches / square feet / square meters (M5-M6)
* decompose / partition (M11)
* skip-count by 6, 7, 8, 9 (M4+ — these are NOT Grade 2 prior knowledge)

---

## 1.4 MISCONCEPTIONS

**[REQUIRED]**

### 1.4.1 #2.0: Counting One-by-One (PRIMARY)

**Trigger Behavior:** With a 5×10 rectangle, student counts 1, 2, 3... 50 instead of skip-counting by rows (10, 20, 30, 40, 50) or columns (5, 10, 15, 20...). Student produces correct area totals but takes significantly longer and cannot describe the structure when asked "How many rows? How many in each row?"

**Why It Happens:** M1-M2 taught and reinforced one-by-one counting as the strategy for finding area. Students counted tiles as they placed them (M2) or counted placed tiles (M1). The shift to structural counting requires seeing tiles not as individual objects but as organized groups — a cognitive leap many students don't make without explicit instruction (only 31% per research). Some students may have established one-by-one as the "correct" method and resist changing strategies.

**Visual Cue:** Row highlighting (auto or tap-activated) makes the group structure visible. When rows are highlighted in different colors, the equal-group structure becomes perceptually obvious. The skip-counting animation along highlighted rows connects the visual structure to the counting strategy.

**Prevention Strategy:** M3's three-step scaffolding (system auto-highlight → student tap-to-highlight → no highlight) gradually transfers structural seeing from the tool to the student. Step 1 (S1): system shows structure — student observes. Step 2 (S2 Transfer): student uses the tool to find structure themselves — the critical internalization step. Step 3 (S3): student sees structure independently without any tool support. The key pedagogical move is requiring structure identification BEFORE area calculation — students must describe "How many rows? How many in each row?" before they can answer "What is the area?" This forces engagement with structure rather than bypassing it through brute-force counting. EC validates this by requiring structure MC selection before accepting area answers. For the 69% of students who cannot spatially structure arrays without explicit instruction, the tap-to-highlight transfer step is essential — passive observation alone does not reliably transfer to independent performance.

**Anti-Pattern Detection (for Practice):** Time-based proxy — if response time on consecutive problems significantly exceeds expected skip-counting time for that rectangle size, flag probable one-by-one counting. Structure MC errors — if student produces correct area but fails structure identification questions, they're bypassing structure. Both triggers return student to tap-to-highlight level (not auto-highlight — student should practice active structure-finding).

### 1.4.2 #9.0: Array Structure Not Seen (SECONDARY)

**Trigger Behavior:** Student sees a rectangle of tiles but doesn't recognize the row/column organization. Counts randomly (jumping between tiles in no order) instead of systematically by rows or columns. When asked "How many rows?", student cannot answer or guesses incorrectly.

**Why It Happens:** Spatial structuring — seeing a collection of objects as organized into rows and columns — is a developmental milestone that research shows many students haven't reached by Grade 3. Students may perceive the tiles as an undifferentiated mass rather than as a structured arrangement. Prior experience with rows/columns from Unit 1 arrays helps (Decision #4) but cannot be assumed.

**Visual Cue:** Row/column highlighting provides the perceptual scaffolding. Auto-highlighting in Section 1 shows the structure explicitly. Tap-to-highlight in Section 2 gives students a tool to reveal structure on demand. By Section 3, students must mentally impose the structure without visual support.

**Prevention Strategy:** The three-step scaffolding (auto → tap → off) is specifically designed for this misconception. Auto-highlighting (S1) shows what structure LOOKS like — the system makes it visible. Tap-to-highlight (S2 Transfer) lets students practice FINDING structure — they actively use the tool to reveal what they're learning to see. No highlighting (S3) tests whether students can SEE structure independently. The key beat — "Every row has the SAME number!" — is the moment structure becomes salient. The tap-to-highlight step is where internalization happens: students move from "the system showed me" to "I can find it myself."

---

## 1.5 TOY SPECIFICATIONS

**[REQUIRED]**

### 1.5.1 Grid Rectangles

**Notion Spec:** [Grid Rectangles](https://www.notion.so/ocpgg/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca) | **Changes from M2:** Row and column highlighting features activated. In M2, Grid Rectangles was display-only (pre-tiled states for observation) or target (for tiling with Unit Square Tiles). In M3, Grid Rectangles is display-only throughout — no tiling in M3 — but now supports row highlighting (auto and tap-to-activate) and column highlighting (tap-to-activate). This is the primary new capability for M3. Three-step scaffolding progression: system auto-highlight (S1) → student tap-to-highlight (S2) → off (S3). AF#5 revised: tap-to-highlight restored as the critical transfer step between passive observation and independent structure-seeing.

**Purpose:** Display tiled rectangles with visible grid and progressive highlighting support. Students observe, identify structure, and skip-count to find area. Grid Rectangles is the ONLY toy in M3 — students do not tile; they analyze pre-tiled rectangles.

**Spec Reference (from M2 verification):** Grid Rectangles is a display object (not draggable). Student actions supported: Shade (individual squares), Select Row, Select Column. For M3, Select Row and Select Column are the key actions — Shade is not used (rectangles are pre-tiled). Grid state is system-controlled.

#### Module Configuration (M3)

| Aspect | This Module |
| :---- | :---- |
| **Mode** | Display only throughout (no tiling, no target mode) |
| **Grid State** | Full grid (`grid_state: "full"`) — always visible. System-controlled. (Decision #3: M1-M4 full grids) |
| **Unit Type** | Generic ("square units") — no standard units until M5 |
| **Shape Types** | Rectangles only |
| **Dimensions** | All dimensions from {2, 3, 4, 5, 10}. Never both dimensions outside this set. |
| **Area Range** | 6-50 square units (products within 60; max 5×10=50 with current constraints) |
| **Orientations** | Both horizontal and vertical |
| **Pre-Tiled State** | All rectangles fully tiled (all grid squares shaded). No gap/overlap displays in M3. |
| **Row Highlighting** | Available. Three modes: (1) System-driven — system highlights rows sequentially in different colors, synced with Guide skip-counting narration; (2) Tap-to-highlight — student taps to reveal row highlighting (student-initiated, system-executed); (3) Off — no highlighting. |
| **Column Highlighting** | Available. Three modes: (1) System-driven — system highlights columns sequentially; (2) Tap-to-highlight — student taps to reveal column highlighting; (3) Off — no highlighting. |
| **Interaction** | MC selection for structure identification and area answers. Tap-to-highlight for student-initiated structure revealing (Section 2 Mid). No drag interactions. |

#### M3 Guardrails

| DO | DO NOT |
| :---- | :---- |
| Show full grid on all rectangles (Decision #3) | Hide, fade, or partially show the grid |
| Pre-tile all rectangles (every square shaded) | Show gap/overlap errors (M2's territory, not M3's) |
| Use three-step highlighting scaffold: system-driven (Early) → tap-to-highlight (Mid) → off (Late/EC) | Keep highlighting permanently on or permanently off; skip the tap-to-highlight transfer step |
| Restrict dimensions to {2, 3, 4, 5, 10} | Use dimensions 6-9 (skip-counting outside Grade 2 prior knowledge) |
| Use rectangles with both orientations | Use only horizontal rectangles |
| Present structure identification BEFORE area calculation | Let students bypass structure and just count all |

#### Progression Within M3

| Phase | Highlighting Configuration | Student Interaction |
| :---- | :---- | :---- |
| **Warmup** | No highlighting — student observes and counts one by one | Observe, count one by one, feel inefficiency |
| **Lesson Section 1 (Early)** | System auto-highlights ROWS (different colors per row, synced with Guide skip-count narration) | Observe highlighted rows, count per row, discover equal count. MC for "How many in each row?" and area. |
| **Lesson Section 2 (Mid — Early)** | System auto-highlights COLUMNS (first exposure to column structure) | Observe highlighted columns, discover columns also equal, confirm same area both ways. MC for per-column count. |
| **Lesson Section 2 (Mid — Transfer)** | Tap-to-highlight (student-initiated): student taps to reveal row/column highlighting | Student actively uses tool to find and reveal structure. Tap-to-highlight rows, then columns. MC for structure description and area. This is the critical TRANSFER step — student moves from passive observation to active structure-finding. |
| **Lesson Section 3 (Late)** | No highlighting — full independence | Student identifies structure visually without any highlighting. MC for structure description and area. |
| **Exit Check** | No highlighting | Independent structure identification + skip-counting. MC for structure and area. |
| **Synthesis** | No highlighting (callback rectangle from Warmup) | Celebrate: same rectangle, now skip-counted efficiently. |

#### Data Constraints by Section

| Section | Dimension Constraint | Rectangle Examples (from TVP) | Area Range |
| :---- | :---- | :---- | :---- |
| **Warmup** | {2-6} × {2-6} for counting task (TVP: 6×4) | 6×4 (24) | 24 |
| **Lesson Section 1 (Early)** | At least one dimension from {2, 5, 10}; other from {2, 3, 5, 10}. Skip-count increment must be Grade 2 prior knowledge (2, 3, 4, 5, 10). | 3×5 (15), 2×5 (10), 2×10 (20), 5×10 (50) | 10-50 |
| **Lesson Section 2 (Mid)** | One dim from {2, 5, 10}, other from {2, 3, 4, 5, 10}. | 2×5 (10), 3×5 (15), 4×5 (20), 3×10 (30) | 10-30 |
| **Lesson Section 3 (Late)** | Same as Mid, larger areas | 4×10 (40), 5×10 (50), 3×10 (30), 4×5 (20) | 20-50 |
| **Exit Check** | Within {2, 3, 4, 5, 10} | Different from Lesson values: 3×4, 5×3, 10×2, 2×4 | 6-50 |
| **Practice** | Within {2, 3, 4, 5, 10} | Varied | 6-50 |
| **Synthesis** | 6×4 (callback) | 6×4 (24) | 24 |

> **Design Note (Warmup Dimensions):** The Warmup rectangle is 6×4 — note that 6 is OUTSIDE the {2, 3, 4, 5, 10} constraint that applies to Lesson/EC. This is intentional: the Warmup rectangle must be large enough to make one-by-one counting feel tedious (24 tiles). The 6-row dimension is used for counting, not for skip-counting — students count all 24 tiles individually. When this rectangle returns in Synthesis, students will skip-count 6 rows of 4: 4, 8, 12, 16, 20, 24 (skip-counting by 4 is Grade 2 prior knowledge). The "6" is the number of GROUPS, not the skip-counting increment — so the skip-counting difficulty is controlled by the columns (4), not the rows (6). Document as KDD.

> **Design Note (EC Area Range):** EC area range is 6-50 (matching Practice), not 10-50. EC problems may use smaller areas when the assessed skill is structural rather than computational. For example, EC.4 (2×4=8) tests column flexibility — the cognitive demand is on seeing columns, not on arithmetic difficulty. Keeping this constraint honest avoids requiring every future EC to document a KDD exception for small-area structural problems.

#### UX Component Requirements

| Component | Requirement | Where Used | Fallback |
| :---- | :---- | :---- | :---- |
| Row auto-highlighting | System highlights rows sequentially in distinct colors, synced with Guide skip-count narration | Lesson Section 1 (Early) | Guide dialogue narrates without visual highlighting (degraded experience) |
| Column auto-highlighting | System highlights columns sequentially in distinct colors, synced with Guide skip-count narration | Lesson Section 2 (Mid — Early, first column exposure) | Guide dialogue narrates without visual highlighting (degraded experience) |
| Tap-to-highlight (rows) | Student taps on rectangle → system reveals row highlighting in distinct colors. Student-initiated, system-executed. | Lesson Section 2 (Mid — Transfer) | Fall back to system auto-highlighting (degraded transfer step) |
| Tap-to-highlight (columns) | Student taps on rectangle → system reveals column highlighting in distinct colors. Student-initiated, system-executed. | Lesson Section 2 (Mid — Transfer) | Fall back to system auto-highlighting (degraded transfer step) |
| Skip-counting animation | Guide narrates count values as system highlights sequential row/column groups ("5... 10... 15!") | Lesson Sections 1-2 | Guide dialogue narrates without animation timing |
| Structure description input | Student selects structure from MC options ("___ rows of ___") | All phases with student action | N/A — MC is the minimum viable interaction |
| Area answer input | Student selects area from MC number options | All phases with student action | ⚠️ AF#3 — modality pending teacher discussion; MC is default |

### Interaction Constraints (All Toys)

* NO verbal/spoken student responses — Guide speaks, student acts
* NO keyboard/text input — all responses via click/tap/MC
* NO open-ended questions requiring typed answers — use selection or action tasks
* Questions in Guide speech must be either rhetorical (Guide answers) or answered through on-screen action
* NO drag-to-place in M3 (M3 is observation/identification, not manipulation)
* Tap-to-highlight is student-INITIATED but system-EXECUTED — student taps to request highlighting; system renders it. Student does not draw or select individual tiles. (AF#5 revised: system-only in S1, tap-to-highlight in S2, off in S3)
* All area answers via MC selection (not typed) — modality pending teacher input (AF#3 deferred); MC is default for drafting

---

# PHASE SPECIFICATIONS

---
# §1.6 WARMUP (2-4 minutes)

### Purpose

Activate M2 tiling knowledge, create felt inefficiency of one-by-one counting, and build motivation for discovering a faster counting strategy — without teaching rows, columns, or skip-counting.

---

### Parameters

| Parameter | Value |
| :---- | :---- |
| **Warmup Type** | Counting Motivation (custom — per TVP) |
| **Interactions** | 2 + bridge |
| **Target Cognitive Load** | 20-30% |
| **Prior Knowledge Activated** | Tiling (M2), one-by-one counting (M1-M2), area as tile count |
| **New Concepts Previewed** | None (motivation only) |
| **Vocabulary Used** | area, tiles, square units, rectangle (all from M1-M2) |
| **Vocabulary Introduced** | None |
| **Toys** | Grid Rectangles (Display) |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Callback to M2's tiling success | Teach rows, columns, or skip-counting |
| Create felt inefficiency of counting one-by-one | Introduce formal vocabulary (row, column, array) |
| Use M1-M2 vocabulary only | Use pressure language or assessment framing |
| End with bridge creating curiosity about faster method | Reveal the "faster way" — that's the Lesson's job |
| Use the 6×4 rectangle (Synthesis callback target) | Use highlighting or structural annotations |

### Warmup Type Rationale

TVP specifies a counting task that creates felt inefficiency: students count a 6×4=24 rectangle one by one, then feel the tedium. This is closest to a modified Notice & Wonder — students notice how long counting takes, which creates the motivating question "Is there a faster way?" The type departs from standard Playbook named types because the TVP specifies a counting ACTION rather than pure observation. The counting task IS the warmup's pedagogical purpose — it must feel slow.

---

### Interaction W.1: Count the Tiles [Type B]

* **Purpose:** Activate M2 knowledge. Student sees a correctly tiled rectangle and counts tiles one by one to find area. The counting itself creates the motivation — 24 tiles is tedious.
* **Visual: Grid Rectangles (Display).** 6×4 rectangle (6 rows, 4 columns). All 24 squares shaded (correct tiling). Full grid visible. No highlighting. Vertical orientation (taller than wide).
* **Guide:** "Here's a rectangle with tiles. No gaps, no overlaps — just like you learned last time. How many square units is the area? Count 'em up."
* **Prompt:** "Count the tiles. What is the area?"
* **Student Action:** MC selection
  * **Options:** 20, 22, 24, 26
* **Correct Answer:** 24
* **Answer Rationale:**
  * 24 = Correct (6×4=24 tiles, all counted)
  * 20 = Miscounted (skipped a row — suggests counting error)
  * 22 = Miscounted (off by 2 — common counting error on larger rectangles)
  * 26 = Miscounted (double-counted — echoes M2's overlap concept)
* **On Correct:** "24 square units. You counted every one."
* **Remediation:** Pipeline

> **Design Note:** The On Correct is deliberately flat — "You counted every one" sets up the payoff in W.2 where counting every one is reframed as inefficient. The 6×4 rectangle is oriented with 6 rows of 4 (vertical) specifically so that when it returns in Synthesis, students skip-count by 4 (Grade 2 prior knowledge): 4, 8, 12, 16, 20, 24.

> **Voice Note:** W.1 opens with a callback to M2 ("No gaps, no overlaps — just like you learned last time") — session-relative language, validates prior learning. Energy is Medium-High per Warmup standard.

---

### Interaction W.2: That Took a While [Type A]

* **Purpose:** Create felt inefficiency. Reframe one-by-one counting as slow and plant the question: "Is there a faster way?" This is the hook — the curiosity gap that drives the entire module.
* **Visual: Grid Rectangles (Display).** Same 6×4 rectangle from W.1. No change to visual — the rectangle stays on screen.
* **Guide:** "That's a lot of counting. What if there were 100 tiles? You'd be counting for a long time. There's a faster way to find the area — without counting every single tile. Want to find out how?"
* **No student action.**

> **Design Note:** W.2 is Pattern 2 (no student action) because the purpose is purely motivational — the Guide creates the curiosity gap. The "What if there were 100 tiles?" escalation makes the inefficiency visceral without actually requiring 100 tiles. "Want to find out how?" is the bridge — it creates anticipation for the Lesson without revealing the strategy. This follows the Warmup Playbook's bridge quality guide: creates a question in the student's mind.

> **Voice Note:** "Want to find out how?" is invitational, not directive. Autonomy support per SDT. Energy shifts from Medium-High (W.1 counting) to genuine curiosity for the bridge.

---

### Verification Checklist (Warmup)

- [x] Hook in first 15-20 seconds — W.1 opens with callback hook + counting task
- [x] 2+ engagement anchors — (1) Personalization: "just like you learned last time" callback; (2) Narrative: "What if there were 100 tiles?" escalation scenario
- [x] 2+ meaningful visual interactions — W.1 (count + MC) + W.2 (observe + bridge)
- [x] 1+ judgment/noticing task — W.1 requires counting and selecting correct area
- [x] Zero formal vocabulary introduced — uses only M1-M2 terms (tiles, area, square units, rectangle)
- [x] Maximum 2 visual states — 1 state (same 6×4 rectangle throughout)
- [x] Clear bridge to Lesson — W.2 creates curiosity: "There's a faster way... Want to find out how?"
- [x] Total time under 5 minutes — 2 interactions, estimated 2-3 minutes
- [x] Cognitive load light (20-30%) — counting is familiar M2 skill; only novelty is the "faster way" question

---

# §1.7 LESSON (8-12 minutes)



---

## Core Purpose + Pedagogical Flow

| Standard CRA | M3 Implementation |
| :---- | :---- |
| **Concrete** (1-2 interactions) | Students observe system-highlighted rows on tiled rectangles, count tiles per row, discover every row has the same number |
| **Relational** (2-3 interactions) | Students compare row-based and column-based views of the same rectangle. Key insight: same area both ways. Multiple rectangles compared for pattern. |
| **Abstract** (1-2 interactions) | Vocabulary formalized: "row," "column," "array." Structure description language: "___ rows of ___" / "___ columns of ___." Skip-counting named as the strategy. |
| **Application** (2-3 interactions) | Students identify structure and skip-count independently with NO highlighting. Increasing rectangle sizes. Both-directions problems. |

---

## Lesson Structure

| Section | Focus | Highlighting | CRA Stage | Interactions | Key Vocabulary |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Purpose Frame | Orientation | None | Pre-CRA | 1 (Pattern 2, Type A) | M1-M2 terms only |
| Section 1: Discovering Rows | Row structure + skip-counting | System auto-highlights rows | Concrete → Relational | 5 (1.1-1.5) | row, "rows of" |
| Section 2: Discovering Columns + Both Directions | Column structure + same-area insight + array | System auto (first exposure) → Tap-to-highlight (transfer) | Relational → Abstract | 5 (2.1-2.5) | column, "columns of," array |
| Section 3: Independence | Structure ID + skip-counting without highlighting | None | Application | 4 (3.1-3.4) | All terms |
| EC Bridge | Transition | None | — | 1 (Pattern 2, Type A) | — |

**Total: 16 interactions** (1 Purpose Frame + 5 Section 1 + 5 Section 2 + 4 Section 3 + 1 EC Bridge)

**Scaffolding Progression (3-step):** System auto-highlight (S1 + S2 first exposure) → Student tap-to-highlight (S2 transfer) → No highlighting (S3/EC). The tap-to-highlight step is the critical transfer mechanism — students move from passive observation to active structure-finding before working independently.

---

## Purpose Frame [Type A]

* **Purpose:** Orient students to what they'll learn and why. Connect backward to M2 (counting every tile) and forward (a faster way). Uses only M1-M2 vocabulary.
* **Visual: Grid Rectangles (Display).** The 6×4 rectangle from Warmup. No highlighting.
* **Guide:** "You already know how to tile rectangles and count every square. That works — but it's slow. Today you're going to find a pattern inside the tiles that lets you count way faster."
* **No student action.**

> **Design Note:** Purpose Frame present per Playbook §1A. Connects backward ("You already know how to tile rectangles") and forward ("a pattern inside the tiles that lets you count way faster"). Uses only M1-M2 vocabulary — no "row," "column," or "skip-count." The word "pattern" is informal and accessible.

---

## Section 1: Discovering Rows (Concrete → Relational)

### Interaction 1.1: Watch the Rows Light Up [Worked Example #1 — Full] [Type A]

* **Purpose:** First exposure to row structure. System highlights rows on a tiled rectangle. Guide narrates the discovery with a think-aloud. This is the pivotal teaching moment — students see tiles organized into groups for the first time.
* **Visual: Grid Rectangles (Display).** 3×5 rectangle (3 rows of 5). All 15 squares shaded. Full grid. System auto-highlights rows one at a time: Row 1 in blue, Row 2 in green, Row 3 in yellow. Each row highlights as Guide narrates.
* **Guide:** [THINK-ALOUD] "Let me show you something. I'm looking at this rectangle, and I notice the tiles make lines going across. Watch — [Row 1 highlights] here's one line. Let me count: 1, 2, 3, 4, 5. Five tiles. [Row 2 highlights] Here's another line: 1, 2, 3, 4, 5. Five again. [Row 3 highlights] And another: 1, 2, 3, 4, 5. Every line has the same number — 5. So instead of counting all 15 tiles, I can count faster: 5... 10... 15. That's 3 groups of 5."
* **No student action.**

> **Scaffolding Note:** This is the full worked example. Guide does ALL the thinking: identifies rows, counts per row, discovers equal count, demonstrates skip-counting. Student observes. The think-aloud uses [PLANNING] ("I'm looking at this rectangle"), [ATTENTION] ("Watch —"), and [SELF-CHECK] ("Every line has the same number"). The word "row" is NOT used yet — Guide says "line" and "group." Formal vocabulary comes after grounding.

---

### Interaction 1.2: How Many in Each Line? [Type C]

* **Purpose:** Example-problem pair — student applies what 1.1 demonstrated. First student action on row structure. Tests whether student can identify the count per row.
* **Visual: Grid Rectangles (Display).** 2×10 rectangle (2 rows of 10). All 20 squares shaded. Full grid. System auto-highlights Row 1 in blue, Row 2 in green.
* **Guide:** "Here's another rectangle. The system highlighted the lines for you. Count the tiles in one line."
* **Prompt:** "How many tiles are in each line?"
* **Student Action:** MC selection
  * **Options:** 2, 5, 10, 20
* **Correct Answer:** 10
* **Answer Rationale:**
  * 10 = Correct (each row has 10 tiles)
  * 2 = Selected the number of rows (groups), not tiles per row
  * 5 = Miscounted (half a row)
  * 20 = Selected total area, not per-row count
* **On Correct:** "10 in each line. And there are 2 lines. So: 10... 20. Twenty square units — without counting every tile."
* **Remediation:** Pipeline

> **Design Note:** The On Correct performs the skip-counting for the student ("10... 20") — modeling the strategy before asking the student to do it. Dimensions 2×10: both from {2, 5, 10}, trivially easy skip-count. The 2-row rectangle makes the structure maximally obvious.

---

### Interaction 1.3: Now You Name It — "Rows" [Type A]

* **Purpose:** Vocabulary formalization — "row." Students have seen two examples of horizontal groupings. Now the Guide names them. Vocabulary-after-grounding principle.
* **Visual: Grid Rectangles (Display).** Same 2×10 rectangle from 1.2 with both rows still highlighted.
* **Guide:** "Those lines going across? They're called rows. A row goes left to right. This rectangle has 2 rows, and each row has 10 tiles. We say: '2 rows of 10.'"
* **No student action.**

> **Voice Note:** The vocabulary introduction is embedded in the Guide's natural speech, not presented as a formal definition. "Those lines going across? They're called rows." is conversational. "We say: '2 rows of 10'" gives the structure-description language.

---

### Interaction 1.4: How Many Rows? [Worked Example #2 — Partial] [Type C]

* **Purpose:** Worked example with partial fading. Student identifies both the number of rows AND the count per row on a new rectangle. Guide provides less scaffolding than 1.1.
* **Visual: Grid Rectangles (Display).** 5×10 rectangle (5 rows of 10). All 50 squares shaded. Full grid. System auto-highlights rows one at a time (5 colors).
* **Guide:** "Here's a bigger rectangle. The rows are lighting up. Count the rows, and count how many are in each row."
* **Prompt:** "How many rows? How many in each row?"
* **Student Action:** MC selection
  * **Options:** "5 rows of 10" / "10 rows of 5" / "5 rows of 5" / "2 rows of 10"
* **Correct Answer:** "5 rows of 10"
* **Answer Rationale:**
  * "5 rows of 10" = Correct (5 horizontal rows, 10 tiles each)
  * "10 rows of 5" = Confused rows with columns (correct numbers, wrong orientation — this is actually the column description, which is valid but not what the highlighting shows)
  * "5 rows of 5" = Correct row count but wrong per-row count
  * "2 rows of 10" = Correct per-row count but wrong row count
* **On Correct:** "5 rows of 10. So instead of counting all 50 tiles: 10... 20... 30... 40... 50."
* **Remediation:** Pipeline

> **Design Note:** This interaction moves to structure-description MC format ("___ rows of ___") which is the assessment format used in EC. Answer option "10 rows of 5" is the column-based description — it's actually mathematically valid but doesn't match what the ROW highlighting shows. This teaches precision in matching description to visual. The On Correct narrates the skip-count sequence, reinforcing the pattern.

> **Scaffolding Note:** Partial fading from 1.1 — Guide no longer narrates the discovery or does the counting. Student identifies structure; Guide narrates the skip-count payoff.

---

### Interaction 1.5: Your Turn to Skip-Count [Type B]

* **Purpose:** Student applies skip-counting to determine area. First time student is responsible for the final area answer using row structure.
* **Visual: Grid Rectangles (Display).** 2×5 rectangle (2 rows of 5). All 10 squares shaded. Full grid. System auto-highlights 2 rows.
* **Guide:** "2 rows of 5. Skip-count by the rows to find the area."
* **Prompt:** "What is the area? Skip-count by rows."
* **Student Action:** MC selection
  * **Options:** 5, 7, 10, 25
* **Correct Answer:** 10
* **Answer Rationale:**
  * 10 = Correct (5 + 5 = 10, or skip-count: 5, 10)
  * 5 = Only counted one row
  * 7 = Added 5 + 2 (confused rows with per-row count)
  * 25 = Multiplied 5 × 5 (wrong operation)
* **On Correct:** "5... 10. Ten square units. Rows make counting faster."
* **Remediation:** Pipeline

> **Design Note:** This is the 2×5 rectangle that returns in Section 2 for the "same answer both ways" moment. Area 10 is trivially easy to verify, so the cognitive demand is on the PROCESS (using rows) not the ARITHMETIC. Deliberate reuse documented in Dimension Tracking.

---

## Section 2: Discovering Columns + Both Directions (Relational → Abstract)

**Scaffolding shift in Section 2:** System auto-highlight for first column exposure (2.1-2.2), then **tap-to-highlight** for transfer practice (2.3-2.4), then array vocabulary capstone (2.5). The tap-to-highlight step is where students move from "the system showed me structure" to "I can find structure myself."

### Interaction 2.1: Now Watch the Other Direction [Worked Example #3 — Partial] [Type C]

* **Purpose:** Introduce column structure. System highlights columns on the SAME 2×5 rectangle from 1.5. This sets up the key insight: columns give the same area as rows. System auto-highlight here because this is the student's FIRST exposure to column structure — they need to see it before they can find it.
* **Visual: Grid Rectangles (Display).** Same 2×5 rectangle (2 rows of 5). System auto-highlights COLUMNS one at a time: 5 columns, each containing 2 tiles. Different colors per column.
* **Guide:** "Same rectangle. But now watch — the system is highlighting a different direction. Going up and down instead of across. Count the tiles in each group."
* **Prompt:** "How many tiles in each up-and-down group?"
* **Student Action:** MC selection
  * **Options:** 2, 5, 7, 10
* **Correct Answer:** 2
* **Answer Rationale:**
  * 2 = Correct (each column has 2 tiles)
  * 5 = Counted the number of columns, not tiles per column
  * 7 = Added 2 + 5
  * 10 = Total area, not per-column count
* **On Correct:** "2 tiles in each group. And there are 5 of those groups going up and down. So: 2... 4... 6... 8... 10. Same answer — 10 square units."
* **Remediation:** Pipeline

> **Design Note:** This is the CRITICAL pedagogical moment — same rectangle, different direction, SAME AREA. The On Correct makes this explicit: "Same answer — 10 square units." The 2×5 rectangle was chosen for this moment because both skip-counts are trivially easy (by 5 and by 2), so the ONLY thing landing is the insight. Per TVP: "Both trivially easy, so the insight is the ONLY thing landing." System auto-highlight is used here (not tap-to-highlight) because column structure must be SHOWN before students can FIND it.

---

### Interaction 2.2: Columns — The Name [Type A]

* **Purpose:** Vocabulary formalization — "column." Same pattern as 1.3 (row naming).
* **Visual: Grid Rectangles (Display).** Same 2×5 rectangle with columns still highlighted.
* **Guide:** "Those groups going up and down? They're called columns. A column goes top to bottom. This rectangle has 5 columns of 2. And look — 5 columns of 2 gives you the same area as 2 rows of 5. Ten square units either way."
* **No student action.**

> **Voice Note:** "And look —" creates a genuine moment of connection. The Guide explicitly states the key insight rather than waiting for the student to discover it (per Lesson Playbook §4B: "State key insight explicitly").

---

### Interaction 2.3: Describe It Both Ways [Type C]

* **Purpose:** Student practices structure description in BOTH directions using **tap-to-highlight**. This is the critical TRANSFER step — student actively uses the tool to reveal structure rather than passively observing system highlighting. Relational — comparing row and column views of the same rectangle.
* **Visual: Grid Rectangles (Display).** 4×5 rectangle (4 rows of 5). All 20 tiles shaded. Full grid. No initial highlighting. Student taps to reveal.
* **Guide:** "You know what rows and columns look like now. Tap on the rectangle to highlight the rows."
* **Student Action:** Tap-to-Highlight (rows). System reveals row highlighting (4 rows in different colors).
* **Guide (after tap):** "There they are — 4 rows. How would you describe this rectangle using rows?"
* **Prompt:** "Describe using rows: ___ rows of ___"
* **Student Action:** MC selection (Part a)
  * **Options:** "4 rows of 5" / "5 rows of 4" / "4 rows of 4" / "5 rows of 5"
* **Correct Answer:** "4 rows of 5"
* **Answer Rationale:**
  * "4 rows of 5" = Correct (4 horizontal rows, 5 tiles each)
  * "5 rows of 4" = Reversed (this is the column description)
  * "4 rows of 4" = Wrong per-row count
  * "5 rows of 5" = Wrong row count AND per-row count
* **On Correct:** "4 rows of 5. Now tap to highlight the columns."
* **Student Action:** Tap-to-Highlight (columns). System reveals column highlighting (5 columns in different colors), replacing row highlighting.
* **Prompt:** "Describe using columns: ___ columns of ___" (Part b)
* **Student Action:** MC selection (Part b)
  * **Options:** "5 columns of 4" / "4 columns of 5" / "5 columns of 5" / "4 columns of 4"
* **Correct Answer:** "5 columns of 4"
* **On Correct:** "5 columns of 4. Both give you the same area: 20 square units."
* **Remediation:** Pipeline

> **Scaffolding Note:** This is the first TAP-TO-HIGHLIGHT interaction. The student initiates highlighting — the system executes it. This is the transfer step: students move from "the system showed me" (2.1) to "I can find it myself" (2.3). Multi-step interaction: tap rows → MC (rows) → tap columns → MC (columns). The Guide cues the tap explicitly ("Tap on the rectangle to highlight the rows") because this is the student's first time using the tool.

> **Design Note:** Same pedagogical content as old 2.4, but the interaction modality shifts from passive observation to active tool use. The structure-description MC format ("___ rows of ___") is unchanged.

---

### Interaction 2.4: Skip-Count Both Ways [Type B]

* **Purpose:** Student skip-counts using BOTH rows and columns on the same rectangle using **tap-to-highlight**. Confirms same area both ways with a larger rectangle. Continued tap-to-highlight practice — less Guide scaffolding than 2.3.
* **Visual: Grid Rectangles (Display).** 3×10 rectangle (3 rows of 10). All 30 tiles shaded. Full grid. No initial highlighting. Student taps to reveal.
* **Guide:** "Here's a bigger one. Tap to highlight the rows, then skip-count to find the area."
* **Student Action:** Tap-to-Highlight (rows). System reveals row highlighting (3 rows in different colors).
* **Prompt:** "What is the area? Skip-count by rows."
* **Student Action:** MC selection (Part a)
  * **Options:** 13, 20, 30, 40
* **Correct Answer:** 30
* **Answer Rationale:**
  * 30 = Correct (10 + 10 + 10 = 30)
  * 13 = Added 3 + 10 instead of skip-counting
  * 20 = Only counted 2 rows
  * 40 = Added an extra row
* **On Correct:** "10... 20... 30. Now tap to highlight the columns. Skip-count by columns."
* **Student Action:** Tap-to-Highlight (columns). System reveals column highlighting (10 columns in different colors).
* **Prompt:** "What is the area? Skip-count by columns." (Part b)
* **Student Action:** MC selection (Part b)
  * **Options:** 13, 20, 30, 40
* **Correct Answer:** 30
* **On Correct:** "3... 6... 9... 12... 15... 18... 21... 24... 27... 30. Same answer — 30 square units. Rows or columns, it always works."
* **Remediation:** Pipeline

> **Scaffolding Note:** Second tap-to-highlight interaction. Guide scaffolding is reduced from 2.3 — no "You know what rows and columns look like now" setup, just direct instruction "Tap to highlight the rows." Student is gaining fluency with the tool.

> **Design Note:** The column skip-count (by 3s: 3, 6, 9... 30) is longer and harder than the row skip-count (by 10s: 10, 20, 30). This makes the "same answer" insight more impressive — even though one path is harder, both arrive at 30. The On Correct narrates the full column skip-count sequence to model it.

---

### Interaction 2.5: Array — You've Seen This Before [Type A]

* **Purpose:** Vocabulary callback — "array." Capstone naming moment for Section 2. Students have now discovered rows, discovered columns, practiced describing both directions, and confirmed "same area both ways." NOW the Guide names the whole arrangement. Per AF#1 resolution: callback from Unit 1, not new introduction.
* **Visual: Grid Rectangles (Display).** 3×5 rectangle (from 1.1). All 15 tiles shaded. No highlighting — students see the full rectangle.
* **Guide:** "Rows and columns together — you've been working with these the whole time. Equal rows and equal columns. That's called an array. This is a 3-by-5 array: 3 rows of 5, or 5 columns of 3."
* **No student action.**

> **Design Note:** Moved from old position (2.3) to section capstone (2.5) per author feedback — students now have full practice with both-direction descriptions before absorbing a third vocabulary term. The arc is cleaner: discover columns (2.1) → name columns (2.2) → practice both directions with tap-to-highlight (2.3-2.4) → name the whole arrangement (2.5). Per AF#1 resolution, "array" is a callback from Unit 1 (Decision #4). "You've been working with these the whole time" is stronger callback language than the previous version because students genuinely HAVE been working with arrays throughout Sections 1-2. The "3-by-5" naming convention introduces the compact description format.

---

## Section 3: Independence (Application)

### Interaction 3.1: No Highlighting — You See It [Type C]

* **Purpose:** First independent structure identification. No system highlighting. Student must visually identify rows and columns from the grid alone.
* **Visual: Grid Rectangles (Display).** 4×10 rectangle (4 rows of 10). All 40 tiles shaded. Full grid. NO highlighting.
* **Guide:** "No highlighting this time. Look at the rectangle. Can you see the rows? Describe the structure, then find the area."
* **Prompt:** "Which describes this rectangle?"
* **Student Action:** MC selection (Part a — structure)
  * **Options:** "4 rows of 10" / "10 rows of 4" / "5 rows of 8" / "4 rows of 8"
* **Correct Answer:** "4 rows of 10"
* **On Correct:** "4 rows of 10. Now find the area."

* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 14, 30, 40, 50
* **Correct Answer:** 40
* **On Correct:** "10... 20... 30... 40. Forty square units."
* **Remediation:** Pipeline

> **Scaffolding Note:** First interaction without highlighting. Guide explicitly cues "Can you see the rows?" to direct attention. Multi-step: structure first, then area. This is the EC format — structure identification BEFORE area calculation.

---

### Interaction 3.2: Describe It Your Way [Type B]

* **Purpose:** Student chooses whether to describe by rows or columns. Tests flexible structure-seeing.
* **Visual: Grid Rectangles (Display).** 5×4 rectangle (5 rows of 4). All 20 tiles shaded. Full grid. NO highlighting.
* **Guide:** "Here's another one. You can describe it using rows OR columns — your choice. Then find the area."
* **Prompt:** "Describe this rectangle using rows or columns."

* **Student Action:** MC selection (Part a — structure, either direction valid)
  * **Options:** "5 rows of 4" / "4 columns of 5" / "5 rows of 5" / "4 rows of 4"
* **Correct Answer:** "5 rows of 4" OR "4 columns of 5" (both accepted)
* **Answer Rationale:**
  * "5 rows of 4" = Correct (row description)
  * "4 columns of 5" = Correct (column description)
  * "5 rows of 5" = Wrong per-row count
  * "4 rows of 4" = Wrong row count
* **On Correct (if "5 rows of 4"):** "5 rows of 4. Now find the area."
* **On Correct (if "4 columns of 5"):** "4 columns of 5. Now find the area."

* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 9, 15, 20, 25
* **Correct Answer:** 20
* **On Correct:** "20 square units. Whether you used rows or columns — same answer."
* **Remediation:** Pipeline

> **Design Note:** Dual-correct MC is an engineering consideration — system must accept either valid structure description. If dual-correct is not supported, default to row-based answer as primary with column-based as an alternative correct answer flagged in the validator. Flag as KDD.

---

### Interaction 3.3: Bigger Rectangle [Type B]

* **Purpose:** Larger rectangle to demonstrate efficiency advantage of structured counting.
* **Visual: Grid Rectangles (Display).** 5×10 rectangle (5 rows of 10). All 50 tiles shaded. Full grid. NO highlighting.
* **Guide:** "This one's big. Counting every tile would take a while. Use what you know — describe the structure and find the area."
* **Prompt:** "Which describes this rectangle?"
* **Student Action:** MC selection (Part a — structure)
  * **Options:** "5 rows of 10" / "10 rows of 5" / "5 rows of 5" / "10 rows of 10"
* **Correct Answer:** "5 rows of 10"

* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 15, 40, 50, 100
* **Correct Answer:** 50
* **On Correct:** "10... 20... 30... 40... 50. Fifty square units — and you didn't need to count every tile."
* **Remediation:** Pipeline

> **Design Note:** 5×10=50 is the largest area in M3 (at TVP's max). The On Correct emphasizes efficiency: "you didn't need to count every tile." This echoes the Warmup's motivation.

---

### Interaction 3.4: EC Bridge [Type A]

* **Purpose:** Transition to Exit Check. Brief, warm, forward-looking.
* **Visual: Grid Rectangles (Display).** The 5×10 rectangle from 3.3.
* **Guide:** "You can see rows, you can see columns, and you can skip-count to find the area. Let's see what you know."
* **No student action.**

> **Voice Note:** "Let's see what you know" follows the Lesson Playbook's standard bridge to EC. Energy is Confident + Forward-looking. Brief — 10 seconds max.

---

## Module-Specific Lesson Guidance

### Required Phrases
* "No gaps, no overlaps" (callback to M2 — reinforce when relevant)
* "___ rows of ___" / "___ columns of ___" (structure description format)
* "Same answer" / "Same area" (when comparing row vs. column counts)
* "Skip-count" (name for the counting strategy)

### Forbidden Phrases
* "multiply" / "multiplication" / "times" (M4)
* "product" / "factor" (M4-M5)
* "length" / "width" / "dimensions" (M7+)
* "formula" (M7+)
* "perimeter" (NOT in Unit 2)
* Skip-count by 6, 7, 8, 9 (not Grade 2 prior knowledge)
* "array" before Interaction 2.5 (vocabulary-after-grounding — moved to section capstone per author review)

### Misconception Prevention

**#2.0 (Counting One-by-One):** The three-section structure (highlighting → both directions → no highlighting) progressively transfers structural seeing from the system to the student. Requiring structure identification BEFORE area calculation (starting at 1.4) prevents students from bypassing structure through brute-force counting. The EC enforces this by requiring structure MC before accepting area answers.

**#9.0 (Array Structure Not Seen):** System-driven highlighting in Sections 1-2 provides perceptual scaffolding. Multiple rectangles with the same highlighting treatment build the internal model. The "same answer both ways" insight (2.1-2.2) makes structure salient by showing its power.

### Incomplete Script Flags (§1.7.4)

* **Skip-counting animation timing:** How does the system sync row/column highlighting with the Guide's skip-count narration? Timing is critical — each row should highlight AS the Guide says the corresponding number. Engineering specification needed.
* **Tap-to-highlight UX:** How does the student initiate tap-to-highlight? Options: (a) student taps on the rectangle and system auto-detects row vs. column intent from tap direction; (b) student taps a "Show Rows" / "Show Columns" button; (c) student taps anywhere and system highlights in the direction specified by the Guide. Engineering specification needed. The SP specifies the INTENT (student initiates, system executes) — the exact UI mechanism is an engineering decision.
* **Dual-correct MC in 3.2:** System must accept two valid answers. If not supported, need fallback design.
* **Area answer modality (AF#3):** All area answers drafted as MC. Pending teacher discussion may change to click-to-set counter or other input.

### Success Criteria (§1.7.5)

* Student can identify "___ rows of ___" for a tiled rectangle without highlighting
* Student can identify "___ columns of ___" for the same rectangle
* Student can skip-count by rows OR columns to determine area
* Student recognizes that row-based and column-based counting give the same area
* Student can describe the arrangement as an "array" (callback from Unit 1)

---

## Verification Checklist (Lesson)

- [x] **2-3 worked examples:** 1.1 (Full — think-aloud), 1.4 (Partial), 2.1 (Partial). Three worked examples with fading. ✓
- [x] **Every observation followed by explicit instruction:** 1.1 observation → Guide states pattern explicitly; 2.1 observation → Guide states "Same answer." ✓
- [x] **No "What do you notice?" without follow-up:** Not used. All observations are Guide-directed ("Watch —", "Notice how"). ✓
- [x] **Vocabulary after visual experience:** "Row" introduced in 1.3 (after 1.1-1.2 grounding). "Column" in 2.2 (after 2.1 grounding). "Array" in 2.5 (section capstone, after both-direction tap-to-highlight practice). ✓
- [x] **Key insights stated explicitly:** "Every line has the same number" (1.1), "Same answer — 10 square units" (2.1), "Rows or columns, it always works" (2.4). ✓
- [x] **Purpose Frame present:** Yes, before Section 1. Uses M1-M2 vocabulary only. ✓
- [x] **CRA phases each have dedicated interactions:** Concrete (1.1-1.2), Relational (1.4-1.5, 2.1-2.2, 2.3-2.4), Abstract (1.3, 2.2, 2.5), Application (3.1-3.3). ✓
- [x] **Relational is SEPARATE:** 2.1 (same rectangle, different direction) and 2.3 (describe both ways with tap-to-highlight) are dedicated comparison interactions, not embedded in vocabulary. ✓
- [x] **Students ACT in every Pattern 1 interaction:** 1.2, 1.4, 1.5, 2.1, 2.3 (tap+MC), 2.4 (tap+MC), 3.1, 3.2, 3.3 all have student action. ✓
- [x] **6+ interactions:** 15 interactions (excluding Purpose Frame and EC Bridge). ✓
- [x] **Think-aloud present:** 1.1 has [PLANNING], [ATTENTION], [SELF-CHECK] elements. ✓
- [x] **Guide/Prompt independence verified:** Spot-checked 1.2 (Prompt: "How many tiles in each line?" — student knows what to do without Guide); 1.4 (Prompt: "How many rows? How many in each row?" — complete); 3.1 (Prompt: "Which describes this rectangle?" — complete standalone). ✓
- [x] **All toys from §1.5:** Grid Rectangles (Display) only. No other toys used. ✓
- [x] **No forbidden vocabulary:** Scanned all Guide/Prompt lines. No multiplication language, no forbidden terms. "Array" appears only in/after 2.3. ✓
- [x] **Vocabulary staging matches §1.3:** Row → 1.3 (Section 1) ✓. Column → 2.2 (Section 2) ✓. Array → 2.5 (Section 2, capstone) ✓. ✓
- [x] **Scaffolding fading documented:** System auto-highlight (S1 + S2 first exposure) → Tap-to-highlight (S2 transfer: 2.3-2.4) → No highlight (S3). Three-step progression restored per author review. ✓

---

# §1.8 EXIT CHECK (3-5 minutes)

## Parameters

| Parameter | Value |
| :---- | :---- |
| **Phase** | Exit Check |
| **Duration** | 3-5 minutes |
| **Problem Count** | 4 (per TVP — distinct assessed skills) |
| **Cognitive Types** | IDENTIFY (EC.1, EC.3, EC.4), CREATE (EC.2) |
| **Toy** | Grid Rectangles (Display) — same as Lesson |
| **Highlighting** | None — matches Lesson Section 3 independence |
| **Interaction** | MC selection — same as Lesson |
| **Vocabulary** | row, column, array, area, square units — all from Lesson |
| **New Concepts** | None |

## Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Test skills taught in Lesson Sections 1-3 | Introduce new visual models or interaction types |
| Use Grid Rectangles (Display) with full grid | Use highlighting (EC = independent assessment) |
| Require structure identification BEFORE area | Allow area-only answers that bypass structure |
| Use MC selection (same as Lesson) | Change to free-response or other input types |
| Use dimensions different from Lesson values | Reuse exact Lesson rectangle dimensions |
| Sequence simple → complex | Front-load the hardest problem |
| Keep feedback brief (5-10 words) | Re-teach concepts in feedback |

## Alignment Check

| EC Problem | Lesson Section Tested | Skill Assessed | Cognitive Type | Toy/Mode Match |
| :---- | :---- | :---- | :---- | :---- |
| EC.1 | Section 1 (row discovery) + Section 3 (independence) | Identify row structure + determine area via skip-counting | IDENTIFY | Grid Rectangles (Display), MC, no highlighting ✓ |
| EC.2 | Section 1-2 (structure description) + Section 3 | Construct structure description ("___ rows of ___") + area | CREATE | Grid Rectangles (Display), MC, no highlighting ✓ |
| EC.3 | Sections 1-3 (skip-counting strategy) | Validate skip-counting on a tall rectangle (10×2); long sequence makes strategy visible | IDENTIFY | Grid Rectangles (Display), MC, no highlighting ✓ |
| EC.4 | Section 2 (column discovery + both directions) | Describe same rectangle using columns; confirm same area | IDENTIFY | Grid Rectangles (Display), MC, no highlighting ✓ |

## Transition Frame [Type A]

* **Purpose:** Signal shift from Lesson to assessment. Low-stakes framing.
* **Visual:** The 5×10 rectangle from interaction 3.3 remains on screen (continuity from EC Bridge).
* **Guide:** "You found rows, columns, and faster ways to count. Let's see what you know — four quick questions."
* **No student action.**

> **Voice Note:** "Let's see what you know" echoes the EC Bridge (3.4). "Four quick questions" sets expectations without creating test anxiety. Tone is confident, warm — the student just succeeded in Section 3.

---

### EC Problem 1: Identify the Structure [IDENTIFY] [Type C]

* **Purpose:** Can the student identify row structure of a rectangle without highlighting? Tests the core skill from Section 1 + Section 3.
* **Visual: Grid Rectangles (Display).** 3×4 rectangle (3 rows of 4). All 12 squares shaded. Full grid. NO highlighting.
* **Prompt:** "Which describes this rectangle?"
* **Student Action:** MC selection (Part a — structure)
  * **Options:** "3 rows of 4" / "4 rows of 3" / "3 rows of 3" / "4 rows of 4"
* **Correct Answer:** "3 rows of 4"
* **Answer Rationale:**
  * "3 rows of 4" = Correct (3 horizontal rows, 4 tiles each)
  * "4 rows of 3" = Confused rows/columns (column description)
  * "3 rows of 3" = Correct row count, wrong per-row count
  * "4 rows of 4" = Wrong row count, correct per-row count
* **On Correct:** "3 rows of 4. What's the area?"
* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 7, 10, 12, 16
* **Correct Answer:** 12
* **Answer Rationale:**
  * 12 = Correct (4 + 4 + 4 = 12)
  * 7 = Added 3 + 4
  * 10 = Common round-number error
  * 16 = 4 × 4 (used one dimension twice)
* **On Correct:** "12 square units."
* **Remediation:** Pipeline

> **Design Note:** 3×4 is NEW — not used in any Lesson interaction. Area 12 is within range (10-50). Structure → area order enforces the "structure before area" principle. Both dimensions from {2, 3, 4, 5, 10}. Skip-counting by 4 is Grade 2 prior knowledge.

---

### EC Problem 2: Describe the Structure [CREATE] [Type B]

* **Purpose:** Can the student construct a complete structure description for a larger rectangle? Tests structure-description language from Sections 1-2.
* **Visual: Grid Rectangles (Display).** 5×3 rectangle (5 rows of 3). All 15 squares shaded. Full grid. NO highlighting. Vertical orientation (taller than wide).
* **Guide:** "How many rows? How many in each row?"
* **Prompt:** "Describe this rectangle."
* **Student Action:** MC selection (Part a — structure)
  * **Options:** "5 rows of 3" / "3 rows of 5" / "5 rows of 5" / "3 rows of 3"
* **Correct Answer:** "5 rows of 3"
* **Answer Rationale:**
  * "5 rows of 3" = Correct (5 horizontal rows, 3 tiles each)
  * "3 rows of 5" = Confused rows/columns (would be the column description: 3 columns of 5)
  * "5 rows of 5" = Wrong per-row count
  * "3 rows of 3" = Wrong row count
* **On Correct:** "5 rows of 3. What's the area?"
* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 8, 12, 15, 20
* **Correct Answer:** 15
* **Answer Rationale:**
  * 15 = Correct (3 + 3 + 3 + 3 + 3 = 15, or skip-count: 3, 6, 9, 12, 15)
  * 8 = Added 5 + 3
  * 12 = Off by one skip-count (stopped at 4 × 3)
  * 20 = 5 × 4 (wrong per-row count)
* **On Correct:** "15 square units."
* **Remediation:** Pipeline

> **Design Note:** 5×3 is the VERTICAL orientation of 3×5 used in Lesson 1.1 and 2.5 — but the key difference is the orientation (5 rows instead of 3). This tests whether students can apply structure identification regardless of orientation, not just on rectangles they've seen before. Classified as CREATE because the Guide's prompt ("How many rows? How many in each row?") asks the student to construct the description, not just recognize a pre-stated one. Area 15 is in-range. Skip-counting by 3 is Grade 2 prior knowledge.

> **Dimension Note:** 5×3 vs. Lesson's 3×5 — these are DIFFERENT rectangles (different orientation, different row/column counts). 3×5 has 3 rows of 5; 5×3 has 5 rows of 3. The visual layout is distinct. This is NOT dimension reuse.

---

### EC Problem 3: Skip-Count to Find Area [IDENTIFY] [Type B]

* **Purpose:** Validates that the student uses skip-counting (not one-by-one) to determine area. Tests the core efficiency strategy from Sections 1-3. A tall rectangle (10 rows of 2) makes the skip-counting process highly visible — the student must skip-count through 10 steps, making the strategy unmistakable.
* **Visual: Grid Rectangles (Display).** 10×2 rectangle (10 rows of 2). All 20 squares shaded. Full grid. NO highlighting. Tall, narrow orientation.
* **Guide:** "You can see the rows. Skip-count to find the area."
* **Prompt:** "What is the area? Skip-count by rows."
* **Student Action:** MC selection
  * **Options:** 12, 15, 20, 30
* **Correct Answer:** 20
* **Answer Rationale:**
  * 20 = Correct (2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 = 20, or skip-count: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
  * 12 = Added 10 + 2 (added dimensions instead of skip-counting)
  * 15 = Miscounted (stopped early or confused with EC.2's area)
  * 30 = 10 × 3 (wrong per-row count)
* **On Correct:** "2... 4... 6... all the way to 20. Twenty square units."
* **Remediation:** Pipeline

> **Design Note:** 10×2 is the ROTATION of Lesson's 2×10 — but a genuinely different rectangle (10 rows of 2 vs. 2 rows of 10). The tall orientation with 10 rows of 2 makes this a distinctive visual experience. The long skip-count by 2s (ten steps) tests whether the student has truly internalized skip-counting as a strategy — one-by-one counting on 20 tiles would feel tedious, making the efficiency advantage of skip-counting palpable. Area 20 is distinct from EC.1 (12), EC.2 (15), and EC.4 (8). Skip-counting by 2 is the easiest increment (Grade 2 prior knowledge).

---

### EC Problem 4: Find the Area Using Columns [IDENTIFY] [Type C]

* **Purpose:** Tests flexible structure-seeing — can the student describe and count using columns? Tests the key insight from Section 2: same area both ways.
* **Visual: Grid Rectangles (Display).** 2×4 rectangle (2 rows of 4). All 8 squares shaded. Full grid. NO highlighting.
* **Guide:** "You described rectangles using rows. Now try columns."
* **Prompt:** "Describe this rectangle using columns: ___ columns of ___"
* **Student Action:** MC selection (Part a — column structure)
  * **Options:** "4 columns of 2" / "2 columns of 4" / "4 columns of 4" / "2 columns of 2"
* **Correct Answer:** "4 columns of 2"
* **Answer Rationale:**
  * "4 columns of 2" = Correct (4 vertical columns, 2 tiles each)
  * "2 columns of 4" = Confused columns/rows (this is the row description: 2 rows of 4)
  * "4 columns of 4" = Wrong per-column count
  * "2 columns of 2" = Wrong column count AND per-column count
* **On Correct:** "4 columns of 2. What's the area?"
* **Prompt:** "What is the area?" (Part b — area)
* **Student Action:** MC selection (Part b)
  * **Options:** 6, 8, 10, 12
* **Correct Answer:** 8
* **Answer Rationale:**
  * 8 = Correct (2 + 2 + 2 + 2 = 8, or skip-count by columns: 2, 4, 6, 8)
  * 6 = Added 4 + 2
  * 10 = Common round-number error
  * 12 = 4 × 3 (wrong dimension)
* **On Correct:** "8 square units. Rows or columns — same area."
* **Remediation:** Pipeline

> **Design Note:** EC.4 is the COLUMN problem, testing the Section 2 insight. The Guide explicitly cues "Now try columns" — assessing flexible structure-seeing per TVP EC Problem 4 specification ("Can you find the area by counting columns too?"). 2×4 is a NEW rectangle not used in Lesson. Area 8 is at the low end of range but appropriate for column assessment — keeping arithmetic trivial so the cognitive demand is on column identification, not skip-counting difficulty. Skip-counting by 2 is the easiest possible.

> **Design Note (Area Range):** 2×4 = 8 is within the Backbone's EC area range of 6-50. Backbone §1.5 Data Constraints updated to reflect that EC problems may use smaller areas when the assessed skill is structural rather than computational.

---

## EC Verification Checklist

- [x] **Each problem maps to specific Lesson content:**
  - EC.1 → Section 1 (row structure ID) + Section 3 (independence)
  - EC.2 → Sections 1-2 (structure description language) + Section 3
  - EC.3 → Sections 1-3 (skip-counting strategy, 10×2)
  - EC.4 → Section 2 (column structure + both directions)
- [x] **All 4 problems test SAME core concept:** Row/column structure identification + skip-counting for area
- [x] **4 problems, simple to complex:** EC.1 (basic row ID) → EC.2 (construct description) → EC.3 (skip-count process) → EC.4 (column flexibility)
- [x] **Same visual model as Lesson:** Grid Rectangles (Display), full grid, pre-tiled ✓
- [x] **Same interaction type as Lesson:** MC selection ✓
- [x] **No highlighting:** All 4 problems have no highlighting (matches S3/EC) ✓
- [x] **Brief feedback:** All On Correct responses ≤10 words + optional skip-count model ✓
- [x] **No new concepts introduced:** All vocabulary, toy modes, and interaction types from Lesson ✓
- [x] **No re-teaching in feedback:** On Correct responses confirm, don't teach ✓
- [x] **Structure before area:** EC.1, EC.2, EC.4 all require structure MC before area MC ✓. EC.3 is area-only but Guide cues "Skip-count by rows" which implicitly references structure. ✓
- [x] **Cognitive types varied:** IDENTIFY (EC.1, EC.3, EC.4), CREATE (EC.2) ✓
- [x] **Cognitive types appropriate for M1-3:** CREATE and IDENTIFY only ✓. COMPARE deferred to Practice (15% Area Comparison target) where it is assessed with APPLY cognitive type per TVP.
- [x] **EC dimensions differ from Lesson:** 3×4, 5×3, 10×2, 2×4 — none are exact matches of Lesson rectangles (10×2 is rotation of Lesson's 2×10) ✓
- [x] **All EC areas distinct:** 8, 12, 15, 20 — no overlaps within EC ✓
- [x] **Difficulty is representative middle:** Not the simplest (2×5=10) or hardest (5×10=50) Lesson values ✓
- [x] **Transition frame present:** Yes, before EC.1 ✓
- [x] **All dimensions within {2, 3, 4, 5, 10}:** 3×4 ✓, 5×3 ✓, 10×2 ✓, 2×4 ✓

---

# §1.8.5 PRACTICE INPUTS

## Practice Phase Overview

Practice is generated by the Pipeline (adaptive engine), not fully scripted in the SP. The SP provides inputs that constrain the Pipeline's problem generation. These inputs define what rectangles, skill types, and anti-pattern detections the Pipeline uses.

---

## Distribution Targets

| Skill Category | Target % | Description | Aligns To |
| :---- | :---- | :---- | :---- |
| **Structure Identification (Row)** | 25% | "___ rows of ___" MC before area | Lesson Section 1 |
| **Structure Identification (Column)** | 15% | "___ columns of ___" MC before area | Lesson Section 2 |
| **Structure Identification (Both)** | 15% | Describe BOTH row AND column for same rectangle | Lesson Section 2-3 |
| **Skip-Count Area (Row)** | 20% | Skip-count by rows to find area | Lesson Sections 1-3 |
| **Skip-Count Area (Column)** | 10% | Skip-count by columns to find area | Lesson Section 2 |
| **Area Comparison** | 15% | Compare areas of two rectangles using structure | Lesson Section 3 extension |

> **Design Note:** Row-focused skills (Structure Row + Skip-Count Row = 45%) outweigh column-focused (Structure Column + Skip-Count Column = 25%), reflecting the Lesson's emphasis: rows are introduced first and practiced longer. Both-directions (15%) tests the Section 2 "same area" insight. Area Comparison (15%) is the Practice-phase extension using APPLY cognitive type (per EC Playbook: APPLY reserved for Practice).

---

## Toy Constraints

| Aspect | Constraint | Rationale |
| :---- | :---- | :---- |
| **Toy** | Grid Rectangles (Display) | Only toy in M3 |
| **Grid State** | Full grid, always visible | Decision #3 (M1-M4 full grids) |
| **Pre-tiled** | All rectangles fully tiled | M3 is display-only (no tiling) |
| **Highlighting** | None (Practice = independent) | Post-EC independence level |
| **Interaction** | MC selection (structure + area) | Same as Lesson + EC |
| **Orientations** | Both horizontal and vertical | Match Lesson variety |

---

## Dimension Constraints

| Constraint | Value | Rationale |
| :---- | :---- | :---- |
| **Dimension pool** | {2, 3, 4, 5, 10} | Backbone §1.5; skip-counting within Grade 2 prior knowledge |
| **Area range** | 6-50 square units | Products within 60 (Learning Goals); max = 5×10=50 |
| **Skip-count increments** | 2, 3, 4, 5, 10 only | Grade 2 prior knowledge; no 6-9 increments |
| **Exclude exact Lesson values** | Prefer fresh orientations | Except when pedagogically justified (KDD) |
| **Both dimensions within pool** | Always | No 6×7, 7×8 etc. |

### Available Rectangle Pool (for Pipeline)

| Rectangle | Area | Row Skip-Count | Column Skip-Count | Notes |
| :---- | :---- | :---- | :---- | :---- |
| 2×3 | 6 | by 3 (3, 6) | by 2 (2, 4, 6) | Smallest in range |
| 2×4 | 8 | by 4 (4, 8) | by 2 (2, 4, 6, 8) | Used in EC.4 — reduce frequency |
| 2×5 | 10 | by 5 (5, 10) | by 2 (2, 4, 6, 8, 10) | Used in Lesson 1.5/2.1 — reduce frequency |
| 2×10 | 20 | by 10 (10, 20) | by 2 (2, 4...20) | Used in Lesson 1.2-1.3 — reduce frequency |
| 3×2 | 6 | by 2 (2, 4, 6) | by 3 (3, 6) | Rotation of 2×3 |
| 3×4 | 12 | by 4 (4, 8, 12) | by 3 (3, 6, 9, 12) | Used in EC.1 — reduce frequency |
| 3×5 | 15 | by 5 (5, 10, 15) | by 3 (3, 6, 9, 12, 15) | Used in Lesson 1.1/2.5 — reduce frequency |
| 3×10 | 30 | by 10 (10, 20, 30) | by 3 (3, 6...30) | Used in Lesson 2.4 — reduce frequency |
| 4×2 | 8 | by 2 (2, 4, 6, 8) | by 4 (4, 8) | Rotation of 2×4 |
| 4×3 | 12 | by 3 (3, 6, 9, 12) | by 4 (4, 8, 12) | Fresh for Practice |
| 4×5 | 20 | by 5 (5, 10, 15, 20) | by 4 (4, 8, 12, 16, 20) | Used in Lesson 2.3 — reduce frequency |
| 4×10 | 40 | by 10 (10, 20, 30, 40) | by 4 (4, 8...40) | Used in Lesson 3.1 — reduce frequency |
| 5×2 | 10 | by 2 (2, 4, 6, 8, 10) | by 5 (5, 10) | Rotation of 2×5 |
| 5×3 | 15 | by 3 (3, 6, 9, 12, 15) | by 5 (5, 10, 15) | Used in EC.2 — reduce frequency |
| 5×4 | 20 | by 4 (4, 8, 12, 16, 20) | by 5 (5, 10, 15, 20) | Used in Lesson 3.2 — reduce frequency |
| 5×10 | 50 | by 10 (10, 20, 30, 40, 50) | by 5 (5, 10...50) | Used in Lesson 1.4/3.3-3.4 — reduce frequency |
| 10×2 | 20 | by 2 (2, 4...20) | by 10 (10, 20) | Used in EC.3 — reduce frequency |
| 10×3 | 30 | by 3 (3, 6...30) | by 10 (10, 20, 30) | Rotation of 3×10 |
| 10×4 | 40 | by 4 (4, 8...40) | by 10 (10, 20, 30, 40) | Rotation of 4×10 |
| 10×5 | 50 | by 5 (5, 10...50) | by 10 (10, 20, 30, 40, 50) | Rotation of 5×10 |

> **Pipeline Guidance:** Prefer rectangles NOT used in Lesson or EC for initial problems. Rotate orientations (e.g., if Lesson used 3×10, Practice can use 10×3). As student demonstrates mastery, increase area and skip-count difficulty (from by-10 and by-5 to by-3 and by-4).

---

## Dimensions Used Tracking (EC + Practice)

| Interaction | Toy | Dimensions | Area | Orientation | Highlighting | Notes |
|-------------|-----|-----------|------|-------------|-------------|-------|
| EC Transition | Grid Rectangles (Display) | 5×10 | 50 | From 3.3 | None | Continuity from Lesson |
| EC.1 | Grid Rectangles (Display) | 3×4 | 12 | 3 rows of 4 | None | NEW. IDENTIFY structure + area. |
| EC.2 | Grid Rectangles (Display) | 5×3 | 15 | 5 rows of 3 (vertical) | None | NEW. CREATE structure description + area. |
| EC.3 | Grid Rectangles (Display) | 10×2 | 20 | 10 rows of 2 (tall, narrow) | None | NEW. IDENTIFY skip-counting. Rotation of Lesson 2×10 but different rectangle. |
| EC.4 | Grid Rectangles (Display) | 2×4 | 8 | 2 rows of 4 | None | NEW. IDENTIFY column flexibility. |
| Practice | Grid Rectangles (Display) | Varied from pool | 6-50 | Both | None | Pipeline-generated from rectangle pool above |

---

## Cross-Module Skill References (for Spiral Review in Practice)

| Prior Module Skill | How It Surfaces in M3 Practice | Priority |
| :---- | :---- | :---- |
| **M2: Tiling accuracy** | All M3 rectangles are pre-tiled (display). Students trust the tiling is complete — no gap/overlap checking needed. Pipeline does NOT include tiling problems. | Background (implicit) |
| **M1: Area = tile count** | Every M3 problem ends with an area answer. Students apply M1's definition (area = number of unit squares) but now use skip-counting instead of one-by-one. | Integrated |
| **Unit 1: Array recognition** | "Array" vocabulary appears in some Practice problems for structure description. Not assessed — descriptive use only. | Light touch |

---

## Anti-Pattern Detection (from Backbone §1.4 #2.0)

| Detection Method | Trigger | Pipeline Response |
| :---- | :---- | :---- |
| **Time-based proxy** | Response time on consecutive problems significantly exceeds expected skip-counting time for that rectangle size | Flag probable one-by-one counting. Insert structure reminder interaction before next problem. |
| **Structure MC errors** | Student produces correct area but selects wrong structure description | Flag structure-area disconnect. Student may be bypassing structure through brute-force counting. Return to problems with structure ID required before area. |
| **Consistent dimension confusion** | Student repeatedly selects column description when asked for rows (or vice versa) | Flag row/column confusion. Insert explicit row vs. column comparison problem. |

> **Remediation Escalation:** If anti-pattern triggers fire on 2+ consecutive problems, Pipeline returns student to scaffolded level (structure ID required + reduced rectangle size). If 3+ consecutive failures, flag for teacher review.

---

## Practice Problem Type Templates

### Type 1: Structure + Area (Row)
```
Visual: Grid Rectangles (Display). [R×C] rectangle. Full grid. No highlighting.
Prompt: "Which describes this rectangle?"
MC: "___ rows of ___" options
On Correct: "[structure]. What's the area?"
Prompt: "What is the area?"
MC: area options
On Correct: "[area] square units."
```

### Type 2: Structure + Area (Column)
```
Visual: Grid Rectangles (Display). [R×C] rectangle. Full grid. No highlighting.
Prompt: "Describe this rectangle using columns."
MC: "___ columns of ___" options
On Correct: "[structure]. What's the area?"
Prompt: "What is the area?"
MC: area options
On Correct: "[area] square units."
```

### Type 3: Both Directions
```
Visual: Grid Rectangles (Display). [R×C] rectangle. Full grid. No highlighting.
Prompt: "Describe this rectangle using rows."
MC: "___ rows of ___" options
On Correct: "Now describe it using columns."
Prompt: "Describe using columns."
MC: "___ columns of ___" options
On Correct: "Same area — [area] square units either way."
```

### Type 4: Area Comparison
```
Visual: Two Grid Rectangles (Display) side by side. [R1×C1] and [R2×C2]. Full grids. No highlighting.
Prompt: "Which rectangle has more area? Use the structure to decide."
MC: "Left: [area1] square units" / "Right: [area2] square units" / "They're the same"
On Correct: "[correct]. [brief rationale]."
```

### Type 5: Skip-Count Validation
```
Visual: Grid Rectangles (Display). [R×C] rectangle. Full grid. No highlighting.
Guide: "Skip-count by rows to find the area."
Prompt: "What is the area?"
MC: area options (include count-all error distractors)
On Correct: "[skip-count sequence]. [area] square units."
```

---

## Incomplete Script Flags (Practice)

* **Area Comparison visual:** Practice Type 4 requires two rectangles displayed side by side. Engineering specification needed for dual-rectangle display within the Grid Rectangles toy. If not supported, replace with sequential presentation (show Rectangle A, record area, then show Rectangle B, compare).
* **Anti-pattern time thresholds:** "Expected skip-counting time" needs calibration data. Initial estimate: rectangle area ÷ skip-count increment × 2 seconds per step + 5 seconds for MC selection. Engineering calibration needed.
* **Area answer modality (AF#3):** All area answers drafted as MC. Per author: MC default, potential for palette entry (equation-builder-style broader option selector) in future. Pipeline should be modality-agnostic if possible.

---

# §1.9 SYNTHESIS (6-8 minutes)

## Parameters

| Parameter | Value |
| :---- | :---- |
| **Phase** | Synthesis |
| **Duration** | 6-8 minutes |
| **Interaction Count** | 4 (Opening Frame + 2 Connection Tasks + Metacognitive Reflection + Closure) |
| **Task Types Used** | Type A (Pattern Discovery + Consolidation), Type C (Real-World Bridge) |
| **Metacognitive Reflection** | Type 1 (Strategy Identification) — planning-focused, strongest for age 8-9 |
| **Toy** | Grid Rectangles (Display) — same as Lesson |
| **Highlighting** | None — post-mastery |
| **Vocabulary** | row, column, array, area, square units — all established |
| **New Concepts** | None |

## Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Connect back to student's module experience | Introduce new procedures or concepts |
| Use Grid Rectangles (Display) with visual support | Use highlighting as scaffold (S.1 system animation is demonstration, not scaffold — see KDD-15) |
| Include at least 2 different task types (A-D) | Make tasks that are just more Practice |
| Include metacognitive reflection before closure | Use extended teaching in remediation |
| End with specific, growth-oriented closure | Use generic praise ("Great job!") |
| Reference the Warmup callback (6×4) per TVP | Include M4 teaser (M4's responsibility) |

---

## Opening Frame [Type A]

* **Purpose:** Signal shift from Practice to reflection/connection. Set tone for discovery. Students have just completed Practice — they've demonstrated mastery. Now we connect to bigger ideas.
* **Visual: Grid Rectangles (Display).** The 6×4 rectangle from Warmup. All 24 squares shaded. Full grid. No highlighting.
* **Guide:** "You've been describing rectangles and counting faster all session. Now let's look back and see what you figured out."
* **No student action.**

> **Voice Note:** "Let's look back and see what you figured out" is warm, reflective, and signals consolidation. The Warmup rectangle reappears — students will recognize it, creating a narrative arc.

> **Design Note:** The Opening Frame reintroduces the 6×4 Warmup rectangle. This is the visual anchor for the entire Synthesis — students will see their growth from "counted every tile" to "skip-counted in seconds."

---

## Connection Task S.1: Two Ways to See It [Type A]

* **Purpose:** Warmup callback + explicit consolidation. The system animates both structural descriptions of the Warmup rectangle — rows then columns — while the Guide narrates both skip-counts landing on the same area. This is the TVP's "Remember when this was hard?" moment AND the consolidation of rows vs. columns. The value is in SEEING both descriptions yield the same result on the rectangle the student struggled with at the start.
* **Task Type:** Type A (Pattern Discovery + Consolidation) — the insight lands through animation and narration, not assessment.
* **Visual: Grid Rectangles (Display).** The 6×4 rectangle from Warmup. All 24 squares shaded. Full grid.

**Part 1 — Rows (system animation):**
* **Guide:** "Remember this rectangle from the beginning? You counted every single tile — all 24. Watch what happens now."
* **System:** Auto-highlights rows sequentially (same animation style as Lesson Section 1).
* **Guide (synced):** "6 rows of 4. Skip-count: 4... 8... 12... 16... 20... 24."

**Part 2 — Columns (system animation):**
* **Guide:** "Now watch the columns."
* **System:** Auto-highlights columns sequentially (same animation style as Lesson Section 2).
* **Guide (synced):** "4 columns of 6: 6... 12... 18... 24."

**Part 3 — Consolidation:**
* **Guide:** "Same rectangle. Same area. Rows or columns — it always works. And you don't have to count every tile anymore."
* **No student action.**

> **Design Note:** This is the module's emotional climax AND its consolidation moment. The system animates rows then columns on the WARMUP rectangle — the same one the student laboriously counted tile-by-tile. Three things land simultaneously: (1) the "before and after" contrast (counting every tile → instant skip-counting), (2) the rows-vs-columns equivalence on a single rectangle (both arrive at 24), and (3) the module's narrative arc comes full circle (Warmup → Lesson → EC → Practice → here). System animation is used because the student's job in this moment is to WATCH and INTERNALIZE, not to perform. The insight is experiential — seeing both skip-counts land on 24 is more powerful than answering a question about it.

> **Voice Note:** "And you don't have to count every tile anymore" — this is the behavioral punchline of the entire module. It references what the student actually DID in the Warmup (counted every tile) and names what changed. The skip-count by 4 (rows) uses Grade 2 prior knowledge. The skip-count by 6 (columns) is Guide-narrated demonstration, not assessed — the student watches but doesn't compute. The point is that BOTH directions arrive at 24.

---

## Connection Task S.2: Rows and Columns Are Everywhere [Type B]

* **Purpose:** Connect the abstract concept of row/column structure to real-world contexts. Students recognize that the organizational pattern they learned (equal rows, equal columns) exists outside of math rectangles. Cements understanding by showing the concept's reach.
* **Task Type:** Type C (Real-World Bridge) — linking mathematical structure to familiar contexts.
* **Visual:** Three skinned Grid Rectangles displayed (each uses the Grid Rectangles toy with a visual skin applied):
  * **Scenario A:** Grid Rectangle skinned as **egg carton** — 2×6 (2 rows of 6). Tiles rendered as egg-shaped cells.
  * **Scenario B:** Grid Rectangle skinned as **bookshelf** — 3×5 (3 rows of 5). Tiles rendered as book spines on shelves.
  * **Scenario C:** Grid Rectangle skinned as **parking lot** — 4×10 (4 rows of 10). Tiles rendered as parking spaces with cars.

* **Guide:** "Rows and columns aren't just in math rectangles. Look at these three pictures."
* **Prompt:** "Which one shows 3 rows of 5?"
* **Student Action:** MC selection
  * **Options:** Scenario A / Scenario B / Scenario C
* **Correct Answer:** Scenario B (bookshelf)
* **Answer Rationale:**
  * Scenario B = Correct (3 shelves with 5 books each = 3 rows of 5)
  * Scenario A = 2 rows of 6 (wrong structure)
  * Scenario C = 4 rows of 10 (wrong structure)
* **On Correct:** "The bookshelf — 3 rows of 5 books. Fifteen books total, and you didn't need to count every one. Rows and columns help you count faster everywhere."
* **Remediation:** Pipeline (light — brief redirect: "Count the shelves. That's how many rows.")

> **Design Note:** All three scenarios show real row-and-column arrangements — no "wrong" example, just "which matches this description." This validates that structure-seeing transfers beyond grid rectangles. The bookshelf is deliberately accessible for 8-9 year olds. The egg carton and parking lot are familiar but use different dimensions. All three use skinned Grid Rectangles — the same toy from Lesson with a visual overlay — rather than photographic images. This eliminates the image-sourcing engineering dependency while maintaining the real-world connection. The grid structure is identical to what students have used all session; only the visual treatment changes.

> **Engineering Note:** Skinned Grid Rectangles require the ability to apply visual overlays to the existing Grid Rectangles toy. Each skin replaces the default tile appearance with a context-appropriate rendering (egg cells, book spines, parking spaces). The underlying grid mechanics (rows, columns, area) are unchanged. If skinning is not yet available, fall back to labeled Grid Rectangles with text labels ("Egg Carton," "Bookshelf," "Parking Lot") above standard Grid Rectangles of the specified dimensions.

---

## Metacognitive Reflection S.3: What Helped You Most? [Type B]

* **Purpose:** Surface and validate the student's preferred strategy. Planning-focused reflection (strongest for age 8-9 per Playbook §3E research note). Students identify which tool or approach helped them count faster.
* **Reflection Type:** Type 1 (Strategy Identification) — "What did I do?"
* **Visual: Grid Rectangles (Display).** The 6×4 rectangle remains visible.
* **Guide:** "You learned a lot of ways to count faster today. What helped you most?"
* **Prompt:** "What helped you count faster?"
* **Student Action:** MC selection
  * **Options:**
    * "Seeing the rows light up"
    * "Counting by groups instead of one by one"
    * "Looking at it both ways — rows and columns"
    * "Knowing every row has the same number"
* **On Selection — "Seeing the rows light up":** "The highlighting made the groups pop out. Now you can see those groups even without the highlighting — that's progress."
* **On Selection — "Counting by groups instead of one by one":** "Skip-counting by groups is so much faster. And you proved it works every time."
* **On Selection — "Looking at it both ways":** "Rows or columns — same answer. Having two ways to check is a powerful tool."
* **On Selection — "Knowing every row has the same number":** "That's the key pattern — equal rows. Once you see it, skip-counting just clicks."

> **Design Note:** All four options are valid strategies from the Lesson. Each On Selection response validates the specific strategy and connects it to the broader learning. No option is "wrong" — reflection has no incorrect answers (per Playbook §3E). The options span the module's key moments: highlighting (S1-S2 scaffold), skip-counting (core strategy), both directions (Section 2 insight), equal groups (foundational pattern). Guide responses are ONE sentence each per Playbook §3E ("Guide response is ONE sentence — don't over-explain").

> **Voice Note:** "What helped you count faster?" is concrete and action-oriented (planning-focused). Avoids abstract self-assessment questions like "How has your understanding changed?" which are weak for this age group.

---

## Identity-Building Closure S.4 [Type A]

* **Purpose:** Specific, growth-oriented affirmation. Connect to what the student actually did in this module. NO M4 teaser — M3 ends on the skip-counting achievement. M4 bridge is M4's responsibility (resolved SME decision).
* **Visual: Grid Rectangles (Display).** The 6×4 rectangle remains visible — the visual thread from Warmup through Synthesis.
* **Guide:** "At the start, you counted 24 tiles one by one. Now you see 6 rows of 4 and know the answer right away. You taught yourself to see the pattern inside the rectangle — and that's a skill that keeps getting more useful."
* **No student action.**

> **Design Note:** Closure references specific behavioral change ("counted 24 tiles one by one" → "see 6 rows of 4 and know the answer right away"). This is the Playbook's Discovery Pattern: "You discovered that [specific pattern]. That thinking will help you with [future application]." The "keeps getting more useful" is a forward reference without naming M4 or multiplication — honoring the SME decision to not tease M4 in M3's Synthesis. The 6×4 rectangle has been the visual thread across the entire session: Warmup (tedious counting) → Synthesis (instant skip-counting). This narrative arc IS the module's story.

> **Voice Note:** "You taught yourself" — autonomy support. The phrasing attributes the growth to the student, not the Guide. "Keeps getting more useful" is warm and forward-looking without being specific about M4.

---

## Synthesis Verification Checklist

- [x] **All required elements present:** Opening Frame ✓, Connection Tasks (S.1, S.2) ✓, Metacognitive Reflection (S.3) ✓, Identity-Building Closure (S.4) ✓
- [x] **3-5 diverse connection tasks:** 4 interactions total (2 connection + 1 reflection + closure). Within Early module range of 3-4. ✓
- [x] **Minimum 2 different task types:** Type A (Pattern Discovery in S.1) + Type C (Real-World Bridge in S.2) ✓
- [x] **At least one pattern/transfer task:** S.1 (before/after pattern recognition) ✓
- [x] **Metacognitive reflection included:** S.3 (Type 1 — Strategy Identification) ✓
- [x] **Identity-building closure specific, not generic:** "You taught yourself to see the pattern inside the rectangle" ✓. No "Great job!" or "Excellent work!" ✓
- [x] **Visual support for every task:** Grid Rectangles (Display) in S.1, S.3, S.4. Three skinned Grid Rectangles in S.2 (egg carton 2×6, bookshelf 3×5, parking lot 4×10). ✓
- [x] **Total time appropriate:** Opening (~30 sec) + S.1 (~90 sec) + S.2 (~2 min) + S.3 (~90 sec) + S.4 (~30 sec) ≈ 6-7 minutes. ✓
- [x] **Zero new teaching:** All references to already-taught concepts. No new procedures. ✓
- [x] **Remediation minimal:** S.1 and S.2 have light redirects only (brief, 10-20 words). S.3 has no wrong answer. ✓
- [x] **Active task check:** S.1 (Type A — system animation, no student action), S.2 (MC scenario selection), S.3 (MC strategy selection). S.2 and S.3 provide student choice; S.1 is observation-focused because the consolidation insight lands through watching, not answering. ✓
- [x] **Consolidation check:** Module taught both row and column strategies. S.1 is the explicit consolidation moment: system animates rows ("6 rows of 4 = 24") then columns ("4 columns of 6 = 24") on the Warmup callback rectangle, showing both descriptions yield the same area. This is a dedicated side-by-side demonstration. S.2 and S.3 reinforce consolidation ("rows and columns help you count faster everywhere"; "Looking at it both ways"). ✓
- [x] **No M4 teaser:** Closure says "keeps getting more useful" — no multiplication language. ✓
- [x] **Warmup callback present:** 6×4 rectangle in Opening, S.1, S.3, S.4. ✓
- [x] **No references to specific Practice problems:** All generalizations. ✓

### Authenticity Check (Playbook §6)
- [x] **Specificity Test:** All lines are M3-specific (rows, columns, skip-counting, 6×4 callback). Could NOT work for a fraction module. ✓
- [x] **Discovery Test:** S.1 is pattern recognition (before/after), S.2 is real-world connection, S.3 is metacognitive reflection. None is "more practice." ✓
- [x] **Behavioral Observation Test:** Closure references "counted 24 tiles one by one" → "see 6 rows of 4 and know the answer right away." Specific behavioral change. ✓
- [x] **Voice Test:** "What helped you count faster?" / "You taught yourself to see the pattern" — natural teacher language. ✓
- [x] **Enthusiasm Test:** On Correct in S.1 ("You just found the area in seconds") conveys genuine excitement about mathematical efficiency. ✓

---

## Incomplete Script Flags (Synthesis)

* **Skinned Grid Rectangles (S.2):** Three Grid Rectangles need visual skins applied (egg carton 2×6, bookshelf 3×5, parking lot 4×10). Engineering specification: can the system render skinned Grid Rectangles with context-appropriate tile appearances? Fallback: use labeled standard Grid Rectangles.
* **Scenario selection UI:** S.2 requires selecting from three visual scenarios, not text-only MC. Engineering specification: can MC options reference skinned Grid Rectangles? Or does the system need a different selection mechanism (e.g., tapping on the grid itself)?

---

# §1.10 KEY DESIGN DECISIONS (KDD)

## Purpose

KDD documents every non-obvious choice made during SP development. Each entry records WHAT was decided, WHY, and WHERE it applies — creating a traceable record for future module authors, reviewers, and the Pipeline team.

---

### KDD-1: Warmup Rectangle Dimensions (6×4)

**Decision:** Use 6×4 for the Warmup rectangle, even though 6 is outside the Lesson/EC dimension constraint of {2, 3, 4, 5, 10}.

**Rationale:** The Warmup rectangle must be large enough to make one-by-one counting feel tedious (24 tiles). Additionally, this rectangle returns in Synthesis as the callback payoff — students skip-count 6 rows of 4: 4, 8, 12, 16, 20, 24. The skip-count increment is 4 (from the columns), which IS Grade 2 prior knowledge. The "6" is the number of groups, not the skip-count increment — so skip-counting difficulty is controlled by the 4, not the 6.

**Sections:** Warmup (W.1, W.2), Purpose Frame, Synthesis (S.1, S.4). Dimension Tracking notes this as intentional exception.

---

### KDD-2: Purpose Frame Present

**Decision:** Include a Purpose Frame before Lesson Section 1.

**Rationale:** Playbook recommends Purpose Frame for all Lessons unless omission is justified. M3's Purpose Frame connects backward to M2 ("You already know how to tile rectangles and count every square") and forward ("a pattern inside the tiles that lets you count way faster"). Uses only M1-M2 vocabulary. Brief (~15 seconds).

**Sections:** §1.7 Purpose Frame.

---

### KDD-3: "Array" as Callback, Not Introduction (AF#1)

**Decision:** Treat "array" as a callback from Unit 1, not a new vocabulary introduction.

**Rationale:** Author confirmed students will have heard "array" in Unit 1. Staging as callback: "You've been working with these the whole time — rows and columns together. That's called an array." Per Decision #4 (helpful but not required): students who had Unit 1 recognize the term; students who didn't learn it here through grounding.

**Sections:** §1.3 Vocabulary Staging (array row), §1.7 Interaction 2.5 (Section 2 capstone).

---

### KDD-4: Four EC Problems (AF#2)

**Decision:** Expand EC from standard 3 to 4 problems, per TVP specification.

**Rationale:** TVP specifies 4 EC problems for M3, testing 4 distinct skills: (1) row structure identification + area, (2) structure description construction + area, (3) skip-counting validation, (4) column flexibility. Each problem targets a different skill taught in a different Lesson section. EC Playbook permits 3-5 problems. Playbook audit identified that COMPARE could be added (Lesson Section 2 teaches comparison), but this was deferred to Practice (15% Area Comparison distribution target) to stay aligned with TVP's 4-problem specification and avoid exceeding EC's 3-5 minute window.

**Sections:** §1.8 Exit Check (EC.1-EC.4).

---

### KDD-5: Area Answer Modality — MC Default, Palette Entry Possible (AF#3)

**Decision:** Use MC for all area answer interactions. Note that palette entry (equation-builder-style broader option selector) may replace MC in future.

**Rationale:** MC is the safest default — works regardless of engineering implementation. Palette entry would give students a broader set of numeric options to select from, reducing the "process of elimination" risk of 4-option MC. Author deferred final decision pending teacher discussion. SP interactions are designed so that swapping MC for palette entry requires no structural changes — only the answer input mechanism changes.

**Sections:** All interactions with area answers (W.1, 1.2, 1.4, 1.5, 2.1, 2.3, 2.4, 3.1, 3.2, 3.3, EC.1-EC.4, Practice). Incomplete Script Flags in §1.7 and §1.8.5.

---

### KDD-6: Skip-Counting as Guide Dialogue + System Highlighting (AF#4)

**Decision:** Skip-counting is narrated by the Guide AND accompanied by system-driven sequential row/column highlighting. Students do not operate the highlighting during skip-counting demonstrations.

**Rationale:** Author confirmed two-part answer: (a) Guide narrates the count ("5... 10... 15!"), (b) system highlights rows/columns sequentially in sync with narration. This means skip-counting is a SYSTEM-DRIVEN demonstration in Sections 1-2. Student's cognitive work is observing the pattern, then answering structure/area questions via MC.

**Sections:** §1.5 UX Component Requirements (skip-counting animation), §1.7 Interactions 1.1, 1.4, 2.1.

---

### KDD-7: Three-Step Highlighting Scaffold — Tap-to-Highlight Restored (AF#5 Revised)

**Decision:** Restore the TVP's three-step highlighting progression: system auto-highlight (S1) → student tap-to-highlight (S2 transfer) → no highlighting (S3).

**Rationale:** Author's Gate 2 review identified removal of tap-to-highlight as a MAJOR finding. For the 69% of students who cannot spatially structure arrays without instruction, the jump from "system shows you" directly to "find it yourself with no help" skips the critical transfer step. Tap-to-highlight is student-INITIATED but system-EXECUTED — students actively use the tool to find structure themselves. This active practice step is where internalization happens. Original AF#5 resolution (system-only) reversed after Gate 2.

**Sections:** §1.5 (Module Configuration, Progression, Guardrails, UX Components, Interaction Constraints), §1.7 Interactions 2.3-2.4 (tap-to-highlight), §1.4 Misconception #2.0 and #9.0 (prevention strategies).

---

### KDD-8: Section 2 Restructured — Array Moved to Capstone

**Decision:** Move "array" vocabulary from mid-Section 2 (old interaction 2.3) to Section 2 capstone (new interaction 2.5). Section 2 arc: discover columns (2.1) → name columns (2.2) → practice both directions with tap-to-highlight (2.3-2.4) → name the whole arrangement (2.5).

**Rationale:** Author's Gate 2 review identified Section 2 as carrying too much conceptual weight. With column introduction AND array vocabulary AND both-directions practice all in the same section, cognitive density was too high. Moving array to capstone means students practice both-direction descriptions BEFORE absorbing a third term. The revised arc follows a natural progression: see it → name it → practice it → name the whole thing.

**Sections:** §1.3 Vocabulary Staging, §1.7 Section 2 (interactions 2.1-2.5).

---

### KDD-9: Dimension Constraint Relaxation — Section 1

**Decision:** Change Section 1 (Early) dimension constraint from "Both dimensions from {2, 5, 10}" to "At least one dimension from {2, 5, 10}; other from {2, 3, 5, 10}."

**Rationale:** Interaction 1.1 uses 3×5 (3 rows of 5). The original constraint excluded 3 from Section 1. However, 3×5 is pedagogically optimal for the first worked example: 3 rows is enough to see the pattern (more than 2), 5 tiles per row is easy to count, and skip-counting by 5 is trivially easy (Grade 2 prior knowledge). The constraint is relaxed to allow one "non-{2,5,10}" dimension as long as the other anchors the skip-count to an easy increment.

**Sections:** §1.5 Data Constraints (Section 1 row).

---

### KDD-10: EC Area Range — 6-50 (Matching Practice)

**Decision:** Set EC area range at 6-50, matching Practice, rather than the original 10-50.

**Rationale:** EC problems may use smaller areas when the assessed skill is structural rather than computational. EC.4 (2×4 = 8) tests column flexibility — the cognitive demand is on seeing columns, not on arithmetic difficulty. Requiring 10-50 as a hard constraint would force every future EC with a structural focus to document a KDD exception. Making the constraint honest (6-50) avoids this precedent issue.

**Sections:** §1.5 Data Constraints (EC row), §1.8 EC.4.

---

### KDD-11: Dual-Correct MC in Interaction 3.2

**Decision:** Interaction 3.2 accepts two valid answers: "5 rows of 4" (row description) OR "4 columns of 5" (column description).

**Rationale:** The whole point of Section 3 is that students can describe structure using rows OR columns. Penalizing a correct column description when the prompt says "your choice" would undermine the Section 2 insight. Engineering consideration: system must support dual-correct MC. If not supported, default to row-based answer as primary with column-based flagged as alternative correct in the validator.

**Sections:** §1.7 Interaction 3.2, Incomplete Script Flags.

---

### KDD-12: EC Cognitive Types — CREATE and IDENTIFY Only

**Decision:** Use CREATE and IDENTIFY only in EC (per EC Playbook M1-3 guideline). COMPARE deferred to Practice.

**Rationale:** The EC Playbook M1-3 guideline says "Focus: CREATE and IDENTIFY only. Don't use COMPARE unless explicitly taught." While Lesson Section 2 does teach comparison ("same area both ways"), the TVP's 4-problem EC design prioritizes structure identification and skip-counting validation over explicit COMPARE assessment. The "both directions = same area" insight is tested implicitly in EC.4 (column flexibility confirms the student can use either direction) and explicitly in Practice (15% Area Comparison distribution target, which uses APPLY cognitive type). This keeps EC focused on foundational skills per the M1-3 guideline while ensuring COMPARE is assessed in Practice where it belongs. Playbook audit validated this approach as acceptable.

**Sections:** §1.8 EC Parameters, EC Verification Checklist, §1.8.5 Practice Distribution Targets.

---

### KDD-13: No M4 Teaser in Synthesis

**Decision:** M3 Synthesis ends on the skip-counting achievement. No multiplication preview, no "next time" language about M4's content.

**Rationale:** Resolved SME decision from TVP review. M3's closure celebrates what students accomplished (structured counting, rows/columns, skip-counting). The multiplication connection belongs in M4's warmup, which must open with an explicit bridge: "Last time you found 6 rows of 4 = 24 by skip-counting. Watch this: 6 × 4 = 24. Same thing — but faster!" This is M4's responsibility, not M3's. M3's closure says "keeps getting more useful" as a forward reference without naming the specific application.

**Sections:** §1.9 Closure (S.4), Working Notes Section Plan (Synthesis).

---

### KDD-14: EC.3 Rectangle Selection (10×2)

**Decision:** Use 10×2 (area 20) for EC.3 rather than 4×3 (area 12, which matched EC.1's area).

**Rationale:** Author requested distinct areas across all EC problems. 10×2 provides area 20 (distinct from EC.1's 12, EC.2's 15, and EC.4's 8). Additionally, 10×2's tall orientation (10 rows of 2) makes the skip-counting process highly visible — the student must skip-count through 10 steps by 2s, making the strategy unmistakable. 10×2 is a rotation of Lesson's 2×10 but a genuinely different rectangle (different orientation, different row/column counts).

**Sections:** §1.8 EC.3, Dimension Tracking.

---

### KDD-15: Synthesis S.1 System Animation (Consolidation)

**Decision:** Use system-driven row and column highlighting animation in Synthesis S.1 for the consolidation moment, despite the general Synthesis principle of "no highlighting."

**Rationale:** S.1 is a Type A consolidation task where the system animates rows then columns on the 6×4 Warmup callback rectangle while the Guide narrates both skip-counts. The animation is a DEMONSTRATION tool (making the equivalence visible), not a SCAFFOLD (the student doesn't need help finding structure — they've demonstrated mastery in EC and Practice). System animation reuses the exact visual language from Lesson Sections 1-2, creating a callback to the instructional experience. The consolidation insight — both directions yield 24 on the same rectangle — is experiential; it lands through watching the animation, not through answering a question. This is the module's narrative climax and its most pedagogically valuable moment.

**Sections:** §1.9 S.1, Synthesis Constraints table (exception noted).

---

## KDD Verification

- [x] **Every Design Note from all phases reviewed:** Warmup (W.1, W.2), Lesson (1.1-3.4), EC (EC.1-EC.4), Practice, Synthesis (S.1-S.4) ✓
- [x] **Every playbook departure documented:** EC cognitive types (KDD-12), EC area range (KDD-10), Synthesis animation (KDD-15) ✓
- [x] **Every conflict resolution from Table C documented:** Dimension constraints (KDD-9), array timing (KDD-3, KDD-8) ✓
- [x] **Purpose Frame decision documented:** KDD-2 ✓
- [x] **Dimension reuse decisions documented:** Warmup 6×4 (KDD-1), EC.3 selection (KDD-14) ✓
- [x] **All Author Flags resolved and documented:** AF#1 (KDD-3), AF#2 (KDD-4), AF#3 (KDD-5), AF#4 (KDD-6), AF#5 (KDD-7) ✓
- [x] **Scope decisions documented:** No M4 teaser (KDD-13), dual-correct MC (KDD-11) ✓
- [x] **Audit-driven revisions documented:** COMPARE deferred to Practice (KDD-12), system animation consolidation (KDD-15) ✓
- [x] **KDD covers decisions from ALL phases:** Warmup ✓, Lesson ✓, EC ✓, Practice ✓, Synthesis ✓

---


# END OF MODULE 3 STARTER PACK

---

## 1.11 FINAL FORMATTING AUDIT

*Complete before submitting Starter Pack:*

### Tag Removal

- [ ] All development tags removed: `[Modeling]`, `[MODIFY]`, `[Vocab_Staging]`, `[Tool_Intro]`, etc.
- [ ] No placeholder text remaining: `[Section X to be added]`, `[TBD]`, etc.

### Version & Structure

- [ ] Version line updated (no "DRAFT" unless intentional)
- [ ] All standard sections present (1.0 through 1.10)
- [ ] Section headers match template: `## **1.X SECTION NAME**`
- [ ] No duplicate sections or orphaned content at end of document

### YAML & Metadata

- [ ] YAML front matter complete (module_id, unit, domain, toys with Notion links)
- [ ] Standards Cascade table format matches template
- [ ] Module Bridges include From/This/To structure
- [ ] OUR Lesson Sources table populated
- [ ] "Changes from M[N-1]" present for every toy in §1.5

### Interaction Block Compliance

- [ ] Every interaction with student action has BOTH Guide: AND Prompt:
- [ ] Every teaching-only interaction has Guide: AND "No student action."
- [ ] Every assessed interaction has `**Remediation:** Pipeline`
- [ ] Every MC interaction has Answer Rationale with distractor analysis
- [ ] All Visual: lines include: Toy Name (Mode), orientation, data summary, visibility flags

### Phase Checklists

- [ ] Verification Checklists present for Warmup, Exit Check, and Synthesis
- [ ] Incomplete Script Flags and Success Criteria present in Lesson (§1.7.4, §1.7.5)
- [ ] KDD Summary present (§1.10) with all significant decisions documented
- [ ] Practice Phase Inputs present if Practice Phase is generated (§1.8.5)

### Content Quality

- [ ] No student-facing dialogue references "Module X" numbers
- [ ] No authored remediation dialogue (all remediation is `Pipeline`)
- [ ] Misconceptions use global IDs from database
- [ ] Session-relative language throughout ("last time/this time," NOT "yesterday/today")
