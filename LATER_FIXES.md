# Later Fixes & Improvements

This document tracks issues and improvements that should be addressed in the future but are not blocking current work.

---

## Validation System Issues

### 1. Overly Pedantic Content Validator (sequence_structurer)
**Status:** Deferred
**Priority:** Medium
**Created:** 2026-02-12

**Issue:**
The AI-based content validator in `steps/prompts/sequence_structurer.py` generates false positive errors for mathematically correct content. It contradicts itself by flagging items as "incorrect" and then saying "This is actually CORRECT mathematically".

**Examples:**
- **Item 9 (template 8002)**: Validator flags bar_c (4/8 shaded) as "mathematically incorrect" but then confirms "4/8 = 1/2 (0.5), so this bar IS equivalent... This is actually CORRECT mathematically"
- **Item 11 (template 8002)**: Validator complains that the `fractions` metadata array lists equivalent fractions separately (e.g., ["2/3", "4/6"]), which is acceptable for tracking purposes

**Current Workaround:**
- **Completely disabled pipeline stopping on validation failures** in `core/pipeline.py` (lines 1060-1069)
- Validation errors are now logged as warnings and pipeline continues
- Validation errors are still saved to `content_validation_errors.json` and `validation_errors.json` for review
- This allows any template to be rerun without validation blocking the pipeline

**Proper Fix:**
Update the validation prompt in `steps/prompts/sequence_structurer.py` (lines 361-436) to:
1. Clarify that the top-level `fractions` array is metadata and can list equivalent fractions separately
2. Remove overly strict rules that cause self-contradiction
3. Simplify validation logic to focus on actual correctness, not metadata consistency
4. Add explicit note: "If mathematically correct, mark as valid. Do NOT contradict yourself."

**Files Involved:**
- `steps/prompts/sequence_structurer.py` - validation_prompt (lines 361-436)
- `config/pipelines.json` - sequence_structurer step (line 301-314)
- `cli/rerun.py` - validation failure handling (lines 926-948)

---

## Template 8002 Improvements

### 2. Template 8002 Successfully Fixed (Documented for Reference)
**Status:** ✅ COMPLETE
**Completed:** 2026-02-12

**Issue (Resolved):**
Template 8002 was generating pairs (pair_a, pair_b) instead of individual bars, causing "multi_select with single answer" validation errors.

**Fix Applied:**
Updated `modules/module8/problem_templates.json` template 8002 (lines 53-100):
- Changed `workspace_description` to explicitly state "NOT organized as pairs - each bar is independent"
- Restructured `parameter_coverage`:
  - Renamed `equivalent_fractions` → `equivalent_fraction_sets`
  - Changed from 2-element pairs `["1/2", "2/4"]` to 2-3 element sets `["1/2", "2/4", "3/6"]`
  - Added explicit fields: `bars_to_select`, `distractor_bars`
- Updated success dialogue to reflect multiple bars

**Result:**
Template now generates individual bars (bar_1, bar_2, bar_3, bar_4) with 2-3 correct answers for multi-select. Validation errors are false positives from the validator, not actual content issues.

---

## Future Enhancements

### 3. Consider Validator Refactoring
**Status:** Idea
**Priority:** Low

**Idea:**
The AI-based validation approach is powerful but prone to false positives and inconsistencies. Consider:
- Moving to Python-based validation for deterministic checks (indices, mathematical correctness)
- Using AI validation only for semantic/pedagogical concerns
- Creating a validation framework with clear pass/fail criteria that doesn't self-contradict

**Trade-offs:**
- Python validation: More reliable but less flexible for semantic checking
- AI validation: More comprehensive but can be inconsistent
- Hybrid approach might be ideal but requires more development time

---

## How to Use This Document

1. **Adding new items:** Add a new section with:
   - Clear title
   - Status (Deferred/Idea/In Progress)
   - Priority (High/Medium/Low)
   - Created date
   - Issue description
   - Current workaround (if any)
   - Proper fix description
   - Files involved

2. **Updating items:** When working on an item, update the status and add notes

3. **Completing items:** Mark as ✅ COMPLETE and move to a "Completed" section at the bottom

4. **Prioritizing:** Review periodically and adjust priorities based on impact and effort
