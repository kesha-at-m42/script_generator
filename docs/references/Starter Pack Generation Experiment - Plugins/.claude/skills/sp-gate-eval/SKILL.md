# SP Gate Evaluation — Orchestrated L1 + L2 Pipeline

You are running a **gate-scoped evaluation** of a Module Starter Pack. This combines Layer 1 mechanical checks (Python scripts) with Layer 2 LLM evaluation agents for deep qualitative analysis. The gate determines which sections are evaluated and which agents are invoked.

---

## STEP 1: IDENTIFY INPUTS

Determine from the user's request or conversation context:

1. **SP file path** — The Starter Pack markdown file to evaluate.
2. **Gate number** (1–4):
   - **Gate 1**: §1.0–§1.5 (Backbone + Cross-Reference)
   - **Gate 2**: §1.0–§1.7 (adds Warmup + Lesson scripts)
   - **Gate 3**: §1.0–§1.10 (adds EC + Synthesis + KDD)
   - **Gate 4**: Full SP (same sections as Gate 3, plus cross-module and comprehensive voice eval)
3. **Previous module SP** (optional) — For cross-module checks at Gate 4.

If gate is unspecified, infer from content (see sp-quick-check heuristic) or ask the user.

---

## STEP 2: RUN LAYER 1 CHECKERS

Run **all 8 gate-scoped checkers** with `--json` output. Resolve the scripts path:

```
SCRIPTS="<workspace>/.claude/scripts"
```

Run each checker. If any checker fails with a Python error, log it and continue.

```bash
python "$SCRIPTS/sp_structure_check.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_vocab_scan.py"        "$SP" --gate $GATE --json
python "$SCRIPTS/sp_voice_scan.py"        "$SP" --gate $GATE --json
python "$SCRIPTS/sp_interaction_check.py" "$SP" --gate $GATE --json
python "$SCRIPTS/sp_timing_estimate.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_toy_consistency.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_dimension_track.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_module_map_check.py"  "$SP" --gate $GATE --json
```

Parse the JSON output from each. Build a consolidated findings list.

Present a **Layer 1 Summary Table** (same format as sp-quick-check: checker × severity matrix). This gives the user early visibility before the slower L2 agents run.

---

## STEP 3: INVOKE LAYER 2 AGENTS

Based on the gate, invoke the appropriate evaluation agents. Each agent is a `.md` file in `<workspace>/.claude/agents/` that should be read and executed as an evaluation task.

### Gate → Agent Mapping

| Gate | Agents to Invoke | Sections Covered |
|------|-----------------|------------------|
| **1** | `m42-gate1-eval.md`, `m42-source-fidelity.md`, `m42-pedagogy-eval.md` | §1.0–§1.5 source fidelity + backbone compliance + Section Plan pedagogy |
| **2** | Gate 1 agents + `m42-warmup-eval.md`, `m42-lesson-eval.md`, `m42-guide-prompt-eval.md` | + §1.6 warmup quality, §1.7 lesson scripting, prompt design (6 agents — mandatory quality gate) |
| **3** | Gate 2 agents (excl. pedagogy) + `m42-ec-practice-eval.md`, `m42-synthesis-eval.md`, `m42-kdd-eval.md` | + §1.8 exit check, §1.9 synthesis, §1.10 design decisions |
| **4** | Gate 3 agents + `m42-voice-eval.md`, `m42-cross-module-eval.md`, `m42-pedagogy-eval.md`, `m42-requirements-eval.md` | + whole-SP voice quality, cross-module alignment, full pedagogy arc, requirements compliance |

### Agent Invocation Protocol

For each agent in the gate's list:

1. **Read the agent definition** from `.claude/agents/<agent-name>.md`
2. **Follow its setup instructions** — locate required files, read reference documents as specified
3. **Execute its check categories** — work through each check systematically
4. **Produce findings in the agent's specified output format** (typically severity-rated findings tables)

**Important execution notes:**
- Agents are **read-only** — they must not modify any files
- Each agent specifies its own **Required Files** and **Recommended Files** — locate and read these independently
- Agents use severity levels: CRITICAL, MAJOR, MINOR, NOTE (same scale as L1)
- If a Required File for an agent is missing, note the absence but continue with remaining agents
- The `m42-cross-module-eval.md` agent requires access to M[X-1] and optionally M[X+1] — skip if not available

### Feeding L1 Findings to L2 Agents

When invoking L2 agents, **share the L1 findings** with them as context. Specifically:
- Structure checker findings inform source-fidelity and gate1-eval agents (missing sections, ordering issues)
- Vocab checker findings inform lesson-eval and warmup-eval agents (staging violations in scripted content)
- Voice checker findings inform voice-eval agent (mechanical anti-patterns as starting point for deeper analysis)
- Module map checker findings inform gate1-eval and source-fidelity agents (content drift from authority docs)
- Interaction checker findings inform guide-prompt-eval agent (malformed interaction blocks)

This prevents L2 agents from re-discovering mechanical issues and lets them focus on qualitative judgment.

---

## STEP 4: CONSOLIDATE AND PRESENT

Produce a **Gate [N] Evaluation Report** with these sections:

### 1. Executive Summary

One paragraph: what gate, what SP, how many total findings at each severity, overall verdict.

### 2. Layer 1 Findings (Mechanical)

The checker × severity matrix from Step 2, followed by all CRITICAL and MAJOR findings listed with ID, location, and message.

### 3. Layer 2 Findings (Qualitative)

For each agent that ran, present:
- Agent name and scope
- Findings table (ID | Severity | Location | Finding | Recommended Fix)
- Agent-specific outputs (e.g., voice-eval produces a Metacognitive Prompt Inventory; gate1-eval produces an Unlogged Conflicts list)

### 4. Cross-Layer Correlations

Identify cases where L1 and L2 findings point to the **same underlying issue**. For example:
- L1 vocab checker flags a missing term + L2 source-fidelity confirms it's dropped from Module Map
- L1 voice checker flags exclamation density + L2 voice-eval identifies Warmth Spectrum miscalibration
- L1 module map checker flags missing misconception + L2 gate1-eval traces the gap to a missing Author Flag

Group these as **correlated findings** and recommend a single fix that addresses both layers.

### 5. Priority Fix List

Ordered list of the top 10 findings by impact. Rank CRITICAL > MAJOR, and within severity, prefer cross-layer correlated findings (they indicate systemic issues). For each:
- Finding ID(s)
- Severity
- Location
- What's wrong
- Recommended fix
- Which layer(s) flagged it

### 6. Gate Verdict

State one of:
- **PASS** — No CRITICAL findings from either layer. SP is ready for the next gate.
- **PASS WITH CONDITIONS** — No CRITICALs, but MAJOR findings should be addressed. List the conditions.
- **FAIL** — CRITICAL findings present. SP requires revision before proceeding. List the blocking issues.

---

## EXECUTION TIPS

- **Gate 1 evaluations** are the fastest (~3 agents). Good for early backbone review.
- **Gate 2 evaluations** are the mandatory quality gate (6 agents including pedagogy-eval). Most common evaluation point — catches ~75% of student-facing content issues.
- **Gate 3 evaluations** are near-complete. The incremental agents (EC, synthesis, KDD) cover smaller sections.
- **Gate 4** is a full audit. The voice-eval agent alone can take significant time. Reserve for pre-release review.
- If the user wants speed over depth, suggest running `sp-quick-check` first, then following up with a targeted gate-eval only if L1 finds issues.
- If the user asks for a specific agent only (e.g., "just run voice eval"), you can skip the full orchestration and invoke that single agent directly from `.claude/agents/`.
