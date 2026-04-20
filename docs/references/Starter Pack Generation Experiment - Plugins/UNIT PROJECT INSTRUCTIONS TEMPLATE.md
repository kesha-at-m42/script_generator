# Grade [X], Unit [Y]: [Unit Title] — Project Instructions

## Unit Overview

**Unit:** [Y] — [Unit Title]
**Grade:** [X]
**Modules:** [N] (M1–M[N])
**Source Curriculum:** Open Up Resources / Illustrative Mathematics Grade [X], Unit [Y]
**TVP:** `[TVP filename].xlsx` (in this folder)
**Toy Flow:** `[Toy Flow filename if exists]` (in this folder)

## Module Sequence

<!-- Organize by tier/section as defined in the TVP. Use the tier structure from the Module Mapping sheet. -->

### [Tier/Section Name]: [Description]
| Module | Core Concept | Source | CRA Balance |
|--------|-------------|--------|-------------|
| M1 | [Core concept from TVP] | [OUR source lessons + transformation tag] | [CONC/PROC/TRANS from Component Balance Hypothesis] |
| M2 | | | |

### [Tier/Section Name]: [Description]
| Module | Core Concept | Source | CRA Balance |
|--------|-------------|--------|-------------|
| M3 | | | |
| M4 | | | |

<!-- Add more tier/section tables as needed. Every module must appear in exactly one table. -->

## Key Design Decisions (Unit-Level)

<!-- Pull from TVP "Important Decisions" sheet. Include only RESOLVED decisions. Format: D# — bold topic sentence, then 1-2 sentence summary of the decision made. -->

Resolved in the TVP. Do not re-litigate in individual module chats unless new evidence surfaces.

- **D1 — [Topic].** [Decision summary.]
- **D2 — [Topic].** [Decision summary.]

<!-- Include all resolved decisions. Omit "FOR SME" decisions that remain unresolved — list those separately below if any. -->

### Unresolved Decisions (if any)

<!-- List any TVP decisions still marked "FOR SME" that may affect module generation. Flag which modules are blocked. -->

| Decision | Topic | Affects Modules | Status |
|----------|-------|----------------|--------|
| D[N] | [Topic] | M[X]–M[Y] | Awaiting SME input |

## Unit-Level Vocabulary Progression

<!-- Build from TVP "Vocabulary to Teach" column. The goal is to show cross-module staging — when each term is introduced and where it's reinforced. This is the authoritative reference for [vocab] markup decisions. -->

The TVP's "Vocabulary to Teach" column is authoritative. Cross-module staging:

| Term | Introduced | Reinforced Through | Notes |
|------|-----------|-------------------|-------|
| [term] | M[X] (NEW or review from G[N]) | M[Y], M[Z] | [Teaching notes — formal vs informal, Grade 2 review, etc.] |

<!-- Guidelines:
- Mark terms as NEW (first time in this grade) or "review from G[N]" (prior grade)
- Note any term that transitions from informal to formal across modules
- Include compound terms as they appear (e.g., "equal parts" not "equal" + "parts")
- This table feeds directly into the Vocabulary Reinforcement Plan in each module's §1.7
-->

## Cross-Module Bridge Chain

<!-- The planned narrative arc connecting each module to the next. These are drafts — the actual bridge text will be written in each module's §1.9 and recorded in the Working Notes. The arrow descriptions here serve as authoring guidance for bridge tone and direction. -->

Track in `UNIT[Y]_WORKING_NOTES.md` as each module completes.

- M1 → M2: [Conceptual bridge — what M1 established → what M2 builds on]
- M2 → M3: [...]
- M[N-1] → M[N]: [...]

<!-- For the final module: note what the NEXT unit expects students to bring. Check the next unit's TVP "Standards - Building On" column for M1. -->

## Pipeline Workflow

### Chat Structure

One chat per Task per module. Name chats: `G[X]U[Y] M[N] Task [T]`

| Chat | Scope | Gate |
|------|-------|------|
| M[X] Task 1 | Backbone + Cross-Reference | Gate 1 |
| M[X] Task 2 | Warmup + Lesson | Gate 2 |
| M[X] Task 3 | EC + Practice + Synthesis + KDD | Gate 3 |
| M[X] Task 4 | Final eval + fixes + Notion push | Gate 4 |

### Before Each Module

1. Read the TVP row for this module (Module Mapping sheet)
2. Read the Working Notes for the prior module's bridge-to-next text
3. Read the prior module's §1.9 (Forward Bridge) if available
4. Check the Toy Flow document for this module's toy assignments (if available)
5. Check the Misconceptions sheet/column for this module's key risks
6. **Verify prior gate artifacts exist.** If this is Task 2+, check that the Working Notes list a real file path for the prior gate's eval output. If the path is missing or the file doesn't exist, re-run the gate eval before proceeding. (This prevents post-compaction fabrication — see Known Pattern context in Cowork Guidance.)
7. **Check Toy Specification Notion links.** Confirm that the Notion page IDs for every toy this module uses are accessible. Copy them into Working Notes Table A so they are available during drafting.

### After Each Module (Task 4 Complete)

**⚠️ REQUIRED — do not skip:** Update `UNIT[Y]_WORKING_NOTES.md` with:
- Vocabulary terms introduced (with introduction interaction IDs)
- Bridge-to-next exact text (from §1.9)
- Dimension values used (number ranges, problem types, etc.)
- Toy configurations used
- Gate eval artifact paths (file path for each completed gate's eval report)
- Any open Author Flags affecting downstream modules
- Any module-specific fields (see Working Notes template for examples)

This is the cross-module baton — the next module's Task 1 chat reads it. If skipped, cross-module continuity breaks.

**Also required:** Save gate eval reports at every gate as standalone files (`G[X]U[Y]M[XX]_Gate[N]_Evaluation.md`), not just Gate 4.

### Structural Documents (Shared — Do Not Duplicate)

All in the parent `Starter Pack Generation Experiment - Plugins/` folder:
- `MODULE STARTER PACK TEMPLATE.02.04.26.md` — format authority
- `Module Starter Pack Cowork Guidance.md` — pipeline + Known Patterns
- `Lesson Phase Playbook.md`
- `Warmup Phase Playbook.md`
- `Exit Check Phase Playbook.md`
- `Synthesis Phase Playbook.md`
- `PRACTICE PHASE PLAYBOOK v3.md`
- `Guide Voice Design Reference - 01.09.26.md`
- `GUIDE vs PROMPT Structure Reference.md`

### Key Misconceptions for This Unit

<!-- Pull from TVP "Key Misconceptions" column. Group by misconception ID. List which modules primarily target each one. This gives each Task 1 chat a quick lookup for which misconceptions to emphasize in the backbone. -->

| ID | Misconception | Primary Module(s) |
|----|--------------|-------------------|
| [ID] | [Description] | M[X], M[Y] |

### Special Considerations for This Unit

<!-- Unit-level authoring guidance that doesn't fit elsewhere. Examples:
- Prerequisite assumptions (what should students bring from prior units?)
- Tonal shifts (where does the unit feel different?)
- Known engineering dependencies or toy limitations
- Diagnostic gates or remediation checkpoints
- SME-flagged risk areas
-->

1. **[Consideration].** [Explanation of why this matters and how it affects module generation.]
2. **No non-template artifacts in the SP body.** Dimension tracking tables, balance calculations, data summaries, and authoring-only annotations belong in Working Notes, not the Starter Pack. The SP body should contain only template-defined sections and fields.
