# MODULE STARTER PACK — COWORK GUIDANCE

**Version:** 04.16.26 v4.11
**Purpose:** Guides Cowork through producing a complete Module Starter Pack. Four drafting tasks, four author review gates, automated evaluation pipeline at each gate. Built from lessons learned producing G3U2 M1–M12. v4 integrates the 3-layer plugin architecture (L1 Python checkers, L2 LLM agents, L3 orchestration skills) and Notion sync tooling proven during M7 evaluation. v4.1 adds Edit Reconciliation Pass and Data-Level Constraint Audit to Task 1, from M8 process assessment. v4.2 adds Activity Queue Compliance patterns (#43-45) and Module-Specific Action Items section from Pedagogical Flow Analysis of M8-M10. v4.3 adds Template Compliance patterns (#46-48) from M8-M12 deviation audit; updates Notion push process to agent-creates-shell/human-pastes-content (Known Pattern #32). v4.4 restructures Known Patterns into gate-scoped shortlists — each Task/Gate section now has a "Patterns to enforce" callout with just the relevant pattern numbers; full appendix remains as numbered reference. Adds Known Pattern spot-check at Gate 2 and full compliance audit at Gate 4 targeting patterns L1/L2 can't cover. Adds Pattern #52 (Options not in Prompt). v4.5 packages the evaluation pipeline as a Cowork plugin (`m42-starter-pack-eval.plugin`) — agents now run as real subagents with isolated context windows instead of prompt templates in the main chat. Updates plugin architecture section and session setup accordingly. v4.6 adds Known Patterns #60 (V4 `[vocab]` tag false positive), #61 (lesson-eval CRA labeling advisory), #62 (gate eval persistence at every gate). Adds gate eval persistence instructions at Gates 1–3. From M1/M2 process review. v4.7 narrows `[vocab]` markup (#56) to NEW and STATUS-CHANGE terms only — established terms from prior modules no longer tagged. Density target (#57) scoped to match. From M3 process review (tag density inflating On Correct word counts). v4.8 adds Known Patterns #63 (interaction heading format — `### Interaction X.Y:` required, I18 "0 found" = structural CRITICAL) and #64 (Identity Closure forward-looking language permitted per Synthesis Playbook §3F). #63 added to Gate 2 shortlist. Both added to Gate 4 shortlist and audit table. From M4 process review (heading format self-reinforcing FP loop, voice-eval vs synthesis-eval closure dispute). v4.9 adds Known Patterns #65 (FP drift — do not auto-inherit L1 false positive classifications from prior modules) and #66 (MM0 checker path configuration per unit). #65 added to Gate 2 shortlist. Both added to Gate 4 shortlist and audit table. From M5 process review (FP drift on ST9/ST11/ST10, MM0 checker broken for G3U4). v4.10 adds Known Patterns #67 (verify §1.5 toy modes against Toy Flow Toy Requirements table — manual check at Gate 1) and #68 (spot-check §1.5 progression tables against actual phase implementations — manual check at Gate 3). Adds "Patterns to enforce" shortlists to Gate 1 and Gate 3 sections (previously only Gate 2, Gate 4, and Task-level had shortlists). From M5 evaluation chat reconciliation (three systematic pipeline blind spots: cross-document spec mismatches, backbone-to-phase fidelity, metadata completeness). v4.11 adds Known Patterns #69 (MC distractors must not penalize properties taught in prior modules — cross-module distractor coherence) and #70 (prior module IC text must be re-read when drafting Warmup bridge, not just TVP Transition Out). #69 added to Task 3 shortlist. #70 added to Task 2 shortlist and document table. Adds EC Closure to Task 3 Step 2 checklist and Gate 3 shortlist as explicit line items. Adds internal constraint table consistency check to Gate 2 shortlist. Adds vocab reinforcement tally spot-check to Gate 3 shortlist. Adds Pipeline Enhancement Backlog section for tracking checker/agent improvements. From M6 evaluation chat reconciliation (7 unique manual findings, 9 unique pipeline findings, complementary detection profiles).

---

## NEW SESSION SETUP

When starting a new module in a fresh Cowork session:

1. Read this document (`Module Starter Pack Cowork Guidance.md`) in full — it is your process runbook.
2. **Verify plugin is installed.** The `m42-starter-pack-eval` plugin must be installed in the Cowork session. Confirm by checking that skills like `sp-gate-eval` and agents like `m42-gate1-eval` appear in the available tools. If not installed, ask the author to install `m42-starter-pack-eval.plugin` from the workspace folder.
3. Read the Module Mapping workbook — scan all sheet names to orient, then read:
   - The **Module Mapping** sheet row for M[X]
   - The **Important Decisions** sheet in full (unit-level constraints)
   - The **Misconceptions** sheet entries for M[X]
4. Read the TVP section for M[X] + transitions in/out.
5. Read the prior module's Starter Pack (`Grade 3 Unit [X]/G3U[X]M[X-1]_Starter_Pack.md` or pull from Notion via `sp-notion-sync`) for cross-module reference.
6. Fill in the Module Variables below.
7. Begin Task 1.

If resuming a module already in progress, follow the Session Start Protocol in the Context Management section instead.

---

## HOW TO USE

1. Fill in Module Variables below.
2. Work through Tasks 1–4 in order. Each task produces a local markdown draft.
3. At each Gate, Cowork runs the evaluation pipeline (`sp-quick-check` → `sp-gate-eval` → `sp-fix`) before the author reviews.
4. Author resolves remaining findings and approves. Approved output feeds the next task.
5. At Task 4, assemble the full SP, convert via `sp_notion_push.py`, and push to Notion.
6. After Gate 4, the SP is ready for SME review on Notion.

### Module Variables (fill in once)

```
Module: M[X]
Title: [Module Title]
Unit: [Unit number]
Domain: [domain]
Grade: [grade]
Prior module: M[X-1]
Next module: M[X+1]
```

### Documents in Workspace

These must be accessible to Cowork (in the workspace folder or project knowledge):

**Source Documents (module-specific):**
Located in the unit folder: `Grade 3 Unit [X]/`
- Module Mapping workbook (`Grade 3 Unit [X] [Topic].xlsx`) — a multi-sheet Excel file containing:
  - **Module Mapping** (sheet) — M[X] row: learning goals, standards, vocabulary, misconceptions, scaffolding notes
  - **Important Decisions** (sheet) — Unit-level design constraints (CRA path, grid fading sequence, scope boundaries, interaction modality rules). Read once at Task 1; applies to ALL modules.
  - **Misconceptions** (sheet) — Global misconception IDs, observable behaviors, where they surface, priority levels
  - **Conceptual Spine Analysis** (sheet) — Where each concept is introduced/developed/mastered + key transition points. Used for cross-module validation.
  - **Conceptual Development** (sheet) — Cognitive demand level (Activate, Build, etc.) and mathematical move per lesson. Used for CRA calibration.
  - **Standards Mapping** (sheet) — Standard-to-lesson alignment with required vocabulary per standard. Used for D-checks.
  - **Original Curriculum Mapping** (sheet) — Source curriculum lesson narratives, example scenarios, key visual descriptions, practice problems with solutions. Supplementary reference only — Module Mapping is authoritative for sequencing and continuity.
- Tool/Visual Plan (TVP) — this module's section + transitions in/out
- Completed Starter Pack for M[X-1] (if available, in the same unit folder)
- Toy Specifications (Notion links or local copies)

**Reference Documents (universal):**
Local markdown copies in the workspace root. Source of truth is Notion — when a reference doc is updated on Notion, manually copy fresh markdown to the workspace before starting a new module. Notion page IDs are listed below for lookup.

*Phase Playbooks:*
- Warmup Phase Playbook <!-- Notion: 32e5917e-ac52-8155-91b1-cdaecbeeacf1 -->
- Lesson Phase Playbook <!-- Notion: 32e5917e-ac52-8162-bc30-d7678a878830 -->
- Exit Check Phase Playbook <!-- Notion: 32e5917e-ac52-8113-8d30-ef26f20a4966 -->
- Practice Phase Playbook <!-- Notion: 32e5917e-ac52-81b9-91a6-d0bfe1c409a2 -->
- Synthesis Phase Playbook <!-- Notion: 32e5917e-ac52-8140-9285-ee0dbf9a34df -->

*System References:*
- Guide Design <!-- Notion: 32e5917e-ac52-8128-9f4a-e21002ba6bdb -->
- Guide vs Prompt Structure Reference <!-- Notion: 3345917e-ac52-8140-93f4-dc550c9d9690 -->
- Universal Mastery Tracking Framework <!-- Notion: 32e5917e-ac52-818f-b7d5-dc3fc1b0098c -->
- Edtech Activity Queue Rulebook v6 — cognitive verb taxonomy (CREATE/IDENTIFY/COMPARE/APPLY/CONNECT), Practice problem classifications (BASELINE/STRETCH/SUPPORT/CONFIDENCE), session timing targets, EC routing thresholds. Primary reference for Tasks 3–4 (EC + Practice design). <!-- Notion: 32e5917e-ac52-8161-8750-c44221623a73 -->
- Guide Voice Design Reference <!-- Notion: 32e5917e-ac52-8160-99c5-f9a4b2e24be9 -->
- Remediation Design Reference <!-- Notion: 32e5917e-ac52-8135-b91e-ee5c61e513ab -->
- Voice Script Prompt <!-- Notion: 3345917e-ac52-818f-9054-d55ac11b4075 -->

*Local-only (no Notion source):*
- Module Starter Pack Template v3 (`MODULE STARTER PACK TEMPLATE.02.04.26.md`)
- Starter Pack Structural Skeleton (`STARTER PACK STRUCTURAL SKELETON.md`) — canonical heading hierarchy used by L1 structure checker
- Module Starter Pack Cowork Guidance (this document)

**Workspace Folder Structure:**
```
<workspace>/
├── Module Starter Pack Cowork Guidance.md    ← this document
├── MODULE STARTER PACK TEMPLATE.02.04.26.md  ← template v3
├── STARTER PACK STRUCTURAL SKELETON.md
├── [Phase Playbooks].md                      ← universal reference docs (Notion-sourced)
├── [System References].md
├── Grade 3 Unit 1/
│   ├── Grade 3 Unit 1 [Topic].xlsx           ← Module Mapping workbook
│   ├── G3U1M01_Starter_Pack.md               ← rolling SP
│   ├── G3U1M01_Working_Notes.md
│   └── G3U1M01_Gate4_Evaluation_Report.md
├── Grade 3 Unit 2/
│   ├── Grade 3 Unit 2 [Topic].xlsx
│   ├── G3U2M01_Starter_Pack.md ... G3U2M12_Starter_Pack.md
│   └── ...
├── Grade 3 Unit [X]/
│   └── ...
├── _archive/                                 ← superseded drafts, old reference docs
└── m42-starter-pack-eval.plugin              ← evaluation pipeline (install in Cowork to activate)
```

**Evaluation Pipeline** is packaged as the `m42-starter-pack-eval` Cowork plugin. Once installed, all scripts, agents, and skills are available automatically. The plugin is private and local — it is not published to any marketplace. Components: 8 L1 Python checkers, 12 L2 evaluation agents (invoked as isolated subagents), 5 L3 orchestration skills. See Plugin Architecture section below for details.

---

## CHAIN OVERVIEW

```
TASK 1: Backbone + Cross-Reference
    ↓
  ══════ GATE 1: sp-gate-eval --gate 1 (L1 × 8 + L2 × 3) → Author Review ══════
    ↓
TASK 2: Warmup + Lesson
    ↓
  ══════ GATE 2: sp-gate-eval --gate 2 (L1 × 8 + L2 × 6) → Author Review ══════
    ↓
TASK 3: Exit Check + Practice + Synthesis + KDD
    ↓
  ══════ GATE 3: sp-gate-eval --gate 3 (L1 × 8 + L2 × 8) → Author Review ══════
    ↓
TASK 4: Full SP Assembly + Notion Push
    ↓
  ══════ GATE 4: sp-gate-eval --gate 4 (L1 × 8 + L2 × 12) → Author Review ══════
    ↓
  sp-notion-sync: Push to Notion → Post evaluation comment
```

---

## PLUGIN ARCHITECTURE (3-Layer Evaluation System)

Generation (Tasks 1–4) produces local markdown files. Evaluation (Gates 1–4) uses the 3-layer plugin system to check them. Fixes are applied locally, then pushed to Notion after Gate 4.

### Layer 1: Python Checkers (deterministic, fast)

8 checkers bundled in the plugin's `scripts/` directory. Each accepts `--gate N --json` and returns structured findings with severity ratings (CRITICAL, MAJOR, MINOR, NOTE). Run time: ~5 seconds per checker.

| Checker | What It Catches |
|---------|----------------|
| `sp_structure_check` | Section presence, ordering, heading levels, YAML, end markers |
| `sp_vocab_scan` | Vocabulary staging violations, forbidden terms, assessment coverage |
| `sp_voice_scan` | Voice anti-patterns: exclamation density, superlatives, feeling assumptions, identity labels, em dashes in dialogue |
| `sp_interaction_check` | Missing fields, malformed blocks, Pattern 1/2 compliance, type labels |
| `sp_timing_estimate` | Phase duration estimates, cognitive load flags |
| `sp_toy_consistency` | Toy names, modes, data constraints match §1.5 |
| `sp_dimension_track` | Dimension reuse detection, range violations |
| `sp_module_map_check` | Content drift from Module Mapping / TVP authority documents |

**Invocation:** The orchestration skills handle script path resolution automatically. Authors don't need to know the paths — just say "quick check the SP" or "run sp-quick-check".

### Layer 2: LLM Evaluation Agents (qualitative, deep)

12 agents installed via the plugin. Each runs as a **real subagent with an isolated context window** — it gets its own fresh context, reads only the files it needs, and returns findings independently. This eliminates the self-grading problem where the drafting chat evaluates its own work. Agents are read-only — they analyze but never modify files.

| Agent | Scope | Gate |
|-------|-------|------|
| `m42-gate1-eval` | Backbone compliance (§1.0–§1.5) | 1+ |
| `m42-source-fidelity` | Source document fidelity (Module Map, TVP, Important Decisions) | 1+ |
| `m42-pedagogy-eval` | Cross-phase pedagogical arc, scaffolding fade, grade-level fit | 1, 4 |
| `m42-warmup-eval` | §1.6 Warmup quality (Playbook compliance, hook/bridge, WR checks) | 2+ |
| `m42-lesson-eval` | §1.7 Lesson scripting (CRA, worked examples, scaffolding fading) | 2+ |
| `m42-guide-prompt-eval` | Prompt design across all interactions (independence, Type A/B/C) | 2+ |
| `m42-ec-practice-eval` | §1.8 Exit Check + Practice (alignment, cognitive types, distribution) | 3+ |
| `m42-synthesis-eval` | §1.9 Synthesis (task types, metacognition, closure quality) | 3+ |
| `m42-kdd-eval` | §1.10 Key Design Decisions (completeness, format, embedded flags) | 3+ |
| `m42-voice-eval` | Whole-SP voice quality (warmth spectrum, SDT alignment) | 4 |
| `m42-cross-module-eval` | Cross-module alignment (bridges, vocab handoff, toy progression) | 4 |
| `m42-requirements-eval` | Playbook requirements verification, template compliance, Known Patterns | 4 |

### Layer 3: Orchestration Skills

5 skills installed via the plugin that coordinate L1 and L2:

| Skill | When to Use |
|-------|------------|
| `sp-quick-check` | Fast L1-only scan. Good for mid-drafting self-checks. |
| `sp-gate-eval` | Full L1+L2 evaluation at a specific gate. **This is the primary gate evaluation tool.** |
| `sp-gate-eval` at Gate N | Runs all 8 L1 checkers + the gate-scoped L2 agents, produces a consolidated report with cross-layer correlations and a priority fix list. |
| `sp-full-eval` | Batch evaluation across multiple modules. For pre-release unit audit. |
| `sp-fix` | Takes evaluation findings and applies fixes: auto-fix (Category A), semi-auto with confirmation (Category B), or manual with author presentation (Category C). |
| `sp-notion-sync` | Pull SP from Notion → local file, push local file → Notion, or apply targeted Notion edits. Also: evaluate-and-comment (posts findings to Notion page). |

### Gate → Agent Mapping (Quick Reference)

| Gate | L1 Checkers | L2 Agents | Total L2 |
|------|------------|-----------|----------|
| 1 | All 8 | gate1-eval, source-fidelity, pedagogy-eval | 3 |
| 2 | All 8 | Gate 1 agents + warmup-eval, lesson-eval, guide-prompt-eval | **6** |
| 3 | All 8 | Gate 2 agents (excl. pedagogy) + ec-practice-eval, synthesis-eval, kdd-eval | 8 |
| 4 | All 8 | Gate 3 agents + voice-eval, cross-module-eval, pedagogy-eval, requirements-eval | 12 |

**Gate 2 is the mandatory quality gate.** It covers ~75% of student-facing content (backbone + warmup + lesson). Pedagogy-eval runs here to catch CRA progression, scaffolding, and Purpose Frame issues while they're cheap to fix. Gate 3 is lighter — EC and Synthesis are shorter sections with clearer Playbook checklists. Gate 4 is the full audit with voice, cross-module, and requirements agents added.

### Evaluation Workflow at Each Gate

```
1. Run sp-quick-check (L1 only) — fast smoke test
2. If L1 clean: Run sp-gate-eval at Gate N (L1 + L2)
3. Review consolidated findings report
4. Run sp-fix to apply auto-fixable issues
5. Re-run sp-quick-check to verify fixes
6. Author reviews remaining Category B/C findings
7. Approved → proceed to next Task
```

---

### Working Notes

Create `Grade 3 Unit [X]/G3U[X]M[XX]_Working_Notes.md` at Task 1 and maintain it throughout. This is a living document that persists across sessions. All module artifacts go in the unit folder.

**Required sections:**
- **Cross-Reference Table A** — Module Mapping extraction (verbatim)
- **Cross-Reference Table B** — TVP extraction (verbatim)
- **Cross-Reference Table C** — Conflict Log (every discrepancy + resolution)
- **Design Constraints** — Important Decisions extraction (which decisions apply, how they constrain this module)
- **Section Plan** — High-level phase outline
- **Author Flags** — Open questions requiring author decision (numbered, with status)
- **Dimension Tracking** — All dimensions/values used per interaction (prevents accidental reuse)
- **Session Log** — Brief note at start of each session: what was completed, what's next
- **Gate Review Log** — Author feedback and corrections at each gate (see format below)

### Gate Review Log

Record every piece of author feedback at each gate review. This is the raw data that feeds the cross-module Pipeline Review Tracker (`Pipeline_Review_Tracker.xlsx` in the workspace root).

```
## Gate Review Log

### Gate 1 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|
| R1 | §1.3 | [what was wrong] | [how it was fixed] | #N or "NEW?" |

### Gate 2 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|
| R2 | §1.7 | ... | ... | ... |

### Gate 3 Review
...

### Gate 4 Review
...
```

The **Pattern?** column connects feedback to Known Patterns. Use a pattern number if it matches an existing pattern, or "NEW?" if this looks like a recurring issue that doesn't have a pattern yet. "NEW?" entries are candidates for the next pipeline postmortem.

### Author Flags

An Author Flag is a decision the author must make that Cowork cannot resolve from source documents alone. Create one when:
- Source documents conflict and the resolution hierarchy doesn't resolve it
- A correct answer depends on authored visual assets not yet created
- An engineering constraint needs confirmation
- A pedagogical judgment exceeds what the source documents specify

Format: `⚠️ **AUTHOR FLAG ([Category]):** [Description]. [What blocks on this decision].]`

Number them sequentially within the Working Notes. Reference them in the SP where they appear.

---

## CONTEXT MANAGEMENT

Each task lists exactly which documents and sections to read. Follow these rules:

1. **Read only what the task specifies.** Playbooks are 300-900 lines. Don't read the entire Playbook when the task only needs §3A and §4D.
2. **Cross-Reference Tables replace re-reading source documents.** After Task 1, draft from the Tables — not from fresh reads of the Module Mapping or TVP.
3. **Working Notes are the continuity mechanism.** At the start of each new session, read the Working Notes first. They tell you what's been done and what's next.
4. **The completed M1 Starter Pack is a structural reference.** When drafting M2+, reference M1's structure (section organization, interaction block format, Design Note placement) — not its content.

### Session Start Protocol

When continuing across sessions:
1. Read `Grade 3 Unit [X]/G3U[X]M[XX]_Working_Notes.md`
2. Read the current state of the SP draft (in the same unit folder)
3. Read the task spec for whatever task is in progress
4. Resume work

---

# TASK 1: BACKBONE + CROSS-REFERENCE

> **Patterns to enforce at this step:** #1–5 (Source document handling), #9 (Interaction numbering), #11 (Vocab after grounding), #22–23 (Author Flags, Working Notes), #36–39 (Extraction fidelity), #49 (One rolling file)

## Read These Documents

| Document | What to Read | Why |
|----------|-------------|-----|
| Module Mapping (sheet) | M[X] row — EVERY column | Source of learning goals, standards, vocabulary, misconceptions |
| Important Decisions (sheet) | All decisions | Unit-level design constraints that apply to every module |
| TVP | M[X] section + transitions in/out | Source of toy configs, data constraints, key beats, SME decisions |
| Module Starter Pack Template v3 | §1.0–§1.5 sections only | Structural format for backbone |
| M[X-1] Starter Pack | §1.2 Must Not Include, §1.3 Vocabulary, §1.5 Toy Specs, §1.9 Synthesis closure, §1.10 KDDs | What students arrive with, what was deferred |
| Misconceptions (sheet) | M[X] entries | Global IDs, trigger behaviors, prevention strategies |
| Conceptual Spine Analysis (sheet) | M[X] concepts | Where each concept sits in the introduce/develop/master arc |
| Standards Mapping (sheet) | Standards addressed by M[X] | Required vocabulary per standard, lesson alignment |

## Produce These Outputs

All outputs go into the Working Notes except the Backbone draft itself.

### 1. Cross-Reference Table A — Module Mapping Extraction

Read every column in the Module Mapping row for M[X]. Transcribe each field value **verbatim** — not summarized, not paraphrased:

```
MODULE MAPPING: M[X]
====================
The One Thing: [exact text]
Learning Goals: [exact text — L1, L2, etc.]
OUR Lessons: [lesson numbers and descriptions]
Standards Addressed: [exact standards]
Standards Building Toward: [exact standards]
Key Misconceptions: [exact text, including IDs]
Vocabulary to Teach: [complete comma-separated list — EVERY term]
Vocabulary to Avoid: [complete list]
Question/Test Language: [exact stems]
Scaffolding of Visuals: [exact text]
Notes: [exact text — including any "Critical:" flags]
[Any other populated columns]: [exact values]
```

After transcribing, flag any field that is empty, ambiguous, or potentially stale.

### 2. Cross-Reference Table B — TVP Extraction

Transcribe the TVP's module section verbatim. Use the TVP's own headers:

```
TVP: MODULE [X]
===============
Learning Goal: [exact text]
Key Teaching Points: [numbered list, verbatim]
What Students DO: [exact list]
Cognitive Focus: [exact types]
Data Constraints: [every constraint, verbatim]
Scaffolding Notes: [exact text]

PHASE-BY-PHASE FLOW:
[Transcribe each phase using the TVP's own headers — all interactions,
 toys, data, guide dialogue examples, progression notes, Early/Mid/Late
 breakdowns if present.]

TRANSITION IN (from M[X-1]):
[Exact text]

TRANSITION OUT (to M[X+1]):
[Exact text]
```

### 3. Design Constraints Extraction — Important Decisions

Read the Important Decisions sheet in full. Extract every decision that applies to M[X]:

```
DESIGN CONSTRAINTS (from Important Decisions)
=============================================
Decision [#]: [Decision title]
  Rule: [the decision statement]
  Applies to M[X]? YES / NO / PARTIAL
  If YES: What it constrains in this module: [specific implication]
  If PARTIAL: [what applies, what doesn't]

[Repeat for each decision]
```

**These are hard constraints.** If a decision says "M1-M4: Full grids," the SP cannot use partial grids for M1-M4. If a decision says "Do NOT introduce perimeter," the SP cannot mention perimeter. Violations are FAILs.

Store in Working Notes. Reference specific decisions in the SP where they constrain design choices (as Design Notes or KDDs).

### 4. Cross-Reference Table C — Conflict Log

Compare Tables A, B, and the Design Constraints field by field. Document every discrepancy:

```
CONFLICT LOG
============
#1
Field: [e.g., "Vocabulary to Teach"]
Module Mapping says: [exact value]
TVP says: [exact value or "not mentioned"]
Resolution: [which source wins and why]
Status: Resolved / Author Flag

[Repeat for each conflict]
```

**Resolution hierarchy:**
1. Important Decisions are HARD CONSTRAINTS — they apply unit-wide and cannot be overridden by module-level sources. Violations are FAILs.
2. TVP overrides Module Mapping for tool/visual/scaffolding decisions (TVP is downstream, reflects SME resolutions)
3. Module Mapping is authoritative for vocabulary lists and standards
4. When both specify and they conflict → Author Flag
5. When Module Mapping has a "Critical:" note → must appear in SP or be flagged
6. When TVP explicitly removes something from Module Mapping → flag the removal, follow TVP
7. The Module Mapping may not have been updated after TVP decisions → flag suspected staleness

### 5. Edit Reconciliation Pass

**After completing Tables A, B, and C, before drafting.** The TVP often contains numbered edits (Edit 83, 84, 88, 91, etc.) that modify earlier decisions. These edits may be acknowledged in footnotes or parentheticals within the extraction without being fully applied to the extracted text.

Walk through every numbered TVP edit that applies to M[X] and verify:

```
EDIT RECONCILIATION
===================
Edit [#]: [Edit title/description]
  What it changes: [the rule or constraint]
  Reflected in Table B? YES / NO / PARTIAL
  If NO/PARTIAL: What needs updating in the extraction:
    Old text: [current extraction text]
    Corrected text: [text with edit applied]
  Downstream impact on Backbone: [which §1.X sections affected]

[Repeat for each edit]
```

**This is the single highest-ROI extraction step.** M8 analysis showed 3 of 5 Backbone issues traced to edits that were footnoted but not applied. Common failure mode: the extraction says `"accept if offered; included in MC per Edit 91"` — the parenthetical acknowledges the edit but the main text retains pre-edit framing. A clean post-edit extraction would state the resolved rule directly.

### 6. Data-Level Constraint Audit

**After extraction and edit reconciliation, before drafting.** The Conflict Log catches field-level disagreements between documents (TVP says X, Module Mapping says Y). This step catches violations within a single document's specific examples.

Audit all concrete examples in the extraction against applicable design constraints:

```
DATA CONSTRAINT AUDIT
=====================
Example: [e.g., "EC distractor set for area 18: (4×5, 3×7), (2×8, 3×5), (2×7, 4×6)"]
Constraint: [e.g., "Edit 83: No shared factors between distractors and correct answers"]
Correct answers: [e.g., "2×9, 3×6, 1×18"]
Violations found:
  - 3×7 shares factor 3 with correct 3×6
  - 2×8 shares factor 2 with correct 2×9
  - 3×5 shares factor 3 with correct 3×6
  - 2×7 shares factor 2 with correct 2×9
Action: Replace violating distractors before drafting

[Repeat for each example set]
```

**What to audit:** Distractor sets against no-shared-factors rules, worked example dimensions against data constraints, EC values against Lesson value ranges, problem counts against both primary specs and edit-modified counts.

### 7. Section Plan

High-level outline of how content distributes across phases. NOT interaction-level:

- **Warmup:** Prior knowledge activated, anticipated warmup type, bridge target
- **Lesson sections:** How many, what each covers, CRA mapping, where major pedagogical moves happen (worked examples, vocabulary introduction, context shifts)
- **Exit Check:** Skills to assess, anticipated cognitive types
- **Synthesis:** Connections to make, anticipated task types, closure/bridge direction

### 8. Backbone Draft (§1.0–§1.5)

Draft from the Cross-Reference Tables (with edits reconciled and data audited), not from memory of the source documents.

- **§1.0 The One Thing** — From TVP learning goal (Table B). Must be testable in EC.
- **§1.1 Learning Goals** — Verbatim from Module Mapping (Table A). Include Standards Cascade, Module Bridges (From/This/To), OUR Lesson Sources.
- **§1.2 Scope Boundaries** — Must Teach + Must Not Include. Cross-check: every item in Table A's Vocabulary to Teach must appear in Must Teach or §1.3.
- **§1.3 Vocabulary Architecture** — Start from Table A's COMPLETE Vocabulary to Teach list. Account for every term. Include bridging/informal terms from "Critical:" notes.
- **§1.4 Misconceptions** — Use global IDs from the Misconceptions database. Verify IDs match.
- **§1.5 Toy Specifications** — Module-specific configuration from Table B. Include: Notion Spec links, Changes from M[X-1], Module Configuration table, Guardrails, Progression, Data Constraints, Interaction Constraints block.

### 9. Backbone Self-Check

Verify each item against the Cross-Reference Tables:

- [ ] Every term in Table A "Vocabulary to Teach" appears in §1.2 or §1.3
- [ ] Every term in Table A "Vocabulary to Avoid" appears in §1.3 Terms to Avoid
- [ ] Module Mapping "Notes" — every "Critical:" flag addressed in SP
- [ ] Module Mapping "Question/Test Language" stems in §1.1 or flagged for §1.7
- [ ] Misconception IDs match database, not module number shorthand
- [ ] Every TVP data constraint appears in §1.5
- [ ] Every conflict in Table C resolved or flagged
- [ ] Every applicable Important Decision reflected in SP or documented as KDD
- [ ] Conceptual Spine Analysis confirms concept intro/develop/master placement for this module
- [ ] Standards Mapping required vocabulary aligns with §1.3
- [ ] The One Thing references only concepts this module teaches
- [ ] YAML front matter complete
- [ ] **Edit Reconciliation complete** — every numbered TVP edit verified in extraction (Step 5)
- [ ] **Data Constraint Audit complete** — all example sets checked against applicable rules (Step 6)
- [ ] **Backbone-to-extraction diff** — every TVP phase-by-phase beat in Table B accounted for in §1.5 or §1.1 (catches content extracted but not transferred to draft)
- [ ] **Problem/interaction counts** cross-checked against both primary TVP spec and any edits that modified them

---

# ══════ GATE 1 ══════

> **Patterns to enforce at this step:** #67 (Verify §1.5 toy modes against Toy Flow Toy Requirements table)

## Step 1: Quick Smoke Test (L1 Only)

Run `sp-quick-check` on the Backbone draft at Gate 1:

Say "quick check the SP at gate 1" or invoke the `sp-quick-check` skill. It runs all 8 L1 checkers gate-scoped to §1.0–§1.5 and presents a consolidated severity matrix.

If CRITICALs appear, fix before proceeding to L2. Common Gate 1 L1 findings: missing sections (ST), vocabulary list drift from Module Map (MM), structure ordering (ST4/ST11).

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 1. This invokes:
- **All 8 L1 checkers** (re-run for consolidated report)
- **L2 agents (3):** `m42-gate1-eval`, `m42-source-fidelity`, `m42-pedagogy-eval`

The agents read: the Backbone draft, the Working Notes (Tables A/B/C, Design Constraints, Section Plan), the Module Mapping sheet, the Important Decisions sheet, the TVP, the Misconceptions sheet, the Conceptual Spine Analysis sheet, the Standards Mapping sheet, and M[X-1] SP if available.

**What `m42-pedagogy-eval` evaluates at Gate 1:** Section Plan coherence (CRA progression logic, interaction sequencing rationale), warmup→lesson cognitive alignment, planned scaffolding fade rate vs grade-level expectations, Relational bridge placement, grade-level language calibration, cognitive load management, misconception prevention design. This is the cheapest point to catch a flawed pedagogical arc — before any content is drafted.

Output: Gate 1 Evaluation Report with severity matrix, cross-layer correlations, priority fix list, and gate verdict (PASS / PASS WITH CONDITIONS / FAIL).

## Step 3: Fix

If findings exist, run `sp-fix`:
- **Category A** (auto-fix): structural issues, heading levels, missing markers
- **Category B** (semi-auto): present proposed fix, author confirms
- **Category C** (manual): present finding + recommendation, author decides

Re-run `sp-quick-check` to verify fixes resolved.

## Step 4: Author Review

Author receives: Backbone draft + Working Notes + Gate 1 Evaluation Report.

**Review focus:**
- Are the Cross-Reference Tables accurate?
- Are Conflict Log resolutions correct?
- Are Author Flags properly identified?
- Does the backbone reflect the right pedagogical intent?

Author resolves remaining findings, approves or revises. Approved backbone becomes input for Task 2.

**Before starting Task 2:** Save the Gate 1 Evaluation Report as `Grade 3 Unit [X]/G3U[X]M[XX]_Gate1_Evaluation.md`. Every gate eval must be persisted as a standalone file — not just Gate 4. This provides the receipt chain for author decisions and prevents findings from being lost across chat boundaries.

---

# TASK 2: WARMUP + LESSON

> **Patterns to enforce at this step:** #6–8 (Guide/Prompt independence, Remediation, Multi-step interactions), #10 (Relational phase), #11–12 (Vocab staging, Purpose Frame), #15–21 (Data/values, Voice), #24 (Scale progression pedagogy), #40–42 (Cross-module quality), #50 (On Correct feedback), #52 (Options not in Prompt), #55 (Student Action vocabulary), #56–57 (Vocab markup + reinforcement density), #70 (Re-read prior module IC verbatim before drafting Warmup bridge)

## Read These Documents

| Document | What to Read | Why |
|----------|-------------|-----|
| Approved Backbone | Full (from Gate 1) | Foundation for all phase work |
| Working Notes | Tables A/B/C, Section Plan, Author Flags | Context and decisions |
| Warmup Phase Playbook | Full read | Phase structure, warmup types, quality checks |
| Lesson Phase Playbook | Full read | CRA requirements, worked examples, think-alouds |
| Guide vs Prompt Structure Reference | Full read | Interaction block format, independence test |
| Voice Script Prompt | §1–§4 (Core rules, Anti-patterns, Red Flag Words) | Dialogue conventions |
| TVP | M[X] warmup + lesson sections | Phase-specific beats and constraints |
| Conceptual Development (sheet) | M[X] lessons | Cognitive demand levels to validate CRA sequencing |
| Misconceptions (sheet) | M[X] entries | Observable behaviors for remediation design |
| Original Curriculum Mapping (sheet) | M[X] lessons — key visual descriptions, example scenarios | Supplementary reference for interaction design |
| M[X-1] Starter Pack | §1.9 Identity Closure **verbatim** (not summarized) | Warmup bridge must be tonally consistent with what the student actually heard in M[X-1]'s closure — not just aligned with TVP Transition Out (#70) |

## Step 1: Requirements Extraction

Before drafting, read each Playbook and produce an operationalized checklist. "Per Playbook" doesn't produce compliance — extract every numbered requirement, structural element, count, and quality check.

### Warmup Requirements Checklist

Extract from Warmup Playbook at minimum:
- Warmup Type selection (§4D — named types and module-range recommendations)
- Interaction count range (min/max)
- Required elements: hook (with timing), engagement anchors (count + 4 named types), judgment task, bridge
- Sequencing rules (hook first, bridge last)
- Cognitive load target
- Remediation convention
- Visual state limit
- Temporal reference rules
- Boundary violations to avoid (from playbook's violation table)
- Every item from the playbook's quality checklist, verbatim

### Lesson Requirements Checklist

Extract from Lesson Playbook at minimum:
- CRA sequence: all 4 phases named with what each requires
- Worked example minimum count (2-3) + fading structure (full → partial → independent)
- Think-aloud requirements: count, required elements ([PLANNING], [ATTENTION], [SELF-CHECK])
- Example-problem pair structure
- Vocabulary staging rule (AFTER visual experience, never before)
- Purpose Frame requirements OR documented omission rationale
- Required bookends (opening Purpose Frame, bridge to EC)
- Active vs Passive check pattern
- Observation-to-instruction timing
- Scaffolding fading documentation requirement
- Guide vs Prompt independence test
- Every item from the playbook's quality checklist, verbatim

## Step 2: Draft Warmup (§1.6)

Draft following Template v3 interaction block format:

**Pattern 1 (student action):** Visual → Guide → Prompt → Student Action → Correct Answer → Answer Rationale (MC only) → On Correct → Remediation: Pipeline

**Pattern 2 (no student action):** Visual → Guide → No student action.

Include:
- **Core Purpose** section (not just a one-line purpose statement). Must contain:
  - One-line purpose summary
  - **Key Function:** What the Warmup does for this module and why — how it positions the Lesson
  - **Why this serves the concept:** Bullet rationale explaining why THIS warmup type is right for THIS module's learning demands
  - **Test:** "If we removed this Warmup, would students lose mathematical preparation for the Lesson?" Answer YES with specific explanation of what would be missing.
- Parameters table
- Constraints table (MUST / MUST NOT)
- Warmup Type Rationale
- All interactions
- Verification Checklist

**Cross-module differentiation check (Known Pattern #40):** After drafting the warmup hook, read M[X-1]'s warmup opening line (from the §1.9 callback source you already read). Verify your hook uses different framing language. The warmup type should drive the hook structure — an Activation hook sounds different from a Mystery Reveal hook. If both modules open with the same phrase pattern (e.g., both start "Check this out..."), rewrite to signal this module's unique cognitive move.

## Step 3: Draft Lesson (§1.7)

Draft following Template v3 format. Include:
- Lesson Requirements Checklist (at top, with `[REQUIRED]` tag)
- Core Purpose + Pedagogical Flow table (Standard CRA → Module Implementation)
- Lesson Structure table (sections × focus × time)
- Purpose Frame (or KDD documenting omission)
- **Required Phrases** — list every vocabulary word and key phrase that MUST appear in script. Include assessment language stems from Module Mapping. Writers use this as a checklist.
- **Forbidden Phrases** — list every phrase that creates misconceptions or violates scope, with explanation of WHY each is problematic. Use ❌ prefix. Include terms from §1.3 "Terms to Avoid" and any scope-violation language.
- **Misconception Prevention** — dedicated section listing each targeted misconception with specific prevention strategies for THIS Lesson (not just restating §1.4). Reference specific interactions where prevention is embedded.
- All lesson section interactions with CRA stage labels and scaffolding stage annotations
- **Section transition markers** between Lesson sections: `→ SECTION X COMPLETE. PROCEED TO SECTION Y.`
- Module-Specific Lesson Guidance (if applicable)
- Incomplete Script Flags (§1.7.4)
- Success Criteria (§1.7.5)
- Verification Checklist

**Key conventions:**
- `Remediation: Pipeline` — no intensity qualifiers, no authored dialogue
- Guide and Prompt independently complete (apply independence test)
- Visual: lines are one line with toy name, mode, orientation, data, scaffold state
- Session-relative language only
- Contractions in Guide dialogue
- Observable acknowledgments only
- Annotations (Design Notes, Voice Notes, Scaffolding Notes) appear AFTER interaction blocks

## Step 4: Self-Check

Before submitting for Gate 2:
- [ ] Warmup Requirements Checklist — every item marked satisfied or flagged
- [ ] Lesson Requirements Checklist — every item marked satisfied or flagged
- [ ] **Warmup Core Purpose** includes Key Function, Why This Serves, and necessity Test
- [ ] Warmup bridge creates anticipation without teaching
- [ ] CRA phases: Concrete, Relational, Abstract, Application — each has dedicated interaction(s)
- [ ] Relational phase is a SEPARATE interaction (not embedded in vocabulary intro)
- [ ] Worked examples counted: [X] with fading stages labeled
- [ ] Think-aloud with tagged elements present
- [ ] Vocabulary staging matches §1.3 exactly
- [ ] **Required Phrases section present** with every vocabulary word and key assessment language
- [ ] **Forbidden Phrases section present** with ❌ prefix and misconception explanations
- [ ] **Misconception Prevention section present** with per-misconception strategies referencing specific interactions
- [ ] No forbidden vocabulary in any Guide or Prompt line
- [ ] Guide/Prompt independence verified on 3+ interactions
- [ ] **Section transition markers** present between Lesson sections (`→ SECTION X COMPLETE.`)
- [ ] **Every interaction has a type label** in its header (e.g., `[WORKED EXAMPLE]`, `[ACTIVATION]`, `[CONCEPTUAL CHECK]`)
- [ ] All interactions use toys/modes documented in §1.5
- [ ] Dimension Tracking updated in Working Notes
- [ ] **Cross-module On Correct check (Pattern #41):** Read M[X-1]'s On Correct lines for the same phase type (Warmup→Warmup, early Lesson→early Lesson). Verify no identical phrasing. Vary by referencing specific context, values, or strategy — not just the operation name.

---

# ══════ GATE 2 ══════

> **Patterns to enforce at this step:** #46–48 (Template compliance: interaction block format check, no invented fields, prior module ≠ format reference), #63 (Interaction heading format — verify `### Interaction X.Y:` and I18 count >0), #65 (No FP drift — re-examine L1 MAJORs against template, not prior module triage). **Manual checks:** Re-verify §1.5.4 data constraint tables against actual Warmup/Lesson values (internal consistency — any changed values must propagate to constraint table).

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 2 (scope: §1.0–§1.7). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 2. This invokes:
- **All 8 L1 checkers** at gate 2
- **L2 agents (6):** `m42-gate1-eval`, `m42-source-fidelity`, `m42-pedagogy-eval`, `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval`

The Gate 2 agents read: the full draft (Backbone + Warmup + Lesson), Working Notes, Warmup Phase Playbook, Lesson Phase Playbook, Guide vs Prompt Structure Reference, TVP (warmup + lesson sections), Conceptual Development sheet, Misconceptions sheet.

**What the L2 agents evaluate at Gate 2:**
- `m42-warmup-eval`: Warmup type selection, hook timing, engagement anchors, bridge quality, WR checklist compliance
- `m42-lesson-eval`: CRA completeness, worked example count/fading, think-aloud elements, vocabulary staging, scaffolding documentation
- `m42-guide-prompt-eval`: Independence test (Guide works alone, Prompt works alone), Type A/B/C classification accuracy, field completeness
- `m42-pedagogy-eval`: CRA progression against executed content (not just Section Plan), scaffolding fade curve, Purpose Frame presence, cross-module promise gaps (PE1.6). **This is the key Gate 2 addition** — catching pedagogical arc issues here saves significant rework vs Gate 4.

**Note on voice:** At Gate 2, voice issues surface through L1's `sp_voice_scan` (mechanical patterns) and L2's `m42-guide-prompt-eval` (structural voice issues in prompts). The dedicated `m42-voice-eval` agent runs at Gate 4 for the comprehensive voice pass. This is intentional — fixing voice before the full SP exists wastes effort on dialogue that may change at Gate 3.

## Step 2b: Known Pattern Spot-Check (Manual)

L1/L2 catch structural and mechanical issues but miss design-judgment patterns. After reviewing the L1+L2 report, pick 2–3 interactions and manually verify these patterns that no checker covers:

- **#10** — Is the Relational phase a *dedicated* interaction (not folded into a vocabulary introduction)?
- **#48** — Does the interaction format follow the *template*, not the prior module's formatting?
- **#50** — Do On Correct lines start with a fact or observable action, not generic praise? Do any On Correct lines introduce NEW information that the next interaction's Guide doesn't independently re-establish? (Students on heavy remediation skip On Correct.)
- **#52** — Are MC/multiselect answer choices in the Options field, not embedded in Prompt text?
- **#56** — Are `[vocab]` tags applied ONLY to new/status-change terms (not established terms from prior modules)? Does the Vocabulary Reinforcement Plan in the Lesson header list only new/status-change terms?
- **#57** — Does each vocabulary term appear in Guide dialogue for at least 50% of remaining interactions after introduction?

If any fail, do a full pass on that pattern across all interactions before proceeding. These are cheaper to fix now than at Gate 4.

## Step 3: Fix

Run `sp-fix` on findings. Re-run `sp-quick-check` to verify.

## Step 4: Author Review

Author receives: Warmup + Lesson draft + Gate 2 Evaluation Report.

**Review focus:**
- Does the CRA sequence work pedagogically?
- Are worked examples and think-alouds natural, not mechanical?
- Does vocabulary staging feel right for the grade level?
- Are voice findings worth fixing now or acceptable until Gate 4?

**Before starting Task 3:** Save the Gate 2 Evaluation Report as `Grade 3 Unit [X]/G3U[X]M[XX]_Gate2_Evaluation.md`.

---

# TASK 3: EXIT CHECK + PRACTICE + SYNTHESIS + KDD

> **Patterns to enforce at this step:** #13–14 (EC design), #25 (Practice as distributed reinforcement), #42 (Synthesis density), #54 (EC distinct correct answers), #69 (MC distractors must not penalize properties taught in prior modules)

## Read These Documents

| Document | What to Read | Why |
|----------|-------------|-----|
| Approved Backbone | §1.3 Vocabulary, §1.5 Toy Specs | Alignment checking |
| Approved Warmup + Lesson | Full (from Gate 2) | EC alignment, Synthesis callbacks |
| Working Notes | Full | Context, Author Flags, dimensions used |
| Exit Check Phase Playbook | Full read | EC structure, alignment rules, cognitive types |
| Synthesis Phase Playbook | Full read | Task types, closure requirements, timing |
| Practice Phase Playbook | §inputs section | What the Pipeline needs from the SP |
| TVP | M[X] EC, practice, synthesis sections + transition out | Phase-specific constraints |
| Guide vs Prompt Structure Reference | Interaction block format | Format compliance |
| Voice Script Prompt | §1–§4 | Dialogue conventions |
| Original Curriculum Mapping (sheet) | M[X] lessons — practice problems + solutions | Reference for EC and Practice design (supplementary, not authoritative) |
| Misconceptions (sheet) | M[X] entries — "Where Likely to Surface" column | Which misconceptions to target in EC |
| Edtech Activity Queue Rulebook v6 | §Mastery Definitions (EC routing), §Practice Phase (problem classifications), Cognitive Verbs table | Defines BASELINE/STRETCH/SUPPORT/CONFIDENCE tiers for §1.8.5; cognitive verb taxonomy for EC cognitive type selection; EC scoring thresholds (3/3, 2/3, 1/3 routing) |

## Step 1: Requirements Extraction

### EC Requirements Checklist

Extract from EC Playbook:
- Problem count (standard 3 vs. expanded 5)
- Cognitive type constraints by module range (M1-3: CREATE/IDENTIFY; M4-6: add COMPARE; M7-12: all)
- Sequencing principle (simple to complex, all testing SAME concept)
- Alignment requirement (every problem → Lesson section; same toys, modes, interaction types)
- Boundary constraints (no new visual models, no new interaction types, no complexity increase)
- Difficulty level (representative middle)
- Transition frame requirements
- Feedback conventions
- Each item from the playbook's checklist, verbatim

### Synthesis Requirements Checklist

Extract from Synthesis Playbook:
- Interaction count range by module level
- Required elements: opening frame (30-45 sec), connection tasks, metacognitive reflection (1-2 min), identity-building closure (30 sec)
- Task type requirements (minimum 2 different types from named list)
- Timing breakdown
- Remediation convention (light only — mastery assumed)
- Cognitive load awareness (post-fatigue phase)
- Closure requirements (behaviorally specific, previews next module, no generic praise)
- Each item from the playbook's success checks, verbatim

## Step 2: Draft EC (§1.8)

- Parameters table
- Constraints table (MUST / MUST NOT)
- Alignment Check table (each problem → Lesson section)
- Transition frame
- All EC interactions in Template v3 format
- **EC Closure interaction** after last EC item (Guide: transition to Practice, e.g. "You're ready. Let's practice." — no student action). This is a standardized structural element; omitting it breaks the EC→Practice handoff.
- SUPPORT tier documentation (if TVP specifies)
- Verification Checklist

**Critical:** EC values must be within Lesson constraints but NOT identical to Lesson values (dimension reuse only when pedagogically justified and documented as KDD).

## Step 3: Draft Practice Inputs (§1.8.5)

- Distribution targets
- Toy constraints table
- Dimensions Used tracking table (from Working Notes)
- Cross-module skill references for spiral review

## Step 4: Draft Synthesis (§1.9)

- Opening Frame
- Connection tasks (each with task type label, Purpose, Visual, Guide, Prompt, Student Action, Correct Answer, On Correct, Connection, Remediation: Pipeline)
- Identity-Building Closure + next-module bridge
- Verification Checklist

## Step 5: Compile KDD (§1.10)

KDDs document the **pedagogical design choices** that make this module work — the decisions a writer, reviewer, or future author needs to understand to preserve instructional integrity. Each entry explains WHAT was decided and WHY it matters for student learning.

**What belongs in KDD (pedagogical — writer needs to know):**
- Instructional strategies: What IS the teaching approach and what breaks if you change it? (e.g., "Three-step highlighting IS the instructional strategy" or "Structure identification before area calculation — always")
- Sequencing philosophy: Why this order? What happens if sections are reordered or compressed?
- Vocabulary/scope decisions: Why specific terms are staged where they are, what's excluded and why
- Playbook departures with pedagogical rationale
- Key rectangle/value/dimension choices that serve a pedagogical purpose (e.g., same rectangle reused for a "same answer both ways" insight)
- Bridge and scope boundary decisions (what's this module's job vs. next module's)

**What does NOT belong in KDD (process — goes in Working Notes):**
- Author Flag resolution history ("AF#3 resolved per author confirmation")
- Gate review details ("Gate 2 review identified...")
- Development chronology ("Originally X, then changed to Y after review")
- Section lists documenting where a decision applies (the KDD should be self-explanatory)

**Format:** 1-3 sentences per entry. Title states the decision. Body states the rationale. No Decision/Rationale/Sections subfields — inline paragraph, M10 style. See M10's KDD section as the reference exemplar.

**High-count modules (>8 KDDs):** Foundational modules (e.g., first module in a unit) and modules with many first-time design decisions may legitimately produce 10-12 KDDs. When count exceeds 8, group entries by theme (e.g., "Vocabulary Staging," "Balance & Constraint," "Scaffolding Design") with H4 subheadings within §1.10. This keeps the section scannable without artificially merging distinct decisions. Track whether M2+ in the same unit also produce high counts — if so, some decisions may belong at the unit level (in Project Instructions) rather than repeated per module.

**Quality test:** Would a writer seeing this module for the first time understand WHY it works this way from the KDDs alone? If a KDD only makes sense in the context of the development history, it belongs in Working Notes.

## Step 6: Self-Check

- [ ] EC Requirements Checklist — every item satisfied or flagged
- [ ] Synthesis Requirements Checklist — every item satisfied or flagged
- [ ] Every EC problem maps to a Lesson section with same toy/mode/interaction
- [ ] EC values differ from Lesson values (except documented KDD reuse)
- [ ] No new visual models, interaction types, or vocabulary in EC
- [ ] Synthesis tasks connect to student experience (not new teaching)
- [ ] At least 2 different Synthesis task types used
- [ ] Metacognitive reflection present
- [ ] Identity-Building Closure is behaviorally specific
- [ ] M[X+1] bridge matches TVP transition out
- [ ] KDD covers decisions from ALL phases
- [ ] Dimension Tracking complete in Working Notes

---

# ══════ GATE 3 ══════

> **Patterns to enforce at this step:** #13–14 (EC design), #25 (Practice as distributed reinforcement), #42 (Synthesis density), #54 (EC distinct correct answers), #68 (Spot-check §1.5 progression tables against actual phase implementations). **Manual checks:** Verify EC Closure interaction present after last EC item; spot-check vocab reinforcement tally (pick 2 NEW/status-change terms from §1.3, count appearances in §1.7/§1.8/§1.9, verify ≥50% of remaining interactions after introduction).

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 3 (scope: §1.0–§1.10). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 3. This invokes:
- **All 8 L1 checkers** at gate 3
- **L2 agents (8):** Gate 2 agents (excl. pedagogy-eval) + `m42-ec-practice-eval`, `m42-synthesis-eval`, `m42-kdd-eval`

The Gate 3 agents read: the full draft (all sections through §1.10), Working Notes, EC Phase Playbook, Synthesis Phase Playbook, Practice Phase Playbook, TVP (EC/practice/synthesis/transition sections), Original Curriculum Mapping sheet, Misconceptions sheet.

**What the new Gate 3 L2 agents evaluate:**
- `m42-ec-practice-eval`: EC alignment to Lesson sections (same toys/modes/interaction types), cognitive type constraints, value differentiation from Lesson, Practice distribution targets, spiral review
- `m42-synthesis-eval`: Task type diversity (min 2 types), metacognitive reflection presence, identity-building closure quality, connection specificity, M[X+1] bridge
- `m42-kdd-eval`: KDD completeness across all phases, format compliance (M10 style — inline paragraph, no Decision/Rationale subfields), embedded operational flags that belong in Working Notes, Author Flag resolution status

## Step 3: Fix

Run `sp-fix` on findings. Re-run `sp-quick-check` to verify.

## Step 4: Author Review

Author receives: Full draft + Gate 3 Evaluation Report.

**Review focus:**
- Does every EC problem genuinely test what was taught?
- Does Synthesis close the module's narrative arc?
- Are KDDs complete and accurate?
- Are Author Flags resolved or properly documented?

**Before starting Task 4:** Save the Gate 3 Evaluation Report as `Grade 3 Unit [X]/G3U[X]M[XX]_Gate3_Evaluation.md`.

---

# TASK 4: FULL SP ASSEMBLY + NOTION PUSH

> **Patterns to enforce at this step:** #31–35 (Notion integration), #49 (One rolling file)

## Step 1: Assemble Full Starter Pack

Combine all approved sections into one markdown document:
- YAML front matter
- §1.0–§1.5 (from approved backbone)
- §1.6 Warmup (from approved Gate 2)
- §1.7 Lesson (from approved Gate 2)
- §1.8 Exit Check (from approved Gate 3)
- §1.8.5 Practice Phase Inputs (from approved Gate 3)
- §1.9 Synthesis (from approved Gate 3)
- §1.10 KDD (from approved Gate 3)
- End marker: `# END OF MODULE [X] STARTER PACK`
- §1.11 Final Formatting Audit checklist

Verify nothing was lost or duplicated during assembly.

## Step 2: Convert to Notion-Ready Format

Use the `sp-notion-sync` skill to convert and push. Internally it runs the `sp_notion_push.py` conversion script.

This handles: YAML → hub properties block, interaction headers → H3, KDD items → H3, [Type A/B/C] label removal, bullet normalization (`*` not `-`), field name v2 compliance, remediation line normalization.

## Step 3: Post-Conversion Verification

Run the Notion conversion checker (handled automatically by `sp-notion-sync`, or say "check the Notion-ready file").

This checks: no old field names, all remediation = Pipeline, no remaining bold interaction headers, no remaining [Type X] labels, [REQUIRED] tags preserved, interaction_count matches, end marker format.

Fix any findings and re-run until clean.

## Step 4: Push to Notion

**Agent creates the page shell; human pastes the content.** (See Known Pattern #32 for rationale.)

1. **Create the page** in the "Level Math Curriculum Documents" database via `notion-create-pages`:
   - Parent: `data_source_id: "3185917e-ac52-80c0-a46b-000be3c6a416"`
   - Properties: `Name` (title), `Module Number` (integer), `Unit` (select), `Status` → "Initial Draft"
   - Content: empty or minimal placeholder — do NOT attempt to push full SP content via API.
2. **Produce a Notion-Ready file** (`Grade 3 Unit [X]/G3U[X]M[XX]_Notion_Ready.md`) — the final SP with all evaluation findings resolved.
3. **Hand off to human** for copy-paste into the Notion page via web editor.
4. **After paste, agent can verify** by fetching the page and checking: section header count, total content length, key markers (§1.0 through §1.11), no truncation.

**Important Notion behaviors (from M7+ experience):**
- Notion automatically adds `\[` escaping to square brackets via its API. This is cosmetic and renders clean — do not try to remove it.
- Large pages (150K+ chars) exceed fetch token limits — results are saved to file and must be searched with Python.
- Notion's web editor handles markdown paste well for most formatting. Spot-check: tables, bold field labels, bullet structure, trailing content.

---

# ══════ GATE 4 ══════

> **Patterns to enforce at this step:** #26–30 (Evaluation pipeline), #43–45 (Activity Queue compliance), #51 (L1 finding triage), #53 (Capstone L1 triage), #54 (EC distinct correct answers), #60 (V4 `[vocab]` tag false positive), #61 (lesson-eval CRA labeling advisory), #62 (Gate eval persistence), #63 (Interaction heading format), #64 (Identity Closure forward-looking language), #65 (No FP drift from prior modules), #66 (MM0 checker path config), #67 (Toy Flow mode verification), #68 (Backbone-to-phase implementation fidelity), #69 (MC distractor cross-module coherence), #70 (Warmup bridge matches prior module IC tone)

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 4 (full SP scope). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 4. This is the **comprehensive audit** — it invokes:
- **All 8 L1 checkers** at gate 4
- **All 12 L2 agents** (Gate 3 agents + `m42-voice-eval`, `m42-cross-module-eval`, `m42-pedagogy-eval`, `m42-requirements-eval`)

**What the Gate 4 L2 agents add:**
- `m42-voice-eval`: Full warmth spectrum analysis across all phases, SDT alignment (autonomy/competence/relatedness), exclamation calibration, emotion layer progression (warmup energy → lesson focus → EC calm → synthesis reflection), red flag word detection in context, observable-vs-assumed behavior audit
- `m42-cross-module-eval`: Bridge alignment (M[X-1] → M[X] → M[X+1]), vocabulary continuity, toy progression accuracy, misconception arc across modules, scope boundary verification
- `m42-pedagogy-eval`: Full cross-phase pedagogical arc evaluation — CRA progression vs execution, scaffolding fade curve (SMOOTH/ADEQUATE/UNEVEN/CLIFF), Lesson→EC independence gap, think-aloud quality, vocabulary timing in the cognitive arc. At Gate 4 this runs the full check set including Teaching Arc Coherence (TA category), which requires the complete SP.
- `m42-requirements-eval`: Playbook requirements verification (walks every extracted checklist item from Working Notes and confirms it was actually met in the SP), Template v3 formatting compliance (interaction block format, heading hierarchy, KDD format, backbone tables), Known Pattern compliance audit (replaces the manual Step 2b checklist with systematic agent verification)

**Important:** The cross-module agent requires access to M[X-1] SP (and optionally M[X+1]). Pull from Notion via `sp-notion-sync` if not available locally.

Output: Gate 4 Evaluation Report — the definitive quality document for this module. Includes: L1 severity matrix, L2 agent findings, cross-layer correlations, priority fix list (top 10), and gate verdict.

**Report size management:** Gate eval reports grow with module complexity (Gate 3–4 reports can reach 250-310 lines). To manage context consumption in downstream chats, each eval report should include a **Findings for Next Task** section at the top (after the Executive Summary) — a 10-15 line extract listing only the items that the next Task's chat needs to act on, with finding IDs for traceability. The full report stays as the archival reference; the extract is what gets loaded into context. The Unit-level Working Notes should link to the full report path (Gate eval artifacts field) rather than summarizing findings inline.

## Step 2b: Known Pattern Compliance Audit (Agent + Author Verification)

`m42-requirements-eval` now runs the Known Pattern compliance checks as part of its KP category. After reviewing its output, the author should verify the agent's findings on these patterns — they require design judgment where the agent may flag false positives or miss context-dependent cases:

| Pattern | Check | How to Verify |
|---------|-------|---------------|
| #5 | Playbook checklists were operationalized, not assumed | Working Notes contain extracted requirement checklists from each Playbook |
| #10 | Relational phase is a dedicated interaction | Find the Relational interaction in §1.7 — it should show 2+ concrete examples simultaneously with explicit pattern statement, not be folded into vocabulary |
| #13 | EC removes scaffolding tools that were learning aids | Compare §1.8 EC toy configs against §1.7 Lesson — scaffolds present in Lesson should be absent in EC |
| #14 | EC problem count matches Parameters table | Cross-reference §1.8 interaction count against the module's Parameters table in the TVP |
| #22–23 | Author Flags surfaced, Working Notes maintained | Scan for any embedded `⚠️` or `PENDING` in the SP body — these should be in Working Notes with clean SP references |
| #25 | Practice distributes across lessons, not just final | §1.8.5 Practice Inputs reference problems from multiple Lesson sections, not just the last one taught |
| #44 | New visual state types flagged for engineering | If any Visual: line specifies a toy state/animation not used in prior modules, it should have a corresponding engineering flag in Working Notes |
| #45 | Consolidation module scope is disciplined | Count distinct problem types in §1.7 — if >4, verify the Section Plan documents the scope rationale |
| #48 | Format follows template, not prior module | Spot-check 3 interactions against template v3 Quick Reference, not against M[X-1] |
| #50 | On Correct lines start with fact/action, not praise; no new information | Scan all On Correct fields for forbidden openers (Excellent!, Amazing!, Perfect!, etc.). Also verify: On Correct must not introduce NEW information (vocabulary, patterns, forward bridges) that isn't restated in the next interaction's Guide. Students on heavy remediation skip On Correct entirely. Target 10–20 words. |
| #52 | Answer choices in Options, not Prompt | Scan all MC interactions — Prompt should be question only, choices in Options field |
| #55 | Student Action uses standard vocabulary | Every Student Action field uses terms from Template §Student Action Vocabulary table — no free-text descriptions |
| #56 | `[vocab]` markup on new/status-change terms only | Only NEW and STATUS-CHANGE terms get `[vocab]` tags. Established terms from prior modules must NOT have tags. Vocabulary Reinforcement Plan tracks only new/status-change terms. |
| #57 | Vocabulary reinforcement density ≥50% | Each formal term appears in Guide dialogue for ≥50% of remaining interactions after introduction. Terms used <3 times after introduction are flagged. |
| #60 | V4 checker `[vocab]` tag false positive triage | Any V4/V1–V6 findings where the flagged term appears inside `[vocab]` tags → triage as false positive, not a real missing-term issue |
| #61 | lesson-eval CRA labeling findings are advisory | CRA phase labels on individual interactions are NOT template-required. Triage lesson-eval CRA-labeling findings as NOTE unless a genuine pedagogical gap exists |
| #62 | Gate eval reports persisted at every gate | Verify that Gate 1–3 eval reports exist as standalone .md files in the unit folder, not just Gate 4 |
| #63 | Interaction headings use `### Interaction X.Y:` format | Grep for `^### Interaction \d+\.\d+:` — count must match expected interaction count. If I18 reports 0 interactions, this is structural CRITICAL, not parser FP |
| #64 | Identity Closure forward-looking language is permitted | §1.9 closure may use "Next time" bridge AFTER behaviorally specific achievement statements. Triage voice-eval CRITICALs on this as FP when both conditions met |
| #65 | L1 FP classifications not auto-inherited from prior modules | For each L1 MAJOR classified as FP, verify the FP rationale holds against the template — not against M[X-1]'s triage. Prior module triage is context, not precedent |
| #66 | MM0 checker configured for current unit | Verify MM0 returns real findings (MM1-MM7), not "Module not found." If broken, note in eval report and run cross-document checks manually |
| #67 | §1.5 toy modes match Toy Flow Toy Requirements | Open Toy Flow `.docx`, compare each toy's mode/interaction-pattern per phase against §1.5 spec. Flag any mismatch. |
| #68 | §1.5 progression tables match actual implementations | Pick 2-3 behavioral notes from §1.5.x (e.g., "no animation in EC") and verify they match the actual Visual/Guide fields |
| #69 | MC distractors don't penalize prior-module properties | Scan EC and Lesson MC distractors: any option that is mathematically equivalent to the correct answer under properties taught in prior modules (commutativity, identity) must not be marked wrong. Commutative rewrites in post-M5 modules are the canonical case |
| #70 | Warmup bridge tonally consistent with prior module IC | Before drafting §1.6, re-read M[X-1]'s §1.9 Identity Closure verbatim. The student experienced THAT text, not the TVP Transition Out summary. §1.6 bridge must be tonally consistent with what the student actually heard — if M[X-1] named a concept, M[X] shouldn't open with discovery framing as if the concept is new |

Record results in the Gate 4 Evaluation Report as a "Known Pattern Audit" section. Mark each as PASS, FAIL (with interaction IDs), or N/A.

## Step 3: Fix

Run `sp-fix` on findings. Re-run `sp-quick-check` to verify. For Gate 4, pay special attention to:
- Voice findings: these are often Category B (semi-auto) or C (manual) — subtle tone adjustments that need author judgment
- Cross-module findings: may require edits to the PRIOR module's SP, not just this one
- KDD embedded flags: any remaining `⚠️ PENDING` blocks should be extracted to Working Notes (see M7 KDD-10 pattern)

## Step 4: Author Review

Author receives: Full SP + Notion page + Gate 4 Evaluation Report.

**Review focus:**
- Is the SP internally consistent end-to-end?
- Are all Author Flags resolved or explicitly documented?
- Is it ready for SME review?

## Step 5: Post-Gate 4 Actions

After author approval:
1. **Update Unit-level Working Notes.** Populate the module's section in `UNIT[Y]_WORKING_NOTES.md` with: vocabulary terms + introduction interaction IDs, bridge-to-next exact text, dimension values used, toy configurations, gate eval artifact paths, open Author Flags. This is the cross-module baton — the next module's Task 1 chat reads it. If this step is skipped, cross-module continuity breaks.
2. **Update Notion page status** to "SME Review" via `notion-update-page` (property update only — this is a small structured operation the API handles well)
3. **Post evaluation summary** as a Notion comment via `notion-create-comment` so SME reviewers see the quality state
4. **Archive the Gate 4 Report** locally as `Grade 3 Unit [X]/G3U[X]M[XX]_Gate4_Evaluation_Report.md`
5. SP goes to SME review. After SME approval: SP is production-ready.
6. **Update the Pipeline Review Tracker** (`Pipeline_Review_Tracker.xlsx` in workspace root). Add rows for: every author correction from the Gate Review Log, every by-design/false-positive finding worth documenting, and any cross-layer correlations from the Gate 4 report. Fill in the Recurrence and Pipeline Action columns.

---

# PIPELINE POSTMORTEM

After every 3–4 modules (or after finishing a unit), review the Pipeline Review Tracker to identify systemic improvements.

**Process:**
1. Open `Pipeline_Review_Tracker.xlsx` → Issue Log sheet. Filter by Action Status = "Pending".
2. Review the Recurring Patterns sheet. Any pattern with 3+ occurrences is a strong candidate for a pipeline fix.
3. For each pending action, decide: (a) update a checker, (b) add/revise a Known Pattern, (c) update the template, (d) update this guidance doc, or (e) defer with rationale.
4. Implement the changes. Update the Postmortem Log sheet with: date, scope (which modules were reviewed), actions taken, new patterns added, checker updates made.
5. Reset Action Status to "Done" for completed items.

**What to look for:**
- **Same checker, same false positive, 3+ modules** → checker needs updating (e.g., V4 vocab scope, dimension reuse noise)
- **Same author correction across modules** → missing Known Pattern or existing pattern not in the right gate shortlist
- **Findings caught at Gate 4 that should have been caught at Gate 2** → move the check earlier (Gate 2 spot-check or Task 2 shortlist)
- **Issues that leaked to SME Review** → gap in Gate 4 evaluation (missing from compliance audit table?)
- **Declining finding counts over time** → pipeline is working; document what caused the improvement

**Tracker location:** `Pipeline_Review_Tracker.xlsx` (workspace root, 3 sheets: Issue Log, Recurring Patterns, Postmortem Log)

## Pipeline Enhancement Backlog

Checker and agent improvements identified through evaluation chat reconciliations. These are NOT Known Patterns (which instruct the generation chat) — they are improvements to the automated evaluation pipeline itself. Track here until implemented in a plugin release.

| # | Enhancement | Layer | Priority | Source | Status |
|---|-------------|-------|----------|--------|--------|
| PE-1 | EC Closure presence check — §1.8 must contain a post-EC interaction with "No student action" and transition language | L1 (`sp_interaction_check`) | High | M6 reconciliation (T3-01) | Pending |
| PE-2 | Lightweight cross-module bridge tone check at Gate 2 — compare M[X-1] IC closure text against M[X] Warmup opening for tonal consistency | L2 (new or `cross-module-eval` lite) | High | M6 reconciliation (XB1.1) | Pending |
| PE-3 | Readiness-before-abstraction heuristic — when CRA stage increases between sections, verify ≥2 independent student-action interactions in preceding section | L2 (`pedagogy-eval`) | High | M6 reconciliation (P-9) | Pending |
| PE-4 | Source-fidelity constraint-set deviation detection — flag when SP specifies a set of allowed values that differs from TVP/Toy Flow set (not just individual value errors) | L2 (`source-fidelity`) | Medium | M6 reconciliation (CA-12) | Pending |
| PE-5 | MC distractor cross-module coherence check — scan distractors for expressions mathematically equivalent to correct answer under prior-module properties | L2 (`ec-practice-eval`) | Medium | M6 reconciliation (T3-02) | Pending |
| PE-6 | Forward-looking vocab flag at Gate 2 — when §1.3 schedules reinforcement in phases not yet drafted, flag scheduled terms so authors include them | L1 (`sp_vocab_scan`) | Medium | M6 reconciliation (V4/SF-04) | Pending |
| PE-7 | Severity auto-escalation by gate stage — findings rated LOW at Gate 2 that persist to Gate 3 auto-escalate to MAJOR | L3 (orchestration) | Low | M6 reconciliation (Type label severity comparison) | Pending |

---

# CONVENTIONS

## Interaction Block Format

**Pattern 1 (Student Action):**
```
### Interaction [ID]: [Title]

* **Purpose:** [What this accomplishes]
* **Visual: [Toy Name] ([Mode]).** [Orientation]. [Data]. [Scaffold state]. [Interaction type]. [Visibility flags].
* **Guide:** "[Teaching content + complete instruction]"
* **Prompt:** "[Complete standalone instruction]"
* **Student Action:** [Use standard vocabulary from Template §Student Action Vocabulary: Select (single) / Select (multiple) / MC (single) / MC (multiple) / Shade / Place tick / Place point / Drag label / Drag to build / Drag to group / Fill blank / Type number / Enter number / Cut — plus toy-specific terms: Stack / Overlay / Separate / Flip. Chain multi-step with arrows.]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer]
* **Answer Rationale:** [MC only — every option with misconception ID or error type]
* **On Correct:** "[10–20 words. Start with fact/action, not praise. Must not contain NEW information — students on heavy remediation skip this.]"
* **Remediation:** Pipeline
```

**Pattern 2 (No Student Action):**
```
### Interaction [ID]: [Title]

* **Purpose:** [What this accomplishes]
* **Visual: [Toy Name] ([Mode]).** [State]
* **Guide:** "[Dialogue]"
* **No student action.**
```

**Pattern 3 (System-Driven):** Specification table + On Complete + Design Note.

**Synthesis additions:** Connection: field after On Correct. Task type label in header.

## Remediation Convention

`Remediation: Pipeline` — no intensity qualifiers, no authored dialogue, no exceptions.

Use `**Remediation Note:**` annotation AFTER the block only when the pipeline genuinely cannot infer the approach from the interaction context.

## Guide and Prompt Rules

- **Guide** = Teaching Content + Complete Instruction (works without Prompt)
- **Prompt** = Complete Instruction only, worksheet-style (works without Guide)
- No Prompt on Pattern 2 interactions
- Apply the independence test: cover the Guide and read only the Prompt — does the student know exactly what to do?

## Voice Conventions

- Contractions always
- Observable acknowledgments only ("You found 12" not "You understood")
- No assumed internal states ("You're thinking" / "You noticed")
- No aspirational identity labels ("You're a mathematician!")
- Connecting observable behavior to mathematical practice IS allowed ("That's what strong mathematicians do")
- Max 1 exclamation per 3 interactions (but not zero across entire module — calibrate for grade level)
- Session-relative language ("last time/this time" not "yesterday/today")
- No "Module X" numbers in student-facing dialogue
- Red Flag Words to avoid: carefully, thoroughly, systematically, understanding, confused, persistent, thinking

## Annotations

Design Notes, Voice Notes, Scaffolding Notes, Remediation Notes appear AFTER interaction blocks as blockquotes, not as fields within the block.

Exception: Connection is a Synthesis-specific field WITHIN the block.

---

# KNOWN PATTERNS — REFERENCE APPENDIX

These are codified from producing Starter Packs. They are design knowledge, not suggestions. Each Task and Gate section above includes a scoped shortlist of the patterns relevant to that step — look for the "Patterns to enforce at this step" callout. This appendix is the full numbered reference.

> **Always active (every step):** #22 (Author Flags are first-class artifacts), #23 (Working Notes are the continuity mechanism), #49 (One rolling SP file)

### Source Document Handling
1. **Waterfall direction.** Edits go into Starter Packs only — never back into TVPs or Module Mapping.
2. **Starter Pack as source of truth.** When sources conflict, the approved live SP wins.
3. **Source documents must be cross-referenced field by field.** Transcribe first, draft from transcription. Never draft from memory of a source document.
4. **Project knowledge can be stale.** The Module Mapping may not reflect TVP decisions. Trust the TVP for tool/visual decisions. Flag suspected staleness.
5. **Playbook compliance requires operationalized checklists.** "Per [Playbook]" doesn't produce compliance. Extract requirements, self-audit against them.

### Interaction Design
6. **Guide vs Prompt independence.** Both must work alone. Test by covering one and reading the other.
7. **Remediation is a separate production step.** `Pipeline` only in the SP. No intensity qualifiers.
8. **Multi-step interactions.** Sub-part numbering (a/b/c). Parent gets Purpose + Visual; sub-parts get their own fields.
9. **Interaction numbering discipline.** Never invent IDs mid-stream. Plan the numbering in the Section Plan, then follow it.
52. **Answer choices belong in Options, not Prompt.** For MC/multiselect interactions, the Prompt field contains only the student-facing question or instruction ("Which rectangle shows 3 × 5?"). The answer choices (A/B/C/D with values) go in the Options field as a sub-bullet under Student Action. Embedding choices in the Prompt text conflates the instruction with the response mechanism — the engineering layer reads Options as a structured field to render the MC UI. If choices appear only in the Prompt, the system has nothing to render.

### Pedagogical Structure
10. **The Relational phase must be a dedicated interaction.** The most common structural gap is jumping from Concrete (tiling) to Abstract (vocabulary) without an explicit Relational bridge. The Relational interaction shows two or more concrete examples simultaneously, the Guide explicitly states the pattern, and the student confirms. It cannot be embedded in a vocabulary introduction.
11. **Vocabulary after grounding, always.** Formal terms are introduced AFTER concrete experience AND the Relational bridge. Never before.
12. **Purpose Frame at Lesson opening.** Per Playbook §1A. If omitting, document in KDD with rationale.
13. **EC tests internalized criteria, not tool proficiency.** Remove scaffolding tools from EC that were learning aids in the Lesson.
14. **EC problem count.** Validate against the module's own Parameters table, not assumptions.
15. **Section 1 as motivation, not assessment.** Pre-CRA comparison/discovery sections create emotional need, not test knowledge.

### Data and Values
16. **Dimension reuse must be deliberate and documented.** When the same dimensions appear in two interactions, document why in a Design Note and KDD. Common valid reasons: reducing cognitive load during a vocabulary transition, EC testing what was taught.
17. **Tile palettes as number ranges.** Not curated lists of specific options.
18. **Dimension Tracking prevents accidents.** Maintain the tracking table in Working Notes. Update after every interaction.

### Voice and Tone
19. **Zero exclamation points is too flat.** For elementary grades, strategic exclamation at genuine breakthrough moments is appropriate. Calibrate for grade level.
20. **Observable behavior praise can reference mathematical practice.** "That's what strong mathematicians do" is behavioral praise connecting action to practice. "You're a mathematician!" is an aspirational identity label and an anti-pattern.
21. **Voice audit is high-value and should not be skipped.** The most common voice issues are subtle: slightly controlling language, assumed internal states, generic praise. A dedicated pass catches what drafting misses.
50. **On Correct feedback must start with fact or observable action, never generic praise.** Forbidden openers: "Excellent!", "Amazing!", "Perfect!", "Wonderful!", "Great!", "Good!", "Right!", "Yes!", "Exactly right!", "That's right!" — these are all generic praise. Correct patterns: factual restatement ("Six equal parts: sixths."), observable action ("You matched each symbol to the right rectangle."), value restatement ("1/4 means one part out of four equal parts."), or conceptual connection ("When you share with fewer people, each person gets a bigger piece."). This was calibrated from shipped M1/M8/M11 On Correct lines — none of them use generic praise openers. From the G3U5 Migration Playbook.

### Process
22. **Author Flags are first-class artifacts.** Don't bury decisions that need author input in Design Notes — surface them as numbered Author Flags in the Working Notes and reference them in the SP. If an Author Flag appears embedded in a KDD or interaction block (e.g., `⚠️ PENDING SME RESOLUTION`), extract it to Working Notes and replace with a clean reference (e.g., `> **Author Flag A9** (see Working Notes): [brief description]`). This was a Gate 4 finding on M7.
23. **Working Notes are the continuity mechanism.** Without them, session boundaries cause rework.
24. **Scale progression pedagogy.** The conceptual leap is unit → non-unit, not between non-unit scales.
25. **Practice Phase as distributed reinforcement.** Lessons shouldn't be assessed in isolation.
49. **One rolling SP file, not separate task files.** Create `Grade 3 Unit [X]/G3U[X]M[XX]_Starter_Pack.md` at Task 1. Task 2 adds sections into the same file. Task 3 adds more sections into the same file. Gate evaluations run against this one file at each gate. Do NOT create separate files per task (`_Task1_Backbone.md`, `_Task2_Warmup_Lesson.md`, `_Task3_EC_Practice_Synthesis_KDD.md`) and then concatenate them at Gate time. Separate task files create unnecessary intermediates, concatenation errors, and confusion about which file is authoritative. The only files on disk in the unit folder should be: `_Starter_Pack.md` (the rolling SP), `_Working_Notes.md` (continuity), and `_Gate4_Evaluation_Report.md` (final eval). At Task 4, rename to `_Notion_Ready.md` when it passes Gate 4.

### Evaluation Pipeline
26. **L1 before L2, always.** Run `sp-quick-check` first. If L1 finds CRITICALs, fix them before wasting tokens on L2 agents that will re-discover the same issues. L1 takes ~5 seconds; L2 takes minutes per agent.
27. **L1 V4 findings may be by-design.** The vocab checker flags assessment vocabulary terms not spoken in EC dialogue. If the EC tests the *skill* that uses those terms (e.g., Equation Builder requires understanding "factor" and "product" without the Guide saying those words), document it as an EC Design Note rather than treating it as a finding. M7 had 11 V4 MAJs that were all intentional design.
28. **Gate 4 is the definitive quality gate.** Gates 1–3 are iterative checkpoints. Don't over-invest in fixing MINOR/NOTE findings at earlier gates — the content will change as later sections are drafted. Gate 4 is where the full cross-layer evaluation matters.
29. **Voice eval at Gate 4, not earlier.** Running the comprehensive voice agent before the full SP exists wastes effort on dialogue that may change when EC and Synthesis are added. L1's `sp_voice_scan` catches mechanical anti-patterns at Gates 1–3; that's sufficient.
30. **Cross-layer correlations are the highest-value findings.** When L1 and L2 flag the same underlying issue from different angles (e.g., L1 vocab checker + L2 source-fidelity both flag a dropped term), that's a systemic issue. Fix those first.
51. **Triage L1 findings by checker and context, not just severity.** Not every MAJOR is a real issue. Common false positives and context-dependent findings (from G3U5 Migration Playbook triage guide): ST5/ST6 in checklist meta-text (false positive — checklist items *mention* tags, they aren't actual tags). VO3 `command_language` for "if you need to" (false positive — invitational, not controlling). VO3 `rhetorical` for "Can you..." in guided practice (pedagogical choice — invitational framing). VO4 `verbose_guide` in worked examples and multi-step demos (by-design — these need more dialogue). I20 `On Correct word count` over 20 words when teaching a concept at the confirmation point (context-dependent). MM* module-map findings when the checker's reference data doesn't match the unit being authored (checker config limitation). At Gate 4, build a triage table: for each finding, mark as Real (fix), False Positive (ignore + document), or Context-Dependent (evaluate + document). This prevents both under-fixing (dismissing real issues) and over-fixing (rewriting sound content to silence a false positive).

### Extraction Fidelity (from M8 process assessment)
36. **TVP edits must be applied, not footnoted.** When the TVP extraction acknowledges an edit in a parenthetical (e.g., "included per Edit 91") but retains the pre-edit framing, the extraction is incomplete. The Edit Reconciliation Pass (Task 1, Step 5) exists specifically to catch this. M8 had 3 of 5 Backbone issues trace to edits footnoted but not applied.
37. **Data-level constraint audits catch what field-level Conflict Logs miss.** The Conflict Log compares Table A vs Table B at the field level. It does not audit individual data examples (distractor sets, worked problem values, EC items) against the design constraints that govern them. M8's distractor violation (shared factors with correct answers, violating Edit 83) was in the TVP itself — the Conflict Log couldn't catch it because it wasn't a cross-document disagreement.
38. **Backbone-to-extraction diff prevents transfer losses.** Content can be correctly extracted into Table B but fail to transfer into the Backbone draft. The "Are there any others?" guide beat in M8 was present in the TVP extraction but absent from the Backbone. A systematic diff after drafting — walking each Table B entry and confirming it appears in the corresponding §1.X section — catches this.
39. **Problem counts need cross-reference, not single-source capture.** When the TVP specifies a count (e.g., "4 forward problems"), verify it against both the primary spec and any discussion or edit that modified it. M8's forward count (4) matched one TVP source but not the resolved discussion (5-6). Edits to counts are easy to miss because they change a number, not a structural element.

### Cross-Module Quality (from M8-M9-M10 comparative analysis)
40. **Warmup hooks must be conceptually distinctive across modules.** M8 and M9 both open with "Check this out" followed by nearly identical sentence structures despite having different cognitive focuses (M8=one-area-many-rectangles surprise, M9=two-question-types contrast). Each module's warmup hook should use language that signals its unique cognitive move. At Task 2 §1.6 drafting, read the prior module's warmup opening and ensure the new module's hook uses different framing language, not just different values. The warmup type (Activation, Mystery Reveal, Challenge, etc.) should drive the hook structure.
41. **On Correct feedback must pass cross-module specificity.** "You multiplied the dimensions" appears nearly identically in M8 and M9 On Correct lines. While each instance passes the single-module specificity test, reading both modules back-to-back reveals templated phrasing. At Task 2, after drafting On Correct lines, check them against the prior module's On Correct lines for the same phase. Vary the phrasing: reference the specific context ("You pulled the dimensions right out of the word problem"), the specific values ("5 rows of 6, that's 30"), or the specific strategy used — not just the generic operation.
42. **Synthesis density should match module scope.** Single-concept modules (M8: forward + reverse = 2 directions) → 4-5 synthesis interactions. Multi-format application modules (M9: 5 problem types) → 5-6 interactions. Synthesis/connection modules (M10: representational shift) → 3-4 interactions (lighter because the concept is consolidation, not breadth). Document the chosen count and rationale in the Section Plan.

### Activity Queue Compliance (from Pedagogical Flow Analysis, M8-M10)
43. **Atomic block must fit the ~15 min module block target.** The Activity Queue Rulebook specifies ~15 minutes per module block because the queue needs real-time decision authority over what comes next. A Lesson phase that runs 15-20 minutes on its own pushes the full atomic block (Warmup + Lesson + EC + Synthesis) to 21-29 minutes, defeating the queue's purpose. When a module's Lesson exceeds ~12 minutes estimated, evaluate which interactions are Practice-level work disguised as Lesson content. CHALLENGE-type problems (additional constraints beyond the core skill), fluency drills, and mixed-format application sets are candidates for deferral to Practice Inputs. Document the split rationale in the Section Plan and ensure the deferred items appear in §1.8 Practice Inputs with full specification.
44. **New visual state types require engineering confirmation.** If a module introduces a visual state not used in any prior module in the unit (e.g., a new animation type, a novel interactive element, a different grid manipulation), flag it explicitly in the Working Notes as an engineering dependency. The SP can specify the desired behavior, but the module should not be marked Gate 4 PASS until engineering confirms buildability. Prior art: M9 introduces animated dimension-label overlays; M10 introduces multiplication-table cell highlighting with row/column trace animations — both need confirmation.
45. **Consolidation modules need explicit scope discipline.** Modules that consolidate prior learning (like M9: multi-format area, M10: area and the multiplication table) naturally want to cover more ground. This is where block timing violations originate. At the Section Plan stage, count the distinct problem types/formats the Lesson must cover. If >4 distinct types, either (a) defer the most complex to Practice, (b) combine types that share the same cognitive move, or (c) split into two modules. Option C is a design-level decision that requires author approval.

### Template Compliance (from M8-M12 deviation audit)
46. **Interaction block format compliance check at Gate 2.** Template drift accelerates across modules because each generation chat reads the prior module as a structural reference, compounding deviations. Before Gate 2, pick 3 interactions at random and verify each against the template's Interaction Block Self-Check (QUICK REFERENCE section of the template v3). Key enforcement points: (a) H3 headers, not bold text or H2/H4, (b) fields as inline bullets (`* **Field:** value`), not field-as-paragraph, (c) `Remediation: Pipeline` only — no inline remediation scripts, (d) no ad-hoc field names, (e) Visual: line passes completeness checklist. If any interaction fails, do a full pass before proceeding. This is cheaper at Gate 2 than at Gate 4.
47. **Do not invent fields.** The template defines a closed set of interaction fields: Purpose, Visual, Guide, Prompt, Student Action, Options, Correct Answer, Answer Rationale, On Correct, Remediation, and `No student action.` If you need to express something these fields don't cover (system animations, pedagogical rationale for no student action, think-aloud structure), use the appropriate Pattern (3 for system-driven, 4 for think-aloud) or a Design Note annotation. Do NOT create `[System Action]`, `Rationale for No Student Action`, `Guide (continuing)`, `[Guide_Think_Aloud]` as field labels, or any other ad-hoc field.
48. **Prior module is a content reference, not a format reference.** When drafting M[X], read M[X-1] for pedagogical continuity (bridge chain, vocabulary, dimension progression) but reference the TEMPLATE for structural format. M[X-1] may contain deviations that are not template-compliant. The template is the format authority; the prior module is the content authority.
53. **Capstone/application modules legitimately deviate from L1 expectations.** L1 checkers are calibrated for standard CRA-progression modules. Capstone modules (e.g., M14) may omit standalone guardrail subsections (using inline error handling instead) and standalone dimension tables (embedding dimensions contextually in interactions). When L1 MAJORs fall entirely into these categories, triage them as by-design rather than fixing them. Document the deviation in a KDD if not already covered. If >10 L1 MAJORs are all non-actionable, that's a signal the module is capstone-pattern and the triage is correct — not a signal something is wrong.
54. **EC items must have distinct correct answers.** If two or more EC sub-items produce the same numeric correct answer (e.g., bookshelf 6×2 = 12 and dresser 4×3 = 12), the later item loses diagnostic value — the student can select the answer without computing. Check all EC correct answers for uniqueness at Gate 3 or Gate 4. If duplicates exist, swap one item's parameters to produce a distinct result while staying within TVP-approved options.
55. **Student Action field must use standard vocabulary.** Every Student Action field must use terms from the Template §Student Action Vocabulary table. Do not invent free-text descriptions like "Student clicks on the fraction that is larger" — use "Select (single)" instead. The vocabulary describes what the student physically does (action-based), not app tool names (which change during engineering). If a toy's interaction genuinely does not map to any standard term, use the extension process: propose a new term with a `⚠️ NEW-ACTION` flag in the Student Action field and Working Notes. For variants of existing terms, use the base term with a parenthetical qualifier (e.g., `Drag to build (slot-constrained)`). When scanning at Gate 4, flag any Student Action that doesn't match, compose from, or extend the standard terms via this process.
56. **`[vocab]` markup is for NEW and STATUS-CHANGE vocabulary only.** Only terms that change status in THIS module get `[vocab]term[/vocab]` markup: (a) NEW terms introduced for the first time, and (b) STATUS-CHANGE terms that transition from informal to formal in this module. Tag from the introduction/formalization interaction through end of module, in both Guide and On Correct fields. ESTABLISHED terms from prior modules (already formally taught) do NOT get `[vocab]` tags, even when reinforced — they were already visually treated in their introduction module. This prevents tag density from inflating On Correct word counts (I20 findings) and keeps the scripter signal focused on genuinely new visual treatment needs. Warmup never has `[vocab]` tags — all Warmup terms are established (activation only). At Gate 2, verify the Vocabulary Reinforcement Plan lists only new/status-change terms.
59. **TVP in docx format: L1 checker limitation.** When the TVP is a .docx file (preferred for comment preservation), the sp_module_map_check (MM0) checker cannot parse it and fires a non-actionable MINOR ("Module not found in Module Map"). This is expected — the source-fidelity L2 agent works from Working Notes Table A/B extractions, which are the authoritative intermediary. The MM0 MINOR can be triaged as a known limitation at every gate. Do not convert the TVP to xlsx/md just for checker access.

58. **Known false positive: Required/Forbidden Phrases placement.** The lesson-eval L2 agent and the L1 ST11 checker both expect the Required/Forbidden Phrases block to appear BEFORE Section 1 in §1.7. The actual template (MODULE STARTER PACK TEMPLATE v3) places them AFTER all Lesson sections. Do NOT move the block when these findings fire — they are confirmed false positives. If the drafting chat moves the block to comply with the agent's recommendation, the L1 checker will flag the move at the next gate, creating a wasteful round-trip. Triage both LS4.1/LS-ORD1 (L2) and ST11 (L1) as false positives and note in the eval report.

57. **Vocabulary reinforcement density target: 50% (new/status-change terms only).** After a NEW or STATUS-CHANGE vocabulary term is introduced/formalized, it should appear in Guide dialogue for at least 50% of remaining interactions in that module. Terms used fewer than 3 times after introduction are under-reinforced. On Correct fields should also use the formal term with `[vocab]` markup when referencing the concept. Established terms from prior modules are naturally reinforced through use but are NOT tracked for density and do NOT carry `[vocab]` tags. If a new term genuinely cannot hit 50% (e.g., introduced in the final section), document the reasoning in a KDD.

60. **V4 checker `[vocab]` tag and symbol-term handling.** Fixed in plugin v0.2.0: `sp_vocab_scan.py` now strips `[vocab]`/`[/vocab]` tags before regex matching and uses smart word boundaries for symbol terms (`÷`, `×`). If running plugin v0.1.0, V4/V1–V6 findings where the flagged term appears inside `[vocab]` tags or is a symbol character should be triaged as false positives. With v0.2.0 installed, remaining V4 findings (e.g., base form vs. inflection like "divide" vs. "divided") are genuine design decisions about assessment vocabulary coverage, not checker bugs.

62. **Persist gate eval reports at every gate, not just Gate 4.** After each gate's Author Review, save the evaluation report as `G3U[X]M[XX]_Gate[N]_Evaluation.md` in the unit folder. M2 only persisted the Gate 4 report — Gates 1–3 results were lost when the chat ended. The receipt chain matters: it documents which findings were raised, which were triaged as false positives, and which author decisions were made. Without it, the next Task's chat has no record of prior gate outcomes and may re-raise resolved findings.

61. **lesson-eval CRA labeling is advisory, not prescriptive.** The `m42-lesson-eval` agent frequently flags interactions for missing explicit CRA phase labels (e.g., "Interaction 2.1 should be labeled as Relational") or for CRA phase sequencing that doesn't match its ideal model. The template does NOT require CRA phase labels on individual interactions — CRA progression is documented in the Section Plan and realized through the interaction sequence, not through per-interaction labels. When lesson-eval raises findings about CRA labeling or CRA phase assignment on individual interactions, triage as advisory (NOTE severity). Only escalate if the finding identifies a genuine pedagogical gap (e.g., no Relational bridge exists at all), not just missing labels. This was raised in both M1 and M2 gate evals and rejected both times by author review.

63. **Interaction headings must use `### Interaction X.Y:` format — treat I18 "0 interactions found" as structural CRITICAL.** The template requires `### Interaction X.Y: Title` (H3) for all interaction headings. Generation chats sometimes drift to `#### S1.1:` or `#### S2.3:` format — especially when Working Notes or prior modules use section-prefixed labels (S1, S2, S3). This creates a self-reinforcing false positive loop: the non-standard format gets documented in Working Notes as intentional, overriding L1 ST11/ST10 findings, and the I18 interaction parser (which expects `### Interaction`) reports "0 interactions found" — which cascades into timing underestimates and empty I-series findings that get dismissed as parser limitations instead of structural errors. **Prevention:** At Gate 2, verify that at least 3 interactions match the `^### Interaction \d+\.\d+:` regex. If I18 reports 0 interactions at any gate, treat it as a structural CRITICAL (heading format wrong), not a parser note. **If found post-Gate 2:** Renumber all interactions to template format before proceeding — the longer it persists, the more findings it corrupts. M4 required renumbering 32 headings (24 main + 8 sub-parts) post-Gate 4.

65. **Do not auto-inherit L1 false positive classifications from prior modules.** When an L1 finding (e.g., ST9, ST10, ST11) was triaged as a false positive in M[X], do not automatically classify the same finding as FP in M[X+1]. Re-examine each finding against the template independently. M5 discovered that ST9 (extra H1 divider), ST11 (Required/Forbidden Phrases ordering), and ST10 (H4 headings) had been classified as FPs since M1, when all three were actually real template violations. The mechanism: M1 accepts a deviation → M2 generation chat reads M1's triage → copies the classification → M3-M5 inherit it. This is "FP drift." **Prevention:** At each gate, the generation chat must compare L1 findings against the template, not against prior modules' triage decisions. Prior module triage is informational context, not precedent. The template is the authority. If a finding was FP in M[X] for a documented design reason, that reason must still hold for M[X+1] — don't assume it does.

66. **MM0 checker requires path configuration for each unit.** The `sp_module_map_check.py` checker has reference file paths that default to the G3U2 directory. For any new unit, the checker will return "Module not found" and silently skip all MM1-MM7 cross-document checks. A patched version (`sp_module_map_check_patched.py`) uses auto-discovery to find `.xlsx` (Module Map) and `*Toy Flow*.docx` files in the SP's own directory. Until the patched version is applied to the plugin, MM0 findings on any non-G3U2 unit are not false positives — they indicate the checker is broken for that unit.

67. **Verify §1.5 toy modes against Toy Flow Toy Requirements table at Gate 1.** The source-fidelity agent checks SP alignment against Module Mapping and TVP learning goals, standards, and vocabulary. It does NOT cross-reference the Toy Flow's per-phase Toy Requirements table (which specifies toy modes and interaction patterns per phase) against §1.5 toy specifications. M5 had a direct contradiction: Toy Flow specified "equation mode (Late)" with student building, but the SP specified display-only throughout. Neither L1 nor L2 caught it. **Manual check:** At Gate 1 Author Review, open the Toy Flow `.docx`, find the module's Toy Requirements table, and compare each row's mode/interaction-pattern against the corresponding §1.5 toy spec entry. Flag any mismatch. This is the most important cross-document check that the automated pipeline currently misses.

68. **Spot-check §1.5 Progression tables against actual phase implementations at Gate 3.** The §1.5.x "Progression Within M[X]" tables make specific behavioral claims about how each toy operates in each phase (e.g., "no rotation animation in EC," "display-only in Synthesis"). No agent currently validates these claims against the actual interactions. M5 had the Backbone claiming "no rotation animation" in EC while the actual EC.1 interaction used rotation animation. **Manual check:** At Gate 3 Author Review (when EC/Synthesis are first drafted), pick 2-3 behavioral notes from the §1.5.x progression tables and verify they match the actual Visual/Guide fields in the corresponding phase interactions.

69. **MC distractors must not penalize properties taught in prior modules.** When designing MC distractors for EC or Lesson interactions, verify that no distractor option is mathematically equivalent to the correct answer under properties formally taught in prior modules. The canonical case: after M5 teaches commutativity, a commutative rewrite of the correct expression (e.g., `(5×2)+(4×2)` as distractor when the correct answer is `(2×5)+(2×4)`) cannot be marked wrong — it contradicts the established principle that order doesn't matter. M6 EC.1 had this exact issue (T3-02). **Prevention:** At Task 3 §1.8 drafting, list the mathematical properties formally taught in prior modules (commutativity after M5, identity, etc.). For each MC distractor, check: "Would this answer be correct under any property the student has already learned?" If yes, replace the distractor with a genuine error (arithmetic mistake, structural misconception like U4.6, wrong operation). This applies to EC and Lesson MC interactions equally.

70. **Re-read prior module's Identity Closure verbatim before drafting Warmup bridge.** The TVP Transition Out provides a planning-level summary of the M[X-1]→M[X] bridge, but the student experiences M[X-1]'s actual Identity Closure text, not the TVP summary. If M[X-1]'s closure explicitly names a concept (e.g., "area models"), M[X]'s Warmup cannot open with discovery framing as if the concept hasn't been previewed — the student just heard it named. M6's XB1.1 CRITICAL resulted from exactly this: M5's closure said "you'll use AREA MODELS" but M6's warmup opened with "What if you could do this with ANY multiplication?" as if the idea were new. **Prevention:** At Task 2 §1.6 drafting, the generation chat must re-read M[X-1]'s §1.9 Identity Closure from the actual SP (not Working Notes summary, not TVP Transition Out). If the closure names a concept or tool, the Warmup bridge must acknowledge it: "Remember when we said [concept] could help? Let's find out how." The discovery should be HOW it works, not THAT it exists.

64. **Identity Closure forward-looking language is permitted per Synthesis Playbook §3F.** The `m42-voice-eval` agent flags "Next time" language in §1.9 Identity-Building Closure as a CRITICAL (citing Guide Voice Design Reference §4.5 which prescribes present-tense achievement framing). However, the Synthesis Playbook §3F explicitly includes a forward-looking bridge as part of the closure pattern, and every module's closure needs to set up the M[X+1] Warmup hook. The Playbook is the higher authority for phase structure; the Voice reference governs tone within that structure. **Resolution:** "Next time" (or equivalent forward bridge) in Identity Closure is acceptable when it follows the achievement statements and serves as the M[X]→M[X+1] bridge. It is NOT acceptable as a replacement for achievement framing (the closure must lead with what the student accomplished). Triage voice-eval CRITICALs on this pattern as false positives when both conditions are met: (a) closure leads with behaviorally specific achievement statements, and (b) forward language appears at the end as a bridge.

### Notion Integration
31. **Local-first for generation, Notion at the end.** Drafting directly in Notion is slow (160K char fetches, silent API failures, escaping complexity). Draft locally, evaluate locally, push to Notion at Task 4.
32. **Agent creates the page, human pastes the content.** The Notion API is reliable for structured operations (creating a page, setting properties) but fragile for pushing 800-1200 lines of richly formatted markdown. At end-of-session context pressure, agents hallucinate API responses and produce content corruption. The correct split: (a) Agent creates the page in the database with correct properties (Name, Module Number, Unit, Status = "Initial Draft"), (b) human copies the Notion-Ready markdown and pastes it into the page in the Notion web editor, (c) human does a quick visual scan. This replaces `sp-notion-sync` for content push. The database details:
    - **Database**: "Level Math Curriculum Documents" (`3185917eac5280abb772efe0552c88ae`)
    - **Data source ID**: `collection://3185917e-ac52-80c0-a46b-000be3c6a416`
    - **Required properties**: Name (title), Module Number (number), Unit (select), Status (status → "Initial Draft")
    - **Optional properties**: IM/OUR Lessons (multi-select), Primary Toys (relation), Secondary Toys (relation), Assigned (person)
    - **Note**: Unit select only has "Unit 1" and "Unit 2" as existing options. New units will auto-create when set via the API.
33. **Notion bracket escaping is cosmetic.** Notion's API automatically adds `\[` before square brackets. This renders clean on the page (no visible backslashes). Do not try to remove it — Notion will re-add it on every save. Only fix triple-escaped patterns (`\\\[`) which show visible backslashes.
34. **Post-paste verification.** After pasting content into Notion, spot-check: (a) interaction block formatting survived (bold field labels, bullet structure), (b) tables rendered correctly, (c) no content truncation at the end of the page, (d) section headers are all present. Notion's markdown paste handles most formatting well but occasionally drops trailing content or misparses complex tables.
35. **ALL CAPS = vocabulary standout, not excitement.** Terms like `ACTIVATION`, `MYSTERY REVEAL`, `JUDGMENT` in interaction headers are deliberate vocabulary emphasis per the SP template. Do NOT lowercase them. The L1 voice checker knows to skip these.

---

# MODULE-SPECIFIC ACTION ITEMS

These are open items identified through evaluation that need resolution in the relevant module's generation context.

### M9: Multi-Format Area (Consolidation)

| # | Priority | Issue | Recommended Action |
|---|----------|-------|--------------------|
| M9-A1 | **Must-Fix** | Lesson phase estimated at 15-20 min, pushing atomic block to 21-29 min (Rulebook target: ~15 min) | Defer interaction 3.4 (CHALLENGE constraint problem: "find rectangles with area 24, one dimension must be odd") to §1.8 Practice Inputs. This is Practice-level work — it requires fluency plus an additional constraint. Reduces Lesson to ~12-17 min. |
| M9-A2 | **Should-Fix** | New animation type (dimension-label overlays on grid) not confirmed buildable | Add engineering dependency flag to Working Notes. Do not mark Gate 4 PASS until confirmed. |
| M9-A3 | **Note** | Notion discussion marker exists on timing concern | Resolve in Notion — either apply the 3.4 deferral or document the design rationale for exceeding the block target. |

### M10: Area and the Multiplication Table

| # | Priority | Issue | Recommended Action |
|---|----------|-------|--------------------|
| M10-A1 | **Should-Fix** | Late Lesson section has 3 pattern activities (rows, columns, diagonals) that may push timing | Consolidate to 2 activities: (1) rows + columns (linear patterns), (2) diagonals (non-linear pattern — the real insight). Trims ~3 min and sharpens the pedagogical contrast. |
| M10-A2 | **Should-Fix** | Multiplication-table cell highlighting with row/column trace animation not confirmed buildable | Add engineering dependency flag to Working Notes. |
| M10-A3 | **Minor** | Missing Correct Answer fields on S2.2-S2.4 (region-marking interactions) | Design ruling needed: do region-marking interactions need an explicit Correct Answer field, or is system validation sufficient? If sufficient, document the pattern in a Design Note. |
| M10-A4 | **Note** | Pushed to Notion before Gate 4 evaluation | Run full Gate 4 (L1 + L2) on the Notion-pulled copy. Apply fixes in Notion directly since the page is already live. |

---

**END OF COWORK GUIDANCE**
