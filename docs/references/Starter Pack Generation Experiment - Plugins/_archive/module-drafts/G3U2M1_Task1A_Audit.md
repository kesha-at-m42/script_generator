# TASK 1A: BACKBONE AUDIT — G3 Unit 2 Module 1

**Module:** M1 — What is Area? Measuring with Unit Squares
**Auditing:** Task 1 Backbone Draft (G3U2M1_Task1_Backbone.md)
**Auditor note:** Reading with fresh eyes. Author feedback incorporated where noted.

---

## AUDIT PASS 1: Cross-Reference Verification

### Table A vs. Module Mapping Spreadsheet

Verified the Module Mapping spreadsheet M1 row (Columns A–M) against Table A. All 13 populated column values transcribed accurately and completely. No columns missed. Columns N–AA are empty as noted. Table A is complete.

### Table B vs. TVP (Toy Flow docx)

Verified TVP Module 1 section (paragraphs 3–135) against Table B. Findings:

| # | Severity | Finding | Detail |
|---|----------|---------|--------|
| 1A.01 | MINOR | Table B labels TVP warmup as "2 sets" but TVP also details Sets 1–2 there | Accurate — just confirming the split is Warmup=Sets 1-2, Lesson Early=Sets 3-4. No error. |
| 1A.02 | NOTE | TVP paragraph 95 describes Late activities twice (paragraphs 90-96 are duplicated content) | The TVP docx contains two "Late activities" blocks. The first (para 84-88) says "3-4 shapes independently" with "rectangles only (tiling targets must tile cleanly with squares; non-rectangles risk accidental gaps before M2 rules)." The second (para 92-97) says "4-5 shapes independently" including "2-3 rectangles + 1-2 rectilinear non-rectangles (L-shapes or T-shapes)." Table B captured the SECOND (more complete) version. The first appears to be an earlier draft that wasn't deleted. **Table B made the right call but should note the TVP duplication.** |
| 1A.03 | MINOR | TVP "Scaffolding Progression" and "Tool Requirements" headers (para 122-123) have no content | The TVP has empty placeholder sections after M1 Synthesis. Table B didn't mention these. Not material — they're empty shells. |

### Table C — Conflict Log

| # | Severity | Finding | Detail |
|---|----------|---------|--------|
| 1A.04 | NOTE | Conflict 6 resolution may be wrong about TVP "copy error" | The TVP line "Quarter-tile snap with overlap detection (visual + audio) — same interaction as M2" could mean the snap MECHANIC is the same as M2 (i.e., the tiles snap the same way), not that overlap FEEDBACK is the same. The Notion spec confirms no feedback in M1, so the resolution is correct regardless. But the characterization of the TVP line as a "copy error" is speculative — it might be describing the snap mechanic, not the feedback system. Recommend: soften language to "this line appears to describe the snap mechanic shared with M2, not gap/overlap feedback." |
| 1A.05 | NOTE | Conflict 7 mis-attributes source text | Table C says TVP says "Counter available as scaffold (implies unlimited or sufficient tiles always present)" — but the TVP line about the counter and the tile supply question are separate issues. The counter line is about counting; the tile supply is a separate Notion spec feature. These are two different things conflated into one conflict entry. Recommend: split into two separate entries or clarify that the tile supply mode comes from the Notion spec alone, not from the counter discussion. |

---

## AUDIT PASS 2: Backbone vs. Cross-Reference Tables

### §1.0 THE ONE THING

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.06 | **MAJOR** | §1.0 Critical Misconception | "Taller = larger" is listed as the Critical Misconception. **Author feedback: this is NOT a standalone misconception worth targeting for the unit.** It's a moment within the comparison activity, not something recurring enough to be the Critical Misconception. The TVP lists it as "PRIMARY" for M1, but the Misconceptions database doesn't include it, and the author confirms it's over-elevated. | **Revise Critical Misconception.** The actual Critical Misconception for M1 should be **#1: Gaps/Overlaps Acceptable** — this is the misconception that carries forward through the unit and that M1 previews for M2. The "taller = larger" tendency is better documented as a design consideration within the comparison activities, not the module's critical misconception. Alternative: the Critical Misconception could be "area is only about rectangles" — the comparison set shape diversity is designed to prevent this. |
| 1A.07 | MINOR | §1.0 The One Thing | Statement includes "with no gaps and no overlaps" — but gap/overlap rules are NOT formally taught in M1 (that's M2). The One Thing references a concept this module only previews. | Soften to: "...measured by counting how many unit squares fit inside it." The gap/overlap precision belongs to M2's One Thing. M1's emphasis is on the concept that area IS measurable by counting tiles. |

### §1.1 LEARNING GOALS

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.08 | NOTE | §1.1 Module Goal | "Today you'll figure out..." uses "Today" — this is acceptable for the Module Goal (student-facing framing) since it's about THIS session, not a cross-session reference. But check against session-relative language rules. The Warmup Playbook says "session-relative language only." "Today" refers to the current session, which is fine. | No fix needed — "Today" for current session is permitted. |
| 1A.09 | MINOR | §1.1.4 | Section numbered §1.1.4 "Cognitive Focus" — but Template v2 doesn't define §1.1.4. The template shows §1.1.1 (Standards Cascade), §1.1.2 (Module Bridges), §1.1.3 (OUR Lesson Sources), and then moves to §1.2. Adding §1.1.4 and §1.1.5 as custom subsections is allowed but should be tagged as `[Module-Specific]`. | Add `[Module-Specific]` tag or integrate Cognitive Focus and Question/Test Language into existing sections. Cognitive Focus could go in §1.1 main body. Question/Test Language could go in §1.2 or §1.8. |

### §1.2 SCOPE BOUNDARIES

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.10 | MINOR | §1.2 Scope Checklist | Checklist items are pre-checked `[x]` — the template shows them as unchecked `[ ]` for the author to resolve. Pre-checking implies they've been verified, which is appropriate for a draft that's been through self-check. However, the convention should be clarified: are these for the DRAFTER to check (pre-checked OK) or for a REVIEWER to check (should be unchecked)? | NOTE for template convention — not a fix for this SP. |

### §1.3 VOCABULARY ARCHITECTURE

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.11 | NOTE | §1.3 Assessment Vocabulary | Lists "area, unit square, square unit" — but does NOT list "plane figure." The Module Mapping includes "plane figure" in Vocabulary to Teach. Is "plane figure" assessment vocabulary (appears on state test)? The 3.MD.C.5 standard uses "plane figure" — likely assessment vocabulary. | Verify: does "plane figure" appear on state tests? If yes, add to Assessment Vocabulary. If it's just instructional vocabulary (used by teachers but not on tests), current placement is fine. Flag for author. |
| 1A.12 | NOTE | §1.3 Vocabulary Staging | "measure" appears in the Vocabulary to Teach list but is staged only as part of "Lesson Mid (Tiling)" alongside "square tiles (bridging), tile, measure." The staging approach for "measure" isn't explicitly described — it's bundled with the bridging terms. | Consider adding explicit staging: "measure" introduced when the Guide frames the transition from estimation to measurement ("We need a TOOL to measure exactly"). This is the Lesson Early→Mid transition. |

### §1.4 MISCONCEPTIONS

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.13 | **MAJOR** | §1.4.1 | "Taller = Larger" is listed as PRIMARY misconception (§1.4.1) with no global ID. Per author feedback, this should NOT be a standalone misconception entry. It's a design feature of the comparison sets, not a targetable misconception for the unit. | **Remove §1.4.1 as a standalone misconception section.** Move the "taller = larger" design consideration into the Plane Figures §1.5.1 Guardrails (already there as "Include at least one set where taller shape has LESS area") and into a Scope Boundary note. Promote #1 Gaps/Overlaps to §1.4.1 as PRIMARY. |
| 1A.14 | MINOR | §1.4.2 | Gaps/Overlaps is labeled "SECONDARY — preview only" but if it becomes the only misconception (after removing "taller = larger"), the label needs to reflect its actual role in M1. | Relabel as PRIMARY with qualifier: "PRIMARY — previewed in M1, formally addressed in M2." This signals to script writers that this misconception IS important to the unit arc even though M1 only introduces it. |
| 1A.15 | NOTE | §1.4 | Template says "Include 1-3 misconceptions most relevant to this module. Use global IDs from the Misconceptions database for cross-referencing." With "taller = larger" removed, we have only 1 misconception (#1 Gaps/Overlaps). Consider: should #9 "Array Structure Not Seen" appear as a SECONDARY since students in M1 Late activities tile rectangles that are arrays? | Probably not — students aren't being asked to SEE array structure in M1 (that's M3). #1 alone is appropriate for M1. |

### §1.5 TOY SPECIFICATIONS

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.16 | NOTE | §1.5.1 Comparison Set Sequence table | Set 1 says "Triangles (3 right triangles, different sizes)" — but the handwritten sketches show 3 triangles that are NOT all right triangles (some appear to be scalene). The TVP says "Triangles — same shape type, different sizes" without specifying right triangles. | Change "3 right triangles" to "3 triangles" to match TVP. The handwritten sketches show varied triangle types. |
| 1A.17 | NOTE | §1.5.1 | The Comparison Set Sequence table is a useful addition not in the Template v2. It's essentially a data specification for the authored comparison sets. This belongs in §1.5 as module-specific content. Good addition — tag as `[Module-Specific]`. | Add `[Module-Specific]` tag to the subsection header. |
| 1A.18 | NOTE | §1.5.2 Side Length Labels | States "Available via tap/click but not proactively shown." Could not verify this from the Unit Square Tiles Notion spec — the spec doesn't mention side length labels on individual tiles. This may be capability assumption. | Verify against Notion spec or remove. If this is a desired capability not yet in the spec, flag as a **Toy Spec Update Needed**. |
| 1A.19 | NOTE | §1.5.2 Snap Mode | States "Quarter-tile snap (half linear measure). Semi-freeform..." — this level of detail comes from the TVP, which says "Quarter-tile snap with overlap detection." The Notion spec for Unit Square Tiles would need to confirm this snap behavior. | Flag as **Toy Spec Verification Needed** — confirm snap mode is documented in the Unit Square Tiles Notion spec. |
| 1A.20 | **MAJOR** | §1.5 | **Missing: Grid Rectangles toy.** The Grid Rectangles Notion spec states it "Can appear with: Unit Square Tiles (M1-M2)" for tiling activities. The TVP says students tile "Plane Figures" — but the actual tiling target surface for rectangles is likely a Grid Rectangle (in "no grid" / blank mode), not a Plane Figure. Plane Figures are display-only polygons; Grid Rectangles are the rectangled tiling surfaces. For the comparison activities (varied polygons), Plane Figures is correct. For tiling activities (rectangles only), it may be Grid Rectangles in blank/no-grid mode. | **Clarify with author:** Are M1 tiling targets rendered as Plane Figures (simple rectangle outlines) or Grid Rectangles (in `grid_state: "none"` or similar)? If Grid Rectangles, add to §1.5 as a secondary toy with M1 configuration (no grid visible, used as tiling target surface). If Plane Figures serve as both comparison shapes AND tiling targets, document this dual-role explicitly. This affects engineering — the two toys have different rendering pipelines. |
| 1A.21 | MINOR | §1.5 | No `interaction_tools` field in YAML front matter. Template v2 checklist item 1A says to include MC, Drag and Drop, Word Problems (or documented reason for omission). | Add `interaction_tools` to YAML: MC (comparison sets), Drag and Drop (tiling). Word Problems not used — document omission. |

---

## AUDIT PASS 3: Template v2 Structural Compliance

### YAML Front Matter

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.22 | MINOR | YAML `module_id` | Value is `M01` — template convention shows `M[XX]` but no zero-padding requirement is stated. Other modules would be M1, M2, etc. Consistency across the unit matters more than the template example. | Standardize with author: `M01` (zero-padded) or `M1`? Both work. Recommend `M01` for sort-order consistency across 14 modules. |
| 1A.23 | MINOR | YAML | Missing `interaction_tools` field (same as 1A.21). | Add field. |

### Required Sections

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.24 | NOTE | §1.6–§1.10 | Sections §1.6 through §1.10 are not present — expected, since this is a backbone-only draft (Task 1 scope is §1.0–§1.5). These will be drafted in Tasks 2-5. | No fix needed — expected for this stage. |

### Naming & Convention

| # | Severity | Location | Finding | Recommended Fix |
|---|----------|----------|---------|-----------------|
| 1A.25 | MINOR | §1.5.1 | "Changes from M[N-1]" uses literal `M[N-1]` instead of the resolved value. Should be "Changes from prior module" or specific text since M1 has no prior module. | Change to `**Changes from prior:** First appearance in Unit 2.` (drop the bracket notation) |

---

## SUMMARY

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR | 3 |
| MINOR | 8 |
| NOTE | 10 |
| **TOTAL** | **21** |

### Top 5 Priority Fixes

1. **[1A.06 + 1A.13] Demote "Taller = Larger" from Critical Misconception and standalone §1.4 entry.** Promote #1 Gaps/Overlaps to PRIMARY. Move the comparison set design considerations into §1.5.1 Guardrails (already partially there). This is the biggest structural change — it affects §1.0 and §1.4.

2. **[1A.07] Remove "no gaps and no overlaps" from The One Thing.** M1 doesn't formally teach this rule. The One Thing should focus on what M1 DOES teach: area is measurable by counting tiles.

3. **[1A.20] Clarify whether tiling targets are Plane Figures or Grid Rectangles.** This is an engineering question with design implications. If Grid Rectangles, add to §1.5 as secondary toy.

4. **[1A.21/1A.23] Add `interaction_tools` to YAML.** Minor but catches a template compliance gap.

5. **[1A.16] Fix "3 right triangles" → "3 triangles"** in Comparison Set Sequence table to match TVP and handwritten sketches.

### Stale Module Mapping Flags

All 5 flags from Table A are legitimate staleness indicators:
- Pattern blocks (resolved by SME — mapping not updated)
- Cutting/overlaying (OUR curriculum activities not in digital adaptation)
- "Square tiles" bridging term (addressed in SP but mapping phrasing is ambiguous)
- Counter scaffold (resolved by SME — mapping not updated)
- Empty columns N–AA (no additional data)

**Recommendation:** These are informational — no SP changes needed, but consider a Module Mapping cleanup pass after the SP chain completes.

### Toy Spec Updates to Track

| Toy | Update Needed | Source |
|-----|---------------|--------|
| Plane Figures | Update "Shapes per comparison" constraint from 2 to 3 | Conflict 4 |
| Plane Figures | Clarify dual role (comparison display + tiling target) OR clarify that tiling uses Grid Rectangles | 1A.20 |
| Unit Square Tiles | Verify snap mode documentation (quarter-tile snap) | 1A.19 |
| Unit Square Tiles | Verify side length labels capability | 1A.18 |

---

**END OF TASK 1A AUDIT**

*Ready for Gate 1: Author reviews backbone + audit findings.*
