# Practice Template Evaluation: U1M1 @ Gate 2

**File:** U1M1_Practice_Templates.md
**Backbone:** U1M1_Practice_Templates_Backbone.md
**Date:** 2026-04-10
**Pipeline:** m42-practice-template-eval v0.1.0 (L1 mechanical + L2 judgment agents)

---

## Layer 1 Summary (Mechanical Checkers)

| Checker | CRIT | MAJ | MIN | NOTE | Status |
|---------|------|-----|-----|------|--------|
| Structure | 0 | 2 | 0 | 0 | ⚠ |
| Voice | 0 | 3 | 12 | 1 | ⚠ |
| Parameters | 0 | 0 | 2 | 7 | ✓ |
| Remediation | 0 | 0 | 3 | 0 | ✓ |
| **TOTAL** | **0** | **5** | **17** | **8** | |

**L1 MAJOR findings:**

- **PS1 (Structure):** §PT.1 and §PT.2 backbone sections not in template file. *Expected — backbone is a separate file per Gate 2 architecture.*
- **PV2 (Voice):** Command language anti-pattern in Medium directions for Templates 0108, 0109, 0110. Phrases like "Stop!", "Ignore" in remediation text.

---

## Layer 2: Source Fidelity — PASS WITH CONDITIONS

All skill IDs, misconception IDs (#16, #17, #6), toy configurations, parameter ranges, and distractor designs trace back to what the backbone documents about the SP. The S3 (most/least) skill decomposition from SP's 4-skill model into 5 skills is justified by Lesson evidence (5 teaching interactions + EC.2 testing).

| ID | Sev | Template | Finding |
|----|-----|----------|---------|
| SF4-B | MINOR | 0101, 0103, 0105, 0107 | Key teaching moment quotes are paraphrased, not verbatim (e.g., "row" vs "row/column") |
| SF3-B | MINOR | 0103, 0106+ | Bar graph axis 0–10 is tighter constraint than backbone documents |
| SF7-B | MINOR | Pool | S5 has no support-tier template; backbone acknowledges gap |

---

## Layer 2: RDR Compliance — PASS WITH CONDITIONS

Structural compliance is strong: all tracks correctly identified, confidence overrides properly applied, post-modeling language fully compliant, no bare "Procedural," all distractor pools ≥4.

| ID | Sev | Template | Finding |
|----|-----|----------|---------|
| RC8 | MINOR | 0101, 0103, 0112 | Distractor tables detect #16 but validator_tag = "—" |
| RC2 | MINOR | 0108, 0109, 0110 | Medium directions 15–18 words, below 20–30 word target |

**Compliance by check:**

- RC1 (Track ID): 15/15 ✅
- RC2 (MC Per-Distractor Medium): 11/11 structurally ✅; word count short on 3
- RC3 (MC Shared Heavy + [Modeling]): 11/11 ✅
- RC4 (Non-MC Full L-M-H): 2/2 ✅
- RC5 (Confidence Light-Only): 2/2 ✅ with [Pedagogical_Override]
- RC6 (Confidence Misconception Exception): 3/3 ✅
- RC7 (Post-Modeling Language): 15/15 ✅
- RC8 (Validator Tags): 12/15 ✅; 3 missing
- RC9 (Per-Step Escalation): 1/1 ✅
- RC10 (Distractor Pool Size): 15/15 ✅

---

## Layer 2: Pedagogy — PASS WITH MAJOR CAVEAT

Scaffolding fade within individual skills is SMOOTH. All Heavy [Modeling] blocks re-demonstrate Lesson techniques specifically. Distractor quality is high — all represent real student thinking. Grade-level appropriateness is excellent.

### Scaffolding Fade Ratings

| Skill | Tiers Covered | Fade Rating | Notes |
|-------|---------------|-------------|-------|
| S1 (read picture graph) | conf, base, stretch | SMOOTH | DT visible→hidden, single→mixed orientation, scaffolds present→absent |
| S2 (read bar graph) | conf, base, stretch | SMOOTH | Same pattern as S1; helping line scaffold at confidence, absent at stretch |
| S3 (most/least) | support, base | ADEQUATE | Only 2 tiers — limited fade range |
| S4 (how many more/fewer) | support, base, stretch | SMOOTH | Full fade with operation-language scaffolding |
| S5 (in all / combine) | base, stretch | ADEQUATE | Only 2 tiers; no support |

### Structural Gaps

| ID | Sev | Finding |
|----|-----|---------|
| PE7 | **MAJOR** | **Two-step operations (S4+S5 combined) only at stretch** — no baseline two-step template. Students cliff-jump from single operations to sequential under stretch-level parameter load. Lesson Phase 3 explicitly models this. |
| PE7 | MINOR | Cross-graph-type reading (S1+S2) only at stretch — Lesson 2.1 explicitly introduces this concept but no baseline template practices it |
| PE1 | MINOR | S3 (most/least) lacks stretch tier despite being a PRIMARY cognitive focus |

### What's Strong

- **PE4 (Key Teaching Moment Grounding):** All 15 templates reference specific Lesson interactions (not generic). Every Heavy [Modeling] block echoes the Lesson's actual teaching technique.
- **PE5 (Distractor Quality):** 100% of distractor types represent real student thinking documented in Lesson EC distractors or Misconception Table. No bare "Procedural" labels.
- **PE6 (Remediation as Re-Teaching):** All 12 MC templates with Heavy [Modeling] re-demonstrate the skill as taught in the Lesson. No generic "here's how to do it" patterns.
- **PE8 (Grade-Level):** All contexts, language, and parameters appropriate for Grade 2.

---

## Cross-Layer Correlations

| L1 Finding | L2 Finding | Merged |
|------------|------------|--------|
| PR8: validator_tag "—" on 0101, 0103, 0112 | RC8: same templates, same issue | Single finding: RC8 MINOR |
| PV2: command language on 0108, 0109, 0110 | RC2: Medium too short on same templates | **Merged**: expanding and softening Medium directions fixes both |

---

## Top Priority Fixes

1. **[MAJOR] Add baseline two-step template (S4+S5)** — Students currently jump from single-operation baseline to two-step stretch with no intermediate staging. The Lesson explicitly models this in Phase 3. The adaptive engine can't compensate for a template that doesn't exist.

2. **[MAJOR → merged L1+L2] Expand and soften Medium directions in 0108, 0109, 0110** — Currently 15–18 words with command patterns ("Stop!", "Ignore"). Expanding to 20–30 words and softening voice addresses both RDR word-count compliance and voice quality.

3. **[MINOR] Add validator tags to 0101, 0103, 0112** — These templates detect #16 in their distractor pools but have validator_tag = "—". Should be `[Validator: Misconception_#16]`.

4. **[MINOR] Add stretch S3 template** — Most/least is a PRIMARY cognitive focus but ends at baseline tier. A stretch variant with 5 categories and close values would test discrimination under complexity.

5. **[MINOR] Add baseline cross-graph template** — Lesson 2.1 explicitly introduces format-switching but no baseline template practices it before stretch.

---

## Verdict

**PASS WITH CONDITIONS**

Zero CRITICALs. The template set is structurally sound, pedagogically grounded, and RDR-compliant in its core architecture.

**Conditions for production readiness:**

- **Mandatory:** Add baseline two-step template (addresses MAJOR scaffolding gap)
- **Mandatory:** Expand/soften Medium directions in 0108, 0109, 0110
- **Recommended:** Add validator tags, stretch S3, baseline cross-graph template

**SME review questions:**

1. Is the S3 decomposition from SP's 4-skill model justified, or should most/least stay folded into S1/S2?
2. Are the confidence-tier parameter values in misconception templates (0120: values to 8, 0122: values to 10) intentionally higher to trigger the misconception, or should they respect the confidence ceiling of ≤6?
3. For the missing baseline two-step template — should it be S4+S5 specifically, or could an S3+S4 combination serve as an intermediate step?
