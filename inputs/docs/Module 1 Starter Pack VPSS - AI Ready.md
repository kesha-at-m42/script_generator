## **MODULE 1: WHAT MAKES A FRACTION? — PATH C (VPSS)**

**Version:** December 2025  
 **Purpose:** Self-contained script generation reference for Console Claude  
 **Status:** This section contains everything needed for script generation. No other Starter Pack sections required.

yaml

```
---
module_id: M01
path: C
version: 2.0
last_updated: 2025-12-02
fractions_required: ["1/2", "1/3", "1/4", "1/6", "1/8"]
misconception_ids: ["M1.1", "M1.2"]
tools: ["Grid Arrays", "Hexagons", "Partition Drawing Tool"]
phases: ["Warmup", "Lesson", "Exit Check", "Practice", "Synthesis"]
---
```

---

## **1.0 LEARNING GOALS (Verbatim — Script Must Achieve These)**

**L1:** "Partition shapes into equal areas (2,3,4,6,8) and name parts; recognize that equal-size parts can be named with fractions."

**L2:** "Express each equal part as a unit fraction of the whole using fraction notation; partition into halves, thirds, fourths, sixths, eighths."

**Module Goal (Student-Facing):**  
 "For our fraction work, you'll learn what makes parts equal by splitting shapes into equal parts of a whole."

**Exit Check Tests:** Can identify equal partitions AND match simple fraction names to visuals (e.g., "which shows thirds?")

---

## **1.1 THE ONE THING**

Students learn that **fractions require EQUAL parts and name them**, and they practice creating and recognizing equal partitions of shapes (2, 3, 4, 6, 8 parts).

**Critical Misconception:** Believing parts can be different sizes and still count as equal fractions (\#1)

**Success Indicator:** Student consistently creates/identifies equal partitions and rejects unequal ones

**Biggest Risk:** Accepting "close enough" instead of true equality; moving to fraction notation too quickly

---

## **1.2 SCOPE BOUNDARIES**

### **✅ MUST TEACH**

* Understanding that shapes must be divided into **EQUAL parts** for fractions  
* Partitioning shapes into 2, 3, 4, 6, 8 equal parts  
* Recognizing when parts are equal vs unequal  
* Understanding "the whole" as what we're dividing  
* Unit fraction notation (1/b) introduced AFTER visual/vocabulary grounding

### **❌ MUST NOT INCLUDE**

* Numerator/denominator terminology (Module 2\)  
* Comparing fraction sizes (Module 10+)  
* Adding fractions (Unit 6\)  
* Equivalent fractions (Module 8\)  
* Number lines (Module 4\)  
* Circles (Module 2 — hexagons complete Module 1 shape progression)  
* Comparing parts from different-sized wholes (Same Whole Principle)

⚠️ SAME WHOLE PRINCIPLE All visual comparisons must use identical shapes and sizes. Never compare fractions across different-sized wholes. If showing 1/4 and 1/2, both must be on identically-sized shapes. This prevents the misconception that fraction size is absolute rather than relative to the whole.

---

## **1.3 VOCABULARY ARCHITECTURE**

### **Vocabulary Staging by Phase**

| Phase | Terms | Introduction Approach |
| ----- | ----- | ----- |
| **Warm-Up** | equal, parts | Use naturally — "Are these pieces equal?" No formal introduction |
| **Lesson Section 1** | "whole" | First activity: "This entire shape — all of it together — is our WHOLE" |
|  | "partition" | After first partition action: "When we split something into equal pieces, we call that PARTITIONING" |
|  | halves, thirds, fourths, sixths, eighths | As students create each type: "You shaded one of two equal parts: that's one HALF" |
|  | "equal parts" | After multiple partition experiences |
| **Lesson Section 2** | "fraction" | With notation bridge: "These equal parts can be named with FRACTIONS, or numbers that show parts of a whole" |
| **Practice** | (All terms) | Use in question contexts: "Which shows fourths?" "Find the shape that’s been divided into thirds" |
| **Synthesis** | (All terms) | Expect natural student use in reflection |

### **Terms to AVOID (Save for Later Modules)**

* numerator, denominator (Module 2\)  
* unit fraction (Module 2\)  
* equivalent (Module 8\)  
* greater than, less than for fractions (Module 10\)  
* improper fraction, mixed number (Module 6-7)

### STRATEGY LANGUAGE REQUIREMENTS

For complex partitions (fourths, sixths, eighths), the Guide MUST provide explicit strategy language BEFORE the student attempts the partition. This is non-negotiable.

**Required Strategy Scripts:**

**Fourths:**

"Here's a strategy to make four equal parts: first split the whole shape in half, then split each half in half again." \[Visual demonstration accompanies this\]

**Sixths:**

"Here's the strategy I use: First split the bar in half. Then split each half into three equal parts. That gives you six equal sections." \[Visual demonstration accompanies this\]

**Eighths:**

"Remember how we made four parts? We can use the same process to make eighths. First click once in the middle. Then click in the middle of each half. Then click in the middle of each of those four parts." \[Visual demonstration accompanies this\]

**Why This Matters:** Singapore script analysis shows explicit strategy scaffolding significantly reduces remediation needs for complex partitions. Students should not be expected to discover multi-step partition strategies independently.  
---

## **1.4 MISCONCEPTIONS — FULL DETAIL**

### **1.4.1: Unequal Parts (PRIMARY)**

**Trigger Behavior:**  
 Student accepts or creates partitions where parts are visibly different sizes; suggests that "sort of equal" is acceptable for fractions

**Why It Happens:**  
 Informal everyday language ("I'll split this") doesn't require precision; visual estimation without measurement tools; lack of understanding that fractions are based on exact equality

**Visual Cue:**  
 Use pattern tiles to overlay and directly compare part sizes; show grid arrays where equal parts fill identical grid units

**Prevention Strategy:**  
 Start with grid rectangles where equality is built-in through counting; use pattern tiles that physically match when overlaid; emphasize visual comparison and matching throughout

---

### **1.4.2: Misidentifying the Whole**

**Trigger Behavior:**  
 Student loses track of what constitutes "one whole"; compares parts from different-sized wholes; treats part as whole or whole as part

**Why It Happens:**  
 No clear boundary established for "the whole"; attention shifts to parts and loses sight of complete object; comparing across different contexts without resetting "whole" reference

**Visual Cue:**  
 Highlight the entire shape before partitioning; show complete grid array with boundary clearly marked; use pattern tiles that show complete hexagon or rectangle as "one whole"

**Prevention Strategy:**  
 Always establish "this is our whole" before partitioning; use consistent shape sizes; keep whole shape visible even after partitioning; build vocabulary around "the whole shape"

---

## **1.5 TOOL SPECIFICATIONS**

### **1.5.1Grid Arrays (Primary Tool)**

| Aspect | Specification |
| ----- | ----- |
| **Available Sizes** | 1x2, 1x3, 1x4, 2x2, 2x3, 3x2, 2x4, 4x2, 1x6, 1x8 |
| **Interaction** | Click to place partition lines along symmetry axes; click to shade sections |
| **Feedback** | Partition lines appear; shaded sections highlight; parts show as selected |
| **Validation** | System counts grid units per section; confirms equality when all sections have same count; system tracks shaded section count |
| **Error Feedback** | Unequal parts trigger visual size mismatch highlight \+ "These parts have different sizes. Try again." |
| **Purpose** | Extend partitioning to multi-sided shapes while maintaining verification through straight edges; substantial practice builds foundation for circles in Module 2 |
| **Shading Purpose** | After partitioning, students shade sections to show "1 of 3 equal parts" \= 1/3, etc. Guide dialogue connects shading to fraction naming. |

### **1.5.2 Hexagons (Pattern Block Shape)**

| Aspect | Specification |
| ----- | ----- |
| **Available Partitions** | 2, 3, 6 divisions (natural hexagon symmetry) |
| **Interaction** | Click to place partition lines along symmetry axes; click to shade sections |
| **Validation** | Visual symmetry check; straight edges make equality verification clear; system tracks shaded section count |
| **Error Feedback** | Asymmetric partition shows mismatch \+ "These sections aren't equal. Look at the symmetry." |
| **Purpose** | Extend partitioning to multi-sided shapes while maintaining verification through straight edges |
| **Shading Purpose** | After partitioning, students shade sections to show "1 of 3 equal parts" \= 1/3, etc. Guide dialogue connects shading to fraction naming. |

### **1.5.3 Partition/Eraser Tool**

| Aspect | Specification |
| ----- | ----- |
| **Interaction** | Click/drag to draw partition lines; hover over line \+ click to erase |
| **Validation** | Lines snap to create equal divisions when close to valid partition |
| **Purpose** | Allows experimentation; reduces anxiety about mistakes |
| **CRITICAL** | Must demonstrate eraser functionality BEFORE first student partition attempt |

### **Interaction Constraints (All Tools)**

* NO verbal/spoken student responses — Guide speaks, student acts  
* NO keyboard/text input — all responses via click/tap/drag  
* NO open-ended questions requiring typed answers — use selection or action tasks  
* Questions in Guide speech must be either rhetorical (Guide answers) or answered through on-screen action

---

**PHASE SPECIFICATIONS**  
---

## **1.7 LESSON (10-14 minutes)**

### **Core Purpose**

Develop understanding that fractions require equal parts; learn to create equal partitions; name them with words, then with mathematical notation.

### **Pedagogical Flow**

Module 1 teaches partitioning, shading, and naming as an integrated progression. The lesson moves through three sections:

1. Grid mastery with fraction words  
2. Notation introduction  
3. Hexagon extension with full naming

This sequence preserves immediate connection (partition→shade) while building from concrete spatial work to abstract notation.

---

### **LESSON INTERACTION BUDGET**

| Section | Interactions | Time |
| :---- | :---- | :---- |
| Section 1: Grid Mastery with Fraction Words | 10 | 7-8 min |
| Section 2: Notation Bridge | 2 | 2-3 min |
| Section 3: Hexagon Extension | 4-6 | 4-5 min |
| **TOTAL** | **16-18** | **13-16 min** |

**Maximum:** 20 interactions (flag if exceeding)

**Why This Count:** Each fraction type requires TWO student interactions—partition (with L-M-H remediation) followed by shade (with L-M-H remediation). This mirrors validated Singapore Path structure. Hexagon section adds shape transfer not present in Singapore.

---

### **SCRIPT ECONOMY PRINCIPLE**

**Each fraction type requires TWO interactions: (1) partition prompt with L-M-H remediation, (2) shade prompt with L-M-H remediation.** Brief naming/verification follows the shade step without a separate prompt.

**Section 1 Interaction Pattern (10 interactions):**

- Halves: Partition (full modeling) \+ Shade \= 2 interactions  
- Fourths: Partition (guided practice) \+ Shade \= 2 interactions  
- Thirds: Partition (independent) \+ Shade \= 2 interactions  
- Sixths: Partition (strategy scaffold) \+ Shade \= 2 interactions  
- Eighths: Partition (doubling pattern) \+ Shade \= 2 interactions

**Why separate partition and shade:**

1. **Cognitive chunking** — One action at a time reduces load  
2. **Targeted remediation** — Partition errors vs. shade errors need different support  
3. **Clear validation** — Each action gets explicit success feedback  
4. **Natural pacing** — Pause between creation and selection

**"All five fraction types appear" ≠ "All five get equal explanation time."** Halves gets full modeling and vocabulary; eighths can have briefer setup because it extends the established doubling pattern. But all five get the two-interaction structure.

---

## **1.7.1 LESSON SECTION 1: GRID MASTERY WITH FRACTION WORDS**

**Interaction 1.1: Establishing the Whole \+ Tool Orientation**

- **Visual:** Complete fraction bar appears  
- **Guide:** "This bar is our WHOLE. It's like one chocolate bar. When we divide the whole into parts, each part is a piece of THIS whole."  
- **Tool Demo:** "If you make a cut you don't like, you can hover over the line and click to erase it. Watch\!"  
- **Prompt:** Student practices eraser on pre-placed line  
- **Vocabulary:** Introduce "whole"  
- **Remediation:** Light only (tool practice)

**Interaction 1.2: Partition into Halves**

- **Prompt:** "Click once in the middle to split the bar into 2 equal parts."  
- **On Correct:** "You made two parts. Let's check—are they equal?"  
- **Verification Prompt**: "Count the grid units. Are all parts equal?" \[click\_choice: yes/no\]  
- **On Verify:** "You verified it—all parts have the same number of grid units. That's two halves."

**Interaction 1.3: Shade One Half**

- **Visual:** Bar partitioned into halves from 1.2  
- **Guide:** "Now, please click one of those parts to shade it."  
- **Prompt:** "Click on 1 of the 2 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus)  
- **On Correct:** "Yes. You selected one part out of two equal parts."  
- **Vocabulary:** After shading, introduce "partition": "When mathematicians divide something into equal parts like you just did, they call it PARTITIONING."

**Interaction 1.4: Partition into Fourths**

- **Visual:** New fraction bar  
- **Guide:** "Here's one way we can split the bar into four equal parts: first split the bar in half, then split each half in half again." \[DEMONSTRATE visually\]  
- **Cut Orientation Note:** "Notice I can cut across the bar like this \[horizontal demo\] OR down like this \[vertical demo\]. As long as each piece is the same size, we’ve created equal parts."  
- **Guide:** "Your turn. Try clicking once in the middle, then click once in each half."  
- **Prompt:** "Please click 3 times to split the bar into 4 equal parts."  
- **Remediation:** Full L-M-H (partition focus, strategy reminder)  
- **On Correct:** "Right. Four equal parts."

**Tool Note for Script Writers:** Students may use vertical cuts, horizontal cuts, or a mix. All are valid if they produce equal parts. Remediation should NOT correct cut orientation—only address whether parts are equal.

**Interaction 1.5: Shade One Fourth**

- **Visual:** Bar partitioned into fourths from 1.4  
- **Guide:** "Next, try shading just one part."  
- **Prompt:** "You can click on one of the 4 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus)  
- **On Correct:** "Good. One out of four equal parts."  
- **Vocabulary:** "When all parts are the same size, we call them EQUAL PARTS."

**⚡ NOTATION INTRODUCTION (embedded after 1.5, before 1.6)**

- **Guide:** "Take a look at this symbol with me: 1/4. That's how we write 'one out of four equal parts.' The bottom number tells us how many equal parts we made. The top number tells us how many parts we selected."  
- **No prompt** — observation only

**Interaction 1.6: Partition into Thirds**

- **Visual:** New fraction bar  
- **Guide:** "Can you partition this bar into three equal parts?"  
- **Prompt:** "Click 2 times to partition this bar into 3 equal parts."  
- **Remediation:** Full L-M-H (partition focus)  
- **On Correct:** "Right. You partitioned the bar into three equal parts."

**Interaction 1.7: Shade One Third**

- **Visual:** Bar partitioned into thirds from 1.6  
- **Guide:** "Can you shade just one part?"  
- **Prompt:** "Click on 1 of the 3 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus)  
- **On Correct:** "Right. That's one out of three equal parts. We write one of three equal parts as 1/3."  
- **Pattern callout:** "Notice the pattern? The bottom number always shows our total number of equal parts."

**Interaction 1.8: Partition into Sixths**

- **Visual:** New fraction bar  
- **Guide:** "Let's try a more advanced problem. Can you partition this bar into six equal parts?"  
- **Strategy (REQUIRED):** "Here's a strategy to help us: First split the bar in half. Then split each half into three equal parts. That gives you six equal sections." \[DEMONSTRATE visually\]  
- **Guide:** "Give it a try. Try clicking once in the middle, then click twice in each half to make thirds."  
- **Prompt:** "Partition the bar into six equal parts."  
- **Remediation:** Full L-M-H (partition focus, strategy scaffold)  
- **On Correct:** "Correct\! You divided the bar into sixths. Six equal parts."

**Interaction 1.9: Shade One Sixth**

- **Visual:** Bar partitioned into sixths from 1.8  
- **Guide:** "Now shade just 1 part, please."  
- **Prompt:** "Click on 1 of the 6 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus)  
- **On Correct:** "Yes. One out of six equal parts. That's 1/6."

**Interaction 1.10: Partition into Eighths**

- **Visual:** New fraction bar  
- **Guide:** "Let's partition one more bar. This time, we’ll divide the whole bar into eight equal parts. Remember how we made four parts? We can extend the same process to make eight parts."  
- **Strategy (REQUIRED):** "First, click once in the middle. Then click in the middle of each half. Then click in the middle of each of those four parts." \[DEMONSTRATE visually\]  
- **Guide:** "Now you try. Remember the strategy we’ve practiced: first halves, then fourths, then eighths."  
- **Prompt:** "Partition the bar into eight equal parts."  
- **Remediation:** Full L-M-H (partition focus, strategy scaffold)  
- **On Correct:** "Good. Eight equal parts."

**Interaction 1.11: Shade One Eighth**

- **Visual:** Bar partitioned into eighths from 1.10  
- **Guide:** "Can you shade just one part?"  
- **Prompt:** "Click on one of the 8 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus)  
- **On Correct:** "Right: 1/8. One out of eight equal parts. You're getting this\!"  
- **Notice**: 2 parts, 4 parts, 8 parts—each time we doubled the number of parts, each piece got smaller. More parts means smaller pieces.

**⚡ SECTION 1 TRANSITION TO SECTION 2  (embedded after 1.11, no prompt)**

- **Visual:** All five fraction bars appear together (1/2, 1/4, 1/3, 1/6, 1/8)  
- **Guide:** "Look at all the fractions you've made: 1/2, 1/4, 1/3, 1/6, and 1/8. Each fraction shows one part of a whole that's been partitioned into equal parts."

### **→ SECTION 1 COMPLETE. PROCEED TO SECTION 2: NOTATION CONSOLIDATION.**

---

## **1.7.2 LESSON SECTION 2: NOTATION BRIDGE**

**Note:** Basic notation (1/4) was introduced embedded in Section 1 after fourths. Section 2 consolidates and extends notation understanding before shape transfer.

**Interaction 2.1: Notation Matching**

- **Visual:** Three partitioned/shaded bars (1/2, 1/3, 1/4) with notation symbols nearby  
- **Guide:** "You've seen how we write fractions. Let's take what we’ve learned through writing fractions and practice matching bars to symbols."  
- **Prompt:** "Match each bar to its fraction symbol." \[Drag-and-drop or selection\]  
- **Remediation:** Full L-M-H  
- **On Correct:** "Right. The bottom number shows total parts, and the top number shows shaded parts."

**Interaction 2.2: Notation Reading**

- **Visual:** Fraction symbol shown (e.g., 1/6), multiple bars to choose from  
- **Guide:** "Which bar shows this fraction?"  
- **Prompt:** "Select the bar that shows 1/6."  
- **Remediation:** Full L-M-H  
- **On Correct:** "Yes. One out of six equal parts."

### **→ SECTION 2 COMPLETE. PROCEED TO SECTION 3: HEXAGON EXTENSION.**

### **⚠️ Lesson is NOT complete without hexagon section.**

---

## **1.7.3 LESSON SECTION 3: HEXAGON EXTENSION**

**(5-7 interactions, 5-6 min)**

**Purpose:** Transfer partitioning skill to new shape; demonstrate that notation works across representations.

**Critical Tool Difference:** Hexagons (and later, circles) use RADIAL cuts—lines that start from the center and go outward to the edges. This is different from bars, where cuts can go anywhere. Students need explicit instruction on this technique.

**Interaction 3.0: Radial Cutting Introduction (No Prompt—Demonstration Only)**

- **Visual:** Hexagon with center point marked  
- **Guide:** "You've been cutting bars with lines that go straight across. For hexagons, we have to work differently to make our parts equal."  
- **Guide:** "See this dot in the center? On hexagons, our cuts start from the center and go out to the edges, like spokes on a wheel."  
- **Visual Demo:** Show a cut being drawn from center to edge  
- **Guide:** "Follow along with me. I start at the center, and draw out to the edge. That's how we'll partition hexagons."  
- **Visual Demo:** Show a second cut from center to opposite edge, creating halves  
- **Guide:** "When me make two cuts from the center that travel  to opposite edges of the shape, we make two equal parts."

**Why This Matters:** Without explicit radial cutting instruction, students will attempt to draw horizontal/vertical lines across hexagons (like bars), which won't create equal parts. This is a tool affordance, not a math concept—but it must be taught.

**Interaction 3.1: Partition Hexagon into Halves**

- **Visual:** Fresh hexagon with center point visible  
- **Guide:** "Your turn to try. Please draw a line from the center to one edge, then from the center to the opposite edge."  
- **Prompt:** "Partition the hexagon into 2 equal parts using radial cuts."  
- **Remediation:**  
  - **Light:** "Almost. Start your cut from the center dot."  
  - **Medium:** \[Visual highlights center point\] "Remember: cuts start from the center of the shape and go out to the edge."  
  - **Heavy:** \[Modeling\] "Follow along, and I’ll show you how I work it out. I click the center, then drag to the edge. Then center again, to the opposite edge. Two equal parts."  
- **On Correct:** "Right. Two equal parts, just like with the bar, but with a different cutting technique."

**Interaction 3.2: Shade One Half on Hexagon**

- **Visual:** Hexagon partitioned into halves from 3.1  
- **Guide:** "Try shading one part."  
- **Prompt:** "Click on one of the 2 parts to shade it."  
- **Remediation:** Full L-M-H (shade focus—same as bar shading)  
- **On Correct:** "Yes. One out of two equal parts—1/2. Same fraction, different shape."

**Interaction 3.3: Partition Hexagon into Thirds**

- **Visual:** New hexagon with center point visible  
- **Guide:** "Now try three equal parts. You'll need three cuts from the center, spaced evenly around the hexagon."  
- **Strategy Scaffold:** "Think of it like slicing a pie into three pieces: each cut goes from the center to the edge."  
- **Prompt:** "Partition the hexagon into 3 equal parts."  
- **Remediation:**  
  - **Light:** "Let’s check again. Remember to space your cuts evenly. Each section should be the same size."  
  - **Medium:** \[Visual shows suggested cut positions\] "Try placing cuts so each section covers two edges of the hexagon."  
  - **Heavy:** \[Modeling\] "Let me show you. Center to here, center to here, center to here. Three equal sections."  
- **On Correct:** "Three equal parts."

**Interaction 3.4: Shade One Third on Hexagon**

- **Visual:** Hexagon partitioned into thirds from 3.3  
- **Guide:** "Please shade one part."  
- **Prompt:** "Click on one of the 3 parts to shade it."  
- **Remediation:** Full L-M-H  
- **On Correct:** "1/3—one out of three equal parts. The notation works the same way."

**Interaction 3.5 (Optional): Partition Hexagon into Sixths**

- **Visual:** New hexagon  
- **Guide:** "One more. Can you make six equal parts?"  
- **Strategy:** "Remember how we made sixths on the bar? First halves, then thirds in each half."  
- **Prompt:** "Partition the hexagon into 6 equal parts."  
- **Remediation:** Full L-M-H  
- **On Correct:** "Six equal parts\!"

**Interaction 3.6 (Optional): Shade One Sixth on Hexagon**

- **Visual:** Hexagon partitioned into sixths from 3.5  
- **Guide:** "Try shading one part of the whole shape."  
- **Prompt:** "Click on one of the 6 parts to shade it."  
- **Remediation:** Full L-M-H  
- **On Correct:** "1/6. You’re seeing how we partition rectangles AND hexagons into equal parts and name them with fractions."

**⚡ CROSS-SHAPE CONNECTION (embedded after final hexagon, no prompt)**

- **Visual:** Rectangle bar showing 1/3 alongside hexagon showing 1/3  
- **Guide:** "Look: here we have different shapes, but the same fraction describes them both. 1/3 means one out of three equal parts, no matter what shape you're working with."

---

## 1.8 SCRIPT GENERATION REQUIREMENTS

### INTERACTION BUDGET (Authoritative)

| Section | Interactions | Time | Content |
| :---- | :---- | :---- | :---- |
| Section 1: Grid Mastery | 11 | 7-8 min | Tool intro \+ 5 fractions (partition+shade each) |
| Section 2: Notation Bridge | 2 | 2-3 min | Matching \+ reading |
| Section 3: Hexagon Extension | 5-7 | 5-6 min | Radial intro \+ 2-3 fractions |
| **TOTAL** | **18-20** | **14-17 min** |  |

**Maximum:** 22 interactions. Flag if exceeding.

**Why This Count:** Each fraction type requires TWO student interactions (partition \+ shade). Hexagon section adds radial cutting instruction not present in Singapore path.

---

### REQUIRED PHRASES (Must Appear in Script)

- "This entire shape is our WHOLE"  
- "When we split one whole into equal pieces, we call that PARTITIONING"  
- "For fractions to work, all pieces must be exactly the same size"  
- "These equal parts can be named with FRACTIONS"  
- All five fraction words: "halves," "thirds," "fourths," "sixths," "eighths"

---

### FORBIDDEN PHRASES (Create Misconceptions)

- ❌ "Close enough" or "about the same" (undermines equality requirement)  
- ❌ "Numerator" or "denominator" (Module 2 vocabulary)  
- ❌ "Which is bigger—halves or fourths?" (comparison is Module 10+)  
- ❌ "These fractions are equal/equivalent" (equivalence is Module 8\)  
- ❌ Any reference to circles (Module 2 content)

---

### VOCABULARY STAGING ORDER

| Term | First Appears | Context |
| :---- | :---- | :---- |
| "whole" | Interaction 1.1 | Before any partitioning |
| "partition/partitioning" | Interaction 1.3 | After first successful partition |
| "equal parts" | Interaction 1.5 | After fourths, with visual verification |
| Fraction words (halves, etc.) | Throughout Section 1 | As each partition type is created |
| "fraction" | Interaction 2.1 | When notation is introduced |

---

### STRATEGY LANGUAGE (Required for Complex Partitions)

These exact strategies must be stated AND demonstrated visually BEFORE student attempts:

**Fourths:**

"Here's a strategy to make four equal parts: first split it in half, then split each half in half again."

**Sixths:**

"Here's the strategy: First split the bar in half. Then split each half into three equal parts. That gives you six equal sections."

**Eighths:**

"Remember how we made four parts? We can extend that strategy. First halves, then fourths, then eighths."

---

### VOICE WARMTH MARKERS (Minimum 3 Required)

Include at least 3 across the Lesson:

| Marker Type | Example | Placement |
| :---- | :---- | :---- |
| Struggle normalization | "Sixths can be tricky—take your time." | Before complex partition |
| Investment signal | "You're building real understanding here." | Mid-lesson |
| Transition warmth | "New shape, same math. Let's see how you do." | Before hexagons |
| Strategy acknowledgment | "That halving strategy is really working for you." | After successful eighths |

---

### PACING REQUIREMENTS

- **Processing pauses:** 15-20 seconds after new partition type for visual analysis  
- **Wait time:** 10-15 seconds after "Are these equal?" for verification  
- **Never skip:** Immediate shading after every partition (reinforces connection)

---

### MISCONCEPTION PREVENTION (Both Required)

**M1.1 (Unequal Parts):**

- Include visual verification prompts throughout Section 1  
- Include ONE interaction showing unequal parts being rejected (place between 1.7 and 1.8)

**M1.2 (Misidentifying the Whole):**

- Establish "whole" explicitly in Interaction 1.1  
- Reference "this whole" when introducing each new bar

---

### NON-NEGOTIABLES

**ALWAYS:**

- Visual before symbolic (show equal parts before naming "fractions")  
- Verify equality explicitly (count grid units or check symmetry)  
- Establish "whole" before partitioning  
- Demonstrate eraser tool before first student partition  
- Shade immediately after every partition

**NEVER:**

- Accept unequal parts as "close enough"  
- Use numerator/denominator terminology  
- Compare fraction sizes  
- Skip visual verification  
- Introduce circles

---

## 1.9 VERIFICATION CHECKLIST

*Use this checklist AFTER generating the script to verify completeness.*

### Section 1 — Grid Mastery (11 interactions)

| \# | Interaction | Content | ☐ |
| :---- | :---- | :---- | :---- |
| 1.1 | Tool \+ Whole | Eraser demo, "whole" introduced | ☐ |
| 1.2 | Partition Halves | Full modeling, partition prompt | ☐ |
| 1.3 | Shade Halves | Shade prompt, "partition" introduced | ☐ |
| 1.4 | Partition Fourths | Strategy stated \+ demo, partition prompt | ☐ |
| 1.5 | Shade Fourths | Shade prompt, "equal parts" introduced | ☐ |
| — | Notation intro | 1/4 explained (embedded, no prompt) | ☐ |
| 1.6 | Partition Thirds | Partition prompt | ☐ |
| 1.7 | Shade Thirds | Shade prompt, pattern callout | ☐ |
| — | Unequal rejection | M1.1 prevention (between 1.7-1.8) | ☐ |
| 1.8 | Partition Sixths | Strategy stated \+ demo, partition prompt | ☐ |
| 1.9 | Shade Sixths | Shade prompt | ☐ |
| 1.10 | Partition Eighths | Strategy stated \+ demo, partition prompt | ☐ |
| 1.11 | Shade Eighths | Shade prompt | ☐ |
| — | Section 1 Synthesis | All 5 bars shown together | ☐ |

**→ SECTION 1 COMPLETE. CONTINUE TO SECTION 2\.**

---

### Section 2 — Notation Bridge (2 interactions)

| \# | Interaction | Content | ☐ |
| :---- | :---- | :---- | :---- |
| 2.1 | Notation Matching | Match bars to symbols, "fraction" introduced | ☐ |
| 2.2 | Notation Reading | Select bar for given symbol | ☐ |

**→ SECTION 2 COMPLETE. CONTINUE TO SECTION 3\.**

---

### Section 3 — Hexagon Extension (5-7 interactions)

| \# | Interaction | Content | ☐ |
| :---- | :---- | :---- | :---- |
| 3.0 | Radial Cutting Demo | Center point, "spokes" analogy, 2+ demo cuts | ☐ |
| 3.1 | Partition Hex Halves | Radial partition prompt | ☐ |
| 3.2 | Shade Hex Halves | Shade prompt | ☐ |
| 3.3 | Partition Hex Thirds | Radial partition prompt | ☐ |
| 3.4 | Shade Hex Thirds | Shade prompt | ☐ |
| 3.5 | Partition Hex Sixths | (Optional) Radial partition prompt | ☐ |
| 3.6 | Shade Hex Sixths | (Optional) Shade prompt | ☐ |
| — | Cross-shape connection | Bar \+ hexagon showing same fraction | ☐ |

**→ SECTION 3 COMPLETE. LESSON COMPLETE.**

---

### Final Counts

☐ Total interactions: \_\_\_\_\_ (Target: 18-20, Maximum: 22\) ☐ Voice warmth markers: \_\_\_\_\_ (Minimum: 3\) ☐ Required phrases: All 5 appear ☐ Forbidden phrases: None appear

---

### INCOMPLETE SCRIPT FLAGS

**If ANY of these are true, STOP and complete the script:**

- ☐ Section 2 missing or fewer than 2 interactions  
- ☐ Section 3 missing or fewer than 5 interactions  
- ☐ No radial cutting instruction before hexagon practice  
- ☐ No unequal parts rejection interaction  
- ☐ Total interaction count below 17  
- ☐ Missing any required phrase  
- ☐ Contains any forbidden phrase

---

### SUCCESS CRITERIA

**The One Thing:** Students understand that fractions require EQUAL parts, and can create/recognize equal partitions (2, 3, 4, 6, 8 parts) and name them.

**Ready for Module 2:** Student can partition shapes, verify equality, match fraction words and notation to visuals, and is prepared for numerator/denominator terminology.  
