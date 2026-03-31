# GATE 1 EVALUATION REPORT
## M7 Backbone Draft: Area Without a Full Grid

**Module:** M7 (Grade 3, Unit 2: Area and Multiplication)
**Evaluation Date:** 2026-03-24
**Evaluator:** Gate 1 Agent
**Document Status:** DRAFT FOR INTERNAL REVIEW
**Overall Rating:** PASS WITH CRITICAL NOTES

---

## EXECUTIVE SUMMARY

The M7 Backbone draft demonstrates comprehensive coverage of the critical abstraction step in the Unit 2 CRA progression. The document correctly implements **Decision #3 (Progressive Grid Removal)** as the centerpiece, with full grid fading (partial → tick marks → dimensions only) specified within the module. Primary misconception #5 (Not Multiplying Side Lengths) is well-targeted across all phases with clear remediation pathways.

**KEY FINDINGS:**
- ✅ Source fidelity to TVP is strong; all critical teaching points and data constraints documented
- ✅ Toy specifications align with TVP requirements; four display modes correctly specified
- ✅ Misconception targeting is thorough; both #5 and #8 have detailed remediation strategies
- ✅ Vocabulary staging respects Known Pattern #11 (introduce after concrete experience)
- ⚠️ CRITICAL: Guide reveal specification needs clarification on M3 flag mechanics
- ⚠️ CRITICAL: Equation Builder is listed as "In development" — verify design status before SP author handoff
- ⚠️ Minor: Perimeter boundary (Decision #5) explicitly affirmed but context not discussed

**RECOMMENDATION:** PASS for Starter Pack authoring with three conditional clarifications before final sign-off.

---

## SECTION A: SOURCE FIDELITY (TVP CROSS-REFERENCE)

### A1. Toy List and Configuration

**CHECK:** Do §1.5 toys match TVP? Check: Grid Rectangles in FOUR modes (full grid reference, partial grid, tick marks, outline/dimensions-only), Guide Reveal (remediation only, not student-facing), Equation Builder (multiplication with unit labels).

**FINDING:** ✅ PASS

**Details:**
- **Grid Rectangles Modes:** All four modes correctly identified and specified in M7 Backbone §1.5:
  1. Full Grid (Warm-up only) — 4×6 rectangle, all 24 squares shown, labeled "4 rows of 6 tiles" ✅
  2. Partial Grid (Early Phase) — "First row fully tiled, first column fully tiled, interior empty" ✅
  3. Tick Marks (Mid Phase) — "Evenly spaced marks along top and left edges; no interior grid or fill" ✅
  4. Dimensions Only (Late Phase) — "Rectangle outline with dimension labels only (e.g., '6 m' on top, '3 m' on left); no grid, no marks" ✅

- **TVP Alignment Check:** The Backbone exactly mirrors TVP §Data Constraints table structure:
  - Partial grid: "first row and first column filled; interior empty" (Backbone §1.5 L356: ✅ matches TVP L568)
  - Tick marks: "evenly spaced marks along top and left edges only" (Backbone §1.5 L357: ✅ matches TVP L579)
  - Dimensions only: "rectangle outline with dimension labels; no grid, no marks" (Backbone §1.5 L358: ✅ matches TVP L589)

- **Guide Reveal (Remediation, Not Student-Facing):**
  - Backbone §1.5 §L365-377 specifies: "Reveal is for guide only; student does not see it unless guide explicitly activates"
  - Trigger: Late Phase rectangle where student cannot solve
  - First reveal: Overlay partial grid temporarily
  - Second reveal: Overlay full grid
  - Logging: If ≥2 reveals used, flag student for M3 reinforcement review
  - TVP Match: ✅ Aligns with TVP L629: "guide-activated grid reveal (showing tick marks or partial grid on a dimensions-only rectangle). This is NOT a student-facing toggle"

- **Equation Builder (Multiplication with Unit Labels):**
  - Backbone §1.5 L405-441 specifies multiplication expression building with unit labels
  - Early Phase: Optional verbal/written response
  - Mid Phase: "Full Equation Builder online. Student drag-places factors from ticks, Equation Builder displays equation and product. Unit labels required."
  - Late Phase: "Full Equation Builder. Student reads dimensions from labels, constructs equation, Equation Builder confirms."
  - EC (Text-Only): Embedded in text with product slot and unit label to fill
  - TVP Match: ✅ Aligns with TVP L585-600 requirement for multiplication with unit labels

**SOURCE REFERENCE:** Backbone §1.5, TVP lines 530-659, Working Notes Table B

---

### A2. Scaffolding Progression

**CHECK:** Does SP plan match TVP's fading: full grid (warmup ref) → partial grid (Early) → tick marks (Mid) → dimensions only (Late) → text-only (Late/EC)?

**FINDING:** ✅ PASS

**Details:**
- **Warmup → Early:** Backbone §1.0 L361: "Warm-up → Early: Show same 4×6 rectangle with full grid, then fade grid interior (keep outline), show partial. Message: 'The area didn't change. We just can't see all the squares.'" ✅ Matches TVP L560-562

- **Early → Mid:** Backbone §1.5 L362: "Early → Mid: Same rectangle with partial grid, then fade partial grid lines, leave tick marks. Message: 'The numbers along the edges tell us what the grid would have looked like.'" ✅ Matches TVP L579

- **Mid → Late:** Backbone §1.5 L363: "Mid → Late: Same rectangle with tick marks, then fade tick marks, keep dimension labels. Message: 'The number already tells us what the tick marks showed.'" ✅ Matches TVP L590 ("Make explicit: 'The number already tells you what the tick marks showed'")

- **Late → EC (Text-Only):** Backbone §1.2 L136-142 specifies text-only problems in Late Phase & EC with rigid template. ✅ Matches TVP L596-600

**PROGRESSION VISUAL (Backbone §1.5 L460-486):**
```
WARM-UP → EARLY → MID → LATE → EC → SYNTHESIS → EXIT CHECK
Full Grid  Partial  Tick  Dims  Mixed  Same rect  Mixed
           Grid    Marks Only  & Text in 4 states
```

**SOURCE REFERENCE:** Backbone §1.5 L360-363, TVP L560-600

---

### A3. Data Constraints

**CHECK:** Verify ALL TVP constraints:
- Partial grid: one factor ≤5, other 3-9, products ≤45, ≤5 factor as column
- Tick marks: factors 3-10, products ≤100
- Dimensions-only: factors 2-10, products ≤100, all four units
- Text-only: rigid template "A [object] is [number] [unit] long and [number] [unit] wide. What is its area?"

**FINDING:** ✅ PASS WITH ONE CLARIFICATION

**Details:**

| Constraint | TVP Spec | Backbone Spec | Match |
|-----------|----------|---------------|-------|
| **Partial Grid Factors** | One ≤5, other 3-9 | L384: "One ≤5 (cols), other 3–9 (rows)" | ✅ |
| **Partial Grid Product** | ≤45 | L384: "≤ 45" | ✅ |
| **Partial Grid Column Rule** | ≤5 factor as column | L384: "Constraint: ≤5 in teaching. Open in practice (up to product limit)" | ✅ CLARIFIED |
| **Tick Marks Factors** | Factors 3-10 | L385: "Factors 3–10 each" | ✅ |
| **Tick Marks Product** | ≤100 | L385: "≤ 100" | ✅ |
| **Tick Marks Density** | (Not explicit in Backbone) | L385: "Tick mark density ≤ 8 (teaching), ≤ 10 (practice)" | ⚠️ ADDED TO SPEC |
| **Dimensions-Only Factors** | Factors 2-10 | L386: "Factors 2–10 each" | ✅ |
| **Dimensions-Only Product** | ≤100 | L386: "≤ 100" | ✅ |
| **Dimensions-Only Units** | All four | L386: "All four (sq ft, sq m, sq in, sq cm)" | ✅ |
| **Text-Only Template** | Rigid: "A [object] is [number] [unit] long and [number] [unit] wide. What is its area?" | L137-140: Exact match | ✅ |
| **Text-Only Factors** | Factors 2-10 | TVP L655-656 confirms | ✅ |

**CLARIFICATION NOTED:**
- Backbone L384 specifies partial grid constraint as "≤5 in teaching. Open in practice (up to product limit)."
- This matches TVP L643 and SME Resolution L683: "Constrain during teaching (Early), not during practice (Late)."
- Working Notes Table C L127 confirms: "Partial grid ≤5 in teaching/open in practice — RESOLVED"
- **STATUS:** ✅ CORRECT AND RESOLVED

**TICK MARK DENSITY NOTE:**
- Backbone §1.5 L385 adds tick mark specification: "Tick mark density ≤ 8 (teaching), ≤ 10 (practice)"
- TVP L649 recommends: "for dimensions > 8, consider slightly wider spacing"
- TVP SME Resolution L685: "Cap at dimensions ≤ 8 during teaching (Mid phase). Practice problems may use any dimension within the unit constraint (≤ 10)."
- **STATUS:** ✅ ADDED APPROPRIATELY; SOURCE IS TVP SME RESOLUTION

**SOURCE REFERENCE:** Backbone §1.5 L379-387, TVP L641-658, Working Notes Table C L125-131

---

### A4. Key Beats

**CHECK:** Does SP plan for: warmup grid→no-grid transition, partial grid "I see 7 in each row and 4 rows", tick-mark dimension reading, dimension-label-replacing-ticks animation, text-only as full abstract endpoint?

**FINDING:** ✅ PASS

**Details:**

| Key Beat | TVP Location | Backbone Location | Status |
|----------|--------------|-------------------|--------|
| **Warmup Grid→No-Grid Transition** | L560-562: "Then: SAME rectangle shown with grid removed — only outline + dimension labels remain" | §1.5 L361, §1.0 L24-27 | ✅ |
| **Partial Grid Verbalization ("I see 7 in each row and 4 rows")** | L569-571: "Students can SEE one complete row (e.g., 7 squares) and count how many rows there are from the column (e.g., 4 rows visible down the left side)...Students state: 'I see 7 in each row and 4 rows, so 4 × 7 = 28'" | §1.0 L40: "Early Phase: Student sees partial grid and verbalizes: 'I see 7 in a row. There are 4 rows. 4 times 7 is 28 square feet.'" | ✅ |
| **Tick-Mark Dimension Reading** | L579-582: "Students read dimensions from tick mark count, multiply for area" | §1.5 L362: "Early → Mid: Same rectangle with partial grid, then fade partial grid lines, leave tick marks. Message: 'The numbers along the edges tell us what the grid would have looked like.'" | ✅ |
| **Dimension-Label-Replacing-Ticks Animation** | L590: "Key beat: Before the first dimensions-only problem, show a tick-marked rectangle, add dimension labels, then fade the tick marks away. Make explicit: 'The number already tells you what the tick marks showed.'" | §1.5 L363: "Mid → Late: Same rectangle with tick marks, then fade tick marks, keep dimension labels. Message: 'The number already tells us what the tick marks showed.'" | ✅ |
| **Text-Only as Full Abstract Endpoint** | L596-600: "Some text-only problems (no rectangle visual)...This is the full abstract endpoint — no visual support at all" | §1.0 L42-43, §1.2 L136-142: Text-only in Late/EC as full abstraction | ✅ |

**SOURCE REFERENCE:** Backbone §1.0, §1.2, §1.5, TVP L557-600

---

### A5. SME-Resolved Decisions

**CHECK:** All three fading levels within M7 (RESOLVED), guide reveal 2+ → M3 flag (RESOLVED), text-only appropriate in M7 (RESOLVED), partial grid ≤5 in teaching/open in practice (RESOLVED), tick marks ≤8 teaching/≤10 practice (RESOLVED).

**FINDING:** ✅ PASS — ALL FIVE RESOLUTIONS CORRECTLY IMPLEMENTED

**Details:**

| SME Decision | TVP Source | Backbone Implementation | Status |
|--------------|-----------|------------------------|--------|
| **All three fading levels within M7 (RESOLVED)** | L677: "All three fading levels (partial grid → tick marks → dimensions only) MUST be completed within M7" | §1.2 L121-126: "All three transitions must complete within M7. No backsliding to M8." | ✅ |
| **Guide reveal 2+ → M3 flag (RESOLVED)** | L679: "Pattern-based — 2+ guide reveals within a single session flags for M3 reinforcement" | §1.5 L372: "Logging: If ≥2 reveals used, flag student for M3 reinforcement review in guide notes." | ✅ |
| **Text-only appropriate in M7 (RESOLVED)** | L681: "Text-only problems are appropriate in M7 Late and exit check" | §1.2 L136-142: "Text-Only Problems (Late Phase & Enrichment Challenge)" | ✅ |
| **Partial grid ≤5 in teaching/open in practice (RESOLVED)** | L683: "Constrain during teaching (Early), not during practice (Late)" | §1.5 L384: "Constraint: ≤5 in teaching. Open in practice (up to product limit)." | ✅ |
| **Tick marks ≤8 teaching/≤10 practice (RESOLVED)** | L685: "Cap at dimensions ≤ 8 during teaching (Mid phase). Practice problems may use any dimension within the unit constraint (≤ 10)" | §1.5 L385: "Tick mark density ≤ 8 (teaching), ≤ 10 (practice)" | ✅ |

**Working Notes Cross-Reference (Table C — Conflict Log):**
All five resolutions also documented in Working Notes L125-131 with "RESOLVED" status. ✅

**SOURCE REFERENCE:** Backbone §1.2 L121-126, §1.5 L372 & L384-385, TVP L677-685, Working Notes Table C

---

### A6. Misconceptions

**CHECK:** #5 Not Multiplying Side Lengths PRIMARY/HIGH. #8 Square Unit Confusion SECONDARY/MEDIUM. Are global IDs correct? (Note: Module Mapping says "M5" for misconception but that's global ID #5, not module M5.)

**FINDING:** ✅ PASS WITH CLARIFICATION

**Details:**

| Misconception | Expected ID | Backbone Reference | Status |
|--------------|------------|-------------------|--------|
| **Not Multiplying Side Lengths** | Global ID #5, PRIMARY, HIGH | §1.0 L29-30, §1.4 L267-302, §1.6 L494 | ✅ CORRECT |
| **Square Unit Confusion** | Global ID #8, SECONDARY, MEDIUM | §1.0 L29-30, §1.4 L305-337, §1.6 L495 | ✅ CORRECT |

**ID CLARIFICATION:**
- Working Notes Table A (Module Mapping) L23 states: "Key Misconceptions: M5 (not multiplying side lengths)"
- This notation refers to **global misconception ID #5**, NOT module M5
- Excel Extraction (Misconceptions sheet) L250 confirms: "MISCONCEPTION 5 - Surfaces in M7 (leads to M8-M9): Not Multiplying Side Lengths"
- Backbone correctly uses **#5** and **#8** throughout, avoiding module-name confusion
- **STATUS:** ✅ CORRECT; NO AMBIGUITY IN BACKBONE

**SEVERITY LEVELS (Per Excel Extraction):**
- Misconception #5: Priority = HIGH ✅
- Misconception #8: Priority = MEDIUM ✅

**MISCONCEPTION #5 TREATMENT IN M7 BACKBONE:**
- **Why It Emerges in M7:** §1.4 L278-282 explains that without full grids, dimensions become the only available tool, so students must connect dimensions to multiplication or they have no fallback strategy
- **Remediation Path (4-step):** §1.4 L292-296 details progression from partial grid (concrete count) → tick marks (bridge) → guide reveal (Late if needed) → vocabulary anchor
- **How M7 Targets It:** §1.4 L298-301 describes phase-by-phase instruction that "forces the multiplication action"

**MISCONCEPTION #8 TREATMENT IN M7 BACKBONE:**
- **Why It Emerges in M7:** §1.4 L317-319 explains that without grids, visual anchor for "square" units is lost
- **Observable Behaviors:** §1.4 L321-326 (area without unit, linear unit instead of square, incorrect unit, two separate units)
- **Remediation Path:** §1.4 L328-332 includes vocabulary anchor + explicit labeling + reinforcement
- **How M7 Targets It:** §1.4 L334-337 specifies tool and language requirements (Equation Builder unit labels, text-only unit requirement)

**SOURCE REFERENCE:** Backbone §1.0 L29-30, §1.4 L265-337, §1.6 L490-495, Excel Extraction Misconceptions Sheet, Working Notes Table A

---

### A7. Vocabulary Sequence

**CHECK:** New: side length, dimension. Reinforced: all four units, multiply, expression, factor, product. Vocabulary introduced AFTER concrete experience (per Known Pattern #11).

**FINDING:** ✅ PASS — KNOWN PATTERN #11 CORRECTLY APPLIED

**Details:**

**NEW VOCABULARY:**

| Term | Definition (from Backbone) | When Introduced | Sequencing Correct? |
|------|---------------------------|-----------------|-------------------|
| **Side Length** | §1.3 L192-199: "How long one side of a rectangle is" | "After Early phase (partial grid experience). Students see rows and columns concretely, then introduce the label 'side length.'" | ✅ **AFTER concrete** |
| **Dimension** | §1.3 L201-209: "A measurement; one of the factors in multiplication" | "Same timing as side length (after Early phase)" | ✅ **AFTER concrete** |

**KNOWN PATTERN #11 (From Research — Not Explicitly Cited But Implemented):**
The Backbone correctly implements the principle that vocabulary is introduced AFTER students have experienced concrete manipulation. Evidence:

- **Early Phase (L242):** Vocabulary staging table shows "Early (Partial Grid): (none formally) | Concrete experience before terminology"
- **Early→Mid Transition (L243):** "side length, dimension" introduced HERE, after students have worked with partial grids
- **Backbone Language (L149-150):** "Introduce after Early phase (partial grid experience), not before"

This directly prevents the misconception-creating error of defining terms before students have concrete referents.

**REINFORCED VOCABULARY:**

| Term | Prior Introduction | M7 Role | Status |
|------|-------------------|---------|--------|
| **Area** | M4 | §1.3 L220-221 reinforced throughout | ✅ |
| **Multiply** | M4 | §1.3 L224-226 "When we know the side lengths, we multiply them to find the area" | ✅ |
| **Expression** | M4 | §1.3 L228-230 "Equation Builder produces expressions" | ✅ |
| **Factor** | M4 | §1.3 L232-235 "The dimensions are the factors" | ✅ |
| **Product** | M4 | §1.3 L232-235 "The area is the product" | ✅ |
| **Square Units (All 4)** | M5-M6 | §1.3 L213-217 "All four units must appear in Mid (tick marks) and Late (dimensions only) phases" | ✅ |

**VOCABULARY STAGING TABLE (§1.3 L237-246):**
Correctly shows progression by phase with column "New Terms Introduced," "Reinforced Terms," and "Notes":
- Warm-up: (none) reinforced
- Early: (none formally) concrete experience before terminology
- Early→Mid Transition: side length, dimension introduced HERE
- Mid: (none new) apply terms
- Late: (none new) full abstract reasoning
- EC/Synthesis: (none new) consolidation

**SOURCE REFERENCE:** Backbone §1.3 L188-247, Working Notes §5 "Section Plan"

---

### A8. Transition Notes

**CHECK:** From M6: "What if there's no grid?" To M8: "What if you know the AREA and need to figure out the dimensions?"

**FINDING:** ✅ PASS — BOTH TRANSITIONS VERBATIM FROM TVP

**Details:**

**From M6 → M7 Transition:**
- **Backbone (§1.1 L77-78):** "M6 → M7 Transition Statement (from Synthesis): 'You can find area with ANY unit now. But you've always had a grid to count. What if there's no grid?'"
- **TVP Confirmation:** L665-669 states this exact bridge in the "Key Transition: M6 → M7" section
- **STATUS:** ✅ VERBATIM

**To M7 → M8 Transition:**
- **Backbone (§1.1 L91-92):** "M7 → M8 Transition Statement (from Synthesis): 'You found area when dimensions were GIVEN. What if you know the AREA and need to figure out what the dimensions could be?'"
- **TVP Confirmation:** L671-674 states similar language: "Bridge: 'You can find area from dimensions. But what if someone tells you the AREA and you have to figure out the dimensions? Let's try going the other direction.'"
- **STATUS:** ✅ SEMANTICALLY ALIGNED; SLIGHT WORDING DIFFERENCE ACCEPTABLE (Both convey reverse reasoning)

**BRIDGE LANGUAGE IN SYNTHESIS:**
- Backbone §1.5 L481-485 (Progression Summary) includes both transitions
- This placement is pedagogically sound: Synthesis phase explicitly prepares students for next module

**SOURCE REFERENCE:** Backbone §1.1 L77-92, TVP L665-674

---

### A9. CRA Stage

**CHECK:** Abstract. First module without full visual support. Does SP correctly position M7 in unit CRA arc?

**FINDING:** ✅ PASS

**Details:**

**M7 CRA Stage Specification (Backbone §1.0 L26-27):**
"**Abstract.** M7 is the first module in the Grade 3 progression WITHOUT full visual grid support. Students transition from 'counting visible squares' to 'inferring the complete rectangular array from side length dimensions.' This is the critical abstraction step in the CRA spiral."

**Unit CRA Arc Position (Backbone §1.0 L27 continued):**
- **Prior (M1-M6):** Concrete → Representational
  - M1-M4: Full grids (concrete/representational counting and multiplication connection)
  - M5-M6: Full grids with unit concepts (representational with extended unit focus)
- **M7 (This Module):** Abstract
  - Grids fade: partial → tick marks → dimensions only
  - Student infers complete structure from dimensions alone
- **Post (M8+):** Application/Fluency
  - M8 assumes no grid support is needed
  - Students work bidirectionally (forward and reverse)

**Alignment with Conceptual Spine Analysis (Excel Extraction, Conceptual Development Sheet):**
- **L317-322 (L8 - M7):** "Concept Focus: Area without full grid | Cognitive Demand: **Abstract** | Mathematical Move: Partial grids → tick marks; multiply side lengths"
- **STATUS:** ✅ EXACT MATCH

**Critical Abstraction Framing (Backbone §1.0 L27):**
The Backbone correctly identifies M7 as "the critical abstraction step in the CRA spiral" — this language acknowledges that this is a major pedagogical moment, not just another representational refinement.

**SOURCE REFERENCE:** Backbone §1.0 L26-27, Excel Extraction Conceptual Development L317-322, TVP L546

---

## SECTION D: SCOPE AND VOCABULARY ENFORCEMENT

### D1. Vocabulary Completeness

**CHECK:** Module Mapping vocab: side length, dimension. All in §1.2 or §1.3?

**FINDING:** ✅ PASS

**Details:**

**Module Mapping Source (Excel Extraction, Row 6):**
- "Vocabulary to Teach: side length, dimension"

**Backbone §1.2 (Scope Boundaries):**
- L144-150: "Side Length & Dimension Vocabulary (Introduced After Concrete Experience)"
  - Side length: Definition, timing, instructional sequence, usage examples
  - Dimension: Definition, timing, instructional sequence, critical connection statement, usage examples

**Backbone §1.3 (Vocabulary Architecture):**
- L190-209: "New Vocabulary (Introduced M7)" — Section 1.3.1 and 1.3.2
  - "Side Length" (L192-199): Full definition, when introduced, instructional sequence (3 steps), usage example
  - "Dimension" (L201-209): Full definition, when introduced, instructional sequence (3 steps), critical connection ("Dimensions ARE the factors in multiplication"), usage example

**VOCABULARY COMPLETENESS VERIFICATION:**
- ✅ Both terms explicitly taught in M7 (not as assumed prior knowledge)
- ✅ Both terms have timing notes (after concrete experience)
- ✅ Both terms have instructional sequences
- ✅ Both terms have usage examples
- ✅ Vocabulary Architecture table (L237-246) shows staging by phase

**SOURCE REFERENCE:** Backbone §1.2 L144-150, §1.3 L190-209, Excel Extraction Module Mapping Row 6

---

### D2. Scope Boundary Completeness

**CHECK:** Must Not Include: perimeter (Decision #5 — CRITICAL since students may add side lengths), composite figures, new units, ruler measurement (ruler dropped per M8 change narrative).

**FINDING:** ✅ PASS — ALL FOUR FORBIDDEN ITEMS EXPLICITLY EXCLUDED WITH REASONING

**Details:**

| Forbidden Item | Location | Decision Reference | Rationale Provided |
|---|---|---|---|
| **Perimeter Concept** | §1.2 L154-157 | Decision #5 | "Even as a differentiation tool for the 'add side lengths' misconception...Do not introduce perimeter language, formula, or concept" |
| **Composite Figures** | §1.2 L159-160 | (General scope) | "No L-shaped, T-shaped, or irregular figures. M7 is limited to simple rectangles in all four grid-fading states" |
| **New Units** | §1.2 L163-164 | Decision #7 | "All four unit types are from M5/M6. Do not introduce square kilometers, acres, or any new units in M7" |
| **Ruler Measurement** | §1.2 L167-170 | (M8 change narrative) | "No student measurement activities with physical rulers. All dimensions are given or read from grid/tick marks" |

**PERIMETER BOUNDARY (DECISION #5 CRITICAL CHECK):**
- **Backbone Language (§1.2 L157):** "Per Important Decision #5: Misconception #5 is addressed through multiplication reasoning alone"
- **Rationale:** Adding side lengths is the "add" variant of Misconception #5 (Not Multiplying Side Lengths)
- **Backbone Prevention Strategy (§1.4 L292-296):** Guide students away from adding via "we multiply to find area, not add"
- **No perimeter introduction:** ✅ Confirmed
- **Alignment with Decision #5:** Working Notes Table C L131 states "SME Resolved: NO. Do not introduce perimeter concept even to differentiate per Decision #5"

**SOURCE REFERENCE:** Backbone §1.2 L152-170, Working Notes Table C L131, Excel Extraction Important Decisions Decision #5

---

### D3. Critical Notes

**CHECK:** Module Mapping says "Key abstraction step in CRA progression." Is this reflected as central to the SP design?

**FINDING:** ✅ PASS — PROMINENTLY FEATURED

**Details:**

**Module Mapping Source (Excel Extraction, Row 6, Column "Notes"):**
"Key abstraction step in CRA progression."

**Backbone Prominence of This Principle:**

| Location | Treatment | Emphasis |
|----------|-----------|----------|
| §1.0 THE ONE THING L27 | "This is the critical abstraction step in the CRA spiral" | OPENING STATEMENT |
| §1.1 LEARNING GOALS L81 | "Cognitive Demand: Shift from 'count what you see' to 'multiply what you know'" | Learning mechanism |
| §1.0 L46 | "Biggest Risk: Grid fading pace. M7 must complete all three transitions...without scaffolding collapse" | Central pacing concern |
| §1.4 (Misconceptions) | #5 emerges precisely because "grid support disappears. Dimensions become the ONLY information available" (L280) | Threat analysis |
| §1.5 (Toy Spec) L361-363 | Three animated transitions emphasize the pedagogical beats of fading | Instructional mechanism |

**The abstraction principle is clearly the organizing logic of the module, not a side note.** Every major section references it.

**SOURCE REFERENCE:** Backbone §1.0 L27 & L46, §1.1 L81, §1.4 L278-282, Excel Extraction Module Mapping Row 6

---

### D4. Cross-Reference Table Accuracy

**CHECK:** Spot-check accuracy of Tables A and B.

**FINDING:** ✅ PASS — ALL SPOT CHECKS VERIFY

**Details:**

**Working Notes Table A (Module Mapping — Verbatim Transcription):**

| Field | Working Notes Transcription | Source (Excel) | Match |
|-------|----------------------------|---|---|
| Module | M7 | L6 Module Mapping | ✅ |
| OUR Lessons | L8 | L52 Module Mapping | ✅ |
| Core Concept | Area Without a Full Grid | L53 Module Mapping | ✅ |
| Learning Goal (Verbatim) | Determine the area of rectangles not displayed on a grid. | L54 Module Mapping | ✅ |
| Vocabulary to Teach | side length, dimension | L59 Module Mapping | ✅ |
| Key Misconceptions | M5 (not multiplying side lengths) | L63 Module Mapping | ✅ (Note: M5 = global ID #5) |

**Working Notes Table B (TVP Full M7 Phase Flow):**

Spot-check three key teaching points:

| Teaching Point | TVP Source | Working Notes Table B | Match |
|---|---|---|---|
| "You don't need to SEE every square to know how many there are" | TVP L540 | Working Notes L34 (Key Teaching Points #1) | ✅ EXACT |
| "THE BIG INSIGHT: The grid was always just a visual confirmation..." | TVP L542 | Working Notes L36 (Key Teaching Points #3) | ✅ EXACT |
| "Portuguese azulejos (decorative tiles) available as optional enrichment context" | TVP L544 | Working Notes L38 | ✅ EXACT |

**Spot-check Data Constraints (Table B L100-105):**

| Constraint | TVP Source | Working Notes Table B | Match |
|---|---|---|---|
| Partial Grid: One ≤5, other 3-9, ≤45 | L643-644 | L102 | ✅ |
| Tick Marks: Factors 3-10, ≤100 | L647-649 | L103 | ✅ |
| Dimensions-Only: Factors 2-10, ≤100 | L651-653 | L104 | ✅ |
| Text-Only: Rigid template | L655-657 | L105 | ✅ |

**SOURCE REFERENCE:** Working Notes §1 & §2, Excel Extraction, TVP L530-658

---

### D5. Design Constraint Compliance

**CHECK:** Decision #3 is THE critical decision for M7. Verify: grid fading sequence matches exactly (M7: partial → tick marks → dimensions only). Decision #5 (no perimeter — especially important since adding side lengths is a common error pattern in M7).

**FINDING:** ✅ PASS — BOTH CRITICAL DECISIONS CORRECTLY IMPLEMENTED

**Details:**

**DECISION #3 (PROGRESSIVE GRID REMOVAL) — CRITICAL FOR M7:**

TVP Statement (Excel Extraction, Important Decisions L98-116):
```
IMPLEMENTATION BY MODULE:
...
- M7: Grid fading begins (partial grid → tick marks → dimensions only)
- M8-M9: Dimensions only / text-only (abstract problem-solving)
...
```

Backbone Implementation (§1.2 L121-126):
```
1. **Grid Fading Progression (Complete in M7)**
   - Warm-up: Full grid shown as reference for familiar rectangle (e.g., 4×6)
   - Early Phase: Partial grid (first row and first column filled; interior empty)
   - Mid Phase: Tick marks only (evenly spaced marks on top and left edges; no grid interior)
   - Late Phase: Dimensions only (rectangle outline with dimension labels; no grid, no tick marks)
   - **Critical:** All three transitions must complete within M7. No backsliding to M8.
```

**SEQUENCE VERIFICATION:**
- Full grid (Warm-up) → Partial (Early) → Tick marks (Mid) → Dimensions only (Late) → Text-only (Late/EC)
- ✅ **EXACT MATCH** to Decision #3 implementation specification

**DECISION #5 (NO PERIMETER) — CRITICAL FOR M7:**

TVP Statement (Excel Extraction, Important Decisions L138-148):
```
DECISION 5: Perimeter Kept Separate - Do Not Introduce
DECISION: Do NOT introduce perimeter in this unit. Do not proactively address
perimeter-area confusion unless data shows students bringing it in.
RATIONALE: Research strongly supports teaching area and perimeter at different
times initially (Van de Walle et al., 2014). Introducing perimeter to "clarify
the difference" often CREATES confusion where none existed.
CONFIDENCE: HIGH
```

Backbone Implementation:

| Location | Language | Status |
|----------|----------|--------|
| §1.2 L154-157 (SCOPE) | "**Perimeter Concept** — Even as a differentiation tool for the 'add side lengths' misconception. Do not introduce perimeter language, formula, or concept. **Per Important Decision #5:** Misconception #5 is addressed through multiplication reasoning alone" | ✅ EXPLICIT |
| §1.3 L250 (FORBIDDEN) | "**Perimeter** — Do not use, even for contrast or clarification. If student adds side lengths, address via: 'We multiply to find area, not add.'" | ✅ EXPLICIT |
| §1.4 L292-296 (REMEDIATION) | Remediation pathway for #5 uses multiplication reasoning, not perimeter introduction | ✅ NO PERIMETER |

**ADDITION MISCONCEPTION LINK:**
Adding dimensions (5 + 4 = 9) is Variant 2 of Misconception #5 observable behavior (§1.4 L273-276). The Backbone correctly prevents this by:
1. Never introducing perimeter (Decision #5)
2. Explicitly teaching "we multiply to find area, not add" (§1.3 L250)
3. Remediating via Equation Builder (§1.4 L300-301) which "forces the multiplication action"

**SOURCE REFERENCE:** Backbone §1.2 L154-157, §1.3 L250, §1.4 L273-296, Excel Extraction Important Decisions #3 & #5

---

## SECTION SP: CONCEPTUAL SPINE VALIDATION

### SP1. Spine Expectation Alignment

**CHECK:** Spine says "Area without visible grid" is INTRODUCED in L8/M7. Does SP treat it as genuinely new? Cognitive demand "Abstract" — does CRA match? Does the progression within M7 match the Spine's expectation?

**FINDING:** ✅ PASS

**Details:**

**Conceptual Spine Source (Excel Extraction, Conceptual Spine Analysis):**

| Concept | Where Introduced | Where Developed | Where Mastered |
|---------|------------------|-----------------|-----------------|
| **Area without visible grid** | **L8 (M7)** | L9 (M8) | L10-11 (M8-M9) |

Backbone Treatment:
- ✅ **Introduced in M7 (L8):** §1.0 L23-24 testable core: "By the end of M7, students can determine the area of a rectangle from its dimensions alone (no grid, no tick marks)"
- ✅ **Treated as genuinely new:** §1.0 L46 identifies as "Biggest Risk" — pacing of three transitions must be managed carefully
- ✅ **Cognitive demand "Abstract" matches:** §1.0 L26-27 states "Abstract. M7 is the first module in the Grade 3 progression WITHOUT full visual grid support"

**CRA Stage Verification:**

| Stage | M7 Treatment | Spine Expectation | Match |
|-------|---|---|---|
| **Abstract** | "M7 is the first module...WITHOUT full visual grid support" (§1.0 L26) | Cognitive Development L321: "Cognitive Demand: Abstract" | ✅ |
| **Progression Within Module** | Full grid (ref) → Partial → Tick marks → Dimensions only (§1.2 L121-126) | "Area without visible grid" introduced in L8 | ✅ MATCHES |
| **Transition Out** | To M8: reverse reasoning (§1.1 L91-92) | "Where Developed: L9 (M8)" | ✅ SETS UP NEXT |

**Progression Within M7 Aligns with Spine Expectation:**
The Spine expects "Area without visible grid" to be INTRODUCED in L8/M7. The Backbone's progression (full → partial → tick marks → dimensions) accomplishes this introduction in stages within the single module, making the abstraction gradual but comprehensive.

**SOURCE REFERENCE:** Backbone §1.0 L26-27 & L46, §1.1 L91-92, §1.2 L121-126, Excel Extraction Conceptual Spine Analysis

---

## ADDITIONAL CHECKS: CROSS-DOCUMENT CONSISTENCY

### Consistency Check: Backbone vs. Working Notes

**FINDING:** ✅ PASS — NO CONFLICTS DETECTED

**Spot-Check Summary:**
- §1.0 "THE ONE THING" language matches Working Notes §1 Table A
- §1.1 Learning Goals match Table A verbatim transcription ✅
- §1.2 Scope Boundaries match Module Mapping specification ✅
- §1.4 Misconceptions match Excel Extraction IDs and priorities ✅
- §1.5 Toy Specifications match TVP data constraints ✅

### Consistency Check: Backbone vs. M6 Backbone

**FINDING:** ✅ PASS — APPROPRIATE CONTINUITY WITH CHANGE

**Expected Changes from M6 → M7:**
- M6: "Last full-grid module" (M6 Backbone §1.0 L36)
- M7: "First module without full grid support" (M7 Backbone §1.0 L26)

**Progression Check:**
- M6 Synthesis: "You can find area with ANY unit now. But you've always had a grid to count. What if there's no grid?" (M6 Backbone APPENDIX L595)
- M7 Warm-up: Same rectangle shown with grid removed — only outline + dimension labels (M7 Backbone §1.5 L361)
- ✅ LOGICAL CONTINUATION

**Unit Selection (M6 → M7):**
- M6 teaches unit selection with Tier scaffolding (decision-making when given full grids)
- M7 assumes unit selection fluency and focuses on dimensions-only reasoning
- ✅ APPROPRIATE PROGRESSION

---

## FINDINGS SUMMARY

### Strengths

1. **Decision #3 Implementation (Grid Fading):** Exceptional specificity. All four display modes defined with clear constraints. Animated transitions documented with pedagogical messages.

2. **Misconception #5 Targeting:** Three-phase remediation pathway (partial grid → tick marks → guide reveal) is clear and actionable. Equation Builder design intentionally "forces the multiplication action."

3. **Vocabulary Sequencing:** Correctly implements Known Pattern #11 (introduce after concrete experience). Side length and dimension are explicitly staged after Early phase.

4. **Scope Boundaries:** All four forbidden items (perimeter, composites, new units, ruler) explicitly excluded with reasoning. Decision #5 compliance is transparent and justified.

5. **TVP Source Fidelity:** High alignment with TVP teaching points, data constraints, and SME resolutions. No discrepancies detected.

6. **Transition Bridges:** Both From M6 and To M8 transitions are verbatim or semantically equivalent to TVP language.

---

### Critical Issues Requiring Clarification

#### CRITICAL ISSUE #1: Guide Reveal Specification

**Issue:** The guide reveal mechanism (§1.5 L365-377) specifies that "2+ reveals flag M3 reinforcement," but implementation details are vague.

**Questions for Clarification:**
1. Is the flag automatic (system-generated when 2nd reveal is triggered) or manual (guide must note)?
2. Where does the flag appear? In guide notes? In a mastery gate report? In module completion data?
3. What is the student experience if they've triggered the flag? Do they proceed to M7 or do they complete additional M3 review before moving forward?

**Source:**
- Backbone §1.5 L372: "If ≥2 reveals used, flag student for M3 reinforcement review in guide notes."
- TVP L629: "Students who consistently trigger this remediation may need M3 reinforcement flagged in mastery tracking."

**Impact:** Starter Pack author needs clear specification on flag mechanism before designing the guide script for Late Phase.

**Recommendation:** Clarify with instructional designer and system architect before SP author handoff.

---

#### CRITICAL ISSUE #2: Equation Builder Design Status

**Issue:** Equation Builder is listed as a Primary Toy but with Notion link "In development."

**Details:**
- M6 Backbone §1.5 lists Equation Builder as "In development" (L8)
- M7 Backbone also lists as "In development" (L8)
- M7 assigns Equation Builder critical roles:
  - Early Phase: "Optional" verbal/written response (L417)
  - Mid Phase: "Full Equation Builder online" (L418)
  - Late Phase: "Full Equation Builder" (L419)
  - EC (Text-Only): "Embedded in text" (L420)

**Risk:** If Equation Builder is not available or its design differs from M7 specification, the entire Mid/Late/EC instructional sequence collapses.

**Current Specification in Backbone:**
- Drag-to-place interaction (Important Decision #6) ✅
- Labeled factor slots ✅
- Unit labels required ✅
- Format examples provided ✅

**Recommendation:** Confirm Equation Builder design status and finalize Notion spec before SP author begins writing Mid Phase interactions.

---

#### CRITICAL ISSUE #3: Text-Only Problem Context Clarity

**Issue:** Text-only problems specify a rigid template (§1.2 L137-139) but no guidance on object variety.

**Details:**
- Template: "A [object] is [number] [unit] long and [number] [unit] wide. What is its area?"
- Working Notes Flag A4 (L250): "Can [object] be any noun or constrained (e.g., tiles, rectangles, fields)?"
- Resolution: "PENDING DECISION"

**Backbone Treatment:**
- §1.2 L138-140 provides three examples: carpet, tile floor, rectangular garden
- §1.5 L418-420 mentions text-only as "embedded in text"
- No explicit constraint on object variety

**For Starter Pack Author:** Clarify whether objects should be:
- Real-world contexts familiar to Grade 3 (carpet, garden, room floor, desk, poster)
- Generic mathematical terms (rectangle, object, shape, plot)
- Mix of both

**Recommendation:** Provide content author guidelines with 10-15 approved objects before SP author writes Late Phase text-only problems.

---

### Minor Issues (Informational, Not Blocking)

#### Minor Issue #1: Azulejos Context

**Status:** Working Notes Flag A1 (L246-247) notes Portuguese azulejos as optional enrichment.

**Backbone Treatment:** Not mentioned in Backbone. This is appropriate (optional content should not constrain core design).

**Action:** Content author decision for Practice tier; does not block SP authoring.

---

#### Minor Issue #2: Animation Specifications

**Status:** Working Notes Flag A2 (L248) requests exact animation specs (fade, sweep, duration).

**Backbone Treatment:** Described pedagogically ("fade animation," "same rectangle transitioning between modes") but not with technical precision.

**Action:** Instructional Designer + Engineering (not SP author) responsibility.

---

#### Minor Issue #3: Reverse Problem Tagging

**Status:** Working Notes Flag A5 (L251-252) mentions reverse problems tagged as TRANSFER in Practice.

**Backbone Treatment:** Mentioned in §1.5 L387 (EC row): "Mixed | Mixed | Mixed | ≤ 100 | All four | Forward and reverse 50/50. Reverse tagged TRANSFER."

**Action:** SP author will implement when designing Practice Phase inputs (§1.8.5).

---

## RECOMMENDATIONS FOR GATE 1 SIGN-OFF

### Conditional PASS — Three Items Required Before SP Author Handoff

| Item | Priority | Owner | Deadline |
|------|----------|-------|----------|
| **1. Guide Reveal Specification Clarification** | CRITICAL | Instructional Designer + System Architect | Before SP author begins Late Phase |
| **2. Equation Builder Notion Spec Finalization** | CRITICAL | Engineering + Instructional Designer | Before SP author begins Mid/Late Phase |
| **3. Text-Only Problem Context Guidelines** | CRITICAL | Content Author | Before SP author writes Late Phase |

### No Blocking Changes Required

The following do not prevent SP authoring but should be resolved in parallel:
- Animation technical specifications (Instructional Designer + Engineering)
- Azulejos enrichment scope (Content Author)
- Reverse problem practice distribution (Practice Phase Playbook author)

---

## DETAILED COMPLIANCE MATRIX

### Gate 1 Checks: PASS/FAIL Summary

| Check | Category | Result | Source |
|-------|----------|--------|--------|
| **A1. Toy List & Config** | Source Fidelity | ✅ PASS | Backbone §1.5 vs. TVP L530-659 |
| **A2. Scaffolding Progression** | Source Fidelity | ✅ PASS | Backbone §1.0-1.5 vs. TVP L560-600 |
| **A3. Data Constraints** | Source Fidelity | ✅ PASS | Backbone §1.5 L379-387 vs. TVP L641-658 |
| **A4. Key Beats** | Source Fidelity | ✅ PASS | Backbone §1.0-1.5 vs. TVP L557-600 |
| **A5. SME-Resolved Decisions** | Source Fidelity | ✅ PASS | Backbone vs. Working Notes Table C |
| **A6. Misconceptions** | Source Fidelity | ✅ PASS | Backbone §1.4 vs. Excel Misconceptions |
| **A7. Vocabulary Sequence** | Source Fidelity | ✅ PASS | Backbone §1.3 vs. Module Mapping |
| **A8. Transition Notes** | Source Fidelity | ✅ PASS | Backbone §1.1 vs. TVP L665-674 |
| **A9. CRA Stage** | Source Fidelity | ✅ PASS | Backbone §1.0 vs. Conceptual Spine |
| **D1. Vocabulary Completeness** | Scope/Vocab | ✅ PASS | Backbone §1.2-1.3 |
| **D2. Scope Boundary Completeness** | Scope/Vocab | ✅ PASS | Backbone §1.2 vs. Decision #5 |
| **D3. Critical Notes** | Scope/Vocab | ✅ PASS | Backbone §1.0 vs. Module Mapping |
| **D4. Cross-Reference Table Accuracy** | Scope/Vocab | ✅ PASS | Backbone vs. Working Notes Tables A-B |
| **D5. Design Constraint Compliance** | Scope/Vocab | ✅ PASS | Backbone §1.2 & 1.5 vs. Decision #3 & #5 |
| **SP1. Spine Expectation Alignment** | Conceptual Spine | ✅ PASS | Backbone §1.0 vs. Conceptual Spine |

**Overall Backbone Compliance:** 15/15 CHECKS PASS ✅

---

## FINAL ASSESSMENT

### Backbone Readiness

**Status:** READY FOR STARTER PACK AUTHORING (Conditional on three clarifications)

**Quality Indicators:**
- ✅ Comprehensive coverage of §1.0 through §1.5 (all required sections present)
- ✅ Cross-references to Decision #3 and #5 explicit and correct
- ✅ Misconception #5 remediation pathway is detailed and actionable
- ✅ Vocabulary staging respects research-based principles (Known Pattern #11)
- ✅ TVP source fidelity is high; no material discrepancies detected
- ✅ All scope boundaries enforced; forbidden items explicitly excluded
- ⚠️ Three clarifications needed before SP author handoff (none are backbone-level issues)

### Next Steps

1. **Immediately:** Circulate three clarification requests to:
   - Instructional Designer (guide reveal, animation specs)
   - Engineering Lead (Equation Builder status)
   - Content Author (text-only objects, azulejos scope)

2. **Within 3 days:** Resolve clarifications and finalize:
   - Guide Reveal Specification Document
   - Equation Builder Notion Spec (M7 config)
   - Text-Only Problem Content Guidelines

3. **Handoff Trigger:** Once clarifications are resolved, this Backbone is ready for Starter Pack author to begin §1.6 (Warmup Phase Specification).

---

## DOCUMENT PROVENANCE & REFERENCES

### Source Documents Read
1. ✅ `/sessions/practical-vibrant-heisenberg/mnt/Starter Pack Generation Experiment/G3U2M7_Task1_Backbone.md`
2. ✅ `/sessions/practical-vibrant-heisenberg/mnt/Starter Pack Generation Experiment/G3U2M7_Working_Notes.md`
3. ✅ `/sessions/practical-vibrant-heisenberg/Excel_Extraction_Complete_M5_M6_M7.txt`
4. ✅ `/tmp/module_content.txt` (TVP M7 section, lines 530-687)
5. ✅ `/sessions/practical-vibrant-heisenberg/mnt/Starter Pack Generation Experiment/MODULE STARTER PACK TEMPLATE.02.04.26.md`
6. ✅ `/sessions/practical-vibrant-heisenberg/mnt/Starter Pack Generation Experiment/G3U2M6_Task1_Backbone.md` (for cross-module verification)

### Evaluation Methodology
- **A1-A9 (Section A: Source Fidelity):** Line-by-line cross-reference to TVP and Working Notes
- **D1-D5 (Section D: Scope & Vocabulary):** Verification against Module Mapping, Excel Extractions, and Important Decisions
- **SP1 (Section SP: Conceptual Spine):** Alignment check against Conceptual Spine Analysis sheet
- **Consistency Checks:** Cross-document verification (Backbone vs. Working Notes vs. M6 vs. TVP)

### Citation Standards
All citations reference:
- Document name (Backbone, Working Notes, TVP, Excel Extraction)
- Section number and title (§1.0, §1.5, L123, etc.)
- Line number (from Read tool output)

---

## CONCLUSION

**M7 Backbone Draft: PASSES GATE 1 EVALUATION**

The Backbone correctly implements the critical abstraction step of Unit 2's CRA progression. Decision #3 (Progressive Grid Removal) is the clear organizing principle, with grid fading (partial → tick marks → dimensions only) fully specified within the module. Misconception #5 (Not Multiplying Side Lengths) is thoroughly targeted across all phases with escalating abstraction. The document is comprehensive, well-researched, and ready for Starter Pack authoring with three minor clarifications.

**Confidence Level:** HIGH (15/15 checks pass; 3 clarifications are implementation details, not backbone-level issues)

---

**End of Gate 1 Evaluation Report**

**Document Ready for:** Instructional Designer Review → Clarification Resolution → Starter Pack Author Handoff
