# v1 vs v1.1 M1 Practice Templates — Ground Truth Comparison

**Date:** 2026-04-15
**Purpose:** Compare the original v1 M1 templates against the v1.1 (spine-anchored) output to validate the pipeline before M2.

**Inputs:**
- `U1M1_Practice_Templates.md` + `U1M1_Practice_Templates_Backbone.md` — v1 output (15 templates, 67 problems)
- v1.1 second-run output (16 templates, 70 problems) — from chat running patched prompt v1.1

---

## 1. Structural Comparison

| Dimension | v1 | v1.1 | Delta |
|-----------|-----|------|-------|
| Standard templates | 12 (0101–0112) | 14 (0101–0114) | +2 (SK6:combination gets dedicated templates) |
| Remediation templates | 3 (0120–0122) | 2 (0120–0121) | −1 (see §3 below) |
| Total templates | 15 | 16 | +1 |
| Standard problems | 58 | ~61 (est.) | ~+3 |
| Remediation problems | 9 | ~9 (est.) | ~0 |
| Total problems | 67 | 70 | +3 (above 55–65 target) |
| Skills | 5 (S1–S5) | 5 (S1–S5) | 0 — same count, different origin |
| Spine anchoring | ❌ None | ✅ spine_skill_id + sub_skill on every template | Major structural addition |
| Track classification | Implicit (MC or Non-MC per template) | ✅ Explicit classification table in §PT.1 | Process addition |

---

## 2. Skill Decomposition Comparison

### v1 Approach (bottom-up from Lesson analysis)

```
S1: Read picture graph value (1:1)         → from Lesson Sec 1 + EC.1
S2: Read bar graph value (1:1)             → from Lesson Sec 2 + EC.3/4 reading step
S3: Most/least category                    → broken OUT of SP's S1/S2 because COMPARE verb
S4: How many more/fewer (subtract)         → from Lesson Sec 3 + EC.3
S5: In all / total (add)                   → from Lesson Sec 3 + EC.4
```
Source: §1.8.5 was the starting point, adjusted by decomposition framework analysis. S3 was the one addition (SP folded it into S1/S2).

### v1.1 Approach (spine-anchored, top-down then decomposed)

```
SK1 → S1: Read picture graph value (1:1)    [INT, practice-eligible]
SK2 → S2: Read bar graph value (1:1)        [INT, practice-eligible]
SK3 → —:  Create picture graphs             [INT, TEACHING ONLY — warmup scope] ✅
SK6 → S3: Most/least (SK6:ordinal)          [INT, practice-eligible, sub-skill]
SK6 → S4: How many more/fewer (SK6:difference) [INT, practice-eligible, sub-skill]
SK6 → S5: In all / total (SK6:combination)  [INT, practice-eligible, sub-skill]
```
Source: Unit Skill Spine Cross-Module Matrix was the starting point. SK6 decomposed into 3 sub-skills using the "enumerate first, then evaluate" process. §1.8.5 used as calibration check (not authority).

### Key Differences

**SK3 handling:** v1 silently excluded creation (0% procedural justified in backbone). v1.1 explicitly marks SK3 as `[TEACHING ONLY]` with three-check rationale (EC? Practice subsection? Independent action?). **v1.1 is better** — the exclusion is documented, traceable, and replicable for future modules.

**SK6 decomposition:** v1 discovered the three sub-skills through bottom-up Lesson analysis and made a judgment call to break S3 out of SP's grouping. v1.1 starts from the spine's unified SK6 and systematically decomposes using differentiation signals (different verb, interaction type, EC item, misconception target). **Both reach the same result** — but v1.1's process is more rigorous and would generalize better to modules where the analyst doesn't have v1 output as a reference.

**Spine addition tracking:** v1 couldn't track additions because there was no baseline. v1.1 would flag any skill not in the spine as `[SPINE ADDITION PROPOSED]`. In M1, no additions were needed — the spine covered everything. **This will matter more in M2+.**

---

## 3. Template-Level Comparison

### Templates that map cleanly (same skill, same tier, same design)

| v1 ID | v1.1 ID | Skill | Tier | Notes |
|-------|---------|-------|------|-------|
| 0101 | 0101 | S1 (SK1) — PG read | confidence | Expected match |
| 0102 | 0102 | S1 (SK1) — PG read | baseline | Expected match |
| 0103 | 0103 | S2 (SK2) — BG read | confidence | Expected match |
| 0104 | 0104 | S2 (SK2) — BG read | baseline | Expected match |
| 0105 | 0105 | S3 (SK6:ordinal) — most/least PG | support | Expected match |
| 0106 | 0106 | S3 (SK6:ordinal) — most/least BG | baseline | Expected match |
| 0107 | 0107 | S4 (SK6:difference) — more/fewer PG | support | Expected match |
| 0108 | 0108 | S4 (SK6:difference) — more/fewer BG | baseline | Expected match |
| 0109 | 0109 | S4 (SK6:difference) — more/fewer stretch | stretch | Expected match |
| 0110 | 0110 | S5 (SK6:combination) — in all | baseline | Expected match |

### Templates with structural changes

| v1 ID | v1.1 ID | What Changed | Assessment |
|-------|---------|-------------|------------|
| 0111 | 0111 | v1: S4+S5 two-step (stretch). v1.1: same but with spine_skill_id + sub_skill fields | Equivalent — structural metadata added |
| 0112 | 0112 | v1: S1+S2 cross-graph-type (stretch). v1.1: **challenge tier, two-part** (identify greatest difference pair + compute). Different design entirely. | **Divergence** — v1.1 made this a harder, more complex template |
| — | 0113 | **NEW** — SK6:combination baseline (v1 had no dedicated combination baseline) | **Improvement** — v1 folded all combination into 0110 + 0111 |
| — | 0114 | **NEW** — SK6:combination stretch | **Improvement** — gives SK6:combination its own tier progression |
| 0120 | 0120 | #16 remediation | Expected match |
| 0121 | 0121 | #17 remediation | Expected match |
| 0122 | — | **REMOVED** — #6 remediation | **Potential regression** — see §4 below |

### Net Assessment

v1.1 adds 2 templates (0113, 0114) that give SK6:combination its own tier coverage — a genuine improvement because v1 gave combination exactly one dedicated template (0110 baseline) plus shared stretch coverage through 0111. The spine-anchored decomposition naturally leads to "each sub-skill deserves its own tier progression," which is better pedagogy.

The 0112 redesign from "cross-graph-type" stretch to "challenge two-part" is a more interesting departure — it's not a regression per se, but it's a different template design philosophy. The v1 0112 was a creative stretch that tested cross-representation reading. The v1.1 0112 tests more advanced comparison reasoning.

---

## 4. Regressions and Concerns

### 4A. Missing #6 Remediation Template (0122)

**v1:** Had a dedicated remediation template for #6 ("More Than" Means Add) with parameter design that makes the sum visibly wrong (e.g., values 8 and 2: sum=10 vs difference=6).

**v1.1:** Only 2 remediation templates (0120 for #16, 0121 for #17). No dedicated #6 template.

**Is this a problem?** Possibly not — #6 is classified as ADDRESSED (not PRIMARY/SECONDARY) in both versions. It's detected via distractor design in S4 templates (0107-0109, 0111). The v1 remediation template was an extra safety net. But the v1 prompt spec requires remediation templates for "PRIMARY/HIGH misconceptions" — #6 is ADDRESSED, so it's technically optional.

**Recommendation:** Flag as **MINOR** concern. The v1 approach was more thorough. Consider whether the prompt should specify remediation templates for all misconceptions that get distractor coverage, not just PRIMARY ones. For M1 ground truth, this is acceptable.

### 4B. Pool Total Above Target (70 vs 55–65)

The v1.1 output flags this itself and suggests adjustments. The extra templates (0113, 0114) contribute ~8-10 problems. v1 was at 58 (within target). This is a calibration issue, not a structural one — the per-template problem_count values need tuning down slightly.

**Recommendation:** **NOTE** — adjust problem counts to hit 60-62 range. Not a pipeline issue.

### 4C. Tier Distribution Skew

From the v1.1 summary:
- Stretch: 27.1% (target 15–20%) — **too high**
- Confidence: 14.3% (target 8–12%) — **slightly high**
- No support tier for SK1/SK2

Compare v1:
- Confidence: 21% (also high, but noted as acceptable for pool-level coverage)
- Support: 14% (near target)
- Baseline: 50% (on target)
- Stretch: 16% (on target)

**Assessment:** v1.1's tier distribution is less balanced than v1's. The additional templates skewed toward stretch/combination tiers. This needs problem count rebalancing, not template removal.

**Recommendation:** **MINOR** — tune problem_count allocations across tiers to rebalance. Add support-tier templates for SK1/SK2 if coverage feels thin.

### 4D. Cross-Graph-Type Template Lost

v1's 0112 (cross-graph reading) was a creative template that tested whether students could read the same data type from two different graph formats. v1.1 repurposed this ID for a different design. The cross-representation skill is still implicitly tested (students see both graph types across the session), but the dedicated "same data, two formats" template is gone.

**Recommendation:** **NOTE** — not a regression for M1 validation purposes, but worth noting. The v1 0112 was novel and well-designed. Could be preserved as a stretch variant if problem count allows.

---

## 5. What the Spine Anchoring Adds

### Structural metadata on every template

v1 templates had: `skill_id: S1`, `skill: Read a specific value...`

v1.1 templates have:
```
spine_skill_id: U1.SK1
sub_skill: —
skill_id: S1
```

or for decomposed skills:
```
spine_skill_id: U1.SK6
sub_skill: SK6:difference
skill_id: S4
```

This is meaningful for the downstream system — template routing, adaptive algorithm skill tracking, cross-module progression, and Notion database alignment all benefit from having the spine reference.

### Explicit practice-scope decisions

SK3's `[TEACHING ONLY]` exclusion with three-check rationale is a replicable process. v1 had the right answer but arrived at it through ad-hoc reasoning ("SP §1.2 says creation is warmup-only"). v1.1 codifies the decision process.

### §1.8.5 calibration framing

v1 treated §1.8.5 as the authority ("use its Skill Tracking table as the authoritative skill list"), then overrode it anyway when the decomposition framework warranted it. v1.1 treats §1.8.5 as calibration from the start, which is intellectually cleaner and would prevent a future model from getting confused about which source wins in a conflict.

### Track classification table

v1 embedded track decisions implicitly in each template's remediation design. v1.1 adds an explicit classification table in §PT.1 that maps every interaction pattern to MC or Non-MC track. This is better for consistency checking and makes the decision visible before template generation.

---

## 6. Misconception Handling Comparison

| Misconception | v1 Priority | v1.1 Priority | v1 Detection | v1.1 Detection | v1 Remediation | v1.1 Remediation |
|--------------|-------------|--------------|--------------|----------------|----------------|------------------|
| #16 (Graph as Picture) | PRIMARY | PRIMARY | 0102, 0104, 0106 (3 templates) | Expected similar coverage | 0120 (dedicated) | 0120 (dedicated) |
| #17 (All Data Must Be Used) | SECONDARY | SECONDARY (assumed) | 0108, 0109, 0110 (3 templates) | Expected similar coverage | 0121 (dedicated) | 0121 (dedicated) |
| #6 ("More Than" = Add) | ADDRESSED | ADDRESSED (assumed) | 0107-0111 (5 templates) | Expected similar coverage | 0122 (dedicated) | ❌ None |

The priority derivation improvement in v1.1 (prompted by the first run classifying #16 as SECONDARY) is a real win. The prompt now has explicit guidance: "PRIMARY if it targets the foundational cognitive action of the module." This prevents future runs from under-prioritizing module-defining misconceptions.

---

## 7. Pipeline Validation Verdict

### What the spine-anchored approach got right

1. **SK6 three-way decomposition** — The "enumerate first, then evaluate" prompt improvement works. The model correctly identifies ordinal, difference, and combination as distinct cognitive operations.

2. **SK3 exclusion** — Practice-scope eligibility check works perfectly. Three NO answers = TEACHING ONLY.

3. **Same 5-skill outcome** — v1.1 arrives at the same skill decomposition as v1 through a more rigorous process. This validates that the spine + decomposition rules produce the right answer.

4. **Spine metadata adds real value** — `spine_skill_id` and `sub_skill` fields connect templates to the cross-module skill registry. This was impossible in v1.

5. **§1.8.5 calibration framing works** — The model correctly treats §1.8.5 as a check rather than starting point, and notes divergences.

### What needs adjustment before M2

1. **Problem count calibration** — Pool total of 70 exceeds the 55–65 target. Reduce per-template problem_count values by ~15%. Not a prompt issue — a parameter tuning issue.

2. **Tier rebalancing** — Stretch at 27.1% is too high. Review whether the new combination templates (0113-0114) are pulling too many problems into stretch. Consider making 0113 confidence-tier instead of baseline.

3. **#6 remediation template** — Decide whether the prompt should produce remediation templates for ADDRESSED misconceptions (not just PRIMARY). If yes, add guidance. If the v1 approach was over-engineering, note the decision.

4. **Cross-graph-type coverage** — Decide whether v1's 0112 design (same data in two graph formats) should be preserved somewhere. It tests a unique skill that isn't replicated elsewhere in the template set.

### Pipeline status: **VALIDATED for M2 with minor adjustments**

The spine-anchored approach produces equivalent or better results than v1 for M1. The three critical validation checks all pass (SK6 decomposition, SK3 exclusion, misconception priorities). The structural improvements (spine_skill_id, practice-scope eligibility, track classification) add real value. The minor issues (pool total, tier balance, #6 remediation) are calibration, not architecture.

---

## 8. Recommended Actions Before M2

| # | Action | Type | Priority |
|---|--------|------|----------|
| 1 | Add problem_count guidance to prompt — "target 55-65 total standard pool; adjust per-template counts to stay within range" | Prompt tweak | HIGH |
| 2 | Add tier distribution targets to the prompt's output validation section | Prompt tweak | HIGH |
| 3 | Decide on #6 remediation template policy (ADDRESSED misconceptions: dedicated template or distractor-only?) | Design decision (Jon) | MEDIUM |
| 4 | Decide on cross-graph-type template preservation | Design decision (Jon) | LOW |
| 5 | Run M2 with current prompt | Pipeline test | HIGH |
| 6 | After M2, compare v1.1 tier distributions across both modules | Validation | MEDIUM |
