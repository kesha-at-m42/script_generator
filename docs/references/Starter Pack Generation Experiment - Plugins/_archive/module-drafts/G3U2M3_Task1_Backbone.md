# MODULE 3: Structured Counting — Rows and Columns

**Version:** 03.13.26

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

# END OF BACKBONE DRAFT

---

## BACKBONE SELF-CHECK

- [x] Every term in Table A "Vocabulary to Teach" (row, column, array) appears in §1.2 or §1.3 — **PASS.** All three terms accounted for. Row and column in Must Teach + §1.3 staging. Array in §1.3 with staging note and AF#1.
- [x] Every term in Table A "Vocabulary to Avoid" — **N/A.** No "Vocabulary to Avoid" column in Module Mapping. Derived from M2 Terms to Avoid + M3 scope constraints. All covered in §1.3 Terms to Avoid.
- [x] Module Mapping "Notes" — every "Critical:" flag addressed — **PASS.** Notes says "CRITICAL MODULE per research." Addressed in: §1.0 (Biggest Risk), §1.2 (⚠️ scope warning), §1.1.2 (This Module bridge), §1.4 (Prevention Strategy), §1.5 (Guardrails — "Present structure identification BEFORE area calculation"). Decision #2 cited throughout.
- [x] Module Mapping "Question/Test Language" stems in §1.1 or flagged for §1.7 — **PASS.** All five stems mapped: "How many rows?" → Lesson S1 + EC P1-2; "How many in each row?" → Lesson S1 + EC P1-2; "How many columns?" → Lesson S2 + EC P4; "How many in each column?" → Lesson S2 + EC P4; "What is the area?" → EC P1-3 + all Lesson practice.
- [x] Misconception IDs match database, not module number shorthand — **PASS.** §1.4 uses #2.0 and #9.0 (global IDs). Module Mapping's "M2" and "M9" shorthand translated.
- [x] Every TVP data constraint appears in §1.5 — **PASS.** Dimension set {2,3,4,5,10}, area range 6-50, products within 60, both orientations, Early/Mid/Late dimension breakdowns, "never both dimensions outside {2,3,4,5,10}" rule — all documented.
- [x] Every conflict in Table C resolved or flagged — **PASS.** 8 conflicts documented; all resolved or assigned Author Flags.
- [x] Every applicable Important Decision reflected in SP or documented as KDD — **PASS.** Decisions 1 (unified CRA path), 2 (explicit spatial structuring — central), 3 (full grids), 4 (array as self-contained), 5 (no perimeter), 6 (partial — tap for selection OK). Decisions 7, 8, 9 confirmed non-applicable.
- [x] Conceptual Spine Analysis confirms concept placement — **PASS.** "Spatial Structuring (row-by-column seeing)" INTRODUCED in L4 (SP treats as explicit new teaching). "Rows & columns counting strategy" INTRODUCED in L4. "No gaps/overlaps rule" continues DEVELOPING from L3 (assumed knowledge in M3). "Unit squares (tiling)" continues DEVELOPING.
- [x] Standards Mapping required vocabulary aligns with §1.3 — **PASS.** 3.MD.C.6 required vocabulary: rows ✓ (§1.3 Lesson S1), columns ✓ (§1.3 Lesson S2). Advanced 3.MD.C.6 vocabulary (sq cm, sq in, sq ft, sq m) all in Terms to Avoid with module deferrals. 3.MD.C.7.b vocabulary (side lengths, multiply, dimensions, length, width) all in Terms to Avoid.
- [x] The One Thing references only concepts this module teaches — **PASS.** §1.0 references row/column structure + skip-counting — both M3 concepts. No multiplication language.
- [x] YAML front matter complete — **PASS.** module_id, unit, domain, primary_toys (with Notion URL), secondary_toys (none), interaction_tools, our_lessons all present.

**Self-Check Result: ALL ITEMS PASS. Ready for Gate 1 evaluation.**
