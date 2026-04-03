# G3U2M4 BACKBONE AUDIT
**Auditor:** Claude (automated) | **Date:** 03.16.26
**Scope:** Field-by-field comparison of `G3U2M4_Task1_Backbone.md` against Module Mapping M4 row, TVP M4 section, and Important Decisions.

---

## AUDIT METHOD

For each Backbone section, I compared every claim against the raw source text. Findings are categorized:

- **✅ MATCH** — Backbone faithfully reflects source
- **⚠️ DISCREPANCY** — Mismatch between Backbone and source requiring author decision
- **🔴 OMISSION** — Source material not represented in Backbone
- **🟡 ADDITION** — Backbone contains material not in any source (may be valid inference)

---

## §1.0 THE ONE THING

### ✅ MATCHES
- **Core statement** ("area of a rectangle can be found by multiplying its side lengths — because '4 rows of 6' IS '4 × 6'") — matches TVP Learning Goal ("Understand that the area of a rectangle can be found by multiplying the side lengths") and Module Mapping Core Concept ("Area as Multiplication").
- **CRA Stage** ("Representational → Abstract transition") — matches TVP ("CRA Stage: REPRESENTATIONAL → ABSTRACT transition").
- **Critical Misconception #4.0** — matches TVP ("Formula as arbitrary rule (PRIMARY)") and Module Mapping ("wrong rectangle for expression").
- **SME insight about recognition vs. efficiency** — verbatim match to TVP: "Don't motivate multiplication primarily through efficiency."
- **Grid support remains throughout** — matches Decision #3 (M1-M4 full grids) and TVP ("Keep full grids through M4").

### ⚠️ DISCREPANCY D1: Success Indicator mentions "states the area with units"
- **Backbone says:** "calculates the product, and states the area with units"
- **TVP SME Q5 resolved:** "No named units in M4. All problems use generic 'square units.'"
- **Assessment:** Not a true error — "units" here means generic "square units," but the language could be read as implying named units. Consider clarifying to "states the area in square units."
- **Severity:** LOW (cosmetic clarity)

### ⚠️ DISCREPANCY D2: Success Indicator mentions "without Equation Builder scaffolding or Guide prompting"
- **Backbone says:** student "independently identifies the dimensions, builds a correct multiplication expression... without Equation Builder scaffolding or Guide prompting."
- **TVP EC structure:** EC.1 uses unlabeled EB slots, EC.2 uses EB with no scaffolding, EC.3 removes EB entirely. The highest bar is EC.3 (no EB at all, MC only).
- **Assessment:** The Backbone's Success Indicator is describing EC.2-level independence (EB present but unscaffolded) while also mentioning "without Equation Builder scaffolding." This is accurate for EC.2 but the *true* culminating indicator should also encompass EC.3 (no EB, can determine area via multiplication or skip-counting alone). Currently the indicator doesn't capture EC.3's MC-only assessment.
- **Severity:** MEDIUM — The success indicator should encompass all three EC levels or clearly state it describes the peak performance target.

### 🟡 ADDITION A1: "Biggest Risk" paragraph
- The "Biggest Risk" paragraph about students mechanically filling in the Equation Builder is a valid authorial synthesis not directly quoted from any single source. It draws on the SME insight and the pedagogical rationale. This is appropriate for §1.0 — no issue.

---

## §1.1 LEARNING GOALS

### ✅ MATCHES
- **L1 verbatim** ("Relate multiplication to finding the area of rectangles.") — exact match to Module Mapping "OUR Learning Goals (Verbatim)."
- **OUR Lessons: L5** — matches Module Mapping.
- **Question/Test Language stems** — all three stems from Module Mapping reproduced verbatim.

### ⚠️ DISCREPANCY D3: Module Goal (Student-Facing) source
- **Backbone says:** "Today you'll discover that the rows and columns you've been counting have a name in math — multiplication..."
- **Source:** This is an authored student-facing restatement, not a verbatim quote from any source document. The TVP's Learning Goal is: "Understand that the area of a rectangle can be found by multiplying the side lengths; use multiplication to find the area of rectangles with whole-number side lengths."
- **Assessment:** Student-facing module goals are expected to be authored per the template ("Module Goal (Student-Facing)"). This is fine — it's flagged for transparency only.
- **Severity:** INFORMATIONAL

### §1.1.1 Standards Cascade

### ✅ MATCHES
- **Building On:** 3.MD.C.6 and 3.OA.A.1 — matches Module Mapping exactly.
- **Building Toward:** 3.MD.C.7.b (area without grid) — matches Module Mapping exactly.
- **3.OA.B.5** in Addressing — matches Module Mapping.

### ✅ AF#1 RESOLUTION CORRECTLY APPLIED
- **3.MD.C.7.a** added to Addressing — author confirmed it fits M4. TVP lists it as a standard (para 353: "Standard: 3.MD.C.7a, 3.MD.C.7b"). Module Mapping only listed 3.MD.C.7.b. The Backbone correctly adds 7.a per author resolution and TVP evidence.

### ⚠️ DISCREPANCY D4: Standards Note vocabulary claim
- **Backbone says:** "Required vocabulary per Standards Mapping for 3.MD.C.7.b: side lengths, multiply, dimensions, length, width."
- **Module Mapping Vocabulary to Teach:** "expression, factor, product, multiply, dimensions" — does NOT include "length" or "width" or "side lengths."
- **TVP Vocabulary Progression:** Introduces "length" and "width" in Mid activities.
- **Assessment:** The Backbone is pulling "length, width, side lengths" from the TVP and the Standards Mapping sheet (which maps standard language), but the Module Mapping's explicit Vocabulary to Teach list doesn't include them. The Backbone's §1.3 Vocabulary Notes paragraph already explains this gap ("Module Mapping lists 'dimensions' but not 'length' and 'width' explicitly. TVP's vocabulary progression introduces 'length' and 'width' in Mid activities."). So the gap is already documented — but the Standards Note in §1.1 states these as "required" without noting the Module Mapping gap.
- **Severity:** LOW (already explained in §1.3, just slightly overstated in §1.1)

### §1.1.2 Module Bridges

### ✅ MATCHES
- **From M3:** Accurately reflects M3 SP content (structure-seeing, skip-counting, "rows of" language). M3 Synthesis closure quote is verbatim.
- **This Module:** Matches TVP's description of the M4 progression (rows-to-multiplication, Equation Builder, commutativity, formula emergence in Synthesis).
- **To M5:** Matches TVP's M4→M5 bridge ("what SIZE are those square units?") almost verbatim from TVP para 478.

### §1.1.3 OUR Lesson Sources

### ✅ MATCHES
- L5 content description matches Module Mapping Notes and TVP activities.
- Adaptation notes correctly flag: physical → digital, gallery walk → systematic expression building, "create rectangle from expression" direction reversed per TVP.

### ⚠️ DISCREPANCY D5: Module Mapping says "Create rectangles from given expressions"
- **Module Mapping Notes:** "Create rectangles from given expressions."
- **TVP:** Students build expressions FROM rectangles (not the reverse).
- **Backbone:** Correctly identifies this as a reversal per TVP ("OUR's 'create rectangle from expression' direction reversed per TVP to 'build expression from rectangle'").
- **Assessment:** The Backbone flags this correctly — the Module Mapping is stale on this point and the TVP supersedes it. This is a known conflict already in Table C. No action needed, but worth confirming the author is aware.
- **Severity:** INFORMATIONAL (already handled)

---

## §1.2 SCOPE BOUNDARIES

### ✅ Must Teach
- Multiplication-area connection ✅
- Expression building from rectangles ✅
- Commutativity ✅
- Vocabulary list ✅ (see D4 re: length/width sourcing)
- Formula "Area = length × width" ✅ (from TVP Synthesis)
- Skip-counting as valid strategy ✅ (from TVP SME Q6)
- Full grid visible ✅ (Decision #3)

### ✅ Must Not Include
- Grid fading (Decision #3) ✅
- Named units (SME Q5) ✅
- Rectangle creation by students (TVP reversal) ✅
- Perimeter (Decision #5) ✅
- Equation Builder as calculator ✅
- Fact memorization ✅
- "Faster" motivation ✅ (SME insight)
- Area without grid ✅
- Composite figures ✅

### ⚠️ DISCREPANCY D6: "expression, factor, product, multiply, dimensions, length, width" in Must Teach
- **Module Mapping Vocabulary to Teach:** "expression, factor, product, multiply, dimensions" (5 terms)
- **Backbone Must Teach:** adds "length, width" (7 terms)
- **TVP:** Introduces "length" and "width" in Mid vocabulary progression.
- **Assessment:** Same issue as D4 — the two extra terms come from TVP, not Module Mapping. Already explained in §1.3 Vocabulary Notes. The question is whether Must Teach should only list Module Mapping terms or should include TVP-sourced terms too.
- **Severity:** LOW — TVP is downstream and more detailed; including them is correct per Resolution Hierarchy (TVP > Module Mapping for tool/visual details). Author should confirm these belong in Must Teach.

### 🔴 OMISSION O1: Module Mapping "Scaffolding of Visuals" not fully represented
- **Module Mapping says:** "Gridded rectangles with row/column counts visible; Expression matching activities; Build rectangle from expression tool"
- **Backbone §1.2:** Covers gridded rectangles and expression building but doesn't mention "Expression matching activities" as a distinct activity type.
- **TVP:** The TVP's Early activities describe identifying structure then building expressions — not "matching" in the MC-matching sense. The Module Mapping phrase may be stale (superseded by TVP's "build expression from rectangle").
- **Assessment:** Likely stale Module Mapping language, but worth confirming. If "expression matching" means something distinct (e.g., given 3 expressions, match each to a rectangle), that activity type isn't in the TVP and isn't in the Backbone.
- **Severity:** LOW (probably stale, but author should confirm)

### ✅ BRIDGE MODULE designation — matches TVP "⚠️ BRIDGE MODULE" flag.

### ✅ Scope Confirmation Checklist — all items accurately reflect the constraints from source documents.

---

## §1.3 VOCABULARY ARCHITECTURE

### ✅ MATCHES
- **Staging table phases** match TVP's Vocabulary Progression (Early: "rows of" → "×"; Mid: length/width; Late: formula).
- **Assessment Vocabulary list** correctly merges Module Mapping and TVP terms.
- **Unit 1 callback note** matches TVP ("Students used Equation Builder for expressions in Unit 1") and Decision #4 (array knowledge helpful not required).

### ✅ Terms to Avoid
- Formula, standard units, perimeter, decompose — all correctly sourced from M3 SP §1.3, Decision #5, and Decision #3.
- "Faster" motivation — correctly sourced from TVP SME insight.

### ⚠️ DISCREPANCY D7: Vocabulary Teaching Notes not fully surfaced
- **Module Mapping Vocabulary Teaching Notes:** "'5 × 7 means 5 rows of 7' or '5 groups of 7.' Factors = numbers multiplied. Product = result. Dimensions = the row and column counts."
- **Backbone §1.3:** The staging table captures these definitions implicitly (e.g., "Factors = numbers multiplied" appears in the Lesson S2 row as "'The numbers you multiply — 3 and 7 — those are called factors.'"). But the specific phrasing "5 groups of 7" and the concise definitions from Module Mapping aren't reproduced verbatim.
- **Assessment:** The Backbone's staging table provides richer, phase-appropriate introduction language that INCLUDES the Module Mapping definitions but rephrases them in context. This is a stylistic choice, not an omission. However, the "groups of" language isn't in the Backbone — the TVP and Backbone both use "rows of" exclusively. Worth noting that Module Mapping's "groups of" framing is NOT in the TVP.
- **Severity:** LOW — "rows of" is more mathematically precise for area context. "Groups of" is general multiplication language from Unit 1 / 3.OA.A.1. The Backbone's choice to use "rows of" aligns with the area-specific TVP language. Author should confirm "groups of" is intentionally excluded from M4.

### 🟡 ADDITION A2: §1.3 introduction approach descriptions
- The staging table's "Introduction Approach" column contains authored pedagogical guidance (e.g., "NOT a formal vocabulary introduction — a recognition moment"). This is valid authorial synthesis consistent with the TVP's pedagogical approach. No issue.

---

## §1.4 MISCONCEPTIONS

### ✅ MATCHES
- **#4.0 as PRIMARY** — matches TVP ("Formula as arbitrary rule (PRIMARY)") and Module Mapping ("wrong rectangle for expression").
- **#2.0 and #9.0 as SECONDARY** — matches Misconceptions sheet (both M3-M4, HIGH).
- **AF#2 resolution** correctly applied.

### ✅ Trigger Behaviors, Why It Happens, Visual Cues, Prevention Strategies
- All three misconception entries contain detailed, accurate descriptions consistent with source materials and pedagogical reasoning.

### ⚠️ DISCREPANCY D8: TVP misconception labeling vs. Misconceptions sheet
- **TVP para 375:** "M3: Formula as arbitrary rule (PRIMARY)"
- **TVP para 376:** "M10: Dimension confusion (MODERATE)"
- **Misconceptions sheet:** #4.0 is "Wrong Rectangle for Expression" (listed at M5, MEDIUM).
- **Backbone:** Maps TVP's "Formula as arbitrary rule" to #4.0, which is reasonable — both describe a disconnect between expression and rectangle structure. But note the Misconceptions sheet places #4.0 at **M5**, not M4. The Module Mapping's "Key Misconceptions" field says **"M4 (wrong rectangle for expression)"** — directly placing it at M4.
- **Assessment:** There's a minor sourcing inconsistency: the Misconceptions sheet says M5, but the Module Mapping row explicitly says M4. The Backbone follows the Module Mapping (correct per Resolution Hierarchy since this is a direct field entry for M4). TVP's "M3: Formula as arbitrary rule" uses TVP-internal numbering (M3 = the 3rd misconception listed in the TVP, not Module 3). This mapping was already flagged as AF#2 and resolved.
- **Severity:** INFORMATIONAL (already resolved, just noting for audit completeness)

### 🔴 OMISSION O2: TVP "Dimension confusion (MODERATE)" not explicitly treated
- **TVP para 376:** "M10: Dimension confusion (MODERATE) — Both orientations taught explicitly to prevent 'which number goes first?' errors"
- **Backbone §1.4:** Mentions "Note: 5×7 and 7×5 are BOTH correct (commutativity) — only truly mismatched dimensions are errors" within #4.0, and the commutativity teaching is thorough. But there's no standalone treatment of "dimension confusion" as a named misconception.
- **Assessment:** The Backbone subsumes dimension confusion into the commutativity teaching and §1.5 orientation handling (AF#3). This is a design choice, not a gap — the TVP calls it MODERATE and says "Both orientations taught explicitly to prevent" it. The Backbone does exactly that. However, the Working Notes Table C Conflict #6 already notes this: "TVP's 'dimension confusion' treated as prevention target within commutativity teaching."
- **Severity:** LOW (intentional design choice, already documented in Working Notes)

---

## §1.5 TOY SPECIFICATIONS

### §1.5.1 Grid Rectangles

### ✅ MATCHES
- **Full grid throughout** — Decision #3 ✅
- **Generic "square units"** — SME Q5 ✅
- **Factors 2-10** — TVP Data Constraints ✅
- **Products within 100** — TVP ✅
- **Both orientations** — TVP + AF#3 ✅
- **Row highlighting available in Warmup/Early, off in Mid/Late** — TVP Table 6 ✅
- **Animated 90° rotation** — TVP Early activities key beat ✅

### ⚠️ DISCREPANCY D9: Dimension Labels not in Backbone
- **TVP Table 7 Row 4 (Dimension Labels):** "Always visible when grid fades | Visible alongside full grid from Mid onward (when 'length' and 'width' vocabulary is introduced)"
- **Backbone §1.5.1:** Does NOT mention dimension labels appearing on Grid Rectangles in Mid/Late. The configuration table covers grid state, highlighting, rotation, and interaction — but not dimension labels.
- **Assessment:** The TVP specifies dimension labels become visible "alongside full grid from Mid onward." This is significant because it's part of the vocabulary bridge (students see "length" and "width" labels on the rectangle sides when those terms are introduced in Lesson S2). The Backbone's vocabulary staging (§1.3) mentions introducing length/width in S2, but the toy configuration doesn't specify that labels appear on the Grid Rectangles display.
- **Severity:** MEDIUM — This is a functional toy configuration detail that script writers need. Dimension labels appearing in Mid is the visual mechanism for the vocabulary transition from "rows/columns" to "length/width."

### ✅ Progression table — phases, configurations, and paired tools all match TVP Table 6 and activity descriptions.

### ✅ Guardrails — accurately derived from Decisions and TVP constraints.

### §1.5.2 Equation Builder

### ✅ MATCHES
- **Components** (number tiles 2-10, ×, =) — TVP para 449 ✅
- **Template** (___ × ___ = ___) — TVP para 450 ✅
- **Interaction** (drag-and-drop or click-and-place) — TVP para 451 + Decision #6 ✅
- **Validation** (both orientations accepted) — TVP para 452 ✅
- **Scaffolding progression** (pre-labeled → unlabeled → independent) — TVP para 453 ✅
- **First appearance note** — TVP para 482 ✅

### ✅ Scaffolding Progression table — matches TVP Table 6 and EC descriptions exactly.

### ✅ Guardrails — correctly derived.

### §1.5.3 Data Constraints

### ✅ MATCHES
- **Warmup rectangles** (4×6, 6×4) — TVP paras 382, 385 ✅
- **Early** (2×4, 3×5, 4×6) — TVP para 399 ✅
- **Mid** (3×7, 5×6, 4×8) — TVP para 409 ✅
- **Late** (6×7, 5×9, 8×8) — TVP para 462 ✅
- **Global constraints** (factors 2-10, products ≤100, both square and non-square, generic square units, no unit conversion, skip-counting available) — all from TVP ✅

### ⚠️ DISCREPANCY D10: TVP Data Constraints mention "cm, inches, feet" but SME Q5 overrides
- **TVP para 458:** "Consistent units within each problem; mix across problems (cm, inches, feet)"
- **TVP SME Q5 (para 484):** "No named units in M4. All problems use generic 'square units.'"
- **Backbone:** Correctly follows the SME resolution — "no named units (SME Q5 resolved)."
- **Assessment:** The Backbone is correct. The TVP Data Constraints line is pre-SME-resolution text that was overridden by SME Q5. This is already in Table C as Conflict #5.
- **Severity:** INFORMATIONAL (correctly handled)

### ⚠️ DISCREPANCY D11: Practice section mentions "word problems" with unit specifics
- **TVP para 433-434:** "Some word problems: 'A rectangle is 7 cm by 3 cm'" then corrected in 434 to "7 units long and 3 units wide... All M4 problems use generic 'square units.'"
- **Backbone §1.5.3 Practice row:** "Within 2-10, products ≤100 | Varied | 4-100 | Full grid visible, no EB scaffolding"
- **Assessment:** The Backbone's Practice row doesn't mention word problems at all. The TVP includes word problems and comparison problems in Practice. This isn't a §1.5 issue per se (Practice content details belong in Task 3 when §1.8 Practice is drafted), but the Data Constraints table could note that Practice includes word problems.
- **Severity:** LOW (Practice section is Task 3 scope; data constraints table is about factor ranges, not activity types)

### ✅ Interaction Constraints — all four constraints (no verbal, no keyboard, no open-ended, Guide speaks/student acts) match platform constraints and are correctly stated.

---

## SUMMARY OF FINDINGS

### By Severity

| ID | Section | Severity | Finding |
|:---|:--------|:---------|:--------|
| D1 | §1.0 | LOW | "states the area with units" — clarify to "in square units" |
| D2 | §1.0 | **MEDIUM** | Success Indicator doesn't fully capture EC.3 (no EB, MC only) |
| D3 | §1.1 | INFO | Student-facing Module Goal is authored (expected) |
| D4 | §1.1 | LOW | Standards Note claims "required" vocabulary not in Module Mapping (explained in §1.3) |
| D5 | §1.1.3 | INFO | Module Mapping "create rectangles" vs. TVP "build expressions" (already in Table C) |
| D6 | §1.2 | LOW | Must Teach vocabulary adds "length, width" beyond Module Mapping list |
| D7 | §1.3 | LOW | "Groups of" phrasing from Module Mapping excluded; "rows of" used per TVP |
| D8 | §1.4 | INFO | Misconceptions sheet vs. Module Mapping on #4.0 module placement (resolved) |
| D9 | §1.5.1 | **MEDIUM** | Dimension Labels on Grid Rectangles in Mid/Late not specified in Backbone |
| D10 | §1.5.3 | INFO | TVP "cm, inches, feet" overridden by SME Q5 (correctly handled) |
| D11 | §1.5.3 | LOW | Practice word problems not mentioned in Data Constraints table |
| O1 | §1.2 | LOW | "Expression matching activities" from Module Mapping not in Backbone (probably stale) |
| O2 | §1.4 | LOW | "Dimension confusion" not standalone misconception (subsumed into commutativity — intentional) |

### Action Items for Author

**MEDIUM priority (recommend fixing before Task 2):**

1. **D2 — Success Indicator scope:** Consider expanding to cover all three EC tiers, e.g.: "EC.1: builds expression with slot scaffolding. EC.2: builds expression independently. EC.3: determines area without Equation Builder (MC only)." Or keep as-is if the Success Indicator is meant to describe the single peak performance target (EC.2 level).

2. **D9 — Dimension Labels:** TVP Table 7 specifies "Dimension Labels: Visible alongside full grid from Mid onward." This should be added to the Grid Rectangles configuration table and the Progression table (Lesson S2/S3/EC/Synthesis rows should note "dimension labels visible"). This is the visual mechanism for the "rows/columns" → "length/width" vocabulary transition.

**LOW priority (can fix now or defer to Task 2):**

3. **D1 — "with units" → "in square units"** in Success Indicator for clarity.
4. **D6/D4 — length/width in Module Mapping:** Confirm that adding "length, width" to Must Teach and Standards Note from TVP (beyond Module Mapping's 5-term list) is intentional.
5. **D7 — "groups of" exclusion:** Confirm that omitting Module Mapping's "groups of" phrasing in favor of TVP's "rows of" is intentional for M4's area context.
6. **O1 — "Expression matching activities":** Confirm this Module Mapping phrase is stale (superseded by TVP's "build expression from rectangle").

**INFORMATIONAL (no action needed):**
- D3, D5, D8, D10 — all previously documented or expected per template conventions.

---

## FIXES APPLIED (03.16.26)

All items below have been applied to the Backbone:

| ID | Fix |
|:---|:----|
| D1 | "with units" → "in square units" in Success Indicator |
| D2 | No change needed — M3 SP uses the same single-target convention for Success Indicator. Consistent. |
| D4/D6 | Added sourcing note in §1.1.1 Standards Note: "Module Mapping lists 5 terms... 'length' and 'width' added per TVP... see §1.3 for rationale." |
| D7 | Added Vocabulary Note: "'Rows of' vs. 'Groups of'" explaining the exclusion of Module Mapping's "groups of" phrasing. |
| D9 | Added Dimension Labels row to §1.5.1 Configuration table with scaffold→remove→reappear pattern (Off in Warmup/Early → Visible in Mid/Late → Off in EC primary flow, available On Correct/Remediation → Visible in Synthesis). Added Dim Labels column to Progression table. |
| O1 | Added note in §1.1.3 OUR Lesson Sources: "Module Mapping's 'Expression matching activities' and 'Build rectangle from expression tool' are superseded by TVP's structure-first approach." |
| — | Added Anti-Pattern Detection block under §1.4.1 #4.0 (PRIMARY misconception), per M3 SP convention. |
| — | Added UX Component Requirements table to §1.5.1, per M3 SP convention. |

---

## M3 STARTER PACK STRUCTURAL COMPARISON

Compared M4 Backbone (§1.0-§1.5) against M3 Starter Pack (§1.0-§1.5) for structural consistency.

### Section-by-Section

| Section | M3 Convention | M4 Status |
|:--------|:-------------|:----------|
| **§1.0 THE ONE THING** | Core statement, CRA Stage, Critical Misconception, Success Indicator, Biggest Risk | ✅ All present, same order, same format |
| **§1.1 LEARNING GOALS** | Verbatim OUR goals, Module Goal (student-facing), EC Tests, Question stems, Standards Cascade, Module Bridges, OUR Sources | ✅ All present. M3 has L1+L2 (two lessons); M4 correctly has L1 only (one lesson). |
| **§1.2 SCOPE BOUNDARIES** | Must Teach, Must Not Include, ⚠️ Critical Module flag, Scope Confirmation Checklist | ✅ All present. M4 uses ⚠️ BRIDGE MODULE instead of ⚠️ CRITICAL MODULE — appropriate. |
| **§1.3 VOCABULARY** | Assessment Vocabulary, Staging table (Phase/Terms/Approach), Vocabulary Notes, Terms to Avoid | ✅ All present. M4 adds two extra Vocab Notes (length/width sourcing, "rows of" vs "groups of") — good. |
| **§1.4 MISCONCEPTIONS** | PRIMARY + SECONDARY with Trigger/Why/Visual/Prevention + Anti-Pattern Detection on PRIMARY | ✅ All present after fix. Anti-Pattern Detection added. |
| **§1.5 TOY SPECS** | Notion Spec + Changes from prior module, Purpose, Config table, Guardrails, Progression table, Data Constraints, UX Component Requirements, Interaction Constraints | ✅ All present after fix. M4 has two toys (Grid Rectangles + Equation Builder) vs. M3's one — each with full config/guardrails/scaffolding progression. UX Component Requirements added. |

### Structural Differences (Intentional)

1. **Two toys vs. one:** M4 introduces Equation Builder alongside Grid Rectangles. Each toy gets its own full specification block (config table, guardrails, scaffolding progression). M3 had only Grid Rectangles. This is a legitimate structural expansion, not a deviation.

2. **Data Constraints as standalone section:** M3 embedded Data Constraints within Grid Rectangles §1.5.1. M4 pulls Data Constraints into its own §1.5.3 subsection because constraints span BOTH toys (grid dimensions affect which EB tiles are available). This is a better organizational choice for multi-toy modules.

3. **Interaction Constraints at end of §1.5:** Both M3 and M4 place Interaction Constraints as the final block after all toy specs. ✅ Consistent.

4. **Dimension Labels (new capability):** M3 didn't use dimension labels. M4 introduces them as part of the vocabulary bridge. Scaffold→remove→reappear pattern established.

### Convention Alignment Verdict

**✅ M4 Backbone is structurally consistent with M3 Starter Pack conventions.** All required subsections are present. The two additions (Anti-Pattern Detection, UX Component Requirements) were missing and have been added. Structural expansions (two toys, separate Data Constraints section) are justified by M4's multi-toy architecture.
