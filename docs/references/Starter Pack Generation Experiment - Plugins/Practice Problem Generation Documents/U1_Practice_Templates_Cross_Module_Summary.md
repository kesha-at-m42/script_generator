# UNIT 1: Practice Templates — Cross-Module Summary

*Generated from 12 module backbone files (M1–M12). Unit-wide view for coverage validation before template writing.*

---

## 1. Skill × Module Coverage Matrix

Shows which skills are actively templated in each module, with spine status (INT = introduced, PRC = practiced, EXT = extended). Blank = not active.

| Skill ID | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|----------|----|----|----|----|----|----|----|----|----|----|-----|-----|
| **DATA DOMAIN** |
| ReadPicGraph | ✅ INT | PRC | PRC | — | — | — | — | — | — | — | — | — |
| ReadBarGraph | — | — | — | PRC | PRC | EXT | — | — | — | — | — | — |
| CreatePicGraph | — | INT | PRC | — | — | — | — | — | — | — | — | — |
| CreateBarGraph | — | — | INT | PRC | — | EXT* | — | — | — | — | — | — |
| InterpretHalfScale | — | INT | — | EXT | — | — | — | — | — | — | — | — |
| CompareData:ordinal | ✅ INT | PRC | PRC | PRC | emb | emb | — | — | — | — | — | — |
| CompareData:difference | ✅ INT | PRC | PRC | PRC | PRC | EXT | — | — | — | — | — | — |
| CompareData:combination | ✅ INT | PRC | PRC | PRC | emb | EXT | — | — | — | — | — | — |
| SelectScale | — | — | — | — | INT | — | — | — | — | — | — | — |
| SolveMultiStepData | — | — | — | — | — | INT | — | — | — | — | — | — |
| **MULTIPLICATION DOMAIN** |
| IdentifyEqualGroups | — | — | — | — | — | — | INT | PRC | — | EXT | — | — |
| WriteMultExpression | — | — | — | — | — | — | — | INT | — | emb | — | — |
| InterpretMultExpression | — | — | — | — | — | — | — | INT | — | EXT | — | — |
| LearnFactorProducts | — | — | — | — | — | — | — | — | INT | — | — | — |
| SolveMultEquation | — | — | — | — | — | — | — | — | — | INT | — | — |
| BuildArray | — | — | — | — | — | — | — | — | — | — | INT | PRC |
| ApplyCommutative | — | — | — | — | — | — | — | — | — | — | — | INT |

*emb = embedded within another skill's templates, not standalone. EXT* = limited (creation as context-setting, not assessed).*

### Coverage Observations

**Skills with single-module coverage (no reinforcement):**
- SelectScale (M5 only)
- SolveMultiStepData (M6 only)
- LearnFactorProducts (M9 only)
- ApplyCommutative (M12 only)

These skills have their entire tier progression compressed into one module's template set. The backbones already note this for SelectScale, SolveMultiStepData, and LearnFactorProducts. For template generation, these modules need especially careful tier distribution — no "next module" to pick up coverage gaps.

**Skills with strong multi-module arcs:**
- CompareData:difference — 6 modules (M1–M6), INT→PRC→PRC→PRC→PRC→EXT
- ReadPicGraph — 3 modules (M1–M3)
- CreateBarGraph — 3 modules (M3–M6)
- IdentifyEqualGroups — 3 modules (M7, M8, M10)
- BuildArray — 2 modules (M11–M12)

**Domain boundary:** Clean break at M6→M7. No data-domain skill appears after M6; no multiplication-domain skill appears before M7.

---

## 2. Template Pool Sizes

| Module | Est. Pool Size | # Skills Templated | Skills per Template (diversity) |
|--------|---------------|-------------------|---------------------------------|
| M1 | 55–65 | 5 | High variety |
| M2 | 55–65 | 6 | High variety |
| M3 | 55–65 | 6 | High variety |
| M4 | 55–65 | 6 | High variety |
| M5 | 60–75 | 3 (+2 emb) | Moderate (SelectScale dominates at 55%) |
| M6 | 60–75 | 5 (+1 emb) | High variety |
| M7 | 55–65 | 1 | **Low** — single skill, context variety only |
| M8 | 55–65 | 3 | Moderate |
| M9 | 55–65 | 1 | **Low** — single skill, factor-type variety only |
| M10 | 60–75 | 3 (+1 emb) | Moderate (SolveMultEquation dominates at 65%) |
| M11 | 55–65 | 1 | **Low** — single skill, interpretation variety |
| M12 | 65–80 | 2 | Moderate (ApplyCommutative 60%, BuildArray 40%) |
| **TOTAL** | **~710–870** | | |

### Single-Skill Module Challenge

M7, M9, and M11 each need 55–65 templates for ONE skill. Each backbone documents how variety comes from dimensions other than skill diversity:

| Module | Skill | Variety Sources |
|--------|-------|-----------------|
| M7 | IdentifyEqualGroups | 3 context types (bags/boxes/circles), group size range, prompt type progression |
| M9 | LearnFactorProducts | 3 factor types (×2/×5/×10), first-factor range, assessment method (MC/equation builder/pattern ID), turn-around presence |
| M11 | BuildArray | 2 modes (describe/construct), 3 contexts (egg cartons/muffin tins/dots), 2 interpretation directions (rows/columns/both), array size |

---

## 3. Distribution Targets — Dominant Skills by Module

Shows which skill(s) get the largest template allocation per module, highlighting where a single skill dominates.

| Module | Dominant Skill | % | Second Skill | % | Concentration |
|--------|---------------|---|-------------|---|---------------|
| M1 | CompareData:difference (S4) | 28% | ReadPicGraph / ReadBarGraph (S1/S2) | 20% each | Distributed |
| M2 | CreatePicGraph | 35% | InterpretHalfScale | 20% | Moderate concentration |
| M3 | CreatePicGraph / CreateBarGraph | 25% each | CompareData:difference | 18% | Distributed |
| M4 | CreateBarGraph | 30% | InterpretHalfScale | 20% | Moderate concentration |
| M5 | **SelectScale** | **55%** | ReadBarGraph | 20% | **High concentration** |
| M6 | SolveMultiStepData | 35% | CompareData:difference | 22% | Moderate concentration |
| M7 | **IdentifyEqualGroups** | **100%** | — | — | **Single skill** |
| M8 | WriteMultExpression | 40% | InterpretMultExpression | 30% | Moderate concentration |
| M9 | **LearnFactorProducts** | **100%** | — | — | **Single skill** |
| M10 | SolveMultEquation (combined) | 65% | IdentifyEqualGroups | 15% | **High concentration** |
| M11 | **BuildArray** | **100%** | — | — | **Single skill** |
| M12 | ApplyCommutative (combined) | 60% | BuildArray | 40% | Moderate (2 skills) |

**Pattern:** Data-domain modules (M1–M6) have more skill diversity per module. Multiplication-domain modules (M7–M12) tend toward single-skill or high-concentration designs. This reflects the unit structure: data domain reviews and layers skills progressively, while multiplication domain introduces one concept per module in a linear chain.

---

## 4. Verb Distribution by Module

| Module | create | identify | compare | apply | connect |
|--------|--------|----------|---------|-------|---------|
| M1 | 0% | ~45% | ~40% | ~14% | 0% |
| M2 | 35%¹ | 10% | 25% | 30% | 0% |
| M3 | 50%¹ | 10% | 28% | 12% | 0% |
| M4 | 30% | 15% | 25% | 30% | 0% |
| M5 | 0% | 20% | 15% | 55%² | 0% |
| M6 | 8% | 15% | 22% | 50%² | 0% |
| M7 | 0% | 100% | 0% | 0% | 0% |
| M8 | 40%³ | 20% | 0% | 0% | 30%³ |
| M9 | 0% | 100% | 0% | 0% | 0% |
| M10 | 65%⁴ | 15% | 0% | 0% | 15% |
| M11 | 100% | 0% | 0% | 0% | 0% |
| M12 | 40% | 0% | 0% | 0% | 60%⁵ |

*Notes: ¹By template allocation, not just skill count. ²SelectScale and SolveMultiStepData both classified as apply/transfer. ³WriteMultExpression=create, InterpretMultExpression=connect. ⁴SolveMultEquation=create (building equations). ⁵ApplyCommutative=connect.*

### Verb Trend Analysis

**Data Domain (M1–M6):** Balanced verb usage. Create peaks in M2–M4 (graph creation modules). Compare is sustained M1–M6 through CompareData sub-skills. Apply rises in M5–M6 as higher-order skills enter.

**Multiplication Domain (M7–M12):** Verb concentrations are more extreme. Several modules use only 1–2 verbs. This is appropriate — each multiplication module teaches a focused concept, and the verb follows the content:
- M7, M9: identify (recognition/recall)
- M8, M10, M11: create (expression/equation/array construction)
- M12: connect (commutative property relationships)

**Unit-wide verb coverage:** All 5 verbs appear across the unit. Connect is the rarest, appearing only in M8, M10, and M12 — all in the multiplication domain where relational understanding is the teaching target.

---

## 5. Misconception Coverage Matrix

| ID | Name | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|----|------|----|----|----|----|----|----|----|----|----|----|-----|-----|
| 1 | Counting Symbols/Gridlines Instead of Scaling | — | **PRI** | **PRI** | **PRI** | SEC | MON | — | — | — | — | — | — |
| 2 | Scale Means Addition | — | SEC | SEC | — | — | — | — | — | — | — | — | — |
| 3 | Can't Create Fractional Symbols | — | **PRI** | — | — | — | — | — | — | — | — | — | — |
| 4 | Wrong Scale Selection | — | — | — | — | **PRI** | — | — | — | — | — | — | — |
| 5 | Can't Interpolate Bar Heights | — | — | — | **PRI** | SEC | MON | — | — | — | — | — | — |
| 6 | "More Than" Means Add | ADDR | — | — | — | — | **PRI** | — | — | — | — | — | — |
| 7 | Combining Before Comparing | — | — | — | — | — | **PRI** | — | — | — | — | — | — |
| 8 | Rows/Columns Confusion | — | — | — | — | — | — | — | — | — | — | **PRI** | SEC |
| 9 | Array Dimensions as Addition | — | — | — | — | — | — | **PRI** | — | — | — | SEC | — |
| 10 | Groups vs. Size Confusion | — | — | — | — | — | — | **PRI** | **PRI** | — | SEC | SEC | — |
| 11 | Multiplication Only Adds | — | — | — | — | — | — | SEC | SEC | — | — | — | — |
| 12 | Times Means Plus | — | — | — | — | — | — | — | SEC | SEC | — | — | — |
| 13 | Order Changes Answer | — | — | — | — | — | — | — | — | — | — | — | **PRI** |
| 14 | Unknown Must Be Last | — | — | — | — | — | — | — | — | — | **PRI** | — | — |
| 15 | Can't Use Inverse Operations | — | — | — | — | — | — | — | — | — | SEC | — | — |
| 16 | Graph as Picture | **PRI** | MON | MON | MON | — | — | — | — | — | — | — | — |
| 17 | All Data Must Be Used | SEC | MON | MON | MON | — | SEC | — | — | — | — | — | — |
| 18 | Skip Counting Without Meaning | — | — | — | — | — | — | — | — | **PRI** | — | — | — |
| 19 | Equal Sign as "Put Answer Here" | — | — | — | — | — | — | — | — | — | **PRI** | — | — |
| 20 | Memorization Without Relationships | — | — | — | — | — | — | — | — | **PRI** | — | — | — |

*PRI = PRIMARY, SEC = SECONDARY, MON = MONITOR, ADDR = ADDRESSED (has dedicated remediation template).*

### Misconception Coverage Observations

**Every misconception (1–20) has at least one PRIMARY module.** No gaps.

**Single-module PRIMARY misconceptions** (detected/remediated in only one module at primary level):
- #3 (M2 only), #4 (M5 only), #6 (M6 only), #7 (M6 only), #8 (M11 only), #13 (M12 only), #14 (M10 only), #16 (M1 only), #18 (M9 only), #19 (M10 only), #20 (M9 only)

This is expected — most misconceptions are tightly coupled to specific content. The monitor/secondary designations in later modules ensure ongoing detection even after the primary teaching moment.

**Cross-module misconception chains:**
- #1 (Counting Instead of Scaling): PRIMARY in M2–M4, SECONDARY in M5, MONITOR in M6. Strong sustained coverage.
- #10 (Groups vs. Size Confusion): PRIMARY in M7–M8, SECONDARY in M10–M11. Longest multiplication-domain chain.
- #17 (All Data Must Be Used): SECONDARY/MONITOR across M1–M6. Persistent data-domain concern.

---

## 6. Tier Architecture Patterns

### INT Skill Tier Focus

All INT skills follow the same pattern: templates span all 5 tiers, with heaviest allocation at baseline (40–50%) and meaningful coverage at confidence/support (combined 23–32%).

### PRC Skill Tier Focus

PRC skills shift emphasis: lighter at confidence (lower end, 8%), heavier at baseline/stretch. Students have prior exposure, so less scaffolding needed.

### EXT Skill Tier Focus

EXT skills focus on baseline and stretch: students are expected to transfer known concepts to new contexts. InterpretHalfScale in M4 (EXT) and CompareData skills in M6 (EXT) both reflect this pattern.

### Common Scaffolding Patterns Across Modules

| Pattern | Modules Used | Scaffold Type |
|---------|-------------|---------------|
| Key/Scale emphasis pulse | M1, M2, M3 | Visual: key highlights on problem load |
| Helping line (bar → axis) | M1, M4, M5, M6 | Visual: system draws reading line |
| Grouping animation | M2, M3 | Visual: items → groups → symbols |
| Half-symbol/midpoint label | M2, M4 | Visual: halfway position labeled |
| Two-bar/category highlight | M1, M6 | Visual: comparison categories highlighted |
| Ghost gridlines | M3, M4 | Visual: gridlines on → available → off |
| Structure label | M8, M10 | Visual: "Groups: X, Items: Y" on visual |
| Group highlight (sequential) | M7, M8 | Visual: groups highlighted one at a time |
| Row/column highlight toggle | M11, M12 | Visual: toggle between interpretations |
| Preview system | M5 | Interactive: preview graph fit at each scale |
| Step prompt (decomposition) | M6 | MC: "What should you find first?" |
| Rotation animation | M12 | Visual: array rotates 90° |

---

## 7. Cross-Module Open Questions

Issues that span multiple backbones or affect unit-level template design decisions.

### 7.1 Single-Skill Module Template Volume

**Modules affected:** M7, M9, M11 (55–65 templates each for one skill)

Each backbone documents variety sources, but the raw volume is high. Template generation should aim for the lower end of the pool target (~55) for single-skill modules and the upper end (~65–75) for multi-skill modules to avoid redundancy.

### 7.2 Embedded vs. Standalone CompareData

**Modules affected:** M5, M6 (CompareData:ordinal and :combination marked "embedded")

In M5, ordinal and combination are embedded within SelectScale templates. In M6, ordinal is embedded in mixed problem sets. This means their standalone template count is very low (3–4 each). If mastery data later shows students struggle with these sub-skills, they may need promotion to standalone status.

### 7.3 Domain Transition Bridge Templates

**Modules affected:** M6→M7

No backbone currently includes cross-domain bridge templates. The M7 backbone mentions a stretch opportunity ("Show a scale-5 picture graph and ask: How many groups? How many in each group?"). This could be a valuable connection point but is flagged as open.

### 7.4 Property Naming Conventions

**Modules affected:** M12

The M12 backbone notes SME preference for "you can multiply in any order" over "turn-around facts" or "commutative property." The formal name should appear only at stretch/challenge tier. Template generation prompts should enforce this language hierarchy.

### 7.5 Square Arrays as Special Case

**Modules affected:** M12

4×4 rotated is still 4×4. The backbone flags 1–2 templates should surface this. Template generation needs explicit guidance to include square-array edge cases.

### 7.6 Real-World Object Constraints

**Modules affected:** M11

Egg cartons (2×6, 2×3) and muffin tins (2×6, 3×4) have realistic size constraints. Templates using concrete objects should respect these. Template generation needs a constraint table for real-world objects.

### 7.7 Turn-Around Facts Scope

**Modules affected:** M9 (preview), M12 (mastery)

M9 previews turn-around facts at stretch/challenge only. M12 formally teaches the commutative property. Template generation for M9 must NOT treat turn-around as a mastered concept — only an exposure.

### 7.8 = Sign Flexibility

**Modules affected:** M10

Both orientations (3×4=12 AND 12=3×4) taught from baseline tier. The backbone allocates 5% (~3–4 templates) to dedicated = flexibility items. This is a low allocation for an important conceptual shift — worth monitoring.

---

## 8. Readiness for Template Generation

### By Module — Backbone Completeness

| Module | Skill Decomposition | Distribution | Tier Mapping | Misconceptions | Data Constraints | Ready? |
|--------|--------------------:|-------------:|-------------:|---------------:|------------------:|-------:|
| M1 | ✅ Full (5 skills) | ✅ | ✅ | ✅ (3: #16, #17, #6) | ✅ | ✅ |
| M2 | ✅ Full (6 skills) | ✅ | ✅ | ✅ (5: #1, #2, #3, #16, #17) | ✅ | ✅ |
| M3 | ✅ Full (6 skills) | ✅ | ✅ | ✅ (4: #1, #2, #16, #17) | ✅ | ✅ |
| M4 | ✅ Full (6 skills) | ✅ | ✅ | ✅ (4: #1, #5, #16, #17) | ✅ | ✅ |
| M5 | ✅ Full (3+2 emb) | ✅ | ✅ | ✅ (3: #4, #1, #5) | ✅ | ✅ |
| M6 | ✅ Full (5+1 emb) | ✅ | ✅ | ✅ (5: #7, #6, #17, #1, #5) | ✅ | ✅ |
| M7 | ✅ Full (1 skill) | ✅ | ✅ | ✅ (3: #9, #10, #11) | ✅ | ✅ |
| M8 | ✅ Full (3 skills) | ✅ | ✅ | ✅ (3: #10, #11, #12) | ✅ | ✅ |
| M9 | ✅ Full (1 skill) | ✅ | ✅ | ✅ (3: #18, #20, #12) | ✅ | ✅ |
| M10 | ✅ Full (3+1 emb) | ✅ | ✅ | ✅ (4: #14, #19, #15, #10) | ✅ | ✅ |
| M11 | ✅ Full (1 skill) | ✅ | ✅ | ✅ (3: #8, #9, #10) | ✅ | ✅ |
| M12 | ✅ Full (2 skills) | ✅ | ✅ | ✅ (1 PRI: #13; 2 SEC: #8, #9) | ✅ | ✅ |

**All 12 modules are backbone-complete and ready for Stage 2 template generation.**

### Recommended Generation Order

1. **M1** — Already validated (v1.1 pipeline reconciliation complete). Generate first as calibration.
2. **M7** — Bridge module, single skill. Clean test of single-skill template generation.
3. **M2** — High skill diversity, INT skills. Tests multi-skill generation.
4. **M8** — Bidirectional understanding, 3 skills. Tests expression-direction variety.
5. **Remaining modules** in numerical order (M3→M4→M5→M6→M9→M10→M11→M12).

This front-loads the most structurally distinct modules for early validation, then batches the rest.
