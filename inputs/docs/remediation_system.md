# Remediation System v2.0

## SECTION 1: OVERVIEW

This reference defines the logic and language templates used to generate remediation error paths in educational interaction scripts.

### What Are Remediations and Error Paths?

**Remediations** are instructional responses that help students correct mistakes and learn from errors during interactive math activities.

**Error Paths** are specific remediation sequences designed for different types of student errors. Each error path contains three progressively supportive steps.

### How the System Works

When a student makes an error:
1. System detects an error on the current attempt.
2. System selects the appropriate error path and scaffolding level based on:
   - **error_type**: The type of error detected on the current attempt (e.g., counting error, reversed symbol, generic, etc.)
   - **error_count**: The total number of errors the student has made in this interaction (cumulative across all error types)
   - The system always serves the remediation level matching the error_count:
     - **Light** level for error_count = 1 (first error)
     - **Medium** level for error_count = 2 (second error)
     - **Heavy** level for error_count ≥ 3 (third or subsequent errors)
   - The error_type determines WHICH error path is used, while error_count determines WHICH LEVEL within that path. For example, if error_count = 2 and the student makes a "reversed symbol" error, the system serves the Medium level of the Reversed Symbol Error path.
3. This process continues, always selecting the error path and scaffolding level that matches the most recent detected error.

**Example:**
- Student shades 3 parts instead of 1 on a fraction bar
- System detects counting error → Serves `error_path_counting` Light: "Count your parts — you need exactly 1."
- Student tries again, but now uses the wrong symbol (< instead of >) → System detects reversed symbol error → Serves `error_path_reversed_symbol` Medium: "The small end points to the smaller number. Check which fraction is smaller."
- Student tries again, makes a generic/ambiguous error → System detects generic error → Serves `error_path_generic` Heavy: "This is tricky, let's walk through it together..."

### Required Error Paths

Writers create multiple error path options for each interaction:
- **`error_path_generic`** — Always required (fallback for ambiguous/undetectable errors)
- **`error_path_<type>`** — Include for each detectable error pattern (see Section 2 for detection requirements)

Each error path must contain exactly 3 steps in sequence: light, medium, heavy.

---

## SECTION 2: DETECTABLE ERROR PATTERNS

### Detectable Error Types

Each detectable error type has:

- Confidence requirement
- When to include
- Label format
- Remediation structure

| Error Type               | Label Format                    | Include When...             | Confidence Required |
|--------------------------|----------------------------------|-----------------------------|---------------------|
| Generic                  | `error_path_generic`            | Always                      | —                   |
| Counting Error           | `error_path_counting`           | Wrong count, equal parts    | HIGH                |
| Off-by-One Error         | `error_path_off_by_one`         | One space off               | HIGH                |
| Reversed Order           | `error_path_reversed_order`     | Sequence flipped            | HIGH                |
| Reversed Symbol          | `error_path_reversed_symbol`    | Used < vs > incorrectly     | HIGH                |
| Misconception #1         | `error_path_misconception_1`    | Unequal parts               | 90%+                |
| Misconception #2         | `error_path_misconception_2`    | Wrong whole                 | 90%+                |
| Misconception #3         | `error_path_misconception_3`    | Num/denom seen separately   | 90%+                |
| Misconception #4         | `error_path_misconception_4`    | Uneven spacing              | 85%+                |
| Misconception #5         | `error_path_misconception_5`    | Counts marks, not spaces    | 85%+                |
| Misconception #6         | `error_path_misconception_6`    | Reversed num/denom          | 90%+                |
| Misconception #7         | `error_path_misconception_7`    | Can't recognize equivalence | 90%+                |
| Misconception #8         | `error_path_misconception_8`    | Size confusion              | 90%+                |
| Misconception #9         | `error_path_misconception_9`    | Thinks fractions = shapes   | 90%+                |
| Misconception #10        | `error_path_misconception_10`   | Overgeneralized rule        | 85%+                |

⚠️ **Detection confidence governs inclusion.** If detection is uncertain → use `error_path_generic` only.

---

## SECTION 3: REMEDIATION STRUCTURE BY LEVEL

### General Requirements

**Workspace Context:** All remediation steps reference existing tangibles from the main interaction flow. Do not redefine tangibles; use workspace_context to indicate which ones are present (metadata only).

**Visual Effects:** Visual specifications describe dynamic effects/animations applied TO those existing tangibles, or null for light level.

---

### Remediation Structure by Level

Each error path must be structured with 3 scaffolding levels delivered as sequential steps. Each step includes dialogue, workspace_context, and visual specifications.

#### LIGHT (10–20 words)
- **Purpose:** Simple redirect without diagnosis
- **Dialogue:** Brief and direct
- **Visual:** `null` (no visual effects applied)
- **Dialogue patterns:**
  - "Check the symbol..."
  - "Count again..."
  - "Try one more jump..."
  - "Look at all your parts..."

#### MEDIUM (20–30 words)
- **Purpose:** Specific hint + visual scaffolding
- **Dialogue:** Acknowledge continued struggle, collaborative language
- **Visual:** Effects object with highlight/pulse/arrow animations applied to tangibles
  - `type`: "highlight", "pulse", "arrow"
  - `target`: Specific tangible_id from workspace
  - `animation`: Animation name (e.g., "pulse", "highlight_sections")
  - `description`: Human-readable description of the visual effect
- **Dialogue patterns:**
  - "You're close! Try moving one more interval."
  - "Let's think together..."
  - "You made 5 parts, but need 4."

#### HEAVY (30–60 words)
- **Purpose:** Step-by-step walkthrough revealing the answer
- **Dialogue:** Full emotional support, complete demonstration
- **Visual:** Effects object with measurement/overlay/demonstration animations
  - `type`: "measurement", "overlay", "demonstration"
  - `target`: Specific tangible_id from workspace
  - `animation`: Animation name (e.g., "measure_sections_equal", "overlay_counting")
  - `description`: Human-readable description of the demonstration
- **Dialogue structure:**
  - Opening: Modeling introduction ("This is tricky, let's walk through it together...")
  - Body: Step-by-step demonstration with the answer revealed

  - Closing: Post-modeling acknowledgment (required)

##### Post-Modeling Acknowledgment Phrases

- **Always ends with one of:**
  - "There we go."
  - "You're getting it now."
  - "See how that works?"
  - "Now you see the pattern."
  - "That makes sense now, right?"
- **Never ends with:**
  - "Perfect!" / "Great job!" / "You figured it out!"

---

## SECTION 4: LANGUAGE TEMPLATES (BY ERROR TYPE)

### Remediation Language Templates

Use these phrases as templates. Do not repeat exact phrasing across 3 interactions.

#### GENERIC

**Light:**
- "Let's try again. Count from zero."
- "Give it another try. Check the spacing."
- "Try again — remember to count each part."

**Medium:**
- "Let's think about this together. You need 4 equal parts."  
  → [Visual: See visual_guide.md for matching highlight]

**Heavy:**
- "This is tricky, let's walk through it. Four fourths is 1, then three more = 7/4."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### COUNTING ERROR

**Detection:** `count ≠ target` (wrong number created/selected, all parts equal)

**Light:**
- "Count your parts - you need exactly 4."
- "Check how many parts you made."

**Medium:**
- "You made 5 parts, but we need 4. Try combining two of them."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "We need 4 parts total. Count with me: 1, 2, 3, 4. That's it!"  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### OFF-BY-ONE ERROR

**Detection:** `abs(position - correct) == 1` (one space/interval off)

**Light:**
- "Check your position - you're one space off."
- "Almost there - adjust by one interval."

**Medium:**
- "You're very close! Move one more interval to the right."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "Count each interval: 1/4, 2/4, 3/4, 4/4 equals 1, then 5/4. We need one more space."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### REVERSED ORDER

**Detection:** `student_order == reversed(correct)` (selected backwards sequence)

**Light:**
- "Check the order - we need biggest to smallest."

**Medium:**
- "The instruction asks for smallest to largest. Try reversing your order."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "We need smallest to largest. This is smallest, this is medium, this is largest."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### REVERSED SYMBOL

**Detection:** `student_symbol ≠ correct_symbol` (uses < instead of > or vice versa)

**Light:**
- "Check your symbol - which way does it point?"

**Medium:**
- "The small end points to the smaller number. Check which fraction is smaller."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "The small end points to the smaller fraction. 3/8 is smaller than 5/8, so: 3/8 < 5/8."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #1: Equal vs. Unequal Parts

**Detection:** `not all_parts_equal()` (treating unequal parts as equal)

**Light:**
- "Are all these parts the same size?"

**Medium:**
- "Your parts need to be equal. This part is bigger than this one."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "Every piece must be exactly the same size. See how this is bigger? Let's make them match."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #2: Misidentifying the Whole

**Detection:** `fractions reference different wholes` (comparing parts from different wholes)

**Light:**
- "Check what the whole bar is."

**Medium:**
- "These bars are different sizes. We need to compare pieces from the same whole."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "This whole bar is our '1'. These parts are from this bar. That bar is different. We can only compare fractions from the same whole."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #3: Numerator/Denominator as Independent

**Detection:** Pattern of independent treatment (treating top and bottom numbers as separate)

**Light:**
- "These numbers work together - check what each shows."

**Medium:**
- "Top counts what you have, bottom counts total parts."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "If I have 2 parts out of 5 total, that's 2/5. The numbers describe the same situation."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #4: Improper Spacing on Number Line

**Detection:** `not all_intervals_equal()` (unequal intervals)

**Light:**
- "Check your spacing - all intervals should be equal."

**Medium:**
- "Each interval needs to be the same width. This space is bigger than that one."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "Each interval must be exactly the same. Watch: this space, this space, this space - all equal."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #5: Counting Tick Marks Instead of Spaces

**Detection:** `student counted marks vs spaces` (counting marks instead of intervals)

**Light:**
- "Count the spaces between marks, not the marks."

**Medium:**
- "The spaces between marks are what we count, not the marks themselves."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "We count spaces, not marks. This space is one fourth, this space is another fourth. Marks show where spaces end."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #6: Reversing Numerator and Denominator

**Detection:** `num == expected_denom && denom == expected_num` (top and bottom numbers swapped)

**Light:**
- "You have the right numbers - check their positions."

**Medium:**
- "Shaded parts go on top, total parts go on bottom."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "Count shaded parts - that's your top number. Count total parts - that's your bottom. So 3 shaded out of 4 total is 3/4."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #7: Difficulty Recognizing Equivalence

**Detection:** Student says unequal when visuals show equal (can't see equal amounts in different representations)

**Light:**
- "Look at the shaded amounts - are they the same?"

**Medium:**
- "These look different but show the same amount. Look at the total shaded space."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "2 out of 4 is 2/4. 1 out of 2 is 1/2. But the shaded amounts take up the same space. Different fractions, same amount."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #8: Errors Comparing Unlike Fractions

**Detection:** Chose larger denominator as larger fraction (thinking more parts = bigger pieces)

**Light:**
- "Look at the actual size of each piece."

**Medium:**
- "More parts means smaller pieces. Which bar has pieces that take up more space?"  
  → [Visual: See visual_guide.md]

**Heavy:**
- "When we cut into fewer pieces, each piece is larger. Three pieces means bigger parts than eight pieces."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #9: Fractions Only Exist in Shapes

**Detection:** Student can't identify non-shape format (can't see fractions in other representations)

**Light:**
- "Fractions work on number lines too."

**Medium:**
- "Fractions aren't just shapes - they're positions on number lines and symbols too."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "In a shape, 1/4 is one part out of four. On a number line, 1/4 is a position. Same fraction, different way to show it."  
  → [Modeling] + [Visual: See visual_guide.md]

---

#### MISCONCEPTION #10: Overgeneralizing Rules

**Detection:** Applied rule incorrectly (applying one rule incorrectly to all contexts)

**Light:**
- "Check with the visual - does that rule work here?"

**Medium:**
- "That rule doesn't work for denominators. More parts means each piece is smaller."  
  → [Visual: See visual_guide.md]

**Heavy:**
- "For numerators, bigger is more: 3/4 > 1/4. For denominators, bigger means smaller pieces: 1/8 < 1/4. Context matters."  
  → [Modeling] + [Visual: See visual_guide.md]

---

## SECTION 5: STRUCTURAL RULES & VALIDATION

### Structural Rules for JSON Generation

- Every interaction must include:
  - `error_path_generic` (always)
  - All detectable error types with required confidence
  - All paths include light, medium, heavy

- **scaffolding_level** must be set at each remediation step
- **visual** = null (light), highlight/pulse (medium), overlay/measurement (heavy)
- **workspace_context** must include tangibles from the main sequence


## SECTION 6: INTERACTION TYPE QUICK REFERENCE

### Common Error Patterns by Interaction Type

| Interaction Type     | Applicable Error Patterns                              |
|----------------------|--------------------------------------------------------|
| **Shading**          | Counting Error, Misconception #6, #1 (if partitioning)|
| **Number Line**      | Off-by-One, Counting Error, Misconception #4, #5      |
| **Comparison**       | Reversed Symbol, Misconception #8, #2                  |
| **Partitioning**     | Counting Error, Misconception #1                       |
| **Ordering**         | Reversed Order                                         |
| **Writing Fractions**| Misconception #6, #3                                   |
| **Equivalence**      | Misconception #7                                       |

---

## SECTION 7: COMPANION FILE

### Companion File: `visual_guide.md`

This file contains visual scaffolds by task type + error pattern.

During generation, reference as:
```
→ [Visual: See visual_guide.md: task="bar_shading", error="counting"]
```

All visual effects referenced in medium and heavy remediations should correspond to animations defined in `visual_guide.md`.



