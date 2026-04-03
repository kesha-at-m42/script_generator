# SP Quick Check — Layer 1 Mechanical Scan

You are running a **quick mechanical scan** of a Module Starter Pack using the Layer 1 Python checkers. This is a fast, deterministic pass — no LLM evaluation agents, no subjective judgment. You run the checkers, collect JSON findings, and present a consolidated summary.

---

## STEP 1: IDENTIFY INPUTS

Determine two things from the user's request or conversation context:

1. **SP file path** — The Starter Pack markdown file to evaluate. Look for:
   - A file the user just mentioned or is working on
   - A `G3U2M*` file in the workspace
   - If ambiguous, ask the user which SP to scan

2. **Gate number** (1–4) — Controls which sections are in scope:
   - **Gate 1**: §1.0–§1.5 (Backbone only)
   - **Gate 2**: §1.0–§1.7 (adds Warmup + Lesson)
   - **Gate 3**: §1.0–§1.10 (adds EC + Synthesis + KDD)
   - **Gate 4**: Same as Gate 3 (full SP)
   - If unspecified, default to the highest gate the SP content supports. A quick heuristic: if the file contains `§1.8` or `## 1.8`, use gate 3+. If it contains `§1.6`/`## 1.6` but not `§1.8`, use gate 2. Otherwise gate 1.

---

## STEP 2: RUN ALL CHECKERS

Run all 8 gate-scoped checkers in sequence. Use `--json` for machine-readable output. Capture both stdout and stderr.

```bash
SCRIPTS="/path/to/.claude/scripts"
SP="/path/to/starter_pack.md"
GATE=3

python "$SCRIPTS/sp_structure_check.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_vocab_scan.py"        "$SP" --gate $GATE --json
python "$SCRIPTS/sp_voice_scan.py"        "$SP" --gate $GATE --json
python "$SCRIPTS/sp_interaction_check.py" "$SP" --gate $GATE --json
python "$SCRIPTS/sp_timing_estimate.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_toy_consistency.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_dimension_track.py"   "$SP" --gate $GATE --json
python "$SCRIPTS/sp_module_map_check.py"  "$SP" --gate $GATE --json
```

**Path resolution**: The scripts directory is at:
```
<workspace>/.claude/scripts/
```
where `<workspace>` is the Starter Pack Generation Experiment - Plugins folder.

**Important**: Run each checker independently. If one fails with a Python error, log the error and continue with the remaining checkers. Do NOT stop the scan.

### Optional: Notion Convert Check

If the SP is a Notion-ready file (contains `<!-- HUB PROPERTIES -->` or filename includes `Notion_Ready`), also run:
```bash
python "$SCRIPTS/sp_notion_convert_check.py" "$SP" --json
```
Note: This checker does NOT accept `--gate`. It always checks the full file.

---

## STEP 3: PARSE AND CONSOLIDATE

Each checker outputs JSON with this structure:
```json
{
  "checker": "sp_structure_check",
  "gate": 3,
  "file": "G3U2M1_Notion_Ready.md",
  "findings": [
    {
      "id": "ST1",
      "severity": "CRITICAL|MAJOR|MINOR|NOTE",
      "message": "...",
      "location": "line 42"
    }
  ],
  "summary": {
    "critical": 0,
    "major": 2,
    "minor": 1,
    "note": 3,
    "total": 6
  }
}
```

Collect all findings across checkers. Group by severity.

---

## STEP 4: PRESENT RESULTS

Present a **consolidated quick-check report** in this format:

### Quick Check: [filename] @ Gate [N]

**Checker Status**

| Checker | CRIT | MAJ | MIN | NOTE | Status |
|---------|------|-----|-----|------|--------|
| Structure | 0 | 2 | 1 | 3 | ⚠ |
| Vocabulary | 0 | 0 | 0 | 1 | ✓ |
| Voice | 0 | 1 | 2 | 0 | ⚠ |
| ... | | | | | |
| **TOTAL** | **0** | **3** | **3** | **4** | |

Status key: ✓ = clean (0 CRIT + 0 MAJ), ⚠ = has findings, ✗ = has CRITICALs, ERR = checker failed

**Verdict:**
- **CLEAN** — 0 CRITICAL, 0 MAJOR findings
- **REVIEW** — 0 CRITICAL, but MAJOR findings need attention
- **BLOCK** — CRITICAL findings must be resolved

Then list **all CRITICAL and MAJOR findings** with their checker ID, location, and message. Group MINORs and NOTEs as a count-only summary unless the user asks for detail.

---

## NOTES

- This skill is **read-only**. Do not edit the SP file.
- If the user wants deeper evaluation (subjective quality, pedagogy, voice tone), recommend running `sp-gate-eval` or `sp-full-eval` instead.
- Total runtime should be under 30 seconds for a typical SP.
- If `openpyxl` or `python-docx` aren't installed, `sp_module_map_check.py` will fail — note this in the report and suggest `pip install openpyxl python-docx --break-system-packages`.
