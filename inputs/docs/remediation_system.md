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
   - **error_count**: The total number of errors the student has made in this interaction
   - The system always serves the remediation level matching the error_count:
     - **Light** level for error_count = 1 (first error)
     - **Medium** level for error_count = 2 (second error)
     - **Heavy** level for error_count ≥ 3 (third or subsequent errors)

### Required Error Paths

Writers create multiple error path options for each interaction:
- **`error_path_generic`** — Always required (fallback for ambiguous/undetectable errors)

Each error path must contain exactly 3 steps in sequence: light, medium, heavy.

## IMPORTANT CLARIFICATION

For the `error_path_generic`, do NOT assume or diagnose a specific error type. This path is used when the system cannot determine the exact nature of the student's mistake. Remediation language and visual scaffolds should remain general, supportive, and non-specific—avoid guessing what the error was. Only reference the student's observable actions or provide general encouragement and guidance.

---

## SECTION 3: REMEDIATION STRUCTURE BY LEVEL

### General Requirements

**Workspace Context:** All remediation steps reference existing tangibles from the main interaction flow. Do not redefine tangibles; use workspace_context to indicate which ones are present (metadata only).

**Visual Effects:** Visual specifications describe dynamic effects/animations applied TO those existing tangibles, or null for light level.

---

### Remediation Structure by Level

Each error path must be structured with 3 scaffolding levels delivered as sequential steps. Each step includes dialogue, workspace_context, and visual specifications.

#### LIGHT
- **Purpose:** Simple redirect without diagnosis
- **Dialogue:** Brief and direct, occasional error signalling.
- **Visual:** `null` (no visual effects applied)
- **Dialogue patterns:**
  - "Check the spacing between marks."
  - "Not quite. Count seven fourths from zero."
  - "Count seven fourths from zero."

#### MEDIUM
- **Purpose:** Specific hint + visual scaffolding
- **Dialogue:** Acknowledge continued struggle, collaborative language
- **Visual:** Effects object with highlight/pulse/arrow animations applied to tangibles
  - `type`: "highlight", "pulse", "arrow"
  - `target`: Specific tangible_id from workspace
  - `animation`: Animation name (e.g., "pulse", "highlight_sections")
  - `description`: Human-readable description of the visual effect
- **Dialogue patterns:**
  - "Let's think about this together..."
  - "Here's a hint..."
  - "You're getting there..."

#### HEAVY
- **Purpose:** Walkthrough revealing the answer
- **Dialogue:** Emotional support, visual demonstration
- **Visual:** Effects object with measurement/overlay/demonstration animations
  - `type`: "measurement", "overlay", "demonstration"
  - `target`: Specific tangible_id from workspace
  - `animation`: Animation name (e.g., "measure_sections_equal", "overlay_counting")
  - `description`: Human-readable description of the demonstration

- **Dialogue structure:**
  - Opening: Modeling introduction ("Let's walk through it together...")
  - Body: Modeling, or demonstration focused on the correct answer
  - Closing: Post-modeling acknowledgment (required)
- **Dialogue patterns:**
  - "Let me help you with this one..."
  - "Here, I'll walk you through this one..."

##### Modeling Guidelines

**Key Principles:**
- Show clear steps that lead to the correct answer. 
- Use visual effects (refer visual_guide.md for inspiration) to support the demonstration

**When you have to look at multiple tangibles to get to the correct answer:**
- **Only focus on what makes the correct answer correct**
- Do not demonstrate what makes the incorrect options incorrect.

**Example Modeling Dialogues:**

Multiple correct answers (bars 1 and 3):
"Let me show you how to find this. We're looking for equal parts. Bar 1 has 4 sections that are all the same width - see how they match up perfectly? Bar 3 has 2 parts which are equal width too. So bars 1 and 3 have equal parts."

Single correct answer (bar 1 only):
"Here, let me show you. A unit fraction has exactly one part shaded. Bar 1 shows exactly one part shaded. That's what makes it a unit fraction."

##### Post-Modeling Acknowledgment Phrases

Reinforce the mathematical concept they just worked through. Make acknowledgment problem-specific and content-focused, not praise-focused.

**Examples:**
- "That's how fourths work - 4 equal parts make a whole."
- "See how all three parts need to be equal for thirds."
- "Now you see why we count from zero on the number line."
- "There we go - one-fourth is 1 out of 4 equal sections."

---

## SECTION 4: LANGUAGE TEMPLATES (BY ERROR TYPE)

### Remediation Language Templates

Use these phrases as templates. Do not repeat exact phrasing across 3 interactions.

#### GENERIC

**Light:**
- "Count seven fourths from zero."
- "Almost. Check your spacing between marks."
- "Check the spacing between marks."
- "Let's try again. Make five equal jumps total."
- "Make five equal jumps from zero."

**Medium:**
- "You're working on it. Here's what helps - each fourth stays the same size even past 1."
- "Let's think about this a bit more. You need 4 equal parts." 
- "Still tricky? Try this..."
- "Here's a different approach..." 
  → [Visual: See visual_guide.md for matching highlight]

**Heavy:**
- "These can be challenging. Let's trace through step by step. Four fourths equals 1, then three more fourths gets us to 7/4."
- "Let's work through this together..."
- "Let me work through it with you..."
- "Here, let me show you..."
- "Let's do it together. Here's how we solve it..." 
- "Let's walk through this step by step together..." 
- "Let me help a bit more..." 
- "Okay, let me show you another way..." 
  → [Modeling] + [Visual: See visual_guide.md]

---

## SECTION 5: COMPANION FILE

### Companion File: `visual_guide.md`

This file contains visual scaffolds by task type + error pattern.

During generation, reference as:
```
→ [Visual: See visual_guide.md: task="bar_shading", error="counting"]
```

All visual effects referenced in medium and heavy remediations should correspond to animations defined in `visual_guide.md`.



