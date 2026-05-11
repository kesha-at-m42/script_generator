## 👥 User Stories

1. As a **student**, when I encounter a new visual tool, I get a brief, hands-on introduction that lets me discover how it works before I'm expected to use it for learning — I never feel lost staring at something I've never seen.
2. As a **content writer**, I have a clear structure (name → recognize → manipulate → bridge) and know that Tool Introductions vary in depth: some tools need 3 minutes of "here's a circle," others need 6+ phases of discovery (like base-10 blocks where the block-to-block relationships must be *built* through interaction).
3. As a **developer**, I implement a `tool_exposure_registry` that tracks which tools each student has seen, and a prerequisite check that fires before any activity requiring an unseen tool — inserting the appropriate Tool Introduction automatically.
4. As a **teacher/parent**, I can see that the system never assumes prior experience — whether my student is a homeschooler who's never touched a manipulative or a classroom kid who's used them for years, the system checks and adapts.
5. As a **product**, I have a scalable approach to tool onboarding that works across units, paths, and assessment contexts — not just path switches.

---

## 🔎 Overview

**Position in Flow:** Prerequisite gate — inserts automatically before any activity that requires a tool the student hasn't seen
**Duration:** 3-4 minutes (simple recognition) to 6-10 minutes (discovery-based, like base-10 blocks)
**Core Function:** Ensure a student can recognize and manipulate a visual tool before they're expected to use it for learning

### Tool Introduction Is Not a Pool Activity

Unlike Fluency, Test Prep, or Spiral Review, Tool Introduction is not something the queue selects from the activity pool. It's a **prerequisite check** that fires when the queue has already selected another activity:

```
Queue selects next activity (e.g., Module 6, Spiral Review, Test Prep)
    ↓
System checks: Does this activity require tools?
    ↓
For each required tool: Is it in this student's tool_exposure_registry?
    ↓
    YES → Proceed to activity
    NO  → Insert Tool Introduction for that tool → Then proceed
```

### When Tool Introductions Trigger

| Context | Example | Why |
| --- | --- | --- |
| **New unit starts** | Unit 3 uses base-10 blocks. Student has never seen them. | Can't assume any prior manipulative experience (homeschool, etc.) |
| **Path switch** | Student switches from Path B (bars) to Path C (grids/circles) | New path uses different visual tools |
| **Spiral Review transfer section** | Transfer section uses alternate path tools | Student may never have seen the other path's representations |
| **Test Prep representational bridge** | Test Prep introduces non-curriculum visuals (shaded circles, set models) | Test formats use tools not in Level's instructional modules |
| **Cross-unit tool reuse** | A tool from Unit 2 appears in Unit 4 but student skipped Unit 2 | Non-linear progression paths may skip tool exposure |
| **Assessment prep** | State test format requires gridded response interaction | Tool-specific input methods need introduction |

### What Tool Introduction Is NOT

- **Not a lesson.** It doesn't teach the math concept — it familiarizes the student with the tool they'll use to learn the concept.
- **Not mastery-gated.** Students don't "pass" a Tool Introduction. They experience it and proceed.
- **Not optional.** If the registry says unseen, the introduction runs. (But see the recognition-first principle below — it may be very brief if the student clearly already knows the tool.)

---

# Key Mechanics

### Tool Exposure Registry

A per-student record of which visual tools they have been introduced to.

| Field | Description |
| --- | --- |
| `student_id` | Student identifier |
| `tool_id` | Unique tool identifier (e.g., `bar_model`, `circle_fraction`, `base10_blocks`, `number_line`, `grid_array`, `set_model`, `gridded_response`) |
| `first_seen` | Timestamp of first Tool Introduction |
| `context` | What triggered it (new_unit, path_switch, spiral_transfer, test_prep) |
| `introduction_type` | Simple (3-4 min) or Discovery (6-10 min) |

**Registry check fires:**

- Before every Module block (W→L→EC) — checks tools required for the module
- Before every Spiral Review — checks tools required for the transfer section
- Before every Test Prep session — checks tools required for the content pool
- After every path switch — checks tools required for the new path

**Engineering note:** The registry should be populated from the tool requirements in Module Starter Packs, Spiral Review scripts, and Test Prep content tags. Each activity type declares its required tools; the queue checks the student's registry against that declaration.

### Two Introduction Types

Not all tools need the same onboarding. A shaded circle for Test Prep needs 3 minutes. Base-10 blocks need a full discovery sequence.

### Simple Introduction (3-4 minutes)

For tools that are visually intuitive and don't require conceptual relationship-building.

| Phase | Duration | What Happens |
| --- | --- | --- |
| 1. Name & Connect | ~30 sec | Name the tool, connect to something familiar. "You've been using bars. Here's a circle — works the same way, different shape." |
| 2. Recognition | ~60 sec | Student identifies features. "Tap the part that shows thirds." Guide shows tool with narration. |
| 3. Guided Manipulation | ~90 sec | Student replicates with full support. Heavy scaffolding acceptable. |
| 4. Bridge to Context | ~45 sec | "You'll see this in reviews and tests. Same fractions, just different pictures." |

**Applies to:** Alternate path tools (circles when you've used bars, bars when you've used grids), test format representations (shaded circles, set models), simple format differences (gridded response input).

### Discovery Introduction (6-10 minutes)

For tools where the relationships between components must be *built through interaction*, not assumed.

**Applies to:** Tools with internal structure that students can't intuit from visual inspection alone. The base-10 blocks example is the prototype: the student must *discover* that 10 ones = 1 ten = 1 rod, that 10 tens = 1 hundred = 1 flat. This can't be told — it must be experienced.

**Structure:** Multi-phase discovery sequence. No fixed template — the phases depend on what relationships need to be built. The base-10 blocks example has 6 phases (meet the ones-cube → discover the ten-rod → discover the hundred-flat → size comparison → connect to notation → efficiency motivation).

**Design principles for discovery introductions:**

- **Discovery over instruction.** The student should feel like they're exploring, not being taught. "Watch what happens..." not "Let me explain..."
- **Interaction builds the relationship.** Dragging, snapping, separating, counting — the student's actions create the understanding. Narration confirms what they just experienced.
- **Reversibility matters.** If something snaps together, the student should be able to take it apart. This proves the equivalence isn't magic — it's structure.
- **One MC checkpoint per major relationship.** After each discovery, a quick MC question verifies the student tracked the insight. These are diagnostic, not gating.
- **End with motivation.** The final phase should answer "why does this tool matter?" — like the efficiency beat in the base-10 blocks example (324 individual cubes → grouped into 3 flats + 2 rods + 4 cubes).

### Recognition-First Language

This is a 1:1 product. We never know what a student has or hasn't seen outside Level. A homeschooler may have never touched a physical manipulative. A classroom student may have used fraction circles since first grade.

**Recognition-first language** means we never assume unfamiliarity, but we always provide the introduction.

| Use | Avoid |
| --- | --- |
| "You might recognize this..." | "Let me introduce..." |
| "This might be new to you..." | "You haven't seen this before..." |
| "Here's a circle — it works like the bars you've been using" | "This is called a fraction circle" (cold introduction) |
| "Same fractions, different picture" | "This is a new tool" |

**Never:** "Some of you might..." — this is 1:1 interaction, not a classroom.

**If the student clearly already knows the tool** (e.g., answers the MC checkpoint instantly and correctly), the system should note this in the registry and may abbreviate future introductions for similar tool types. But the first introduction always runs in full.

### Guide Role

| Phase | Guide Mode |
| --- | --- |
| Simple Introduction | Light instruction. Conversational. "Here's a circle — works the same way." |
| Discovery Introduction | Facilitative. "Watch what happens..." / "What do you notice?" / "How many ones is that?" |
| MC Checkpoints | Brief and diagnostic. Not remediated heavily — if wrong, Guide clarifies and moves on. |
| Bridge to Context | Forward-looking. "You'll use this in..." |

**Guide is NOT in full instructional mode.** Tool Introductions are about familiarization, not teaching the math. The Guide's energy should be curious and exploratory, not authoritative and explanatory.

### Queue Integration

Tool Introduction is a **prerequisite gate**, not a pool activity. It modifies the queue's selection, not the selection itself.

**Queue engine pseudo-logic:**

```
selected_activity = queue.select_next()

required_tools = selected_activity.get_required_tools()
unseen_tools = [t for t in required_tools
                if t not in student.tool_exposure_registry]

if unseen_tools:
    for tool in unseen_tools:
        queue.insert_before(selected_activity,
                           ToolIntroduction(tool))
    # Brain Break eligible between Tool Intro and selected activity

proceed(selected_activity)
```

**Placement rules:**

- Tool Introduction always runs immediately before the activity that needs it
- Brain Break eligible between Tool Introduction and the subsequent activity (standard rules)
- If multiple unseen tools are required, introductions run sequentially with breaks between
- Tool Introduction counts toward educational time
- Tool Introduction cannot be skipped

**Priority:** Tool Introduction is not in the priority stack — it's a modifier. It fires whenever needed, regardless of what activity was selected. Even Interventions get a Tool Introduction first if they use an unseen tool (unlikely but architecturally possible).

### What Gets Tracked

| Data Point | Purpose | Mastery Impact |
| --- | --- | --- |
| Tool introduced (tool_id + timestamp) | Populates registry | None |
| MC checkpoint responses | Diagnostic — did they track the relationship? | None |
| Time spent per phase | Engagement signal | None |
| Context (why triggered) | Analytics — how often do path switches vs. new units trigger introductions? | None |

**Mastery impact: None.** Tool Introduction is infrastructure, not assessment.

---

## 👨‍💻 Development Phases

### Phase 1: Registry + Simple Introductions

- Build tool_exposure_registry (per-student, per-tool)
- Implement prerequisite check in queue engine
- Create Simple Introduction template (4 phases, 3-4 min)
- Write Simple Introductions for Unit 5 path switch tools (bars ↔ circles/grids)
- Queue insertion logic for path switch context

### Phase 2: Discovery Introductions + Cross-Context

- Create Discovery Introduction framework (variable-length, multi-phase)
- Write discovery sequences for tools requiring relationship-building (base-10 blocks, etc.)
- Extend prerequisite check to Spiral Review transfer sections
- Extend prerequisite check to Test Prep bridge sessions
- Tool requirement tagging on all activity content

### Phase 3: Optimization

- Abbreviation logic: if student demonstrates instant familiarity (MC correct in <2 sec), flag for shorter introductions on similar tool types
- Cross-unit tool reuse tracking (student used number lines in Unit 2 — skip introduction in Unit 4)
- Analytics: which tools need introductions most often? Which contexts trigger them?
- Teacher visibility: "Your student received a tool introduction for base-10 blocks before starting Unit 3"

---

## 📝 Notes

## References

**Internal:**

- Activity Queue FDB / Rulebook v6 (queue integration, prerequisite gate model)
- Path Switch Protocol FDB (path switch trigger for tool introductions)
- Spiral Review FDB (transfer section tool requirements)
- Test Prep Activity FDB (non-curriculum visual tool requirements)
- Module Starter Packs (tool requirements per module)
- Engineering Specifications: Visualizations (tool catalog)
- Unit 3 Tool Flow: Base-10 Blocks Introduction (discovery introduction example)

### Scope & Constraints

**In Scope:**

- Tool exposure registry design
- Queue prerequisite check logic
- Two introduction types (Simple + Discovery) with structure
- Recognition-first language patterns
- Trigger contexts (path switch, new unit, spiral transfer, test prep, assessment)
- Guide role during introductions

**Out of Scope:**

- Specific Tool Introduction scripts (separate content docs per tool)
- Tool catalog / engineering specs (see Visualizations documentation)
- Tool Flow per module (see Phase 7 of Unit Curriculum Adaptation Process)
- Within-module scaffolding progressions (Tool Introduction is pre-module only)

**Constraints:**

- Cannot be skipped — if registry says unseen, introduction runs
- Discovery introductions cannot be abbreviated on first exposure (recognition-first principle)
- 1:1 language only — never "some of you" or classroom assumptions
- MC checkpoints are diagnostic, not gating — wrong answers get clarification, not remediation
- Tool Introduction teaches the tool, not the math — no concept instruction during introduction

### Open Questions

| Question | Current Hypothesis | Confidence | To Validate |
| --- | --- | --- | --- |
| Should the registry carry over across school years? | Yes — if you've seen base-10 blocks, you've seen them | Medium | Students may forget tools over summer |
| How to handle students who clearly already know a tool? | Run introduction anyway (first time); abbreviate similar tools later | Medium | Might feel condescending to experienced students |
| Should Test Prep non-curriculum tools get Simple or Discovery introductions? | Simple — these are representational variants, not new tool relationships | High | Unless a test format tool has complex internal structure |
| Maximum number of Tool Introductions in one session? | Cap at 2 — more than that means the session is all onboarding | Low | Depends on how often this actually happens |
| Should Tool Introduction problems count toward misconception validators? | No — it's not assessment | High | MC checkpoints are too few and too scaffolded to be meaningful signals |
