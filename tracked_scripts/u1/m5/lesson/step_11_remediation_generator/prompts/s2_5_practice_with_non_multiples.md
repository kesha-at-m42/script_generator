# Prompt: remediation_generator
# Generated: 2026-05-05T13:24:36.553398
======================================================================

## API Parameters
- temperature: 1
- max_tokens: 8000

======================================================================

## System Prompt

### Block 1: Role
Purpose: Establishes AI role and task context
Cacheable: Yes

# ROLE & CONTEXT

You are generating remediation feedback states for lesson section JSON. This is AUTHORING work. You write instructional dialogue and scene beats that guide a student who answered incorrectly.

----------------------------------------------------------------------

### Block 2: Reference Doc (remediation_design_ref.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: remediation_design_ref.md

<remediation_design_ref>
# REMEDIATION DESIGN REFERENCE v3

**Version:** 3.2
**Last Updated:** April 2026
**Purpose:** Authoritative guide for **branching remediation requirements** across learning modules — defines what feedback to serve and when. This document does not govern validation. Validator coverage is intentionally broader than remediation branching; the goal is to diagnose the cause of student error from accumulated data, not to presume it in advance.

---

## TABLE OF CONTENTS

**SECTION 1** \- System Architecture Overview
**SECTION 2** \- Non-MC Remediation (Generic L-M-H)
**SECTION 3** \- Single-Select MC Remediation (Per-Distractor Branching)
**SECTION 3B** \- Multiselect MC Remediation (Per-Branch Branching)
**SECTION 4** \- Light Remediation Language Patterns
**SECTION 5** \- Medium Remediation Language Patterns
**SECTION 6** \- Heavy Remediation Language Patterns
**SECTION 7** \- Post-Modeling Language
**SECTION 8** \- Error Signal Strategy
**SECTION 9** \- Remediation by Phase
**SECTION 10** \- Quality Checklist
**SECTION 11** \- Output Format Examples

---

## SECTION 1: System Architecture Overview

### 1.1 The Simplified Model

**v3 introduces a three-track approach based on question type:**

| Question Type | Remediation Approach | Rationale |
| :---- | :---- | :---- |
| **Non-MC with ambiguous errors** (create, shade, place, etc. — no specific wrong answers identified) | Generic L-M-H only | Error cause often ambiguous; tracking handles patterns |
| **Non-MC with specific errors** (same interaction types, but spec identifies one or more known wrong answers) | One Medium per specific condition + generic L-M-H for other answers | Spec identifies a known error (e.g. "reversed numbers") worth targeted feedback; see Section 2.5 |
| **Single-Select MC** (one correct answer) | Per-distractor branching | We know exactly which wrong answer; targeted feedback valuable |
| **Multiselect MC** ("select all that apply") | Per-branch Medium + single Heavy | Selection pattern reveals cognitive state; generic language stays scalable |

**Why This Works:**

- Non-MC errors are noisy. Kids click wrong for many reasons
- Single-Select MC distractors give clear diagnostic signal about thinking
- True misconceptions are caught by pattern tracking, not single-instance diagnosis
- Content volume becomes manageable without sacrificing quality

### 1.2 The Two Systems Working Together

```
IMMEDIATE FEEDBACK (This Document)
├── Non-MC (ambiguous errors): Generic L-M-H
│   └── Validators tag probable error type (for tracking only)
├── Non-MC (specific errors): One Medium per spec-defined condition + generic L-M-H for other answers
│   └── Spec identifies one or more known wrong-answer conditions; see Section 2.5
├── Single-Select MC: Per-distractor Medium + Heavy
│   └── Targeted feedback based on which wrong answer chosen
└── Multiselect MC: Per-branch Medium + Heavy
    └── Branch by selection pattern (under-select, all-wrong, mixed, or success)

PATTERN DETECTION (Background)
├── Rolling window tracks misconception indicators
├── Threshold triggers Intervention Activity
└── Intervention queued as next activity
```

### 1.3 Core Principles (Unchanged)

- **Sequential only:** Light → Medium → Heavy (max 3 attempts)
- **Never alternatives:** No "Try X or Y" or "Another way to think about it"
- **Progressive support:** Each level provides meaningfully more help
- **System takeover:** After Heavy, system moves student forward

### 1.4 What Changed from v2

| v2 (Old) | v3 (New) |
| :---- | :---- |
| Three remediation types at each level (Generic, Common Error, Misconception) | Non-MC: Generic only; Single-Select MC: Per-distractor; Multiselect MC: Per-branch |
| System detects error type and selects remediation in real-time | Non-MC: No detection needed; Single-Select MC: Distractor choice is the detection; Multiselect MC: Selection pattern is the detection |
| 9-15 remediation pieces per question | 3 pieces (Non-MC), 4-5 pieces (Single-Select MC), or 4 pieces (Multiselect MC) |
| Misconception addressed via targeted immediate feedback | Misconception addressed via Intervention after pattern detected |

---

### 1.5 Branching vs. Validation: Separate Concerns

These are two independent systems with different scopes:

| Concern | What it governs | Coverage |
| :---- | :---- | :---- |
| **Branching (this document)** | What remediation to serve and when | Only the cases worth targeted feedback |
| **Validation (separate)** | What error patterns to log for tracking | Intentionally broader — captures cases not covered by branching |

**The distinction matters.** A wrong answer that receives generic L-M-H feedback can still receive a precise validator tag. Validators are not constrained by what the remediation structure handles. We expect to capture more error patterns than we intend to remediate. The tracking system accumulates data so that error causes are diagnosed from evidence, not assumed in advance — a detected pattern may indicate a misconception, a skill gap, or something else entirely. The cause is a question for the data to answer, not a label to apply upfront.

Do not design validator tags based on what remediations exist. Design them based on what error patterns are worth understanding.

**Validation design is a separate effort from remediation design — and should be treated differently.** Remediation branching is relatively stable once written: changing it means authoring new feedback states and updating production content. Validation should be flexible and subject to ongoing iteration. Validator tags can be added, renamed, split, or retired as understanding of student error patterns develops. The two should not be versioned or locked together. Build remediation to last; build validation to learn.

---

## SECTION 2: Non-MC Remediation

### 2.1 Overview

For all non-multiple-choice interactions (shading, partitioning, placing on number lines, dragging, build-mode, etc.), the generic L-M-H is always present. **The validator still tags the probable error type** for misconception tracking, but the student receives generic feedback for any wrong answer — regardless of detected error type. Note: if more conditions are defined in the spec than have remediations designed, those conditions still fall through to the generic L-M-H. This is also true for validation: validators may tag error types that have no corresponding specific-condition state. Validator coverage is not bounded by the branching structure — they are separate authoring decisions.

When the spec identifies one or more specific known wrong-answer conditions, one targeted Medium per condition is added before the generic states. These specific condition states are a special case of the generic structure — see Section 2.5.

### 2.2 Why Generic Works

- Single errors are noisy. We can't reliably diagnose from one mistake
- Pattern detection across multiple opportunities is more accurate
- Reduces content creation burden dramatically
- Interventions (when triggered) provide better conceptual support than in-the-moment micro-corrections

### 2.3 Non-MC Flow

```
Student attempts → Wrong
    ↓
Light Remediation (generic)
    ↓
Student attempts → Wrong
    ↓
Medium Remediation (generic) + Visual scaffold
    ↓
Student attempts → Wrong
    ↓
Heavy Remediation (generic) + Full modeling → Reveals answer
    ↓
System moves forward

[Background: Validator logs probable error type for tracking]
```

### 2.4 Generic Non-MC Structure

**Light (10-20 words):** Brief redirect, no visual.

**Medium (20-30 words):** Visual scaffold required. Teach the method — name what to look at and in what order — without supplying the specific counts or values. The student still has to do the work. Close with a pointed question or specific imperative that sends the student back to the problem.

**Heavy (30-60 words):** Full modeling with \[Modeling\] tag. Narrate the thinking, not just the mechanics — name the structure being demonstrated, connect each step to what it means. End with the underlying principle: why the answer has to be what it is, not just what the answer is.

### 2.5 Specific Conditions (special case)

Some Non-MC prompts have specific wrong-answer conditions identified in the spec (e.g. "student reverses the two numbers"). There may be one or more such conditions.

**One Medium per identified condition.** Each condition gets one state, written at Medium level (visual scaffold + 20–30 words of dialogue). It fires on either the first or second attempt when that specific wrong answer is given. The generic L-M-H remains — it covers all other wrong answers, and covers the specific conditions on attempt 3+.

**State order when specific conditions are present:**

1. One Medium per specific condition — fires on attempt 1 or 2 when that specific wrong answer is given
2. Generic Light — attempt 1, wrong answer that did not match a specific condition
3. Generic Medium — attempt 2, wrong answer that did not match a specific condition
4. Generic Heavy — system models the correct answer. Always last. Also fires for specific conditions on attempt 3+.

### Writing specific condition dialogue

Two patterns work well for specific condition mediums:

**Pattern A — Credit + narrow:** When the student got part of the answer right, acknowledge it, then narrow to the specific thing that was wrong. Close with a pointed question.

> "You're right that there are 4 columns. But count how many dots are in each column. Are there 4?"

Structure: `[What was right]. [But/Now] [what to re-examine]. [Pointed question or one step.]`

**Pattern B — Name + redirect + point:** Name what the student did briefly, redirect to the correct concept, give one concrete action or question.

> "You counted the Dogs. When we ask how many fewer, we need to find the difference. Count how far apart Dogs and Fish are."

Structure: `[What they did — one phrase]. [What the question actually needs]. [One action or question.]`

In both patterns: do not give the correct counts or values. The student still has to look and execute. The medium names the error and points the way — it does not complete the work.

**Rules:**
- Each specific condition is ONE state covering attempt 1 or 2. Do not write separate states per attempt.
- Generic L-M-H states are always required even when specific conditions are present.
- Specific condition states are Non-MC only. Single-Select MC and Multiselect MC use per-distractor/per-branch logic instead.

---

## SECTION 3: Single-Select MC Remediation (Per-Distractor Branching)

### 3.1 Overview

For single-select multiple choice questions, we know exactly which wrong answer the student chose. Each distractor represents a specific error or misconception, so we can provide **targeted feedback**.

### 3.2 Single-Select MC Structure

For a 4-option Single-Select MC question (1 correct \+ 3 distractors):

- **3 Medium remediations** (one per distractor)
- **1 Heavy remediation** (explains the correct answer)

**No Light remediation for Single-Select MC.** Rationale: If they knew the right answer, they would have picked it. A generic "check your answer" rarely helps when we have specific diagnostic information.

### 3.3 Single-Select MC Flow

```
Student selects Distractor A → Wrong
    ↓
Medium A (targeted to Distractor A's error) + Visual scaffold
    ↓
Student selects Distractor B → Wrong
    ↓
Medium B (targeted to Distractor B's error) + Visual scaffold
    ↓
Student selects any wrong answer → Wrong
    ↓
Heavy (explains correct answer) + Full modeling
    ↓
System moves forward
```

**Same distractor twice:** Student receives the same Medium again. This provides reinforcement and removes any gaming incentive (no shortcut to Heavy/completion).

### 3.4 Single-Select MC Distractor Design Principles

Each distractor should represent a **diagnosable error:**

| Distractor Type | Example | Medium Focus |
| :---- | :---- | :---- |
| Numerator/denominator confusion | Selected 4/3 instead of 3/4 | "The numerator tells us how many parts we have, not the total" |
| Counted total instead of shaded | Selected 6/6 when 4/6 shaded | "Count only the shaded parts for the numerator" |
| Ignored equal parts requirement | Selected unequal partition | "For fractions, all parts must be equal size" |
| Whole number thinking | Selected 3 instead of 3/4 | "We need a fraction. The bottom number tells us the size of parts" |

### 3.5 Metacognitive Single-Select MC Questions

Metacognitive questions ("Which strategy would help?", "What should you check first?") are **highest value for branching**. Each wrong strategy choice reveals specific thinking patterns we can address.

---

## SECTION 3B: Multiselect MC Remediation (Per-Branch Branching)

### 3B.1 Overview

For "select all that apply" questions, students may select multiple answers simultaneously. The error signal is not a single distractor but a **selection pattern** — which correct and incorrect options were included in the submission. Branching is based on that pattern rather than on a specific choice.

### 3B.2 Multiselect MC Structure

Before generating remediation, identify whether the question has wrong options:

**Signal — check whether the question has any wrong options:**
- If some options are ones the student should **not** select → **standard variant** (some options are wrong)
- If every option is a valid correct answer → **no-wrong-options variant** (see Section 3B.9)

**Standard variant** (has wrong options):

- **3 Medium remediations** (one per error branch)
- **1 Heavy remediation** (explains the full correct selection)

**No Light remediation for standard Multiselect MC.** Same rationale as Single-Select MC: a generic "check your answer" provides little help when the selection pattern gives specific diagnostic information.

**No-wrong-options variant:** See Section 3B.9.

### 3B.3 The Four Branches

| Branch | Condition | Remediation | Tone |
| :---- | :---- | :---- | :---- |
| **Branch 1** | All correct answers selected, no incorrect | Success path | — |
| **Branch 2** | Only correct answers selected, but not all | Medium 2 — under-selecting | Near-success: acknowledge what they got right; nudge toward the rest |
| **Branch 3** | All incorrect answers selected, none correct | Medium 3 — all-wrong | Foundational: redirect to the concept before re-attempting; do not acknowledge selections positively |
| **Branch 4** | Mix of correct and incorrect selected | Medium 4 — over-selecting | Acknowledge the correct picks genuinely; clearly flag that one or more choices don't fit |

**Pedagogical principle:** Tone must reflect how close the student actually is to the correct answer. Branch 2 is a near-success — every selection was valid, the student just stopped short — and deserves meaningfully more positive framing than Branch 3, where no correct answers were identified. Remediation language should never feel uniform across branches; each branch represents a meaningfully different cognitive state.

### 3B.4 Multiselect MC Flow

```
Student submits selection
    ↓
Branch 1: All correct → Success
Branch 2: Correct-only, incomplete → Medium 2 + Visual scaffold
Branch 3: All incorrect → Medium 3 + Visual scaffold
Branch 4: Mixed correct + incorrect → Medium 4 + Visual scaffold
    ↓
Student submits again
    ↓
Same branch → Same Medium repeated (reinforcement; removes gaming incentive)
Different branch → That branch's Medium
    ↓
Student submits again (3rd attempt)
    ↓
Heavy (all branches share one Heavy) + Full modeling → Reveals correct answer
    ↓
System moves forward
```

**Same branch twice:** Student receives the same Medium again. This provides reinforcement and removes any gaming incentive, consistent with Single-Select MC logic.

### 3B.5 Generic Language Requirement

Multiselect MC Mediums use **generic language across all submissions in a given branch** — no per-combination branching. This is a deliberate architectural constraint, not an oversight.

**The under-selecting case is where this is most tempting to violate.** When the correct answers are {A, B} and a student selects only A, it is natural to want to say "You got A — now find the other one." When a student selects only B, it is natural to say "You got B — now find the other one." But these are the same cognitive state (correct so far, incomplete) and must receive the same generic Medium. Do not enumerate partial-correct combinations, even when there are only two correct answers.

**Why:** With N correct answers, the number of partial-correct combinations is 2ᴺ − 2. With 2 correct answers that is 2 variants; with 3 it is 6; with 4 it is 14. Per-combination branching is unscalable, and the combinations do not represent meaningfully different cognitive states — they represent the same state (under-selecting) reached via different paths.

A student who selected only {A} and a student who selected only {A, B} (when correct answers are {A, B, C}) both receive Branch 2 Medium. The Medium acknowledges that their selections were valid but incomplete and prompts them to look for more — without referencing which specific answers they chose.

### 3B.6 Branch 3 Tone Distinction

Branch 3 (all-wrong) must be **distinctly more foundational in tone** than Branches 2 and 4. All-wrong signals a deeper conceptual gap — the student has not identified any correct answers. Branch 3 Medium should redirect the student to what the concept means before they attempt again. Do not frame this as "close" or acknowledge the selections positively in any way.

### 3B.7 Branch Condition Patterns

Each branch must be expressed as a self-sufficient condition — do not rely on evaluation order to exclude cases that the condition itself does not rule out. The correct patterns, where `[C...]` are correct answer values and `[W...]` are incorrect answer values:

| Branch | Condition logic |
| :---- | :---- |
| **Branch 2** (under-selecting) | (any correct selected) AND NOT (all correct selected) AND NOT (any incorrect selected) |
| **Branch 3** (all-wrong) | NOT (any correct selected) |
| **Branch 4** (mixed) | (any incorrect selected) AND (any correct selected) |
| **Heavy** | `{}` — unconditional fallback |

**Branch 2 must explicitly exclude incorrect selections.** Without that clause, a student who selects one correct answer plus one incorrect answer will be caught by Branch 2 (under-selecting) instead of Branch 4 (mixed). This is the most common condition bug for multiselect questions.

**Branch 4 must explicitly require at least one correct selection.** Without that clause, the condition overlaps with Branch 3. The overlap is masked by evaluation order but makes the condition's intent ambiguous and fragile.

### 3B.9 No-Wrong-Options Variant

Some Multiselect MC prompts have **no incorrect options** — every option in the list is a valid correct answer.

In this case, Branch 3 (all-wrong) and Branch 4 (mixed correct + incorrect) are **structurally impossible**. The student can only under-select or select all.

**Detection:** If every option in the question is a correct answer, this is the no-wrong-options variant.

#### Why specific remediations still matter here

Even though there are no wrong options, targeted remediations are valuable when the spec or content gives us confidence about which options students commonly miss. A student who recognizes two out of three valid scenarios has made real progress — generic "you missed some" language fails to credit that and misses the chance to point them toward the specific gap.

When the likely missing option is predictable (e.g. a less obvious scenario, a counter-intuitive case), a targeted Medium pointing toward that option gives meaningfully more help than a generic nudge. This follows the same logic as Non-MC specific conditions (Section 2.5): where we can identify the error pattern with confidence, we write for it.

#### Positive reinforcement requirement

Because every option the student selected is correct, remediation language at Light and Medium level **must acknowledge what they got right**. The student has made no errors — they have only stopped short. Tone should be genuinely near-success, not corrective.

- Do not say "Not quite" or "Let's try again" — those signal an error that isn't there
- Do say "You found some — are there any others?" or "Those are all correct. Did you select ALL?"

#### Structure

**Generic (no predictable missing option):** Use attempt-count conditions — the same L/M/H pattern as Non-MC.

- **Light (first attempt):** Short nudge with positive framing, no scene beat. Example: "Those are correct — did you select ALL of them?"
- **Medium (second attempt):** Acknowledge correct selections, then guide toward what's missing with a visual scaffold (20–30 words).
- **Heavy (final attempt):** Models all correct answers. Full modeling demonstration required.

**Specific (commonly missed option known):** Add one targeted Medium per predictable gap before the generic states, following the same order as Non-MC specific conditions (Section 2.5). Generic L/M/H remains — it covers all other under-selecting patterns and covers specific gaps on the final attempt.

**Do not invent phantom wrong options.** If every option is correct, emit L/M/H by attempt count — not Branch 2/3/4.

---

### 3B.8 Heavy for Multiselect MC

All branches escalate to the same single Heavy on the final attempt. Heavy for Multiselect MC:

- Explains which answers are correct and why
- Demonstrates the full correct selection with \[Modeling\] tag
- Reveals the answer explicitly
- Does not reference the student's specific wrong submission

After Heavy, the system moves the student forward regardless of response.

```
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words explaining the correct selections and demonstrating the reasoning]"
[Visual: Correct answers highlighted; system demonstrates selection process]
Guide: "[Post-modeling acknowledgment]"
```

---

## SECTION 4: Light Remediation Language Patterns

**Length:** 10-20 words
**Tone:** Brief and direct
**Visual:** None
**Applies to:** Non-MC interactions only (Single-Select MC and Multiselect MC both skip Light)

### 4.1 With Error Signal (40-50% of interactions)

Use at beginning of module, after successes, when student might think they're right:

- "Not quite. \[specific guidance\]"
- "Almost. \[specific guidance\]"
- "Let's try again. \[specific guidance\]"
- "Let's look at this problem again."
- "Let's take another look."
- "Let's try that again."
- "Let's look closely: \[specific guidance\]"

### 4.2 Without Error Signal (50-60% of interactions)

Use mid-module, when error is obvious, to avoid repetition:

- Direct guidance with no preamble
- "Check \[specific element\]"
- "Count \[specific element\]"
- "Focus on \[specific element\]"
- Simple imperative statements

### 4.3 Guidance Alternatives to "Remember"

Save "Remember" for Medium/Heavy. At Light level, use:

- "The key is..."
- "Focus on..."
- "Notice that..."
- "Here's what helps..."
- "Check the..."

### 4.4 Light Examples

- "Not quite. Count the shaded parts only."
- "Check the spacing between marks."
- "Focus on equal-sized parts."
- "Let's look closely: which parts are shaded?"
- "Count from zero, not from one."

---

## SECTION 5: Medium Remediation Language Patterns

**Length:** 20-30 words
**Tone:** Acknowledge struggle, collaborative
**Visual:** REQUIRED (from Visual Scaffolds TSV)
**Applies to:** Non-MC, Single-Select MC, and Multiselect MC

### 5.1 Approved Starters (Non-MC)

- "Let's think about this together. \[specific help\]"
- "Here's a hint: \[specific clue\]"
- "You're working on it. Here's what helps: \[specific support\]"
- "You're getting there. The key is \[crucial detail\]"
- "Let's think about this a bit more. \[guidance\]"

### 5.2 Closing with a Call to Action

Every medium closes with a call to action that sends the student back to attempt. Use a pointed question or a specific imperative — concrete enough that the student knows exactly where to look or what to do next.

Effective CTAs:
- "How many rows do you see?"
- "Count those and place the numbers."
- "Place those numbers into the expression."
- "Does it change?"

The starter establishes the redirect; the CTA makes it actionable.

### 5.2 Single-Select MC Medium Structure

For Single-Select MC, Medium is targeted to the specific distractor chosen:

**Template:**

```
[Medium_Remediation - Distractor_A] [Meta_Remediation]: "[20-30 words addressing why Distractor A is wrong and redirecting thinking]"
[Visual: Scaffold highlighting the specific error]
```

**Example (student chose 6/6 when 4/6 was shaded):**

```
[Medium_Remediation - Distractor_B] [Meta_Remediation]: "You counted all the parts. The numerator only counts the shaded parts. How many are filled in?"
[Visual: Shaded parts pulse/highlight, unshaded parts dim]
```

### 5.3 Medium Examples (Non-MC)

- "Let's think about this together. Four fourths equals 1, then three more fourths gets us to 7/4." \[Visual: Number line with 4/4 marked at 1\]
- "Here's a hint: each fourth stays the same size, even past 1." \[Visual: Equal jumps highlighted\]
- "You're working on it. Count the shaded parts for the top number." \[Visual: Shaded sections pulse\]

### 5.4 "Remember" Usage

- Maximum 2-3 times per entire module
- Medium/Heavy only (never Light)
- Use for genuinely important callbacks to prior learning

---

## SECTION 6: Heavy Remediation Language Patterns

**Length:** 30-60 words
**Tone:** Full support, complete demonstration
**Visual:** REQUIRED (full modeling demonstration)
**Tag:** \[Modeling\] REQUIRED
**Closure:** REQUIRED — dialogue ends with a statement that names the correct answer and the concept the question was testing (see Section 7)
**Applies to:** Non-MC, Single-Select MC, and Multiselect MC

### 6.1 Approved Opening Language

- "This one takes a bit of thought, so let's work through it together..."
- "Let me show you how this works."
- "Here, let me walk you through this one."
- "Let's work through this step by step..."
- "These can be challenging. Let me show you..."
- "Let me help a bit more."
- "This one needs a closer look, so let's do it together."

### 6.2 Heavy Structure (Non-MC)

```
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words with complete step-by-step demonstration, ending with closure: name the correct answer and the concept it demonstrates]"
[Visual: System demonstrates complete solution]
```

### 6.3 Heavy Structure (Single-Select MC)

For Single-Select MC, Heavy explains why the correct answer is right:

```
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words explaining the correct answer and demonstrating the thinking, ending with closure: name the correct answer and the concept it demonstrates]"
[Visual: Correct answer highlighted with supporting scaffold]
```

### 6.4 Heavy Examples

**Non-MC:** "Let me show you how this works. First, I count the total parts. That's my denominator: 4\. Then I count just the shaded parts. That's my numerator: 3\. So the fraction is 3/4." \[Visual: System highlights total parts, then shaded parts, then shows 3/4\]

**Single-Select MC:** "Let me show you how to think about this. The question asks which fraction is shown. I count 4 equal parts total. That's the denominator. 3 parts are shaded. That's the numerator. So the answer is 3/4, not 4/3." \[Visual: Correct answer highlighted, visual shows counting sequence\]

---

## SECTION 7: Post-Modeling Closure

Heavy is the final state for a question. There is no student call-to-action after Heavy — the system moves the student forward automatically. The closing line of the Heavy dialogue must provide **closure**: a statement that names the correct answer and the concept the question was testing.

This is the same function that on_correct feedback serves when a student answers correctly. After being shown the answer, the student should leave knowing what the answer was and why it is correct.

### 7.1 Closure Structure

The Heavy dialogue ends with a closure sentence that:

- Names the correct answer explicitly in the context of the question
- States the underlying concept briefly (the "so what")
- Does not ask the student to do anything

**Pattern:** `[Modeling narration ends.] [Correct answer stated in context.] [Brief concept restatement.]`

### 7.2 Closure Examples

**Non-MC (fraction shading):** "...I count the total parts. That is my denominator: 4. I count the shaded parts. That is my numerator: 3. The fraction shown is 3/4."

**Single-Select MC:** "...The denominator is 4, the numerator is 3. The answer is 3/4, not 4/3. The numerator counts the shaded parts, not the total."

**Multiselect MC:** "...Both A and C show equal parts of a whole. Those are the fractions. That is what makes something a fraction — equal parts with a count."

### 7.3 NEVER Use as the Closing Line

- ❌ "See how that works?" — does not name the answer
- ❌ "There we go." — does not name the answer
- ❌ "Now you understand." — does not name the answer
- ❌ "Perfect\!" (they didn't do it alone)
- ❌ "You figured it out\!" (guide showed them)
- ❌ "Great job\!" (too independent)
- ❌ "Excellent work\!" (overpraises assisted work)

### 7.4 Forward Move (Optional)

A brief forward phrase may follow the closure line but is not required:

- "Now let's continue."
- "Let's keep going."

Do not use "Let's try another one." — it implies an immediate retry of the same problem, which does not reflect system behavior after Heavy.

---

## SECTION 8: Error Signal Strategy

### 8.1 When to Use Error Signals

Use error signals (40-50% of Light remediations) when:

- Beginning of module (establish pattern)
- After successes (clear change signal)
- When student might think they're right
- Ambiguous errors

### 8.2 When to Skip Error Signals

Skip error signals (50-60% of Light remediations) when:

- Error is obvious
- Would cause repetition
- Mid-module routine corrections
- Guidance itself implies error

### 8.3 Variety Requirement

Never repeat the same error signal phrase within 3 interactions. Rotate through:

- "Not quite."
- "Almost."
- "Let's try again."
- "Let's look at this problem again."
- "Let's take another look."

---

> **Context — Related Systems (defined separately):** Validator tags feed a background error pattern tracking system that triggers Intervention Activities when patterns reach threshold. A triggered pattern is a hypothesis, not a diagnosis — the cause may be a misconception, a skill gap, or something else. Tracking parameters and intervention design are out of scope here; see the *Error Pattern Tracking Spec* and *Intervention Activity Design Brief*.

---

## SECTION 9: Remediation by Phase

### 9.1 Requirements by Phase

| Phase | Non-MC Requirement | Single-Select MC Requirement | Multiselect MC Requirement | Notes |
| :---- | :---- | :---- | :---- | :---- |
| Warmup | Light minimum | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Heavy if key prior knowledge |
| Lesson | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | All interactions |
| Exit Check | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | MANDATORY \- gateway phase |
| Practice | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Light only for confidence builders |
| Synthesis | Light minimum | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Full L-M-H for pattern discovery |
| Challenge | None | None | None | Assessment mode |

### 9.2 Module Complexity Considerations

**Modules 1-3 (Simple concepts):**

- Light remediation may be sufficient for some interactions
- Simpler language appropriate
- Don't force full L-M-H if unnecessary

**Modules 4-8 (Building complexity):**

- Full L-M-H progression more common
- Can reference earlier module strategies

**Modules 9-12 (Complex concepts):**

- Full L-M-H usually needed
- More nuanced explanations appropriate

**Documentation:** Use \[Pedagogical\_Override\] when reality differs from stated requirements.

---

## SECTION 10: Quality Checklist

### 10.1 Non-MC Remediation Checklist

**Track A (ambiguous errors — no specific conditions):**
- [ ] Generic L-M-H only (no branching by error type)
- [ ] Light: 10-20 words, no visual
- [ ] Medium: 20-30 words, visual REQUIRED
- [ ] Heavy: 30-60 words, \[Modeling\] tag REQUIRED, visual REQUIRED
- [ ] Heavy dialogue ends with closure: names the correct answer and the concept it demonstrates
- [ ] Different language at each level
- [ ] No independent-success praise after modeling
- [ ] Validator tags probable error type (noted in script or separate)

**Track B (specific errors — spec defines known wrong answers):**
- [ ] One state per specific condition using `and`/`or` condition: `{ "and": [{ condition }, { "or": [{"incorrect_count":1},{"incorrect_count":2}] }] }`, Medium level, visual REQUIRED
- [ ] Generic Light (`incorrect_count: 1`) after all specific-condition states
- [ ] Generic Medium (`incorrect_count: 2`), visual REQUIRED
- [ ] Generic Heavy (`condition: {}`), \[Modeling\] tag REQUIRED, visual REQUIRED
- [ ] Heavy dialogue ends with closure: names the correct answer and the concept it demonstrates

### 10.2 Single-Select MC Remediation Checklist

- [ ] One Medium per distractor (3 distractors \= 3 Mediums)
- [ ] Each Medium targets specific error that distractor represents
- [ ] One Heavy explaining correct answer
- [ ] All Mediums have visual scaffolds
- [ ] Heavy has \[Modeling\] tag
- [ ] No Light remediation (Single-Select MC skips to Medium)

### 10.2B Multiselect MC Remediation Checklist

- [ ] Three Medium remediations — one per error branch (under-selecting, all-wrong, mixed)
- [ ] Branch 2 Medium (under-selecting) acknowledges correct picks and nudges toward missing answers — near-success tone
- [ ] Branch 3 Medium (all-wrong) redirects to the concept without positively acknowledging selections — foundational tone, distinctly more remedial than Branches 2 and 4
- [ ] Branch 4 Medium (mixed) acknowledges correct picks genuinely and clearly flags what doesn't fit
- [ ] All three Mediums use generic language — no per-combination branching
- [ ] One Heavy explaining the full correct selection with \[Modeling\] tag
- [ ] All Mediums have visual scaffolds
- [ ] No Light remediation (Multiselect MC skips to Medium)
- [ ] Tone varies meaningfully across branches — remediation language does not feel uniform

### 10.3 Variety Checklist (Per Module)

- [ ] Minimum 8 different Light patterns (non-MC)
- [ ] 4-5 different Medium approaches
- [ ] "Remember" maximum 2-3 times total
- [ ] No exact phrase repeated within 3 problems
- [ ] Error signals rotated (40-50% with signal)

### 10.4 Structure Violations (Never Include)

- ❌ Alternative paths ("Try X or Y")
- ❌ Light remediation that teaches new content
- ❌ Medium without visual scaffold
- ❌ Heavy without \[Modeling\] tag
- ❌ Independent success praise after modeling
- ❌ More than 3 attempts before system takeover

---

## SECTION 11: Output Format Examples

### 11.1 Non-MC Format

```
Activity X - [Title]
Visual: [Description]
Prompt: "[Instruction]"
Guide: "[Support]"

[Student attempts]

SUCCESS PATH:
Guide: "[Specific acknowledgment]"

ERROR PATH:
[Light_Remediation] [Meta_Remediation]: "[10-20 words]"

[Medium_Remediation] [Meta_Remediation]: "[20-30 words]"
[Visual: Description of scaffold]

[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words with complete demonstration]"
[Visual: System demonstrates solution]
Guide: "[Post-modeling acknowledgment]"

[Validator: Probable error type for tracking - e.g., Misconception_#3]
```

### 11.2 Single-Select MC Format

```
Activity X - [Title] (Multiple Choice)
Visual: [Description]
Prompt: "[Question]"
Guide: "[Support]"

Options:
A) [Correct answer]
B) [Distractor - represents error type X]
C) [Distractor - represents error type Y]
D) [Distractor - represents error type Z]

[Student selects]

SUCCESS PATH (Option A):
Guide: "[Specific acknowledgment]"

ERROR PATHS:

[Medium_Remediation - Distractor_B] [Meta_Remediation]: "[20-30 words targeting error type X]"
[Visual: Scaffold addressing error type X]

[Medium_Remediation - Distractor_C] [Meta_Remediation]: "[20-30 words targeting error type Y]"
[Visual: Scaffold addressing error type Y]

[Medium_Remediation - Distractor_D] [Meta_Remediation]: "[20-30 words targeting error type Z]"
[Visual: Scaffold addressing error type Z]

[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words explaining why A is correct]"
[Visual: Demonstrates correct answer with full explanation]
Guide: "[Post-modeling acknowledgment]"
```

### 11.2B Multiselect MC Format

```
Activity X - [Title] (Multiselect MC — "Select all that apply")
Visual: [Description]
Prompt: "[Question]"
Guide: "[Support]"

Options:
A) [Correct answer]
B) [Correct answer]
C) [Incorrect distractor]
D) [Incorrect distractor]

[Student selects and submits]

SUCCESS PATH (all correct, none incorrect):
Guide: "[Specific acknowledgment]"

ERROR PATHS:

BRANCH 2 — Under-selecting (correct answers only, but not all):
[Medium_Remediation - Branch_2] [Meta_Remediation]: "[20-30 words: acknowledge correct picks; nudge student toward the answers they missed]"
[Visual: Scaffold highlighting the concept; correct selections reinforced]

BRANCH 3 — All-wrong (no correct answers selected):
[Medium_Remediation - Branch_3] [Meta_Remediation]: "[20-30 words: redirect to what the concept means; do not acknowledge selections positively; foundational tone]"
[Visual: Scaffold reorienting student to core concept]

BRANCH 4 — Mixed (some correct, some incorrect selected):
[Medium_Remediation - Branch_4] [Meta_Remediation]: "[20-30 words: genuinely acknowledge the correct picks; clearly flag that one or more choices don't fit]"
[Visual: Scaffold distinguishing correct from incorrect selections]

[Heavy — shared across all branches on final attempt]:
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words explaining which answers are correct, why, and demonstrating the full correct selection]"
[Visual: All correct answers highlighted; system demonstrates selection process]
Guide: "[Post-modeling acknowledgment]"
```

### 11.3 Validator Notation

For tracking purposes, include validator notation:

```
[Validator: This interaction tracks toward Misconception_#3, Misconception_#6]
```

Or in a separate tracking document linked to interaction IDs.

---

## APPENDIX: Misconception Reference

### Full Misconception List

| ID | Misconception | Description |
| :---- | :---- | :---- |
| \#1 | Unequal parts acceptable | Believes fractions don't require equal-sized parts |
| \#2 | Numerator \= total parts | Confuses numerator with denominator |
| \#3 | Fractions aren't numbers | Sees fractions as two separate numbers, not one value |
| \#4 | Larger denominator \= larger fraction | Believes 1/8 \> 1/4 because 8 \> 4 |
| \#5 | Fractions can't be \> 1 | Doesn't understand improper fractions |
| \#6 | Numerator \= denominator for "one whole" | Confusion about unit fractions and wholes |
| \#7 | Position on number line \= numerator only | Ignores denominator when placing fractions |
| \#8 | Different shapes can't show same fraction | Doesn't understand fraction equivalence across representations |
| \#9 | Adding fractions \= adding tops and bottoms | Treats numerator and denominator independently |
| \#10 | Fractions only apply to circles/pizzas | Limited mental model of fraction contexts |

### Tracking by Visual Type

Validators may specify visual context for more precise tracking:

- `Misconception_#3_RectangleBar`
- `Misconception_#3_NumberLine`
- `Misconception_#3_Grid`

These aggregate to the misconception level for Intervention triggers.

---

## END OF DOCUMENT

**Version:** 3.2
**Document Type:** Authoritative reference for script writers
**Major Changes from v2.0:**

- Simplified to two-track system (Non-MC generic, MC per-distractor)
- Removed three-type branching architecture
- Added Misconception Tracking & Intervention system overview
- Reduced content creation burden significantly
- Clarified MC structure (Medium per distractor \+ single Heavy)

**Major Changes from v3.1:**

- Clarified document scope: branching remediation requirements only, not validation requirements (Sections 1.5, 2.1, 9.1)
- Added explicit branching vs. validation distinction (Section 1.5): validator coverage is intentionally broader than branching; error causes are diagnosed from data, not assumed in advance
- Fixed version number discrepancy (header/footer now consistent)

**Major Changes from v3.0:**

- Added Multiselect MC as a third remediation track (Section 3B)
- Renamed "Multiple Choice" to "Single-Select MC" throughout for clarity
- Added Multiselect MC quality checklist (Section 12.2B)
- Added Multiselect MC output format example (Section 13.2B)
- Updated phase requirements table to include Multiselect MC column (Section 11.1)

**Related Documents:**

- Remediation Addition Prompt v3 (for Console Claude)
- Intervention Activity Design Brief (for Intervention creation)
- Edtech Activity Queue Rulebook (for queue placement)
- Visual Scaffolds TSV (for visual specifications)

**Maintenance:** Update version number and date when making changes

</remediation_design_ref>

----------------------------------------------------------------------

### Block 3: Reference Doc (references/lesson_script_schema_guide.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: references/lesson_script_schema_guide.md

<lesson_script_schema_guide>
# Lesson Script Schema Guide

Reference for the `lesson.json` script format. Covers every field, beat type, condition shape, and naming convention.

---

## Design Requirements

Two goals shape this schema.

### 1. Readability and Notion Portability

The format is human-readable first and machine-processed second. This makes it suitable for collaborative review in Notion, where non-engineers can read, comment on, and edit lesson content without touching raw JSON.

Key choices that serve this goal:

- **Plain-text content fields**: `dialogue.text` and `prompt.text` contain natural language, not markup or encoded content
- **Notion callout mapping**: each beat type maps to a specific Notion callout emoji (💬 dialogue, ❓ prompt, 🎬/🎞️ scene), so the JSON can round-trip to/from Notion without losing information on the editable fields
- **Selective editability**: only `dialogue.text` and `prompt.text` are editable in Notion; `scene` beats are display-only, so reviewers cannot inadvertently break structural logic
- **Human-readable IDs and slugs**: section IDs include a slug (e.g. `s1_1_most_votes`) so a reviewer can follow the navigation flow without reading code
- **`description` on validator states**: every validator state carries a plain-English description of the student condition it captures, making branching logic readable without interpreting condition syntax

### 2. Translatable Structured Data

The schema is an authored intermediate representation, not the final runtime format. It must be structured enough to be mechanically translated to a downstream schema (a runtime engine, a CMS, or a future schema revision).

Key choices that serve this goal:

- **Typed beats**: `type` is always explicit (`"dialogue"`, `"scene"`, `"prompt"`, `"current_scene"`), enabling switch-based translation with no ambiguity
- **Explicit targeting**: tangibles are always referenced by `tangible_id` or `tangible_type`, never by position or implicit state
- **No logic embedded in text**: conditions and branching live exclusively in `validator`; dialogue strings carry no conditional content
- **Flat, predictable field shapes**: each beat type has a fixed, documented field set; the only open-ended field is `params`, which is scoped to a specific `method` and documented
- **Validator as a declarative state machine**: validator states are a portable condition/goto structure with no runtime-specific implementation details, making them translatable to any branching execution model
- **IDs as the only coupling between sections**: sections are independent units; the schema makes no assumptions about execution order

These two goals can create tension: fully specified structured data tends toward verbosity, while readability pushes toward concision. The schema resolves this by separating concerns. Structural and logic fields are fully specified for translation fidelity, while human-facing fields (`text`, `description`, ID slugs) carry the readability load.

---

## Top-Level Structure

```json
{
  "id": "u3_m4_lesson",
  "sections": [ ... ]
}
```

| Field | Type | Description |
|---|---|---|
| `id` | string | Sequence identifier. See format below. |
| `sections` | array | Ordered list of all sections (main, transition, remediation) |

### Lesson ID Format

```
u{unit}_m{module}_{phase}

u3_m4_lesson
u3_m4_warmup
u3_m4_synthesis
u3_m4_practice
u3_m4_exitcheck
```

| Segment | Description |
|---|---|
| `u{n}` | Unit number |
| `m{n}` | Module number within the unit |
| `{phase}` | One of: `lesson`, `warmup`, `synthesis`, `practice`, `exitcheck` |

---

## Section

```json
{
  "id": "s1_1_most_votes",
  "type": "remediation",
  "beats": [ ... ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique section ID. See [Naming Conventions](#section-id-naming-conventions). |
| `type` | string | no | `"transition"` or `"remediation"`. Omit for normal sections. |
| `beats` | array | yes | Flat array of all beats in this section |

Every section begins with an empty screen. There is no carry-over from the previous section. Everything visible must be explicitly put on screen by `scene` beats before it appears.

### Step Groups

Beats are flat, but are logically grouped into **step groups** — a group of beats that play together before the lesson pauses for student interaction. Step groups are delimited by `current_scene` beats: a new step group begins after each `current_scene`.

Beat order within a step group:

1. **`scene`** — things appear or change on screen
2. **`dialogue`** — the guide speaks
3. **`prompt`** — student interacts (at most one per step group)
4. **`current_scene`** — snapshot of the screen after all beats have played (always last in a step group)

```json
"beats": [
  { "type": "scene", "method": "show", "tangible_id": "pg_fruits" },
  { "type": "dialogue", "text": "You made a graph with your Minis' votes." },
  { "type": "prompt", "text": "Which fruit got the most votes? Click it.", "tool": "click_category", "target": "pg_fruits", "validator": [...] },
  { "type": "current_scene", "elements": [...] },
  { "type": "dialogue", "text": "Apples got 6 votes, the most of any fruit." },
  { "type": "current_scene", "elements": [...] }
]
```

### Section ID Naming Conventions

```
s{group}_{seq}_{slug}              →  s1_1_most_votes
s{group}_{seq}{variant}_{slug}     →  s2_2a_fewest_books
s{group}_transition                →  s2_transition
```

| Segment | Description |
|---|---|
| `s` | Fixed prefix |
| `{group}` | Concept group number, local to the unit/module, not the phase |
| `{seq}` | Sequence position within the group |
| `{variant}` | Optional letter suffix for sub-problems, e.g. `a`, `b`, `c` |
| `{slug}` | Human-readable label for the problem |

**Key rules:**
- Section IDs are **sequential**: `{group}` and `{seq}` reflect the order sections appear in the phase
- Some sections are **misconception specific**: written to address a known error pattern
  rather than advancing the main concept sequence

---

## Beat Types

### Scene

**Scene beats are the only way to change screen state.** If anything needs to appear, disappear, animate, or update — a tangible, a parameter, any visual state at all — it must come from a `scene` beat.

Display-only in Notion (🎬 callout for all methods).

Three targeting levels. Omit fields to broaden scope:

| Target | Fields present |
|---|---|
| Specific instance | `tangible_id` |
| All instances of a type | `tangible_type` |
| All instances on screen | neither |

`add` is the exception: it always requires both `tangible_id` and `tangible_type`.

Interactivity is **implicit**. A tangible becomes interactive when a prompt's `tool` targets it, and resets automatically when the prompt resolves. Use `lock`/`unlock` only for edge cases that need explicit control.

| Method | Notion icon | `params` fields | Description |
|---|---|---|---|
| `show` | 🎬 | — | Make tangible visible |
| `hide` | 🎬 | — | Remove tangible from view |
| `animate` | 🎬 | `event`, `status`, `description`, ...tangible-specific | Trigger a named animation |
| `update` | 🎬 | `description: string` (required), ...tangible-specific | Change toy state (highlighting, mode switch, template change, etc.) |
| `add` | 🎬 | tangible-specific config (optional) | Add a new instance to the scene |
| `remove` | 🎬 | — | Remove a tangible instance from the scene |
| `lock` | 🎬 | — | Prevent student interaction regardless of active prompt |
| `unlock` | 🎬 | — | Re-enable student interaction on a locked tangible |

**show / hide**
```json
{ "type": "scene", "method": "show", "tangible_id": "pg_fruits" }
{ "type": "scene", "method": "hide", "tangible_id": "data_table" }
```

**animate: specific instance**
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_id": "bg_animals",
  "params": {
    "event": "draw_bar_guideline",
    "status": "proposed",
    "description": "Guideline draws from top of Monkeys bar to axis",
    "category": "Monkeys"
  }
}
```

**animate: all instances of a type**
```json
{
  "type": "scene",
  "method": "animate",
  "tangible_type": "picture_graph",
  "params": {
    "event": "transform_to_bar_graph",
    "status": "proposed",
    "description": "All picture graphs collapse into bar graphs"
  }
}
```

**update**
```json
{
  "type": "scene",
  "method": "update",
  "tangible_id": "bg_colors",
  "params": {
    "highlight_categories": ["Blue", "Yellow"],
    "description": "Blue and Yellow bars highlight."
  }
}
```

`params.description` is required on every `update` beat — plain English of what visually changes. Include any additional toy-specific state fields alongside it.

**add**
```json
{
  "type": "scene",
  "method": "add",
  "tangible_id": "numline_a",
  "tangible_type": "number_line",
  "params": { "min": 0, "max": 2 }
}
```

**remove**
```json
{ "type": "scene", "method": "remove", "tangible_id": "numline_a" }
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"scene"` | yes | |
| `method` | string | yes | `show` `hide` `animate` `update` `add` `remove` |
| `tangible_id` | string | conditional | Instance ID. Required for `add`. Omit to broaden scope to type or all. |
| `tangible_type` | string | conditional | Required for `add`. Omit to broaden scope to all instances on screen. |
| `params` | object | no | Method-specific configuration; omit when not needed |

---

### Dialogue

Narration or teacher speech. Editable in Notion (💬 callout).

```json
{
  "type": "dialogue",
  "text": "You made a graph with your Minis' votes. Each picture stands for one vote."
}
```

```json
{
  "type": "dialogue",
  "text": "Here's a graph: animals at the zoo. Every picture graph has a key that tells you what each symbol means.",
  "tags": ["vocabulary"]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"dialogue"` | yes | |
| `text` | string | yes | Spoken/displayed text |
| `tags` | string[] | no | Semantic labels, e.g. `["vocabulary"]` |

---

### Prompt

Student interaction point. Text is editable in Notion (❔ callout).

**Workspace tool: single tangible**
```json
{
  "type": "prompt",
  "text": "Which fruit got the most votes? Click it.",
  "tool": "click_category",
  "target": "pg_fruits",
  "validator": [...]
}
```

**Workspace tool: specific component**
```json
{
  "type": "prompt",
  "text": "Click on the part that tells us what each symbol means.",
  "tool": "click_component",
  "target": "picture_graph_animals.key",
  "validator": [...]
}
```

**Workspace tool: explicit list of tangibles**
```json
{
  "type": "prompt",
  "text": "Which graph shows the most cats?",
  "tool": "click_tangible",
  "target": ["pg_fruits", "pg_animals", "pg_pets"],
  "validator": [...]
}
```

**Workspace tool: all tangibles of a type**
```json
{
  "type": "prompt",
  "text": "Which graph shows the most cats?",
  "tool": "click_tangible",
  "target": { "type": "picture_graph" },
  "validator": [...]
}
```

**Overlay tool**: generates its own UI, no tangible target.
```json
{
  "type": "prompt",
  "text": "How many monkeys are at the zoo?",
  "tool": "multiple_choice",
  "options": [5, 6, 7, 8],
  "validator": [...]
}
```

```json
{
  "type": "prompt",
  "text": "Select all the categories you need to answer this question.",
  "tool": "multi_select",
  "options": ["Dogs", "Cats", "Fish", "Birds", "Lizards"],
  "validator": [...]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `"prompt"` | yes | |
| `text` | string | yes | Question or instruction shown to student |
| `tool` | string | yes | `click_category` · `click_component` · `click_tangible` · `multiple_choice` · `multi_select` |
| `target` | string \| string[] \| object | conditional | What the tool acts on. Omit for overlay tools. See shapes below. |
| `options` | array | conditional | Overlay tools only: `multiple_choice` and `multi_select`. Numbers or strings. |
| `validator` | array | yes | See [Validator](#validator) |

**`target` shapes:**

| Shape | When to use | Example |
|---|---|---|
| `"tangible_id"` | Single tangible instance | `"target": "picture_graph_fruits"` |
| `"tangible_id.component"` | Specific component within a tangible | `"target": "picture_graph_animals.key"` |
| `["id1", "id2"]` | Explicit list of selectable instances | `"target": ["pg_fruits", "pg_animals"]` |
| `{ "type": "..." }` | All instances of a tangible type | `"target": { "type": "picture_graph" }` |

---

### current_scene

Always the last beat in every step group. It is a pure derived snapshot: it reflects only what `scene` beats have established. Within a section, tangibles carry forward step to step — a tangible stays on screen until a `scene` beat removes or hides it. `current_scene` never introduces new tangibles or state that no `scene` beat has declared.

```json
{
  "type": "current_scene",
  "elements": [
    {
      "tangible_id": "picture_graph_fruits",
      "description": "Horizontal picture graph. Favorite Fruits data. Apples row highlighted.",
      "tangible_type": "picture_graph",
      "mode": "reading",
      "orientation": "horizontal",
      "categories": ["Apples", "Bananas", "Oranges", "Grapes"]
    }
  ]
}
```

If the screen is empty, write `"elements": []`.

---

### empty

Used in validator state `beats` arrays to signal that no feedback is needed for this state. Preferred over an empty array (`[]`) because it makes the intent explicit — this state is intentionally silent, not accidentally incomplete.

```json
{ "type": "empty" }
```

Only valid inside validator state `beats`. Not used in outer section beats.

---

## Validator

A flat array of states evaluated **in order**; the first match wins. The final state is always an empty condition (`{}`) catch-all. Each state contains inline `beats`, which play when the state matches.

Every state must include `is_correct: true` or `is_correct: false`. `incorrect_count` is the one system parameter; all other condition keys are tangible-specific fields.

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student selected Apples",
    "is_correct": true,
    "beats": [
      { "type": "scene", "method": "animate", "tangible_id": "pg_fruits",
        "params": { "event": "highlight_category", "status": "confirmed",
                    "description": "Apples row highlights to confirm selection", "category": "Apples" } },
      { "type": "dialogue", "text": "Apples got 6 votes, the most of any fruit." },
      { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
    ]
  },
  {
    "condition": { "incorrect_count": 1 },
    "description": "Student selected any wrong answer on first attempt",
    "is_correct": false,
    "beats": [
      { "type": "dialogue", "text": "Look at the numbers next to each row. Which one is biggest?" },
      { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Picture graph unchanged.", "tangible_type": "picture_graph" } ] }
    ]
  },
  {
    "condition": { "incorrect_count": 2 },
    "description": "Student selected any wrong answer on second attempt",
    "is_correct": false,
    "beats": [
      { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
        "params": { "highlight_categories": ["Apples"], "description": "Apples row highlights." } },
      { "type": "dialogue", "text": "Count the Apples row: 6 symbols. Count the others: Bananas 4, Oranges 5, Grapes 3. Which row has the most?" },
      { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
    ]
  },
  {
    "condition": {},
    "description": "Catch-all: any remaining state",
    "is_correct": false,
    "beats": [
      { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
        "params": { "highlight_categories": ["Apples"], "description": "Apples row highlights." } },
      { "type": "dialogue", "text": "Apples has 6 symbols, more than any other row. Click Apples." },
      { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
    ]
  }
]
```

| Field | Type | Description |
|---|---|---|
| `condition` | object | Matching condition. Multiple keys implicitly ANDed. Use `or`/`and` arrays for explicit logic. |
| `description` | string | Precise plain-English description of exactly what student state this condition captures. |
| `is_correct` | boolean | **Required.** `true` if this state represents a correct student response, `false` otherwise. |
| `beats` | array | Flat array of beats to play when this state matches. Same structure as section `beats`. |

### Condition Parameters

| Parameter | Type | Description |
|---|---|---|
| `selected` | string \| number | What the student selected from the tool's available options |
| `incorrect_count` | number | System counter: how many times the student has triggered a non-first-match state on this prompt. Max 3. |
| `tangible_id` | string | Scopes remaining keys to a specific tangible instance. Used when checking tangible state fields directly. |
| *(tangible fields)* | any | State fields exposed by the scoped tangible, used alongside `tangible_id` |

### Condition Logic

**Single tangible check:**
```json
{ "condition": { "selected": "Bananas", "incorrect_count": 1 } }
```

**Specific tangible field check:**
```json
{ "condition": { "tangible_id": "numline_a", "shaded_interval_count": 3 } }
```

**Multiple tangibles (AND):**
```json
{
  "condition": {
    "and": [
      { "tangible_id": "bar_a", "points": [1, 2] },
      { "tangible_id": "numline_a", "shaded_interval_count": 3 }
    ]
  }
}
```

**OR across values:**
```json
{ "condition": { "or": [{ "selected": "Oranges" }, { "selected": "Grapes" }] } }
```

**Negation:**
```json
{ "condition": { "not": { "selected": "Apples" } } }
```

**Fallback: empty object; always matches:**
```json
{}
```

---

## Remediation Pattern

Remediation is inline. Feedback beats live directly in validator states, not in separate sections. The three-level scaffold maps to `incorrect_count` values:

| Validator state | Hint style |
|---|---|
| `incorrect_count: 1` | Light: minimal nudge, direct attention without revealing the answer |
| `incorrect_count: 2` | Medium: partial reveal, show the key data, let the student conclude |
| catch-all `{}` | Heavy: full scaffold, state the answer explicitly, prompt to confirm |

Each state's `beats` contains the beats for that hint level. See the [Validator](#validator) section for a full example.

---

## Tangible ID Conventions

Tangible ID prefixes and naming patterns are defined in the toy spec files (`toy_specs/`). Consult the relevant toy spec for the canonical prefix and any instance-naming rules for that toy type.

---

## Beat Summary

| Type | Notion format | Editable | Fields |
|---|---|---|---|
| `scene` | 🎬 callout | no | `method`, `tangible_id`, `params?` |
| `dialogue` | 💬 callout | yes: `text` | `text`, `tags?` |
| `prompt` | ❔ callout | yes: `text` | `text`, `tool`, `options?`, `validator` |
| `current_scene` | 📋 toggle | no | `elements` |
| `empty` | plain text suffix | no | — (validator beats only) |

</lesson_script_schema_guide>

----------------------------------------------------------------------

### Block 4: Reference Doc (dialogue_examples/remediations.md)
Purpose: Reference documentation
Cacheable: Yes

# REFERENCE DOCUMENTATION: dialogue_examples/remediations.md

<remediations>
# Remediation Beats — Gold Standard Examples

Remediation beats fire when a student answers incorrectly. Three levels: light, medium, heavy.

- **Light:** Minimal redirect. Assumes the student is close and just needs a nudge.
- **Medium:** More targeted. Identifies what to look at or re-route their thinking.
- **Heavy:** Full model. Guide demonstrates the action or reasoning, then hands it back.

---

## Design Principles

**Light remediations are direct statements, not questions.** Statements redirect; questions can feel like testing. "Look again at the parts in the bars. They all need to be the same width." — not "Are they all the same width?"

**Medium remediations teach the method, not the answer.** Name what to look at and in what order without supplying the counts or values. The student still has to do the work. Close with a pointed question or specific imperative.

**Heavy remediations model reasoning, not just the answer.** Narrate the thinking during the demo. End with the underlying principle — why the answer has to be what it is, not just what it is.

**"You're working on it" used sparingly.** It works when genuine as a gentle acknowledgment before redirecting. Avoid using it in every medium remediation — it becomes formulaic.

---

## Gold Standard Examples by Level

### LIGHT REMEDIATIONS

**Simple count redirect (M10)**
> "Try counting which bar has more sixths shaded."

Why it works: One sentence. Names exactly what to do. No hedging.

---

**Count from zero (M11)**
> "Count the intervals from zero. We need two intervals."

Why it works: Tells the student the method and the target. Unambiguous.

---

**Size comparison redirect (M11)**
> "Not quite. Both show 3 pieces. But look at the SIZE of those pieces."

Why it works: "Not quite" acknowledges the error without dwelling on it. Capitalizing SIZE in the spoken version should be read as mild vocal emphasis.

---

**Equal parts check (M1)**
> "Look again at the parts in the bars. They all need to be the same width."

Why it works: Removed the old "Hmm" and rhetorical question. Direct statement of what to look for.

---

**Strategy reminder (M5)**
> "Not quite. Remember, six equal spaces."

Why it works: Minimum viable redirect when the strategy has already been taught. Doesn't re-explain.

---

### MEDIUM REMEDIATIONS

**Piece size comparison with visual anchor (M2)**
> "Let's compare - see how the one half piece is much bigger than the one fourth piece? Fewer parts means bigger pieces."

Why it works: "Let's compare" is collaborative. Points to the visual, then states the principle. Short.

---

**Denominator as jump size (M6)**
> "Remember that five fourths means five equal jumps total from 0. Count them carefully."

Why it works: Restates the meaning of the fraction in terms of the action (counting jumps). "Count them carefully" is actionable.

---

**Same-denominator logic restated (M10)**
> "Both pieces are divided into sixths, so the pieces are the same size. Which is more, four pieces or two pieces?"

Why it works: Walks through the logic step by step. Ends with a question the student can answer — gives them agency in the correction.

---

**Half vs more-than-half framing (M12)**
> "Remember from the warmup, three fourths was above halfway and two sixths was below. The number line shows the same thing, just in a different way."

Why it works: Connects to something the student already saw. The transfer is explicit: "same thing, different way."

---

**Numerator = spaces from zero (M5)**
> "Here's a hint: The top number, 1, means one sixth is one space from 0."

Why it works: "Here's a hint" signals that the next thing is help, not correction. Restates the fraction-as-position concept precisely.

---

### SPECIFIC CONDITION MEDIUMS (per-distractor)

Specific condition mediums fire when the student makes an identifiable wrong choice. They name the error precisely, redirect to the correct concept, and close with a call to action. They do not complete the work — the student still has to execute.

**Pattern A — Credit + narrow (M11)**
> "You're right that there are 4 columns. But count how many dots are in each column. Are there 4?"

Why it works: Opens by crediting what was correct. Narrows to exactly the one thing that was wrong. Ends with a pointed question the student can immediately act on.

---

**Pattern A — Credit + narrow, two-step problem (M1)**
> "That's the Fish and Lizards total. The question asks how many MORE have Cats. You need to compare Cats to that total."

Why it works: Names what the student found (a correct partial result). Redirects to what the question actually asks. One clear action.

---

**Pattern B — Name + redirect + point (M1)**
> "You counted the Dogs. When we ask how many fewer, we need to find the difference. Count how far apart Dogs and Fish are."

Why it works: One-phrase description of the error. States what the question needs. Points to the evidence in the visual.

---

**Pattern B — Name + redirect + point (M11)**
> "That's the rows description. Look at columns now. How many columns are there? Each column has how many dots?"

Why it works: Names the error (described rows when asked for columns). Redirects with a direct imperative. Ends with two questions that walk the student through the correct path step by step.

---

### HEAVY REMEDIATIONS

**Reasoning narrated during demo (M8)**
> "Let me show you by selecting the bigger piece. I'm choosing the one-fourth piece because when we cut the same cake into fewer pieces, each piece is bigger."

Why it works: States the action and the reason simultaneously. The student sees what to do AND why. Ends with the principle, not the action.

---

**Step-by-step counting on number line (M10)**
> "Let me show you how I'd solve this: On number lines, fractions get bigger as you move right. Look — two sixths only goes two intervals from 0. But five sixths goes five intervals from 0, almost to 1. The one that goes farther right is bigger. So five sixths is greater."

Why it works: Narrates the visual observation the student should be making. "Almost to 1" anchors the magnitude. Ends with a clear conclusion.

---

**Pattern revealed through modeling (M6)**
> "Let me help a bit more. Look at this pattern: four fourths equals 1 whole, they're the same number. Another four fourths makes another whole. So eight fourths equals 2. Same number, different ways to write it. The pattern tells you something. Every four fourths makes a whole number!"

Why it works: "Let me help a bit more" is warmer than "Let me show you." The demo reveals a pattern rather than just demonstrating a procedure. The exclamation is earned — this is a genuine discovery moment.

---

**Equivalent fraction by counting steps (M9)**
> "Let me help you think through this. Three halves means: one half, two halves — that's 1 — then three halves, lands here between 1 and 2. Now count fourths: one fourth, two fourths, three fourths, four fourths — that's 1 — five fourths, six fourths, lands at the same spot. So six fourths is the answer."

Why it works: Walks both number lines step by step. The student can follow the counting. Ends with the conclusion stated plainly.

---

**Collaborative walkthrough framing (M1)**
> "I'll walk us through this problem: First I divide in half, then I divide the left half, then the right half. See how all four parts match?"

Why it works: "I'll walk us through this" is collaborative. The step-by-step mirrors the strategy taught earlier. The closing question invites the student to verify, not just observe.

---

**Counting both lines together (M9)**
> "Let's work together. For two thirds: count one third, two thirds. Two thirds goes here. Two-thirds of the way from 0 to 1. For four sixths: count one sixth, two sixths, three sixths, four sixths. Same position! When dots line up vertically, fractions are equivalent."

Why it works: Does both number lines step by step. "Same position!" is earned here. Ends with the rule the student should take away.

---

**Principle ending — two paths modeled (M11)**
> "Let me show you the two ways to think about this array. If I want rows, I count the horizontal rows: 6 rows. Then I count the dots in one row: 3 dots. 6 rows of 3 is 18 total dots. 6 times 3 equals 18. If I want columns, I count the vertical columns: 3 columns. Then I count the dots in one column: 6 dots. 3 columns of 6 is 18 total dots. 3 times 6 equals 18. Two ways to describe this array and equations that match. Both are correct."

Why it works: Models both valid paths, not just one. Names the structure at each step ("horizontal rows", "vertical columns"). Ends with the principle — the student leaves knowing the rule, not just the answer.

---

**Principle ending — invariant stated (M12)**
> "Here's what matters: when you describe an array by rows or columns, the dots don't change. 3 times 5 has the exact same dots as 5 times 3. You just read them differently. Same dots means same total. That is why both expressions give the same product."

Why it works: States the principle and explains why it must be true. The closing sentence ("Same dots means same total. That is why...") is the insight the student carries forward.

---

## Remediation Register Notes

**Light:** One or two sentences. No explanation of why the answer was wrong. Just a redirect.

**Medium:** Two to four sentences. Teaches the method — names what to look at and in what order — without supplying the specific counts or values. Visual scaffold required. Closes with a pointed question or specific imperative. Does not solve the problem.

**Specific Condition Medium:** Same length and visual requirement as Medium. Names the error in one phrase, redirects to the correct concept, closes with a call to action. Does not give away the correct counts or values.

**Heavy:** Models the full solution. Narrates the thinking, not just the mechanics — names the structure being demonstrated. Ends with the underlying principle: why the answer has to be what it is.

**On-correct and Heavy share a closing philosophy:** both end by naming what was demonstrated, not just what the answer was. Heavy closes with why (the structural insight). On-correct closes with what was demonstrated (the discovery or principle the student just proved). The closing sentence should be transferable to the next problem.

**All levels:** Avoid "You're almost there!" (assuming closeness) and "Don't worry!" (assuming feelings).

</remediations>

----------------------------------------------------------------------

### Block 5: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

The section to process is in `<input>`. Walk its `beats` array and find every `prompt` beat. For each prompt, generate the incorrect validator states. Output one inner array of states per prompt, in the order the prompts appear in the section.

**Skip any prompt whose `validator` is a single state with `condition: {}`** (any-response-advances). Emit nothing for it.

**Do NOT skip a `multiple_choice` prompt just because its validator only contains the correct state.** A `multiple_choice` validator that has only one `is_correct: true` state with `condition: { "selected": "..." }` means the wrong-answer states haven't been written yet — that is exactly what you are here to generate. The absence of pre-existing `is_correct: false` states is normal, not a signal to skip.

---

## OUTPUT FORMAT

An array of arrays. One inner array per qualifying prompt, in section order:

```json
[
  [ <states for prompt 0> ],
  [ <states for prompt 1> ]
]
```

Each state follows the validator state schema:
```json
{
  "condition": { ... },
  "description": "...",
  "is_correct": false,
  "steps": [ [ <beats> ] ]
}
```

`is_correct` must be `false` on every state you generate.

---

## STEP 1: DETECT QUESTION TYPE

For each qualifying prompt, check the `tool` field:

| `tool` | Track |
|---|---|
| `click_category`, `click_tangible`, `click_component`, or any workspace tool | **Non-MC** → Generic L-M-H |
| `multiple_choice` | **Single-Select MC** → Per-distractor Medium + Heavy |
| `multi_select` | **Multiselect MC** → Per-branch Medium + Heavy |

---

## STEP 2A: NON-MC: STATES

Follow `<remediation_design_ref>` Sections 2.4–2.5 for state structure and order. Always emit generic L/M/H after any specific-condition states. Follow length, visual, and language rules from `<remediation_design_ref>` Sections 4–6.

**Specific conditions** are pre-defined in the input — do not invent them. Inspect the existing `validator` for `is_correct: false` states with non-empty conditions (not just `{}`). Each such state has:
- `condition`: the base condition (e.g. `{ "container_count": 3 }`) — rewrite it into the `and`/`or` shape from the STATE ORDER section below
- `description`: a plain-English label for what wrong answer this represents
- `beats`: placeholder dialogue already written — use as inspiration when writing Medium-quality content (visual scaffold + 20–30 words)

For each specific condition, emit one state using the `and`/`or` condition shape from the STATE ORDER section below. Write or rewrite the dialogue and scene beats to Medium standard — do not just copy the placeholder beats verbatim.

**Two effective patterns for specific condition dialogue:**

- **Pattern A — Credit + narrow:** When the student got part right, acknowledge it, then narrow to the specific error. Close with a pointed question.
  > "You're right that there are 4 columns. But count how many dots are in each column. Are there 4?"

- **Pattern B — Name + redirect + point:** Name what the student did in one phrase, redirect to the correct concept, give one concrete action or question.
  > "You counted the Dogs. When we ask how many fewer, we need to find the difference. Count how far apart Dogs and Fish are."

In both patterns: the Medium answer rule applies — do not give the correct counts or values. The student still has to execute.

**Light** (`incorrect_count: 1`): dialogue only.
```json
{
  "condition": { "incorrect_count": 1 },
  "description": "Student answered incorrectly on first attempt",
  "is_correct": false,
  "steps": [
    [ { "type": "dialogue", "text": "..." } ]
  ]
}
```

**Medium** (`incorrect_count: 2`): scene beat required. Dialogue teaches the method — name what to look at and in what order. Close with a pointed question or specific imperative.
```json
{
  "condition": { "incorrect_count": 2 },
  "description": "Student answered incorrectly on second attempt",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

**Scenario image prompts (`click_tangible` on `image` tangibles):** When the prompt targets scenario images (real-world connection sections), never reference images by letter label in any state. For each state that needs to draw attention to a specific image, emit a `scene animate` beat with `event: "highlight"` on that tangible ID, then say "this image" in the dialogue. Apply this in Medium states (highlight the specific wrong or correct image) and Heavy states (highlight each relevant image in sequence as the guide narrates).

```json
{ "type": "scene", "method": "animate", "tangible_id": "scenario_image_counting",
  "params": { "event": "highlight", "status": "confirmed", "description": "Counting money scenario image highlights." } },
{ "type": "dialogue", "text": "Look at this image. Does this situation use groups of 10?" }
```

**Heavy** (catch-all `{}`): `scene animate` beat required (system demonstrates the answer). Dialogue narrates the thinking, not just the mechanics — name the structure being demonstrated and connect each step to what it means. End with the underlying principle: why the answer has to be what it is, not just what the answer is.

**For the on_correct beat:** use it only to identify what concept the answer demonstrates and what the closing principle should be. Do not treat it as a template for which tangibles to animate — it only shows the confirmation step, not the reasoning.

**For the Heavy's animate beats:** read the section's `scene add` beats and the dialogue beat that introduces the prompt. These tell you which tangibles are part of the reasoning and what each one contributes (line counts, axis values, etc.). The Heavy must animate every tangible involved in the reasoning — in the order the section presents them — and narrate what the guide observes about each one, arriving at the correct answer as the conclusion.

**Use `<section_context>` to confirm the teaching strategy and align vocabulary.** If the section context shows that the guide's teaching walked through multiple visuals in sequence, the Heavy's animate beats must follow that same sequence.
```json
{
  "condition": {},
  "description": "Student answered incorrectly three or more times. System models the answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STEP 2B: SINGLE-SELECT MC: PER-DISTRACTOR STATES

The correct option is in the correct state's `condition.selected`. All other values in `tool.options` are distractors.

**Derive distractors explicitly:** take the full `options` array and remove any value that appears as `condition.selected` in an `is_correct: true` validator state. Every remaining option is a distractor that requires a Medium state. Do this even if no `is_correct: false` states exist yet in the validator.

See `<remediation_design_ref>` Section 3.2 for Single-Select MC structure (no Light state; per-distractor Mediums + one Heavy). Per that design, the condition for each Medium is `{ "selected": <distractor> }` only. Do not add `incorrect_count` — per-distractor and LMH are separate branching dimensions and must never be combined.

One **Medium** per distractor: scene beat required. Dialogue names the error and redirects to the correct concept or tool. Close with a pointed question or specific imperative.
```json
{
  "condition": { "selected": <distractor> },
  "description": "Student selected <distractor>: <why this is wrong>",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required.
```json
{
  "condition": {},
  "description": "Student answered incorrectly. System models the correct answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STEP 2C: MULTISELECT MC: PER-BRANCH STATES

Identify **correct answers** from the success/correct validator state condition — these are the values listed under `selected` clauses. **Incorrect answers** are values listed under `not_selected` clauses in that same condition.

**First, detect the no-wrong-options variant:** Count `not_selected` clauses in the correct validator condition. If there are **none**, all options are correct — no wrong options exist. Follow Section 3B.9 of `<remediation_design_ref>` and emit only Branch 2 + Heavy. Do NOT invent phantom wrong option values.

For the **no-wrong-options variant**, every possible error is an under-selecting error — so use `incorrect_count` conditions (same as Non-MC L/M/H). Do NOT use Branch 2/3/4 conditions.

**Light** (`incorrect_count: 1`) — dialogue only:
```json
{
  "condition": { "incorrect_count": 1 },
  "description": "Student has not selected all correct answers (first attempt)",
  "is_correct": false,
  "steps": [
    [ { "type": "dialogue", "text": "..." } ]
  ]
}
```
Use a short nudge (10–20 words) pointing toward completeness — e.g. "Read the scenarios carefully. Did you select ALL?" Adapt to the content.

**Medium** (`incorrect_count: 2`) — scene beat required:
```json
{
  "condition": { "incorrect_count": 2 },
  "description": "Student has not selected all correct answers (second attempt)",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

**Heavy** (`condition: {}`) — `scene animate` beat required. Models all correct answers.

For the **standard variant** (has at least one `not_selected` clause = has wrong options), identify all options not listed as `selected` in the correct condition as incorrect answers. See `<remediation_design_ref>` Section 3B for structure, branch definitions, language requirements, and condition patterns (no Light; Branches 2/3/4 Mediums + one Heavy).

One **Medium per branch**: scene beat required.
```json
{
  "condition": { <see Section 3B.7 for correct condition logic per branch> },
  "description": "Branch <N>: <description of student's selection state>",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "update", "tangible_id": "...", "params": { "highlight_categories": ["..."] } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

One **Heavy** (`condition: {}`): `scene animate` beat required. Shared fallback for all branches.
```json
{
  "condition": {},
  "description": "Student answered incorrectly. System models the correct answer.",
  "is_correct": false,
  "steps": [
    [
      { "type": "scene", "method": "animate", "tangible_id": "...",
        "params": { "event": "...", "status": "confirmed", "description": "..." } },
      { "type": "dialogue", "text": "..." }
    ]
  ]
}
```

---

## STATE ORDER

**Non-MC inner array:**
1. One Medium per specific condition (if any) — `{ "and": [{ specific_condition }, { "or": [{"incorrect_count": 1}, {"incorrect_count": 2}] }] }`
2. Generic Light — `{ "and": [{"incorrect_count": 1}, {"not": { specific_condition }}, ...] }` (one `not` per specific condition)
3. Generic Medium — `{ "and": [{"incorrect_count": 2}, {"not": { specific_condition }}, ...] }` (one `not` per specific condition)
4. Generic Heavy (`condition: {}`): always last

**Single-Select MC inner array:**
1. One Medium per distractor (any order among themselves)
2. Heavy (`condition: {}`): always last

**Multiselect MC inner array (standard — has wrong options):**
1. Branch 2 Medium — under-selecting
2. Branch 3 Medium — all-wrong
3. Branch 4 Medium — mixed
4. Heavy (`condition: {}`): always last

**Multiselect MC inner array (no-wrong-options variant — zero `not_selected` in correct condition):**
1. Light — `{ "incorrect_count": 1 }` — dialogue only
2. Medium — `{ "incorrect_count": 2 }` — scene beat required
3. Heavy — `condition: {}` — always last

---

## LANGUAGE RULES

Follow all language patterns, word counts, visual requirements, and prohibited constructs from `<remediation_design_ref>` Sections 4–8 and 12.4.

**Light:** Use openers from Sections 4.1–4.2. Cycle — do not reuse the same phrase within a section.

**Medium:** Use a starter from Section 5.1. Cycle — do not reuse within a section.

**Medium — universal answer rule (applies to all tracks and specific conditions):** Never state the correct answer, value, or count in a Medium. This applies even when the answer is visible on screen (e.g. a key showing "Each ⭐ = 5", a label, a highlighted number). Redirect the student to the right place and let them read it. A Medium that names the answer removes the work the student needs to do. If you find yourself writing the correct value in a Medium, rewrite it as a question or imperative that sends the student to look.

**Heavy:** Choose an opener from Section 6.1. Rotate across the full range of available openers — "Let me show you", "Let me help you think through this", "Let's work together", "I'll walk us through this", "Here's what matters" — treating each as equally valid. Cycle — do not reuse the same opener within a section. Refer to <remediations.md> for opener variety and the principle-ending pattern. End with closure per Section 7.

---

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Do not reference concepts from <advanced_concepts>. Reference <required_phrases> in Medium/Heavy where genuinely appropriate. Ground explanations in <the_one_thing>. Keep tangible references consistent with the section's `scene` array and existing scene beats. **Do not fabricate game data values** — specific quantities, scale-key values, or item counts that come from live game content are not available at script-writing time unless they appear explicitly in the input section JSON or `<lesson_sections>`. Do not invent them. In Light and Medium states, redirect the student to look at the relevant element rather than stating a value. In Heavy states, narrate the structural pattern being animated without naming specific quantities that aren't grounded in the input.

When <lesson_sections> is available, use it to align correction language with how the lesson taught the concept — match the vocabulary the guide used in earlier sections and frame corrections in terms the student has already encountered.

When <section_context> is available, read every section summary whose `## section_id` appears before the current section's id. Identify the most recently taught strategy: what approach did the guide use to explain the concept, what scaffold did it provide, what vocabulary did it lean on? Use that strategy — and only that strategy — to frame remediation. Do not introduce a shortcut, pattern, or reasoning method that does not appear in any prior section summary. If a student is stuck on `s2_5`, the remediation should teach using the same scaffold introduced in `s2_1`–`s2_4`, not a rule the lesson hasn't covered yet.

For prompts with `"variable_answer": true`: do not assume the student's specific attempt in Light or Medium dialogue. For Heavy, model one specific valid example but frame it as one way, not the only answer.

---

## OUTPUT RULES

- Output ONLY the `incorrects` array content. No explanation, no markdown fences.
- **Flag placeholders and uncertain content:** When a beat or validator state contains content that could not be grounded in the input — game data values not present in the section JSON or `<section_context>`, unresolved visual elements, invented quantities — add `"flag": "placeholder — <brief reason>"` to that beat or state object. This makes uncertain content findable for human review without blocking output. Example: `"flag": "placeholder — scale key values not in input"`.
- The prefill already opens `{"id": "...", "incorrects": [`. Complete from that point.
- Use double quotes throughout
- `is_correct: false` on every state
- Do not use em dashes (—) or double hyphens (--) in any text field; to create a pause or connect two thoughts, use a period or comma instead



----------------------------------------------------------------------

### Block 6: Output Schema
Purpose: Defines expected output structure
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

# OUTPUT STRUCTURE

<output_structure>

{
  "id": "s1_1_most_votes",
  "incorrects": [
    [
      {
        "condition": { "incorrect_count": 1 },
        "description": "Student clicked a wrong category on first attempt",
        "is_correct": false,
        "steps": [
          [ { "type": "dialogue", "text": "Not quite. Look at the numbers next to each row." } ]
        ]
      }
    ]
  ]
}

</output_structure>

----------------------------------------------------------------------

### Block 7: Context
Purpose: Pipeline-injected context (e.g. lesson sections)
Cacheable: Yes
*[CACHED: {'type': 'ephemeral'}]*

<lesson_sections>
[
  {
    "id": "s1_1_transition_warmup",
    "type": "transition",
    "beats": [
      {
        "type": "dialogue",
        "text": "In Warmup, all four scales worked for your data. You had options!"
      },
      {
        "type": "dialogue",
        "text": "But what happens when the numbers are bigger? Let's find out."
      },
      {
        "type": "current_scene",
        "elements": []
      }
    ],
    "flag": "placeholder — visual references 'Scale Preview System from Warmup' but workspace_specs lists no toys; no scene beats generated as toy spec not defined and prior section summaries not provided",
    "_generated_at": "2026-05-05T18:15:23.701907+00:00"
  },
  {
    "id": "s1_2_when_scale_needs_too_many",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "categories": [
            "Aisha",
            "Ben",
            "Carlos",
            "Dana"
          ],
          "values": [
            20,
            35,
            55,
            80
          ],
          "description": "Data table appears. Books Read This Month. Aisha: 20, Ben: 35, Carlos: 55, Dana: 80."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_books",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "vertical",
          "categories": [
            "Aisha",
            "Ben",
            "Carlos",
            "Dana"
          ],
          "axis_range": [
            0,
            50
          ],
          "scale": 5,
          "description": "Vertical bar graph appears. Axis shows 0 to 50. Scale of 5 pre-selected. Graph initially empty."
        }
      },
      {
        "type": "dialogue",
        "text": "Here's data about how many books four students read this month. Dana read the most—80 books!"
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph. Axis 0-50. Scale of 5 selected. Graph empty.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              50
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Let me try Scale of 5 and see what happens."
      },
      {
        "type": "scene",
        "method": "animate",
        "tangible_id": "bar_graph_books",
        "params": {
          "event": "generate_preview",
          "status": "confirmed",
          "description": "Preview generates. Aisha (20), Ben (35), Carlos (55) bars appear. Dana's bar (80) extends past graph boundary. Warning indicator appears."
        }
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph. Aisha, Ben, Carlos bars visible. Dana's bar extends past top. Warning indicator present.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              50
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Hmm. Carlos's bar is just above my graph, but Dana's bar goes past the top. The graph only goes up to 50 right now."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph. Aisha, Ben, Carlos bars visible. Dana's bar extends past top. Warning indicator present.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              50
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "I COULD make the graph taller to fit 80. Let's see... I'd need 55, 60, 65, 70, 75, 80..."
      },
      {
        "type": "scene",
        "method": "animate",
        "tangible_id": "bar_graph_books",
        "params": {
          "event": "extend_axis",
          "status": "confirmed",
          "description": "Axis extends upward. Tick marks appear: 55, 60, 65, 70, 75, 80. Axis now crowded with many tick marks."
        }
      },
      {
        "type": "scene",
        "method": "update",
        "tangible_id": "bar_graph_books",
        "params": {
          "axis_range": [
            0,
            80
          ],
          "description": "Axis now extends from 0 to 80 with scale of 5."
        }
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph with extended axis 0-80. All tick marks visible (0, 5, 10...75, 80). Axis appears crowded.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "That's a LOT of numbers on the axis. 0, 5, 10, 15, 20... all the way up to 80. That's 17 tick marks!"
      },
      {
        "type": "scene",
        "method": "update",
        "tangible_id": "bar_graph_books",
        "params": {
          "highlight_component": "axis",
          "description": "Axis highlights showing all 17 tick marks (0, 5, 10, 15... 75, 80)."
        }
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph with extended axis 0-80. Axis highlighted showing all 17 tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "It works... but is there a better way?"
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph with extended axis 0-80. Axis highlighted showing all 17 tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 5
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "When one scale needs too many tick marks, try a bigger scale."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph with extended axis 0-80. Axis highlighted showing all 17 tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 5
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:15:53.073071+00:00"
  },
  {
    "id": "s1_3_trying_bigger_scale",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "description": "Data table showing Books Read This Month. Categories: Aisha, Ben, Carlos, Dana. Values: 20, 35, 55, 80."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_books",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "vertical",
          "categories": [
            "Aisha",
            "Ben",
            "Carlos",
            "Dana"
          ],
          "values": [
            20,
            35,
            55,
            80
          ],
          "axis_range": [
            0,
            80
          ],
          "scale": 5,
          "scale_selector_active": true,
          "description": "Vertical bar graph appears. Books Read This Month data. Scale of 5 active. Axis shows 0–80 with 17 tick marks visible. Scale selector interactive."
        }
      },
      {
        "type": "dialogue",
        "text": "Scale of 5 works, but that's a lot of tick marks. Let's try a bigger scale."
      },
      {
        "type": "prompt",
        "text": "Click Scale of 10 to see what happens.",
        "tool": "click_scale_button",
        "target": "bar_graph_books",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 10
            },
            "description": "Student clicked Scale of 10 button",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_books",
                "params": {
                  "scale": 10,
                  "tick_marks_count": 9,
                  "description": "Graph updates to scale of 10. Axis now shows 0, 10, 20, 30, 40, 50, 60, 70, 80—only 9 tick marks. All four bars fit cleanly. Checkmark indicator appears."
                }
              },
              {
                "type": "dialogue",
                "text": "Look at that—only 9 tick marks now instead of 17. Much cleaner!"
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Data table showing Books Read This Month values.",
                    "tangible_type": "data_table"
                  },
                  {
                    "tangible_id": "bar_graph_books",
                    "description": "Vertical bar graph with scale of 10. Books Read This Month data. Axis 0–80 with 9 tick marks. Checkmark indicator visible. All bars fit cleanly.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "vertical",
                    "categories": [
                      "Aisha",
                      "Ben",
                      "Carlos",
                      "Dana"
                    ],
                    "scale": 10,
                    "axis_range": [
                      0,
                      80
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph in reading mode. Books Read This Month data. Scale of 5 active, showing 17 tick marks. Scale selector interactive, awaiting student choice.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "scale": 5,
            "axis_range": [
              0,
              80
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "All the data fits, and the graph is easier to read."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph with scale of 10. Books Read This Month data. Axis 0–80 with 9 tick marks. All bars fit cleanly. Graph is easier to read than with scale of 5.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "scale": 10,
            "axis_range": [
              0,
              80
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:16:18.004989+00:00"
  },
  {
    "id": "s1_4_range_check_efficiency",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "categories": [
            "Aisha",
            "Ben",
            "Carlos",
            "Dana"
          ],
          "values": [
            20,
            35,
            55,
            80
          ],
          "description": "Data table appears showing Books Read This Month data. Aisha=20, Ben=35, Carlos=55, Dana=80."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_books",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "vertical",
          "categories": [
            "Aisha",
            "Ben",
            "Carlos",
            "Dana"
          ],
          "values": [
            20,
            35,
            55,
            80
          ],
          "axis_range": [
            0,
            80
          ],
          "scale": 10,
          "scale_selector_visible": true,
          "description": "Vertical bar graph appears showing Books Read This Month data with scale of 10 preview active. All four bars visible (Aisha=20, Ben=35, Carlos=55, Dana=80). 9 tick marks on axis (0, 10, 20, 30, 40, 50, 60, 70, 80)."
        }
      },
      {
        "type": "scene",
        "method": "update",
        "tangible_id": "data_table",
        "params": {
          "highlight_values": [
            80
          ],
          "description": "Dana's value 80 highlights in data table."
        }
      },
      {
        "type": "dialogue",
        "text": "Here's the first thing to check: What's your BIGGEST number? That tells you what scales might work."
      },
      {
        "type": "prompt",
        "text": "What's the biggest number in this data?",
        "tool": "multiple_choice",
        "options": [
          20,
          35,
          55,
          80
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 80
            },
            "description": "Student selected 80, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "dialogue",
                "text": "80 is the biggest. Always check the biggest number first—does it fit on the scale without too many lines on the axis?"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values. Dana's 80 highlighted.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph showing Books Read This Month data with scale of 10, axis 0–80, 9 tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 10
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "You saw that Scale of 5 needed 17 tick marks. Scale of 10 only needs 9. For big data, bigger scales make cleaner graphs."
      },
      {
        "type": "dialogue",
        "text": "When more than one scale fits, pick the one that's easier to read."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Books Read This Month values. Dana's 80 highlighted.",
            "tangible_type": "data_table",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ]
          },
          {
            "tangible_id": "bar_graph_books",
            "description": "Vertical bar graph showing Books Read This Month data with scale of 10, axis 0–80, 9 tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Aisha",
              "Ben",
              "Carlos",
              "Dana"
            ],
            "values": [
              20,
              35,
              55,
              80
            ],
            "axis_range": [
              0,
              80
            ],
            "scale": 10
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:16:40.973093+00:00"
  },
  {
    "id": "s2_1_all_scales_fit_small_data",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "categories": [
            "Jar A",
            "Jar B",
            "Jar C",
            "Jar D"
          ],
          "values": [
            7,
            12,
            19,
            23
          ],
          "description": "Horizontal data table appears showing Marbles in Jars data: Jar A: 7, Jar B: 12, Jar C: 19, Jar D: 23."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_marbles",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "horizontal",
          "categories": [
            "Jar A",
            "Jar B",
            "Jar C",
            "Jar D"
          ],
          "values": [
            7,
            12,
            19,
            23
          ],
          "scale": null,
          "axis_range": [
            0,
            23
          ],
          "scale_selector_visible": true,
          "description": "Scale selector panel appears with all four scale buttons (1, 2, 5, 10) visible. No graph bars displayed yet."
        },
        "flag": "placeholder — Scale Preview System not yet fully specced; using bar_graph with scale_selector_visible based on UX context"
      },
      {
        "type": "dialogue",
        "text": "Here's data about marbles. Look at the biggest number—23. That's pretty small!"
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Horizontal data table showing Marbles in Jars data: Jar A: 7, Jar B: 12, Jar C: 19, Jar D: 23.",
            "tangible_type": "data_table",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ]
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Scale selector panel with four scale buttons visible. No bars displayed yet.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ],
            "scale": null,
            "axis_range": [
              0,
              23
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "This graph is horizontal—the bars go sideways. Let's check: which scales fit? Try clicking each scale."
      },
      {
        "type": "prompt",
        "text": "Click each scale to see if 23 fits.",
        "tool": "click_scale_button",
        "target": "bar_graph_marbles",
        "validator": [
          {
            "condition_id": "explored_all_scales",
            "condition": {},
            "description": "Student explored all four scale options (1, 2, 5, 10) and observed that all fit the data range 0-23",
            "is_correct": true,
            "beats": [
              {
                "type": "dialogue",
                "text": "You checked them all. All four scales fit!"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Horizontal data table showing Marbles in Jars data: Jar A: 7, Jar B: 12, Jar C: 19, Jar D: 23.",
            "tangible_type": "data_table",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ]
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Scale selector panel showing all four scale buttons with checkmarks indicating all scales fit. Student has explored all options.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ],
            "scale": null,
            "axis_range": [
              0,
              23
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "All four scales fit! Let's look at Scale of 1."
      },
      {
        "type": "prompt",
        "text": "Click Scale of 1 to see what it looks like.",
        "tool": "click_scale_button",
        "target": "bar_graph_marbles",
        "validator": [
          {
            "condition_id": "selected_scale_1",
            "condition": {
              "selected": 1
            },
            "description": "Student clicked Scale of 1 button",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_marbles",
                "params": {
                  "scale": 1,
                  "tick_marks": 24,
                  "description": "Horizontal bar graph displays with scale of 1. All four bars fit correctly, but axis shows 24 tick marks (0 through 23)."
                }
              },
              {
                "type": "dialogue",
                "text": "It works—every number lands exactly. But look at all those lines on the side!"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Horizontal data table showing Marbles in Jars data: Jar A: 7, Jar B: 12, Jar C: 19, Jar D: 23.",
            "tangible_type": "data_table",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ]
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph with scale of 1. All four bars displayed (Jar A: 7, Jar B: 12, Jar C: 19, Jar D: 23). Axis shows 24 tick marks from 0 to 23.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ],
            "scale": 1,
            "axis_range": [
              0,
              23
            ],
            "tick_marks": 24
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:17:11.337152+00:00"
  },
  {
    "id": "s2_2_but_which_is_best_efficiency",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "description": "Data table appears showing Marbles in Jars data: Jar A=7, Jar B=12, Jar C=19, Jar D=23."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_marbles",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "horizontal",
          "categories": [
            "Jar A",
            "Jar B",
            "Jar C",
            "Jar D"
          ],
          "axis_range": [
            0,
            23
          ],
          "scale": 1,
          "description": "Horizontal bar graph appears. Marbles in Jars data. Scale of 1, axis 0–23 with 24 tick marks visible."
        }
      },
      {
        "type": "dialogue",
        "text": "Scale of 1 works, but that's a lot of lines. You learned bigger scales are usually easier to read."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars values: Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 1, axis 0–23, 24 tick marks. Four bars displayed.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "axis_range": [
              0,
              23
            ],
            "scale": 1
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Let's try Scale of 10."
      },
      {
        "type": "prompt",
        "text": "Click 'Scale of 10' to compare.",
        "tool": "click_scale_button",
        "target": "bar_graph_marbles",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 10
            },
            "description": "Student clicked Scale of 10",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_marbles",
                "params": {
                  "scale": 10,
                  "axis_range": [
                    0,
                    30
                  ],
                  "warning_indicators": [
                    "Jar A",
                    "Jar C"
                  ],
                  "description": "Graph updates to scale of 10. Bars appear with ⚠️ indicators on Jar A and Jar C. Jar A (7) between 0 and 10. Jar C (19) between 10 and 20. Axis shows 0, 10, 20, 30—3 tick marks."
                }
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars values: Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 10, axis 0–30, 4 tick marks. ⚠️ indicators on Jar A and Jar C bars.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "axis_range": [
              0,
              30
            ],
            "scale": 10
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Hmm. Scale of 10 fits, but there are only 3 marks on the axis. Look at those warnings. Can you tell the exact value of where those bars end? Someone looking at our graph without the data table would need to guess how many marbles are shown."
      },
      {
        "type": "scene",
        "method": "animate",
        "tangible_id": "bar_graph_marbles",
        "params": {
          "event": "show_warning_message",
          "status": "confirmed",
          "description": "⚠️ on Jar A highlights with message: '7 won't land exactly on a line or in the middle.'"
        }
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars values: Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 10, axis 0–30. ⚠️ on Jar A showing exactness warning message.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "axis_range": [
              0,
              30
            ],
            "scale": 10
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "For big data, we'd pick Scale of 10 anyway. It's the easiest to read because we don't want too many lines on the axis. But these numbers are small and it's hard to find the exact location of the bar on the graph. We can do better."
      },
      {
        "type": "dialogue",
        "text": "When data is small, you have room to find a scale where everything lands exactly."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars values: Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 10, axis 0–30, 4 tick marks. ⚠️ indicators on Jar A and Jar C.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "axis_range": [
              0,
              30
            ],
            "scale": 10
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:17:48.653871+00:00"
  },
  {
    "id": "s2_3_scale_2_works_non_multiples",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "categories": [
            "Jar A",
            "Jar B",
            "Jar C",
            "Jar D"
          ],
          "values": [
            7,
            12,
            19,
            23
          ],
          "description": "Data table appears. Marbles in Jars. Jar A=7, Jar B=12, Jar C=19, Jar D=23."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_marbles",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "horizontal",
          "categories": [
            "Jar A",
            "Jar B",
            "Jar C",
            "Jar D"
          ],
          "values": [
            7,
            12,
            19,
            23
          ],
          "scale": 10,
          "axis_range": [
            0,
            30
          ],
          "warning_categories": [
            "Jar A",
            "Jar C"
          ],
          "description": "Horizontal bar graph appears. Marbles in Jars data. Scale of 10. Axis 0–30. Warning indicators on Jar A and Jar C bars (values 7 and 19 do not land exactly on tick marks or midpoints)."
        }
      },
      {
        "type": "dialogue",
        "text": "Let's try a smaller scale. Try a Scale of 2."
      },
      {
        "type": "prompt",
        "text": "Click 'Scale of 2' to preview.",
        "tool": "click_scale_button",
        "target": "bar_graph_marbles",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 2
            },
            "description": "Student clicked Scale of 2 button. Preview displays: all bars land exactly, checkmark indicator, no warnings.",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_marbles",
                "params": {
                  "scale": 2,
                  "axis_range": [
                    0,
                    24
                  ],
                  "warning_categories": [],
                  "description": "Graph updates to Scale of 2. Axis 0–24 with 13 tick marks. All bars land exactly. Checkmark indicator appears. No warnings."
                }
              },
              {
                "type": "dialogue",
                "text": "Look—we can read the end of the bars clearly. ALL the numbers land exactly. 7 is right at 7, exactly halfway between 6 and 8. 12 is right at 12."
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Data table showing Marbles in Jars. Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
                    "tangible_type": "data_table",
                    "categories": [
                      "Jar A",
                      "Jar B",
                      "Jar C",
                      "Jar D"
                    ],
                    "values": [
                      7,
                      12,
                      19,
                      23
                    ]
                  },
                  {
                    "tangible_id": "bar_graph_marbles",
                    "description": "Horizontal bar graph. Marbles in Jars. Scale of 2. Axis 0–24. All bars land exactly. Checkmark indicator visible. No warnings.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "horizontal",
                    "categories": [
                      "Jar A",
                      "Jar B",
                      "Jar C",
                      "Jar D"
                    ],
                    "values": [
                      7,
                      12,
                      19,
                      23
                    ],
                    "scale": 2,
                    "axis_range": [
                      0,
                      24
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars. Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ]
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 10 active. Axis 0–30. Warning indicators on Jar A and Jar C. Scale selector interactive.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ],
            "scale": 10,
            "axis_range": [
              0,
              30
            ],
            "warning_categories": [
              "Jar A",
              "Jar C"
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "With Scale of 2, half of 2 is 1. So you can show ANY whole number exactly."
      },
      {
        "type": "dialogue",
        "text": "Scale of 2 works to show the exact value for all numbers—and for small data, the graph won't have too many marks on the axis."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Marbles in Jars. Jar A=7, Jar B=12, Jar C=19, Jar D=23.",
            "tangible_type": "data_table",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ]
          },
          {
            "tangible_id": "bar_graph_marbles",
            "description": "Horizontal bar graph. Marbles in Jars. Scale of 2. Axis 0–24. All bars land exactly. Checkmark indicator visible.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Jar A",
              "Jar B",
              "Jar C",
              "Jar D"
            ],
            "values": [
              7,
              12,
              19,
              23
            ],
            "scale": 2,
            "axis_range": [
              0,
              24
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:18:19.240081+00:00"
  },
  {
    "id": "s2_4_digit_pattern_recognition_shortcut",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "dataset_a_display",
        "tangible_type": "image",
        "params": {
          "description": "Left panel labeled 'Data Set A' shows four values: 20, 35, 55, 80 with annotation 'Ones digits: 0 or 5'."
        },
        "flag": "placeholder — image toy spec not yet defined; using as static visual display"
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "dataset_b_display",
        "tangible_type": "image",
        "params": {
          "description": "Right panel labeled 'Data Set B' shows four values: 7, 12, 19, 23 with annotation 'Ones digits: 7, 2, 9, 3'."
        },
        "flag": "placeholder — image toy spec not yet defined; using as static visual display"
      },
      {
        "type": "dialogue",
        "text": "Here's a quick way to know if you need Scale of 2. Check the last digit of each number in the ones place."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "dataset_a_display",
            "description": "Left panel: Data Set A showing 20, 35, 55, 80 labeled 'Ones digits: 0 or 5'.",
            "tangible_type": "image"
          },
          {
            "tangible_id": "dataset_b_display",
            "description": "Right panel: Data Set B showing 7, 12, 19, 23 labeled 'Ones digits: 7, 2, 9, 3'.",
            "tangible_type": "image"
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Numbers that end in 0 or 5—like 20, 35, 55, 80—those are multiples of 5 and can be shown clearly with Scales of 5 and 10."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "dataset_a_display",
            "description": "Left panel: Data Set A showing 20, 35, 55, 80 labeled 'Ones digits: 0 or 5'.",
            "tangible_type": "image"
          },
          {
            "tangible_id": "dataset_b_display",
            "description": "Right panel: Data Set B showing 7, 12, 19, 23 labeled 'Ones digits: 7, 2, 9, 3'.",
            "tangible_type": "image"
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "But look at 7, 12, 19, 23. See the digits in the ones place? 7, 2, 9, 3. None are 0 or 5—that tells you they aren't multiples of 5 so Scale of 2 might be your best choice."
      },
      {
        "type": "dialogue",
        "text": "Check our groups. Which data set has last digits that are NOT 0 or 5?"
      },
      {
        "type": "prompt",
        "text": "Which data set has last digits that are NOT 0 or 5?",
        "tool": "click_tangible",
        "target": [
          "dataset_a_display",
          "dataset_b_display"
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": "dataset_b_display"
            },
            "description": "Student clicked Data Set B (7, 12, 19, 23), correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "animate",
                "tangible_id": "dataset_b_display",
                "params": {
                  "event": "highlight",
                  "status": "confirmed",
                  "description": "Data Set B panel highlights to confirm selection."
                }
              },
              {
                "type": "dialogue",
                "text": "Right. Look at those last digits: 7, 2, 9, 3. None are 0 or 5—that's your Scale of 2 signal."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "dataset_a_display",
            "description": "Left panel: Data Set A showing 20, 35, 55, 80 labeled 'Ones digits: 0 or 5'.",
            "tangible_type": "image"
          },
          {
            "tangible_id": "dataset_b_display",
            "description": "Right panel: Data Set B showing 7, 12, 19, 23 labeled 'Ones digits: 7, 2, 9, 3'. Click target active.",
            "tangible_type": "image"
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:18:44.644052+00:00"
  },
  {
    "id": "s2_5_practice_with_non_multiples",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "orientation": "vertical",
          "categories": [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4"
          ],
          "values": [
            22,
            15,
            8,
            31
          ],
          "description": "Vertical data table appears. Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31."
        }
      },
      {
        "type": "dialogue",
        "text": "Here's data from a game. Four rounds of points: 22, 15, 8, 31."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Round 1",
              "Round 2",
              "Round 3",
              "Round 4"
            ],
            "values": [
              22,
              15,
              8,
              31
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Check the ones place digits: 2, 5, 8, 1. Do they all end in 0 or 5?"
      },
      {
        "type": "dialogue",
        "text": "22... no. 15... yes! 8... no. 31... no. Three of them don't so they aren't multiples of 5. Which scale will show ALL values exactly?"
      },
      {
        "type": "prompt",
        "text": "Which scale will show ALL values exactly?",
        "tool": "multiple_choice",
        "options": [
          "Scale of 1",
          "Scale of 2",
          "Scale of 5",
          "Scale of 10"
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": "Scale of 2"
            },
            "description": "Student selected Scale of 2, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "add",
                "tangible_id": "bar_graph_points",
                "tangible_type": "bar_graph",
                "params": {
                  "mode": "reading",
                  "orientation": "vertical",
                  "categories": [
                    "Round 1",
                    "Round 2",
                    "Round 3",
                    "Round 4"
                  ],
                  "values": [
                    22,
                    15,
                    8,
                    31
                  ],
                  "scale": 2,
                  "axis_range": [
                    0,
                    32
                  ],
                  "description": "Vertical bar graph appears. Points Scored. Scale of 2. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31. All bars land exactly on tick marks."
                }
              },
              {
                "type": "dialogue",
                "text": "Scale of 2. All of the bars fit well on the graph and their exact values are clear."
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
                    "tangible_type": "data_table",
                    "orientation": "vertical",
                    "categories": [
                      "Round 1",
                      "Round 2",
                      "Round 3",
                      "Round 4"
                    ],
                    "values": [
                      22,
                      15,
                      8,
                      31
                    ]
                  },
                  {
                    "tangible_id": "bar_graph_points",
                    "description": "Vertical bar graph. Points Scored. Scale of 2. All bars land exactly on tick marks.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "vertical",
                    "categories": [
                      "Round 1",
                      "Round 2",
                      "Round 3",
                      "Round 4"
                    ],
                    "values": [
                      22,
                      15,
                      8,
                      31
                    ],
                    "scale": 2,
                    "axis_range": [
                      0,
                      32
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Round 1",
              "Round 2",
              "Round 3",
              "Round 4"
            ],
            "values": [
              22,
              15,
              8,
              31
            ]
          }
        ]
      },
      {
        "type": "scene",
        "method": "update",
        "tangible_id": "bar_graph_points",
        "params": {
          "scale": 1,
          "axis_range": [
            0,
            31
          ],
          "description": "Bar graph updates to Scale of 1. Same Points Scored data."
        }
      },
      {
        "type": "dialogue",
        "text": "Scale of 1 also shows the exact values, but it would require a lot of marks on the axis to get to the greatest value of 31. Let's consider when we might choose a scale of 1."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Round 1",
              "Round 2",
              "Round 3",
              "Round 4"
            ],
            "values": [
              22,
              15,
              8,
              31
            ]
          },
          {
            "tangible_id": "bar_graph_points",
            "description": "Vertical bar graph. Points Scored. Scale of 1. All bars visible.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Round 1",
              "Round 2",
              "Round 3",
              "Round 4"
            ],
            "values": [
              22,
              15,
              8,
              31
            ],
            "scale": 1,
            "axis_range": [
              0,
              31
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:19:12.358465+00:00"
  },
  {
    "id": "s2_6_very_small_data_scale_1",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "orientation": "vertical",
          "categories": [
            "Mia",
            "Noah",
            "Olivia",
            "Pete"
          ],
          "values": [
            9,
            5,
            7,
            3
          ],
          "title": "Stickers Earned Today",
          "description": "Vertical data table appears. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_stickers",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "vertical",
          "categories": [
            "Mia",
            "Noah",
            "Olivia",
            "Pete"
          ],
          "scale_selector_visible": true,
          "bars_visible": false,
          "description": "Vertical bar graph frame appears. Scale Preview System available. No bars showing yet."
        }
      },
      {
        "type": "dialogue",
        "text": "Look at these numbers: 9, 5, 7, 3. They're really small!"
      },
      {
        "type": "dialogue",
        "text": "What happens if we try Scale of 10?"
      },
      {
        "type": "prompt",
        "text": "Click 'Scale of 10'",
        "tool": "click_scale_button",
        "target": "bar_graph_stickers",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 10
            },
            "description": "Student clicked Scale of 10 button",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_stickers",
                "params": {
                  "scale": 10,
                  "axis_range": [
                    0,
                    10
                  ],
                  "tick_marks": [
                    0,
                    10
                  ],
                  "bars_visible": true,
                  "warning_indicators": [
                    "Mia",
                    "Noah",
                    "Olivia",
                    "Pete"
                  ],
                  "description": "Graph updates to Scale of 10. Only tick marks at 0 and 10. Bars appear with warning indicators."
                }
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
                    "tangible_type": "data_table",
                    "orientation": "vertical",
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ],
                    "values": [
                      9,
                      5,
                      7,
                      3
                    ]
                  },
                  {
                    "tangible_id": "bar_graph_stickers",
                    "description": "Vertical bar graph. Scale 10. Axis 0-10 with tick marks at 0 and 10 only. All four bars show warning indicators.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "vertical",
                    "scale": 10,
                    "axis_range": [
                      0,
                      10
                    ],
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "values": [
              9,
              5,
              7,
              3
            ]
          },
          {
            "tangible_id": "bar_graph_stickers",
            "description": "Vertical bar graph. Scale Preview System active. No bars showing. Scale selection pending.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "scale_selector_visible": true,
            "bars_visible": false
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "The bars fit, but we don't know the exact value for any of the bars."
      },
      {
        "type": "dialogue",
        "text": "Think about the numbers: 9, 5, 7, 3. They don't end in 0 or 5 so we know Scale of 2 is clearer to show any number. Click 'Scale of 2.'"
      },
      {
        "type": "prompt",
        "text": "Click 'Scale of 2'",
        "tool": "click_scale_button",
        "target": "bar_graph_stickers",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 2
            },
            "description": "Student clicked Scale of 2 button",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_stickers",
                "params": {
                  "scale": 2,
                  "axis_range": [
                    0,
                    10
                  ],
                  "tick_marks": [
                    0,
                    2,
                    4,
                    6,
                    8,
                    10
                  ],
                  "bars_visible": true,
                  "checkmark_indicator": true,
                  "description": "Graph updates to Scale of 2. All bars show checkmark indicator. Clean graph with 0-10 range."
                }
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
                    "tangible_type": "data_table",
                    "orientation": "vertical",
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ],
                    "values": [
                      9,
                      5,
                      7,
                      3
                    ]
                  },
                  {
                    "tangible_id": "bar_graph_stickers",
                    "description": "Vertical bar graph. Scale 2. Axis 0-10. All bars land on tick marks or midpoints. Checkmark indicator visible.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "vertical",
                    "scale": 2,
                    "axis_range": [
                      0,
                      10
                    ],
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "values": [
              9,
              5,
              7,
              3
            ]
          },
          {
            "tangible_id": "bar_graph_stickers",
            "description": "Vertical bar graph. Scale of 10 previously selected. Bars showing with warning indicators. Scale selector still active.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "scale": 10,
            "axis_range": [
              0,
              10
            ],
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "scale_selector_visible": true
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "That's better! We can see the bars end at lines or exactly halfway. Scale of 2 could work. But when numbers are this small, you have another option. Try Scale of 1. What do you notice?"
      },
      {
        "type": "prompt",
        "text": "Click 'Scale of 1'",
        "tool": "click_scale_button",
        "target": "bar_graph_stickers",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 1
            },
            "description": "Student clicked Scale of 1 button",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_stickers",
                "params": {
                  "scale": 1,
                  "axis_range": [
                    0,
                    10
                  ],
                  "tick_marks": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10
                  ],
                  "bars_visible": true,
                  "checkmark_indicator": true,
                  "description": "Graph updates to Scale of 1. All bars land exactly on tick marks. Checkmark indicator. Clean graph with 0-10 range."
                }
              },
              {
                "type": "current_scene",
                "elements": [
                  {
                    "tangible_id": "data_table",
                    "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
                    "tangible_type": "data_table",
                    "orientation": "vertical",
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ],
                    "values": [
                      9,
                      5,
                      7,
                      3
                    ]
                  },
                  {
                    "tangible_id": "bar_graph_stickers",
                    "description": "Vertical bar graph. Scale 1. Axis 0-10. All bars land exactly on tick marks. Checkmark indicator visible.",
                    "tangible_type": "bar_graph",
                    "mode": "reading",
                    "orientation": "vertical",
                    "scale": 1,
                    "axis_range": [
                      0,
                      10
                    ],
                    "categories": [
                      "Mia",
                      "Noah",
                      "Olivia",
                      "Pete"
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "values": [
              9,
              5,
              7,
              3
            ]
          },
          {
            "tangible_id": "bar_graph_stickers",
            "description": "Vertical bar graph. Scale of 2 currently displayed. Bars showing with checkmark indicator. Scale selector active.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "scale": 2,
            "axis_range": [
              0,
              10
            ],
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "scale_selector_visible": true
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Every number lands right on a line. No halfway bars needed. We can read the graph accurately without having the data table."
      },
      {
        "type": "dialogue",
        "text": "For very small numbers, Scale of 1 can be a great choice—simple and exact."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Stickers Earned Today. Mia: 9, Noah: 5, Olivia: 7, Pete: 3.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ],
            "values": [
              9,
              5,
              7,
              3
            ]
          },
          {
            "tangible_id": "bar_graph_stickers",
            "description": "Vertical bar graph. Scale 1. Axis 0-10 with all tick marks. All bars land exactly on lines.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "vertical",
            "scale": 1,
            "axis_range": [
              0,
              10
            ],
            "categories": [
              "Mia",
              "Noah",
              "Olivia",
              "Pete"
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:19:58.163105+00:00"
  },
  {
    "id": "s3_1_independent_selection_multiples_5",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "orientation": "vertical",
          "categories": [
            "Dates",
            "Cherries",
            "Bananas",
            "Apples"
          ],
          "values": [
            60,
            45,
            30,
            15
          ],
          "description": "Vertical data table appears. Favorite Fruits data. Dates: 60, Cherries: 45, Bananas: 30, Apples: 15."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_fruits",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "horizontal",
          "categories": [
            "Dates",
            "Cherries",
            "Bananas",
            "Apples"
          ],
          "values": [
            60,
            45,
            30,
            15
          ],
          "scale": null,
          "axis_range": [
            0,
            60
          ],
          "description": "Horizontal bar graph appears. Favorite Fruits data. Scale Preview System available—no scale selected yet."
        }
      },
      {
        "type": "dialogue",
        "text": "Here's data about students' favorite fruits. The most votes went to Dates with 60. Scale of 1 doesn't make sense here because it would take 60 lines on the axis. That's too much!"
      },
      {
        "type": "dialogue",
        "text": "Your job: pick the right scale. Which scale will you use?"
      },
      {
        "type": "prompt",
        "text": "Explore the Scale Preview System with scales 2, 5, and 10.",
        "tool": "click_scale_button",
        "target": "bar_graph_fruits",
        "validator": [
          {
            "condition_id": "explored_scales",
            "condition": {},
            "description": "Student explored scale options freely; all three scales (2, 5, 10) show checkmarks",
            "is_correct": true,
            "beats": [
              {
                "type": "empty"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Favorite Fruits data. Dates: 60, Cherries: 45, Bananas: 30, Apples: 15.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ]
          },
          {
            "tangible_id": "bar_graph_fruits",
            "description": "Horizontal bar graph. Favorite Fruits data. Scale Preview System shows checkmarks for scales 2, 5, and 10.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ],
            "axis_range": [
              0,
              60
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Which scale will you use?"
      },
      {
        "type": "prompt",
        "text": "Which scale will you use?",
        "tool": "multiple_choice",
        "options": [
          "Scale of 2",
          "Scale of 5",
          "Scale of 10"
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": "Scale of 10"
            },
            "description": "Student selected Scale of 10, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "update",
                "tangible_id": "bar_graph_fruits",
                "params": {
                  "scale": 10,
                  "description": "Bar graph updates to Scale of 10. All bars land on tick marks."
                }
              },
              {
                "type": "dialogue",
                "text": "Good choice."
              }
            ]
          },
          {
            "condition_id": "scale_2",
            "condition": {
              "selected": "Scale of 2"
            },
            "description": "Student selected Scale of 2—works but not optimal for this data",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "That scale could work, but check—all values end in 0 or 5. Which scale would be easiest to read?"
              }
            ]
          },
          {
            "condition_id": "scale_5",
            "condition": {
              "selected": "Scale of 5"
            },
            "description": "Student selected Scale of 5—works but not optimal for this data",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "That scale could work, but check—all values end in 0 or 5. Which scale would be easiest to read?"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Favorite Fruits data. Dates: 60, Cherries: 45, Bananas: 30, Apples: 15.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ]
          },
          {
            "tangible_id": "bar_graph_fruits",
            "description": "Horizontal bar graph. Favorite Fruits data. Scale of 10 selected. All bars visible.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ],
            "scale": 10,
            "axis_range": [
              0,
              60
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Why is Scale of 10 a good choice? Choose all of the reasons."
      },
      {
        "type": "prompt",
        "text": "Why is Scale of 10 a good choice? Choose all of the reasons.",
        "tool": "multi_select",
        "options": [
          "All values end in 0 or 5 so they can be graphed precisely.",
          "The graph is easy to read.",
          "The biggest number is 60 so the bars fit on the graph.",
          "Scale of 2 takes too many marks to reach the biggest number."
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "and": [
                {
                  "selected": "All values end in 0 or 5 so they can be graphed precisely."
                },
                {
                  "selected": "The graph is easy to read."
                },
                {
                  "selected": "The biggest number is 60 so the bars fit on the graph."
                },
                {
                  "selected": "Scale of 2 takes too many marks to reach the biggest number."
                }
              ]
            },
            "description": "Student selected all four reasons, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "dialogue",
                "text": "Exactly. All values are multiples of 5, so scales of 5 and 10 both work to read the graph clearly. For data going up to 60, Scale of 10 gives you a cleaner graph."
              }
            ]
          },
          {
            "condition_id": "incomplete",
            "condition": {},
            "description": "Student did not select all four reasons",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "Let's consider the questions we ask when choosing a scale. What is the biggest number? Does the data all fit? Look at all the numbers—do they end in 0 or 5 so we can find the exact location of the bars? What scale can we use for the best looking graph? All of these reasons help us choose the scale of 10."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table. Favorite Fruits data. Dates: 60, Cherries: 45, Bananas: 30, Apples: 15.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ]
          },
          {
            "tangible_id": "bar_graph_fruits",
            "description": "Horizontal bar graph. Favorite Fruits data. Scale of 10. All bars visible and landing on tick marks.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Dates",
              "Cherries",
              "Bananas",
              "Apples"
            ],
            "values": [
              60,
              45,
              30,
              15
            ],
            "scale": 10,
            "axis_range": [
              0,
              60
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:20:37.223025+00:00"
  },
  {
    "id": "s3_2_selection_creation_non_multiples",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "orientation": "vertical",
          "categories": [
            "Guitar",
            "Piano",
            "Violin",
            "Drums"
          ],
          "values": [
            27,
            14,
            41,
            33
          ],
          "description": "Vertical data table appears. Minutes of Practice data. Guitar: 27, Piano: 14, Violin: 41, Drums: 33."
        }
      },
      {
        "type": "dialogue",
        "text": "Here's data about how many minutes students practiced their instruments."
      },
      {
        "type": "dialogue",
        "text": "Check: are these numbers multiples of 5? Which scale is best for this data?"
      },
      {
        "type": "prompt",
        "text": "Which scale is best for this data?",
        "tool": "multiple_choice",
        "options": [
          "Scale of 1",
          "Scale of 2",
          "Scale of 5",
          "Scale of 10"
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": "Scale of 2"
            },
            "description": "Student selected Scale of 2, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "dialogue",
                "text": "Scale of 2. You saw that 14, 27, 33, 41 aren't multiples of 5 so we need scale of 2 to graph them precisely. Scale of 2 can work when the largest value is 41."
              }
            ]
          },
          {
            "condition_id": "selected_scale_5_or_10",
            "condition": {},
            "description": "Student selected Scale of 5 or Scale of 10",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "These numbers aren't multiples of 5 so the values can't be shown exactly with that scale. Try scale of 2."
              }
            ]
          },
          {
            "condition_id": "selected_scale_1",
            "condition": {
              "selected": "Scale of 1"
            },
            "description": "Student selected Scale of 1",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "Scale of 1 lets us graph exact numbers, but the largest value is 41. That would be a lot of marks on the axis. Which scale would be exact and look cleaner?"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Minutes of Practice. Guitar: 27, Piano: 14, Violin: 41, Drums: 33.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Guitar",
              "Piano",
              "Violin",
              "Drums"
            ],
            "values": [
              27,
              14,
              41,
              33
            ]
          }
        ]
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_practice",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "building",
          "orientation": "vertical",
          "categories": [
            "Guitar",
            "Piano",
            "Violin",
            "Drums"
          ],
          "scale": 2,
          "axis_range": [
            0,
            42
          ],
          "description": "Vertical bar graph creation tool appears. Minutes of Practice data. Scale of 2 active. Gridlines visible at each tick mark. All bars at zero height awaiting student input."
        }
      },
      {
        "type": "dialogue",
        "text": "Now create the bar graph."
      },
      {
        "type": "prompt",
        "text": "Set the bar heights for all 4 categories.",
        "tool": "click_to_set_height",
        "target": "bar_graph_practice",
        "validator": [
          {
            "condition_id": "all_bars_set",
            "condition": {},
            "description": "Student set all four bar heights",
            "is_correct": true,
            "beats": [
              {
                "type": "empty"
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Minutes of Practice. Guitar: 27, Piano: 14, Violin: 41, Drums: 33.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Guitar",
              "Piano",
              "Violin",
              "Drums"
            ],
            "values": [
              27,
              14,
              41,
              33
            ]
          },
          {
            "tangible_id": "bar_graph_practice",
            "description": "Vertical bar graph displays all 4 bars at correct heights. Guitar: 27, Piano: 14, Violin: 41, Drums: 33. Scale of 2, axis range 0-42.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "vertical",
            "categories": [
              "Guitar",
              "Piano",
              "Violin",
              "Drums"
            ],
            "scale": 2,
            "axis_range": [
              0,
              42
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "You chose the right scale and created the graph. Every bar lands exactly where it should."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Vertical data table showing Minutes of Practice. Guitar: 27, Piano: 14, Violin: 41, Drums: 33.",
            "tangible_type": "data_table",
            "orientation": "vertical",
            "categories": [
              "Guitar",
              "Piano",
              "Violin",
              "Drums"
            ],
            "values": [
              27,
              14,
              41,
              33
            ]
          },
          {
            "tangible_id": "bar_graph_practice",
            "description": "Vertical bar graph displays all 4 bars at correct heights. Guitar: 27, Piano: 14, Violin: 41, Drums: 33. Scale of 2, axis range 0-42.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "vertical",
            "categories": [
              "Guitar",
              "Piano",
              "Violin",
              "Drums"
            ],
            "scale": 2,
            "axis_range": [
              0,
              42
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:21:06.914050+00:00"
  },
  {
    "id": "s3_3_final_application",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "description": "Data table appears. Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40."
        }
      },
      {
        "type": "dialogue",
        "text": "Last one! Here are scores from four teams. Yellow Team won with 70 points."
      },
      {
        "type": "dialogue",
        "text": "You've done this vertical and horizontal now. Same process every time: check the numbers, choose the scale."
      },
      {
        "type": "dialogue",
        "text": "Which scale works best for this data?"
      },
      {
        "type": "prompt",
        "text": "Which scale works best for this data?",
        "tool": "click_scale_button",
        "target": "bar_graph_teams",
        "options": [
          1,
          2,
          5,
          10
        ],
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "selected": 10
            },
            "description": "Student selected Scale of 10, correct, most efficient for values ending in 0 or 5, range up to 70",
            "is_correct": true,
            "beats": [
              {
                "type": "dialogue",
                "text": "Good choice. All values end in 0 or 5, and the biggest is 70. Scale of 10 gives you a clean graph."
              }
            ]
          },
          {
            "condition_id": "selected_scale_1_or_2",
            "condition": {
              "selected": 1
            },
            "description": "Student selected Scale of 1, would need many axis lines",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "That would need a lot of lines on the axis. All the values end in 0 or 5—which bigger scale would be easier to read?"
              }
            ]
          },
          {
            "condition_id": "selected_scale_2",
            "condition": {
              "selected": 2
            },
            "description": "Student selected Scale of 2, would need many axis lines",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "That would need a lot of lines on the axis. All the values end in 0 or 5—which bigger scale would be easier to read?"
              }
            ]
          },
          {
            "condition_id": "selected_scale_5",
            "condition": {
              "selected": 5
            },
            "description": "Student selected Scale of 5, works but not most efficient given max value 70",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "That works! But notice the biggest value is 70. Scale of 10 would give you fewer lines and still show everything exactly."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Bar graph (horizontal orientation, building mode) with scale selection active. Team Scores dataset. Scale Preview System available.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "horizontal"
          }
        ]
      },
      {
        "type": "scene",
        "method": "update",
        "tangible_id": "bar_graph_teams",
        "params": {
          "mode": "building",
          "scale": 10,
          "axis_range": [
            0,
            80
          ],
          "description": "Bar graph updates to building mode with Scale of 10 active. Horizontal orientation. Axis 0–80 showing tick marks at 0, 10, 20, 30, 40, 50, 60, 70, 80. Empty graph ready for bar placement."
        }
      },
      {
        "type": "dialogue",
        "text": "Now create the graph. Place each bar at the right length."
      },
      {
        "type": "dialogue",
        "text": "Click to place the bar for Red Team at 25 points."
      },
      {
        "type": "prompt",
        "text": "Click to place the bar for Red Team at 25 points.",
        "tool": "click_to_set_height",
        "target": "bar_graph_teams",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "bar_height": 25,
              "category": "Red Team"
            },
            "description": "Student set Red Team bar to 25, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "animate",
                "tangible_id": "bar_graph_teams",
                "params": {
                  "event": "lock_bar",
                  "status": "confirmed",
                  "description": "Red Team bar locks at 25.",
                  "category": "Red Team",
                  "value": 25
                }
              },
              {
                "type": "dialogue",
                "text": "Right at 25—halfway between 20 and 30."
              }
            ]
          },
          {
            "condition_id": "incorrect_height",
            "condition": {},
            "description": "Student placed Red Team bar at incorrect height",
            "is_correct": false,
            "beats": [
              {
                "type": "dialogue",
                "text": "25 is halfway between 20 and 30. Find that spot."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Horizontal bar graph in building mode. Scale of 10. Axis 0–80. Red Team bar set at 25. Blue, Green, Yellow bars not yet placed.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "horizontal",
            "scale": 10,
            "axis_range": [
              0,
              80
            ],
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Click to place the bar for Blue Team at 40 points."
      },
      {
        "type": "prompt",
        "text": "Click to place the bar for Blue Team at 40 points.",
        "tool": "click_to_set_height",
        "target": "bar_graph_teams",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "bar_height": 40,
              "category": "Blue Team"
            },
            "description": "Student set Blue Team bar to 40, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "animate",
                "tangible_id": "bar_graph_teams",
                "params": {
                  "event": "lock_bar",
                  "status": "confirmed",
                  "description": "Blue Team bar locks at 40.",
                  "category": "Blue Team",
                  "value": 40
                }
              },
              {
                "type": "dialogue",
                "text": "Right on 40."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Horizontal bar graph in building mode. Scale of 10. Axis 0–80. Red Team bar at 25, Blue Team bar at 40. Green and Yellow bars not yet placed.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "horizontal",
            "scale": 10,
            "axis_range": [
              0,
              80
            ],
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Click to place the bar for Green Team at 55 points."
      },
      {
        "type": "prompt",
        "text": "Click to place the bar for Green Team at 55 points.",
        "tool": "click_to_set_height",
        "target": "bar_graph_teams",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "bar_height": 55,
              "category": "Green Team"
            },
            "description": "Student set Green Team bar to 55, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "animate",
                "tangible_id": "bar_graph_teams",
                "params": {
                  "event": "lock_bar",
                  "status": "confirmed",
                  "description": "Green Team bar locks at 55.",
                  "category": "Green Team",
                  "value": 55
                }
              },
              {
                "type": "dialogue",
                "text": "55—halfway between 50 and 60."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Horizontal bar graph in building mode. Scale of 10. Axis 0–80. Red Team bar at 25, Blue Team bar at 40, Green Team bar at 55. Yellow bar not yet placed.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "horizontal",
            "scale": 10,
            "axis_range": [
              0,
              80
            ],
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "Click to place the bar for Yellow Team at 70 points."
      },
      {
        "type": "prompt",
        "text": "Click to place the bar for Yellow Team at 70 points.",
        "tool": "click_to_set_height",
        "target": "bar_graph_teams",
        "validator": [
          {
            "condition_id": "correct",
            "condition": {
              "bar_height": 70,
              "category": "Yellow Team"
            },
            "description": "Student set Yellow Team bar to 70, correct",
            "is_correct": true,
            "beats": [
              {
                "type": "scene",
                "method": "animate",
                "tangible_id": "bar_graph_teams",
                "params": {
                  "event": "lock_bar",
                  "status": "confirmed",
                  "description": "Yellow Team bar locks at 70.",
                  "category": "Yellow Team",
                  "value": 70
                }
              },
              {
                "type": "dialogue",
                "text": "Right on 70."
              }
            ]
          }
        ]
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Horizontal bar graph in building mode. Scale of 10. Axis 0–80. All four bars placed: Red Team at 25, Blue Team at 40, Green Team at 55, Yellow Team at 70.",
            "tangible_type": "bar_graph",
            "mode": "building",
            "orientation": "horizontal",
            "scale": 10,
            "axis_range": [
              0,
              80
            ],
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ]
          }
        ]
      },
      {
        "type": "dialogue",
        "text": "That's it. You chose the scale and placed every bar exactly where it should be, some exactly on the lines and some halfway between."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores. Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40.",
            "tangible_type": "data_table"
          },
          {
            "tangible_id": "bar_graph_teams",
            "description": "Horizontal bar graph completed. Scale of 10. Axis 0–80. All four bars displayed: Red Team at 25, Blue Team at 40, Green Team at 55, Yellow Team at 70.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "scale": 10,
            "axis_range": [
              0,
              80
            ],
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ]
          }
        ]
      }
    ],
    "_generated_at": "2026-05-05T18:21:56.477757+00:00"
  },
  {
    "id": "s3_4_bridge_exit_check",
    "type": "transition",
    "beats": [
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "data_table",
        "tangible_type": "data_table",
        "params": {
          "orientation": "horizontal",
          "categories": [
            "Red Team",
            "Green Team",
            "Yellow Team",
            "Blue Team"
          ],
          "values": [
            25,
            55,
            70,
            40
          ],
          "description": "Data table appears: Team Scores. Red Team 25, Green Team 55, Yellow Team 70, Blue Team 40."
        }
      },
      {
        "type": "scene",
        "method": "add",
        "tangible_id": "bar_graph_team_scores",
        "tangible_type": "bar_graph",
        "params": {
          "mode": "reading",
          "orientation": "horizontal",
          "categories": [
            "Red Team",
            "Green Team",
            "Yellow Team",
            "Blue Team"
          ],
          "values": [
            25,
            55,
            70,
            40
          ],
          "scale": 10,
          "axis_range": [
            0,
            80
          ],
          "description": "Horizontal bar graph appears: Team Scores. Scale of 10, axis 0–80. Red Team bar at 25, Green Team at 55, Yellow Team at 70, Blue Team at 40. All bars locked in place."
        }
      },
      {
        "type": "dialogue",
        "text": "You learned to CHOOSE scales. Check the biggest number. Does it fit without too many marks on the axis? Check the ones place digits. Are they 0 or 5 to find the exact place for the bar? For very small data, Scale of 1 could work. Then pick the easiest to read."
      },
      {
        "type": "current_scene",
        "elements": [
          {
            "tangible_id": "data_table",
            "description": "Data table showing Team Scores: Red Team 25, Green Team 55, Yellow Team 70, Blue Team 40.",
            "tangible_type": "data_table",
            "orientation": "horizontal",
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ],
            "values": [
              25,
              55,
              70,
              40
            ]
          },
          {
            "tangible_id": "bar_graph_team_scores",
            "description": "Horizontal bar graph: Team Scores. Scale of 10, axis 0–80. All four bars locked at correct heights.",
            "tangible_type": "bar_graph",
            "mode": "reading",
            "orientation": "horizontal",
            "categories": [
              "Red Team",
              "Green Team",
              "Yellow Team",
              "Blue Team"
            ],
            "values": [
              25,
              55,
              70,
              40
            ],
            "scale": 10,
            "axis_range": [
              0,
              80
            ]
          }
        ]
      },
      {
        "type": "scene",
        "method": "animate",
        "tangible_id": "bar_graph_team_scores",
        "params": {
          "event": "fade_out",
          "status": "confirmed",
          "description": "Bar graph fades out."
        }
      },
      {
        "type": "scene",
        "method": "remove",
        "tangible_id": "bar_graph_team_scores"
      },
      {
        "type": "scene",
        "method": "animate",
        "tangible_id": "data_table",
        "params": {
          "event": "fade_out",
          "status": "confirmed",
          "description": "Data table fades out."
        }
      },
      {
        "type": "scene",
        "method": "remove",
        "tangible_id": "data_table"
      },
      {
        "type": "dialogue",
        "text": "Let's see what you know."
      },
      {
        "type": "current_scene",
        "elements": []
      }
    ],
    "_generated_at": "2026-05-05T18:22:14.876940+00:00"
  }
]
</lesson_sections>
<section_context>
## s1_1_transition_warmup
# Section Summary: s1_1_transition_warmup

**VISUAL STATE:** Empty workspace. No tangible visualizations, graphs, or data displays are present on screen at section end.

**CONTENT:** Transition dialogue acknowledging that in the Warmup section, all four scales (linear, log, square root, and reciprocal) were viable options for the student's dataset. The section introduces the concept that scale choice becomes more constrained when working with larger numbers, setting up the next investigation.

**STUDENT ACTION:** No interactive action required. The student listened to dialogue explaining that scale flexibility depends on data magnitude, preparing them for the upcoming exploration of how larger numbers affect scale viability.

## s1_2_when_scale_needs_too_many
# Section Summary: s1_2_when_scale_needs_too_many

**VISUAL STATE AT SECTION END:**
A data table and vertical bar graph are displayed side-by-side. The data table shows "Books Read This Month" with categories Aisha, Ben, Carlos, Dana and values 20, 35, 55, 80 respectively. The bar graph is vertical, in reading mode, with axis range 0–80, scale of 5, and all 17 tick marks highlighted (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80).

**CONTENT:**
The section introduced the problem that when a scale is too small relative to data range, it creates too many tick marks on the axis, making the graph crowded and difficult to read. The key vocabulary introduced was the principle: "When one scale needs too many tick marks, try a bigger scale." Students observed that a scale of 5 with axis 0–80 produces 17 tick marks, demonstrating visual clutter.

**STUDENT ACTION:**
The student (via guided exploration) selected a scale of 5, observed the preview showing Dana's bar extending past the initial 0–50 boundary, then extended the axis to 0–80 to accommodate all data. This revealed the crowding problem, leading to the conceptual takeaway about choosing appropriate scales.

## s1_3_trying_bigger_scale
# Section Summary: s1_3_trying_bigger_scale

**VISUAL STATE AT SECTION END:**
Two tangibles are on screen: (1) a data table displaying "Books Read This Month" with categories Aisha, Ben, Carlos, Dana and values 20, 35, 55, 80 respectively; (2) a vertical bar graph in reading mode showing the same data with scale 10, axis range 0–80 containing 9 tick marks (0, 10, 20, 30, 40, 50, 60, 70, 80), all four bars fitting cleanly.

**CONTENT:**
The section introduced the concept of adjusting graph scale to improve readability. Students learned that increasing the scale from 5 to 10 reduces the number of tick marks (from 17 to 9), making the graph cleaner and easier to interpret while still displaying all data accurately.

**STUDENT ACTION:**
The student clicked the "Scale of 10" button on the interactive scale selector, triggering the graph to update and demonstrating the effect of a larger scale on axis tick mark density and overall visual clarity.

## s1_4_range_check_efficiency
# Section Summary: s1_4_range_check_efficiency

**VISUAL STATE AT SECTION END:**
- **Data Table** ("Books Read This Month"): Categories—Aisha, Ben, Carlos, Dana; Values—20, 35, 55, 80 respectively; Dana's value (80) highlighted.
- **Bar Graph** (vertical, reading mode): Same dataset; axis range 0–80; scale of 10; 9 tick marks (0, 10, 20, 30, 40, 50, 60, 70, 80); all four bars visible.

**CONTENT:**
Introduced the "range check" strategy for selecting appropriate graph scales: identify the biggest number in the dataset first, then choose a scale that fits the maximum value without creating too many axis tick marks. Formally introduced the principle that larger scales (e.g., 10 vs. 5) produce cleaner, more readable graphs when multiple scales are viable. Compared efficiency: Scale of 5 requires 17 tick marks; Scale of 10 requires only 9 for the same data.

**STUDENT ACTION:**
Answered a multiple-choice question identifying 80 as the largest value in the dataset, demonstrating understanding of the first step in scale selection.

## s2_1_all_scales_fit_small_data
# Section Summary: s2_1_all_scales_fit_small_data

**VISUAL STATE AT SECTION END:**
A horizontal bar graph (dataset: Marbles in Jars) displays four bars for categories Jar A, Jar B, Jar C, and Jar D with values 7, 12, 19, and 23 respectively. The graph uses a scale of 1 with an axis range of 0–23 and 24 tick marks. A horizontal data table showing the same four categories and values appears alongside the graph.

**CONTENT:**
The section introduced the concept that multiple scales can fit small datasets and demonstrated how to evaluate scale appropriateness by checking whether the maximum data value (23) fits within each scale option. Students learned that while all four scales (1, 2, 5, 10) are mathematically valid, scale choice affects readability—specifically, a scale of 1 produces many tick marks (24), which can clutter the axis.

**STUDENT ACTION:**
The student clicked through all four scale buttons to explore which scales fit the data range, then selected Scale of 1 to observe the resulting graph with its dense tick-mark display.

## s2_2_but_which_is_best_efficiency
# Section Summary: s2_2_but_which_is_best_efficiency

**VISUAL STATE AT SECTION END:**
A data table displays "Marbles in Jars" with four categories: Jar A=7, Jar B=12, Jar C=19, Jar D=23. A horizontal bar graph (reading mode) shows the same data with scale of 10, axis range 0–30 (4 tick marks), and warning indicators (⚠️) on Jar A and Jar C bars, signaling that values 7 and 19 do not land exactly on axis lines or midpoints.

**CONTENT:**
The section introduced the concept of **scale efficiency**—balancing readability (fewer axis lines) against precision (exact value placement). Students learned that while larger scales (e.g., 10) reduce visual clutter for big datasets, they can create ambiguity for small data values. The vocabulary term **"scale"** was reinforced as a tool choice that affects graph clarity and accuracy.

**STUDENT ACTION:**
The student clicked a "Scale of 10" button to switch the graph from scale 1 (24 tick marks, 0–23 range) to scale 10 (4 tick marks, 0–30 range), then observed warning indicators highlight precision problems with values that don't align to grid lines.

## s2_3_scale_2_works_non_multiples
# Section Summary: s2_3_scale_2_works_non_multiples

**VISUAL STATE AT SECTION END:**
- **Data Table** ("Marbles in Jars"): 4 categories (Jar A, Jar B, Jar C, Jar D) with values 7, 12, 19, 23 respectively
- **Horizontal Bar Graph** ("bar_graph_marbles"): reading mode, Scale of 2, axis range 0–24, categories Jar A, Jar B, Jar C, Jar D with values 7, 12, 19, 23; all bars land exactly on tick marks with checkmark indicator visible, no warning indicators

**CONTENT:**
The section introduced the concept that **Scale of 2 works universally for whole numbers** because its half-interval (1) allows any integer to land exactly on a tick mark or midpoint. Students learned that Scale of 2 is effective for small datasets because it produces a manageable number of axis marks while ensuring precise value representation—contrasting with Scale of 10, which generated warnings for non-multiple values (7 and 19).

**STUDENT ACTION:**
The student clicked the "Scale of 2" button to preview the graph transformation, observing how all data values (7, 12, 19, 23) aligned exactly with axis marks when the scale changed from 10 to 2.

## s2_4_digit_pattern_recognition_shortcut
# Section Summary: s2_4_digit_pattern_recognition_shortcut

**VISUAL STATE:** Two side-by-side image panels are displayed. Left panel ("Data Set A") shows values 20, 35, 55, 80 with annotation "Ones digits: 0 or 5." Right panel ("Data Set B") shows values 7, 12, 19, 23 with annotation "Ones digits: 7, 2, 9, 3." Both panels remain visible throughout; Data Set B becomes highlighted after student interaction.

**CONTENT:** Students learned a shortcut for scale selection by examining the ones digit (last digit) of dataset values. The key pattern introduced: numbers ending in 0 or 5 are multiples of 5 (suitable for Scales of 5 and 10), while numbers with other ones digits (like 7, 2, 9, 3) signal that Scale of 2 may be the best choice. This digit-checking strategy provides a quick decision rule for scale selection.

**STUDENT ACTION:** Student clicked on Data Set B to answer the prompt "Which data set has last digits that are NOT 0 or 5?" The correct selection (Data Set B) triggered a highlight animation and confirmatory dialogue reinforcing that ones digits 7, 2, 9, 3 indicate a Scale of 2 signal.

## s2_5_practice_with_non_multiples
# Section Summary: Practice with Non-Multiples

**VISUAL STATE:** At section end, the screen displays two tangibles: (1) a vertical data table titled "Points Scored" with categories Round 1, Round 2, Round 3, Round 4 and values 22, 15, 8, 31 respectively; (2) a vertical bar graph in reading mode with the same dataset, scale of 1, axis range 0–31, where all bars are visible and land on tick marks.

**CONTENT:** Students practiced selecting appropriate scales for datasets containing non-multiples of common scale intervals. The lesson introduced the strategy of checking ones-place digits to determine divisibility by 5, then reasoned that a scale of 2 works well for this data (since all values are even) while a scale of 1, though accurate, requires many axis marks. The concept reinforced is that scale choice balances exactness with readability.

**STUDENT ACTION:** The student answered a multiple-choice question selecting "Scale of 2" as the best scale to show all values exactly, then observed the resulting bar graph and compared it to a scale-of-1 version to evaluate trade-offs between precision and practicality.

## s2_6_very_small_data_scale_1
# Section Summary: s2_6_very_small_data_scale_1

**VISUAL STATE AT SECTION END:**
Two tangibles are on screen: (1) A vertical data table titled "Stickers Earned Today" with categories Mia, Noah, Olivia, Pete and values 9, 5, 7, 3 respectively; (2) A vertical bar graph in reading mode displaying the same dataset with Scale of 1, axis range 0–10, tick marks at 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, and all four bars landing exactly on tick marks.

**CONTENT:**
The section introduced the concept of **scale selection for very small datasets** and the vocabulary term **"Scale of 1"** as an optimal choice for small numbers. Students learned that when data values (9, 5, 7, 3) don't align neatly with larger scales, Scale of 1 provides precision and simplicity—every bar lands exactly on a tick mark with no need for halfway estimates, making the graph readable without referencing the data table.

**STUDENT ACTION:**
The student clicked through three scale options sequentially: Scale of 10 (which produced warning indicators), Scale of 2 (which showed checkmarks), and finally Scale of 1 (which produced checkmarks and exact alignment). This interactive exploration demonstrated why Scale of 1 is superior for very small numbers.

## s3_1_independent_selection_multiples_5
# Section Summary: s3_1_independent_selection_multiples_5

## VISUAL STATE
At section end, two tangibles are displayed:
1. **Data Table** (vertical orientation): "Favorite Fruits" dataset with categories Dates, Cherries, Bananas, Apples and values 60, 45, 30, 15 respectively.
2. **Bar Graph** (horizontal orientation, reading mode): "Favorite Fruits" dataset with categories Dates, Cherries, Bananas, Apples and values 60, 45, 30, 15; scale set to 10; axis range 0–60; all bars visible and landing precisely on tick marks.

## CONTENT
Students practiced **selecting an appropriate scale for a bar graph** by evaluating which scale (2, 5, or 10) best represents data where all values are multiples of 5. The section introduced the reasoning process: checking the maximum value, ensuring data fits, verifying values align with scale tick marks, and prioritizing readability. Key vocabulary: *scale*, *tick marks*, *multiples*.

## STUDENT ACTION
Students (1) explored three scale options (2, 5, 10) using the Scale Preview System and earned checkmarks for all three; (2) selected "Scale of 10" from a multiple-choice prompt; (3) selected all four reasons why Scale of 10 is optimal from a multi-select prompt (values end in 0 or 5, graph is easy to read, biggest number fits, Scale of 2 requires too many marks).

## s3_2_selection_creation_non_multiples
# Section Summary: s3_2_selection_creation_non_multiples

**VISUAL STATE AT SECTION END:**
Two tangibles are displayed: (1) a vertical data table titled "Minutes of Practice" with categories Guitar, Piano, Violin, Drums and values 27, 14, 41, 33 respectively; (2) a vertical bar graph in building mode with the same four categories, scale of 2, axis range 0–42, displaying all four bars at their correct heights (Guitar: 27, Piano: 14, Violin: 41, Drums: 33) with gridlines visible at each tick mark.

**CONTENT:**
Students learned to select an appropriate scale for data that contains non-multiples of 5. The section introduced the reasoning that when data values (14, 27, 33, 41) are not multiples of 5, a scale of 2 is more efficient than scale of 1 (which would create excessive axis marks) or scales of 5 and 10 (which cannot represent values exactly). The vocabulary "scale" was reinforced in the context of axis design.

**STUDENT ACTION:**
The student answered a multiple-choice question selecting "Scale of 2" as the best scale for the data, then used a click-to-set-height tool to manually set all four bar heights on the vertical bar graph to match the data values precisely.

## s3_3_final_application
# Section Summary: s3_3_final_application

**VISUAL STATE AT SECTION END:**
Two tangibles are on screen: (1) a data table displaying Team Scores with four categories—Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40; (2) a completed horizontal bar graph titled "Team Scores" in reading mode, scale of 10, axis range 0–80 with tick marks at 0, 10, 20, 30, 40, 50, 60, 70, 80, showing all four bars locked in place (Red Team at 25, Blue Team at 40, Green Team at 55, Yellow Team at 70).

**CONTENT:**
This section applied the complete bar graph construction process (scale selection and bar placement) to a new dataset. Students practiced choosing an appropriate scale by analyzing data characteristics (values ending in 0 or 5, maximum value 70) and selecting scale of 10 as most efficient. They then placed all four bars by clicking to set exact heights, reinforcing precision in reading axis values and positioning bars both on tick marks and at midpoints between them.

**STUDENT ACTION:**
Student selected scale of 10 from options [1, 2, 5, 10], then sequentially placed four bars by clicking to set heights: Red Team (25), Blue Team (40), Green Team (55), and Yellow Team (70). Each bar placement was validated and locked before proceeding to the next.

## s3_4_bridge_exit_check
# Section Summary: s3_4_bridge_exit_check

**VISUAL STATE AT SECTION END:**
The screen is blank with no tangibles displayed. Both the data table and horizontal bar graph have faded out and been removed.

**CONTENT:**
This transition section reviewed the concept of **choosing appropriate scales for bar graphs**. The lesson reinforced that students should: (1) check the largest data value to ensure it fits without overcrowding the axis, (2) examine ones-place digits (0 or 5) to locate bars precisely, and (3) consider using a scale of 1 for very small datasets. The vocabulary term **"scale"** was formally reinforced in context.

**STUDENT ACTION:**
The student did not perform an interactive action in this section. Instead, they passively observed a data table and horizontal bar graph displaying Team Scores (Red Team: 25, Green Team: 55, Yellow Team: 70, Blue Team: 40) with a scale of 10 and axis range 0–80, then listened to a summary dialogue before both visuals faded out. This section serves as a bridge to an upcoming assessment ("Let's see what you know").
</section_context>

----------------------------------------------------------------------

## User Message

<input>
{
  "id": "s2_5_practice_with_non_multiples",
  "beats": [
    {
      "type": "scene",
      "method": "add",
      "tangible_id": "data_table",
      "tangible_type": "data_table",
      "params": {
        "orientation": "vertical",
        "categories": [
          "Round 1",
          "Round 2",
          "Round 3",
          "Round 4"
        ],
        "values": [
          22,
          15,
          8,
          31
        ],
        "description": "Vertical data table appears. Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31."
      },
      "id": "s2_5_practice_with_non_multiples_b0"
    },
    {
      "type": "dialogue",
      "text": "Here's data from a game. Four rounds of points: 22, 15, 8, 31.",
      "id": "s2_5_practice_with_non_multiples_b1"
    },
    {
      "type": "current_scene",
      "elements": [
        {
          "tangible_id": "data_table",
          "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
          "tangible_type": "data_table",
          "orientation": "vertical",
          "categories": [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4"
          ],
          "values": [
            22,
            15,
            8,
            31
          ]
        }
      ],
      "id": "s2_5_practice_with_non_multiples_b2"
    },
    {
      "type": "dialogue",
      "text": "Check the ones place digits: 2, 5, 8, 1. Do they all end in 0 or 5?",
      "id": "s2_5_practice_with_non_multiples_b3"
    },
    {
      "type": "dialogue",
      "text": "22... no. 15... yes! 8... no. 31... no. Three of them don't so they aren't multiples of 5. Which scale will show ALL values exactly?",
      "id": "s2_5_practice_with_non_multiples_b4"
    },
    {
      "type": "prompt",
      "text": "Which scale will show ALL values exactly?",
      "tool": "multiple_choice",
      "options": [
        "Scale of 1",
        "Scale of 2",
        "Scale of 5",
        "Scale of 10"
      ],
      "validator": [
        {
          "condition_id": "correct",
          "condition": {
            "selected": "Scale of 2"
          },
          "description": "Student selected Scale of 2, correct",
          "is_correct": true,
          "beats": [
            {
              "type": "scene",
              "method": "add",
              "tangible_id": "bar_graph_points",
              "tangible_type": "bar_graph",
              "params": {
                "mode": "reading",
                "orientation": "vertical",
                "categories": [
                  "Round 1",
                  "Round 2",
                  "Round 3",
                  "Round 4"
                ],
                "values": [
                  22,
                  15,
                  8,
                  31
                ],
                "scale": 2,
                "axis_range": [
                  0,
                  32
                ],
                "description": "Vertical bar graph appears. Points Scored. Scale of 2. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31. All bars land exactly on tick marks."
              },
              "id": "s2_5_practice_with_non_multiples_b5_v0_b0"
            },
            {
              "type": "dialogue",
              "text": "Right. Scale of 2. All of the bars fit well on the graph and their exact values are clear.",
              "id": "s2_5_practice_with_non_multiples_b5_v0_b1"
            },
            {
              "type": "current_scene",
              "elements": [
                {
                  "tangible_id": "data_table",
                  "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
                  "tangible_type": "data_table",
                  "orientation": "vertical",
                  "categories": [
                    "Round 1",
                    "Round 2",
                    "Round 3",
                    "Round 4"
                  ],
                  "values": [
                    22,
                    15,
                    8,
                    31
                  ]
                },
                {
                  "tangible_id": "bar_graph_points",
                  "description": "Vertical bar graph. Points Scored. Scale of 2. All bars land exactly on tick marks.",
                  "tangible_type": "bar_graph",
                  "mode": "reading",
                  "orientation": "vertical",
                  "categories": [
                    "Round 1",
                    "Round 2",
                    "Round 3",
                    "Round 4"
                  ],
                  "values": [
                    22,
                    15,
                    8,
                    31
                  ],
                  "scale": 2,
                  "axis_range": [
                    0,
                    32
                  ]
                }
              ],
              "id": "s2_5_practice_with_non_multiples_b5_v0_b2"
            }
          ]
        }
      ],
      "id": "s2_5_practice_with_non_multiples_b5"
    },
    {
      "type": "current_scene",
      "elements": [
        {
          "tangible_id": "data_table",
          "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
          "tangible_type": "data_table",
          "orientation": "vertical",
          "categories": [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4"
          ],
          "values": [
            22,
            15,
            8,
            31
          ]
        }
      ],
      "id": "s2_5_practice_with_non_multiples_b6"
    },
    {
      "type": "scene",
      "method": "update",
      "tangible_id": "bar_graph_points",
      "params": {
        "scale": 1,
        "axis_range": [
          0,
          31
        ],
        "description": "Bar graph updates to Scale of 1. Same Points Scored data."
      },
      "id": "s2_5_practice_with_non_multiples_b7"
    },
    {
      "type": "dialogue",
      "text": "Scale of 1 also shows the exact values, but it would require a lot of marks on the axis to get to the greatest value of 31. Let's consider when we might choose a scale of 1.",
      "id": "s2_5_practice_with_non_multiples_b8"
    },
    {
      "type": "current_scene",
      "elements": [
        {
          "tangible_id": "data_table",
          "description": "Vertical data table showing Points Scored. Round 1: 22, Round 2: 15, Round 3: 8, Round 4: 31.",
          "tangible_type": "data_table",
          "orientation": "vertical",
          "categories": [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4"
          ],
          "values": [
            22,
            15,
            8,
            31
          ]
        },
        {
          "tangible_id": "bar_graph_points",
          "description": "Vertical bar graph. Points Scored. Scale of 1. All bars visible.",
          "tangible_type": "bar_graph",
          "mode": "reading",
          "orientation": "vertical",
          "categories": [
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4"
          ],
          "values": [
            22,
            15,
            8,
            31
          ],
          "scale": 1,
          "axis_range": [
            0,
            31
          ]
        }
      ],
      "id": "s2_5_practice_with_non_multiples_b9"
    }
  ],
  "_generated_at": "2026-05-05T18:19:12.358465+00:00"
}
</input>

======================================================================

## Prefill

{"id": "s2_5_practice_with_non_multiples", "incorrects": [
