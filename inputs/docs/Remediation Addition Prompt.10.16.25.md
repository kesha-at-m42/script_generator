# **REMEDIATION ADDITION PROTOCOL**

## **Pipeline Step: Add Remediations to Interaction Scripts**

Version: 2.0  
 For: Console Claude adding remediations to completed interaction scripts  
 Required Inputs: (1) Interaction script, (2) Visual Scaffolds TSV, (3) Remediation System v2.0

---

## **YOUR TASK**

Add remediation OPTIONS at each level (Light, Medium, Heavy) to every interaction.

**KEY CONCEPT:** Students progress through ONE sequence (Light → Medium → Heavy, max 3 attempts). At EACH level, the system selects which remediation to serve based on real-time error detection. Your job is to provide all applicable options at each level.

**Example:**

* Student attempts → Wrong → **Light level** → System detects Counting Error → Serves Counting Error Light  
* Student attempts → Wrong → **Medium level** → System detects Misconception \#3 → Serves Misconception \#3 Medium  
* Student attempts → Wrong → **Heavy level** → System detects Misconception \#6 → Serves Misconception \#6 Heavy

You prepare the options. System decides which to use.

---

## **STEP 1: IDENTIFY TASK TYPE AND APPLICABLE ERROR PATTERNS**

For each interaction in script:

1. **Match task to TSV** by Visual Type \+ Task Category \+ Interaction Type  
2. **Find all applicable error patterns** in TSV for this task (Generic, Common Errors, Misconceptions)  
3. **Note which options to prepare** at each level:  
   * Generic (always \- this is your fallback)  
   * Common Error types (if HIGH confidence detection possible)  
   * Misconception \#X (if 90%+ confidence detection possible)

**Example TSV Lookup:**

```
Task: "Shade X Parts" on Rectangle Bars
TSV Shows:
- Generic (always present)
- Counting Error (student shades wrong number)
- Misconception #6 (student shades denominator count)
- Misconception #3 (doesn't connect numerator to action)

Therefore prepare options at EACH level (L-M-H) for:
✓ Generic
✓ Common_Error_Counting
✓ Misconception_#6
✓ Misconception_#3
```

---

## **STEP 2: DETERMINE REMEDIATION OPTIONS AT EACH LEVEL**

**Critical Concept:** There is ONE remediation sequence (Light → Medium → Heavy, max 3 attempts). At EACH level, you prepare MULTIPLE remediation options. The system detects the error in real-time and selects which option to serve.

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
           
System takes over after 3 attempts
```

**For Each Interaction, Prepare:**

**Light Level Options:**

* ✅ Generic Light (always required \- fallback for undetectable errors)  
* ✅ Common\_Error\_X Light (if TSV shows \+ HIGH confidence detection)  
* ✅ Misconception\_\#Y Light (if TSV shows \+ 90%+ confidence detection)

**Medium Level Options:**

* ✅ Generic Medium (always required \- fallback)  
* ✅ Common\_Error\_X Medium (if TSV shows \+ HIGH confidence detection)  
* ✅ Misconception\_\#Y Medium (if TSV shows \+ 90%+ confidence detection)

**Heavy Level Options:**

* ✅ Generic Heavy (always required \- fallback)  
* ✅ Common\_Error\_X Heavy (if TSV shows \+ HIGH confidence detection)  
* ✅ Misconception\_\#Y Heavy (if TSV shows \+ 90%+ confidence detection)

**Detection Confidence Check:**

* Common Error: HIGH confidence required (clearly observable procedural error)  
* Misconception: 90%+ confidence required (clear conceptual error)  
* If unsure → Generic option handles it

---

## **STEP 3: WRITE REMEDIATION OPTIONS AT EACH LEVEL**

### **Generic Track (Always Required)**

**Light Remediation (10-20 words)** \- NO visual

*With Error Signal (40-50% of interactions):*

* "Not quite. Count seven fourths from zero."  
* "Almost. Check your spacing between marks."  
* "Let's try again. Five equal jumps total."  
* "Let's look closely \- seven fourths from zero."  
* "Let's see \- seven fourths from zero."  
* "Let's look at this problem again."  
* "Let's take another look."  
* "Let's try that again."  
* "Give it another try. Remember…"  
* "Let's give it another try. Remember…"

*Without Error Signal (50-60% of interactions):*

* "Count seven fourths from zero."  
* "Check the spacing between marks."  
* "Five equal jumps from zero."  
* "Same size jumps past 1."  
* "Seven equal jumps from zero."  
* Direct guidance with no preamble  
* "Check..." \+ what to check  
* "Count..." \+ what to count  
* Simple imperative statements

**Medium Remediation (20-30 words)** \- MUST include \[Visual: from TSV\]

*Approved Starters:*

* "Let's think about this together. Four fourths equals 1, then three more fourths gets us to 7/4." \[Visual: from TSV\]  
* "Here's a hint: three thirds make 1, then two more thirds puts us at 5/3." \[Visual: from TSV\]  
* "You're working on it. Here's what helps \- each fourth stays the same size even past 1." \[Visual: from TSV\]  
* "You're getting there. The key is counting from zero: 1/3, 2/3, 3/3 equals one." \[Visual: from TSV\]  
* "Let's think about this a bit more. You need 4 equal parts." \[Visual: from TSV\]  
* "Still tricky? Try this..." \+ specific help \[Visual: from TSV\]  
* "Here's a different approach..." \+ guidance \[Visual: from TSV\]

**Heavy Remediation (30-60 words)** \- MUST include \[Modeling\] \+ \[Visual: from TSV\]

*Approved Openings:*

* "This is tricky, so let's work through it together. Starting from zero: 1/4, 2/4, 3/4, 4/4 lands at 1\. Then 5/4, 6/4, 7/4. Seven fourths total." \[Visual: from TSV\] \[Modeling\]  
* "Let me help you with this one. We need eleven fourths: 4/4 gets to 1, 8/4 to 2, then three more fourths makes 11/4." \[Visual: from TSV\] \[Modeling\]  
* "Here, I'll walk you through this one. Three thirds equal one whole. Two more thirds past that makes five thirds total \- that's 5/3." \[Visual: from TSV\] \[Modeling\]  
* "These can be challenging. Let's trace through step by step. Four fourths equals 1, then three more fourths gets us to 7/4." \[Visual: from TSV\] \[Modeling\]  
* "This can be tricky, so let's do it together. \[complete step-by-step demonstration\]" \[Visual: from TSV\] \[Modeling\]  
* "Let's work through this together..." \[complete demonstration\] \[Visual: from TSV\] \[Modeling\]  
* "Let me work through it with you. \[step-by-step walkthrough\]" \[Visual: from TSV\] \[Modeling\]  
* "Here, let me show you: \[complete demonstration\]" \[Visual: from TSV\] \[Modeling\]  
* "Let's do it together. Here's how we solve it..." \[demonstration\] \[Visual: from TSV\] \[Modeling\]  
* "Let's walk through this step by step together..." \[demonstration\] \[Visual: from TSV\] \[Modeling\]  
* "Let me help a bit more. \[demonstration\]" \[Visual: from TSV\] \[Modeling\]  
* "Okay, let me show you another way..." \[demonstration\] \[Visual: from TSV\] \[Modeling\] (occasional only)

*Post-Modeling (REQUIRED \- Use ONLY These):*

* "There we go."  
* "See how that works?"  
* "It's okay if this is tricky."  
* "You're getting it now."  
* "Now you understand."  
* "That makes sense now, right?"  
* "That's it \- now you've got it."  
* "Good \- you understand now."  
* "Now you see the pattern."

*NEVER After Modeling:*

* ✗ "Perfect\!" (they didn't do it alone)  
* ✗ "You figured it out\!" (guide showed them)  
* ✗ "Great job\!" (too independent)  
* ✗ "Excellent work\!" (overpraises assisted work)

---

### **Common Error Tracks (When TSV Shows)**

**Counting Error** \- Wrong number created/selected, all parts equal

*Light (10-20 words):*

* "Count your parts \- you need exactly 4."  
* "Check how many parts you made."  
* "Count the shaded parts again."  
* "Count again \- we need 3 shaded."

*Medium (20-30 words):*

* "You're close\! You made 5 parts, but we need 4\. Try combining two of them." \[Visual: from TSV\]  
* "You shaded 2, but we need 3\. Count the shaded parts again." \[Visual: from TSV\]  
* "You're working on it. Count total parts \- we need exactly 4 equal sections." \[Visual: from TSV\]

*Heavy (30-60 words):*

* "Let me show you. We need 4 parts total. Count with me as we divide: 1, 2, 3, 4\. That's it\!" \[Visual: from TSV\] \[Modeling\]  
* "Here's how we do this. Count each part: 1, 2, 3, 4, 5\. We have 5, but need 4\. Let me show you the right number." \[Visual: from TSV\] \[Modeling\]

---

**Off-by-One Error** \- One space/interval off

*Light:*

* "Check your position \- you're one space off."  
* "Almost there \- adjust by one interval."  
* "Count the spaces one more time."

*Medium:*

* "You're very close\! Move one more interval to the right." \[Visual: from TSV\]  
* "You're getting there. Check the spacing \- you need one more jump." \[Visual: from TSV\]

*Heavy:*

* "Here's how we find the exact spot. Count each interval: 1/4, 2/4, 3/4, 4/4 equals 1, then 5/4. See? We need to go one more space." \[Visual: from TSV\] \[Modeling\]

---

**Reversed Order** \- Selected backwards sequence

*Light:*

* "Check the order \- we need biggest to smallest."  
* "Look at the instruction again \- smallest to largest."

*Medium:*

* "You're working on it. The instruction asks for smallest to largest. Try reversing your order." \[Visual: from TSV\]

*Heavy:*

* "Let me show you. We need smallest to largest. This piece is smallest, this is medium, this is largest. That's the order: smallest first, largest last." \[Visual: from TSV\] \[Modeling\]

---

**Reversed Symbol** \- Uses \< instead of \> or vice versa

*Light:*

* "Check your symbol \- which way does it point?"  
* "Look at the symbol direction again."

*Medium:*

* "You're getting there. The small end points to the smaller number. Check which fraction is smaller." \[Visual: from TSV\]

*Heavy:*

* "Here's a way to think about the symbols. The small end points to the smaller fraction. 3/8 is smaller than 5/8, so: 3/8 \< 5/8. The small end points left to the smaller number." \[Visual: from TSV\] \[Modeling\]

---

### **Misconception Types (When TSV Shows \+ 90%+ Confidence)**

**CRITICAL PEDAGOGICAL REQUIREMENT:** When using misconception remediation (90%+ confidence detection), explicitly name what the student did wrong. This helps students understand their specific error and build metacognition.

**Structure by Level:**

* **Light:** May be indirect OR direct ("Are these equal?" OR "These aren't equal")  
* **Medium:** MUST explicitly identify the error made ("Looks like these are flipped", "Your parts aren't equal")  
* **Heavy:** MUST show error \+ explain why incorrect \+ model correct approach

---

**Misconception \#1: Equal vs. Unequal Parts**

*Light:*

* "Are all these parts the same size?"  
* "Check if all your parts are equal."  
* "Look at the sizes of each part."

*Medium:*

* "**Your parts need to be equal. This part is bigger than this one.**" \[Visual: from TSV\]  
* "Fractions only work when all parts are equal. **This section doesn't match the others.**" \[Visual: from TSV\]

*Heavy:*

* "**I see you made parts of different sizes. That's a common mistake.** For equal parts, every piece must be exactly the same size. Watch \- I'll measure each one. See how this is bigger? Let's make them all match." \[Visual: from TSV\] \[Modeling\]  
* "**Look \- this part is bigger than that part.** When parts aren't equal, we can't use fractions. We need same-sized pieces. Here's how to check: \[demonstrates measuring\]." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#2: Misidentifying the Whole**

*Light:*

* "Check what the whole bar is."  
* "Look at the complete shape first."

*Medium:*

* "You're working on it. These bars are different sizes. We need to compare pieces from the same whole." \[Visual: from TSV\]

*Heavy:*

* "Watch this. This whole bar is our '1'. These parts are from this bar. That whole bar is different \- it's a different '1'. We can only compare fractions from the same whole." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#3: Numerator/Denominator as Independent**

*Light:*

* "These numbers work together \- check what each shows."  
* "The top and bottom numbers are connected."

*Medium:*

* "The top and bottom numbers are connected. Top counts what you have, bottom counts total parts." \[Visual: from TSV\]  
* "You're getting there. These numbers describe the same situation together." \[Visual: from TSV\]

*Heavy:*

* "Watch: if I have 2 parts (numerator) out of 5 total (denominator), that's 2/5. The numbers describe the same situation." \[Visual: from TSV\] \[Modeling\]  
* "Let me show you how they work together. Count shaded parts \- that's your top number. Count total parts \- that's your bottom number. They both describe this one fraction." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#4: Improper Spacing on Number Line**

*Light:*

* "Check your spacing \- all intervals should be equal."  
* "Make sure each space is the same size."

*Medium:*

* "You're working on it. Each interval needs to be the same width. This space is bigger than that one." \[Visual: from TSV\]

*Heavy:*

* "Let me show you equal spacing. Each interval must be exactly the same. Watch: this space, this space, this space \- all equal. That's how we partition a number line." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#5: Counting Tick Marks Instead of Spaces**

*Light:*

* "Count the spaces between marks, not the marks."  
* "We count intervals, not tick marks."

*Medium:*

* "Here's a hint: the spaces between marks are what we count, not the marks themselves. Try counting spaces." \[Visual: from TSV\]

*Heavy:*

* "Watch how we count on a number line. We count spaces, not marks. See: this space is one fourth, this space is another fourth. Marks are just there to show where spaces end." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#6: Reversing Numerator and Denominator**

*Light:*

* "You have the right numbers \- check their positions."  
* "Check which number goes on top."  
* "Look at the order of the numbers."

*Medium:*

* "**Looks like these are flipped.** Shaded parts go on top, total parts go on bottom." \[Visual: from TSV\]  
* "**You swapped the numbers.** The numerator (top) counts shaded parts. The denominator (bottom) counts total parts." \[Visual: from TSV\]

*Heavy:*

* "**I see you reversed the numbers \- you put 4 on top and 3 on bottom.** That's backwards. Let me show you the order: count shaded parts \- that's your top number. Count total parts \- that's your bottom number. So 3 shaded out of 4 total is 3/4." \[Visual: from TSV\] \[Modeling\]  
* "**You flipped them \- the 5 should be on top, not the 8\.** Watch: if I have 5 parts shaded (numerator) out of 8 total (denominator), that's 5/8. Top number \= shaded. Bottom number \= total." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#7: Difficulty Recognizing Equivalence**

*Light:*

* "Look at the shaded amounts \- are they the same?"  
* "Check how much is shaded in each."

*Medium:*

* "You're getting there. These look different but show the same amount. Look at the total shaded space." \[Visual: from TSV\]

*Heavy:*

* "Watch this. This bar has 2 out of 4 shaded \- that's 2/4. This bar has 1 out of 2 shaded \- that's 1/2. But look: the shaded amounts take up the same space. Different fractions, same amount." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#8: Errors Comparing Unlike Fractions**

*Light:*

* "Look at the actual size of each piece."  
* "Check which pieces are bigger."

*Medium:*

* "**You chose the bigger number, but more parts means smaller pieces.** Which bar has pieces that take up more space?" \[Visual: from TSV\]  
* "**That's backwards \- more parts doesn't mean bigger pieces.** It means smaller ones. Check the visual." \[Visual: from TSV\]

*Heavy:*

* "**I see you picked 1/8 because 8 is bigger than 3\. That's a common mistake.** See how 1/3 is bigger than 1/8? When we cut into fewer pieces, each piece is larger. Three pieces means bigger parts." \[Visual: from TSV\] \[Modeling\]  
* "**You thought more parts \= bigger, but it's the opposite.** Watch this. This bar has 3 parts \- each part is this big. This bar has 8 parts \- each part is much smaller. More parts \= smaller pieces." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#9: Fractions Only Exist in Shapes**

*Light:*

* "Fractions work on number lines too."  
* "This shows the same fraction, just differently."

*Medium:*

* "You're getting there. Fractions aren't just shapes \- they're positions on number lines and symbols too." \[Visual: from TSV\]

*Heavy:*

* "Watch. In a shape, 1/4 is one shaded part out of four. On a number line, 1/4 is a position \- one jump out of four equal jumps to 1\. Same fraction, different way to show it." \[Visual: from TSV\] \[Modeling\]

---

**Misconception \#10: Overgeneralizing Rules**

*Light:*

* "Check with the visual \- does that rule work here?"  
* "Look at the pieces, not just the numbers."

*Medium:*

* "You're working on it. That rule doesn't work for denominators. More parts means each piece is smaller." \[Visual: from TSV\]

*Heavy:*

* "Watch how this works. For numerators, bigger is more: 3/4 \> 1/4 because we have more pieces. For denominators, bigger means smaller pieces: 1/8 \< 1/4 because eighths are tiny. Context matters." \[Visual: from TSV\] \[Modeling\]

**Key Point:** These are OPTIONS at each level, not sequential tracks. System serves one option per attempt based on real-time error detection.

---

## **STEP 4: PULL VISUAL SCAFFOLDS FROM TSV**

1. **Find task row** in TSV (Visual Type \+ Task Category \+ Interaction)  
2. **Find error pattern column** (Generic/Counting Error/Misconception \#X)  
3. **Copy visual scaffold** from that cell into \[Visual: description\]  
4. **If cell empty:** Use similar task's visual or note for human review

---

## **STEP 5: ENSURE VARIETY**

**Per Module (assuming 8-12 interactions):**

* Minimum 8 different Light patterns  
* Rotate error signals (40-50% with signal, 50-60% without)  
* Never repeat exact phrase within 3 interactions  
* "Remember" maximum 2-3 times total (Medium/Heavy only)

**Track Across Script:**

* \[ \] No repeated Light language within 3 problems  
* \[ \] Error signal distribution balanced  
* \[ \] "Remember" count ≤ 3 for entire module  
* \[ \] Post-modeling language varies (if multiple Heavy instances)

---

## **STEP 6: QUALITY CHECKS**

**Before Submitting:**

**Structure:**

* \[ \] Every interaction has Generic options at L-M-H (required fallback)  
* \[ \] All applicable Common Error options included at L-M-H  
* \[ \] All applicable Misconception options included at L-M-H  
* \[ \] All Medium options have \[Visual: ...\] from TSV  
* \[ \] All Heavy options have \[Modeling\] tag \+ \[Visual: ...\] from TSV  
* \[ \] All remediation has \[Meta\_Remediation\] tag  
* \[ \] Labels correct (Generic, Common\_Error\_X, Misconception\_\#X)

**Language:**

* \[ \] Light options \= 10-20 words each  
* \[ \] Medium options \= 20-30 words each  
* \[ \] Heavy options \= 30-60 words each  
* \[ \] Post-modeling uses only approved language (Section 8\)  
* \[ \] Language patterns from Step 3 examples

**Variety:**

* \[ \] No exact repetition within 3 interactions  
* \[ \] Error signal distribution appropriate (40-50% with signal)  
* \[ \] "Remember" ≤ 3 times total module  
* \[ \] Different Generic language across interactions

**Visual Integration:**

* \[ \] All Medium/Heavy options have visual descriptions  
* \[ \] Visuals match TSV scaffolds for each error type  
* \[ \] Visual state notation if needed (\[NEW\], \[MODIFY\], etc.)

**Conceptual:**

* \[ \] Generic options work for ambiguous/unknown errors  
* \[ \] Common Error options target procedural mistakes  
* \[ \] Misconception options target conceptual confusion  
* \[ \] Each level has appropriate number of options (1-4 typically)

---

## **QUICK REFERENCE: REMEDIATION OPTIONS BY ERROR PATTERN**

| Error Pattern | When to Include | Confidence Required | Available at All Levels? |
| ----- | ----- | ----- | ----- |
| **Generic** | Every interaction | Always | L-M-H (required) |
| **Counting Error** | Wrong count, equal parts | HIGH | L-M-H (if detectable) |
| **Off-by-One** | One space off | HIGH | L-M-H (if detectable) |
| **Reversed Order** | Backwards sequence | HIGH | L-M-H (if detectable) |
| **Reversed Symbol** | Wrong \< or \> | HIGH | L-M-H (if detectable) |
| **Misconception \#1** | Unequal treated as equal | 90%+ | L-M-H (if detectable) |
| **Misconception \#2** | Wrong whole | 90%+ | L-M-H (if detectable) |
| **Misconception \#3** | Independent num/denom | 90%+ | L-M-H (if detectable) |
| **Misconception \#4** | Uneven spacing | 85%+ | L-M-H (if detectable) |
| **Misconception \#5** | Counts ticks | 85%+ | L-M-H (if detectable) |
| **Misconception \#6** | Reversed num/denom | 90%+ | L-M-H (if detectable) |
| **Misconception \#7** | Can't see equivalence | 90%+ | L-M-H (if detectable) |
| **Misconception \#8** | Size confusion | 90%+ | L-M-H (if detectable) |
| **Misconception \#9** | Only shapes | 90%+ | L-M-H (if detectable) |
| **Misconception \#10** | Rule overgeneralization | 85%+ | L-M-H (if detectable) |

**Remember:** Include options at ALL three levels (L-M-H) for each detectable error pattern. System selects which option to serve at each attempt.

---

## **PHASE-SPECIFIC REQUIREMENTS**

| Phase | Remediation Requirement |
| ----- | ----- |
| Warmup | Light minimum (Heavy if key prior knowledge) |
| Lesson | Full L-M-H all interactions |
| Exit Check | Full L-M-H all interactions (MANDATORY) |
| Practice | Full L-M-H (Light only for confidence builders) |
| Synthesis | Light minimum (Full L-M-H for pattern discovery) |
| Challenge | None (assessment mode) |

---

## **OUTPUT FORMAT**

Add remediation directly after each interaction, organized by LEVEL (not by track):

```
Activity X - [Title]
Visual: [Description]
Prompt: "[Instruction]"
Guide: "[Support]"

If incorrect:

--- LIGHT LEVEL OPTIONS ---
[Light_Remediation] [Meta_Remediation]: "[10-20 words]"

[Light_Remediation - Common_Error_Counting] [Meta_Remediation]: "[10-20 words]"
(Include if applicable)

[Light_Remediation - Misconception_#6] [Meta_Remediation]: "[10-20 words]"
(Include if applicable)

--- MEDIUM LEVEL OPTIONS ---
[Medium_Remediation] [Meta_Remediation]: "[20-30 words]"
[Visual: Description from TSV]

[Medium_Remediation - Common_Error_Counting] [Meta_Remediation]: "[20-30 words]"
[Visual: Description from TSV]
(Include if applicable)

[Medium_Remediation - Misconception_#6] [Meta_Remediation]: "[20-30 words]"
[Visual: Description from TSV]
(Include if applicable)

--- HEAVY LEVEL OPTIONS ---
[Heavy_Remediation] [Meta_Remediation] [Modeling]: "[30-60 words revealing answer]"
[Visual: Description from TSV]
Guide: "[Approved post-modeling acknowledgment]"

[Heavy_Remediation - Common_Error_Counting] [Meta_Remediation] [Modeling]: "[30-60 words]"
[Visual: Description from TSV]
Guide: "[Approved post-modeling acknowledgment]"
(Include if applicable)

[Heavy_Remediation - Misconception_#6] [Meta_Remediation] [Modeling]: "[30-60 words]"
[Visual: Description from TSV]
Guide: "[Approved post-modeling acknowledgment]"
(Include if applicable)
```

**Note:** System will serve ONE option per attempt based on detected error. Writers provide all applicable options at each level.

---

## **WHEN TO FLAG FOR HUMAN REVIEW**

**Stop and Flag If:**

* TSV visual scaffold cell is empty for needed error pattern  
* Uncertain about error detection confidence level  
* Task type not found in TSV  
* Conflicting guidance between TSV and Remediation System  
* Module complexity suggests different tier requirements

---

## **PIPELINE COMPLETE WHEN:**

* \[ \] All interactions have remediation options at each level (L-M-H)  
* \[ \] Generic options present for every interaction (fallback)  
* \[ \] Common Error options included where detectable with HIGH confidence  
* \[ \] Misconception options included where detectable with 90%+ confidence  
* \[ \] All visuals pulled from TSV for appropriate error types  
* \[ \] All language pulled from Step 3 approved examples  
* \[ \] Variety requirements met across module  
* \[ \] Quality checks passed  
* \[ \] Format matches output template (options organized by level)

**Version:** 2.0  
 **Pipeline Step:** Add Remediations  
 **Next Step:** Enhancement & Voice Polish