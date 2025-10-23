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

## SECTION 3: REMEDIATION STRUCTURE BY LEVEL

### General Requirements

**Workspace Context:** All remediation steps reference existing tangibles from the main interaction flow. Do not redefine tangibles; use workspace_context to indicate which ones are present (metadata only).

**Visual Effects:** Visual specifications describe dynamic effects/animations applied TO those existing tangibles, or null for light level.

---

### Remediation Structure by Level

Each error path must be structured with 3 scaffolding levels delivered as sequential steps. Each step includes dialogue, workspace_context, and visual specifications.

#### LIGHT (10–20 words)
- **Purpose:** Simple redirect without diagnosis
- **Dialogue:** Brief and direct, occasional error signalling.
- **Visual:** `null` (no visual effects applied)
- **Dialogue patterns:**
  - "Check the spacing between marks."
  - "Not quite. Count seven fourths from zero."
  - "Count seven fourths from zero."

#### MEDIUM (20–30 words)
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
  - Body: Modeling, or step-by-step demonstration with the answer revealed
  - Closing: Post-modeling acknowledgment (required)
- **Dialogue patterns:**
  - "This is tricky, so let's work through it together..."
  - "Let me help you with this one..."
  - "Here, I'll walk you through this one..."

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
- "This can be tricky, so let's do it together.
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



