# STARTER PACK STRUCTURAL SKELETON
**Version:** 03.25.26
**Purpose:** Single canonical reference for the exact heading hierarchy, section ordering, and formatting patterns that every Module Starter Pack MUST follow.
**Authority:** Cowork Guidance v3 (03.12.26) + M4 Notion page + M5 Notion-Ready local file

---

## CONFLICTS RESOLVED

This skeleton establishes definitive answers to four structural conflicts across competing docs:

| Conflict | Competing Docs | Resolution | Rationale |
|----------|----------------|-----------|-----------|
| **Required/Forbidden Phrases placement** | Template v2 says "after interactions"; Cowork Guidance v3 says "before interactions" | ✅ **BEFORE interactions** (H3, after Purpose Frame) | Cowork Guidance line 694 + M4 Notion visual hierarchy confirm phrases must anchor lesson pedagogy before student engagement |
| **Module-Specific Lesson Guidance wrapper** | Template v2 includes; Evaluation Prompt v3 omits | ❌ **NO wrapper header** — each subsection (Required, Forbidden, Misconception, ISF, Success, Verification) stands as independent H3 | M4 Notion page and M5 local file show no wrapper; subsections are self-contained and parallel |
| **Learning Goals §1.1 subtitle formatting** | Template v2 uses H3 "Learning Context"; Cowork v3 shows italic line | ✅ **Italic subtitle** (`*Verbatim from OUR Curriculum*`) as body text, NOT an H3 | Cowork Guidance visual shows italic treatment; inline fields (**L1:**, **L2:**, etc.) follow standard pattern |
| **KDD numbering and header level** | Template v2 uses numbered list; M4 Notion uses H3 | ✅ **H3 format** (`### KDD-N: Title`) — not numbered list | M4 Notion + M5 consistency: KDDs are structural sections, not list items |

---

## HEADING HIERARCHY RULES

- **Exactly 3 H1s:** Module title, BACKBONE, END OF MODULE
- **All numbered sections (1.0–1.10) are H2**
- **Everything inside sections is H3** (including interactions, toys, KDD items, subsection headers)
- **No H4s anywhere** — use bold inline labels instead
- **Horizontal rules (`---`)** separate major blocks and section transitions

---

## COMPLETE STRUCTURAL SKELETON

```markdown
# MODULE [X]: [Title]

<!--
HUB PROPERTIES BLOCK (optional Notion metadata comment)
Contains version info, timestamps, relationship tags if needed
Format: HTML comment block, does not appear in rendered output
-->

# BACKBONE

---

## 1.0 THE ONE THING

<!--
This is a dense, single paragraph synthesizing the core learning challenge.
Uses bold inline labels to mark key concepts.
No sub-headers; paragraph only.
-->

**CRA Stage:** [Concrete/Representational/Abstract stage this module targets]
**Critical Misconception:** [The deepest misconception students bring to this module]
**Success Indicator:** [How you know students truly understand]
**Biggest Risk:** [What derails implementation if not managed]
[Additional inline labels and explanations as needed]

---

## 1.1 LEARNING GOALS

*Verbatim from OUR Curriculum — Script Must Achieve These*

**L1:** "[Full learning goal text from curriculum]"
**L2:** "[Additional goal if applicable]"
**Module Goal (Student-Facing):** "[Goal written in language students will hear]"

**Exit Check Tests:**
* [First exit check test/problem type]
* [Second exit check test/problem type]

**Question/Test Language Stems (from Module Mapping):**
* "[Sample question stem]" → Maps to [Phase/Section reference]
* "[Another stem]" → Maps to [Phase/Section reference]

### 1.1.1 Standards Cascade

<!-- List progression of standards this module addresses -->

### 1.1.2 Module Bridges

<!-- How this module connects to prior/subsequent modules -->

### 1.1.3 OUR Lesson Sources

<!-- References to curriculum documents, lesson banks, etc. -->

---

## 1.2 SCOPE BOUNDARIES

### ✅ Must Teach

<!-- List what MUST be covered in this module -->

### ❌ Must Not Include

<!-- List what explicitly falls outside scope; save for later modules -->

### Scope Confirmation Checklist

<!-- Checklist of boundary decisions to verify before finalizing -->

---

## 1.3 VOCABULARY ARCHITECTURE

<!--
Opens with a paragraph defining the vocabulary strategy for this module.
Describes phasing, assessment terminology, and spiraling approach.
Then subsections follow.
-->

### Vocabulary Staging by Phase

<!--
Table or structured list showing:
- Concrete Phase: [terms]
- Representational Phase: [terms]
- Abstract Phase: [terms]
-->

### [Vocabulary Notes if applicable]

<!-- Optional subsection for nuanced guidance on tricky terms -->

### Terms to Avoid (Save for Later Modules)

<!-- Language/terms students should NOT encounter yet -->

---

## 1.4 MISCONCEPTIONS

### 1.4.1 #[ID]: [Misconception Name] (PRIMARY)

<!--
Concise description of the misconception.
How it manifests in student work/speech.
Why it's a barrier to the learning goal.
Brief intervention strategy.
-->

### 1.4.2 #[ID]: [Misconception Name] (SECONDARY)

<!-- Same format as 1.4.1 -->

### 1.4.3 #[ID]: [Additional misconceptions as needed]

---

## 1.5 TOY SPECIFICATIONS

### 1.5.1 [Primary Toy Name/ID]

<!--
Physical/visual specs of this toy.
Why it's the primary scaffold.
Key interaction affordances.
What conceptual load it carries.
-->

### 1.5.2 [Secondary Toy Name/ID]

<!-- Same format -->

### [Additional toy subsections as needed]

---

### Interaction Constraints (All Toys)

<!--
Cross-cutting constraints that apply to every toy interaction in this module.
Examples: timing windows, material limitations, transition rules.
-->

---

## 1.6 WARMUP (3–5 minutes)

### Core Purpose

<!--
Why this warmup exists.
What conceptual or procedural ground it prepares.
How it connects to the lesson's core learning goal.
-->

---

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 3–5 minutes |
| Toy(s) Used | [Toy name(s)] |
| [Additional rows as needed] | |

### Constraints

| Constraint | Details |
|-----------|---------|
| [Constraint name] | [Description] |
| [Another constraint] | [Description] |

### Warmup Type Rationale

<!-- Why this warmup type (e.g., activation, exposure, review) serves the lesson -->

---

### Interaction W.1: [Title] [TYPE LABEL]

<!--
TYPE LABEL examples: [EXPOSURE], [ACTIVATION], [REVIEW], [EMBODIED]
Includes all fields from Interaction Block (see Annotated Format Examples below)
-->

---

### Interaction W.2: [Title] [TYPE LABEL]

---

### Interaction W.X: Bridge to Lesson [BRIDGE]

<!--
Final warmup interaction that explicitly connects warmup to lesson opening.
Signals shift from warmup to lesson.
-->

---

### Verification Checklist (Warmup)

- [x] **W-Setup:** [Item description]
- [ ] **W-Flow:** [Item description]
- [ ] **W-Timing:** [Item description]
- [ ] **W-Bridge:** [Item description]

---

## 1.7 LESSON ([TIME RANGE])

### Core Purpose + Pedagogical Flow

<!--
Why this lesson structure works.
How the three CRA stages unfold.
How Required/Forbidden Phrases anchor the teaching.
What students should think/do/say by end.
-->

---

### Lesson Structure

| Phase | Duration | CRA Stage | Focus |
|-------|----------|-----------|-------|
| Section 1: [Title] | [Time] | Concrete | [What happens] |
| Section 2: [Title] | [Time] | Representational | [What happens] |
| Section 3: [Title] | [Time] | Abstract | [What happens] |
| Exit Check | 3–5 min | Application | [What happens] |

---

### Required Phrases

<!--
Phrases students MUST be able to say/understand by end of lesson.
Format: bullet with phrase in quotes, then explanation.
Example:
* "three groups of four" — enables flexible grouping language
* "skip-count by fours" — connects to repeated addition
-->

* "[phrase]" — [explanation and why it matters for learning goal]
* "[phrase]" — [explanation]

---

### Forbidden Phrases

<!--
Language to AVOID during lesson that would reinforce misconceptions or confuse conceptual development.
Format: line-starter emoji (❌), bold phrase in quotes, explanation.
Example:
❌ **"carry the one"** — reinforces algorithm-as-magic rather than place value understanding
❌ **"the answer is on top"** — obscures fractional reasoning
-->

❌ **"[phrase]"** — [explanation and why it blocks learning]
❌ **"[phrase]"** — [explanation]

---

### Purpose Frame

<!--
Teacher opens lesson with this frame.
No student action during frame — teacher sets context, goal, relevance.
Concrete language. Why today matters.
-->

---

### Section 1: [Title] — [Stage] ([CRA Label])

<!--
Introduction to this section.
What students do with the toy/material.
What observation or discovery they make.
-->

---

### Interaction L.1: [Title] [TYPE LABEL]

<!--
Full Interaction Block (see Annotated Format Examples).
Includes all fields: Setup, Student Action, Teacher Move, Key Observation, Common Detour, Intervention, Next Move, Duration.
-->

---

### Interaction L.2: [Title] [TYPE LABEL]

---

[... more interactions as needed ...]

---

→ **SECTION 1 COMPLETE. PROCEED TO SECTION 2.**

---

### Section 2: [Title] — [Stage] ([CRA Label])

<!--
Introduction to this section.
What shifts from Section 1 (less concrete, more abstract).
How students use the toy differently or think differently.
-->

---

### Interaction L.X: [Title] [TYPE LABEL]

---

[... more interactions ...]

---

→ **SECTION 2 COMPLETE. PROCEED TO SECTION 3.**

---

### Section 3: [Title] — [Stage] ([CRA Label])

<!--
Introduction to this section.
Most abstract phase of lesson.
Students apply learning independently or with minimal scaffolding.
-->

---

### Interaction L.X: [Title] [TYPE LABEL]

---

[... more interactions ...]

---

→ **SECTION 3 COMPLETE. PROCEED TO EXIT CHECK.**

---

### Misconception Prevention

<!--
Specific callouts showing where each primary/secondary misconception is addressed.
Links each misconception from §1.4 to the interaction that prevents/corrects it.
Example:
**#M1 (Students think groups are permanent):** Addressed in L.5 when students regroup same objects.
-->

---

### Incomplete Script Flags (§1.7.4)

<!--
Red flags: if teacher skips these, students will not meet the learning goal.
List specific interactions or moves that cannot be omitted.
Example:
🚩 If teacher skips L.3, students will not understand why grouping structure matters.
-->

---

### Success Criteria (§1.7.5)

<!--
Observable behaviors/statements that show students are ready for exit check.
Tied to L1/L2 learning goals from §1.1.
Example:
✅ Student can skip-count aloud without counting ones.
✅ Student spontaneously says "three groups of four" rather than just counting.
-->

---

### Verification Checklist (Lesson)

- [x] **L-Purpose:** [Item]
- [ ] **L-CRA:** [Item]
- [ ] **L-Phrases:** [Item]
- [ ] **L-Misconceptions:** [Item]
- [ ] **L-Closure:** [Item]

---

### [Module-Specific Subsections if Needed]

<!--
Examples: Dimension Tracking, Symbolic Progression, Pacing Notes, etc.
Format: H3, relevant to lesson implementation.
-->

---

## 1.8 EXIT CHECK (3–5 minutes)

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 3–5 minutes |
| Problem Count | [#] problems |
| Toy(s) Used | [Toy name(s)] or None |
| [Additional rows] | |

### Constraints

| Constraint | Details |
|-----------|---------|
| [Constraint name] | [Description] |

### Alignment Check

<!--
Table showing which exit check problem(s) map to which learning goals (L1, L2, Module Goal).
Ensures every goal is assessed.
-->

| Exit Check Problem | L1 | L2 | Module Goal | Notes |
|-------------------|----|----|-------------|-------|
| EC.1 | ✓ | | ✓ | [Details] |
| EC.2 | | ✓ | ✓ | [Details] |

---

### EC Rectangle Selection [if applicable]

<!--
If exit check involves selecting/arranging rectangles or other visual items.
Specify the pool of available options and constraints on selection.
-->

---

### Transition Frame

<!--
Teacher language that moves students from lesson to exit check.
Sets expectations for independence.
Brief, clear.
-->

---

### EC.1: [Title] [COGNITIVE TYPE]

<!--
COGNITIVE TYPE examples: [FLUENCY], [REASONING], [APPLICATION], [REPRESENTATION]
Full problem statement and expected solution(s).
What indicates student readiness to proceed to next module.
-->

---

### EC.2: [Title] [COGNITIVE TYPE]

---

### EC.3: [Title] [COGNITIVE TYPE]

---

### EC Verification Checklist

- [ ] **EC-Alignment:** Exit check assesses all learning goals
- [ ] **EC-Independence:** Student solves without toy support
- [ ] **EC-Language:** Student uses required phrases from §1.7
- [ ] **EC-Readiness:** Passing grade indicates readiness for next module

---

## 1.8.5 PRACTICE INPUTS

### Practice Phase Overview

<!--
Purpose of practice beyond the lesson/exit check.
How practice deepens automaticity, flexibility, or confidence.
Duration and frequency guidance.
-->

---

### Distribution Targets

| Problem Type | Count | Rationale |
|--------------|-------|-----------|
| [Type] | [#] | [Why this many] |

---

### Toy Constraints

| Constraint | Details |
|-----------|---------|
| [Constraint name] | [Description] |

---

### Dimension Constraints

<!--
If exit check/practice involves varying dimensions (e.g., array sizes, number ranges).
Specify which dimensions are available, which are restricted, progression logic.
-->

### Available Rectangle Pool (for Pipeline)

<!--
If applicable: list of all possible problem instances/configurations available for generation.
Helps script understand the full design space.
-->

---

### Dimensions Used Tracking (EC + Practice)

<!--
Record keeping: which dimensions/sizes were used in exit check.
Ensures practice problems vary appropriately without exact repetition.
-->

---

### [Module-Specific Subsections if Needed]

<!-- Examples: Differentiation Paths, Extended Practice, Acceleration Options -->

---

## 1.9 SYNTHESIS (6–8 minutes)

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 6–8 minutes |
| Toy(s) Used | [Toy name(s)] or None |
| Student Grouping | [Whole group, small group, partner, individual] |
| [Additional rows] | |

### Constraints

| Constraint | Details |
|-----------|---------|
| [Constraint name] | [Description] |

---

### Opening Frame [No Student Action]

<!--
Teacher plants the seed for synthesis.
No student action yet.
References the learning goal and what students just mastered.
Sets up connection task.
-->

---

### Connection Task S.1: [Title] [Task Type]

<!--
TASK TYPE examples: [COMPARISON], [CONTEXT], [GENERALIZATION], [ERROR ANALYSIS]
Prompts students to connect module learning to real world, prior knowledge, or next module.
Specific language for prompt.
Expected student responses/artifacts.
-->

---

### Connection Task S.2: [Title] [Task Type]

---

### Metacognitive Reflection S.X: [Title]

<!--
Prompts for student reflection on their own learning process.
Examples: "What was hard? How did you solve it? What would you tell a friend?"
Open-ended, not graded.
-->

---

### Identity-Building Closure S.X + M[X+1] Bridge [No Student Action]

<!--
Teacher closes synthesis with identity affirmation.
Links this module to next module's goal.
No student action; teacher speaks.
Example: "You are now mathematicians who can group and skip-count. Next, you'll use that power to..."
-->

---

### Synthesis Verification Checklist

- [ ] **S-Connection:** Student task connects module to real world or next learning
- [ ] **S-Reflection:** Student articulates their own thinking process
- [ ] **S-Identity:** Teacher explicitly affirms student identity as mathematician/thinker
- [ ] **S-Bridge:** Teacher previews next module goal

---

### Incomplete Script Flags (Synthesis)

<!--
If these elements are omitted, synthesis loses its power.
Example: 🚩 If teacher skips metacognitive reflection, students miss opportunity to build self-awareness.
-->

---

## 1.10 KEY DESIGN DECISIONS (KDD)

### Purpose

<!--
Why KDD section exists: to document non-obvious choices that hold the module together.
These are design trade-offs, pedagogical moves, or constraint decisions that deserve explanation.
A reader unfamiliar with the module should understand the "why" behind structural choices.
-->

---

### KDD-1: [Title of Decision]

<!--
What choice was made and why.
What alternative was considered and rejected.
How this decision supports the learning goal and misconception prevention.
1-3 sentences typically sufficient.
-->

---

### KDD-2: [Title of Decision]

---

### KDD-3: [Title of Decision]

---

[... more KDDs as needed, numbered sequentially ...]

---

# END OF MODULE [X] STARTER PACK

---
```

---

## ANNOTATED FORMAT EXAMPLES

These examples show the exact formatting and field structure for patterns used throughout the skeleton.

### EXAMPLE 1: §1.1 Learning Goals Format

```markdown
## 1.1 LEARNING GOALS

*Verbatim from OUR Curriculum — Script Must Achieve These*

**L1:** "Students will understand that multiplication can be represented as equal groups."
**L2:** "Students will fluently skip-count by a given factor to find the total in a multi-group array."
**Module Goal (Student-Facing):** "You will become expert group-counters who can figure out how many objects are in a collection of equal groups."

**Exit Check Tests:**
* Given a quantity of objects arranged in equal groups, student determines the total using skip-counting or groups-and-singles
* Given a written multiplication problem (5 × 3), student represents it with a physical or drawn array and states the total

**Question/Test Language Stems (from Module Mapping):**
* "How many [objects] are there if you have [#] groups of [#]?" → Maps to CRA Concrete Phase
* "Show me 4 groups of 5. How did you figure out the total?" → Maps to CRA Representational Phase
* "Write a multiplication problem for [image of array]. Explain your thinking." → Maps to CRA Abstract Phase

### 1.1.1 Standards Cascade

CCSS.MATH.3.OA.A.1 — Interpret products of whole numbers
CCSS.MATH.3.OA.B.5 — Fluently multiply within 100

### 1.1.2 Module Bridges

**Prior Module:** Module 4 (Understanding Equal Groups)
**Next Module:** Module 6 (Division as Inverse of Multiplication)

### 1.1.3 OUR Lesson Sources

- OUR Curriculum Scope & Sequence, Grade 3, Unit 2, Lesson Bank 4–7
- Singapore Textbook 3A, Chapter 2 (Multiplication with Arrays)
```

---

### EXAMPLE 2: Required Phrases Format

```markdown
### Required Phrases

* "[#] groups of [#]" — enables flexible discussion of groups without fixing singular/plural form
* "skip-count by [#]s" — connects skip-counting to multiplication as repeated addition
* "groups and singles" — helps students see remainders and flexible grouping
* "total" — precise language for the result; avoids "answer" which can feel procedural
```

---

### EXAMPLE 3: Forbidden Phrases Format

```markdown
### Forbidden Phrases

❌ **"multiply"** — too abstract at this stage; keeps focus on repeated addition and grouping, not algorithm
❌ **"the answer is"** — shifts focus from understanding to product-retrieval; say "the total" instead
❌ **"you can't divide by zero"** — rule-based without meaning; save for later when students understand division concept
❌ **"just count them all"** — undermines the value of grouping strategy; encourages inefficient counting
```

---

### EXAMPLE 4: Interaction Block (Full Structure)

```markdown
### Interaction L.3: Regroup and Count [EMBODIED]

**Setup:**
Each student receives 12 small cubes. Teacher has a large pile of cubes visible. "We have lots and lots of cubes. Let's see if we can count them faster by making groups."

**Student Action:**
Students make groups of 4 using their 12 cubes. Teacher circulates and observes how they organize (some may group all, some may make piles). "How many groups did you make? Count by fours to figure out the total."

**Teacher Move:**
Ask: "How many fours are in your pile? Show me with your fingers. Now skip-count with me: four... eight... twelve."
Affirm: "Yes! You made 3 groups of 4, and you figured out the total is 12. You used grouping to count faster!"
Intervene (if student counts all individually): "Try making the groups first, THEN skip-count the groups. That's the shortcut."

**Key Observation:**
Students recognize that skip-counting groups is faster than counting ones.
Students may naturally say "four, eight, twelve" or "4, 8, 12" — both are acceptable.

**Common Detour:**
Student makes groups but then loses track and counts all ones again.
Student groups but doesn't use skip-counting (says "4, 4, 4, total 12").

**Intervention:**
Say: "Let's try it together. First, point to group 1 and say four. Point to group 2 and say eight. What's next?" (Guide the skip-counting gesture and rhythm.)

**Next Move:**
Transition to representational: "Now let's draw pictures of groups instead of using cubes. Your pictures will help you remember what you did."

**Duration:**
3–4 minutes for the full interaction (setup, action, observation, intervention if needed)
```

---

### EXAMPLE 5: Section Transition Markers

```markdown
→ **SECTION 1 COMPLETE. PROCEED TO SECTION 2.**

---

### Section 2: Representational — Arrays and Skip-Counting (REPRESENTATIONAL)
```

---

### EXAMPLE 6: KDD Items (H3 Format)

```markdown
### KDD-1: Why We Use Cubes Instead of Pre-Made Arrays

Array worksheets are faster to distribute, but students who don't physically group the cubes often memorize "5 × 3 = 15" without understanding grouping. Using cubes forces the grouping action, which is non-negotiable for misconception prevention. Once students can physically make and count groups (Concrete), they can visualize the same action in arrays (Representational).

### KDD-2: Three Sections Mirrors the Three Stages of Misconception Unwinding

Section 1 (Concrete) addresses the misconception "groups are just piles" by having students physically arrange and recount groups multiple times. Section 2 (Representational) addresses "the picture is the whole story" by having students generate their own drawings and skip-count from drawings. Section 3 (Abstract) addresses "symbols have no meaning" by tying written multiplication directly back to groups.

### KDD-3: Why Synthesis Includes Real-World Connection but NOT Application to Division

This module establishes grouping as the foundation of multiplication. Division (as inverse) comes next module. Prematurely linking to division risks confusion. Synthesis connects backward (to "you can skip-count") and forward (to "next you'll split groups"), but does not solve division problems.
```

---

### EXAMPLE 7: Verification Checklist with Bold IDs

```markdown
### Verification Checklist (Lesson)

- [x] **L-Purpose:** Teacher opens with clear purpose frame ("Today we're learning to count groups fast")
- [ ] **L-CRA:** All three CRA stages are present; concrete comes before representational comes before abstract
- [ ] **L-Phrases:** Teacher uses required phrases ("[#] groups of [#]", "skip-count by [#]s") at least 3 times
- [ ] **L-Misconceptions:** Teacher explicitly addresses each primary/secondary misconception (e.g., "Your pile is 3 groups of 4, not just a big pile")
- [ ] **L-Closure:** Lesson ends with success criteria confirmed and bridge to exit check ("Now you're ready to show me you can do this on your own")
```

---

### EXAMPLE 8: Learning Goal Alignment Check (Table)

```markdown
### Alignment Check

| Exit Check Problem | L1 (Equal Groups) | L2 (Fluent Skip-Count) | Module Goal | Notes |
|-------------------|-------------------|------------------------|-------------|-------|
| EC.1 (Interpret 4 groups of 5) | ✓ | | ✓ | Assesses understanding of grouping |
| EC.2 (Skip-count and write multiplication) | | ✓ | ✓ | Assesses fluency and symbolic notation |
| EC.3 (Array problem with remainder) | ✓ | ✓ | ✓ | Assesses flexible thinking about groups |
```

---

## USAGE NOTES FOR AI GENERATION

1. **Section Order Is Non-Negotiable:** 1.0 → 1.1 → 1.2 → ... → 1.10. Do not rearrange.
2. **All Numbered Sections (1.0–1.10) Are H2.** No exceptions.
3. **All Subsections and Interactive Elements Are H3.** If you find yourself writing an H4, convert to bold inline label instead.
4. **Required/Forbidden Phrases Come BEFORE Interactions in §1.7.** This is a critical sequencing rule.
5. **No "Module-Specific Lesson Guidance" Wrapper.** Each subsection (Misconception Prevention, Incomplete Script Flags, Success Criteria, Verification Checklist) is its own H3.
6. **Section Markers Use Arrow Format.** `→ **SECTION X COMPLETE. PROCEED TO SECTION Y.**`
7. **KDD Items Are H3, Not Numbered Lists.** Format: `### KDD-N: Title`
8. **Verification Checklists Use Checkbox Format.** `- [x] **Item ID:** Description`
9. **Tables Appear in Parameters, Constraints, Alignment Check, Distribution Targets, Etc.** Use standard markdown table syntax.
10. **Interaction Blocks Include All Nine Fields:** Setup, Student Action, Teacher Move, Key Observation, Common Detour, Intervention, Next Move, Duration. (See Example 4.)

---

## QUICK REFERENCE: WHAT GOES IN EACH MAJOR SECTION

| Section | Purpose | Key Content |
|---------|---------|-------------|
| **1.0 THE ONE THING** | Elevator pitch for the module | Bold inline labels: CRA Stage, Critical Misconception, Success Indicator, Biggest Risk |
| **1.1 LEARNING GOALS** | Curriculum alignment and exit criteria | L1, L2, Module Goal, Exit Check Tests, Question Stems, Standards Cascade, Bridges, Sources |
| **1.2 SCOPE BOUNDARIES** | What's in/out of this module | Must Teach, Must Not Include, Confirmation Checklist |
| **1.3 VOCABULARY ARCHITECTURE** | Vocabulary staging and strategy | Staging by Phase, Notes, Terms to Avoid |
| **1.4 MISCONCEPTIONS** | Non-obvious student reasoning errors | Misconception IDs, descriptions, manifestations, interventions |
| **1.5 TOY SPECIFICATIONS** | Physical/visual materials used | Toy names, specs, affordances, constraints |
| **1.6 WARMUP** | 3–5 min activation phase | Purpose, Parameters, Constraints, 2–3 interactions, Verification |
| **1.7 LESSON** | Main 15–20 min teaching | Purpose + Flow, Structure Table, Required/Forbidden Phrases, Purpose Frame, 3 CRA Sections with interactions, Misconception Prevention, Flags, Success Criteria, Verification, Module-Specific Notes |
| **1.8 EXIT CHECK** | 3–5 min formative assessment | Parameters, Constraints, Alignment Check, Transition Frame, 3 Problems, Verification |
| **1.8.5 PRACTICE INPUTS** | Homework/fluency phase | Overview, Distribution Targets, Toy/Dimension Constraints, Pool & Tracking, Module-Specific Notes |
| **1.9 SYNTHESIS** | 6–8 min closure and preview | Parameters, Constraints, Opening Frame, 2 Connection Tasks, Metacognitive Reflection, Identity Closure, Verification, Flags |
| **1.10 KEY DESIGN DECISIONS** | Rationale for non-obvious choices | 3–5 KDD items explaining pedagogical trade-offs |

---

**Document Version:** 03.25.26
**Last Updated:** 2026-03-25
**Status:** Canonical Reference — Use This for All Module Starter Pack Generation
