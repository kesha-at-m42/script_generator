# **REMEDIATION SYSTEM \- THREE-TYPE ARCHITECTURE**

Version: 2.0  
 Last Updated: October 2025  
 Purpose: Authoritative guide for all remediation across learning modules

**Word Count Philosophy:** Ranges based on real examples. Faster is ok if it makes the point clearly. Quality and clarity matter more than hitting exact word counts.

---

## **TABLE OF CONTENTS**

**SECTION 1** \- Three-Type System Architecture  
 **SECTION 2** \- Type 1: Generic Remediation (Always Present)  
 **SECTION 3** \- Type 2: Common Error Remediation (Predictable Procedural)  
 **SECTION 4** \- Type 3: Misconception Remediation (Conceptual)  
 **SECTION 5** \- Light Remediation Language Patterns  
 **SECTION 6** \- Medium Remediation Language Patterns  
 **SECTION 7** \- Heavy Remediation Language Patterns  
 **SECTION 8** \- Post-Modeling Language  
 **SECTION 9** \- Error Signal Strategy  
 **SECTION 10** \- Avoiding Condescending Language  
 **SECTION 11** \- Practice Phase Variety Strategies  
 **SECTION 12** \- Remediation Completeness by Phase  
 **SECTION 13** \- Exit Check Special Requirements  
 **SECTION 14** \- Critical Reminders and Quality Checklist  
 **SECTION 15** \- Remediation Red Flags  
 **SECTION 16** \- Common Error Patterns by Task Type  
 **SECTION 17** \- Full Misconceptions Reference

---

## **SECTION 1: Three-Type System Architecture**

### **1.1 The New Paradigm**

Every task has **THREE types of remediation available:**

```
At Each Level (Light, Medium, Heavy):

OPTION 1: GENERIC (Always Available)
└─ Fallback for unpredictable/ambiguous errors

OPTION 2: COMMON ERRORS (Add When Detectable)
└─ Targets predictable procedural mistakes (HIGH confidence)

OPTION 3: MISCONCEPTIONS (Add When Highly Confident)
└─ Targets conceptual errors (90%+ confidence)
```

**How It Works:**

* Students progress through ONE sequence: Light → Medium → Heavy (max 3 attempts)  
* At EACH level, multiple remediation options are available  
* System detects error in real-time and selects appropriate option  
* Writers prepare all applicable options at each level

**Example Student Journey:**

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

### **1.2 Detection Priority Framework**

```
ERROR OCCURS
    ↓
CHECK: Does error match MISCONCEPTION pattern? (HIGH confidence 90%+)
    ↓
    YES → Use Misconception_#X remediation
    NO → ↓
    
CHECK: Does error match COMMON ERROR pattern? (HIGH confidence)
    ↓
    YES → Use Common_Error_[Type] remediation
    NO → ↓
    
DEFAULT → Use Generic remediation
```

### **1.3 Quick Complexity Guide**

**Task Type Determines Remediation Depth:**

* **2 choices** \= 1 level (Light only)  
  * Example: Binary true/false, yes/no questions  
  * Generic Light required, add specific types if detectable  
* **3-4 choices** \= 2 levels (Light→Medium)  
  * Example: Multiple choice with 3-4 options  
  * Generic L-M required, add specific types if detectable  
* **Construction tasks** \= 3 levels (Light→Medium→Heavy)  
  * Example: Partition shapes, place on number line, shade parts  
  * Full L-M-H required for all applicable types

**Reality Check:**

* Don't over-engineer simple tasks (binary questions don't need Heavy)  
* Don't under-engineer complex tasks (construction always needs full L-M-H)  
* When in doubt, build full L-M-H \- better to have it and not need it

### **1.4 Three-Tier Error Classification**

**Tier 1: Generic (Unpredictable)**

* **When to use:** Error doesn't match known patterns  
* **Characteristics:** Could be any cause, no clear pattern, ambiguous reasoning  
* **Example:** Student makes unexpected selection with no clear reason

**Tier 2: Common Error (Predictable, Non-Conceptual)**

* **When to use:** Error matches predictable simple mistake pattern  
* **Characteristics:** Procedural/execution error, NOT conceptual, can be detected with HIGH confidence  
* **Common types:** Counting errors, off-by-one, misread instruction, incomplete action  
* **Example:** Asked for 4 parts, creates 5 equal parts (counting error, concept intact)

**Tier 3: Misconception (Conceptual)**

* **When to use:** Error reveals conceptual misunderstanding with HIGH confidence (90%+)  
* **Characteristics:** Systematic conceptual error, maps to known misconception (\#1-\#10)  
* **Example:** Creates 4 unequal parts when asked for "4 equal parts" (doesn't understand "equal")

### **1.5 Key Distinction: Procedural vs Conceptual**

**Critical Question:** Is it conceptual or procedural?

| Student Action | Classification | Reasoning |
| ----- | ----- | ----- |
| Shades 4 parts when asked for 3/4 | **Misconception \#6** | Systematic conceptual error (denominator confusion) |
| Shades 2 parts when asked for 3/4 | **Common Error \- Counting** | Miscounted, not conceptual |
| Creates 5 equal parts instead of 4 | **Common Error \- Counting** | Counting mistake, concept intact |
| Creates 4 unequal parts | **Misconception \#1** | Doesn't understand "equal parts" |

### **1.6 The Reality of Remediation**

**Student Distribution:**

* 70% of students see Light only (resolve on first redirect)  
* 25% of students reach Medium (need scaffolding)  
* 5% of students need Heavy (require modeling)

**Key Insight:** Students rarely see all three levels in sequence, therefore each level needs maximum variety.

### **1.6 The Sequential Rule (Within Each Track)**

**STRICT ORDER \- NEVER alternatives:**

* First error → Light (nudge)  
* Second error → Medium (scaffold)  
* Third error → Heavy (model)

**Never Use:** "Try X or Y" or "another way to think about it"

### **1.8 Implementation Strategy**

**For Each Task, Ask:**

1. **What are the common simple mistakes?** (Counting, off-by-one, etc.)

   * If HIGH confidence detection → Add Common\_Error options at each level  
2. **What are the detectable misconceptions?** (\#1-\#10 with HIGH confidence)

   * If 90%+ confidence → Add Misconception\_\#X options at each level  
3. **What could be ambiguous/random?** (Everything else)

   * Always have Generic options as fallback (required at every level)

**Build Priority:**

1. ✅ Generic L-M-H (always, for every task)  
2. ✅ Common\_Error L-M-H options (when predictable with HIGH confidence)  
3. ✅ Misconception\_\#X L-M-H options (when conceptual with 90%+ confidence)

### **1.9 Benefits of Three-Type System**

* More precise remediation without over-diagnosing  
* Distinguishes "oops, miscounted" from "doesn't understand concept"  
* Targeted support for predictable procedural errors  
* Conservative fallback to Generic when uncertain  
* Avoids false positives in misconception detection  
* **Flexible response**: System can serve different error types at different levels based on actual student behavior  
* **Efficient**: Only one remediation served per attempt, selected based on detected error

### **1.10 Critical Violations (Must Not Have)**

**Never Include These:**

* ❌ **Alternative paths** ("Try X or Y" / "Another way to think about it")  
  * Reason: System serves ONE option per attempt, not choices  
* ❌ **Light remediation that teaches new content**  
  * Reason: Light redirects existing knowledge, doesn't introduce concepts  
* ❌ **Medium without visual scaffolding**  
  * Reason: Visual scaffold is mandatory at Medium level  
* ❌ **Heavy without \[Modeling\] tag**  
  * Reason: Heavy always includes full demonstration  
* ❌ **Generic-only responses without considering specific types**  
  * Reason: When Common Errors or Misconceptions are detectable with HIGH confidence, add those options  
* ❌ **Infinite loops or circular remediation**  
  * Reason: Max 3 attempts, then system takes over

**If You Find These:** Stop and revise before continuing.

---

## **SECTION 2: Type 1 \- Generic Remediation (Always Present)**

### **2.1 Overview**

**Purpose:** Catch-all for unpredictable, ambiguous, or first-time errors

**When to Use:**

* Error doesn't match known patterns  
* Unclear what happened  
* No clear reason visible  
* First occurrence without pattern

**Characteristics:**

* Most frequently used track (handles majority of errors)  
* Progressive acknowledgment at each level  
* No assumptions about error cause

### **2.2 Generic Light**

**Length:** 10-20 words  
 **Tone:** Brief and direct  
 **Focus:** Simple redirect without diagnosis

**Progressive Acknowledgment:** Simple correction (first attempt)

**Examples:**

* "Not quite. Try again."  
* "Let's look at this problem again."  
* "Let's take another look."  
* "Count seven fourths from zero."  
* "Check the spacing between marks."

### **2.3 Generic Medium**

**Length:** 20-30 words  
 **Tone:** Acknowledge continued struggle  
 **Focus:** General scaffolding without assuming error type  
 **Requirements:** MUST include \[Visual\] line

**Progressive Acknowledgment:** "Still/You're getting there" (second attempt)

**Examples:**

* "Let's think about this together. You need 4 equal parts." \[Visual: Sequential division strategy shown\]  
* "You're working on it. Focus on counting from zero." \[Visual: Highlight starting point\]

### **2.4 Generic Heavy**

**Length:** 30-60 words  
 **Tone:** Full support with complete demonstration  
 **Focus:** Step-by-step walkthrough  
 **Requirements:** MUST include \[Modeling\] tag

**Progressive Acknowledgment:** "This is tricky/challenging" (third attempt)

**Examples:**

* "This is tricky, so let me show you. Starting from zero: 1/4, 2/4, 3/4, 4/4 lands at 1\. Then 5/4, 6/4, 7/4. Seven fourths total." \[Visual: Shows each jump\] \[Modeling\]

---

## **SECTION 3: Type 2 \- Common Error Remediation (Predictable Procedural)**

### **3.1 Overview**

**Purpose:** Target predictable procedural mistakes with HIGH confidence detection

**When to Use:**

* Error matches predictable simple mistake pattern  
* NOT conceptual (student likely knows concept)  
* Procedural/execution error  
* Can be detected with HIGH confidence

**Key Principle:** Only add when you can detect with HIGH confidence. When in doubt, use Generic.

### **3.2 Common Error Types**

#### **Counting Error**

**Pattern:** Creates/selects wrong quantity  
 **Detection:** Count ≠ requested, but all parts equal  
 **Confidence:** HIGH (observable, unambiguous)  
 **Example:** Asked for 4 parts, makes 5 equal parts

#### **Off-by-One**

**Pattern:** Systematically one more/less  
 **Detection:** Position/count \= correct ± 1  
 **Confidence:** HIGH (observable pattern)  
 **Example:** Places fraction one space too far on number line

#### **Misread Instruction**

**Pattern:** Did something other than asked  
 **Detection:** Action doesn't match instruction  
 **Confidence:** MEDIUM (sometimes ambiguous)  
 **Example:** Asked to shade, partitioned instead

#### **Incomplete Action**

**Pattern:** Started but didn't finish  
 **Detection:** Partial completion visible  
 **Confidence:** MEDIUM (may be intentional)  
 **Example:** Shaded 2 parts when asked for 3

#### **Over-Extension**

**Pattern:** Did too much  
 **Detection:** Count \> requested  
 **Confidence:** HIGH (clearly observable)  
 **Example:** Shaded 4 parts when asked for 3

### **3.3 Common\_Error\_Counting Examples**

**Light:**

* "Count your parts \- you need exactly 4."  
* "Check how many parts you made."  
* "Count again \- we need 3 shaded."

**Medium:**

* "You're close\! You made 5 parts, but we need 4\. Try combining two of them." \[Visual: Highlight the extra partition\]  
* "You shaded 2, but we need 3\. Count the shaded parts again." \[Visual: Number each part\]

**Heavy:**

* "Let me show you. We need 4 parts total. Count with me as we divide: 1, 2, 3, 4\. That's it\!" \[Visual: Count each part as created\] \[Modeling\]

### **3.4 Common\_Error\_Off\_By\_One Examples**

**Light:**

* "Check your position \- you're one space off."  
* "Almost there \- adjust by one interval."

**Medium:**

* "You're very close\! Move one more interval to the right." \[Visual: Show correct position highlighted\]

**Heavy:**

* "Here's how we find the exact spot. Count each interval: 1/4, 2/4, 3/4, 4/4 equals 1, then 5/4. See? We need to go one more space." \[Visual: Demonstrate counting\] \[Modeling\]

### **3.5 When NOT to Use Common Error Track**

**Don't Use When:**

* Confidence is MEDIUM or LOW  
* Error could have multiple causes  
* Pattern isn't clearly observable  
* Distinction from misconception is unclear

**Example of Ambiguity:**

* Student shades wrong parts → Could be counting error OR conceptual confusion  
* **Solution:** Use Generic unless you can detect with HIGH confidence

---

## **SECTION 4: Type 3 \- Misconception Remediation (Conceptual)**

### **4.1 Overview**

**Purpose:** Target systematic conceptual errors with 90%+ confidence detection

**When to Use:**

* Error reveals conceptual misunderstanding  
* Maps to known misconception (\#1-\#10)  
* Can be detected with HIGH confidence (90%+)  
* NOT a simple procedural mistake

**Critical Threshold:** Only use when you're 90%+ confident it's the specific misconception

**PEDAGOGICAL REQUIREMENT:** Because misconceptions are detected with 90%+ confidence, remediation should explicitly name what the student did wrong. This helps students:

* Understand their specific error (metacognition)  
* Distinguish this misconception from other errors  
* Build awareness to self-correct in future

### **4.2 Detection Confidence Requirements**

**HIGH Confidence (90%+) Required:**

* Pattern matches known misconception exactly  
* Error is systematic, not random  
* Visual/behavioral evidence is unambiguous  
* Alternative explanations ruled out

**Example of HIGH Confidence:**

* Student asked to create "4 equal parts"  
* Student creates 4 parts of visibly different sizes  
* **Confidence:** HIGH \- clearly Misconception \#1 (Equal vs. Unequal Parts)

**Example of LOW Confidence (Use Generic Instead):**

* Student shades wrong number of parts  
* Could be counting error, could be misconception  
* **Confidence:** LOW \- use Generic or Common\_Error\_Counting

### **4.3 Misconception Remediation Structure**

Each misconception gets full L-M-H progression, just like Generic and Common Errors.

**Format:**

```
[Light_Remediation - Misconception_#X]
[Medium_Remediation - Misconception_#X]
[Heavy_Remediation - Misconception_#X] [Modeling]
```

### **4.4 Example: Misconception \#1 (Unequal Parts)**

**Light:**

* "Are all these parts the same size?"  
* "Check if all your parts are equal."

**Medium:**

* "Your parts need to be equal. This part is bigger than this one." \[Visual: Overlay smallest piece on largest to show difference\]

**Heavy:**

* "For equal parts, every piece must be exactly the same size. Watch \- I'll measure each one. See how this is bigger? Let's make them all match." \[Visual: Demonstrate measuring/comparing each part\] \[Modeling\]

### **4.5 Example: Misconception \#6 (Reversal)**

**Light:**

* "You have the right numbers \- check their positions."  
* "Check which number goes on top."

**Medium:**

* "Looks like these are flipped. Shaded parts go on top, total parts go on bottom." \[Visual: Highlight numerator and denominator positions\]

**Heavy:**

* "Let me show you the order: count shaded parts \- that's your top number. Count total parts \- that's your bottom number. So 3 shaded out of 4 total is 3/4." \[Visual: Step-by-step labeling\] \[Modeling\]

### **4.6 When NOT to Use Misconception Options**

**Don't Use When:**

* Confidence is below 90%  
* Error could be procedural  
* First occurrence (wait for pattern)  
* Mixed signals in student work

**Safe Default:** When in doubt, use Generic or Common\_Error options

---

## **SECTION 5: Light Remediation Language Patterns**

### **5.1 Overview**

**Characteristics:**

* Length: 10-20 words (brief and direct)  
* Tone: Minimal warmth, maximum variety needed  
* Focus: Brief redirect without teaching  
* Frequency: 70% of students see only this level

**Progressive Acknowledgment:** Simple correction (first attempt)

### **5.2 Structure Options**

**With error signal (40-50% of time):**

* Signal \+ brief guidance

**Without error signal (50-60% of time):**

* Direct guidance only

### **5.3 Approved Language Patterns**

**With Error Signal:**

* "Not quite." \+ guidance  
* "Almost." \+ guidance  
* "Let's try again." \+ guidance  
* "Let's look closely \-" \+ specific guidance  
* "Let's see \-" \+ guidance  
* "Let's look at this problem again."  
* "Let's take another look."  
* "Let's try that again."

**Without Error Signal:**

* Direct guidance (no preamble)  
* "Check..." \+ what to check  
* "Count..." \+ what to count  
* Simple imperative statements

### **5.4 Concrete Examples (All Types)**

**Generic Light:**

* "Not quite. Count seven fourths from zero."  
* "Check the spacing between marks."  
* "Five equal jumps from zero."

**Common\_Error\_Counting Light:**

* "Count your parts \- you need exactly 4."  
* "Check how many parts you made."  
* "Count the shaded parts again."

**Misconception\_\#1 Light:**

* "Are all these parts the same size?"  
* "Check if all your parts are equal."

**Misconception\_\#6 Light:**

* "Check which number goes on top."  
* "You have the right numbers \- check their positions."

### **5.5 Avoid in Light**

**Do Not Use:**

* "Remember..." (save for Medium/Heavy)  
* "Give it another try" (redundant)  
* "Let's give it another try" (too wordy)  
* Extended preambles  
* Excessive warmth

**Instead of "Remember..." use:**

* "The key is..."  
* "Focus on..."  
* "Notice that..."  
* "Here's what helps..."

### **5.6 Visual Requirements**

**Light Level:** NO visuals (words only)

---

## **SECTION 6: Medium Remediation Language Patterns**

### **6.1 Overview**

**Characteristics:**

* Length: 20-30 words (faster ok if it makes the point)  
* Tone: Acknowledge continued struggle, collaborative language  
* Focus: Specific hint \+ visual scaffolding  
* Frequency: 25% of students reach this level

**Progressive Acknowledgment:** "Still/You're getting there" (second attempt)

### **6.2 Requirements (Non-negotiable)**

* MUST include \[Visual\] line showing scaffolding  
* Acknowledge struggle \+ specific hint  
* Some warmth appropriate  
* Can use "Remember" sparingly (1-2 times per module max)

### **6.3 Approved Language Patterns**

**Starters:**

* "Let's think about this together..." \+ specific help  
* "Here's a hint:" \+ specific clue  
* "Let's think about this a bit more..." \+ guidance  
* "You're working on it. Here's what helps..." \+ specific support  
* "You're getting there. The key is..." \+ crucial detail  
* "Still tricky? Try this..."  
* "Here's a different approach..."

### **6.4 Template Structure**

**Guide:** "You're working on it. Here's what helps: \[specific hint about denominator/numerator/counting\]"  
 **\[Visual:** Highlight or indicate specific element to focus on\]

### **6.5 Concrete Examples (All Types)**

**Generic Medium:**

* "Let's think about this together. Four fourths equals 1, then three more fourths gets us to 7/4." \[Visual: Highlight the 1 mark\]

**Common\_Error\_Counting Medium:**

* "You're close\! You made 5 parts, but we need 4\. Try combining two of them." \[Visual: Highlight the extra partition\]

**Misconception\_\#1 Medium:**

* "Your parts need to be equal. This part is bigger than this one." \[Visual: Overlay smallest piece on largest to show difference\]

**Misconception\_\#6 Medium:**

* "Looks like these are flipped. Shaded parts go on top, total parts go on bottom." \[Visual: Highlight numerator and denominator positions\]

### **6.6 Visual Requirements**

**Medium Level:** SUBTLE visuals (highlights, dotted lines, numbers)

---

## **SECTION 7: Heavy Remediation Language Patterns**

### **7.1 Overview**

**Characteristics:**

* Length: 30-60 words (accommodates varying problem complexity; faster ok if complete)  
* Tone: Full emotional support, complete demonstration  
* Focus: Step-by-step walkthrough revealing the answer  
* Frequency: 5% of students need this level

**Progressive Acknowledgment:** "This is tricky/challenging" (third attempt)

### **7.2 Required Elements (All 5 mandatory)**

1. \[Modeling\] tag (ALWAYS)  
2. Step-by-step walkthrough  
3. Visual showing complete demonstration  
4. Correct answer revealed at end  
5. Acknowledgment of assisted success (never independent praise)

### **7.3 Approved Opening Language**

* "This is tricky, so let's work through it together..."  
* "This can be tricky, so let's do it together."  
* "Let's work through this together..."  
* "Let me work through it with you."  
* "These can be challenging. Let's trace through step by step..."  
* "Here, let me show you:"  
* "Let's do it together. Here's how we solve it..."  
* "Let's walk through this step by step together..."  
* "Let me help a bit more."  
* "Here, I'll walk you through this one."  
* "Okay, let me show you another way..." (occasional only)

### **7.4 Template Structure**

**Heavy Remediation \[Meta\_Remediation\] \[Modeling\]:** "This is tricky, so let me show you. \[complete demonstration 30-60 words showing each step\]"  
 **\[Visual:** System demonstrates complete solution step by step\]  
 **\[Implicit:** Student completes with guidance \- note for writer only, don't include in script\]  
 **Guide:** "\[Post-modeling acknowledgment\]"

### **7.5 Concrete Examples (All Types)**

**Generic Heavy:**

* "This is tricky, so let's work through it together. Starting from zero: 1/4, 2/4, 3/4, 4/4 lands at 1\. Then 5/4, 6/4, 7/4. Seven fourths total." \[Visual: Shows each jump\] \[Modeling\]

**Common\_Error\_Counting Heavy:**

* "Let me show you. We need 4 parts total. Count with me as we divide: 1, 2, 3, 4\. That's it\!" \[Visual: Count each part as created\] \[Modeling\]

**Misconception\_\#1 Heavy:**

* "For equal parts, every piece must be exactly the same size. Watch \- I'll measure each one. See how this is bigger? Let's make them all match." \[Visual: Demonstrate measuring/comparing each part\] \[Modeling\]

**Misconception\_\#6 Heavy:**

* "Let me show you the order: count shaded parts \- that's your top number. Count total parts \- that's your bottom number. So 3 shaded out of 4 total is 3/4." \[Visual: Step-by-step labeling\] \[Modeling\]

### **7.6 Visual Requirements**

**Heavy Level:** FULL modeling (complete demonstration)

---

## **SECTION 8: Post-Modeling Language**

### **8.1 Critical Rule**

Use ONLY approved acknowledgments after \[Modeling\] tag. Acknowledge assisted success, never independent success.

### **8.2 Appropriate Acknowledgments**

**Use These (acknowledges help):**

* "There we go."  
* "See how that works?"  
* "It's okay if this is tricky."  
* "You're getting it now."  
* "Now you understand."  
* "That makes sense now, right?"  
* "That's it \- now you've got it."  
* "Good \- you understand now."  
* "Now you see the pattern."

### **8.3 Never Use After Modeling**

* "Perfect\!" (they didn't do it alone)  
* "You figured it out\!" (guide showed them)  
* "Great job\!" (too independent)  
* "Excellent work\!" (overpraises assisted work)

### **8.4 Post-Modeling Transitions**

**Move forward assuming understanding:**

* "Let's try another one."  
* "Now let's continue."  
* "Ready for the next?"  
* "Let's keep going."

---

## **SECTION 9: Error Signal Strategy**

### **9.1 Usage Guidelines**

**Use error signals strategically (40-50% of Light remediations)**

### **9.2 When to Use Error Signals**

* Beginning of module (establish pattern)  
* After successes (clear change signal)  
* When student might think they're right

### **9.3 When to Skip Error Signals**

* Error is obvious  
* Would cause repetition  
* Mid-module routine corrections  
* Guidance itself implies error

---

## **SECTION 10: Avoiding Condescending Language**

### **10.1 Instead of Excessive "Let's..."**

**Use:**

* Direct guidance  
* "Try..."  
* Simple imperative statements

**Save "Let's" for:** Genuine collaboration (Medium/Heavy)

### **10.2 Language Distribution Principles**

**Light:** Brief, minimal warmth (students see this most)  
 **Medium:** Acknowledge struggle, collaborative, specific hint  
 **Heavy:** Full emotional support, complete worked example

---

## **SECTION 11: Practice Phase Variety Strategies**

### **11.1 Five Variation Strategies**

**Purpose:** Prevent repetition across multiple practice problems

| Strategy | Focus | Example Language |
| ----- | ----- | ----- |
| Visual Focus | Direct attention to visual | "Look at the leftmost bar" |
| Conceptual Focus | Reinforce concept | "Remember what denominator means" |
| Strategic Focus | Suggest approach | "Try counting out loud" |
| Comparative Focus | Use comparison | "How is this different from the last one?" |
| Metacognitive Focus | Self-checking | "What would help you check your answer?" |

### **11.2 Quick Variety Bank**

**Instead of "Check again" use:**

* "Hmm, take another look"  
* "Something's not quite right"  
* "Let me see... try once more"  
* "Count those parts again for me"

### **11.3 Example: Varying Remediation Across Practice**

**Same Error Type, Different Approaches:**

**Task 1 Error (Direct):**

* Light: "Count the shaded parts again."  
* Medium: "You counted total parts \- we need shaded parts for the numerator."  
* Heavy: \[Full modeling with visual walkthrough\]

**Task 2 Error (Visual Focus):**

* Light: "Check what the numerator represents."  
* Medium: "The top number isn't the total \- it's how many you selected."  
* Heavy: \[Different example with highlighting\]

**Task 3 Error (Strategic Focus):**

* Light: "Which parts did you interact with?"  
* Medium: "Try pointing to each shaded part as you count for the numerator."  
* Heavy: \[Physical counting strategy demonstration\]

---

## **SECTION 12: Remediation Completeness by Phase**

### **12.1 Completeness Requirements by Phase**

| Phase | Requirement | Exception |
| ----- | ----- | ----- |
| Warmup | Light minimum | Heavy if addressing key prior knowledge |
| Lesson | Full L-M-H | None |
| Exit Check | Full L-M-H | None \- it's the gateway |
| Practice | Full L-M-H | Light only for confidence builders |
| Synthesis | Light minimum | Full L-M-H for pattern discovery |
| Challenge | None | Assessment mode |

### **12.2 Remediation Depth by Module Complexity**

**REMEMBER:** Module complexity determines remediation depth

**Modules 1-3 (Simple concepts):**

* Light remediation may be sufficient  
* Don't force all three tiers if unnecessary  
* "Let's try again" might be enough  
* Simpler language appropriate  
* Basic vocabulary

**Modules 4-8 (Building complexity):**

* Full L-M-H progression more common  
* Can reference earlier module strategies  
* Vocabulary builds on previous modules  
* More sophisticated explanations appropriate

**Modules 9-12 (Complex concepts):**

* Full L-M-H progression usually needed  
* Can use advanced language and vocabulary learned in previous modules  
* Reference multiple strategies and prior knowledge  
* More nuanced conceptual explanations

**Documentation:** Use \[Pedagogical\_Override\] when reality differs from stated requirements

---

## **SECTION 13: Exit Check Special Requirements**

### **13.1 Mandatory Requirement**

Complete L-M-H for EVERY Exit Check Interaction (no exceptions)

### **13.2 Exit Check Interaction Template**

**Question:** \[Assessment question\]

**\[If correct\]:** Guide: \[Specific praise \+ readiness indicator\]

**\[Light\_Remediation \- Type\]:** "\[10-20 word redirect\]"

**\[Medium\_Remediation \- Type\]:** "\[20-30 word conceptual reminder\]"

**\[Heavy\_Remediation \- Type\] with \[Modeling\]:** "\[30-60 word full demonstration\]"

*Type \= Generic, Common\_Error\_\[Type\], or Misconception\_\#X*

---

## **SECTION 14: Critical Reminders and Quality Checklist**

### **14.1 Core Rules (Never Violate)**

* Sequential only \- never offer alternatives  
* One error path per problem, not multiple options  
* Medium MUST have \[Visual\] line  
* Heavy MUST have \[Modeling\] tag  
* After \[Modeling\], acknowledge assisted success only  
* System takes over after Heavy remediation

### **14.2 Variety Requirements**

**Per Module (assuming 8-12 problems):**

**Light Remediation:**

* Minimum 8 different patterns (students see Light most often)  
* Alternate between with/without error signals (40-50% with signal)  
* NEVER repeat same phrase within 3 interactions

**Medium Remediation:**

* 4-5 different approaches  
* Rotate through approved starters  
* Use "Remember" sparingly (1-2 times per module max)

**Heavy Remediation:**

* 2-3 variations sufficient (only 5% of students reach Heavy)  
* Mix opening language for variety

**Overall Module Limits:**

* "Remember" maximum 2-3 times per entire module (Medium/Heavy only)  
* Never repeat exact phrase within 3 problems  
* Mix collaborative and direct language

### **14.3 Visual Scaffolding by Level**

* **Light:** NO visuals (words only)  
* **Medium:** SUBTLE visuals (highlights, dotted lines, numbers)  
* **Heavy:** FULL modeling (complete demonstration)

### **14.4 Structure Quality Checklist**

**Within Each Problem:**

* Different language at each level  
* No repeated phrases ("Remember", "Try again")  
* Progressive acknowledgment of struggle

**Within Each Module:**

* Rotate through error signals  
* Vary guidance patterns  
* Maximum 2-3 "Remember" uses total  
* No exact phrase within 3 problems

### **14.5 Word Count Verification**

* Light \= 10-20 words  
* Medium \= 20-30 words (faster ok if clear)  
* Heavy \= 30-60 words (faster ok if complete)  
* Each level provides meaningfully more support than previous

### **14.6 Content Quality**

* Light redirects without revealing answer  
* Medium provides conceptual reminder  
* Heavy includes full modeling  
* Language varies across tasks  
* Type labels accurate (Generic, Common\_Error, or Misconception)

### **14.7 Voice Quality**

* Warm and supportive throughout  
* No frustration or impatience  
* Acknowledges student thinking  
* Builds confidence even in correction

### **14.8 Technical Notes**

* The \[Implicit\] line in Heavy template is for writer reference only  
* Don't include in final script

---

## **SECTION 15: Remediation Red Flags**

### **15.1 Fix These Issues Immediately**

* Exact same wording repeated  
* Jump from Light to Heavy (skipping Medium)  
* Heavy without \[Modeling\] tag  
* Using misconception tags when confidence is LOW  
* Using misconception tags for procedural errors  
* Answer given away in Light/Medium  
* Cold or dismissive tone  
* Over 60 words in Heavy  
* Missing type specification (Generic, Common\_Error, or Misconception)

---

## **SECTION 16: Common Error Patterns by Task Type**

### **16.1 Partitioning/Division Tasks**

**Common Error: Counting Error**

* **Pattern:** Wrong number of parts created  
* **Detection:** Count parts ≠ requested parts, BUT parts are equal  
* **Confidence:** HIGH  
* **Add remediation:** Yes

**Common Error: Incomplete Action**

* **Pattern:** Started dividing but stopped early  
* **Detection:** Partial divisions visible, fewer than requested  
* **Confidence:** MEDIUM  
* **Add remediation:** Maybe (if detectable)

**Misconception \#1: Unequal Parts**

* **Pattern:** Correct number of parts, but unequal sizes  
* **Detection:** Count \= requested, but parts visibly different  
* **Confidence:** HIGH  
* **Add remediation:** Yes

### **16.2 Shading Tasks**

**Common Error: Counting Error**

* **Pattern:** Wrong number of parts shaded (but not denominator)  
* **Detection:** Shaded count ≠ numerator AND ≠ denominator  
* **Confidence:** HIGH  
* **Add remediation:** Yes

**Common Error: Over-Extension**

* **Pattern:** Shaded too many parts (more than numerator)  
* **Detection:** Shaded count \> numerator  
* **Confidence:** HIGH  
* **Add remediation:** Yes

**Common Error: Under-Extension**

* **Pattern:** Shaded too few parts (less than numerator)  
* **Detection:** Shaded count \< numerator AND ≠ any other number  
* **Confidence:** HIGH  
* **Add remediation:** Yes

**Misconception \#6: Reversal**

* **Pattern:** Shades denominator instead of numerator  
* **Detection:** Shaded count \= denominator (systematic pattern)  
* **Confidence:** HIGH  
* **Add remediation:** Yes

### **16.3 Number Line Tasks**

**Common Error: Off-by-One**

* **Pattern:** Placed one space too far or too close  
* **Detection:** Position \= correct ± 1 interval  
* **Confidence:** HIGH  
* **Add remediation:** Yes

**Misconception \#4: Improper Spacing**

* **Pattern:** Spacing units unevenly (systematic)  
* **Detection:** Visual analysis shows inconsistent intervals  
* **Confidence:** MEDIUM-HIGH  
* **Add remediation:** Yes if clearly systematic

**Misconception \#5: Counting Tick Marks**

* **Pattern:** Counts ticks instead of spaces  
* **Detection:** Position suggests tick-counting logic  
* **Confidence:** MEDIUM-HIGH  
* **Add remediation:** Yes if pattern is clear

### **16.4 Comparison/Selection Tasks**

**Common Error: Reversed Selection**

* **Pattern:** Selected "smallest" when asked for "biggest"  
* **Detection:** Misread instruction direction  
* **Confidence:** MEDIUM (hard to distinguish from misconception)  
* **Add remediation:** Maybe

**Misconception \#8: Size Confusion**

* **Pattern:** Believes larger denominator \= larger fraction  
* **Detection:** Systematic selection of wrong size  
* **Confidence:** HIGH when pattern is clear  
* **Add remediation:** Yes

### **16.5 Quick Reference: Error Type Detection**

| Task Type | Common Error | Misconception | Detection Confidence |
| ----- | ----- | ----- | ----- |
| Partition into X parts | Counting Error | \#1 Unequal Parts | HIGH / HIGH |
| Shade X parts | Counting Error | \#6 Reversal | HIGH / HIGH |
| Number Line Placement | Off-by-One | \#4 Spacing, \#5 Ticks | HIGH / MEDIUM-HIGH |
| Compare Fractions | Reversed Selection | \#8 Size Confusion | MEDIUM / HIGH |

---

## **SECTION 17: Full Misconceptions Reference**

### **17.1 Complete Misconceptions List**

| \# | Misconception | Full Description | Detection Confidence Required |
| ----- | ----- | ----- | ----- |
| 1 | Equal vs. Unequal Parts | Believing parts can be different sizes and still count as equal fractions | 90%+ |
| 2 | Misidentifying the Whole | Losing track of what the "1" is; comparing parts of different wholes | 90%+ |
| 3 | Numerator/Denominator as Independent | Seeing numerator and denominator as unrelated values or labels | 90%+ |
| 4 | Improper Spacing on Number Line | Spacing units unevenly or inconsistently | 85%+ (visual) |
| 5 | Counting Tick Marks Instead of Spaces | Thinking each tick is a part, rather than the spaces between | 85%+ (pattern) |
| 6 | Reversing Numerator and Denominator | Swapping top/bottom when labeling or reading fractions | 90%+ |
| 7 | Difficulty Recognizing Equivalence | Not seeing that 2/4 \= 1/2, even when visually aligned | 90%+ |
| 8 | Errors Comparing Unlike Fractions | Believing larger denominator \= larger fraction | 90%+ |
| 9 | Fractions Only Exist in Shapes | Not recognizing fractions on number lines or symbols | 90%+ |
| 10 | Overgeneralizing Rules | Applying rules like "larger number \= bigger piece" across contexts | 85%+ |

### **17.2 Quick Error-to-Type Map**

| If Student... | Classification | Diagnostic | Remediation Type |
| ----- | ----- | ----- | ----- |
| Makes 5 equal parts (asked for 4\) | Common Error \- Counting | Simple counting mistake | Common\_Error\_Counting |
| Makes 4 unequal parts | Misconception \#1 | Doesn't understand "equal" | Misconception\_\#1 |
| Shades 4 parts (asked for 3/4) | Misconception \#6 | Reversal pattern | Misconception\_\#6 |
| Shades 2 parts (asked for 3/4) | Common Error \- Counting | Miscounted | Common\_Error\_Counting |
| Off by one space on number line | Common Error \- Off-by-One | Position error | Common\_Error\_Off\_By\_One |
| Spaces number line unevenly | Misconception \#4 | Doesn't understand equal spacing | Misconception\_\#4 |
| Selects biggest visual piece | Misconception \#8 | Size confusion | Misconception\_\#8 |
| Random/unclear error | Generic | Ambiguous cause | Generic |

### **17.3 Diagnostic Flow**

```
Error Occurs
     ↓
Check error type in map above
     ↓
Determine confidence level (90%+ for misconception)
     ↓
Select appropriate remediation type:
  - 90%+ confidence + conceptual → Misconception
  - HIGH confidence + procedural → Common Error
  - Ambiguous/unclear → Generic
     ↓
Apply targeted remediation L-M-H
     ↓
If persists → Re-evaluate type selection
```

### **17.4 Most Common by Module**

**Modules 1-2:** \#1 (Unequal parts), \#2 (Wrong whole)  
 **Modules 3-4:** \#3 (Independent values), \#6 (Reversal)  
 **Modules 5-6:** \#4 (Improper spacing), \#5 (Tick marks)  
 **Modules 7-8:** \#7 (Equivalence), \#8 (Size confusion)  
 **Modules 9-10:** \#9 (Limited representation), \#10 (Overgeneralization)

### **17.5 Tag Format Examples**

**Generic Type:**

```
[Light_Remediation] [Meta_Remediation]
[Medium_Remediation] [Meta_Remediation]
[Heavy_Remediation] [Meta_Remediation] [Modeling]
```

**Common Error Type:**

```
[Light_Remediation - Common_Error_Counting] [Meta_Remediation]
[Medium_Remediation - Common_Error_Counting] [Meta_Remediation]
[Heavy_Remediation - Common_Error_Counting] [Meta_Remediation] [Modeling]
```

**Misconception Type:**

```
[Light_Remediation - Misconception_#1] [Meta_Remediation]
[Medium_Remediation - Misconception_#1] [Meta_Remediation]
[Heavy_Remediation - Misconception_#1] [Meta_Remediation] [Modeling]
```

---

## **END OF REFERENCE DOCUMENT**

**Version:** 2.0  
 **Document Type:** Authoritative reference for script writers  
 **Major Changes from v1.0:**

* Introduced three-type remediation architecture (not parallel tracks)  
* Clarified: One sequence (L→M→H), multiple options at each level  
* Distinguished Generic, Common Error, and Misconception types  
* Emphasized detection confidence requirements  
* Clarified procedural vs. conceptual error distinction  
* Added comprehensive error pattern library by task type

**Maintenance:** Update version number and date when making changes  
 **Questions:** Refer to specific section numbers for clarification

