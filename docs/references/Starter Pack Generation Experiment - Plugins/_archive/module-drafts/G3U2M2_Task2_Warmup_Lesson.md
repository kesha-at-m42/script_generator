# M2 TASK 2: WARMUP + LESSON DRAFT

**Version:** 03.13.26 (v2 — Post-Gate 3 Author Review)

**Change Log (v2):**
- Split 1.3 into observe-only (1.3) + student-action (1.4) for gap/overlap symmetry
- Added 1.8 (correct tiling identification) for ternary classification training
- Changed 1.7 (was 1.6) from binary to ternary error ID options
- Fixed 1.2 Guide/Prompt language alignment (both say "gaps")
- Clarified overlap visual descriptions (authored pre-tiled state, not runtime detection)
- Removed 5×5=25 from Section 3 (moved to Practice); renumbered 3.4→3.3, 3.5→3.4
- Added script writer note to W.1 re: distractor design for 3rd graders

---

## WARMUP REQUIREMENTS CHECKLIST (from Warmup Phase Playbook)

- [ ] **Warmup Type:** Notice & Wonder (§4D — recommended for M1-3, visual-rich content, open exploration)
- [ ] **Interaction count:** 2-3 (min 2, max 5)
- [ ] **Hook** in first 15-20 seconds (curiosity gap)
- [ ] **2+ Engagement Anchors** from approved list (Personalization + Curiosity)
- [ ] **1+ Judgment/Noticing Task** requiring thought
- [ ] **Bridge to Lesson** (10-15 sec) creating anticipation without teaching
- [ ] Sequencing: Hook first, bridge last
- [ ] Cognitive load: 20-30%
- [ ] Zero formal vocabulary introduced
- [ ] Maximum 2 visual states
- [ ] Session-relative language only
- [ ] No pressure language, no tool introduction, no complex multi-step instructions

## LESSON REQUIREMENTS CHECKLIST (from Lesson Phase Playbook)

- [ ] **CRA Sequence:** Concrete → Relational → Abstract → Application — each with dedicated interaction(s)
- [ ] **Relational phase is a SEPARATE interaction** (not embedded in vocabulary intro)
- [ ] **Worked examples:** 2-3 minimum with fading (full → partial → independent)
- [ ] **Think-aloud:** 1-2 with tagged elements ([PLANNING], [ATTENTION], [SELF-CHECK])
- [ ] **Example-problem pairs** (Guide demos → student replicates)
- [ ] **Vocabulary staging:** AFTER visual experience, never before (gap, overlap, tiling per §1.3)
- [ ] **Purpose Frame** at Lesson opening (or KDD documenting omission)
- [ ] **Required bookends:** Purpose Frame → first interaction; bridge to EC at end
- [ ] **Active vs Passive:** Student ACTION follows demonstration
- [ ] **6+ total interactions** in Lesson
- [ ] **Guide/Prompt independence** verified (cover one, read the other — does student know what to do?)
- [ ] **Observation (15-30 sec) → explicit instruction** (no extended discovery)
- [ ] All interactions use toys/modes documented in §1.5
- [ ] No forbidden vocabulary in Guide or Prompt lines
- [ ] Remediation: Pipeline (no intensity qualifiers, no authored dialogue)

---

# **1.6 WARMUP (3-5 minutes)**

**[REQUIRED]**

### **Purpose**

Activate the "good tiling" mental model from M1 before introducing what happens when tiling goes wrong. Callback to M1 Synthesis closure (bad tiling with gaps/overlaps) to create continuity. Build curiosity about WHY proper tile placement matters — without teaching the rules.

### **Parameters**

| Parameter | Value |
| :---- | :---- |
| **Duration** | 2-3 minutes |
| **Interactions** | 2 + Bridge |
| **Warmup Type** | Notice & Wonder (§4D) |
| **Cognitive Load** | 20-30% (observation + simple judgment) |
| **Toy** | Grid Rectangles (display mode, full grid, `grid_state: "full"`) |
| **Vocabulary** | M1 terms only (area, tiles, square units). No new formal vocabulary. |

### **Constraints**

| MUST | MUST NOT |
| :---- | :---- |
| Callback to M1 tiling experience | Introduce "gap," "overlap," or "tiling" formally |
| Use Grid Rectangles in display mode only | Use Unit Square Tiles (save for Lesson) |
| Keep tasks single-action | Teach why gaps/overlaps are wrong (save for Lesson) |
| End with anticipation for Lesson | Name or define the errors students see |

### **Warmup Type Rationale**

Notice & Wonder selected because: (1) M2 is Module 2 — early in the sequence, visual-rich content. (2) The TVP specifies students "observe and describe what they notice about how tiles fit" — this maps directly to Notice & Wonder. (3) The Warmup needs to activate recognition of "good" tiling before the Lesson presents "bad" tiling — Notice & Wonder primes this observation skill without teaching.

---

### Interaction W.1: What Do You Notice? [Type C]

* **Purpose:** Activate M1's tiling experience. Students observe a correctly tiled rectangle and describe (via MC) what they notice. Hook: callback to M1 Synthesis — "Last time, you saw something that didn't look right with some tiles. But first — check this one out."
* **Visual: Grid Rectangles (Display).** Full grid. 3×4 rectangle, all 12 squares shaded (representing complete, correct tiling). Horizontal orientation.
* **Guide:** "Last time, you ended by looking at some tiles that didn't fit quite right. But first, check this one out. What do you notice about how these tiles fit together?"
* **Prompt:** "What do you notice about the tiles? Pick one."
* **Student Action:** MC selection
  * **Options:** The tiles fit together with no space between them; Some tiles are on top of each other; There are empty spaces inside the shape; The tiles are different sizes
* **Correct Answer:** The tiles fit together with no space between them
* **Answer Rationale:**
  - "No space between them" = Correct — tiles are edge-to-edge with complete coverage
  - "On top of each other" = Incorrect — no overlaps visible (distractor targets overlap misconception #1.0)
  - "Empty spaces" = Incorrect — no gaps visible (distractor targets gap misconception #1.0)
  - "Different sizes" = Incorrect — all tiles are uniform unit squares (distractor targets unit square understanding)
* **On Correct:** "Every tile fits right next to the others. No space left over."
* **Remediation:** Pipeline

> **Voice Note:** Hook uses Personalization anchor (callback to M1) + Curiosity anchor ("check this one out"). Energy is Medium-High per Warmup voice guidelines. "Last time" uses session-relative language.

> **Design Note:** Engagement Anchors: (1) Personalization — "Last time, you ended by looking at..." callbacks to M1 Synthesis. (2) Curiosity — "check this one out" with a visual that primes the concept. The MC options are designed so each distractor maps to a concept that will be taught in the Lesson (gaps, overlaps, non-uniform tiles), surfacing any pre-existing confusion without correcting it.

> **Script Writer Note:** Three of four W.1 options describe things that aren't visible in the image. For 8-year-olds, evaluating text descriptions against a visual is a subtler cognitive task than it appears — weaker readers may select a plausible-sounding statement rather than evaluating each option. The Guide's "check this one out" language must genuinely direct attention to the visual BEFORE the MC options appear. Consider a brief pause or visual focus cue between the Guide and the MC display. This is low-stakes (Warmup, Pipeline handles remediation), but pacing matters.

---

### Interaction W.2: Same Area, Different Look [Type B]

* **Purpose:** Judgment/noticing task. Students see two correctly tiled rectangles with the SAME area (12 square units) but different dimensions (3×4 and 2×6). Students select which has more area or recognize they're equal. Primes L1 goal: "same number of unit squares = same area."
* **Visual: Grid Rectangles (Display).** Two rectangles shown side by side. Left: 3×4 (horizontal). Right: 2×6 (vertical). Both fully shaded (all squares filled). Full grid visible on both.
* **Guide:** "Here are two rectangles. They look pretty different. Which one covers more space?"
* **Prompt:** "Which rectangle has more area? Select A, B, or Same."
* **Student Action:** MC selection
  * **Options:** A (3×4), B (2×6), Same Area
* **Correct Answer:** Same Area (both are 12 square units)
* **On Correct:** "They look different, but they both have 12 tiles. Same number of tiles, same area."
* **Remediation:** Pipeline

> **Design Note:** This interaction primes the Module Mapping Question/Test Language stem: "These rectangles have the same area — how do you know?" The concept (same number of squares = same area) is SHOWN here but not formally taught — the Warmup activates the observation; the Lesson grounds it. Grid Rectangles spec confirms support for multiple rectangles displayed simultaneously (up to 2 standard, per spec layout constraints).

---

### Bridge to Lesson

* **Purpose:** Create anticipation for Lesson's error presentation. Callbacks to M1 Synthesis ("something that didn't fit right") and pivots to "now let's find out what happens."
* **Visual: Grid Rectangles (Display).** The 3×4 rectangle from W.1 remains on screen.
* **Guide:** "Those tiles fit perfectly. But what if they didn't? What if there were spaces, or tiles piled on top of each other? Let's find out what happens to the count."
* **No student action.**

> **Voice Note:** Bridge creates anticipation ("Let's find out") without teaching ("gaps mean undercounting"). The question in the student's mind: "What DOES happen when tiles don't fit right?" — the Purpose Frame answers this.

---

### Verification Checklist (Warmup)

- [x] Hook in first 15-20 seconds — W.1 opens with M1 callback + "check this one out"
- [x] 2+ engagement anchors — Personalization (M1 callback) + Curiosity ("check this one out")
- [x] 2+ meaningful visual interactions — W.1 (notice correct tiling) + W.2 (compare equal areas)
- [x] 1+ judgment/noticing task — W.2 requires comparison judgment
- [x] Zero formal vocabulary introduced — uses "tiles," "space," "area" (all M1 terms)
- [x] Maximum 2 visual states — W.1 single rectangle; W.2 two rectangles (2 states)
- [x] Clear bridge to Lesson — anticipation created without teaching
- [x] Total time under 5 minutes — 2 interactions + bridge ≈ 2-3 min
- [x] Cognitive load 20-30% — observation and simple MC only

---

# **1.7 LESSON (10-14 minutes)**

**[REQUIRED]**

### **Lesson Requirements Checklist** [REQUIRED]

*(Extracted from Lesson Phase Playbook — each item marked satisfied or flagged after drafting)*

- [x] CRA phases present: Concrete (Section 1: 1.1-1.4), Relational (1.5), Abstract (1.6-1.8), Application (Sections 2-3)
- [x] Relational phase is a SEPARATE dedicated interaction (1.5)
- [x] 2-3 worked examples with fading stages — 3 worked examples (2.1 full, 2.2 partial, 2.3 independent)
- [x] 1-2 think-alouds with tagged elements — 1 think-aloud in 2.1 with [PLANNING], [ATTENTION], [SELF-CHECK]
- [x] Example-problem pairs — 2.1 (Guide demos) → 2.2 (student replicates with partial support)
- [x] Vocabulary after grounding — gap/overlap introduced in 1.2/1.4 AFTER observing concrete errors; tiling in 1.6 AFTER relational bridge
- [x] Purpose Frame present at Lesson opening
- [x] Required bookends — Purpose Frame → first interaction; 3.4 bridges to EC
- [x] Active vs Passive — student ACTION follows demonstration in every section
- [x] 6+ total interactions — 17 interactions total (8 in Section 1, 3 in Section 2, 4 in Section 3 + Purpose Frame)
- [x] Guide/Prompt independence verified on 3+ interactions (see self-check below)
- [x] All interactions use toys from §1.5 (Grid Rectangles + Unit Square Tiles)
- [x] No forbidden vocabulary scanned (see Forbidden Phrases below)
- [x] Remediation: Pipeline throughout

---

### **Core Purpose + Pedagogical Flow**

| Standard CRA Phase | M2 Implementation | Interactions |
| :---- | :---- | :---- |
| **Concrete** | Students observe pre-made tilings with errors (gaps, overlaps) and identify each error type. Symmetrical scaffolding: observe gap → identify gap; observe overlap → identify overlap. They discover that gaps → too few tiles and overlaps → too many tiles by observing the numerical consequences. | 1.1–1.4 |
| **Relational** | Students see all three tiling states (gap, overlap, correct) compared simultaneously. Guide explicitly states the pattern: "No gaps and no overlaps = the right count." Student confirms via MC. | 1.5 |
| **Abstract** | Formal vocabulary introduced: "tiling." Student applies gap/overlap/correct classification in ternary MC — genuine evaluation, not elimination. | 1.6–1.8 |
| **Application** | Students tile rectangles themselves, applying gap/overlap awareness with decreasing support. Worked examples with fading. Self-check routine modeled and practiced. | 2.1–2.3, 3.1–3.4 |

### **Lesson Structure**

| Section | Focus | Approx. Time | Interactions |
| :---- | :---- | :---- | :---- |
| Purpose Frame | Orient to learning + why it matters | 15 sec | (no student action) |
| **Section 1: Understanding the Problem** | Sequential error presentation (Concrete → Relational → Abstract) | 5-6 min | 1.1–1.8 |
| **Section 2: Practicing the Rules (Guided)** | Worked examples, tiling with support, self-check modeling | 3-4 min | 2.1–2.3 |
| **Section 3: Independence with Validation** | Decreasing support, varied orientations, self-check practice | 3-4 min | 3.1–3.4 |

---

### **Purpose Frame**

* **Purpose:** Orient students to what they'll learn and why. Connects backward (M1 tiling) and forward (WHY proper tiling matters for accurate counting).
* **Visual: Grid Rectangles (Display).** Clear state (no rectangle shown — blank canvas).
* **Guide:** "You already know how to cover shapes with tiles and count them. But here's the thing — if tiles don't fit together just right, your count can be wrong. Today you're going to find out exactly what goes wrong, and learn the rules for getting it right every time."
* **No student action.**

> **Design Note:** Purpose Frame uses only M1 vocabulary (tiles, count, shapes). Describes what students will learn to DO (find out what goes wrong, learn the rules). Connects backward (you know how to tile) and forward (but the count can be wrong). Does NOT introduce gap/overlap vocabulary — that comes after concrete experience.

---

## **Section 1: Understanding the Problem** (Concrete → Relational → Abstract)

**CRA Stage: Concrete (1.1–1.4) → Relational (1.5) → Abstract (1.6–1.8)**

**Scaffolding Pattern:** Symmetrical observe→act for each error type. Gaps: 1.1 (observe) → 1.2 (act). Overlaps: 1.3 (observe) → 1.4 (act). This gives each error type equal pacing and landing time, consistent with the Backbone's "build SEPARATE mental models for each error type" principle (TVP SME Decision #3).

---

### Interaction 1.1: The Gap Problem [Type A]

* **Purpose:** First error presentation — students observe a rectangle tiled WITH GAPS and discover the numerical consequence (area count too low). Guide directs attention to empty spaces and explicitly states the problem.
* **Visual: Grid Rectangles (Display).** Full grid. 3×4 rectangle (12 squares total). 10 squares shaded, 2 squares unshaded (gaps) — clearly visible empty grid cells within the rectangle boundary.
* **Guide:** "Here's a rectangle with empty spaces inside. The tiles cover 10 squares, but the whole rectangle is 12 squares. The empty spaces made the count too low."
* **No student action.**

> **Scaffolding Note:** CRA Stage = Concrete (observation). This is a display-only interaction because the student needs to SEE the error and its consequence before being asked to identify it. The Guide explicitly names the numerical discrepancy (10 vs. 12) and the direction of the error (too low). The word "gap" is NOT used yet — it's described as "empty spaces."

---

### Interaction 1.2: What Went Wrong Here? (Gaps) [Type C]

* **Purpose:** Student identifies what's wrong with the gap tiling from 1.1. Formal term "gap" introduced immediately after the concrete observation — vocabulary grounded in experience.
* **Visual: Grid Rectangles (Display).** Same 3×4 rectangle with gaps from 1.1 (10 shaded, 2 unshaded).
* **Guide:** "Those empty spaces have a name — they're called GAPS. A gap is space left uncovered. Gaps made the count too low because some space wasn't counted. How many gaps are there?"
* **Prompt:** "How many gaps are there? Select 1, 2, or 3."
* **Student Action:** MC selection
  * **Options:** 1, 2, 3
* **Correct Answer:** 2
* **Answer Rationale:**
  - 2 = Correct (2 unshaded squares visible in the rectangle)
  - 1 = Incorrect (only counted one gap — likely looked at only part of the rectangle)
  - 3 = Incorrect (overcounted — may have confused edge squares with gaps)
* **On Correct:** "Two gaps. Two squares that didn't get counted! That's why the count was off — 10 instead of 12."
* **Remediation:** Pipeline

> **Scaffolding Note:** CRA Stage = Concrete → transitioning to Abstract. Vocabulary "gap" introduced HERE, immediately after observing the error (1.1). The term attaches to the concrete "empty spaces" the student just saw. Per Lesson Playbook §4A: experience → naming → application.

---

### Interaction 1.3: The Overlap Problem [Type A]

* **Purpose:** Second error presentation — students observe a rectangle tiled WITH OVERLAPS and discover the numerical consequence (area count too high). Display-only to mirror the gap observation pattern (1.1 observe → 1.2 act; 1.3 observe → 1.4 act). This symmetry gives overlaps the same pacing and landing time as gaps.
* **Visual: Grid Rectangles (Display).** Full grid. 3×4 rectangle (12 squares total). All 12 squares shaded PLUS 2 tiles visually stacked/overlapping. Authored pre-tiled state using overlap visual treatment (same color change appearance as runtime overlap detection, for visual consistency). Display mode — no student interaction. Tile count displayed: 14.
* **Guide:** "Now look at this one. See where tiles are stacked on top of each other? The tiles cover 14 squares, but the whole rectangle is only 12 squares. The stacked tiles made the count too high."
* **No student action.**

> **Scaffolding Note:** CRA Stage = Concrete (observation). Mirrors the gap pattern: 1.1 (observe gap) → 1.2 (act on gap); 1.3 (observe overlap) → 1.4 (act on overlap). The word "overlap" is NOT used yet — it's described as "stacked" tiles. The Guide explicitly names the numerical discrepancy (14 vs. 12) and the direction of the error (too high).

> **Engineering Note:** The visual is an authored pre-tiled state, NOT runtime overlap detection. The overlap detection system does not need to be active in display mode. The visual treatment should match the runtime overlap detection appearance (same color change) for visual consistency when students encounter overlaps during tiling later, but this is a static display state.

---

### Interaction 1.4: What Went Wrong Here? (Overlaps) [Type C]

* **Purpose:** Student identifies what's wrong with the overlap tiling from 1.3. Formal term "overlap" introduced immediately after the concrete observation — vocabulary grounded in experience. Mirrors the gap pattern (1.1→1.2).
* **Visual: Grid Rectangles (Display).** Same 3×4 rectangle with overlaps from 1.3 (14 tiles shown, 2 stacked). Authored pre-tiled state using overlap visual treatment (same color change appearance as runtime overlap detection, for visual consistency). Display mode.
* **Guide:** "Those stacked tiles have a name — they're called OVERLAPS. An overlap is a tile on top of another tile. Overlaps made the count too high because some space got counted twice. How many overlaps are there?"
* **Prompt:** "How many overlaps are there? Select 1, 2, or 3."
* **Student Action:** MC selection
  * **Options:** 1, 2, 3
* **Correct Answer:** 2
* **Answer Rationale:**
  - 2 = Correct (2 locations where tiles are stacked)
  - 1 = Incorrect (only identified one overlap)
  - 3 = Incorrect (overcounted)
* **On Correct:** "Two overlaps. Two spaces counted twice. That's why the count was 14 instead of 12 — too high."
* **Remediation:** Pipeline

> **Scaffolding Note:** CRA Stage = Concrete → transitioning to Abstract. Vocabulary "overlap" introduced HERE, immediately after observing the error (1.3). Same pattern as "gap" in 1.1→1.2: experience → naming → application. The term attaches to "stacked tiles" the student just saw.

---

### Interaction 1.5: Correct Tiling — The Pattern [Type C]

**[RELATIONAL PHASE — DEDICATED INTERACTION]**

* **Purpose:** RELATIONAL bridge. Show correct tiling alongside the two error states. Guide explicitly states the pattern: "No gaps and no overlaps = the right count." Student confirms understanding via MC. This is the critical conceptual bridge from observing individual errors to understanding the RULE.
* **Visual: Grid Rectangles (Display).** Three 3×4 rectangles displayed simultaneously (Grid Rectangles spec supports up to 2 standard; 3 confirmed feasible at smaller sizes — AF #4 resolved). Left: gap tiling (10 tiles, labeled "10"). Center: overlap tiling (14 tiles, labeled "14"). Right: correct tiling (12 tiles, labeled "12").
* **Guide:** "Look at all three. Gaps: 10 — too low. Overlaps: 14 — too high. No gaps, no overlaps: 12 — just right. That's how you get the right count."
* **Prompt:** "Which tiling gives the correct area? Select A, B, or C."
* **Student Action:** MC selection
  * **Options:** A (gap tiling — 10), B (overlap tiling — 14), C (correct tiling — 12)
* **Correct Answer:** C (correct tiling — 12)
* **Answer Rationale:**
  - C (correct) = Correct — no gaps, no overlaps, count matches actual area
  - A (gaps) = Incorrect — missing tiles mean uncounted space (#1.0)
  - B (overlaps) = Incorrect — stacked tiles mean double-counted space (#1.0)
* **On Correct:** "No gaps, no overlaps — that's how you know the count is right!"
* **Remediation:** Pipeline

> **Design Note (RELATIONAL):** This is the RELATIONAL interaction per Known Pattern #10. It shows two or more concrete examples simultaneously (all three tiling states), the Guide explicitly states the pattern ("no gaps, no overlaps = right count"), and the student confirms understanding via MC. It exists as a SEPARATE interaction — not embedded in vocabulary introduction.

---

### Interaction 1.6: Naming the Rule [Type A]

* **Purpose:** ABSTRACT phase — formalize vocabulary. Introduce "tiling" as the formal term for covering a shape with no gaps and no overlaps. The term attaches to the concrete-relational experience just completed.
* **Visual: Grid Rectangles (Display).** The correctly tiled 3×4 rectangle from 1.5, displayed alone. Clean, complete coverage visible.
* **Guide:** "When you cover a shape with tiles and there are no gaps and no overlaps — that's called TILING. Good tiling means every square is covered exactly once. And that's the only way to get the right area."
* **No student action.**

> **Scaffolding Note:** CRA Stage = Abstract (vocabulary formalization). "Tiling" introduced AFTER concrete observation (1.1-1.4) and relational comparison (1.5). Per §1.3, this is the planned staging point. The term is simple and maps directly to what students just experienced.

---

### Interaction 1.7: Error Identification Practice — Can You Spot It? [Type C]

* **Purpose:** Student applies gap/overlap/correct classification to a NEW example with ternary options. Three options force genuine evaluation — not elimination. With only two options, a student could use count direction (too low = not overlap) as an elimination strategy without understanding the concept. Three options mean the student must evaluate whether there's an error at all AND what type.
* **Visual: Grid Rectangles (Display).** Full grid. 4×3 rectangle (vertical orientation — change from horizontal to build flexibility). 11 squares shaded, 1 gap visible. Area labeled "11 tiles."
* **Guide:** "Here's another rectangle. Someone tiled it, but the count says 11. The real area is 12. What's going on?"
* **Prompt:** "What's wrong with this tiling? Select Gap, Overlap, or Correct."
* **Student Action:** MC selection
  * **Options:** Gap, Overlap, Correct — no errors
* **Correct Answer:** Gap
* **Answer Rationale:**
  - Gap = Correct — there's an uncovered square, count is too low (11 < 12)
  - Overlap = Incorrect — overlaps make the count too HIGH, not too low. The count is 11 (below 12), confirming it's a gap.
  - Correct — no errors = Incorrect — the count doesn't match the area (11 ≠ 12), so there IS an error.
* **On Correct:** "A gap — one square wasn't covered, so the count came up short."
* **Remediation:** Pipeline

> **Design Note:** Ternary options (Gap / Overlap / Correct) require genuine evaluation. This trains the classification that EC will test. Vertical orientation provides variety from 1.1–1.5 (all horizontal). The numerical reasoning (11 < 12 = too low = gap) reinforces the Concrete phase learning.

---

### Interaction 1.8: Error Identification Practice — Is This One Right? [Type C]

* **Purpose:** Student evaluates a correctly tiled rectangle and confirms "no errors." This is critical: without practicing the "nothing's wrong" answer, students learn that every tiling shown in identification format has something wrong — a cueing pattern that undermines genuine evaluation in EC.
* **Visual: Grid Rectangles (Display).** Full grid. 3×3 rectangle (square orientation). 9 squares shaded, no gaps, no overlaps. Area labeled "9 tiles."
* **Guide:** "One more. This one says 9 tiles, and the real area is 9. What do you think?"
* **Prompt:** "Is there a problem with this tiling? Select Gap, Overlap, or Correct."
* **Student Action:** MC selection
  * **Options:** Gap, Overlap, Correct — no errors
* **Correct Answer:** Correct — no errors
* **Answer Rationale:**
  - Correct — no errors = Correct — all squares covered, no stacking, count matches area (9 = 9)
  - Gap = Incorrect — no empty squares visible, count matches area
  - Overlap = Incorrect — no stacked tiles visible, count matches area
* **On Correct:** "No gaps, no overlaps — the count matches. This tiling is correct."
* **Remediation:** Pipeline

> **Design Note:** This completes the ternary classification training. Students have now practiced: identifying a gap (1.7), and confirming correct tiling (1.8). Combined with overlap identification in 1.4, all three classification outcomes are trained before EC. The 3×3=9 rectangle is small and quick — this is a judgment task, not a visual search task.

---

## **Section 2: Practicing the Rules (Guided Tiling)**

**CRA Stage: Application — students tile rectangles with gap/overlap awareness**

---

### Interaction 2.1: Worked Example — Tiling a Rectangle [Type A → Type C multi-step]

* **Purpose:** FIRST worked example with think-aloud. Guide demonstrates tiling a 3×4 rectangle step by step, modeling the self-check routine. Then student tiles a similar rectangle. Example-problem pair structure.

#### 2.1a: Guide Demonstration (Worked Example #1 — Full) [Type A]

* **Purpose:** Guide models complete tiling process with think-aloud.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 3×4 empty rectangle with full grid visible. Tile bank with exactly 12 tiles (exact match supply). System demonstrates Guide placing tiles via animation.
* **Guide:** "[PLANNING] Let me show you how I tile this rectangle. First, I ask myself: what do I need to do? I need to cover every square — no gaps, no overlaps. [ATTENTION] I'll start in this corner and work across the row. [ACTION — system animates tiles being placed row by row] One, two, three, four — that's the first row. Now the second row... [SELF-CHECK] Before I say I'm done, let me check. Any gaps? I look for empty squares... none. Any overlaps? I look for stacked tiles... none. Every square is covered once. The area is 12 square units."
* **No student action.** (Guide demonstration)

> **Scaffolding Note:** CRA Stage = Application, Scaffolding Stage = Full Worked Example. Think-aloud tags: [PLANNING] (what do I need to do?), [ATTENTION] (start in corner, work across), [SELF-CHECK] (any gaps? any overlaps?). The self-check routine is MODELED here — students will be prompted to use it starting in 2.2.

---

#### 2.1b: Your Turn — Tile This Rectangle [Type C]

* **Purpose:** Student replicates what Guide demonstrated. Example-problem pair: same dimensions (2×5 — similar complexity to 3×4) so the task structure is familiar but values differ.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 2×5 empty rectangle with full grid visible. Tile bank with exactly 10 tiles (exact match supply). Overlap detection active (color change + audio). Completion feedback: immediate (Scaffolding Stage 1).
* **Guide:** "Your turn. Tile this rectangle — cover every square with no gaps and no overlaps. Then count your tiles and tell me the area."
* **Prompt:** "Drag tiles to cover the rectangle. No gaps, no overlaps. Then select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 8, 10, 12
* **Correct Answer:** 10 square units (2×5 = 10)
* **On Correct:** "10 square units. Every square covered, nothing stacked. That's good tiling."
* **Remediation:** Pipeline

> **Scaffolding Note:** Scaffolding Stage = Full support. Exact tile supply (no surplus to manage). Overlap detection always active. Completion feedback is immediate — system confirms area count right away. This is the first time students tile in M2 with the full grid visible (M1 had no grid on targets).

---

### Interaction 2.2: Guided Tiling with Self-Check Prompt (Worked Example #2 — Partial) [Type C]

* **Purpose:** Second worked example — PARTIAL. Student tiles, Guide prompts self-check before submission. Scaffolding fades: Guide no longer demonstrates, but still prompts the self-check routine.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 4×4 empty rectangle with full grid visible. Tile bank with exactly 16 tiles (exact match supply). Overlap detection active. Completion feedback: submit-only (Scaffolding Stage 2 — feedback after student submits, not immediate).
* **Guide:** "Tile this rectangle. When you think you're done, check first — any gaps? Any overlaps? Then count your tiles."
* **Prompt:** "Drag tiles to cover the rectangle. Check for gaps and overlaps before selecting the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 14, 16, 18
* **Correct Answer:** 16 square units (4×4 = 16)
* **On Correct:** "16 square units. You checked, and it's right."
* **Remediation:** Pipeline

> **Scaffolding Note:** Scaffolding Stage = Partial worked example. Guide PROMPTS the self-check ("check first — any gaps? any overlaps?") but does NOT model it step-by-step as in 2.1a. Student performs the check independently. Completion feedback shifts to submit-only — student must submit before getting confirmation. This is the first fading step.

---

### Interaction 2.3: Guided Tiling — Less Support (Worked Example #3 — Minimal) [Type B]

* **Purpose:** Third worked example — MINIMAL support. Brief instruction, student tiles and self-checks independently. Continued fading.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 3×3 empty rectangle with full grid visible. Tile bank with exactly 9 tiles. Overlap detection active. Completion feedback: submit-only.
* **Guide:** "One more. You know what to do."
* **Prompt:** "Drag tiles to cover the rectangle. Select the area when done."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 7, 9, 11
* **Correct Answer:** 9 square units (3×3 = 9)
* **On Correct:** "9 square units."
* **Remediation:** Pipeline

> **Scaffolding Note:** Scaffolding Stage = Minimal support. Guide instruction is brief (Type B). Self-check is expected but not prompted — student has heard the routine in 2.1a (modeled) and 2.2 (prompted). This completes the fading arc: Full → Partial → Minimal.

---

## **Section 3: Independence with Validation**

**CRA Stage: Application — independent practice with decreasing support**

---

### Interaction 3.1: Independent Tiling — Surplus Tiles [Type B]

* **Purpose:** First independent tiling with surplus tiles. Student must judge completeness without exact tile count as a crutch.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 2×6 empty rectangle (vertical orientation) with full grid visible. Tile bank with 15 tiles (surplus — 3 extra). Overlap detection active. Completion feedback: self-check before submit (Scaffolding Stage 3 — no system feedback until EC).
* **Guide:** "There are extra tiles this time. Tile the rectangle — use only what you need."
* **Prompt:** "Drag tiles to cover the rectangle. Select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 10, 12, 15
* **Correct Answer:** 12 square units (2×6 = 12)
* **On Correct:** "12 square units. You used exactly what you needed."
* **Remediation:** Pipeline

> **Scaffolding Note:** First use of surplus tiles (from exact match in Section 2 to modest surplus here). Vertical orientation introduced. Self-check before submit — student is expected to check independently. No system feedback on completion accuracy until EC.

---

### Interaction 3.2: Independent Tiling — Horizontal [Type B]

* **Purpose:** Continued independent practice. Different dimensions, horizontal orientation.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 5×3 empty rectangle (horizontal) with full grid visible. Tile bank with 18 tiles (surplus — 3 extra). Overlap detection active. No completion feedback.
* **Guide:** "Tile this rectangle. Before you submit — any gaps? Any overlaps?"
* **Prompt:** "Drag tiles to cover the rectangle. Select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 13, 15, 18
* **Correct Answer:** 15 square units (5×3 = 15)
* **On Correct:** "15 square units."
* **Remediation:** Pipeline

---

### Interaction 3.3: Independent Tiling — Small and Fast [Type B]

* **Purpose:** Quick, small rectangle for confidence-building before EC bridge. Brisk pacing.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 2×4 empty rectangle (horizontal) with full grid visible. Tile bank with 10 tiles (surplus). Overlap detection active. No completion feedback.
* **Guide:** "One more."
* **Prompt:** "Drag tiles to cover the rectangle. Select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 6, 8, 10
* **Correct Answer:** 8 square units (2×4 = 8)
* **On Correct:** "8 square units."
* **Remediation:** Pipeline

---

### Interaction 3.4: Bridge to Exit Check [Type A]

* **Purpose:** Transition from Lesson to EC. Brief, confident tone. Signals shift from learning to assessment.
* **Visual: Grid Rectangles (Display).** Blank (clear state).
* **Guide:** "You've got the rules down — no gaps, no overlaps, and the count is right. Let's see what you know."
* **No student action.**

---

### **Required Phrases**

| Phrase | Where Used |
| :---- | :---- |
| "No gaps, no overlaps" | 1.5 (pattern statement), 2.1a (self-check), bridge |
| "Gaps make the count too low" | 1.1, 1.2 |
| "Overlaps make the count too high" | 1.3, 1.4 |
| "That's called tiling" | 1.6 |
| "Any gaps? Any overlaps?" | 2.1a (modeled), 2.2 (prompted), 3.2 (independent) |

### **Forbidden Phrases**

| Phrase | Why | Module |
| :---- | :---- | :---- |
| rows / columns | M3 vocabulary | M3 |
| skip-count / skip-counting | M3 | M3 |
| multiply / multiplication | M5 | M5 |
| formula / length × width | M7+ | M7+ |
| perimeter | Decision #5 | N/A |
| square centimeters / square inches / etc. | M5-M6 | M5-M6 |
| array | Decision #4 | M3+ |

**Forbidden Phrase Scan:** All Guide: and Prompt: lines in §1.6-§1.7 have been checked. No forbidden phrases found.

---

### **Module-Specific Lesson Guidance**

**Sequential Error Presentation with Symmetrical Scaffolding:** The TVP specifies and the SME resolved: present gaps FIRST (1.1-1.2), then overlaps (1.3-1.4), then correct tiling (1.5). This builds distinct mental models for each error type before combining them. Do NOT present gaps and overlaps simultaneously in the first exposure. Each error type gets the same observe→act pacing: 1.1 observe gap → 1.2 identify gap; 1.3 observe overlap → 1.4 identify overlap. A script writer following this pattern should write both error sections at the same pace.

**Ternary Error Classification:** Error identification interactions (1.7, 1.8) use three options: Gap, Overlap, Correct — no errors. This trains genuine evaluation (is there an error? what type?) rather than binary elimination. Students practice all three outcomes before EC tests identification.

**Self-Check Routine Fading:**
1. 2.1a — Guide MODELS ("Let me check. Any gaps? ...Any overlaps? ...")
2. 2.2 — Guide PROMPTS ("Check first — any gaps? Any overlaps?")
3. 3.1+ — Student PERFORMS independently (Guide may give brief reminder in 3.2 but does not model)

**Overlap Detection vs. Gap Awareness:**
- Overlap detection is MECHANICAL (always-on visual + audio feedback from Unit Square Tiles). It catches the error automatically.
- Gap awareness is CONCEPTUAL (taught in Section 1, practiced via self-check in Sections 2-3). There is no "gap detection" system — the full grid makes gaps visible, but the student must LOOK for them.
- This asymmetry is intentional: overlap correction is motor-level (snap behavior), gap prevention is cognitive-level (planning + checking).

---

### **Misconception Prevention**

**#1.0: Gaps/Overlaps Acceptable (PRIMARY)**
- **Where surfaced:** Throughout Lesson — students who don't check coverage quality
- **Prevention:** Section 1 makes the NUMERICAL consequences visible (gaps = too few, overlaps = too many). This converts the misconception from "tiles don't have to be perfect" to "imperfect tiling = wrong count." The self-check routine ("Any gaps? Any overlaps?") is the internalized prevention strategy.
- **Observable behavior for remediation:** Student submits tiling with visible gaps and doesn't self-correct before submission. Pipeline handles remediation.

**#9.0: Array Structure Not Seen (PREVIEW)**
- **Where surfaced:** Sections 2-3 — students count one-by-one rather than by rows
- **Prevention:** NOT a prevention target in M2. One-by-one counting is expected and appropriate. If student spontaneously counts by rows, Guide can acknowledge ("You found a pattern!") without formally teaching.

---

### **Incomplete Script Flags (§1.7.4)**

- ⚠️ **MC Area Options:** The specific MC options for area in each tiling interaction (2.1b–3.3) are drafted with plausible distractors based on common counting errors (±2 of correct answer). Pipeline should generate contextually appropriate distractors if these are modified during engineering.
- ⚠️ **Multi-step Interaction 2.1:** The worked example (2.1a) uses system animation to show Guide placing tiles. Engineering must confirm animation capability for step-by-step tile placement demonstration.
- ⚠️ **Three Simultaneous Rectangles in 1.5:** Author confirmed feasible (AF #4 resolved). Engineering should confirm rendering at smaller sizes.
- ⚠️ **Overlap Visual in Display Mode (1.3, 1.4):** These interactions use an authored pre-tiled state, NOT runtime overlap detection. The visual treatment should match the runtime overlap detection appearance (same color change) for consistency, but the overlap detection system itself does not need to be active. Script writer and engineer: this is a static display state.

---

### **Success Criteria (§1.7.5)**

Students who complete the Lesson successfully can:
1. Identify gaps in a pre-made tiling and explain why they make the area count too low
2. Identify overlaps in a pre-made tiling and explain why they make the area count too high
3. Use the terms "gap," "overlap," and "tiling" correctly
4. Classify a tiling as having a gap, an overlap, or no errors (ternary evaluation)
5. Tile a rectangle with no gaps and no overlaps using drag-to-place
6. State the area in square units after tiling
7. Perform a self-check ("Any gaps? Any overlaps?") before submitting

---

### **Verification Checklist (Lesson)**

**CRA Structure:**
- [x] Concrete phase (1.1-1.4): symmetrical observe→act for each error type
- [x] Relational phase (1.5): comparison + explicit pattern-stating — DEDICATED interaction
- [x] Abstract phase (1.6-1.8): vocabulary + ternary classification practice
- [x] Application phase (2.1-3.3): increasing independence

**Worked Examples:**
- [x] 3 worked examples with fading: 2.1 (full), 2.2 (partial), 2.3 (minimal)
- [x] Think-aloud in 2.1a with [PLANNING], [ATTENTION], [SELF-CHECK]
- [x] Example-problem pairs: 2.1a (demo) → 2.1b (student attempt)

**Vocabulary:**
- [x] "gap" introduced in 1.2 (AFTER observing gap error in 1.1)
- [x] "overlap" introduced in 1.4 (AFTER observing overlap error in 1.3)
- [x] "tiling" introduced in 1.6 (AFTER relational comparison in 1.5)
- [x] No formal vocabulary in Warmup or before visual grounding

**Scaffolding Symmetry:**
- [x] Gaps: observe (1.1) → identify (1.2) — 2 interactions
- [x] Overlaps: observe (1.3) → identify (1.4) — 2 interactions
- [x] Equal pacing for each error type ✓

**Ternary Classification:**
- [x] 1.7: Gap error with Gap/Overlap/Correct options (answer: Gap)
- [x] 1.8: Correct tiling with Gap/Overlap/Correct options (answer: Correct)
- [x] All three classification outcomes trained before EC ✓

**Guide/Prompt Independence (spot-checked 3 interactions):**
- [x] 1.2: Cover Guide → "How many gaps are there? Select 1, 2, or 3." ✓ Student knows task.
- [x] 2.1b: Cover Guide → "Drag tiles to cover the rectangle. No gaps, no overlaps. Then select the area." ✓ Student knows task.
- [x] 3.1: Cover Prompt → Guide says "There are extra tiles this time. Tile the rectangle — use only what you need." ✓ Student knows task.

**Data Constraints:**
- [x] All rectangles within 2-6 per side (2×4, 2×5, 2×6, 3×3, 3×4, 4×3, 4×4, 5×3)
- [x] All areas within 6-25 (8, 9, 10, 12, 15, 16)
- [x] Both horizontal and vertical orientations used
- [x] Square orientation included (3×3, 4×4)

**Toys:**
- [x] Grid Rectangles: Display (Section 1, bridge) + Target (Sections 2-3)
- [x] Unit Square Tiles: Drag-to-place (Sections 2-3 only)
- [x] No toys used outside §1.5 specification
