# G3U4 M02 Working Notes — Representing Division (Drawings → Symbols → Expressions)

## Session Log

| Date | Session | Status | Notes |
|------|---------|--------|-------|
| 2026-04-08 | Task 1 | Complete | Initial extraction and Backbone draft. Source docs: Module Mapping M2 row, TVP M2 section, Important Decisions (all), Misconceptions (U4.2, A1 primary), M1 SP (§1.2, §1.3, §1.5, §1.9, §1.10). Gate 1: PASS WITH CONDITIONS. |
| 2026-04-08 | Task 2 | Complete | Warmup (§1.6) + Lesson (§1.7) drafted. Source docs: Warmup Playbook, Lesson Playbook, Guide vs Prompt Reference, Voice Design Reference, Template v3. R2/R5 applied. Gate 2 feedback applied: §1.7.4-§1.7.7 documentation sections added, PE1.3 consolidation note, D6.01 mode scope, D2.01 bridge, PE2.1 transition. New interaction 2.5 added (quotitive eq→display). 1.4 quotient changed (12÷2=6→16÷2=8). R3 skip removed (not engineered). |
| 2026-04-08 | Task 3 | Complete | EC (§1.8) + Practice Inputs (§1.8.5) + Synthesis (§1.9) + KDD (§1.10) drafted. Source docs: EC Playbook, Synthesis Playbook, Template v3, M1 SP (§1.8-§1.10). D8 formalized in KDD. R4 (EC.3 lower range) applied. Measurement contexts specified in Practice. M3 bridge in Synthesis closure. Gate 3: PASS WITH CONDITIONS — KDD format + KDD #16 applied. |
| 2026-04-08 | Task 4 | Complete | Assembly verified (1363 lines, §1.0-§1.10 in order, 16 KDDs in H3 format, version 04.08.26). Notion page created (ID: 33c5917e-ac52-8127-b5d5-eec70b45e8e9). Properties set: Name, Module Number=2, Unit=Unit 4, Status=Initial Draft, IM/OUR Lessons=[L3,L4,L5]. Full SP content pushed via incremental update_content operations (11 pushes). Note: some orphaned duplicate blocks remain at bottom of Notion page after END marker — requires manual cleanup in Notion (delete everything below "# END OF MODULE 2 STARTER PACK"). |
| 2026-04-08 | Gate 4 | Complete | Full L1 (8 checkers) + L2 (12 agents) evaluation. Verdict: PASS WITH CONDITIONS. Author triage applied — 6 fixes accepted, remaining findings rejected with rationale. See G3U4M02_Gate4_Evaluation.md §7 for full triage table. |
| 2026-04-08 | Post-Gate 4 Cleanup | Complete | **Template compliance fix:** Removed non-templated elements that the AI drafter added during Tasks 2-3 that do not appear in Template v3. Removed: (1) "Section X Data Summary" tables after each Lesson section, EC, and Synthesis — tables listing every problem's type/dividend/divisor/quotient/context, used as authoring aids for D2 balance tracking but not part of template structure; (2) "Section X Balance" blockquote annotations tallying partitive/quotitive balance per section; (3) "Division Type Balance" blocks in EC and Synthesis; (4) "S1→S2 Transition" and "S2→S3 Transition" prose blockquotes between sections. Replaced section transitions with template-standard `**→ SECTION X COMPLETE. PROCEED TO SECTION Y.**` markers (matching M01 SP pattern). Also applied: KDD-5 extended (AF3 deferral), KDD-17 added (2-worked-example rationale), KDD-2 extended (vocab bundling rationale), Int 2.2/2.3 Prompts tightened for independence, warmth bridge note removed (was part of non-templated S1→S2 block). **Root cause:** AI drafter generated balance/data tracking tables as inline authoring artifacts rather than keeping them in Working Notes. These should have been generated here in Working Notes or stripped at assembly. Flag for prompt refinement. |

---

## Cross-Reference Table A — Module Mapping Extraction

```
MODULE MAPPING: M2
====================
The One Thing: [Not a separate column — derived from Core Concept + Learning Goal]
Core Concept: Representing Division (Drawings → Symbols → Expressions)

OUR Source Lessons: L3 (partial), L4, L5 [OUR_Combined]
  L3 (partial): interpret and connect drawings to ÷ notation — concrete situations already established in M1; M2 picks up the representational/symbolic bridge
  L4: interpret ÷ expressions
  L5: write ÷ expressions

Learning Goals (Verbatim):
  L3: Interpret and relate drawings and descriptions of division situations. Understand that a division situation may involve finding an unknown number of groups or finding an unknown number of objects in each group.
  L4: Interpret division expressions. Understand that the same division expression can be used to represent both types of division situations.
  L5: Solve "how many groups?" and "how many in each group?" problems. Write division expressions to represent division situations.

Standards - Building On: M1 (both division types)
Standards - Addressing: 3.OA.A.2 (interpret quotients); 3.OA.A.3 (word problems)
Standards - Building Towards: 3.OA.B.6 (unknown factor)

Notes:
  Per SME: L3 concrete content absorbed into M1. M2 picks up L3's representational work (interpreting drawings, connecting to division expressions) which builds naturally into L4-L5. This makes L3-4-5 compression appropriate — students arrive at M2 with concrete division understanding already established.
  Module purpose (per SME): making meaning and connecting equations to pictures — building a solid foundation for visualizing and making sense of division. Students both INTERPRET and CREATE representations (not just select from options).
  CRA arc: Early = interpret AND create drawings of division situations using Equal Groups tool (bags/boxes/circles) → Mid = connect drawings to ÷ symbol, matching both directions (drawing → expression AND expression → drawing) → Late = write division expressions independently from word problems.
  Per D2 resolved: problems in M2 should maintain 50-50 partitive/quotitive balance. When students write expressions from word problems, ensure equal representation of both division types.
  Equations presented in nonstandard formats from the start (per D8 — presentation pattern, not true/false activities).
  Misconceptions targeted: U4.2 (partitive/quotitive confusion), A1 (dividend/divisor confusion)
  CRA: Concrete → early Representational
  Critical: Word problem contexts must include MEASUREMENT QUANTITIES alongside equal groups per 3.OA.A.3. Examples: "How many 4-centimeter pieces can you cut from 24 centimeters of ribbon?" (quotitive), "A recipe uses 3 cups of flour per batch. You used 18 cups. How many batches?" (quotitive), "You have 20 liters of juice to pour equally into 5 bottles. How many liters in each bottle?" (partitive). These are not new problem types — they are equal-groups/sharing problems with units attached. Include in Practice problems.

Vocabulary to Teach: ÷ (division symbol), division expression/equation, dividend, divisor (informal usage — deferred per SME), word problem (reinforce)

Question/Test Language: "What does 12 ÷ 3 mean?" "Write a division expression for this picture." "Does 20 ÷ 4 show sharing or grouping?"

Vocabulary Teaching Notes:
  The ÷ symbol is the major new notation. OUR L4-L5 introduce "division expression."
  Dividend/divisor are NOT formally named in OUR at this point — use "the total number" and "the number of groups / size of groups" instead.
  "Word problem" reinforced — students write expressions FROM word problem contexts.
  Key insight to reinforce: same expression represents BOTH division types.
  Per SME: defer dividend/divisor terminology — "too much to introduce here and doesn't add a lot of value right now." Keep focus on meaning-making, not formal naming. Informal language ("the total number," "the number of groups / size of groups") is sufficient and keeps cognitive load on the concept, not the labels.

Scaffolding of Visuals:
  Early: interpret AND create drawings of division situations. Students use Equal Groups tool (bags/boxes/circles) to build their own representations, not only select from options. Both directions: given a situation, create a drawing; given a drawing, describe the situation.
  Mid: connect drawings to ÷ expressions — match both directions (drawing → expression AND expression → drawing). Introduce ÷ symbol as notation for what they've been doing concretely.
  Late: given word problem, write expression independently. Key insight reinforced: same expression represents BOTH division types.

Key Misconceptions:
  U4.2 (partitive/quotitive confusion): Same expression for both types is conceptually hard.
  A1 (dividend/divisor confusion): Which number goes where in 12 ÷ 3? Focus on meaning, not position rules.

Component Balance Hypothesis: CONC 50% / PROC 30% / TRANS 20% — Bridge module.

Expected Struggles:
  Connecting a drawing to an expression requires abstract reasoning.
  Students may memorize "big number ÷ small number" as a rule rather than understanding what each position means.
  Reading ÷ expressions aloud correctly is a new skill.

SME Review Questions: [RESOLVED] Defer dividend/divisor. L3-4-5 compression is appropriate.
SME Review Answers: Defer dividend and divisor. Have this module be about making meaning and connecting equations to pictures. Students also need to create drawings (not just select). L3 split between M1 and M2 is appropriate.
```

---

## Cross-Reference Table B — TVP Extraction

```
TVP: MODULE 2 — Representing Division (Drawings → Symbols → Expressions)
=========================================================================
OUR Lessons 3 (partial), 4, 5 | Standards: 3.OA.A.2 (interpret quotients), 3.OA.A.3 (multiply/divide word problems)

Learning Goal: Interpret and relate drawings and descriptions of division situations. Interpret division expressions. Write division expressions to represent division situations.

Key Teaching Points:
  1. Division situations can be DRAWN — the Equal Groups tool lets students build their own representations (bags, boxes, circles with items)
  2. The ÷ symbol is a shorthand for what students have been doing concretely: "12 ÷ 3 means start with 12, make 3 equal groups"
  3. THE BIG INSIGHT: The same division expression (e.g., 20 ÷ 4) can represent BOTH division types. "Share 20 among 4 groups" AND "Measure out groups of 4 from 20" are both written 20 ÷ 4. The expression doesn't tell you which type — only the context does.
  4. Two-directional fluency: situation → drawing → expression AND expression → drawing → situation. Students must be able to go both ways.
  5. Students arrive with concrete division experience from M1 (both types, Equal Groups animations). M2 moves from watching to constructing.
  6. CRA Stage: Concrete → Representational bridge. Students still use Equal Groups with concrete contexts (bags/boxes) but now CREATE representations and connect them to symbolic notation.

Cognitive Focus:
  CREATE (Procedural) — constructing Equal Groups representations from word problems
  IDENTIFY (Conceptual) — recognizing what a ÷ expression means in context
  COMPARE (Conceptual) — understanding that one expression maps to both division types
  CONNECT (Transfer) — linking concrete representations to symbolic ÷ notation

Misconceptions Targeted:
  U4.2: Partitive/quotitive confusion (PRIMARY) — The same expression representing both types is genuinely hard. Students must see concrete examples where 20 ÷ 4 = 5 means both "share 20 into 4 groups, 5 each" AND "measure groups of 4 from 20, get 5 groups."
  A1: Dividend/divisor confusion (PRIMARY) — "Which number goes first?" Students default to "big number ÷ small number" as a rule. M2 counters by always grounding in meaning: "What's the total? That goes first."

PHASE-BY-PHASE FLOW:

WARM-UP — Callback to M1
  Equal Groups (Mode 3: Partitive, concrete bags) → System runs a brief partitive animation: 15 items shared into 3 bags, 5 each.
  Guide: "You know this — sharing 15 into 3 equal groups. 5 in each. Today you're going to learn how to DRAW situations like this yourself, and how mathematicians write them with a new symbol."
  Purpose: Reactivate M1 experience, preview both new skills (drawing + symbol).

LESSON

Early activities (Creating and interpreting drawings):
  Equal Groups (Stepper Mode — +/- controls for groups and items per group; numeric total ON) → Word problems presented. Student uses stepper controls to BUILD the division situation.
  Key beat — student construction through stepper, not observation: In M1, students watched animations. Now they actively adjust the stepper to BUILD the answer. Both steppers are free — the student must determine which quantity is known (groups or items per group) and set that stepper first, then adjust the other until total matches. This decision IS the division type identification, turning the M1 framing question into a tool interaction.
  Scaffolding: First 1–3 problems: guide explicitly bridges from the framing question to the tool ("What do you know — the groups or the items per group? You know 3 groups. Set the groups stepper to 3 first. Now adjust items per group until the total reaches 15."). Next 1–2 problems: guide asks the framing question but does not name the stepper — student must translate the question to tool action independently.
  Reverse direction also practiced: system displays completed arrangement, student describes what division problem it shows.
  4–5 problems. Mix of construct-from-situation and interpret-from-display. Both division types (~50-50 balance). Concrete contexts only (bags, boxes with pictures).

Mid activities (Introducing ÷ and connecting to drawings):
  Equal Groups (completed display) + Equation Builder (÷ tile now available)
  Key beat — first ÷ equation: Guide introduces the ÷ symbol alongside a familiar Equal Groups display. "15 ÷ 3 = 5." Connection lines animate from visual elements to equation parts (total → 15, groups → 3, per-group → 5). Read aloud: "15 divided by 3 equals 5."
  Student practices MATCHING in both directions: display → select equation, and equation → select display.
  Key beat — same equation, both types: Two different arrangements both represent 20 ÷ 4 = 5 (one partitive, one quotitive). Both shown simultaneously. "Same numbers, same equation — but the pictures look different. One is sharing, one is grouping. The expression works for both."
  4–5 matching problems across both directions.
  Starter Pack Note: For Practice/Exit Check, consider a multi-select format: "Given this equation, which stories could match it?" with 4 options — one correct partitive, one correct quotitive, and two distractors.

Late activities (Writing equations independently):
  Equation Builder (student constructs ÷ equations from word problems, no visual provided upfront)
  Full tile bank (numbers + ÷ + = + ?) with no pre-labeled slots — student constructs from scratch.
  Some problems show the Equal Groups visual as confirmation AFTER the student builds the equation.
  Final problem: student writes equation AND builds the Equal Groups representation for the same problem — full context → symbol → drawing loop.
  Remediation (per SME): If a student struggles, keep them building the equation — do not drop to stepper mode. Instead, link Equal Groups display to Equation Builder in real time: as the student places numbers in equation slots, the visual updates live.
  4–5 problems. Both division types. Numeric total OFF (available as remediation).

EXIT CHECK
  3 problems:
  1. Drawing → equation: Completed Equal Groups display → student builds matching ÷ equation. (Tests: visual-to-symbolic translation)
  2. Equation → drawing: ÷ equation shown, student selects matching display from options including a numbers-swapped distractor. (Tests: what each number in the equation represents — A1 check)
  3. Context → equation: Word problem only → student builds ÷ equation. (Tests: context-to-symbolic without visual scaffolding)

PRACTICE
  Mixed problems across all three translation directions
  Equation Builder + Equal Groups stepper both available
  Both division types balanced (~50-50)
  Error patterns to watch: consistently placing smaller number first (A1 signal); writing × expressions instead of ÷

SYNTHESIS
  Word problem + Equal Groups drawing + ÷ equation — all three representations visible simultaneously. "Three ways to show the same thing: a story, a picture, an expression/equation."
  Vocabulary consolidation: ÷ (division symbol), division expression/equation
  Bridge to M3: "You know that 3 × 5 = 15. And today you learned that 15 ÷ 3 = 5. Those look related. Tomorrow we'll explore WHY."

Scaffolding Progression:
  CRA Note: M2 is the concrete-to-representational bridge. Early activities are still concrete (students manipulate the Equal Groups tool with bags/boxes/pictures), but the cognitive demand shifts from experiencing division to representing it. Mid introduces symbolic notation (÷) alongside the concrete representations.

Toy Requirements:
  Numeric total toggle: The Equal Groups stepper displays a running total that updates in real-time as the student adjusts either stepper. This can be toggled on/off per problem:
  ON (default for Early): Student is trying to hit a target total — visible count is essential, not a crutch.
  OFF (Late, Exit Check): Student must reason about the total from the visual or from the word problem context. Toggled back ON as remediation if the student struggles.

Data Constraints:
  Dividends: 10–40 (expanded from M1's 10–30 range)
  Divisors: 2, 3, 4, 5, 6 (6 added — within familiar multiplication facts from Units 1-2)
  All problems divide evenly — no remainders
  Early (drawing creation): Dividends ≤ 24, divisors 2–4 (keep construction manageable)
  Mid (matching): Dividends ≤ 30, divisors 2–5 (comfortable range for matching)
  Late (expression writing): Dividends ≤ 40, divisors 2–6 (full range)
  Same-expression-both-types examples (Mid key moment): Use numbers where both readings are clean. 20 ÷ 4 = 5 works well (4 groups of 5 OR 5 groups of 4). 12 ÷ 3 = 4 likewise.
  Item types: Pictures in bags/boxes (Early), transition to circles with dots (Late) — gradual abstraction
  Container types: Bags, boxes (Early/Mid), circles (Late) — matching Equal Groups toy progression

Vocabulary:
  Introduced: ÷ (division symbol), division expression/equation
  Deferred (per SME): dividend, divisor — use "the total number" and "the number of groups" / "the number in each group" instead. Formal terms introduced in M3.
  Reinforced from M1: divide, equal groups, equal shares, share, group, partition
  Language pattern: "__ ÷ __ = __" read aloud as "[total] divided by [groups/group size] equals [result]"

TRANSITION IN (from M1):
  Pedagogical Shift: Observation → Construction → Representation
  What carries forward: Both division types, Equal Groups as primary tool, concrete contexts (bags/boxes/pictures), ~50-50 partitive/quotitive balance
  What's new: Student BUILDS representations (not just watches), ÷ symbol and division expressions/equations, Equation Builder enters the picture, two-directional translation (visual ↔ symbolic)
  Bridge: M1 Synthesis previewed "tomorrow you'll DRAW division situations and learn a new symbol." M2 Warm-up callbacks to M1's concrete experience.

TRANSITION OUT (to M3):
  What M2 establishes: Students can create Equal Groups representations, interpret and write ÷ expressions/equations, and translate between context/drawing/expression. The ÷ symbol is familiar. Students have seen (observationally) that one expression represents both division types.
  What M3 builds: THE inverse relationship — connecting ÷ to ×. "15 ÷ 3 = 5 is the same as ? × 3 = 15." Arrays as the unifying representation. Formal vocabulary (quotient, dividend, divisor). Unknown factor framing.
  Bridge: M2 Synthesis teases: "15 ÷ 3 = 5 and 3 × 5 = 15 look related. Tomorrow we'll explore WHY."
  Engineering note: M3 transitions from Equal Groups to Arrays as the primary tool. The groups-to-arrays bridge requires both tools on screen simultaneously for the opening of M3.

SME Resolutions:
  Stepper locking: RESOLVED — Both steppers free from the start. Students must determine which quantity is known and set that stepper first — this decision IS the division type identification.
  Same-expression-both-types: RESOLVED — Observation moment remains observational (not assessed in Mid). For later assessment use multi-select format.
  Expression writing without visual: RESOLVED — Standard Late: student writes equation, visual confirmation after. Remediation: linked display updates live as student places equation tiles.
  Abstraction progression: RESOLVED — Circles with dots appropriate within M2.
```

---

## Cross-Reference Table C — Conflict Log

```
CONFLICT LOG
============

#1
Field: Vocabulary to Teach
Module Mapping says: "÷ (division symbol), division expression/equation, dividend, divisor (informal usage — deferred per SME), word problem (reinforce)"
TVP says: "Introduced: ÷ (division symbol), division expression/equation. Deferred: dividend, divisor — use 'the total number' and 'the number of groups' / 'the number in each group' instead."
Discrepancy: Module Mapping lists "dividend, divisor (informal usage — deferred per SME)" which is ambiguous — are they taught informally or fully deferred? TVP is clear: deferred entirely, use positional language instead.
Resolution: Follow TVP — dividend/divisor are DEFERRED, not taught even informally. The Module Mapping's "informal usage" parenthetical is stale; the SME explicitly said "defer dividend and divisor" and the TVP reflects this resolution. Module Mapping also lists "word problem (reinforce)" which TVP doesn't list — include as reinforced vocabulary (not new).
Status: Resolved — TVP wins per resolution hierarchy rule #2 (TVP downstream, reflects SME resolutions)

#2
Field: Dividends range
Module Mapping says: No explicit range specified for M2
TVP says: "Dividends: 10–40 (expanded from M1's 10–30 range)"
Discrepancy: Module Mapping doesn't specify M2 ranges — only TVP does.
Resolution: Follow TVP — 10–40. Module Mapping's absence of ranges is expected (TVP is the tool/data authority).
Status: Resolved — TVP authoritative for data constraints

#3
Field: Divisors
Module Mapping says: No explicit divisor range for M2
TVP says: "Divisors: 2, 3, 4, 5, 6 (6 added — within familiar multiplication facts)"
Discrepancy: Module Mapping silent; TVP specifies.
Resolution: Follow TVP — {2, 3, 4, 5, 6}.
Status: Resolved

#4
Field: CRA Stage
Module Mapping says: "CRA: Concrete → early Representational"
TVP says: "CRA Stage: Concrete → Representational bridge"
Discrepancy: Minor wording — "early Representational" vs "Representational bridge."
Resolution: Essentially the same. Use "Concrete → Representational bridge" as TVP is more specific. The Module Mapping's "early" qualifier aligns with TVP's note that Early activities are still concrete.
Status: Resolved — no substantive conflict

#5
Field: Division type assessment approach
Module Mapping Question/Test Language says: "Does 20 ÷ 4 show sharing or grouping?"
TVP SME Resolution says: "Yes/no MC questions should not be used (binary guess). For later assessment use multi-select format."
Discrepancy: Module Mapping implies a binary sharing/grouping question. TVP explicitly resolves against binary MC for division type identification.
Resolution: Follow TVP — do NOT use binary sharing/grouping MC. Use the multi-select format recommended by SME for any division-type assessment. The "Does 20 ÷ 4 show sharing or grouping?" stem can be adapted into a multi-select: "Which stories could match 20 ÷ 4?" with both correct + distractors.
Status: Resolved — TVP wins (reflects SME resolution)

#6
Field: Equation format
Module Mapping says: "Equations presented in nonstandard formats from the start (per D8)"
TVP says: No explicit mention of nonstandard equation formats in M2 section
Discrepancy: Module Mapping references D8 for M2, but TVP doesn't specify nonstandard formats.
Resolution: D8 applies unit-wide. M2 introduces the ÷ symbol for the first time, so nonstandard formats (e.g., 5 = 15 ÷ 3) should appear naturally alongside standard format. However, M2's cognitive load is already high (new symbol + two-directional translation), so nonstandard formats should be LIGHT — perhaps 1–2 instances in Late or Synthesis, not the primary presentation format. Document as KDD if limiting nonstandard exposure in M2.
Status: Resolved — D8 applies but calibrated for cognitive load

#7
Field: Measurement quantity word problems
Module Mapping says: "Critical: Word problem contexts must include MEASUREMENT QUANTITIES alongside equal groups per 3.OA.A.3."
TVP says: No mention of measurement quantity word problems in M2 lesson section
Discrepancy: Module Mapping has a "Critical:" flag for measurement contexts but TVP doesn't include them in the lesson flow.
Resolution: The Module Mapping flag says "Include in Practice problems" — not necessarily in the Lesson. M2's Lesson focuses on the drawing→symbol→expression progression. Measurement quantity contexts (ribbon, flour, juice examples) belong in Practice Inputs (§1.8.5), not in the core Lesson interactions where the cognitive load is on tool manipulation and symbol introduction. Flag this in §1.8.5 Practice design at Task 3.
Status: Resolved — measurement contexts go in Practice per Module Mapping's own direction
```

---

## Design Constraints Extraction — Important Decisions

```
DESIGN CONSTRAINTS (from Important Decisions)
=============================================

Decision D1: Path Decision (Unified vs. Multi-Path)
  Rule: UNIFIED PATH with adaptive scaffolding intensity
  Applies to M2? YES
  What it constrains: Single instructional path through M2. Scaffolding intensity adapts (stepper scaffolding fades from guided to independent) but all students follow the same Drawing→Symbol→Expression arc.

Decision D2: Partitive/Quotitive Division Balance
  Rule: Both types from Day 1 with 50-50 balance. System flag at 45%, hard floor at 40%.
  Applies to M2? YES
  What it constrains: M2 problems must maintain 50-50 partitive/quotitive balance across Early (drawing), Mid (matching), Late (expression writing), EC, and Practice. Both types must appear in all phases.

Decision D3: Array Tool Design
  Rule: Extend Unit 1 Arrays tool, not new tool
  Applies to M2? NO — M2 uses Equal Groups tool, not Arrays. Arrays enter in M3.
  Note: M2's Equal Groups stepper mode IS the primary tool. Arrays are not used.

Decision D4: CRA Stage Progression (Simultaneous Connections)
  Rule: NOT strict sequential gates. Abstract appears alongside concrete.
  Applies to M2? YES
  What it constrains: The ÷ symbol (abstract) can appear alongside Equal Groups displays (concrete) in Mid activities. This is explicitly what the TVP designs: Mid shows the equation NEXT TO the visual, with connection lines. No need to "complete" concrete before introducing symbolic.

Decision D5: Properties Naming
  Rule: Commutative named informally; distributive/associative as strategies only
  Applies to M2? NO — Properties not addressed in M2.

Decision D6: Never "Add a Zero"
  Rule: Forbidden phrase
  Applies to M2? NO — Multiples of 10 not in scope.

Decision D7: Unknown Representation Scaffold (?→□→letter)
  Rule: ? in M1-M3, □ in M3-M4, letters in M10+. All interchangeable from M4.
  Applies to M2? PARTIAL
  What it constrains: M2 uses ? for any unknown representation. The TVP specifies the Equation Builder tile bank includes "?" along with numbers, ÷, and =. No □ or letters in M2.

Decision D8: Equals Sign as Presentation Pattern
  Rule: Nonstandard equation formats woven throughout. No standalone true/false activities.
  Applies to M2? YES
  What it constrains: When ÷ equations appear, occasionally present in nonstandard format (e.g., 5 = 15 ÷ 3). But M2 is the INTRODUCTION of ÷, so standard format (15 ÷ 3 = 5) should dominate. Nonstandard can appear lightly in Late/Synthesis. See Conflict Log #6.

Decision D9: Commutativity Non-Application to Division
  Rule: Test immediately after discovery in M5
  Applies to M2? NO

Decision D10: Multiplication Fluency Diagnostic Gate
  Rule: 80% accuracy threshold before M11
  Applies to M2? NO

Decision D11: L22 Optional Handling
  Rule: OPEN — Pending SME
  Applies to M2? NO

Decision D12: Bar/Tape Diagram Tool
  Rule: DEFERRED to Phase 6-7
  Applies to M2? NO

Decision D13: M4/M5 Split
  Rule: Original M4 split into M4 (fact families) + M5 (patterns/properties)
  Applies to M2? NO — Downstream only
```

---

## Author Flags

⚠️ **AUTHOR FLAG AF1 (Engineering):** The TVP specifies "connection lines animate from visual elements to equation parts" during the first ÷ equation introduction (Mid key beat). This animation type (element-to-equation mapping lines) was not used in M1 and may be a new visual state type requiring engineering confirmation. Flag per Known Pattern #44.

⚠️ **AUTHOR FLAG AF2 (Engineering):** The TVP specifies remediation where "Equal Groups display linked to Equation Builder in real time — as student places numbers in equation slots, the visual updates live." This real-time cross-tool linking is a significant engineering feature. Confirm buildability.

⚠️ **AUTHOR FLAG AF3 (Pedagogical):** The TVP's Late section specifies "Full tile bank (numbers + ÷ + = + ?) with no pre-labeled slots." The interaction type where students drag tiles to construct an equation from scratch is a construction interaction that may need a specific Student Action vocabulary term. Current standard terms include "Drag to build" — confirm this maps correctly to the Equation Builder tile-construction pattern.

---

## Edit Reconciliation Pass

```
EDIT RECONCILIATION
===================
The G3U4 TVP does not use numbered edits (unlike G3U2's Edit 83, 84, 88, 91 system).
SME resolutions are embedded inline as "RESOLVED per SME" blocks within the TVP text.

All SME resolutions affecting M2 have been verified against Table B extraction:

1. Stepper locking: RESOLVED — Both steppers free. 
   Reflected in Table B? YES — extracted verbatim.

2. Same-expression-both-types assessment format: RESOLVED — No binary MC; use multi-select.
   Reflected in Table B? YES — extracted under Mid and Starter Pack Note.

3. Expression writing remediation: RESOLVED — Keep building equation, link to visual.
   Reflected in Table B? YES — extracted under Late activities.

4. Circles with dots abstraction: RESOLVED — Appropriate within M2.
   Reflected in Table B? YES — noted in Data Constraints.

5. D7 revision (letters from M4, not M10): 
   Reflected in Table B? N/A for M2 — M2 uses ? only per original D7 (M1-M3). 
   The revision changes M4+ behavior, not M2.

6. D8 nonstandard equation formats:
   Reflected in Table B? PARTIAL — Module Mapping references D8 for M2 but TVP 
   doesn't explicitly show nonstandard formats in M2. See Conflict Log #6.
   Downstream impact: Light nonstandard format exposure in Late/Synthesis. 
   Document in KDD if limiting.

No edit-footnoted-but-not-applied issues found. The inline resolution format 
used by G3U4's TVP is cleaner than the numbered edit system — resolutions 
replace the original text rather than being appended as parentheticals.
```

---

## Data-Level Constraint Audit

```
DATA CONSTRAINT AUDIT
=====================

Applicable constraints for M2:
  - Dividends: 10–40 (phase-specific: Early ≤24, Mid ≤30, Late ≤40)
  - Divisors: {2, 3, 4, 5, 6} (phase-specific: Early 2–4, Mid 2–5, Late 2–6)
  - All problems divide evenly — no remainders
  - 50-50 partitive/quotitive balance (D2)
  - Same-expression-both-types examples: numbers where both readings are clean

Audit 1: TVP "same equation both types" example set
  Example: 20 ÷ 4 = 5 (TVP Mid key beat)
  Partitive reading: Share 20 among 4 groups → 5 each ✓
  Quotitive reading: Groups of 4 from 20 → 5 groups ✓
  Both readings produce whole numbers: ✓
  Within Mid constraints (dividend ≤30, divisor 2–5): ✓ (20 ≤ 30, 4 ∈ {2,3,4,5})
  No constraint violations.

Audit 2: TVP "same equation both types" second example
  Example: 12 ÷ 3 = 4
  Partitive reading: Share 12 among 3 groups → 4 each ✓
  Quotitive reading: Groups of 3 from 12 → 4 groups ✓
  Both readings produce whole numbers: ✓
  Within Mid constraints: ✓ (12 ≤ 30, 3 ∈ {2,3,4,5})
  No constraint violations.

Audit 3: TVP Warmup example
  Example: 15 ÷ 3 = 5
  Within data constraints: ✓ (15 in 10–40, 3 ∈ {2,3,4,5,6})
  Partitive (as specified): Share 15 into 3 bags, 5 each ✓
  Note: Same values as M1 W.2 (15÷3). Intentional callback — not a reuse concern.

Audit 4: EC value design (from TVP)
  EC.1: Drawing → equation (visual-to-symbolic). Values TBD at Task 3.
  EC.2: Equation → drawing with "numbers-swapped distractor" (A1 check). Values TBD.
  EC.3: Word problem → equation (context-to-symbolic). Values TBD.
  Constraint check: EC values must differ from Lesson values but stay within 
  M2 data constraints. Will audit fully at Task 3.

Audit 5: Phase-specific constraint coherence
  Early: Dividends ≤ 24, divisors 2–4
    Valid dividend/divisor/quotient triples: 
    10÷2=5, 12÷2=6, 12÷3=4, 12÷4=3, 14÷2=7, 15÷3=5, 16÷2=8, 16÷4=4, 
    18÷2=9, 18÷3=6, 20÷2=10, 20÷4=5, 21÷3=7, 24÷2=12, 24÷3=8, 24÷4=6
    Sufficient variety for 4–5 problems ✓

  Mid: Dividends ≤ 30, divisors 2–5
    Adds: 25÷5=5, 30÷5=6, 30÷3=10, 20÷5=4, 15÷5=3, 10÷5=2
    Plus all Early triples ✓
    Sufficient for 4–5 matching problems ✓

  Late: Dividends ≤ 40, divisors 2–6
    Adds 6 as divisor: 12÷6=2, 18÷6=3, 24÷6=4, 30÷6=5, 36÷6=6
    Plus: 28÷4=7, 32÷4=8, 35÷5=7, 40÷5=8, 36÷4=9, 40÷4=10
    Sufficient for 4–5 expression-writing problems ✓

No constraint violations found. Value pools are adequate for all phases.
```

---

## Section Plan

### Warmup (~1.5 min)
- **Type:** Activation (callback to M1 concrete experience)
- **Prior knowledge activated:** M1 partitive division with Equal Groups, framing question
- **Hook:** System replays a brief M1-style partitive animation (15 ÷ 3 = 5, bags with pictures). Familiar action, then Guide previews the shift: "Today you'll learn to DRAW these yourself and learn a new symbol."
- **Bridge target:** Transitions from "watching division happen" (M1) to "building and writing division" (M2)
- **Interaction count:** 1–2 (brief activation, not assessment)

### Lesson Section 1: Creating and Interpreting Drawings (~4–5 min)
- **CRA:** Concrete (student constructs with Equal Groups Stepper)
- **Focus:** Student builds division situations using stepper controls. Both steppers free — student determines known quantity. Both directions: word problem → build representation AND completed display → describe the division.
- **Major pedagogical move:** Shift from M1's OBSERVATION to M2's CONSTRUCTION. The framing question ("Do you know the groups or the items per group?") becomes a tool interaction — setting the correct stepper first IS identifying the division type.
- **Scaffolding:** Guided (Guide bridges framing question to stepper) → Independent (student translates on own)
- **Interaction count:** 4–5 (mix construct + interpret, ~50-50 P/Q)

### Lesson Section 2: Introducing ÷ and Connecting to Drawings (~4–5 min)
- **CRA:** Concrete → Representational bridge (D4: simultaneous connection)
- **Focus:** ÷ symbol introduced alongside completed Equal Groups displays. Equation Builder enters. Matching in both directions: display → equation AND equation → display.
- **Major pedagogical move:** Vocabulary introduction — ÷ symbol and "division expression" introduced AFTER concrete experience (Known Pattern #11). Key insight: same equation represents both division types (20 ÷ 4 = 5 shown with partitive AND quotitive arrangements).
- **Vocabulary introduced:** [vocab]÷[/vocab] (division symbol), [vocab]division expression[/vocab] / [vocab]division equation[/vocab]
- **Relational interaction:** Dedicated comparison showing two arrangements (one partitive, one quotitive) both matching the same equation. Guide states the pattern explicitly. Student confirms.
- **Direction order (R2):** First 1–2 matching problems = display→equation (easier: student reads familiar visual, selects new notation). Next 2–3 = equation→display or mixed (harder: decode new notation first). This scaffolds the new symbolic layer.
- **Interaction count:** 4–5 (matching problems, both directions)

### Lesson Section 3: Writing Expressions Independently (~3–4 min)
- **CRA:** Representational → early Abstract (expression construction from context alone)
- **Focus:** Student constructs ÷ equations from word problems using Equation Builder. No visual upfront — student reasons from context to symbol. Some problems show Equal Groups confirmation AFTER submission. Final problem closes the loop: context → equation → drawing.
- **Major pedagogical move:** Full representational independence. Visual scaffolding removed (or deferred to confirmation/remediation). Nonstandard equation format (D8) appears lightly.
- **Scaffolding:** Visual confirmation after → no confirmation → full loop (context ↔ symbol ↔ drawing)
- **Interaction count:** 4–5

### Exit Check (~2 min)
- **Skills assessed:** (1) Visual-to-symbolic translation, (2) Symbolic-to-visual with A1 distractor check, (3) Context-to-symbolic without visual scaffolding
- **Cognitive types:** CREATE (build equation), IDENTIFY (select matching display), CREATE (build equation from context)
- **Problem count:** 3
- **Note:** Module is M2 (early module range M1-3), so cognitive types restricted to CREATE/IDENTIFY per EC Playbook

### Practice (~distributed)
- **Format:** Mixed problems across all three translation directions (drawing↔equation, context→equation)
- **Tools available:** Equation Builder + Equal Groups stepper
- **Distribution:** ~50-50 partitive/quotitive, measurement quantity word problems included (per Module Mapping "Critical" flag)
- **Spiral review:** M1 skills (identifying quotients from Equal Groups animations)

### Synthesis (~2 min)
- **Task types:** (1) Real-world connection — triple representation visible simultaneously (story + drawing + equation); (2) Metacognitive reflection on strategy
- **Connections:** "Three ways to show the same thing: a story, a picture, an equation."
- **Vocabulary consolidation:** ÷, division expression/equation, reinforce all M1 terms
- **Closure/bridge:** "You know that 3 × 5 = 15. And today you learned that 15 ÷ 3 = 5. Those look related. Tomorrow we'll explore WHY." → sets up M3 inverse relationship
- **Interaction count:** 3–4

### Estimated Module Timing
| Phase | Est. Time |
|-------|-----------|
| Warmup | ~1.5 min |
| Lesson S1 | ~4–5 min |
| Lesson S2 | ~4–5 min |
| Lesson S3 | ~3–4 min |
| EC | ~2 min |
| Synthesis | ~2 min |
| **Total** | **~17–19.5 min** |

**Note:** Total is within the ~15–20 min range. If timing runs high, S1 can be trimmed from 5 to 4 problems (the reverse-direction "interpret from display" problems are lower-priority). The Phase-by-Phase flow from TVP specifies 4–5 per section, so 4 is acceptable.

---

## Dimension Tracking

| Interaction | Division Problem | Type | Dividend | Divisor | Quotient | Toy Mode | Notes |
|-------------|-----------------|------|----------|---------|----------|----------|-------|
| W.1 | 15 ÷ 3 = 5 | Partitive | 15 | 3 | 5 | Mode 3 (Partitive) | M1 callback — same as M1 W.2 |
| W.2 | (same display) | — | — | — | — | Mode 3 (static) | MC: identify unknown — activation |
| 1.1 | 12 ÷ 3 = 4 | Partitive | 12 | 3 | 4 | Stepper | Worked example (no action) |
| 1.2 | 24 ÷ 4 = 6 | Partitive | 24 | 4 | 6 | Stepper | Guided — explicit stepper bridge |
| 1.3 | 18 ÷ 3 = 6 | Quotitive | 18 | 3 | 6 | Stepper | Guided — framing Q only |
| 1.4 | 16 ÷ 2 = 8 | Quotitive | 16 | 2 | 8 | Stepper | Independent |
| 1.5 | 20 ÷ 4 = 5 | Partitive | 20 | 4 | 5 | Mode 3 (display) | Reverse: display → identify situation |
| 2.1 | 15 ÷ 3 = 5 | Partitive | 15 | 3 | 5 | Mode 3 + Eq Builder | Worked example — ÷ vocab intro |
| 2.2 | 24 ÷ 4 = 6 | Partitive | 24 | 4 | 6 | Display + Eq Builder | Display→equation (labeled slots) |
| 2.3 | 18 ÷ 3 = 6 | Quotitive | 18 | 3 | 6 | Display + Eq Builder | Display→equation (quotitive) |
| 2.4 | 20 ÷ 4 = 5 | Both | 20 | 4 | 5 | Mode 3+4 side-by-side | KEY: same expression, both types |
| 2.5 | 30 ÷ 5 = 6 | Quotitive | 30 | 5 | 6 | Displays (MC select) | Equation→display quotitive, applies 2.4 insight |
| 2.6 | 12 ÷ 3 = 4 | Partitive | 12 | 3 | 4 | Displays (MC select) | Equation→display partitive, A1 distractor |
| 3.1 | 30 ÷ 5 = 6 | Partitive | 30 | 5 | 6 | Eq Builder (full) | Word problem → expression + visual confirm |
| 3.2 | 28 ÷ 4 = 7 | Quotitive | 28 | 4 | 7 | Eq Builder (full) | Word problem → expression, no confirm |
| 3.3 | 36 ÷ 6 = 6 | Partitive | 36 | 6 | 6 | Eq Builder (full) | Independent |
| 3.4a | 20 ÷ 4 = 5 | Quotitive | 20 | 4 | 5 | Eq Builder (full) | Loop: expression step |
| 3.4b | 20 ÷ 4 = 5 | Quotitive | 20 | 4 | 5 | Stepper (circles/dots) | Loop: construction step |
| EC.1 | 15 ÷ 3 = 5 | Quotitive | 15 | 3 | 5 | Display + Eq Builder | Visual→equation, circles/dots |
| EC.2 | 21 ÷ 3 = 7 | Partitive | 21 | 3 | 7 | Displays (MC select) | Equation→display, A1 distractor |
| EC.3 | 18 ÷ 3 = 6 | Partitive | 18 | 3 | 6 | Eq Builder (full) | Context→equation, no visual, R4 lower range |
| S.1 | 25 ÷ 5 = 5 | Quotitive | 25 | 5 | 5 | Display + text | Triple representation match |
| S.2 | 30 ÷ 6 = 5 | Both | 30 | 6 | 5 | Text only | D8 nonstandard (5 = 30 ÷ 6) |
| S.3 | 24 ÷ 4 = 6 | — | 24 | 4 | 6 | Display (split) | Tool preference reflection |

**Division Type Balance (assessed interactions only):**
- S1: 2P (1.2, 1.5) / 2Q (1.3, 1.4) = **50-50**
- S2: 2P (2.2, 2.6) / 2Q (2.3, 2.5) / 1 Both (2.4) = **50-50** (both-types counted as neutral)
- S3: 2P (3.1, 3.3) / 2Q (3.2, 3.4) = **50-50**
- **Lesson total: 7P / 6Q / 1 Both = 50-43-7% → within D2 tolerance**

**Data Range Compliance:**
- S1 (Early ≤24, div 2-4): ✅ All values comply (max dividend 24, divisors {2,3,4})
- S2 (Mid ≤30, div 2-5): ✅ All values comply (max dividend 30, divisors {3,4,5})
- S3 (Late ≤40, div 2-6): ✅ All values comply (max dividend 36, divisors {4,5,6}). 3.2 changed from 24÷4=6 to 28÷4=7 for quotient variety.

---

## Gate Review Log

## Backbone Self-Check Results

| # | Check Item | Result | Notes |
|---|-----------|--------|-------|
| 1 | Every Table A "Vocabulary to Teach" term in §1.2 or §1.3 | ✅ PASS | ÷, division expression/equation taught; dividend/divisor deferred; word problem reinforced |
| 2 | Every Table A "Vocabulary to Avoid" in §1.3 Terms to Avoid | ✅ PASS | Complete alignment with M1 deferred list |
| 3 | Module Mapping "Critical:" flags addressed | ✅ PASS | Measurement contexts flagged for §1.8.5 Practice |
| 4 | Question/Test Language stems addressed | ✅ PASS | Stems 1-2 addressed; stem 3 resolved to multi-select per Conflict #5 |
| 5 | Misconception IDs match database | ✅ PASS | U4.2, A1 both present with correct IDs |
| 6 | Every TVP data constraint in §1.5 | ✅ PASS | Exact alignment across all phases |
| 7 | Every Conflict Log entry resolved or flagged | ✅ PASS | All 7 conflicts resolved |
| 8 | Every applicable Important Decision in SP | ✅ PASS | D1, D2, D4, D7, D8 all reflected |
| 9 | Conceptual Spine confirms M2 placement | ✅ PASS | Both division types "Where Developed" at M2 |
| 10 | Standards Mapping required vocabulary aligns | ✅ PASS | All 3.OA.A.2/A.3 terms addressed; quotient handled per SME |
| 11 | The One Thing references only M2 concepts | ✅ PASS | No forward-looking concepts |
| 12 | YAML front matter complete | ✅ PASS | All fields present |
| 13 | Edit Reconciliation complete | ✅ PASS | No numbered edits in G3U4 TVP; inline resolutions verified |
| 14 | Data Constraint Audit complete | ✅ PASS | All example sets checked; value pools adequate |
| 15 | Backbone-to-extraction diff | ✅ PASS | All TVP phase-by-phase beats accounted for in §1.5 or §1.1 |
| 16 | Problem/interaction counts cross-checked | ✅ PASS | TVP 4-5 per section reflected in Section Plan |

---

### Gate 1 Review
| # | Location | Issue (author feedback) | Resolution | Pattern? |
|---|----------|------------------------|------------|----------|
| R1 | Conflict Log #6 / §1.10 | D8 nonstandard equation format calibration ("from the start" in MM vs "Late/Synthesis only" in SP) is pedagogically sound but needs formal KDD documentation, not just Conflict Log reasoning. | Add KDD at Task 3 §1.10: "D8 nonstandard formats limited to Late/Synthesis in M2 — cognitive load from new ÷ symbol + Equation Builder + two-directional translation makes M2 the wrong place for aggressive nonstandard exposure. Module Mapping's 'from the start' is a unit-level directive; M2 calibrates locally." | NEW? |
| R2 | Section Plan S2 | S2 matching direction order not specified. First 1-2 matching problems should be display→equation (easier: student reads familiar visual, selects new notation) before equation→display (harder: decode new notation). | Update Section Plan and enforce at Task 2 scripting: S2 first 2 problems = display→equation, next 2-3 = equation→display (or mixed). Document in S2 Section Plan. | — |
| R3 | Section Plan S3 | S3 "final loop problem" (context→equation→drawing) is a three-step cognitive chain. If student is struggling on earlier S3 problems, they'll hit the loop in remediation mode. Needs explicit skip-if-in-remediation note. | ~~REMOVED~~ — Conditional interaction skipping is not engineered. The three-step chain (3.4a→3.4b) stands for all students. Pipeline handles remediation within each sub-step. | — |
| R4 | §1.8 (Task 3) | EC.3 (word problem→equation, no visual) is highest-demand item. Word problems should use lower end of Late data range (dividends 10-24, divisors 2-4) to avoid confounding conceptual assessment with computational difficulty. | Flag for Task 3 EC design: EC.3 values from lower Late range. Document rationale in EC Parameters. | — |
| R5 | §1.1.1 Standards | Module Mapping "Building Towards" may include 3.OA.C.7 (fluently multiply and divide within 100). SP lists only 3.OA.B.6. | 3.OA.C.7 is not in the workbook's Standards Mapping sheet (which covers 3.OA.A.2, A.3, A.4, B.5, B.6, D.8, D.9 and 3.MD.C.7). Add 3.OA.C.7 to Building Toward as it's the broader fluency standard M2 contributes to. | — |

### Gate 3 Review (L1 + L2)

**L1:** 0 CRITICAL, 0 genuine MAJOR (2 V4 false positives), 29 MINOR (all accepted).
**L2:** 8 agents ran. Key findings and resolutions:

| # | Location | Issue | Resolution | Pattern? |
|---|----------|-------|------------|----------|
| G3.1 | §1.10 KDD format | KDD entries as numbered list, not H3 headings per Structural Skeleton | FIXED — Converted all 15 entries to `### KDD-N:` H3 format | — |
| G3.2 | §1.9 S.1 | Type D (Representation Transfer) used in Synthesis for early module; Playbook §3C prefers Type A + C | FIXED — Added KDD-16 documenting pedagogical override: M2's core work IS representation transfer | — |
| G3.3 | §1.6 W.3 | "write this down without drawing" risks visual-abandonment interpretation | FIXED — Changed to "write this down that goes with your pictures" | — |
| G3.4 | §1.8 EC.3 On Correct | 13 words (target 5-10) | FIXED — Trimmed to 10 words: "You divided 18 into 3 equal groups." | — |
| G3.5 | §1.8 EC divisors | All 3 EC items use divisor 3 | ACCEPTED — Playbook doesn't mandate divisor variety; documented as note | — |
| G3.6 | V4 "divide" in EC | L1 checker flagged as MAJOR | FALSE POSITIVE — "divide"/"divided" present in EC dialogue inside [vocab] tags; checker doesn't parse them | V4 tag parsing |
| G3.7 | V4 "quotient" in EC | L1 checker flagged as MAJOR | ACCEPTED FALSE POSITIVE — M2 defers "quotient" to M3 per §1.2 Scope Boundaries | — |

**Post-Gate 3 author feedback (applied):**

| # | Location | Issue | Resolution | Pattern? |
|---|----------|-------|------------|----------|
| G3.8 | §1.7.3 Interaction 3.2 | S3 quotient-6 concentration: 3.1, 3.2, 3.3 all yield 6 — recreates the issue KDD-8 fixed in S1 | FIXED — Changed 3.2 from 24÷4=6 to 28÷4=7. S3 quotient sequence now 6, 7, 6, 5. KDD-8 updated to cover module-wide quotient variety. | — |
| G3.9 | §1.8.5 Cross-Module | M1 spiral content in Practice not appropriate — M1 skills are prerequisites, not spiral targets | FIXED — Removed M1 skill references. Practice stays within M2's S1–S5. | — |
| G3.10 | §1.10 KDD-15 | "feedback memory: no spec tables" is an internal process reference | FIXED — Changed to "Consistent with M1 SP convention." | — |
| G3.11 | §1.8.5 Data ranges | Lesson over-indexes on divisor 3 (10/21) and quotient 6 (10/21); Practice needs to compensate | FIXED — Added coverage note to Practice data ranges directing system to increase divisor 5/6 and vary quotients. | — |
| G3.12 | §1.8 EC divisors | All 3 EC items use divisor 3 | ACCEPTED — Tests translational skill, not computational breadth. 3 problems can't cover everything. Documented. | — |

