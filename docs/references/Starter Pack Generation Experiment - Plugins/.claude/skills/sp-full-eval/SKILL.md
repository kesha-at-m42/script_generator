# SP Full Evaluation — Multi-Module Pipeline with Consolidated Report

You are running a **full evaluation pipeline** across one or more Module Starter Packs. This is the most comprehensive evaluation mode — it runs all Layer 1 checkers and all Layer 2 agents at the highest applicable gate, then produces a consolidated multi-module report suitable for review handoff.

Use this skill for:
- Pre-release audit of a complete unit's SPs
- Batch evaluation when multiple modules need scoring
- Generating a summary document that can be shared with the team

---

## STEP 1: IDENTIFY INPUTS

1. **SP files** — One or more Starter Pack files. Accept:
   - A single file path
   - A glob pattern (e.g., `G3U2M*_Notion_Ready.md`)
   - "All SPs in the workspace" — glob for `G3U2M*.md` files
   - A list of specific files

2. **Gate** — Default to **Gate 4** (full SP). The user can override.

3. **Output file** (optional) — Where to save the consolidated report. Default: `<workspace>/SP_Full_Eval_Report.md`

If multiple SPs are provided, evaluate each independently, then produce both per-module reports and a cross-module summary.

---

## STEP 2: FOR EACH SP, RUN THE GATE-EVAL PIPELINE

For each SP file, execute the full sp-gate-eval pipeline (Steps 2–4 from that skill). Specifically:

### A. Layer 1: Run All 8 Checkers

```bash
SCRIPTS="<workspace>/.claude/scripts"
for checker in sp_structure_check sp_vocab_scan sp_voice_scan sp_interaction_check sp_timing_estimate sp_toy_consistency sp_dimension_track sp_module_map_check; do
    python "$SCRIPTS/${checker}.py" "$SP" --gate $GATE --json
done
```

Collect JSON findings from each.

### B. Layer 2: Run All Gate-Scoped Agents

At Gate 4, this means ALL 10 agents:

| Agent | Focus |
|-------|-------|
| m42-gate1-eval | Backbone compliance (§1.0–§1.5) |
| m42-source-fidelity | Source document fidelity |
| m42-warmup-eval | §1.6 Warmup quality |
| m42-lesson-eval | §1.7 Lesson scripting |
| m42-guide-prompt-eval | Prompt design across all interactions |
| m42-ec-practice-eval | §1.8 Exit Check / Practice |
| m42-synthesis-eval | §1.9 Synthesis |
| m42-kdd-eval | §1.10 Key Design Decisions |
| m42-voice-eval | Whole-SP voice quality |
| m42-cross-module-eval | Cross-module alignment |

Read each agent definition from `<workspace>/.claude/agents/`, follow its protocol, and collect findings.

**Cross-module agent note**: When evaluating multiple SPs, the cross-module agent can reference the actual adjacent module SPs rather than marking them as unavailable. Pass M[X-1] and M[X+1] paths when available.

### C. Consolidate Per-Module

For each SP, produce the Gate Verdict (PASS / PASS WITH CONDITIONS / FAIL) and a findings summary.

---

## STEP 3: CROSS-MODULE ANALYSIS

After all individual evaluations complete, perform cross-module analysis:

### Consistency Checks

1. **Vocabulary continuity** — Terms introduced in M[X] should be carried (not re-introduced) in M[X+1]. Terms avoided in M[X] should remain avoided.
2. **Bridge alignment** — M[X]'s "To [Next Module]" bridge should match M[X+1]'s "From [Prior Module]" bridge.
3. **Toy progression** — "Changes from M[X-1]" in each SP should accurately describe what changed.
4. **Misconception arc** — Misconceptions that span multiple modules should show progressive prevention strategies.
5. **Scope creep** — Content in M[X+1] that duplicates M[X]'s "Must Teach" items without clear progression.

### Pattern Detection

Look for **systemic issues** that appear across multiple modules:
- Same voice anti-pattern in 3+ modules → training issue, not module-specific
- Same structural violation in 3+ modules → template misunderstanding
- Same vocabulary staging error across modules → systematic extraction gap
- Interaction format errors in the same position across modules → copy-paste inheritance

---

## STEP 4: GENERATE CONSOLIDATED REPORT

Write a markdown report to the output file path. Structure:

```markdown
# Starter Pack Full Evaluation Report
**Generated**: [date]
**Unit**: [unit name]
**Gate**: [N]
**Modules evaluated**: [list]

---

## Unit-Level Summary

| Module | Gate | CRIT | MAJ | MIN | NOTE | Verdict |
|--------|------|------|-----|-----|------|---------|
| M01 | 4 | 0 | 3 | 5 | 8 | PASS W/ CONDITIONS |
| M02 | 4 | 1 | 2 | 3 | 6 | FAIL |
| ... | | | | | | |

### Systemic Issues
[Issues appearing across 3+ modules]

### Cross-Module Alignment
[Bridge mismatches, vocabulary handoff gaps, toy progression errors]

---

## Module: M01 — [Module Title]

### Layer 1 Summary
[Checker × severity matrix]

### Layer 2 Summary
[Agent × findings summary]

### Top Findings
[Priority-ordered list of CRITICAL and MAJOR findings]

### Gate Verdict: [PASS / PASS WITH CONDITIONS / FAIL]
[Conditions or blocking issues listed]

---

## Module: M02 — [Module Title]
[Same structure as above]

---

## Appendix A: Complete Findings by Checker
[Every L1 finding, grouped by checker, for reference]

## Appendix B: Complete Findings by Agent
[Every L2 finding, grouped by agent, for reference]

## Appendix C: Cross-Layer Correlations
[Correlated L1+L2 findings with recommended unified fixes]
```

---

## STEP 5: PRESENT TO USER

1. Save the report to `<workspace>/SP_Full_Eval_Report.md`
2. Present the **Unit-Level Summary table** and **Systemic Issues** directly in conversation
3. For each module with CRITICAL findings, highlight the blocking issues
4. Offer to drill into any specific module or finding category

---

## EXECUTION GUIDANCE

### Performance

A full eval of 6 modules at Gate 4 involves:
- 48 checker runs (8 checkers × 6 modules)
- Up to 60 agent evaluations (10 agents × 6 modules)

This is substantial. Manage expectations:
- Layer 1 is fast (~30 seconds total for all modules)
- Layer 2 is the bottleneck. Each agent evaluation takes 1-3 minutes.
- Consider running L1 first, presenting results, then asking if the user wants to proceed with L2.

### Incremental Mode

If the user has already run evaluations on some modules, don't re-evaluate them. Check for existing findings and only evaluate new/changed modules.

### Targeted Follow-Up

After presenting the full report, common follow-up requests:
- "Fix the CRITICALs in M02" → Switch to editing mode (not this skill)
- "Run just voice eval on M05" → Invoke the single agent directly
- "Show me all vocabulary findings" → Filter the report data
- "Compare M03 and M04 bridges" → Invoke cross-module-eval agent specifically

### Authority Documents

The full eval pipeline uses these reference documents (resolved relative to workspace):
- `STARTER PACK STRUCTURAL SKELETON.md` — Canonical heading hierarchy
- `Guide Voice Design Reference - 01.09.26.md` — Voice quality standards
- `Grade 3 Unit 2 Area and Multiplication .xlsx` — Module Map (per-module canonical data)
- `Grade 3 Unit 2_ Toy Flow.docx` — TVP (toy specifications + scaffolding)

If any authority document is missing, note which L1 checkers and L2 agents are affected and proceed with available documents.
