# MODULE STARTER PACK — COWORK GUIDANCE

**Version:** 03.26.26 v4.1
**Purpose:** Guides Cowork through producing a complete Module Starter Pack. Four drafting tasks, four author review gates, automated evaluation pipeline at each gate. Built from lessons learned producing G3U2 M1–M7. v4 integrates the 3-layer plugin architecture (L1 Python checkers, L2 LLM agents, L3 orchestration skills) and Notion sync tooling proven during M7 evaluation. v4.1 adds Edit Reconciliation Pass and Data-Level Constraint Audit to Task 1, from M8 process assessment.

---

## NEW SESSION SETUP

When starting a new module in a fresh Cowork session:

1. Read this document (`Module Starter Pack Cowork Guidance.md`) in full — it is your process runbook.
2. **Verify plugin infrastructure.** Confirm these exist in the workspace:
   - `.claude/scripts/` — 8 L1 Python checkers + utility scripts (see Plugin Architecture below)
   - `.claude/agents/` — 10 L2 evaluation agent definitions
   - `.claude/skills/` — 5 L3 orchestration skills (`sp-quick-check`, `sp-gate-eval`, `sp-full-eval`, `sp-fix`, `sp-notion-sync`)
   - Run a quick smoke test: `python .claude/scripts/sp_structure_check.py --help` to verify Python deps are available
3. Read the Module Mapping workbook — scan all sheet names to orient, then read:
   - The **Module Mapping** sheet row for M[X]
   - The **Important Decisions** sheet in full (unit-level constraints)
   - The **Misconceptions** sheet entries for M[X]
4. Read the TVP section for M[X] + transitions in/out.
5. Read the prior module's Starter Pack (`M[X-1]_Starter_Pack.md` or pull from Notion via `sp-notion-sync`) for cross-module reference.
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
- Module Mapping workbook — a multi-sheet Excel file containing:
  - **Module Mapping** (sheet) — M[X] row: learning goals, standards, vocabulary, misconceptions, scaffolding notes
  - **Important Decisions** (sheet) — Unit-level design constraints (CRA path, grid fading sequence, scope boundaries, interaction modality rules). Read once at Task 1; applies to ALL modules.
  - **Misconceptions** (sheet) — Global misconception IDs, observable behaviors, where they surface, priority levels
  - **Conceptual Spine Analysis** (sheet) — Where each concept is introduced/developed/mastered + key transition points. Used for cross-module validation.
  - **Conceptual Development** (sheet) — Cognitive demand level (Activate, Build, etc.) and mathematical move per lesson. Used for CRA calibration.
  - **Standards Mapping** (sheet) — Standard-to-lesson alignment with required vocabulary per standard. Used for D-checks.
  - **Original Curriculum Mapping** (sheet) — Source curriculum lesson narratives, example scenarios, key visual descriptions, practice problems with solutions. Supplementary reference only — Module Mapping is authoritative for sequencing and continuity.
- Tool/Visual Plan (TVP) — this module's section + transitions in/out
- Completed Starter Pack for M[X-1] (if available)
- Toy Specifications (Notion links or local copies)

**Reference Documents (universal):**
- Module Starter Pack Template v2
- Lesson Phase Playbook
- Warmup Phase Playbook
- Exit Check Phase Playbook
- Synthesis Phase Playbook
- Practice Phase Playbook
- Guide vs Prompt Structure Reference
- Voice Script Prompt
- Guide Voice Design Reference
- Starter Pack Structural Skeleton (`STARTER PACK STRUCTURAL SKELETON.md`) — canonical heading hierarchy used by L1 structure checker
- Edtech Activity Queue Rulebook v6 — cognitive verb taxonomy (CREATE/IDENTIFY/COMPARE/APPLY/CONNECT), Practice problem classifications (BASELINE/STRETCH/SUPPORT/CONFIDENCE), session timing targets, EC routing thresholds. Primary reference for Tasks 3–4 (EC + Practice design).

**Plugin Infrastructure (in `.claude/`):**
- `scripts/` — 8 L1 checkers: `sp_structure_check`, `sp_vocab_scan`, `sp_voice_scan`, `sp_interaction_check`, `sp_timing_estimate`, `sp_toy_consistency`, `sp_dimension_track`, `sp_module_map_check`. Plus utilities: `sp_parse_interactions`, `sp_notion_pull`, `sp_notion_push`, `sp_notion_convert_check`.
- `agents/` — 10 L2 evaluation agents: `m42-gate1-eval`, `m42-source-fidelity`, `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval`, `m42-ec-practice-eval`, `m42-synthesis-eval`, `m42-kdd-eval`, `m42-voice-eval`, `m42-cross-module-eval`.
- `skills/` — 5 L3 orchestration skills: `sp-quick-check` (L1 only), `sp-gate-eval` (L1+L2), `sp-full-eval` (batch multi-module), `sp-fix` (apply findings), `sp-notion-sync` (Notion pull/push/edit).

---

## CHAIN OVERVIEW

```
TASK 1: Backbone + Cross-Reference
    ↓
  ══════ GATE 1: sp-gate-eval --gate 1 (L1 × 8 + L2 × 2) → Author Review ══════
    ↓
TASK 2: Warmup + Lesson
    ↓
  ══════ GATE 2: sp-gate-eval --gate 2 (L1 × 8 + L2 × 5) → Author Review ══════
    ↓
TASK 3: Exit Check + Practice + Synthesis + KDD
    ↓
  ══════ GATE 3: sp-gate-eval --gate 3 (L1 × 8 + L2 × 8) → Author Review ══════
    ↓
TASK 4: Full SP Assembly + Notion Push
    ↓
  ══════ GATE 4: sp-gate-eval --gate 4 (L1 × 8 + L2 × 10) → Author Review ══════
    ↓
  sp-notion-sync: Push to Notion → Post evaluation comment
```

---

## PLUGIN ARCHITECTURE (3-Layer Evaluation System)

Generation (Tasks 1–4) produces local markdown files. Evaluation (Gates 1–4) uses the 3-layer plugin system to check them. Fixes are applied locally, then pushed to Notion after Gate 4.

### Layer 1: Python Checkers (deterministic, fast)

8 checkers in `.claude/scripts/`. Each accepts `--gate N --json` and returns structured findings with severity ratings (CRITICAL, MAJOR, MINOR, NOTE). Run time: ~5 seconds per checker.

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

**Invocation:**
```bash
SCRIPTS="<workspace>/.claude/scripts"
python "$SCRIPTS/sp_structure_check.py" "$SP" --gate $GATE --json
```

### Layer 2: LLM Evaluation Agents (qualitative, deep)

10 agent definitions in `.claude/agents/`. Each is a `.md` file that specifies: what to read, what checks to run, and how to report findings. Agents are read-only — they analyze but never modify files.

| Agent | Scope | Gate |
|-------|-------|------|
| `m42-gate1-eval` | Backbone compliance (§1.0–§1.5) | 1+ |
| `m42-source-fidelity` | Source document fidelity (Module Map, TVP, Important Decisions) | 1+ |
| `m42-warmup-eval` | §1.6 Warmup quality (Playbook compliance, hook/bridge, WR checks) | 2+ |
| `m42-lesson-eval` | §1.7 Lesson scripting (CRA, worked examples, scaffolding fading) | 2+ |
| `m42-guide-prompt-eval` | Prompt design across all interactions (independence, Type A/B/C) | 2+ |
| `m42-ec-practice-eval` | §1.8 Exit Check + Practice (alignment, cognitive types, distribution) | 3+ |
| `m42-synthesis-eval` | §1.9 Synthesis (task types, metacognition, closure quality) | 3+ |
| `m42-kdd-eval` | §1.10 Key Design Decisions (completeness, format, embedded flags) | 3+ |
| `m42-voice-eval` | Whole-SP voice quality (warmth spectrum, SDT alignment) | 4 |
| `m42-cross-module-eval` | Cross-module alignment (bridges, vocab handoff, toy progression) | 4 |

### Layer 3: Orchestration Skills

5 skills in `.claude/skills/` that coordinate L1 and L2:

| Skill | When to Use |
|-------|------------|
| `sp-quick-check` | Fast L1-only scan. Good for mid-drafting self-checks. |
| `sp-gate-eval` | Full L1+L2 evaluation at a specific gate. **This is the primary gate evaluation tool.** |
| `sp-gate-eval` at Gate N | Runs all 8 L1 checkers + the gate-scoped L2 agents, produces a consolidated report with cross-layer correlations and a priority fix list. |
| `sp-full-eval` | Batch evaluation across multiple modules. For pre-release unit audit. |
| `sp-fix` | Takes evaluation findings and applies fixes: auto-fix (Category A), semi-auto with confirmation (Category B), or manual with author presentation (Category C). |
| `sp-notion-sync` | Pull SP from Notion → local file, push local file → Notion, or apply targeted Notion edits. Also: evaluate-and-comment (posts findings to Notion page). |

### Gate → Agent Mapping (Quick Reference)

| Gate | L1 Checkers | L2 Agents |
|------|------------|-----------|
| 1 | All 8 | gate1-eval, source-fidelity |
| 2 | All 8 | Gate 1 agents + warmup-eval, lesson-eval, guide-prompt-eval |
| 3 | All 8 | Gate 2 agents + ec-practice-eval, synthesis-eval, kdd-eval |
| 4 | All 8 | Gate 3 agents + voice-eval, cross-module-eval |

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

Create `[Module]_Working_Notes.md` at Task 1 and maintain it throughout. This is a living document that persists across sessions.

**Required sections:**
- **Cross-Reference Table A** — Module Mapping extraction (verbatim)
- **Cross-Reference Table B** — TVP extraction (verbatim)
- **Cross-Reference Table C** — Conflict Log (every discrepancy + resolution)
- **Design Constraints** — Important Decisions extraction (which decisions apply, how they constrain this module)
- **Section Plan** — High-level phase outline
- **Author Flags** — Open questions requiring author decision (numbered, with status)
- **Dimension Tracking** — All dimensions/values used per interaction (prevents accidental reuse)
- **Session Log** — Brief note at start of each session: what was completed, what's next

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
1. Read `[Module]_Working_Notes.md`
2. Read the current state of the SP draft
3. Read the task spec for whatever task is in progress
4. Resume work

---

# TASK 1: BACKBONE + CROSS-REFERENCE

## Read These Documents

| Document | What to Read | Why |
|----------|-------------|-----|
| Module Mapping (sheet) | M[X] row — EVERY column | Source of learning goals, standards, vocabulary, misconceptions |
| Important Decisions (sheet) | All decisions | Unit-level design constraints that apply to every module |
| TVP | M[X] section + transitions in/out | Source of toy configs, data constraints, key beats, SME decisions |
| Module Starter Pack Template v2 | §1.0–§1.5 sections only | Structural format for backbone |
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

## Step 1: Quick Smoke Test (L1 Only)

Run `sp-quick-check` on the Backbone draft at Gate 1:

```bash
# Runs all 8 L1 checkers, gate-scoped to §1.0–§1.5
SCRIPTS="<workspace>/.claude/scripts"
for checker in sp_structure_check sp_vocab_scan sp_voice_scan sp_interaction_check sp_timing_estimate sp_toy_consistency sp_dimension_track sp_module_map_check; do
    python "$SCRIPTS/${checker}.py" "$SP" --gate 1 --json
done
```

If CRITICALs appear, fix before proceeding to L2. Common Gate 1 L1 findings: missing sections (ST), vocabulary list drift from Module Map (MM), structure ordering (ST4/ST11).

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 1. This invokes:
- **All 8 L1 checkers** (re-run for consolidated report)
- **L2 agents:** `m42-gate1-eval` + `m42-source-fidelity`

The agents read: the Backbone draft, the Working Notes (Tables A/B/C, Design Constraints), the Module Mapping sheet, the Important Decisions sheet, the TVP, the Misconceptions sheet, the Conceptual Spine Analysis sheet, the Standards Mapping sheet, and M[X-1] SP if available.

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

---

# TASK 2: WARMUP + LESSON

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
| M[X-1] Starter Pack | §1.9 Synthesis closure only | Warmup callback source |

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

Draft following Template v2 interaction block format:

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

## Step 3: Draft Lesson (§1.7)

Draft following Template v2 format. Include:
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

---

# ══════ GATE 2 ══════

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 2 (scope: §1.0–§1.7). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 2. This invokes:
- **All 8 L1 checkers** at gate 2
- **L2 agents (5):** `m42-gate1-eval`, `m42-source-fidelity`, `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval`

The Gate 2 agents read: the full draft (Backbone + Warmup + Lesson), Working Notes, Warmup Phase Playbook, Lesson Phase Playbook, Guide vs Prompt Structure Reference, TVP (warmup + lesson sections), Conceptual Development sheet, Misconceptions sheet.

**What the L2 agents evaluate at Gate 2:**
- `m42-warmup-eval`: Warmup type selection, hook timing, engagement anchors, bridge quality, WR checklist compliance
- `m42-lesson-eval`: CRA completeness, worked example count/fading, think-aloud elements, vocabulary staging, scaffolding documentation
- `m42-guide-prompt-eval`: Independence test (Guide works alone, Prompt works alone), Type A/B/C classification accuracy, field completeness

**Note on voice:** At Gate 2, voice issues surface through L1's `sp_voice_scan` (mechanical patterns) and L2's `m42-guide-prompt-eval` (structural voice issues in prompts). The dedicated `m42-voice-eval` agent runs at Gate 4 for the comprehensive voice pass. This is intentional — fixing voice before the full SP exists wastes effort on dialogue that may change at Gate 3.

## Step 3: Fix

Run `sp-fix` on findings. Re-run `sp-quick-check` to verify.

## Step 4: Author Review

Author receives: Warmup + Lesson draft + Gate 2 Evaluation Report.

**Review focus:**
- Does the CRA sequence work pedagogically?
- Are worked examples and think-alouds natural, not mechanical?
- Does vocabulary staging feel right for the grade level?
- Are voice findings worth fixing now or acceptable until Gate 4?

---

# TASK 3: EXIT CHECK + PRACTICE + SYNTHESIS + KDD

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
- All EC interactions in Template v2 format
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

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 3 (scope: §1.0–§1.10). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 3. This invokes:
- **All 8 L1 checkers** at gate 3
- **L2 agents (8):** All Gate 2 agents + `m42-ec-practice-eval`, `m42-synthesis-eval`, `m42-kdd-eval`

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

---

# TASK 4: FULL SP ASSEMBLY + NOTION PUSH

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

Use the `sp_notion_push.py` script to convert the assembled SP:

```bash
python <workspace>/.claude/scripts/sp_notion_push.py <assembled_sp.md> --json
```

This handles: YAML → hub properties block, interaction headers → H3, KDD items → H3, [Type A/B/C] label removal, bullet normalization (`*` not `-`), field name v2 compliance, remediation line normalization.

## Step 3: Post-Conversion Verification

Run the Notion conversion checker:

```bash
python <workspace>/.claude/scripts/sp_notion_convert_check.py <notion_ready.md> --json
```

This checks: no old field names, all remediation = Pipeline, no remaining bold interaction headers, no remaining [Type X] labels, [REQUIRED] tags preserved, interaction_count matches, end marker format.

Fix any findings and re-run until clean.

## Step 4: Push to Notion

Use `sp-notion-sync` (Operation 3: Push) to upload the Notion-ready file:

1. **Look up or create the page.** Check the Known Module Pages table in `sp-notion-sync` SKILL.md, or query the database.
2. **Push content** via `notion-update-page` with `replace_content` command (for existing pages) or `notion-create-pages` (for new modules).
3. **Update properties** (Status → "Initial Draft" or "SME Review", Module Number, etc.)
4. **Verify** by fetching the page back and spot-checking 2-3 sections.

**Important Notion behaviors (from M7 experience):**
- Notion automatically adds `\[` escaping to square brackets via its API. This is cosmetic base escaping and renders clean on the page — do not try to remove it.
- The `update_content` API returns `{"page_id":"..."}` even when `old_str` doesn't match (silent success). Always verify edits by re-fetching.
- Large pages (150K+ chars) exceed fetch token limits — results are saved to file and must be searched with Python.

---

# ══════ GATE 4 ══════

## Step 1: Quick Smoke Test

Run `sp-quick-check` at Gate 4 (full SP scope). Fix any CRITICALs before proceeding.

## Step 2: Full Gate Evaluation (L1 + L2)

Run `sp-gate-eval` at Gate 4. This is the **comprehensive audit** — it invokes:
- **All 8 L1 checkers** at gate 4
- **All 10 L2 agents** (Gate 3 agents + `m42-voice-eval`, `m42-cross-module-eval`)

**What the Gate 4 L2 agents add:**
- `m42-voice-eval`: Full warmth spectrum analysis across all phases, SDT alignment (autonomy/competence/relatedness), exclamation calibration, emotion layer progression (warmup energy → lesson focus → EC calm → synthesis reflection), red flag word detection in context, observable-vs-assumed behavior audit
- `m42-cross-module-eval`: Bridge alignment (M[X-1] → M[X] → M[X+1]), vocabulary continuity, toy progression accuracy, misconception arc across modules, scope boundary verification

**Important:** The cross-module agent requires access to M[X-1] SP (and optionally M[X+1]). Pull from Notion via `sp-notion-sync` if not available locally.

Output: Gate 4 Evaluation Report — the definitive quality document for this module. Includes: L1 severity matrix, L2 agent findings, cross-layer correlations, priority fix list (top 10), and gate verdict.

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
1. **Update Notion page status** to "SME Review" via `sp-notion-sync`
2. **Post evaluation summary** as a Notion comment (Operation 5 in `sp-notion-sync`) so SME reviewers see the quality state
3. **Archive the Gate 4 Report** locally as `G3U2M[X]_Gate4_Evaluation_Report.md`
4. SP goes to SME review. After SME approval: SP is production-ready.

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
* **Student Action:** [MC selection / click-to-set / drag-to-place / etc.]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer]
* **Answer Rationale:** [MC only — every option with misconception ID or error type]
* **On Correct:** "[Feedback]"
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

# KNOWN PATTERNS

These are codified from producing Starter Packs. They are design knowledge, not suggestions.

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

### Process
22. **Author Flags are first-class artifacts.** Don't bury decisions that need author input in Design Notes — surface them as numbered Author Flags in the Working Notes and reference them in the SP. If an Author Flag appears embedded in a KDD or interaction block (e.g., `⚠️ PENDING SME RESOLUTION`), extract it to Working Notes and replace with a clean reference (e.g., `> **Author Flag A9** (see Working Notes): [brief description]`). This was a Gate 4 finding on M7.
23. **Working Notes are the continuity mechanism.** Without them, session boundaries cause rework.
24. **Scale progression pedagogy.** The conceptual leap is unit → non-unit, not between non-unit scales.
25. **Practice Phase as distributed reinforcement.** Lessons shouldn't be assessed in isolation.

### Evaluation Pipeline
26. **L1 before L2, always.** Run `sp-quick-check` first. If L1 finds CRITICALs, fix them before wasting tokens on L2 agents that will re-discover the same issues. L1 takes ~5 seconds; L2 takes minutes per agent.
27. **L1 V4 findings may be by-design.** The vocab checker flags assessment vocabulary terms not spoken in EC dialogue. If the EC tests the *skill* that uses those terms (e.g., Equation Builder requires understanding "factor" and "product" without the Guide saying those words), document it as an EC Design Note rather than treating it as a finding. M7 had 11 V4 MAJs that were all intentional design.
28. **Gate 4 is the definitive quality gate.** Gates 1–3 are iterative checkpoints. Don't over-invest in fixing MINOR/NOTE findings at earlier gates — the content will change as later sections are drafted. Gate 4 is where the full cross-layer evaluation matters.
29. **Voice eval at Gate 4, not earlier.** Running the comprehensive voice agent before the full SP exists wastes effort on dialogue that may change when EC and Synthesis are added. L1's `sp_voice_scan` catches mechanical anti-patterns at Gates 1–3; that's sufficient.
30. **Cross-layer correlations are the highest-value findings.** When L1 and L2 flag the same underlying issue from different angles (e.g., L1 vocab checker + L2 source-fidelity both flag a dropped term), that's a systemic issue. Fix those first.

### Extraction Fidelity (from M8 process assessment)
36. **TVP edits must be applied, not footnoted.** When the TVP extraction acknowledges an edit in a parenthetical (e.g., "included per Edit 91") but retains the pre-edit framing, the extraction is incomplete. The Edit Reconciliation Pass (Task 1, Step 5) exists specifically to catch this. M8 had 3 of 5 Backbone issues trace to edits footnoted but not applied.
37. **Data-level constraint audits catch what field-level Conflict Logs miss.** The Conflict Log compares Table A vs Table B at the field level. It does not audit individual data examples (distractor sets, worked problem values, EC items) against the design constraints that govern them. M8's distractor violation (shared factors with correct answers, violating Edit 83) was in the TVP itself — the Conflict Log couldn't catch it because it wasn't a cross-document disagreement.
38. **Backbone-to-extraction diff prevents transfer losses.** Content can be correctly extracted into Table B but fail to transfer into the Backbone draft. The "Are there any others?" guide beat in M8 was present in the TVP extraction but absent from the Backbone. A systematic diff after drafting — walking each Table B entry and confirming it appears in the corresponding §1.X section — catches this.
39. **Problem counts need cross-reference, not single-source capture.** When the TVP specifies a count (e.g., "4 forward problems"), verify it against both the primary spec and any discussion or edit that modified it. M8's forward count (4) matched one TVP source but not the resolved discussion (5-6). Edits to counts are easy to miss because they change a number, not a structural element.

### Notion Integration
31. **Local-first for generation, Notion at the end.** Drafting directly in Notion is slow (160K char fetches, silent API failures, escaping complexity). Draft locally, evaluate locally, push to Notion at Task 4. Use `sp-notion-sync` for the push.
32. **Notion bracket escaping is cosmetic.** Notion's API automatically adds `\[` before square brackets. This renders clean on the page (no visible backslashes). Do not try to remove it — Notion will re-add it on every save. Only fix triple-escaped patterns (`\\\[`) which show visible backslashes.
33. **Verify every Notion edit.** The `update_content` API returns success even when `old_str` doesn't match. Always re-fetch and check after edits. For batch edits, use `replace_all_matches: true` when the pattern occurs multiple times.
34. **Post-push evaluation.** After pushing to Notion, pull the page back via `sp_notion_pull.py` and run `sp-quick-check` on the pulled copy. The round-trip can introduce formatting changes that create new findings.
35. **ALL CAPS = vocabulary standout, not excitement.** Terms like `ACTIVATION`, `MYSTERY REVEAL`, `JUDGMENT` in interaction headers are deliberate vocabulary emphasis per the SP template. Do NOT lowercase them. The L1 voice checker knows to skip these.

---

**END OF COWORK GUIDANCE**
