# Vocabulary Moment Analysis: App (Unit 5) vs Starter Packs (Unit 2)

**Date:** April 3, 2026
**Claim tested:** "The app does a much better job at vocabulary moments than the Starter Packs, especially for Unit 1."
**Data sources:** 12 Unit 5 app JSON files (lesson, warmup, synthesis per module), 11 Unit 2 Starter Packs (no Unit 1 SPs available for comparison)

---

## Verdict: The claim is partially correct — but the gap is about *mechanism and density*, not pedagogical sequencing.

The SPs actually have **better vocabulary sequencing** than some app modules (clearer CRA staging, explicit causal chains). But the app has three capabilities the SPs completely lack, and those capabilities make the vocabulary moments land harder for students.

---

## The Three Gaps

### Gap 1: No `[vocab]` markup in SPs — the biggest mechanical gap

**App:** 117 `[vocab]` tags across Unit 5 (52 in M1 alone). Every vocabulary term is explicitly marked so the app can render it with special visual treatment (highlighting, bold, audio emphasis).

**SPs:** **Zero** `[vocab]` tags across all 11 Unit 2 SPs. Not a single instance.

**Why this matters:** When a scripter converts the SP to app JSON, they have to decide independently which words deserve `[vocab]` treatment. If the SP author intended "unit square" to be a highlighted vocabulary moment but only wrote it in plain Guide dialogue, the scripter might miss it — or highlight it in some interactions but not others. The SP is the source document. If it doesn't specify vocabulary markup, the app implementation will be inconsistent.

**Impact:** High. This is purely a format gap — easy to fix, high payoff.

### Gap 2: Vocabulary reinforcement density is 4-8x lower in SPs

**App M1 (fractions):** "equal parts" appears **42 times** across 29 lesson steps. That's 1.4 uses per step. The term is woven into Guide dialogue, On Correct, remediation, and synthesis.

**App M3 (numerator/denominator):** "numerator" appears **31 times**, "denominator" **31 times** across 19 steps.

**SP M1 (area):** "unit square" appears in the introduction interaction and perhaps 3-5 subsequent interactions. Across 21 interactions, that's roughly 5-10 uses — approximately **5x less dense** than the app equivalent.

**SP M11 (composite figures):** "decomposing" introduced once, used in ~4 subsequent interactions. "Composite figure" introduced once, reinforced ~3 times.

**Why this matters:** Vocabulary research is clear that term acquisition requires multiple exposures in varied contexts. The app achieves this through sheer repetition — every Guide turn that references the concept uses the formal term. SPs tend to introduce the term once (well!) and then assume it's established, without specifying how many times and in what contexts the term should reappear.

**Impact:** High. The SP doesn't need to repeat the term 42 times — the scripter will naturally use it in dialogue. But the SP should specify a **vocabulary reinforcement target** (e.g., "Term X should appear in Guide dialogue for at least 6 of the remaining interactions after introduction") so the scripter knows the intent.

### Gap 3: No vocab in On Correct or remediation dialogue

**App M1, Step 7 On Correct:** "Yes. You made two [vocab]equal parts[/vocab]: two halves. See how each part is exactly the same size?"

**App M1, Step 7 Heavy Remediation:** "Let me show you. Watch as I click right in the middle to make two [vocab]equal parts[/vocab]. See? Now both parts are the same size."

**SPs:** On Correct is 10-20 words, no vocab markup. Remediation is "Pipeline" — no dialogue specified. The SP author has no mechanism to ensure vocabulary terms appear in the remediation path.

**Why this matters:** Students who get remediation are the ones who need vocabulary reinforcement most. If a student struggles, gets heavy remediation, and the remediation dialogue never uses the formal term, they miss the vocabulary moment entirely. The app avoids this by embedding vocab tags throughout all dialogue paths. The SP can't specify this because remediation is a separate pipeline.

**Impact:** Medium. This intersects with the "On Correct no-new-info rule" — we already established that On Correct shouldn't introduce NEW vocabulary. But it absolutely should USE established vocabulary. And the SP format can't influence remediation dialogue. This is a pipeline boundary issue, not something the SP can fully solve.

---

## What SPs Do BETTER Than the App

### Better: Explicit causal "because" chains

**SP M1:** "Each tile is called a UNIT SQUARE **because** it covers one SQUARE UNIT of space."

**App M2:** "This is called a unit fraction. 'Unit' means one."

The SP's causal chain is pedagogically stronger — it connects the term to the action the student just performed. The app's etymology ("unit means one") is informative but less grounded in the student's experience. SPs consistently use "because" language; the app is mixed.

### Better: CRA staging discipline

SPs enforce a deliberate 2-4 interaction gap between first visual exposure and formal naming. Module 1 (area) gives students 4 full interactions of tiling, counting, and comparing before introducing "unit square." This is textbook CRA.

The app is sometimes tighter than ideal. Module 2 introduces "unit fraction" at Step 2 — just one step after the visual. Module 6 introduces "improper fraction" almost immediately. Some app modules front-load vocabulary more than the Playbook recommends.

### Better: Phase-labeled vocabulary staging

SPs explicitly label which CRA phase vocabulary appears in (always Abstract, after Concrete + Relational). The app doesn't have phase labels — terms just appear when they appear. This makes the SP a better design document for the curriculum team, even if the app execution sometimes works well despite less deliberate staging.

---

## What the App Does That SPs Can't (Inherent Format Limitations)

### Event-synchronized visual highlighting

App M1, Step 2: `[event:68fa6beed22740ab] is our [vocab]whole[/vocab]`

The `[event]` tag fires an animation AT THE EXACT WORD where "whole" is spoken. The bar highlights or pulses at the moment the term is named. This creates a multimodal vocabulary moment — audio (Guide says the word) + visual (bar highlights) + text (term appears highlighted) simultaneously.

SPs can only describe a static Visual state. They can't specify "the bar should highlight at the moment the Guide says 'whole'." This synchronization is the single biggest qualitative difference between app vocabulary moments and SP vocabulary moments. It's an inherent limitation of the SP format as a design document — it would require an event scripting layer that doesn't belong in the SP.

### Vocabulary in warmup activation

The app has 16 `[vocab]` tags in Warmup files, reviewing established terms in the new module's opening. SPs may activate vocabulary in Warmup but the Playbook says "Vocabulary: Forbidden to teach" in Warmup — which is correct for NEW vocabulary but doesn't explicitly address review/activation markup of ESTABLISHED terms.

---

## Recommendations

### 1. Add `[vocab]` markup to the SP format (HIGH PRIORITY)

Add a rule to the Template and Playbook: Every formal vocabulary term, from the interaction where it's introduced through the end of the module, should be marked with `[vocab]term[/vocab]` in Guide dialogue and On Correct fields. This is a simple, mechanical change that closes the biggest gap.

**Template change needed:** Add to interaction block format:
- Guide dialogue should mark established vocabulary terms with `[vocab]term[/vocab]` markup
- On Correct should use `[vocab]` markup for any established terms it references

### 2. Add a Vocabulary Reinforcement Target to each module's Section Plan (HIGH PRIORITY)

After the vocabulary introduction interaction, the Section Plan should specify how many subsequent interactions will use the formal term. Suggested minimum: the term appears in Guide dialogue for at least **50% of remaining interactions** after introduction. This prevents the "introduce once and forget" pattern.

**Template change needed:** Add to Section Plan format:
- Vocabulary Reinforcement Plan: [Term] introduced at [Interaction]. Reinforced in: [list of subsequent interaction IDs where term appears in Guide dialogue]

### 3. Clarify the Warmup Playbook on vocabulary ACTIVATION vs TEACHING (MEDIUM)

The Warmup Playbook says vocabulary is "Forbidden to teach" — but the app productively uses `[vocab]` tags in Warmup to activate prior-module terms. The Playbook should clarify: NEW vocabulary is forbidden in Warmup; REVIEW of established vocabulary from prior modules is encouraged and should use `[vocab]` markup.

### 4. Add a Vocabulary Density check to the eval plugin (MEDIUM)

The SP eval plugin should flag modules where a vocabulary term is introduced but then appears fewer than 3 times in subsequent Guide dialogue. This is a mechanical check that could catch under-reinforcement.

### 5. Accept the event-synchronization limitation (NO ACTION NEEDED)

The SP cannot and should not try to specify animation-to-dialogue timing. That's the scripter's job. The SP's role is to mark WHAT terms need special treatment (`[vocab]` tags) and WHEN they're introduced (CRA phase). The HOW of visual synchronization belongs to the scripting/engineering pipeline.

### 6. Note the remediation boundary (AWARENESS ONLY)

Remediation dialogue is a separate pipeline. SPs can't specify vocab-rich remediation. But the remediation pipeline team should know that the SP's vocabulary terms need to appear in remediation dialogue, especially heavy remediation which replaces On Correct. This is a cross-pipeline communication issue, not an SP format issue.

---

## Raw Data Summary

| Metric | App (Unit 5) | SPs (Unit 2) |
|---|---|---|
| Total `[vocab]` tags | 117 | **0** |
| M1 vocab tags in lesson | 52 | 0 |
| "equal parts" / "unit square" frequency | 42x in 29 steps | ~5-10x in 21 interactions |
| Vocab in On Correct | Yes (tagged) | Yes (plain text, no markup) |
| Vocab in remediation | Yes (tagged) | No (Pipeline) |
| Vocab in warmup | 16 tags across unit | Not marked |
| CRA staging compliance | Mixed (some cold intros) | 100% compliant |
| Causal "because" chains | Sometimes | Always |
| Event-synchronized highlights | Yes | N/A (format limitation) |
| Modules with NO vocab moments | 2 (M7, M9) | 3 (M8, M9, M12) |
