# Visual Guide: Animation Types & Scaffolding Reference

## PURPOSE
This guide defines the **available visual animations and scaffolding types** that can be used in interactive fraction exercises. When the Remediation System document references "see Visual Guide," consult this document for appropriate animation types based on the student's learning stage and error type.

## CORE INSTRUCTION
You are creating interactive visual fraction exercises using rectangle bars, shapes, and grid arrays. Match the interaction type and scaffolding level to the student's learning stage.

---

## INTERACTION TYPE DECISION TREE

### Step 1: Identify the Learning Goal
Choose the task category from this list:
- Divide/partition shapes into equal parts
- Shade portions of shapes
- Count and identify parts (equal/unequal)
- Compare fraction sizes
- Match fractions to notation (a/b)
- Order fractions
- Identify equivalent fractions

### Step 2: Determine Interaction Method

**Use "ON THE VISUAL" interaction when:**
- Students need hands-on manipulation
- Task involves: dividing, shading, clicking specific shapes, ordering by clicking
- Early learning stages (Modules 1-4)
- Building conceptual understanding

**Use "MULTIPLE CHOICE" interaction when:**
- Students are practicing recognition
- Task involves: selecting quantities, counting, yes/no decisions
- Assessment or quick checks
- Reinforcing learned concepts

---

## SCAFFOLDING LEVELS (Choose Based on Module)

### Level 1: Visual Scaffold (Modules 1-3)
**When to use:** Introducing new concepts, early fraction work

**Animation supports:**
```
- Sequential division strategy: Show how to divide step-by-step
- One-piece outline: Highlight the first piece to shade
- Progressive highlighting: Number each piece as it's counted (1...2...3)
- Size comparison overlay: Overlay one piece on top of another
```

### Level 2: Medium Remediation (Modules 3-5)
**When to use:** Students understand basics but need guidance

**Animation supports:**
```
- Pieces outline one-by-one with counter
- Equal parts glow together
- Unequal parts show largest/smallest pulsing
- Progressive fraction counter (e.g., "1/5 → 2/5 → 3/5")
```

### Level 3: Minimal Support (Modules 6+)
**When to use:** Students work independently

**Animation supports:**
```
- Minimal or no animation
- Subtle highlighting on hover only
- Immediate feedback after selection
```

---

## PROMPT TEMPLATES BY TASK TYPE

### Template 1: Division & Partitioning Tasks
```
TASK: [Divide shape into X equal parts / Shade X parts]
INTERACTION: On the Visual
MODULE LEVEL: [1-2 / 3-4 / 5+]

VISUAL DESIGN:
- Show [rectangle bar / circular shape / grid array]
- Size: [specify dimensions appropriate for age group]
- Colors: [use high contrast, colorblind-friendly palette]

SCAFFOLDING (if Module 1-2):
- Animation: Sequential division strategy
- Show: Dotted lines appearing one-by-one to guide partitioning
- Counter: Display "Part 1 of X, Part 2 of X..." as divisions appear

INTERACTION:
- Student action: [Click to divide / Drag to create lines / Tap segments to shade]
- Feedback: [Correct divisions turn green / Incorrect shake and reset]
```

### Template 2: Comparison Tasks
```
TASK: [Compare shaded parts / Identify bigger/smaller pieces]
INTERACTION: On the Visual
MODULE LEVEL: [1-2 / 3-4 / 5+]

VISUAL DESIGN:
- Show 2-4 shapes side-by-side
- Each shape: [same total size but different partitions]
- Shaded portions: [use consistent shading color across shapes]

SCAFFOLDING (if Module 1-4):
- Animation: Outline comparison overlay
- Show: Extract shaded piece from Shape A, overlay onto Shape B
- Highlight: Which piece is larger with pulsing border
- Optional: Show size difference with visual gap measurement

INTERACTION:
- Student action: Click the shape with [larger/smaller/equal] shaded portion
- Feedback: Selected shape highlights with checkmark or X
```

### Template 3: Fraction Notation Matching
```
TASK: [Match visual to fraction / Click shape showing a/b]
INTERACTION: [On the Visual / Multiple Choice]
MODULE LEVEL: [typically 4+]

VISUAL DESIGN:
- Show shape with [X out of Y parts shaded]
- Display fraction notation: a/b

SCAFFOLDING (if needed):
- Animation: Progressive counter
- Show: "1/5... 2/5... 3/5" as pieces highlight sequentially
- Emphasize: Final fraction matches shaded amount

INTERACTION METHOD A (On Visual):
- Student clicks the shape that matches given fraction
- Multiple shapes shown with different shaded amounts

INTERACTION METHOD B (Multiple Choice):
- Shape is shown, student selects matching fraction from 3-4 options
- Options include common misconceptions (e.g., reversed numerator/denominator)
```

### Template 4: Equivalence Tasks
```
TASK: [Identify equivalent fractions / Shade to make equivalent]
INTERACTION: On the Visual
MODULE LEVEL: [typically 5+]

VISUAL DESIGN:
- Show 2+ shapes with different partitions (e.g., halves vs fourths)
- Same total size for all shapes
- Some shapes pre-shaded

SCAFFOLDING (if needed):
- Animation: None typically, or subtle alignment guides
- Show: Overlay grids align to show equivalence
- Optional: Number line below showing both fractions at same point

INTERACTION:
- Identify task: Click shapes that show equivalent amounts
- Shading task: Shade additional pieces to match given fraction
- Feedback: Equivalent shapes highlight together with connecting line
```

### Template 5: Ordering Tasks
```
TASK: [Order shapes from smallest to largest / Click in sequence]
INTERACTION: On the Visual
MODULE LEVEL: [typically 4+]

VISUAL DESIGN:
- Show 3-5 shapes in random arrangement
- Each with different shaded amounts
- Numbered placeholders below (1st, 2nd, 3rd...)

SCAFFOLDING (if Module 4-5):
- Animation: Outline comparison overlay for selected shapes
- Show: Extract and align shaded portions for comparison
- Counter: "You've placed X of Y shapes"

INTERACTION:
- Student clicks shapes in order
- Each clicked shape moves to next numbered position
- Can undo/rearrange before submitting
- Feedback: All correct = green checkmarks, any incorrect = highlighting

---

## EXAMPLE PROMPT IN USE

**Input Context:**
- Task: "Shade 3 parts of a rectangle divided into 5 equal pieces"
- Student Level: Module 2 (early learning)
- Interaction: On the Visual

**Generated Instruction to AI Image/Animation Creator:**

```
CREATE INTERACTIVE FRACTION EXERCISE:

Visual: Rectangle bar, divided into 5 equal vertical sections

Initial State:
- 5 sections outlined with black borders
- All sections white/unshaded
- Sections numbered 1-5 in bottom corner

Scaffolding Animation (on load):
- Each section outline highlights sequentially
- Counter appears above: "1 of 5 parts... 2 of 5 parts..." through "5 of 5 parts"

Student Interaction:
- Click any section to toggle shading (blue fill)
- Maximum 3 sections can be shaded
- Each shaded section shows checkmark

Feedback:
- If exactly 3 sections shaded: All sections get green border, success message
- If <3 or >3: Shake animation, counter shows "You've shaded X of 3"
- Reset button appears if incorrect

Accessibility:
- Alt text: "Rectangle divided into 5 equal parts. Shade 3 parts."
- Keyboard: Tab between sections, Space to toggle shade
```

---

## QUICK REFERENCE CHECKLIST

Before generating any visual interaction, confirm:
- [ ] Task type identified from learning goal
- [ ] Interaction method chosen (On Visual vs Multiple Choice)
- [ ] Module level determined (affects scaffolding)
- [ ] Appropriate animation/scaffold selected
- [ ] Visual design follows specifications
- [ ] Feedback mechanisms defined
- [ ] Accessibility features included
- [ ] Clear success/failure states

---

## NOTES FOR AI GENERATORS

**Common Pitfalls to Avoid:**
- Don't over-animate for advanced modules (keeps scaffolding at basic level)
- Don't use red/green only for feedback (add patterns/icons)
- Don't make touch targets too small (minimum 44px)
- Don't progress counter too fast (students need processing time)
- Don't show all scaffolding at once (sequential is clearer)

**Best Practices:**
- Match visual complexity to student ability
- Use consistent colors across similar task types
- Provide undo options for hands-on interactions
- Celebrate success with positive visual feedback
- Make incorrect answers learning moments (show why, not just that it's wrong)