# MISSION42 STARTER PACK PLUGIN ARCHITECTURE

**Version:** 0.2 — Revised per Author Feedback
**Date:** 2026-03-24
**Purpose:** Replace the current monolithic gate evaluation system with a layered plugin architecture that eliminates missed findings, reduces variance, and removes the separate-chat workflow.

---

## PROBLEM STATEMENT

The current Cowork Guidance defines 4 drafting tasks and 4 evaluation gates. In practice, three problems undermine the system:

1. **Gates miss things.** The evaluation agents are reading a 690-line monolithic eval prompt plus multiple source documents, then trying to hold 15-20 checks in context simultaneously. Attention degrades. Mechanical checks (vocabulary scanning, field presence, interaction format) are done by the LLM and are therefore non-deterministic.

2. **Workflow friction.** Gates aren't reliably invoked from within the drafting session. The author runs evaluations in a separate chat, then manually bridges findings back. Every round-trip costs time and introduces transcription risk.

3. **Output variance.** The same gate run on the same draft can produce different findings depending on what the model attends to, how it interprets "spot-check," and whether it actually reads every source document it's told to.

Additionally, a gap analysis of all guidance documents reveals that the current gates cover roughly 40-50% of the checkable requirements defined across the Template, Playbooks, Voice references, Audit Prompt, and Activity Queue Rulebook.

---

## ARCHITECTURE OVERVIEW

Three layers, each solving a different problem:

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 3: ORCHESTRATION SKILLS                          │
│  Gate skills that wire checkers + agents together        │
│  Invoked from within the drafting session                │
│  → Solves: workflow friction (Problem 2)                 │
├─────────────────────────────────────────────────────────┤
│  LAYER 2: FOCUSED EVAL AGENTS                           │
│  One agent per judgment domain, narrow context           │
│  Each embeds ONLY its checks + required source refs      │
│  → Solves: missed findings + variance (Problems 1 & 3)  │
├─────────────────────────────────────────────────────────┤
│  LAYER 1: PROGRAMMATIC CHECKERS                         │
│  Deterministic scripts for mechanical checks             │
│  Zero variance, instant, catches everything              │
│  → Solves: variance + coverage (Problems 1 & 3)         │
└─────────────────────────────────────────────────────────┘
```

---

## CROSS-CUTTING DESIGN DECISIONS

### Stage Awareness

The SP is built incrementally across 4 tasks. At any given gate, only a subset of sections exist:

| Gate | Sections in Scope | What's New | What's Approved Prior |
|------|------------------|-----------|----------------------|
| Gate 1 | §1.0–§1.5 + Working Notes | Backbone + Cross-Reference Tables | — |
| Gate 2 | §1.0–§1.7 | §1.6 Warmup + §1.7 Lesson | §1.0–§1.5 |
| Gate 3 | §1.0–§1.10 | §1.8 EC + §1.8.5 Practice + §1.9 Synthesis + §1.10 KDD | §1.0–§1.7 |
| Gate 4 | Full SP + Notion-ready file | Assembled document + Notion conversion | §1.0–§1.10 |

Every Layer 1 checker accepts a `--gate N` parameter that controls scope. At Gate 1, `sp_interaction_check.py` skips interaction format checks (no interactions exist yet). At Gate 2, `sp_vocab_scan.py` scans Guide/Prompt lines in §1.6–§1.7 but validates vocabulary completeness against the approved §1.3. At Gate 4, everything runs against the full document.

Each checker's stage-specific behavior is documented in its **Stage Scope** subsection below.

### Layer 1 → Layer 2 Handoff

Checkers write structured JSON output to `.claude/eval-outputs/[checker-name]-[module]-gate[N].json`. Each agent's document manifest includes a directive to read its relevant checker outputs from this directory before starting judgment checks. This keeps the agent prompt clean (no serialized JSON in the prompt string) and makes checker outputs reviewable by the author.

Example: At Gate 2, after checkers run, the eval-outputs directory contains:
```
.claude/eval-outputs/
├── sp_interaction_check-M06-gate2.json
├── sp_vocab_scan-M06-gate2.json
├── sp_voice_scan-M06-gate2.json
├── sp_dimension_track-M06-gate2.json
└── sp_timing_estimate-M06-gate2.json
```

Each agent reads the files relevant to its domain. The agent's prompt says: "Read the mechanical findings in `.claude/eval-outputs/` first. These issues are already caught — do not re-check them. Focus your attention on judgment-based checks."

### Revision Loop

Gates are not one-shot evaluations. Each gate skill implements this cycle:

```
Run Layer 1 checkers
    ↓
Launch Layer 2 agents (in parallel where possible)
    ↓
Collect all findings into unified report
    ↓
Present findings to author with severity counts + priority fixes
    ↓
Author reviews, directs fixes (or approves as-is)
    ↓
Cowork makes directed fixes
    ↓
Re-run affected checkers to verify fixes landed
    ↓
IF new findings → present delta report → repeat
    ↓
Author approves → gate passed → proceed to next task
```

The re-run step is targeted: if the author fixed a vocabulary issue, only `sp_vocab_scan.py` re-runs. If a structural fix was made, `sp_structure_check.py` re-runs. Agents are NOT re-launched for verification — the mechanical checkers confirm the fix, and the author uses judgment on whether the agent's qualitative findings have been addressed.

### Upstream Revision Handling

Sometimes a Gate 2 finding requires changes to the backbone (§1.0–§1.5) that was approved at Gate 1. For example: the Lesson draft reveals that the vocabulary staging plan in §1.3 doesn't work in practice, or an interaction design exposes a gap in §1.5 toy specifications.

When an agent identifies a finding that requires changes to a section approved at a prior gate, it flags the finding with an **UPSTREAM** tag:

```
| # | Severity | Location | Finding | Upstream? | Recommended Fix |
|---|----------|----------|---------|-----------|-----------------|
| L3.07 | MAJOR | §1.7 Int 2.3 | Vocab "area model" used before §1.3 staging | UPSTREAM: §1.3 | Either move staging earlier in §1.3 or defer this interaction |
```

The gate skill collects upstream findings into a separate section of the report. The author decides whether to:
- (a) Fix upstream (edit the approved section) — triggers re-run of the prior gate's checkers on the modified section
- (b) Fix downstream (change the new content to fit the approved section)
- (c) Document as KDD (the departure is intentional)

This prevents the current failure mode where approved sections accumulate hidden inconsistencies as later phases are drafted.

---

## LAYER 1: PROGRAMMATIC CHECKERS

These are Python/bash scripts that run deterministic checks. They write structured JSON output to `.claude/eval-outputs/` for Layer 2 agents to consume. They never miss, never vary, and run in seconds.

All checkers accept `--gate N` to control scope and `--module MXX` for file naming.

### Checker 1: `sp_structure_check.py`

**What it checks:** Structural presence and ordering of all required sections.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: §1.0–§1.5 + YAML. Checks backbone sections only. Does not flag missing §1.6–§1.10.
- Gate 2: §1.0–§1.7. Adds check for §1.6 and §1.7 presence + subsection structure (§1.7.4, §1.7.5).
- Gate 3: §1.0–§1.10. Full section set minus end marker and §1.11.
- Gate 4: Everything. Full section set + end marker + §1.11.

**Checks:**
- YAML front matter present with all required fields (`module_id`, `unit`, `domain`, `primary_toys` as name/url objects, `secondary_toys`, `interaction_tools`)
- No legacy YAML fields (`path`, `fractions_required`, `shapes`)
- All required sections present: §1.0 through §1.10 + end marker
- Conditional sections flagged if expected but absent (§1.1.4, §1.5.X Data Constraints, §1.8.5)
- Section ordering correct (§1.0 → §1.1 → ... → §1.10 → end marker)
- No duplicate sections
- No placeholder text: `[TBD]`, `[Section to be added]`, `[PLACEHOLDER]`
- No development tags: `[Modeling]`, `[MODIFY]`, `[Vocab_Staging]`, `[Tool_Intro]`
- No `Detail Level:` markers
- Version line present
- §1.11 Final Formatting Audit present (if full SP)
- Heading hierarchy correct (H2 for primary sections, H3 for subsections/interactions)
- End marker format: `# END OF MODULE [X] STARTER PACK`

**Output:** JSON findings list with severity, location, finding text, and recommended fix.

---

### Checker 2: `sp_interaction_check.py`

**What it checks:** Every interaction block for format compliance.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Skipped (no interactions in backbone).
- Gate 2: Checks §1.6 and §1.7 interactions only.
- Gate 3: Checks §1.8 and §1.9 interactions. Also re-validates aggregate counts across §1.6–§1.9.
- Gate 4: All interactions across all phases.

**Checks (per interaction):**

*Pattern 1 (student action):*
- `Purpose:` field present
- `Visual:` field present, starts with `**Visual: [Toy Name] ([Mode]).**`, is one line
- `Guide:` field present with quoted dialogue
- `Prompt:` field present with quoted instruction
- `Student Action:` field present with typed action
- `Correct Answer:` field present
- `On Correct:` field present
- `Remediation: Pipeline` present (no intensity qualifiers, no authored dialogue)
- If MC: `Options:` field present, `Answer Rationale:` field present

*Pattern 2 (teaching only):*
- `Visual:` field present
- `Guide:` field present
- Ends with `**No student action.**`
- Does NOT have `Prompt:`, `Student Action:`, `Correct Answer:`, or `Remediation:` fields

*Pattern 3 (system-driven):*
- Specification table or equivalent present
- `On Complete:` block present
- Design Note explaining why Pattern 1/2 don't apply

*All patterns:*
- Interaction header has pedagogical type label in brackets (e.g., `[WORKED EXAMPLE]`, `[ACTIVATION]`)
- No legacy `[Type A]`, `[Type B]`, `[Type C]` labels
- Annotations (Design Notes, Voice Notes, Scaffolding Notes, Remediation Notes) appear AFTER blocks, not within
- Exception: `Connection:` field in Synthesis appears WITHIN block

*Multi-step interactions:*
- Parent has Purpose and overall Visual
- Each sub-part with student action has own Guide, Prompt, Student Action, Correct Answer, Remediation

**Aggregate checks:**
- Total interaction count per phase (Warmup: 2-5, Lesson: 6+, EC: per Parameters table, Synthesis: 3-4 tasks + frame + closure)
- `interaction_count` in YAML/hub properties matches actual H3 interaction count
- Phase Structure Preview (§1.1.4) counts match actual counts (if present)

**Output:** JSON with per-interaction findings + aggregate summary.

---

### Checker 3: `sp_vocab_scan.py`

**What it checks:** Vocabulary compliance across all dialogue lines.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Completeness checks only — every term in "Vocabulary to Teach" accounted for in §1.2/§1.3, every term in "Vocabulary to Avoid" in §1.3 Terms to Avoid. No dialogue lines to scan yet.
- Gate 2: Adds dialogue scanning of §1.6–§1.7 Guide/Prompt/On Correct lines against Terms to Avoid + Forbidden Phrases. Checks vocabulary timing against §1.3 staging.
- Gate 3: Scans §1.8–§1.9 dialogue. Also checks Assessment Vocabulary appears in EC. Cross-phase timing validation.
- Gate 4: Full scan of all phases.

**Checks:**
- Every term in "Terms to Avoid" scanned against ALL `Guide:`, `Prompt:`, and `On Correct:` lines — reports exact matches with interaction ID and line
- Every term in "Forbidden Phrases" (if §1.7 has this section) scanned the same way
- Vocabulary timing: no formal vocabulary term appears in any dialogue line BEFORE its designated staging phase in §1.3
- Vocabulary completeness: every term in "Vocabulary to Teach" (from Module Mapping / Table A) appears in §1.2 Must Teach or §1.3 Staging table
- Every term in "Vocabulary to Avoid" appears in §1.3 Terms to Avoid
- Assessment Vocabulary terms appear in at least one EC interaction
- Session-relative language: no "yesterday," "today," "tomorrow" in Guide/Prompt/On Correct
- No "Module X" numbers in student-facing dialogue (Guide/Prompt/On Correct)

**Output:** JSON with per-violation findings including exact text match, interaction ID, and line content.

---

### Checker 4: `sp_voice_scan.py`

**What it checks:** Mechanical voice rule violations.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Skipped (no dialogue lines in backbone).
- Gate 2: Scans §1.6–§1.7 dialogue.
- Gate 3: Scans §1.8–§1.9 dialogue. Phase-level exclamation count now includes all phases.
- Gate 4: Full scan across all phases.

**Checks:**
- **Red flag word scan:** Scan all `Guide:`, `Prompt:`, `On Correct:` lines for: carefully, thoroughly, systematically, understanding, confused, clarity, persistence, perseverance, determination, excited, proud, confident, frustrated, happy, nervous, eager, enthusiastic, approach, method, strategy, technique, "to be sure," "because you wanted," "in order to," "so that you could"
- **Exclamation count:** Count `!` per phase. Flag if zero across entire module. Flag if >1 per 3 interactions in any phase.
- **Anti-pattern scan:** Scan for: "Perfect!", "Excellent!", "Amazing!", "Incredible!", "Fantastic!", "You're so smart!", "You're a mathematician!", "You have to...", "You need to...", "I want you to...", "I need you to...", "Can you..." (rhetorical command), "Let's" frequency (>1 per 3 interactions)
- **Conciseness check:** Count sentences in each `Guide:` line before the instruction portion. Flag any with 4+ sentences.
- **Contraction check:** Flag `Guide:` lines that use "let us," "you are," "do not," "it is," "that is" instead of contractions (except when used for emphasis in caps)
- **Generic praise scan:** Flag "Good job!", "Great work!", "Well done!", "Nice!" (without specifics following)

**Output:** JSON with per-violation findings including exact text, interaction ID, category, and suggested replacement.

---

### Checker 5: `sp_dimension_track.py`

**What it checks:** Dimensions and values used across interactions.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Validates §1.5 data constraint internal consistency only (example values within stated ranges).
- Gate 2: Tracks dimensions in §1.6–§1.7 interactions. Validates against §1.5 constraints.
- Gate 3: Adds §1.8–§1.9. Flags EC values identical to Lesson values. Cross-phase comparison.
- Gate 4: Full tracking across all phases.

**Checks:**
- Parse all `Visual:` lines and `Correct Answer:` lines to extract dimensions, values, areas, factors, tile counts
- Build a usage table: which values appear in which interactions
- Flag exact dimension reuse across interactions (unless documented in Design Note or KDD)
- Flag values outside §1.5 stated constraint ranges
- Flag EC values that are identical to Lesson values (unless KDD justifies)
- Flag Synthesis values identical to Lesson or EC values

**Output:** JSON dimension tracking table + violation findings.

---

### Checker 6: `sp_toy_consistency.py`

**What it checks:** Toy naming and configuration consistency.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Validates §1.5 structure (Notion Spec, Changes from M[N-1], Module Configuration table, Guardrails table, v2 naming, Interaction Constraints block).
- Gate 2: Adds cross-reference: every toy in §1.6–§1.7 Visual: lines matches §1.5.
- Gate 3: Adds §1.8–§1.9 cross-reference.
- Gate 4: Full cross-reference. Every §1.5 toy used in at least one interaction.

**Checks:**
- Every toy name in `Visual:` lines matches a toy defined in §1.5
- Every toy in §1.5 appears in at least one interaction
- Toy naming is consistent (same toy not called different things in different places)
- No descriptive suffixes on toy names ("— Reduced Role", "— Full Variety")
- Mode specified in parentheses only when non-default
- §1.5 has required subsections for each toy: Notion Spec line, Changes from M[N-1] line, Module Configuration table, Guardrails table
- §1.5 naming is v2: "Module Configuration" not "Core Specifications," "Guardrails" not "M[X]-Specific Constraints"
- Interaction Constraints block (universal NO list) present at end of §1.5

**Output:** JSON with toy inventory, cross-reference, and violation findings.

---

### Checker 7: `sp_timing_estimate.py`

**What it checks:** Whether phase durations are realistic against Activity Queue Rulebook targets.

**Inputs:** The Starter Pack markdown file + `--gate N`.

**Stage Scope:**
- Gate 1: Skipped (no interactions to time).
- Gate 2: Estimates Warmup + Lesson timing.
- Gate 3: Adds EC + Synthesis. Produces full session estimate.
- Gate 4: Re-runs on assembled document for final timing check.

**Checks:**
- Count interactions per phase
- Estimate timing per interaction (rough heuristic: teaching-only ~20-30s, student-action ~30-60s, MC ~45-60s, multi-step ~60-90s)
- Compare against Rulebook targets: Warmup 2-3 min, Lesson 8-10 min, EC 3-4 min, Synthesis 5-7 min (total ~25-30 min)
- Flag phases significantly over or under target
- Flag if Warmup exceeds 5 minutes (hard cap in Template)

**Note:** These are rough ballpark estimates, not authoritative timing predictions. The value is catching obviously over- or under-scoped phases, not precision.

**Output:** JSON timing estimate per phase + compliance assessment.

---

### Standalone Checker: `sp_notion_convert_check.py`

**What it checks:** Notion conversion compliance.

**Not part of the gate system.** Runs as a standalone verification immediately after Notion conversion (Task 4 Step 2), before the final Gate 4 quality evaluation. Notion conversion is a mechanical transformation — it either works or doesn't — and should be verified and fixed before the quality gate runs.

**Inputs:** The Notion-ready markdown file (`[Module]_Notion_Ready.md`).

**Checks:**
- YAML front matter replaced with HTML comment block containing hub properties
- Interaction headers at H3 level (not bold)
- KDD items at H3 level (not numbered list)
- No `[Type A/B/C]` labels in headers
- Bullet style uses `*` not `-` (except checklists)
- No old field names: `Method:`, `Validation:`, `Detail Level:`
- All `Student Action:` (not `Method:`), all `Correct Answer:` (not `Validation:`)
- All remediation lines say exactly `Pipeline`
- `[REQUIRED]` tags preserved
- `interaction_count` in hub properties matches actual H3 interaction count
- End marker format correct
- Misconception headers use `#[ID]: [Name]` format

**Output:** JSON findings list. Fix all findings before proceeding to Gate 4.

---

## LAYER 2: FOCUSED EVAL AGENTS

Each agent has a single evaluation domain, embeds only its own checks, specifies its tools and model, and receives Layer 1 mechanical findings as input (so it doesn't waste attention on things already caught).

All agents are read-only (tools: Read, Grep, Glob). Default model is `opus` for maximum judgment quality; exceptions noted per agent.

### Agent 1: `m42-source-fidelity.md`

**Gate mapping:** Replaces current Gate 1 A-checks + D-checks + SP-checks.

**Domain:** Verifying that cross-reference tables and the backbone accurately reflect source documents.

**Receives from Layer 1:** `sp_structure_check` output (so it skips structural presence checks), `sp_vocab_scan` output (so it skips mechanical vocabulary completeness).

**Judgment checks:**
- A1: Module Mapping extraction completeness — every populated column in Table A, values verbatim (not summarized)
- A2: TVP extraction completeness — every section in Table B, verbatim
- A3: Important Decisions extraction — every applicable decision with specific implication statement
- A4: Conflict Log completeness — every discrepancy between sources logged, resolutions follow hierarchy
- A5: Misconceptions extraction — global IDs, observable behaviors, priority levels match database
- A6: Conceptual Spine validation — concept intro/develop/master placement correct for this module
- A7: Standards Mapping validation — standards in §1.1.1 match Standards Mapping sheet, required vocabulary per standard present in §1.3
- A8: TVP key beats — every key beat has a corresponding planned interaction, verbatim language preserved for load-bearing notes
- A9: SME-resolved decisions — every resolution reflected in SP, none still listed as open
- A10: Inter-module content consistency — no content M[X] practices that M[X+1] claims to introduce
- D1-D5: Design constraint compliance — every applicable Important Decision reflected in backbone
- AF1: Author Flag identification — are flags properly identified? Genuine decision points that can't be resolved from sources? Or are any resolvable from the documents (and therefore shouldn't be flags)?
- AF2: Author Flag completeness — any decision points the drafter didn't flag that should be flagged?

**Document manifest (what to read, in order):**
1. Layer 1 findings (provided as input)
2. Working Notes (Tables A, B, C, Design Constraints)
3. Module Mapping sheet — M[X] row (fresh read)
4. Important Decisions sheet (fresh read)
5. TVP — M[X] section + transitions (fresh read)
6. Misconceptions sheet — M[X] entries
7. Conceptual Spine Analysis sheet
8. Standards Mapping sheet
9. Backbone draft (§1.0–§1.5)
10. M[X-1] Starter Pack (if available)

**Output format:** Structured findings table (ID, Severity, Location, Finding, Source citation, Recommendation) + summary counts + verdict.

---

### Agent 2: `m42-warmup-eval.md`

**Gate mapping:** NEW — currently not covered by any gate.

**Model:** `sonnet` — Warmup evaluation is a simpler domain (fewer checks, less source cross-referencing) than Lesson or Source Fidelity. Sonnet handles it well and saves the Opus budget for the heavier agents.

**Domain:** Warmup Phase Playbook compliance and pedagogical quality.

**Receives from Layer 1:** `sp_interaction_check` output (Warmup section), `sp_voice_scan` output (Warmup section).

**Judgment checks:**
- Hook present in first 15-20 seconds / first interaction
- Hook quality: creates curiosity or connection, doesn't teach
- Engagement anchors: 2+ present, from approved types (Narrative, Personalization, Choice, Strength Prompt), different types
- Judgment/noticing task present (not just clicking)
- Warmup type selection appropriate for module level (per Playbook §4D recommendations)
- Bridge quality: creates anticipation for Lesson without teaching content
- No formal vocabulary introduction
- Cognitive load appropriate (20-30% — no complex new concepts)
- Maximum 2 visual states (exceptions require KDD)
- Instructions under 15 words per prompt
- Core Purpose section quality: Key Function present and substantive, "Why this serves the concept" rationale present, necessity Test answers YES with specific explanation
- Warmup Parameters table present and reasonable
- Warmup Constraints table present (MUST / MUST NOT)
- Warmup Verification Checklist present and items match content
- Session-relative language only
- Bridge does not duplicate Lesson Purpose Frame

**Document manifest:**
1. Layer 1 findings
2. Warmup draft (§1.6)
3. Approved Backbone (§1.0, §1.3, §1.5)
4. Warmup Phase Playbook (full read)
5. TVP — M[X] warmup section
6. M[X-1] Starter Pack — §1.9 Synthesis closure (for callback verification)

---

### Agent 3: `m42-lesson-eval.md`

**Gate mapping:** Replaces current Gate 2 B-checks (CRA) + expands with full Lesson Playbook compliance.

**Domain:** Lesson Phase Playbook compliance, CRA quality, and interaction pedagogy.

**Receives from Layer 1:** `sp_interaction_check` output (Lesson section), `sp_vocab_scan` output, `sp_voice_scan` output, `sp_dimension_track` output.

**Judgment checks:**

*CRA Phase Quality:*
- Concrete phase: student physically manipulates toy, worked example with think-aloud precedes first attempt, think-aloud has [PLANNING], [ATTENTION], [SELF-CHECK] tags, example-problem pair present
- Relational phase: DEDICATED interaction (not embedded in vocabulary intro), 2+ concrete examples displayed simultaneously, Guide explicitly states pattern, student confirms
- Abstract phase (vocabulary): formal terms introduced AFTER concrete + relational, follows sequence (reference experience → introduce term → connect to visual), student applies vocabulary immediately after teaching
- Application phase: 2+ independent interactions, decreasing Guide support visible, new contexts introduced

*Lesson Structure:*
- Purpose Frame present at opening (or omission documented in KDD with rationale)
- Purpose Frame quality: only previously-known vocabulary, concrete/behavioral language, connects backward + forward, ≤15 seconds (~2-3 sentences)
- Worked example count (minimum 2-3) with fading structure labeled (full → partial → independent)
- Section transition markers present between sections (`→ SECTION X COMPLETE.`)
- Required Phrases section present with every vocabulary word and assessment language
- Forbidden Phrases section present with ❌ prefix and misconception explanations
- Misconception Prevention section present with per-misconception strategies referencing specific interaction IDs
- Incomplete Script Flags present (§1.7.4)
- Success Criteria present (§1.7.5), restates The One Thing in observable terms

*Interaction Quality:*
- Guide/Prompt independence verified on representative interactions (cover Guide, read Prompt — can student complete? Cover Prompt, read Guide — can student complete?)
- No teaching content in Prompt fields
- Observation windows: instruction follows demonstration within 15-30 seconds
- Active vs Passive: student acts in every non-teaching interaction

*Pedagogical Flow:*
- CRA stages labeled on interactions
- Scaffolding stages annotated
- Vocabulary staging matches §1.3 exactly
- Cognitive demand levels align with Conceptual Development sheet (if available)

**Document manifest:**
1. Layer 1 findings
2. Lesson draft (§1.7)
3. Approved Backbone (§1.0–§1.5)
4. Lesson Phase Playbook (full read)
5. Guide vs Prompt Structure Reference
6. TVP — M[X] lesson sections
7. Working Notes (Tables A/B, Section Plan)
8. Conceptual Development sheet (if available)

---

### Agent 4: `m42-ec-practice-eval.md`

**Gate mapping:** Replaces current Gate 3 F-checks + H-checks, adds EC Playbook depth.

**Domain:** Exit Check alignment, Practice inputs, and EC Playbook compliance.

**Receives from Layer 1:** `sp_interaction_check` output (EC section), `sp_dimension_track` output, `sp_timing_estimate` output.

**Judgment checks:**

*EC Alignment:*
- Every EC problem tests a skill explicitly taught in Lesson with student action (not just mentioned)
- Alignment Check table present and correct (each problem → Lesson section)
- Same toys, modes, and interaction types as Lesson
- No new visual models, interaction types, vocabulary, or concepts
- EC difficulty does not exceed Lesson difficulty (representative middle)
- EC values within Lesson constraints but NOT identical (unless KDD justifies)

*EC Playbook Compliance:*
- Module-level cognitive type restrictions enforced: M1-3 CREATE+IDENTIFY only; M4-6 add COMPARE if taught; M7-12 all types available
- Problem count matches Parameters table (typically 3)
- Transition frame present with low-stakes, no-pressure language
- Feedback brevity (5-10 words per On Correct)
- SUPPORT tier documented if TVP specifies

*Practice Inputs:*
- Distribution targets present and consistent with Playbook module-range recommendations
- Toy constraints table present
- Dimensions Used tracking table present
- Each skill maps to a specific Lesson section
- Non-assessed skills flagged ("exposure skill — not assessed")
- Cross-module spiral references present for M2+ modules

**Document manifest:**
1. Layer 1 findings
2. EC draft (§1.8) + Practice Inputs (§1.8.5)
3. Approved Backbone + Lesson
4. Exit Check Phase Playbook (full read)
5. Practice Phase Playbook (§inputs section)
6. TVP — M[X] EC and practice sections
7. Misconceptions sheet — "Where Likely to Surface" column
8. Working Notes (dimensions tracking)

---

### Agent 5: `m42-synthesis-eval.md`

**Gate mapping:** Replaces current Gate 3 G-checks, adds Synthesis Playbook depth.

**Domain:** Synthesis Phase Playbook compliance and quality.

**Receives from Layer 1:** `sp_interaction_check` output (Synthesis section), `sp_voice_scan` output (Synthesis section).

**Judgment checks:**
- Opening frame present (30-45 seconds), signals reflection shift
- At least 2 different task types used from: Pattern Discovery, Representation Transfer, Real-World Bridge, Metacognitive Reflection
- Module-level task type recommendations applied (Early modules: A+C, Middle: all, Late: B+D emphasized)
- At least 1 metacognitive reflection present
- Metacognitive reflection type selection appropriate for module level (Types 1+3 for M1-6, all for M7-12)
- Connection: field present on every Synthesis task
- Every task connects to student experience from Lesson (not new teaching)
- Tasks are cognitively distinct (not variations of same check)
- Consolidation moment present if module taught 2+ strategies (explicit side-by-side review)
- Identity-building closure is behaviorally specific (names what student actually did/discovered)
- Closure avoids generic praise
- Closure previews next module without teaching it
- Bridge to M[X+1] matches TVP transition section and §1.1.2 Module Bridges "To [Next Module]"
- Remediation is light only (10-20 word redirects, mastery assumed)
- Type A interactions dominate (70-80%) — reflective, not practice-focused
- No new procedures or vocabulary introduced

**Document manifest:**
1. Layer 1 findings
2. Synthesis draft (§1.9)
3. Approved Backbone + Lesson
4. Synthesis Phase Playbook (full read)
5. TVP — M[X] synthesis + transition out sections
6. Working Notes

---

### Agent 6: `m42-voice-eval.md`

**Gate mapping:** Replaces current Voice Agent (Gates 2 and 4).

**Domain:** Voice quality, tone, and Guide Voice Design Reference compliance.

**Receives from Layer 1:** `sp_voice_scan` output (all mechanical findings already caught).

**Focus:** The judgment-based voice checks that the mechanical scanner can't do:
- Observable vs. Assumed: every acknowledgment references observable behavior, not assumed internal states — requires reading the interaction context to judge
- Praise specificity: On Correct lines name what student did (not just "Correct!" after mechanical filter catches the obvious ones)
- Tone consistency per phase: Warmup (medium-high energy, curious), Lesson S1 (curious → pivotal), Lesson S2 (supportive, steady), Lesson S3 (brief, confident), EC (calm, neutral), Synthesis (warm, reflective)
- Guide personality authenticity: sounds like a caring older sibling/competent tutor, not a robot or cheerleader
- Transition quality: links backward before moving forward, uses connective language
- Autonomy support: invitational phrasing ("Try..." / "You can...") not controlling ("You have to..." / "You need to...")
- Metacognitive prompt quality: purpose-driven, not back-to-back, developmentally appropriate, max 4-6 per module
- Identity closure quality: 1-2 per module, formula = [Observable change] + [What it demonstrates] + [Optional: Future connection]
- Emotion layer alignment: emotion type matches moment (routine success gets steady confidence, not joyful surprise)
- The Four Quality Tests applied to key lines: Observation, Journey, Surprise, Specificity

**Document manifest:**
1. Layer 1 `sp_voice_scan` findings (mechanical issues already flagged)
2. Full Starter Pack (all phases)
3. Voice Script Prompt (full read)
4. Guide Voice Design Reference (full read)

---

### Agent 7: `m42-kdd-eval.md`

**Gate mapping:** Replaces current Gate 3/4 E6 checks.

**Domain:** KDD quality, completeness, and format.

**Receives from Layer 1:** `sp_structure_check` output (§1.10 presence confirmed).

**Judgment checks:**

*Completeness:*
- Every deliberate departure from source documents or template conventions documented
- Decisions visible in phases (unusual toy config, non-standard CRA, vocabulary timing, dimension reuse) have corresponding KDDs
- KDDs cover decisions from ALL phases (not just most recent task)
- Playbook departures documented with rationale

*Quality:*
- Each KDD explains a pedagogical design choice a writer needs to understand
- No development process history (AF# resolutions, gate review chronology, author confirmations) — that belongs in Working Notes
- Quality test: would a writer seeing this module for the first time understand WHY from the KDDs alone?

*Format:*
- 1-3 sentences per entry
- Title states the decision, body states the rationale
- No multi-paragraph entries with Decision/Rationale/Sections subfields — inline paragraph style
- If 10+ KDDs, organized by section

*Author Flags (prominent check — run at every gate this agent is invoked):*
- All Author Flags either resolved in SP or explicitly documented as open
- No unresolved flags without documentation
- Flags resolved since last gate: verify the resolution is reflected in the SP content (not just marked "resolved" in Working Notes)
- Cross-reference with `m42-source-fidelity` AF1/AF2 findings (Gate 1 identifies flags; this agent verifies they're resolved at Gate 3+)

**Document manifest:**
1. Layer 1 findings
2. Full Starter Pack (all phases for cross-reference)
3. Working Notes (Author Flags, development context)

---

### Agent 8: `m42-cross-module-eval.md`

**Gate mapping:** Replaces current Gate 4 X-checks + Audit Prompt Pass 7.

**Domain:** Cross-module coherence (only runs when adjacent module SPs are available).

**Judgment checks:**
- Scope boundary handoffs: M[X-1] deferred content appears in M[X] Must Teach, M[X] Must Not Include defers to M[X+1]
- No concept falls through gap between modules
- No concept claimed by both modules
- Vocabulary handoffs: terms introduced in M[X-1] are "carried" not re-introduced, Terms to Avoid don't conflict
- Toy progression: "Changes from M[X-1]" accurately describes actual changes, "First appearance" toys genuinely absent from M[X-1]
- Bridge symmetry: M[X-1] Synthesis closure → M[X] Warmup callback, M[X] Synthesis closure → M[X+1] Warmup callback
- Misconception continuity: consistent global IDs, prevention strategies don't contradict
- Data value continuity: ranges don't regress without explanation, appropriately progressive

**Document manifest:**
1. M[X] Starter Pack (full)
2. M[X-1] Starter Pack (full, if available)
3. M[X+1] TVP section (if available)
4. Important Decisions sheet (constraint continuity)

---

### Agent 9: `m42-guide-prompt-eval.md`

**Gate mapping:** NEW — currently only spot-checked (5 interactions in Gate 2).

**Domain:** Guide vs Prompt independence and structural compliance across ALL interactions.

**Receives from Layer 1:** `sp_interaction_check` output.

**Judgment checks (applied to every student-action interaction):**
- Independence test: cover Guide, read Prompt only — can student complete the task? Cover Prompt, read Guide only — can student complete?
- No teaching content in Prompt field (Prompt is worksheet-style instruction only)
- Type classification correct: Type A (teaching only) has no Prompt, Type B (minimal teaching) has brief context + instruction in both, Type C (substantial teaching) has teaching in dialogue only
- Dialogue includes both teaching content AND complete instruction
- Prompt includes complete instruction with action verb, target/object, all values, options if applicable
- Dialogue uses conversational phrasing with fractions spelled out; Prompt uses formal instruction with fraction notation
- Type A interactions dominate Synthesis (70-80%)
- No teaching content in any Prompt field across entire SP

**Document manifest:**
1. Layer 1 findings
2. Full Starter Pack (all phases)
3. Guide vs Prompt Structure Reference (full read)

---

## LAYER 3: ORCHESTRATION SKILLS

Skills in `.claude/skills/` that wire Layers 1 and 2 together. Invoked from within the drafting session — no separate chat needed.

Each gate skill implements the revision loop described in the Cross-Cutting Design Decisions section. The sequences below describe the initial evaluation pass. After the author reviews findings and directs fixes, the skill re-runs only the affected checkers to verify fixes landed.

### Skill: `m42-gate1`

**Trigger:** After Task 1 (Backbone + Cross-Reference) is complete.

**Initial evaluation:**
1. Run `sp_structure_check.py --gate 1` on backbone draft
2. Run `sp_vocab_scan.py --gate 1` on backbone + Working Notes Table A
3. Run `sp_toy_consistency.py --gate 1` on backbone
4. Run `sp_dimension_track.py --gate 1` on §1.5 (internal consistency only)
5. Launch `m42-source-fidelity` agent with Layer 1 outputs
6. Collect findings into structured report
7. Present to author with severity counts + top priority fixes + verdict

**Revision loop:**
- Author reviews findings, directs fixes or approves
- Cowork applies directed fixes to backbone and/or Working Notes
- Re-run affected checkers (e.g., if §1.3 vocab changed, re-run `sp_vocab_scan.py --gate 1`)
- Present delta report (new findings only)
- Repeat until author approves → Gate 1 passed

---

### Skill: `m42-gate2`

**Trigger:** After Task 2 (Warmup + Lesson) is complete.

**Initial evaluation:**
1. Run `sp_structure_check.py --gate 2`
2. Run `sp_interaction_check.py --gate 2` on §1.6–§1.7
3. Run `sp_vocab_scan.py --gate 2` on full draft through §1.7
4. Run `sp_voice_scan.py --gate 2` on §1.6–§1.7
5. Run `sp_dimension_track.py --gate 2` on §1.6–§1.7
6. Run `sp_timing_estimate.py --gate 2` on §1.6–§1.7
7. Launch in parallel:
   - `m42-warmup-eval` agent (model: sonnet) with Layer 1 outputs
   - `m42-lesson-eval` agent with Layer 1 outputs
   - `m42-guide-prompt-eval` agent with Layer 1 outputs (§1.6–§1.7 scope)
   - `m42-voice-eval` agent with Layer 1 outputs (§1.6–§1.7 scope)
8. Collect all findings into unified report
9. Separate upstream findings (changes needed in §1.0–§1.5) from current-scope findings
10. Present with severity counts + top priority fixes + upstream flags + verdict

**Revision loop:**
- Author reviews findings, decides on upstream vs. downstream fixes
- If upstream fixes applied to backbone: re-run `sp_structure_check.py --gate 1` and `sp_vocab_scan.py --gate 1` on modified sections
- Re-run affected Gate 2 checkers on revised §1.6–§1.7
- Present delta report
- Repeat until author approves → Gate 2 passed

---

### Skill: `m42-gate3`

**Trigger:** After Task 3 (EC + Practice + Synthesis + KDD) is complete.

**Initial evaluation:**
1. Run `sp_structure_check.py --gate 3`
2. Run `sp_interaction_check.py --gate 3` on §1.8–§1.9 (re-validates aggregate counts across all phases)
3. Run `sp_vocab_scan.py --gate 3` on full draft through §1.10
4. Run `sp_voice_scan.py --gate 3` on §1.8–§1.9
5. Run `sp_dimension_track.py --gate 3` on full draft (cross-phase comparison)
6. Run `sp_timing_estimate.py --gate 3` on full draft
7. Launch in parallel:
   - `m42-ec-practice-eval` agent with Layer 1 outputs
   - `m42-synthesis-eval` agent with Layer 1 outputs
   - `m42-kdd-eval` agent with Layer 1 outputs
   - `m42-guide-prompt-eval` agent (§1.8–§1.9 scope)
   - `m42-voice-eval` agent (§1.8–§1.9 scope)
8. Collect findings, separate upstream flags
9. Present report

**Revision loop:**
- Same pattern as Gate 2
- Upstream findings may touch §1.5 (toy constraints discovered during EC design) or §1.3 (vocabulary timing issues in Synthesis)
- Re-run affected prior-gate checkers if upstream changes made

---

### Skill: `m42-gate4`

**Trigger:** After Task 4 (Full SP Assembly). Note: Notion conversion verification runs separately — see below.

**Initial evaluation:**
1. Run ALL Layer 1 gate checkers at `--gate 4` on full assembled SP
2. Launch in parallel:
   - `m42-kdd-eval` agent (final pass, full-document scope)
   - `m42-cross-module-eval` agent (auto-triggered if adjacent module SPs detected in workspace)
   - `m42-voice-eval` agent (full SP scope)
   - `m42-guide-prompt-eval` agent (full SP scope)
3. Produce final compliance scorecard (matching Audit Prompt Pass 1-7 structure)
4. Present with verdict: READY FOR SME REVIEW? YES / YES WITH CAVEATS / NO

**Revision loop:**
- Final quality gate — fixes here should be minor (major issues caught at Gates 1-3)
- If CRITICAL findings surface, investigate whether earlier gates missed them and flag for process improvement

---

### Standalone Skill: `m42-notion-verify`

**Trigger:** After Task 4 Step 2 (Notion conversion), BEFORE Gate 4.

**Sequence:**
1. Run `sp_notion_convert_check.py` on the `[Module]_Notion_Ready.md` file
2. Present findings to author
3. Fix all conversion issues before proceeding to Gate 4

This is a mechanical verification, not a quality evaluation. Conversion either complies or doesn't. Keep it separate from Gate 4's quality focus.

---

## MAPPING: CURRENT GATES → NEW ARCHITECTURE

| Current Check | Current Location | New Location | Type Change |
|--------------|-----------------|-------------|-------------|
| YAML validation | Gate 1/4 | `sp_structure_check.py` | LLM → Programmatic |
| Section presence | Gate 1/4 | `sp_structure_check.py` | LLM → Programmatic |
| Interaction format (spot-check 5) | Gate 2 C3 | `sp_interaction_check.py` (ALL) | Spot-check → Comprehensive + Programmatic |
| Type labels | Gate 2 C4 | `sp_interaction_check.py` | LLM → Programmatic |
| Vocab Terms to Avoid scan | Gate 2 D1 | `sp_vocab_scan.py` | LLM → Programmatic |
| Vocabulary timing | Gate 2 D2 | `sp_vocab_scan.py` | LLM → Programmatic |
| Red flag words | Voice V4 | `sp_voice_scan.py` | LLM → Programmatic |
| Exclamation count | Voice V5 | `sp_voice_scan.py` | LLM → Programmatic |
| Source fidelity (A1-A12) | Gate 1 | `m42-source-fidelity` agent | LLM → Focused LLM |
| CRA completeness (B1-B5) | Gate 2 | `m42-lesson-eval` agent | LLM → Focused LLM |
| Warmup playbook compliance | **NOT CHECKED** | `m42-warmup-eval` agent | **New coverage** |
| EC alignment (F1-F4) | Gate 3 | `m42-ec-practice-eval` agent | LLM → Focused LLM |
| EC cognitive type constraints | **NOT CHECKED** | `m42-ec-practice-eval` agent | **New coverage** |
| Synthesis quality (G1-G4) | Gate 3 | `m42-synthesis-eval` agent | LLM → Focused LLM |
| Synthesis module-level rules | **NOT CHECKED** | `m42-synthesis-eval` agent | **New coverage** |
| KDD quality (E6) | Gate 3/4 | `m42-kdd-eval` agent | LLM → Focused LLM |
| Voice quality (V1-V7) | Voice Agent | `sp_voice_scan.py` + `m42-voice-eval` | Split: mechanical + judgment |
| Guide/Prompt independence | Gate 2 (spot-check) | `m42-guide-prompt-eval` agent (ALL) | Spot-check → Comprehensive |
| Cross-module coherence | Gate 4 X1-X3 | `m42-cross-module-eval` agent | LLM → Focused LLM |
| Dimension tracking | **NOT CHECKED** | `sp_dimension_track.py` | **New coverage** |
| Toy consistency | Gate 4 (partial) | `sp_toy_consistency.py` | LLM → Programmatic |
| Session timing | **NOT CHECKED** | `sp_timing_estimate.py` | **New coverage** |
| Notion conversion | **NOT CHECKED** | `sp_notion_convert_check.py` (standalone) | **New coverage** |
| Author Flag identification | Gate 1 (weak) | `m42-source-fidelity` AF1/AF2 | LLM → Focused LLM |
| Author Flag resolution | Gate 4 E6 (buried) | `m42-kdd-eval` (prominent check) | Elevated priority |
| 7-pass Audit Prompt | **Manual separate chat** | Absorbed into gate skills | **Integrated** |

---

## WHAT CHANGES IN THE COWORK GUIDANCE

The Cowork Guidance document needs targeted updates at each gate section. The task definitions (Tasks 1-4) stay the same. The gate sections change from "launch a separate agent with the Starter Pack Evaluation Prompt — Gate N section" to "invoke the m42-gateN skill."

Specifically:

**Gate 1 section** (currently lines 299-327):
Replace with: "Invoke the `m42-gate1` skill. It runs programmatic structure, vocabulary, and toy checks, then launches the source fidelity evaluation agent. Review findings. Direct fixes or approve. Re-run affected checkers after fixes. Approve when satisfied."

**Gate 2 section** (currently lines 453-489):
Replace with: "Invoke the `m42-gate2` skill. It runs programmatic checks, then launches warmup, lesson, guide/prompt, and voice evaluation agents in parallel. Review findings — note upstream flags separately. Direct fixes (upstream or downstream). Re-run affected checkers. Approve."

**Gate 3 section** (currently lines 602-625):
Replace with: "Invoke the `m42-gate3` skill. It runs programmatic checks, then launches EC/practice, synthesis, KDD, guide/prompt, and voice agents in parallel. Review findings. Direct fixes. Approve."

**Gate 4 section** (currently lines 671-697):
Replace with: "After Notion conversion, invoke `m42-notion-verify` to verify conversion compliance. Fix any conversion issues. Then invoke `m42-gate4` for the final quality evaluation. Review compliance scorecard. Approve for SME review."

**Documents to retire:**

Move to an `archive/` folder in the workspace. They're valuable as the archaeological record of how the checks evolved, and useful if an agent definition ever seems incomplete. But don't maintain them — that's exactly the duplicate-source-of-truth problem the Known Patterns section warns about (Pattern #2).

- `Starter_Pack_Evaluation_Prompt.md` → `archive/` — content absorbed into individual agent definitions
- `MODULE STARTER PACK AUDIT PROMPT.md` → `archive/` — 7-pass structure absorbed into Layer 1 checkers + Layer 2 agents

---

## IMPLEMENTATION SEQUENCE

### Phase 1: Programmatic Checkers (Highest ROI, fastest to build)

Build and test these scripts. They can be used immediately in your current workflow — run them manually in any session before or after drafting. Validate against existing completed SPs (M1-M5) to calibrate detection accuracy.

**Priority order:**
1. `sp_vocab_scan.py` — highest-value single check, most commonly missed
2. `sp_interaction_check.py` — catches the most frequent format violations
3. `sp_voice_scan.py` — mechanical voice checks eliminate the easy-to-catch issues
4. `sp_structure_check.py` — fast to build, good safety net
5. `sp_toy_consistency.py` — frequently missed in current gates
6. `sp_dimension_track.py` — catches subtle cross-interaction issues
7. `sp_timing_estimate.py` — ballpark phase timing
8. `sp_notion_convert_check.py` — standalone, only needed post-conversion

### Phase 2: Agent Definitions (Medium effort, big quality gain)

Create 9 agent files in `.claude/agents/`. Each embeds its specific checks from this spec. Iterative refinement as you test against real modules.

**Priority order:**
1. `m42-source-fidelity.md` — already partially exists as `m42-gate1-eval.md`, expand it
2. `m42-lesson-eval.md` — CRA is the most complex judgment check
3. `m42-warmup-eval.md` — biggest current gap (entirely unchecked today)
4. `m42-voice-eval.md` — voice issues are your most common finding category
5. `m42-guide-prompt-eval.md` — independence testing is critical and currently spot-checked
6. `m42-ec-practice-eval.md` — alignment is high-stakes
7. `m42-synthesis-eval.md` — synthesis quality varies most between runs
8. `m42-kdd-eval.md` — smaller scope, straightforward
9. `m42-cross-module-eval.md` — auto-triggers when adjacent SPs exist

### Phase 3: Orchestration Skills (Wires everything together)

Create 5 skill files in `.claude/skills/`. Each skill invokes the appropriate checkers and agents for its gate, implements the revision loop, and handles upstream flagging.

**Priority order:**
1. `m42-gate1/SKILL.md` — start with Gate 1 since you can test it against any backbone
2. `m42-gate2/SKILL.md` — heaviest gate (4 parallel agents), most complex orchestration
3. `m42-gate3/SKILL.md`
4. `m42-gate4/SKILL.md`
5. `m42-notion-verify/SKILL.md` — standalone, straightforward

---

## FILE STRUCTURE

```
.claude/
├── agents/
│   ├── m42-source-fidelity.md
│   ├── m42-warmup-eval.md          (model: sonnet)
│   ├── m42-lesson-eval.md
│   ├── m42-ec-practice-eval.md
│   ├── m42-synthesis-eval.md
│   ├── m42-voice-eval.md
│   ├── m42-kdd-eval.md
│   ├── m42-cross-module-eval.md     (auto-triggered when adjacent SPs detected)
│   └── m42-guide-prompt-eval.md
├── skills/
│   ├── m42-gate1/SKILL.md
│   ├── m42-gate2/SKILL.md
│   ├── m42-gate3/SKILL.md
│   ├── m42-gate4/SKILL.md
│   └── m42-notion-verify/SKILL.md   (standalone, runs before Gate 4)
├── scripts/
│   ├── sp_parse_interactions.py     (shared utility — dialogue line extraction)
│   ├── sp_structure_check.py        (gate-aware)
│   ├── sp_interaction_check.py      (gate-aware)
│   ├── sp_vocab_scan.py             (gate-aware, imports sp_parse_interactions)
│   ├── sp_voice_scan.py             (gate-aware, imports sp_parse_interactions)
│   ├── sp_dimension_track.py        (gate-aware, auto-appends to Working Notes)
│   ├── sp_toy_consistency.py        (gate-aware)
│   ├── sp_notion_convert_check.py   (standalone, not gate-aware)
│   └── sp_timing_estimate.py        (gate-aware)
├── eval-outputs/                    (Layer 1 → Layer 2 handoff, accumulated)
│   └── G[grade]U[unit]/
│       └── M[XX]/
│           └── [checker]-gate[N].json
└── ...

archive/
├── Starter_Pack_Evaluation_Prompt.md    (retired — absorbed into agents)
└── MODULE STARTER PACK AUDIT PROMPT.md  (retired — absorbed into checkers + agents)
```

---

## DECISIONS RESOLVED (from v0.1 review)

| # | Question | Decision | Rationale |
|---|----------|----------|-----------|
| 1 | Checker granularity | Keep separate | Each checker has a distinct domain and stage scope. Combining obscures what's being checked. |
| 2 | Gate 2 agent count | Keep 4 agents separate | Narrow focus is the whole point. Warmup runs on Sonnet to manage token budget. |
| 3 | Cross-module eval trigger | Auto-trigger | `m42-cross-module-eval` launches automatically at Gate 4 when adjacent SPs detected in workspace. |
| 4 | Timing heuristics | Rough is fine | Ballpark estimates to catch obviously over/under-scoped phases. Not authoritative timing. |
| 5 | Notion conversion | Standalone pre-Gate 4 | `m42-notion-verify` skill runs after conversion, before Gate 4. Mechanical check, not quality eval. |
| 6 | Quick audit | Removed | Unnecessary if gates are properly broken up. Layer 1 checkers run at every gate anyway. |
| 7 | Backward compatibility | Retire to `archive/` | Keep as archaeological record. Don't maintain — avoids duplicate source of truth (Known Pattern #2). |

## ADDITIONAL DECISIONS (resolved v0.3)

| # | Question | Decision | Rationale |
|---|----------|----------|-----------|
| 8 | Checker granularity (vocab + voice) | Keep separate, extract shared parser module | Both checkers need to parse dialogue lines from interaction blocks. Build a shared `sp_parse_interactions.py` utility that extracts Guide/Prompt/On Correct lines with interaction IDs. Both `sp_vocab_scan` and `sp_voice_scan` import it. Checkers stay independent and testable; parsing logic doesn't duplicate. |
| 9 | Agent re-run threshold | Checkers-only by default; agent re-run only on explicit author request | During revision loops, re-run affected checkers to verify mechanical fixes. Agents are NOT re-launched unless the author made changes affecting the agent's judgment domain AND explicitly asks for re-evaluation. Keeps the loop fast. |
| 10 | Eval-output retention | Accumulate in unit/module subfolders | Outputs accumulate across gates, organized as `.claude/eval-outputs/G[grade]U[unit]/M[XX]/[checker]-gate[N].json`. Gate 4 agents benefit from seeing the full evaluation history. Cleanup is manual per-module after SME approval. |
| 11 | Working Notes integration | Auto-append dimension tracking only | `sp_dimension_track.py` auto-appends its dimension tracking table to the Working Notes file after each gate run (replacing the previous version). This is the one checker output the drafter needs persistent access to during subsequent tasks. Timing estimates and other outputs are ephemeral — live in eval-outputs only. |

---

**END OF ARCHITECTURE SPEC**
