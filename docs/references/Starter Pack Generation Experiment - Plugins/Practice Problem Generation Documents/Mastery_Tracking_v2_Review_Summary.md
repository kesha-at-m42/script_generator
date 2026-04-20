# Skill Knowledge Graph & Mastery Tracking v2 — Review Summary

**For:** Data Architecture, Platform Engineering
**From:** Jon Frye, Curriculum/Product
**Date:** April 2026
**Full spec:** Mastery_Tracking_FDB_v2.md (linked in Notion)
**Ask:** Alignment on the knowledge graph architecture + engineering feasibility of the schema and queries that sit on top of it

---

## Definitions

These terms have specific meanings in this system. Getting the vocabulary aligned now prevents misunderstandings downstream.

**Skill:** An atomic, assessable student capability — the smallest unit we track mastery on. A skill is curriculum-independent: it exists in the registry regardless of where or when a student encounters it. Example: `CompareData:difference` (the ability to figure out "how many more" or "how many fewer" by comparing two groups on a graph). A skill belongs to one component and is assessed by one or more cognitive types.

**Sub-skill:** A leaf-level skill that sits under a parent skill. Sub-skills are the nodes students actually see and are assessed on. Example: `CompareData:difference` and `CompareData:ordinal` are both sub-skills of `CompareData`. The distinction matters because only sub-skills (leaf nodes) appear in the student-facing display — parent skills are architectural groupings.

**Parent skill:** An organizational node that groups related sub-skills. NOT directly assessed — it exists for structural clarity in the registry. Example: `CompareData` is the parent of `CompareData:difference` and `CompareData:ordinal`. Parent skills are hidden from the student view.

**Module:** A collection of skills taught together as a unit (e.g., M4 — Bar Graphs & 1:10 Scale). A module contains 1–6 skills, each with a defined role. Modules are curriculum-specific — a different curriculum could define different modules from the same skill nodes, with different sequencing and different role assignments.

**Curriculum:** A graph that organizes skills into modules, defines paths between modules, and assigns each skill a role within each module where it appears. Currently we have one curriculum (Unit 1, Grade 3). The architecture should support multiple curricula sharing the same skill registry.

**Role (INT / PRC / EXT):** The teaching intent for a skill within a specific module in a specific curriculum. This is a property of (skill × module × curriculum), NOT a property of the skill itself.
- **INT (Introduced):** First encounter. The skill is new learning in this module. Highest-stakes — failure here means the core concept didn't land.
- **PRC (Practiced):** Reinforcement. The student has seen this skill before (INT in an earlier module) and is now practicing it in a new context or representation. Failure suggests a representation barrier or need for more reps, not necessarily a fundamental gap.
- **EXT (Extended):** Transfer. The skill is applied in novel contexts or combined with other skills. Tracking only — no gating.

**Representation:** The visual or contextual form a skill takes in a given module. Example: `CompareData:difference` operates on Picture Graphs in M1 (INT) and Bar Graphs in M4 (PRC). The skill is the same; the representation is different. This distinction is how the system diagnoses "knows the skill but can't read the new format" vs. "doesn't know the skill."

**Assessment mode:** Whether a skill is assessed through dedicated templates (standalone) or within another skill's templates (embedded). Standalone skills get more assessment data and more reliable status verdicts. Embedded skills have smaller sample sizes and may stay at "Still Gathering" longer.

**Component:** The type of understanding a skill tests — PROCEDURAL (can execute), CONCEPTUAL (understands the idea), or TRANSFER (can apply in new situations).

**Cognitive type:** How the student demonstrates understanding — CREATE, IDENTIFY, COMPARE, APPLY, or CONNECT. Each skill maps to one or more cognitive types.

**Tier:** The difficulty/purpose classification of a practice problem — BASELINE (standard), STRETCH (harder), CHALLENGE (above-grade bonus), SUPPORT (confidence builder after struggle), CONFIDENCE (very easy emotional support). Only BASELINE and STRETCH count toward mastery.

**Template:** A reusable problem blueprint that assesses one skill at one tier. At runtime, specific parameter values are selected to generate the problem the student actually sees. Each template carries metadata: skill, tier, component, cognitive type, assessment mode, representation.

**Display-layer decomposition:** For groups with a single skill (e.g., M7 has only `IdentifyEqualGroups`), the student display breaks that one skill into sub-labels using variety dimensions from the content (e.g., "bags," "boxes," "circles with dots"). These are NOT sub-skills in the registry — they're a rendering-layer concept that provides more granular feedback without changing the knowledge graph structure.

---

## The Knowledge Graph

The foundation of everything in this document is a two-layer knowledge graph. Getting this structure right matters more than any individual mastery tracking decision, because the graph is the data structure that every downstream system — mastery tracking, routing, display, spiral review, and eventually multi-curriculum support — queries against.

### Layer 1: The Skill Registry

A universal, curriculum-independent catalog of atomic student capabilities. Each skill is a node that exists regardless of what curriculum a student is in or what order they encounter it.

Example nodes: `CompareData:difference`, `BuildArray`, `LearnFactorProducts`, `ReadGraph:scaled`

Each skill node carries:

| Property | Example | Notes |
|----------|---------|-------|
| `skill_id` | `CompareData:difference` | Global identifier, stable across curricula |
| `component` | CONCEPTUAL | What type of understanding (PROCEDURAL / CONCEPTUAL / TRANSFER) |
| `cognitive_types` | [COMPARE] | Which assessment types can measure this skill |
| `plain_language` | "I can figure out how many more or fewer by comparing groups on a graph" | Student/parent-facing label |
| `student_display` | true | Whether this skill surfaces in the student view (false for parent/architectural nodes) |
| `parent_skill` | `CompareData` | Architectural grouping — parent nodes are hidden from students |

**Key property:** Skill identity is universal. `CompareData:difference` is the same node whether a student encounters it in Unit 1 Module 1 or in a hypothetical alternative curriculum that introduces comparison later. Student performance data is keyed to the skill node, not to the module or curriculum it appeared in.

Currently Unit 1 has 18 skill nodes across 12 modules. Some are leaf skills (directly assessed), some are parent skills (architectural groupings of leaf skills, hidden from students).

### Layer 2: The Curriculum Graph

A curriculum organizes skill nodes into **modules**, defines **paths** between modules, and assigns each skill a **role** within each module where it appears.

The same skill appears in multiple groups within a single curriculum — that's the whole point. `CompareData:difference` might be:
- **INT** (introduced) in Module 1 — first encounter, new learning
- **PRC** (practiced) in Module 4 — reinforcement in a new representation (bar graphs instead of picture graphs)
- **EXT** (extended) in Module 8 — applied in transfer contexts

The role (INT/PRC/EXT) is NOT a property of the skill. It's a property of **(skill × module × curriculum)**. It tells the system the teaching intent: is this the student's first encounter with this capability, or reinforcement, or extension? That intent drives everything downstream — how we assess it, what thresholds apply, how we respond to failure.

The curriculum graph also defines:

| Property | What it controls |
|----------|-----------------|
| **Module membership** | Which skills are in which module. A module typically has 2-6 skills. |
| **Module sequencing** | What order modules come in, and what paths exist between them. |
| **Module stage** | Foundational / Building / Complex — affects pool sizes, minimum attempt thresholds. |
| **Skill role per module** | INT / PRC / EXT — the teaching intent for this skill in this module. |
| **Skill representation per module** | Which visual context (Picture Graphs, Bar Graphs, Arrays, etc.) this skill operates on in this module. |
| **Assessment mode per module** | standalone / embedded — whether the skill has dedicated assessment templates or is assessed within another skill's templates. |

### Why Two Layers

A different curriculum could reuse the same skill nodes but wire them into different modules with different paths. The skill registry doesn't change — `CompareData:difference` is still `CompareData:difference`. The curriculum graph changes — which module introduces it, what role it has, what representation it uses.

If the schema treats (skill × module) as a fixed relationship, adding a second curriculum is a structural migration. If it keeps skill identity (layer 1) separate from curriculum structure (layer 2), a second curriculum is an additive change: new graph, same skill nodes, same student performance data.

**We're building one curriculum for pilot.** But the schema should reflect the two-layer reality now so we don't paint ourselves into a corner.

### What the Schema Needs to Support

**The skill registry** is relatively simple — a table of skill nodes with the properties listed above.

**The curriculum graph** needs to express:
- Groups and their sequence within a curriculum
- Which skills belong to which groups
- The role (INT/PRC/EXT), representation, and assessment mode for each (skill × module) pair
- A `curriculum_id` as a top-level key, even if there's only one value for now

**Student performance data** should be keyed to the skill (layer 1), not to the curriculum structure (layer 2). The attempt record stores what happened: which skill, what the student did, when. The curriculum graph tells you how to *interpret* that data: what role the skill had, what the teaching intent was. This means `spine_status` should be derived from a (skill × module × curriculum) lookup at query time, not stored as a static field on the attempt record.

**Proposed attempt record:**

`(student_id, skill_id, module_id, curriculum_id, representation, tier, correct, timestamp, sequence_position, misconception_id, distractor_selected)`

Where `spine_status` and `assessment_mode` are looked up from the curriculum graph, not stored on the attempt record.

---

## What Sits on Top: Mastery Tracking v2

The knowledge graph is the foundation. Mastery tracking is the primary consumer. Here's what it does with the graph — summarized, not exhaustive. The full spec has pseudocode and detailed query definitions.

### Skill Status Model

Practice produces a per-skill status report instead of a module-level pass/fail. Three states: **Strong** (enough evidence, above threshold), **Needs Practice** (enough evidence, below threshold), **Still Gathering** (not enough evidence to claim). Status is computed per skill per module, using only mastery-eligible attempts (BASELINE + STRETCH tiers).

The "Still Gathering" state matters — making premature claims about an 8-year-old's competency has real cost. The system waits for a minimum number of attempts (starting hypothesis: 4) before labeling any skill.

### Response Gradient

When the status report shows weakness, the system responds with a gradient, not a binary:

1. **Draw ratio adjustment** (default): Reweight the template draw pool — more problems on weak skills, starting at an easier tier. Student stays in practice. Not routing — rebalancing.
2. **Routing** (exception): Lesson repeat, spiral review, or targeted intervention. Only fires on specific triggers — persistent misconceptions, broad failure on newly-introduced skills, or two practice attempts without recovery.
3. **Gate** (rare): Path switch. Existing v1 escalation, retained as last resort.

The response gradient depends on the knowledge graph's role assignments. An INT skill at "Needs Practice" is a more serious signal than a PRC skill at "Needs Practice" — the core concept didn't land vs. reinforcement needs more reps. The gate check specifically requires all INT-status skills to be Strong before advancing.

### Runtime Queries (3 high-priority)

**Q1 — Skill Status + Draw Ratio:** For each skill in the current module, compute status and return a draw weight. This is the hot-path query — runs during practice between every template serve. Simple aggregation over current session attempts.

**Q4 — Routing Trigger Check:** After a full practice attempt, determine if the student needs routing (lesson repeat, intervention) rather than continued draw adjustment. Depends on Q1 + misconception detection + attempt count.

**Q7 — Module Completion Check:** All INT skills Strong + 70% aggregate + transfer gate + minimum attempts. Replaces v1's single-threshold check.

All three queries need: the attempt log (keyed to skill), the curriculum graph (for role lookups), and the session context (attempt count, sequence position).

---

## Logging: What Exists vs. What's New

The existing Fractions telemetry schema (Edtech Telemetry Payload Fields) already covers most of the data the knowledge graph needs. Here's the gap analysis:

### Already in the telemetry schema

| Our requirement | Existing field | Event | Notes |
|----------------|---------------|-------|-------|
| Skill identity | `mastery_skill_id` | `prompt_created` | Maps to our `skill_id`. Need to confirm this is the universal skill node ID, not a module-specific label. |
| Sequence position | `sequence_position` | `answer_submitted`, `step_complete` | Already indexed starting at 1, resets per activity. Covers our trajectory/fatigue detection need. |
| Misconception ID | `misconception_id` | `prompt_created` | Exists. Need to confirm it's also available on `answer_submitted` or joinable via `prompt_id`. |
| Misconception tag | `misconception_tag` | `answer_submitted` | Already on the answer event. |
| Tier | `tier` | `prompt_created`, `answer_submitted` | Already present. |
| Module | `module` | `prompt_created`, `answer_submitted` | Already present. |
| Component | `component` | `prompt_created` | Already present. |
| Cognitive verb | `cognitive_verb` | `prompt_created`, `step_complete` | Already present. |
| Correct/incorrect | `response_correct` | `answer_submitted` | Already present. |
| Attempt number | `attempt_number` | `answer_submitted` | Already indexed starting at 1. |
| Curriculum/path | `learning_path` | `prompt_created` | Exists — need to decide if this is our `curriculum_id` or if we need a separate concept. |
| Remediation level | `remediation_level` | `answer_submitted` | Already present. |
| Toy/representation | `toy` | `prompt_created`, `answer_submitted` | Array of available toys. May partially cover our `representation` concept — need to discuss whether toy = representation or if we need a separate field. |

### New fields needed

| Field | Event | Why |
|-------|-------|-----|
| `distractor_selected` | `answer_submitted` | Which specific MC distractor the student chose. Needed for per-distractor remediation routing. Currently we have `misconception_evidence` (describes the manner of incorrectness) but not the specific distractor option selected. |
| `assessment_mode` | `prompt_created` | `standalone` / `embedded` — whether this prompt is a primary assessment for the skill or embedded within another skill's template. New concept, not currently in the schema. |

### Fields that need discussion

| Topic | Question |
|-------|----------|
| `mastery_skill_id` as universal skill node | Is this ID stable across curricula / learning paths, or is it scoped to a specific path? If it's path-scoped, we need a separate universal `skill_id`. |
| `learning_path` as `curriculum_id` | Does `learning_path` (e.g., "singapore") serve as our curriculum graph identifier? Or do we need a separate `curriculum_id` that maps to the graph structure? |
| `toy` vs. `representation` | `toy` captures the visual tool (bar, number_line). Our `representation` concept is broader — "Picture Graphs," "Bar Graphs," "Arrays." Is `toy` sufficient, or do we need a higher-level `representation` field? |
| `misconception_id` availability at answer time | `misconception_id` is on `prompt_created` but the routing engine needs it at `answer_submitted` time. Is it joinable via `prompt_id`, or should it be denormalized onto the answer event? |

---

## Open Questions for This Review

**1. Two-layer schema feasibility.** Can the schema separate skill identity (layer 1) from curriculum structure (layer 2)? Can `spine_status` be derived from a (skill × module × curriculum) lookup rather than stored on the attempt record? This is the most important architectural question — it determines whether multi-curriculum is additive or a migration.

**2. `mastery_skill_id` as the universal skill node.** The existing telemetry has `mastery_skill_id` on `prompt_created`. Is this ID stable and universal (same ID regardless of which `learning_path` the student is on), or is it scoped to a specific path? If it's universal, it's our Layer 1 skill identity. If it's path-scoped, we need to add a separate universal `skill_id`.

**3. `learning_path` as `curriculum_id`.** The existing `learning_path` field (e.g., "singapore") on `prompt_created` — does this map to our concept of a curriculum graph? Can it serve as the top-level key for the curriculum graph, or do we need a separate `curriculum_id`?

**4. Hot-path query performance.** Q1 (skill status + draw ratio) runs between every template serve during practice. It aggregates current-session attempts by `mastery_skill_id` and `tier`. The data is already on `answer_submitted` events. Does the access pattern work, or does it need a materialized view / session-scoped cache?

**5. `distractor_selected` field.** The one clearly new field. We have `misconception_evidence` (describes the manner of incorrectness) but need the actual distractor option the student picked to drive per-distractor remediation. What's the lift to add this to `answer_submitted`?

**6. `assessment_mode` on prompts.** New enum (`standalone` / `embedded`) on `prompt_created`. This is a content metadata field set by scripting. Any concerns with adding it?

**7. Shadow logging for pilot.** The rollout plan calls for v1 routing with v2 status computations logged as shadow data. This means running the Q1 computation on every practice session and storing what v2 *would have done*. Is there a natural place for this shadow log, or does it need a new event type?

---

## Rollout Sequence

1. **Now:** Alignment on the knowledge graph schema and mastery tracking model.
2. **Pre-pilot (May–Jul):** Implement the two-layer schema (skill registry + curriculum graph). Add the 2 new logging fields (`distractor_selected`, `assessment_mode`). Non-breaking — instruments v1 without changing behavior.
3. **Pilot (Aug–Sep):** v1 routing + v2 shadow logging. System records what v2 would have done.
4. **Analysis (Sep–Oct):** Compare v1 vs. v2 routing decisions against student outcomes.
5. **v2 activation (TBD):** Switch live routing once shadow data validates the model.

---

## What I Need Back

- **Data architecture:** Does the two-layer model (universal skill registry + curriculum graph) work with our current data model? Is `mastery_skill_id` already universal, or path-scoped? Can `spine_status` be derived at query time from the curriculum graph rather than stored on attempts?
- **Platform engineering:** The existing telemetry covers most of what we need. The new fields are `distractor_selected` and `assessment_mode` — what's the lift? Any concerns about Q1 aggregation as a hot-path query between template serves? Where does shadow logging fit?
- **General:** Anything in this schema that'll be painful to change later? Does `learning_path` cover our curriculum concept, or do we need a separate structure?

The full spec (Mastery_Tracking_FDB_v2.md) has pseudocode for every query, the complete hypothesis stack (9 tunable parameters with test methods), and detailed module completion criteria. This summary is the architecture and the asks — the spec is there when you need implementation detail.
