# M11 Interaction 1.1 — Restructured to Template v3

**What changed:** Single multi-phase block split into 1.1a/1.1b/1.1c sub-parts per template v3 Multi-Step Interactions spec. Missing Answer Rationale added to phases 2 and 3. Think-aloud tags moved inside single Guide field per Pattern 4. `Guide (continuing)` ad-hoc field replaced with standard `Guide` field in each sub-part. `Visual (after correct)` ad-hoc field replaced with Design Note. Annotations converted to `>` blockquote format.

---

## FIND AND REPLACE IN NOTION

**Delete everything from `### Interaction 1.1:` through the `---` before `### Interaction 1.2:` and replace with:**

---

### Interaction 1.1: First System-Decomposed Problem [WORKED EXAMPLE — FULL]

* **Purpose:** Full worked example of decompose-calculate-add workflow. Guide think-aloud models strategic approach using [PLANNING], [ATTENTION], and [SELF-CHECK] tags. Student computes each rectangle's area (1.1a, 1.1b) and the sum (1.1c). Three sub-parts — one per student submission.
* **Visual: Composite Figures (Full grid mode).** L-shape from W.4, decomposition line already drawn by system. Rectangle A (blue) = 4 wide × 3 tall. Rectangle B (pink) = 5 wide × 2 tall. Dimensions labeled on each rectangle's edges. Equation Builder co-displayed: (__ × __) + (__ × __) = ?

#### Interaction 1.1a: Blue Rectangle Area

* **Guide:** "[PLANNING] Let's figure out the area of this shape. It's not a rectangle, but it's MADE of rectangles. The line splits it into two. I need to find the area of the whole shape. [ATTENTION] I'll start with the blue rectangle. It's 4 by 3. What's 4 times 3?"
* **Prompt:** "What is the area of the blue rectangle? (4 × 3)"
* **Student Action:** MC selection
  * **Options:** A) 7 square units, B) 12 square units, C) 14 square units, D) 16 square units
* **Correct Answer:** B) 12 square units
* **Answer Rationale:**
  - B = Correct (4 × 3 = 12)
  - A = Addition error (4 + 3 = 7)
  - C = Multiplication neighbor (2 × 7 = 14)
  - D = Multiplication neighbor (4 × 4 = 16)
* **On Correct:** "12 square units for the blue rectangle."
* **Remediation:** Pipeline

#### Interaction 1.1b: Pink Rectangle Area

* **Visual:** Equation Builder updates: (4 × 3) + (__ × __) = ? Blue rectangle area filled in.
* **Guide:** "Now the pink one. It's 5 by 2. What's 5 times 2?"
* **Prompt:** "What is the area of the pink rectangle? (5 × 2)"
* **Student Action:** MC selection
  * **Options:** A) 7 square units, B) 10 square units, C) 15 square units
* **Correct Answer:** B) 10 square units
* **Answer Rationale:**
  - B = Correct (5 × 2 = 10)
  - A = Addition error (5 + 2 = 7)
  - C = Multiplication error (5 × 3 = 15; student may use blue rectangle's dimension instead of pink's)
* **On Correct:** "10 square units for the pink one."
* **Remediation:** Pipeline

#### Interaction 1.1c: Total Area (Sum)

* **Visual:** Equation Builder updates: (4 × 3) + (5 × 2) = 12 + 10 = ? Both rectangle areas filled in.
* **Guide:** "Now add them together. 12 plus 10."
* **Prompt:** "What is 12 + 10?"
* **Student Action:** MC selection
  * **Options:** A) 20, B) 22, C) 24
* **Correct Answer:** B) 22
* **Answer Rationale:**
  - B = Correct (12 + 10 = 22)
  - A = Subtraction or rounding error (student may estimate or confuse with 10 + 10)
  - C = Addition error (12 + 12 = 24; student may double one rectangle's area)
* **On Correct:** "[SELF-CHECK] 12 plus 10 is 22 square units. That's the total area of the whole shape."
* **Remediation:** Pipeline

---

> **Design Note (1.1):** This is the full worked example. The Guide's think-aloud models [PLANNING] ("I need to find the area of the whole shape"), [ATTENTION] ("I'll start with the blue rectangle"), and [SELF-CHECK] ("12 plus 10 is 22"). The student does the computation (MC for each rectangle's area and the sum) while the Guide provides the strategic frame. After 1.1c correct, Equation Builder fills in completely: (4 × 3) + (5 × 2) = 12 + 10 = 22.

> **Scaffolding Note (1.1):** Same figure from W.4 — students already know the answer (22), so the think-aloud models the PROCESS, not the answer. System places the decomposition line. System labels dimensions on each rectangle. Equation Builder structure is pre-set. Student's only task is computation. Fading begins in 1.2.

---
