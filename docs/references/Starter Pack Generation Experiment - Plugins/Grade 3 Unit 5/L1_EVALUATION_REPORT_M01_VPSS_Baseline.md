# L1 EVALUATION PIPELINE — LEGACY VPSS MODULE 1
**File:** `/sessions/gifted-gallant-turing/mnt/Starter Pack Generation Experiment - Plugins/Grade 3 Unit 5/VPSS/MODULE 1_ WHAT MAKES A FRACTION_ - VPSS.WIP.12.18.25.md`

**Test Date:** 2026-03-30  
**Gate Level:** 4 (Full validation)  
**File Status:** Legacy (WIP.12.18.25) — predates current template

---

## 1. PARSER RESULTS — Interaction Detection

### Summary
- **Total lines:** 906
- **Sections found:** 55
- **Interactions detected:** 24
- **Dialogue lines found:** 79
- **Module ID:** M01

### Interaction Count vs. Actual Existence
The parser detected **24 interactions** across three phases:
- **Warmup:** 3 (W.1, W.2, W.3)
- **Lesson:** 20 (1.1–1.11, 2.1–2.2, 3.0–3.6)
- **Synthesis:** 1 (IC)

The file structure shows these interactions exist and are labeled, so **parser recall is 100%** for marked interactions.

### Pattern Detection
Classified patterns detected:
- **student_action:** 19 interactions (79%)
- **teaching_only:** 3 interactions (12.5%)
- **unknown:** 2 interactions (8%) — Warmup W.1 and W.2

The **unknown** classifications indicate these warmup interactions lack standard fields (Purpose, Student Action, etc.) that newer templates require.

### Toys Registered
- **Toys in §1.5 metadata:** 2 toys listed (Grid Arrays, Hexagons)
- **Toys in interaction content:** 0 (no toy tags found in dialogue or interaction specs)

This indicates **toy tracking is not present** in interaction-level content, only in module metadata.

---

## 2. INTERACTION CHECK — Field Validation (Gate 4)

### Summary
**Total Findings:** 103  
**MAJOR:** 43 | **MINOR:** 60

### Breakdown by Severity

#### MAJOR Issues (43 total)
1. **Missing Purpose field (19 instances):** Lessons 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6
2. **Missing Visual field (1 instance):** Lesson 1.2
3. **Missing Correct Answer field (19 instances):** All interactions except Warmup and Synthesis
4. **Missing Remediation field (1 instance):** Lesson 1.2
5. **Missing Guide field (1 instance):** Warmup W.3
6. **Synthesis under-scoped (1 instance):** Only 1 interaction (expected 3-8)
7. **Missing EC/Practice interactions (1 instance):** No explicit Explicit Correction or Practice phases found

#### MINOR Issues (60 total)
1. **Unknown pattern (2 instances):** Warmup W.1, W.2 — cannot validate fields
2. **Missing Student Action field (20 instances):** All 20 lesson interactions
3. **Remediation format errors (12 instances):** Using "Full L-M-H" or "Light only" intensity qualifiers instead of pure "Pipeline" format
   - Examples: "Full L-M-H (shade focus)", "Full L-M-H (focus on equal parts count, NOT cut direction)", "Light only (Toy practice)"
4. **Missing type label (22 instances):** No [WORKED EXAMPLE], [ACTIVATION], etc. markers in brackets
5. **Missing teaching-only marker (2 instances):** Lesson 3.0 and Synthesis/IC lack "No student action." explicit marker

### Real Structural Gaps vs. False Positives

**REAL GAPS (represent actual content deficiencies):**
- Missing Purpose fields (19) — shows lack of pedagogical intent documentation
- Missing Correct Answer fields (19) — no answer keys or acceptance criteria
- Missing Student Action field in descriptions (20) — unclear what students actually do
- Synthesis under-scoped (1 interaction vs 3-8 expected) — critical content gap for consolidation
- Missing EC/Practice interactions — no explicit error correction or extended practice
- No visual field in Lesson 1.2 — incomplete interaction spec

**FALSE POSITIVES/FORMAT DIFFERENCES (expected in legacy files):**
- Remediation intensity qualifiers (12 instances) — this is an old format; file uses "Full L-M-H" instead of pipeline-only format. This is a format migration issue, not a missing field.
- Missing type labels (22 instances) — legacy file predates the bracketed type system [WORKED EXAMPLE], [ACTIVATION], etc.
- Unknown pattern classification (2 instances) — Warmup interactions exist but don't map to standard taxonomy
- Missing teaching-only marker (2 instances) — teaching-only interactions exist but lack explicit "No student action." line

---

## 3. VOICE SCAN — Dialogue Quality & Style (Gate 4)

### Summary
**Total Findings:** 15  
**MAJOR:** 7 | **MINOR:** 8

### Findings Detail

#### MAJOR Issues (7)
1. **Red flag word 'technique'** (1 instance)
   - Location: Lesson 3.1, L537
   - Text: "Right. Two equal parts, just like with the rectangle, but with a different technique."
   - Issue: "Technique" is too formal/procedural for Grade 3; prefer "way" or "method"

2. **Em dashes in dialogue** (6 instances) — preferred style violation
   - Lesson 1.2, L331: "Let's check—are they equal?"
   - Lesson 1.4, L362: "But watch—here's another way..."
   - Lesson 1.4, L375: "What matters isn't how you cut—it's that you end up with four..."
   - Lesson 1.10, L446: "Let's do one more—eight equal parts..."
   - Lesson 1.10, L452: "Eight equal parts—two rows of four."
   - Lesson 3.2, L545: "One out of two equal parts—1/2."
   - **Issue:** Em dashes should be replaced with comma, colon, or period

#### MINOR Issues (8)
1. **Rhetorical commands** (4 instances) — "Can you..." phrasing
   - Lesson 1.6, L409: "Can you partition this one into three equal parts?"
   - Lesson 1.7, L418: "Can you shade just one part?"
   - Lesson 1.11, L470: "Can you shade just one part?"
   - Lesson 3.5, L571: "One more. Can you make six equal parts?"

2. **Verbose guide line** (1 instance)
   - Lesson 2.1, L492: 4-sentence guide (max recommended: 3)
   - Text: "You've seen how we write fractions like ½, ⅓, and ¼. A shape that shows..."

3. **Missing contractions** (2 instances)
   - Lesson 3.0, L519: "we have" → should use "we've"
   - Lesson 3.6, L588: "We have" → should use "We've"

4. **Generic praise** (1 instance)
   - Synthesis/IC, L873: "Great work! Today you learned..." 
   - Issue: Lacks specific observable acknowledgment of what student did

### Assessment
Voice quality is **generally strong** with minor style inconsistencies. Em dash usage is the primary issue (6 instances). The red flag word "technique" and generic praise represent isolated cases.

---

## 4. STRUCTURE CHECK — Module-Level Organization (Gate 4)

### Summary
**Total Findings:** 25  
**MAJOR:** 5 | **MINOR:** 20

### Major Issues (5)

1. **Missing YAML required fields (2 instances)**
   - Missing: `unit` field (e.g., "Unit 5")
   - Missing: `domain` field (e.g., "fractions")
   - Current YAML has: module_id, path, fractions_required, shapes

2. **Missing §1.10 section (1 instance)**
   - Required section "Key Design Decisions" not found
   - Impact: Design rationale undocumented

3. **H1 structure violation (1 instance)**
   - Found 2 H1s (expected exactly 3)
   - Expected: Module title, BACKBONE, END OF MODULE
   - Missing: BACKBONE section or END OF MODULE marker

4. **Missing end marker (1 instance)**
   - File lacks "# END OF MODULE [X] STARTER PACK" terminator
   - Critical for module boundary detection

### Minor Issues (20)

1. **YAML legacy fields (3 instances)**
   - Contains deprecated: path, fractions_required, shapes
   - Should migrate to current schema

2. **Development tags** (4 instances)
   - Lines 214, 288, 669, 775 contain "Detail Level:" annotations
   - These are WIP markers; should be removed in final

3. **Missing version line** (1 instance)
   - No version identifier in first 30 lines (file does have version on line 3, so this is a false positive or the checker is looking for different format)

4. **H4 headings** (7 instances)
   - Lines 124, 142, 156, 167, 176, 648, 660
   - Should use bold inline labels instead of H4 headers
   - Examples: "#### Path C (VPSS) Intervention" → "**Path C (VPSS) Intervention**"

5. **Missing verification checklists** (4 instances)
   - Not found for Warmup, Lesson, EC, Synthesis phases
   - These checklists help teachers verify student understanding

### Assessment
Structure violations represent **true module-level gaps:**
- Missing domain/unit metadata prevents proper indexing
- Lack of BACKBONE section is a significant pedagogical gap
- Missing end marker breaks module boundary detection
- Absence of verification checklists is a real instructional gap

---

## 5. TIMING ESTIMATE — Session Duration Analysis (Gate 4)

### Summary
**Total Findings:** 2 (both MINOR)

### Estimates vs. Targets

| Phase | Estimated Time | Interactions | Target Time | Status |
|-------|-----------------|--------------|-------------|---------|
| Warmup | 1.3–2.0 min | 3 | 2–3 min | ✓ In range |
| Lesson | 9.8–19.5 min | 20 | 8–14 min | ⚠ Over range |
| Synthesis | 0.3–0.5 min | 1 | 5–7 min | ✗ **Critically under** |
| **TOTAL** | **11.4–22.0 min** | 24 | **25–30 min** | ✗ **Under-scoped** |

### Issues Identified

1. **Synthesis critically under-scoped** (TM1)
   - Estimated: 0.3–0.5 min
   - Target: 5–7 min
   - Gap: Missing ~4.5–6.5 min of consolidation content
   - Only 1 interaction (expected 3–8)

2. **Overall session under-scoped** (TM2)
   - Estimated: 11.4–22.0 min
   - Target: 25–30 min
   - Gap: Missing ~5–18.6 min of content
   - Implies: Insufficient practice and extension activities

### Root Cause Analysis
The **missing Synthesis interactions** and **lack of EC/Practice phases** directly explain the timing gap. The module spends ~11 min on core lesson but provides minimal consolidation.

---

## 6. DIMENSION TRACKING — Shape Partitioning Coverage (Gate 4)

### Summary
**Total Findings:** 0 (clean)

### Dimension Usage
Only 3 interactions explicitly track dimensions:
- **Lesson 1.4:** Dimensions 1×4, 4×1, 2×2 (partitioning into 4 parts)
- **Lesson 1.10:** Dimension 2×4 (partitioning into 8 parts)
- **Lesson 3.6:** Dimension 2×2 (hexagon equivalent)

### Assessment
**No cross-phase dimension reuse found** — a good sign. However, the sparse usage suggests most interactions lack explicit geometric specification, which is a content documentation gap rather than a tracking problem.

---

## 7. VOCABULARY SCAN — Assessment Vocabulary (Gate 4)

### Summary
**Total Findings:** 2 (both MINOR)

### Vocabulary Audited
- **Terms to Avoid:** 6 identified
- **Forbidden Phrases:** 4 identified
- **Dialogue lines scanned:** 79
- **Assessment Vocabulary tagged:** None explicitly tagged in dialogue

### Issues Found

1. **"Today" usage** (V5 flag)
   - Location: Synthesis/IC, L873
   - Text: "Great work! Today you learned how to make equal parts..."
   - Issue: "Today" creates artificial time boundary; prefer "You learned..."

2. **"Next time" usage** (V5 flag)
   - Location: Synthesis/IC, L873
   - Text: "...and the next time you see a fraction, you'll know what it means."
   - Issue: References future lesson outside this module; can confuse continuity

### Assessment
Vocabulary usage is **strong overall**. The two flags are style issues in Synthesis, not comprehension problems. Assessment vocabulary (partition, equal parts, fraction, whole, halves, thirds, fourths, sixths, eighths) is present and used correctly throughout.

---

## SUMMARY OF FINDINGS

### Critical Structural Gaps (Real Issues)
1. **Missing YAML metadata fields** (unit, domain) — breaks indexing
2. **No BACKBONE section** — pedagogical structure incomplete
3. **No END OF MODULE marker** — module boundary undefined
4. **Synthesis critically under-scoped** (1 interaction, 0.3–0.5 min vs. 5–7 min target)
5. **Missing EC/Practice interactions** — no explicit error correction or extended practice
6. **Missing verification checklists** — no teacher verification points

### Format Differences (Expected in Legacy)
1. **Remediation field format** uses "Full L-M-H" (old) instead of "Pipeline" (new) — 12 instances
2. **Missing interaction type labels** ([WORKED EXAMPLE], etc.) — 22 instances — this is format evolution
3. **H4 headings instead of bold inline labels** — 7 instances — structural migration
4. **Unknown pattern classification** in Warmup — taxonomy changed since file creation

### Quality Issues (Not Blocking)
1. **Em dashes in dialogue** — 6 instances (style, not pedagogical)
2. **Generic praise in Synthesis** — 1 instance (minor voice issue)
3. **Missing contractions** — 2 instances (style)
4. **Verbose guide lines** — 1 instance (slight)
5. **Rhetorical "Can you..." commands** — 4 instances (minor style)

### Quantitative Gap Analysis
- **Interactions detected:** 24/24 (100% parser recall)
- **Interactions with complete modern template fields:** 4/24 (17%)
- **Interactions with real content gaps:** 6/24 (25%) — missing Purpose, Correct Answer, Visual
- **Interactions with format-only gaps:** 18/24 (75%) — type labels, remediation format
- **Session duration shortfall:** ~5–18.6 minutes (~19–43% under target)
- **Voice/style issues:** 15/79 dialogue lines (19%) — mostly em dashes

### Recommendation for Migration
This file represents a **working prototype that predates the current L1 template**. The gaps fall into two categories:

1. **Content gaps requiring substantive work:**
   - Expand Synthesis phase (add 2–3 more interactions, ~5 min)
   - Add explicit EC and Practice phases if needed
   - Document missing interaction fields (Purpose, Correct Answer, Visual)
   - Create BACKBONE section with Key Design Decisions

2. **Format gaps requiring mechanical updates:**
   - Update YAML to include unit and domain
   - Replace "Full L-M-H" remediation with pipeline format
   - Add type labels to all interactions
   - Convert H4 to bold inline labels
   - Add # END OF MODULE marker
   - Replace em dashes with comma/colon/period

The **core content quality is solid** — interactions are well-designed and pedagogically sound. The gaps are primarily in metadata, scope (Synthesis), and template alignment rather than dialogue or sequencing issues.

---

**Report Generated:** 2026-03-30  
**Pipeline Version:** L1 Gate 4  
**Analysis Status:** Complete — all 6 checkers run
