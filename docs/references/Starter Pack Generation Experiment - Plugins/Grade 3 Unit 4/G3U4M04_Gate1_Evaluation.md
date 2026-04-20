# G3U4 M04 — Gate 1 Evaluation Report

**Module:** M4 — Fact Families & Inverse Relationship
**Gate:** 1 (Backbone: §1.0–§1.5)
**Date:** 2026-04-09
**SP Version:** 2026-04-09
**Evaluator:** sp-gate-eval pipeline (L1 mechanical + L2 agents)

---

## 1. Executive Summary

Gate 1 evaluation of G3U4 M04 (Fact Families & Inverse Relationship) assessed the Backbone draft (§1.0–§1.5) using all 8 L1 mechanical checkers and 3 L2 evaluation agents (gate1-eval, source-fidelity, pedagogy-eval). The Backbone is structurally sound, pedagogically well-designed, and faithfully represents source documents. L1 produced 6 findings (all MINOR known false positives). L2 produced 0 CRITICAL findings, 10 MAJOR findings (9 source-fidelity clarity improvements + 1 pedagogy vocab load concern), and no MINOR findings. All MAJORs are non-blocking improvements recommended before Task 2.

**Overall Verdict: PASS WITH CONDITIONS** — 10 MAJOR items should be addressed before Task 2 scripting begins.

---

## 2. Layer 1 Findings (Mechanical)

### Checker × Severity Matrix

| Checker | CRITICAL | MAJOR | MINOR | Total |
|---------|----------|-------|-------|-------|
| sp_structure_check | 0 | 0 | 5 | 5 |
| sp_vocab_scan | 0 | 0 | 0 | 0 |
| sp_voice_scan | 0 | 0 | 0 | 0 |
| sp_interaction_check | — | — | — | — |
| sp_timing_estimate | — | — | — | — |
| sp_toy_consistency | 0 | 0 | 0 | 0 |
| sp_dimension_track | — | — | — | — |
| sp_module_map_check | 0 | 0 | 1 | 1 |
| **Total** | **0** | **0** | **6** | **6** |

(— = not applicable at Gate 1: no interactions/dialogue to scan)

### All Findings

| ID | Severity | Location | Finding | Disposition |
|----|----------|----------|---------|-------------|
| ST10-1 | MINOR | §1.5 L233 | H4 heading: `#### Module Configuration (M4)` (Arrays) | **Known FP** — §1.5 subsections use H4 for toy sub-tables per M1–M3 convention. Intentional. |
| ST10-2 | MINOR | §1.5 L245 | H4 heading: `#### M4 Guardrails` (Arrays) | Known FP — same pattern. |
| ST10-3 | MINOR | §1.5 L257 | H4 heading: `#### Progression Within M4` (Arrays) | Known FP — same pattern. |
| ST10-4 | MINOR | §1.5 L272 | H4 heading: `#### Module Configuration (M4)` (Eq Builder) | Known FP — same pattern. |
| ST10-5 | MINOR | §1.5 L283 | H4 heading: `#### M4 Guardrails` (Eq Builder) | Known FP — same pattern. |
| MM0-1 | MINOR | §1.1 | Module M04 not found in Module Map/TVP — skipping cross-document checks | **Known FP** — MM0 fires because the .xlsx Module Mapping is not parseable by the L1 checker (docx/xlsx limitation). Module Mapping was manually verified during cross-reference extraction. |

**L1 Assessment:** All 6 findings are known false positives previously documented for M1–M3 (ST10 in §1.5 subsections, MM0 docx limitation). No action required.

---

## 3. Layer 2 Findings (Qualitative)

### 3.1 gate1-eval (Backbone Template Compliance)

**Scope:** 28 checks across §1.0–§1.5 template fields, completeness, internal consistency.

**Result: PASS — 0 findings.**

All 28 checks pass. YAML frontmatter complete, §1.0 One Thing present with CRA stage + critical misconception + biggest risk + success indicator, §1.1 Learning Goals with verbatim source goals + standards cascade + module bridges + OUR lesson sources, §1.2 Scope Boundaries with Must Teach + Must Not Include + construction emphasis + scope confirmation checklist, §1.3 Vocabulary Architecture with assessment vocab + staging by phase + reinforcement plan + terms to avoid + design notes, §1.4 Misconceptions with three entries (PRIMARY/SECONDARY/MONITOR) each with trigger behavior + why it happens + visual cue + prevention strategy, §1.5 Toy Specifications with two primary tools fully specified including module configuration + guardrails + progression + data constraints + interaction constraints.

### 3.2 source-fidelity (Source Document Alignment)

**Scope:** Cross-reference between SP §1.0–§1.5 and source documents (Module Mapping, TVP, Misconceptions sheet, Standards Mapping, M3 SP bridge).

**Result: PASS WITH CONDITIONS — 0 CRITICAL, 9 MAJOR.**

| ID | Severity | Location | Finding | Recommended Fix |
|----|----------|----------|---------|-----------------|
| SF-1 | MAJOR | Working Notes | Equal Groups tool scope conflict between Module Mapping ("Equal Groups, Arrays, or Equation Builder") and TVP (Arrays-only remediation, no backward step to Equal Groups) is not logged in Conflict Log | Add Conflict Log #8 documenting the discrepancy. Resolution: TVP is authoritative (later SME revision). §1.5 correctly omits Equal Groups as a primary tool but §1.2 should note the Module Mapping language explicitly and explain the resolution. |
| SF-2 | MAJOR | §1.5.2 | §1.5.2 says □ and letters are "added" in M4 but doesn't clarify they are FIRST INTRODUCED here (never seen before in division context) | Add explicit statement: "□ and letter unknowns are **first introduced** in M4 (students know letters from Unit 3 M14/15 addition/subtraction context; M4 is their first use in multiplication/division)." |
| SF-3 | MAJOR | §1.2 | "Full range" language in Must Teach items and Data Constraints lacks per-phase specificity | Add parenthetical phase breakdown: "Increasing fact complexity across full single-digit range: factors 2–6, products ≤30 (Early) → factors 2–9, products ≤100 (Mid) → factors 2–10, products ≤100 (Late)." Already present in §1.5.3 Data Constraints table but not in §1.2 scope text. |
| SF-4 | MAJOR | §1.1 | L8 Reframe footnote is useful context but belongs in Working Notes, not the SP body | Move the L8 Reframe block quote from §1.1 to Working Notes (Cross-Reference Table A already contains this information). Replace with a one-line reference: "L8 reframed per SME — see Working Notes." |
| SF-5 | MAJOR | §1.3 | Vocabulary Architecture lists □ as a vocabulary term in the Reinforcement Plan, but □ is a notation/symbol, not vocabulary | Clarify the distinction: □ and letter unknowns are notation conventions, not vocabulary. Consider moving them to a "Notation Staging" sub-section within §1.3 or adding a note: "Listed here for staging purposes; these are notation symbols, not vocabulary terms per se." |
| SF-6 | MAJOR | §1.0 | Success Indicator mentions "verify a division answer using multiplication (check-by-inverse)" but the Module Mapping Notes section places check-by-inverse as an EXTENSION, not a core success criterion | Adjust Success Indicator to distinguish: think-multiplication is core, check-by-inverse is extension. Or: add a note acknowledging the extension status. |
| SF-7 | MAJOR | §1.4 | A4 misconception (associative interference) is listed as MONITOR but its Prevention Strategy is as detailed as the PRIMARY misconception | Trim A4 prevention strategy to monitoring-level detail (2–3 sentences). The current level of detail implies active teaching focus, which contradicts MONITOR status. |
| SF-8 | MAJOR | §1.5.1 | Warmup array configuration says "3×5 = M3 callback" but M3 Synthesis used 4×9=36 as its fresh value, not 3×5 | Verify the intended callback. M3 S1 used 3×5=15 for the initial dual-read. M3 Synthesis S.2 used 4×9=36 as the fresh family. If the callback should be to M3's opening moment (S1), 3×5=15 is correct. If it should be to M3's closing moment (Synthesis), use 4×9=36. Document the rationale either way. |
| SF-9 | MAJOR | §1.3 | Design Note on D7 Revised references "Conflict Log #1 in Working Notes" — verify this conflict log entry exists and is numbered correctly | Verify Working Notes Conflict Log #1 exists with D7 discrepancy. (It does — confirmed during cross-reference extraction.) |

### 3.3 pedagogy-eval (Pedagogical Arc & Scaffolding)

**Scope:** CRA progression design, scaffolding fade curve, vocabulary load, cognitive alignment across planned phases.

**Result: PASS — 0 CRITICAL, 1 MAJOR.**

| ID | Severity | Location | Finding | Recommended Fix |
|----|----------|----------|---------|-----------------|
| PE-1 | MAJOR | §1.3 / Section Plan S1 | Vocabulary density in S1 (Early) is high: "related facts" (NEW) + □ (NEW notation) + vocabulary retrieval for dividend/divisor/quotient all in the same phase. Grade 3 students doing word problem → array construction → dual equation production are already at high cognitive load. | Consider deferring active vocabulary retrieval (dividend/divisor/quotient identification questions) to S2 (Mid), where the construction demand drops (arrays given, not built). S1 would still USE these terms in context but not require explicit identification. This preserves the exposure→retrieval loop (M3 exposure → M4 retrieval) while moving retrieval to a lower-demand phase. |

**Scaffolding Fade Curve:** SMOOTH. The planned progression (S1: construct from word problem → S2: produce from given array → S3: equations only with array on demand) follows a clear fade from maximum scaffolding to minimal. Each phase removes one support layer while preserving access to the prior layer as remediation.

**CRA Arc:** STRONG. The backbone correctly positions M4 as Representational → early Abstract (§1.0 CRA Stage), consistent with the TVP's CONC 50 / PROC 20 / TRANS 30. The array remains available throughout as a concrete anchor but shifts from required (S1) to given (S2) to optional (S3) — a textbook scaffolding fade. The transition to symbolic-only work in S3 is appropriate given M3's foundation.

**Vocabulary Load Assessment:** The total vocabulary introduction in M4 (fact family, related facts, inverse, □, letters) is manageable for Grade 3 given that 3 of 5 items are reinforcement/retrieval rather than genuinely new concepts. The concern is concentration in S1, not total volume.

---

## 4. Cross-Layer Correlations

| Correlated Finding | L1 Source | L2 Source | Underlying Issue | Single Fix |
|--------------------|-----------|-----------|------------------|------------|
| None identified | — | — | L1 findings are all structural false positives unrelated to L2 qualitative concerns | — |

No cross-layer correlations at Gate 1. This is expected — L1 structural checks and L2 qualitative checks target different domains at the backbone stage.

---

## 5. Priority Fix List

Ordered by impact. All are MAJOR severity (no CRITICALs).

| # | ID(s) | Location | What's Wrong | Recommended Fix | Layer |
|---|-------|----------|-------------|-----------------|-------|
| 1 | SF-1 | Working Notes | Equal Groups tool scope conflict unlogged | Add Conflict Log #8: Module Mapping says "Equal Groups, Arrays, or Equation Builder" but TVP specifies Arrays-only remediation. Resolution: TVP authoritative. Add §1.2 note. | L2 |
| 2 | PE-1 | §1.3 / S1 | Vocabulary density in S1 Early too high alongside construction demand | Defer explicit vocabulary retrieval (dividend/divisor/quotient identification) to S2 Mid. S1 uses terms in context only. | L2 |
| 3 | SF-2 | §1.5.2 | □ and letters described as "added" not "first introduced" | Clarify that M4 is the FIRST INTRODUCTION of □ and letters in mult/div context. | L2 |
| 4 | SF-3 | §1.2 | "Full range" lacks per-phase specificity | Add phase breakdown parenthetical to Must Teach scope text. | L2 |
| 5 | SF-6 | §1.0 | Check-by-inverse in Success Indicator but it's an extension per Module Mapping | Distinguish core (think-multiplication) from extension (check-by-inverse) in Success Indicator. | L2 |
| 6 | SF-8 | §1.5.1 | Warmup callback value (3×5) — which M3 moment is it referencing? | Verify and document: M3 S1 opening (3×5=15) vs. M3 Synthesis (4×9=36). | L2 |
| 7 | SF-4 | §1.1 | L8 Reframe footnote is Working Notes material, not SP body | Move block quote to Working Notes, replace with one-line reference. | L2 |
| 8 | SF-7 | §1.4 | A4 MONITOR misconception has PRIMARY-level detail | Trim prevention strategy to 2–3 sentences appropriate for monitoring. | L2 |
| 9 | SF-5 | §1.3 | □ listed as vocabulary when it's notation | Add note distinguishing notation from vocabulary, or create sub-section. | L2 |
| 10 | SF-9 | §1.3 | Conflict Log cross-reference — verify it exists | Confirmed: Conflict Log #1 exists in Working Notes. No action needed. | L2 |

---

## 6. Gate Verdict

### **PASS WITH CONDITIONS**

**Conditions (address before Task 2):**

1. **Add Conflict Log #8** (SF-1) — Equal Groups tool scope. Non-blocking but should be documented for audit trail.
2. **Defer vocab retrieval to S2** (PE-1) — Adjust Section Plan so S1 (Early) uses dividend/divisor/quotient in context but does not require explicit identification. Move identification questions to S2 (Mid) where construction demand is lower.
3. **Clarify §1.5.2 introduction language** (SF-2) — "First introduced" not just "added."
4. **Add phase breakdown to §1.2** (SF-3) — Per-phase factor/product ranges in scope text.
5. **Distinguish core vs. extension in §1.0** (SF-6) — Think-multiplication core; check-by-inverse extension.

**Recommended (may address during Task 2):**

6. **Verify Warmup callback** (SF-8) — 3×5 vs. 4×9 rationale.
7. **Move L8 Reframe to Working Notes** (SF-4) — Keep SP body clean.
8. **Trim A4 prevention strategy** (SF-7) — Match MONITOR level.
9. **Notation vs. vocabulary note** (SF-5) — Clarify □/letter status.
10. **Conflict Log #1 verified** (SF-9) — No action needed.

**Blocking issues:** None. The Backbone is ready for Task 2 scripting after the 5 conditions above are addressed.

---

*Report generated by sp-gate-eval pipeline. L1: 8 checkers (6 findings, all known FP). L2: 3 agents (gate1-eval PASS, source-fidelity PASS WITH CONDITIONS, pedagogy-eval PASS). Total: 0 CRITICAL, 10 MAJOR, 6 MINOR.*
