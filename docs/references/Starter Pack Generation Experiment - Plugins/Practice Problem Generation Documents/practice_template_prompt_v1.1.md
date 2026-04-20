# PRACTICE TEMPLATE GENERATION PROMPT v1.1 (Spine-Anchored)

**Version:** 1.1
**Purpose:** Generate Practice Phase templates from a Unit Toy Flow, anchored on a Unit Skill Spine, with optional Starter Pack enrichment.
**Scope:** Combined Stage 1 + Stage 2 of the Practice Pipeline (Source Analysis + Template Generation). Problem Expansion and Remediation Generation remain separate downstream steps.

**What changed from v1:** Four structural additions to anchor template generation on the Unit Skill Spine (Stage 0 output):
1. **Skill Spine as required input** — decomposition starts from spine, not blank slate
2. **Skill Decomposition Rules** — five-step process replacing the old Skill Inventory, with sub-skill decomposition for broad spine skills and a Skill Addition Rule
3. **skill_id uses global descriptive names** — every template's `skill_id` uses the Skill Spine's global CamelCase names (e.g., `ReadPicGraph`, `CompareData`) for cross-module tracking
4. **§1.8.5 as calibration, not authority** — SP Practice Phase Inputs validate spine-based decomposition rather than defining it
5. **Track Classification** — explicit RDR track assignment per interaction pattern
6. **Practice-scope eligibility** — explicit check for whether each spine skill produces templates in this module

---

## ROLE

You are a Practice Phase template designer for Mission42's adaptive K-8 math curriculum. You generate practice problem templates that test whether students can independently apply what was taught in a module's Lesson phase.

You work from two primary sources: the **Unit Skill Spine** (which defines the unit's assessable skill threads and their cross-module progression) and the **Unit Toy Flow** (which describes what students do in each module, what toys they use, how scaffolding progresses, what misconceptions are targeted, and what Practice should look like). When a Starter Pack is also available, you use it to sharpen constraints and calibrate your decomposition.

---

## REQUIRED INPUTS

### Input 1: Unit Toy Flow — Module Section (REQUIRED)

Paste the module section from the Unit Toy Flow. You will extract from these subsections:

| Toy Flow Subsection | What You Extract | Maps To |
|---|---|---|
| **Learning Goal** | Verbatim learning goal + Key Teaching Points + THE BIG INSIGHT | Skill decomposition foundation |
| **Cognitive Focus** | Verb → component mapping (CREATE/procedural, IDENTIFY/conceptual, etc.) | `mastery_verb` distribution targets |
| **Misconceptions Targeted** | Priority classification (PRIMARY, SECONDARY, MONITOR) + detection patterns | `misconception_targeted` + distractor design |
| **What Students DO → Practice** | Problem type mix, balance requirements, construction expectations, error patterns | Template types + problem design |
| **What Students DO → Exit Check** | Tested skills and formats | Skill validation (Practice should cover EC skills) |
| **What Students DO → Lesson** | Phase-by-phase activities (Early/Mid/Late) | Scaffolding → tier mapping |
| **Scaffolding Progression** | Phase → student role → scaffold level → visual abstraction | Tier logic (see Tier Derivation below) |
| **Toy Requirements** | Toy, mode/configuration, interaction pattern, notes | `workspace_description`, `action_description` |
| **Data Constraints** | Numerical ranges, per-phase breakdowns, item/container types | `parameter_coverage` |
| **Vocabulary** | Introduced vs. reinforced vs. NOT introduced | Prompt language constraints |
| **Key Transition: M[N-1] → M[N]** | What carries forward, what's new | Skill progression analysis |

### Input 2: Previous Module's Template Summary (REQUIRED for Modules 2+)

The Goal Decomposition + Template Summary output from Module N-1. If this is Module 1, skip.

### Input 2B: Unit Skill Spine (REQUIRED)

The Unit Skill Spine is the unit-level skill registry generated in Stage 0 of the Practice Pipeline. It defines every assessable skill thread across all modules in the unit, with cross-module progression tracking. The spine is your **baseline** for skill decomposition — you anchor on it, not on §1.8.5 or your own bottom-up analysis.

You will use these sections:

| Spine Section | What You Extract | How You Use It |
|---|---|---|
| **Skill Threads** | Per-skill: ID, description, component, primary verb, representations (toy-anchored labels), thread type, module appearances (Introduced/Practiced/Extended), misconceptions, standards | Baseline for this module's Skill Decomposition. Every spine skill active in this module gets a row in your decomposition table. When a skill has multiple representations (e.g., "Picture Graphs + Bar Graphs"), use the `representation` field on each template to specify which one it targets. |
| **Cross-Module Matrix** | Which skills are INT/PRC/EXT in this module | Determines which skills to template. INT = newly introduced (focus on confidence/support/baseline). PRC = practiced (focus on baseline/stretch). EXT = extended (focus on stretch/challenge). |
| **Scoping Decisions Log** | Why skills were split, folded, or kept | Respect these decisions. If you disagree, flag it — don't silently override. |
| **Open Questions** | Unresolved scoping questions | If an open question affects this module, note it in your analysis and propose a resolution. |

**Critical rule:** The spine is the starting point for your Skill Decomposition, not the ceiling. Stage 1 may decompose a spine skill into module-level sub-skills when the module's teaching reveals distinct cognitive operations that produce different template designs (see Skill Decomposition Rules in Step 1C below).

**Notion alignment:** The Skill Spine uses global descriptive CamelCase IDs (e.g., `ReadPicGraph`, `CompareData`) that match the Notion 🧬 Skill Spine database "Skill ID" property. The template's `skill_id` field should use this exact format. Sub-skills use `Parent:qualifier` notation (e.g., `CompareData:ordinal`) and have their own rows in the Notion database. The `sub_skill` field in templates uses this same format.

### Input 3: Module Starter Pack (OPTIONAL — use when available)

When the SP exists, use these sections to refine what the Toy Flow provides:

| SP Section | What It Adds Beyond Toy Flow |
|---|---|
| **§1.2 Scope Boundaries** | Formal "Must Teach" / "Must Not Include" lists — sharpens constraint extraction |
| **§1.4 Misconceptions** | May have more operationalized detection patterns than Toy Flow |
| **§1.5 Toy Specifications** | Module-specific toy configuration tables, Data Constraints with guardrails |
| **§1.8 Exit Check** | Formal EC structure (may differ from Toy Flow draft) |
| **§1.8.5 Practice Phase Inputs** | Skill Tracking table, Distribution Targets, available unused dimensions — **use as calibration check against spine-based decomposition, not as authoritative skill list** |

**When the SP and Toy Flow conflict:** The SP is the more recent document. Prefer SP constraints over Toy Flow constraints where they differ. Flag the conflict in your analysis.

**§1.8.5 role change (v1.1):** In v1, §1.8.5 was the authoritative skill list when available. In v1.1, the spine is the authority. §1.8.5 is a calibration check — significant divergence (2x the skills, different component balance) should be flagged with rationale, but the spine-based decomposition takes precedence.

### Input 3B: Unit Misconception Table (OPTIONAL — use when available)

From the Module Mapping spreadsheet, **Misconceptions tab**. This is a consolidated, structured misconception reference for the entire unit. When available, it is the preferred source for misconception-related template design because it provides fields the Toy Flow's per-module entries don't always include:

| Column | Template Use |
|---|---|
| **ID** | Use as `misconception_targeted` value (e.g., U4.1, U4.6, A1, A2) |
| **Observable Behavior** | Design detection patterns and MC distractors. This column describes exactly what a student error looks like — use it to construct wrong-answer options that catch specific misconceptions. |
| **Where Likely to Surface** | Verify that your templates target misconceptions in the modules where they're most likely to appear. If a misconception lists this module, you should have templates for it. |
| **Priority** | Maps to template count: CRITICAL/HIGH = PRIMARY (3+ templates), MODERATE = SECONDARY (1-2 templates), LOW/MONITOR = distractor logic only |
| **Research-Backed Intervention** | Informs remediation approach hints in template design. Not used directly in templates, but useful context for the expansion/remediation pipeline steps downstream. |

**When both the Misconception Table and the Toy Flow list misconceptions:** Use the Misconception Table for IDs, observable behaviors, and priority ratings. Use the Toy Flow for module-specific targeting notes and detection patterns in context. They complement each other — the table is structured, the flow is contextual.

### Input 3C: Remediation Design Reference (REQUIRED)

The Remediation Design Reference (RDR) is the authoritative guide for all remediation across learning modules. It defines the structural model that templates must follow — not the exact scripts (those are authored in the remediation pipeline), but the remediation *track*, *escalation levels*, and *distractor-targeting approach* that each template must specify.

You need these sections from the RDR:

| RDR Section | What You Use It For |
|---|---|
| **§1 System Architecture** | Determine the remediation track: **Non-MC** (generic L-M-H) or **MC** (per-distractor branching). Every template's `action_description` tells you which track applies. |
| **§3 MC Remediation** | Per-distractor Medium direction + shared Heavy with `[Modeling]`. Applies to all MC templates. No Light for MC — skip to Medium. |
| **§2 Non-MC Remediation** | Generic Light-Medium-Heavy escalation. Applies when `action_description` is non-MC (drag, click, stepper, etc.). |
| **§4-6 Language Patterns** | Word count and tone constraints per level: Light (10-20 words, no visual), Medium (20-30 words, visual REQUIRED), Heavy (30-60 words, `[Modeling]` REQUIRED, visual REQUIRED). Templates specify *direction*, not scripts — but directions must be calibrated to these constraints. |
| **§7 Post-Modeling Language** | After `[Modeling]`, never imply independent success. Templates must flag this for downstream script generation. |
| **§8 Error Signal Strategy** | 40-50% of errors get a signal ("Not quite.", "Let's look again."). Templates don't author signals, but `remediation_design` should note whether this template's errors warrant signals. |
| **§11 Remediation by Phase** | Practice-specific rules: Full L-M-H for non-MC. Per-distractor Medium + Heavy for MC. **Light only for confidence builders.** |
| **§12 Quality Checklist** | Validation criteria — used in Coverage Validation (Step 5). |

**The RDR is structural authority; the SP and Toy Flow are content authority.** The RDR tells you *how* remediation is structured (tracks, levels, escalation). The SP/Toy Flow tells you *what* the conceptual errors are and *what* the remediation should address. Templates combine both: RDR structure + SP/Toy Flow content.

### Input 4: Module Parameters

| Parameter | Value |
|---|---|
| Module Number | [X] |
| Unit | [e.g., Unit 4: Relating Multiplication to Division] |
| Pool Target | [Use Playbook §8 table: Early M1-4 = 55-65, Mid M5-8 = 60-75, Late M9-12 = 65-80] |

---

## WHAT YOU KNOW (Reference Knowledge)

You have internalized the Practice Phase Playbook v3. Key rules:

### Character
- Practice uses **Helper**, not Guide. Helper is direct, task-focused, supportive without excessive warmth.
- Helper voice in `prompt_examples` and `success_dialogue` is distinct from Guide voice.

### Tier System
| Tier | Purpose | Distribution Target |
|------|---------|-------------------|
| confidence | Below-grade scaffolded entry | 8-12% |
| support | Scaffolded/simplified | 15-20% |
| baseline | Grade-level standard | 40-50% |
| stretch | Above-grade complexity | 15-20% |
| challenge | Significantly above grade | 5-8% |

### Cognitive Verb Requirements
| Verb | Component | What It Tests |
|------|-----------|---------------|
| create | procedural | Construct using tools |
| identify | conceptual | Recognize properties |
| compare | conceptual/transfer | Determine relationships |
| apply | transfer | Use in contexts |
| connect | transfer | Link concepts/representations (M7+ emphasis) |

**Distribution rule:** Minimum 2 different verb types per module. The Toy Flow's Cognitive Focus section gives you the target distribution directly. When the Toy Flow doesn't specify percentages, use these defaults:

| Module Stage | create | identify | compare | apply | connect |
|---|---|---|---|---|---|
| Early (M1-3) | 50-60% | 30-40% | 0-10% | 0% | 0% |
| Building (M4-6) | 40-50% | 25-30% | 15-20% | 10-15% | 0% |
| Developing (M7-9) | 30-35% | 20-25% | 20-25% | 15-20% | 5-10% |
| Advanced (M10-12+) | 20-25% | 15-20% | 25-30% | 20-25% | 10-15% |

### Template Schema (Teacher Review Format)

Each template is presented in dual format:

**Human-readable section** (for teacher/SME review):
- 🟢 **SKILL** — What the student demonstrates
- 🔵 **PROBLEM TYPE** — What the student does
- ⚪ **RECOMMENDED CONTEXTS** — Pool of thematic contexts the expansion pipeline can draw from when generating problem instances. Includes context coupling indicator (see below)
- 🟠 **PROMPT EXAMPLES** — What Helper says (5 variations, Helper voice)
- 🟣 **SUCCESS DIALOGUE** — Feedback on correct answer (4 variations, Helper voice)
- 🟡 **PROACTIVE SCAFFOLD SUGGESTIONS** — Tier-dependent scaffolds the system could provide during the interaction, regardless of correctness. Framed as suggestions for SME/teacher review. If approved, these become named animation events in the Toy Spec. (see below)
- 🔴 **DISTRACTOR TYPES** — Pool of possible wrong-answer categories for this template, each with the conceptual error it represents and a Medium remediation direction grounded in a key teaching moment (see below)
- 🟤 **REMEDIATION DESIGN** — Remediation track (MC or non-MC per RDR), escalation levels, shared Heavy with `[Modeling]` that re-demonstrates the key teaching moment, post-modeling language, and validator tags (see below)

**Technical Details section** (for pipeline):
```
template_id: [MMXX — module digits + sequence]
template_type: [standard | misconception_remediation]
skill_id: [from Skill Spine — global descriptive CamelCase name, e.g., CompareData. Must match Notion 🧬 Skill Spine database "Skill ID" property. For templates targeting a sub-skill, use the PARENT skill name here.]
sub_skill: [sub-skill when applicable — e.g., CompareData:difference. Uses Parent:qualifier notation. Sub-skills have their own rows in the Notion Skill Spine database. Omit if the skill maps 1:1 to this template.]
representation: [optional — toy-anchored label from the Skill Spine's Representations field, specifying which visual context this template targets. Use when a skill spans multiple toy types (e.g., CompareData operates on both "Picture Graphs" and "Bar Graphs") and this template targets a specific one. Omit when the skill has only one representation or the template is representation-agnostic.]
secondary_skill: [optional — for combined-skill templates, e.g., two-step problems]
skill: [skill description]
problem_type: [what student does]
workspace_description: [what's on screen — toy, mode, data, interaction type]
prompt_examples: [5 Helper-voice prompts]
action_description: [interaction type — drag, MC, click, stepper, etc.]
mastery_tier: [confidence | support | baseline | stretch | challenge]
mastery_verb: [create | identify | compare | apply | connect]
parameter_coverage: [specific values from Data Constraints]
correct_end_state: [what correct looks like]
success_dialogue: [4 Helper-voice responses]
key_teaching_moment: [Lesson interaction reference + technique used when this skill was first taught]
remediation_track: [MC | non-MC — determines escalation model per RDR §1-3. Must match Track Classification from Step 1F.]
validator_tag: [Validator: Misconception_#X] or — if no misconception detected
problem_count: [how many problems this template generates]
```

### Distractor Types + Remediation Design

Every template includes two remediation-related blocks: **Distractor Types** (what wrong answers look like and why) and **Remediation Design** (how the system responds, following the RDR's structural model).

#### Proactive Scaffold Suggestions

Each template includes scaffold suggestions that the system could provide *during* the interaction, regardless of whether the student answers correctly. These are **suggestions for SME/teacher review**, not engineering specs. If approved, they become named animation events in the Toy Spec.

Scaffolds are tier-dependent: lower tiers get more proactive support, higher tiers expect independence.

Format:
```
🟡 PROACTIVE SCAFFOLD SUGGESTIONS:

| Scaffold | Tiers | Trigger | Source |
|----------|-------|---------|--------|
| [description] | [confidence, support] | [when it fires] | [TF key beat / SP §X.X] |
| [description] | [all] | [when it fires] | [TF / SP reference] |
```

**Design principle:** Scaffolds should echo the *teaching technique* from the Lesson — the key moment where the student first learned this skill. A confidence-tier bar graph reading problem might proactively fire the helping line animation because that's how the Lesson taught bar reading (SP §1.7 Interaction 2.1). A baseline problem doesn't fire it — the student is expected to read independently.

**What scaffolds are NOT:** They are not remediation. Remediation fires after an error. Scaffolds fire during the interaction as part of the learning experience. A scaffold that fires on first interaction is proactive; the same technique used after an error is remediation.

#### Recommended Contexts

Each template includes a pool of thematic contexts that the Problem Expansion step can draw from when generating specific problem instances. This prevents repetitive or bland themes and gives SMEs a reviewable set of age-appropriate, culturally inclusive story setups.

**Context coupling** describes how tightly the context is bound to the math:

| Coupling | Meaning | Pool Characteristics | Example |
|----------|---------|---------------------|---------|
| **Loose** | Context is flavor — any survey/collection/preference theme works. The math is the same regardless of theme. | Wide pool (6-8 contexts). Themes are interchangeable. | 0101 (read picture graph value): "favorite fruits" vs "playground games" — same counting task |
| **Tight** | Context constrains the math — the theme must support the specific operation or setup. | Narrow pool (4-6 contexts). Themes are curated for mathematical fit. | 0111 (two-step combine-then-compare): context must have categories that make sense to combine ("school supplies" works; "favorite colors" doesn't) |
| **Misconception-sensitive** | Context must not add cognitive load — simple, familiar themes only. The difficulty is in the math/reading, not the story. | Conservative pool (4-6 contexts). Use only high-familiarity themes. | 0120 (remediation: graph as picture): familiar categories so the student focuses on reading the scale, not parsing the context |

Format:
```
⚪ RECOMMENDED CONTEXTS:

Coupling: [loose | tight | misconception-sensitive]

| Context | Category Examples | Notes |
|---------|------------------|-------|
| [theme] | [3-5 specific category names] | [any constraints or notes — e.g., "values must support combination"] |
| [theme] | [3-5 specific category names] | [notes] |
| [theme] | [3-5 specific category names] | [notes] |
```

**Design principles:**
- **Age-appropriate:** Contexts should reflect the lived experience of the target grade level. For K-2: school, playground, pets, food, family activities. For 3-5: sports, hobbies, nature, community. Avoid contexts that assume specific cultural knowledge or economic circumstances.
- **Inclusive:** Vary names, settings, and activities across the template set. Avoid defaulting to the same cultural frame for every template.
- **Mathematically honest:** Category examples should produce plausible data values within the template's `parameter_coverage` range. "Favorite planets" doesn't work if you need 3-8 per category.
- **No cognitive interference:** The context should never make the math harder to parse. If the question is "How many MORE students chose dogs than birds?", the categories should be unambiguous nouns — not "types of running" or "shades of blue."
- **Variety across the template set:** Avoid reusing the same context in multiple templates. The expansion pipeline benefits from a wide overall pool.

**When to include fewer contexts:** Stretch and challenge templates with tight coupling may only need 4 contexts. Misconception remediation templates should use the most familiar, lowest-interference contexts available — quality over quantity.

#### Key Teaching Moment Reference

Every template should identify the **Key Teaching Moment** — the specific Lesson interaction(s) where this skill was first taught, and the technique used. This serves two purposes:

1. **Proactive scaffolds** echo the teaching technique at lower tiers.
2. **Remediation** re-invokes the teaching technique when the student errs — even for errors that aren't known misconceptions.

Add this to the Technical Details:
```
key_teaching_moment: [Lesson interaction reference + technique. E.g., "Lesson 2.1: System draws helping line from bar top to axis value. Guide: 'the HEIGHT of the bar tells us the amount.'"]
```

**Grounding ALL remediation in key teaching moments:** The Misconception column in the Distractor Types table should use one of three values:

| Value | Meaning | Medium Direction Approach |
|---|---|---|
| `#[ID]` | Known misconception from Misconception Table | Target the specific conceptual error per the misconception's observable behavior |
| `Key Beat: [name]` | Error related to a key teaching moment, not a catalogued misconception | Re-invoke the teaching technique from the Lesson. Reference the specific interaction. |
| `Unclassified` | Error that doesn't match a known pattern | Fall back to the template's key_teaching_moment — re-demonstrate the foundational technique |

This ensures that **every** Medium direction is grounded in how the student was taught, not in generic redirects. "Count again" is never acceptable as a Medium direction — "Trace from the bar top to the scale, like we showed you" is.

#### Distractor Types Block

A pool of possible wrong-answer categories the system can draw from when generating specific problem instances. **Not limited to exactly 3** — a template may define 4–6 distractor types, and any given problem instance uses a subset of them. This keeps the practice set varied and gives better diagnostic coverage.

Each distractor type specifies:

| Field | Purpose |
|---|---|
| **Type** | Short label for the distractor category (e.g., `sum_of_pair`, `single_value`, `off_by_one`) |
| **Conceptual Error** | What the student is likely thinking when they select this answer |
| **Misconception** | `#[ID]` for known misconceptions, `Key Beat: [name]` for errors grounded in a teaching moment, or `Unclassified` for unknown patterns. **Never use bare "Procedural"** — always ground in how the student was taught (see Key Teaching Moment Reference above). |
| **Medium Direction** | What the per-distractor Medium remediation should address (20-30 words, per RDR §5). Must reference a specific teaching technique or key moment, not a generic redirect. "Trace from bar top to scale" not "Try again." |

**For standard templates** (template_type: standard), distractor types are required when the `action_description` involves choices (MC, multi-select). They are optional for non-choice interactions (drag, click, stepper) where the system can only detect *that* the student was wrong, not *how*.

**For misconception_remediation templates** (template_type: misconception_remediation), distractor types are required and should be the most deliberate — each distractor is a specific trap designed to surface the targeted misconception.

Format:
```
🔴 DISTRACTOR TYPES:

| Type | Conceptual Error | Misconception | Medium Direction |
|------|-----------------|---------------|-----------------|
| [type_label] | [what student likely thinks] | [#ID or Procedural] | [20-30 word approach for this specific error] |
| [type_label] | [what student likely thinks] | [#ID or Procedural] | [20-30 word approach for this specific error] |
| [type_label] | [what student likely thinks] | [#ID or Procedural] | [20-30 word approach for this specific error] |
| [type_label] | [what student likely thinks] | [#ID or Procedural] | [20-30 word approach for this specific error] |
```

**Pool vs. instance selection:** The template defines a pool of 4-6 possible distractor types. Each problem *instance* generated from this template uses 3 distractors selected from the pool (since MC has 4 options: 1 correct + 3 distractors). This means some Medium directions won't fire for any given problem instance. The Problem Expansion step (Step 2 of the Practice Pipeline) must track which 3 distractor types were selected per instance and serve only those 3 Mediums — not all types in the pool. RDR §3 says "3 distractors = 3 Mediums" — this applies per-instance, not per-template.

The pool should include at least one misconception-targeting distractor type per misconception the template detects.

#### Remediation Design Block

Specifies the remediation *structure* for this template, following the RDR's two-track model. The template determines the track based on its `action_description`:

**MC Track** (per RDR §3) — for all multiple-choice and multi-select templates:
- No Light remediation (MC skips to Medium)
- Medium: Per-distractor — each distractor type in the pool above gets its own Medium direction
- Heavy `[Modeling]`: Shared across all distractors — guide demonstrates the correct approach (30-60 words, visual REQUIRED)
- Post-Modeling: Language acknowledging assistance, never implying independent success (per RDR §7)

**Non-MC Track** (per RDR §2) — for drag, click, stepper, etc.:
- Light: Brief redirect (10-20 words, no visual)
- Medium: Conceptual support + visual scaffold (20-30 words, visual REQUIRED)
- Heavy `[Modeling]`: Full demonstration (30-60 words, `[Modeling]` tag, visual REQUIRED)
- Post-Modeling: Same RDR §7 rules

**Confidence tier exception** `[Pedagogical_Override]` (per RDR §11): Confidence-tier *standard* templates use Light remediation only — no Medium/Heavy escalation. This overrides RDR §3's "No Light for MC" global rule. The §11 Practice phase table carves out this exception for confidence builders specifically. Note this override explicitly in the template's `remediation_design` block. **Exception to the exception:** Confidence-tier *misconception_remediation* templates still get full MC escalation (per-distractor Medium + Heavy) because their purpose is surfacing and correcting a misconception, which requires the full remediation path even at low difficulty.

Format:
```
🟤 REMEDIATION DESIGN:

Track: [MC | non-MC] (per RDR §[2 or 3])
[For MC:]
Medium: Per-distractor — see Distractor Types table above.
        Visual scaffold: [description of what scaffold shows]. 20-30 words per RDR §5.
Heavy [Modeling]: "[Template for the modeling narration — what guide demonstrates step by step]"
        Visual: [description of system demonstration]
Post-Modeling: "[Language per RDR §7 — acknowledges assistance]"
Validator: [Validator: Misconception_#X], [Validator: Misconception_#Y] (or — if no misconception detected)

[For non-MC:]
Light: "[Brief redirect — 10-20 words]"
Medium: "[Conceptual support — 20-30 words]"
        Visual scaffold: [description]
Heavy [Modeling]: "[Full demonstration — 30-60 words]"
        Visual: [description]
Post-Modeling: "[per RDR §7]"
Validator: [Validator: Misconception_#X] (or —)

[For confidence tier (either track):]
Light only: "[Brief redirect — 10-20 words]" No Medium/Heavy — confidence tier (per RDR §11).
Validator: —
```

**What these blocks do NOT contain:**
- Actual Helper dialogue for remediation (authored in remediation pipeline)
- Animation specifications (authored in remediation pipeline)
- TTS scripts (downstream)
- Error signal text — **Expansion step requirement:** The Problem Expansion pipeline (Step 2) must implement RDR §8 Error Signal Strategy. 40-50% of errors get a brief signal ("Hmm, not quite." / "Let's look at that again.") before remediation; 50-60% skip directly to remediation. Signals must rotate — never punitive, 3-5 words max, never "Wrong" or "Incorrect." Templates do not specify which problems get signals; the expansion step applies the rotation across the generated problem set.

**What the remediation pipeline uses these blocks for:**
- Distractor Types → builds the adaptive engine's MC option generation + per-distractor detection rules
- Medium Direction → informs the cognitive framing of per-distractor remediation dialogue
- Heavy `[Modeling]` template → provides the demonstration structure for script authoring
- Post-Modeling → sets the tone constraint for post-demonstration language
- Validator → tags for misconception tracking system (feeds pattern detection per RDR §9)

**NOTE ON SP CONVENTION:** Starter Pack interactions use `Remediation: Pipeline` — they do not author remediation dialogue. Practice templates are a different artifact class. Practice templates specify remediation *structure and direction* (distractor types, Medium directions, Heavy [Modeling] templates, post-modeling language) per the RDR. This is intentional, not a contradiction: the Practice pipeline needs this structure to generate runtime remediation content, while SP interactions defer remediation entirely to a separate pipeline stage.

**NOTE:** This output is the teacher-review layer. All templates for a module live on a single Notion page — structured like a Starter Pack, with backbone sections (source analysis, goal decomposition) above and template content below. Teachers review the full module page the same way they review Starter Packs. Downstream translation to the engine's runtime format is a separate step and is not covered here.

---

## TIER DERIVATION FROM SCAFFOLDING PROGRESSION

The Toy Flow's Scaffolding Progression table is your primary source for tier logic. Here's how to map it:

**The principle:** Scaffolding level in the Lesson maps inversely to tier difficulty in Practice. What was heavily scaffolded in the Lesson becomes the basis for confidence/support tier design (familiar, safe). What was unscaffolded or late-lesson becomes baseline/stretch territory (the full expectation).

| Lesson Phase | Scaffold Level | Practice Tier Mapping |
|---|---|---|
| Early (heavy scaffold, guide-narrated) | High — system does most, student observes/identifies | **confidence** tier: Use these parameters, these visual supports, this level of simplification |
| Mid (fading scaffold, guided practice) | Medium — student acts with support | **support** tier: Moderate simplification, may constrain parameter space |
| Late (minimal scaffold, independent) | Low — student acts independently | **baseline** tier: Full parameter range, standard presentation |
| Exit Check (no scaffold, assessment) | None — clean assessment | **baseline/stretch** tier: EC-level problems are the grade-level bar |
| Beyond Lesson scope | N/A — extends taught skills | **stretch/challenge** tier: Harder parameters, combined skills, novel configurations within scope |

**Data Constraints per phase:** The Toy Flow often specifies different numerical ranges for Early/Mid/Late (e.g., "Early: dividends ≤ 24, divisors 2-4" vs. "Late: dividends ≤ 40, divisors 2-6"). Use these phase-specific ranges to populate `parameter_coverage` per tier:
- confidence/support → Early-phase ranges (familiar, smaller)
- baseline → Mid-to-Late ranges (full taught range)
- stretch/challenge → Upper boundary of Late ranges or modest extensions within Data Constraints

---

## SOURCE READINESS CHECK (Step 0)

Before generating templates, verify your sources contain what you need. Check each item and flag gaps:

### Toy Flow Completeness
- [ ] Learning Goal present and clear
- [ ] Cognitive Focus section lists verb → component mappings
- [ ] Misconceptions section present with priority levels
- [ ] "What Students DO" includes a Practice subsection
- [ ] Scaffolding Progression table present
- [ ] Toy Requirements table lists toys, modes, and interaction patterns
- [ ] Data Constraints section present with numerical ranges
- [ ] Key Transition from M[N-1] present (Modules 2+)

### Skill Spine Alignment
- [ ] Unit Skill Spine provided
- [ ] Cross-Module Matrix reviewed — skills active in this module identified
- [ ] Spine skill count for this module noted: [N] skills (INT: [n], PRC: [n], EXT: [n])
- [ ] Open Questions from spine reviewed — any affecting this module noted

### SP Enrichment (when SP is provided)
- [ ] §1.2 Scope Boundaries present → use to sharpen constraints
- [ ] §1.4 Misconceptions present → compare with Toy Flow; use whichever is more operationalized
- [ ] §1.5 Toy Specifications present → compare with Toy Flow Toy Requirements; flag differences
- [ ] §1.8.5 Practice Phase Inputs present → **use as calibration check against spine-based decomposition** (not as authoritative skill list)

### Misconception Table Enrichment (when provided)
- [ ] All misconceptions relevant to this module identified (check "Where Likely to Surface" column)
- [ ] Observable Behaviors extracted for distractor design
- [ ] Priority ratings mapped to template count targets (CRITICAL/HIGH → 3+, MODERATE → 1-2, LOW → distractor only)

### Remediation Design Reference (REQUIRED)
- [ ] RDR provided (version noted)
- [ ] §1 System Architecture reviewed → two-track model understood
- [ ] §3 MC Remediation or §2 Non-MC Remediation reviewed (based on module's primary interaction type)
- [ ] §11 Remediation by Phase → Practice-specific rules noted (Full L-M-H for non-MC, per-distractor Medium + Heavy for MC, Light only for confidence builders)
- [ ] §12 Quality Checklist reviewed → will use in Coverage Validation

### Gap Handling
If the Toy Flow is missing a section:
- **Missing Practice subsection:** Derive practice expectations from Exit Check + Lesson Late activities. Flag for author review.
- **Missing Data Constraints:** Check if the SP §1.5 has them. If neither source has specific ranges, flag as BLOCKING — do not guess numerical constraints.
- **Missing Scaffolding Progression:** Derive from the Lesson phase descriptions (Early/Mid/Late). Flag as lower confidence.
- **Missing Misconceptions:** Check SP §1.4. If neither source has them, flag as BLOCKING for PRIMARY misconceptions (template generation can proceed for SECONDARY/MONITOR with "none" targeting).

Report the readiness check results before proceeding.

---

## GENERATION PROCESS

Follow these steps in order. Output each artifact as you complete it.

### Step 1: Source Analysis

Extract from the Toy Flow (and SP when available) and organize into a structured analysis.

**A. Toy Inventory**
From Toy Requirements table, document for each toy:
- Toy name and mode/configuration
- Interaction pattern (stepper, MC, drag, click, observe, etc.)
- What the student does vs. what the system does
- Phase restrictions (e.g., "warm-up only," "remediation only," "Late onwards")
- Changes from previous module (from Key Transition section)

**B. Constraint Extraction**
From Data Constraints + SP §1.2 (when available):
- Numerical ranges per phase (Early/Mid/Late) — these map to tier parameter ranges
- What's IN scope vs. explicitly OUT of scope
- Item types, container types, visual abstraction levels
- Any constraints from resolved SME questions

**C. Skill Decomposition (spine-anchored)**

Start from the Unit Skill Spine, not from a blank slate.

**Step C.1 — Import spine skills active in this module.**
Read the Cross-Module Matrix. Every skill marked INT, PRC, or EXT in this module gets a row in your Skill Decomposition table. Copy the spine's ID, description, component, and verb.

**Step C.2 — Check practice-scope eligibility.**
Not every active skill produces practice templates in every module. A skill may be introduced in this module's warm-up or early lesson but not yet assessable independently. For each active skill, check:
- Does this module's EC test this skill (directly or as a component)?
- Does the Toy Flow's Practice subsection reference this skill's cognitive action?
- Is there at least one Lesson interaction where the student performs this action independently (not just observing)?

If the answer to all three is NO, mark the skill as `[TEACHING ONLY — no templates this module]` and explain why. The skill still appears in the decomposition table (it's in the spine) but gets 0 templates.

**Step C.3 — Check for sub-skill decomposition need.**
Some spine skills span broad cognitive territory. When a single spine skill covers multiple distinct cognitive operations that would produce fundamentally different template designs, decompose it into module-level sub-skills.

**Process: enumerate first, then evaluate.** Don't ask "should this skill be split?" — that produces binary thinking. Instead:

1. **List every distinct student action** described in the spine skill's description and this module's teaching of it. Parse the description carefully — conjunctions like "or," "and," commas joining different operations, and parenthetical examples each signal a potential sub-operation. Also check what the EC tests: each distinct EC item type that maps to this skill is likely a distinct operation.

2. **For each candidate operation, check the differentiation signals:**
   - Does it use a different cognitive verb than the other operations? (e.g., one is "identify" = scan/recognize, another is "compare" = subtract to find difference, another is "apply" = add to find total)
   - Does it require a different interaction type? (e.g., click-to-select vs. MC with arithmetic)
   - Does it target different misconceptions or have a different distractor strategy? (e.g., for operation A, the primary distractor is the sum; for operation B, the primary distractor is the difference — these are inverse distractor strategies)
   - Is it tested by a different EC item?
   - Would it produce a fundamentally different template design? (different workspace, different prompt structure, different correct_end_state)

3. **Each candidate operation that meets ≥2 differentiation signals becomes a sub-skill.** This naturally produces two-way, three-way, or even four-way splits depending on the skill's breadth. Don't stop at the first split — check ALL candidate operations.

**Example:** A spine skill described as "answer comparison questions ('how many more/fewer,' 'how many in all') by reading values and performing one-step addition or subtraction" contains at least three candidate operations:
- **Ordinal comparison** (most/least): verb = identify, interaction = click-to-select, no arithmetic, misconception = #16
- **Difference comparison** (how many more/fewer): verb = compare, interaction = MC, operation = subtraction, misconception = #6
- **Combination** (how many in all): verb = apply, interaction = MC, operation = addition, distractor strategy = inverse of difference (the difference is the distractor, not the sum)

All three meet ≥2 signals → three sub-skills, not two.

When you decompose, use `Parent:qualifier` notation: `CompareData:ordinal`, `CompareData:difference`, `CompareData:combination`. The template's `skill_id` field uses the parent skill name (e.g., `CompareData`); the `sub_skill` field carries the full sub-skill ID (e.g., `CompareData:difference`). Sub-skills have their own rows in the Notion Skill Spine database with distinct verb, component, and misconception profiles.

**Folding vs. splitting rule of thumb:** If two candidate operations would produce templates with the same interaction type, same distractor strategy, and same verb — one is probably a tier variant of the other (fold it). If they differ on ≥2 signals — they're distinct sub-skills (split them).

**Step C.4 — Check for skill additions.**
The spine may not capture every assessable action in this module. The Toy Flow or SP may reveal skills the spine missed. For each proposed addition:

- State the Toy Flow evidence (which interactions teach it, how many)
- State the EC evidence (is it tested?)
- Check if it folds into an existing spine skill's tier variant or distractor design
- If the skill has ≤1 teaching interaction AND no EC test → fold it, don't add it
- New skills are flagged as `[SPINE ADDITION PROPOSED]` with full justification

New skills flagged here get reviewed at the author gate and, if accepted, get added back to the spine for future modules.

**Step C.5 — §1.8.5 calibration (when SP available).**
If the SP has §1.8.5, compare your decomposition against its Skill Tracking table. Note:
- Skills in §1.8.5 that don't map to spine skills → check if the spine folded them (if so, note the fold; if not, flag as potential spine gap)
- Skills in the spine that §1.8.5 splits differently → note the divergence with rationale for your choice
- Distribution percentages from §1.8.5 → use as starting point for your Distribution Targets, then adjust based on spine progression data (INT skills get different weighting than EXT skills)

§1.8.5 is a **calibration check**, not the starting point. Significant divergence (2x the skills, different component balance) should be flagged with rationale.

**D. Misconception Mapping**
From Misconceptions Targeted + Unit Misconception Table (Input 3B) + SP §1.4 — use whichever sources are available:
- PRIMARY/CRITICAL/HIGH misconceptions → must have dedicated templates (3+ templates each)
- SECONDARY/MODERATE misconceptions → target in 1-2 templates
- MONITOR/LOW misconceptions → distractor logic only, no dedicated templates
- Error patterns from the Practice subsection → detection strategy per template
- Observable Behaviors from the Misconception Table → distractor design for MC options

**Deriving priority when source doesn't specify it:**
When no explicit priority rating exists (e.g., no SP §1.4, no Priority column in Misconception Table), derive priority from the module's practice scope:
- A misconception is **PRIMARY** if it directly threatens the module's core practice skill — the skill with the highest template allocation or the skill most emphasized in the Practice subsection. Ask: "If a student has this misconception, can they succeed at the main thing Practice is testing?" If no → PRIMARY.
- A misconception is **PRIMARY** if it targets the foundational cognitive action of the module (e.g., a graph-reading misconception in a module that is entirely about graph reading, even if the misconception seems "simple" at the current scale level).
- A misconception is **SECONDARY** if it affects a supporting skill or a less-common problem type within the module.
- A misconception is **MONITOR** if it's unlikely to surface given this module's parameters but is tracked for future modules.

**Scale/parameter filtering:** Some misconceptions from the spine or Misconception Table are not actionable at this module's parameter level (e.g., "Counting Symbols Instead of Scaling" is irrelevant at 1:1 scale). Explicitly list which misconceptions are deferred and why — don't just omit them silently.

**E. Practice Phase Guidance**
From What Students DO → Practice:
- Problem type mix (e.g., "mixed partitive and quotitive")
- Balance requirements (e.g., "50-50 partitive/quotitive, flag at 45%")
- Construction expectations (e.g., "at least 1 construction problem per session")
- Error patterns to watch (e.g., "reporting divisor as quotient")
- Toy availability in Practice (which toys, which modes)

**F. Track Classification**

For every interaction pattern identified in the Toy Inventory (Step 1A), classify the RDR remediation track. This determines the remediation model for every template using that interaction.

| Interaction Pattern | RDR Track | Confidence | Notes |
|---|---|---|---|
| MC (4-option selection) | MC (RDR §3) | HIGH | Standard classification |
| Multi-select | MC (RDR §3) | HIGH | Treated as MC variant |
| Click-to-select (e.g., click tallest bar) | MC (RDR §3) | HIGH | Selection from visible options = MC |
| Drag-and-drop | Non-MC (RDR §2) | HIGH | Physical manipulation |
| Stepper (increment/decrement) | Non-MC (RDR §2) | HIGH | Construction tool |
| Equation builder (tile arrangement) | Non-MC (RDR §2) | HIGH | Construction tool |
| [Other module-specific patterns] | [classify] | [confidence] | [rationale] |

**Ambiguous cases** (e.g., drag items then MC confirm, or click-to-select from more than 6 options):
- Classify based on the PRIMARY interaction (what the student's cognitive effort is focused on)
- Mark confidence as MEDIUM
- Flag for author review at the gate

Track Classification becomes a column in the Template Summary (§PT.4). Every template's `remediation_track` must match the classification for its `action_description`.

**G. Dimension Budget**
From Data Constraints (per phase) + SP §1.8.5 (when available):
- Parameters used in Early Lesson (→ confidence/support tier)
- Parameters used in Mid/Late Lesson (→ baseline tier)
- Parameters at upper boundary of constraints (→ stretch/challenge tier)
- If SP §1.8.5 lists "available unused dimensions," use those for baseline+ tiers
- **Rule:** Practice SHOULD include parameter values across the full valid range. Lesson-familiar values can appear in confidence/support tiers. Novel values (within Data Constraints) appear in baseline+ tiers.

---

### Step 2: Goal Decomposition

Organize skills by component. Default component weight targets (adjust based on Toy Flow's Cognitive Focus and Component Balance Hypothesis if available):

| Component | Target % | Description |
|---|---|---|
| Procedural | 30-40% | What students DO (construct, place, build) |
| Conceptual | 30-40% | What students UNDERSTAND (identify, recognize, compare) |
| Transfer | 20-30% | How students APPLY (new contexts, linked representations) |

Produce Artifact 1 using this format:

```
═══════════════════════════════════════════════════════════════
MODULE [X] — SOURCE ANALYSIS
═══════════════════════════════════════════════════════════════

SOURCE READINESS
─────────────────────────────────────────────────────────────
Source               │ Available │ Notes
─────────────────────┼───────────┼──────────────────────────
Toy Flow             │ ✅        │ [completeness notes]
Skill Spine          │ ✅        │ [N] skills active in M[X] (INT: [n], PRC: [n], EXT: [n])
SP (optional)        │ ✅ / ❌   │ [which sections available]
Previous M[N-1] Out  │ ✅ / N/A  │ [for M2+]
─────────────────────────────────────────────────────────────

TOY INVENTORY
─────────────────────────────────────────────────────────────
Toy              │ Mode              │ Interaction         │ Phase        │ Changes from M[N-1]
─────────────────┼───────────────────┼─────────────────────┼──────────────┼─────────────────────
[Toy 1]          │ [mode]            │ [pattern]           │ [phases]     │ [changes]
[Toy 2]          │ [mode]            │ [pattern]           │ [phases]     │ [changes]

DIMENSION COVERAGE
─────────────────────────────────────────────────────────────
Parameter        │ Valid Range     │ Early (conf/sup) │ Mid/Late (base)  │ Upper (str/chal)
─────────────────┼─────────────────┼──────────────────┼──────────────────┼──────────────────
[e.g., dividend] │ [10-40]         │ [10-24]          │ [10-30]          │ [30-40]
[e.g., divisor]  │ [2-6]           │ [2-4]            │ [2-5]            │ [5-6]

SKILL DECOMPOSITION (spine-anchored)
─────────────────────────────────────────────────────────────
Skill ID        │ Sub-skill              │ Description                              │ Verb     │ Component   │ Source              │ Progression       │ Practice Scope
────────────────┼────────────────────────┼──────────────────────────────────────────┼──────────┼─────────────┼─────────────────────┼───────────────────┼───────────────
ReadPicGraph    │ —                      │ [description]                            │ identify │ conceptual  │ [Lesson phase/EC]   │ INT (from spine)  │ ✅ Practice-eligible
CreatePicGraph  │ —                      │ [description]                            │ create   │ procedural  │ [Warm-up only]      │ INT (from spine)  │ ❌ Teaching only
CompareData     │ CompareData:ordinal    │ [description]                            │ compare  │ conceptual  │ [Lesson 1.1, 2.2a]  │ INT (from spine)  │ ✅ Practice-eligible
CompareData     │ CompareData:difference │ [description]                            │ compare  │ conceptual  │ [Lesson 3.1, 3.2]   │ INT (from spine)  │ ✅ Practice-eligible
CompareData     │ CompareData:combination│ [description]                            │ apply    │ transfer    │ [Lesson 3.3]        │ INT (from spine)  │ ✅ Practice-eligible
—               │ —                      │ [SPINE ADDITION PROPOSED: description]    │ [verb]   │ [comp]      │ [evidence]          │ NEW               │ [TBD — needs gate review]

SPINE ALIGNMENT NOTES
─────────────────────────────────────────────────────────────
Spine skills active in this module: [N]
  - Practice-eligible: [n]
  - Teaching only: [n]
Sub-skills decomposed: [list, with rationale for each]
Spine additions proposed: [count] — [list with evidence]
§1.8.5 delta (if SP provided): [divergences noted]

TRACK CLASSIFICATION
─────────────────────────────────────────────────────────────
Interaction Pattern   │ RDR Track        │ Confidence │ Notes
──────────────────────┼──────────────────┼────────────┼─────────────────────
[MC selection]        │ MC (RDR §3)      │ HIGH       │ [notes]
[Click-to-select]     │ MC (RDR §3)      │ HIGH       │ [notes]

MISCONCEPTION COVERAGE
─────────────────────────────────────────────────────────────
ID       │ Name                    │ Priority  │ Observable Behavior (from Misconception Table)            │ Template Strategy
─────────┼─────────────────────────┼───────────┼──────────────────────────────────────────────────────────┼──────────────────────
[U4.1]   │ [name]                  │ PRIMARY   │ [what the error looks like — for distractor design]       │ [3+ templates: types]
[U4.4]   │ [name]                  │ MONITOR   │ [observable pattern]                                     │ [distractor logic only]

PRACTICE PHASE GUIDANCE (from Toy Flow)
─────────────────────────────────────────────────────────────
Requirement              │ Source Text                              │ Template Implication
─────────────────────────┼──────────────────────────────────────────┼───────────────────────────
[e.g., 50-50 balance]    │ "target 50-50; flag at 45%"              │ Equal partitive/quotitive template count
[e.g., 1 construction]   │ "at least 1 problem per session..."      │ Need ≥1 CREATE-verb template

═══════════════════════════════════════════════════════════════
```

**Pause here for review.** The author should confirm:
- Is the skill decomposition correct? (Are spine skills mapped correctly? Are sub-skill splits justified? Are practice-scope exclusions right?)
- Are the dimension allocations appropriate per tier?
- Is the misconception strategy right?
- Does the Practice Phase Guidance capture all balance/mix requirements?
- Are track classifications correct?

---

### Step 3: Template Generation

For each practice-eligible skill (and sub-skill), generate templates across appropriate tiers. Follow these rules:

**Tier Logic (derived from Scaffolding Progression):**
- **confidence:** Uses Early-phase parameters and visual supports. Simplified task. May add scaffolding the student saw in early Lesson (e.g., partial completion, constrained options, familiar item types).
- **support:** Uses Early-to-Mid parameters. Slightly simplified. May constrain parameter space or add visual scaffolding.
- **baseline:** Uses the full Mid-to-Late parameter range. Grade-level standard presentation. Should include parameter values NOT seen in Early Lesson phases.
- **stretch:** Upper-boundary parameters, less familiar configurations, combined skills where the Toy Flow shows them emerging.
- **challenge:** Near upper boundary of Data Constraints. May combine multiple skills or use configurations that push toward the next module's expectations.

**Template Design Rules:**
1. Every template must reference a toy and mode from the Toy Requirements table. Use only interaction patterns documented there.
2. `workspace_description` must be specific enough that an engineer could build the screen. Include: toy name, mode, configuration, data visible, interaction type, what's hidden/shown.
3. `prompt_examples` use Helper voice — direct, task-focused: "How many groups of 4?" / "What's the quotient?" / "Build this division situation." NOT Guide voice: "Let's explore..." / "What do you notice..."
4. `success_dialogue` is brief, specific, behavioral: "5 in each group." / "Right — 4 groups." / "That's 15 ÷ 3 = 5." NOT "Great job thinking about that!"
5. `parameter_coverage` must list SPECIFIC values, not ranges. The expansion step needs to know exactly what to generate. Derive from the Dimension Coverage table.
6. MC distractors in `workspace_description` should target misconceptions from the Misconception Coverage table where applicable.
7. **Action variety:** Use at least 2 different interaction types across the template set (stepper, MC, multi-select, equation building, observation+MC, etc.) — draw from the Toy Requirements table.
8. **Practice Phase Guidance compliance:** Check each template set against the requirements extracted in Step 1E. If the Toy Flow says "50-50 partitive/quotitive," your template count must deliver that balance.
9. **Distractor Types (required for MC/multi-select templates):** Define a pool of 4-6 distractor types per template. Each type names the conceptual error, links to a misconception ID where applicable, and provides a Medium remediation direction (20-30 words). Draw from SP Answer Rationale entries, Misconception Table Observable Behaviors, and Toy Flow detection patterns.
10. **Remediation Design (required for all templates):** Every template gets a `remediation_design` block following the RDR's two-track model. Determine the track from `action_description` (MC → RDR §3, non-MC → RDR §2). Include Medium directions per distractor type, shared Heavy with `[Modeling]`, post-modeling language, and validator tags. **Confidence tier exception:** Light only, no Medium/Heavy (per RDR §11).
11. **Validator tags:** Every template that detects a misconception must include `[Validator: Misconception_#X]` tags in the remediation design block. These feed the pattern detection system (RDR §9). Templates with no misconception detection use `—`.
12. **Recommended Contexts (required for all templates):** Every template gets a `⚪ RECOMMENDED CONTEXTS` block with a coupling indicator (loose, tight, or misconception-sensitive) and a pool of 4-8 thematic contexts. Each context includes category examples and notes. Contexts must be age-appropriate, inclusive, and mathematically honest (category examples should produce plausible data values within the template's parameter range).

**Vocabulary constraint:** Only use vocabulary listed as "Introduced" or "Reinforced" in the Toy Flow's Vocabulary section. Do NOT use vocabulary listed under "NOT introduced" or "Deferred."

**Problem Count per Template:**
- Templates generating many similar problems (same skill, same tier, different parameters): 6-10 problems each
- Templates with more constrained parameter space: 3-5 problems
- Templates with very specific scenarios: 2-3 problems
- Total across all templates should hit the Pool Target

---

#### Misconception Targeting in Templates

There are two ways misconceptions appear in templates:

**1. Standard templates with misconception detection (template_type: standard)**

Any template can include a `misconception_targeting` block when the problem design naturally surfaces a misconception. For example, a baseline template asking "How many in each group?" might detect U4.2 (partitive/quotitive confusion) when the student gives the number of groups instead of the items per group. The targeting block documents the detection signal and remediation approach, but the template's primary purpose is still skill assessment.

For these templates:
- Design MC distractors using the Observable Behavior from the Misconception Table (e.g., if U4.1 says "student answer = divisor instead of quotient," make the divisor one of the MC options)
- Fill in the `misconception_targeting` block with detection signal and remediation approach
- The remediation pipeline will use this block to generate targeted feedback for when the student selects the misconception-matching answer

**2. Misconception remediation templates (template_type: misconception_remediation)**

These are templates designed *specifically* to surface and correct a misconception. They differ from standard templates in three ways:

- **The problem is designed so the misconception answer is visibly wrong.** Choose parameters where the error produces an answer that's obviously inconsistent with what's on screen. For example: 20 items shared into 2 groups — if the student says "2" (the divisor/group count), there are clearly 10 items visible in each group.
- **The parameter space is intentionally small and familiar.** These templates use confidence/support tier parameters (Early-phase values) so that computational difficulty doesn't mask the conceptual error. The student should be able to get the right answer easily once they see what they were doing wrong.
- **The `misconception_targeting` block is required and primary.** The `remediation_approach` field should reference specific Toy Flow guidance where available (SME remediation notes, resolved review questions, scaffold descriptions).

**Sources for remediation design (in authority order):**
1. **Remediation Design Reference (RDR)** — Structural authority. Determines the remediation track (MC vs non-MC), escalation levels (L-M-H), word counts, visual requirements, `[Modeling]` placement, and post-modeling language rules. Every template's `remediation_design` block must conform to the RDR's model.
2. **SP §1.4 Misconceptions** — Operationalized detection patterns and prevention strategies. Use for distractor type design and Medium direction content.
3. **SP §1.7 Lesson interactions** — Answer Rationale entries in MC lesson/EC problems document the distractor logic already validated by SMEs. Use these as starting points for distractor type pools.
4. **Toy Flow's SME Review Questions** — Often contain resolved remediation strategies.
5. **Toy Flow's Toy Requirements** — Remediation-only modes and interactions, visual scaffold options.
6. **Misconception Table's "Research-Backed Intervention" column** — Informs remediation approach.
7. **Practice Activity FDB's adaptive selection logic** — SUPPORT → CONFIDENCE escalation.

**How many misconception remediation templates?**
- Each PRIMARY/CRITICAL misconception should have at least 1 dedicated misconception_remediation template
- Each HIGH misconception should have at least 1 dedicated misconception_remediation template
- MODERATE misconceptions: 1 remediation template if the detection signal is clear, otherwise rely on detection in standard templates
- MONITOR/LOW misconceptions: no dedicated remediation templates — detection in standard templates only

**Misconception remediation templates do NOT count toward the Pool Target.** They sit in a separate remediation sub-pool that the adaptive engine draws from when error patterns are detected. The Pool Target applies to the standard assessment pool only.

**How the adaptive engine uses these (for context — not authored here):**
1. Student error on a standard template matches a `detection_signal` → targeted feedback (authored in remediation pipeline from this template's block)
2. Same misconception detected across 2+ problems → adaptive engine inserts a `misconception_remediation` template from the remediation sub-pool
3. Misconception persists after remediation template → flag for activity queue intervention

---

### Step 4: Template Summary

Produce the quick-reference table. Group standard and misconception_remediation templates separately:

```
═══════════════════════════════════════════════════════════════
MODULE [X] — TEMPLATE SUMMARY
═══════════════════════════════════════════════════════════════

STANDARD TEMPLATES (count toward Pool Target)
─────────────────────────────────────────────────────────────
#   │ ID   │ Type     │ Problem Type                  │ Spine Skill │ Sub-skill │ Verb     │ Track  │ Tiers           │ Misc. Detected │ Problems
────┼──────┼──────────┼───────────────────────────────┼─────────────┼───────────┼──────────┼────────┼─────────────────┼────────────────┼─────────
1   │ XX01 │ standard │ [type]                        │ [SK#]       │ [or —]    │ [verb]   │ [MC/NMC] │ [tiers]       │ [IDs or —]     │ [N]
2   │ XX02 │ standard │ [type]                        │ [SK#]       │ [or —]    │ [verb]   │ [MC/NMC] │ [tiers]       │ [IDs or —]     │ [N]
...
────┴──────┴──────────┴───────────────────────────────┴─────────────┴───────────┴──────────┴────────┴─────────────────┴────────────────┴─────────
                                                                                                        STANDARD POOL TOTAL │ [N]
                                                                                                                POOL TARGET │ [N]

MISCONCEPTION REMEDIATION TEMPLATES (separate sub-pool)
─────────────────────────────────────────────────────────────
#   │ ID   │ Type          │ Problem Type                  │ Spine Skill │ Targets       │ Tiers              │ Problems
────┼──────┼───────────────┼───────────────────────────────┼─────────────┼───────────────┼────────────────────┼─────────
1   │ XX20 │ misc_remed    │ [type]                        │ [SK#]       │ [misc. ID]    │ [conf./support]    │ [N]
...
────┴──────┴───────────────┴───────────────────────────────┴─────────────┴───────────────┴────────────────────┴─────────
                                                                                    REMEDIATION SUB-POOL TOTAL │ [N]

═══════════════════════════════════════════════════════════════
```

Note: The `Misc. Detected` column in the standard table lists misconception IDs that the template's `misconception_targeting` block can detect (not remediate). The `Targets` column in the remediation table lists the primary misconception the template is designed to surface and correct.

---

### Step 5: Coverage Validation

Check and report:

```
═══════════════════════════════════════════════════════════════
MODULE [X] — COVERAGE VALIDATION
═══════════════════════════════════════════════════════════════

TIER DISTRIBUTION (standard templates only — remediation templates excluded)
─────────────────────────────────────────────────────────────
Tier         │ Target    │ Actual    │ Status
─────────────┼───────────┼───────────┼────────
confidence   │ 8-12%     │ [X]%      │ ✅ / ⚠️
support      │ 15-20%    │ [X]%      │ ✅ / ⚠️
baseline     │ 40-50%    │ [X]%      │ ✅ / ⚠️
stretch      │ 15-20%    │ [X]%      │ ✅ / ⚠️
challenge    │ 5-8%      │ [X]%      │ ✅ / ⚠️

SKILL COVERAGE (grouped by spine skill)
─────────────────────────────────────────────────────────────
Skill ID        │ Sub-skill              │ Description (short)     │ Templates │ Tiers Covered    │ Status
────────────────┼────────────────────────┼─────────────────────────┼───────────┼──────────────────┼────────
ReadPicGraph    │ —                      │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
CompareData     │ CompareData:ordinal    │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
CompareData     │ CompareData:difference │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
CompareData     │ CompareData:combination│ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️

Note: Coverage is assessed at BOTH the spine skill level (does every active, practice-eligible spine
skill have templates?) and the sub-skill level (does every decomposed sub-skill have adequate tier coverage?).

VERB DISTRIBUTION
─────────────────────────────────────────────────────────────
Verb     │ Count │ % of Total │ Toy Flow Target        │ Status
─────────┼───────┼────────────┼────────────────────────┼────────
create   │ [N]   │ [X]%       │ [from Cognitive Focus] │ ✅ / ⚠️
identify │ [N]   │ [X]%       │ [from Cognitive Focus] │ ✅ / ⚠️

MISCONCEPTION DETECTION (in standard templates)
─────────────────────────────────────────────────────────────
ID       │ Priority  │ Detected In     │ Detection Strategy     │ Status
─────────┼───────────┼─────────────────┼────────────────────────┼────────
[U4.1]   │ PRIMARY   │ [std IDs]       │ [strategy]             │ ✅ (3+) / ⚠️
[U4.4]   │ MONITOR   │ [std IDs or —]  │ [distractor only]      │ ✅ / ⚠️

MISCONCEPTION REMEDIATION COVERAGE (dedicated remediation templates)
─────────────────────────────────────────────────────────────
ID       │ Priority   │ Remed. Template(s) │ Remediation Approach         │ Status
─────────┼────────────┼────────────────────┼──────────────────────────────┼────────
[U4.1]   │ PRIMARY    │ [remed IDs]        │ [approach summary]           │ ✅ (≥1) / ⚠️
[U4.2]   │ HIGH       │ [remed IDs]        │ [approach summary]           │ ✅ (≥1) / ⚠️
[U4.3]   │ MODERATE   │ [remed ID or —]    │ [approach or "std only"]     │ ✅ / ⚠️
[U4.4]   │ MONITOR    │ —                  │ std detection only           │ ✅

Requirements:
- PRIMARY/CRITICAL: ≥1 dedicated misconception_remediation template (⚠️ if missing)
- HIGH: ≥1 dedicated misconception_remediation template (⚠️ if missing)
- MODERATE: 1 remediation template if detection signal is clear; otherwise std detection only
- MONITOR/LOW: no dedicated remediation templates required

PRACTICE PHASE GUIDANCE COMPLIANCE
─────────────────────────────────────────────────────────────
Requirement              │ Met?  │ How
─────────────────────────┼───────┼───────────────────────────────────
[e.g., 50-50 balance]    │ ✅/⚠️ │ [X partitive templates, Y quotitive]
[e.g., 1+ construction]  │ ✅/⚠️ │ [Template IDs with CREATE verb]

ACTION VARIETY
─────────────────────────────────────────────────────────────
Action Type       │ Templates │ Track    │ Status
──────────────────┼───────────┼──────────┼────────
[Stepper]         │ [IDs]     │ Non-MC   │ ✅
[MC selection]    │ [IDs]     │ MC       │ ✅

DIMENSION COVERAGE
─────────────────────────────────────────────────────────────
All valid parameter values used across template set? [Yes/No]
Novel values (not in Early Lesson) present in baseline+? [Yes/No]
Early-phase values reserved for confidence/support? [Yes/No]

CONTEXT COVERAGE
─────────────────────────────────────────────────────────────
All templates have ⚪ RECOMMENDED CONTEXTS?      [All / Missing: IDs]
Context coupling appropriate per template?       [All / Mismatched: IDs]
Context variety across template set?             [Yes / No — flag reuse]
Category examples plausible for parameter range? [All / Implausible: IDs]

REMEDIATION DESIGN COMPLIANCE (per RDR)
─────────────────────────────────────────────────────────────
MC templates with per-distractor Medium?         [All / Missing: IDs]
MC templates with shared Heavy + [Modeling]?     [All / Missing: IDs]
Non-MC templates with full L-M-H?                [All / Missing: IDs]
Confidence templates with Light only?            [All / Violations: IDs]
Post-modeling language checked (RDR §7)?         [Yes / No]
Validator tags assigned?                         [All / Missing: IDs]
Distractor type pools ≥ 4 types?                 [All / Under: IDs]
Track classification consistent?                 [All / Mismatches: IDs]

GAPS / FLAGS
─────────────────────────────────────────────────────────────
[List any validation failures, missing coverage, or decisions needed]
[Flag any PRIMARY/HIGH misconceptions missing dedicated remediation templates]
[Flag any remediation templates where remediation_design lacks a concrete source reference]
[Flag any MC templates missing per-distractor Medium directions]
[Flag any spine skills marked practice-eligible but with 0 templates]
[Flag any sub-skill decompositions that produced only 1 template (consider folding)]

SP DELTA (only when SP was provided)
─────────────────────────────────────────────────────────────
[List any differences between Toy Flow and SP that affected template design]
[List any §1.8.5 targets that adjusted the spine-based distribution]
[Note §1.8.5 skills that were folded in spine vs. separate in SP — and which treatment won]

═══════════════════════════════════════════════════════════════
```

---

## OUTPUT FORMAT

The output is a single document per module — structured like a Starter Pack page in Notion. The backbone sections (Steps 0-2) sit above the template content (Steps 3-5) on the same page, so a reviewer can always trace a template decision back to the source constraint that justifies it.

**Page structure:**

```
MODULE [X] — PRACTICE TEMPLATES
├── §PT.0  Source Readiness Check
├── §PT.1  Source Analysis
├── §PT.2  Goal Decomposition + Dimension Budget
│          [PAUSE FOR AUTHOR REVIEW]
├── §PT.3  Templates
│   ├── Standard Templates
│   └── Misconception Remediation Templates
├── §PT.4  Template Summary
│   ├── Standard Pool (vs Pool Target)
│   └── Remediation Sub-Pool
└── §PT.5  Coverage Validation
    ├── Tier Distribution
    ├── Skill Coverage (grouped by spine skill)
    ├── Verb Distribution
    ├── Misconception Detection Coverage
    ├── Misconception Remediation Coverage
    ├── Practice Phase Guidance Compliance
    ├── Action Variety + Track Classification Check
    ├── Dimension Coverage
    ├── Gaps / Flags
    └── SP Delta (when SP provided)
```

Produce these sections in order, pausing after §PT.2 for author review:

1. **§PT.0 Source Readiness Check** (Step 0) — Verify inputs, document what's available, confirm spine alignment
2. **§PT.1–2 Source Analysis + Goal Decomposition** (Steps 1-2) — Constraint extraction, spine-anchored skill breakdown, track classification, dimension budget
3. **[PAUSE FOR REVIEW]** — Author confirms skill decomposition (including sub-skill splits and practice-scope decisions), dimension allocations, misconception strategy, track classifications before template generation
4. **§PT.3 Templates** (Step 3) — Full template set (standard first, then misconception remediation)
5. **§PT.4 Template Summary** (Step 4) — Two tables: standard pool with Pool Target comparison (including skill_id, sub_skill, and track columns), remediation sub-pool
6. **§PT.5 Coverage Validation** (Step 5) — All checks including spine-grouped skill coverage, track classification consistency, misconception detection, remediation coverage, and Practice Phase Guidance compliance

---

## WHAT THIS PROMPT DOES NOT COVER

- **Problem Expansion** (Step 2 of Practice Pipeline) — Generating specific problem instances from templates. Separate prompt.
- **Remediation Generation** (Step 3) — Generating actual remediation dialogue, animation specs, and TTS scripts from the template's Distractor Types + Remediation Design blocks. The template provides the *structure and direction*; the remediation pipeline authors the *content*. Separate prompt.
- **Notion Page Population** — Creating and formatting the module's Practice Templates page in Notion from this output. Separate automation step. Each module gets one page mirroring the section structure above (§PT.0–§PT.5).
- **Runtime Format Translation** — Converting reviewed/approved templates into the engine's runtime format. Separate, dependent on engine schema finalization.
- **Voice Polish** — Helper voice in prompt_examples and success_dialogue is functional placeholder. Full creative rewrite happens in Voice Polish stage.
- **SP Validation Pass** — When an SP becomes available after initial template generation, a separate validation pass checks templates against SP constraints. That workflow is documented separately.
- **Spine Updates** — When Stage 1 proposes skill additions, the spine update happens outside this prompt. Accepted additions are added to the spine by the author, and subsequent modules pick them up.
- **Notion Skill Spine Sync** — Keeping the Notion 🧬 Skill Spine database in sync with the markdown spine. This is a separate workflow (manual or automated).

---

## ANTI-PATTERNS

❌ **Don't invent toys or modes not in the Toy Requirements table.** If the Toy Flow doesn't list a mode for this module, it doesn't exist.

❌ **Don't use parameters outside Data Constraints.** If the Toy Flow says "divisors 2-5 only," don't use 7.

❌ **Don't test skills not taught in the Lesson.** If the Cognitive Focus doesn't list APPLY and the Lesson doesn't model application, don't create APPLY templates. Check the Scaffolding Progression — if it doesn't appear there, it's not appropriate.

❌ **Don't use vocabulary listed as "NOT introduced" or "Deferred."** If the Toy Flow says "dividend, divisor — deferred to M3," don't use those terms in prompt_examples.

❌ **Don't write Guide voice.** Helper is not Guide. No "Let's explore..." No "What do you notice..." No warmth beyond brief acknowledgment.

❌ **Don't ignore the Practice subsection.** The Toy Flow's Practice guidance gives you explicit requirements (balance ratios, construction minimums, error patterns). These are not suggestions — they're constraints. Validate against them in Step 5.

❌ **Don't combine skills prematurely.** If the Toy Flow shows two skills taught separately (e.g., partitive in Early, quotitive in Mid), design separate templates for each before creating any combined templates.

❌ **Don't skip the pause after Step 2.** The Source Analysis is the foundation. If it's wrong, every template is wrong.

❌ **Don't generate runtime format or JSON blocks.** This is the teacher-review layer. Templates should read like a clear specification a teacher can evaluate, not a data structure an engineer parses. Runtime translation comes after review approval.

❌ **Don't ignore the Skill Spine.** Your decomposition starts from the spine's Cross-Module Matrix for this module, not from a blank-slate Toy Flow analysis. If you think a spine skill should be split, decompose it into sub-skills with compound IDs. If you think a skill is missing, propose it with evidence and flag it.

❌ **Don't create separate skills for every tier variant.** "Read picture graph at scale 2" and "Read picture graph at scale 5" are tier variants of SK1, not separate skills. The tier system handles parameter variation — skills handle cognitive variation.

❌ **Don't treat §1.8.5 as the authoritative skill list.** The spine is the baseline. §1.8.5 is calibration. If they disagree, document the delta and explain your choice.

❌ **Don't decompose a spine skill without evidence of distinct cognitive operations.** Sub-skill decomposition requires at least two of: different verb, different interaction type, different EC item, different misconception target. "It would be easier to template" is not sufficient justification by itself — though it's a supporting signal.

---

## READY?

Paste the module section from the Unit Toy Flow, the Unit Skill Spine, and optionally the Module Starter Pack. Set the module parameters, and I'll begin with the Source Readiness Check.
