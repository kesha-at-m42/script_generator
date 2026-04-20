# MODULE 5: Multiplication Table Patterns & Properties

**Version:** 2026-04-10

```
---
module_id: M05
unit: 4
domain: operations_algebraic_thinking
primary_toys:
  - name: "Arrays"
    notion_url: "https://www.notion.so/Arrays-1395917eac5280e5a0b3f06e5f6e23a4"
  - name: "Multiplication Tables Grid"
    notion_url: "https://www.notion.so/Multiplication-Tables-Grid-1395917eac52801da8e3d35eb2e6ca3e"
secondary_toys:
  - name: "Equation Builder"
    notion_url: "https://www.notion.so/Equation-Builder-2fc5917eac52803f8604f47c62304ee7"
interaction_tools:
  - "Click/Tap (array observation, MC selection, table cell selection)"
  - "Select (single) (table cell clicks for commutative partner discovery)"
  - "Select (multiple) (W.1 paired equation selection, 2.5 commutative partner pairs)"
---
```

---

# BACKBONE

---

## 1.0 THE ONE THING

**[REQUIRED]**

Switching the order of factors in multiplication always produces the same product (3 × 5 = 5 × 3) — this is the commutative property — but switching the order in division does NOT work (12 ÷ 4 ≠ 4 ÷ 12), so order matters for division even though it doesn't matter for multiplication.

**CRA Stage:** Abstract (with representational grounding through arrays). The multiplication table is a symbolic representation, but the array rotation animation connects it to the concrete/representational work from M3–M4. Students move between arrays (representational) and the table (abstract) throughout.

**Critical Misconception:** A3 — Overgeneralizing commutativity to division. Students learn "order doesn't matter for multiplication" and naturally assume the same applies to all operations. The entire Late section is designed around surfacing and refuting this overgeneralization through concrete testing.

**Biggest Risk:** Students memorize "order doesn't matter for multiplication" as a rule without understanding WHY (the array rotation proof), OR they become confused about whether multiplication really IS commutative after discovering division isn't (secondary uncertainty — overcorrection from the A3 discovery). The paired discovery structure (works for ×, then immediately tested and fails for ÷) must land as a coherent contrast, not as two disconnected facts.

**Success Indicator:** Given an array (e.g., 4 × 6), the student can explain that rotating it produces 6 × 4 with the same total, identify the commutative partner in the multiplication table, AND correctly state that switching the order does NOT work for division (e.g., 24 ÷ 4 ≠ 4 ÷ 24) with a concrete reason ("you can't share 4 among 24 groups and get a whole number").

---

## 1.1 LEARNING GOALS

**[REQUIRED]**

*Verbatim — Script Must Achieve These*

**L9 (narrowed per SME):** Recognize that multiplication is commutative. Discover that division is NOT commutative. Use the multiplication table to see the commutativity pattern (symmetry across diagonal).

**Module Goal (Student-Facing):** "You'll discover why switching the order works for multiplication — and find out what happens when you try it with division."

**Exit Check Tests:** (1) Commutativity recognition through an array, (2) table symmetry connection, (3) non-commutativity of division identification.

### Standards Cascade

| Role | Standard | Description |
| :---- | :---- | :---- |
| **Addressing** | 3.OA.D.9 | Identify arithmetic patterns (including patterns in the multiplication table), and explain them using properties of operations. |
| **Addressing** | 3.OA.B.5 | Apply properties of operations as strategies to multiply and divide. |
| **Building On** | M4 | Fact families — students have been writing commutative pairs (3 × 5 = 15 and 5 × 3 = 15) without examining why both work. |
| **Building On** | Units 1–2 | Multiplication table introduction, "turn-around facts" (Unit 1 M12). |
| **Building Toward** | 3.OA.C.7 | Fluently multiply and divide within 100 — commutativity halves the unique facts to learn. |
| **Building Toward** | M6 | Area model decomposition strategies — multiplication table helps students see WHY decomposition works. |

### Module Bridges

| Direction | Content |
| :---- | :---- |
| **From M4** | Students arrive with fact families as a systematic tool. They can produce all four equations from an array, given fact, or unknown-factor equation. Think-multiplication is a named strategy. All three unknown representations (?, □, letter) are used interchangeably. Students have been writing commutative multiplication pairs in every fact family without examining WHY both give the same answer. |
| **This Module (M5)** | Surface the commutativity pattern students have been using implicitly. Prove it through array rotation (same dots, same total). See it at scale in the multiplication table (symmetry across diagonal). Then test whether it applies to division — discover that it does NOT. Name the property informally: "order doesn't matter for multiplication." |
| **To M6** | Students leave understanding that multiplication is commutative (order doesn't matter) and division is not (order does matter). M6 uses the multiplication table as a reference while introducing area model decomposition strategies. The table connection (commutative pairs = same product) supports the distributive property discovery in M6. |

### OUR Lesson Sources

| OUR Lesson | Scope | Transformation |
| :---- | :---- | :---- |
| L9 | Arithmetic patterns in multiplication table, commutativity, properties of operations | Reframed per SME: NARROWED to commutativity discovery + non-commutativity of division only. Table pattern exploration (skip-counting, even/odd, multiples) already covered in Units 1–2. Decomposition-based table strategies deferred to M6. |

---

## 1.2 SCOPE BOUNDARIES

**[REQUIRED]**

### ✅ Must Teach

* Commutativity of multiplication proven visually through array rotation (3 × 5 array rotated 90° becomes 5 × 3 — same dots, same total)
* Commutativity named informally: "order doesn't matter for multiplication" — with light formal term: "Mathematicians call this the commutative property" (per D5: informal naming, CCSS says students need not use formal terms)
* Multiplication table symmetry: commutative pairs have the same value, table is symmetric across the diagonal
* Active discovery of table symmetry: student finds commutative partner cells ("turn-around facts" in the table)
* Reverse-direction table discovery: given a product, identify the factor pairs that produce it (per SME addition)
* Non-commutativity of division discovered IMMEDIATELY after commutativity is established (per D9): "Does 12 ÷ 4 = 4 ÷ 12?" — tested concretely, students experience the failure
* Paired contrast as the conceptual core: multiplication IS commutative, division is NOT
* "Arithmetic pattern" reinforced as 3.OA.D.9 standards language
* All reinforced vocabulary used naturally: multiplication table, row, column, pattern, arithmetic pattern, fact family, array, factor, product, equation, multiply, divide
* Unknown representations (?, □, letter) in Practice per D7 cumulative flexibility

### ❌ Must Not Include

* Table pattern exploration beyond commutativity — skip-counting patterns, even/odd, multiples (Units 1–2 — already covered)
* Decomposition-based table strategies — using known facts to derive unknown facts (M6 — needs area model support)
* Distributive property (M6+, per D5)
* Associative property (M6+, per D5)
* Formal property terminology as required student vocabulary — students are NOT assessed on "commutative property" (per CCSS note in D5)
* Division with remainders (all M5 divisions exact where applicable)
* Think-multiplication as a formal strategy (M4 named it; M5 reinforces implicitly through commutativity — M12 is full assessment)
* Two-step word problems (M10+)
* Area models (M6+)
* New unknown representations (all three already introduced by M4)

⚠️ **NARROWED SCOPE (D13 + SME):** M5 exists from the D13 split of the original M4. Andrea explicitly directed: "focus this module only on the commutative property (and absolutely connecting to division isn't commutative)." All other L9 content is addressed elsewhere in the unit or in other units.

### Scope Confirmation Checklist

- [x] Concepts IN scope: commutativity (×), non-commutativity (÷), table symmetry
- [x] Concepts deferred: decomposition strategies (M6), other table patterns (Units 1–2), formal property names as assessed vocabulary (CCSS)
- [x] Vocabulary introduced: commutative (informal only)
- [x] Vocabulary reinforced: multiplication table, row, column, pattern, arithmetic pattern, fact family, array, factor, product
- [x] Vocabulary forbidden: distributive, associative (M6+)
- [x] Value constraints: factors 2–7 for array proofs, avoid squares; fluent facts first for table; swapped division pairs must produce non-whole results
- [x] Both × and ÷ situations present (but ÷ only in Late non-commutativity section)
- [x] OUR L9 = sole lesson source, reframed per SME
- [x] Scope boundaries: M4 covers inverse relationship/fact families; M5 covers commutativity/table patterns; M6 covers area models/decomposition

---

## 1.3 VOCABULARY ARCHITECTURE

**[REQUIRED]**

**Assessment Vocabulary (appears on state test):** pattern, arithmetic pattern, multiplication table, commutative (per 3.OA.B.5 — though CCSS states students need not use formal property names)

### Vocabulary Staging by Phase

| Phase | Terms | Introduction Approach |
| :---- | :---- | :---- |
| **Warmup** | fact family (established M4), multiply, divide, equation, array | Activation only — no formal introduction. All terms established in M3–M4. |
| **Lesson S1 (Early)** | [vocab]commutative[/vocab] (NEW — informal: "order doesn't matter for multiplication") | Introduced AFTER array rotation proof provides visual grounding. Light formal term after multiple examples: "Mathematicians call this the commutative property." Follows vocab-after-grounding rule. |
| **Lesson S2 (Mid)** | multiplication table, row, column, pattern (all reinforced from Units 1–2) | Used naturally during table navigation. "Arithmetic pattern" reinforced as 3.OA.D.9 language when the table diagonal is identified. |
| **Lesson S3 (Late)** | (no new terms — [vocab]commutative[/vocab] reinforced through contrast) | "Order doesn't matter for multiplication" compared to "order DOES matter for division." Commutative property reinforced by contrast with non-commutativity. |
| **EC** | (all terms — assessment context) | Students use terms to explain commutativity and identify non-commutativity. |
| **Practice** | (all terms) | Used in problem contexts. |
| **Synthesis** | (all terms — consolidation) | Side-by-side summary. Bridge to M6 mentions "multiplication table." |

### Vocabulary Reinforcement Plan (NEW/status-change terms only)

| Term | Introduction Interaction | Reinforcement Target (≥50% of remaining) |
| :---- | :---- | :---- |
| commutative | S1 (after rotation proof, ~Interaction 1.3–1.4) | Guide dialogue in S2, S3, EC, Synthesis — all remaining phases |

> **Vocab Tag Policy (v4.7):** Only "commutative" gets `[vocab]` markup as the sole NEW term. All other terms (fact family, array, multiplication table, row, column, pattern, arithmetic pattern, factor, product, multiply, divide, equation, quotient, dividend, divisor) are ESTABLISHED from prior modules and appear untagged.

### Terms to Avoid (Save for Later Modules)

* distributive (M6 — area models provide conceptual support, per D5)
* associative (M6+ — implicit in multiples-of-10 reasoning, per D5)
* "add a zero" (NEVER — per D6)

---

## 1.4 MISCONCEPTIONS

**[REQUIRED]**

### 1.4.1 A3: Overgeneralizing Commutativity to Division (PRIMARY)

**Trigger Behavior:** Student claims 12 ÷ 4 = 4 ÷ 12, or states "it doesn't matter which order" for all operations. When challenged, may try to compute 4 ÷ 12 and become confused because it doesn't yield a whole number. May write fact families with extra "reversed division" equations. In MC format, may select swapped division expression as equivalent.

**Why It Happens:** Students learn 3 × 5 = 5 × 3 and naturally assume all operations work the same way. Addition and multiplication (the two operations students know well) are both commutative, creating an expectation that commutativity is universal. This is a correct identification of a pattern applied too broadly — the misconception comes from the overgeneralization, not from poor reasoning.

**Visual Cue:** Arrays make the non-commutativity of division concrete: a 12-dot array CAN be read as 12 ÷ 4 = 3 (4 columns, 3 dots each), but a 4-dot arrangement CANNOT be read as 4 ÷ 12 = anything whole. The impossibility is visual and physical, not just numerical.

**Prevention Strategy:** The entire Late section (S3) is designed as a discovery experience. After establishing commutativity for multiplication through multiple array proofs and table symmetry, the Guide poses: "Does this work for division too?" Students test 2–3 division pairs and discover the answer is NO. The paired structure (works for ×, then immediately fails for ÷) ensures the contrast is salient. Per D9: this discovery happens DURING the lesson while both results are cognitively active, not deferred to Synthesis. Frame as investigation, not correction.

---

### 1.4.2 A4: Associative Interference in Fact Recall (SECONDARY)

**Trigger Behavior:** Student answers 6 × 8 = 42 (confusing with 6 × 7) or 7 × 8 = 54 (confusing with 9 × 6). Errors cluster around facts with shared operands or nearby products. May self-correct after a pause.

**Why It Happens:** Similar multiplication facts compete in memory. The 6, 7, 8, and 9 tables dominate the hardest facts because they share operands and have nearby products. This is a retrieval error, not a conceptual gap.

**Visual Cue:** The multiplication table itself shows these facts in adjacent cells, which can reinforce confusion if confusable facts are presented back-to-back. Deliberate sequencing avoids this.

**Prevention Strategy:** When navigating the multiplication table in S2, avoid placing confusable facts in adjacent activities. Use the interference research ordering: start with 2s, 5s, 10s (high fluency, low interference); extend to 3s, 4s (moderate); reserve 6s–9s for later table interactions where the commutative pattern is already established. This is a data constraint, not an instructional strategy — the A4 prevention is built into the interaction sequencing, not into the teaching.

---

## 1.5 TOY SPECIFICATIONS

**[REQUIRED]**

### 1.5.1 Arrays

**Notion Spec:** [Arrays](https://www.notion.so/Arrays-1395917eac5280e5a0b3f06e5f6e23a4)
**Changes from M4:** M4 used arrays for fact family production (student-specified construction, display with equation overlay, array-on-demand toggle). M5 uses arrays for rotation proof (rotation animation, existing from Unit 1 M12) and Non-Commutativity of Division Discovery mode (new capability per toy spec). No student construction — arrays are system-displayed and manipulated.

**Module Configuration (M5)**

| Aspect | This Module |
| :---- | :---- |
| **Mode — Rotation Proof (S1)** | Dot array displayed at specified dimensions, then system-animated 90° rotation. Equation overlay shows both readings (pre- and post-rotation). |
| **Mode — Non-Commutativity Discovery (S3)** | Dot array displayed for original division, then system attempts the swapped division visually — dots cannot be arranged into the specified groups. Shows the failure concretely. |
| **Factors** | 2–7 (visual clarity). Avoid squares (rotation of a square is visually identical). |
| **Interaction** | Student observes rotation animation → confirms via MC. Student observes non-commutativity attempt → confirms via MC. No student construction of arrays in M5. |

**M5 Guardrails**

| DO | DO NOT |
| :---- | :---- |
| Use arrays with clearly different row/column counts (3×5, 2×7, 4×6) | Use square arrays (4×4, 5×5) — rotation is visually identical |
| Show equation overlay alongside array for both readings | Show arrays without equations (the equation connection is the point) |
| Use Non-Commutativity Discovery mode per toy spec for S3 | Create ad-hoc "failed division" animations outside the spec |
| Keep array dimensions within factors 2–7 | Use factors >7 where dot arrays become hard to count visually |

**Progression Within M5**

| Phase | Configuration |
| :---- | :---- |
| **Warmup** | Not used (Equation Builder displays the fact family) |
| **Lesson S1 (Early)** | Rotation Proof mode — 3×5, 2×7, 4×6. System displays array, animates rotation, shows both equations. |
| **Lesson S2 (Mid)** | Not primary (Multiplication Tables Grid is the primary tool). Arrays may appear in Design Notes as conceptual reference. Student role: Active discoverer — finds commutative partners in the table (per TVP scaffolding). |
| **Lesson S3 (Late)** | Non-Commutativity Discovery mode — 12÷4 vs 4÷12, 20÷5 vs 5÷20. System shows original division reading, then attempts swapped version. |
| **EC** | EC.1 uses Arrays in Rotation Proof mode (rotation animation present — student observes rotation, then confirms product via MC). EC.3 uses Non-Commutativity Discovery mode for division testing. |
| **Synthesis** | Display only — side-by-side reference for the × vs ÷ contrast. |

---

### 1.5.2 Multiplication Tables Grid

**Notion Spec:** [Multiplication Tables Grid](https://www.notion.so/Multiplication-Tables-Grid-1395917eac52801da8e3d35eb2e6ca3e)
**Changes from M4:** Not used in M4. Familiar to students from Units 1–2. M5 adds guided-highlighting interaction for commutative partner discovery and diagonal symmetry observation.

**Module Configuration (M5)**

| Aspect | This Module |
| :---- | :---- |
| **Grid size** | 10×10 (standard, familiar from Unit 2) |
| **Highlighting** | Guide-controlled cell highlighting to draw attention to specific cells. Student clicks cells to select commutative partners. Diagonal highlighted as a structural feature. |
| **Interaction** | Student selects cells (Select (single) — click the commutative partner). Guide narrates the pattern. |
| **Products displayed** | Full table visible. No hidden/masked cells. |

**M5 Guardrails**

| DO | DO NOT |
| :---- | :---- |
| Highlight cells students are fluent with first (2s, 5s, 10s) then extend | Start with 6s–9s (high interference zone, per A4) |
| Highlight the diagonal as a structural feature after partner discovery | Treat diagonal as a separate teaching target — it's evidence for commutativity, not its own concept |
| Allow table to remain visible as reference during Practice | Remove table access during assessment (EC) — EC tests commutativity through arrays and expressions, not table navigation |

**Progression Within M5**

| Phase | Configuration |
| :---- | :---- |
| **Warmup** | Not used |
| **Lesson S1 (Early)** | Not used (arrays are the primary tool for S1) |
| **Lesson S2 (Mid)** | PRIMARY tool. Guide-highlighted cells → student finds partner → diagonal observation. 3–4 "find the turn-around fact" interactions + 1–2 "find factor pairs for this product" reverse-direction interactions. |
| **Lesson S3 (Late)** | Not used (arrays return for division non-commutativity) |
| **EC** | EC.2 uses the table (two highlighted cells, commutative pair — student identifies WHY they have the same value) |
| **Practice** | Available as reference tool throughout |
| **Synthesis** | May appear in side-by-side summary alongside array |

---

### 1.5.3 Equation Builder (Secondary — Display Only)

**Notion Spec:** [Equation Builder](https://www.notion.so/Equation-Builder-2fc5917eac52803f8604f47c62304ee7)
**Changes from M4:** M4 used Equation Builder interactively (?, □, letter tiles for fact family construction). M5 uses Equation Builder in DISPLAY ONLY mode — showing equations alongside arrays and table cells. No student tile manipulation.

> **SP Note (CA-3):** The Toy Flow lists Equation Builder as "equation mode (Late)" with "student builds for division testing." Resolution: The TVP's label refers to the Equation Builder DISPLAYING equation content during S3 division testing, not student-interactive equation building. In S3, the student interaction occurs on the Arrays toy (Non-Commutativity Discovery mode) and MC confirmation. Equation Builder remains display-only throughout M5.

**Module Configuration (M5)**

| Aspect | This Module |
| :---- | :---- |
| **Mode** | Display only — no student interaction with Equation Builder tiles |
| **Content** | Shows multiplication equations alongside arrays (S1), shows fact family equations (Warmup), shows division equations alongside arrays (S3) |
| **Format variety** | Per D8: include nonstandard formats (15 = 3 × 5, 15 = 5 × 3) naturally alongside standard formats |

**M5 Guardrails**

| DO | DO NOT |
| :---- | :---- |
| Display equations in varied formats per D8 | Require student to build equations (display only in M5) |
| Show both commutative multiplication equations side by side | Show equations without the paired visual (array or table) |

---

### 1.5.4 Data Constraints by Section

| Section | Array Dimensions | Table Cells | Division Pairs | Constraints |
| :---- | :---- | :---- | :---- | :---- |
| **Warmup** | — | — | — | Uses M4 callback value: {3, 5, 15} fact family displayed via Equation Builder |
| **Lesson S1** | 3×5, 2×7, 4×6 (rotation proofs); 5×8 (1.5 conceptual check) | — | — | Factors 2–8. No squares. Products: 15, 14, 24, 40. Cross-module: 15 is deliberate M4 thread. |
| **Lesson S2** | — | 2s, 5s, 10s first → extend | — | Avoid confusable facts adjacent (A4). Include 1–2 "find factor pairs for this product" interactions (SME addition). |
| **Lesson S3** | Used for division non-commutativity | — | 12÷4 vs 4÷12, 20÷5 vs 5÷20 | Swapped version must NOT produce a whole number. 2–3 pairs tested. |
| **EC** | EC.1: fresh array (not from Lesson) | EC.2: two highlighted cells | EC.3: fresh division pair | All values within Lesson constraints but NOT identical to Lesson values. |
| **Practice** | Mixed arrays | Table available | Mixed division pairs | ?, □, letter unknowns per D7. Include "which operation can you switch order?" format. |
| **Synthesis** | Display reference | Optional reference | Side-by-side summary | Fresh value for connection task. |

---

### Interaction Constraints (All Toys)

* NO verbal/spoken student responses — Guide speaks, student acts
* NO keyboard/text input — all responses via click/tap/drag or MC selection
* NO open-ended questions requiring typed answers — use selection or action tasks
* Questions in Guide speech must be either rhetorical (Guide answers) or answered through on-screen action

---

## 1.6 WARMUP

**[REQUIRED]**

### Core Purpose

**Purpose:** Retrieve the paired multiplication equations from M4 fact families and surface the question: "Why do BOTH orders always work for multiplication?" — the question M5 answers.

**Key Function:** The Warmup uses the M4 callback value (3 × 5 = 15 fact family) to retrieve the pattern students produced without examining: every fact family contained BOTH a × b and b × a. By displaying the completed fact family and asking students to notice the two multiplication equations, the Warmup creates the driving question for the Lesson. This positions S1 to deliver the answer visually (array rotation proof).

**Why this serves the concept:**

* Retrieves the specific pattern M5 will name and explain — commutativity has been in students' work since M4 but never examined
* Activates the fact family structure from M4 as the familiar frame, then zooms in on one aspect (the two multiplication equations always give the same answer) that students have taken for granted
* Creates a genuine question ("Is this always true, or did we just get lucky with these numbers?") that the Lesson answers through proof

**Test:** If we removed this Warmup, would students lose mathematical preparation for the Lesson? YES — students would enter S1 without (1) reactivation of the paired multiplication equations they produced in M4, (2) the explicit question "Why do both orders give the same answer?" which frames the rotation proof, and (3) the fact family context that makes commutativity meaningful rather than abstract.

### Parameters

| Parameter | Value |
| :---- | :---- |
| **Time** | ~3 minutes |
| **Interactions** | 3 (2 with student action + 1 bridge) |
| **Warmup Type** | Activation (M4 Callback) |
| **Cognitive Load** | 20–30% — recognition within a familiar pattern, no new mathematical content |
| **Remediation** | Pipeline (light) |
| **Vocabulary** | NEW terms: forbidden. ESTABLISHED terms activated: fact family, array, multiply, equation, factor, product. No `[vocab]` tags in Warmup — all terms are established. |
| **Visual States** | 2 max: [DISPLAY] fact family equations, [MODIFY] highlight paired multiplication equations |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Retrieve the two paired multiplication equations (3 × 5 = 15 and 5 × 3 = 15) from the M4 fact family context | Teach WHY both orders work (that's S1's rotation proof) |
| Surface the question "Does switching the order ALWAYS give the same product?" | Introduce "commutative," "commutative property," or any formal property name |
| Use the M4 callback value {3, 5, 15} per Data Constraints | Use division as focus (division non-commutativity is S3) |
| Use session-relative language ("last time" / "this time") | Use temporal language ("yesterday" / "today") |
| Create anticipation for PROVING whether this always works | Tell students the answer before the Lesson proves it |
| Include 2+ engagement anchors from approved list | Exceed 2 visual states |

> **Warmup Type Rationale:** Activation (M4 Callback) is the right type because M5 examines a pattern students have been USING since M4 without examining it. The warmup's job is retrieval (reactivate the paired multiplication equations from fact families) + noticing (zoom in on the two × equations giving the same answer) + questioning (is this always true?). Notice & Wonder would also work for a pattern-discovery module, but M5 needs a specific prior-knowledge link to M4 fact families, not open-ended exploration. Activation with a callback value is more targeted.

> **Design Note — Cross-module hook differentiation (Pattern #40):** M4's warmup opened with "Look what's back — the array you read four different ways last time" (M3 callback). M5's warmup opens with a different frame: starting from the fact family as a whole, then zooming into the multiplication pair. The hook is about NOTICING something inside a familiar pattern, not recalling a prior visual.

---

### Interaction W.1: Two Equations, Same Answer [ACTIVATION]

* **Purpose:** Retrieve M4 fact family and direct attention to the paired multiplication equations that always produce the same product. Student identifies which two equations "say the same thing but in different order."
* **Visual: Equation Builder (display) — Select (multiple).** Four equations displayed: 3 × 5 = 15, 5 × 3 = 15, 15 ÷ 3 = 5, 15 ÷ 5 = 3. All visible simultaneously. Standard fact family layout from M4.
* **Guide:** "Remember this fact family? 3, 5, and 15. You built it with arrays. Look at just the multiplication equations: 3 × 5 = 15 and 5 × 3 = 15. Same answer, but the factors are switched. Which two equations have their factors in different order but give the same product?"
* **Prompt:** "Select the two equations that have their factors switched but give the same product."
* **Student Action:** Select (multiple) — select 2 of 4 equations
  * **Options:**
  A. 3 × 5 = 15
  B. 5 × 3 = 15
  C. 15 ÷ 3 = 5
  D. 15 ÷ 5 = 3
* **Correct Answer:** A and B
* **Answer Rationale:**
  - A + B = Correct (both are multiplication equations with factors 3 and 5 in different order, same product 15)
  - C or D selected = Student confused multiplication equations with division equations; may not distinguish × from ÷ in the fact family
* **On Correct:** "3 × 5 and 5 × 3. Same factors, different order, same product."
* **Remediation:** Pipeline

> **Engagement Anchors:** (1) Personalization — "a fact family you worked with last time" (M4 callback). (2) Narrative — zooming into a familiar pattern to notice something specific creates a "detective" frame.

---

### Interaction W.2: Always True or Just Lucky? [JUDGMENT]

* **Purpose:** Pose the driving question: does switching the factor order ALWAYS produce the same product, or was {3, 5, 15} a special case? Student makes a prediction. This creates the curiosity gap the Lesson answers.
* **Visual: Equation Builder (display) — Select (single).** [MODIFY] from W.1: the two multiplication equations (3 × 5 = 15 and 5 × 3 = 15) are highlighted/enlarged. Division equations dimmed.
* **Guide:** "So 3 × 5 and 5 × 3 both equal 15. But here's the real question: is that ALWAYS true? If you switch the order of the factors in ANY multiplication problem, do you always get the same answer? Or did we just get lucky with 3 and 5?"
* **Prompt:** "Do you think switching the factor order ALWAYS gives the same product?"
* **Student Action:** Select (single)
  * **Options:**
  A. Yes — it always works
  B. No — it only works sometimes
  C. I'm not sure
* **Correct Answer:** A (but all answers accepted — this is a prediction, not assessment)
* **Answer Rationale:**
  - A = Student predicts commutativity always holds (most common intuition after seeing one example)
  - B = Student suspects the pattern may not generalize (healthy skepticism, creates strong investigation motivation)
  - C = Student withholds judgment (also valid, creates genuine curiosity)
  - All answers are intentionally accepted. This is a prediction task, not assessment. Pedagogical value is in posing the question, not in the answer.
* **On Correct:** "You predicted it always works. Let's find out if you're right."
* **Remediation:** Pipeline
  * **Remediation Note:** All responses are valid predictions. Pipeline should acknowledge the student's thinking and transition forward regardless of selection. For B or C: "Interesting — you're not sure yet. That's exactly what we're about to investigate."

> **Engagement Anchor:** (3) Choice/Agency — student makes a genuine prediction that creates personal stake in the investigation. The question is authentic because students may genuinely wonder.

> **Design Note:** Accepting all answers as valid maintains the low-stakes warmup philosophy. The pedagogical value is in POSING the question, not in students getting it "right." Students who predict "no" or "not sure" may be MORE engaged in the proof because they have a genuine hypothesis to test.

---

### Interaction W.3: Bridge to Lesson [BRIDGE]

* **Purpose:** Create anticipation for the Lesson by previewing the investigation approach (arrays + rotation) without teaching the result.
* **Visual: Equation Builder (display).** Same state as W.2 (highlighted multiplication pair).
* **Guide:** "Only one way to find out. We need PROOF! And the cool thing is, you already have a tool that can show you. Remember arrays? Let's see if they can prove whether switching the order always works."
* **No student action.**

> **Design Note — Bridge Quality:** The bridge creates anticipation through (1) the word "proof" — elevating the investigation, (2) callback to arrays as a familiar tool students trust, (3) the open question "can they prove it?" rather than stating the answer. The Purpose Frame at the Lesson opening will complete the orientation.

---

### Warmup Verification Checklist

- [x] Hook in first 15–20 seconds: W.1 opens with fact family callback + "look at just the multiplication equations"
- [x] 2+ engagement anchors: Personalization (M4 callback), Narrative (zooming into pattern), Choice/Agency (prediction)
- [x] 2+ meaningful interactions: W.1 (select paired equations) + W.2 (prediction/judgment)
- [x] 1+ judgment/noticing task: W.2 ("Is it ALWAYS true?")
- [x] Zero formal vocabulary introduced: "commutative" not used, only established terms
- [x] Maximum 2 visual states: [DISPLAY] full family → [MODIFY] highlight × pair
- [x] Bridge creates anticipation without teaching: previews investigation, doesn't state result
- [x] Total time ~3 minutes: 3 interactions, brisk
- [x] Cognitive load 20–30%: recognition within familiar pattern + genuine prediction
- [x] Session-relative language: "last time" (not "yesterday")
- [x] Every interaction with student action has both Guide: and Prompt:
- [x] Cross-module hook differentiation (Pattern #40): M4 hook = "Look what's back — the array." M5 hook = "Here's a fact family you worked with" + zoom into × pair. Different frame.
- [x] No terms from Vocabulary To Avoid list (distributive, associative, "add a zero")

**Module-specific:**
- [x] Uses M4 callback value {3, 5, 15} per §1.5.4
- [x] Does not use arrays (Warmup uses Equation Builder per TVP)
- [x] Does not pose division question (reserved for S3)

---

## 1.7 LESSON (~10-12 min)

**[REQUIRED]**

### Core Purpose

Students discover and name the commutative property of multiplication — that switching the order of factors always produces the same product — through array rotation proofs and multiplication table symmetry. Then they test whether this property extends to division and discover it does NOT. By the end, students can articulate: "Order doesn't matter for multiplication, but order DOES matter for division."

### Pedagogical Flow

The Lesson follows a discovery-to-contrast arc in three sections:

**S1 (Concrete/Representational):** Arrays prove commutativity visually. A 3×5 array rotated 90° becomes 5×3 with the same total. Multiple examples generalize this. The term "commutative" is introduced informally AFTER the visual proof grounds it. **CRA: Concrete → Relational.**

**S2 (Abstract):** The Multiplication Tables Grid shows commutativity at scale. Students actively discover commutative partners in the table, then observe the diagonal symmetry. The property moves from "this works for these specific arrays" to "this works for ALL multiplication facts." **CRA: Abstract.**

**S3 (Application/Transfer with representational support):** The critical pivot. "Does switching the order work for division too?" Students test division pairs using arrays and discover the answer is NO. The paired structure (works for ×, fails for ÷) ensures the contrast is salient and both rules are cognitively active. **CRA: Application/Transfer.**

### Lesson Structure

| Section | Focus | Time | CRA Stage |
| :---- | :---- | :---- | :---- |
| S1 — Commutativity Proof Through Arrays | Visual proof via rotation, generalizing across examples, informal naming | 3–4 min | Concrete → Relational |
| S2 — Table Symmetry Discovery | Commutative partner finding in table, diagonal observation, property at scale | 3–4 min | Abstract |
| S3 — Non-Commutativity of Division | Test commutativity for division, discover failure, crystallize contrast | 3–4 min | Application/Transfer |

### Vocabulary Reinforcement Plan

| Term | Introduced At | Reinforced In | Target Density |
| :---- | :---- | :---- | :---- |
| [vocab]commutative[/vocab] (informal: "order doesn't matter for multiplication") | Interaction 1.4 | 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.3, 3.4 | 9x in 10 remaining interactions (90%) |

**Warmup activation:** Established terms activated in Warmup: fact family, array, multiply, equation, factor, product. All used without `[vocab]` tags.

---

### Required Phrases (Must Appear in Script)

* "order doesn't matter for multiplication" (D5 informal naming — primary language)
* "[vocab]commutative[/vocab]" (formal term, introduced informally per D5)
* "same product" / "same answer" (describing commutativity outcome)
* "switch the order" / "factors switched" (describing the operation)
* "order DOES matter for division" (non-commutativity crystallization)
* "does NOT work for division" / "doesn't give the same answer" (A3 refutation)
* "rotate" / "rotation" (array proof mechanism — S1)
* "same dots, same total" (rotation proof logic — S1)
* "diagonal" (table symmetry observation — S2)
* "[vocab]commutative[/vocab] partner" (table interaction language — S2)

### Forbidden Phrases (Create Misconceptions)

* ❌ "commutative property" as formal term without informal grounding first (per D5: informal naming before or alongside formal)
* ❌ "distributive property" / "associative property" (per D5: not named in M5, deferred to M6+)
* ❌ "add a zero" (per D6: never used as computation strategy)
* ❌ "you can't divide a smaller number by a larger number" (mathematically false — you CAN, the result is a fraction/decimal; students just haven't learned that yet. Say "doesn't give a whole number" instead)
* ❌ "division is the opposite of multiplication" (oversimplification — M4 taught inverse relationship more precisely; "opposite" creates confusion)
* ❌ "it always works" without specifying WHICH operation (ambiguous — could overgeneralize)
* ❌ "the rule" (singular) when discussing both commutativity and non-commutativity (they're two distinct observations, not one rule)
* ❌ "you need to memorize this" (undermines the proof-based discovery approach)

---

### Purpose Frame [RECOMMENDED]

* **Purpose:** Orient students to what they will learn and why — connecting the Warmup question to the investigation they're about to do.
* **Visual: Equation Builder (display).** Same highlighted multiplication pair from Warmup (3 × 5 = 15 and 5 × 3 = 15).
* **Guide:** "You wrote 3 × 5 and 5 × 3 in your fact family, and they both gave 15. Now you're going to find out if switching the factors ALWAYS gives the same product, and arrays are going to help you prove it."
* **No student action.**

> **Design Note — Purpose Frame scope:** The frame previews S1–S2 (commutativity proof through arrays and table) without previewing S3 (division test). The division pivot is deferred to 3.1's pivot question, which is more dramatic as a genuine surprise. The phrase "arrays are going to help you prove it" connects to the Warmup bridge ("remember arrays?"). Per §1A, the Purpose Frame uses only vocabulary students already know — no new terms. Revised per Gate 2 author review (G2.2): simplified to Grade 3 concrete language, removed abstract framing ("ALWAYS," "prove," "EVERY operation").

---

### 1.7.1 LESSON SECTION 1: Commutativity Proof Through Arrays

**CRA Stage:** Concrete → Relational

### Interaction 1.1a: The First Rotation — Setup [WORKED EXAMPLE / Guide_Think_Aloud]

* **Purpose:** Guide introduces the M4 callback array (3×5) and triggers the rotation animation. Students observe the transformation.
* **Visual: Arrays (Rotation Proof mode).** Horizontal. 3 rows × 5 columns = 15 dots. Equation overlay: "3 × 5 = 15" displayed. Rotation animation triggered by Guide narration.
* **Guide:** "[PLANNING] Here's an array: 3 rows of 5, that's 3 × 5 = 15. [ACTION] Now watch what happens when I rotate it. [event: rotation_90]"
* **No student action.**

### Interaction 1.1b: The First Rotation — Confirm [WORKED EXAMPLE / Guide_Think_Aloud]

* **Purpose:** After observing the rotation, Guide narrates the key insight (same dots, changed description) and student confirms the product is unchanged.
* **Visual: Arrays (Rotation Proof mode) — Select (single).** Post-rotation: 5 rows × 3 columns = 15 dots. Equation overlay: "5 × 3 = ?"
* **Guide:** "[ATTENTION] Now it's 5 rows of 3. Same dots, same total, but the equation changed to 5 × 3. [SELF-CHECK] Rotating didn't add or remove any dots. So 3 × 5 really does equal 5 × 3."
* **Prompt:** "After rotating the 3 × 5 array, the product is:"
* **Student Action:** Select (single)
  * **Options:**
  A. 15 — same product
  B. 8 — the factors added
  C. 35 — the digits combined
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (rotation preserves total; 3 × 5 = 5 × 3 = 15)
  - B = Student added factors (3 + 5 = 8) — confusing operation
  - C = Student concatenated digits (3 and 5 → 35) — surface-level error
* **On Correct:** "15 before, 15 after. Rotating the array didn't change the total."
* **Remediation:** Pipeline

> **Design Note — Think-aloud tags:** [PLANNING], [ATTENTION], [ACTION], [SELF-CHECK] are authoring annotations per Lesson Playbook §3A. Strip before publishing to Notion/scripting. The Guide dialogue reads naturally without them.

> **Design Note — M4 thread:** The 3×5=15 array is the M4 callback value. Using it for the first rotation proof creates a cross-module thread: M3 (dual-read) → M4 (fact family) → M5 (commutativity proof). The student sees the same array do different mathematical work in each module.

---

### Interaction 1.2: A Second Proof [WORKED EXAMPLE — Partial]

* **Purpose:** Second rotation proof with a fresh array (2×7). Guide narrates more briefly (fading from full worked example). Student confirms the result.
* **Visual: Arrays (Rotation Proof mode) — Select (single).** Horizontal. 2 rows × 7 columns = 14 dots. Equation overlay: "2 × 7 = 14." Rotation animation pending.
* **Guide:** "Now a different array: 2 rows of 7, that's 2 × 7 = 14. Watch the rotation. [event: rotation_90] 7 rows of 2. Same dots. Is the total still 14?"
* **Prompt:** "What is the product of the rotated array (7 × 2)?"
* **Student Action:** Select (single)
  * **Options:**
  A. 14
  B. 9
  C. 12
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (7 × 2 = 14, same total as 2 × 7)
  - B = Student added factors (7 + 2 = 9)
  - C = Nearby product — possible A4 interference or guessing
* **On Correct:** "14 both ways. Two rotations, same result both times."
* **Remediation:** Pipeline

---

### Interaction 1.3: Student Tests a Third Array [GUIDED PRACTICE]

* **Purpose:** Student predicts the result of rotating a third array (4×6) BEFORE seeing the animation. This shifts from observation to prediction — increasing cognitive demand. The rotation confirms.
* **Visual: Arrays (Rotation Proof mode) — Select (single).** Horizontal. 4 rows × 6 columns = 24 dots. Equation overlay: "4 × 6 = 24." Rotation animation NOT yet played.
* **Guide:** "Here's a new array: 4 rows of 6, that's 4 × 6 = 24. Before I rotate it, think about this: if the array becomes 6 rows of 4, will the total change? What will 6 × 4 equal?"
* **Prompt:** "Predict: what is 6 × 4?"
* **Student Action:** Select (single)
  * **Options:**
  A. 24
  B. 10
  C. 20
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (6 × 4 = 24, commutative property)
  - B = Student added factors (6 + 4 = 10)
  - C = Nearby product — possible retrieval error
* **On Correct:** "24. Let's see... [event: rotation_90] 6 rows of 4, 24 dots. You predicted it."
* **Remediation:** Pipeline

> **Scaffolding Note:** Interactions 1.1→1.2→1.3 fade from full worked example (Guide narrates everything, student confirms) to partial (Guide narrates briefly, student confirms) to prediction (student predicts before animation). This is the fading structure per Lesson Playbook §3.

---

### Interaction 1.4: Naming the Property [VOCABULARY INTRODUCTION / Type A + Type C]

* **Purpose:** After three visual proofs, formally introduce the informal name: "Multiplication is [vocab]commutative[/vocab] — order doesn't matter." The naming comes AFTER experience, per vocabulary staging rules.
* **Visual: Arrays (display).** All three arrays shown in a strip: 3×5, 2×7, 4×6, each with both orientations displayed. Equation Builder (display) shows all six equations (pre- and post-rotation) alongside.
* **Guide:** "Three rotations, and every time the product stayed the same: 3 × 5 = 5 × 3, 2 × 7 = 7 × 2, 4 × 6 = 6 × 4. There's a name for this: multiplication is [vocab]commutative[/vocab]! That just means order doesn't matter. Switch the factors and the product stays the same."
* **No student action.**

> **Design Note — Vocabulary staging:** "Commutative" is introduced AFTER three visual proofs (interactions 1.1–1.3), per §1.3 staging plan and Lesson Playbook §4A. The informal definition ("order doesn't matter for multiplication") comes immediately with the term. Per D5, the formal name is mentioned lightly — the primary language is the informal description.

> **Voice Note:** "That's a big word, but it just means..." is Grade 3-calibrated metacognitive framing. It acknowledges the term is new without creating anxiety, and immediately grounds it in accessible language.

---

### Interaction 1.5: Commutative Check [CONCEPTUAL CHECK]

* **Purpose:** Quick check that students connect the term to the concept. Uses a fresh pair (not from the three proofs) to test transfer.
* **Visual: Equation Builder (display) — Select (single).** Shows: "5 × 8 = 40" and "8 × 5 = ?"
* **Guide:** "Multiplication is [vocab]commutative[/vocab], order doesn't matter. So if 5 × 8 = 40, what does 8 × 5 equal?"
* **Prompt:** "If 5 × 8 = 40, what is 8 × 5?"
* **Student Action:** Select (single)
  * **Options:**
  A. 40
  B. 13
  C. 58
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (commutative property: 8 × 5 = 5 × 8 = 40)
  - B = Added factors (5 + 8 = 13)
  - C = Concatenated digits (5 and 8 → 58)
* **On Correct:** "40. Order doesn't matter. 5 × 8 and 8 × 5 are [vocab]commutative[/vocab] partners."
* **Remediation:** Pipeline

**→ SECTION 1 COMPLETE. PROCEED TO SECTION 2.**

---

### 1.7.2 LESSON SECTION 2: Table Symmetry Discovery

**CRA Stage:** Abstract

### Interaction 2.1: Find the Partner — Easy [GUIDED DISCOVERY]

* **Purpose:** First table interaction. Guide highlights a cell (2 × 5 = 10) and asks student to find its commutative partner (5 × 2). Uses the most fluent facts first per A4 prevention ordering.
* **Visual: Multiplication Tables Grid (10×10, full display) — Select (single).** Cell at row 2, column 5 highlighted (value: 10). Student can click cells.
* **Guide:** "Here's the multiplication table. See this highlighted cell? That's 2 × 5 = 10. If multiplication is [vocab]commutative[/vocab], there should be another cell with the same product but the factors switched. Find 5 × 2 in the table."
* **Prompt:** "Find the cell for 5 × 2 in the table."
* **Student Action:** Select (single) — click cell at row 5, column 2
* **Correct Answer:** Cell (5, 2) = 10
* **On Correct:** "5 × 2 = 10, same as 2 × 5. The [vocab]commutative[/vocab] partner."
* **Remediation:** Pipeline

> **Scaffolding Note (PE-4 sequencing):** S2 begins with 2s and 5s — the most fluent facts with lowest interference risk per A4 research ordering. This is the guided entry point.

---

### Interaction 2.2: Find the Partner — Familiar [GUIDED PRACTICE]

* **Purpose:** Second partner-finding interaction. Uses 3 × 5 (the M4 thread value) in the table context. Slightly less guidance than 2.1.
* **Visual: Multiplication Tables Grid — Select (single).** Cell at row 3, column 5 highlighted (value: 15). Prior cell pair (2,5)/(5,2) subtly marked.
* **Guide:** "There's 3 × 5 = 15, the fact family from your Warmup. The [vocab]commutative[/vocab] partner has the factors switched. Find it."
* **Prompt:** "Find the cell for 5 × 3 in the table."
* **Student Action:** Select (single) — click cell at row 5, column 3
* **Correct Answer:** Cell (5, 3) = 15
* **On Correct:** "5 × 3 = 15. Same product, factors switched."
* **Remediation:** Pipeline

---

### Interaction 2.3: Find the Partner — Moderate [INDEPENDENT PRACTICE]

* **Purpose:** Third partner-finding. Extends to 4 × 7 (moderate difficulty, outside the 2s/5s comfort zone). Less guidance — student should recognize the pattern.
* **Visual: Multiplication Tables Grid — Select (single).** Cell at row 4, column 7 highlighted (value: 28).
* **Guide:** "Here's 4 × 7 = 28. You know what to do. Find the [vocab]commutative[/vocab] partner."
* **Prompt:** "Find the cell for 7 × 4 in the table."
* **Student Action:** Select (single) — click cell at row 7, column 4
* **Correct Answer:** Cell (7, 4) = 28
* **On Correct:** "7 × 4 = 28. Same product, opposite sides again. Do you see where the partners always sit?"
* **Remediation:** Pipeline

> **Scaffolding Note:** 2.1 (2×5) → 2.2 (3×5) → 2.3 (4×7): progression from easiest fluent facts to moderate, with decreasing Guide narration. This addresses the PE3.2 within-S2 scaffolding fade.

---

### Interaction 2.4: The Diagonal [OBSERVATION / Type A]

* **Purpose:** Guide draws attention to the diagonal symmetry. After finding three partner pairs, students can see that partners are always reflected across the diagonal. This is Guide-led observation, not a separate teaching target (per §1.5.2 guardrails).
* **Visual: Multiplication Tables Grid.** All three partner pairs highlighted with connecting lines: (2,5)↔(5,2), (3,5)↔(5,3), (4,7)↔(7,4). Diagonal line displayed across the table.
* **Guide:** "Look at where those partners sit. 2 × 5 is HERE [event: highlight_cell_2_5], and 5 × 2 is over HERE [event: highlight_cell_5_2], opposite sides of this line going corner to corner. That's the diagonal. The table is like a mirror: every [vocab]commutative[/vocab] pair sits on opposite sides. That's an arithmetic pattern in the multiplication table."
* **No student action.**

> **Design Note — Diagonal treatment:** Per §1.5.2 guardrails, the diagonal is evidence for commutativity, not its own concept. The Guide names it as a structural feature ("like a mirror") without elevating it to a separate learning target. Students don't need to "learn about diagonals" — they need to see that the table's structure reflects the property they just proved with arrays.

---

### Interaction 2.5: Reverse Direction — Find Factor Pairs [HIGHER-DEMAND TASK]

* **Purpose:** SME-added interaction type. Given a product, find the factor pairs that produce it. This is the highest-demand task in S2 — student works from product to factors rather than factors to product.
* **Visual: Multiplication Tables Grid — Select (multiple).** Product 24 highlighted in multiple cells. Student can click cells.
* **Guide:** "Now try something different. The number 24 appears in several places in the table. Can you find two cells that show 24 and are [vocab]commutative[/vocab] partners, same product, factors switched?"
* **Prompt:** "Find two cells showing 24 where the factors are switched (e.g., 3 × 8 and 8 × 3)."
* **Student Action:** Select (multiple) — select 2 cells showing 24 that are commutative partners (e.g., cells (3,8) and (8,3), or (4,6) and (6,4))
* **Correct Answer:** Any valid commutative pair: (3,8)+(8,3) or (4,6)+(6,4) or (2,12) — but 12 is outside the 10×10 visible range, so (3,8)+(8,3) or (4,6)+(6,4)
* **On Correct:** "Those two cells are commutative partners. Same product, factors switched, opposite sides of the diagonal."
* **Remediation:** Pipeline
  * **Remediation Note:** If student selects two cells showing 24 that are NOT partners (e.g., (3,8) and (4,6)), pipeline should clarify: "Both show 24, but commutative partners have the SAME two factors in different order."

> **SP Note — Multi-answer validation (CA-8):** This interaction accepts multiple valid answer sets: (3,8)+(8,3) OR (4,6)+(6,4). Engineering must implement multi-set validation — any valid commutative pair of cells showing 24 is correct. The On Correct and Remediation text work for either pair.

**→ SECTION 2 COMPLETE. PROCEED TO SECTION 3.**

---

### 1.7.3 LESSON SECTION 3: Non-Commutativity of Division Discovery

**CRA Stage:** Application/Transfer (with representational support)

### Interaction 3.1: The Pivot Question [DISCOVERY FRAME / Type A]

* **Purpose:** Pose the critical question that drives S3: "Does switching the order work for division too?" This connects back to the Warmup's broader question ("every operation?") and the Purpose Frame's preview.
* **Visual: Equation Builder (display).** Side by side: "3 × 5 = 5 × 3 ✓" and "12 ÷ 4 = ? ÷ ? = ?"
* **Guide:** "You've proven that multiplication is [vocab]commutative[/vocab], order doesn't matter. But here's the big question: does that work for DIVISION too? If 12 ÷ 4 = 3... does 4 ÷ 12 also equal 3? Let's test it!"
* **No student action.**

> **Design Note — D9 compliance:** Per D9 (the primary design decision for M5), the non-commutativity discovery happens IMMEDIATELY after commutativity is established, while both results are cognitively active. This interaction is the pivot — placed right after S2's table symmetry confirmation. Not deferred to Synthesis.

---

### Interaction 3.2: Testing Division — First Pair [GUIDED DISCOVERY]

* **Purpose:** Test 12 ÷ 4 vs 4 ÷ 12 concretely using the array. Students see that 12 dots CAN be arranged into 4 groups of 3, but 4 dots CANNOT be arranged into 12 groups. The failure is visual and physical.
* **Visual: Arrays (Non-Commutativity Discovery mode) — Select (single).** First display: 12 dots arranged as 4 columns × 3 rows. Equation: "12 ÷ 4 = 3." Then system attempts to show "4 ÷ 12": 4 dots, trying to split into 12 groups — the dots cannot be divided evenly. Visual shows the impossibility.
* **Guide:** "12 ÷ 4: twelve dots, 4 equal groups, 3 in each. That works. Now switch: 4 ÷ 12. [event: division_attempt] Four dots, twelve groups. You can't split 4 things into 12 equal groups."
* **Prompt:** "Does 12 ÷ 4 give the same answer as 4 ÷ 12?"
* **Student Action:** Select (single)
  * **Options:**
  A. Yes — same answer
  B. No — different answers
* **Correct Answer:** B
* **Answer Rationale:**
  - A = Overgeneralizing commutativity to division (A3 misconception) — student assumes "order doesn't matter" applies to all operations
  - B = Correct (12 ÷ 4 = 3, but 4 ÷ 12 cannot produce a whole number)
* **On Correct:** "12 ÷ 4 = 3, but 4 ÷ 12 doesn't give a whole number. Different answers."
* **Remediation:** Pipeline
  * **Remediation Note:** A3 misconception trigger. Pipeline should use the array visual: "Look — 12 dots split into 4 groups gives 3 each. But 4 dots split into 12 groups? There aren't enough dots. The answers are NOT the same."

---

### Interaction 3.3: Testing Division — Second Pair [INDEPENDENT PRACTICE]

* **Purpose:** Second test with 20 ÷ 5 vs 5 ÷ 20. Less guidance — student should anticipate the result from the first test.
* **Visual: Arrays (Non-Commutativity Discovery mode) — Select (single).** 20 dots arranged as 5 columns × 4 rows. Equation: "20 ÷ 5 = 4." Then system attempts "5 ÷ 20."
* **Guide:** "Let's try another. 20 ÷ 5 = 4, twenty dots, five groups, four in each. Now switch: 5 ÷ 20. Five dots, twenty groups. [event: division_attempt] Can you split 5 things into 20 equal groups?"
* **Prompt:** "Does 20 ÷ 5 give the same answer as 5 ÷ 20?"
* **Student Action:** Select (single)
  * **Options:**
  A. Yes — same answer
  B. No — different answers
* **Correct Answer:** B
* **Answer Rationale:**
  - A = A3 misconception persistence
  - B = Correct (20 ÷ 5 = 4, but 5 ÷ 20 is not a whole number)
* **On Correct:** "20 ÷ 5 = 4, but 5 ÷ 20 doesn't work. Switching breaks it again."
* **Remediation:** Pipeline

---

### Interaction 3.4: The Contrast — Two Rules [CONSOLIDATION / Type C]

* **Purpose:** Crystallize the contrast: multiplication IS commutative, division is NOT. This is the consolidation statement required at the S3→EC transition (per CA-3 Task 2 guidance). Student selects which operation allows order switching.
* **Visual: Equation Builder (display) — Select (single).** Side-by-side display:
Left: "3 × 5 = 5 × 3 ✓" / "2 × 7 = 7 × 2 ✓" / "4 × 6 = 6 × 4 ✓"
Right: "12 ÷ 4 ≠ 4 ÷ 12 ✗" / "20 ÷ 5 ≠ 5 ÷ 20 ✗"
* **Guide:** "Here's what you've discovered. Multiplication is [vocab]commutative[/vocab]: switching the order always gives the same answer. But division does NOT work that way. Order doesn't matter for multiplication; order DOES matter for division."
* **Prompt:** "Which operation is commutative (lets you switch the order and get the same answer)?"
* **Student Action:** Select (single)
  * **Options:**
  A. Multiplication
  B. Division
  C. Both
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (multiplication is commutative; division is not)
  - B = Incorrect (division is NOT commutative — switching order changes the result)
  - C = A3 misconception — believes commutativity is universal
* **On Correct:** "Multiplication. You can switch factors and get the same product. Division doesn't work that way."
* **Remediation:** Pipeline

> **Design Note — CA-3 consolidation:** This interaction fulfills the Task 2 guidance from CA-3: explicitly distinguishing the two rules at the S3→EC boundary. Both properties are stated in the Guide dialogue and tested in the MC. Students who get heavy remediation on this interaction receive the explicit contrast through the pipeline.

---

### Bridge to Exit Check [TRANSITION / Type A]

* **Purpose:** Signal shift from learning to low-stakes assessment.
* **Visual: Equation Builder (display).** Same side-by-side contrast display from 3.4.
* **Guide:** "You proved something important: multiplication is [vocab]commutative[/vocab], order doesn't matter for factors. And you discovered that division is NOT. Order matters there. Let's see what you know."
* **No student action.**

**→ SECTION 3 COMPLETE. LESSON COMPLETE.**

---

### Misconception Prevention

**#A3: Overgeneralizing commutativity to division (PRIMARY)**

* **Prevention:** The entire S3 is designed as a paired discovery — immediately after establishing commutativity for multiplication, the same question is tested for division and FAILS. Per D9, this happens during the lesson while both results are cognitively active, not deferred to Synthesis.
* **Specific interactions:** 3.2 (first division test), 3.3 (second division test), 3.4 (explicit contrast)
* **Visual cue:** Arrays make the non-commutativity of division concrete — 12 dots CAN form 4 groups of 3, but 4 dots CANNOT form 12 groups. The impossibility is visual, not just numerical.
* **Language design:** The Guide says "Order doesn't matter for multiplication" followed immediately by "But does it work for division?" — framing the test as a natural question, not a trick. When division fails, the Guide names the contrast explicitly: "Order DOESN'T matter for multiplication. Order DOES matter for division."

**#A4: Associative interference in fact recall (SECONDARY)**

* **Prevention:** Data constraint ordering in S2 sequences facts from fluent (2s, 5s) to moderate (3s, 4s), avoiding confusable facts adjacent. Per §1.5.2 guardrails, 6s–9s reserved for later table interactions after the commutative pattern is established.
* **Specific interactions:** S2 ordering (2.1: 2×5, 2.2: 3×5, 2.3: 4×7) deliberately avoids the high-interference zone.

---

### 1.7.4 Incomplete Script Flags

**If ANY of these are true, STOP and resolve:**

- [ ] Total interaction count below 12 (current: 14 including transitions and bridges — PASS)
- [ ] Missing "commutative" introduction after visual grounding
- [ ] Missing non-commutativity discovery (S3)
- [ ] Missing explicit contrast statement at S3→EC boundary
- [ ] Contains any forbidden phrase
- [ ] Purpose Frame missing with no KDD justification

### 1.7.5 Success Criteria

**The One Thing:** Switching the order of factors in multiplication always produces the same product (commutative property), but switching the order in division does NOT — order matters for division.

**Ready for Module 6:** Students can explain why multiplication is commutative using arrays (rotation proof), identify commutative partners in the multiplication table, and articulate that division is NOT commutative. This understanding underpins M6's area model work — where decomposing factors (distributive property) relies on commutativity to rearrange partial products.

---

## 1.8 EXIT CHECK (3-5 minutes)

**[REQUIRED]**

### Purpose

Verify Lesson understanding before Practice. Tests whether students can (1) identify that rotating an array produces the same product (commutativity through arrays), (2) find the commutative partner of a given fact in the multiplication table, and (3) determine that switching the order does NOT work for division (non-commutativity).

### Parameters

| Element | Specification |
| :---- | :---- |
| **Problems** | 3 |
| **Cognitive Types** | IDENTIFY (EC.1 — product recognition after rotation; EC.2 — partner location in table); COMPARE (EC.3 — × vs ÷ order-switching). Per EC Playbook §3A: M4-6 may add COMPARE when taught in Lesson; M5 taught comparison explicitly in S3. |
| **Time** | 3-5 minutes |
| **Tone** | Calm, low-stakes |
| **Toys Used** | Arrays (Rotation Proof mode — EC.1), Multiplication Tables Grid (EC.2), Arrays (Non-Commutativity Discovery mode — EC.3) |
| **Remediation** | Pipeline |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Use Arrays + Multiplication Tables Grid (same configurations as Lesson) | Introduce new tools or interaction types |
| Use values NOT identical to Lesson or Warmup interactions | Reuse exact Lesson/Warmup factor/product triples |
| Stay within data constraints (factors 2-9, products ≤ 100) | Exceed Lesson complexity range |
| Test commutativity (array rotation), table symmetry, AND non-commutativity | Test skills not explicitly taught in Lesson |
| Include A3 distractor (overgeneralizing commutativity to division) in EC.3 | Omit the primary misconception from assessment |

### Alignment Check

| Problem | Tests | Lesson Source | Cognitive Type |
| :---- | :---- | :---- | :---- |
| EC.1 | Commutativity — identify product of rotated array | Section 1: array rotation proofs (1.1–1.3) | IDENTIFY |
| EC.2 | Table symmetry — find commutative partner cell | Section 2: partner discovery (2.1–2.3) | IDENTIFY |
| EC.3 | Non-commutativity of division — compare switched results | Section 3: division testing (3.2–3.3) | COMPARE |

---

### Interaction EC.1: Rotation Product [IDENTIFY]

* **Purpose:** Student identifies the product of a rotated array. Tests S1's core insight: rotating doesn't change the total. Fresh array (5×6), not used in Lesson.
* **Visual: Arrays (Rotation Proof mode) — Select (single).** Horizontal. 5 rows × 6 columns = 30 dots. Equation overlay: "5 × 6 = 30." Array rotates 90° to show 6 rows × 5 columns. Equation overlay: "6 × 5 = ?"
* **Guide:** "Here's an array: 5 rows of 6, that's 5 × 6 = 30. Now it rotates. What is 6 × 5?"
* **Prompt:** "After the array rotates, what is 6 × 5?"
* **Student Action:** Select (single)
  * **Options:**
  A. 30
  B. 11
  C. 56
* **Correct Answer:** A
* **Answer Rationale:**
  - A = Correct (rotation preserves total; 5 × 6 = 6 × 5 = 30)
  - B = Student added factors (5 + 6 = 11)
  - C = Concatenated digits (5 and 6 → 56)
* **On Correct:** "30. Same dots, same product. Multiplication is commutative."
* **Remediation:** Pipeline

> **Value Selection:** 5 × 6 = 30 — product 30 not used in any Lesson, Warmup, or S2 interaction. Factors within Lesson range (2–8). Familiar fact, low arithmetic demand.

---

### Interaction EC.2: Find the Partner in the Table [IDENTIFY]

* **Purpose:** Student finds the commutative partner of a given cell in the multiplication table. Tests S2's partner-discovery skill with a fresh pair (6 × 7 = 42, not used in Lesson's 2.1–2.3).
* **Visual: Multiplication Tables Grid — Select (single).** Cell at row 6, column 7 highlighted (value: 42).
* **Guide:** "Here's 6 × 7 = 42 in the table. Find its commutative partner."
* **Prompt:** "Find the cell for 7 × 6 in the table."
* **Student Action:** Select (single) — click cell at row 7, column 6
* **Correct Answer:** Cell (7, 6) = 42
* **On Correct:** "42 both ways. You found the commutative partner across the diagonal."
* **Remediation:** Pipeline

> **Value Selection:** 6 × 7 = 42 — product 42 not in any Lesson interaction. Extends beyond Lesson's factor range (Lesson used 2s, 3s, 4s, 5s, 7s in S2) to test transfer. Moderate difficulty within data constraints.

---

### Interaction EC.3: Does Switching Work for Division? [COMPARE]

* **Purpose:** Student determines whether switching the order in a division problem gives the same result. Tests S3's non-commutativity discovery with a fresh pair (18 ÷ 6 vs 6 ÷ 18). A3 distractor (option A) targets the primary misconception.
* **Visual: Arrays (Non-Commutativity Discovery mode) — Select (single).** 18 dots arranged as 6 columns × 3 rows. Equation: "18 ÷ 6 = 3." Then system attempts "6 ÷ 18": 6 dots, trying to split into 18 groups. Visual shows the impossibility.
* **Guide:** "18 ÷ 6 = 3. Now switch: 6 ÷ 18. Does switching the order give the same answer for division?"
* **Prompt:** "Does 18 ÷ 6 give the same answer as 6 ÷ 18?"
* **Student Action:** Select (single)
  * **Options:**
  A. Yes, same answer
  B. No, different answers
* **Correct Answer:** B
* **Answer Rationale:**
  - A = A3 misconception — overgeneralizing commutativity to division. Student assumes "order doesn't matter" applies to all operations.
  - B = Correct (18 ÷ 6 = 3, but 6 ÷ 18 does not produce a whole number)
* **On Correct:** "18 ÷ 6 = 3, but 6 ÷ 18 doesn't work. Order matters for division."
* **Remediation:** Pipeline
  * **Remediation Note:** A3 misconception trigger. Pipeline should use the array visual: "Look, 18 dots split into 6 groups gives 3 each. But 6 dots split into 18 groups? Not enough dots. Different answers."

> **Value Selection:** 18 ÷ 6 = 3 — dividend 18 not used in any Lesson division interaction (Lesson used 12÷4 and 20÷5). 6÷18 cannot produce a whole number. Fresh pair within data constraints.

---

### EC Verification Checklist

**Structure:**

- [x] 3 problems testing 3 distinct M5 skills (array rotation, table partner-finding, division non-commutativity)
- [x] Each problem maps to a Lesson section (see Alignment Check)
- [x] Transition frame at end of Lesson (Bridge to Exit Check interaction)
- [x] Total time 3-5 minutes

**Alignment:**

- [x] All visual models appeared in Lesson (Arrays Rotation Proof mode — S1; Multiplication Tables Grid — S2; Arrays Non-Commutativity Discovery mode — S3)
- [x] All interaction types appeared in Lesson (Select single — all sections)
- [x] Values differ from all Lesson and Warmup values:
  - EC.1: 5 × 6 = 30 (fresh product)
  - EC.2: 6 × 7 = 42 (fresh product)
  - EC.3: 18 ÷ 6 = 3 (fresh dividend/divisor pair)
- [x] No skill tested that wasn't explicitly taught
- [x] Two cognitive types: IDENTIFY (EC.1, EC.2) and COMPARE (EC.3). Sequence: IDENTIFY → IDENTIFY → COMPARE.

**Constraints:**

- [x] No new vocabulary introduced
- [x] No new visual models introduced
- [x] No complexity increase beyond Lesson (Lesson used factors 2-8; EC uses 5, 6, 7, 18)
- [x] A3 distractor present in EC.3 (option A: "Yes, same answer")
- [x] Every interaction has both Guide: and Prompt:
- [x] On Correct follows EC Playbook §3E: brief, specific, 5-10 words, no new information
- [x] M4 EC values (21, 45, 72) not reused — no cross-module collision

---

## 1.8.5 PRACTICE PHASE INPUTS

**[REQUIRED]**

### Skill Tracking

| Skill ID | Description | Lesson Source | Cognitive Type |
| :---- | :---- | :---- | :---- |
| SK1 | Identify the commutative product — given a × b, state what b × a equals (with or without array) | Section 1 (1.1–1.5) | IDENTIFY |
| SK2 | Find commutative partner in the multiplication table — given one cell, locate the mirrored cell | Section 2 (2.1–2.3) | IDENTIFY |
| SK3 | Determine whether switching the order works — given a ÷ pair, state whether the switched version gives the same result | Section 3 (3.2–3.3) | COMPARE |
| SK4 | Discriminate × from ÷ commutativity — identify which operation allows order-switching | Section 3 (3.4) | COMPARE |
| SK5 | Reverse direction — given a product, find the commutative factor pairs in the table | Section 2 (2.5) | IDENTIFY |

### Distribution Targets

* **SK1 (Commutative product identification):** 25% of problems — core module concept. Mix of array-based (rotation visual) and symbolic (equation-only). Include fresh facts across the 2-9 factor range.
* **SK2 (Table partner-finding):** 25% of problems — table application of commutativity. Given a cell, find the partner. Include both easy pairs (2s, 5s) and harder pairs (6s, 7s, 8s). Some with diagonal reference visible, some without.
* **SK3 (Division non-commutativity):** 20% of problems — A3 misconception prevention. Given a ÷ pair, determine if switching works. The swapped version must NOT produce a whole number. Mix of dividends across 12–40 range.
* **SK4 (Operation discrimination):** 15% of problems — consolidation of the × vs ÷ contrast. MC format: "Which operation lets you switch the order?" or "Can you switch the order in 24 ÷ 6?" Appears interleaved with SK1/SK3 to maintain the contrast.
* **SK5 (Reverse-direction product → factors):** 15% of problems — highest demand. Given a product highlighted in the table, find the commutative factor pairs. Tests the SME-added interaction type from 2.5.

**Tier Classification:**

* **BASELINE:** SK1, SK2, SK4 — core commutativity identification and table application, counts toward mastery
* **STRETCH:** SK3 (division non-commutativity with larger dividends) + SK5 (reverse-direction factor-pair finding), counts toward mastery
* **SUPPORT:** SK1 reduced — array rotation shown with Guide narrating the proof, student only confirms product from MC. Factors ≤ 5, products ≤ 25. Does not count toward mastery.
* **CONFIDENCE:** Single commutative pair displayed, student confirms "same product" from MC. Familiar facts only (2s, 5s). Does not count toward mastery.

### Toy Constraints for Practice

Same as Lesson with the following notes:

* **Arrays:** Used for SK1 problems (Rotation Proof mode) and SK3 problems (Non-Commutativity Discovery mode). Full display with rotation animation for SK1. Division attempt animation for SK3.
* **Multiplication Tables Grid:** Used for SK2 and SK5 problems. Full 10×10 display. Diagonal reference may or may not be visible (scaffolding fade: early problems show diagonal, later problems hide it).
* **Equation Builder:** Display mode for consolidation prompts (SK4). Not interactive in Practice — commutativity is demonstrated through Arrays and Table, not equation manipulation.
* **Data ranges:** Factors 2-9, products ≤ 100, all exact multiplication. Division pairs: dividend always divisible by divisor, swapped version always NOT a whole number.
* **A3 monitoring:** System should track SK3 responses. If student selects "Yes, same answer" on 2+ SK3 problems, flag A3 misconception and route to SUPPORT with explicit array-based division testing.

### Dimensions Used Tracking (EC + Practice)

| Interaction | Factors | Product/Dividend | Division Pair | Notes |
|-------------|---------|-----------------|---------------|-------|
| EC.1 | 5, 6 | 30 | — | Array rotation, fresh product |
| EC.2 | 6, 7 | 42 | — | Table partner, fresh product |
| EC.3 | 18, 6 | 18 | 18÷6 vs 6÷18 | Non-commutativity, fresh pair |

**Non-overlap verification:** No EC product/dividend matches any Lesson product (30, 42, 18 vs. 15, 14, 24, 40, 10, 28, 12, 20). No EC value matches M4 EC products (vs. 21, 45, 72). ✓

**Note:** This table covers EC values only. Practice values are Pipeline-generated at runtime per the Distribution Targets and Toy Constraints above; no pre-specified dimensions. Full authored-content dimension tracking (Warmup + Lesson + EC + Synthesis) is in Working Notes.

### Cross-Module Skill References

M5 Practice does NOT include M3/M4 content as spiral review. M4's fact family production is prerequisite knowledge that M5 has subsumed — commutative partners ARE the paired multiplication equations within fact families. The table structure from Units 1-2 is familiar context, not spiral content.

### Error-Pattern Monitoring

The following error patterns should trigger diagnostic flags in the Practice pipeline:

* **A3 — Overgeneralizing commutativity to division (PRIMARY):** Student selects "Yes, same answer" on SK3 problems. Intervention: route to SUPPORT with explicit array-based division attempt. Show the impossibility visually. Increase SK3 frequency with explicit Guide contrast: "Works for multiplication, NOT for division."
* **A4 — Associative interference in fact recall (SECONDARY):** Student produces incorrect products on SK1/SK2 problems involving confusable facts (e.g., 6×7 vs 6×8). Intervention: avoid adjacent confusable facts, present with array support to ground the product visually.
* **Table navigation error:** Student clicks the correct product but wrong cell (e.g., finds a cell showing 42 that is NOT the commutative partner). Intervention: highlight the row/column labels, route to SUPPORT with Guide pointing out row-column mapping.
* **Factor-addition error:** Student adds factors instead of multiplying (e.g., 5 × 6 = 11). Intervention: return to array representation to rebuild visual connection between arrangement and product.

> **Note:** Distribution targets are starting proportions for the Practice pipeline. The system adjusts based on student performance data — increasing weight on skills where errors are detected and decreasing weight on mastered skills.

---

## 1.9 SYNTHESIS (6-8 minutes)

**[REQUIRED]**

### Purpose

Students step back from commutativity proofs, table partner-finding, and division testing to see the BIGGER PICTURE: the multiplication table has a mirror symmetry (the diagonal) BECAUSE multiplication is commutative, and this means knowing half the facts gives you all of them. But division breaks that symmetry — order matters there. They connect across representations (array rotation → table diagonal → operation comparison), reflect on which tool helped most, and preview M6's area model strategies. Per Tension 2 (Working Notes): strategic payoff ("you only need half the table") should be EXPERIENCED in Practice before being NAMED in Synthesis.

### Parameters

| Element | Specification |
| :---- | :---- |
| **Duration** | 6-8 minutes |
| **Toys Used** | Arrays (display), Multiplication Tables Grid (display), Equation Builder (display) |
| **Interaction Count** | 3 student-action moments (S.1 representation transfer, S.2 pattern discovery, S.3 metacognitive reflection) + Opening Frame + Identity-Building Closure |
| **Task Types** | Type D: Representation Transfer (S.1 — same commutative pair across array and table), Type A: Pattern Discovery (S.2 — × commutative vs ÷ not), Metacognitive Reflection Type 3: Tool/Approach Preference (S.3) |

### Constraints

| MUST | MUST NOT |
| :---- | :---- |
| Use a fresh value set not seen in Lesson, EC, or Warmup | Reuse Lesson/EC/Warmup factor-product triples |
| Connect across representations (array ↔ table ↔ equation) | Present more practice problems disguised as Synthesis |
| Include at least 2 different task types (Type D + Type A) | Use only one task type |
| Include metacognitive reflection before closure | Skip reflection |
| Identity-building closure references specific student achievements | Use generic praise ("Great job!") |
| Bridge to M6 mentions "area models" per TVP transition out | Bridge to content beyond M6 |
| Name the strategic implication ("half the table") per Tension 2 | Teach the strategic implication as new content |
| Light remediation only (mastery assumed) | Extended reteaching |

---

### Opening Frame [No Student Action]

* **Purpose:** Signal shift from assessment to reflection. Connect backward to the three Lesson sections (array proofs, table partners, division testing) and set up the consolidation work.
* **Visual: Arrays (display).** A single 4×9 array shown in both orientations side by side (4 rows × 9 columns AND 9 rows × 4 columns). **Multiplication Tables Grid (display).** Cells (4,9) and (9,4) highlighted with connecting line across diagonal. **Equation Builder (display).** Shows: "4 × 9 = 36" and "9 × 4 = 36."
* **Guide:** "You rotated arrays, found partners in the table, and tested whether division works the same way. Look at this: the same pair, shown three different ways. What do you notice?"
* **No student action.**

> **Design Note:** Opening displays all three representations simultaneously — array, table, and equations — showing the same commutative pair (4 × 9 = 36). Fresh value (36 not used in Lesson, EC, or Warmup). The simultaneous display sets up S.1's representation transfer question.

---

### Interaction S.1: Three Representations, One Property [REPRESENTATION TRANSFER — Type D]

* **Purpose:** Students identify what stays the same across three representations of commutativity: the array rotation, the table symmetry, and the equation pair. Type D task: same concept shown in different forms.
* **Visual:** Three panels side by side:
  - Panel A: Array — 4 rows × 9 columns AND 9 rows × 4 columns (rotation shown)
  - Panel B: Multiplication Tables Grid — cells (4,9) and (9,4) highlighted, diagonal visible
  - Panel C: Equations — "4 × 9 = 36" and "9 × 4 = 36"
* **Guide:** "The array, the table, and the equations. All three show the same thing. What stays the same?"
* **Prompt:** "What do the array rotation, the table partners, and the equations all have in common?"
* **Student Action:** Select (single)
* **Options:**
A. They all show that 4 × 9 and 9 × 4 give the same product
B. They all show that 4 + 9 and 9 + 4 give the same sum
C. They all show division
D. They all need an array
* **Correct Answer:** A
* **Answer Rationale:**
  - A (correct): The commutative property — switching factors gives the same product — is the invariant across all three representations.
  - B: Correct operation (commutative) but wrong operation type — the panels show multiplication (4 × 9), not addition (4 + 9). Tests whether student attends to the specific operation.
  - C: No division appears in any panel.
  - D: Only Panel A has the array. The table and equations don't.
* **On Correct:** "Same product both ways. The array, the table, and the equations all prove it."
* **Connection:** Students see that array rotation, table symmetry, and paired equations aren't three separate ideas — they're three ways of seeing the same property: multiplication is commutative.
* **Remediation:** Pipeline (light)

---

### Interaction S.2: The Odd One Out [PATTERN DISCOVERY — Type A]

* **Purpose:** Students identify which operation breaks the pattern. Four panels show order-switching: three multiplication examples that work, and one division example that doesn't. Type A task: identify the outlier.
* **Visual: Equation Builder (display).** Four panels in a 2×2 grid:
  - Top left: "3 × 5 = 15" and "5 × 3 = 15 ✓"
  - Top right: "4 × 9 = 36" and "9 × 4 = 36 ✓"
  - Bottom left: "2 × 7 = 14" and "7 × 2 = 14 ✓"
  - Bottom right: "18 ÷ 6 = 3" and "6 ÷ 18 = ? ✗"
* **Guide:** "Four pairs. In each one, the order is switched. Three of them work. Which one breaks the pattern?"
* **Prompt:** "Which pair does NOT give the same answer when you switch the order?"
* **Student Action:** Select (single)
* **Options:**
A. 3 × 5 and 5 × 3
B. 4 × 9 and 9 × 4
C. 2 × 7 and 7 × 2
D. 18 ÷ 6 and 6 ÷ 18
* **Correct Answer:** D
* **Answer Rationale:**
  - A: 3 × 5 = 5 × 3 = 15. Commutative. ✓
  - B: 4 × 9 = 9 × 4 = 36. Commutative. ✓
  - C: 2 × 7 = 7 × 2 = 14. Commutative. ✓
  - D (correct): 18 ÷ 6 = 3, but 6 ÷ 18 is not a whole number. Division is not commutative. ✗
* **On Correct:** "Multiplication works every time. Division doesn't. That's the difference."
* **Connection:** This is the consolidation moment — the student sees three multiplication successes and one division failure side by side, crystallizing the × vs ÷ distinction.
* **Remediation:** Pipeline (light)

> **Design Note — Strategic implication (Tension 2):** The Guide adds after the On Correct: "And here's something powerful: because switching always works for multiplication, you already know MORE facts than you think. Every time you learn one multiplication fact, you know its partner too." This names the "half the table" strategic payoff that Practice demonstrated experientially.

---

### Interaction S.3: Which Tool Helped Most? — Metacognitive Reflection (Type 3: Tool/Approach Preference) [REFLECTION]

* **Purpose:** Students identify which representation helped them most: the array rotation, the multiplication table, or the equations. Type 3 (Tool/Approach Preference) appropriate for M5. Produces a concrete self-awareness output.
* **Visual: Arrays (display).** Small array icon. **Multiplication Tables Grid (display).** Small table icon. **Equation Builder (display).** Small equation icon. All three shown as labeled options.
* **Guide:** "You used arrays, the multiplication table, and equations. Which one helped you understand commutativity the most?"
* **Prompt:** "Which tool helped you understand commutativity best?"
* **Student Action:** Select (single)
* **Options:**
A. The arrays — seeing the rotation helped
B. The multiplication table — finding partners helped
C. The equations — seeing the numbers switch helped
D. I'm not sure yet
* **Correct Answer:** Any (all valid metacognitive responses — all-correct MC)
* **Answer Rationale:**
  - "The arrays" = Visual-spatial learner, rotation proof resonated
  - "The multiplication table" = Pattern-recognition learner, symmetry resonated
  - "The equations" = Symbolic learner, number relationships resonated
  - "I'm not sure yet" = Valid — still developing preference awareness
* **On Correct:** (per selection)
  - A → "The rotation made it click. Same dots, same total, just rearranged."
  - B → "The table shows the pattern everywhere. Partners on opposite sides of the diagonal."
  - C → "Numbers don't lie. 4 × 9 and 9 × 4 both equal 36."
  - D → "Still figuring it out is fine. You have all three tools now."
* **Connection:** Students develop metacognitive awareness of their representational preferences. All responses are validated — there's no wrong answer in reflection.
* **Remediation:** Pipeline (light)

> **Design Note — All-Correct MC (Pipeline):** Intentionally all-correct MC. Every option is a valid metacognitive response — no wrong answers. Pipeline should NOT trigger remediation on any selection. All four On Correct responses are tailored.

---

### Identity-Building Closure + M6 Bridge [No Student Action]

* **Purpose:** Specific, growth-oriented affirmation. Names what the student accomplished (proved commutativity through arrays, discovered the diagonal pattern, tested division), previews M6's area model work.
* **Visual:** Multiplication Tables Grid with diagonal highlighted. Fading slightly as closure begins.
* **Guide:** "You proved that multiplication is commutative by rotating arrays. You found the mirror pattern in the multiplication table. And you discovered that division doesn't work the same way. Next time, you'll use AREA MODELS to discover strategies for multiplying larger numbers, and commutativity will help you there too."
* **No student action.**

> **Bridge Note:** Per TVP M5→M6 transition: M6 introduces area model decomposition strategies, where the distributive property emerges from gridded rectangles. "Area models to discover strategies for multiplying larger numbers" matches TVP bridge text. "Commutativity will help you there too" creates forward connection — rearranging partial products relies on commutativity.

> **Design Note — Closure specificity:** "You proved... You found... You discovered." Names three concrete achievements matching the module's three-section arc (S1 array proofs, S2 table symmetry, S3 division testing). Per Synthesis Playbook §3F: specific behavioral language, not generic praise.

---

### Synthesis Verification Checklist

**Structure:**

- [x] Opening frame signals shift to reflection/consolidation (30-45 sec)
- [x] Connection tasks present (S.1 representation transfer, S.2 pattern discovery)
- [x] Metacognitive reflection moment (S.3 — Type 3: Tool/Approach Preference)
- [x] Identity-building closure previews M6 with specific behavioral affirmation
- [x] Total time 6-8 minutes

**Task Coverage:**

- [x] Type D: Representation Transfer — S.1 (same commutative pair across array/table/equations)
- [x] Type A: Pattern Discovery — S.2 (× commutative vs ÷ not — odd one out)
- [x] Metacognitive Reflection — S.3 (tool preference, all-correct MC)
- 2+ task types used (Type D + Type A + Reflection = 3 types) ✓
- [x] At least one active task (S.1, S.2, S.3 are MC selections requiring analysis)

**Alignment:**

- [x] Uses only Toys from Lesson (Arrays display, Multiplication Tables Grid display, Equation Builder display)
- [x] Visual support for every task
- [x] Fresh value: 4 × 9 = 36 (not in Lesson, EC, or Warmup; not in M4)
- [x] S.2 reuses Lesson values (3×5, 2×7) and EC value (18÷6) in a comparison display — deliberate consolidation, not fresh-value violation
- [x] Connections emerge from student experience (three representations from the three Lesson sections; × vs ÷ contrast from S3's discovery)
- [x] No new teaching — consolidates properties already taught
- [x] Strategic implication ("half the table") named after Practice experience per Tension 2

**Constraints:**

- [x] Remediation via Pipeline (light)
- [x] No new procedures introduced
- [x] No new vocabulary introduced
- [x] Closure is behaviorally specific ("You proved... You found... You discovered...")
- [x] M6 bridge matches TVP transition out ("area models... strategies for multiplying larger numbers")
- [x] Every interaction with student action has both Guide: and Prompt:
- [x] **Cross-module check:** M4 Synthesis used Type D (Representation Transfer: array→equations→strategy) + Type A (Pattern Discovery: structural invariant). M5 Synthesis uses Type D (Representation Transfer: array→table→equations) + Type A (Pattern Discovery: × vs ÷ contrast). Same types, different cognitive targets — acceptable.

---

## 1.10 KEY DESIGN DECISIONS

**[REQUIRED]**

### Purpose

KDDs document the non-obvious pedagogical design choices that make this module work. Each entry explains WHAT was decided and WHY this path serves student learning. A reader seeing this module for the first time should understand why it works this way from the KDDs alone.

---

**Proof & Discovery Design**

### KDD-1: Three-Proof Fading Structure (S1)

S1 uses three array rotation proofs with a fading worked-example structure: 1.1 (full — Guide narrates everything, student confirms), 1.2 (partial — briefer narration), 1.3 (prediction — student predicts BEFORE rotation). This follows Lesson Playbook §3's fading protocol. A single proof might not convince; two proofs establish the pattern; the third shifts ownership to the student through prediction. Cutting to two proofs would skip the prediction step, which is where students move from "I saw it" to "I expected it."

### KDD-2: Non-Commutativity Immediately After Commutativity (D9)

S3 tests division non-commutativity immediately after S1-S2 establish commutativity, while both results are cognitively active. Per D9 and SME guidance, the discovery happens during the Lesson, not deferred to Synthesis. Delaying the contrast would allow the overgeneralization (A3: "order never matters") to solidify before being corrected. The paired discovery — works for ×, fails for ÷ — must land as a coherent contrast, not two disconnected facts.

---

**Vocabulary & Scope**

### KDD-3: Informal Naming of Commutativity (D5)

"Commutative" is introduced with the informal definition "order doesn't matter for multiplication" in 1.4, AFTER three visual proofs. Per D5, the primary language throughout is the informal description; the formal term is mentioned lightly. Naming the property formally before the visual grounding would make it an abstract rule to memorize rather than a pattern students discovered.

### KDD-4: Narrow Scope — Commutativity + Non-Commutativity Only (D13)

M5 covers only two ideas: multiplication is commutative, division is not. Per D13 (SME Andrea), the module does NOT extend to distributive property, associative property, or decomposition-based table strategies. These are deferred to M6 where area models provide conceptual support. The narrow scope prevents cognitive overload and keeps the × vs ÷ contrast sharp.

---

**Experience-Before-Naming**

### KDD-5: Experience-Before-Naming in S1 and S2

Both S1 and S2 follow the same pedagogical pattern: students experience the phenomenon multiple times before the Guide names it. S1: three rotation proofs → then "commutative" in 1.4. S2: three partner-finding interactions → then diagonal observation in 2.4. Naming before experience would make the naming feel like a rule; naming after experience makes it feel like recognition. This approach was chosen over restructuring S2 with an early relational pause because the experience-before-naming pattern is consistent across both sections and keeps the naming moment a payoff rather than a setup.

### KDD-6: "Arithmetic Pattern" Placed in 2.4 Dialogue

"Arithmetic pattern" is Assessment Vocabulary per §1.3 but is not a distinct teaching target. It's placed in 2.4's Guide dialogue ("That's an arithmetic pattern in the multiplication table") where the diagonal symmetry is being observed — grounding the term in a concrete visual pattern rather than introducing it as abstract vocabulary. It also appears in §1.2's reinforced vocabulary list to ensure consistent activation across the module.

---

**Representation & Tool Design**

### KDD-7: M4 Callback Value (3 × 5 = 15) as Cross-Module Thread

The Warmup opens with the 3 × 5 = 15 fact family from M4, and S1's first rotation proof uses the same array. This creates a three-module thread: M3 (dual-read) → M4 (fact family) → M5 (commutativity proof). The student sees the same array do different mathematical work in each module. A fresh value would sever this connection and make each module feel isolated.

### KDD-8: Diagonal as Evidence, Not Learning Target

Per §1.5.2 guardrails, the table diagonal is presented as visual evidence for commutativity, not as its own concept. The Guide names it briefly in 2.4 ("like a mirror") without elevating it to a separate teaching target. Students don't need to "learn about diagonals" — they need to see that the table's structure reflects the property they proved with arrays.

---

**Scaffolding & Sequencing**

### KDD-9: S2 Sequencing — Fluent Facts First (PE-4)

S2 sequences partner-finding from fluent facts (2s, 5s in 2.1) through familiar (3s in 2.2) to moderate (4s, 7s in 2.3), with the highest-demand task (reverse-direction product → factors in 2.5) last. This follows TVP guidance: "highlight cells students are fluent with first, then extend." Starting with hard facts would conflate retrieval difficulty with conceptual understanding of commutativity.

### KDD-10: Purpose Frame Simplified to S1-S2 Scope

The Purpose Frame covers only commutativity (S1 array proofs, S2 table symmetry). Division non-commutativity is NOT mentioned — it arrives as a surprise in S3's pivot question (3.1: "Does switching work for division too?"). The simplified framing protects the Purpose Frame's Grade 3 language level and preserves the dramatic contrast when division fails as a genuine discovery moment.

### KDD-11: Think-Aloud Tags as Authoring Annotations

[PLANNING], [ATTENTION], [ACTION], [SELF-CHECK] tags in S1 Guide dialogue are authoring annotations per Lesson Playbook §3A. They mark the metacognitive structure of the worked example for reviewers and scripters, but are stripped before publishing. The Guide dialogue reads naturally without them.

---

## 1.11 FINAL FORMATTING AUDIT

- [ ] All `[vocab]` tags on NEW/status-change terms only; established terms untagged
- [ ] All interaction headers include descriptive label in brackets
- [ ] CRA Stage line present after each §1.7.x section header
- [ ] No development tags remaining in student-facing content (confirm [PLANNING]/[ATTENTION]/[ACTION]/[SELF-CHECK] are authoring annotations per KDD-11)
- [ ] All Prompts are Guide-independent (R1 applied: "commutative partner" removed from Prompts)
- [ ] No gate-review process references in KDD entries (R2 applied)
- [ ] Dimension Tracking table in Working Notes matches SP values
- [ ] Version date updated to reflect final edit date
- [ ] END OF MODULE marker present
- [ ] No placeholder text remaining (search for bracket-wrapped stubs)

---

# END OF MODULE 5 STARTER PACK
