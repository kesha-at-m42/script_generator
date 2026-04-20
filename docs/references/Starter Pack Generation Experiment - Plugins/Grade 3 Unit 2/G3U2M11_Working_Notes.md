# G3U2 M11 — Working Notes

**Module:** M11
**Title:** Area is Additive
**Unit:** Unit 2 (Area and Multiplication)
**Domain:** Measurement and Data (3.MD)
**Grade:** 3
**Prior module:** M10 (Area and the Multiplication Table)
**Next module:** M12 (Composite Figures Without Grids)
**OUR Lesson:** L12
**Standard Addressed:** 3.MD.C.7.d (area as additive — decomposing rectilinear figures into non-overlapping rectangles)

---

## Session Log

**Session 1 (2026-03-30):** Starting fresh. Task 1 completed:
- Tables A, B, C populated with verbatim extractions
- Design Constraints extracted (9 decisions evaluated)
- Edit Reconciliation: CLEAN (no numbered edits; 7 SME resolutions documented)
- Data Constraint Audit: PASS (8 example sets; 1 minor TVP text inconsistency noted)
- Section Plan completed
- Backbone §1.0–§1.5 drafted
- Self-check: 16/16 items PASS
- L1 Gate 1 smoke test: 1 MINOR remaining (YAML module_id format — by-design)
- Full L1 + L2 Gate 1 evaluation run. L1: 1 MINOR (by-design). L2: 0 CRITICAL, 0 MAJOR, 5 MINOR (source-fidelity), 1 NOTE.
- Applied 5 source-fidelity MINOR clarifications: (1) warmup vocab staging note, (2) Equation Builder availability-by-phase precision, (3) parentheses notation emphasis as descriptive, (4) data constraint reasoning for total-area ceilings, (5) — merged into #3.
- Applied author SHOULD-FIX: T-shape exception in Early corner-identification beat (§1.2 figure types, §1.5 config table, §1.5 capabilities). TVP explicitly places a T-shape in Early for corner identification only (recognition, no decomposition). Backbone's blanket "T-shapes Late only" didn't distinguish recognition vs. decomposition. Fix adds the exception with rationale (prevents "one inside corner per figure" overgeneralization).
- Applied author Minor 4: Late efficiency observation + validate-first safeguard (§1.2). TVP says efficiency is observation only (1 problem), never assessed. Added validate-first principle: a correct decomposition is NEVER wrong even if inefficient.
- Re-run L1 smoke test: PASS. 8/8 checkers ran. 2 MINOR (both by-design: YAML module_id format, module map ID format mismatch). 0 new findings from applied fixes.
- Backbone ready for author review → Gate 1 approval
- Gate 1 APPROVED by author.

**Session 1 (continued) — Task 2:**
- Read all 4 required playbooks: Warmup Phase Playbook, Lesson Phase Playbook, Guide vs Prompt Structure Reference, Voice Script Prompt (§1–§4). Read M10 §1.6 Warmup (opening line for Pattern #40) and §1.9 Synthesis (M11 bridge callback source).
- Extracted Warmup Requirements Checklist (WR-1 through WR-13) and Lesson Requirements Checklist (LR-1 through LR-16) per guidance Step 1.
- Drafted §1.6 Warmup: Activation + Discovery hybrid type. 4 interactions (W.1–W.4): 2 Grid Rectangles forward checks → L-shape counting → system decomposition demonstration. TVP warmup flow followed exactly (Version 2 text per Conflict #8). Core Purpose includes Key Function, Why This Serves, and necessity Test.
- Drafted §1.7 Lesson: 3 sections (Early S1.1–S1.5, Mid S2.1–S2.4, Late S3.1–S3.4). 13 interactions total. CRA: Concrete (Early) → Relational (Mid) → Application (Late). 3 worked examples with fading. 1 think-aloud with [PLANNING]/[ATTENTION]/[SELF-CHECK]. Vocabulary staging matches §1.3 exactly. Required/Forbidden Phrases sections present. Misconception Prevention section present. Section transition markers present. All interactions have type labels.
- Key design choices: (1) Corner identification beat placed after bounding-rectangle demo (S1.5), (2) Multiple decomposition beat split into "observe comparison" (S2.2) + "student does both" (S2.4) per TVP, (3) Efficiency observation in S3.4 fires conditionally (only if student uses 3 rectangles when 2 suffice) with validate-first safeguard, (4) Purpose Frame connects Warmup directly to Lesson workflow using only known vocabulary.
- Dimension tracking values used in Lesson: S1.1 (4×3 + 5×2 = 22), S1.2 (3×6 + 2×4 = 26), S1.4 (bounding 6×5 = 30), S2.2 (comparison: Method 1 and 2 both = 22), S3.3 (3-component, values TBD at script level).
- L1 + L2 Gate 2 evaluation pending

---

## Cross-Reference Table A — Module Mapping Extraction

```
MODULE MAPPING: M11
====================
The One Thing: [Not a separate column — derived from Core Concept + Learning Goals]
Core Concept: Area is Additive
OUR Lessons: L12
OUR Learning Goals (Verbatim): Find the area of figures composed of rectangles. Recognize that area is additive.
Standards - Building On: 3.MD.C.7.b (rectangle area - from M4-M9); 2.NBT.B.5 (add within 100)
Standards - Addressing: 3.MD.C.7.d (area as additive - decomposing)
Standards - Building Towards: 3.NBT.A.2 (add within 1000); 3.MD.C.7.d (ungridded figures)
Notes: Introduction to composite figures WITH FULL GRIDS. Key insight: decompose into rectangles, find each area, ADD together. Multiple valid decompositions. Parentheses introduced for grouping expressions.
Vocabulary to Teach: composite figure, decompose, rectilinear
Question/Test Language: Find the area of this figure. Show how you broke it into rectangles. Is there another way to decompose this figure?
Vocabulary Teaching Notes: Decompose = break into parts. Composite = made of multiple parts. Rectilinear = made of rectangles (all right angles).
Scaffolding of Visuals: Gridded L-shapes and rectilinear figures; Multiple decomposition options shown; Color-coding for different rectangles
Key Misconceptions: M6 (overlapping decomposition); M11 (completing the rectangle)
```

**Flags on Table A fields:**
- "The One Thing" is not a separate column in the Module Mapping. Will derive from TVP Learning Goal per guidance.
- "Question/Test Language" contains 3 stems that must appear in §1.1 or be flagged for §1.7: (1) "Find the area of this figure," (2) "Show how you broke it into rectangles," (3) "Is there another way to decompose this figure?"
- Vocabulary to Teach lists 3 terms; TVP distinguishes "rectilinear" as receptive-only. This is a potential conflict (see Table C).
- Misconception IDs use module-number shorthand ("M6", "M11") — need to map to global database IDs: M6 → ID 6.0 (Overlapping Decomposition); M11 → ID 11.0 (Completing the Rectangle).

---

## Cross-Reference Table B — TVP Extraction

```
TVP: MODULE 11
===============
OUR Lesson: L12
Standard: 3.MD.C.7.d (area as additive — decomposing rectilinear figures into non-overlapping rectangles)

⚠️ CRA RESET — GRIDS RETURN. After M7's grid fading and M8–M10's fully abstract
work, this module returns to full grids. Composite figures are a NEW concept requiring
concrete support. The CRA progression resets for the new concept.

New primary tool: Composite Figures. Grid Rectangles are NOT used in M11. Composite
Figures provides its own continuous grid across the entire shape. The grid spans the
whole figure (one shape), not separate grids per rectangle (multiple shapes).

Learning Goal: Find the area of figures composed of rectangles. Recognize that area
is additive — the total area of a composite figure equals the sum of its parts.

Key Teaching Points:
1. THE BIG INSIGHT: You can break a complicated shape into rectangles you already
   know how to measure. Find each rectangle's area, then ADD them together. This
   works because area is additive — the total area is the sum of non-overlapping parts.
2. This isn't a rectangle, so you can't just multiply two sides. But it's MADE of
   rectangles. The only new skill is decomposition — seeing where to draw the line.
3. There's often MORE THAN ONE correct way to decompose a figure. Different
   decompositions produce different rectangles but always the same total area.
4. Parentheses in expressions: (4 × 5) + (3 × 6) = 20 + 18 = 38. Parentheses group
   each rectangle's area calculation before adding. Notation, not a new operation.
5. The grid makes every square visible. Students can COUNT to verify their
   multiplication. Safety net — decomposition is new, but area-finding is M3–M4 territory.

CRA Stage: Concrete/Representational — full grids throughout. M12 begins fading.

Cognitive Focus:
- IDENTIFY (Conceptual) — recognizing that a composite figure is made of rectangles;
  seeing where decomposition lines can go
- CREATE (Procedural) — drawing decomposition lines to partition a figure into rectangles
- APPLY (Transfer) — using known rectangle-area skills in a new context (parts of a
  composite figure), then adding results
- CONNECT (Transfer) — linking the additive property of area to the visual
  decomposition — "two parts, one total"

Misconceptions Targeted:
- #11: Completing the Rectangle (PRIMARY) — Students treat L-shapes as complete
  rectangles by multiplying longest horizontal × longest vertical. Full grid is the
  primary defense. Guide explicitly addresses: "Is this shape a rectangle? No — look
  at the corner. Those squares aren't there."
- #6: Overlapping Decomposition (SECONDARY) — Students draw a line creating
  overlapping regions and count some squares twice. Grid makes this visible. System
  validation prevents it in the tool, but guide addresses the CONCEPT.

PHASE-BY-PHASE FLOW:

WARM-UP:
- Grid Rectangles (outline + dimensions, no grid) → 2 rapid forward area problems.
  "This rectangle is 5 by 4. What's the area?" and "This rectangle is 7 by 3. What's
  the area?" Purpose: confirm dimensions-to-area multiplication is automatic.
  ⚠️ NOTE: TVP text contains a DUPLICATE of this warmup block (paras 39-42 and 51-53).
  The second instance slightly varies the framing ("People approach this kind of problem
  differently. Here's one way that always works..." vs "You got it — 22 square units.
  You counted every square. But that took a while."). The second version is the refined
  text. Using the second version.
- Composite Figures (L-shape, full grid, 2 components) → Display only. Show L-shaped
  figure with full grid. Guide: "This shape isn't a rectangle. Can you still find its area?"
  Student counts all squares: MC with total (e.g., 22 squares).
  After answer: "You got it — 22 square units! People approach this kind of problem
  differently. Here's one way that always works..."
- System demonstrates decomposition: System draws a horizontal (or vertical) line through
  the figure, splitting it into two rectangles. Each rectangle highlights in a different
  color. Student: blue area (MC) + pink area (MC) = total (MC).
- Purpose: Activate prior knowledge, surface the L-shape, show decomposition is a
  reliable strategy. The warm-up introduces the IDEA visually; Early activities
  formalize the workflow.
- "No teaching in warm-up" — the decompose-calculate-add workflow is introduced in
  Early activities.

LESSON — EARLY (System decomposes, student calculates):
- Composite Figures (L-shapes + simple rectilinear, full grid, 2 components) +
  Equation Builder (addition with parenthesized multiplication)
- System displays composite figure with decomposition line already drawn. Two rectangles
  highlighted in different colors.
- For each rectangle: system highlights it, shows dimensions. Student finds area via MC.
- After both areas: "Now add them together." Equation Builder displays:
  (4 × 3) + (5 × 2) = ___ → Student selects total from MC.
- Parentheses introduction (first time): Guide: "The parentheses show that we're finding
  each rectangle's area first, then adding."
- 3–4 problems. System places all decomposition lines.
- Additive property statement (after 2nd problem): "When you find each rectangle's area
  and add them, you get the total area of the whole shape. That's because the area is
  ADDITIVE — the parts add up to the whole."
- Completing the rectangle check (after 3rd problem): System shows bounding rectangle
  (dotted outline). "If we multiplied 6 by 5, we'd get 30. But are there 30 squares?"
  Highlights "missing corner." "The bounding rectangle is too big — it includes squares
  that don't belong to our shape. Just multiplying the longest sides doesn't work BY
  ITSELF. That's why we break the shape into parts."
  ⚠️ NOTE: "by itself" framing is deliberate foreshadowing for M12 Late (subtraction
  decomposition).
- Key beat — finding the cut point (after completing-rectangle check): Guide: "Find a
  corner that goes INWARD — not one of the outside corners, but a corner that points
  INTO the shape." Student selects from highlighted corners (MC: 2–3 outside + 1–2
  inside corners). Then: 2 more composite shapes with all corners highlighted. Student
  identifies inside corner(s) on each. T-shape has 2 inside corners.
  Cost: ~2–3 minutes (3 shapes, corner identification only).

LESSON — MID (Student draws decomposition lines):
- Composite Figures (L-shapes + simple rectilinear, full grid, 2–3 components) +
  Equation Builder
- Student places a straight line across the figure. System validates: horizontal or
  vertical, edge-to-edge, creates complete rectangles.
  ⚠️ Engineering/UX: interaction pattern needs usability testing. Options: two-tap,
  snap-to-cut, constrained drag.
- Key beat — multiple valid decompositions (after 2nd problem): After student solves one
  way, guide: "Is that the ONLY way to break it apart?" System shows alternative
  decomposition. Student calculates both ways — same total.
  "Different rectangles, same total area! Area is additive."
- 1 problem where student tries SECOND decomposition + 1 where guide just mentions
  "there's another way."
- Equation Builder shows both expressions side by side.

LESSON — LATE (Independent decompose-calculate-add):
- Composite Figures (L-shapes, T-shapes, U-shapes, full grid, 2–3 components) +
  Equation Builder (available but not pre-loaded)
- Full independence: student sees figure, draws line(s), calculates, adds.
- Figure variety increases: L + T + U shapes (still 2–3 components).
- Limit 3-component figures to 1–2 problems.
- 3–4 problems total.
- Key beat — choosing efficient decompositions (1 problem only): "You broke it into 3
  rectangles. Could you have done it with just 2?" Light-touch efficiency observation.
- Valid but awkward decompositions: ALWAYS validate first, then optionally note efficiency.

EXIT CHECK:
- 3 problems:
  1. Guided decomposition → calculate: L-shape with system-placed decomposition line.
     Two rectangles color-coded, dimensions labeled. "What is the total area?" Student
     calculates each area (MC), then adds (MC). Tests: calculate + add given decomposition.
  2. Student decomposition → calculate: L-shape with NO decomposition line. "Break this
     figure into rectangles and find the total area." Student draws line, then calculates.
     Tests: identify valid decomposition AND complete calculation.
  3. Misconception check: Figure with answer options including "completing the rectangle"
     error. E.g., L-shape with bounding box 6 × 8. Correct = 38. MC includes 48 (6×8
     bounding), 38 (correct), 28 (partial calculation), 34 (addition error).
     Tests: avoids bounding-rectangle trap.
- Assessment ratio: 1 guided : 1 independent : 1 misconception-targeted.

PRACTICE:
- Mixed figure types: L-shapes, T-shapes, U-shapes
- All gridded (full grid throughout M11)
- Student draws decomposition lines for all problems
- Some problems ask: "Show TWO different ways to break this figure into rectangles."
- Equation Builder available for all problems
- Error patterns to watch: completing the rectangle, overlapping decomposition,
  forgetting to add, dimension misread

SYNTHESIS:
- The decompose-calculate-add strategy summary
- Vocabulary consolidation: composite figure (new active), decompose (new active),
  rectilinear (receptive — guide uses naturally)
- Parentheses reminder: "(4 × 3) + (5 × 2). They show each rectangle's area before
  we add."
- Bridge to M12: "Today you had grids to help you see every square. What if the grid
  disappeared and you only had the side lengths?" — brief display of ungridded composite
  figure with dimension labels. Don't solve. Leave as teaser.

TRANSITION IN (from M10):
What M10 establishes: The full multiplication-area connection — every product is an
area, every cell is a rectangle.
What M11 builds: Composite figures — shapes made of MULTIPLE rectangles. Area is
additive. Full grids return.
Bridge: "You've been finding the area of SINGLE rectangles. What if a shape is made
of TWO rectangles stuck together? How would you find ITS area?"
⚠️ Engineering alert — grids come back in M11. Pedagogically intentional CRA reset.

TRANSITION OUT (to M12):
What M11 establishes: The decompose-calculate-add workflow; area is additive; multiple
valid decompositions; parenthesized expressions; comfort with L/T/U-shapes.
What M12 builds: Same decomposition strategy, but grids fade. Partial grid → dimensions
only. Real-world contexts (patio paving).
Bridge: "Today you had grids to help you see every square. What if the grid disappeared
and you only had the side lengths?"
Engineering note: M12 uses Composite Figures with partial grid → tick marks → labels only.
```

**Scaffolding Progression:**
Grid is constant (full grid throughout). What changes is WHO places the decomposition line (system → student) and the VARIETY of figure types (L-shape only → multiple configurations).

**Tool Requirements:**
1. Critical — Continuous grid across entire figure (NOT separate grids per rectangle)
2. Critical — Decomposition line validation (straight, edge-to-edge, horizontal/vertical)
3. Critical — Color-coding per rectangle (max 3 colors for M11)
4. Critical — Multiple decomposition display (2 valid decompositions side by side or overlaid)
5. Equation Builder integration — parenthesized expression with color-coded terms matching rectangle colors

**Data Constraints (from TVP):**
- Figure dimensions: All side lengths 1–10
- Component rectangle areas ≤ 50
- Total area ≤ 40 for Early/Mid; ≤ 50 for Late
- Early: 2-component L-shapes, clean dimensions, component areas should be different
- Mid: 2–3 component L-shapes + simple rectilinear, at least 2 valid decomposition paths; avoid decompositions creating 1×n strips
- Late: L + T + U shapes, 2–3 components, 3-component limited to 1–2 problems; component areas require genuine multiplication (not 1×n)
- Equation Builder: Products ≤ 81; sums ≤ 100
- Avoid: missing dimensions (?), subtraction decomposition, ungridded figures, >3 components, real-world contexts
- EC misconception check: bounding box producing memorable wrong answer (e.g., 6×8=48 vs correct 38)

**Vocabulary (from TVP):**
- New (active): composite figure, decompose
- New (receptive only): rectilinear
- Reinforced: area, square units, rectangle, multiply, add, dimensions, rows, columns, expression
- Language patterns provided (5 patterns for decompose-calculate-add workflow)
- Parentheses language: "The parentheses show each rectangle's area" — do NOT introduce "order of operations"

**SME Review Questions (all RESOLVED):**
- Parentheses depth: Descriptive approach confirmed. Students do NOT write own parentheses; Equation Builder handles notation automatically.
- Engineering: Equation Builder must dynamically generate expression based on number of rectangles from student's decomposition (2 or 3 terms).
- Figure type progression: L-shapes through Mid, T/U in Late. CONFIRMED.
- Completing the rectangle: Proactive for v1. CONFIRMED.
- Multiple decompositions: 1 solve-both + 1 mention-only. CONFIRMED.
- Grid verification: Do not require counting verification. CONFIRMED.
- 3-component figures: Keep in Late, limit 1–2. CONFIRMED.

---

## Design Constraints Extraction — Important Decisions

```
DESIGN CONSTRAINTS (from Important Decisions)
=============================================

Decision 1: Unified Path with Adaptive Pacing
  Rule: Use a single instructional path following CRA progression. Differentiate
  through pacing and representation duration, not different approaches.
  Applies to M11? YES
  What it constrains: M11 follows CRA (Concrete/Representational with full grids).
  Pacing adapts — students who need more time stay with system-placed decomposition
  longer before drawing their own.

Decision 2: Explicit Spatial Structuring as Central Focus
  Rule: Make row-by-column "seeing" an explicit instructional target with dedicated
  activities, not an assumed skill.
  Applies to M11? PARTIAL
  What applies: Row-by-column structuring is prerequisite (taught M3-M4). M11 assumes
  this skill is established. The new spatial skill is decomposition-line identification
  (finding inside corners). This gets its own dedicated activities (Early: corner
  identification step).
  What doesn't: The specific "How many rows? How many in each row?" activities are
  M3-M4 territory, not M11.

Decision 3: Progressive Grid Removal (Concreteness Fading)
  Rule: Follow research-backed fading sequence. M11 specific: "Full grids return for
  composite figures (CRA reset — decomposition is new concept)"
  Applies to M11? YES — HARD CONSTRAINT
  What it constrains: ALL M11 figures must have full grids. No partial grids, no tick
  marks, no dimensions-only. The grid is constant throughout the module. M12 begins
  fading for composites.

Decision 4: Array Knowledge is Helpful but Not Required
  Rule: Design Unit 2 to be self-contained. Leverage array/multiplication knowledge
  IF students have it, but do not assume Unit 1 completion.
  Applies to M11? PARTIAL
  What applies: M11 warmup includes 2 rapid forward multiplication checks as safety
  net. By M11, students have been through M1–M10 within this unit, so multiplication
  fluency within the unit IS established. The decision's spirit (don't assume external
  prerequisites) is honored — M11 only assumes skills taught within Unit 2.

Decision 5: Perimeter Kept Separate — Do NOT Introduce
  Rule: Do NOT introduce perimeter in this unit.
  Applies to M11? YES
  What it constrains: No mention of perimeter, even for contrast. The "completing the
  rectangle" misconception check should NOT reference perimeter. It references "bounding
  rectangle" and "missing corner" language instead.

Decision 6: Dragging Over Tapping for Manipulatives
  Rule: Prioritize drag-to-place for virtual manipulatives over tap-to-place.
  Exception: Simple selection tasks (MC, identifying) can use tap.
  Applies to M11? YES
  What it constrains: Decomposition line drawing should use drag or constrained-drag
  interaction (not single tap). MC selections use tap per the exception. The TVP notes
  this is a UX decision pending usability testing — options include two-tap, snap-to-cut,
  or constrained drag.

Decision 7: Standard Units Get Full Scaffolding
  Rule: Keep sq inches/cm and sq feet/meters as separate modules.
  Applies to M11? NO
  M11 uses generic "square units" — no specific unit types.

Decision 8: Include Multiplication Table Connection (L11) as Module
  Rule: Include L11 (Area & Multiplication Table) as a synthesis/connection module.
  Applies to M11? NO (applies to M10)
  Relevant context: M10 is no longer optional (per SME resolution). M11 can assume M10
  completion — students arrive with full multiplication-table-as-area understanding.

Decision 9: Keep Application Module (L15) Standalone
  Rule: Include L15 (New Room application) as standalone module.
  Applies to M11? NO (applies to M14/M15)

Unnumbered Decision: Ruler Dropped from M8
  Rule: Dropped ruler measurement; replaced with extended dimensions-only practice +
  reverse problems.
  Applies to M11? NO (applies to M8)
```

---

## Cross-Reference Table C — Conflict Log

```
CONFLICT LOG
============

#1
Field: Vocabulary to Teach — "rectilinear" classification
Module Mapping says: "rectilinear" listed as Vocabulary to Teach (active)
TVP says: "rectilinear" is receptive only — guide uses it, students hear it, not assessed
Resolution: TVP wins (downstream, reflects SME decision). Rectilinear is receptive only.
Active vocabulary limited to "composite figure" and "decompose." This reduces cognitive
load to two new active terms. Document in §1.3 with clear receptive-only designation.
Status: Resolved — follow TVP

#2
Field: Warmup structure — Grid Rectangles usage
Module Mapping says: [No warmup detail]
TVP says: Warmup starts with Grid Rectangles (outline + dimensions, no grid) for 2
rapid forward area problems, THEN switches to Composite Figures for the L-shape.
TVP also says: "Grid Rectangles are NOT used in M11" (general statement)
Resolution: The "Grid Rectangles are NOT used" statement refers to the Lesson/EC/Practice
phases — the warmup uses Grid Rectangles briefly for activation (2 quick forward problems)
before transitioning to Composite Figures. This is consistent: Grid Rectangles serve as
a prior-knowledge check, Composite Figures is the primary tool. Document in §1.5.
Status: Resolved — warmup activation uses Grid Rectangles; all other phases use Composite Figures only

#3
Field: Misconception IDs
Module Mapping says: "M6 (overlapping decomposition); M11 (completing the rectangle)"
Misconceptions Sheet says: ID 6.0 (Overlapping Decomposition, surface M12-M14, HIGH);
ID 11.0 (Completing the Rectangle, surface M12-M14, HIGH)
TVP says: #11 PRIMARY, #6 SECONDARY — with detailed prevention strategies
Resolution: Global IDs are 6.0 and 11.0. Module Mapping uses "M6/M11" shorthand but
these map to database IDs 6/11. Note: Misconceptions sheet says both surface in M12-M14,
but TVP explicitly targets them in M11 with proactive prevention. This is correct —
M11 introduces composite figures where these misconceptions first become relevant,
even though the sheet says M12-M14 (likely because M12-M14 is where they're most
problematic with ungridded figures).
Status: Resolved — use global IDs 6 and 11; note the surface-range discrepancy as
intentional early prevention

#4
Field: Scaffolding of Visuals
Module Mapping says: "Gridded L-shapes and rectilinear figures; Multiple decomposition
options shown; Color-coding for different rectangles"
TVP says: L-shapes in Early/Mid, T-shapes and U-shapes added in Late. Color-coding
max 3 colors. Multiple decompositions in Mid (1 full solve + 1 mention).
Resolution: Consistent. Module Mapping's "rectilinear figures" encompasses T/U-shapes.
TVP adds the specific progression (L only → L+T+U). No conflict.
Status: Resolved — no conflict

#5
Field: "Notes" Critical flags
Module Mapping says: "Parentheses introduced for grouping expressions"
TVP says: Parentheses are descriptive notation, not prescriptive. "Do NOT introduce
'order of operations' language." Equation Builder handles notation automatically;
students do not write their own parentheses.
Resolution: Consistent but TVP adds important constraint. Module Mapping flags
parentheses as a teaching point; TVP clarifies the scope: students SEE and INTERPRET
parenthesized expressions but don't produce them. Document this constraint clearly.
Status: Resolved — follow TVP's scoping of parentheses instruction

#6
Field: Question/Test Language stem #2
Module Mapping says: "Show how you broke it into rectangles"
TVP says: Students draw decomposition lines (a spatial action) — they don't "show"
or "explain" in written form. The closest TVP equivalent is the student-drawn
decomposition line itself.
Resolution: The "show" in the test stem maps to the decomposition line drawing
interaction, not a verbal/written explanation. In EC, this manifests as EC problem 2
(student decomposition → calculate). Document the mapping in §1.1.
Status: Resolved — test language maps to interaction design, not verbal production

#7
Field: Standards Building Towards — 3.MD.C.7.d (ungridded figures)
Module Mapping says: M11 is "building towards" 3.MD.C.7.d for ungridded figures
Module Mapping also says: M11 is "addressing" 3.MD.C.7.d
Resolution: M11 addresses 3.MD.C.7.d for GRIDDED composite figures. It builds toward
the same standard applied to UNGRIDDED figures (M12-M14). Both are correct — the
standard covers the full range; M11 covers the gridded subset.
Status: Resolved — no conflict, document dual use of standard

#8
Field: Warmup TVP duplicate text
TVP contains two versions of the warmup description (paras 39-60):
  Version 1 (paras 39-49): "You got it — 22 square units. You counted every square.
  But that took a while. What if there were a LOT more squares?"
  Version 2 (paras 51-61): "You got it — 22 square units! People approach this kind
  of problem differently. Here's one way that always works..."
Resolution: Version 2 is the refined text (appears later, slightly different framing).
Version 2 avoids the "But that took a while" framing which could feel dismissive of
counting. "People approach this kind of problem differently" is more respectful.
Using Version 2.
Status: Resolved — use Version 2 (refined)
```

---

## Edit Reconciliation Pass

The TVP for M11 does not reference numbered edits (Edit 83, 84, 88, 91, etc.) that were present in earlier modules' TVP sections (those edits applied to M8-M10 content). The M11 TVP section was written after those edits were already incorporated into the overall design.

However, there are several SME Review resolutions that function as edit-like refinements:

```
EDIT RECONCILIATION
===================

SME Resolution 1: Parentheses — students do NOT write own
  What it changes: Scopes parentheses instruction to interpretive only
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.5 Toy Specs (Equation Builder handles notation automatically),
  §1.7 Lesson (guide dialogue must be flexible for 2 or 3 terms)

SME Resolution 2: Figure type progression confirmed (L through Mid, T/U in Late)
  What it changes: Confirms figure variety constraints
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.5 Data Constraints, §1.7 Lesson sections

SME Resolution 3: Completing the rectangle — proactive for v1
  What it changes: All students get the bounding-rectangle demonstration in Early
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.7 Early section interaction design

SME Resolution 4: Grid verification — do NOT require counting verification
  What it changes: No prompted counting after warmup
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.7 Early/Mid interactions (no "count to check" steps)

SME Resolution 5: 3-component figures — keep in Late, limit 1–2
  What it changes: Confirms 3-component scope
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.5 Data Constraints, §1.7 Late section

SME Resolution 6: Module 10 no longer optional
  What it changes: M11 can assume M10 completion
  Reflected in Table B? YES — transition section notes this
  Downstream impact: §1.1 Module Bridges (can reference M10's table insight confidently)

SME Resolution 7: Equation Builder must dynamically generate expressions
  What it changes: Engineering requirement — EB generates (a×b)+(c×d) or (a×b)+(c×d)+(e×f)
  based on student's decomposition, not pre-set template
  Reflected in Table B? YES — fully captured
  Downstream impact: §1.5 Toy Specs (engineering flag)
```

No numbered TVP edits (Edit XX) found for M11. All SME resolutions are fully reflected in the extraction. Edit Reconciliation Pass: CLEAN.

---

## Data-Level Constraint Audit

Auditing all concrete examples in the TVP extraction against applicable design constraints:

```
DATA CONSTRAINT AUDIT
=====================

Example Set 1: Warmup forward problems
  Values: "5 by 4" and "7 by 3"
  Constraint: Side lengths 1–10 ✓; Products ≤ 50 ✓ (20 and 21)
  Constraint: Grid Rectangles used (outline + dimensions, no grid) — this is the
  warmup activation, not Composite Figures
  Violations found: None

Example Set 2: Warmup L-shape counting
  Values: Total area = 22 square units
  Constraint: Total area ≤ 40 for Early/Mid ✓ (warmup counts as Early-level)
  Constraint: Full grid ✓
  Violations found: None

Example Set 3: Early Equation Builder examples
  Values: (4 × 3) + (5 × 2) = 12 + 10 = 22
  Constraint: Side lengths 1–10 ✓; Component areas ≤ 50 ✓ (12, 10)
  Constraint: Total area ≤ 40 ✓ (22)
  Constraint: Products ≤ 81 ✓; Sums ≤ 100 ✓
  Constraint: Component areas should be different ✓ (12 ≠ 10)
  Violations found: None

Example Set 4: Early — another example
  Values: 3×6 + 2×4 = 18 + 8 = 26
  Constraint: All checks pass ✓
  Violations found: None

Example Set 5: Mid — multiple decompositions beat
  Values: Total area = 26 square units (first example); expressions shown as
  Method 1: (4 × 3) + (5 × 2) = 12 + 10 = 22
  Method 2: (4 × 5) + (2 × 2) = 20 + 2 = 22
  Constraint: Side lengths 1–10 ✓; Component areas ≤ 50 ✓
  Constraint: "Avoid decompositions creating 1×n" — Method 2 creates 2×2 (not 1×n) ✓
  ⚠️ NOTE: The TVP uses 22 for the multi-decomposition example but says "26 square
  units" in the preceding guide line ("Great! You found the total area is 26 square
  units"). This is likely a values mismatch in the TVP text — the 26 from the
  guide dialogue doesn't match the 22 from the expression examples. The expression
  examples (22) are internally consistent. The guide dialogue value (26) appears to
  be from a different figure.
  Action: Flag as minor TVP inconsistency. Use internally consistent values when
  drafting. This doesn't affect the SP — we'll design our own specific values.

Example Set 6: Late — 3-component example
  Values: (2 × 7) + (3 × 4) + (2 × 3) = 14 + 12 + 6 = 32
  Constraint: Side lengths 1–10 ✓; Component areas ≤ 50 ✓
  Constraint: Total area ≤ 50 (Late) ✓ (32)
  Constraint: "Component areas require genuine multiplication (not 1×n)" ✓ (2×7, 3×4, 2×3)
  Constraint: Products ≤ 81 ✓; Sums ≤ 100 ✓
  Violations found: None

Example Set 7: EC misconception check
  Values: Bounding box 6 × 8 = 48; correct area = 38
  MC options: 48 (bounding error), 38 (correct), 28 (partial), 34 (addition error)
  Constraint: Side lengths 1–10 ✓; Total area ≤ 50 ✓
  ⚠️ CHECK: Is 38 achievable from an L-shape with bounding box 6×8?
    Bounding box = 48. If "missing corner" = 10 (e.g., 2×5), then area = 38. ✓
    One valid decomposition: (6×3) + (4×5) = 18 + 20 = 38. Bounding = 6×8 = 48. ✓
    Distractor 28: could be one rectangle's area (e.g., student only calculates the
    larger piece). ✓ plausible
    Distractor 34: 18 + 20 = 38, not 34. 34 would be an addition error on some
    decomposition — e.g., (6×3)+(4×4) = 18+16 = 34 (wrong dimension for second rect).
    ✓ plausible
  Constraint: "Bounding box producing memorable wrong answer" ✓ (48 is salient)
  Violations found: None — values are internally consistent

Example Set 8: Equation Builder example (Data Constraints section)
  Values: (4 × 5) + (3 × 6) = 20 + 18 = 38
  Constraint: All checks pass ✓
  Violations found: None
```

**Data Constraint Audit Summary:** All TVP example values pass constraint checks. One minor inconsistency flagged (Example Set 5: guide dialogue says "26" but expression examples total "22" — different figures conflated in TVP text). No violations requiring correction before drafting.

---

## Author Flags

No Author Flags identified at Task 1. All SME Review Questions in the TVP are marked RESOLVED. No source document conflicts requiring author decision. The TVP duplicate text (warmup versions) was resolved using the refined version.

---

## Dimension Tracking

Updated through Task 3 (v3.1). All values final.

| Phase | Interaction | Dimensions | Area/Total | Notes |
|-------|------------|------------|------------|-------|
| Warmup | W.1 — Forward check 1 | 5 × 4 | 20 | Grid Rectangles (activation) |
| Warmup | W.2 — Forward check 2 | 7 × 3 | 21 | Grid Rectangles; distractors 8×3, 6×4, 5×4 |
| Warmup | W.3 — L-shape counting | (no dimensions shown) | 22 | Composite Figures, counting only |
| Warmup | W.4 — Decomposition demo | 4×3 + 5×2 | 12+10=22 | System demonstration; same figure reused in 1.1 |
| Early | 1.1 — Worked example | 4×3 + 5×2 | 12+10=22 | Same figure from W.4 (KDD-3); 3-step MC |
| Early | 1.2 — Faded example | 3×6 + 2×4 | 18+8=26 | Single MC for total (KDD-4); distractors 24,28,30 |
| Early | 1.3 — Additive property | (no new values) | — | Teaching only; names additive property |
| Early | 1.4 — 3rd system problem | 6×4 + 3×3 | 24+9=33 | KDD-5; distractors 30,36,42 |
| Early | 1.5 — Bounding rectangle | Bounding 6×5 | 30 (wrong) | Misconception prevention; actual area ≠ 30 |
| Early | 1.6 — Corner ID | (3 figures) | — | Recognition beat; no area calculation |
| Mid | 2.1 — Student decomposition | [a]×[b] + [c]×[d] | pipeline | Student draws line; values from pipeline |
| Mid | 2.2 — Multiple decompositions | 4×3+5×2 vs 4×5+2×2 | both=22 | Same total, different rectangles |
| Mid | 2.3 — Independent practice | pipeline | pipeline | Student draws + calculates |
| Mid | 2.4 — Two-way decomposition | pipeline | pipeline | Student finds two valid decompositions |
| Late | 3.1 — L-shape anchor | pipeline | pipeline | Familiar shape, full independence |
| Late | 3.2 — T-shape + rectilinear | pipeline | pipeline | New figure type + vocabulary |
| Late | 3.3 — U-shape (3 components) | pipeline | pipeline | 3-rectangle decomposition |
| EC | EC.1 — Guided decomposition | 5×3 + 4×2 | 15+8=23 | APPLY; distractors 21,25,30 |
| EC | EC.2 — Student decomposition | pipeline | pipeline | CREATE; student draws + calculates |
| EC | EC.3 — Misconception check | Bounding 6×8 | 38 (correct) | IDENTIFY; distractor 48 (6×8); TVP values |
| Synthesis | SY.1 — Pattern discovery | 4×3 + 5×2 (Panel 1) | 22 | Reference panels from Lesson; Panel 3 is novel |
| Synthesis | SY.2 — Vocabulary MC | (no new values) | — | 3-step vocab consolidation |
| Synthesis | SY.3 — Key takeaway | (no values) | — | Metacognitive reflection |

---

## Section Plan

**Warmup (3–5 min):** Activation type. Prior knowledge activated: single-rectangle area via multiplication (2 rapid forward problems using Grid Rectangles). Anticipated warmup type: Activation + Discovery — students count an L-shape's squares (slow method), then system demonstrates decomposition (fast method). Bridge target: "People approach this kind of problem differently. Here's one way that always works..." → Early activities formalize the workflow.

**Lesson Section 1 — Early (~5 min):** System decomposes, student calculates. CRA: Concrete/Representational. System-placed decomposition lines on 2-component L-shapes. Student reads dimensions, multiplies for each rectangle area, adds. Parentheses introduced as notation. Additive property statement. Completing-the-rectangle misconception check (proactive). Inside-corner identification (recognition step before production). Major pedagogical moves: parentheses introduction, M11 misconception prevention, cut-point heuristic.

**Lesson Section 2 — Mid (~5 min):** Student draws decomposition lines. CRA still Concrete/Representational. Key shift: student now places the line (production, not just recognition). Multiple valid decompositions beat — same figure, two ways, same total. 2–3 component figures (still mostly L-shapes).

**Lesson Section 3 — Late (~5 min):** Independent decompose-calculate-add. Full independence. Figure variety expands to T-shapes and U-shapes. 3-component figures introduced (1–2 only). Light-touch efficiency observation (1 problem). Vocabulary staging: "composite figure" and "decompose" used actively; "rectilinear" introduced receptively.

**Exit Check (3–5 min):** 3 problems testing: (1) calculate given decomposition, (2) decompose and calculate independently, (3) avoid completing-the-rectangle error. Same toy (Composite Figures), same modes, same interaction types as Lesson. Cognitive types: APPLY (EC.1), CREATE+APPLY (EC.2), IDENTIFY (EC.3).

**Synthesis (~6–8 min):** Decompose-calculate-add strategy summary. Vocabulary consolidation (composite figure, decompose, rectilinear). Anticipated task types: at least 2 from Synthesis Playbook. Metacognitive reflection. Identity-building closure. Bridge to M12: ungridded composite figure teaser.
