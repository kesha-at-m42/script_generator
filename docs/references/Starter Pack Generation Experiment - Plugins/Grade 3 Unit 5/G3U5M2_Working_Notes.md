# G3U5M2 — Working Notes (Migration)

**Module:** Module 2: Naming Unit Fractions
**Date:** 2026-03-30
**Source:** `Grade 3 Unit 5/VPSS/MODULE 2_ NAMING UNIT FRACTIONS — VPSS.WIP.12.18.25.md`
**Output:** `G3U5M2_Starter_Pack.md`

---

## Migration Summary

Module 2 was significantly cleaner than Module 1 at baseline (52 findings vs 147). The legacy VPSS file had excellent pedagogical content, good synthesis structure (5 interactions vs M1's 1), and strong voice quality. The migration was primarily structural reformatting plus creation of two missing sections (§1.8.5 Practice Inputs, §1.10 KDD).

---

## What Was Carried Forward (Preserved As-Is)

1. **§1.0 THE ONE THING** — Core learning objective, critical misconception (#3), success indicator, biggest risk. Minor rewording for template alignment.

2. **§1.1 LEARNING GOALS** — L1 (3.NF.A.1), standards cascade, module bridges (M1→M2→M3). Added L2 from Reframing Tracker, OUR Lesson Sources table.

3. **§1.2 SCOPE BOUNDARIES** — "Must Teach" and "Must Not Include" lists preserved. Added Scope Confirmation Checklist and Same Whole Principle callout.

4. **§1.3 VOCABULARY ARCHITECTURE** — Staging table, Terms to Avoid, assessment vocabulary. Content preserved; formatting aligned to template.

5. **§1.4 MISCONCEPTIONS** — All three misconceptions (#3 PRIMARY, #6 SECONDARY, #8 variant SECONDARY) preserved with trigger behavior, why it happens, visual cue, prevention strategy.

6. **§1.5 TOY SPECIFICATIONS** — Grid Arrays, Circles (NEW with [TOY_INTRO]), Hexagons (familiar). All specifications, constraints, and configuration tables preserved. Added Notion URLs from M1 reference.

7. **§1.6 WARMUP** — All 3 interactions (W.1 pizza hook, W.2 notation matching, W.3 bridge) preserved. Reformatted to full field structure.

8. **§1.7 LESSON** — All 19 interactions across 4 sections preserved:
   - Section 1: L.1.1–L.1.6 (Unit Fraction Vocabulary on Grids)
   - Section 2: L.2.1–L.2.6 (Hexagon Bridge → Circle Introduction)
   - Section 3: L.3.1–L.3.5 (Size Patterns / Inverse Relationship)
   - Section 4: L.4.1–L.4.2 (Consolidation)
   - Required Phrases (6), Forbidden Phrases, Misconception Prevention — all preserved and expanded

9. **§1.8 EXIT CHECK** — All 3 problems (EC.1 Notation Recognition, EC.2 Create Unit Fraction, EC.3 Size Understanding) preserved.

10. **§1.9 SYNTHESIS** — All 5 elements preserved (Opening Frame, S.1 Pattern Discovery, S.2 Representation Transfer, S.3 Real-World Bridge, Metacognitive Reflection, Identity Closure).

---

## What Was Added (New Content)

1. **YAML Front Matter** — Created from scratch per Playbook §3.6. Added module_id, unit, domain, conceptual_spine_cluster (from Reframing Tracker), primary_toys with Notion URLs.

2. **BACKBONE H1 + END OF MODULE H1** — Added structural markers.

3. **§1.8.5 Practice Phase Inputs** — Created from scratch:
   - Practice Phase Overview (purpose, mastery criteria)
   - Distribution Targets: 26-36 problems across 5 types (notation matching 8-10, shading 6-8, size comparison 6-8, real-world 4-6, mixed representation 2-4)
   - Toy Constraints: 60% grids, 20% circles, 20% hexagons (from legacy toy spec guidance)
   - Dimension Constraints (which fractions, shapes, configurations)
   - Available Rectangle Pool (all valid grid configurations)
   - Dimensions Used Tracking (EC dimensions recorded for practice variance)
   - Module-Specific Notes (progression, differentiation, advancement criteria)

4. **§1.10 Key Design Decisions** — Created from scratch, 5 KDDs:
   - KDD-1: Why Circles Introduced in M2 (builds on M1 hexagon radial, prevents shape-specificity)
   - KDD-2: Why "Unit Fraction" Before "Numerator/Denominator" (informal-before-formal principle)
   - KDD-3: Why Hexagon Bridge Precedes Circles (familiar→new scaffolding)
   - KDD-4: Why All Size Comparisons Use Identical Wholes (Same Whole Principle)
   - KDD-5: Why Inverse Relationship Gets Dedicated Section (counterintuitive concept needs time)

5. **Scope Confirmation Checklist** — Added to §1.2 per template.

6. **OUR Lesson Sources table** — Added to §1.1.3 from Reframing Tracker data.

7. **Purpose Frame** — Added to §1.7 before Section 1.

8. **Verification Checklists** — Added/expanded for all 4 phases with proper subsection structure.

---

## What Was Changed (Modified Content)

### Structural Changes
- All headings: Removed bold markers, converted H4→bold inline labels
- All interaction headers: Converted from bold text to H3 markdown with [TYPE LABEL]
- Remediation: 8+ instances changed from "Full L-M-H" to "Pipeline"
- Section transitions: Standardized to "→ **SECTION X COMPLETE.**" format
- EC cognitive types: Changed from `(IDENTIFY)` to `[IDENTIFY]`
- Synthesis task types: Changed from `(Type A)` to `[PATTERN DISCOVERY]`

### Voice Changes
- **Em dashes in dialogue:** ~15 instances replaced with colons, commas, periods, or parentheses
- **Generic praise On Correct:** 5 instances rewritten:
  - "Right! The top number..." → "The top number..."
  - "Right! When you split..." → "The slice from the cake cut into 4..."
  - "Exactly right! That's one of..." → "Smaller. That's one of..."
  - "You got it! The other three..." → "2/3 breaks the pattern..."
  - "Right! One section out of four—" → "One section out of four:"
- **"Exactly!" in Synthesis** → "They're all 1/3:..."
- **"today" reference** → Removed ("Let's find out today" → "Let's find out")
- **Red flag words:** "carefully" → "Take your time"; "understanding" → "deep knowledge"

### Field Structure Changes
- Purpose field: Added to all ~30 interactions (was missing from most)
- Student Action field: Added with explicit type to all assessed interactions
- Correct Answer field: Made explicit and separate from On Correct
- Answer Rationale: Added to key MC interactions with misconception cross-references
- Options field: Added to all MC interactions
- Connection field: Added post-task explanations in Synthesis

### Forbidden Phrases
- Expanded from 5 module-specific items to 10 (6 universal + 4 module-specific)
- Universal items added per Playbook §3.2

---

## Author Flags (Items for Human Review)

1. **EC.2 Multi-Step Structure:** The legacy EC.2 had two sequential prompts (partition circle, then shade). The migrated version keeps this as a single EC.2 interaction rather than splitting to EC.2a/EC.2b. This maintains the pedagogical intent (partition→shade as connected action) but could be reconsidered if assessment scoring needs separate tracking.

2. **Section 3 Duration:** 5 comparison interactions (L.3.1–L.3.5) may push Section 3 to 5-6 minutes on its own. Combined with Sections 1 (5-7 min), 2 (3-4 min), and 4 (2-3 min), total lesson may exceed 16 minutes. The legacy file budgeted 10-14 minutes which seems tight. Current estimate: 15-20 minutes. May need pacing guidance.

3. **Circles Toy Specification:** The legacy file mentions circles support "2, 3, 4, 6, 8" partitions via "LCM snapping system." This is claimed but not verified against the actual Notion toy spec. Recommend confirming circle partitions match the Regular Polygons toy specification.

4. **L.2.3 Circle Introduction:** Legacy has student partitioning the circle (radial cuts from center) during [TOY_INTRO]. But §1.2 Scope says "NO partitioning by students in Module 2." This is an intentional exception for the toy introduction (students need to experience cutting on the new shape once). Documented in legacy Constraints but could create checker confusion. The interaction is marked [TOY_INTRO] to signal this exception.

5. **Synthesis S.1 Uses Non-Unit Fraction (2/3):** The synthesis "Pattern Discovery" task shows 2/3 among unit fractions for a "what doesn't belong" exercise. This is pedagogically sound (it defines unit fractions by contrast) but technically introduces a non-unit fraction visual. This is an observation task, not instruction, so it stays within scope. Flagged for awareness.

---

## Comparison to M1 Migration

| Dimension | M1 | M2 |
|---|---|---|
| Baseline findings | 147 | 52 |
| Final findings | 0 | 0 |
| Synthesis gap | Catastrophic (1 interaction → 5+) | None (5 interactions at baseline) |
| Sections created from scratch | §1.8.5, §1.10 | §1.8.5, §1.10 |
| Voice fixes needed | ~30+ | ~20 |
| Interaction count | 24 | 30 |
| Lesson sections | 3 (C/R/A) | 4 (C-R/R-Bridge/R-A/A) |
| New toy introduction | None | Circles [TOY_INTRO] |

M2 migration was faster and cleaner than M1. The pattern is established: legacy files need (a) structural reformatting, (b) interaction field completion, (c) voice pass, (d) §1.8.5 + §1.10 creation. Expect M3-M12 to follow similar pattern.

---

## Post-Gate 4 Review Changes (Author Feedback)

Six changes applied after initial Gate 4 pass, based on author review:

1. **L.1.5 Distractor Fix:** Replaced "Total number of parts" option (redundant with "Bottom number") with "The shape they're drawn on" — a meaningful surface-feature distractor. Added expanded Answer Rationale explaining each option.

2. **L.1.2 Consecutive Passivity Fix:** Added a confirmation click ("Click on the number that tells us how many equal parts make the whole") to break the L.1.1→L.1.2 consecutive non-interactive sequence. Changed interaction from pure [INSTRUCTION] to include a low-stakes student action. Design Note documents the rationale.

3. **S.1 Scope Exception Design Note:** Added explicit documentation that the 2/3 "breaker" in Pattern Discovery is a deliberate scope exception from §1.2 "Must Not Include." Students observe 2/3 by contrast, not work with it. Prepares for Module 3.

4. **EC.4 Added:** New exit check problem testing the defining feature of unit fractions ("Which one is NOT a unit fraction?"). Shows 1/3 (grid), 1/4 (circle), 2/4 (grid), 1/6 (hexagon). Closes a coverage gap — the "1 on top" definition was tested in Lesson and Synthesis but not in the assessment phase. Uses 2/4 rather than 2/3 to avoid repeating the S.1 distractor exactly. EC problem count: 3→4. Alignment table updated.

5. **W.1 Visual Simplification:** Replaced the 4-grid design (which showed 2/4 in two configurations and 3/4) with a cleaner version: three unit-fraction grids (1/2, 1/3, 1/4) plus one 2/4 distractor. Reduces pre-teaching noise by naturally previewing the "one part shaded" pattern without multiple non-unit fraction distractors. Task prompt changed from "Which shows ONE part shaded?" to "Which shows MORE than one part shaded?" for cleaner identification.

6. **§1.5.1 Orientation Consistency Note:** Added to Grid Arrays Module 2 Usage table: "For size comparisons within a single interaction, use consistent grid orientation (all tall OR all wide) to avoid confounding visual variables."

---

**Document Version:** 03.30.26 (rev 2)

