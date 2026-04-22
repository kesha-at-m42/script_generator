# Script Generation: End-to-End Flow

This document covers the full pipeline from raw IM 360 curriculum source through to the final TOML sequences consumed by Lesson Lab (the edtech product students use).

There are two distinct parts: **upstream curriculum adaptation** (human-driven, 8 phases) and **downstream script generation** (code-driven). The upstream work produces the Module Starter Pack, which is the primary input to code.

---

## Part 1: Upstream — Curriculum Adaptation (8 Phases)

**Key rule:** Complete each phase for ALL modules before advancing to the next. Lesson-by-lesson iteration causes analysis paralysis and misses cross-module patterns.

---

### Phase 1: Source Organization

**Goal:** Confirm the IM 360 source data is ready to use.

The raw source is the **IM 360 Curriculum Mapping tab** in each unit's Module Mapping workbook (19 columns, covering all lessons in the unit). If this tab is missing, the extraction pipeline is run against IM 360 HTML source files at `/illustrative_mathematics_360/grade-[X]/teacher/unit-[X]/`.

Legacy note: Grade 3 Units 1–5 were originally adapted from OUR, not IM 360. Their Module Mapping tabs reference OUR data and don't need to change.

---

### Phase 2: Raw Data Extraction

**Goal:** Create a structured dataset of all IM 360 lesson content (if not already extracted).

The 19-column CSV structure covers:
- IM 360 Lesson number, Section, Lesson Title
- Learning Goals (verbatim — includes modality language like "Comprehend (in spoken language)..." — copy as-is)
- Student-Facing Goal (the "Let's..." framing)
- Lesson Purpose (synthesized from per-activity purpose statements in HTML)
- Standards: Building On, Addressing, Building Towards
- Example Scenarios, Key Visual Descriptions
- Practice Problem + Solution
- Mathematical Practices (MPs)
- Student Misconceptions (from "Advancing Student Thinking" sections — what students get wrong, not teacher response prompts)
- Instructional Routines, Responding to Student Thinking, Suggested Centers

IM 360 adds four columns OUR didn't have: Student-Facing Goal, Instructional Routines, Responding to Student Thinking, Suggested Centers.

**Note:** Separate visual pedagogy analysis from CSV extraction. Visual analysis costs ~25–30k tokens/lesson vs. ~10–15k for CSV only — do visuals as a separate pass if needed.

---

### Phase 3: Standards Mapping & Conceptual Spine

**Goal:** See patterns across ALL lessons before making any module decisions.

Two outputs:

**Standards Mapping Table:**
```
| Standard  | Lessons Where It Appears | Pattern Observed              |
|-----------|--------------------------|-------------------------------|
| 3.OA.A.1  | 1, 2, 3, 7, 14           | Introduced→practiced→reviewed |
```

**Conceptual Spine:**
```
| Concept      | Introduced | Developed | Mastered |
|--------------|------------|-----------|----------|
| Equal Groups | L1-2       | L3-5      | L6       |
```

Also track: vocabulary progression (when terms are introduced), visual model progression, standards trajectory (Building On → Addressing → Building Toward).

IM 360 standards are a superset of OUR's — every OUR standard appears in IM 360, plus IM 360 adds per-activity granularity resulting in more codes per lesson. Use IM 360 as the primary source.

---

### Phase 4: Research & Path Decision

**Goal:** Evidence-based decision on whether this unit needs differentiated teaching paths or a unified approach.

**Key question:** Does this unit's content have competing pedagogical methodologies with research support, or do curricula show uniformity?

- If topic has multiple established methodologies (e.g., fractions: Singapore vs. VPSS vs. Montessori) → consider multi-path
- If topic shows curricular uniformity (e.g., data/graphs, basic geometry, place value) → unified approach

**Deliverable: Research Summary Document**

This becomes a formal input to Phase 5:

```
PATH DECISION
[Unified / Multi-path] — [Rationale]

KEY PEDAGOGICAL COMMITMENTS
1. [Research-backed requirement]
2. [...]

CRITICAL MISCONCEPTIONS TO ADDRESS
| Misconception | Where It Appears | How to Address |

RESEARCH-BACKED REQUIREMENTS
- [e.g., Visual-to-numeric bridge in every scale module]

TOOL/INTERACTION IMPLICATIONS
- [e.g., Side-by-side comparison needed for scale selection]

OPEN QUESTIONS FOR TEACHERS
- [e.g., Is 1:5 scale worth the added complexity?]
```

**Why a formal doc:** In Unit 1, research findings lived in chat history. This worked but wasn't systematic — findings didn't reliably influence module decisions. The formal document ensures research actually shapes the architecture.

Unit 1 learning: elementary graphing showed remarkable uniformity across curricula. Research before assuming paths are needed.

---

### Phase 5: Module Mapping

**Goal:** Define the architecture — how IM 360 lessons become modules.

**Inputs:** IM 360 Curriculum Mapping tab, Standards Mapping, Research Summary, Universal Mastery Tracking Framework, Edtech Activity Queue Rulebook.

The **Module Mapping workbook** is a multi-sheet Excel file. Sheets: Module Mapping, Important Decisions, Misconceptions, Conceptual Spine Analysis, Conceptual Development, Standards Mapping, Original Curriculum Mapping.

**Principles:**
- Typical count: 10–15 modules per unit
- ONE primary concept per module (no "and")
- Clear progression with dependencies mapped
- No redundant overlap between modules

**Transformation rules** (source lessons → modules):
- One lesson may SPLIT across multiple modules
- Multiple lessons may COMBINE into one module
- Some content may be ELIMINATED as redundant
- New content may be ADDED to fill gaps
- Order may be REORGANIZED for better flow

**Module Mapping Table:**
```
| Module | Title | IM 360 Lessons (+ Transformation Tag) | Learning Goal | Standards |
|--------|-------|---------------------------------------|---------------|-----------|
| M1     | ...   | L1, L2 (partial)                      | ...           | 3.MD.B.3  |
| M2     | ...   | L2 (partial), L3                      | ...           | 3.MD.B.3  |
```

**Checkpoint:** Get teacher/SME feedback on module architecture before proceeding. Unit 1: teacher feedback led to combining M2a/M2b and swapping M9/M10. Don't skip this.

---

### Phase 6: Toys/Interactables Specs (FDBs)

**Goal:** Define the tool catalog — what buildable interactive components exist and what they can do.

**Audience:** Engineering (what to build), UX (how it works and looks).

**Output:** One Feature Design Brief (FDB) per buildable component (e.g., Bar Graphs, Picture Graphs, Number Line). These are the authoritative specs for what each toy is capable of, and they become a direct input to the toy glossary in the downstream script generation pipeline.

**Source:** FDBs live in a Notion database — see the [Toy/Tool Specs database](https://www.notion.so/ocpgg/c92bd6781875447fa9fd72827e50ccee?v=6581c5e4a3ba4eaf97cd1f05c313b2e7).

**Why this comes before Tool Flow:** You can't write "Picture Graph: pre-filled → partial → blank" until you've defined what the Picture Graph tool is capable of.

**Principles:**
- Organize by buildable component (Bar Graphs, not "Data System")
- Consolidate similar tools — don't define 5 separate bar graph variants
- Specify capabilities, not implementation (describe what it does, not how to code it)
- Include all interaction patterns (hover, click, drag, tap, display)

Every toy referenced in the Module Mapping must have an FDB. Every FDB must support the scaffolding progressions planned in Phase 7.

---

### Phase 7: Toy Flow Document (TVP)

**Goal:** Specify HOW toys are deployed in each module with scaffolding progressions.

**Audience:** Engineering and UX/UI Design.

**Also referred to as TVP (Tool/Visual Plan)** in the gate evaluation agents — same document.

**Relationship to Phase 6:** Phase 6 = "What tools exist?" Phase 7 = "How are those tools used per module?"

**What Toy Flow contains:**
- Which toys are used in each module phase (Warm-up / Lesson Early/Mid/Late / Exit Check / Practice / Synthesis)
- Toy configurations and modes per phase (e.g., "full grid → outline only")
- Scaffolding progressions: how support decreases across Early → Mid → Late
- Interaction patterns: drag-drop, click-select, tap-to-reveal, display only
- Observable student actions at each scaffolding level
- Data constraints (number ranges, factor limits, example values)
- Key transition points between adjacent modules
- SME review questions
- **Key beats** (1–3 per module max) — illustrative teaching moments where the concept lives or dies on a specific interaction

**What Toy Flow does NOT contain:** Full guide dialogue, MC answer options, remediation scripts, numbered activity sequences, timing estimates.

**The Key Beat test:** Include a moment only if "if someone changed this, it would break the pedagogical design."
- ✅ Include: "Same rectangle displayed with both grid sizes simultaneously — student sees more smaller squares fill the same space" (defines the concept)
- ❌ Exclude: "Guide says: 'What do you notice about Grid A and Grid B?'" (one of many valid prompts — Starter Pack territory)

Key beats are ONE sentence. Three lines of guide dialogue = a script, not a beat.

Template: `docs/references/Starter Pack Generation Experiment - Plugins/Toy Flow Module Template.md`

**Scaffolding precision matters:** "Support decreases across activities" is not enough. Specify what decreases:
- "Row highlighting: auto → tap-activated → off"
- "Equation Builder slots: pre-labeled → unlabeled → independent"

---

### Phase 8: Module Starter Pack

**Goal:** Create the curriculum spine optimized for AI script generation.

**Audience:** Claude (the script generation pipeline).

A Starter Pack is NOT the final script. It specifies what should happen pedagogically so that scripts, animations, and toy behaviors can be built from it.

**SP Sections (§1.0–§1.10):**

| Section | Purpose |
|---------|---------|
| 1.0 The One Thing | Core learning insight, CRA stage, biggest risk |
| 1.1 Learning Goals | Curriculum alignment, standards cascade, exit check tests |
| 1.2 Scope Boundaries | Must-teach vs. must-not-include |
| 1.3 Vocabulary Architecture | Staging by phase, terms to avoid |
| 1.4 Misconceptions | Global IDs, trigger behaviors, prevention strategies |
| 1.5 Toy Specifications | Module-specific configuration of interactive manipulatives |
| 1.6 Warmup | 3–5 min activation (2–3 interactions) |
| 1.7 Lesson | 8–12 min main teaching (6+ interactions, CRA sequence) |
| 1.8 Exit Check | 3–5 min formative assessment (3 problems) |
| 1.8.5 Practice Inputs | Distribution targets, skill tracking, spiral review |
| 1.9 Synthesis | 5–7 min closure and preview of next module |
| 1.10 Key Design Decisions | Non-obvious pedagogical trade-offs |

Sections §1.0–§1.5 are the **Backbone** — the pedagogical foundation authored first (Task 1), before any phase specs.

**Design principles for Claude navigation:**
- Section numbering for easy reference
- Phase-specific guidance consolidated (not scattered across sections)
- Module-specific constraints only — universal rules live in the Guide Design Prompt
- Clear scope fences to prevent Claude from drifting

**SP authoring is structured as 4 tasks, each ending with a gate evaluation:**

```
Task 1: Backbone (§1.0–§1.5)        → Gate 1
Task 2: Warmup + Lesson (§1.6–§1.7) → Gate 2
Task 3: EC + Synthesis (§1.8–§1.9)  → Gate 3
Task 4: Assembly + Notion push       → Gate 4
```

Each gate runs a 3-layer evaluation:

**L1 — Python checkers** (deterministic, 8 total): `sp_structure_check.py`, `sp_vocab_scan.py`, `sp_voice_scan.py`, `sp_interaction_check.py`, `sp_timing_estimate.py`, `sp_toy_consistency.py`, `sp_dimension_track.py`, `sp_module_map_check.py`

**L2 — LLM agents** (judgment-based, run in parallel):

| Agent | Gates | Scope |
|-------|-------|-------|
| `m42-gate1-eval` | 1+ | Backbone completeness |
| `m42-source-fidelity` | 1+ | SP vs. TVP (Toy Flow doc) vs. Module Mapping alignment |
| `m42-pedagogy-eval` | 1, 4 | Pedagogical intent |
| `m42-warmup-eval` | 2+ | Warmup phase quality |
| `m42-lesson-eval` | 2+ | CRA progression, interaction design |
| `m42-guide-prompt-eval` | 2+ | Guide/Prompt independence |
| `m42-ec-practice-eval` | 3+ | Exit check alignment, practice inputs |
| `m42-synthesis-eval` | 3+ | Synthesis connection tasks, identity closure |
| `m42-kdd-eval` | 3+ | KDD completeness |
| `m42-voice-eval` | 4 | Guide voice authenticity |
| `m42-cross-module-eval` | 4 | Cross-module continuity |
| `m42-requirements-eval` | 4 | Final requirements compliance |

Agent counts: G1=3, G2=6, G3=8, G4=12. **L3** = `sp-gate-eval` orchestration skill coordinates all agents and feeds L1 findings to L2. (`m42-pedagogy-audit` is being integrated separately; not counted in the 12 main agents.)

**`m42-pedagogy-audit`** is a cross-cutting agent that catches design issues phase-scoped agents miss (they evaluate one phase in isolation). It checks: arc coherence, whether interactions deliver their stated purpose (Guide must not pre-answer), interaction type selection, cross-document source verification (TVP ↔ Module Mapping ↔ SP), cognitive readiness at transitions, MC distractor quality, and internal consistency.

**Gate verdict options:** PASS / PASS WITH CONDITIONS (no CRITICALs, proceed) / FAIL (CRITICALs present, must revise before advancing).

**When a gate fails — the iteration loop:**

Findings are triaged into three categories:
- **Category A (auto-fix):** Structural issues (heading levels, ordering, missing markers) — applied mechanically by the `sp-fix` tool
- **Category B (semi-auto):** Clear fix patterns needing confirmation (section moves, vocab staging gaps, superlative praise)
- **Category C (manual):** Pedagogical judgment calls (learning goal drift, missing misconceptions, tone) — human edit required

The loop:
1. Run `sp-fix` on Category A/B findings
2. Re-run `sp-quick-check` (L1 only, ~5 seconds) to verify
3. Fix remaining Category C findings manually in the local `.md` file
4. Re-run `sp-gate-eval` at the same gate (not the next one) until verdict is PASS or PASS WITH CONDITIONS
5. Persist the evaluation report as `G3U{X}M{N}_Gate{N}_Evaluation.md`
6. Advance to the next task

**Key rules:** Always fix L1 (structural) CRITICALs before running L2 agents — L1 takes ~5 seconds, L2 takes minutes. Draft and revise locally; Notion push happens only at Gate 4. No path to bypass a FAIL gate.

**Working Notes — cross-module baton**

File: `G3U[X]M[XX]_Working_Notes.md`. Updated after every Task 4 (required); read by the next module's Task 1. Tracks:
- Vocabulary introduced, with the interaction ID where each term was first used
- Exact §1.9 bridge text (copied verbatim — next module's Warmup opens from here)
- Dimension values and toy configurations for this module
- Gate eval artifact paths (file references to actual evaluation reports) — if a path doesn't exist, the gate hasn't run
- Open Author Flags

**Post-compaction fabrication risk:** In a long chat that has been compacted, the model may claim a gate passed when it didn't. Gate eval artifact paths are the defense — they must resolve to real files. Verify before advancing.

The SP is considered ready for Phase A ingestion once it passes Gate 4.

---

## Part 2: Downstream — Script Generation (3 Phases)

---

### Phase A: Ingestion + Toy Glossary Creation

**Inputs:** Notion Starter Pack, Phase 6 FDBs, Phase 7 Toy Flow doc.

This phase pulls the Starter Pack from Notion, splits it into per-phase files, and builds the toy glossary that the generation pipeline will use to understand what each toy can do.

**`starter_pack_ingestion` pipeline:**

1. **`notion_pull_starter_pack`** — fetches Notion page, converts blocks to Markdown → `_starter_pack_ref.md`
2. **`phase_splitter`** — splits by `## WARMUP`, `## LESSON`, `## EXIT CHECK`, `## SYNTHESIS` headings → four `.md` files
3. **`starter_pack_json_loader`** — extracts structured metadata (vocabulary, learning goals, variables, misconceptions) → `starter_pack.json`

**Toy glossary creation** (`toy_spec_loader`):

Runs before the core generation step (`section_structurer`) so that every section knows exactly what toys are available and how they're configured. Steps:
- Scans the spec for toy references (e.g., "picture graph", "bar model")
- Looks up matching FDBs from the canonical `toy_specs/` directory using a phrase map (`glossary.md`)
- Uses Claude as a fallback for unmatched toy descriptions
- Builds a global `toy_specs` dictionary of all toys in the module, plus a `workspace_specs` field per section listing the specific toys active in that interaction

The glossary is built from two sources: Phase 6 FDBs (what each toy can do) and SP §1.5 Toy Specifications (how each toy is configured for this specific module).

All files land in `units/unit{N}/module{M}/`.

---

### Phase B: Generation

One pipeline per phase (warmup, lesson, exitcheck, synthesis). All four run in parallel via `cli/run_module.py`. Defined in `config/pipelines.json`, executed by `core/pipeline.py`.

Each run creates a timestamped output directory: `units/unit{N}/module{M}/path{c}/{pipeline}/v{YYYYMMDD_HHMMSS}/`

**Pipeline steps for the lesson phase:**

| Step | Type | What it does |
|------|------|--------------|
| `spec_splitter` | formatting | Splits `lesson.md` into individual interaction sections by heading |
| `starterpack_parser` | AI (batch) | Parses each section into structured fields; assigns stable IDs |
| `toy_spec_loader` | formatting | Builds toy glossary; enriches each section with its active toys |
| `glossary_drift_checker` | formatting | Validates vocabulary against canonical glossary; emits drift report |
| `section_structurer` | AI (batch) | **Core generation step** — Claude converts each spec section into scene beats, dialogue beats, and prompt beats organized into steps |
| `id_stamper` | formatting | Stamps stable beat IDs onto the generated structure |
| `dialogue_extractor` | formatting | Pulls all dialogue beats out for a focused rewrite pass |
| `dialogue_rewriter` | AI (batch) | Claude rewrites each dialogue beat for voice quality and warmth |
| `dialogue_merger` | formatting | Merges rewritten dialogue back into section objects |
| `remediation_filter` | formatting | Identifies sections that have student prompts (need error paths) |
| `remediation_generator` | AI (batch) | Claude generates incorrect-answer variants for each prompt (Light/Medium/Heavy severity) |
| `remediation_merger` | formatting | Merges remediation back in; stamps validator IDs |
| `notion_push` | formatting | Pushes final JSON to Notion |

**Formatting vs. AI steps:** Formatting steps are deterministic, fast, and free. AI steps call Claude in batch mode (one call per section). The split means the pipeline can be re-run from any step — changing the dialogue rewriter prompt doesn't re-run structure generation.

**Output per phase:** `lesson_sections.json` — an array of section objects:

```
sections[
  {
    id: "s1_1_most_votes",
    steps: [
      {
        beats: [
          { type: "scene", ... },      // what appears on screen
          { type: "dialogue", ... },   // what the Guide says
          { type: "prompt", ... },     // student interaction
          { type: "on_correct", ... }, // brief confirmation (Heavy-path students skip this)
          { type: "remediation", ... } // error paths (Light/Medium/Heavy)
        ]
      }
    ]
  }
]
```

Each step is a "do-together" block that ends at a student input pause.

---

### Phase C: Review, Stitching, and Ingestion into Lesson Lab

Phase B's final step pushes the generated JSON to Notion for human review. Phase C takes over from there.

**1. Human review in Notion**

The script is rendered in Notion as a human-readable callout-based layout. Reviewers edit dialogue, fix wording, or flag issues directly on the page.

**2. Pull from Notion** (`notion_pull` step / `utils/notion.py`)

After review, changes are pulled back from Notion into `pull.json`. The pull reconciles reviewer edits from the rendered callout blocks back into the JSON structure, merging them with the original raw JSON footer the push embedded.

Output: `tracked_scripts/u{N}/m{N}/{phase}/step_{N}_pull/pull.json`

**3. Extract to tracked_scripts** (`fixes/stitch_pipeline_outputs.py`)

The latest pipeline version output is extracted into `tracked_scripts/u{N}/m{N}/{phase}/` — a stable, version-controlled snapshot of the approved script. This is the canonical source used for TOML conversion and Lesson Lab deployment.

**4. Convert to TOML** (`steps/formatting/toml_sequence_writer.py`)

Converts `pull.json` into a `.toml` sequence file the Lesson Lab can consume. The TOML:
- Assigns section keys (`section_100_slug`) and step keys (`step_100_slug`)
- Maps dialogue beats → `dialogue = "..."` fields
- Maps prompt beats → `components = ["PromptComponent"]`
- Drops scene beats (handled by the app engine separately)
- Applies `[vocab]word[/vocab]` tagging for vocabulary terms
- Stamps `_toml_key` back into `pull.json` for traceability

Output: `tracked_scripts/u{N}/m{N}/{phase}/step_{N}_toml/{phase}-script.toml`

**5. Copy to Lesson Lab** (`SEQUENCES_DIR` env var)

The TOML is copied to `SEQUENCES_DIR/unit{N}/module_{N}/{phase}-script.toml` — the Lesson Lab repo. This is the final handoff. The Lesson Lab reads these TOML sequence files directly to drive the Godot app's lesson execution.

Note: output files use LF line endings (Lesson Lab requirement — see launchpad repo dependency).

---

## App Architecture (Lesson Lab)

Understanding how the JSON gets executed:

- **Guide**: Narrated audio character who teaches (`dialogue` field). Conversational, warm. Must work standalone — cover the Prompt, student can still engage. Audio is generated via TTS inside the Lesson Lab — this pipeline only produces the dialogue text.
- **Prompt**: Written on-screen instruction (`prompt.text`). Formal, worksheet-style. Must work standalone — cover the Guide audio, student can still complete the task.
- **Toys**: Interactive visual manipulatives (Bar Model, Grid Rectangles, Number Line, Equation Builder, etc.)
- **Remediation**: 3 levels — Light / Medium / Heavy. Students on the Heavy path **skip On Correct entirely** and go directly to the next interaction. On Correct must never carry load-bearing content.
- **Events** `[event:...]`: Animation triggers embedded in dialogue — stripped before scripting, invisible to the eval pipeline.
- **Scenes**: `Lesson` vs. `ZoomedOut`. Synthesis always opens in ZoomedOut — a deliberate UX shift.

**4 interaction patterns:**

| Pattern | Description |
|---------|-------------|
| 1 — Student Action | Guide + Prompt both required; student submits an answer |
| 2 — Teaching-Only | Guide only; ends with `* **No student action.**` |
| 3 — System-Driven | Spec table + `On Complete:` block; student observes or confirms |
| 4 — Think-Aloud | Guide models cognitive process; `[PLANNING]`/`[ATTENTION]`/`[SELF-CHECK]` tags are authoring-only, stripped before scripting |

**Student action vocabulary (closed set):** `Select (single)`, `Select (multiple)`, `MC (single)`, `MC (multiple)`, `Shade`, `Place tick`, `Place point`, `Drag label`, `Drag to build`, `Drag to group`, `Fill blank`, `Type number`, `Enter number`

**Guide/Prompt interaction types (A/B/C):**

| Type | Structure | When to Use |
|------|-----------|-------------|
| **A — Teaching Only** | Dialogue only, no prompt field | Concept intro, reflection, transitions, identity moments, Synthesis (70–80% of it) |
| **B — Minimal Teaching** | Dialogue = brief context + complete instruction; Prompt = complete instruction | Routine practice after mastery, simple continuation |
| **C — Substantial Teaching** | Dialogue = extended teaching + complete instruction; Prompt = complete instruction | First application of concept, complex tasks, discovery moments |

Both dialogue and prompt must work standalone (independence rule): cover the prompt → student hears audio → can complete task; mute audio → student reads prompt → can complete task. Teaching content goes only in dialogue, never in the prompt field.

---

## The Full Picture

```
IM 360 HTML source
    │
    ├─ Phase 1–3: Extract & map (CSV, Standards Map, Conceptual Spine)
    ├─ Phase 4:   Research → Research Summary (path decision, misconceptions)
    ├─ Phase 5:   Module Mapping (architecture + teacher review)
    ├─ Phase 6:   Toys/Interactables Specs / FDBs (tool catalog + capabilities)
    ├─ Phase 7:   Toy Flow Doc (how toys deploy per module, scaffolding)
    └─ Phase 8:   Module Starter Pack (§1.0–§1.10, authored in Notion)
                  + Gate evaluation (4 tasks × 3-layer eval: L1 Python + L2 LLM agents + L3 orchestration)
                        │  SP passes Gate 4
                        ▼
         ── Phase A: Ingestion + Toy Glossary ──
              starter_pack_ingestion
              (Notion → lesson.md, starter_pack.json)
              toy_spec_loader
              (FDBs + Toy Flow + SP §1.5 → toy glossary)
                        │
                        ▼
         ── Phase B: Generation ──
              lesson_generator_dialogue_pass  (× 4 phases, parallel)
              spec_splitter → starterpack_parser → toy_spec_loader
              → section_structurer   (Claude: scene/dialogue/prompt beats)
              → dialogue_rewriter    (Claude: voice polish)
              → remediation_generator (Claude: error paths)
              → notion_push
                        │
                        ▼
         ── Phase C: Review, Extract & Lesson Lab Ingestion ──
              Notion review → notion_pull → pull.json
              → extract latest version → tracked_scripts/
              → toml_sequence_writer → {phase}-script.toml
              → copy to SEQUENCES_DIR (Lesson Lab repo)
```
