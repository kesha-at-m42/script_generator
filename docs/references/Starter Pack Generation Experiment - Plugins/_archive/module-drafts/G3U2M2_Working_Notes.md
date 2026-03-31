# G3U2 M2 WORKING NOTES

**Module:** M2
**Title:** Tiling Rectangles — No Gaps, No Overlaps
**Unit:** 2
**Domain:** measurement_area
**Grade:** 3
**Prior module:** M1 (What is Area? Measuring with Unit Squares)
**Next module:** M3 (Structured Counting — Rows and Columns)

---

## SESSION LOG

**Session 1 (2026-03-12):** New module setup. Read all source documents. Built Cross-Reference Tables, Design Constraints, Conflict Log, Section Plan, Backbone draft (§1.0–§1.5). Completed Backbone Self-Check. Ran Gate 1 (18 PASS, 1 FLAG, 0 FAIL). Author reviewed 3 Author Flags — all resolved. Updated Backbone with spec-verified Grid Rectangles info, MC error identification in Lesson. Drafted full Warmup (§1.6) + Lesson (§1.7) — Task 2 complete.

**Session 2 (2026-03-12, continued):** Populated Dimension Tracking table. Completed Task 2 Self-Check. Ran Gate 2 (15 PASS, 3 FLAG, 0 FAIL) + Voice Agent (5 MAJOR, rest MINOR). Author approved revisions. Applied voice tightening, added exclamation points, resolved AF#4.

**Session 3 (2026-03-13):** Drafted Task 3: EC (§1.8, 3 problems), Practice Inputs (§1.8.5), Synthesis (§1.9, 3 tasks + closure), KDD (§1.10, 15 decisions). Completed Task 3 Self-Check. Ran Gate 3 (11 PASS, 2 FLAG, 0 FAIL).

**Session 4 (2026-03-13, continued):** Author review of Gate 3 + comprehensive Lesson/EC/Synthesis feedback. Applied structural changes:
- **Tier 1 (Script-breaking):** Split 1.3 into observe-only (new 1.3) + student-action (new 1.4) for gap/overlap symmetry. Added 1.8 (correct tiling identification) for ternary classification. Changed 1.7 from binary to ternary options. Everything renumbered.
- **Tier 2 (Clarity):** Fixed 1.2 Guide/Prompt alignment ("gaps" in both). Clarified overlap visual descriptions as authored pre-tiled state (not runtime detection).
- **Tier 3 (Quality):** Removed 5×5=25 from Section 3 (moved to Practice). Added script writer note to W.1. Renumbered Section 3.
- **EC fix:** EC.2 upgraded from binary to ternary options (Gap/Overlap/Correct).
- **Synthesis fix:** S.2 redesigned to use Grid Rectangles (not custom illustrations). Real-world bridge via language framing.
- **Gate 3 flags:** H3 resolved (S4 not independently assessed). E6 resolved (KDD #16-17 added, flagged not SME reviewed).
- Updated KDDs: #1 (symmetrical scaffolding), #5 (ternary classification), #7 (5×5 to Practice), #12 (v2 revisions), added #16, #17, #18. Total: 18 KDDs.
- Dimension Tracking fully updated with new interactions.

---

## CROSS-REFERENCE TABLE A — MODULE MAPPING EXTRACTION

```
MODULE MAPPING: M2
====================
Module: M2
OUR Lessons: L3
Core Concept: Tiling Rectangles - No Gaps No Overlaps
The One Thing / OUR Learning Goals (Verbatim): Explain that rectangles that can be covered by the same number of unit squares without gaps or overlaps have the same area. Find the area of rectangles (within 24 square units) by counting unit squares.
Standards - Building On: 3.MD.C.5.a (unit squares - from M1)
Standards - Addressing: 3.MD.C.5.b (no gaps/overlaps rule); 3.MD.C.6 (counting unit squares - intro)
Standards - Building Towards: 3.MD.C.6 (systematic counting)
Notes: Critical rule establishment. Students see WHY gaps and overlaps give wrong answers. Same area = same number of squares. Rectangles focus begins here.
Vocabulary to Teach: gap, overlap, tiling, rectangle
Question/Test Language: Is this tiled correctly? Why or why not? These rectangles have the same area - how do you know?
Vocabulary Teaching Notes: 'Gap' = space left uncovered. 'Overlap' = squares on top of each other. Both cause wrong counts.
Scaffolding of Visuals: Examples of correct vs incorrect tiling; Drag tiles to complete partial tilings; Visual feedback highlighting gaps/overlaps
Key Misconceptions: M1 (gaps/overlaps acceptable); M9 (array structure not seen)
```

**Flags on Table A:**
- No "Vocabulary to Avoid" column in Module Mapping — must derive from M1's Terms to Avoid list + scope constraints
- "Key Misconceptions" uses module shorthand (M1, M9) — global IDs are #1.0 and #9.0
- Notes field has no "Critical:" flag — just a general note about rule establishment
- "within 24 square units" in Learning Goals — TVP says "6-25 square units" (see Conflict Log #1)

---

## CROSS-REFERENCE TABLE B — TVP EXTRACTION

```
TVP: MODULE 2
===============
Title: Tiling Rectangles — No Gaps, No Overlaps
OUR Lessons: L3 | Standard: 3.MD.C.6

Learning Goal: Tile rectangles to find the area; recognize that unit squares must have no gaps or overlaps to accurately measure area.

Key Teaching Points:
1. Area measurement requires COMPLETE coverage
2. Gaps = missing space = wrong count (too few)
3. Overlaps = counting space twice = wrong count (too many)
4. Proper tiling: edge-to-edge, no gaps, no overlaps
5. Rectangle focus (4 right angles, opposite sides equal)
6. This establishes the RULES for accurate measurement
7. CRA Stage: Still CONCRETE — manipulation with explicit rule-building

Cognitive Focus:
- IDENTIFY (Conceptual) — recognizing gaps/overlaps as errors
- COMPARE (Conceptual) — distinguishing correct from incorrect tilings
- CREATE (Procedural) — tiling shapes correctly
- CONNECT (Transfer) — understanding WHY rules matter for measurement

Misconceptions Targeted:
- Gaps/overlaps acceptable (PRIMARY) — Students must understand these produce wrong counts
- Rectangle properties unclear (MODERATE) — Formalize rectangle definition

What Students DO:

WARM-UP:
- Grid Rectangles (display) → Show rectangle with perfect tiling (edge-to-edge, complete)
- Students observe and describe what they notice about how tiles fit
- Purpose: activate "good tiling" mental model before naming the rules

LESSON:

Early activities (Understanding the problem — sequential error presentation):
- Grid Rectangles (display) → Show rectangle tiled WITH GAPS (some squares missing)
  - Students identify the problem, count tiles, then count empty spaces
  - Key beat: "The REAL area is 12, but we only counted 10. Gaps give us the WRONG answer — too few."
- Grid Rectangles (display) → Show rectangle tiled WITH OVERLAPS (stacked tiles)
  - Students identify the problem, count tiles including doubles
  - Key beat: "The REAL area is 12, but we counted 14. Overlaps give us the WRONG answer — too many."
- Grid Rectangles (display) → Show CORRECT tiling → students confirm: no gaps, no overlaps, correct count
- Vocabulary formalized: gaps, overlaps, proper tiling

Mid activities (Practicing the rules):
- Unit Square Tiles (draggable, snap-to-grid) + Grid Rectangles (target area)
  - Students tile rectangles with explicit rule reminders
  - Snap-to-grid feature prevents accidental gaps; overlap detection highlights stacking
  - Scaffolded feedback: immediate feedback on gaps/overlaps → feedback on submit only → self-check before submit
  - Quarter-tile snap allows semi-freeform placement — students must apply gap/overlap rules with genuine precision, but motor demands stay age-appropriate
  - Overlap detection: immediate visual feedback (tile color change) + audio cue on overlap, with opportunity to correct before continuing. Always active during tiling.
  - Scaffolded feedback on COMPLETION (area count accuracy): immediate → submit-only → self-check before submit
  - Guide models self-check routine first, then prompts students to self-check
  - Rectangles: 3×4, 2×5, 4×4 (simple dimensions)

Late activities (Independence with validation):
- Unit Square Tiles + Grid Rectangles
  - Student tiles 4-5 rectangles with decreasing support
  - Self-check prompt: "Before you submit, check: Any gaps? Any overlaps?"
  - Scaffolding fades: immediate feedback → submit-only feedback → no feedback until exit check
  - Varied rectangle orientations (horizontal and vertical)

EXIT CHECK:
- Unit Square Tiles + Grid Rectangles
- 3 problems:
  1. Tile a rectangle, state area
  2. Identify error type in pre-made tiling (gap or overlap?)
  3. Tile a rectangle, state area
- Assessing: gap-free/overlap-free tiling + error identification in others' work

PRACTICE:
- Multiple rectangles to tile (within 25 square units)
- Mix: some tile-from-scratch, some identify/fix errors in pre-made tilings

SYNTHESIS:
- Rule consolidation: "No gaps and no overlaps" — WHY these rules matter (wrong counts)
- Rectangle vocabulary reinforced (prior knowledge from Grade 2): 4 sides, 4 right angles, opposite sides equal and parallel. Not new teaching — activation of existing knowledge.
- Bridge to M3: display a correctly tiled 3×4 rectangle. "You can tile perfectly now! But counting every square takes time. Is there a FASTER way?" Briefly highlight one row as a teaser.

TRANSITION IN (from M1):
- M1 Synthesis closure previews "bad" tiling with gaps/overlaps: "But look at this one. Something's off. See those gaps? And that overlap? Next time, we'll figure out why that matters."
- Students arrive knowing: area = space covered, measured by counting tiles. They've tiled but haven't learned the rules for accurate tiling.

TRANSITION OUT (to M3):
- M2 Synthesis bridge: display correctly tiled 3×4 rectangle, highlight one row: "Is there a FASTER way to count?"
- Students leave M2 with: accurate tiling skills, gap/overlap rules internalized, rectangle focus established. M3 teaches structured counting (rows × skip-count).

Scaffolding Progression:
[Header present but no content beneath it in TVP]

Tool Requirements:
[Header present but no content beneath it in TVP]

Data Constraints:
- Rectangles: dimensions 2–6 on each side
- Areas: 6–25 square units
- Both horizontal and vertical orientations

SME Review Questions (All RESOLVED):
1. Snap-to-grid precision? RESOLVED: Quarter-tile snap (half linear measure). Semi-freeform — students must place precisely but motor demands stay age-appropriate. Full snap removed because it prevented genuine learning about gap/overlap awareness.
2. Overlap detection automatic vs. self-identify? RESOLVED: Automatic, always-on. Immediate visual (color change) + audio cue with opportunity to correct. No fade — overlap feedback stays active during all tiling modules.
3. Sequential vs. simultaneous error presentation? RESOLVED: Keep sequential (Gaps → Overlaps → Correct). Gaps and overlaps are different errors with opposite numerical effects (too few vs. too many). Sequential presentation helps students build distinct mental models.
4. Rectangle definition? RESOLVED: Students define rectangles as "polygon with 4 sides and 4 right angles" from Grade 2. They also know attributes: opposite sides are equal and parallel.
```

---

## DESIGN CONSTRAINTS (from Important Decisions)

### Decision 1: Unified Path with Adaptive Pacing
**Rule:** Use a single instructional path following CRA progression. Differentiate through pacing and representation duration, not different approaches.
**Applies to M2?** YES
**What it constrains:** M2 follows a single CRA path (still Concrete per TVP). No alternative instructional sequences.

### Decision 2: Explicit Spatial Structuring as Central Focus
**Rule:** Make row-by-column "seeing" an explicit instructional target with dedicated activities.
**Applies to M2?** NO — Spatial structuring is M3-M4's focus. M2 is pre-structuring (tiling rules only).
**Note:** M2 should NOT introduce row/column language or activities. M2 establishes accurate tiling; M3 builds structure on top of that.

### Decision 3: Progressive Grid Removal (Concreteness Fading)
**Rule:** M1-M4: Full grids.
**Applies to M2?** YES
**What it constrains:** All M2 target rectangles must display full grids. This is a CHANGE from M1, where target shapes had NO visible grid (students created coverage). M2 uses "Grid Rectangles" — rectangles displayed on/with a full grid.
**Important nuance:** M1 explicitly had NO grid on target shapes because the learning was about the process of covering. M2 shifts to Grid Rectangles because the learning is about gap/overlap RULES — the grid makes gaps/overlaps visible. Decision #3 confirms M2 should have full grids.

### Decision 4: Array Knowledge is Helpful but Not Required
**Rule:** Design Unit 2 to be self-contained. Don't assume Unit 1 completion.
**Applies to M2?** YES
**What it constrains:** M2 cannot reference arrays, multiplication from Unit 1, or assume array vocabulary. This is natural for M2 since it's still focused on tiling rules, not structure.

### Decision 5: Perimeter Kept Separate — Do Not Introduce
**Rule:** Do NOT introduce perimeter in this unit.
**Applies to M2?** YES
**What it constrains:** No perimeter language, no "distance around" framing, no area-perimeter comparison. Perimeter stays in Terms to Avoid.

### Decision 6: Dragging Over Tapping for Manipulatives
**Rule:** Prioritize drag-to-place for virtual manipulatives. Exception: simple selection (MC, identifying) can use tap.
**Applies to M2?** YES
**What it constrains:** All tiling interactions use drag-to-place. MC selection for error identification uses tap (per exception). Same as M1.

### Decision 7: Standard Units Get Full Scaffolding
**Rule:** Keep square inches/centimeters and square feet/meters as separate modules.
**Applies to M2?** NO — Standard units are M5-M6. M2 uses generic "square unit."

### Decision 8: Include Multiplication Table Connection
**Rule:** Include L11 as synthesis/connection module.
**Applies to M2?** NO — This applies to M10.

### Decision 9: Keep Application Module Standalone
**Rule:** Include L15 as standalone module.
**Applies to M2?** NO — This applies to M14.

**Summary of applicable constraints for M2:** Decisions 1, 3, 4, 5, 6. Decisions 2, 7, 8, 9 do not apply.

---

## CROSS-REFERENCE TABLE C — CONFLICT LOG

### Conflict #1: Area Range
**Field:** Data Constraints / Learning Goal area limit
**Module Mapping says:** "within 24 square units" (in Learning Goal — OUR verbatim)
**TVP says:** "Areas: 6–25 square units"
**Resolution:** The Module Mapping value is OUR's verbatim text for the learning goal. The TVP's 6-25 range is the operational constraint for interactions. Follow TVP for operational constraints (25 sq units max); preserve OUR verbatim in Learning Goals. The TVP range (6-25) encompasses the OUR goal (within 24). The 1-unit difference is likely TVP expanding slightly to accommodate 5×5=25.
**Status:** Resolved — TVP wins for operational data constraints per hierarchy rule #2. OUR verbatim preserved in §1.1.

### Conflict #2: Standards Listed
**Field:** Standards Addressing
**Module Mapping says:** 3.MD.C.5.b (no gaps/overlaps rule); 3.MD.C.6 (counting unit squares — intro)
**TVP says:** "Standard: 3.MD.C.6" (only one standard listed)
**Resolution:** Module Mapping is authoritative for standards (hierarchy rule #3). TVP likely lists only the primary focus standard. Both 3.MD.C.5.b and 3.MD.C.6 belong in the SP. The Standards Mapping sheet confirms: 3.MD.C.5.b → L2, L3; 3.MD.C.6 → L3, L4, L15.
**Status:** Resolved — Module Mapping wins for standards listing.

### Conflict #3: Misconceptions — Divergent Lists
**Field:** Key Misconceptions
**Module Mapping says:** #1.0 (gaps/overlaps acceptable); #9.0 (array structure not seen)
**TVP says:** Gaps/overlaps acceptable (PRIMARY); Rectangle properties unclear (MODERATE)
**Analysis:**
- #1.0 (Gaps/overlaps acceptable): Both sources agree. PRIMARY priority. ✓
- #9.0 (Array structure not seen): Module Mapping includes; TVP does not mention. Per Misconceptions sheet, #9.0 surfaces M3-M4. Including in M2 as PREVIEW seems Module Mapping's intent — students in M2 are tiling rectangles and may not "see" the row/column structure, but M2 doesn't teach that structure. Including as PREVIEW/SECONDARY is reasonable.
- "Rectangle properties unclear": TVP includes; Module Mapping does not list; NOT in Misconceptions database (no global ID). TVP says MODERATE priority. This appears to be a TVP-specific pedagogical note about ensuring rectangle vocabulary is activated, not a formal misconception requiring a database entry.
**Resolution:** Include #1.0 as PRIMARY. Include #9.0 as PREVIEW (per Module Mapping — it surfaces soon after). Document "Rectangle properties unclear" as a pedagogical note in §1.5 or §1.7 Design Note, not as a formal misconception (no global ID exists). Flag the missing global ID.
**Status:** Resolved with Author Flag #1 (re: rectangle properties — does this need a global misconception ID?)

### Conflict #4: "Rectangle" as Vocabulary to Teach vs. Prior Knowledge
**Field:** Vocabulary status of "rectangle"
**Module Mapping says:** Vocabulary to Teach includes "rectangle"
**TVP says:** "Rectangle vocabulary reinforced (prior knowledge from Grade 2): 4 sides, 4 right angles, opposite sides equal and parallel. Not new teaching — activation of existing knowledge."
**Analysis:** Module Mapping lists "rectangle" as Vocabulary to Teach, implying it's a term students learn in this module. TVP explicitly says it's NOT new teaching — it's activation of Grade 2 knowledge. Module Mapping is authoritative for vocabulary lists (hierarchy rule #3), but the TVP's characterization of HOW the term is used reflects an SME pedagogical decision.
**Resolution:** Include "rectangle" in §1.3 Vocabulary Architecture but mark it as "Activation — prior knowledge from Grade 2" rather than "New introduction." The word appears in Vocabulary to Teach (per Module Mapping) but the teaching approach is activation, not introduction (per TVP).
**Status:** Resolved — hybrid approach respects both sources.

### Conflict #5: Toy Architecture — "Grid Rectangles" vs. M1 Toy List
**Field:** Toy list
**Module Mapping says:** (no specific toy names)
**TVP says:** "Grid Rectangles (display)" and "Unit Square Tiles (draggable, snap-to-grid) + Grid Rectangles (target area)"
**M1 SP says:** "Plane Figures" + "Unit Square Tiles" (no "Grid Rectangles")
**Analysis:** M2 introduces "Grid Rectangles" as a new toy (confirmed: has its own Notion spec at https://www.notion.so/ocpgg/Grid-Rectangles-2fb5917eac528035a19dc2b5b49aeeca). This REPLACES Plane Figures (which was M1's display-only comparison toy). Grid Rectangles serves both as display (showing pre-tiled rectangles in Warmup/Lesson Early) and as target surface (for tiling in Lesson Mid/Late/EC). M1's Unit Square Tiles continues.
**Resolution:** M2 primary toys: Grid Rectangles + Unit Square Tiles. Plane Figures NOT used in M2 (it was M1-specific for shape comparison). Document in §1.5 as "Changes from M1."
**Status:** Resolved — TVP is authoritative for tool decisions.

### Conflict #6: Scaffolding Progression — TVP Empty Headers
**Field:** Scaffolding Progression / Tool Requirements
**TVP says:** Headers present but no content beneath "Scaffolding Progression" and "Tool Requirements"
**Analysis:** The TVP's "What Students DO" section contains detailed scaffolding information inline (feedback fading, snap behavior, overlap detection), making the separate headers redundant. The TVP effectively documents scaffolding within the phase-by-phase flow rather than in a summary table.
**Resolution:** Extract scaffolding progression from TVP inline descriptions (Lesson Mid and Late sections) and document in §1.5. Not a true conflict — just organizational difference.
**Status:** Resolved.

### Conflict #7: TVP Learning Goal vs. Module Mapping Learning Goals
**Field:** Learning Goal phrasing
**Module Mapping says:** "Explain that rectangles that can be covered by the same number of unit squares without gaps or overlaps have the same area. Find the area of rectangles (within 24 square units) by counting unit squares."
**TVP says:** "Tile rectangles to find the area; recognize that unit squares must have no gaps or overlaps to accurately measure area."
**Analysis:** Module Mapping is OUR verbatim (two goals: explain same-area principle + find area by counting). TVP is a synthesized version focusing on the tiling action + gap/overlap recognition. Both are valid; they emphasize different aspects.
**Resolution:** §1.0 (The One Thing) draws from TVP's synthesized goal (per Guidance). §1.1 (Learning Goals) uses Module Mapping's verbatim text. No conflict in practice — different sections, different purposes.
**Status:** Resolved.

### Conflict #8: 3.MD.C.6 Required Vocabulary vs. M2 Scope
**Field:** Standards Mapping required vocabulary
**Standards Mapping says:** 3.MD.C.6 requires vocabulary "rows, columns, square centimeter, square inch, square foot, square meter"
**M2 scope says:** M2 addresses 3.MD.C.6 (intro only). Rows/columns belong to M3. Standard units belong to M5-M6.
**Analysis:** M2 only introduces 3.MD.C.6 — it doesn't fully address it. The required vocabulary for the standard spans across multiple modules. M2 addresses the "counting unit squares" aspect of 3.MD.C.6 without the advanced vocabulary.
**Resolution:** Document in §1.1 that M2 begins 3.MD.C.6 (counting unit squares) but defers rows/columns vocabulary to M3 and standard units to M5-M6. Not a compliance gap — the standard is progressively addressed across modules. Keep "rows," "columns," and all standard unit terms in Terms to Avoid.
**Status:** Resolved.

---

## AUTHOR FLAGS

**⚠️ AUTHOR FLAG #1 (Misconception Database):** RESOLVED — No new global ID needed. "Rectangle properties unclear" remains a pedagogical note addressed through Synthesis vocabulary activation, not a formally tracked misconception.

**⚠️ AUTHOR FLAG #2 (Grid Rectangles Notion Spec):** RESOLVED — Spec read successfully. Key confirmations: Grid Rectangles is a display object (not draggable); supports Full Grid state for M1-M6; generic "square units" for M1-M4; can appear with Unit Square Tiles and Counter; Shade action supports pre-tiled display (shaded = tiled, unshaded = gap). One finding: spec says "Typical M1-M2: Up to 24 square units" which tightens TVP's 6-25 range. Backbone §1.5.1 updated with spec-verified configuration.

**⚠️ AUTHOR FLAG #3 (EC Problem #2 — Error Identification):** RESOLVED — Author confirmed: add MC error identification interaction in Lesson Section 1 so students practice identifying gap/overlap errors as a student-action skill BEFORE EC tests it. Section Plan updated to include 4-5 interactions in Section 1 (display presentations + MC identification). Grid Rectangles spec confirms display capabilities (Shade for pre-tiled states). MC is the correct modality for error identification (Decision #6 exception: simple selection uses tap).

**⚠️ AUTHOR FLAG #4 (Three Simultaneous Grid Rectangles in 1.5):** RESOLVED — Author confirmed feasible. Three small Grid Rectangles displayed simultaneously in the Relational interaction (1.5) is within engineering capabilities. No fallback needed.

---

## SECTION PLAN

### Warmup
- **Prior knowledge activated:** M1's tiling experience — students can tile shapes and count squares. M1 Synthesis showed "good" tiling; M2 Warmup activates "good tiling" mental model.
- **Warmup type:** Notice & Wonder. Students observe a correctly tiled rectangle and describe what they see.
- **Bridge target:** Sets up the Lesson's error presentation — "you just described what GOOD tiling looks like. Now let's see what happens when it goes wrong."

### Lesson Sections
- **Section 1 (Lesson Early — Understanding the Problem):** 8 interactions. Symmetrical observe→act scaffolding: gap observe (1.1) → gap identify (1.2); overlap observe (1.3) → overlap identify (1.4); relational comparison (1.5); vocabulary (1.6); ternary error ID ×2 (1.7 gap, 1.8 correct). CRA: Concrete (1.1-1.4) → Relational (1.5) → Abstract (1.6-1.8).
  - Key vocabulary introduced here: gap (1.2), overlap (1.4), tiling (1.6)

- **Section 2 (Lesson Mid — Practicing the Rules):** 3 guided tiling interactions. Worked example with fading (Full → Partial → Minimal). Self-check routine modeled then prompted.
  - Interaction types: Pattern 1 (drag-to-place tiling + count + state area)

- **Section 3 (Lesson Late — Independence with Validation):** 3 independent tiling interactions + EC bridge. Decreasing support. Self-check expected. Varied orientations. 5×5=25 removed (moved to Practice for pacing).
  - Interaction types: Pattern 1 (drag-to-place, decreasing Guide support)

### Exit Check
- **Skills to assess:** (1) Gap-free/overlap-free tiling + area statement; (2) Ternary error identification (gap/overlap/correct)
- **Cognitive types:** CREATE (tiling) + IDENTIFY (ternary classification)
- **3 problems per TVP**

### Synthesis
- **Connections:** Rule consolidation — WHY "no gaps, no overlaps" matters (wrong counts)
- **Task types:** Pattern Discovery (Grid Rectangles), Real-World Bridge (Grid Rectangles with language framing), Metacognitive reflection
- **Closure/bridge:** Bridge to M3 — "Is there a FASTER way to count?" with highlighted row

---

## DIMENSION TRACKING

| Interaction | Toy | Dimensions | Area | Orientation | Notes |
|-------------|-----|-----------|------|-------------|-------|
| W.1 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Correct tiling — all shaded |
| W.2 (left) | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Correct tiling — same area comparison |
| W.2 (right) | Grid Rectangles (display) | 2×6 | 12 | Vertical | Correct tiling — same area comparison |
| 1.1 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Gap tiling — 10 shaded, 2 gaps |
| 1.2 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Same as 1.1 (gap identification) |
| 1.3 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Overlap tiling — 14 tiles shown. Observe only. |
| 1.4 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Same as 1.3 (overlap identification) |
| 1.5 (×3) | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Three states: gap (10), overlap (14), correct (12) |
| 1.6 | Grid Rectangles (display) | 3×4 | 12 | Horizontal | Correct tiling from 1.5 (vocabulary formalization) |
| 1.7 | Grid Rectangles (display) | 4×3 | 12 | Vertical | Gap tiling — 11 shaded, 1 gap. Ternary ID (Gap/Overlap/Correct) |
| 1.8 | Grid Rectangles (display) | 3×3 | 9 | Square | Correct tiling — 9 shaded. Ternary ID (answer: Correct) |
| 2.1a | Grid Rect (target) + UST | 3×4 | 12 | Horizontal | Worked example #1 (full) — Guide demo |
| 2.1b | Grid Rect (target) + UST | 2×5 | 10 | Horizontal | Student tiles — exact supply (10 tiles) |
| 2.2 | Grid Rect (target) + UST | 4×4 | 16 | Square | Worked example #2 (partial) — exact supply (16) |
| 2.3 | Grid Rect (target) + UST | 3×3 | 9 | Square | Worked example #3 (minimal) — exact supply (9) |
| 3.1 | Grid Rect (target) + UST | 2×6 | 12 | Vertical | Surplus tiles (15). First independent |
| 3.2 | Grid Rect (target) + UST | 5×3 | 15 | Horizontal | Surplus tiles (18) |
| 3.3 | Grid Rect (target) + UST | 2×4 | 8 | Horizontal | Surplus tiles (10). Quick confidence builder |
| EC.1 | Grid Rect (target) + UST | 3×5 | 15 | Horizontal | Surplus tiles (18). CREATE test |
| EC.2 | Grid Rectangles (display) | 5×2 | 10 | Vertical | Overlap error (11 tiles shown). IDENTIFY test — ternary |
| EC.3 | Grid Rect (target) + UST | 4×5 | 20 | Vertical | Surplus tiles (24). CREATE test |
| S.1 (×4) | Grid Rectangles (display) | 2×3, 3×4, 4×3, 2×5 | 6, 12, 12, 10 | Mixed | Pattern Discovery — 3 correct + 1 gap |
| S.2 (×3) | Grid Rectangles (display) | 3×4, 3×4, 3×4 | 12, 12, 12 | Horizontal | Real-World Bridge — correct, gap, overlap |

**Dimension Tracking Analysis:**
- **Dimension range:** 2-6 per side ✓ (min=2, max=6)
- **Area range:** 6-25 sq units ✓ (within TVP constraint; Lesson min=8 in 3.3; Synthesis min=6 in S.1)
- **Orientations:** Horizontal (W.1, 1.1-1.6, 2.1a, 2.1b, 3.2, 3.3), Vertical (W.2 right, 1.7, 3.1), Square (1.8, 2.2, 2.3) ✓
- **TVP-specified dimensions used:** 3×4 ✓ (2.1a), 2×5 ✓ (2.1b), 4×4 ✓ (2.2)
- **Area 12 repetition:** Section 1 holds area constant at 12 to isolate gap/overlap variable. Intentional per KDD #2.
- **Unique areas used (all phases):** 6, 8, 9, 10, 12, 15, 16, 20 (8 distinct values). 5×5=25 moved to Practice.
- **EC values all differ from Lesson:** EC.1 (3×5=15) ✓, EC.2 (5×2=10) ✓, EC.3 (4×5=20) ✓
- **5×5=25:** Removed from Lesson Section 3, moved to Practice per KDD #7.
- **New interactions (v2):** 1.3 (overlap observe), 1.4 (overlap identify), 1.8 (correct tiling ID). S.2 redesigned (3× Grid Rectangles instead of custom illustrations).

---

## BACKBONE SELF-CHECK (Task 1)

- [x] Every term in Table A "Vocabulary to Teach" (gap, overlap, tiling, rectangle) appears in §1.2 or §1.3 — **PASS.** All four terms accounted for. Rectangle noted as activation.
- [x] Every term in Table A "Vocabulary to Avoid" — **N/A.** No "Vocabulary to Avoid" column in Module Mapping. Derived terms from M1 Terms to Avoid + scope constraints. All covered in §1.3.
- [x] Module Mapping "Notes" — every "Critical:" flag addressed — **PASS.** No explicit "Critical:" flag in Notes field. General note about rule establishment is addressed throughout SP.
- [x] Module Mapping "Question/Test Language" stems in §1.1 or flagged for §1.7 — **PASS (after fix).** Added Question/Test Language stems to §1.1 with mapping to EC and Lesson sections.
- [x] Misconception IDs match database, not module number shorthand — **PASS.** §1.4 uses #1.0 and #9.0 (global IDs). Module Mapping's "M1" and "M9" shorthand translated.
- [x] Every TVP data constraint appears in §1.5 — **PASS.** Dimensions 2-6, Areas 6-25, both orientations, specific TVP dimensions (3×4, 2×5, 4×4) all documented.
- [x] Every conflict in Table C resolved or flagged — **PASS.** 8 conflicts documented; all resolved or assigned Author Flags.
- [x] Every applicable Important Decision reflected in SP or documented as KDD — **PASS.** Decisions 1, 3, 4, 5, 6 all reflected. Decisions 2, 7, 8, 9 confirmed non-applicable.
- [x] Conceptual Spine Analysis confirms concept placement — **PASS.** "No gaps/overlaps rule" is Introduced in L2-3 (SP treats as introduction/explicit teaching). "Unit squares (tiling)" Developed in L3-4 (SP continues development). "Area as space covered" Developed in L2-3 (SP continues from M1).
- [x] Standards Mapping required vocabulary aligns with §1.3 — **PASS.** 3.MD.C.5.b vocabulary (gaps, overlaps, tiling) all in §1.3. 3.MD.C.6 advanced vocabulary (rows, columns, standard units) all in Terms to Avoid with module deferrals noted.
- [x] The One Thing references only concepts this module teaches — **PASS.** §1.0 references gap/overlap rules and accurate area measurement — all M2 concepts.
- [x] YAML front matter complete — **PASS.** module_id, unit, domain, primary_toys (with Notion URLs), secondary_toys, interaction_tools all present.

**Self-Check Result: ALL ITEMS PASS. Ready for Gate 1 evaluation.**

---

## TASK 2 SELF-CHECK (Warmup + Lesson) — v2

- [x] **Warmup Requirements Checklist** — every item marked satisfied or flagged in Task 2 draft. All 11 items pass. ✓
- [x] **Lesson Requirements Checklist** — every item marked satisfied or flagged in Task 2 draft. All 14 items pass. ✓
- [x] **Warmup bridge creates anticipation without teaching** — Bridge says "What if there were spaces, or tiles piled on top of each other? Let's find out what happens to the count." Creates curiosity without naming gap/overlap or explaining why they're wrong. ✓
- [x] **CRA phases: Concrete, Relational, Abstract, Application — each has dedicated interaction(s)** — Concrete: 1.1-1.4. Relational: 1.5 (DEDICATED). Abstract: 1.6-1.8. Application: 2.1-3.4. ✓
- [x] **Relational phase is a SEPARATE interaction (not embedded in vocabulary intro)** — 1.5 is a standalone interaction with three-state comparison + pattern statement. Vocabulary "tiling" comes AFTER in 1.6. ✓
- [x] **Symmetrical scaffolding for error types** — Gaps: 1.1 observe → 1.2 act. Overlaps: 1.3 observe → 1.4 act. Equal pacing for each error type. ✓
- [x] **Ternary error classification trained** — 1.7 (gap, answer=Gap), 1.8 (correct, answer=Correct). All three outcomes practiced before EC. ✓
- [x] **Worked examples counted: 3 with fading stages labeled** — 2.1 (Full), 2.2 (Partial), 2.3 (Minimal). ✓
- [x] **Think-aloud with tagged elements present** — 2.1a contains [PLANNING], [ATTENTION], [SELF-CHECK]. ✓
- [x] **Vocabulary staging matches §1.3 exactly:**
  - §1.3 says gap → Lesson Section 1. Draft: gap in 1.2. ✓
  - §1.3 says overlap → Lesson Section 1. Draft: overlap in 1.4. ✓
  - §1.3 says tiling → Lesson Section 1 (Rule Formation). Draft: tiling in 1.6. ✓
  - §1.3 says rectangle → Synthesis (activation). Draft: not in Warmup or Lesson. ✓
  - §1.3 says no formal vocabulary in Warmup. Draft: W.1 and W.2 use only M1 terms. ✓
- [x] **No forbidden vocabulary in any Guide or Prompt line** — Scanned all v2 text. None found. ✓
- [x] **Guide/Prompt independence verified on 3+ interactions** — Verified on 1.2, 2.1b, 3.1. ✓
- [x] **Guide/Prompt language alignment** — 1.2 Guide and Prompt both say "gaps" (fixed from v1 mismatch). ✓
- [x] **Overlap visual descriptions clarified** — 1.3 and 1.4 specify "Authored pre-tiled state using overlap visual treatment... Display mode — no student interaction." ✓
- [x] **5×5=25 removed from Section 3** — Moved to Practice per pacing concern. Section 3 has 3 independent tilings + bridge. ✓
- [x] **All interactions use toys/modes documented in §1.5** — Grid Rectangles (display + target), Unit Square Tiles (drag-to-place). No toys outside §1.5. ✓
- [x] **Dimension Tracking updated in Working Notes** — Table updated with new interactions (1.3, 1.4, 1.8) and removed interaction (old 3.3). ✓

**Self-Check Result: ALL ITEMS PASS.**

---

## TASK 3 SELF-CHECK (EC + Practice + Synthesis + KDD) — v2

- [x] **EC Requirements Checklist** — every item satisfied. 3 problems, CREATE+IDENTIFY, same toys/modes, values differ from Lesson, ternary options for IDENTIFY. ✓
- [x] **Synthesis Requirements Checklist** — every item satisfied. 3 tasks + Opening + Closure. All visuals use Grid Rectangles (no custom illustrations). ✓
- [x] **Every EC problem maps to a Lesson section with same toy/mode/interaction** — EC.1→Sections 2-3, EC.2→Section 1 (1.7-1.8), EC.3→Section 3. ✓
- [x] **EC values differ from Lesson values** — EC.1 (3×5), EC.2 (5×2), EC.3 (4×5) — none used in Lesson. ✓
- [x] **EC.2 uses ternary options** — Gap/Overlap/Correct matching Lesson 1.7-1.8 training. ✓
- [x] **No new visual models, interaction types, or vocabulary in EC** — All from Lesson. ✓
- [x] **Synthesis S.2 uses Grid Rectangles** — Redesigned from custom illustrations to Grid Rectangles with language-based real-world connection. ✓
- [x] **At least 2 different Synthesis task types** — 3 types: Pattern Discovery, Real-World Bridge, Metacognitive Reflection. ✓
- [x] **Metacognitive reflection present** — S.3 (Type 1: Strategy Identification). ✓
- [x] **Identity-Building Closure is behaviorally specific** — Names what student DID. ✓
- [x] **M3 bridge matches TVP transition out** — Correctly tiled 3×4, highlighted row, "Is there a FASTER way to count?" ✓
- [x] **KDD covers all structural decisions** — 18 KDDs covering all phases + v2 structural changes. #16-17 flagged not SME reviewed. ✓
- [x] **H3 resolved** — S4 Assessment Note added to §1.8.5. ✓
- [x] **5×5=25 documented for Practice** — Added to §1.8.5 as Practice candidate. ✓
- [x] **Dimension Tracking complete** — Updated with S.2 redesigned dimensions. ✓

**Self-Check Result: ALL ITEMS PASS.**

---

*End of Working Notes — Session 4*
