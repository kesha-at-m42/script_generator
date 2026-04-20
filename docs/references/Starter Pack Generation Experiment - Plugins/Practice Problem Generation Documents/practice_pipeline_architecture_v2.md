# PRACTICE TEMPLATE PIPELINE — ARCHITECTURE v2

**Version:** 2.0 (April 2026)
**Purpose:** Define the multi-stage gated pipeline for practice template generation, replacing the monolithic v1 prompt.
**Scope:** Stage 0 through Stage 3 + Post-Unit LC Reconciliation. Problem Expansion, Remediation Generation, and Runtime Translation remain separate downstream steps.

---

## PIPELINE OVERVIEW

```
STAGE 0 ──────────────────────────────────────────────────────────
  Skill Spine Generation (ONCE PER UNIT)
  Input:  Full Unit Toy Flow + Module Mapping xlsx + SPs (when available)
  Output: Unit Skill Spine — cross-module skill registry
  Gate:   Author confirms spine completeness and scoping
──────────────────────────────────────────────────────────────────

  ┌─── PER MODULE ────────────────────────────────────────────────┐
  │                                                              │
  │  STAGE 1 (ALL MODULES IN PARALLEL after Stage 0) ─────────  │
  │    Source Analysis + Goal Decomposition                      │
  │    Input:  Module section of Toy Flow + Skill Spine          │
  │            + SP (optional) + RDR v3 + Module Mapping         │
  │    Output: §PT.0 Source Readiness + §PT.1 Source Analysis    │
  │            + §PT.2 Goal Decomposition + Track Classification │
  │    Gate:   Author verifies source pull, skill decomp,        │
  │            dimension allocations, misconception strategy,     │
  │            track classifications (batch review across modules)│
  │                                                              │
  │  STAGE 2 (SEQUENTIAL — needs M[N-1] Stage 3 output) ──────  │
  │    Template Architecture                                     │
  │    Input:  Approved Stage 1 output + Skill Spine             │
  │            + Practice Phase Playbook distribution targets     │
  │            + Previous module's Template Summary               │
  │    Output: Template Blueprint — coverage plan, tier map,     │
  │            verb distribution, distractor strategy             │
  │    Gate:   Author reviews architectural plan before           │
  │            template writing begins                            │
  │                                                              │
  │  STAGE 3 (SEQUENTIAL — follows Stage 2 approval) ──────────  │
  │    Template Generation                                       │
  │    Input:  Approved Blueprint + all Stage 1 source data      │
  │            + Helper Voice Reference                           │
  │    Output: §PT.3 Templates + §PT.4 Summary + §PT.5 Validation│
  │    Gate:   Eval pipeline (pt-eval) catches quality issues     │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘

POST-UNIT ────────────────────────────────────────────────────────
  LC Reconciliation + Standards Crosswalk
  Input:  All module skill spines + Learning Commons API
  Output: Skill → LC Component mapping + 50-state standards coverage
──────────────────────────────────────────────────────────────────
```

---

## STAGE 0: SKILL SPINE GENERATION

**Runs:** Once per unit, before any per-module work begins.

### Purpose

Build a unit-level skill registry that ensures cross-module consistency. The spine is to skills what the Conceptual Spine (Module Mapping tab) is to concepts — a single source of truth for naming, scoping, and progression tracking.

### Why This Stage Exists

Without a spine, per-module skill decomposition produces inconsistent skill IDs. Module 1 names a skill "read a value from a bar graph" as S2; Module 3 names "read a value from a scaled bar graph" as a new skill; Module 7 names "read a value to solve a problem" as yet another. These are the same skill thread at different sophistication levels — but without a spine, the system can't track mastery progression across modules.

### Inputs

| Input | Required? | What It Provides |
|-------|-----------|-----------------|
| Full Unit Toy Flow | REQUIRED | Module-by-module learning goals, cognitive focus, scaffolding progressions, skill-level detail |
| Module Mapping xlsx — Conceptual Spine tab | REQUIRED | Concept threads across modules — spine skills should align with concept threads |
| Module Mapping xlsx — Misconceptions tab | OPTIONAL | Cross-module misconception landscape (informs which skills are misconception-heavy) |
| Available SPs (any modules) | OPTIONAL | §1.8.5 Skill Tracking tables where they exist — calibration data for decomposition granularity |
| Previous unit's Skill Spine (for Unit 2+) | OPTIONAL | Cross-unit skill thread continuity |

### Process

1. **Scan the full Toy Flow** for every module's Learning Goals, Cognitive Focus, and "What Students DO" sections. Identify every distinct assessable action students perform.

2. **Thread identification.** Group related actions across modules into skill threads. A thread represents one skill at increasing sophistication:
   - Where is it introduced? (first module where students do this action)
   - Where is it practiced? (subsequent modules where the same action appears with different parameters)
   - Where is it extended? (modules where the skill combines with new skills or reaches new complexity)
   - Where does it transform? (modules where the skill evolves into a qualitatively different skill)

3. **Scoping decisions.** For each thread, decide:
   - Is this one skill at different difficulty levels, or genuinely separate skills?
   - Calibration check: if §1.8.5 exists for any module, compare its skill count against what you're producing. If you're generating 2x the skills §1.8.5 lists for comparable modules, you're probably over-decomposing.
   - Folding rule: if a "skill" has ≤1 teaching interaction in any module and isn't independently tested in EC, prefer folding it into an adjacent skill's tier variant or distractor design.

4. **ID assignment.** Assign stable global descriptive IDs:
   - Format: CamelCase descriptive names (e.g., `ReadPicGraph`, `CompareData`, `BuildArray`)
   - IDs are unit-independent — the same skill reused across units keeps the same ID
   - Sub-skills use `Parent:qualifier` notation (e.g., `CompareData:ordinal`)
   - Each module's Stage 1 will map its local skills to spine IDs
   - New skills discovered in Stage 1 get added back to the spine (with author approval at the Stage 1 gate)

5. **LC breadcrumbs** (lightweight, not a full mapping):
   - For each spine skill, note: likely LC alignment exists / no obvious LC match / LC splits this differently
   - These are signals for the post-unit reconciliation, not authoritative mappings

### Output Format

```
═══════════════════════════════════════════════════════════════
UNIT [X] — SKILL SPINE v1
═══════════════════════════════════════════════════════════════

SPINE OVERVIEW
─────────────────────────────────────────────────────────────
Total skill threads: [N]
Modules covered: M1–M[N]
Conceptual Spine alignment: [notes on how skill threads map to concept threads]

SKILL THREADS
─────────────────────────────────────────────────────────────

[SkillName] — [Skill description]
  Description: [What the student can do — verb + object + context]
  Component: [procedural / conceptual / transfer]
  Primary verb: [create / identify / compare / apply / connect]
  Introduced: M[N] — [brief context]
  Practiced: M[N], M[N] — [how it progresses]
  Extended: M[N] — [what changes]
  Related misconceptions: [IDs if applicable]
  LC breadcrumb: [likely match / no match / LC splits differently]
  Notes: [scoping decisions, why this is one skill vs. two, etc.]

[AnotherSkill] — [Skill description]
  ...

CROSS-MODULE MATRIX
─────────────────────────────────────────────────────────────
Skill ID          │ M1  │ M2  │ M3  │ M4  │ ... │ M[N]
──────────────────┼─────┼─────┼─────┼─────┼─────┼──────
ReadPicGraph      │ INT │ PRC │ PRC │ EXT │     │
ReadBarGraph      │     │ INT │ PRC │ PRC │ PRC │ EXT
CreatePicGraph    │ INT │     │     │     │ EXT │ TRN
...
Key: INT = Introduced, PRC = Practiced, EXT = Extended, TRN = Transforms

SCOPING DECISIONS LOG
─────────────────────────────────────────────────────────────
[Document every non-obvious scoping decision:
 - "Folded 'count symbols in a row' into ReadPicGraph because
   counting is not independently assessed — it's the mechanism for reading."
 - "Split 'compare two categories' from 'compare across graphs' because
   M7 introduces cross-graph comparison as a qualitatively new task."
]

═══════════════════════════════════════════════════════════════
```

### Gate Criteria — Stage 0

Author reviews the spine and confirms:

- [ ] Every module's learning goals are represented by at least one skill thread
- [ ] Skill threads are scoped correctly (not over-decomposed, not under-decomposed)
- [ ] Cross-module matrix shows plausible progression (skills don't appear and disappear randomly)
- [ ] Scoping decisions are documented and defensible
- [ ] Skill count is calibrated against available §1.8.5 data (where it exists)
- [ ] No "orphan" skills that appear in only one module with no clear thread

---

## STAGE 1: SOURCE ANALYSIS + GOAL DECOMPOSITION

**Runs:** Once per module.

### Purpose

Extract everything the template set needs from source documents. Decompose the module's skills — anchored to the spine. Identify gaps and flag decisions for the author.

### Why This Stage Exists Separately

If source analysis is wrong, every template is wrong. Separating extraction from generation means the author catches errors before they cascade. This stage is verification-focused: "did we pull information correctly? Are we missing anything?"

### Inputs

| Input | Required? | What It Provides |
|-------|-----------|-----------------|
| Module section of Unit Toy Flow | REQUIRED | Primary source for everything — see extraction table below |
| Unit Skill Spine (Stage 0 output) | REQUIRED | Skill IDs, cross-module threading, scoping constraints |
| Previous module's Stage 1 output | REQUIRED (M2+) | Skill progression context, parameter continuity |
| Module Starter Pack | OPTIONAL | §1.2 scope, §1.4 misconceptions, §1.5 toy specs, §1.8 EC, §1.8.5 practice inputs |
| Unit Misconception Table (Module Mapping xlsx) | OPTIONAL | Structured misconception data with Observable Behaviors |
| Remediation Design Reference v3 | REFERENCE | Reviewed in Source Readiness Check to understand track model (MC vs non-MC); actively used in Stage 3 for remediation blocks |

### Process

**Step 0: Source Readiness Check (§PT.0)**

Before any analysis, audit input completeness. For each required data point, document:
- Whether the Toy Flow provides it (✅ / ⚠️ / ❌)
- Whether the SP fills any gaps
- Whether the Module Mapping enriches it
- RDR track audit: confirm which interaction types this module uses (MC, drag, stepper, etc.) and identify the applicable RDR track (MC → §3, non-MC → §2). This informs distractor strategy in Stage 2 and remediation blocks in Stage 3.

Gap handling rules (from v1 — unchanged):
- Missing Practice subsection → derive from EC + Lesson Late. Flag for review.
- Missing Data Constraints → check SP §1.5. If neither source has ranges, BLOCKING.
- Missing Scaffolding Progression → derive from Lesson phase descriptions. Flag as lower confidence.
- Missing Misconceptions → check SP §1.4. If neither source has PRIMARY misconceptions, BLOCKING.

**Step 1: Source Analysis (§PT.1)**

Extract and organize (carried forward from v1 Steps 1A-1F):

| Sub-step | What | Source Priority |
|----------|------|----------------|
| A. Toy Inventory | Toys, modes, interactions, phase restrictions, changes from M[N-1] | Toy Flow → SP §1.5 |
| B. Constraint Extraction | Numerical ranges per phase, scope boundaries, item/container types | Toy Flow Data Constraints → SP §1.2 + §1.5 |
| C. Skill Inventory | Assessable skills mapped to spine IDs | Toy Flow Cognitive Focus + What Students DO + EC → Skill Spine → SP §1.8.5 (validation) |
| D. Misconception Mapping | Priority classification, observable behaviors, detection strategies — classify as PRIMARY (3+ templates), SECONDARY (1-2 templates), MONITOR (distractor only) | Toy Flow + SP §1.4 + Unit Misconception Table |
| E. Practice Phase Guidance | Explicit requirements from Toy Flow "What Students DO → Practice" — any constraint stated as a rule, ratio, minimum, or balance target (e.g., "50-50 partitive/quotitive," "at least 1 construction problem per session") | Toy Flow → SP §1.8.5 |
| F. Dimension Budget + Tier Mapping | Parameter ranges per tier, derived from Scaffolding Progression (see Tier Derivation below) | Toy Flow Data Constraints + Scaffolding Progression → SP §1.8.5 |

**Tier Derivation from Scaffolding Progression** (carried from v1):

The Toy Flow's Scaffolding Progression table is the primary source for tier logic. Scaffolding level in the Lesson maps inversely to tier difficulty in Practice:

| Lesson Phase | Scaffold Level | Practice Tier |
|---|---|---|
| Early (heavy scaffold, guide-narrated) | High — system does most | **confidence**: Early-phase parameters, familiar visual supports, simplified tasks |
| Mid (fading scaffold, guided practice) | Medium — student acts with support | **support**: Early-to-Mid parameters, moderate simplification |
| Late (minimal scaffold, independent) | Low — student acts independently | **baseline**: Full Mid-to-Late parameter range, standard presentation |
| Exit Check (no scaffold, assessment) | None — clean assessment | **baseline/stretch**: EC-level problems are the grade-level bar |
| Beyond Lesson scope | N/A — extends taught skills | **stretch/challenge**: Upper boundary parameters, combined skills, novel configurations within scope |

Phase-specific Data Constraints map to tier parameter ranges: confidence/support → Early ranges, baseline → Mid-to-Late ranges, stretch/challenge → upper boundary of Late or modest extensions within Data Constraints.

**Step 2: Goal Decomposition (§PT.2)**

Organize skills by component with spine references:

| Component | Target % |
|-----------|----------|
| Procedural | 30-40% |
| Conceptual | 30-40% |
| Transfer | 20-30% |

**Skill Addition Rule** (anchored on spine, not §1.8.5):

The Unit Skill Spine is the baseline decomposition. Stage 1 may identify module-specific skills not in the spine if the Toy Flow reveals assessable actions the spine didn't capture. For each proposed addition:
- State the Toy Flow evidence (which interactions teach it, how many)
- State the assessment evidence (is it tested in EC?)
- State whether it maps to a Skill Spine thread
- If the skill has ≤1 teaching interaction and no EC test, prefer folding it into an existing skill's tier variant or distractor design
- New skills flagged here get reviewed at the Stage 1 gate and, if accepted, added back to the spine

**§1.8.5 as validation** (when available): If the SP has §1.8.5, compare your decomposition against its Skill Tracking table. Significant divergence (2x the skills, different component balance) should be flagged with rationale. §1.8.5 is a calibration check, not the starting point.

**Step 3: Track Classification**

For every interaction pattern identified in the Toy Inventory (Step 1A), classify the RDR remediation track:

```
TRACK CLASSIFICATION
─────────────────────────────────────────────────────────────
Interaction Pattern  │ Track  │ Confidence │ Notes
─────────────────────┼────────┼────────────┼──────────────────────────
MC (4-option select) │ MC     │ HIGH       │ RDR §3
Stepper              │ non-MC │ HIGH       │ RDR §2
Drag-to-place        │ non-MC │ HIGH       │ RDR §2
Drag + MC confirm    │ ???    │ LOW        │ [Author decision needed]
Observe + MC         │ MC     │ MEDIUM     │ MC is the assessed action
```

Rules:
- If the student's assessed action is a choice (MC, multi-select), track = MC (RDR §3)
- If the assessed action is construction (drag, stepper, click-to-place), track = non-MC (RDR §2)
- If the interaction has both construction and choice components, flag as ambiguous — author decides at gate
- Confidence tier override (RDR §11) applies regardless of track — note but don't resolve here

This classification flows into Stage 2 (distractor strategy depends on track) and Stage 3 (remediation block structure).

### Output Format

Same structured format as v1 (§PT.0, §PT.1, §PT.2 sections) with these additions:
- Track Classification table (new — from Step 3 above)
- Skill Decomposition table adds `skill_id` column (global CamelCase name from Skill Spine)
- Skill Decomposition table adds `Progression from M[N-1]` column referencing spine
- New skills not in spine are flagged with `[SPINE ADDITION PROPOSED]`
- §1.8.5 delta section (when SP provided): any differences between spine-based decomposition and §1.8.5

### Gate Criteria — Stage 1

Author reviews and confirms:

- [ ] Source Readiness Check shows no BLOCKING gaps (or gaps are acceptable)
- [ ] Toy Inventory matches what's actually available in Practice (not just Lesson)
- [ ] Constraint Extraction is correct — numerical ranges match source documents
- [ ] Skill decomposition maps cleanly to spine (no orphans, no ID conflicts)
- [ ] Any proposed spine additions are justified (teaching evidence + assessment evidence)
- [ ] Misconception strategy is appropriate (PRIMARY → 3+ templates, SECONDARY → 1-2, MONITOR → distractor only)
- [ ] All track classifications resolved (no LOW confidence / ambiguous tracks remaining)
- [ ] Practice Phase Guidance captures all explicit requirements from Toy Flow
- [ ] Dimension budget per tier is reasonable (Early→confidence, Late→baseline, Upper→stretch)
- [ ] Tier derivation from Scaffolding Progression is reasonable (Early→confidence, Late→baseline, etc.)
- [ ] §1.8.5 delta is explained (when SP provided)

**Decision point:** Are there any unknowns the Toy Flow doesn't resolve? If yes, flag for SME and either resolve before Stage 2 or document the assumption being made.

---

## STAGE 2: TEMPLATE ARCHITECTURE

**Runs:** Once per module, after Stage 1 gate approval.

### Purpose

Design the template set — how many templates, which skills at which tiers, verb distribution, distractor pool strategy, coverage plan. This is the "blueprint" the author approves before any template writing happens.

### Why This Stage Exists Separately

Stage 2 is where the most consequential judgment calls happen. If you bundle it with template generation (Stage 3), the author reviews architectural decisions and template details simultaneously — and they'll focus on the concrete details and miss structural problems. Cheaper to fix a bad plan than bad execution.

### Inputs

| Input | Required? | What It Provides |
|-------|-----------|-----------------|
| Approved Stage 1 output (§PT.0-2) | REQUIRED | Skill inventory, dimension budget, misconception strategy, practice guidance |
| Unit Skill Spine | REQUIRED | Cross-module context — which skills are new vs. practiced vs. extended |
| Practice Phase Playbook v3 | REQUIRED | Distribution targets, tier definitions, schema requirements |
| Previous module's Template Summary (§PT.4 from Stage 3) | REQUIRED (M2+) | What was already covered, verb distribution so far in unit. **Sequencing note:** Module N's Stage 2 requires Module N-1's Stage 3 output. Stages 2-3 run sequentially per module. However, Stage 1 has no cross-module dependency — all modules can run Stage 1 in parallel after Stage 0, with batch author review. |

### Process

**Step 1: Template Count + Allocation**

Starting from the approved skill inventory and pool target:
- Calculate how many templates are needed per skill based on tier coverage requirements
- Allocate across tiers to hit distribution targets (confidence 8-12%, support 15-20%, baseline 40-50%, stretch 15-20%, challenge 5-8%)
- Check: does the allocation hit the pool target? (Early M1-4: 55-65, Mid M5-8: 60-75, Late M9-12: 65-80)

**Step 2: Verb Distribution Plan**

Map cognitive verbs to templates:
- Use Toy Flow's Cognitive Focus for target distribution
- When Toy Flow doesn't specify percentages, use module stage defaults from Playbook
- Ensure minimum 2 different verb types
- Tag each planned template with its primary verb
- Check cumulative unit verb distribution (using previous modules' summaries)

**Step 3: Distractor Strategy**

For each skill with MC/multi-select interaction:
- Map which misconceptions the template should detect (from misconception strategy)
- Plan which distractor types will be shared across templates vs. unique
- Identify where misconception_remediation templates are needed (PRIMARY/HIGH misconceptions)

**Step 4: Interaction Type Plan**

Map interaction types to templates:
- Draw only from toys/modes available in Practice (from Toy Inventory)
- Ensure minimum 2 different interaction types across the set
- Check that interaction variety is authentic (not forcing a stepper where MC is natural)

**Step 5: Coverage Map**

Produce the blueprint — a compact representation of the entire template set plan:

### Output Format

```
═══════════════════════════════════════════════════════════════
MODULE [X] — TEMPLATE BLUEPRINT
═══════════════════════════════════════════════════════════════

POOL TARGET: [N] (from Playbook §8)
PLANNED STANDARD TEMPLATES: [N] → [N] problems
PLANNED REMEDIATION TEMPLATES: [N] (separate sub-pool)

TEMPLATE PLAN
─────────────────────────────────────────────────────────────
#  │ Planned ID │ Skill ID         │ Tier       │ Verb     │ Interaction  │ Misc. Detected │ Problems
───┼────────────┼──────────────────┼────────────┼──────────┼──────────────┼────────────────┼─────────
1  │ XX01       │ ReadPicGraph     │ confidence │ identify │ MC           │ —              │ 6
2  │ XX02       │ ReadPicGraph     │ baseline   │ identify │ MC           │ #16            │ 8
3  │ XX03       │ ReadBarGraph     │ support    │ create   │ stepper      │ —              │ 6
...

REMEDIATION TEMPLATE PLAN
─────────────────────────────────────────────────────────────
#  │ Planned ID │ Targets    │ Tier       │ Interaction │ Problems
───┼────────────┼────────────┼────────────┼─────────────┼─────────
1  │ XX20       │ #16        │ confidence │ MC          │ 4
...

DISTRIBUTION CHECK
─────────────────────────────────────────────────────────────
                     Planned  │ Target    │ Status
confidence           [X]%     │ 8-12%     │ ✅ / ⚠️
support              [X]%     │ 15-20%    │ ✅ / ⚠️
baseline             [X]%     │ 40-50%    │ ✅ / ⚠️
stretch              [X]%     │ 15-20%    │ ✅ / ⚠️
challenge            [X]%     │ 5-8%      │ ✅ / ⚠️

VERB DISTRIBUTION CHECK
─────────────────────────────────────────────────────────────
Verb       │ Planned │ Target (from TF) │ Cumulative Unit │ Status
───────────┼─────────┼──────────────────┼─────────────────┼────────
create     │ [X]%    │ [X]%             │ [X]% (M1-N)     │ ✅ / ⚠️
identify   │ [X]%    │ [X]%             │ [X]% (M1-N)     │ ✅ / ⚠️
...

MISCONCEPTION COVERAGE CHECK
─────────────────────────────────────────────────────────────
ID     │ Priority  │ Standard Detection │ Remed. Template │ Status
───────┼───────────┼────────────────────┼─────────────────┼────────
[#16]  │ PRIMARY   │ XX02, XX05         │ XX20            │ ✅
[#17]  │ SECONDARY │ XX08               │ —               │ ✅

PRACTICE PHASE GUIDANCE COMPLIANCE
─────────────────────────────────────────────────────────────
Requirement              │ Planned │ Status
─────────────────────────┼─────────┼────────
[e.g., 50-50 balance]    │ [how]   │ ✅ / ⚠️

INTERACTION VARIETY
─────────────────────────────────────────────────────────────
Type          │ Templates │ Status
──────────────┼───────────┼────────
MC            │ [IDs]     │
Stepper       │ [IDs]     │
─────────────────────────────────── Min 2 types: ✅ / ⚠️

ARCHITECTURAL DECISIONS
─────────────────────────────────────────────────────────────
[Document every non-obvious choice:
 - "Gave ReadPicGraph more templates than CreatePicGraph because ReadPicGraph
   is the foundational read-a-value skill that everything else builds on."
 - "No challenge tier for CreateBarGraph because the Toy Flow only introduces
   this skill in Late Lesson — no room to extend beyond baseline."
 - "Used identify verb for Template XX05 even though the interaction
   is drag — student is identifying the correct bar, not constructing."
]

═══════════════════════════════════════════════════════════════
```

### Gate Criteria — Stage 2

Author reviews the blueprint and confirms:

- [ ] Template count hits pool target (or deviation is explained)
- [ ] Tier distribution is within targets
- [ ] Verb distribution matches Toy Flow Cognitive Focus (or deviation is explained)
- [ ] Every PRIMARY/HIGH misconception has detection in standard templates + a remediation template
- [ ] Practice Phase Guidance requirements are all addressed
- [ ] Interaction types are varied (min 2) and authentic for each template
- [ ] Architectural decisions are documented and defensible
- [ ] Spine skill coverage is complete — every skill from Stage 1 decomposition has templates
- [ ] No skill is over-represented relative to its importance

**Decision point:** Does the plan make sense before we write 15+ detailed templates? Adjustments here are cheap. Adjustments after Stage 3 are expensive.

---

## STAGE 3: TEMPLATE GENERATION

**Runs:** Once per module, after Stage 2 gate approval.

### Purpose

Execute the approved blueprint. Write every template to full schema spec. Produce the validation tables.

### Why This Stage Exists Separately

With the architectural decisions already made and approved (Stage 2), this stage is pure execution. The system follows the blueprint, the author's review focuses on template quality (not template strategy), and the eval pipeline catches mechanical issues.

### Inputs

| Input | Required? | What It Provides |
|-------|-----------|-----------------|
| Approved Stage 2 Blueprint | REQUIRED | Template plan — what to build |
| Stage 1 output (§PT.0-2) | REQUIRED | Source data — constraint details, dimension budgets, misconception details |
| Helper Voice Reference | REQUIRED | Voice constraints for prompt_examples and success_dialogue |
| Remediation Design Reference v3 | REQUIRED | Structural model for Distractor Types + Remediation Design blocks |
| Practice Phase Playbook v3 | REQUIRED | Schema definition, template design rules |

### Process

For each template in the blueprint:

1. **Write the template** following the full schema from v1 (all blocks: 🟢 SKILL, 🔵 PROBLEM TYPE, ⚪ RECOMMENDED CONTEXTS, 🟠 PROMPT EXAMPLES, 🟣 SUCCESS DIALOGUE, 🟡 PROACTIVE SCAFFOLD SUGGESTIONS, 🔴 DISTRACTOR TYPES, 🟤 REMEDIATION DESIGN, Technical Details)

2. **Add skill reference** — `skill_id` (global CamelCase name) and `sub_skill` (when applicable) in Technical Details link to the Skill Spine

3. **Follow all v1 Template Design Rules** (carried forward — see Reference section below)

4. **Produce Template Summary (§PT.4)** — standard pool and remediation sub-pool tables

5. **Produce Coverage Validation (§PT.5)** — all validation checks from v1

### Template Design Rules (from v1 — carried forward)

These rules are unchanged from the v1 prompt. They live in Stage 3 because they govern template writing, not architecture:

1. Every template must reference a toy and mode from the Toy Inventory. Use only documented interaction patterns.
2. `workspace_description` must be specific enough to build the screen.
3. `prompt_examples` use Helper voice (from Helper Voice Reference).
4. `success_dialogue` is brief, specific, behavioral.
5. `parameter_coverage` lists SPECIFIC values, not ranges.
6. MC distractors target misconceptions from the Misconception Coverage table.
7. Minimum 2 different interaction types across the set.
8. Practice Phase Guidance compliance — check against requirements from Stage 1E.
9. Distractor Types: pool of 4-6 per template, each with conceptual error, misconception link, Medium direction.
10. Remediation Design: follow RDR two-track model. Confidence tier exception: Light only.
11. Validator tags on every misconception-detecting template.
12. Recommended Contexts with coupling indicator and age-appropriate, inclusive context pools.
13. Vocabulary constraint — only Introduced or Reinforced terms.

### Output Format

Same as v1 §PT.3, §PT.4, §PT.5 — with `skill_id` and `sub_skill` in Technical Details.

### Quality Gate — Stage 3

After Stage 3, the eval pipeline (pt-eval) runs. Author review focuses on:

- [ ] Templates match the approved blueprint (no unapproved additions or removals). If Stage 3 reveals need for templates not in the blueprint (e.g., a misconception remediation template the architecture missed), escalate to author — do not add without Stage 2 re-approval.
- [ ] Helper voice is correct (not Guide voice)
- [ ] Workspace descriptions are buildable
- [ ] Parameter coverage uses specific values within approved dimension budget
- [ ] Distractor types are grounded in teaching moments (no generic "Try again" Medium directions)
- [ ] Remediation design follows RDR (correct track, correct escalation, modeling tags)
- [ ] Coverage Validation passes all checks
- [ ] Context pools are age-appropriate, inclusive, and mathematically honest

---

## POST-UNIT: LC RECONCILIATION + STANDARDS CROSSWALK

**Runs:** Once per unit, after all modules' Stage 3 outputs are complete.

### Purpose

Map Mission42 skill spine to Learning Commons knowledge graph components for 50-state standards coverage. This is a translation layer — it doesn't change the skill decomposition.

### Why This Runs Post-Unit

The LC mapping serves compliance and interoperability, not pedagogical design. Running it after template generation ensures the teaching-forward decomposition stays clean and isn't influenced by LC's component granularity (which may not match Mission42's pedagogical model).

### Process (to be detailed when LC MCP is available)

1. For each spine skill, query LC for closest learning component(s)
2. Evaluate alignment quality: exact match / partial match / no match / LC splits differently
3. For partial matches and splits, document the relationship (e.g., "CreatePicGraph maps to LC components X and Y combined")
4. Generate standards crosswalk: spine skill → LC component → state standards (all 50 states)
5. Flag coverage gaps: any state standards not covered by any spine skill

### Output: Skill → Standards Crosswalk Table

```
Skill ID          │ Skill             │ LC Component(s) │ Match Quality │ CCSS     │ TEKS    │ [etc.]
──────────────────┼───────────────────┼─────────────────┼───────────────┼──────────┼─────────┼────────
ReadPicGraph      │ [description]     │ [LC ID(s)]      │ exact         │ 3.OA.1   │ 3.4A    │ ...
ReadBarGraph      │ [description]     │ [LC ID(s)]      │ partial       │ 3.OA.2   │ —       │ ...
```

---

## SUPPORTING DOCUMENTS

### Helper Voice Reference (to be drafted)

Shared reference document used by Stage 3. Defines:
- Helper character constraints (what Helper does and doesn't do)
- Distinction from Guide voice
- Prompt example patterns (direct, task-focused)
- Success dialogue patterns (brief, specific, behavioral)
- Boundaries (no relationship-building, no "what do you notice," no excessive warmth)
- What Helper shares with Guide (authentic, warm, never punitive, age-appropriate)

### Document Relationships

```
Practice Phase Playbook v3
  └── defines schema, tier system, cognitive types, validation criteria
  └── referenced by: Stage 2 (distribution targets), Stage 3 (template rules)

Remediation Design Reference v3
  └── defines remediation structure (tracks, levels, escalation)
  └── referenced by: Stage 1 (RDR readiness check), Stage 3 (template remediation blocks)

Helper Voice Reference (new)
  └── defines helper character voice for practice
  └── referenced by: Stage 3 (prompt_examples, success_dialogue)

Unit Skill Spine (Stage 0 output)
  └── defines cross-module skill threads + representations (toy-anchored labels)
  └── referenced by: Stage 1 (skill decomposition anchor, representation targeting), Stage 2 (coverage planning)
```

---

## WHAT CHANGED FROM v1

| v1 (monolithic prompt) | v2 (staged pipeline) | Why |
|------------------------|---------------------|-----|
| Single prompt, single output | 4 stages with gates | Separate verification from architecture from execution |
| No skill spine — per-module decomposition | Stage 0 builds unit-level skill spine | Cross-module consistency |
| §1.8.5 treated as "highest-value SP addition" | Spine is baseline; §1.8.5 is validation | SP is optional — can't be baseline |
| Source Readiness Check was invented by output (§PT.0) | Source Readiness Check is a required first step in Stage 1 | Formalized what worked |
| No architectural review before template writing | Stage 2 Blueprint reviewed before Stage 3 | Catch structural problems cheaply |
| Per-module verb minimums only (min 2 types) | Stage 2 tracks cumulative unit verb distribution across all modules | Supports cognitive verb hypothesis — need analytical signal across the unit |
| Helper voice rules embedded in prompt | Helper Voice Reference as shared document | Reduces per-template review burden; single source of truth |
| No mechanism to constrain skill over-decomposition | Skill Addition Rule anchored on spine + folding rule | Prevents over-decomposition problem from M1 |
| No LC integration point | Post-unit reconciliation stage | 50-state standards coverage without compromising pedagogy |
| No global skill ID in schema | `skill_id` (global CamelCase) + `sub_skill` required in Technical Details | Cross-module mastery tracking via Notion Skill Spine database |
| No representation metadata | `Representations` on spine skills + `representation` on templates | Skills spanning multiple toy types (e.g., CompareData on Picture Graphs + Bar Graphs) need templates to declare which representation they target. Supports knowledge graph routing and coverage analysis. |

---

## DELIVERABLES — CRITICAL PATH

Build order optimized for fastest path to next data point. Validate before automating.

### Phase 1: Validate Spine + Generalization (NOW)

| # | Deliverable | Status | Notes |
|---|------------|--------|-------|
| 1 | **Stage 0 Prompt — Skill Spine Generation** | TO BUILD | Lightweight v1. Highest-value deliverable — everything else depends on it. |
| 2 | **Patched v1 Prompt** (combined Stage 1+2) | TO BUILD | Four changes to existing v1: formalize Source Readiness Check, add Skill Addition Rule anchored on spine, add `skill_id`/`sub_skill` to schema (global CamelCase names), §1.8.5 as validation. Plus: add Track Classification to Stage 1 output. |

**Runs:**
- Stage 0 on Unit 1 → validate spine quality
- Patched v1 on U1 M2 or M7 (different module profile than M1) → validate generalization
- Patched v1 on one more module → third data point

**Postmortem after Phase 1:**
- Is the spine at the right granularity?
- Does the patched prompt generalize across module types?
- Did the Skill Addition Rule prevent over-decomposition?
- Were there architectural decisions that the author caught too late (argues for Stage 2 separation)?

### Phase 2: Stage Separation (IF Phase 1 postmortem supports it)

| # | Deliverable | Status | Notes |
|---|------------|--------|-------|
| 3 | Stage 1 Prompt (standalone) | DEFERRED | Split from patched v1 if postmortem shows value in separating source analysis from architecture |
| 4 | Stage 2 Prompt — Template Architecture | DEFERRED | Build only if postmortem shows authors catching structural problems too late |
| 5 | Stage 3 Prompt — Template Generation | DEFERRED | Build only if Stage 2 separation is confirmed |
| 6 | Helper Voice Reference | DEFERRED | Build when Stage 3 is being built — not before |

### Phase 3: Ecosystem (AFTER templates are being generated reliably)

| # | Deliverable | Status | Notes |
|---|------------|--------|-------|
| 7 | Updated pt-eval plugin | DEFERRED | Update when there are templates to evaluate against spine + blueprint |
| 8 | LC Reconciliation Process | DEFERRED | Depends on LC MCP availability and quality assessment |

---

## TEST PLAN

**Run 1 — Spine:** Stage 0 on Unit 1. Validates whether the Toy Flow has enough detail for unit-level skill decomposition. Calibrate against §1.8.5 where available.

**Run 2 — Generalization:** Patched v1 on U1 M2 or U1 M7 (procedural or bridge module — different profile from M1). Tests whether spine anchoring + skill addition rule work for non-conceptual modules.

**Run 3 — Stress test:** Patched v1 on U2 M2 (different unit entirely). Tests whether the pipeline works with a different Toy Flow quality/structure.

**Postmortem criteria:**
- Is the spine at the right granularity? (Too many threads = over-decomposed, too few = losing signal)
- Does the Skill Addition Rule prevent over-decomposition without suppressing real skills?
- Were there architectural decisions the author caught too late? (If yes → build Stage 2)
- Did track classification catch ambiguous cases? (If not → simplify)
- Is the patched v1 too long / too complex for reliable output? (If yes → split into stages)
