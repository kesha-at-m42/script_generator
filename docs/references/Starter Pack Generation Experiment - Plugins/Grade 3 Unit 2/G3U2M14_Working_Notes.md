# G3U2M14 Working Notes

## Session Log

**2026-04-02 — Session 1:** Starting Task 1 (Backbone + Cross-Reference). Reading Module Mapping, TVP, Important Decisions, Misconceptions, Conceptual Spine Analysis, Standards Mapping, Conceptual Development. M13 SP available for cross-module reference.

**2026-04-02 — Session 2 (continued):** Completed Task 2 self-check + Dimension Tracking. Gate 2 L1 run + author review. Applied all Gate 2 fixes (em-dashes, section reorder, distractors, ISFs, ATW items). Started and completed Task 3: §1.8 Exit Check (Ben's Room, 3 problems, error isolation), §1.8.5 Practice Inputs (4-tier distribution, 10–12 problems), §1.9 Synthesis (5 interactions, unit capstone, MP4 naming), §1.10 Key Design Decisions (10 KDDs). Task 3 self-check passed. SP feature-complete through §1.10.

**2026-04-02 — Session 3 (continued):** Gate 3 evaluation: L1 (16 MAJORs, all triaged non-actionable — 7 I9 checker limitation, 8 V4 terse-by-design, 1 ST9 section count) + L2 (8 agents, all PASS, 0 CRITICAL). Applied 1 fix from Gate 3: 2.2b prompt vagueness ("How much total?" → "How much total floor space do both pieces need?"). Author accepted notation inconsistency (ft vs feet) as-is. Task 4 assembly: updated YAML status, added end marker + §1.11 Final Formatting Audit checklist. Notion-ready file generated via sp_notion_push.py. Notion page created: `3365917e-ac52-81ff-a74b-ef6c0b2c65cf` (Status: Initial Draft). Awaiting human paste of full SP content.

---

## Cross-Reference Table A — Module Mapping Extraction

```
MODULE MAPPING: M14
====================
Module: M14
OUR Lessons: L15
Core Concept: Room Design Application
OUR Learning Goals (Verbatim): Solve problems involving the area of ungridded figures composed of rectangles including figures with missing side lengths.
Standards - Building On: All 3.MD.C standards from unit
Standards - Addressing: 3.MD.C.5; 3.MD.C.6; 3.MD.C.7.b; 3.MD.C.7.d (comprehensive application)
Standards - Building Toward: (application/synthesis module)
Notes: Culminating application. Room and furniture context. Students find missing sides, calculate room area, determine if furniture fits. Multiple valid approaches. Mathematical modeling precursor. OPTIONAL lesson included per Decision 9 - kept standalone.
Vocabulary to Teach: (consolidation - no new vocabulary)
Question/Test Language: Will the bed and desk fit in the room? Show your work. What is the usable floor space?
Vocabulary Teaching Notes: Real-world terms: room, furniture, floor space. Connect to area vocabulary.
Scaffolding of Visuals: Room diagram with some measurements; Furniture with dimensions; Design/planning context
Key Misconceptions: All previous misconceptions may surface
```

**Flag — Vocabulary to Teach:** "(consolidation - no new vocabulary)" — no new terms to teach. This is consistent with M14 being a culminating application module. Reinforcement only.

**Flag — Standards - Building Toward:** "(application/synthesis module)" — no future standard is built toward. M14 is the capstone. Consistent with Decision 9 (optional standalone).

---

## Cross-Reference Table B — TVP Extraction

```
TVP: MODULE 14
===============
Title: Room Design Application
OUR Lesson: 15 (optional, per Decision 9)
Standards: 3.MD.C.5; 3.MD.C.6; 3.MD.C.7.b; 3.MD.C.7.d (comprehensive application)

⚠️ APPLICATION MODULE — NO NEW SKILLS. M14 applies everything from M11–M13 in a sustained real-world context. Students find missing side lengths, calculate composite area, and make decisions about furniture placement. The cognitive challenge is not any single step — it's orchestrating ALL steps in service of a real question: "Will the furniture fit?"

What makes this different from M13: M13 isolated missing-side reasoning with abstract figures. M14 embeds the same skills inside a multi-phase problem where the math ANSWERS a question. Students don't just "find the area" — they find the area because they need to know if a bed and desk will fit in a room. This is mathematical modeling: translating a real situation into math, solving, then translating the answer back into a decision.

Why standalone (Decision 9): The room design problem is substantial enough to fill a module. It combines missing sides (M13), decomposition (M11–M12), area calculation, comparison (M9), and spatial decision-making into a single sustained problem.

Learning Goal: Solve problems involving the area of ungridded figures composed of rectangles including figures with missing side lengths.

Key Teaching Points:
1. Everything you've learned about area comes together here: finding missing sides, breaking shapes into rectangles, multiplying to find area, adding areas together.
2. THE BIG SHIFT: The question isn't "What is the area?" — it's "Will this furniture fit?" Area is the TOOL for answering a real question.
3. The room is an L-shaped (or T-shaped) composite figure with some missing dimensions. Students must find missing sides before they can calculate the room's total area. This is M13's skill in context.
4. Furniture (bed, desk) has given dimensions. Students calculate furniture areas and compare them to available room space. This is M9's comparison skill applied to composite figures.
5. Multiple valid approaches: Students can decompose the room in different ways, place furniture in different locations, and reason about "usable space" differently.
6. "Usable floor space" = total room area minus furniture area. This is a new application of subtraction in the area context (not subtraction decomposition of the shape — subtraction of object areas from room area).

CRA Stage: Abstract — labels only, no grids. Full independence.

Cognitive Focus:
- APPLY (Transfer) — orchestrating the full find-missing-sides → decompose → calculate → add workflow in context
- CONNECT (Transfer) — linking area calculation to real-world decision-making ("will it fit?")
- COMPARE (Conceptual) — comparing furniture areas to available room space

Misconceptions Targeted:
- M7: Wrong Missing Side Length (PRIMARY, HIGH) — Room shapes have more sides than abstract M13 figures; real-world context adds parsing overhead. Addressed by: Highlight Related Sides available as remediation; "related sides" vocabulary established in M13.
- M12: Multiplying All Given Numbers (SECONDARY) — Room diagrams have many visible numbers (room + furniture + found sides). Addressed by: clear visual separation between room and furniture; per-rectangle dimension highlighting after decomposition.
- M11: Completing the Rectangle (SECONDARY) — L-shaped rooms invite bounding-box thinking. Addressed by: decomposition-first workflow; furniture-fitting question catches error (room area too large → furniture "obviously fits").
- M6: Overlapping Decomposition (TERTIARY) — May surface from careless decomposition. Lower risk — students practiced across M11–M13.
- Context-specific: Confusing room area with furniture area — Students calculate room correctly but use room dimensions for furniture. Addressed by: clear visual separation; furniture shown separately.

PHASE-BY-PHASE FLOW:

WARM-UP — Notice and Wonder
- Composite Figures (L-shaped room diagram, labels only, some missing sides marked "?") displayed as a room floor plan. Labels: "Ana's New Room." Furniture NOT shown yet.
- "What do you notice? What do you wonder?"
- MC notice options (select all that apply): "The room isn't a rectangle," "Some measurements are missing," "The room has a bump/indent," "There are numbers on some sides." All correct selections acknowledged.
- MC wonder options (select 1): "How big is the room?", "What could fit in this room?", "What are the missing measurements?" All valid; guide affirms selected one and adds: "Great question! Let's figure all of that out."
- Purpose: Activate prior knowledge, orient to room context, let students notice composite shape and missing sides WITHOUT being told what to do yet.
- No calculation in warm-up. Observation and engagement only.

LESSON — Early activities (Understand the room — find missing sides + total room area):
- Composite Figures (L-shaped room, labels only, 2 missing sides marked "?", units in feet)
- Guide: "Before we can figure out what fits in Ana's room, we need to know how big it is. But first — some measurements are missing. Let's find them."
- Students find missing sides using M13 workflow. Highlight Related Sides: remediation only (guide-activated if wrong MC answer). No automatic support.
- After missing sides found, all dimensions visible. Guide: "Now we know all the measurements. How can we find the total area?"
- Students decompose (student-placed), calculate each rectangle's area, add. Standard M12 workflow — fully independent. Equation Builder available but not required.
- Guide: "Ana's room is [X] square feet. Now — what can she fit in it?"
- 1 room shape, worked through step by step. SINGLE problem with multiple stages.
- ⚠️ Key beat — the room IS the problem: ONE room for the entire module. Every subsequent activity builds on this room. Missing sides found in Early are USED in Mid and Late.
- ⚠️ Engineering — state persistence: Room figure with resolved missing sides must persist across lesson phases.

LESSON — Mid activities (Furniture fitting — calculate and compare):
- Room diagram persists from Early (all dimensions visible). Two furniture items introduced SEPARATELY:
  - Bed: Rectangle, 7 ft × 4 ft
  - Desk: Rectangle, 5 ft × 3 ft
- ⚠️ Visual design — furniture displayed SEPARATELY from room. NOT overlaid.
- ⚠️ Pronoun ambiguity with multiple objects: Guide must NEVER say "look at the dimensions" without specifying WHICH object.
- Step 1: Calculate furniture areas.
  - "How much floor space does the bed need?" Student: 7 × 4 = 28 sq ft
  - "How much floor space does the desk need?" Student: 5 × 3 = 15 sq ft
  - "How much total floor space do both pieces need?" Student: 28 + 15 = 43 sq ft
- Step 2: Will it fit?
  - "Ana's room is [X] square feet. The bed and desk together need 43 square feet. Will they fit?"
  - MC: Yes / No / Not sure — depends on shape
  - ⚠️ KEY MATHEMATICAL MODELING MOMENT: "enough area ≠ it fits." Room dimensions designed so furniture DOES fit (positive resolution).
- Step 3: Where does it go?
  - Room decomposed regions visible. Student selects which region fits the bed (dimensions ≥ 7 and ≥ 4 in either orientation). Then desk. Multiple valid placements acknowledged.
- 1 sustained problem across all three steps.
- ⚠️ Explicit step-naming for pacing recommended.

LESSON — Late activities (Usable floor space — remaining area):
- Room with furniture placed (from Mid).
- "How much floor space is left for walking around?"
- Usable floor space = room area − furniture area. SUBTRACTION of areas, not subtraction decomposition.
- ⚠️ FIRST subtraction in area context. Guide must frame operation contrast: "We found the total room area by ADDING rectangle areas together. Now we're taking AWAY the furniture area..."
- Student calculates: [room area] − [bed area] − [desk area] = [usable space]
- "Is that enough to move around?" (Open question — no right answer)
- Extension (if time allows): SECOND room layout (T-shape, different dimensions, missing sides). Compare to Ana's room. STRETCH, not core requirement. 1 problem max.
- Key beat: By end of Late, students have used every skill from M11–M14 arc.

EXIT CHECK:
- 3 problems (NEW room, not Ana's — tests transfer):
  1. Missing sides + total area: L-shaped room with 1 missing side. Find missing dimension, decompose, calculate total area.
  2. Furniture fitting comparison: "A bookshelf is 6 ft × 2 ft. A dresser is 4 ft × 3 ft. What is the total floor space both pieces need?" (Multi-step area calculation)
  3. Decision problem: "The room from problem 1 has [X] sq ft. The furniture from problem 2 needs [Y] sq ft. Is there enough room? How much floor space is left over?" (Comparison + subtraction)
- ⚠️ Error isolation: Problems 1–3 are connected but if student gets P1 wrong, P2–3 use CORRECT room area. Each tests its target skill independently.

PRACTICE:
- Mixed room-design problems with NEW room shapes
- Some rooms with 1 missing side, some with 2
- Various furniture combinations
- All in square feet (room context)
- Highlight Related Sides as remediation only
- ⚠️ Error cascading guidance from M13 still applies
- STRETCH — "Enough area but doesn't fit" problems (1–2, tagged CHALLENGE):
  - Furniture selection: Display room with decomposed regions, 4–5 furniture items. "Select ALL that fit in [region]." Some items have area < region but dimensions exceed.
  - Playpen design: 12 sq ft playpen for 5×4 region. Student explores factor pairs (1×12, 2×6, 3×4). Discovery that some valid areas don't fit.

SYNTHESIS — Unit Capstone:
- NOT just M14 synthesis — synthesis for M11–M14 arc and entire unit's area progression.
- ⚠️ Celebration tone, not test review.
- The area toolkit — everything students can now do: M1–M2 (unit squares), M3–M4 (row-by-column), M5–M6 (standard units), M7–M8 (multiply side lengths), M9 (real-world problems), M10 (multiplication table), M11 (composite shapes), M12 (without grids), M13 (missing sides), M14 (room design).
- "You started this unit covering shapes with squares. Now you can find the area of a room, figure out if furniture fits, and calculate how much floor space is left. That's what mathematicians do — they use math to solve real problems."
- Vocabulary review (consolidation only): area, square unit, square foot, square meter, dimensions, multiply, decompose, composite figure, missing side, related sides, expression, additive
- Mathematical Practices: MP1 (persevered), MP4 (modeling with mathematics). Named, not taught.

Scaffolding Progression:
- Almost no scaffolding to fade — that's the point. Students should arrive having mastered each component skill.
- Only scaffold: Highlight Related Sides as remediation for missing-side errors.
- If students aren't ready: M14 is optional (Decision 9). Skip and revisit M11–M13 instead.

Tool Requirements:
- Composite Figures (same as M11–M13): L/T-shaped rooms, labels only, missing sides, decomposition, color-coding
- Equation Builder (same as M12–M13): additive expressions, color-coded terms
- NEW — Furniture display: Simple labeled rectangles (bed, desk, etc.) displayed SEPARATELY from room. Reference info, NOT interactive.
- NEW — Furniture placement MC: After decomposition, room regions highlighted. Student selects which region fits furniture by comparing dimensions. MC options = decomposed regions.
- ⚠️ Engineering — state persistence across lesson phases: Room established in Early (including resolved missing sides) must persist into Mid and Late.
- ⚠️ Engineering — authored figure metadata (from M13): Missing side solving order pre-defined per room figure.

Data Constraints:
- Room figures: L-shaped or T-shaped rooms. 2–3 component rectangles. Side lengths 3–10 feet. Total area 40–80 sq ft. 1–2 missing sides.
- Room dimensions designed so target furniture FITS (area + dimensions compatible). Positive resolution.
- Missing sides follow M13 constraints: values ≥ 2, clean subtraction, authored solving order.
- Room shapes should feel room-like (closet bump-out, window alcove — not abstract puzzles).
- Furniture items: Simple rectangles, whole-number ft dimensions.
  - Bed: 7 × 4 or 6 × 4
  - Desk: 5 × 3 or 4 × 3
  - Optional: bookshelf (6 × 2), rug (5 × 4), dresser (4 × 3)
  - Furniture dimensions ≤ smallest room region dimension they fit in
  - 2 dimensions each, no compound furniture
- Fitting constraints:
  - At least one decomposed region with dimensions ≥ both furniture dimensions (either orientation)
  - Total furniture area < total room area
  - "Will it fit?" = YES for all main lesson problems
  - Practice: 1–2 STRETCH where "enough area ≠ it fits"
- Usable floor space: room area − furniture areas. Result ≥ 5 sq ft.
- EC room: Different from lesson room. L-shaped, 1 missing side, simpler. Total area 30–60 sq ft. 2 furniture items.
- Context: All in square feet. Room/furniture context throughout. No abstract figures.
- AVOID: U-shapes or complex figures, >2 missing sides/room, furniture that doesn't fit (main lesson), gridded figures, problems without context, >2 furniture items in lesson (3rd in Practice as stretch).

Vocabulary:
- New: (none)
- Reinforced: area, square feet, dimensions, composite figure, decompose, missing side, related sides, multiply, add, expression
- Context vocabulary (receptive, not taught): room, floor plan, furniture, floor space, "usable space"
- Language patterns:
  - "The room has an area of ___ square feet."
  - "The bed needs ___ square feet of floor space."
  - "Is there enough room for the bed and desk? How do you know?"
  - "How much floor space is left after placing the furniture?"

TRANSITION IN (from M13):
- Pedagogical Shift: Abstract skill isolation (M13) → Contextual application (M14). Same skills, real-world purpose.
- What carries forward: Missing-side reasoning, decompose-calculate-add workflow, dimension pairing, all M11–M13 engineering specs, Highlight Related Sides (remediation only), "related sides" vocabulary
- What's new: Sustained room context (one room across entire module), furniture comparison, "will it fit?" decision-making, usable floor space calculation, state persistence across lesson phases, mathematical modeling precursor (MP4)

TRANSITION OUT:
- M14 is the final module in Unit 2. No M15 transition. Unit capstone.
- M14 establishes: Students can use area to answer real-world questions. Can orchestrate multi-step problem involving composite shapes, missing dimensions, area calculation, and comparison — all without visual scaffolding.
- What this prepares for: Mathematical modeling (MP4) thread across grades 3–5. M14 is first experience with "use math to make a decision about the real world."

SME Review Resolutions:
1. Furniture fitting "gotcha" — RESOLVED: Not in main lesson. Practice includes 1–2 STRETCH problems.
2. State persistence — RESOLVED: If supported, true persistence. Fallback: re-display with all dimensions + brief reminder.
3. Second room in Late extension — RESOLVED: Optional/stretch.
4. Equation Builder — RESOLVED: Keep available. Orchestration is the challenge, not arithmetic.
5. Unit-level synthesis — RESOLVED: Keep in M14's synthesis as unit-wide review and celebration.
6. M14 optional status — CONFIRMED per Decision 9.
```

---

## Cross-Reference Table C — Conflict Log

```
CONFLICT LOG
============

#1
Field: Vocabulary to Teach
Module Mapping says: "(consolidation - no new vocabulary)"
TVP says: No new terms. Reinforced: area, square feet, dimensions, composite figure, decompose, missing side, related sides, multiply, add, expression. Context vocabulary: room, floor plan, furniture, floor space, "usable space."
Resolution: Aligned — both agree no new vocabulary. TVP provides specific reinforcement list. Use TVP's reinforcement list in §1.3.
Status: Resolved

#2
Field: Key Misconceptions
Module Mapping says: "All previous misconceptions may surface"
TVP says: Specific prioritization — M7 (PRIMARY HIGH), M12 (SECONDARY), M11 (SECONDARY), M6 (TERTIARY), plus context-specific (confusing room/furniture area)
Resolution: TVP provides the detailed analysis. Use TVP's prioritized list in §1.4. Module Mapping's "all may surface" is accurate but non-specific — TVP refines it.
Status: Resolved (TVP wins for specificity)

#3
Field: Standards - Building On
Module Mapping says: "All 3.MD.C standards from unit"
TVP says: (Implicit — standards listed as 3.MD.C.5, 3.MD.C.6, 3.MD.C.7.b, 3.MD.C.7.d as both addressed and built on)
Resolution: Module Mapping's "all 3.MD.C standards" is broader. TVP specifies the four main ones. For §1.1 Standards Cascade, use TVP's specific list with Module Mapping's broader framing.
Status: Resolved

#4
Field: Scaffolding of Visuals
Module Mapping says: "Room diagram with some measurements; Furniture with dimensions; Design/planning context"
TVP says: Detailed specification — L/T-shaped rooms, labels only, 1–2 missing sides, furniture displayed separately, decomposed regions for placement MC, dimension highlighting per rectangle after decomposition
Resolution: TVP provides full specification. Module Mapping's description is high-level and consistent. Use TVP in §1.5.
Status: Resolved (TVP wins for tool/visual decisions per resolution hierarchy)

#5
Field: Figure types
Module Mapping says: (not specified beyond "room and furniture context")
TVP says: L-shaped and T-shaped rooms only. NO U-shapes or complex figures. Avoid >2 missing sides per room.
Resolution: TVP constrains figure types. Module Mapping doesn't contradict. Follow TVP.
Status: Resolved

#6
Field: Missing side dependency chains
Module Mapping says: (not specified)
TVP says: M14 "may also introduce dependency chains (where one missing side requires another to be found first)" per M13 Module Bridge, BUT the TVP's actual M14 specification says "1–2 missing sides" and follows M13 constraints (independently solvable). The data constraints say "Missing sides follow M13 constraints."
Resolution: The M13 Bridge text suggests M14 MAY have dependency chains, but the actual M14 TVP section constrains missing sides to M13 constraints (independently solvable). The TVP's specific M14 data constraints override the forward-looking bridge text. No dependency chains in M14 main content. This is conservative — if SME review wants dependency chains, flag as Author Flag.
Status: Resolved — ⚠️ AUTHOR FLAG AF-1 (see below)

#7
Field: Furniture dimensions
Module Mapping says: (not specified)
TVP says: Bed 7×4 or 6×4, Desk 5×3 or 4×3. Optional: bookshelf 6×2, rug 5×4, dresser 4×3.
Resolution: Follow TVP.
Status: Resolved
```

---

## Design Constraints Extraction — Important Decisions

```
DESIGN CONSTRAINTS (from Important Decisions)
=============================================

Decision 1: Unified Path with Adaptive Pacing
  Rule: Single instructional path following CRA progression. Differentiate through pacing and representation duration.
  Applies to M14? YES
  Constraint: M14 uses the same path all students followed through M11–M13. No alternative approaches based on ability level.

Decision 2: Explicit Spatial Structuring as Central Focus
  Rule: Row-by-column "seeing" is an explicit instructional target. Delay multiplication formula until students demonstrate structuring.
  Applies to M14? PARTIAL
  Applies: Students should be fluent with row-column structuring by M14. The spatial structuring concept is ASSUMED, not taught.
  Doesn't apply: The "delay formula" aspect was resolved in earlier modules.

Decision 3: Progressive Grid Removal (Concreteness Fading)
  Rule: M13–M14: Dimensions only with missing sides (full abstraction)
  Applies to M14? YES — HARD CONSTRAINT
  Constraint: NO grids in any phase of M14. All figures are labels-only with dimension values. Full abstraction. This is the culmination of the fading sequence.

Decision 4: Array Knowledge is Helpful but Not Required
  Rule: Design Unit 2 to be self-contained. Leverage array knowledge if present, don't assume it.
  Applies to M14? PARTIAL
  By M14, students have been working with area concepts for 13 modules. Array knowledge is well-established within this unit. The "self-contained" principle is fully served.

Decision 5: Perimeter Kept Separate — Do Not Introduce
  Rule: Do NOT introduce perimeter. Do not proactively address perimeter-area confusion.
  Applies to M14? YES — HARD CONSTRAINT
  Constraint: No mention of perimeter. "Usable floor space" calculation (room area − furniture area) must NOT be framed as perimeter-adjacent. The subtraction is of AREAS, not edge measurements.

Decision 6: Dragging Over Tapping for Manipulatives
  Rule: Prioritize drag-to-place for virtual manipulatives. Exception: Simple selection tasks use tap.
  Applies to M14? YES
  Constraint: Decomposition line drawing uses drag. MC selections use tap. Furniture placement MC uses tap (simple selection). No new drag interactions specified in M14.

Decision 7: Standard Units Get Full Scaffolding (L6 and L7 Separate)
  Rule: Keep square inches/cm and square feet/meters as separate modules.
  Applies to M14? NO — already resolved in earlier modules. M14 uses square feet only.

Decision 8: Include Multiplication Table Connection (L11) as Module
  Rule: Include OUR L11 as synthesis/connection module.
  Applies to M14? NO — resolved. M10 is in the unit. M14 references M10 in synthesis toolkit list.

Decision 9: Keep Application Module (L15) Standalone
  Rule: Include OUR's optional L15 as standalone module, not combined.
  Applies to M14? YES — DEFINING CONSTRAINT
  Constraint: M14 IS L15. It is recommended but optional. Students who complete M13 successfully have met all Unit 2 standards. M14 adds application value but no new standards content.
```

---

## Author Flags

⚠️ **AUTHOR FLAG AF-1 (Dependency Chains):** The M13 Starter Pack's Module Bridge text says M14 "may also introduce dependency chains (where one missing side requires another to be found first)." However, the TVP's actual M14 data constraints specify "Missing sides follow M13 constraints" (independently solvable) and limit rooms to 1–2 missing sides. I'm following the TVP's specific M14 constraints (no dependency chains). If you want dependency chains introduced in M14, this would need to be explicitly designed into the room figures and the data constraints updated. **Decision needed:** Confirm no dependency chains in M14, or specify which lesson phase should introduce them and with what scaffolding.

⚠️ **AUTHOR FLAG AF-2 (Room Dimensions for Lesson):** The TVP specifies bed 7×4 and desk 5×3 (total furniture area = 43 sq ft). The room must be L-shaped, 40–80 sq ft total, with decomposed regions where at least one region has dimensions ≥ 7 and ≥ 4 (bed fits). I need to design specific room dimensions. The TVP doesn't provide a specific room layout. **Decision needed:** Should I design the room dimensions, or do you have a specific layout in mind? I'll propose one in the Backbone draft for your review.

⚠️ **AUTHOR FLAG AF-3 (EC Room Dimensions):** The TVP specifies a different L-shaped room for EC, simpler than lesson, 30–60 sq ft, 1 missing side, 2 furniture items (bookshelf 6×2, dresser 4×3 per TVP options). Needs specific dimensions designed. Same question as AF-2 for the EC room.

---

## Section Plan

**Warmup (~2 min):** Notice and Wonder warmup type. L-shaped room floor plan ("Ana's New Room") with some missing side labels. MC notice (multi-select) and MC wonder (single-select). NO calculation — observation and engagement. Bridge: orients to room context, activates composite figure and missing-side recognition from M13, establishes the sustained problem context that carries through the entire module.

**Lesson (~10–12 min):** Three sections forming ONE sustained problem (same room throughout).
- **Early (~4 min):** Find missing sides on Ana's room (M13 skill transfer to room context) + decompose + calculate total room area (M12 workflow). HRS remediation-only. 1 room, multiple stages. CRA: Application stage — full abstraction, known skills in real-world context.
- **Mid (~4–5 min):** Furniture fitting — calculate bed/desk areas, compare to room area ("Will it fit?" MC), determine placement (which region). Three sub-steps in one sustained problem. Key mathematical modeling moment: "enough area ≠ it fits" surfaced through discussion but furniture DOES fit. CRA: Application (same stage, new cognitive demand: orchestration + comparison + decision-making).
- **Late (~2–3 min):** Usable floor space — room area minus furniture area. FIRST subtraction in area context — must frame operation contrast explicitly. Optional stretch: second room (T-shape) comparison. CRA: Application (consolidation).

**Exit Check (~3 min):** 3 connected problems on a NEW room (transfer test). EC.1: missing side + total area (APPLY). EC.2: furniture areas (APPLY — simple multiplication + addition). EC.3: comparison + remaining space (COMPARE + APPLY). Error isolation: each problem tests independently even though context is shared.

**Practice:** Mixed room-design problems, new rooms, various furniture. BASELINE through STRETCH tiers. STRETCH includes "enough area but doesn't fit" problems (furniture selection multi-select, playpen design factor-pair exploration). All in square feet, room context.

**Synthesis (~5–6 min):** UNIT CAPSTONE — not just M14 synthesis. Celebration tone. Toolkit review (M1→M14 arc). Metacognitive reflection on orchestration. Identity-building closure connecting to mathematical modeling (MP4). No M15 bridge (unit ends here).

**Module timing estimate:** ~20–23 min total (Warmup 2 + Lesson 10–12 + EC 3 + Synthesis 5–6). Slightly above the ~15 min block target. NOTE: This is acceptable because M14 is optional (Decision 9) and functions as a capstone application module. The sustained-context structure (one room across all phases) makes timing harder to compress without losing coherence. The Late extension (second room) is explicitly optional/stretch and should be deferred to Practice if timing is tight. Without the Late extension, Lesson is ~9–10 min, bringing the block closer to target.

**Synthesis task types (per Playbook minimum 2):**
1. Real-World Bridge → Toolkit Display (unit progression walkthrough — M1 through M14)
2. Metacognitive Reflection (Type 1: Strategy Identification — "What helped you orchestrate all those steps?")
3. Identity-Building Closure (celebration of growth + MP4 connection)

**Interaction count estimate:** Warmup ~3, Lesson Early ~4–5 (multi-step on one room), Lesson Mid ~4–5 (3 sub-steps), Lesson Late ~2–3, EC 3, Synthesis 4–5. Total: ~20–24 interactions.

---

## Dimension Tracking

*Populated during Task 2. Tracks all numerical values across Warmup and Lesson interactions to verify consistency, catch dimension ambiguity, and support EC/Practice design.*

### Room Dimensions (Ana's Room — persists W.1 through 3.2)

| Side | Length | Direction | Position | Visible From |
|------|--------|-----------|----------|-------------|
| Bottom | 10 ft | Horizontal | Outer bottom | W.1 |
| Left | 9 ft | Vertical | Outer left | W.1 |
| Top-right | 4 ft | Horizontal | Inner top-right | W.1 |
| Right | 4 ft | Vertical | Outer right | W.1 |
| Top-left (missing) | 6 ft | Horizontal | Inner top-left | Resolved at 1.2 |
| Inner step (missing) | 5 ft | Vertical | Inner vertical step | Resolved at 1.3 |

**Dimension-ambiguity note:** Two sides are 4 ft (top-right horizontal, right-side vertical). Bed is also 4 ft wide. Guide language always specifies direction + position (e.g., "the room's right side, which is 4 feet tall") per Task 2 Watch Item #7.

### Decomposition Options

| Cut | Region A | Region B | Total |
|-----|----------|----------|-------|
| Horizontal | 10 × 4 = 40 sq ft (bottom strip) | 6 × 5 = 30 sq ft (top-left block) | 70 sq ft |
| Vertical | 6 × 9 = 54 sq ft (left block) | 4 × 4 = 16 sq ft (bottom-right square) | 70 sq ft |

### Furniture Dimensions

| Item | Width | Height | Area | Introduced At |
|------|-------|--------|------|---------------|
| Bed | 7 ft | 4 ft | 28 sq ft | 2.1 |
| Desk | 5 ft | 3 ft | 15 sq ft | 2.2a |
| **Total** | — | — | **43 sq ft** | 2.2b |

### Interaction-Level Value Tracking

| Interaction | Values Used | MC Options | Correct | Key Calculation |
|-------------|-------------|------------|---------|-----------------|
| W.1 | 10, 9, 4, 4 (visible); 6, 5 (hidden as "?") | A/B/C/D (all valid) | All | Observation only |
| W.2 | Same room | A/B/C (all valid) | All | Observation only |
| 1.1 | Same room (no calculation) | — (Type A) | — | Planning think-aloud |
| 1.2 | 10, 4 → 6 (horizontal missing side) | 6, 14, 5, 4 | A (6) | 10 − 4 = 6 |
| 1.3 | 9, 4 → 5 (vertical missing side) | 5, 13, 6, 3 | A (5) | 9 − 4 = 5 |
| 1.4 | All 6 dims visible | Drag decomposition | Any valid cut | Decompose L-shape |
| 1.5a | First rectangle dims | 40, 14, 30, 60 | A (40) | 10 × 4 = 40 (H-path) |
| 1.5b | Second rectangle dims | 30, 11, 40, 54 | A (30) | 6 × 5 = 30 (H-path) |
| 1.5c | Sum of rectangles | 70, 60, 80, 90 | A (70) | 40 + 30 = 70 |
| 2.1 | Bed 7, 4 | 28, 11, 40, 70 | A (28) | 7 × 4 = 28 |
| 2.2a | Desk 5, 3 | 15, 20, 8, 50 | A (15) | 5 × 3 = 15 |
| 2.2b | 28, 15 | 43, 33, 13, 70 | A (43) | 28 + 15 = 43 |
| 2.3 | Room 70, Furniture 43 | Yes / No / Depends | C (best); A (accepted) | 70 > 43 + dimensional check |
| 2.4 | Bed 7×4 vs regions | Region A / Region B | Region A (H-path) | 7 ≤ 10, 4 ≤ 4 |
| 2.5 | Desk 5×3 vs remaining | Yes / No | A (Yes) | 5 ≤ 6, 3 ≤ 5 (H-path) |
| 3.1 | Room 70, Furniture 43 | 27, 113, 33, 70 | A (27) | 70 − 43 = 27 |
| 3.2 | Recap all values | — (Type A) | — | Reflection |

### EC Room Dimensions (different room — transfer test)

| Side | Length | Direction | Notes |
|------|--------|-----------|-------|
| Bottom | 8 ft | Horizontal | |
| Left | 7 ft | Vertical | |
| Top-left | 5 ft | Horizontal | |
| Inner step (missing) | 4 ft | Vertical | 7 − 3 = 4 |
| Top-right | 3 ft | Horizontal | |
| Right | 3 ft | Vertical | |

EC total area: 44 sq ft. EC furniture: bookshelf 6×2 (12 sq ft) + dresser 4×3 (12 sq ft) = 24 sq ft. Usable: 20 sq ft.

### EC Interaction-Level Value Tracking

| Interaction | Values Used | MC Options | Correct | Key Calculation |
|-------------|-------------|------------|---------|-----------------|
| EC Transition | Ben's room (8, 7, 5, 3, 3, "?") | — (no action) | — | Orientation |
| EC.1a | Left 7, Right 3 → missing 4 | 4, 10, 3, 7 | A (4) | 7 − 3 = 4 |
| EC.1b | All dims visible | Drag decomposition | Any valid cut | Decompose L-shape |
| EC.1c | Decomposed rectangles | 44, 56, 35, 24 | A (44) | H: 8×3+5×4 or V: 5×7+3×3 |
| EC.2a | Bookshelf 6, 2 | 12, 8, 18, 42 | A (12) | 6 × 2 = 12 |
| EC.2b | Dresser 4, 3 | 12, 7, 16, 32 | A (12) | 4 × 3 = 12 |
| EC.2c | 12, 12 | 24, 20, 44, 14 | A (24) | 12 + 12 = 24 |
| EC.3a | Room 44, Furniture 24 | Yes, No | A (Yes) | 44 > 24 |
| EC.3b | 44, 24 | 20, 68, 24, 44 | A (20) | 44 − 24 = 20 |

### Value Consistency Cross-Check

- [x] Room dimensions in W.1 match §1.5 Data Constraints (10, 9, 4, 4 visible; 6, 5 hidden) ✓
- [x] Missing side calculations consistent across 1.2 and 1.3 ✓
- [x] Decomposition totals equal in both paths (70 sq ft) ✓
- [x] Furniture areas correct: 7×4=28, 5×3=15, total=43 ✓
- [x] Usable floor space: 70−43=27 ≥ 5 ✓
- [x] EC values differ from Lesson values ✓ (different room, different furniture). Room: 44 vs 70 sq ft. Furniture: 24 vs 43 sq ft. Usable: 20 vs 27 sq ft. Missing side: 4 (from 7−3) vs 6 and 5 (from 10−4 and 9−4). No shared calculation results.
- [x] All MC distractors are distinct from correct answer and from each other within each interaction ✓ (verified for both Lesson and EC interactions)
- [x] Cross-interaction distractor reuse: 70 appears as distractor D in both 2.1 (room area grab) and 2.2b (anchoring on room area). Same value, same diagnostic meaning (student confused room total for a per-item value). Acceptable — different interactions testing different skills, and 70 is the most natural wrong-grab value in both contexts. No other cross-interaction duplicates.
- [x] Dimension-ambiguity convention applied consistently (4 ft always specified by direction+position) ✓

---

## Edit Reconciliation Pass

```
EDIT RECONCILIATION
===================
No numbered TVP edits (Edit 83, 84, 88, 91, etc.) apply to M14.
The M14 TVP section references only Important Decisions (Decision 9).
The earlier edits (which primarily affected M7–M9 data constraints)
have no downstream impact on M14.

Status: COMPLETE — no edits to reconcile.
```

---

## Data-Level Constraint Audit

```
DATA CONSTRAINT AUDIT
=====================

Example Set 1: Lesson Room — L-shaped, bed 7×4, desk 5×3
Constraints:
- Room total area 40–80 sq ft
- Side lengths 3–10 feet
- 1–2 missing sides, independently solvable, values ≥ 2
- At least one decomposed region with dimensions ≥ 7 and ≥ 4 (bed fits either orientation)
- At least one remaining region with dimensions ≥ 5 and ≥ 3 (desk fits either orientation)
- Total furniture area (43 sq ft) < total room area
- Usable floor space ≥ 5 sq ft
- Room feels room-like (closet bump-out, window alcove)
Proposed room: L-shaped, two rectangles:
  Rectangle A: 10 × 7 = 70 sq ft (where: width=10 along bottom, height=7 up left side)
  Rectangle B: 3 × 4 = 12 sq ft (bump-out/alcove — width 3, height 4)
  Wait — this doesn't form a clean L-shape. Need to design carefully.

  Better approach: L-shape formed by cutting a notch from a bounding rectangle.
  Bounding rectangle: 10 × 8
  Notch cut: 4 × 3 from one corner
  Resulting L-shape total area: 80 − 12 = 68 sq ft
  Two component rectangles after decomposition:
    Option A: 10 × 5 = 50 and 6 × 3 = 18 → total 68 ✓
    Option B: 10 × 8 = 80 minus 4 × 3 = 12 → 68 (subtraction decomp, NOT used per M13 conventions)

  Visible dimensions on the L-shape:
    Bottom: 10 ft
    Left side: 8 ft
    Top-left horizontal: 6 ft (missing? or labeled)
    Notch vertical: 5 ft (missing? or labeled)
    Notch horizontal: 4 ft
    Right side going up from bottom: 3 ft — WAIT, this needs more careful geometry.

  Let me define the L-shape precisely:
    Outer bottom: 10 ft (horizontal)
    Left side: 8 ft (vertical, full height)
    Top of left section: goes right 6 ft (horizontal)
    Step down: 5 ft vertical (from 8 to 3)... No, step down = 8 - 3 = 5 ft
    Top-right horizontal: 4 ft (= 10 - 6)
    Right side: 3 ft (vertical, up from bottom-right)

    Side lengths: 10, 8, 6, 5, 4, 3
    All in range 3–10 ✓

    Missing sides: Could hide the 6 ft (top-left horizontal) and the 5 ft (step vertical).
      6 = 10 - 4 ✓ (horizontal: total 10, piece 4, missing = 6)
      5 = 8 - 3 ✓ (vertical: total 8, piece 3, missing = 5)
    Both independently solvable ✓
    Both ≥ 2 ✓

    Decomposition options:
      Horizontal cut: 10 × 3 (bottom) + 6 × 5 (top-left) = 30 + 30 = 60 sq ft
      Vertical cut: 6 × 8 (left) + 4 × 3 (bottom-right) = 48 + 12 = 60 sq ft

    Total area: 60 sq ft ✓ (in 40–80 range)

    Bed 7×4 fitting check:
      Horizontal decomp: 10×3 (bed 7×4 — fits: 7≤10, 4>3 NO. Try other orientation: 4≤10, 7>3 NO)
      Bed doesn't fit in 10×3 region. Try 6×5: 7>6 NO; 4≤6, 7>5 NO. BED DOESN'T FIT.

    PROBLEM: With this L-shape (total 60 sq ft), neither decomposed region fits a 7×4 bed.
    Need larger regions.

  Revised room: L-shape with larger sections.
    Outer bottom: 10 ft
    Left side: 9 ft
    Top-left: 6 ft
    Step down: 9 - 4 = 5 ft
    Top-right: 4 ft (= 10 - 6)
    Right side: 4 ft

    Missing sides: 6 (= 10 - 4, horizontal) and 5 (= 9 - 4, vertical)
    Both independently solvable ✓, both ≥ 2 ✓

    Decomposition (vertical cut): 6 × 9 = 54 + 4 × 4 = 16 → total 70 sq ft
    Decomposition (horizontal cut): 10 × 4 = 40 + 6 × 5 = 30 → total 70 sq ft

    Bed 7×4 in 6×9 region: 7>6 NO; swap: 4≤6, 7≤9 YES ✓
    Desk 5×3 in 4×4 region: 5>4 NO; swap: 3≤4, 5>4 NO. DESK DOESN'T FIT in 4×4.
    Desk in 6×9 (if bed elsewhere): 5≤6, 3≤9 YES. But bed is in 6×9.
    Can both fit in 6×9? 6×9 = 54 sq ft. Bed takes 28, desk takes 15 = 43. 54 > 43 but dimension overlap.

    Use the horizontal decomposition: 10×4 and 6×5.
    Bed in 10×4: 7≤10, 4≤4 YES ✓ (tight fit!)
    Desk in 6×5: 5≤6, 3≤5 YES ✓
    Both fit in separate regions ✓

    Total room: 70 sq ft. Furniture: 43 sq ft. Usable: 27 sq ft ≥ 5 ✓

    This works! Let me verify all constraints:
    - Side lengths: 10, 9, 6, 5, 4, 4 → all 3–10 ✓
    - Total area: 70 sq ft → 40–80 ✓
    - 2 missing sides, independently solvable ✓
    - Missing side values: 6, 5 → both ≥ 2 ✓
    - Bed fits in 10×4 region ✓
    - Desk fits in 6×5 region ✓
    - Furniture total (43) < room total (70) ✓
    - Usable floor space: 27 sq ft ≥ 5 ✓
    - Positive resolution ✓
    - Room feels room-like: L-shaped room with a smaller bump-out section ✓

Room layout confirmed. Will use in Backbone §1.5 Data Constraints.

Example Set 2: EC Room — L-shaped, 1 missing side, 30–60 sq ft, bookshelf 6×2, dresser 4×3
  Need: L-shape, simpler than lesson room, 1 missing side.
  EC furniture: bookshelf 6×2 (area 12) + dresser 4×3 (area 12). Total furniture: 24 sq ft.

  Proposed EC room:
    Outer bottom: 8 ft
    Left side: 7 ft
    Top-left: 5 ft
    Step down: 7 - 3 = 4 ft
    Top-right: 3 ft (= 8 - 5)
    Right side: 3 ft

    Missing side: 4 ft (vertical step = 7 - 3, vertical direction)
    (Could also hide the 5 ft: 5 = 8 - 3, horizontal direction)
    Pick one: hide the 4 ft (vertical: 7 - 3 = 4)

    Decomposition (vertical cut): 5 × 7 = 35 + 3 × 3 = 9 → total 44 sq ft
    Decomposition (horizontal cut): 8 × 3 = 24 + 5 × 4 = 20 → total 44 sq ft

    Total area: 44 sq ft → 30–60 ✓
    Furniture: 24 sq ft < 44 ✓
    Usable: 20 sq ft ≥ 5 ✓

    Bookshelf 6×2 in 5×7: 6>5 NO; 2≤5, 6≤7 YES ✓
    Dresser 4×3 in 3×3: 4>3 NO; 3≤3, 4>3 NO. Doesn't fit in 3×3.
    Dresser in 5×7: 4≤5, 3≤7 YES ✓. Both items can fit in the 5×7 region.
    Or: Dresser in 8×3: 4≤8, 3≤3 YES ✓ (tight).

    Works ✓.

    Side lengths: 8, 7, 5, 4, 3, 3 → all 3–10 ✓
    1 missing side ✓
    Independently solvable ✓
    Missing value 4 ≥ 2 ✓

EC Room confirmed.

Example Set 3: STRETCH — "Enough area but doesn't fit"
  TVP specifies: Playpen design, 12 sq ft in 5×4 region.
  Factor pairs of 12: 1×12, 2×6, 3×4, 4×3, 6×2, 12×1
  In 5×4 region:
    3×4: 3≤5, 4≤4 ✓ FITS
    4×3: 4≤5, 3≤4 ✓ FITS (same pair, other orientation)
    2×6: 2≤5, 6>4 NO; 6>5 NO → DOESN'T FIT ✓
    6×2: same → DOESN'T FIT ✓
    1×12: 12>5, 12>4 → DOESN'T FIT ✓
    12×1: same → DOESN'T FIT ✓
  At least one fits (3×4) and at least one doesn't (2×6, 1×12) ✓
  TVP constraint satisfied ✓

Status: COMPLETE — all example sets verified.
```

---

## Backbone Self-Check (Task 1 Step 9)

- [x] Every term in Table A "Vocabulary to Teach" appears in §1.2 or §1.3 → Table A says "(consolidation - no new vocabulary)". §1.3 confirms no new vocabulary. §1.2 Must Teach lists reinforcement terms. ✓
- [x] Every term in Table A "Vocabulary to Avoid" → Table A has no Vocabulary to Avoid column populated. §1.3 Terms to Avoid carries forward unit-wide constraints (perimeter, formula, divide, ruler, opposite sides). ✓
- [x] Module Mapping "Notes" — every "Critical:" flag addressed → Notes say "Culminating application. Room and furniture context. Students find missing sides, calculate room area, determine if furniture fits. Multiple valid approaches. Mathematical modeling precursor. OPTIONAL lesson included per Decision 9 - kept standalone." All addressed: room/furniture context (§1.0, §1.2), missing sides (§1.0, §1.5), furniture fitting (§1.0, §1.2), multiple valid approaches (§1.2 Must Teach, §1.5 decomposition options), mathematical modeling (§1.0, §1.1), optional per Decision 9 (§1.1.3, §1.2). No "Critical:" flag in Notes. ✓
- [x] Module Mapping "Question/Test Language" stems in §1.1 or flagged → "Will the bed and desk fit?" and "What is the usable floor space?" both appear in §1.1 Exit Check Tests and Question/Test Language Stems. ✓
- [x] Misconception IDs match database → #7 (Wrong Missing Side Length), #12 (Multiplying All Given Numbers), #11 (Completing the Rectangle), #6 (Overlapping Decomposition) — all match Misconceptions sheet IDs. Context-specific misconception (room/furniture confusion) is correctly labeled as context-specific, not given a global ID. ✓
- [x] Every TVP data constraint appears in §1.5 → Checked: room side lengths 3–10 ✓, total area 40–80 ✓, 1–2 missing sides ✓, independently solvable ✓, values ≥ 2 ✓, bed 7×4 ✓, desk 5×3 ✓, furniture fits ✓, usable floor space ≥ 5 ✓, L and T shapes only ✓, no U-shapes ✓, max 2 furniture in Lesson ✓, all in sq ft ✓, EC different room ✓, EC 30–60 sq ft ✓, EC 1 missing side ✓, playpen 12 sq ft in 5×4 ✓.
- [x] Every conflict in Table C resolved or flagged → 7 conflicts, all resolved (6 cleanly, 1 with Author Flag AF-1). ✓
- [x] Every applicable Important Decision reflected in SP or documented → Decision 1 (unified path) ✓ in §1.0/§1.1. Decision 3 (no grids) ✓ in §1.0, §1.2, §1.5. Decision 5 (no perimeter) ✓ in §1.2, §1.3. Decision 6 (dragging) ✓ in §1.5 Interaction Constraints. Decision 9 (standalone optional) ✓ in §1.0, §1.1, §1.2. Decisions 2, 4, 7, 8 partial/NA as documented in Design Constraints extraction. ✓
- [x] Conceptual Spine Analysis confirms concept placement → "Missing side lengths" introduced L14, developed L14–L15, mastered L15. "Composite/rectilinear figures" introduced L12, developed L13–L14, mastered L15. M14 (L15) is Application/Mastery for these concepts. ✓
- [x] Standards Mapping required vocabulary aligns with §1.3 → 3.MD.C.7.d requires: decompose, composite figure, rectilinear. 3.MD.C.7.b requires: side lengths, multiply, dimensions, length, width. 3.MD.C.5 requires: area, plane figure. 3.MD.C.6 requires: rows, columns, square foot, square meter. All present in §1.3 Assessment Vocabulary or reinforcement list. ✓
- [x] The One Thing references only concepts this module teaches → §1.0 references orchestrating the workflow (no new skills), finding missing sides (M13), decomposing (M11–M12), calculating area (M4+), comparing (M9), and real-world decision-making. All are APPLIED, none are new. ✓
- [x] YAML front matter complete → module_id, title, unit, domain, our_lesson, standard_addressed, primary_toys, status, version, date all present. ✓
- [x] Edit Reconciliation complete → No numbered TVP edits apply to M14. ✓
- [x] Data Constraint Audit complete → Lesson room (70 sq ft), EC room (44 sq ft), playpen stretch all verified. ✓
- [x] Backbone-to-extraction diff → Walked Table B phase-by-phase: Warmup Notice/Wonder ✓ in Section Plan. Lesson Early (missing sides + room area) ✓ in §1.5 progression. Lesson Mid (furniture fitting, 3 sub-steps) ✓ in §1.5. Lesson Late (usable floor space, optional extension) ✓ in §1.5. EC (3 connected problems, NEW room) ✓ in §1.5. Practice (mixed problems, stretch "doesn't fit") ✓ in §1.5. Synthesis (unit capstone, celebration) ✓ in Section Plan. Tool requirements (furniture display, placement MC, state persistence) ✓ in §1.5. Scaffolding (HRS remediation only) ✓ in §1.5. All TVP data constraints ✓ in §1.5.
- [x] Problem/interaction counts cross-checked → TVP: 1 room sustained across Lesson, 3 EC problems, Practice mixed. §1.5 matches. EC.1/EC.2/EC.3 structure from TVP preserved. ✓

**Self-Check Status: PASS** — All items verified. 3 Author Flags (AF-1 dependency chains, AF-2 lesson room dimensions, AF-3 EC room dimensions) surfaced for author review.

---

## Gate Review Log

### Gate 1 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|
| G1-1 | §1.4 | Missing Misconception #5 (Not Multiplying Side Lengths) — low risk at M14 but should be listed given cognitive load creates regression risk | Added as §1.4.5, TERTIARY. Full entry with trigger, rationale, visual cue, prevention. | — |
| G1-2 | §1.3 | "missing side" and "related sides" absent from Assessment Vocabulary despite being core to M14 workflow | Added to Assessment Vocabulary line. Both terms were already in Vocabulary Staging table and §1.2 but missing from the assessment-specific list. | — |
| G1-3 | §1.2 | T-shape scope ambiguous — could read as core figure type alongside L-shapes | Clarified: L-shapes are core (Warmup, Early/Mid, EC). T-shapes appear only in Late extension or Practice. | — |
| G1-SF1 | External | Misconceptions sheet lists #7 surface range as "M14" but should be "M13–M14" since M13 also targets it | Noted in Working Notes maintenance flag below. Not an SP fix — requires spreadsheet update. | — |
| G1-SF2 | §1.1.1 | 2.NBT.B.5 in Standards Cascade is SP-originated, not in Module Mapping | Added italic source note: "SP-added: not in Module Mapping but mathematically prerequisite." | #38 (Source Attribution) |
| G1-SF3 | §1.5 | Room dimensions have repeated value "4" (two sides + bed dimension), creating guide-language ambiguity risk | Added dimension-ambiguity note to Data Constraints with guidance for Task 2 interaction design. | — |
| G1-M1 | §1.0 | One Thing skill chain narrowly cited M11–M13; M14 orchestrates skills from across the full unit (M9 comparison, M4+ calculation) | Broadened §1.0 opening to cite module sources for each skill in the chain. | — |
| G1-M2 | §1.2 | Subtraction decomposition "Must Not Include" lacked source attribution | Added italic source note tracing to TVP M12 additive-only constraint + SP extension rationale. | #38 (Source Attribution) |
| G1-M3 | §1.5.1 | §1.5.1 Composite Figures spec is dense; suggested splitting for readability | Deferred to Task 2 — will consider structural split when drafting interactions. Noted in Task 2 Watch Items. | — |
| G1-M4 | §1.1.3 | MP6 in OUR Lesson Sources is SP-originated, not from TVP | Added italic source note: "SP-originated; not named in TVP but implicit in pronoun-ambiguity constraint." | #38 (Source Attribution) |
| G1-M5 | Working Notes | TVP's alternative Brain Break design for M14 not referenced in SP | Noted below. TVP describes a Brain Break alternative but M14's sustained-context structure makes a mid-lesson break architecturally complex. Defer to Task 2 lesson pacing decisions. | — |

### Gate 2 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|
| G2-1 | §1.7 all dialogue | VO13: Em dashes in Guide/On Correct/Prompt text (15 instances) | Replaced all em dashes with commas, colons, periods, or restructured sentences. | — |
| G2-2 | §1.7 structure | ST11: Required Phrases and Forbidden Phrases appeared after Purpose Frame | Reordered: Required Phrases → Forbidden Phrases → Misconception Prevention → Purpose Frame → Sections. | — |
| G2-3 | 1.2 On Correct | V5: "last time" flagged as session-relative language | Changed to "same as before" — avoids cross-session reference. | — |
| G2-SF1 | 2.1 options, 2.2a options | Distractor values didn't map to stated error patterns (74, 53 implausible; 16 weak diagnostic) | 2.1-D: 74 → 70 (room area grab). 2.1-B: 22 → 11 (addition). 2.1-C added 40 (10×4 cross-contamination). 2.2a-B: 16 → 20 (5×4 cross-contam). 2.2a-D: 53 → 50 (5×10 cross-contam). | — |
| G2-SF2 | §1.7.4 | Late T-shape extension specified in Backbone/TVP but omitted from Lesson without documentation | Added ISF-3 to §1.7.4: T-shape extension deferred to Practice STRETCH. | — |
| G2-SF3 | §1.7.4 | "No incomplete script flags" statement contradicted by deferred vertical decomposition scripting | Rewrote §1.7.4 with three explicit ISF entries (vertical conditionals, Equation Builder sub-steps, T-shape extension). | — |
| G2-M1 | §1.6 WR-4 checklist | "Personalization" mislabeled — student choosing wonder question is Choice/Agency, not Personalization | Fixed label in WR-4 verification item. | — |
| G2-M2 | §1.7 LR-2 checklist | Worked examples satisfaction claim is a stretch for Application module | Added Design Note (LR-2 Worked Examples Departure) as KDD parallel to CRA Departure. Updated LR-2 verification entry. | — |
| G2-M3 | §1.7 all interactions | Options field nested under Student Action rather than as separate bullet-level field | Noted as accepted convention (consistent with M13 SP). No change. | — |
| G2-M4 | 2.3 | [CONCEPTUAL CHECK] not in template's named type list | Changed to [APPLICATION — CONCEPTUAL]. | — |
| G2-M5 | 2.2a-B | Distractor 16 (4×4) has weak diagnostic signal — double error | Changed to 20 (5×4, clean single cross-contamination). Covered in G2-SF1. | — |

### Gate 3 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|

### Gate 4 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|

---

## Maintenance Flags

**SF-1 — Misconceptions Sheet #7 Surface Range:** The Misconceptions sheet in the Module Mapping workbook lists #7 (Wrong Missing Side Length) with a surface range of "M14" only. This should be "M13–M14" since M13 also targets #7 as PRIMARY. This is a spreadsheet maintenance item, not an SP fix. Flag for author to update the Misconceptions sheet.

**M-5 — Brain Break Alternative:** The TVP includes an alternative Brain Break design for M14 (movement-based activity between Lesson sections). The SP does not currently reference this because M14's sustained-context structure (one room across Early/Mid/Late) makes a mid-lesson break architecturally complex — the room state must persist across the break. Defer to Task 2 lesson pacing: if the Lesson runs long, a Brain Break between Mid and Late is the natural insertion point (room state is fully established, furniture fitting is complete, usable-floor-space is a fresh sub-problem).

---

## Task 2 Watch Items

*From Gate 1 author review — items to address during Task 2 (Warmup + Lesson) drafting:*

1. **Step-naming scaffold precision:** ✅ RESOLVED in §1.7. Designed as explicit Guide language only (not visual). Appears at: 1.1 ("Step 1: figure out the room's total area"), 1.5 On Correct ("That's Step 1 done"), 2.1 ("That's Step 2"), 3.1 implicit in operation-contrast framing, 3.2 full three-step recap. Consistent naming throughout. See Design Note at 1.1 and 1.5.

2. **Vertical decomposition branching:** ✅ RESOLVED — Option (b) chosen. System accepts both decompositions. Guide does NOT steer toward horizontal. If student chooses vertical, furniture placement adapts: bed fits in 6×9 (rotated), desk doesn't fit in 4×4 so both pieces go in larger section. Guide acknowledges without penalizing. Design Notes at 1.4, 2.4, and 2.5 document the conditional paths. Full conditional scripting deferred to Gate 3 (see §1.7.4 Incomplete Script Flags).

3. **EC error isolation design:** ✅ RESOLVED in §1.8. System provides correct room area (44 sq ft) if EC.1 is wrong. EC.2 and EC.3 test independently. See Design Note (Error Isolation) at EC.1 and KDD-8.

4. **Synthesis scope as unit capstone:** ✅ RESOLVED in §1.9. 5 interactions covering both M14-specific orchestration reflection (S.3) and unit-wide toolkit celebration (S.2, S.4, S.5). MP4 named in S.4. No M15 bridge — real-life closure. See KDD-9.

5. **Interaction count management:** ✅ RESOLVED. Lesson has 12 interactions (5 Early + 5 Mid + 2 Late). Warmup has 2 interactions. Total W+L = 14. Consolidation applied: 2.2 is multi-step (desk area + total furniture in one interaction rather than two). Late is lean (2 interactions) because the sustained problem naturally wraps up quickly. The 12 Lesson interactions are well above the 6 minimum but justified by the multi-phase problem structure.

*Additional Task 2 notes from Gate 1 triage:*

6. **§1.5.1 structural density:** ✅ RESOLVED. §1.5.1 was not expanded further in Task 2 — interaction-level detail lives in §1.7, not §1.5. The Module Configuration table remains a reference spec; interaction specs are self-contained with their own Visual lines. No split needed.

7. **Dimension-ambiguity in guide language:** ✅ RESOLVED. Convention applied: every reference to "4" specifies object + direction + position. See 1.2 ("the top-right piece is 4 feet"), 1.3 ("the right wall is 4 feet"), and Design Note at 1.2. Bed dimension "4 feet" always prefixed with "the bed's" or "the bed is 7 feet by 4 feet." Tracked in Dimension Tracking table.

---

## Gate 2 Areas to Watch

*From Gate 2 review — not compliance issues, but pedagogical questions for author consideration:*

**ATW-1: Section 3 (Late) operation contrast is stated but not tested.** ✅ RESOLVED — Accept tradeoff. EC.3 tests the skill; the Lesson interaction plants the concept. Adding a conceptual check to Late would push a 12-interaction Lesson to 13 in an already-long optional module.

**ATW-2: No [SELF-CHECK] think-aloud in an orchestration module.** ✅ RESOLVED — Added [SELF-CHECK] to 1.5 On Correct: "70 square feet. That's about the size of a small bedroom, so that checks out." All three tag types now represented: [PLANNING] (1.1), [SELF-CHECK] (1.5), [ATTENTION] (3.1). LR-3 verification updated.

**ATW-3: Interaction 1.5 density.** ✅ RESOLVED — Added 1.5a/1.5b/1.5c sub-step notation with full MC options and Answer Rationale per sub-step, matching the 2.2a/2.2b convention. Script-writer clarity improved.

**ATW-4: Warmup-to-Lesson visual repetition.** ✅ RESOLVED — Keep the Purpose Frame. It does different work than the Warmup bridge (orients to specific task vs. channels curiosity). If timing becomes an issue during piloting, it's the first thing to cut, but don't pre-optimize. Purpose Frame also updated to include "composite figures" naturally ("You've figured out the area of composite figures..."), satisfying the Required Phrases entry for that term early and cleanly.
