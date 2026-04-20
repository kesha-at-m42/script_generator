# **📘 Edtech Activity Queue Rulebook v6**

Version March 2026  
---

## **🏛 Core Purpose**

The Edtech Activity Queue governs the sequencing of all learner-facing activities in the app. It ensures that:

* Students encounter the right type of activity at the right time  
* Daily sessions start with gentle re-entry  
* Mastery and struggle trigger appropriate follow-ups  
* Spaced and spiral review are woven into the flow  
* Tool introductions always happen in a supported instructional context  
* **Learning is tracked at multiple granularity levels for precise routing decisions**

---

### **Cognitive Verbs (Domain-Specific Actions)**

| Cognitive Verb | Description | Component Mapping | Example Skills |
| :---- | :---- | :---- | :---- |
| **CREATE** | Build or construct | PROCEDURAL | Shade 3/4, Partition into fifths, Build equivalent fraction |
| **IDENTIFY** | Recognize or select | CONCEPTUAL | Find unit fractions, Select equivalents, Name fraction shown |
| **COMPARE** | Determine relationships | CONCEPTUAL | Which is larger?, Order fractions, Judge equality |
| **APPLY** | Use in context | TRANSFER | Solve word problems, Real-world situations |
| **CONNECT** | Link representations | TRANSFER | Show multiple ways, Link visual to symbolic |

**Component Definitions:**

- **PROCEDURAL**: Can execute the core skill (tracked via CREATE)  
- **CONCEPTUAL**: Understands the concept (tracked via IDENTIFY, COMPARE)  
- **TRANSFER**: Can apply in new contexts (tracked via APPLY, CONNECT)

**Note:** SYNTHESIS has been replaced with CONNECT to avoid confusion with Synthesis Phase.  
---

## **⌚ Queue Timing Logic**

| Type | Basis | Use Case | Duration |
| ----- | ----- | ----- | ----- |
| Start of Day Recap | Time-based | First activity of each new session | 1-2 min |
| Fluency/Speed Challenge | Queue-scheduled | Automaticity practice on mastered content (daily) | 3-5 min |
| Warm-Up | Contextual | New module or return | 2-3 min |
| Lesson | Session-based | New concept introduction | 8-10 min |
| Exit Check | Post-Lesson | Readiness assessment | 3-4 min |
| Practice | Post-Exit Check | Skill building | 15 min max |
| Synthesis | Post-Practice | Generalization | 6-8 min |
| End of Day Recap | Time-based | Last activity before transition to Freeplay | 1-2 min |
| Test Prep | Weekly / curriculum-position | Representational bridge \+ strategy instruction \+ format exposure | 5-10 min |
| Challenge | TBD | Scope undefined — see note below | \~5 min |
| Spiral Review | See Schedule | Retention & transfer; Tool Intros may trigger before | 8-10 min |
| Intervention | Misconception threshold | Targeted misconception remediation (signal from Remediation System) | 5-8 min |

Total Module Target: \~25-30 minutes

Note on Challenge: Challenge is listed as a placeholder. It may overlap with Test Prep, serve as a lighter mastery pulse-check, or be something else entirely. Decision pending. If it's a subset of Test Prep, collapse them. If it's a distinct mastery check, keep it separate.

---

## **📈 Mastery Definitions & Thresholds**

More Details here: [Universal Mastery Tracking Framework v3](https://docs.google.com/document/d/1JFSm4j3JMFmTIEiIurpvlr9zhY4HfSHsF7jeq_bgnB0/edit?usp=sharing)

### **Exit Check (Readiness Assessment)**

Purpose: Quick confidence check before Practice   
Problems: 3 total   
Duration: 3-4 minutes

Scoring & Routing:

* 3/3 correct → Proceed to Practice  
* 2/3 correct → Proceed to Practice (marginal pass)  
* 1/3 correct → Intervention Options: a) Repeat Lesson after recess/break b) Offer Path Switch choice  
* 0/3 correct → Strongly recommend Path Switch

Rationale: Small sample size demands quick response to prevent frustration buildup No retry within same session \- either repeat after break or switch paths

### **Practice Phase (Skill Development)**

Purpose: Build fluency through adaptive practice  
Duration: 15 minutes maximum   
Problems: 10-12 per attempt

PHASE 1 SCORING (Current \- Testing):

* Pass Threshold: 70% on BASELINE/STRETCH problems  
* Transfer Gate: Must pass 1+ APPLY or CONNECT problem  
* SUPPORT/CONFIDENCE problems don't count toward mastery

Multi-Level Adaptive System:

Level 1 \- Problem Remediation (Every Problem):

* Light: Gentle hint after wrong  
* Medium: Conceptual support if still wrong  
* Heavy: Full modeling with \[Modeling\] tag

Level 2 \- Within-Attempt Adaptation:

* 2 incorrect in row → Insert SUPPORT problem (easier, doesn't count)  
* SUPPORT failed → Insert CONFIDENCE problem (very easy, doesn't count)  
* NO EARLY EXIT \- must complete all 10-12 problems (prevents gaming)

Level 3 \- Between-Attempt Routing:

* Attempt 1: \<70% → Try once more with adjustments  
* Attempt 2: \<70% → AUTOMATIC PATH SWITCH  
* Maximum attempts: 2 (testing hypothesis, may adjust to 3 based on data)

Problem Classification:

* BASELINE: Core assessment (counts toward mastery)  
* STRETCH: Extended assessment (counts toward mastery)  
* SUPPORT: Confidence building (doesn't count)  
* CONFIDENCE: Emotional support (doesn't count)  
* CHALLENGE: Bonus only (if time permits)

---

## **🧠 Routing Decision Engine**

### **Routing Decision Matrix**

**PHASE 1 ROUTING (Current \- Simple)**

```javascript
// Simple routing based on overall performance only

// Exit Check Routing
IF exit_check_score <= 1/3:
  → Offer: Repeat lesson after break OR Path switch
ELSE:
  → Continue to Practice

// Practice Phase Routing  
IF practice_attempt == 1 && score < 0.70:
  → Try again with increased support
  
IF practice_attempt == 2 && score < 0.70:
  → AUTO PATH SWITCH (no 3rd attempt)
  
IF score >= 0.70 && transfer_gate_passed:
  → Continue to next module

// Within-Practice Adaptation
IF consecutive_wrong >= 2:
  → Insert SUPPORT problem (doesn't count)
  
IF support_failed:
  → Insert CONFIDENCE problem (doesn't count)

// Anti-gaming Rule
NO EARLY EXIT - Must complete all 10-12 problems
```

### **Phase-Specific Routing Constraints**

**Critical Rule:** Path reroutes ONLY occur after repeated failure in:

* Practice Phase  
* Exit Check

**NO rerouting from:**

* Warm-Up (always completes)  
* Synthesis (diagnostic only)  
* Challenge (assessment mode)  
* Spiral Review (reinforcement only)

### **Rerouting Triggers**

**Immediate Rerouting Consideration:**

* Exit Check: 1/3 or 0/3 correct (offer path switch)  
* Practice: Failed 2 attempts without reaching 70%  
* Transfer Gate: Cannot pass any APPLY/CONNECT problems

**Adaptive Support (Not Rerouting):**

* 2 wrong in row → SUPPORT problem inserted  
* SUPPORT failed → CONFIDENCE problem inserted  
* Heavy remediation 2x → More scaffolding, not path switch

**Path Switch Protocol:**

1. Only after 2 full Practice attempts OR Exit Check failure  
2. Never mid-attempt (must complete all problems)  
3. Accompanied by tool introduction if needed  
4. Track reason for data analysis

---

## **STANDALONE TOOL INTRODUCTIONS:**

* Duration: 3-4 minutes  
* Triggered: When tool\_never\_seen OR major\_interaction\_new  
* Structure:  
  * Name and connect to familiar tool (30 sec)  
  * Recognition practice (1 min)  
  * Guided manipulation (1.5 min)  
  * Simple application (1 min)  
* Tags: \[Tool\_Intro\], \[Transfer\_Thinking\], \[System\_Leverage\]  
* Heavy scaffolding acceptable throughout

PATH B (Singapore) \- STRICT:

- Shaded rectangle bars (horizontal)  
- Number lines with bars ABOVE  
- Combined representations  
- NO area models, NO other variations

PATH C (VPSS):

- Pattern tiles (modules 1-3, 8-12)  
- Grid arrays (multi-row for non-number line work)  
- Circles (partitioned)  
- Single-row grid overlays ON number lines (modules 4-7)

VISUAL CONVERGENCE ZONES: Modules 4-7: Both paths use number lines

- Path B: Bars above line  
- Path C: Single-row grid on line  
- Minimal visual transfer needed

---

## **🔄 Tool Introduction & Tracking**

### **Scaffolding Rules**

**Major Interactions** (require introduction on first exposure):

* Partition, Shade, Construct, Transform

**Minor Interactions** (transfer from similar tools):

* Recognize, Select, Compare, Tap

### **Conditional Tool Introduction**

```
IF tool_never_seen:
  [Tool_Intro] Full introduction with 2-3 practice problems
  
ELIF major_interaction_never_done:
  [Light_Scaffold] Brief demonstration then try
  
ELSE:
  No scaffolding needed
```

---

## **SPIRAL REVIEW SCHEDULE:**

* After Module 4: Review Modules 2-3 content  
* After Module 8: Review Modules 4-7 content  
* After Module 10 or 11: Review Modules 8-9 content  
* After Module 12: Review Modules 10-11 content

Duration: 8-12 minutes per review Structure: Two sections (see below)

## **SPIRAL REVIEW SCRIPT STRUCTURE 📊**

4 Review Points × 2 Path Versions \= 8 Scripts

Each script has:

- MAIN SECTION: Uses student's CURRENT path tools  
- TRANSFER SECTION: Shows OTHER path tools

Which spiral review script a student gets should be triggered by their CURRENT PATH.

### **The 8 Scripts:**

1. **spiral\_review\_2\_3\_path\_B.md**  
   * Main: Singapore bars (current path)  
   * Transfer: VPSS circles/tiles (exposure)  
2. **spiral\_review\_2\_3\_path\_C.md**  
   * Main: VPSS patterns (current path)  
   * Transfer: Singapore bars (exposure)  
3. **spiral\_review\_4\_7\_path\_B.md**  
   * Main: Bars above number lines (current)  
   * Transfer: Grid overlay (minimal \- 5%)  
4. **spiral\_review\_4\_7\_path\_C.md**  
   * Main: Grid overlay on lines (current)  
   * Transfer: Bars above (minimal \- 5%)  
5. **spiral\_review\_8\_9\_path\_B.md**  
   * Main: Singapore bar equivalence (current)  
   * Transfer: Pattern tile equivalence (50%)  
6. **spiral\_review\_8\_9\_path\_C.md**  
   * Main: Visual pattern equivalence (current)  
   * Transfer: Bar model equivalence (50%)  
7. **spiral\_review\_10\_11\_path\_B.md**  
   * Main: Bar comparison methods (current)  
   * Transfer: Circle/grid comparison (70%)  
8. **spiral\_review\_10\_11\_path\_C.md**  
   * Main: Visual comparison (current)  
   * Transfer: Bar comparison methods (70%)

## ---

### **Fluency/Speed Challenge**

Standalone timed activities that build math fact automaticity and computational fluency. The math equivalent of "Fast Math" — students practice previously taught skills under light time pressure, competing against their own personal best. No new instruction; the toy carries the experience.

**Core Principle:** Timed practice on *already-mastered* material improves automaticity. Timed practice on *not-yet-mastered* material creates anxiety and reinforces errors. The content boundary is the single most important constraint.

**Why this is different from Practice:** Practice builds mastery — students encounter new problem types, receive remediation, and the system decides whether they've learned the skill. Fluency/Speed Challenge assumes mastery is already established and focuses purely on speed and accuracy of retrieval. No teaching, no remediation, no mastery gating.

**Parameters:**

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| Duration | 3-5 min | Brief — energizing, not exhausting |
| Phase structure | Brief Intro → Activity (toy-driven) | No 5-phase module structure |
| Guide role | Minimal — brief setup, celebration at end | Toy carries the experience |
| Mastery impact | None | Performance tracked but doesn't gate progression |
| Content source | Mastered modules only | Never introduces unlearned material |

**Pedagogical Guardrails:**

* **Mastered content only** — system serves problems exclusively from modules the student has passed (≥70% \+ transfer gate)  
* **Personal best, not competition** — no leaderboards, no peer comparison. Student competes against their own history  
* **No mastery impact** — performance data is informational, never gating  
* **Energizing, not punishing** — time pressure should feel like a game, not a test. No fail states.  
* **Always completable** — every session ends with a sense of accomplishment  
* **Errors are data, not events** — wrong answers tracked quietly for pattern analysis. No visible error count, no "lives"  
* **No extrinsic reward mechanics** — no coins, unlockables, or streaks. Conflicts with SDT.

**Content Rules:**

* Single-step or fast-retrieval problems only (automaticity, not problem-solving)  
* Skills from current unit AND prior units (cross-unit review is valuable)  
* Difficulty scales via speed targets, mix complexity, number range — not harder math  
* All content draws from the student's mastered pool

**What Gets Tracked (not for mastery):**

* Accuracy (% correct)  
* Speed (problems per minute or avg response time)  
* Personal best history  
* Error patterns (may feed Remediation System validators)  
* Session-over-session trend

**Queue Placement:**

* Target: 1x per session (daily), typically after Start-of-Day Recap  
* Alternative slots: between modules (palate cleanser), after Spiral Review  
* Never mid-module  
* Displaced by: Intervention, required Spiral Review, Test Prep  
* Counts toward educational time  
* Brain Break eligible after completion

**Guide Role:**

* **Before:** Brief, energizing — "Ready to see how fast you've gotten?" Optionally reference personal best.  
* **During:** Silent or minimal. No per-problem feedback. Uninterrupted rhythm.  
* **After:** Brief, effort-focused celebration. New personal best → "New record\!" No new personal best → "Solid session. That practice builds speed over time." Never frame not-improving as failure.

See: **Fluency/Speed Challenge FDB** for full design brief (including open game design surface for designers/devs).

---

### **Test Prep Activity**

Test Prep bridges between how Level teaches concepts and how state assessments represent and test them. It serves three purposes that no other activity covers:

**1\. Representational Bridge** Students learn fractions with bar models and grids in Level's curriculum — but STAAR shows area models, SBAC uses number lines, and MAPS frames the same skill as a multi-step word problem. Test Prep introduces visuals and toys *not in our curriculum* so students recognize their knowledge in unfamiliar formats.

Example: "You've been using bar models. This test shows the same fraction as a shaded circle. Same idea — what fraction is shaded?"

**2\. Test-Taking Strategy Instruction** Process of elimination, reading all answer choices before selecting, identifying key words in a question stem, checking work against the question asked, knowing when to skip and come back. These are teachable skills that matter for performance but don't belong in content modules.

**3\. Format Exposure** Students work through problems in test-like conditions (no Guide support, timed feel, unfamiliar layout) so the real test isn't the first time any of it feels new.

**Parameters:**

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| Duration | 5-10 min | Varies by purpose — strategy instruction runs longer |
| Guide role | Varies by purpose (see below) | Not a single mode |
| Mastery impact | Diagnostic only | Results inform routing but don't count toward module mastery |
| Remediation | Varies by purpose | Strategy instruction includes feedback; format exposure does not |
| Student skip | Not allowed | But kept short to minimize friction |

**Guide Role by Purpose:**

| Purpose | Guide Involvement |
| :---- | :---- |
| Representational bridge | Brief frame ("You already know this — here's how it looks on their test"), then student works |
| Strategy instruction | Active — teaches and models ("Before you pick, let's cross off the ones that can't be right") |
| Format exposure | Silent during; brief debrief after |

**Test-Taking Strategies to Teach:**

| Strategy | What the Guide Models |
| :---- | :---- |
| Process of elimination | "Let's cross off answers that CAN'T be right" |
| Read all choices first | "Don't pick the first one that looks right — check them all" |
| Key word identification | "Circle the word that tells you what to DO" |
| Check against the question | "Your math is right — but did you answer what they ASKED?" |
| Skip and return | "If one is tricky, mark it and come back" |
| Estimation as check | "Before you solve, roughly what should the answer be?" |

**State-by-State Adaptation:**

Test Prep content is tagged by target assessment so the queue serves the right content for each student.

| Dimension | How It Varies |
| :---- | :---- |
| Visual representations | STAAR uses area models heavily; SBAC favors number lines |
| Question stem formatting | SBAC Part A/Part B structure vs. single-question formats |
| Answer input types | MC, gridded response, drag-and-drop, typed numeric entry |
| Multi-step structures | SBAC performance tasks vs. discrete items |
| Emphasis areas | Texas emphasizes computation; CA emphasizes reasoning |

**Content Scope:**

* Draws from mastered and in-progress module content  
* May use visual tools (toys) NOT in Level's instructional curriculum — this is intentional  
* Includes cross-module problems combining skills  
* No trick questions or gotchas — the goal is confidence, not traps  
* Strategy instruction is domain-general but uses domain-specific examples

**What Gets Tracked (diagnostic only):**

* Accuracy by standard/skill  
* Performance by question format (MC, constructed response, gridded, multi-step)  
* Representational transfer success (can they apply known skills to unfamiliar visuals?)  
* Strategy application patterns  
* Time-on-task

**Queue Placement:**

* Scheduled weekly (specific day TBD)  
* Ramps up in Modules 10-12 (assessment prep zone)  
* Slots in after completed module or Spiral Review — never mid-module  
* Can be displaced by Intervention  
* Counts toward educational time  
* Brain Break eligible after

**Curriculum Position Ramp:**

| Unit Phase | Frequency | Emphasis |
| :---- | :---- | :---- |
| Modules 1-4 | 1x/week | Strategy instruction \+ light format exposure |
| Modules 5-8 | 1x/week | Balanced across all three purposes |
| Modules 9-10 | 1-2x/week | Heavier representational bridge |
| Modules 11-12 | 2-3x/week | Full format exposure, simulate test conditions |

**Key Principles:**

* **Normalize, don't stress** — "This is just practice, and it helps you get ready"  
* **Transfer is the point** — connecting what they know to how it's represented elsewhere  
* **Strategies are real instruction** — process of elimination is a teachable skill, not something kids figure out on their own  
* **Diagnostic, not punitive** — results route to support, never to consequences  
* **State-specific** — same core curriculum, Test Prep adapts to each state's testing reality

See: **Test Prep Activity FDB** for full specification including open questions.

---

### **Start/End-of-Day Recap**

Session bookends that anchor where a student is in their learning journey. Start-of-Day re-orients after time away. End-of-Day reinforces effort and previews what's next. Both are brief, warm, and non-assessmentive.

**Start-of-Day Recap:**

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| Trigger | First activity of each new session | Automatic — always first |
| Duration | 1-2 min | Brief re-entry |
| Guide role | Welcoming, orienting | "Here's where you are, here's what's next" |
| Mastery impact | None | No assessment |

What it does:

* Welcomes student back  
* Reminds where they left off (module, phase, concept)  
* Previews what's coming (sense of direction, not detailed agenda)  
* If returning after multiple days, may include warm-up reference

What it does NOT do:

* Assess or quiz  
* Teach new content  
* Require meaningful interaction (click-through is fine)  
* Reference calendar time — uses session-relative language ("last time," not "yesterday")

**End-of-Day Recap:**

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| Trigger | educational\_content\_time ≥ 35 minutes | At next natural break point after threshold |
| Duration | 1-2 min | Brief closure |
| Guide role | Celebratory, forward-looking | "Here's what you accomplished, here's what's ahead" |
| Mastery impact | None | No assessment |
| Follows | Transition to FreePlay | Session complete after recap |

**Trigger Logic:**

```
IF educational_content_time >= 35 minutes:
  → At next phase transition, queue End-of-Day Recap
  → After Recap → Transition to FreePlay
  → Session complete
```

What it does:

* Names what the student accomplished ("Today you worked on comparing fractions and did a spiral review")  
* Acknowledges effort, not just performance  
* Previews next session  
* Transitions to FreePlay

What it does NOT do:

* Summarize scores or accuracy  
* Assign homework or preview obligations  
* Create anxiety about unfinished work  
* Reference absolute time

**Queue Rules (both):**

* Start-of-Day: always first, before any educational activity (including Fluency/Speed Challenge)  
* End-of-Day: always last educational activity, immediately before FreePlay  
* Neither displaced by other queue items  
* Neither counts toward the 35-minute educational time threshold (they bookend it)  
* Brain Breaks NOT offered between Recap and next/previous activity (momentum)

**Key Principles:**

* **Session-relative language only** — "last time / this time / next time," never "yesterday / today / tomorrow"  
* **Effort-focused, not score-focused**  
* **Brief and warm** — greetings and goodbyes, not instructional events  
* **Consistent rhythm** — every session starts and ends the same way

---

## **🎮 Anti-Gaming Measures**

### **Preventing Intentional Failure**

**Critical Rules:**

1. **NO EARLY EXIT** \- Students must complete all 10-12 Practice problems  
2. **SUPPORT doesn't count** \- Failing to get easier problems doesn't help  
3. **Path switch only after genuine attempts** \- Not immediate escape  
4. **All patterns tracked** \- Suspicious behavior flagged for teachers

**Why This Matters:** Students may try to fail intentionally to:

- Exit Practice early (prevented by no early exit)  
- Get easier problems (SUPPORT doesn't count toward mastery)  
- Switch to perceived "easier" path (requires 2 full attempts)

---

### **Component Tracking (Phase 1 \- Background Only)**

**What We're Tracking:** Even though Phase 1 uses simple scoring (70% overall), we track component performance to understand patterns.

**How Components Map to Problem Types:**

```javascript
// Every problem tagged with its cognitive verb
PROCEDURAL problems = CREATE verbs (making/building)
CONCEPTUAL problems = IDENTIFY, COMPARE verbs (understanding)
TRANSFER problems = APPLY, CONNECT verbs (using in context)
```

**Phase 1 (Current):**

* Track all component scores in background  
* Use simple 70% threshold for pass/fail  
* All students get same problem distribution

**Phase 2 (Potential Future \- IF Data Supports):** Component scores might influence practice problem selection:

```javascript
// HYPOTHETICAL Phase 2 Problem Selection
IF student.CONCEPTUAL < 60%:
  → Practice includes MORE IDENTIFY/COMPARE problems
  → Remediation focuses on visual understanding
  → Still same path, just different problem mix
  
IF student.PROCEDURAL < 60%:
  → Practice includes MORE CREATE problems
  → Remediation adds extra scaffolding/modeling
  → Still same path, just more hands-on practice

IF student.TRANSFER < 60%:
  → Practice includes MORE APPLY/CONNECT problems
  → Add word problems and contexts
  → Still same path, just more application practice
```

**What Component Tracking WON'T Do:**

* Won't trigger path switches (that's for overall failure)  
* Won't prevent progression (if 70% overall met)  
* Won't change lesson content

**What It MIGHT Do (If Validated):**

* Adjust practice problem distribution  
* Customize remediation language  
* Inform teacher about specific weaknesses  
* Surface targeted support materials

**Example:**

```
Student A: 70% overall, weak CONCEPTUAL (40%)
Phase 1: PASSES, continues normally
Phase 2 (hypothetical): PASSES, but next practice has extra IDENTIFY problems
Student B: 70% overall, weak TRANSFER (45%)  
Phase 1: PASSES, continues normally
Phase 2 (hypothetical): PASSES, but next practice has extra word problems
```

**Why We're Not Sure Yet:**

* Maybe overall score is sufficient  
* Maybe component breakdown doesn't predict success  
* Maybe all students need balanced practice regardless  
* Need data to validate before adding complexity

---

## **🎯 Misconception Intervention System (Phase 2\)**

**Architecture Note:** The Intervention system has two homes. The *trigger mechanics* (pattern detection, rolling window, threshold, validator tagging) live in the **Remediation FDB** as System 2: Pattern Detection. The *queue behavior* (when to insert, what it displaces, break rules) lives here in the Activity Queue. The *activity structure* (Clarify → Model → Confirm) lives in the **Intervention Activity FDB**. This section covers the queue behavior and references the other two for their respective domains.

### Overview

Intervention Activities are standalone instructional sequences that address persistent misconceptions. They trigger when background tracking detects a pattern of errors suggesting the same underlying misconception.

**Key Principle:** Single errors are noisy—we don't diagnose misconceptions from one mistake. Pattern detection across multiple opportunities is more accurate, and dedicated Interventions provide better conceptual support than in-the-moment micro-corrections.

### How It Works

```
Student makes error → Immediate remediation served (L-M-H)
                   → Validator logs probable misconception
                   → Running count updated in rolling window

[At phase transition]
System checks: Has any misconception hit threshold?
    YES → Queue Intervention Activity as next item
    NO → Continue normal flow
```

### Tracking Parameters

| Parameter | Value | Notes |
| :---- | :---- | :---- |
| **Trigger threshold** | 5 errors | Placeholder—TBD with data |
| **Rolling window** | Last 20 opportunities | Natural decay mechanism |
| **Window spans** | Lesson, Exit Check, Practice, Spiral Review, Test Prep | Cross-activity tracking |
| **Check timing** | Phase transitions | Not mid-activity |
| **Post-Intervention window** | Lowers to 15 | Catches continued struggle faster |

### What Gets Tracked

**Tracked (feeds Intervention triggers):**

- Misconception indicators (\#1-\#10)  
- Tracked per visual type for accuracy  
- Aggregated at misconception level for trigger

**Not tracked for Intervention:**

- Common procedural errors (counting mistakes, off-by-one)  
- Random/ambiguous errors

### Intervention Activity Structure

| Phase | Name | Purpose | Duration |
| :---- | :---- | :---- | :---- |
| 1 | **Clarify** | Name the misconception metacognitively | \~1-2 min |
| 2 | **Model** | Worked examples across 2-3 problems | \~2-3 min |
| 3 | **Confirm** | Independent problems to verify understanding | \~2-3 min |

**Total Duration:** 5-8 minutes

### Queue Placement Rules

1. **Triggers at phase transition** — never interrupts mid-activity  
2. **Replaces next scheduled activity** — slots into queue position  
3. **Brain breaks apply** — if recess was due, it happens first  
4. **Multiple triggers** — queue multiple Interventions with brain breaks between

**Example Flow:**

```
Student completes Practice → Phase transition
System checks: Misconception #3 count = 6 (threshold = 5)
    → Queue: Misconception #3 Intervention
    
Next scheduled: Synthesis
Actual next: Misconception #3 Intervention → then Synthesis
```

### Multiple Misconception Triggers

If multiple misconceptions hit threshold simultaneously:

1. Queue all triggered Interventions  
2. Brain breaks between each (standard recess rules)  
3. No maximum limit (rare to trigger 3+)  
4. Order by: most recent trigger first

**Example:**

```
Misconception #3: Hit threshold at Practice end
Misconception #6: Hit threshold at Practice end

Queue becomes:
→ Intervention #3
→ Brain Break (if recess due)
→ Intervention #6
→ Original next activity (Synthesis)
```

### Post-Intervention Behavior

⚠️ **This section contains hypotheses.** We need data to validate.

**Current Thinking:**

| Question | Hypothesis | Confidence |
| :---- | :---- | :---- |
| Should there be a cooldown? | Yes—probably not same day | Medium |
| Cooldown mechanism | Time-based (24h) vs. trigger-based (after X activities) | Low |
| Threshold after Intervention | Lower window to 15? Or keep at 20? | Low |

**Options we're considering:**

| Option | Pros | Cons |
| :---- | :---- | :---- |
| **Cooldown period** (not same day) | Prevents frustrating repetition; time for concepts to settle | Student continues making errors in meantime |
| **Lower threshold for re-trigger** (window shrinks to 15\) | Catches continued struggle faster | Could feel punitive if triggered repeatedly |
| **Queue targeted Practice first** | Lighter touch; more exposure before full Intervention | Adds complexity; not yet designed |
| **Flag for teacher review** | Human judgment on persistent gaps | Depends on teacher dashboard (not built) |

**Current lean:** Some kind of cooldown makes sense—not same day feels right intuitively. But we need to test whether that means the student just keeps struggling without support until tomorrow.

**Unresolved:** Should cooldown be time-based (24 hours) or trigger-based (after X more activities)?

### Anti-Gaming Considerations

- Interventions cannot be skipped  
- Must complete all three phases (Clarify, Model, Confirm)  
- Confirm phase problems don't count toward module mastery  
- Completing Intervention doesn't grant any progression credit

### Engineering Requirements

**Tracking System:**

- Per-student, per-misconception rolling window counter  
- Validator tagging on every interaction  
- Phase transition threshold check  
- Counter reset logic (lowers to 15 post-Intervention)

**Queue System:**

- Intervention as activity type  
- Priority insertion at queue head  
- Multiple Intervention queuing with break insertion

**Validator Format:**

```
[Validator: Tracks toward Misconception_#3, Misconception_#6]
```

---

### **Hierarchy of Support**

**Phase 1 (Current):**

1. **Light Remediation** (first error)  
   * Gentle redirection (10-20 words)  
   * "Check the parts more carefully"  
2. **Medium Remediation** (second error)  
   * Conceptual reminder \+ guidance (20-30 words)  
   * "Equal parts means each piece is the same size"  
3. **Heavy Remediation** (third error)  
   * Full modeling with demonstration (30-60 words)  
   * \[Modeling\] tag required

**Phase 2 Additions:**

* **Non-MC questions:** Generic L-M-H only (validators track misconceptions in background)  
* **MC questions:** Per-distractor Medium \+ single Heavy  
  * Each distractor gets targeted feedback  
  * No Light for MC (if they knew, they'd have picked it)  
* **Misconception Interventions:** Triggered by pattern detection, not immediate feedback  
  * See "Misconception Intervention System" section

---

## **📱 Current Design: Session Structure**

### **Daily Session Design (Temporary \- October Build Only)**

**Total Session:** \~60 minutes

* Educational Content: 30-40 minutes  
* Recess/Entertainment: 20-30 minutes  
* Ratio: Roughly 2:1 education to entertainment

### **Recess Specifications**

**Trigger Logic:**

```
After 10-15 minutes of educational content:
  → Offer Recess opportunity (at natural break point)
  → Student can choose: Take Recess OR Continue Learning
  
Natural Break Points:
  - Between phases (never mid-phase)
  - After Practice completion
  - After module completion
  - NOT between Warm-Up and Lesson
  - NOT during Exit Check sequence
```

**Recess Structure:**

* **Duration:** 10 minutes exactly  
* **Content:** Pure entertainment (games/videos)  
* **Selection:** Student choice  
* **Timer Display:** Visible countdown  
* **9-Minute Warning:** "You have 1 minute left of recess"  
* **Auto-Return:** At 10:00, automatic pull back to educational queue  
* **Guide Framing:** "Great work\! Time for a brain break. I'll see you in 10 minutes."

### **Brain Breaks**

Brain Breaks are short entertainment experiences (30 seconds to \~3 minutes) that slot between instructional activities. They're distinct from Recess.

**Brain Breaks vs. Recess:**

| Aspect | Brain Breaks | Recess |
| :---- | :---- | :---- |
| Duration | 30s \- 3 min | 10 minutes exactly |
| Trigger | After completing activities | After 10-15 min education |
| Content | Curated experiences | Full student choice |
| Skip | Always skippable | Student chooses when to take |
| Purpose | Joy \+ cognitive shift \+ effort acknowledgment | Extended autonomy \+ recovery |

**Placement Rules:**

| Placement | Status |
| :---- | :---- |
| After Exit Check | ✓ Appropriate |
| After Practice | ✓ Appropriate |
| After Synthesis | ✓ Appropriate |
| After Intervention | ✓ Appropriate |
| After Spiral Review | ✓ Appropriate |
| After Fluency/Speed Challenge | ✓ Appropriate |
| After Test Prep | ✓ Appropriate |
| Mid-activity | ✗ Never |
| Between Warmup → Lesson | ✗ Avoid (momentum) |
| Between Lesson → Exit Check | ✗ Avoid (momentum) |

**Key Principles:**

* **Effort-contingent, not performance-contingent** — Everyone who completes an activity gets access; never withheld based on score  
* **Always skippable** — Student autonomy preserved  
* **No failure states** — Every interaction has an enjoyable outcome  
* **No disguised assessment** — Genuine entertainment, not learning in disguise  
* **Either/or with Recess** — If Recess is due, offer Recess; if not, Brain Break may be offered. Never stack both at the same transition.

**Note:** Brain Breaks don't affect routing or mastery. Completion/skip has no impact on progression.

See: **Brain Breaks Content Guide** for full design guidelines and content categories.

### **End-of-Day Trigger**

```
IF educational_content_time >= 35 minutes:
  → Queue End-of-Day Recap
  → Transition to FreePlay
  → Session complete
```

### **Sample Daily Flow (Current Design \- hour long session)**

```
Start → Start-of-Day Recap (1-2 min)
 → Fluency/Speed Challenge (3-5 min) [if scheduled — typical daily opener]
 → Module 5 Warm-Up (3 min)
 → Module 5 Lesson (10 min)
 → Module 5 Exit Check (3 min)
 → [Brain Break - 30s-3min, skippable] OR [Recess Opportunity - 10 min if taken]
 → Module 5 Practice (15 min)
 → [Brain Break - 30s-3min, skippable] OR [Recess Opportunity - 10 min if taken]
 → Module 5 Synthesis (8 min)
 → [Brain Break - 30s-3min, skippable]
 → [Intervention — if triggered at any phase transition]
 → Spiral Review Module 3 (5 min) OR Test Prep (5-10 min, if weekly)
[Check: Have we hit 35+ min education?]
 → End-of-Day Recap (1-2 min) → FreePlay (remainder of time)
```

Note: This is a representative flow, not a fixed sequence. The Activity Queue assembles each session dynamically. Fluency/Speed Challenge may slot elsewhere. Interventions insert at any phase transition. Test Prep may replace a Spiral Review slot. The queue optimizes based on student profile, performance, and available time.

---

**Brain Break vs. Recess Logic:**

- If Recess is due (10-15 min education threshold), offer Recess  
- If Recess is NOT due, Brain Break may be offered  
- Never stack both at the same transition point

**Note:** Exact logic TBD through testing—Brain Breaks may serve as Recess alternative in some contexts.  
---

## **✅ Implementation Priorities**

### **Phase 1 (October Build)**

* Simple scoring (70% \+ Transfer gate)  
* Track components in background (not enforced)  
* 2-attempt Practice routing  
* Exit Check 1/3 intervention  
* SUPPORT/CONFIDENCE problem insertion  
* NO early exit enforcement  
* Collect all data for Phase 2 validation

### **Phase 2**

* **Fluency/Speed Challenge:**  
  * Basic problem serving from mastered content pool  
  * Personal best tracking  
  * Queue integration at daily cadence  
  * Data collection: accuracy, speed, session trends  
* **Test Prep Activity (Foundation):**  
  * State-assessment tagging schema  
  * Initial content pool (STAAR \+ SBAC)  
  * Format exposure at weekly cadence  
  * Diagnostic tracking  
* **Misconception Intervention System:**  
  * Rolling window tracking (20 opportunities)  
  * Threshold triggers (5 errors, TBD with data)  
  * Intervention Activity queue insertion  
  * Post-Intervention threshold adjustment (window to 15\)  
* **MC Per-Distractor Remediation:**  
  * Targeted feedback based on which wrong answer chosen  
  * 3 Medium (per distractor) \+ 1 Heavy (explains correct)  
* May adjust practice problem distribution based on components:  
  * Weak PROCEDURAL → More CREATE problems in practice mix  
  * Weak CONCEPTUAL → More IDENTIFY/COMPARE problems  
  * Weak TRANSFER → More APPLY/CONNECT problems  
  * Note: This would be subtle problem selection, NOT path switching. Path switches still only happen after 2 failed attempts overall  
* Cross-tool transfer logic  
* Assessment prep modules

### **Phase 3**

* **Test Prep (Full Build):**  
  * Strategy instruction curriculum (6+ strategies, sequenced)  
  * Representational bridge content for all units  
  * Non-curriculum toy specifications  
  * State-specific format templates  
  * Adaptive selection (shift purpose mix based on student needs)  
* **Fluency/Speed Challenge (Polish):**  
  * Mixed-operation sessions  
  * Adaptive difficulty based on demonstrated fluency  
  * Cross-unit content mixing  
  * Game design refinement based on engagement data  
* Predictive routing  
* Full cognitive load modeling  
* Personalized pacing  
* Teacher/parent dashboards

---

## **🚦 Summary Principles**

* **Mastery is multi-layered** \- Track at question, skill, learning goal, and standard levels  
* **Exit Checks assess readiness** (\~50%), not mastery (80%)  
* **Practice adapts within single flow** \- No explicit "rounds"  
* **Tool introduction is contextual** \- Major interactions need scaffolding  
* **Rerouting is strategic** \- Based on skill deficits, not just accuracy  
* **Breaks are natural** \- Between phases, with re-engagement protocols  
* **Assessment prep is built-in** \- Modules 10-12 ensure test readiness  
* **Every decision is tracked** \- For continuous improvement and research  
* **Misconceptions need patterns, not guesses** \- Single errors are noisy; Interventions trigger after repeated signals  
* **Brain Breaks acknowledge effort** — Short entertainment between activities; always skippable, never withheld as punishment  
* **Intervention cooldown TBD** — Re-trigger logic needs testing; likely not same day  
* **Fluency is not mastery** — Speed Challenge practices retrieval on already-mastered content. Timed pressure on unlearned material creates anxiety; on mastered material, it builds automaticity.  
* **Test Prep bridges representation, not knowledge** — Students know the math. Test Prep teaches them to recognize it in unfamiliar formats and apply test-taking strategies. State-by-state adaptation makes this relevant everywhere.  
* **Sessions have rhythm** — Start-of-Day Recap and End-of-Day Recap bookend every session, creating predictable structure. Session-relative language only ("last time," never "yesterday").  
* **Personal best, not competition** — Fluency/Speed Challenge tracks growth against self. No leaderboards, no peer comparison. SDT: autonomy and competence through self-referential improvement.  
  


