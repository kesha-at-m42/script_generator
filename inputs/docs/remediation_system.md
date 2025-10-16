# Remediation System - Error Response Framework

**Version:** 2.0  
**Purpose:** Define error patterns and remediation strategies for interactive fraction exercises  
**Usage:** This document helps predict likely student errors and provides remediation dialogue templates

## DOCUMENT RELATIONSHIP

**Remediation System (this document):**
- Goal: Predict error paths based on common misconceptions
- Provides: Dialogue templates and remediation strategies
- References: Visual Guide for animation types

**Visual Guide (companion document):**
- Goal: Define visually possible animations and scaffolding
- Provides: Animation types, interaction methods, scaffolding levels
- Referenced by: Remediation System when specifying visual support

**When creating remediations:** Use this document to determine error paths and dialogue. When you see "[Visual animation: see Visual Guide]", consult the Visual Guide to select appropriate animation types from the available catalog.

---

## SYSTEM OVERVIEW

### Core Concept
Students progress through ONE remediation sequence (Light → Medium → Heavy, max 3 attempts). At EACH level, the system selects which remediation to serve based on real-time error detection.

**Your job:** Provide all applicable remediation OPTIONS at each level.

**Example Flow:**
```
Attempt 1: Wrong → Light level
           System detects: Common_Error_Counting
           System serves: Common_Error_Counting Light

Attempt 2: Wrong → Medium level  
           System detects: Misconception_#3
           System serves: Misconception_#3 Medium

Attempt 3: Wrong → Heavy level
           System detects: Misconception_#6  
           System serves: Misconception_#6 Heavy
```

---

## REMEDIATION LEVELS

### Light Level (10-20 words) - NO visual
**Purpose:** Quick redirect without heavy scaffolding  
**Components:** Brief guidance only

**With Error Signal (40-50% of interactions):**
- "Not quite. Count seven fourths from zero."
- "Almost. Check your spacing between marks."
- "Let's try again. Five equal jumps total."
- "Let's look closely - seven fourths from zero."
- "Let's see - seven fourths from zero."
- "Let's look at this problem again."
- "Let's take another look."
- "Let's try that again."
- "Give it another try. Remember…"
- "Let's give it another try. Remember…"

**Without Error Signal (50-60% of interactions):**
- "Count seven fourths from zero."
- "Check the spacing between marks."
- "Five equal jumps from zero."
- "Same size jumps past 1."
- "Seven equal jumps from zero."
- Direct guidance with no preamble
- "Check..." + what to check
- "Count..." + what to count
- Simple imperative statements

### Medium Level (20-30 words) - MUST include visual animation (reference: Visual Guide)
**Purpose:** More explicit guidance with visual support  
**Components:** Explanation + visual scaffold (animation types defined in Visual Guide)

**Approved Starters:**
- "Let's think about this together. [guidance]" [Visual animation: see Visual Guide]
- "Here's a hint: [specific help]" [Visual animation: see Visual Guide]
- "You're working on it. Here's what helps - [guidance]" [Visual animation: see Visual Guide]
- "You're getting there. The key is [concept]" [Visual animation: see Visual Guide]
- "Let's think about this a bit more. [guidance]" [Visual animation: see Visual Guide]
- "Still tricky? Try this..." + specific help [Visual animation: see Visual Guide]
- "Here's a different approach..." + guidance [Visual animation: see Visual Guide]

### Heavy Level (30-60 words) - MUST include visual animation (reference: Visual Guide)
**Purpose:** Complete demonstration with step-by-step walkthrough  
**Components:** Full demonstration + visual animation (animation types in Visual Guide) + acknowledgment

**Approved Openings:**
- "This is tricky, so let's work through it together. [complete demonstration]" [Visual animation: see Visual Guide]
- "Let me help you with this one. [step-by-step walkthrough]" [Visual animation: see Visual Guide]
- "Here, I'll walk you through this one. [demonstration]" [Visual animation: see Visual Guide]
- "These can be challenging. Let's trace through step by step. [demonstration]" [Visual animation: see Visual Guide]
- "This can be tricky, so let's do it together. [demonstration]" [Visual animation: see Visual Guide]
- "Let's work through this together..." [demonstration] [Visual animation: see Visual Guide]
- "Let me work through it with you. [walkthrough]" [Visual animation: see Visual Guide]
- "Here, let me show you: [demonstration]" [Visual animation: see Visual Guide]

**Post-Demonstration Acknowledgment (REQUIRED - Use ONLY These):**
- "There we go."
- "See how that works?"
- "It's okay if this is tricky."
- "You're getting it now."
- "Now you understand."
- "That makes sense now, right?"
- "That's it - now you've got it."
- "Good - you understand now."
- "Now you see the pattern."

**NEVER After Demonstration:**
- ✗ "Perfect!" (they didn't do it alone)
- ✗ "You figured it out!" (guide showed them)
- ✗ "Great job!" (too independent)
- ✗ "Excellent work!" (overpraises assisted work)

---

## ERROR PATTERN CATALOG

### Generic Track (Always Required)
**When:** Every interaction (fallback for undetectable errors)  
**Confidence:** Always  
**Available:** Light, Medium, Heavy

### Common Error: Counting Error
**When:** Wrong number created/selected, all parts equal  
**Confidence:** HIGH required  
**Available:** Light, Medium, Heavy

**Light (10-20 words):**
- "Count your parts - you need exactly 4."
- "Check how many parts you made."
- "Count the shaded parts again."
- "Count again - we need 3 shaded."

**Medium (20-30 words):**
- "You're close! You made 5 parts, but we need 4. Try combining two of them." [Visual animation: see Visual Guide]
- "You shaded 2, but we need 3. Count the shaded parts again." [Visual animation: see Visual Guide]
- "You're working on it. Count total parts - we need exactly 4 equal sections." [Visual animation: see Visual Guide]

**Heavy (30-60 words):**
- "Let me show you. We need 4 parts total. Count with me as we divide: 1, 2, 3, 4. That's it!" [Visual animation: see Visual Guide]
- "Here's how we do this. Count each part: 1, 2, 3, 4, 5. We have 5, but need 4. Let me show you the right number." [Visual animation: see Visual Guide]

### Common Error: Off-by-One Error
**When:** One space/interval off  
**Confidence:** HIGH required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check your position - you're one space off."
- "Almost there - adjust by one interval."
- "Count the spaces one more time."

**Medium:**
- "You're very close! Move one more interval to the right." [Visual animation: see Visual Guide]
- "You're getting there. Check the spacing - you need one more jump." [Visual animation: see Visual Guide]

**Heavy:**
- "Here's how we find the exact spot. Count each interval: 1/4, 2/4, 3/4, 4/4 equals 1, then 5/4. See? We need to go one more space." [Visual animation: see Visual Guide]

### Common Error: Reversed Order
**When:** Selected backwards sequence  
**Confidence:** HIGH required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check the order - we need biggest to smallest."
- "Look at the instruction again - smallest to largest."

**Medium:**
- "You're working on it. The instruction asks for smallest to largest. Try reversing your order." [Visual animation: see Visual Guide]

**Heavy:**
- "Let me show you. We need smallest to largest. This piece is smallest, this is medium, this is largest. That's the order: smallest first, largest last." [Visual animation: see Visual Guide]

### Common Error: Reversed Symbol
**When:** Uses < instead of > or vice versa  
**Confidence:** HIGH required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check your symbol - which way does it point?"
- "Look at the symbol direction again."

**Medium:**
- "You're getting there. The small end points to the smaller number. Check which fraction is smaller." [Visual animation: see Visual Guide]

**Heavy:**
- "Here's how symbols work. The small end points to the smaller fraction. 3/8 is smaller than 5/8, so: 3/8 < 5/8. The small end points left to the smaller number." [Visual animation: see Visual Guide]

---

## MISCONCEPTION PATTERNS

### Misconception #1: Equal vs. Unequal Parts
**When:** Treating unequal parts as equal  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Are all these parts the same size?"
- "Check if all your parts are equal."
- "Look at the sizes of each part."

**Medium:**
- "Your parts need to be equal. This part is bigger than this one." [Visual animation: see Visual Guide]
- "Fractions only work when all parts are equal. Check if each section matches." [Visual animation: see Visual Guide]

**Heavy:**
- "For equal parts, every piece must be exactly the same size. Watch - I'll measure each one. See how this is bigger? Let's make them all match." [Visual animation: see Visual Guide]
- "Look - this part is bigger than that part. When parts aren't equal, we can't use fractions. We need same-sized pieces." [Visual animation: see Visual Guide]

### Misconception #2: Misidentifying the Whole
**When:** Comparing parts from different wholes  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check what the whole bar is."
- "Look at the complete shape first."

**Medium:**
- "You're working on it. These bars are different sizes. We need to compare pieces from the same whole." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch this. This whole bar is our '1'. These parts are from this bar. That whole bar is different - it's a different '1'. We can only compare fractions from the same whole." [Visual animation: see Visual Guide]

### Misconception #3: Numerator/Denominator as Independent
**When:** Treating top and bottom numbers as separate  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "These numbers work together - check what each shows."
- "The top and bottom numbers are connected."

**Medium:**
- "The top and bottom numbers are connected. Top counts what you have, bottom counts total parts." [Visual animation: see Visual Guide]
- "You're getting there. These numbers describe the same situation together." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch: if I have 2 parts (numerator) out of 5 total (denominator), that's 2/5. The numbers describe the same situation." [Visual animation: see Visual Guide]
- "Let me show you how they work together. Count shaded parts - that's your top number. Count total parts - that's your bottom number. They both describe this one fraction." [Visual animation: see Visual Guide]

### Misconception #4: Improper Spacing on Number Line
**When:** Unequal intervals on number line  
**Confidence:** 85%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check your spacing - all intervals should be equal."
- "Make sure each space is the same size."

**Medium:**
- "You're working on it. Each interval needs to be the same width. This space is bigger than that one." [Visual animation: see Visual Guide]

**Heavy:**
- "Let me show you equal spacing. Each interval must be exactly the same. Watch: this space, this space, this space - all equal. That's how we partition a number line." [Visual animation: see Visual Guide]

### Misconception #5: Counting Tick Marks Instead of Spaces
**When:** Counting marks instead of intervals  
**Confidence:** 85%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Count the spaces between marks, not the marks."
- "We count intervals, not tick marks."

**Medium:**
- "Here's a hint: the spaces between marks are what we count, not the marks themselves. Try counting spaces." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch how we count on a number line. We count spaces, not marks. See: this space is one fourth, this space is another fourth. Marks are just there to show where spaces end." [Visual animation: see Visual Guide]

### Misconception #6: Reversing Numerator and Denominator
**When:** Top and bottom numbers swapped  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "You have the right numbers - check their positions."
- "Check which number goes on top."
- "Look at the order of the numbers."

**Medium:**
- "Looks like these are flipped. Shaded parts go on top, total parts go on bottom." [Visual animation: see Visual Guide]
- "You're working on it. The numerator (top) counts shaded parts. The denominator (bottom) counts total parts." [Visual animation: see Visual Guide]

**Heavy:**
- "Let me show you the order: count shaded parts - that's your top number. Count total parts - that's your bottom number. So 3 shaded out of 4 total is 3/4." [Visual animation: see Visual Guide]
- "Watch: if I have 2 parts shaded (numerator) out of 5 total (denominator), that's 2/5. Top number = shaded. Bottom number = total." [Visual animation: see Visual Guide]

### Misconception #7: Difficulty Recognizing Equivalence
**When:** Can't see equal amounts in different representations  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Look at the shaded amounts - are they the same?"
- "Check how much is shaded in each."

**Medium:**
- "You're getting there. These look different but show the same amount. Look at the total shaded space." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch this. This bar has 2 out of 4 shaded - that's 2/4. This bar has 1 out of 2 shaded - that's 1/2. But look: the shaded amounts take up the same space. Different fractions, same amount." [Visual animation: see Visual Guide]

### Misconception #8: Errors Comparing Unlike Fractions
**When:** Thinking more parts = bigger pieces  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Look at the actual size of each piece."
- "Check which pieces are bigger."

**Medium:**
- "More parts means smaller pieces. Which bar has pieces that take up more space?" [Visual animation: see Visual Guide]
- "You're working on it. More parts doesn't mean bigger pieces - it means smaller ones." [Visual animation: see Visual Guide]

**Heavy:**
- "See how 1/3 is bigger than 1/8? When we cut into fewer pieces, each piece is larger. Three pieces means bigger parts." [Visual animation: see Visual Guide]
- "Watch this. This bar has 3 parts - each part is this big. This bar has 8 parts - each part is much smaller. More parts = smaller pieces." [Visual animation: see Visual Guide]

### Misconception #9: Fractions Only Exist in Shapes
**When:** Can't see fractions in other representations  
**Confidence:** 90%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Fractions work on number lines too."
- "This shows the same fraction, just differently."

**Medium:**
- "You're getting there. Fractions aren't just shapes - they're positions on number lines and symbols too." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch. In a shape, 1/4 is one shaded part out of four. On a number line, 1/4 is a position - one jump out of four equal jumps to 1. Same fraction, different way to show it." [Visual animation: see Visual Guide]

### Misconception #10: Overgeneralizing Rules
**When:** Applying one rule incorrectly to all contexts  
**Confidence:** 85%+ required  
**Available:** Light, Medium, Heavy

**Light:**
- "Check with the visual - does that rule work here?"
- "Look at the pieces, not just the numbers."

**Medium:**
- "You're working on it. That rule doesn't work for denominators. More parts means each piece is smaller." [Visual animation: see Visual Guide]

**Heavy:**
- "Watch how this works. For numerators, bigger is more: 3/4 > 1/4 because we have more pieces. For denominators, bigger means smaller pieces: 1/8 < 1/4 because eighths are tiny. Context matters." [Visual animation: see Visual Guide]

---

## ERROR PATTERN DECISION MATRIX

### How to Determine If Error Is Detectable

**Include this error pattern ONLY if you can answer YES to:**
1. Does this error pattern apply to this specific interaction type?
2. Can the system observe clear evidence of this error?
3. Can you write a simple detection rule?

**Examples of Detectable:**
- ✅ "Student shaded 4 parts but fraction is 3/4" → Counting Error (count ≠ numerator)
- ✅ "Student clicked at position 6/4 but correct is 5/4" → Off-by-One (position off by 1 interval)
- ✅ "Student wrote 4/3 but visual shows 3/4" → Misconception #6 (numerator/denominator reversed)

**Examples of NOT Detectable:**
- ❌ "Student doesn't understand equivalence" → Too vague, no clear evidence
- ❌ "Student is confused" → Mental state, not observable
- ❌ "Student might have..." → Speculation, no certainty

### Decision Matrix

| Error Pattern | When to Include | How System Detects It | Available Levels |
|--------------|-----------------|------------------------|------------------|
| **Generic** | **Every interaction** | **N/A - fallback for all errors** | **L-M-H (REQUIRED)** |
| Counting Error | Shading, Partitioning, Number lines | Compare count to expected: `count ≠ target` | L-M-H |
| Off-by-One | Number lines, Click positions | Check position: `abs(position - correct) == 1` | L-M-H |
| Reversed Order | Ordering, Sequencing tasks | Compare sequence: `student_order == reversed(correct)` | L-M-H |
| Reversed Symbol | Comparison with < or > | Check symbol: `student_symbol ≠ correct_symbol` | L-M-H |
| Misconception #1 | Partitioning tasks | Measure part sizes: `not all_parts_equal()` | L-M-H |
| Misconception #2 | Comparing different wholes | Check: `fractions reference different wholes` | L-M-H |
| Misconception #3 | Writing fractions, Mixed tasks | Pattern: student treats num/denom separately | L-M-H |
| Misconception #4 | Number line partitioning | Measure intervals: `not all_intervals_equal()` | L-M-H |
| Misconception #5 | Number line positioning | Compare: `student counted marks vs spaces` | L-M-H |
| Misconception #6 | Shading, Writing fractions | Check: `num == expected_denom && denom == expected_num` | L-M-H |
| Misconception #7 | Equivalence tasks | Student says unequal when visuals show equal amounts | L-M-H |
| Misconception #8 | Comparing unlike denominators | Pattern: student chose larger denominator as larger fraction | L-M-H |
| Misconception #9 | Representation tasks | Student can't identify fraction in non-shape format | L-M-H |
| Misconception #10 | Rule application | Student applied rule incorrectly across contexts | L-M-H |

### Detectability Guidelines by Interaction Type

**Shading Tasks:**
- ✅ Counting Error (count shaded regions)
- ✅ Misconception #6 (shaded denominator instead of numerator)
- ✅ Misconception #1 (if task includes partitioning)

**Number Line Tasks:**
- ✅ Off-by-One (position check)
- ✅ Counting Error (count intervals)
- ✅ Misconception #4 (measure spacing)
- ✅ Misconception #5 (ticks vs spaces pattern)

**Comparison Tasks:**
- ✅ Reversed Symbol (< vs >)
- ✅ Misconception #8 (unlike denominator confusion)
- ✅ Misconception #2 (different wholes)

**Partitioning Tasks:**
- ✅ Counting Error (count parts)
- ✅ Misconception #1 (measure equality)

**Ordering/Sequencing:**
- ✅ Reversed Order (sequence check)

**Writing Fractions:**
- ✅ Misconception #6 (num/denom reversal)
- ✅ Misconception #3 (independence pattern)

**Equivalence Tasks:**
- ✅ Misconception #7 (equivalence recognition)



