# Mastery Tracking FDB v2.0

**Status:** Draft — design review
**Version:** 2.0 (replaces v1.1)
**Category:** Student Performance
**Date:** April 2026

---

## What Changed from v1

v1 was written before the Skill Spine existed. It used a single module-level gate (70% on BASELINE + STRETCH) because there was no skill-level tracking infrastructure. v2 integrates the Skill Spine's cross-module knowledge graph to produce **skill-level status reports** instead of binary pass/fail, and replaces the single gate with a **response gradient** (draw ratio adjustment → routing → gate).

| v1 | v2 |
|----|----|
| Module-level 70% pass/fail | Per-skill status report (Strong / Needs Practice / Still Gathering) |
| One gate, one threshold | Three-tier response gradient |
| Skills tracked but not used for decisions | Skills drive display + draw ratio adjustment |
| Component tracking "not enforced" | Component tracking retained as diagnostic layer |
| Routing = binary (pass → advance, fail → retry) | Routing = gradient (draw ratio → lesson repeat/spiral/intervention → path switch) |

**What carries over unchanged:** Content hierarchy, tier classification (which problems count), component taxonomy, cognitive type framework, anti-gaming rules, data across activity types (Tier 1/2/3), minimum attempts by module stage.

---

## User Stories

1. As a **student**, I can see which skills I'm strong on and which need more practice — not just whether I "passed."
2. As a **student**, I experience appropriate challenge because the system adjusts what it serves me based on my skill profile.
3. As a **student**, I can't game the system by failing intentionally or rushing through.
4. As a **content writer**, I know how to classify problems (tier, component, cognitive type, skill, assessment mode) so the system tracks them correctly.
5. As a **developer**, I have clear status computation rules, response triggers, and runtime queries to implement.
6. As a **teacher**, I can see which specific skills a student is struggling with and what the system is doing about it.
7. As a **parent**, I understand my child's progress in plain language tied to specific capabilities.

---

## Content Hierarchy

*Carried over from v1 with one addition: Skill Spine integration.*

| Level | Example | What It Is |
|-------|---------|------------|
| **Grade** | Grade 3 | Top-level grouping, maps to CCSS grade standards |
| **Unit** | Unit 1 – Data & Multiplication | Major topic area. 10-12 modules per unit |
| **Module** | M4 – Bar Graphs & 1:10 Scale | One primary concept. Has one Learning Goal and defined prerequisites from prior modules |
| **Phase** | Warmup → Lesson → Exit Check → Practice → Synthesis | Activity sequence within a module |
| **Skill** | CompareData:difference | The atomic unit of mastery. Defined in the Unit Skill Spine. Each skill belongs to one component and has a cross-module lifecycle (INT → PRC → EXT) |
| **Template** | U1M4-0012 | A reusable problem blueprint. Each template assesses one skill at one tier. |
| **Problem** | (runtime-generated) | What the student actually sees. Generated from a template by selecting specific parameters. |

**How mastery flows:**

- Problem instances are scored individually
- Scores aggregate at the **skill level** within a module — each skill gets a status (Strong / Needs Practice / Still Gathering)
- Skill statuses determine the **practice response** — draw ratio adjustment, routing, or gating
- Skills provide diagnostic granularity — when a student struggles, we identify WHICH skill(s) are weak AND whether the issue is the skill itself or the representation/context
- Module completion is determined by the combination of per-skill statuses + the module-level fallback threshold

**Module stages** affect problem pool size, component weighting, and cognitive type targets:

| Stage | Modules | Pool Target | Character |
|-------|---------|-------------|-----------|
| Foundational | 1-4 | 55-65 problems | Heavy procedural + conceptual |
| Building | 5-8 | 60-75 problems | Balanced, transfer emerging |
| Complex | 9-12 | 65-80 problems | Transfer-heavy |

---

## Problem Classifications

*Carried over from v1.*

Every problem is classified on three dimensions:

| Dimension | Options | Purpose |
|-----------|---------|---------|
| Tier | BASELINE, STRETCH, CHALLENGE, SUPPORT, CONFIDENCE | Determines if it counts toward mastery |
| Component | PROCEDURAL, CONCEPTUAL, TRANSFER | What type of understanding it tests |
| Cognitive Type | CREATE, IDENTIFY, COMPARE, APPLY, CONNECT | How student demonstrates understanding |

**What counts toward mastery:**

- ✅ BASELINE problems (always)
- ✅ STRETCH problems (always)
- ✅ CHALLENGE problems (bonus only — counts if correct, doesn't penalize if wrong)
- ❌ SUPPORT problems (never counts)
- ❌ CONFIDENCE problems (never counts)

### Tiers

| Tier | Purpose | Counts | When Served |
|------|---------|--------|-------------|
| **BASELINE** | Core assessment at standard difficulty | ✓ Yes | Default draw pool |
| **STRETCH** | Extended assessment, slightly harder | ✓ Yes | Default draw pool |
| **CHALLENGE** | Above-grade exploration | Bonus only | Served when student is performing well |
| **SUPPORT** | Confidence builder after struggles | ✗ No | Inserted after 2 wrong in a row |
| **CONFIDENCE** | Emotional support (very easy) | ✗ No | Inserted after SUPPORT fails |

### Components

| Component | What It Measures | Typical Cognitive Types |
|-----------|-----------------|----------------------|
| **PROCEDURAL** | Can execute the skill correctly | CREATE |
| **CONCEPTUAL** | Understands the underlying concept | IDENTIFY, COMPARE |
| **TRANSFER** | Can apply in new situations | APPLY, CONNECT |

### Cognitive Types

| Type | Definition | Example (Unit 1) | Component |
|------|-----------|-------------------|-----------|
| **CREATE** | Construct using visual tools | "Draw a bar graph that matches this data" | PROCEDURAL |
| **IDENTIFY** | Recognize properties or values | "How many students chose cats?" | CONCEPTUAL |
| **COMPARE** | Determine relationships | "How many more chose dogs than cats?" | CONCEPTUAL |
| **APPLY** | Use in contexts or multi-step tasks | "Solve this two-step problem using the graph" | TRANSFER |
| **CONNECT** | Link representations or integrate concepts | "Show that 3×4 and 4×3 give the same answer" | TRANSFER |

### Skills

Skills are defined in the **Unit Skill Spine** — a cross-module knowledge graph generated in Stage 0 of the Practice Template Pipeline.

**Skill ID format:** Global CamelCase (e.g., `CompareData:difference`, `BuildArray`, `LearnFactorProducts`)

**What a skill defines:**
- A specific, assessable student capability
- Which component it belongs to (PROCEDURAL, CONCEPTUAL, or TRANSFER)
- Which cognitive type(s) assess it
- Its **cross-module lifecycle**: INT (introduced) → PRC (practiced) → EXT (extended)
- Its **representations**: which visual contexts it operates on (e.g., "Picture Graphs", "Bar Graphs", "Arrays")
- A **plain language name** for student/parent display (e.g., "I can figure out how many more or how many fewer by comparing two groups on a graph")

**New in v2 — Skill metadata for tracking:**

| Property | Source | Purpose |
|----------|--------|---------|
| `skill_id` | Skill Spine | Global identifier, consistent across modules |
| `spine_status` | Skill Spine (per module) | INT / PRC / EXT — teaching intent in this module |
| `representation` | Template metadata | Which visual context this specific template targets |
| `assessment_mode` | Template metadata | standalone / embedded — how the skill was assessed in this module |
| `student_display` | Skill Spine | Whether this skill appears in the student-facing status display |

**Data the system stores per skill per student per module:**
- Attempts on mastery-eligible tiers (BASELINE + STRETCH count)
- Correct count on mastery-eligible tiers
- Attempts on all tiers (for sample-size threshold)
- Per-attempt sequence: (attempt_number, tier, correct/incorrect, timestamp, misconception_id_if_MC)
- Most recent result
- Linked template IDs

---

## The Skill Status Model

*Replaces v1's "Simple Scoring" section.*

### Three States

The practice phase produces a **per-skill status report**, not a binary pass/fail score. For each skill the student encountered in a module, the report shows one of three states:

| State | Meaning | Visual | Criteria |
|-------|---------|--------|----------|
| **Strong** | Enough evidence, performance above threshold | ✅ | ≥ [ACCURACY_THRESHOLD] correct on BASELINE + STRETCH, with ≥ [MIN_ATTEMPTS] attempts |
| **Needs Practice** | Enough evidence, performance below threshold | 🔄 | < [ACCURACY_THRESHOLD] correct on BASELINE + STRETCH, with ≥ [MIN_ATTEMPTS] attempts |
| **Still Gathering** | Not enough evidence to make a claim | ⏳ | < [MIN_ATTEMPTS] attempts on this skill |

**[DECISION NEEDED] ACCURACY_THRESHOLD:** Starting hypothesis is 70%, matching v1's module-level threshold. This is a tunable parameter. See Hypotheses section for the data question.

**[DECISION NEEDED] MIN_ATTEMPTS:** Starting hypothesis is 4 attempts on mastery-eligible tiers. Modules with fewer problems per skill (single-skill modules, embedded skills) may need different thresholds. See Hypotheses section.

### Why Three States, Not Two

"Still Gathering" exists because making premature claims about a student's competency has real cost. A student who saw 2 problems on a skill and got 1 wrong should not see "Needs Practice" — that's noise, not signal. At this age, skill-level labels are identity-forming. "You need practice on creating graphs" is something a student will internalize. The system should only make that claim when it has enough evidence.

"Still Gathering" is also pedagogically useful — it tells the student "we're still learning what you know" rather than making a premature judgment.

### How Status Is Computed

For each skill active in the current module:

```
attempts = count of BASELINE + STRETCH problems for this skill
correct = count of correct BASELINE + STRETCH problems for this skill
accuracy = correct / attempts

if attempts < MIN_ATTEMPTS:
    status = "Still Gathering"
elif accuracy >= ACCURACY_THRESHOLD:
    status = "Strong"
else:
    status = "Needs Practice"
```

SUPPORT, CONFIDENCE, and CHALLENGE problems are **not included** in the status computation. They're tracked separately for diagnostic purposes.

### The Dimensional Model

Every student attempt is logged with these dimensions:

`(student_id × skill_id × module × spine_status × representation × tier × correct × timestamp × sequence_position × misconception_id)`

This compound key enables the system to distinguish:

- **Skill vs. representation barrier:** A student who's Strong on CompareData:difference in M1 (Picture Graphs) but Needs Practice in M4 (Bar Graphs) has a representation barrier, not a skill gap. The remediation is different.
- **INT vs. PRC trajectory:** A student encountering a skill for the first time (INT) is expected to need more support than one practicing it (PRC). The system can track whether PRC performance meets expectations given INT history.
- **Standalone vs. embedded evidence:** A "Needs Practice" verdict on a skill assessed with 15 standalone templates is stronger evidence than the same verdict on a skill assessed with 3 embedded templates.

### Still Gathering Resolution at Module Completion

What happens when practice ends and a skill is still at "Still Gathering"? This is a real scenario — a student could complete the minimum attempt count for the module without accumulating enough mastery-eligible attempts on every individual skill (especially embedded skills or skills introduced late in the practice set).

**Policy:** Skills at "Still Gathering" when the module completes are **queued for spiral review**. The system does NOT treat them as failures (the student isn't blocked) and does NOT treat them as passes (no "Strong" claim is made). Instead:

1. **Student display:** Shows ⏳ "Still Gathering" — honest about the state of evidence.
2. **Module completion:** "Still Gathering" skills do NOT block module completion. Only INT skills at "Needs Practice" trigger the gate (see Module Completion Criteria). A skill the system hasn't assessed enough is categorically different from a skill the system has assessed and found weak.
3. **Spiral review queue:** The skill is added to the spiral review priority list (Q9) with a `reason: "insufficient_evidence"` tag. It gets moderate priority — above Strong skills (no need to review) but below Needs Practice skills (known weakness).
4. **Parent/teacher view:** Shows ⏳ with a note: "Not enough practice problems to assess this skill yet — queued for review."

**Why not force more attempts?** Extending practice to guarantee MIN_ATTEMPTS on every skill would penalize students who are otherwise ready to advance. The spiral review system exists precisely for this case — it catches what practice missed.

**Key reframe:** A skill can be "PRC of the skill" and "INT of the representation" simultaneously. CompareData:difference in M4 is PRC (the student has compared before) but operates on Bar Graphs for the first time. The dimensional model captures this because the template carries both `skill_id` (same thread) and `representation` (new context).

---

## The Response Gradient

*Replaces v1's "Routing Logic" section.*

When the skill status report shows anything other than "all Strong," the system responds. The response is a **gradient**, not a binary:

### Level 1: Draw Ratio Adjustment (Default)

**Trigger:** One or more skills at "Needs Practice." This is the common case.

**What happens:** The system adjusts the template draw ratio within the current practice session using these starting values:

| Skill Status | Draw Weight Multiplier | Tier Shift |
|-------------|----------------------|------------|
| **Needs Practice** | 2.0× (double the default draw probability) | Next 2 templates for this skill drawn from SUPPORT tier before returning to BASELINE |
| **Strong** | 0.5× (half the default draw probability) | No shift — continue BASELINE/STRETCH |
| **Still Gathering** | 1.0× (default — unchanged) | No shift |

**[HYPOTHESIS — H7]** These multipliers are starting values. The 2.0× weight for Needs Practice may be too aggressive (student gets frustrated seeing the same skill repeatedly) or too mild (not enough additional reps to make a difference). The SUPPORT tier shift (2 problems before returning to BASELINE) is designed to rebuild confidence without permanently lowering the bar. All values are tunable — see H7 in Hypotheses.

**What the student experiences:** More problems on the skill they're struggling with, starting at a slightly easier level. The display shows "Needs Practice" on that skill, so the extra problems feel purposeful, not punitive.

**What doesn't happen:** The student is NOT routed out of practice. They continue working through the practice set with an adjusted mix. Skills at "Strong" are NOT removed from the draw pool — they still appear, just less frequently.

### Level 2: Routing (Exception)

**Trigger:** Draw ratio adjustment is insufficient. Specific triggers:

| Trigger | Response | Rationale |
|---------|----------|-----------|
| Student completes full practice set and still has skills at "Needs Practice" | Retry practice with adjusted draw ratio (heavier weighting toward weak skills) | First failure → more reps, not rerouting |
| Student completes practice twice and still has skills at "Needs Practice" | Route to **targeted intervention** on the specific weak skill(s) | Two full attempts without improvement is a meaningful signal |
| Persistent misconception pattern: same misconception ID flagged across 3+ problems within the session | Route to **misconception intervention** | The student has a specific conceptual error that more practice won't fix |
| **[HYPOTHESIS — H9]** ≥50% of standalone-assessed INT-status skills at "Needs Practice" after first practice attempt | Route to **lesson repeat** | Broad INT weakness suggests the lesson didn't land |

**Lesson-repeat trigger logic:** Count only standalone-assessed skills at INT status. If ≥50% are at "Needs Practice" after the first full practice attempt, route to lesson repeat. PRC/EXT skills at "Needs Practice" do not count toward this trigger — they indicate reinforcement needs, not lesson failure. Embedded skills (assessment_mode = "embedded") do not count — their sample sizes are too small to be reliable signals.

**[HYPOTHESIS — H9]** The 50% INT-skill threshold is a starting hypothesis. A module with 2 INT skills triggers at 1 Needs Practice; a module with 4 INT skills triggers at 2. This may be too aggressive (holding back students who would recover with draw-ratio adjustment) or too permissive (letting students through who genuinely didn't understand the lesson). Calibrate with pilot data by tracking: of students who hit this trigger and were re-routed to lesson repeat, what percentage subsequently passed practice? Of students just below the trigger who continued, what percentage passed?

### Level 3: Gate (Rare)

**Trigger:** Student has completed two full practice attempts AND received targeted intervention, and still doesn't meet module completion criteria.

**What happens:** Path switch consideration. This is the existing v1 escalation path.

**Module completion criteria (v2):**

| Criterion | Specification | Source |
|-----------|--------------|--------|
| Skill status threshold | No INT-status skill at "Needs Practice" (all INT skills must be Strong or Still Gathering) | New in v2 |
| Module accuracy fallback | 70% correct on BASELINE + STRETCH (aggregate) | Carried from v1 |
| Transfer gate | At least 1 APPLY or CONNECT problem correct | Carried from v1 |
| Minimum attempts | M1-4: 4 problems / M5-8: 5 problems / M9-12: 6 problems | Carried from v1 |

**Design intent:** The INT-skill gate is the **primary check** — it catches the highest-stakes failure mode (core concept didn't land). The module accuracy threshold is the **secondary check** — it catches broad weakness that might not concentrate on a single skill. Both must pass. A student who has all INT skills Strong but only 60% aggregate still fails (broad weakness). A student at 80% aggregate but with one INT skill at Needs Practice also fails (specific concept gap). Neither check alone is sufficient.

**The INT-skill check is a hard gate.** If any INT-status skill is at "Needs Practice" after two practice attempts + intervention, the student does not advance. This is the one place where gating earns its keep: INT failure means the core concept didn't land, and PRC encounters in later modules will be confusing rather than reinforcing without it.

**[HYPOTHESIS — H6]** This hard gate may be overly restrictive if the spiral and intervention machinery prove effective at recovering INT weaknesses. H6 tests whether students who would have been blocked by the INT floor actually need the block — or whether they recover through subsequent PRC encounters. If data shows recovery without the gate, soften to a teacher-flagged signal. Until that data exists, default to the safer option: block progression when a newly introduced concept hasn't landed.

### Within-Practice Adaptation

*Carried over from v1.*

| Trigger | Response |
|---------|----------|
| 2 incorrect in a row (any skill) | Insert SUPPORT problem for that skill |
| SUPPORT failed | Insert CONFIDENCE problem for that skill |

These insertions happen in real time during the practice session, independent of the skill status computation. SUPPORT and CONFIDENCE problems don't count toward mastery.

### Exit Check → Practice Routing

*Carried over from v1.*

| Score | Action |
|-------|--------|
| 3/3 | → Proceed to Practice |
| 2/3 | → Proceed to Practice (marginal) |
| 1/3 | → Intervention: Repeat Lesson after break OR Path Switch |
| 0/3 | → Strongly recommend Path Switch |

---

## The Student-Facing Display

### Design Principles

1. **The display IS the routing logic, made visible.** What the student sees (skill statuses) is the same data the system uses to adjust the draw ratio. The display isn't decorative — it's a legible version of what the router is doing.
2. **No premature claims.** "Still Gathering" is shown when the system doesn't have enough evidence. This protects students from internalizing false verdicts about their competence.
3. **Scoped to current module.** Students see only the skills active in the module they just practiced. The full unit view is for parents and teachers.
4. **Plain language.** Skills are described using "I can..." statements from the Skill Spine (e.g., "I can figure out how many more or how many fewer by comparing two groups on a graph").

### Student View (Post-Practice)

After completing a practice session, the student sees a status report for the current module's active skills:

**Example — M4 (6 skills):**

| Skill | Status |
|-------|--------|
| I can read values from a bar graph, even when the bar stops between the lines | ✅ Strong |
| I can draw a bar graph that matches the information I'm given | 🔄 Needs Practice |
| I can show in-between numbers on a graph using half of a bar | ⏳ Still Gathering |
| I can look at a graph and figure out which category has the most or the fewest | ✅ Strong |
| I can figure out how many more or how many fewer by comparing two groups on a graph | ✅ Strong |
| I can add groups together from a graph to find out how many in all | ✅ Strong |

**Example — M9 (single-skill module, 1 spine skill):**

For single-skill modules, the display decomposes the skill along its **variety dimensions** (from the backbone) to avoid a single binary verdict:

| Skill | Status |
|-------|--------|
| I can use my multiplication facts for 2s | ✅ Strong |
| I can use my multiplication facts for 5s | ✅ Strong |
| I can use my multiplication facts for 10s | ⏳ Still Gathering |

These sub-labels are **display-layer decompositions**, not spine skills. They're pulled from the backbone's variety dimensions (factor families, context types, etc.) and exist only in the rendering layer. The spine skill remains `LearnFactorProducts` as a single node.

**Note:** M9 also tracks pattern recognition internally (e.g., does the student use known facts to derive unknown ones, or count from scratch each time?). This is valuable diagnostic data for the teacher view and spiral review priority, but is NOT surfaced in the v1 student display — the cognitive cost of explaining "you know your facts but don't use efficient strategies" to a 3rd grader outweighs the benefit. v2 upgrade path: surface as a teacher-only insight once we have data on how teachers use it.

### Parent/Teacher View

Parents and teachers see the **unit-wide skill profile** — all skills across all completed modules, with cross-module trajectory:

| Skill | M1 | M2 | M3 | M4 | Most Recent |
|-------|----|----|----|----|-------------|
| I can read values from a picture graph | ✅ | ✅ | ✅ | — | Strong (M3) |
| I can draw a picture graph that matches the information I'm given | — | 🔄 | ✅ | — | Strong (M3, improved) |
| I can figure out how many more or how many fewer... | ✅ | ✅ | ✅ | ✅ | Strong (M4) |

**Why "Most Recent" not "Current":** "Current" implies a live, aggregated state — but the system doesn't recompute a global skill status across modules. Each module produces its own status. The "Most Recent" column shows the status from the most recent module where the skill was assessed, with the module ID in parentheses so parents/teachers know how fresh the data is. A skill last assessed in M1 is staler than one assessed in M4.

### Display Visibility Rules

Not all spine skills appear in the student view.

| Skill Type | Student Display | Example |
|------------|----------------|---------|
| Leaf sub-skill (with distinct cognitive operation) | ✅ Yes | CompareData:difference, CompareData:ordinal |
| Parent skill (architectural grouping) | ❌ Hidden | CompareData (parent) — redundant with children |
| Embedded skill (< MIN_ATTEMPTS in this module) | ⏳ Still Gathering or hidden | CompareData:ordinal in M5 (embedded in SelectScale templates) |

The Skill Spine should include a `student_display` property (yes / hidden) to control this.

---

## Schema Additions

### Template Metadata — New Fields

| Field | Type | Values | Purpose |
|-------|------|--------|---------|
| `assessment_mode` | enum | `standalone` / `embedded` | Whether this template is a primary assessment for the skill or embedded within another skill's template. Affects sample-size thresholds for display claims. |

**Why this matters:** CompareData:ordinal in M5 is embedded within SelectScale templates (3-4 items). CompareData:ordinal in M1 is standalone (dedicated templates). A "Needs Practice" verdict based on 3 embedded items is much weaker evidence than the same verdict on 15 standalone items. The display and routing logic need to know the difference.

### Skill Spine — New Properties

| Property | Type | Purpose |
|----------|------|---------|
| `student_display` | checkbox | Whether this skill appears in the student-facing status display. Parent skills (e.g., CompareData) should be hidden. |

### Platform Logging — Required Fields

| Field | Purpose | Notes |
|-------|---------|-------|
| `timestamp` | When the attempt occurred | Required for trajectory analysis (Query 11) |
| `sequence_position` | Nth attempt in this practice session | Required for trajectory analysis and fatigue detection |
| `misconception_id` | Which misconception was triggered (MC problems) | Required for misconception pattern detection (Query 6) |
| `distractor_selected` | Which MC distractor the student chose | Required for per-distractor remediation routing |

---

## Runtime Query Set

These are the questions the routing engine and display layer need to answer in real time. Each query lists its data dependencies and any v2 upgrade path.

### Q1: Skill Status + Draw Ratio (merged)

**Question:** "For student S in module M, what is the status of each active skill, and what draw ratio adjustment (if any) should be applied?"

**Data needed:** Per-attempt log of (skill_id, tier, correct/incorrect) for this session. Minimum-attempts threshold. Accuracy threshold.

**Computation:**
```
For each skill in module M:
  attempts_eligible = count(BASELINE + STRETCH attempts)
  correct_eligible = count(correct BASELINE + STRETCH attempts)
  mode = assessment_mode for this skill in this module
  
  # Determine minimum attempts based on assessment mode
  min_att = EMBEDDED_MIN_ATTEMPTS if mode == "embedded" else STANDALONE_MIN_ATTEMPTS
  
  if attempts_eligible < min_att:
    # Exception: unambiguous embedded evidence (0% or 100% on 3+ attempts)
    if mode == "embedded" and attempts_eligible >= 3:
      if correct_eligible == 0:
        status = "Needs Practice"
      elif correct_eligible == attempts_eligible:
        status = "Strong"
      else:
        status = "Still Gathering"
    else:
      status = "Still Gathering"
    draw_weight = 1.0  # default
  elif correct_eligible / attempts_eligible >= ACCURACY_THRESHOLD:
    status = "Strong"
    draw_weight = 0.5  # reduce draw probability
  else:
    status = "Needs Practice"
    draw_weight = 2.0  # increase draw probability
    tier_shift = "SUPPORT for next 2 templates, then BASELINE"
```

**[HYPOTHESIS — H2a/H2b]** STANDALONE_MIN_ATTEMPTS = 4. EMBEDDED_MIN_ATTEMPTS = 4 (same default), but embedded skills allow early claims on unambiguous evidence (0% or 100% on 3+ attempts). If pilot data shows embedded assessments at 4 attempts are unreliable, raise EMBEDDED_MIN_ATTEMPTS or default all embedded skills to "Still Gathering" regardless of performance.

**Why merged:** The skill status display and the draw ratio adjustment are two views of the same computation. The student sees "Needs Practice" because the same calculation that produces that label also increases the draw weight. This coupling is the transparency property — the display IS the routing logic made visible.

### Q2: Assessment Confidence

**Question:** "For skill X in module M, was assessment standalone or embedded, and how many mastery-eligible attempts has student S had?"

**Data needed:** `assessment_mode` from template metadata. Per-attempt count.

**Why it matters:** A "Needs Practice" verdict on 3 embedded items should default to "Still Gathering" unless the evidence is unambiguous (e.g., 0/3 correct). The display threshold may differ by assessment mode.

### Q3: Cross-Module Skill Thread History

**Question:** "For skill X appearing in module M at status PRC/EXT, what was student S's performance on skill X in prior modules?"

**Data needed:** Historical per-skill accuracy, keyed by (skill_id × module). Spine status per module.

**Output:** Returns a history object per skill thread:
```
{
  skill_id: "CompareData:difference",
  history: [
    { module: "M1", status: "INT", accuracy: 0.85, status_label: "Strong" },
    { module: "M4", status: "PRC", accuracy: 0.50, status_label: "Needs Practice" }
  ],
  diagnosis: "representation_barrier"  // or "underlying_skill_gap" or "consistent"
}
```

**Diagnosis logic:**
- `consistent`: Strong at all prior encounters → no concern
- `representation_barrier`: Strong at INT, Needs Practice at PRC/EXT → the new context is the issue, not the skill. Remediation: bridge the representation (e.g., connect picture graph comparison to bar graph comparison)
- `underlying_skill_gap`: Needs Practice at INT AND PRC/EXT → the skill itself didn't land. Remediation: reteach the skill from foundation

**Consumers:**
- **Teacher view:** Shows the diagnosis alongside the current status, enabling targeted intervention ("this student understands comparison but can't read scaled bar graphs" vs. "this student doesn't understand comparison")
- **Spiral review (Q9):** Skills with `underlying_skill_gap` diagnosis get higher priority than `representation_barrier`
- **v1 scope:** Diagnostic only — displayed to teachers, used for spiral review ranking. Does NOT affect within-session routing or draw ratio. v2 upgrade could use this to influence initial tier selection when a student enters a new module (start PRC skills at support tier if prior INT was weak).

**v2 upgrade:** Once the representation field is tracked per attempt, this query can further distinguish "same representation, harder parameters" from "new representation entirely."

### Q4: Routing Trigger Check

**Question:** "Does student S's current practice session warrant routing (lesson repeat / spiral review / intervention) rather than continued draw-ratio adjustment?"

**Data needed:** Count of skills at Needs Practice (standalone-assessed only). Misconception pattern flags. Total attempts vs. minimum. Practice attempt number (1st or 2nd).

**Computation:**
```
int_skills_standalone = skills where spine_status == INT and assessment_mode == "standalone"
int_needs_practice = count(int_skills_standalone where status == "Needs Practice")
int_total = count(int_skills_standalone)

misconception_flag = any misconception_id appears in 3+ attempts this session
attempt_number = which full practice attempt this is (1st or 2nd)

if attempt_number == 1 and int_needs_practice / int_total >= 0.50:
    route = "lesson_repeat"                     -- H9: broad INT weakness
elif misconception_flag:
    route = "misconception_intervention"         -- persistent conceptual error
elif attempt_number == 2 and any skill at "Needs Practice":
    route = "targeted_intervention"              -- two attempts without recovery
else:
    route = "continue_draw_ratio_adjustment"     -- default
```

All thresholds in this computation are hypotheses — see H8 (misconception threshold) and H9 (lesson-repeat trigger) in the Hypotheses section.

### Q5: Misconception Pattern Detection

**Question:** "Has student S triggered the same misconception ID across 3+ problems in this practice session?"

**Data needed:** Per-attempt misconception tagging (from distractor selection in MC problems). Session-scoped rolling window.

**Window:** Current practice session only (v1). Cross-session detection is a v2 upgrade.

**[HYPOTHESIS]** The threshold of 3 problems is a starting hypothesis. It may need to be 2 (more aggressive detection) or 4 (fewer false positives). Calibrate with pilot data.

**Why 3, not 2:** Two problems sharing a misconception could be coincidence (same distractor happens to test the same error). Three is a pattern. But this depends on how many distractors test the same misconception — if there's only one distractor per misconception per template, then 2 is already meaningful. Template-level metadata should inform the threshold.

### Q6: Transfer Gate Check

**Question:** "Has student S answered at least 1 APPLY or CONNECT problem correctly in this practice session?"

**Data needed:** Per-attempt log with `mastery_verb` field.

**Carried from v1.** No changes.

### Q7: Module Completion Check

**Question:** "Has student S met module completion criteria?"

**Data needed:** Aggregate accuracy on BASELINE + STRETCH. Transfer gate status. Per-skill status for INT skills. Total attempt count.

**Computation:**
```
module_complete = (
  no INT-status skill at "Needs Practice"        -- primary check
  AND aggregate_accuracy >= 0.70                  -- secondary check
  AND transfer_gate_passed
  AND total_attempts >= MIN_ATTEMPTS_FOR_MODULE_STAGE
)
```

### Q8: Parent/Teacher Unit-Wide View

**Question:** "For student S, what is the per-skill status across all modules completed so far in this unit?"

**Data needed:** Historical per-skill status, all modules. Cross-module trajectory (improving, stable, regressing).

### Q9: Spiral Review Priority

**Question:** "Which skills should be prioritized in student S's next spiral review session?"

**Data needed:** Skills where status was Needs Practice at module completion. Skills where PRC/EXT performance dropped relative to INT performance. Time since last encounter.

**v1 ranking:** Recency + accuracy delta (skills with biggest drop, most recently encountered, get priority).

**v2 upgrade:** Once a downstream dependency graph exists, skills that are load-bearing for upcoming modules should be prioritized above those with no downstream encounter. This is a known upgrade path — not blocking for v1.

### Q10: Within-Session Trajectory

**Question:** "What is student S's performance trajectory on skill X across recent attempts in this session?"

**Data needed:** Per-attempt sequence: (sequence_position, correct/incorrect) for this skill in this session.

**Why it matters:** A student who started 0/3 and is now 4/5 is learning. A student who started 4/4 and is now 0/3 is fatiguing or losing focus. Both might have the same rolling accuracy, but the system response should differ:
- **Learning trajectory:** Continue current draw ratio. The student is improving.
- **Declining trajectory:** Consider Brain Break before continuing. Draw ratio adjustment won't help if the issue is fatigue, not skill.

**v1 scope:** Track and display to teacher. Don't automate response yet — fatigue detection needs calibration.

---

## Anti-Gaming Rules

*Carried over from v1.*

| Rule | Rationale |
|------|-----------|
| No early exit | Must complete full problem set — can't fail fast to escape |
| SUPPORT doesn't count | Getting easier problems doesn't inflate mastery score |
| Path switch requires 2 full practice attempts + intervention | Can't immediately escape to perceived "easier" path |

---

## Data Across Activity Types

*Carried over from v1 with minor framing updates.*

### Tier 1: Gates Progression

| Activity | What It Gates | Data Used |
|----------|--------------|-----------|
| **Exit Check** | Entry to Practice | 3-question score → routing (3/3, 2/3 proceed; 1/3, 0/3 reroute) |
| **Practice** (skill status report) | Module completion → Synthesis | Per-skill status (Strong/Needs Practice/Still Gathering) + module-level 70% fallback + transfer gate |

### Tier 2: Informs Routing (Diagnostic)

| Activity | What It Tells Us | How It Feeds Back |
|----------|-----------------|-------------------|
| **Spiral Review** (Main) | Is mastery durable? | Low accuracy → queue additional review. Response time increasing → mastery may be fragile. **v2:** Spiral review priority informed by per-skill status history (Query 9). |
| **Spiral Review** (Transfer) | Can they recognize the concept in other visual tools? | Low transfer accuracy → more cross-path exposure. |
| **Intervention** (Confirm phase) | Did intervention resolve the misconception? | Low Confirm accuracy → re-trigger. High accuracy → misconception counter resets. |
| **Synthesis** | Can they generalize and reflect? | If student needs more than Light remediation, flag that Practice mastery may be superficial. |

**Key principle:** None of this data changes a student's mastery score. But all of it should influence *what the queue serves next*.

### Tier 3: Tracks Fluency (Separate Dimension)

*Carried over from v1. No changes.*

Fluency/Speed Challenge measures retrieval speed — a different dimension than the accuracy-based mastery system. No fixed threshold; personal best trajectory. Gates nothing.

---

## Hypotheses and Data Questions

Every policy choice in this document is a hypothesis. The system is instrumented to collect the data needed to validate or revise each one. This section makes the hypothesis stack explicit.

### H1: Accuracy Threshold

**Current setting:** 70% on BASELINE + STRETCH (carried from v1).

**Data question:** Is 70% the right boundary between "Strong" and "Needs Practice"? Does it differ by module stage (Foundational vs. Complex)? By spine status (INT vs. PRC vs. EXT)?

**What would change it:** If students classified as "Strong" at 70% consistently struggle on the same skill in later modules (PRC/EXT encounters), the threshold is too low. If students classified as "Needs Practice" at 65% consistently succeed later, the threshold is too high.

**How to test:** Track per-skill status at module N, then track performance on the same skill thread at module N+k. Compute correlation between "Strong at 70%" and "Strong at PRC/EXT."

### H2: Minimum Attempts Threshold

**Current setting:** 4 attempts on mastery-eligible tiers before the system makes a status claim (H2a: standalone, H2b: embedded — see Q1 pseudocode for embedded exception logic).

**Data question:** Is 4 enough to distinguish signal from noise? Does it need to differ for standalone vs. embedded assessment?

**What would change it:** If "Needs Practice" verdicts at 4 attempts are frequently reversed within the same session (student was just warming up), the threshold is too low. If students with 3 attempts are reliably classifiable, 4 is too high.

**How to test:** At what attempt count does the status classification best predict downstream performance on the same skill thread? For each possible threshold (3, 4, 5, 6), compute: when the system says "Strong" at N attempts, how often is the student Strong on the same skill in the next module? When it says "Needs Practice" at N attempts, how often does the student still struggle later? The threshold that maximizes predictive correlation is the right one. Note: simple status-stability testing (does the label change after attempt N?) only tells you when the computation converges, not whether it converges to the right answer.

### H3: Is Skill-Level Tracking Predictive?

**Data question:** Does per-skill status predict future performance better than module-level aggregate?

**How to test:** For students who pass at the module level (70% aggregate), compare: do students with all skills Strong outperform students with some skills at Needs Practice in subsequent modules? If yes, skill-level tracking adds predictive value beyond the aggregate.

### H4: Is Cognitive Verb Predictive?

**Data question:** Does performance by verb type (CREATE, IDENTIFY, COMPARE, APPLY, CONNECT) predict anything that component (PROCEDURAL, CONCEPTUAL, TRANSFER) doesn't?

**How to test:** For students with the same component profile, does verb-level performance distinguish outcomes? Example: two students both at 70% CONCEPTUAL, but one is strong on IDENTIFY and weak on COMPARE, the other vice versa. Do they have different outcomes in later modules?

### H5: Does the Spiral Actually Work?

**Data question:** Do PRC skill scores improve over time through exposure alone, or does improvement require explicit intervention?

**How to test:** Track PRC skill performance across modules for students who were Needs Practice on the INT encounter. Do they improve at PRC without intervention (spiral effect), or only with intervention? If exposure alone drives improvement, the soft-gating approach for PRC is validated. If not, PRC may need harder gating.

**Confound to control for:** If PRC performance improves over time, that could be spiral exposure, developmental maturation, or classroom instruction (the teacher is covering the same content). The cleanest test compares students who had Needs Practice at INT and encountered the skill again at PRC vs. students who had Needs Practice at INT and did NOT encounter it again (if such students exist — some skills have no PRC follow-up). That cohort comparison isolates the spiral effect from general maturation. Constructing this cohort may require cross-unit data.

### H6: INT-Skill Floor

**Data question:** Should there be a minimum accuracy requirement on INT-status skills specifically?

**What would change it:** If students who are Needs Practice on INT skills but pass at the module level consistently fail at PRC encounters, an INT floor is needed. If they recover through the spiral, it's not.

**How to test:** Track module-level passers who had INT skills at Needs Practice. Compare their PRC/EXT performance to students who had all INT skills Strong. If the groups diverge significantly, add an INT floor.

### H7: Draw Ratio Adjustment Effectiveness

**Data question:** Does adjusting the template draw ratio actually improve skill status within a session, or does it just give students more opportunities to fail?

**How to test:** Compare sessions where draw ratio adjustment was applied vs. sessions where it wasn't (natural experiment from skill mix). Track whether students who received more templates on a weak skill improved by end of session.

**Methodology caveat:** This comparison has a built-in selection effect — students who trigger draw ratio adjustment are weaker on that skill by definition, so comparing them to students who didn't trigger it conflates the treatment effect with the baseline difference. The cleanest test is **A/B testing** (randomly withhold draw ratio adjustment for a subset) or **matched-pair analysis** (compare students with similar accuracy at the triggering moment, where one happened to trigger the adjustment due to sequencing and one didn't). Observational data alone will overstate the effectiveness of the adjustment if improving students are credited to the treatment when they would have improved anyway.

### H8: Misconception Detection Threshold

**Data question:** Is 3 problems the right threshold for flagging a persistent misconception?

**How to test:** At threshold=3, what percentage of flagged misconceptions persist beyond the practice session (true positives) vs. self-correct (false positives)? Optimize the threshold for a target false-positive rate.

### H9: Lesson-Repeat Trigger Threshold

**Current setting:** Route to lesson repeat when ≥50% of standalone-assessed INT-status skills are at "Needs Practice" after the first full practice attempt.

**Data question:** Is 50% the right threshold? Does the trigger correctly identify students who need the lesson repeated vs. students who would recover through draw ratio adjustment alone?

**What would change it:** If students who trigger the lesson repeat at 50% frequently would have recovered with just another practice attempt (draw ratio adjustment was sufficient), the threshold is too aggressive — raise it. If students just below 50% frequently fail the second practice attempt too, the threshold is too permissive — lower it.

**How to test:** Track three cohorts: (1) students who triggered lesson repeat (≥50% INT skills at NP), (2) students just below the threshold (e.g., 1 of 3 INT skills at NP = 33%) who continued to practice attempt 2, and (3) students well below (0 INT skills at NP). For cohort 1: after lesson repeat + second practice attempt, what percentage reach module completion? For cohort 2: without lesson repeat, what percentage reach module completion on attempt 2? If cohort 2's success rate is comparable to cohort 1's post-repeat rate, the repeat isn't adding value at that threshold — students recover on their own.

**Edge case:** Modules with only 1-2 INT skills make the threshold binary (1 of 2 = 50%, triggers immediately). This may be appropriate (a single INT failure in a 2-skill module IS serious) or too aggressive (one bad skill out of two could be noise). Monitor per-module trigger rates in pilot.

### Deferred Design Questions

These require data or infrastructure that doesn't exist yet. They're documented here so the architecture supports them when the time comes.

| Question | Requires | Priority |
|----------|----------|----------|
| Should gating floors be computed from downstream skill dependency weight? | Downstream dependency graph in the Skill Spine | Medium — accumulating reasons to build this |
| Should spiral review priority account for downstream load-bearing skills? | Same dependency graph | Medium |
| Should cross-session misconception persistence trigger different routing than within-session? | Cross-session misconception logging with recency weighting | Low for v1 |
| Should the spine audit for atomic sub-skills (LearnFactorProducts → :recall + :patterns) be done? | Walkthrough validation (M2 + M9) to test whether the display model needs it | Medium — do after walkthroughs |
| Should trajectory data (Q10) automatically trigger Brain Breaks? | Pilot data on fatigue patterns | Low for v1 |
| Does the "suspected transfer relationship" edge type belong in the knowledge graph? (e.g., SolveMultiStepData → SolveMultEquation) | Graph schema design decision | Low — schema insurance, not urgent |

---

## Rollout Plan

**v1 → v2 transition:** v1 (module-level 70% gate) is the current shipping design. v2 (skill-level status report + response gradient) is a design proposal that requires validation and engineering work before it can replace v1.

**Recommended sequence:**

1. **Now (Apr 2026):** Finalize this FDB v2 document through design review. Run the M2 + M9 walkthroughs to validate the display model, query set, and routing policy.
2. **Pre-pilot (May–Jul 2026):** Engineering implements the logging schema additions (assessment_mode, per-attempt sequence, misconception_id). These are non-breaking additions to v1 — they instrument the system to collect the data v2 needs without changing any routing behavior. Template metadata gets the `assessment_mode` field. Skill Spine gets the `student_display` property.
3. **Pilot launch (Aug–Sep 2026):** Launch with v1 routing logic but v2 logging. The system computes v2 skill statuses and logs them as shadow data — it records what v2 *would have done* without actually changing student routing. This lets us validate every hypothesis (H1–H9) against real student data before committing to v2 behavior.
4. **Shadow analysis (Sep–Oct 2026):** Analyze shadow data. Where would v2 have made different routing decisions than v1? Were those decisions better (student who v2 would have flagged for draw ratio adjustment actually struggled later) or worse (student who v2 would have routed to lesson repeat actually recovered fine)?
5. **v2 activation (TBD):** Switch live routing from v1 to v2 once shadow data validates the hypothesis stack. This could be a full cutover or a gradual rollout (v2 for new cohorts, v1 for in-progress students).

**Key constraint:** v1 and v2 should NOT run in parallel for the same student — a student shouldn't see module-level pass/fail AND skill-level status reports simultaneously. The shadow period (step 3) gives us v2 data without v2 UX.

---

## References

**Internal:**
- [Mastery Tracking FDB v1.1](https://www.notion.so/2b75917eac5280e587d1efbce0b04281) — predecessor document
- [Unit 1 Skill Spine](Notion Skill Spine database) — cross-module knowledge graph
- [Practice Pipeline Architecture v2](practice_pipeline_architecture_v2.md) — template generation pipeline
- [Unit 1 Cross-Module Summary](U1_Practice_Templates_Cross_Module_Summary.md) — module-by-module skill coverage matrix
- [Universal Mastery Tracking Framework v3](https://www.notion.so/32e5917eac52818fb7d5dc3fc1b0098c)
- [Edtech Activity Queue](https://www.notion.so/32e5917eac5281618750c44221623a73)

**Research Alignment:** Cognitive Load Theory, Self-Determination Theory (competence need — display supports self-knowledge), UDL, Formative Assessment Best Practices

---

## Validation Plan

Before this design ships, validate with two walkthroughs:

1. **M2 walkthrough** (multi-skill module, 6 skills, mix of INT/PRC). Simulate a student who is Strong on 4 skills, Needs Practice on 1, Still Gathering on 1. Walk through: what the display shows, what draw ratio adjustment does, whether the routing triggers fire correctly.

2. **M9 walkthrough** (single-skill module, LearnFactorProducts only). Simulate a student who is Strong on ×2 and ×5 but Still Gathering on ×10. Walk through: how the display decomposes the single skill, whether "Still Gathering" on one variety dimension produces sensible behavior.

Both walkthroughs should validate the runtime queries — can each query be answered from the data the templates produce?
