# WORKING NOTES — G3 Unit 2 Module 1

*Process artifacts retained for reference during drafting and review. Not part of the Starter Pack.*

## SOURCE HIERARCHY (for Starter Pack drafting)

**TVP (Tool Flow) > Module Mapping > Notion Spec**

The TVP is the upstream authority for Starter Packs. The Notion Spec describes what a toy *can* do; the TVP specifies what it *does* in each module. When they conflict, the TVP wins for Starter Pack purposes.

---

## CONFLICT LOG

```
CONFLICT 1:
Field: Scaffolding of Visuals / Pattern Blocks
Module Mapping says: "Pattern blocks for informal covering"
TVP says: "Skip pattern blocks, go directly to unit square tiles. Confirmed by SME."
Resolution: FOLLOW TVP. SME resolved this. Module Mapping was not updated.
Pattern blocks do NOT appear in the SP.

CONFLICT 2:
Field: Scaffolding of Visuals / Counter
Module Mapping says: "Counter showing square units"
TVP says: "Counter removed. Students count tiles themselves."
Notion Spec says: Counter is "REMEDIATION ONLY — guide-activated"
Resolution: FOLLOW TVP + NOTION SPEC. Counter is NOT a standard scaffold.
Available only as guide-activated remediation tool for students who demonstrate
repeated inability to track running count (2+ miscounts on consecutive problems
where tiling is correct but stated area is wrong). NOT available during exit checks.
Document in SP §1.5 and flag as KDD.

CONFLICT 3:
Field: Notes / Activities described
Module Mapping says: "comparing shapes by cutting, overlaying, pattern blocks"
TVP says: Visual comparison via Plane Figures (display only), then tiling with Unit Square Tiles
Resolution: FOLLOW TVP. Module Mapping describes the OUR curriculum's physical activities.
The digital adaptation uses Plane Figures for comparison (no cutting/overlaying).
The TVP is the downstream digital design.

CONFLICT 4:
Field: Comparison set size / Shapes per comparison
Plane Figures Notion spec (Question Constraints) says: "Shapes per comparison: 2 (paired comparison)"
TVP says: "Authored comparison sets, 3 shapes labeled A, B, C per set"
Handwritten TVP sketches show: 3 shapes per set, labeled A, B, C, with "Same Space" option
Resolution: ⚠️ FLAG FOR AUTHOR. The TVP and handwritten sketches consistently use
3 shapes per set (A, B, C) with 4 MC options (A, B, C, "They cover the same space").
The Plane Figures spec constraint table says 2. The spec appears to have been written
before the TVP finalized the 3-shape design. RECOMMEND: Follow TVP (3 shapes per set)
and update Plane Figures spec. But need author confirmation.

CONFLICT 5:
Field: Vocabulary bridging term "square tiles"
Module Mapping says: "Critical: squares called 'square tiles' to emphasize measurement purpose."
TVP says: Vocabulary introduced as "Each tile is one SQUARE UNIT."
Resolution: Both can coexist. "Square tiles" is the informal bridging term used before
formal vocabulary. "Square unit" is the formal term introduced after the tiling experience.
Document the staging: "square tiles" (informal, used during tiling) → "unit square" / "square unit"
(formal, introduced mid-lesson). This aligns with vocabulary staging rules (informal before formal).

CONFLICT 6:
Field: M1 Gap/Overlap handling
TVP says: "Semi-freeform placement with immediate overlap feedback (visual color change + audio cue). Same tiling behavior as M2 — consistent interaction across all tiling modules."
Notion Spec (Unit Square Tiles) says: M1 — Gaps: Allowed (no feedback); Overlaps: Allowed (no feedback)
Resolution: FOLLOW TVP (corrected after author review). The TVP is the upstream authority
for Starter Packs. The mechanical overlap feedback is always on — students see when tiles
overlap. The conceptual rules (why gaps/overlaps produce wrong counts) aren't taught until M2.
The Notion Spec describes capability; the TVP specifies module behavior.

CONFLICT 7:
Field: Tile supply mode
TVP says: "Counter available as scaffold" (implies unlimited or sufficient tiles always present)
Notion Spec says: Early activities = exact match (bank has exactly the tiles needed);
Mid-Late = modest surplus (more tiles than needed)
Resolution: FOLLOW NOTION SPEC. The progressive supply mode (exact → surplus) is
pedagogically designed. Document in §1.5.
```

---

## SECTION PLAN

**Warmup (3-5 min):** Prior knowledge activation via visual comparison of plane figures. 2 authored comparison sets (triangles, then mixed polygons). Students select which covers more space from 3 shapes (A/B/C) or "Same Space." Quick success, builds confidence, activates informal "which is bigger" reasoning. Bridge teases that "bigger" isn't always what it seems.

**Lesson Section 1 — Escalating Comparison (3-4 min):** 2 more comparison sets (parallelograms, then rectangles). Difficulty escalates. Set 3 introduces the "taller has less area" counterexample — key misconception surface. Set 4 creates genuine visual uncertainty with rectangles of different proportions. The "close call" motivates measurement: "Our eyes can trick us. We need a TOOL." Major pedagogical move: creating the need for measurement before introducing the tool.

**Lesson Section 2 — Tiling Introduction (5-7 min):** Unit Square Tiles introduced with guide demonstration. Students drag tiles onto rectangular shapes. First tiling is guided (worked example with think-aloud), then 1-2 more with decreasing support. Vocabulary introduced AFTER first tiling experience: "square tiles" → "unit square" / "square unit" → "area." Key pedagogical move: vocabulary staging after visual experience.

**Lesson Section 3 — Independent Tiling (5-7 min):** Student tiles 4-5 shapes independently. Rectangles first, then 1-2 L/T shapes. States area in square units each time. No structured counting expected — one-by-one is appropriate. Tile supply shifts from exact to surplus. No decomposition guidance on non-rectangular shapes.

**Exit Check (3-5 min):** 3 problems testing tiling + counting. Rectangles only. Student tiles shape → counts → states area in square units. Cognitive types: CREATE (tiling) and IDENTIFY (stating area). Some partially pre-tiled problems as SUPPORT tier.

**Synthesis (5-7 min):** Callback to warm-up comparison — now verify with tile measurement. "Earlier we GUESSED. Now we can MEASURE." Vocabulary consolidation. Why square tiles? (square vs. circular tiles illustration). Bridge to M2: preview a "bad" tiling with gaps/overlaps.

---

## MODULE MAPPING FLAGS (Stale Entries)

- ⚠️ Module Mapping Notes mention "pattern blocks for informal covering" — stale after SME decision.
- ⚠️ Module Mapping Notes mention "cutting, overlaying" — reflects OUR curriculum, not digital adaptation.
- ⚠️ Module Mapping says "Critical: squares called 'square tiles'" — TVP doesn't use this term in vocabulary beat. Staged in §1.3.
- ⚠️ Counter scaffold: Module Mapping lists it; TVP removed it; Notion spec has it as remediation-only. Reconciled.
- ⚠️ Columns N–AA in the Module Mapping are empty for M1.

---

## TOY SPEC UPDATES TO TRACK

1. **Plane Figures — Shapes per comparison:** Spec says 2; TVP says 3. Update spec to 3 after author confirmation.
2. **Unit Square Tiles — Counter:** Spec says "remediation only, guide-activated." Confirm this matches M1 implementation (counter NOT available in EC).
3. **Unit Square Tiles — Overlap feedback:** Notion Spec says M1 has no overlap feedback. TVP says overlap feedback is always active. TVP wins — confirm Notion Spec update needed.
