# Remediation System

Error patterns and remediation strategies for fraction exercises. Use with Visual Guide for animation types.

## HOW IT WORKS

Students get 3 attempts max (Light → Medium → Heavy). System detects specific errors and serves appropriate remediation.

**Your job:** Provide all applicable error paths at each level.

---

## REMEDIATION LEVELS

### Light (10-20 words) - No visual
Quick redirect only.

**Patterns:**
- With error signal (40-50%): "Not quite. [guidance]" / "Let's try again. [hint]"
- Direct (50-60%): "Count [X]" / "Check [Y]" / Simple imperatives

### Medium (20-30 words) - Visual required
Explanation + visual hint (animation types in Visual Guide).

**Patterns:**
- "Let's think about this together. [guidance]" + visual
- "Here's a hint: [specific help]" + visual
- "You're working on it. [guidance]" + visual

### Heavy (30-60 words) - Visual + demonstration required
Full walkthrough (animation types in Visual Guide) + acknowledgment.

**Patterns:**
- "This is tricky, so let's work through it together. [demonstration]" + visual
- "Let me help you with this one. [walkthrough]" + visual
- "Here, I'll walk you through this. [step-by-step]" + visual

**Post-Demo (required):**
✓ "There we go." / "See how that works?" / "It's okay if this is tricky."
✗ Never: "Perfect!" / "Great job!" (they didn't do it alone)

---

## ERROR PATTERNS

### Generic (ALWAYS REQUIRED)
**When:** Every interaction (fallback)  
**Detection:** N/A  
**Levels:** L-M-H

### Common Errors

**Counting Error**  
Wrong number created/selected, all parts equal  
Detection: `count ≠ target`  
Levels: L-M-H

- L: "Count your parts - you need exactly 4." / "Check how many parts you made."
- M: "You made 5 parts, but we need 4. Try combining two of them." + visual
- H: "We need 4 parts total. Count with me: 1, 2, 3, 4. That's it!" + visual

**Off-by-One**  
One space/interval off  
Detection: `abs(position - correct) == 1`  
Levels: L-M-H

- L: "Check your position - you're one space off." / "Almost there - adjust by one interval."
- M: "You're very close! Move one more interval to the right." + visual
- H: "Count each interval: 1/4, 2/4, 3/4, 4/4 equals 1, then 5/4. We need one more space." + visual

**Reversed Order**  
Selected backwards sequence  
Detection: `student_order == reversed(correct)`  
Levels: L-M-H

- L: "Check the order - we need biggest to smallest."
- M: "The instruction asks for smallest to largest. Try reversing your order." + visual
- H: "We need smallest to largest. This is smallest, this is medium, this is largest." + visual

**Reversed Symbol**  
Uses < instead of > or vice versa  
Detection: `student_symbol ≠ correct_symbol`  
Levels: L-M-H

- L: "Check your symbol - which way does it point?"
- M: "The small end points to the smaller number. Check which fraction is smaller." + visual
- H: "The small end points to the smaller fraction. 3/8 is smaller than 5/8, so: 3/8 < 5/8." + visual

### Misconceptions

**#1: Equal vs. Unequal Parts**  
Treating unequal parts as equal  
Detection: `not all_parts_equal()`  
Levels: L-M-H

- L: "Are all these parts the same size?"
- M: "Your parts need to be equal. This part is bigger than this one." + visual
- H: "Every piece must be exactly the same size. See how this is bigger? Let's make them match." + visual

**#2: Misidentifying the Whole**  
Comparing parts from different wholes  
Detection: `fractions reference different wholes`  
Levels: L-M-H

- L: "Check what the whole bar is."
- M: "These bars are different sizes. We need to compare pieces from the same whole." + visual
- H: "This whole bar is our '1'. These parts are from this bar. That bar is different. We can only compare fractions from the same whole." + visual

**#3: Numerator/Denominator as Independent**  
Treating top and bottom numbers as separate  
Detection: Pattern of independent treatment  
Levels: L-M-H

- L: "These numbers work together - check what each shows."
- M: "Top counts what you have, bottom counts total parts." + visual
- H: "If I have 2 parts out of 5 total, that's 2/5. The numbers describe the same situation." + visual

**#4: Improper Spacing on Number Line**  
Unequal intervals  
Detection: `not all_intervals_equal()`  
Levels: L-M-H

- L: "Check your spacing - all intervals should be equal."
- M: "Each interval needs to be the same width. This space is bigger than that one." + visual
- H: "Each interval must be exactly the same. Watch: this space, this space, this space - all equal." + visual

**#5: Counting Tick Marks Instead of Spaces**  
Counting marks instead of intervals  
Detection: `student counted marks vs spaces`  
Levels: L-M-H

- L: "Count the spaces between marks, not the marks."
- M: "The spaces between marks are what we count, not the marks themselves." + visual
- H: "We count spaces, not marks. This space is one fourth, this space is another fourth. Marks show where spaces end." + visual

**#6: Reversing Numerator and Denominator**  
Top and bottom numbers swapped  
Detection: `num == expected_denom && denom == expected_num`  
Levels: L-M-H

- L: "You have the right numbers - check their positions."
- M: "Shaded parts go on top, total parts go on bottom." + visual
- H: "Count shaded parts - that's your top number. Count total parts - that's your bottom. So 3 shaded out of 4 total is 3/4." + visual

**#7: Difficulty Recognizing Equivalence**  
Can't see equal amounts in different representations  
Detection: Student says unequal when visuals show equal  
Levels: L-M-H

- L: "Look at the shaded amounts - are they the same?"
- M: "These look different but show the same amount. Look at the total shaded space." + visual
- H: "2 out of 4 is 2/4. 1 out of 2 is 1/2. But the shaded amounts take up the same space. Different fractions, same amount." + visual

**#8: Errors Comparing Unlike Fractions**  
Thinking more parts = bigger pieces  
Detection: Chose larger denominator as larger fraction  
Levels: L-M-H

- L: "Look at the actual size of each piece."
- M: "More parts means smaller pieces. Which bar has pieces that take up more space?" + visual
- H: "When we cut into fewer pieces, each piece is larger. Three pieces means bigger parts than eight pieces." + visual

**#9: Fractions Only Exist in Shapes**  
Can't see fractions in other representations  
Detection: Student can't identify non-shape format  
Levels: L-M-H

- L: "Fractions work on number lines too."
- M: "Fractions aren't just shapes - they're positions on number lines and symbols too." + visual
- H: "In a shape, 1/4 is one part out of four. On a number line, 1/4 is a position. Same fraction, different way to show it." + visual

**#10: Overgeneralizing Rules**  
Applying one rule incorrectly to all contexts  
Detection: Applied rule incorrectly  
Levels: L-M-H

- L: "Check with the visual - does that rule work here?"
- M: "That rule doesn't work for denominators. More parts means each piece is smaller." + visual
- H: "For numerators, bigger is more: 3/4 > 1/4. For denominators, bigger means smaller pieces: 1/8 < 1/4. Context matters." + visual

---

## DETECTABILITY RULES

Include error pattern ONLY if all 3 are YES:
1. Applies to this specific interaction type?
2. System can observe clear evidence?
3. Can write simple detection rule?

**Examples:**
- ✅ "Student shaded 4 but fraction is 3/4" → Counting Error
- ✅ "Student wrote 4/3 but visual shows 3/4" → Misconception #6
- ❌ "Student doesn't understand" → Too vague
- ❌ "Student might be confused" → Speculation

## INTERACTION TYPE QUICK REFERENCE

**Shading:** Counting Error, Misconception #6, #1 (if partitioning)
**Number Line:** Off-by-One, Counting Error, Misconception #4, #5
**Comparison:** Reversed Symbol, Misconception #8, #2
**Partitioning:** Counting Error, Misconception #1
**Ordering:** Reversed Order
**Writing Fractions:** Misconception #6, #3
**Equivalence:** Misconception #7



