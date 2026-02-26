# PRACTICE PHASE PLAYBOOK v3

## **1\. PHASE IDENTITY**

| Attribute | Value |
| :---- | :---- |
| Phase Name | Practice |
| Position | After Exit Check, before Synthesis |
| Character | **Helper** (not Guide) |
| Duration | 10 to 15 minutes |
| Purpose | Independent application through varied problem sets |

**Core Purpose:** Independent application of Lesson concepts through varied problem sets. This Playbook guides **template generation** (Step 1 of the Practice pipeline).

**What This Playbook Covers:**

- Lesson analysis and constraint extraction
- Goal decomposition into skills
- Template schema and requirements
- Tier and cognitive type distribution
- Helper voice guidelines
- Template validation criteria

**What Other Documents Cover:**

- Problem Expansion (Step 2\) → separate prompt
- Remediation Generation (Step 3\) → separate prompt
- Pattern definitions → Pattern Library

**Character Note:** Practice phase uses **Helper**, not Guide. Helper is direct, task-focused, and supportive without excessive warmth. This separation preserves Guide for high-stakes moments (Lesson, Exit Check, Synthesis). Template `prompt_examples` and `success_dialogue` should reflect Helper voice.

---

## **2\. GOAL DECOMPOSITION FRAMEWORK**

**Goal decomposition is integrated into template generation.** The AI produces the lesson analysis, decomposition, AND templates in a single output.

### **Decomposition Structure**

Skills are organized by component and linked to templates. For Modules 2+, each skill documents its relationship to previous module skills (as identified in Lesson Analysis).

**Module 1 Format:**

```
COMPONENT A: PROCEDURAL (30-40%)

M1-01  Student can identify equal parts in partitioned shapes
       Lesson: Steps 1.2-1.4 — shape partitioning introduction
       Verbs: identify
       Tiers: support, baseline
       Templates: 1001, 1002
```

**Modules 2+ Format (includes progression):**

```
COMPONENT A: PROCEDURAL (30-40%)

M4-01  Student can place unit fraction on 0-1 number line
       Builds on: M3-02 — counting equal parts
       Extension: Counting transfers to linear model (intervals)
       Lesson: Steps 2.1-2.3 — number line introduction
       Verbs: create
       Tiers: support, baseline
       Templates: 4001, 4002

M4-02  Student can place non-unit fraction on 0-1 number line
       Builds on: M4-01 + M3-04 — unit placement + non-unit understanding
       Extension: Combines skills for non-unit on number line
       Lesson: Steps 2.4-2.6 — non-unit placement
       Verbs: create
       Tiers: baseline, stretch
       Templates: 4003, 4004
```

**Required Fields (Modules 2+):**

* `Builds on:` — Previous skill ID(s) from Lesson Analysis, or "NEW"
* `Extension:` — What's new/different (omit for NEW skills)
* `Lesson:` — Step reference showing where skill was taught
* `Verbs:` — Cognitive action(s) assessed
* `Tiers:` — Difficulty range
* `Templates:` — Template IDs assessing this skill

The `Builds on` and `Extension` fields should match the Skill Progression Analysis from Lesson Analysis—Goal Decomposition applies that analysis to specific skills.

### **Skill ID Convention**

Format: `MX-0Y` where:

- `M` \= literal "M" for mastery
- `X` \= module number
- `0Y` \= two-digit skill number within module

Examples: `M4-01`, `M4-02`, `M10-03`

### **Lesson Alignment Requirement**

Every skill MUST include a Lesson Alignment statement showing:

- Which Lesson step(s) taught this skill
- Specific interaction type or prompt that introduced it
- OR explicit "Skill transfer" notation if not directly taught

This validates that Practice assesses what was taught, not new content.

### **Skill Coverage Validation**

Each skill becomes a "template family." Coverage validation:

- ✓ Every skill has at least one template
- ✓ Every skill has documented Lesson Alignment
- ✓ Tier distribution matches targets
- ✓ All required fractions covered across templates

---

## **2B. LESSON ANALYSIS**

Before decomposing skills, analyze the Lesson to understand constraints.

### **Fraction Coverage Analysis**

Document which fractions were explicitly taught vs. require skill transfer:

```
─────────────────────────────────────────────────────────────
Fraction     │ In Lesson? │ Practice Strategy
─────────────────────────────────────────────────────────────
1/3, 1/4     │ ✅ Yes     │ Direct practice
3/4, 3/5     │ ✅ Yes     │ Direct practice
5/4          │ ✅ Yes     │ Direct practice
─────────────────────────────────────────────────────────────
1/2, 1/6     │ ❌ No      │ Skill transfer — same counting strategy
2/3, 5/6     │ ❌ No      │ Skill transfer — same counting strategy
6/4, 7/4     │ ❌ No      │ Skill transfer — same beyond-1 strategy
─────────────────────────────────────────────────────────────
```

**Decision Rule:** If a fraction wasn't taught but uses the same generalizable skill, document the transfer rationale and proceed.

### **Toy Constraints Table**

Extract available toys and their interaction constraints:

```
─────────────────────────────────────────────────────────────
Toy                │ Description              │ Student Interaction
─────────────────────────────────────────────────────────────
extended_number_line│ Pre-partitioned 0-1 line │ click_tick to place point
fraction_bar       │ Shaded rectangle bar     │ Display only (reference)
─────────────────────────────────────────────────────────────
```

### **Key Constraints**

Document critical constraints that affect problem design:

```
⚠️ KEY CONSTRAINTS FOR MODULE 4:
• All number lines come PRE-PARTITIONED
• Students CLICK existing tick marks (not create them)
• Student-created partitioning is MODULE 5
• Range: 0-1 for standard, 0-2 for beyond-1
```

These constraints determine which problem types are valid.

---

## **2C. MISCONCEPTION PRIORITIZATION**

Not all misconceptions apply equally to all templates. Classify by priority:

### **Primary Misconceptions**

High likelihood of occurrence; MUST be targeted by multiple templates.

### **Secondary Misconceptions**

Lower likelihood or narrower scope; target in specific relevant templates.

**Example for Module 4:**

```
─────────────────────────────────────────────────────────────
PRIMARY MISCONCEPTIONS (target in 3+ templates)
─────────────────────────────────────────────────────────────
#5  Counting Ticks Instead of Spaces
    What it looks like: Counts tick marks including endpoints
    Detection: Answer = denominator + 1 or denominator - 1

#4  Improper Spacing
    What it looks like: Accepts unequal intervals as valid
    Detection: Selects line with unequal spacing

─────────────────────────────────────────────────────────────
SECONDARY MISCONCEPTIONS (target in 1-2 templates)
─────────────────────────────────────────────────────────────
#2  Misidentifying the Whole
    What it looks like: Restarts counting at 1 on 0-2 line
    Detection: Position in second whole at wrong interval

#6  Numerator/Denominator Reversal
    What it looks like: Counts denominator intervals, not numerator
    Detection: Position = denominator instead of numerator
```

---

## **2D. SKILL PROGRESSION ANALYSIS (Modules 2+)**

For Modules 2 and beyond, analyze how this module's skills will connect to the previous module. This analysis happens BEFORE goal decomposition, informing how you break down the learning goal.

### **Input Required**

Before generating templates for Module N, obtain:

- **Module N-1 Goal Decomposition** — skills that were just established
- **Module N-1 Template Summary** — what was just practiced

These documents show what students have already mastered, enabling explicit skill building.

**Module 1:** Skip this analysis (no previous module exists).

### **Analysis Process**

1. Review previous module's skills
2. Identify which previous skills are prerequisites for THIS module's learning goal
3. Note which previous skills will be EXTENDED (same skill, harder content)
4. Note which previous skills will be APPLIED in new contexts
5. Identify any genuinely NEW skills this module introduces

### **Progression Classification**

| Classification | Definition | Example |
| :---- | :---- | :---- |
| **BUILDS ON** | Directly extends a previous skill to harder content | M3: place unit fractions → M4: place non-unit fractions |
| **EXTENDS** | Applies a previous skill to new representation | M3: count parts in shapes → M4: count intervals on number line |
| **COMBINES** | Integrates multiple previous skills | M4: placement \+ comparison → M5: ordering multiple fractions |
| **NEW** | Genuinely new skill not dependent on previous module | First introduction of a concept |

### **Output: Skill Progression Table**

Include this table in Lesson Analysis (Output 1):

───────────────────────────────────────────────────────────── SKILL PROGRESSION ANALYSIS ─────────────────────────────────────────────────────────────

Previous Module Skills (M3): M3-01: Identify equal parts in partitioned shapes M3-02: Count equal parts to determine denominator M3-03: Identify fraction from shaded shape M3-04: Understand non-unit fractions (multiple parts shaded) M3-05: Compare fractions using visual models

Anticipated Progressions for This Module (M4): ───────────────────────────────────────────────────────────── Previous Skill │ Relationship │ This Module Extension ───────────────────────────────────────────────────────────── M3-02 │ EXTENDS │ Counting → number line (intervals) M3-03 │ EXTENDS │ Reading fraction → linear model M3-04 │ BUILDS ON │ Non-unit understanding → non-unit placement M3-05 │ EXTENDS │ Shape comparison → number line comparison — │ NEW │ Inverse task: identify fraction from point ─────────────────────────────────────────────────────────────

Prerequisites: M3-02, M3-04 (counting and non-unit understanding required)

This analysis directly informs Goal Decomposition—each anticipated progression becomes a skill with documented lineage.

### **Chain of Custody**

Each module only needs the PREVIOUS module's outputs. The chain preserves lineage:

- M3's decomposition references M2
- M4's decomposition references M3 (which already incorporated M2)
- No need to include M1-M2 when generating M4

This keeps context manageable while maintaining curriculum continuity.
---

## **3\. BOUNDARIES & CONSTRAINTS**

### **Permitted Elements**

- Problems using ONLY visuals/toys from Lesson
- Problems using ONLY actions demonstrated in Lesson
- Fractions from Module Starter Pack requirements
- Tier-appropriate scaffolding
- Helper voice (direct, task-focused)
- Skill transfer for fractions using taught strategies

### **Forbidden Elements**

- New visual tools not introduced in Lesson
- Actions students haven't practiced
- Fractions requiring untaught strategies
- Guide dialogue in Practice phase (use Helper only)
- Generic feedback ("good job") that works for any problem
- Excessive warmth or celebration

### **Critical Constraint**

All variety must use ONLY what was taught in Lesson:

- ✓ Use `toy` values from Lesson
- ✓ Use workspace specs matching Lesson constraints
- ✓ Use `action_list` items practiced in Lesson
- ✗ Do NOT introduce new toys
- ✗ Do NOT change fundamental constraints
- ✗ Do NOT add actions students haven't seen

---

## **4\. STRUCTURAL REQUIREMENTS**

### **Pool Target**

Each module specifies a target problem count:

| Module Stage | Typical Pool Target |
| :---- | :---- |
| Early (1-4) | 55-65 problems |
| Mid (5-8) | 60-75 problems |
| Late (9-12) | 65-80 problems |

Pool target should be specified in the generation prompt.

### **Tier Distribution Targets**

| Tier | Target % | Counts Toward Mastery |
| :---- | :---- | :---- |
| `baseline` | 40-50% | Yes |
| `stretch` | 20-25% | Yes |
| `support` | 15-20% | No |
| `confidence` | 10-15% | No |
| `challenge` | 5-10% | Yes |

### **Component Weight Targets**

| Component | Target % | Description |
| :---- | :---- | :---- |
| `procedural` | 30-40% | Execute the skill |
| `conceptual` | 30-40% | Understand the concept |
| `transfer` | 20-30% | Apply to new contexts |

---

## **4B. TEMPLATE SCHEMA (Teacher Review)**

### **Template ID Convention**

Format: `"XXXX"` where first digit(s) \= module, remaining \= sequence

* `"4001"` \= Module 4, Template 1
* `"4012"` \= Module 4, Template 12
* `"10003"` \= Module 10, Template 3

Templates are presented in a dual-format structure optimized for teacher review while preserving JSON for the pipeline.

**Format Structure:**

Each template includes:

1. **Human-readable section** with color-coded key fields
2. **JSON block** containing the complete template specification

**Color Key for Teacher Review:**

* 🟢 **Green** \= SKILL (what the student demonstrates)
* 🔵 **Blue** \= PROBLEM TYPE (what the student does)
* 🟠 **Orange** \= PROMPT EXAMPLES (what Helper says)
* 🟣 **Purple** \= SUCCESS DIALOGUE (feedback on correct answer)

**Teacher Review Focus:** Teachers review the colored sections for pedagogical accuracy, age-appropriateness, and voice quality. The JSON travels intact to the next pipeline step.

**Example template (dual format):**

---

**Template 4001 — Place Unit Fraction on 0-1 Line**

**SKILL** *(highlight green)* Student can place unit fractions on 0-1 number line by counting intervals from zero

**PROBLEM TYPE** *(highlight blue)* Student clicks tick mark to place unit fraction on pre-partitioned 0-1 number line

**PROMPT EXAMPLES** *(highlight orange)*

* "Place one-third on the number line."
* "Find 1/4. Click its position."
* "Where is one-fifth? Place a point there."

**SUCCESS DIALOGUE** *(highlight purple)*

* "One-third. One interval from zero."
* "That's 1/4. Got it."
* "Right—one-fifth."

**Technical Details (JSON)**

sson

```json
{
  "template_id": "4001",
  "skill_id": "M4-01",
  "skill": "Student can place unit fractions on 0-1 number line by counting intervals from zero",
  "problem_type": "Student clicks tick mark to place unit fraction on pre-partitioned 0-1 number line",
  "workspace_description": "Horizontal number line from 0 to 1 with tick marks pre-placed at all fraction positions for the given denominator. Only 0 and 1 are labeled.",
  "prompt_examples": [
    "Place one-third on the number line.",
    "Find 1/4. Click its position.",
    "Where is one-fifth? Place a point there."
  ],
  "action_description": "Student clicks a tick mark to place a point at that position",
  "mastery_tier": ["support", "baseline"],
  "mastery_verb": "create",
  "parameter_coverage": {
    "fractions": ["1/2", "1/3", "1/4", "1/5", "1/6", "1/8"]
  },
  "correct_end_state": "Point placed at the correct tick mark position corresponding to the target fraction",
  "success_dialogue": [
    "One-third. One interval from zero.",
    "That's 1/4. Got it.",
    "Right—one-fifth."
  ]
}

```

### **Field Reference**

| Field | Type | Description |
| :---- | :---- | :---- |
| `template_id` | string | `"XXXX"` format (module \+ sequence) |
| `skill` | string | What student demonstrates mastery of |
| `problem_type` | string | Human-readable description of what student does |
| `workspace_description` | string | Plain-language visual description including any multiple choice options |
| `prompt_examples` | array | 3-5 example phrasings of the instruction |
| `action_description` | string | Narrative of student actions |
| `mastery_tier` | array | Difficulty range: `"confidence"`, `"support"`, `"baseline"`, `"stretch"`, `"challenge"` |
| `mastery_verb` | string | Cognitive action: `"create"`, `"identify"`, `"compare"`, `"apply"`, `"analyze"`, `"evaluate"` |
| `parameter_coverage` | object | Mathematical parameters that vary (fractions, denominators, etc.) |
| `correct_end_state` | string | What success looks like |
| `success_dialogue` | array | Brief Helper feedback messages (5-15 words each) |

### **Field Details**

**skill**

* Self-contained statement of what student demonstrates
* Should align to Goal Decomposition skills
* Example: `"Student can count intervals to identify the denominator"`

**mastery\_tier**

* Array indicating the difficulty range this template serves
* A template marked `["baseline", "stretch"]` can generate problems at either level
* Scaffolding and parameter selection at generation time determine actual tier
* Example: `["support", "baseline"]` or `["challenge"]`

**parameter\_coverage**

* Defines what varies across problem instances generated from this template
* Common parameters:
  * `fractions`: specific fractions like `["1/3", "2/3", "3/4"]`
  * `denominators`: when varying denominator broadly like `[2, 3, 4, 6, 8]`
* Add problem-specific parameters as needed (e.g., `"ranges"`, `"comparison_types"`)

**success\_dialogue**

* Brief, varied Helper voice feedback
* Should reference the specific mathematical content where appropriate
* Avoid generic praise ("Great job\!") — use task-focused acknowledgment

### **What Happens After Teacher Review**

After teachers approve templates, a separate pipeline step expands this schema into the full engineering specification, adding:

* `workspace_detailed` — technical specs for each visual element
* `action_list` — parsed interaction types
* `misconceptions_targeted` — assigned based on problem\_type patterns
* `remediation_approach` — generated via Remediation Addition Protocol
* `tier_constraints` — scaffolding specs per difficulty level
* `target_count` — determined during pool composition

Teachers do not need to specify these fields. The expansion step extrapolates them from the teacher-reviewed schema plus module conventions.

---

## **5A. PROBLEM DESIGN FRAMEWORK**

**The Five Cognitive Types:**

**CREATE** \- Constructing or building representations

* *Definition:* Student constructs a fraction using visual tools
* *Example prompt:* "Place three-fourths on the number line."
* *Maps to:* `mastery_component: "procedural"` (can execute the skill)
* *Typical actions:* `place_tick`, `click_tick`, `tap_to_shade`, `partition`, `drag`
* *Reality check:* Appropriate for all modules when building/placing is the goal

**IDENTIFY** \- Recognizing and selecting

* *Definition:* Student recognizes/selects a fraction from options or visual
* *Example prompt:* "How many equal spaces are between 0 and 1?"
* *Maps to:* `mastery_component: "conceptual"` (understands what fractions mean)
* *Typical actions:* `select`, `click_choice`, `select_tick`
* *Reality check:* Appropriate for all modules when recognition is the goal

**COMPARE** \- Analyzing relationships between fractions

* *Definition:* Student compares two or more fractions or representations
* *Example prompt:* "Which number line shows fourths?"
* *Maps to:* `mastery_component: "conceptual"` or `"transfer"` (understands relationships)
* *Typical actions:* `select`, `multi_select`, `drag_to_order`
* *Reality check:* Only appropriate when comparison was explicitly taught in Lesson

**APPLY** \- Using fractions in context

* *Definition:* Student uses fractions to solve a contextualized problem
* *Example prompt:* "Find 3/4 inch on the ruler."
* *Maps to:* `mastery_component: "transfer"` (can use knowledge flexibly)
* *Typical actions:* `click_tick`, `tap_to_shade`, `select`
* *Reality check:* Only appropriate when context application was modeled in Lesson

**CONNECT** \- Linking representations or concepts

* *Definition:* Student connects different fraction representations
* *Example prompt:* "The bar shows a fraction. Find the same fraction on the number line."
* *Maps to:* `mastery_component: "transfer"` (sees connections across representations)
* *Typical actions:* `place_tick`, `select_tick`, `drag_to_match`
* *Reality check:* Only appropriate when multiple representations were explicitly linked in Lesson

---

### **Cognitive Type to Template Mapping**

| mastery\_verb | Primary mastery\_component | Typical Tiers | Common Actions |
| :---- | :---- | :---- | :---- |
| `create` | `procedural` | baseline, support | `place_tick`, `click_tick`, `tap_to_shade`, `partition` |
| `identify` | `conceptual` | baseline, support, stretch | `select`, `click_choice`, `select_tick` |
| `compare` | `conceptual` or `transfer` | baseline, stretch, challenge | `select`, `multi_select`, `drag_to_order` |
| `apply` | `transfer` | stretch, challenge | `click_tick`, `tap_to_shade`, `select` |
| `connect` | `transfer` | stretch, challenge | `place_tick`, `select_tick`, `drag_to_match` |

---

## **5B. COGNITIVE TYPE PROGRESSION BY MODULE**

Not all cognitive types are appropriate for all modules. Use these targets:

### **Modules 1-3 (Foundational)**

| Cognitive Type | Target % | Notes |
| :---- | :---- | :---- |
| `create` | 50-60% | Primary focus |
| `identify` | 30-40% | Secondary focus |
| `compare` | 0-10% | Only if explicitly taught |
| `apply` | 0% | Not yet |
| `connect` | 0% | Not yet |

### **Modules 4-6 (Building)**

| Cognitive Type | Target % | Notes |
| :---- | :---- | :---- |
| `create` | 40-50% | Still primary |
| `identify` | 25-30% | Growing |
| `compare` | 15-20% | Emerging |
| `apply` | 10-15% | Beginning |
| `connect` | 0% | Not until Module 7+ |

### **Modules 7-9 (Developing)**

| Cognitive Type | Target % | Notes |
| :---- | :---- | :---- |
| `create` | 30-35% | Decreasing |
| `identify` | 20-25% | Stable |
| `compare` | 20-25% | Growing |
| `apply` | 15-20% | Growing |
| `connect` | 5-10% | Emerging |

### **Modules 10-12 (Advanced)**

| Cognitive Type | Target % | Notes |
| :---- | :---- | :---- |
| `create` | 20-25% | Maintenance |
| `identify` | 15-20% | Maintenance |
| `compare` | 25-30% | Primary |
| `apply` | 20-25% | Primary |
| `connect` | 10-15% | Growing |

---

## **5C. PROBLEM POOL STRATEGY**

### **Variety Within Constraints**

Vary problems by:

- Different fractions within `parameter_coverage`
- Different prompt phrasings from `prompt_examples`
- Different workspace setups per `tier_constraints`

### **Critical: Stay Within Lesson Boundaries**

All variety must use ONLY what was taught in Lesson:

- ✓ Use `toy` values from Lesson
- ✓ Use workspace specs matching Lesson constraints
- ✓ Use `action_list` items practiced in Lesson
- ✗ Do NOT introduce new toys
- ✗ Do NOT change fundamental constraints
- ✗ Do NOT add actions students haven't seen

---

## **5D. TIER DEFINITIONS**

### **BASELINE**

- Core grade-level problems
- Standard presentation
- Counts toward mastery
- Largest portion of pool (40-50%)

### **STRETCH**

- More challenging parameters (larger denominators, non-unit fractions)
- Less scaffolding
- Counts toward mastery
- Second largest portion (20-25%)

### **SUPPORT**

- Simplified parameters (smaller denominators, unit fractions)
- Additional scaffolding (guides, hints visible)
- Does NOT count toward mastery
- For students needing extra help (15-20%)

### **CONFIDENCE**

- Very simple problems
- Maximum scaffolding
- Does NOT count toward mastery
- Build confidence before retry (10-15%)

### **CHALLENGE**

- Most difficult parameters
- No scaffolding, may include distractors
- Counts toward mastery
- For advanced students (5-10%)

### **Tier Assignment in Templates**

A single template can span multiple tiers via the `mastery_tier` array:

```json
"mastery_tier": ["baseline", "stretch"]
```

Tier-specific constraints (which parameters, target counts, workspace setup) go in `tier_constraints`:

```json
"tier_constraints": {
  "baseline": {
    "fractions": ["1/3", "1/4", "2/3", "3/4"],
    "target_count": 8,
    "workspace_requirements": "Standard number line"
  },
  "stretch": {
    "fractions": ["1/6", "1/8", "5/6", "3/8"],
    "target_count": 4,
    "workspace_requirements": "Standard number line, more intervals"
  }
}
```

---

## **5E. TEMPLATE CLASSIFICATION**

Classification lives in `goal_decomposition`:

```json
{
  "goal_decomposition": {
    "mastery_tier": ["baseline", "stretch"],
    "mastery_verb": "identify",
    "mastery_component": "conceptual",
    "mastery_skill_id": "M4-03",
    "mastery_skill": "Student can count intervals to identify the denominator",
    "lesson_alignment": "MultipleChoice prompts: 'How many spaces between 0 and 1?'"
  }
}
```

**Key points:**

- `mastery_tier` is an **array** — one template can span multiple tiers
- Tier-specific constraints go in `tier_constraints`, not here
- `mastery_skill_id` format: `"MX-0Y"` (M \+ module number \+ hyphen \+ skill number)
- `lesson_alignment` is **required** — documents where skill was taught

---

## **5F. HELPER CHARACTER**

Practice phase uses **Helper**, not Guide. This separation:

- Maintains Guide's role for high-stakes moments (Lesson, Exit Check, Synthesis)
- Keeps Practice dialogue direct and efficient
- Prevents student fatigue from constant Guide warmth

### **Helper Voice Guidelines**

| Dimension | Helper Approach |
| :---- | :---- |
| **Warmth** | Moderate \- supportive but efficient |
| **Length** | Concise \- direct and focused |
| **Praise** | Brief acknowledgment, task-focused |
| **Remediation** | Clear, instructional, progressive |
| **Tone** | "Here's what to try..." not "I'm so excited..." |

### **Helper Success Feedback**

Brief, varied, task-focused:

- "That's right."
- "Got it."
- "Yes, three-fourths."
- "Correct—two spaces from zero."
- "One-third. Good."

**Avoid:**

- "Great job\!" (too warm for Helper)
- "You're amazing\!" (Guide territory)
- "I knew you could do it\!" (over-invested)

### **Helper Remediation Language**

**Light (10-20 words):**

- "Count the spaces from zero."
- "Look at how many intervals."
- "Check—count spaces, not tick marks."

**Medium (25-35 words):**

- "Count the spaces between tick marks, starting from zero. The numerator tells you how many to count."
- "The denominator says how many equal parts. Count that many spaces."

**Heavy (40-60 words):**

- "Let me show you. \[demonstration\] That's three-fourths."
- "Watch this. \[modeling\] Count with me: one, two, three. Three spaces from zero."

**Post-Modeling (Helper stays in Practice):**

- "There you go."
- "Now you've got it."
- "See how that works?"

---

## **6\. TEMPLATE VALIDATION CHECKLIST**

**Before submitting templates for teacher review:**

### **Lesson Analysis Complete**

- [ ] Fraction coverage analysis documented (taught vs. transfer)
- [ ] Tool constraints identified
- [ ] Key constraints noted
- [ ] Primary vs. secondary misconceptions classified

### **Goal Decomposition Complete**

- [ ] All three components represented (`procedural`, `conceptual`, `transfer`)
- [ ] Each skill clearly stated
- [ ] Skills collectively cover the full learning goal
- [ ] Lesson alignment verified (skills match what was taught)

### **Skill Progression Complete (Modules 2+ only)**

- [ ] Previous module Goal Decomposition reviewed
- [ ] Previous module Template Summary reviewed
- [ ] Skill Progression Analysis included in Lesson Analysis output
- [ ] Each skill in Goal Decomposition has `Builds on` field
- [ ] `Builds on` references match Lesson Analysis progression table
- [ ] Extension descriptions explain what's new
- [ ] No skills marked NEW that clearly build on previous module
- [ ] Prerequisites from previous module identified

### **Template Coverage**

- [ ] Every skill has at least one template
- [ ] All Starter Pack required fractions appear across `parameter_coverage`
- [ ] Tier ranges appropriate for module level
- [ ] Cognitive verb (`mastery_verb`) distribution reasonable for module stage

### **Template Quality**

Each template includes:

- [ ] `template_id` — format `"XXXX"` (module \+ sequence)
- [ ] `skill` — clear statement of what student demonstrates
- [ ] `problem_type` — describes what student does
- [ ] `workspace_description` — plain language visual setup
- [ ] `prompt_examples` — 3-5 varied phrasings
- [ ] `action_description` — what student physically does
- [ ] `mastery_tier` — appropriate difficulty range
- [ ] `mastery_verb` — correct cognitive type
- [ ] `parameter_coverage` — all relevant parameters listed
- [ ] `correct_end_state` — clear success state
- [ ] `success_dialogue` — 3+ varied Helper responses

### **Terminology Compliance**

- [ ] `mastery_tier` values lowercase
- [ ] `mastery_verb` values lowercase
- [ ] Tool names in `workspace_description` match engineering conventions

### **Distribution Checks**

**Tier Coverage (across all templates):**

| Tier | Coverage Expectation |
| :---- | :---- |
| `confidence` | At least 1-2 templates include this tier |
| `support` | At least 2-3 templates include this tier |
| `baseline` | Most templates should include this tier |
| `stretch` | At least 3-4 templates include this tier |
| `challenge` | At least 1-2 templates (Modules 4+) |

**Cognitive Verb Distribution:**

Check against Section 5B targets for your module stage. Flag if any required verb type has zero templates.
---

## **7\. TEMPLATE GENERATION WORKFLOW**

This Playbook supports **Step 1: Template Generation**. Problem expansion and remediation generation are covered in separate documents.

**Required Inputs:**

| Document | Contents | Required For |
| :---- | :---- | :---- |
| Module Starter Pack | Learning goals, concepts, misconceptions, fraction requirements | All modules |
| Lesson JSON | Actual taught content, toys, actions, constraints | All modules |
| This Playbook | Schema, validation criteria, distribution targets | All modules |
| Previous Module Outputs | Goal Decomposition \+ Template Summary from Module N-1 | Modules 2+ |

**Module 1:** Only requires first three inputs.

**Modules 2+:** Must include previous module's Goal Decomposition and Template Summary to enable Skill Progression Analysis in Lesson Analysis step.

### **Input Parameters**

| Parameter | Description | Example |
| :---- | :---- | :---- |
| Module Number | Which module | 4 |
| Path | Which pedagogical path | B (Singapore) |
| Pool Target | Total problems to generate | 60-65 |

### **Generation Process**

1. **Analyze the Lesson** — Extract toys, actions, constraints, fraction coverage
2. **Classify misconceptions** — Primary vs. secondary
3. **Decompose the learning goal** — Skills by component with lesson alignment
4. **Generate templates** — Covering all skills across tiers
5. **Validate coverage** — Check all requirements
6. **Output artifacts** — Goal Decomposition \+ Template Summary \+ Templates \+ Coverage Summary

### **Output Artifacts**

Template generation produces FOUR outputs:

---

#### **Artifact 1: Lesson Analysis**

Documents constraints and coverage analysis.

```
═══════════════════════════════════════════════════════════════
MODULE 4 PATH B — LESSON ANALYSIS
═══════════════════════════════════════════════════════════════

FRACTION COVERAGE
─────────────────────────────────────────────────────────────
Fraction     │ In Lesson? │ Practice Strategy
─────────────────────────────────────────────────────────────
1/3, 1/4     │ ✅ Yes     │ Direct practice
3/4, 3/5     │ ✅ Yes     │ Direct practice
5/4          │ ✅ Yes     │ Direct practice
─────────────────────────────────────────────────────────────
1/2, 1/6     │ ❌ No      │ Skill transfer — same counting strategy
2/3, 5/6     │ ❌ No      │ Skill transfer — same counting strategy
6/4, 7/4     │ ❌ No      │ Skill transfer — same beyond-1 strategy
─────────────────────────────────────────────────────────────

TOYS AVAILABLE
─────────────────────────────────────────────────────────────
Toy                  │ Description              │ Interaction
─────────────────────────────────────────────────────────────
extended_number_line │ Pre-partitioned 0-1 line │ click_tick
fraction_bar         │ Shaded rectangle         │ Display only
─────────────────────────────────────────────────────────────

KEY CONSTRAINTS
─────────────────────────────────────────────────────────────
⚠️ All number lines come PRE-PARTITIONED
⚠️ Students CLICK existing tick marks (not create them)
⚠️ Student-created partitioning is MODULE 5
⚠️ Range: 0-1 standard, 0-2 for beyond-1
─────────────────────────────────────────────────────────────

MISCONCEPTION PRIORITY
─────────────────────────────────────────────────────────────
PRIMARY (target in 3+ templates):
  #5  Counting Ticks Instead of Spaces
  #4  Improper Spacing

SECONDARY (target in 1-2 templates):
  #2  Misidentifying the Whole
  #6  Numerator/Denominator Reversal
═══════════════════════════════════════════════════════════════

SKILL PROGRESSION ANALYSIS (Modules 2+ only)
─────────────────────────────────────────────────────────────

Previous Module Skills (M[N-1]):
  M[N-1]-01: [skill statement]
  M[N-1]-02: [skill statement]
  [continue for all previous module skills...]

Anticipated Progressions for This Module:
─────────────────────────────────────────────────────────────
Previous Skill │ Relationship │ This Module Extension
─────────────────────────────────────────────────────────────
M[N-1]-XX      │ EXTENDS      │ [what changes]
M[N-1]-XX      │ BUILDS ON    │ [what's added]
M[N-1]-XX      │ EXTENDS      │ [new context]
—              │ NEW          │ [why genuinely new]
─────────────────────────────────────────────────────────────

Prerequisites: [which previous skills are required for this module]

```

---

#### **Artifact 2: Goal Decomposition (Teacher Review)**

Human-readable skill breakdown for teacher approval.

```
═══════════════════════════════════════════════════════════════ MODULE 4 PATH B — SKILL DECOMPOSITION ═══════════════════════════════════════════════════════════════ LEARNING GOAL: "[Paste verbatim from Section 1.1]" ─────────────────────────────────────────────────────────────── COMPONENT A: PROCEDURAL (35%) What students DO ─────────────────────────────────────────────────────────────── M4-01 Student can place unit fraction on 0-1 number line Builds on: M3-02 — counting equal parts Extension: Counting transfers to linear model Lesson: Steps 2.1-2.3 Verbs: create Tiers: support, baseline Templates: 4001, 4002 M4-02 Student can place non-unit fraction on 0-1 number line Builds on: M4-01, M3-04 Extension: Combines unit placement + non-unit understanding Lesson: Steps 2.4-2.6 Verbs: create Tiers: baseline, stretch Templates: 4003, 4004 ─────────────────────────────────────────────────────────────── COMPONENT B: CONCEPTUAL (40%) What students UNDERSTAND ─────────────────────────────────────────────────────────────── M4-03 Student can identify fraction from point on number line Builds on: M3-03 — identifying fractions in shapes Extension: Reading transfers to linear representation Lesson: Steps 3.1-3.2 Verbs: identify Tiers: baseline, stretch Templates: 4005, 4006 M4-04 Student can count intervals to determine denominator NEW — first introduction of denominator from visual Lesson: Steps 2.2, 3.3 Verbs: identify Tiers: support, baseline Templates: 4007 ─────────────────────────────────────────────────────────────── COMPONENT C: TRANSFER (25%) How students APPLY ─────────────────────────────────────────────────────────────── M4-05 Student can compare positions on different number lines Builds on: M3-05 — comparing fractions in shapes Extension: Comparison transfers to linear model Lesson: Steps 4.1-4.2 (implicit pattern recognition) Verbs: compare Tiers: stretch, challenge Templates: 4008, 4009 ═══════════════════════════════════════════════════════════════ SUMMARY ═══════════════════════════════════════════════════════════════ Total Skills: 5 Total Templates: 9 Component Distribution: PROC 35% | CONC 40% | TRANS 25% Progression: 4 build on previous | 1 genuinely new ═══════════════════════════════════════════════════════════════
```

**Teacher Review Questions:**

- Are these the right skills for this learning goal?
- Is any skill missing?
- Is the component distribution appropriate?
- Are tier assignments reasonable?
- Are lesson alignments accurate?

---

#### **Artifact 3: Template Summary (Quick Reference)**

Human-readable summary before full JSON.

```
═══════════════════════════════════════════════════════════════
MODULE 4 PATH B — TEMPLATE SUMMARY
═══════════════════════════════════════════════════════════════

#   │ ID   │ Problem Type                         │ Verb     │ Tiers           │ Problems
────┼──────┼──────────────────────────────────────┼──────────┼─────────────────┼─────────
1   │ 4001 │ Place unit fraction on 0-1 line      │ create   │ baseline, sup   │ 10
2   │ 4002 │ Place unit fraction (scaffolded)     │ create   │ confidence      │ 4
3   │ 4003 │ Place non-unit fraction on 0-1 line  │ create   │ baseline, str   │ 12
4   │ 4004 │ Place non-unit fraction (scaffolded) │ create   │ support         │ 5
5   │ 4005 │ Place fraction beyond 1 on 0-2 line  │ create   │ baseline, str   │ 6
6   │ 4006 │ Place beyond 1 (scaffolded)          │ create   │ support         │ 3
7   │ 4007 │ Count intervals to find denominator  │ identify │ baseline, str   │ 8
8   │ 4008 │ Count intervals (simple denominators)│ identify │ confidence      │ 3
9   │ 4009 │ Identify fraction from placed point  │ identify │ baseline, str   │ 6
10  │ 4010 │ Identify fraction (beyond 1)         │ identify │ baseline        │ 4
11  │ 4011 │ Compare lines by fraction type       │ compare  │ baseline, str   │ 5
12  │ 4012 │ Find fraction on ruler               │ apply    │ baseline, str   │ 4
────┴──────┴──────────────────────────────────────┴──────────┴─────────────────┴─────────
                                                                         TOTAL │ 70

═══════════════════════════════════════════════════════════════
```

---

#### **Artifact 4: Templates (JSON)**

Complete template specifications in JSON format using the teacher review schema.

Templates are presented in a dual-format structure optimized for teacher review while preserving JSON for the pipeline.

**Format Structure:**

Each template includes:

1. **Human-readable section** with color-coded key fields
2. **JSON block** containing the complete template specification

**Color Key for Teacher Review:**

* 🟢 **Green** \= SKILL (what the student demonstrates)
* 🔵 **Blue** \= PROBLEM TYPE (what the student does)
* 🟠 **Orange** \= PROMPT EXAMPLES (what Helper says)
* 🟣 **Purple** \= SUCCESS DIALOGUE (feedback on correct answer)

**Teacher Review Focus:** Teachers review the colored sections for pedagogical accuracy, age-appropriateness, and voice quality. The JSON travels intact to the next pipeline step.

**Example template (dual format):**

---

**Template 4001 — Place Unit Fraction on 0-1 Line**

**SKILL** *(highlight green)* Student can place unit fractions on 0-1 number line by counting intervals from zero

**PROBLEM TYPE** *(highlight blue)* Student clicks tick mark to place unit fraction on pre-partitioned 0-1 number line

**PROMPT EXAMPLES** *(highlight orange)*

* "Place one-third on the number line."
* "Find 1/4. Click its position."
* "Where is one-fifth? Place a point there."

**SUCCESS DIALOGUE** *(highlight purple)*

* "One-third. One interval from zero."
* "That's 1/4. Got it."
* "Right—one-fifth."

**Technical Details (JSON)**

```json
[
  {
    "template_id": "4001",
    "skill": "Student can place unit fractions on 0-1 number line by counting intervals from zero",
    "problem_type": "Student clicks tick mark to place unit fraction on pre-partitioned 0-1 number line",
    "workspace_description": "Horizontal number line from 0 to 1 with tick marks pre-placed at all fraction positions for the given denominator. Only 0 and 1 are labeled.",
    "prompt_examples": [
      "Place one-third on the number line.",
      "Find 1/4. Click its position.",
      "Where is one-fifth? Place a point there."
    ],
    "action_description": "Student clicks a tick mark to place a point at that position",
    "mastery_tier": ["support", "baseline"],
    "mastery_verb": "create",
    "parameter_coverage": {
      "fractions": ["1/2", "1/3", "1/4", "1/5", "1/6", "1/8"]
    },
    "correct_end_state": "Point placed at the correct tick mark position corresponding to the target fraction",
    "success_dialogue": [
      "One-third. One interval from zero.",
      "That's 1/4. Got it.",
      "Right—one-fifth."
    ]
  },
  {
    "template_id": "4002",
    "skill": "Student can place non-unit fractions on 0-1 number line by counting intervals from zero",
    "problem_type": "Student clicks tick mark to place non-unit fraction on pre-partitioned 0-1 number line",
    "workspace_description": "Horizontal number line from 0 to 1 with tick marks pre-placed at all fraction positions for the given denominator. Only 0 and 1 are labeled.",
    "prompt_examples": [
      "Place three-fourths on the number line.",
      "Find 2/3. Click its position.",
      "Where is five-sixths? Place a point there."
    ],
    "action_description": "Student clicks a tick mark to place a point at that position",
    "mastery_tier": ["baseline", "stretch"],
    "mastery_verb": "create",
    "parameter_coverage": {
      "fractions": ["2/3", "3/4", "2/4", "3/5", "3/6", "5/6", "3/8"]
    },
    "correct_end_state": "Point placed at the correct tick mark position corresponding to the target fraction",
    "success_dialogue": [
      "Three-fourths. Three intervals from zero.",
      "That's 2/3.",
      "Right—five spaces from zero."
    ]
  }
]
```

---

#### **Artifact 5: Coverage Summary (Teacher Review)**

Human-readable validation report. See existing Coverage Summary format in Section 7—no changes needed to this artifact structure.

---

#### **Post-Review: Schema Expansion**

After teachers approve templates, a separate pipeline step expands the teacher review schema into the full engineering specification. This expansion adds:

| Added Field | Source |
| :---- | :---- |
| `workspace_detailed` | Expanded from `workspace_description` \+ tool conventions |
| `action_list` | Parsed from `action_description` |
| `mastery_component` | Inferred from `mastery_verb` |
| `misconceptions_targeted` | Assigned from `problem_type` patterns \+ Starter Pack |
| `remediation_approach` | Generated via Remediation Addition Protocol |
| `tier_constraints` | Created based on `mastery_tier` \+ scaffolding conventions |
| `target_count` | Determined during pool composition step |
| `skill_id` | Generated to link skill text to Goal Decomposition |

The expanded schema feeds into problem generation and remediation pipelines. Teachers review only the lean schema; engineering details are extrapolated automatically.

**Teacher Review Questions:**

- Are any required fractions missing?
- Is tier distribution appropriate for this module?
- Are all misconceptions adequately covered?
- Which options should we pursue for the flagged gaps?

---

### **Teacher Review Workflow**

1. **Review Lesson Analysis** — confirm constraints are correct
2. **Review Goal Decomposition** — approve skill breakdown and lesson alignments
3. **Review Template Summary** — check problem types and counts
4. **Review Coverage Summary** — verify requirements met, decide on gaps
5. **Spot-check Templates** — review 2-3 templates for quality
6. **Approve or Request Changes**

Teachers do NOT need to review every template field. The summary artifacts surface any issues.

---

## **8\. QUICK REFERENCE**

### **Template ID Format**

`"XXXX"` — first digit(s) \= module, remaining \= sequence

### **Required Template Fields (Teacher Review Schema)**

1. `template_id`
2. `skill`
3. `problem_type`
4. `workspace_description`
5. `prompt_examples`
6. `action_description`
7. `mastery_tier`
8. `mastery_verb`
9. `parameter_coverage`
10. `correct_end_state`
11. `success_dialogue`

### **Enum Values (all lowercase)**

**mastery\_tier:** `confidence`, `support`, `baseline`, `stretch`, `challenge`

**mastery\_verb:** `create`, `identify`, `compare`, `apply`, `analyze`, `evaluate`

### **Verb to Component Mapping (for expansion)**

| Verb | Primary Component |
| :---- | :---- |
| `create` | `procedural` |
| `identify` | `conceptual` |
| `compare` | `conceptual` or `transfer` |
| `apply` | `transfer` |
| `analyze` | `conceptual` |
| `evaluate` | `transfer` |

### **Common Action Descriptions**

- "Student clicks a tick mark to place a point at that position"
- "Student selects the correct option"
- "Student taps cells to shade them"
- "Student drags the marker to the correct position"
- "Student clicks to partition the shape"

### **Pool Targets by Module Stage**

| Stage | Modules | Target |
| :---- | :---- | :---- |
| Early | 1-4 | 55-65 |
| Mid | 5-8 | 60-75 |
| Late | 9-12 | 65-80 |
