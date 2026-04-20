# U1 Skill Spine ↔ M1 Practice Templates — Reconciliation Record

**Date:** 2026-04-15
**Purpose:** Validate the Unit 1 Skill Spine (Stage 0 output) against the existing M1 Practice Templates (v1 output). Surface design tensions, make scoping decisions, and establish precedent for how spine-to-template mapping works before generating M2.

**Inputs:**
- `Grade 3 Unit 1/U1_Skill_Spine.md` — 15 skills, generated from Toy Flow + Module Mapping
- `U1M1_Practice_Templates.md` — 15 templates (12 standard + 3 remediation), 5 skills (S1-S5)
- `U1M1_Practice_Templates_Backbone.md` — Skill decomposition rationale, distribution targets

---

## 1. Skill Mapping

### Direct Mappings (agreements)

| v1 Skill | v1 Description | Spine Skill | Spine Description | Alignment |
|----------|---------------|-------------|-------------------|-----------|
| S1 | Read picture graph value (1:1) | U1.SK1 | Read values from scaled picture graphs | ✅ Clean match. Spine is broader (includes scaled), v1 is M1-scoped (1:1 only). Spine correctly marks SK1 as INT in M1, PRC in M2-M3. |
| S2 | Read bar graph value (1:1) | U1.SK2 | Read values from scaled bar graphs | ✅ Clean match. Same pattern as S1/SK1. |

### Tension: v1 S3/S4/S5 vs. Spine SK6

| v1 Skill | v1 Description | Verb | Candidate Spine Skill |
|----------|---------------|------|-----------------------|
| S3 | Identify most/least category | compare | SK6 (Compare data across graph categories) |
| S4 | How many more/fewer (subtraction) | compare | SK6 (Compare data across graph categories) |
| S5 | In all / total (addition) | apply | SK6 (Compare data across graph categories) — or SK8 (Multi-step)? |

**What happened:** The spine treats "compare data across graph categories" as one progressive skill (SK6) spanning M1-M6. The v1 templates split this territory into three skills with distinct cognitive operations:

- **S3 (most/least):** Evaluate a relationship across ALL categories to find an extremum. No arithmetic required — visual/ordinal comparison. Tested by EC.2.
- **S4 (how many more/fewer):** Read two specific values, then SUBTRACT to find the difference. Requires arithmetic + "more than means subtract" understanding. Tested by EC.3.
- **S5 (in all/total):** Read two or more values, then ADD. The v1 templates reclassified this from "compare" to "apply" — the student applies the "combine = add" rule, which is transfer, not comparison. Tested by EC.4.

**Why this matters for templates:** Each of these produces fundamentally different template designs:

- S3 templates use click-to-select interaction (0105, 0106) — student clicks the tallest bar or category with most symbols. No MC arithmetic distractors.
- S4 templates use MC with arithmetic distractors where the sum is the primary distractor for Misconception #6 (0107-0109). The remediation path teaches "compare = subtract."
- S5 templates use MC with difference as the inverse distractor (0110). The two-step stretch (0111) chains S5→S4.

If these were one skill (SK6), the template generator would need internal logic to produce three different template designs under one skill umbrella. The tier system would need to encode the cognitive operation type, not just difficulty.

**Why the spine folded them:** SK6's description says "answer comparison questions ('how many more/fewer,' 'how many in all')." The spine sees the progression as one thread: simple comparison (M1) → scaled comparison (M2-M5) → complex comparison without data table (M6). From a *curriculum trajectory* perspective, this is one thread. From a *template design* perspective, it's three.

---

### Tension: SK3 in M1

| Spine Skill | Spine M1 Status | v1 Treatment |
|-------------|-----------------|--------------|
| U1.SK3 (Create picture graphs) | INT (Introduced) | Excluded. 0% procedural. "M1 creation happens in warmup only, not in lesson/EC/practice scope." |

**What happened:** The spine correctly identifies that picture graph creation is introduced in M1 warm-up. But the v1 templates excluded creation from M1's practice scope entirely — and had good reasoning: the SP §1.2 scope boundaries say graph creation is warmup-only for M1, and the EC tests reading, not creation.

**Why this matters:** If Stage 1 naively reads "SK3 active in M1" from the spine's cross-module matrix, it would try to generate creation templates for M1. The spine needs a way to distinguish "introduced in teaching" from "assessable in practice." The cross-module matrix uses INT/PRC/EXT but doesn't encode practice-scope eligibility.

---

### Tension: §1.8.5 Availability

The spine says "§1.8.5 Calibration Data: None available (no G3U1 Starter Packs exist)" for every skill. But the v1 M1 templates used SP §1.8.5 extensively:

- §1.8.5 defined S1-S4 skill tracking with distribution percentages (S1 30%, S2 30%, S3 30%, S4 10%)
- §1.8.5 informed the v1 decomposition (S3 was "folded into S1/S2 by SP" but the v1 templates split it back out)
- The backbone cross-references every skill to §1.8.5

**What happened:** Either the SPs weren't provided as input to the spine generation, or the spine generator couldn't locate them. This means the spine's scoping decisions for M1 were made purely from Toy Flow + Module Mapping, without the SP's practice-specific calibration data.

**Impact assessment:** The spine's M1 skills (SK1, SK2, SK6) are actually *more conservative* than the v1's (S1-S5). The spine produced fewer, broader skills. The §1.8.5 data might have led to more granular decomposition (as it did in v1). But the spine's job is to set the *baseline*, and Stage 1 is where SP enrichment happens — so this may be working as designed.

---

## 2. Template-to-Spine Mapping

How each existing M1 template maps to spine skills:

| Template | v1 Skill | Spine Skill | Notes |
|----------|----------|-------------|-------|
| 0101 — Read PG value (confidence) | S1 | SK1 | ✅ Clean |
| 0102 — Read PG value (baseline) | S1 | SK1 | ✅ Clean |
| 0103 — Read BG value (confidence) | S2 | SK2 | ✅ Clean |
| 0104 — Read BG value (baseline) | S2 | SK2 | ✅ Clean |
| 0105 — Most/least PG (support) | S3 | SK6 | ⚠️ SK6 subsumes S3 |
| 0106 — Most/least BG (baseline) | S3 | SK6 | ⚠️ SK6 subsumes S3 |
| 0107 — More/fewer PG (support) | S4 | SK6 | ⚠️ SK6 subsumes S4 |
| 0108 — More/fewer BG (baseline) | S4 | SK6 | ⚠️ SK6 subsumes S4 |
| 0109 — More/fewer stretch | S4 | SK6 | ⚠️ SK6 subsumes S4 |
| 0110 — In all/total (baseline) | S5 | SK6 (or SK8?) | ⚠️ See Decision 1 |
| 0111 — Two-step (stretch) | S4+S5 | SK6 + SK8? | ⚠️ Two-step → which spine skill? |
| 0112 — Cross-graph reading (stretch) | S1+S2 | SK1 + SK2 | ✅ Clean composite |
| 0120 — Remediation #16 | S1/S2 | SK1/SK2 | ✅ Misconception maps to same skills |
| 0121 — Remediation #17 | S4/S5 | SK6 | ⚠️ Misconception #17 maps to SK6 |
| 0122 — Remediation #6 | S4 | SK6 | ⚠️ Misconception #6 maps to SK6 |

**Observation:** 8 of 15 templates (53%) map to a single spine skill (SK6). This is the core tension. If the adaptive engine routes on spine skills, SK6 becomes a mega-bucket where the engine can't distinguish "student struggles with most/least" from "student struggles with subtraction comparison" from "student struggles with addition combination."

---

## 3. Design Decisions Required

### DECISION 1: Should SK6 be split for template purposes?

**Option A — Keep SK6 unified, use sub-skill tags in templates.**
The spine stays as-is. Stage 1 adds sub-skill annotations (e.g., `SK6.ordinal`, `SK6.difference`, `SK6.combination`) that the template generator and adaptive engine can use for routing. The spine tracks the curriculum thread; the sub-skills track the assessment granularity.

- Pro: Spine stays clean and curriculum-aligned. One thread, one progression.
- Pro: Sub-skills are a template-level concern, not a curriculum-level concern.
- Con: Adds a layer of indirection. Sub-skills need their own naming convention and consistency rules.
- Con: The adaptive engine needs to understand sub-skills, not just skills.

**Option B — Split SK6 into SK6a/SK6b/SK6c in the spine.**
Three skills: SK6a (ordinal comparison — most/least), SK6b (difference comparison — how many more/fewer), SK6c (combination — in all/total). Each gets its own progression row in the cross-module matrix.

- Pro: Template generation is 1:1 with skills. Simpler Stage 1 logic.
- Pro: Adaptive engine routes on skills directly. No sub-skill layer needed.
- Con: Inflates skill count to 17 (ratio goes from 1.25x to 1.42x — still below 1.5x minimum).
- Con: SK6c might violate the folding rule: "in all/total" in M1 has ≤1 dedicated teaching interaction and isn't EC-tested as a standalone item (EC.4 tests it, but it's one item out of four).
- Con: The spine's Scoping Decision 9 already justified the low ratio. Adding skills to fix a template-mapping problem, not a curriculum-scoping problem, feels like tail wagging the dog.

**Option C — Keep SK6 unified, split at Stage 1 per-module decomposition.**
The spine has one SK6. But when Stage 1 runs for M1, it decomposes SK6 into module-level sub-skills (M1.S3, M1.S4, M1.S5) that map to specific template designs. The spine tracks the thread; Stage 1 tracks the assessable actions within that thread for each module.

- Pro: Spine stays clean. Stage 1 does the granular work it was designed to do.
- Pro: Different modules can decompose SK6 differently (M1 has three sub-actions; M6 might have two).
- Con: The "skill" that templates reference isn't a spine skill — it's a Stage 1 decomposition. The `spine_skill_id` field in templates would need a compound format like `SK6:difference`.
- Con: Cross-module analysis of "how is the student doing on comparison?" requires aggregating across sub-decompositions.

**Author decision (2026-04-15): Option C — Keep SK6 unified in spine, decompose at Stage 1.** The spine tracks the curriculum thread; Stage 1 decomposes into sub-skills (SK6:ordinal, SK6:difference, SK6:combination) when distinct cognitive operations require different template designs. Compound IDs preserve the parent reference for cross-module tracking. **Validation needed:** Run patched v1 on M1 to confirm Stage 1 catches the decomposition without manual intervention.

---

### DECISION 2: How should the spine encode practice-scope eligibility?

**The problem:** SK3 is marked INT in M1, but M1 templates correctly excluded creation from practice. The cross-module matrix doesn't distinguish "taught in lesson" from "assessable in practice."

**Option A — Add a practice-scope column to the cross-module matrix.**
Each cell becomes `INT-P` (introduced AND practice-scoped) vs `INT-T` (introduced in teaching only). SK3 in M1 would be `INT-T`. SK3 in M2 would be `INT-P`.

- Pro: Stage 1 can read the matrix directly to know which skills to template.
- Pro: Preserves the spine's completeness (still tracks all teaching, not just assessment).
- Con: Adds complexity to the matrix. Every cell needs a practice-scope judgment.

**Option B — Leave the spine as-is. Stage 1 determines practice scope from source analysis.**
The spine tracks curriculum trajectory. Stage 1's source readiness check determines whether a skill is practice-eligible for that module by checking EC coverage, lesson scope boundaries, and SP §1.2.

- Pro: Spine stays simple. Practice-scope is a Stage 1 judgment call.
- Pro: Practice eligibility can change based on SP enrichment that the spine doesn't have.
- Con: Stage 1 might make inconsistent practice-scope calls across modules without spine-level guidance.

**Author decision (2026-04-15): Option B — Stage 1 determines practice scope from source analysis.** The spine stays simple; Stage 1 checks EC coverage, lesson scope boundaries, and SP §1.2 to determine whether a skill is practice-eligible in each module. **Validation needed:** Run patched v1 on M1 to confirm Stage 1 correctly excludes SK3 from practice scope (warm-up only).

---

### DECISION 3: Should the spine be re-run with SPs as input?

**The evidence:** The spine was generated without SP data. The v1 templates used SP data extensively and made different decomposition choices (particularly S3 as a separate skill, informed by §1.8.5's EC alignment analysis).

**Option A — Don't re-run. SP enrichment is Stage 1's job.**
The architecture doc says SPs are "optional enrichment" for Stage 0 and "OPTIONAL" input for Stage 1. The spine's job is to set the baseline from Toy Flow + Module Mapping. SP-informed adjustments happen in Stage 1 per-module.

- Pro: Validates the architecture's source hierarchy (Toy Flow primary, SP secondary).
- Pro: If the spine is good without SPs, it means Stage 0 works as designed.
- Con: We lose the chance to see if SP data would have changed the spine's scoping decisions.

**Option B — Re-run with SPs to compare, then decide which version to keep.**
A/B test: current spine (Toy Flow only) vs. enriched spine (Toy Flow + SPs). Compare the two and see if SP data materially changes the decomposition.

- Pro: Empirical answer to "does SP data matter for Stage 0?"
- Pro: Low cost — just re-run the skill.
- Con: If the enriched version is better, we've invalidated the architecture's source hierarchy.
- Con: SPs don't exist for every unit. If the spine requires SPs, it can't run ahead of SP generation.

**Option C — Don't re-run, but document that Decision 1 (SK6 split) was likely influenced by the absence of SP data.**
The §1.8.5 analysis is what led v1 to split comparison into three skills. Without §1.8.5, the spine folded them. This is useful context for Decision 1, not a reason to re-run Stage 0.

- Pro: Cheapest option. Uses what we learned without adding work.
- Pro: Keeps the pipeline architecture clean (Stage 0 = Toy Flow + Module Mapping).
- Con: Doesn't give us the empirical comparison.

**Author decision (2026-04-15): Option C — Don't re-run. Document that the SK6 breadth was likely influenced by absence of SP data.** After Starter Packs are available, reconcile in some way (post-SP calibration pass). The M1 test run of the patched v1 will show whether Stage 1's SP enrichment compensates. **Additional note:** The pt-spine plugin should be updated to check Notion or file structure for existing SPs — logged as a tooling improvement.

---

## 4. What the Spine Got Right

Before focusing only on tensions, the spine made several calls that align with or improve on the v1 approach:

1. **SK1/SK2 split (picture vs. bar graph reading)** — v1 agreed. Both produced this split for the same reason (different module trajectories, different cognitive mechanics).

2. **Misconception mapping** — The spine maps Misconceptions #16, #17, #6 to SK1/SK2/SK6, exactly matching the v1 templates' detection strategy.

3. **No creation in M1 practice** — While the matrix shows SK3 as INT in M1, the spine's description correctly notes "M1 — Create 1:1 picture graph with collected data (warm-up; limited scaffolding)" — signaling this is warm-up, not lesson/EC. A careful Stage 1 reader would catch this.

4. **Thread progression tracking** — The spine's INT→PRC→EXT progression for SK1 (M1→M2→M3) and SK2 (M1→M4→M5→M6) gives Stage 1 clear guidance about how each skill develops across modules. v1 didn't have this cross-module context.

5. **Scoping decisions log** — Decisions 1-10 with evidence citations give Stage 1 (and human reviewers) transparent reasoning. v1's decomposition notes were good but less structured.

6. **Component and verb distribution** — The spine's 33% procedural / 40% conceptual / 27% transfer distribution at the unit level is well-balanced. v1 could only assess at the module level (M1 = 0% procedural, 95% conceptual, 5% transfer), which is expected for a review module but doesn't tell you about unit health.

---

## 5. Reconciliation Verdict

**Is the spine ready to anchor M2?** Conditionally yes — after Decision 1 is resolved.

- If SK6 stays unified (Option A or C): Stage 1 for M2 needs clear guidance on how to decompose SK6 into template-level skills. The patched v1 prompt needs a "spine skill decomposition" step.
- If SK6 is split (Option B): The spine gets updated, and Stage 1 maps directly to spine skills. Simpler downstream but inflates the spine.

Decision 2 (practice-scope encoding) can be resolved during the M2 run — it's a process question, not a blocker.

Decision 3 (SP re-run) doesn't need to be resolved now. The M2 run will tell us whether Stage 1's SP enrichment compensates for Stage 0's lack of SP data.

**Recommended next step:** Resolve Decision 1, then run the patched v1 on M2 with the spine as anchor. Compare M2 output quality to M1 output quality. That comparison — not this document — is the real validation of the pipeline.
