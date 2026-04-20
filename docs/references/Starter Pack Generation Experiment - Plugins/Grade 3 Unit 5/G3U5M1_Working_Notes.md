# G3U5M1 Working Notes — VPSS Migration

**Module:** M01 — What Makes a Fraction?
**Unit:** Unit 5: Fractions
**Grade:** 3
**Migration Source:** `Grade 3 Unit 5/VPSS/MODULE 1_ WHAT MAKES A FRACTION_ - VPSS.WIP.12.18.25.md`
**Template Target:** MODULE STARTER PACK TEMPLATE.02.04.26.md
**Migration Started:** 2026-03-30

---

## Session Log

### Session 1 — 2026-03-30
- Read all source documents (Cowork Guidance v4.2, Template v2, all 4 playbooks, Structural Skeleton, Pedagogical Justification, Baseline Report)
- Step 0 (Baseline) already completed — see `L1_EVALUATION_REPORT_M01_VPSS_Baseline.md`
- Beginning Step 1 (Backbone) migration

---

## Migration Mapping — Legacy → Template

This replaces the standard Cross-Reference Tables A/B/C since there is no Module Mapping workbook or TVP for Unit 5. The legacy VPSS file is the source of truth.

### Section Mapping

| Template Section | Legacy Section | Status | Notes |
|-----------------|---------------|--------|-------|
| YAML front matter | Lines 6-11 (code-fenced metadata) | NEEDS MIGRATION | Missing: `unit`, `domain`, `primary_toys` with Notion links. Has: `module_id`, `path`, `fractions_required`, `shapes` |
| # MODULE 1: [Title] | Line 1 (H1 title) | EXISTS | Needs subtitle format adjustment |
| # BACKBONE | — | MISSING | Must add structural marker |
| §1.0 The One Thing | Lines 17-25 (§1.0) | EXISTS | Needs CRA Stage field added |
| §1.1 Learning Goals | Lines 29-57 (§1.1) | EXISTS | Has L1, L2, Module Goal, Exit Check Tests, Standards Cascade, Module Bridges. Missing: §1.1.3 OUR Lesson Sources, Question/Test Language Stems |
| §1.2 Scope Boundaries | Lines 61-83 (§1.2) | EXISTS | Has Must Teach, Must Not Include, Same Whole Principle. Missing: Scope Confirmation Checklist |
| §1.3 Vocabulary Architecture | Lines 87-110 (§1.3) | EXISTS | Has Assessment Vocabulary, Staging by Phase table, Terms to Avoid. Complete. |
| §1.4 Misconceptions | Lines 114-150 (§1.4) | EXISTS | Two misconceptions with full detail. Missing: global IDs from misconceptions database (uses #1 shorthand). H4 headings need → H3 |
| §1.5 Toy Specifications | Lines 154-204 (§1.5) | EXISTS | Detailed Grid Arrays + Hexagons specs. Missing: Notion Spec links, Changes from M[N-1], Module Configuration table format, Guardrails table format, Progression table |
| Interaction Constraints | Lines 200-204 | EXISTS | Complete — 4 constraints listed |
| §1.6 Warmup | Lines 212-282 (§1.6) | EXISTS | 3 interactions (W.1, W.2, W.3). Has Purpose, Parameters, Constraints. Missing: Core Purpose expanded format (Key Function, Why This Serves, Test), Warmup Type Rationale, full interaction block format fields |
| §1.7 Lesson | Lines 286-665 (§1.7) | EXISTS | 20 interactions across 3 sections. Substantial content. Missing: Core Purpose + Pedagogical Flow CRA table, Purpose Frame, type labels, CRA stage labels, full block format fields (Purpose, Student Action, Correct Answer on most interactions), Required/Forbidden Phrases BEFORE interactions |
| §1.8 Exit Check | Lines 667-770 (§1.8) | EXISTS | 3 problems (EC.1, EC.2a/b, EC.3). Has Purpose, Parameters, Constraints, Alignment Check. Missing: Transition Frame as interaction block, some block format fields |
| §1.8.5 Practice Phase Inputs | — | MISSING | Must create entirely |
| §1.9 Synthesis | Lines 773-905 (§1.9) | EXISTS but CRITICALLY UNDER-SCOPED in baseline; EXPANDED in current VPSS to 5 tasks + reflection + closure | Now has: Opening Frame, S.1 Size Observation, S.2 Pattern Discovery, S.3 Real-World Reasoning, Metacognitive Reflection, S.4 Generalization, Identity-Building Closure. Needs format migration. |
| §1.10 Key Design Decisions | — | MISSING | Must create from scattered design notes |
| # END OF MODULE marker | — | MISSING | Must add |
| §1.11 Final Formatting Audit | — | MISSING | Must add checklist |

### Content Carried Forward (Preserve As-Is)

These elements contain sound pedagogical design work that should be transplanted without substantive changes:

1. **The One Thing** — Clear, focused: "fractions require EQUAL parts and name them"
2. **Learning Goals** — L1, L2, Module Goal, Exit Check Tests all well-specified
3. **Standards Cascade** — Building On → Addressing → Building Toward correctly mapped
4. **Module Bridges** — From Grade 2 → This Module → To Module 2 correctly stated
5. **Scope Boundaries** — Must Teach and Must Not Include comprehensive and accurate
6. **Same Whole Principle** — Critical constraint correctly documented
7. **Vocabulary Architecture** — Assessment terms, staging by phase, terms to avoid all correct
8. **Misconceptions** — Two misconceptions with trigger behaviors, why it happens, visual cues, prevention strategies
9. **Toy Specifications** — Grid Arrays and Hexagons with detailed specs, cut limitations, supported configurations, eighths constraint
10. **Interaction Constraints** — All 4 digital interaction constraints
11. **All 24 interaction sequences** — The pedagogical progression through partition→shade→name for halves, thirds, fourths, sixths, eighths on grids, then hexagon extension, is sound
12. **Required Phrases** — 5 required phrases listed
13. **Forbidden Phrases** — 4 forbidden phrases with rationale
14. **Cut Orientation Flexibility** — Key teaching moment at fourths
15. **Misconception Prevention** — Both strategies documented
16. **EC Alignment Check** — Maps each EC problem to a Lesson section
17. **Synthesis tasks** — S.1-S.4 are pedagogically sound connection tasks

### Content That Needs Structural Migration (Format Changes Only)

1. YAML front matter: code-fenced → proper YAML, add missing fields
2. H4 headings → H3 headings (7 instances per baseline)
3. Interaction blocks: add missing fields (Purpose, Student Action, Correct Answer, Pattern, On Correct/On Incorrect separation)
4. Remediation: "Full L-M-H" → "Pipeline" (12 instances)
5. Type labels: add to all interaction headers
6. Em dashes in dialogue → comma/colon/period (6 instances)
7. Development tags ("Detail Level:") → remove (4 instances)
8. "Can you..." rhetorical commands → direct prompts (4 instances)
9. Generic praise → specific observable feedback (1 instance in closure)
10. "Today"/"next time" → session-relative language (2 instances in closure)
11. Missing contractions: "we have" → "we've" (2 instances)
12. Red flag word "technique" → "way" or "method" (1 instance)

### Content That Needs Substantive Work

1. **§1.8.5 Practice Phase Inputs** — Create entirely. Decompose learning goals into trackable sub-skills, set distribution targets, document toy constraints for Practice.
2. **§1.10 Key Design Decisions** — Collect scattered design decisions into formal KDD section. Source from: Cut Orientation Flexibility section, Same Whole Principle, Eighths Constraint, Shading Purpose, progressive disclosure rationale, hexagon radial cutting instruction, notation introduction placement.
3. **§1.1.3 OUR Lesson Sources** — Identify which OUR lessons map to this module. Reference Pedagogical Justification doc.
4. **CRA Stage Labels** — Add Concrete/Relational/Abstract/Application labels to all Lesson interactions
5. **Warmup expanded Core Purpose** — Add Key Function, Why This Serves The Concept, and necessity Test
6. **Warmup Type Rationale** — Classify as Binary Choice type per Playbook §4D
7. **Purpose Frame** — Determine if needed or if Warmup bridge is sufficient; document in KDD
8. **Scope Confirmation Checklist** — Add per template requirement
9. **Misconception global IDs** — Verify/assign from misconceptions database

---

## Author Flags

✅ **AUTHOR FLAG 1 (Toy Specs) — RESOLVED:** Notion Spec links now populated for both toys. Grid Arrays → [Grid Arrays/Fraction Grids](https://www.notion.so/ocpgg/Grid-Arrays-Fraction-Grids-2f45917eac528068ac90c4b052736ce0). Hexagons → [Regular Polygons (Fractions)](https://www.notion.so/ocpgg/Regular-Polygons-Fractions-2fa5917eac5280b6b786e44beb952c39). Note: the Notion spec uses the formal name "Regular Polygons (Fractions)" — the SP section heading updated to "Regular Polygons — Hexagons" to bridge both names; body text retains "Hexagons" as the in-context toy name.

✅ **AUTHOR FLAG 2 (OUR Lesson Sources) — RESOLVED:** Confirmed via Lesson Reframing Tracker (Module Mapping sheet): M1 maps to OUR Lessons [1, 2]. SP §1.1 already states "OUR Lesson 1-2" — no change needed.

✅ **AUTHOR FLAG 3 (Misconception Global IDs) — RESOLVED:** Lesson Reframing Tracker (Misconceptions sheet) provides unit-level IDs. M1 addresses Tracker #1 (Equal vs. Unequal Parts) and Tracker #2 (Misidentifying the Whole). SP §1.4 headings and §1.7.4 Misconception Prevention now include "Tracker #N" cross-references alongside section-relative IDs (#1.4.1, #1.4.2).

📋 **AUTHOR FLAG 4 (Purpose Frame) — NOTED:** The Warmup bridge (W.3) teases that equal parts have special names but doesn't orient students to what they'll learn. Recommendation to add a Purpose Frame at Lesson opening stands. Author noted — to be addressed in review pass.

📋 **AUTHOR FLAG 5 (Synthesis Scope) — NOTED:** Baseline report flagged Synthesis as "catastrophically under-scoped" (1 interaction), but the VPSS file contains a full Synthesis section (5 tasks + reflection + closure). Likely expanded after baseline, or baseline parser only detected "IC" interaction. Current content meets Synthesis Playbook requirements — format migration applied, no expansion needed. Author noted.

---

## Dimension Tracking

| Interaction | Toy | Dimensions/Values | Fractions | Notes |
|-------------|-----|-------------------|-----------|-------|
| W.1 | Pre-partitioned rectangles | 2 parts (equal) vs 2 parts (unequal) | — | No toy manipulation |
| W.2 | Pre-partitioned rectangles | 4 equal, 4 unequal, 5 equal | — | Count + equality distractors |
| W.3 | — | Keeps W.2 correct visible | — | Bridge, no student action |
| 1.1 | Grid Arrays | Undivided wide rectangle | — | Toy orientation + eraser demo |
| 1.2 | Grid Arrays | 1×2 or 2×1 | 1/2 | Partition into halves |
| 1.3 | Grid Arrays | From 1.2 | 1/2 | Shade one half |
| 1.4 | Grid Arrays | 1×4, 4×1, 2×2 (all demo'd) | 1/4 | Cut flexibility key moment |
| 1.5 | Grid Arrays | From 1.4 | 1/4 | Shade one fourth |
| 1.6 | Grid Arrays | 1×3 or 3×1 | 1/3 | Partition into thirds |
| 1.7 | Grid Arrays | From 1.6 | 1/3 | Shade one third |
| 1.8 | Grid Arrays | 2×3, 3×2, 1×6, 6×1 | 1/6 | Partition into sixths, strategy demo |
| 1.9 | Grid Arrays | From 1.8 | 1/6 | Shade one sixth |
| 1.10 | Grid Arrays | 2×4 (demo'd) | 1/8 | Partition into eighths, strategy demo |
| 1.11 | Grid Arrays | From 1.10 | 1/8 | Shade one eighth + "more parts = smaller pieces" |
| S1 Transition | Grid Arrays | All 5 shaded grids together | 1/2, 1/4, 1/3, 1/6, 1/8 | Visual summary |
| 2.1 | Grid Arrays | Three partitioned/shaded (1/2, 1/3, 1/4) with notation | 1/2, 1/3, 1/4 | Notation matching drag-and-drop |
| 2.2 | Grid Arrays | 1/6 symbol + multiple bars | 1/6 | Notation reading/selection |
| 3.0 | Hexagons | Center point marked | — | Radial cutting demo, no student action |
| 3.1 | Hexagons | 2 parts | 1/2 | Partition hexagon into halves |
| 3.2 | Hexagons | From 3.1 | 1/2 | Shade one half, cross-shape comparison |
| 3.3 | Hexagons | 3 parts | 1/3 | Partition hexagon into thirds |
| 3.4 | Hexagons | From 3.3 | 1/3 | Shade one third |
| 3.5 | Hexagons | 6 parts | 1/6 | Partition hexagon into sixths |
| 3.6 | Hexagons | From 3.5 (2×2 equivalent) | 1/6 | Shade one sixth, cross-shape connection |
| EC.1 | Grid Arrays | Three arrays (1/3, 1/4, 1/6 partitioned+shaded) | 1/4 tested | Notation recognition (IDENTIFY) |
| EC.2a | Grid Arrays | Fresh undivided rectangle | — | Partition into thirds (CREATE) |
| EC.2b | Grid Arrays | From EC.2a | 1/3 | Shade one third (CREATE) |
| EC.3 | Hexagons | Three hexagons (1/2, 1/3, 1/6 partitioned+shaded) | 1/3 tested | Hexagon recognition (IDENTIFY) |
| S.1 | Grid Arrays | Two same-size: halves (1 shaded) vs fourths (1 shaded) | 1/2 vs 1/4 | Size observation |
| S.2 | Grid Arrays + Hexagons | Four shapes: hex halves, grid thirds, hex thirds, grid 3-unequal | — | Pattern discovery (equal vs unequal) |
| S.3 | Grid Arrays | Three bars: fourths, thirds, sixths (all 1 shaded) | 1/4, 1/3, 1/6 | Real-world reasoning (chocolate bars) |
| S.4 | Grid Arrays + Hexagons | Four shapes: hex 1/2, grid 1/4, hex 1/3, grid 1/6 | 1/2, 1/4, 1/3, 1/6 | Generalization (MC) |

**No cross-phase dimension reuse detected** — each phase uses fresh configurations.

---

## Design Constraints (Unit 5)

Since there is no Important Decisions sheet for Unit 5, these constraints are extracted from the legacy VPSS file and the Pedagogical Justification document:

1. **Same Whole Principle:** All visual comparisons must use identical shapes and sizes. Never compare fractions across different-sized wholes.
2. **Eighths Constraint:** Cannot support 8 horizontal strips on Grid Arrays (would require 7 cuts on short side; max is 5). Scripts must NOT demonstrate or expect 8×1 horizontal configuration.
3. **Progressive Disclosure:** Fractions introduced progressively: halves → fourths → thirds → sixths → eighths (building complexity).
4. **Shading Always Follows Partitioning:** After partitioning, students immediately shade sections to maintain connection between action and fraction naming. Never skip shading after partitioning.
5. **Cut Orientation Flexibility:** Fourths is the key teaching moment for showing multiple valid configurations. After fourths, accept any valid configuration without re-demonstrating.
6. **Notation After Visual Grounding:** Fraction notation (1/4) introduced only AFTER students have physical/visual experience creating equal parts.
7. **No Circles:** Circles are Module 2 content. Module 1 uses grid arrays and hexagons only.
8. **Radial Cutting Instruction Required:** Students need explicit instruction on hexagon radial cuts before attempting hexagon partitioning (different from grid cutting).

---

## Section Plan

### Warmup (2-3 min, 3 interactions)
- **Type:** Binary Choice (per Playbook §4D — recommended for M1-3, concrete simple activation)
- **Hook:** Real-world connection (splitting something into same-sized pieces)
- **W.1:** Hook + First Identification (2 parts, equal vs unequal)
- **W.2:** Second Identification (4 parts, equality + count distractors)
- **W.3:** Bridge to Lesson (teases naming)
- **Engagement Anchors:** Real-world connection (hook) + Choice/Agency (selection tasks)

### Lesson (10-14 min, 20+ interactions across 3 sections)
- **Section 1 — Grid Mastery with Fraction Words (Concrete → Relational):** Partitioning grid arrays into 2, 4, 3, 6, 8 parts; shading; introducing vocabulary through experience
- **Section 2 — Notation Bridge (Abstract):** Matching notation to visuals, reading notation
- **Section 3 — Hexagon Extension (Application):** Transfer partitioning to new shape, demonstrate notation works across representations
- **CRA Mapping:** S1 Early = Concrete, S1 Late = Relational, S2 = Abstract, S3 = Application

### Exit Check (3-4 min, 3 problems)
- EC.1: Notation recognition on grids (IDENTIFY) — tests S2
- EC.2a/b: Partition + shade on grid (CREATE) — tests S1
- EC.3: Hexagon recognition (IDENTIFY) — tests S3
- Cognitive types: IDENTIFY and CREATE only (correct for M1-3 per EC Playbook)

### Synthesis (6-8 min, 5 tasks + reflection + closure)
- Opening Frame
- S.1: Size Observation (more parts = smaller pieces)
- S.2: Pattern Discovery (equal vs unequal)
- S.3: Real-World Reasoning (chocolate bars)
- Metacognitive Reflection
- S.4: Generalization (what's always true about fractions)
- Identity-Building Closure + M2 bridge
- **Task types used:** Pattern Discovery (S.2), Real-World Bridge (S.3), Generalization (S.4), Progressive Challenge element (S.1) — meets minimum 2 different types requirement

---

## Baseline → Gate Progress Tracking

| Metric | Step 0 (Baseline) | Step 1 (Gate 1) | Step 2 (Gate 2) | Step 3 (Gate 4) |
|--------|-------------------|-----------------|-----------------|-----------------|
| Total Findings | 147 | — | — | — |
| CRITICAL | 0 | — | — | — |
| MAJOR | 55 | — | — | — |
| MINOR | 92 | — | — | — |
| NOTE | 0 | — | — | — |
| Interactions Detected | 24 | — | — | — |
| Complete Block Format | 4/24 (17%) | — | — | — |

*Will be filled in as evaluations are run at each gate.*
