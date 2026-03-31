# M2 TASK 3: EXIT CHECK + PRACTICE INPUTS + SYNTHESIS + KDD

**Version:** 03.13.26 (v2 — Post-Gate 3 Author Review)

**Change Log (v2):**
- EC.2: Added "Correct — no errors" third option to match Lesson's ternary classification training
- S.2: Redesigned to use Grid Rectangles capabilities (not custom illustrations)
- §1.8.5: Added S4 assessment note (H3 resolution), added 5×5=25 as Practice candidate
- §1.10: Updated KDDs #1, #5, #7; added KDDs #16, #17 (flagged not SME reviewed)

---

## EC REQUIREMENTS CHECKLIST (from Exit Check Phase Playbook)

- [ ] **Problem count:** 3 standard (expand to 5 if needed)
- [ ] **Cognitive types:** Modules 1-3 → CREATE and IDENTIFY only
- [ ] **Sequencing:** Simple to complex, all testing SAME concept from Lesson
- [ ] **Alignment:** Every problem maps to a Lesson section with same toy, mode, interaction type
- [ ] **No new content:** No new visual models, interaction types, vocabulary, or concepts
- [ ] **Difficulty:** Representative middle (not too easy, not too hard)
- [ ] **Transition frame** at start (low-stakes, no pressure)
- [ ] **Feedback:** Brief, specific (5-10 words), neutral
- [ ] **Values differ** from Lesson values (except documented KDD reuse)
- [ ] **Same visual models** as Lesson
- [ ] **Same orientations** demonstrated in Lesson (both horizontal and vertical were used)
- [ ] **Different cognitive types** across problems
- [ ] **Ternary options** for IDENTIFY problems match Lesson training (Gap/Overlap/Correct)

## SYNTHESIS REQUIREMENTS CHECKLIST (from Synthesis Phase Playbook)

- [ ] **Interaction count:** 3-4 for Early Modules (1-3)
- [ ] **Required elements:** Opening Frame (30-45 sec), Connection Tasks (4-5 min), Metacognitive Reflection (1-2 min), Identity-Building Closure (30 sec)
- [ ] **Task type diversity:** Minimum 2 different types from: Pattern Discovery, Representation Transfer, Real-World Bridge, Metacognitive Reflection
- [ ] **Preferred types for Early Modules:** Type A (Pattern Discovery) + Type C (Real-World Bridge)
- [ ] **Metacognitive reflection:** 1 per Synthesis, after tasks before closure. Prefer Type 1 (Strategy Identification) or Type 3 (Tool Preference) for Modules 1-6
- [ ] **Timing:** 6-8 minutes total
- [ ] **Remediation:** Light only (mastery assumed)
- [ ] **Cognitive load:** Post-fatigue phase — efficient, varied, rewarding
- [ ] **Closure:** Behaviorally specific, previews next module, no generic praise
- [ ] **Zero new teaching or procedures**
- [ ] **Visual support** for every task — using only toys from Lesson

---

# **1.8 EXIT CHECK (3-5 minutes)**

**[REQUIRED]**

### **Purpose**

Verify Lesson understanding before Practice. Tests whether student can (1) tile a rectangle with no gaps and no overlaps using drag-to-place and state the area, (2) identify whether a pre-made tiling has a gap, an overlap, or is correct (ternary classification).

### **Parameters**

| Element | Specification |
| :---- | :---- |
| **Problems** | 3 |
| **Cognitive Types** | CREATE (EC.1, EC.3) + IDENTIFY (EC.2) |
| **Time** | 3-5 minutes |
| **Tone** | Calm, low-stakes |
| **Remediation** | Pipeline |

### **Constraints**

| MUST | MUST NOT |
| :---- | :---- |
| Use Grid Rectangles (target + display) as in Lesson | Introduce new visual models |
| Use Unit Square Tiles (drag-to-place) as in Lesson | Add new interaction types (no drag-to-snap, no free draw) |
| Use MC for area selection and error identification | Add new vocabulary not taught in Lesson |
| Stay within dimensions 2-6, areas 6-25 | Increase complexity beyond Lesson (no dimensions >6) |
| Use both horizontal and vertical orientations (both appeared in Lesson) | Test skills not explicitly taught (no structured counting, no row language) |
| Use ternary options for IDENTIFY problems (Gap/Overlap/Correct) | Use binary options that reduce evaluation to elimination |

### **Alignment Check**

| Problem | Tests | Cognitive Type | Lesson Source |
| :---- | :---- | :---- | :---- |
| EC.1 | Tile rectangle + state area | CREATE | Section 2 (Guided Tiling) + Section 3 (Independent Tiling) |
| EC.2 | Identify error type OR confirm correct tiling (ternary) | IDENTIFY | Section 1 (Error Presentation + 1.7-1.8 Error Identification) |
| EC.3 | Tile rectangle + state area | CREATE | Section 3 (Independent Tiling) |

---

### **Transition into Exit Check**

* **Purpose:** Signal shift from Lesson to low-stakes assessment. Reuse 3.4 bridge from Lesson.
* **Visual: Grid Rectangles (Display).** Clear state.
* **Guide:** "You've got the rules down — no gaps, no overlaps, and the count is right. Let's see what you know."
* **No student action.**

> **Design Note:** The Lesson already ends with interaction 3.4 (Bridge to EC) which serves as the transition frame. The above is included for structural completeness — in production, 3.4 and the EC transition are the same moment.

---

### Interaction EC.1: Tile and Count [Type C]

* **Purpose:** Test CREATE skill — can student tile a rectangle with no gaps/overlaps and state the area? Uses dimensions NOT used in Lesson tiling interactions.
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 3×5 empty rectangle (horizontal) with full grid visible. Tile bank with 18 tiles (surplus). Overlap detection active. No completion feedback.
* **Guide:** "Tile this rectangle. No gaps, no overlaps. Then tell me the area."
* **Prompt:** "Drag tiles to cover the rectangle. Select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 13, 15, 18
* **Correct Answer:** 15 square units (3×5 = 15)
* **Answer Rationale:**
  - 15 = Correct (3×5 = 15, complete tiling)
  - 13 = Incorrect (undercounting — may have missed tiles or counted gaps as empty)
  - 18 = Incorrect (tile bank count, not rectangle area — student counted supply instead of coverage)
* **On Correct:** "15 square units."
* **Remediation:** Pipeline

> **Design Note:** 3×5=15 was NOT used as a tiling dimension in the Lesson (Lesson used 3×4, 2×5, 4×4, 3×3, 2×6, 5×3, 2×4). Horizontal orientation matches multiple Lesson interactions. Surplus tiles test judgment — student must stop at 15, not use all 18.

---

### Interaction EC.2: What's Wrong? [Type C]

* **Purpose:** Test IDENTIFY skill — can student classify a pre-made tiling using ternary evaluation (gap / overlap / correct)? Uses a new rectangle with an overlap error (Lesson 1.7 tested gap identification; EC.2 tests overlap identification for variety). Three options match Lesson training (1.7-1.8).
* **Visual: Grid Rectangles (Display).** Full grid. 5×2 rectangle (vertical orientation). All 10 squares shaded PLUS 1 tile visually stacked/overlapping (authored pre-tiled state using overlap visual treatment). Tile count displayed: 11.
* **Guide:** "Someone tiled this rectangle, but the count says 11. The real area is 10. What went wrong?"
* **Prompt:** "What's the problem? Select Gap, Overlap, or Correct."
* **Student Action:** MC selection
  * **Options:** Gap, Overlap, Correct — no errors
* **Correct Answer:** Overlap
* **Answer Rationale:**
  - Overlap = Correct — 11 > 10, count is too HIGH, meaning a space was double-counted (overlap)
  - Gap = Incorrect — gaps make the count too LOW (less than actual area), but 11 > 10 (#1.0)
  - Correct — no errors = Incorrect — the count doesn't match the area (11 ≠ 10), so there IS an error
* **On Correct:** "An overlap — one space counted twice."
* **Remediation:** Pipeline

> **Design Note:** 5×2=10 was NOT used in Lesson Section 1 error presentations (those used 3×4=12 and 4×3=12). Vertical orientation provides variety. Overlap error chosen because Lesson 1.7 tested gap identification — EC.2 tests the other error type for balanced assessment. Ternary options (Gap/Overlap/Correct) match Lesson training in 1.7-1.8, preventing the binary elimination problem where students could use count direction alone to answer.

---

### Interaction EC.3: Tile Another [Type C]

* **Purpose:** Second CREATE test — confirms tiling skill with a different rectangle. Vertical orientation (different from EC.1's horizontal).
* **Visual: Grid Rectangles (Target) + Unit Square Tiles (Drag-to-Place).** 4×5 empty rectangle (vertical) with full grid visible. Tile bank with 24 tiles (surplus). Overlap detection active. No completion feedback.
* **Guide:** "One more. Tile it, and tell me the area."
* **Prompt:** "Drag tiles to cover the rectangle. Select the area."
* **Student Action:** Drag-to-place tiles, then MC selection for area
  * **Options (area):** 18, 20, 24
* **Correct Answer:** 20 square units (4×5 = 20)
* **Answer Rationale:**
  - 20 = Correct (4×5 = 20, complete tiling)
  - 18 = Incorrect (undercounting — may have miscounted or left unnoticed gap)
  - 24 = Incorrect (tile bank count — counted supply instead of coverage)
* **On Correct:** "20 square units."
* **Remediation:** Pipeline

> **Design Note:** 4×5=20 was NOT used in Lesson tiling interactions. Vertical orientation provides balance (EC.1 horizontal, EC.3 vertical). Area 20 is within range and larger than EC.1's 15, providing simple-to-complex progression within CREATE type. Tile bank surplus (24) tests the same judgment as EC.1 — student must stop at the right count.

---

### **Verification Checklist (Exit Check)**

**Structure:**

- [x] 3 problems testing 2 distinct skills (tiling + error identification)
- [x] Each problem maps to a Lesson section (see Alignment Check)
- [x] Transition frame at start (low-stakes)
- [x] Total time 3-5 minutes

**Alignment:**

- [x] All visual models appeared in Lesson (Grid Rectangles display + target, Unit Square Tiles)
- [x] All interaction types appeared in Lesson (drag-to-place, MC selection)
- [x] All values within Lesson constraints (dimensions 2-6, areas 6-25)
- [x] No skill tested that wasn't explicitly taught
- [x] Different cognitive types across problems (CREATE: EC.1, EC.3; IDENTIFY: EC.2)
- [x] Ternary options match Lesson training (1.7-1.8) ✓

**Constraints:**

- [x] No new vocabulary introduced
- [x] No new visual models introduced
- [x] No complexity increase beyond Lesson (EC dimensions within Lesson range)
- [x] Every interaction has both Guide: and Prompt:

**Value Separation:**

- [x] EC.1 (3×5=15): NOT used in Lesson tiling ✓
- [x] EC.2 (5×2=10): NOT used in Lesson error displays ✓
- [x] EC.3 (4×5=20): NOT used in Lesson tiling ✓

---

# **1.8.5 PRACTICE PHASE INPUTS**

**[REQUIRED]**

### **Skill Tracking**

| Skill ID | Description | Cognitive Type | Lesson Source |
| :---- | :---- | :---- | :---- |
| S1 | Tile a rectangle with no gaps and no overlaps using drag-to-place | CREATE | Sections 2-3 |
| S2 | State the area in square units after tiling | CREATE | Sections 2-3 |
| S3 | Identify whether a pre-made tiling has a gap, overlap, or is correct (ternary) | IDENTIFY | Section 1 (1.2, 1.4, 1.7, 1.8) |
| S4 | Apply self-check routine before submitting ("Any gaps? Any overlaps?") | CREATE (embedded) | Sections 2-3 (modeled 2.1a, prompted 2.2, independent 3.1+) |

> **Note:** S1 and S2 always occur together (tile then count). S4 is embedded in S1/S2 — not a separate problem type, but an expected behavior during tiling. S3 is a separate MC-based skill using ternary options (Gap/Overlap/Correct).

> **S4 Assessment Note (H3 Resolution):** S4 (self-check routine) is scaffolded via prompt structure, not independently assessed by Pipeline. There is no telemetry or metric that detects whether a student actually self-checks before submitting. The self-check is encouraged through the Lesson's fading arc (modeled → prompted → independent) and through prompt language that reminds students to check. Practice can continue to include prompt-level encouragement ("Check before you submit") but should not treat S4 as a discrete, scoreable skill. Pipeline remediation triggers are based on S1 (gap/overlap in submitted tiling) and S2 (incorrect area count), not on whether the student performed a self-check.

### **Distribution Targets**

| Skill | Target Distribution | Rationale |
| :---- | :---- | :---- |
| S1+S2 (Tile + Count) | ~65% of problems | Primary skill — most Practice time on tiling with gap/overlap awareness |
| S3 (Error Identification — ternary) | ~25% of problems | Secondary skill — MC identification of gap vs. overlap vs. correct in pre-made tilings |
| Mixed (S1+S2 with error correction) | ~10% of problems | Student tiles a rectangle that has a pre-existing partial tiling with an error — must fix then complete |

### **Toy Constraints for Practice**

Same as Lesson:
- Grid Rectangles: Target mode (for tiling) + Display mode (for error identification)
- Unit Square Tiles: Drag-to-place, overlap detection always active
- Grid state: Full grid always visible
- Tile supply: Surplus (never exact match in Practice — student must judge completeness)
- Feedback: No completion feedback (self-check expected)

### **Data Constraints for Practice**

| Constraint | Value |
| :---- | :---- |
| Dimensions per side | 2-6 (same as Lesson) |
| Area range | 6-25 square units |
| Orientations | Both horizontal and vertical, including square |
| Error types for S3 | Mix of gap, overlap, AND correct tilings (ternary — include "no error" problems) |
| New dimension combinations | Use combinations NOT in Lesson or EC where possible |

### **Dimensions Used (from Working Notes)**

Already used in Lesson: 3×4, 2×5, 4×4, 3×3, 2×6, 5×3, 2×4, 4×3
Already used in EC: 3×5, 5×2, 4×5

**Available unused combinations (within 2-6 per side, area 6-25):** 2×3=6, 3×2=6, 3×6=18, 4×2=8, 4×6=24, 5×4=20, 6×2=12, 6×3=18, 6×4=24

**Available for Practice:** 2×3, 3×6, 4×2, 4×6, 6×2, 6×3, 6×4 (plus reuse of Lesson/EC values with documentation)

**5×5=25 for Practice:** The 5×5=25 rectangle was removed from Lesson Section 3 due to pacing constraints (25 drag actions for an 8-year-old exceeds Section 3's time budget). 5×5=25 is appropriate for Practice where pacing is flexible and the upper boundary of the TVP data constraint range should still be exercised. Include 5×5=25 as a Practice problem in the S1+S2 category.

### **Cross-Module Skill References**

**M1 Skills for Spiral Review:**
* M1: Tile shapes (including non-rectangular) with unit squares and count to find area — no gap/overlap rule awareness required. Uses Plane Figures (not Grid Rectangles).

> **Note:** M1 spiral review in Practice would require Plane Figures toy (not used in M2). If Practice phase supports cross-toy spiral, include M1 tiling of non-rectangular shapes. If Practice is single-toy, omit M1 spiral and note as limitation.

---

# **1.9 SYNTHESIS (6-8 minutes)**

**[REQUIRED]**

### **Purpose**

Consolidate the "no gaps, no overlaps" rule by connecting it to pattern recognition and real-world contexts. Activate rectangle vocabulary from Grade 2. Preview M3's structured counting through the bridge.

---

### Opening Frame

* **Purpose:** Signal shift from assessment to reflection. Warm, connecting tone.
* **Visual: Grid Rectangles (Display).** A correctly tiled 3×4 rectangle (12 squares, all shaded). Full grid visible.
* **Guide:** "You tiled rectangles, you found errors, you got the count right every time. Now let's step back and see the big picture."
* **No student action.**

---

### Interaction S.1: Which Ones Follow the Rule? — Pattern Discovery (Type A)

* **Purpose:** Rule consolidation. Students see 4 tilings and identify which 3 follow the "no gaps, no overlaps" rule. Surfaces the core principle as a recognizable pattern across multiple examples.
* **Visual: Grid Rectangles (Display).** Four rectangles displayed in a 2×2 grid:
  - Top-left: 2×3 rectangle, correctly tiled (6 squares shaded). Labeled "6 tiles."
  - Top-right: 3×4 rectangle with 1 gap (11 shaded, 1 empty). Labeled "11 tiles."
  - Bottom-left: 4×3 rectangle, correctly tiled (12 squares shaded). Labeled "12 tiles."
  - Bottom-right: 2×5 rectangle, correctly tiled (10 squares shaded). Labeled "10 tiles."
* **Guide:** "Look at these four rectangles. Three of them are tiled the right way. One has a problem. Which one doesn't follow the rule?"
* **Prompt:** "Which tiling has a problem? Select A, B, C, or D."
* **Student Action:** MC selection
  * **Options:** A (top-left, 2×3 correct), B (top-right, 3×4 gap), C (bottom-left, 4×3 correct), D (bottom-right, 2×5 correct)
* **Correct Answer:** B (3×4 with gap — 11 tiles instead of 12)
* **Answer Rationale:**
  - B = Correct — the 3×4 rectangle has a gap (empty square visible, count is 11 instead of 12)
  - A, C, D = Incorrect — these are all correctly tiled with no gaps and no overlaps
* **On Correct:** "B has a gap. The other three follow the rule — no gaps, no overlaps, and the count matches the real area."
* **Connection:** "The rule is the same no matter what size the rectangle is. No gaps, no overlaps = the right count. That's what makes tiling work."
* **Remediation:** Pipeline

> **Design Note:** Pattern Discovery (Type A) — 4 examples visible simultaneously, 3 follow the pattern, 1 breaks it. Uses varied rectangle sizes (2×3, 3×4, 4×3, 2×5) to show the rule is size-independent. The "odd one out" has a gap (the more subtle error — overlaps are more visually obvious with the color change). This tests internalized criteria, not mechanical detection.

---

### Interaction S.2: Where Does This Rule Matter? — Real-World Bridge (Type C)

* **Purpose:** Connect the "no gaps, no overlaps" principle to familiar real-world contexts. The real-world connection comes from the Guide's framing, not from custom illustrations. Uses Grid Rectangles to show three tiling patterns that students evaluate through a real-world lens.
* **Visual: Grid Rectangles (Display).** Three 3×4 rectangles displayed:
  - A: Correctly tiled (12 squares, all shaded, no gaps, no overlaps)
  - B: Tiled with 2 gaps (10 shaded, 2 empty)
  - C: Tiled with 2 overlaps (14 tiles shown, 2 stacked — authored pre-tiled state using overlap visual treatment)
* **Guide:** "No gaps and no overlaps isn't just a math rule. Imagine you're putting tiles on a kitchen floor. Which of these would work?"
* **Prompt:** "Which tiling would work for a real floor? Select A, B, or C."
* **Student Action:** MC selection
  * **Options:** A (complete tiling), B (gaps), C (overlaps)
* **Correct Answer:** A (complete tiling — no gaps, no overlaps)
* **Answer Rationale:**
  - A = Correct — complete coverage, no gaps, no overlaps. A real floor needs every spot covered with no tiles stacked.
  - B = Incorrect — gaps mean bare floor showing through
  - C = Incorrect — overlaps mean bumpy, uneven surface
* **On Correct:** "A! No gaps means no bare floor. No overlaps means no bumps. The tiling rule works the same way in the real world."
* **Connection:** "Tiling is everywhere — floors, walls, even sidewalks. When things fit together perfectly, no space is wasted."
* **Remediation:** Pipeline

> **Design Note:** Real-World Bridge (Type C) redesigned to use Grid Rectangles capabilities rather than requiring custom illustrations (floor tiles, puzzle pieces, stickers). The real-world connection comes from the Guide's language ("kitchen floor," "bare floor," "bumps") rather than from the visual. Three Grid Rectangles showing complete, gap, and overlap tilings are within engineering capabilities (confirmed for 1.5). Students transfer the abstract rule to a concrete scenario through language framing, not illustration.

---

### Interaction S.3: What Helped You Most? — Metacognitive Reflection (Type 1: Strategy Identification)

* **Purpose:** Students reflect on which strategy helped them tile accurately. Builds metacognitive awareness of the self-check routine and gap/overlap detection.
* **Visual: Grid Rectangles (Display).** The correctly tiled 3×4 from the Opening Frame.
* **Guide:** "You tiled a lot of rectangles today. What helped you get the count right?"
* **Prompt:** "What helped you most? Pick one."
* **Student Action:** MC selection
  * **Options:**
    - Checking for gaps before I finished
    - Looking at the grid lines
    - Starting in one corner and working across
    - Counting the tiles at the end
* **Correct Answer:** All valid (no wrong answer in metacognitive reflection)
* **On Correct (per selection):**
  - "Checking for gaps" → "Checking for gaps is exactly what strong mathematicians do — they don't just finish, they verify."
  - "Looking at the grid lines" → "The grid shows you where every tile belongs. Using it is a smart strategy."
  - "Starting in one corner" → "Starting organized keeps you from missing spots. That's a planning strategy."
  - "Counting the tiles" → "Counting at the end is a self-check. That's how you catch mistakes."
* **Connection:** "Knowing what strategy works for YOU is part of getting better at math. You'll use these strategies again."
* **Remediation:** Pipeline

> **Design Note:** Metacognitive Reflection Type 1 (Strategy Identification) — preferred for Modules 1-6 per Playbook §3E. PLANNING-focused reflection: "What did I do?" rather than "How is my understanding changing?" All options are valid strategies observed in the Lesson. Guide validation connects each to mathematical practice without generic praise.

---

### Identity-Building Closure + M3 Bridge

* **Purpose:** Specific, growth-oriented affirmation. Activates rectangle vocabulary from Grade 2. Previews M3's structured counting.
* **Visual: Grid Rectangles (Display).** A correctly tiled 3×4 rectangle with one row visually highlighted (e.g., top row of 4 tiles in a different shade or with a border). Full grid visible.
* **Guide:** "Today you learned the rules for measuring area: no gaps, no overlaps. You tiled rectangles — shapes with 4 sides and 4 right angles — and you got the count right every time. But counting every single tile takes time. Look at this row. Is there a faster way to count? That's what we'll figure out next time."
* **No student action.**

> **Design Note:** Closure names what student DID (tiled rectangles, got count right, learned rules) — behaviorally specific, not generic praise. Rectangle vocabulary activated from Grade 2 ("4 sides, 4 right angles") per §1.3 staging plan and TVP Synthesis section. M3 bridge matches TVP transition: "display a correctly tiled 3×4 rectangle. You can tile perfectly now! But counting every square takes time. Is there a FASTER way?" The highlighted row is the teaser for M3's row-by-column structuring. The question hangs — no answer provided.

> **Voice Note:** Closure energy is Warm + Reflective (per Playbook §1). The M3 bridge question creates genuine curiosity without teaching. "That's what we'll figure out next time" uses session-relative language.

---

### **Verification Checklist (Synthesis)**

**Structure:**

- [x] Opening frame signals shift to reflection (30-45 sec) ✓
- [x] 3 connection tasks (S.1 Pattern Discovery, S.2 Real-World Bridge, S.3 Metacognitive Reflection)
- [x] 1 metacognitive reflection moment (S.3) ✓
- [x] Identity-building closure previews M3 ✓
- [x] Total time 6-8 minutes ✓

**Task Coverage:**

- [x] Pattern Discovery (Type A): S.1 — rule consolidation across varied rectangles
- [x] Real-World Bridge (Type C): S.2 — tiling rules applied to real-world context via language framing
- [x] Metacognitive Reflection (Type 1): S.3 — strategy identification
- [x] At least 2 different task types ✓ (3 types used)

**Alignment:**

- [x] Uses only Toys from Lesson (Grid Rectangles display mode) ✓
- [x] Visual support for every task ✓
- [x] Connections emerge from student experience ✓
- [x] S.2 uses Grid Rectangles capabilities (no custom illustrations required) ✓

**Constraints:**

- [x] Remediation via Pipeline (light) ✓
- [x] No new procedures introduced ✓
- [x] No new vocabulary introduced ✓ (rectangle activated, not introduced)
- [x] Closure is behaviorally specific ("you tiled rectangles and got the count right") ✓
- [x] Every interaction with student action has both Guide: and Prompt: ✓

**Authenticity:**

- [x] Tasks involve CONNECTION, not just APPLICATION ✓
- [x] Each task is cognitively distinct ✓
- [x] Closure specific to what THIS student discovered ✓

---

# **1.10 KEY DESIGN DECISIONS SUMMARY**

**[REQUIRED]**

1. **Sequential Error Presentation with Symmetrical Scaffolding (Gaps → Overlaps → Correct).** TVP SME Decision #3 resolved: present gaps first, then overlaps, then correct tiling. Each error type gets equal pacing: observe → identify. Gaps: 1.1 (display-only) → 1.2 (student counts gaps). Overlaps: 1.3 (display-only) → 1.4 (student counts overlaps). This symmetry prevents a script writer from writing the overlap section faster than the gap section, which would undermine the core principle of building SEPARATE mental models for each error type. The SME resolved that sequential presentation is worth ~60-90 seconds of pacing cost because each concept needs landing time. §1.7 Section 1, §1.5.

2. **Area 12 Held Constant Across Section 1.** All Section 1 interactions (1.1-1.6) use 3×4=12 or 4×3=12 to isolate the gap/overlap variable. When the rectangle stays the same, the ONLY thing that changes is the tiling quality — making the numerical consequences (10 vs. 12 vs. 14) directly comparable. Error identification (1.7-1.8) uses 4×3=12 and 3×3=9. §1.7 Section 1, Working Notes Dimension Tracking.

3. **Grid Rectangles Replaces Plane Figures for M2.** M2 introduces Grid Rectangles as a new primary toy (confirmed via Notion spec). Plane Figures (M1's display-only comparison toy) is NOT used in M2. Grid Rectangles displays rectangles on a full grid — consistent with Decision #3 (M1-M4: Full grids). The transition from Plane Figures to Grid Rectangles reflects the shift from shape comparison (M1) to tiling rules (M2). §1.5.1.

4. **"Rectangle" as Vocabulary Activation, Not Introduction.** Module Mapping lists "rectangle" in Vocabulary to Teach. TVP explicitly states it's "prior knowledge from Grade 2 — not new teaching." Resolved as hybrid: "rectangle" appears in §1.3 Vocabulary Architecture but marked as Activation (students know this word). The Synthesis phase explicitly reinforces rectangle properties. This respects both sources without overtreating a familiar term. §1.3, §1.9 Closure. Conflict Log #4.

5. **Ternary Error Classification in Lesson and EC.** Error identification interactions (1.7, 1.8, EC.2) use three options: Gap, Overlap, Correct — no errors. Binary options (Gap/Overlap only) reduce identification to an elimination task — a student can use count direction alone (too low = gap, too high = overlap) without genuine evaluation. Ternary options force the student to evaluate whether there IS an error before classifying type. A second identification problem (1.8) shows correct tiling where "Correct — no errors" is the answer, ensuring students practice all three classification outcomes before EC tests them. §1.7 Interactions 1.7-1.8, §1.8 EC.2.

6. **Three Simultaneous Grid Rectangles in Relational Interaction.** Interaction 1.5 displays three 3×4 rectangles simultaneously (gap, overlap, correct) for the Relational comparison. Grid Rectangles spec says max 2 standard (3-4 at smaller sizes). Author confirmed feasibility (AF #4 resolved). §1.7 Interaction 1.5.

7. **5×5=25 Moved to Practice.** TVP data constraints specify areas 6-25. 5×5=25 was originally in Lesson Section 3 but was removed due to pacing: 25 drag actions for an 8-year-old exceeds the Section 3 time budget, and 3.1 + 3.2 already provide adequate independence assessment. 5×5=25 moves to Practice where pacing is flexible and the upper boundary should still be exercised. §1.7 Section 3, §1.8.5.

8. **No Area=6 in Lesson or EC.** TVP lower bound is 6 (e.g., 2×3). Smallest tiling in Lesson is 2×4=8; smallest in EC is 5×2=10. Deliberate: 2×3=6 is too small for meaningful gap/overlap demonstration (only 6 squares — errors are trivially visible). Area=6 reserved for Practice phase where small rectangles serve as confidence builders. Synthesis uses 2×3=6 in the Pattern Discovery task (S.1). §1.7, §1.8, Working Notes Dimension Tracking.

9. **Misconception #9.0 (Array Structure Not Seen) as PREVIEW Only.** Module Mapping includes #9.0 for M2; TVP does not mention it. #9.0 surfaces primarily in M3-M4 (Decision #2: Explicit Spatial Structuring). Included in §1.4 as PREVIEW — M2 acknowledges that students may not see row/column structure, but this is expected and appropriate. One-by-one counting is the norm for M2. If students spontaneously count by rows, Guide acknowledges without formally teaching. §1.4.2.

10. **Purpose Frame Present Per Playbook Recommendation.** Lesson opens with a Purpose Frame (Pattern 2 interaction) per Lesson Phase Playbook §1A. It connects backward to M1 tiling experience and forward to WHY coverage quality matters. Uses only M1 vocabulary. No KDD needed for omission. §1.7 Purpose Frame.

11. **Self-Check Routine Fading (Modeled → Prompted → Independent).** The self-check "Any gaps? Any overlaps?" follows a three-stage fading arc: (a) 2.1a — Guide MODELS the check step-by-step in the think-aloud; (b) 2.2 — Guide PROMPTS the check ("check first — any gaps? any overlaps?"); (c) 3.1+ — Student CHECKS independently, Guide gives only brief reminders. This matches the worked example fading (Full → Partial → Minimal) and the TVP's scaffolded feedback progression. S4 is scaffolded via prompt structure, not independently assessed — see §1.8.5 S4 Assessment Note. §1.7 Sections 2-3.

12. **Voice Revisions from Gate 2 and Author Review.** Guide dialogue in 1.1, 1.3, and 1.5 (was 1.4) tightened per Voice Agent findings (5 sentences → 3-4 sentences each). 2.3 Guide warmed ("One more. You know what to do." replacing command-style "Tile it, check it, count it."). Two exclamation points added at genuine discovery moments (1.2 On Correct, 1.5 On Correct). Overlap visual descriptions clarified as authored pre-tiled state (not runtime overlap detection). 1.2 Guide/Prompt language aligned to both say "gaps." §1.7.

13. **EC Value Separation from Lesson.** All EC dimensions deliberately differ from Lesson tiling dimensions. EC.1 (3×5=15), EC.2 (5×2=10), EC.3 (4×5=20) — none of these appear in Lesson interactions. EC.2 uses an overlap error (Lesson 1.7 used a gap error) for balanced assessment of both error types. §1.8, Working Notes Dimension Tracking.

14. **Synthesis Rectangle Vocabulary Activation in Closure.** TVP Synthesis section specifies "Rectangle vocabulary reinforced (prior knowledge from Grade 2)." Rather than creating a separate interaction for rectangle activation, it's integrated into the Identity-Building Closure: "You tiled rectangles — shapes with 4 sides and 4 right angles." This is efficient (avoids adding a thin interaction) and natural (the closure is summarizing what the student did). §1.9 Closure, §1.3.

15. **M3 Bridge Matches TVP Transition.** TVP specifies: "display a correctly tiled 3×4 rectangle. 'You can tile perfectly now! But counting every square takes time. Is there a FASTER way?' Briefly highlight one row." The Synthesis closure reproduces this beat: correctly tiled 3×4, highlighted top row, question about faster counting. The highlighted row is the teaser for M3's row-by-column structuring. No answer is provided — the question creates motivation for M3. §1.9 Closure, §1.1.2 Module Bridges.

16. **Practice Skill Distribution Rationale (65/25/10).** ⚠️ NOT REVIEWED BY SME. S1+S2 (Tile + Count) at ~65% because tiling is the primary skill and needs the most Practice reps. S3 (Error Identification) at ~25% because it's a secondary MC-based skill that requires less time per problem. Mixed (error correction) at ~10% because it combines identification and tiling — higher cognitive load, appropriate as a stretch category. These targets are starting points for Practice engineering; actual distribution should be validated against student performance data. §1.8.5.

17. **Practice Dimension Selection Strategy.** ⚠️ NOT REVIEWED BY SME. Practice dimensions should prioritize unused combinations (2×3, 3×6, 4×6, 6×2, 6×3, 6×4) to avoid dimension overlap with Lesson and EC. When Lesson/EC dimensions must be reused (e.g., for error correction problems), document the reuse. 5×5=25 moved from Lesson to Practice for pacing reasons — include as a Practice problem to exercise the upper boundary. Avoid clustering too many problems at area=12 (already heavily used in Lesson Section 1). §1.8.5, Working Notes Dimension Tracking.

18. **Synthesis Real-World Bridge Uses Grid Rectangles.** S.2 uses Grid Rectangles to display three tiling patterns (correct, gap, overlap) with the real-world connection provided through Guide language ("Imagine you're putting tiles on a kitchen floor"). This avoids requiring custom illustrations (floor tiles, puzzle pieces, stickers) that would need a different display mechanism. The toy capability is confirmed (three simultaneous Grid Rectangles supported per KDD #6). The real-world bridge is a language bridge, not a visual bridge. §1.9 S.2.

---

# END OF TASK 3 DRAFT
