# Release A: Plugin Patches

**Version:** 0.3.0-a
**Date:** 2026-04-16
**Contents:** Pedagogy-audit agent + PE-1 EC Closure check + FP suppressions + orchestration updates

---

## 1. NEW FILE: agents/m42-pedagogy-audit.md

Copy from workspace: `m42-pedagogy-audit.md` (already written, v0.2 with "documented≠resolved" and mandatory PA1.3 changes applied).

**Destination:** `plugin_0127pTNMJD8NG2q7AhCwCXQr/agents/m42-pedagogy-audit.md`

---

## 2. PATCH: scripts/sp_interaction_check.py — PE-1 EC Closure Presence Check

### 2a. Add new check I22 to docstring (after line 37)

```python
  Structural:
    I22: EC Closure interaction present after last EC item (Gate 3+)
```

### 2b. Add the check function (after `check_purpose_length` function, before Aggregate checks section ~line 318)

```python
def check_ec_closure(interactions: list, gate: int) -> list:
    """I22: Verify EC Closure interaction present after last EC item.

    The EC phase must end with a teaching-only interaction that transitions
    the student to Practice. This is a standardized structural element;
    omitting it breaks the EC→Practice handoff.

    Gate 3+ only (EC must exist).
    """
    if gate < 3:
        return []

    findings = []
    ec_interactions = [ix for ix in interactions if ix.phase == "EC"]

    if not ec_interactions:
        return []  # No EC — phase coverage check (I18) handles this

    # Find the last EC interaction
    last_ec = ec_interactions[-1]

    # The last EC interaction should be teaching-only (the closure/transition)
    # Check: is the last EC interaction a teaching-only pattern?
    if last_ec.pattern != "teaching_only":
        # Additional check: does any EC interaction after the last student-action
        # look like a closure? (might be labeled differently)
        last_student_action_idx = None
        for i, ix in enumerate(ec_interactions):
            if ix.pattern == "student_action":
                last_student_action_idx = i

        if last_student_action_idx is not None:
            # Check if there's ANY interaction after the last student action
            remaining = ec_interactions[last_student_action_idx + 1:]
            has_closure = any(
                ix.pattern == "teaching_only" for ix in remaining
            )
            if not has_closure:
                findings.append({
                    "check": "I22",
                    "severity": "MAJOR",
                    "phase": "EC",
                    "interaction_id": last_ec.id,
                    "detail": "No EC Closure interaction after last EC assessment item. "
                              "EC should end with a teaching-only transition to Practice "
                              "(e.g., Guide: \"You're ready. Let's practice.\")",
                    "line_number": last_ec.line_number,
                })
    else:
        # Last interaction IS teaching-only — check it has Guide text
        # (not just an empty placeholder)
        if not last_ec.has_guide:
            findings.append({
                "check": "I22",
                "severity": "MINOR",
                "phase": "EC",
                "interaction_id": last_ec.id,
                "detail": "EC Closure interaction exists but has no Guide text — "
                          "should contain a transition message to Practice",
                "line_number": last_ec.line_number,
            })

    return findings
```

### 2c. Wire up in `run_interaction_check` (after purpose_findings, ~line 486, before aggregate checks)

```python
    # EC Closure check (Gate 3+)
    ec_closure_findings = check_ec_closure(sp_filtered.interactions, gate)
    all_findings.extend(ec_closure_findings)
    if ec_closure_findings:
        checks_run.update(f["check"] for f in ec_closure_findings)
```

---

## 3. PATCH: scripts/sp_structure_check.py — FP Suppressions

### 3a. ST10 (H4 false positives in KDD section)

The current `check_no_h4` function flags ALL H4 headings. KDD entries legitimately use H4 for individual decision headings. Suppress H4 findings within §1.10.

**Replace the `check_no_h4` function (lines 366-379):**

```python
def check_no_h4(sp) -> list:
    """ST10: No H4s anywhere EXCEPT in §1.10 (KDDs use H4 for individual entries)."""
    findings = []

    # Find §1.10 boundaries to exclude
    kdd_start = None
    kdd_end = None
    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        if re.match(r'^##\s+.*1\.10\b', stripped) or \
           re.match(r'^##\s+.*Key\s+Design\s+Decisions\b', stripped, re.IGNORECASE):
            kdd_start = i
        elif kdd_start is not None and re.match(r'^##\s+', stripped):
            kdd_end = i
            break

    if kdd_start and not kdd_end:
        kdd_end = len(sp.lines)

    for i, line in enumerate(sp.lines):
        stripped = line.strip()
        if re.match(r'^#{4}\s+[^#]', stripped):
            # Suppress if inside §1.10 KDD section
            if kdd_start is not None and kdd_start <= i < kdd_end:
                continue
            findings.append({
                "check": "ST10",
                "severity": "MINOR",
                "detail": f"H4 heading found (use bold inline label instead): '{stripped[:70]}'",
                "line_number": i + 1,
            })
    return findings
```

### 3b. ST11 (Forbidden phrase ordering FP for KP#58-compliant phrasing)

The current ordering check fires on Required/Forbidden Phrases sections. Some SPs combine these into a single block or use variant headings that match the regex but aren't out of order. The fix is to only flag when the ordering is *clearly* wrong (not just when landmarks are missing).

**No code change needed** — the current logic already only flags when a later landmark appears *before* an earlier one. The FP was from a heading regex matching too broadly. Add a note to the `_LESSON_ORDERING_LANDMARKS` patterns to require stricter matching:

**In `_LESSON_ORDERING_LANDMARKS` (line 383), tighten the Section 1 pattern to not match "Section Plan" or similar:**

```python
    ("Section 1",              re.compile(r'^###\s+\**Section\s+1\s*(?:[:(—]|\b)', re.IGNORECASE)),
```

This prevents matching `### Section 1 Plan` or similar non-interaction headings. The `\s*(?:[:(—]|\b)` requires either punctuation after "Section 1" or a word boundary.

---

## 4. PATCH: scripts/sp_vocab_scan.py — FP Suppressions

### 4a. VO4 (Vocab-before-introduction on worked examples)

Worked examples legitimately use formal vocabulary in Guide's think-aloud because the Guide is *modeling* usage, not teaching the term to the student. The term's "introduction point" is the Abstract phase interaction where it's formally named — Guide modeling in a worked example before that point is expected pedagogy, not a violation.

**In `check_vocab_timing` function (~line 357), add a filter to skip timing violations in worked-example interactions:**

After the line `if earliest_rank <= rank: continue` (~line 381), add:

```python
            # Suppress timing violations in worked examples — Guide is modeling
            # the term in a think-aloud, not teaching it to the student.
            # The interaction type label [WORKED EXAMPLE] signals this.
            ix_for_dl = next(
                (ix for ix in interactions if ix.id == dl.interaction_id), None
            )
            if ix_for_dl and ix_for_dl.type_label and \
               'WORKED EXAMPLE' in ix_for_dl.type_label.upper():
                continue
```

This requires passing `interactions` to `check_vocab_timing`. Update the function signature:

```python
def check_vocab_timing(sp: ParsedSP, timing_map: dict, interactions: list) -> list:
```

And the call site (already has correct signature — verify `interactions` is passed from `run_vocab_scan`).

---

## 5. PATCH: skills/sp-gate-eval/SKILL.md — Orchestration Updates

### 5a. Gate → Agent Mapping (lines 61-66)

**Replace:**
```
| **2** | Gate 1 agents + `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval` |
```

**With:**
```
| **2** | Gate 1 agents + `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval`, `m42-pedagogy-audit` |
```

**Note:** `m42-pedagogy-audit` persists through Gates 3 and 4 automatically since "Gate 2 agents" is the base for Gate 3, and "Gate 3 agents" is the base for Gate 4.

### 5b. Parallel Agent Counts (lines 81-85)

**Replace:**
```
- Gate 1: Launch all 3 agents in parallel
- Gate 2: Launch all 6 agents in parallel
- Gate 3: Launch all 8 agents in parallel
- Gate 4: Launch all 12 agents in parallel
```

**With:**
```
- Gate 1: Launch all 3 agents in parallel
- Gate 2: Launch all 7 agents in parallel
- Gate 3: Launch all 9 agents in parallel
- Gate 4: Launch all 13 agents in parallel
```

### 5c. L1 Feeding Rules (after line 95)

**Add:**
```
- `m42-pedagogy-audit`: Structure checker + Dimension tracker + Interaction checker + Toy consistency findings (cross-checks constraints, values, toys, and interaction types)
```

---

## 6. NOT IN RELEASE A (deferred)

- **TC parenthetical parse issue** — This is in `sp_parse_interactions.py`, not a checker. Needs investigation into how Visual: lines with parentheticals are tokenized. Deferred to Release B.
- **PE-6 forward-looking vocab flag** — Medium effort, needs staging table → interaction cross-reference logic. Deferred.
- **Agent rebuilds** (lesson-eval, warmup-eval, synthesis-eval, kdd-eval) — Release B after M8-M9 calibration data.
- **PE-2, PE-4, PE-7** — Release B.

---

## Testing Plan

After applying patches:
1. Run `sp_interaction_check.py` on M6 SP at Gate 3 — verify I22 does NOT fire (closure was added in G3-02 fix)
2. Run `sp_structure_check.py` on M4 SP at Gate 2 — verify ST10 no longer fires on KDD H4s
3. Run `sp_vocab_scan.py` on M3 SP at Gate 2 — verify V3 doesn't fire on worked example Guide text
4. **Live test on M8 and M9** — run full gate eval pipeline with pedagogy-audit agent integrated
