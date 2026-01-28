# Remediation System - Verbal Scaffolding

## Overview

This reference defines error path remediation for educational interaction scripts.

**Error Path Structure:** Each interaction has one `error_path_generic` containing 3 progressive scaffolding levels:
- **Light** (error_count = 1): Brief redirect
- **Medium** (error_count = 2): Hints and guidance
- **Heavy** (error_count ≥ 3): Full solution walkthrough

**Key Principle:** You only know the student selected a wrong answer - not which specific wrong answer. Design remediation by:
1. Analyzing the interaction structure and possible answers
2. Inferring what types of errors are likely (e.g., if task involves counting intervals, errors likely involve miscounting)
3. Addressing those common error patterns through solution-focused guidance

**Example:** For "Which number line shows thirds?" with options showing fourths, fifths, and thirds, remediation should address counting equal parts, not guess which wrong option they chose.

**Verbal-Only:** All remediation uses dialogue only. No animations, visual effects, or demonstrations.

---

## Three Scaffolding Levels

### LIGHT
**Purpose:** Brief redirect to key problem features

**Characteristics:**
- 1-2 sentences
- May include brief acknowledgment ("almost", "not quite")
- Redirect attention to relevant problem features
- No explanation of concepts

**Examples:**
- "Almost. Check the spacing between marks."
- "Count seven fourths from zero."
- "Not quite. Look at how many equal parts there are."
- "Let's try again. Make five equal jumps from zero."
- "Check if all the parts are equal."

---

### MEDIUM
**Purpose:** Provide hints about how to solve

**Characteristics:**
- 2-4 sentences
- Acknowledge continued effort
- Explain relevant concepts or strategies
- Reference workspace elements ("the number line", "the parts")
- Don't fully reveal the answer
- Use collaborative language

**Examples:**
- "You're working on it. Here's what helps - each fourth stays the same size even past 1."
- "Let's think about this a bit more. You need 4 equal parts to make the whole."
- "Still tricky? Remember that equal parts means each section is the same size."
- "Here's a hint - count how many equal parts make up the whole."
- "Let's focus on what the denominator tells us. It shows how many equal parts we need."
- "Think about where the halfway point would be, then compare to that."

---

### HEAVY
**Purpose:** Full solution walkthrough revealing the correct answer

**Structure:**
1. **Opening:** Supportive introduction
2. **Solution:** Step-by-step explanation of how to solve
3. **Closing:** Concept reinforcement

**Characteristics:**
- Walk through the complete solution process
- Reveal and explain the correct answer
- Focus on what makes the correct answer correct
- Don't explain what makes incorrect options incorrect
- End with brief concept reinforcement (not generic praise)

**Examples:**

*Number line - locating fraction:*
"Let's work through this together. The number line is divided into thirds - that means 3 equal parts between 0 and 1. Each part represents one-third. To find two-thirds, we count 2 of these parts from 0. That lands us right here at this point. That's how we locate fractions on a number line."

*Number line - fraction beyond 1:*
"These can be challenging. Let's trace through step by step. Four fourths equals 1, then three more fourths gets us to 7/4. That's how we count past 1 on a number line."

*Select - multiple correct answers:*
"Let me work through it with you. We're looking for equal parts. Bar 1 has 4 parts that are all the same size - see how they match up perfectly? Bar 3 has 2 parts which are equal size too. So bars 1 and 3 have equal parts. That's what equal parts means - each section is the same size."

*Select - single correct answer:*
"Here, let me help you with this one. A unit fraction has exactly one part shaded. Bar 1 shows exactly one part shaded. That's what makes it a unit fraction. So the answer is bar 1."

**Concept Reinforcement Examples:**
- "That's how fourths work - 4 equal parts make a whole."
- "That's how we locate fractions on the number line."
- "See how all three parts need to be equal for thirds."
- "There we go - one-fourth is 1 out of 4 equal sections."

---

## Language Guidelines

**Tone:**
- Supportive and encouraging
- Natural and conversational
- Use collaborative language ("let's", "we")

**Avoid:**
- Negative language ("wrong", "incorrect") - use "not quite", "almost", or "let's try again"
- Diagnosing which specific answer the student selected (we don't know this)
- Over-praising - keep concept-focused
- Judgmental phrasing

**Vocabulary:**
- Use developmentally appropriate language
- Reference workspace elements naturally ("the number line", "the tick marks", "the point", "the bar")
- Use consistent fraction terminology ("one-third", "1/3", "thirds")

---

## Output Format

```json
"error_path_generic": {
  "steps": [
    {
      "scaffolding_level": "light",
      "dialogue": "Brief redirect (1-2 sentences)"
    },
    {
      "scaffolding_level": "medium",
      "dialogue": "Hints and guidance (2-4 sentences)"
    },
    {
      "scaffolding_level": "heavy",
      "dialogue": "Full solution walkthrough with concept reinforcement"
    }
  ]
}
```

---

## Quick Quality Checklist

**Light:**
- [ ] 1-2 sentences, brief redirect
- [ ] May include brief acknowledgment ("almost", "not quite")
- [ ] No explanation of concepts

**Medium:**
- [ ] 2-4 sentences with specific hints
- [ ] Acknowledges continued effort
- [ ] Explains concepts without revealing answer
- [ ] Uses collaborative language

**Heavy:**
- [ ] Opens supportively
- [ ] Walks through complete solution step-by-step
- [ ] Reveals and explains correct answer
- [ ] Ends with concept reinforcement (not praise)
- [ ] Focuses on correct answer only

**All Levels:**
- [ ] Progressive scaffolding (light → medium → heavy)
- [ ] Addresses likely error types based on interaction structure
- [ ] Doesn't diagnose which specific answer was selected
- [ ] Solution-focused guidance
- [ ] Developmentally appropriate language
- [ ] Encouraging tone throughout
