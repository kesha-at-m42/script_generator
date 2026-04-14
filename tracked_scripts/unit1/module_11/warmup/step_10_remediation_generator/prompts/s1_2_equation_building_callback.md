# Prompt: remediation_generator
# Generated: 2026-04-07T13:23:16.789756
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

**Version:** 3.1
**Last Updated:** March 2026
**Purpose:** Authoritative guide for all remediation across learning modules

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
**SECTION 9** \- Misconception Tracking & Intervention Triggers
**SECTION 10** \- Intervention Activity Overview
**SECTION 11** \- Remediation by Phase
**SECTION 12** \- Quality Checklist
**SECTION 13** \- Output Format Examples

---

## SECTION 1: System Architecture Overview

### 1.1 The Simplified Model

**v3 introduces a three-track approach based on question type:**

| Question Type | Remediation Approach | Rationale |
| :---- | :---- | :---- |
| **Non-MC** (create, shade, place, etc.) | Generic L-M-H only | Error cause often ambiguous; tracking handles patterns |
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
├── Non-MC: Generic L-M-H
│   └── Validators tag probable error type (for tracking only)
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

## SECTION 2: Non-MC Remediation (Generic L-M-H)

### 2.1 Overview

For all non-multiple-choice interactions (shading, partitioning, placing on number lines, dragging, etc.), use **Generic remediation only**.

**The validator still tags the probable error type** for misconception tracking, but the student receives generic feedback regardless of detected error.

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

### 2.4 Non-MC Structure

**Light (10-20 words):** Brief redirect, no visual **Medium (20-30 words):** Conceptual reminder \+ visual scaffold **Heavy (30-60 words):** Full modeling with \[Modeling\] tag, reveals answer

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

For a typical Multiselect MC question:

- **3 Medium remediations** (one per error branch)
- **1 Heavy remediation** (explains the full correct selection)

**No Light remediation for Multiselect MC.** Same rationale as Single-Select MC: a generic "check your answer" provides little help when the selection pattern gives specific diagnostic information.

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
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words with complete step-by-step demonstration]"
[Visual: System demonstrates complete solution]
Guide: "[Post-modeling acknowledgment]"
```

### 6.3 Heavy Structure (Single-Select MC)

For Single-Select MC, Heavy explains why the correct answer is right:

```
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words explaining the correct answer and demonstrating the thinking]"
[Visual: Correct answer highlighted with supporting scaffold]
Guide: "[Post-modeling acknowledgment]"
```

### 6.4 Heavy Examples

**Non-MC:** "Let me show you how this works. First, I count the total parts. That's my denominator: 4\. Then I count just the shaded parts. That's my numerator: 3\. So the fraction is 3/4." \[Visual: System highlights total parts, then shaded parts, then shows 3/4\]

**Single-Select MC:** "Let me show you how to think about this. The question asks which fraction is shown. I count 4 equal parts total. That's the denominator. 3 parts are shaded. That's the numerator. So the answer is 3/4, not 4/3." \[Visual: Correct answer highlighted, visual shows counting sequence\]

---

## SECTION 7: Post-Modeling Language

After Heavy remediation with \[Modeling\], use **only** language that acknowledges assisted success:

### 7.1 Approved Post-Modeling Phrases

- "There we go."
- "See how that works?"
- "It's okay if this takes a moment."
- "You're getting it now."
- "Now you understand."
- "That makes sense now, right?"
- "That's it. Now you've got it."
- "Good. You understand now."
- "Now you see the pattern."

### 7.2 NEVER Use After Modeling

- ❌ "Perfect\!" (they didn't do it alone)
- ❌ "You figured it out\!" (guide showed them)
- ❌ "Great job\!" (too independent)
- ❌ "Excellent work\!" (overpraises assisted work)

### 7.3 Post-Modeling Transitions

After Heavy remediation, move forward assuming understanding:

- "Let's try another one."
- "Now let's continue."
- "Ready for the next?"
- "Let's keep going."

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

## SECTION 9: Misconception Tracking & Intervention Triggers

### 9.1 How Tracking Works

Even though non-MC remediation is generic, **validators tag the probable error type** for every wrong answer. This feeds the misconception tracking system.

```
Student makes error → Generic remediation served
                   → Validator logs: "Probable Misconception #3"
                   → Running count updated

[After phase transition]
System checks: Has any misconception hit threshold?
    YES → Queue Intervention Activity
    NO → Continue normal flow
```

### 9.2 Tracking Parameters

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| **Trigger threshold** | 5 errors (placeholder) | TBD with data |
| **Rolling window** | Last 20 opportunities | Natural decay mechanism |
| **Window spans** | Lesson, Exit Check, Practice, Spiral Review, Test Prep | Cross-activity tracking |
| **Check timing** | Phase transitions | Engineer to confirm feasibility |
| **Post-Intervention threshold** | Window lowers to 15 | Catches continued struggle faster |

### 9.3 What Gets Tracked

**Tracked (feeds Intervention triggers):**

- Misconception indicators (\#1-\#10)
- Tracked per visual type for accuracy
- Combined at misconception level for Intervention trigger

**Not Tracked for Intervention:**

- Common procedural errors (counting mistakes, off-by-one)
- Random/ambiguous errors

### 9.4 Example Tracking Flow

```
Opportunity 1: Error on Rectangle Bar → Validator: Misconception #3 → Count: 1
Opportunity 5: Error on Number Line → Validator: Misconception #3 → Count: 2
Opportunity 9: Error on Rectangle Bar → Validator: Misconception #3 → Count: 3
Opportunity 14: Error on Grid → Validator: Misconception #3 → Count: 4
Opportunity 18: Error on Rectangle Bar → Validator: Misconception #3 → Count: 5 ← THRESHOLD

[At next phase transition]
→ Misconception #3 Intervention queued as next activity
```

---

## SECTION 10: Intervention Activity Overview

### 10.1 What Interventions Are

Intervention Activities are **standalone instructional sequences** that address a specific misconception directly. They sit outside regular modules and slot into the activity queue when triggered.

### 10.2 Intervention Scope

- **\~10 total** (one per misconception)
- **Combines visuals** (not visual-specific)
- **Path-flexible** (may use visuals from multiple paths with worked examples)

### 10.3 Intervention Structure

| Phase | Name | Purpose | Approach |
| :---- | :---- | :---- | :---- |
| 1 | **Clarify** | Name the misconception | Metacognitive: "A lot of students think X. Let's look at why that's hard to see..." |
| 2 | **Model** | Worked examples | Guide demonstrates across 2-3 examples using multiple visuals |
| 3 | **Confirm** | Independent verification | 2-3 problems student completes independently |

### 10.4 Queue Placement

- Intervention replaces whatever activity would have been next
- Multiple triggers \= multiple Interventions queued with brain breaks between
- Follows existing recess/break logic in Activity Queue

### 10.5 After Intervention

- Rolling window lowers to 15 (from 20\)
- If misconception continues to appear, re-triggers faster
- Alternative: Queue targeted Practice problems before re-triggering full Intervention

### 10.6 Intervention Design (Separate Document)

Full Intervention Activity design specifications in: **Intervention Activity Design Brief**

---

## SECTION 11: Remediation by Phase

### 11.1 Requirements by Phase

| Phase | Non-MC Requirement | Single-Select MC Requirement | Multiselect MC Requirement | Notes |
| :---- | :---- | :---- | :---- | :---- |
| Warmup | Light minimum | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Heavy if key prior knowledge |
| Lesson | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | All interactions |
| Exit Check | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | MANDATORY \- gateway phase |
| Practice | Full L-M-H | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Light only for confidence builders |
| Synthesis | Light minimum | Per-distractor Medium \+ Heavy | Per-branch Medium \+ Heavy | Full L-M-H for pattern discovery |
| Challenge | None | None | None | Assessment mode |

### 11.2 Module Complexity Considerations

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

## SECTION 12: Quality Checklist

### 12.1 Non-MC Remediation Checklist

- [ ] Generic L-M-H only (no branching by error type)
- [ ] Light: 10-20 words, no visual
- [ ] Medium: 20-30 words, visual REQUIRED
- [ ] Heavy: 30-60 words, \[Modeling\] tag REQUIRED, visual REQUIRED
- [ ] Different language at each level
- [ ] Post-modeling language acknowledges assistance (not independent success)
- [ ] Validator tags probable error type (noted in script or separate)

### 12.2 Single-Select MC Remediation Checklist

- [ ] One Medium per distractor (3 distractors \= 3 Mediums)
- [ ] Each Medium targets specific error that distractor represents
- [ ] One Heavy explaining correct answer
- [ ] All Mediums have visual scaffolds
- [ ] Heavy has \[Modeling\] tag
- [ ] No Light remediation (Single-Select MC skips to Medium)

### 12.2B Multiselect MC Remediation Checklist

- [ ] Three Medium remediations — one per error branch (under-selecting, all-wrong, mixed)
- [ ] Branch 2 Medium (under-selecting) acknowledges correct picks and nudges toward missing answers — near-success tone
- [ ] Branch 3 Medium (all-wrong) redirects to the concept without positively acknowledging selections — foundational tone, distinctly more remedial than Branches 2 and 4
- [ ] Branch 4 Medium (mixed) acknowledges correct picks genuinely and clearly flags what doesn't fit
- [ ] All three Mediums use generic language — no per-combination branching
- [ ] One Heavy explaining the full correct selection with \[Modeling\] tag
- [ ] All Mediums have visual scaffolds
- [ ] No Light remediation (Multiselect MC skips to Medium)
- [ ] Tone varies meaningfully across branches — remediation language does not feel uniform

### 12.3 Variety Checklist (Per Module)

- [ ] Minimum 8 different Light patterns (non-MC)
- [ ] 4-5 different Medium approaches
- [ ] "Remember" maximum 2-3 times total
- [ ] No exact phrase repeated within 3 problems
- [ ] Error signals rotated (40-50% with signal)

### 12.4 Structure Violations (Never Include)

- ❌ Alternative paths ("Try X or Y")
- ❌ Light remediation that teaches new content
- ❌ Medium without visual scaffold
- ❌ Heavy without \[Modeling\] tag
- ❌ Independent success praise after modeling
- ❌ More than 3 attempts before system takeover

---

## SECTION 13: Output Format Examples

### 13.1 Non-MC Format

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

### 13.2 Single-Select MC Format

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

### 13.2B Multiselect MC Format

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

### 13.3 Validator Notation

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

**Version:** 3.1
**Document Type:** Authoritative reference for script writers
**Major Changes from v2.0:**

- Simplified to two-track system (Non-MC generic, MC per-distractor)
- Removed three-type branching architecture
- Added Misconception Tracking & Intervention system overview
- Reduced content creation burden significantly
- Clarified MC structure (Medium per distractor \+ single Heavy)

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
  "steps": [ [...], [...] ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Unique section ID. See [Naming Conventions](#section-id-naming-conventions). |
| `type` | string | no | `"transition"` or `"remediation"`. Omit for normal sections. |
| `steps` | array[] | yes | Array of steps; each step is an array of beats |

Every section begins with an empty screen. There is no carry-over from the previous section. Everything visible must be explicitly put on screen by `scene` beats in the first step.

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

## Steps

`steps` is an **array of arrays**. Each inner array is one step, a group of beats that play together before the lesson pauses for student interaction.

```json
"steps": [
  [beat, beat, beat],   // step 1: scene setup + dialogue + prompt
  [beat, beat]          // step 2: follow-up after correct answer
]
```

Beats within a step follow this order:

1. **`scene`** — things appear or change on screen
2. **`dialogue`** — the guide speaks
3. **`prompt`** — student interacts (at most one per step)
4. **`current_scene`** — snapshot of the screen after all beats have played (always last)

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

Always the last beat in every step, and the last beat in every validator state's inner step. It is a pure derived snapshot: it reflects only what `scene` beats have established. Within a section, tangibles carry forward step to step — a tangible stays on screen until a `scene` beat removes or hides it. `current_scene` never introduces new tangibles or state that no `scene` beat has declared.

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

## Validator

A flat array of states evaluated **in order**; the first match wins. The final state is always an empty condition (`{}`) catch-all. Each state contains inline `steps`, beats that play when the state matches.

Every state must include `is_correct: true` or `is_correct: false`. `incorrect_count` is the one system parameter; all other condition keys are tangible-specific fields.

```json
"validator": [
  {
    "condition": { "selected": "Apples" },
    "description": "Student selected Apples",
    "is_correct": true,
    "steps": [
      [
        { "type": "scene", "method": "animate", "tangible_id": "pg_fruits",
          "params": { "event": "highlight_category", "status": "confirmed",
                      "description": "Apples row highlights to confirm selection", "category": "Apples" } },
        { "type": "dialogue", "text": "Apples got 6 votes, the most of any fruit." },
        { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
      ]
    ]
  },
  {
    "condition": { "incorrect_count": 1 },
    "description": "Student selected any wrong answer on first attempt",
    "is_correct": false,
    "steps": [
      [
        { "type": "dialogue", "text": "Look at the numbers next to each row. Which one is biggest?" },
        { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Picture graph unchanged.", "tangible_type": "picture_graph" } ] }
      ]
    ]
  },
  {
    "condition": { "incorrect_count": 2 },
    "description": "Student selected any wrong answer on second attempt",
    "is_correct": false,
    "steps": [
      [
        { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
          "params": { "highlight_categories": ["Apples"], "description": "Apples row highlights." } },
        { "type": "dialogue", "text": "Count the Apples row: 6 symbols. Count the others: Bananas 4, Oranges 5, Grapes 3. Which row has the most?" },
        { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
      ]
    ]
  },
  {
    "condition": {},
    "description": "Catch-all: any remaining state",
    "is_correct": false,
    "steps": [
      [
        { "type": "scene", "method": "update", "tangible_id": "pg_fruits",
          "params": { "highlight_categories": ["Apples"], "description": "Apples row highlights." } },
        { "type": "dialogue", "text": "Apples has 6 symbols, more than any other row. Click Apples." },
        { "type": "current_scene", "elements": [ { "tangible_id": "pg_fruits", "description": "Apples row highlighted.", "tangible_type": "picture_graph" } ] }
      ]
    ]
  }
]
```

| Field | Type | Description |
|---|---|---|
| `condition` | object | Matching condition. Multiple keys implicitly ANDed. Use `or`/`and` arrays for explicit logic. |
| `description` | string | Precise plain-English description of exactly what student state this condition captures. |
| `is_correct` | boolean | **Required.** `true` if this state represents a correct student response, `false` otherwise. |
| `steps` | array[] | Inline beats to play when this state matches. Same structure as section `steps`. |

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

Each state's `steps` contains the beats for that hint level. See the [Validator](#validator) section for a full example.

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

</lesson_script_schema_guide>

----------------------------------------------------------------------

### Block 4: Instructions
Purpose: Step-by-step task instructions
Cacheable: Yes

# TASK INSTRUCTIONS


## TASK

The section to process is in `<input>`. Walk its `steps` array and find every `prompt` beat. For each prompt, generate the incorrect validator states. Output one inner array of states per prompt, in the order the prompts appear in the section.

**Skip any prompt whose `validator` is a single state with `condition: {}`** (any-response-advances). Emit nothing for it.

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

For each qualifying prompt, check `tool.name`:

| `tool.name` | Track |
|---|---|
| `click_category`, `click_tangible`, or any workspace tool | **Non-MC** → Generic L-M-H |
| `multiple_choice` | **Single-Select MC** → Per-distractor Medium + Heavy |
| `multi_select` | **Multiselect MC** → Per-branch Medium + Heavy |

---

## STEP 2A: NON-MC: THREE STATES

Emit in this order. Follow length, visual, and language rules from `<remediation_design_ref>` Sections 4–6.

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

**Medium** (`incorrect_count: 2`): scene beat required.
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

**Heavy** (`condition: {}`): `scene animate` beat required (system demonstrates the answer).
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

See `<remediation_design_ref>` Section 3.2 for Single-Select MC structure (no Light state; per-distractor Mediums + one Heavy).

One **Medium** per distractor: scene beat required.
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

Identify **correct answers** from the success/correct validator state condition. All other options are **incorrect answers**.

See `<remediation_design_ref>` Section 3B for structure, branch definitions, language requirements, and condition patterns (no Light; Branches 2/3/4 Mediums + one Heavy).

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
1. Light (`incorrect_count: 1`)
2. Medium (`incorrect_count: 2`)
3. Heavy (`condition: {}`): always last

**Single-Select MC inner array:**
1. One Medium per distractor (any order among themselves)
2. Heavy (`condition: {}`): always last

**Multiselect MC inner array:**
1. Branch 2 Medium — under-selecting
2. Branch 3 Medium — all-wrong
3. Branch 4 Medium — mixed
4. Heavy (`condition: {}`): always last

---

## LANGUAGE RULES

Follow all language patterns, word counts, visual requirements, and prohibited constructs from `<remediation_design_ref>` Sections 4–8 and 12.4.

**Light:** Draw openers from `<remediation_design_ref>` Sections 4.1–4.2. Cycle through the full lists. Do not reuse the same phrase within a section.

**Medium:** Open with a starter from `<remediation_design_ref>` Section 5.1. Cycle through the full list. Do not reuse the same starter within a section. For MC: address specifically why the chosen distractor is wrong.

**Heavy:** Open with a phrase from `<remediation_design_ref>` Section 6.1. Cycle through the full list. Do not reuse the same opener within a section. States the correct answer explicitly with step-by-step demonstration. Follow post-modeling language from `<remediation_design_ref>` Section 7.

---

## SCOPE CONSTRAINTS

Use vocabulary naturally from <vocabulary>. Do not use phrases from <forbidden_phrases>. Reference <required_phrases> in Medium/Heavy where genuinely appropriate. Ground explanations in <the_one_thing>. Keep tangible references consistent with the section's `scene` array and existing scene beats.

---

## OUTPUT RULES

- Output ONLY the `incorrects` array content. No explanation, no markdown fences.
- The prefill already opens `{"id": "...", "incorrects": [`. Complete from that point.
- Use double quotes throughout
- `is_correct: false` on every state
- Do not use em dashes (—) or double hyphens (--) in any text field; to create a pause or connect two thoughts, use a period or comma instead



----------------------------------------------------------------------

### Block 5: Output Schema
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

## User Message

<input>
{
  "id": "s1_2_equation_building_callback",
  "beats": [
    {
      "type": "scene",
      "method": "add",
      "tangible_id": "equal_groups_bags",
      "tangible_type": "equal_groups",
      "params": {
        "groups": 3,
        "items_per_group": 5,
        "visual_style": "pictures",
        "container_type": "bags",
        "description": "Equal groups visual appears showing 3 bags with 5 items each."
      },
      "id": "s1_2_equation_building_callback_b0"
    },
    {
      "type": "scene",
      "method": "add",
      "tangible_id": "equation_builder_bags",
      "tangible_type": "equation_builder",
      "params": {
        "template": [
          "___",
          "×",
          "___",
          "=",
          "___"
        ],
        "palette": [
          2,
          3,
          4,
          5,
          6,
          8,
          12,
          14,
          15,
          16
        ],
        "description": "Equation builder appears alongside equal groups. Full equation template with three blanks. Tile palette shows numbers 2, 3, 4, 5, 6, 8, 12, 14, 15, 16."
      },
      "id": "s1_2_equation_building_callback_b1"
    },
    {
      "type": "dialogue",
      "text": "Let's warm up. Check out these bags. Build the equation.",
      "id": "s1_2_equation_building_callback_b2"
    },
    {
      "type": "prompt",
      "text": "Build the equation to match this picture.",
      "tool": "place_tile",
      "target": "equation_builder_bags",
      "validator": [
        {
          "condition": {
            "placed": {
              "groups": 3,
              "items": 5,
              "total": 15
            }
          },
          "description": "Student placed 3, 5, and 15 in equation slots, correct",
          "is_correct": true,
          "beats": [
            {
              "type": "scene",
              "method": "animate",
              "tangible_id": "equation_builder_bags",
              "params": {
                "event": "confirm_equation",
                "status": "confirmed",
                "description": "Equation confirms as correct: 3 × 5 = 15."
              },
              "id": "s1_2_equation_building_callback_b3_v0_b0"
            },
            {
              "type": "dialogue",
              "text": "Right. 3 times 5 equals 15.",
              "id": "s1_2_equation_building_callback_b3_v0_b1"
            },
            {
              "type": "current_scene",
              "elements": [
                {
                  "tangible_id": "equal_groups_bags",
                  "description": "Equal groups visual showing 3 bags with 5 items each.",
                  "tangible_type": "equal_groups",
                  "groups": 3,
                  "items_per_group": 5,
                  "visual_style": "pictures",
                  "container_type": "bags"
                },
                {
                  "tangible_id": "equation_builder_bags",
                  "description": "Equation builder showing confirmed equation: 3 × 5 = 15.",
                  "tangible_type": "equation_builder",
                  "template": [
                    "3",
                    "×",
                    "5",
                    "=",
                    "15"
                  ]
                }
              ],
              "id": "s1_2_equation_building_callback_b3_v0_b2"
            }
          ]
        }
      ],
      "id": "s1_2_equation_building_callback_b3"
    },
    {
      "type": "current_scene",
      "elements": [
        {
          "tangible_id": "equal_groups_bags",
          "description": "Equal groups visual showing 3 bags with 5 items each.",
          "tangible_type": "equal_groups",
          "groups": 3,
          "items_per_group": 5,
          "visual_style": "pictures",
          "container_type": "bags"
        },
        {
          "tangible_id": "equation_builder_bags",
          "description": "Equation builder with three empty blanks. Tile palette active with numbers 2, 3, 4, 5, 6, 8, 12, 14, 15, 16.",
          "tangible_type": "equation_builder",
          "template": [
            "___",
            "×",
            "___",
            "=",
            "___"
          ],
          "palette": [
            2,
            3,
            4,
            5,
            6,
            8,
            12,
            14,
            15,
            16
          ]
        }
      ],
      "id": "s1_2_equation_building_callback_b4"
    }
  ],
  "_generated_at": "2026-04-07T18:22:46.771161+00:00"
}
</input>

======================================================================

## Prefill

{"id": "s1_2_equation_building_callback", "incorrects": [

