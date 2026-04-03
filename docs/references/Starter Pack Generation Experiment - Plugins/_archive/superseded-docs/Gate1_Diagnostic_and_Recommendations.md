# Gate 1 Diagnostic: Why Were the 5 FAILs Missed?

**Date:** 2026-03-24
**Context:** Manual audit of M5, M6, M7 backbones found 5 FAILs that all three Gate 1 evaluations rated PASS. This document maps each FAIL to the Gate 1 check that *should* have caught it, diagnoses why it didn't, and recommends specific changes to the Starter Pack Evaluation Prompt.

---

## FAIL-by-FAIL Diagnosis

### FAIL 1: M5 §1.5 — Changes from M4 table says M4 had grid fading

**What happened:** The backbone's "Changes from M4" table stated: "M4 Behavior: Grids fade progressively per lesson phase." M4 actually kept full grids throughout (Decision #3, M4 SP §1.2 Must Not Include).

**Which Gate 1 check should have caught it:** **A2 (Scaffolding Progression)** — "Does the SP's scaffolding arc match the TVP's Scaffolding Progression?" Also **D5 (Design Constraint Compliance)** — "For each decision in the Important Decisions sheet that applies to this module, verify it is reflected in the SP."

**Why it was missed:** A2 is scoped to check whether *this module's* scaffolding matches the TVP. The "Changes from M[X-1]" table describes the *prior* module's behavior — A2 doesn't instruct the evaluator to verify backward-looking claims about M[X-1]. D5 checks whether Important Decisions are *reflected* in the SP, and Decision #3 IS correctly reflected in M5 (full grids throughout). The error is that the M4 *description* is wrong, not that M5's own behavior violates a constraint.

**Root cause:** No Gate 1 check asks the evaluator to verify the accuracy of "Changes from M[X-1]" descriptions against M[X-1]'s actual SP or the Important Decisions timeline. The checks assume forward-looking fidelity (does THIS module match its sources?) but not backward-looking accuracy (does this module's DESCRIPTION of the prior module match reality?).

---

### FAIL 2: M6 §1.5 — Missing verbatim screen limitation language

**What happened:** TVP has a load-bearing Starter Pack note requiring the guide to explicitly say: "These squares are shrunk to fit on our screen. A REAL square foot is about the size of a floor tile — much bigger than what you see here!" The backbone alluded to a "text note" but didn't include the actual language.

**Which Gate 1 check should have caught it:** **A4 (Key Beats)** — "For each key beat in the TVP, does the SP contain a planned interaction that delivers it?" Also **A5 (SME-Resolved Decisions)** — "For each resolved SME question in the TVP, is the resolution reflected in the SP?"

**Why it was missed:** A4 checks whether a "planned interaction" *delivers* each key beat, but doesn't specify that **load-bearing notes with verbatim language** must be transcribed verbatim. The backbone does acknowledge the screen limitation ("Text note alerts students"), so a superficial check would mark this PASS — the *beat* is delivered, just not with the *required language*. A5 is closer but focuses on SME-resolved questions, not on TVP notes tagged as "load-bearing."

**Root cause:** The evaluation prompt doesn't distinguish between (a) key beats that are satisfied by any interaction that achieves the intent, and (b) load-bearing notes where the TVP specifies *exact language* that must appear in the SP. The current A4 check treats all key beats at the same fidelity level.

---

### FAIL 3: M6 §1.5 — "Too many" calculation wrong (~1,785 vs. ~10,800 sq cm)

**What happened:** The backbone stated the dense cm grid for a 4ft×3ft rectangle would show "~1,785 sq cm." The actual value is ~10,800 sq cm (4ft ≈ 122cm, 3ft ≈ 91cm, 122×91 ≈ 11,102). TVP's own example says "120 cm × 90 cm = 10,800 sq cm."

**Which Gate 1 check should have caught it:** **A3 (Data Constraints)** — "Do the SP's dimension ranges, area ranges, factor limits, and shape types match the TVP's Data Constraints? Are specific values called out in the TVP reflected in the SP?"

**Why it was missed:** A3 checks whether *ranges and limits* match (factors 2-10, products ≤100), not whether *derived calculations* within the SP are arithmetically correct. The evaluator verified that the factor ranges and product limits matched the TVP, but didn't independently compute the cm conversion to verify the stated number. The TVP gives the example number (10,800), but A3 doesn't instruct the evaluator to cross-check computed values in the SP against TVP example values.

**Root cause:** A3 is a *constraint-matching* check, not a *computation-verification* check. When the SP introduces a derived value (like converting feet to centimeters and computing an area), there's no check that says "verify the math." The evaluation prompt assumes the SP author's arithmetic is correct and only checks whether stated constraints align with the TVP.

---

### FAIL 4: M7 — EC labeled "Enrichment Challenge" instead of "Exit Check"

**What happened:** The backbone uses "EC (Enrichment Challenge)" in multiple places. Per established convention (M1-M4 SPs), EC = Exit Check — a mastery assessment, not an enrichment activity. These are pedagogically different concepts.

**Which Gate 1 check should have caught it:** This falls in a gap. **D1 (Vocabulary Completeness)** checks terms from the Module Mapping, not structural/phase terminology. **A1 (Toy List and Configuration)** checks toys, not phase labels. The closest candidate is the **Cross-Module Checks (X1-X3)** in Gate 4, which verify terminology continuity with M[X-1] — but these are Gate 4, not Gate 1.

**Why it was missed:** Gate 1 has no check for *phase/section naming consistency* with prior SPs. The evaluation prompt assumes the author will use correct terminology for structural elements (Warmup, Lesson, Exit Check, Synthesis, Practice). When the author invents a new name for an established phase, no check catches it because the checks are about *content fidelity* (does the SP match the TVP?) not *convention fidelity* (does the SP use the same terms as prior SPs?).

**Root cause:** Gate 1 lacks a terminology/convention consistency check. The Cross-Module Checks (X1-X3) exist in Gate 4 but not in Gate 1. Since Gate 1 is the first evaluation pass, terminology errors propagate through the entire drafting pipeline before being caught.

---

### FAIL 5: M7 — Practice reverse problems accepted silently (M7 vs. M8 conflict)

**What happened:** TVP M7 Practice says "50% forward, 50% reverse." TVP M8's learning goal introduces reverse reasoning as NEW. The backbone transcribed the M7 TVP faithfully without noticing the inter-module conflict. This needed an Author Flag.

**Which Gate 1 check should have caught it:** **A8 (Transition Notes)** — "Do §1.1.2 Module Bridges match the TVP's transition sections?" This is the closest, but A8 checks whether the *bridge statements* match, not whether the *content planned for this module* conflicts with the *next module's claims of novelty*.

**Why it was missed:** All A-section checks are single-module scoped. They verify that M[X]'s SP matches M[X]'s TVP section. They don't cross-reference M[X]'s content against M[X+1]'s learning goals in the TVP. The evaluator would need to read BOTH the M7 TVP section AND the M8 TVP section simultaneously to notice this conflict — and no check instructs them to do so.

**Root cause:** Gate 1 has no *inter-module content consistency* check. A8 checks transition *language*, not whether content planned for M[X] undermines M[X+1]'s novelty claims. The evaluation prompt assumes the TVP is internally consistent across modules. When it isn't, the SP author is expected to catch the conflict — but the Gate 1 evaluator has no instruction to verify this.

---

## Summary of Root Causes

| Root Cause | FAILs Affected | Category |
|------------|---------------|----------|
| No check for accuracy of "Changes from M[X-1]" descriptions | FAIL 1 | Backward-looking verification gap |
| No distinction between key beats (intent) vs. load-bearing notes (verbatim) | FAIL 2 | Fidelity granularity gap |
| No computation verification for derived values | FAIL 3 | Arithmetic verification gap |
| No phase/convention naming consistency check in Gate 1 | FAIL 4 | Terminology consistency gap |
| No inter-module content consistency check | FAIL 5 | Cross-module verification gap |

---

## Recommended Changes to Starter_Pack_Evaluation_Prompt.md

### Change 1: Add check A10 — Changes from M[X-1] Accuracy

**Where:** Section A (Source Fidelity), after A9

**Proposed text:**

```
### A10. Changes from M[X-1] Accuracy
- If §1.5 includes a "Changes from M[X-1]" table, verify each claim about M[X-1]'s behavior:
  - Against the M[X-1] SP (if available) — especially §1.5 Toy Specs and §1.2 Must Not Include
  - Against Important Decisions that constrain M[X-1]'s behavior (e.g., grid fading sequence, CRA stage assignments)
- Any M[X-1] description that contradicts M[X-1]'s own SP or the Important Decisions → FAIL
- If M[X-1] SP is not available, verify against Important Decisions only and FLAG any claims that cannot be verified
```

**Rationale:** The "Changes from M[X-1]" table is a high-value, high-risk element. It's the first place a downstream reader (content author, tool designer) will look to understand what's different. An error here propagates into implementation. This check is cheap (the evaluator already has the Important Decisions and M[X-1] SP in their document list) and catches a class of error that's invisible to all current checks.

---

### Change 2: Amend A4 to distinguish verbatim load-bearing notes

**Where:** Section A, check A4 (Key Beats)

**Current text:**
> For each key beat in the TVP, does the SP contain a planned interaction that delivers it? Is the key beat's essential interaction preserved in the Section Plan?

**Proposed revised text:**

```
### A4. Key Beats
- For each key beat in the TVP, does the SP contain a planned interaction that delivers it?
- Is the key beat's essential interaction preserved in the Section Plan?
- **Verbatim check:** For any TVP note explicitly tagged as "load-bearing," "Starter Pack note," or containing specific script language (dialogue in quotes), verify the SP includes the verbatim language — not just the intent. Paraphrases of load-bearing notes → FAIL.
```

**Rationale:** The TVP uses specific tags ("Starter Pack note," "load-bearing") to signal that exact language must carry through. The current check treats all beats equally, allowing paraphrases to pass. The amendment adds a fidelity tier: normal beats need intent-matching; tagged beats need verbatim transcription.

---

### Change 3: Amend A3 to include computation verification

**Where:** Section A, check A3 (Data Constraints)

**Current text:**
> Do the SP's dimension ranges, area ranges, factor limits, and shape types match the TVP's Data Constraints? Are specific values called out in the TVP reflected in the SP?

**Proposed revised text:**

```
### A3. Data Constraints
- Do the SP's dimension ranges, area ranges, factor limits, and shape types match the TVP's Data Constraints?
- Are specific values called out in the TVP reflected in the SP?
- **Computation check:** For any derived value in the SP (unit conversions, computed areas, ratios, or counts that result from applying constraints), verify the arithmetic is correct. Cross-check against TVP example values where available. Incorrect computations → FAIL.
```

**Rationale:** When the SP introduces computed values (like converting 4ft × 3ft to square centimeters), an error in arithmetic propagates into tool design and instruction. This is a ~30-second verification per derived value and catches a class of error that's otherwise invisible until implementation.

---

### Change 4: Add check A11 — Phase and Convention Terminology

**Where:** Section A, after the new A10

**Proposed text:**

```
### A11. Phase and Convention Terminology
- Verify that all structural phase labels in the SP (Warmup, Lesson, Exit Check, Practice, Synthesis) match the established naming conventions from the Module Starter Pack Template and prior SPs
- Check for renamed, invented, or conflated phase labels (e.g., "Enrichment Challenge" for "Exit Check," "Assessment" for "Exit Check," "Activity" for "Lesson")
- If M[X-1] SP is available, verify terminology is consistent across both SPs
- Incorrect or invented phase labels → FAIL (these propagate into implementation and create confusion across the production pipeline)
```

**Rationale:** Phase labels are structural vocabulary — they're used by content authors, tool designers, and the Guide script system. When a backbone invents a new label for an established phase, everyone downstream is confused. This check is trivial (scan headers and phase references against template) and catches a class of error that no current check addresses.

---

### Change 5: Add check A12 — Inter-Module Content Consistency

**Where:** Section A, after A11

**Proposed text:**

```
### A12. Inter-Module Content Consistency (if adjacent module TVP sections are available)
- For any content planned in M[X]'s Practice, EC, or late phases, check whether M[X+1]'s learning goals claim that same content as NEW or INTRODUCED
- If M[X] plans substantial practice of a skill that M[X+1] claims to introduce, this is a source document conflict → FLAG with Author Flag recommendation
- Specifically check: Does M[X]'s Practice or EC include problem types, reasoning modes, or skill applications that M[X+1]'s learning goal describes as novel?
- This check requires reading both M[X] and M[X+1] TVP sections. If M[X+1] TVP is not available, note which checks cannot be completed.
```

**Rationale:** The TVP is a multi-module document written by different authors or at different times. Inter-module consistency isn't guaranteed. When the SP author transcribes M[X]'s TVP faithfully, they may not notice that M[X+1]'s TVP contradicts it. This check is the cheapest place to catch these conflicts — before they're built into detailed instructional designs.

---

## Implementation Priority

| Change | Effort | Impact | Priority |
|--------|--------|--------|----------|
| **Change 3** (Computation check on A3) | Low — one sentence amendment | High — catches factual errors | **Do first** |
| **Change 2** (Verbatim check on A4) | Low — one bullet amendment | High — catches missing load-bearing language | **Do first** |
| **Change 4** (A11: Phase terminology) | Low — new short check | High — prevents pipeline-wide confusion | **Do first** |
| **Change 1** (A10: Changes from M[X-1]) | Medium — new check, requires M[X-1] SP | Medium — catches backward-looking errors | **Do second** |
| **Change 5** (A12: Inter-module consistency) | Medium — requires reading adjacent TVP sections | Medium — catches source conflicts | **Do second** |

---

## Broader Observation

The 5 FAILs share a pattern: they're all **cross-referencing errors** — cases where the SP's content needs to be verified against something *other than* the direct TVP section for this module. The current Gate 1 checks are excellent at single-module, forward-looking verification (does M[X]'s SP match M[X]'s TVP?). They're weak at:

1. **Backward-looking verification** — does M[X]'s description of M[X-1] match reality?
2. **Cross-document computation** — are derived values arithmetically correct?
3. **Convention enforcement** — does M[X] use the same structural terms as M[X-1]?
4. **Forward-looking consistency** — does M[X]'s content conflict with M[X+1]'s novelty claims?

The recommended changes address each of these gaps without significantly increasing evaluation time. The computation and verbatim checks add ~2-3 minutes per evaluation. The cross-module checks require the evaluator to read adjacent TVP sections, adding ~5 minutes.

---

**END OF DIAGNOSTIC**
