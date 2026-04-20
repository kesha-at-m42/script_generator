# Starter Pack Evaluation Plugin vs. Level App Execution: Gap Analysis

**Date:** 2026-04-03
**Scope:** m42-starter-pack-eval plugin (L1 checkers + L2 agents) vs. Unit 5 Level App Module JSON files
**Purpose:** Identify where evaluation criteria diverge from actual app execution — both things the evals miss and assumptions the evals make that don't match reality.

---

## 1. The Remediation Model: Biggest Structural Divergence

**What the eval checks:** The SP format requires `* **Remediation:** Pipeline` — a single word. The L1 checker (I8) flags anything other than the literal word "Pipeline." The eval treats remediation as a black box that will be handled downstream.

**What the app actually does:** Every prompt in the app JSON contains a full `remediations` array with three authored Step objects at escalating intensity levels:

```json
"remediations": [
  { "id": "light",  "step": { "dialogue": "Try clicking right in the middle...", "audio_dir": "..." } },
  { "id": "medium", "step": { "dialogue": "[event:690a5d53fe338284] By finding the exact center...", "audio_dir": "..." } },
  { "id": "heavy",  "step": { "dialogue": "Let me show you. [event:...] Watch as I click...", "audio_dir": "..." } }
]
```

**Gap:** The eval currently has zero visibility into remediation quality — whether the light hint reframes vs. reveals, whether the heavy level demonstrates vs. tells, whether event triggers are used appropriately at each level, and whether remediation voice matches the Guide Voice Design Reference. This is a substantial portion of the student-facing content in the app (roughly 3 additional dialogue lines per prompt) that goes entirely unevaluated.

**Implication for the pipeline:** Whoever authors the light/medium/heavy remediation content after the SP is written does so without the benefit of any of the eval's pedagogical, voice, or scaffolding checks. If remediation authoring happens in a separate step, the eval plugin has no way to catch issues like feeling-assumptions in remediation text, generic praise in medium hints, or cognitive overload in heavy demonstrations.

---

## 2. On Correct: Richer in App Than Eval Assumes

**What the eval checks:** On Correct is a brief text field. L1 checker I20 flags anything over 20 words (target 5–15). L2 voice eval checks that it names what the student did specifically and starts with fact/action, not praise.

**What the app actually does:** `on_correct` is a full Step object with dialogue, audio_dir, and event markers:

```json
"on_correct": {
  "@type": "Step",
  "dialogue": "Yes. You made two [vocab]equal parts[/vocab]: two halves[event:6908edffb57438ca]. See how [event:68fa7214113e92af]each part is exactly the same size?",
  "audio_dir": "module_1/lesson_8517304187604168670"
}
```

**Gap:** The app's On Correct responses routinely include vocabulary reinforcement (`[vocab]...[/vocab]`), visual event triggers that highlight what the student just accomplished, and follow-up observations. Some are significantly longer than 20 words. The eval's 20-word cap may be overly restrictive relative to what the app actually delivers — or the app may be deviating from the design intent. Either way, there's a misalignment worth resolving.

---

## 3. The Event System: Invisible to Evals

**What the eval checks:** Nothing. No L1 checker or L2 agent references `[event:...]` markers.

**What the app actually does:** Event markers are threaded throughout every dialogue string — warmup, lesson, synthesis, exit check, remediation, and on_correct. They trigger animations, visual highlights, glows, pulses, and demonstrations. Examples from the actual JSON:

- `[event:68fa6ab6209ce5db]` before introducing a vocab term (likely highlights the visual)
- `[event:68fa6df96e1a9c90]` during "Watch first" (likely triggers a demonstration animation)
- `[event:68fa7214113e92af]` in on_correct (likely highlights the result)

In remediation metadata, events are even described explicitly:
```json
"metadata": {
  "events": [
    { "name": "sections_glow_together", "description": "Bar top's equal sections glow together..." },
    { "name": "largest_smallest_pulse", "description": "Bar middle's largest and smallest sections pulse..." }
  ]
}
```

**Gap:** Events are a core part of the instructional experience — they're how the app coordinates "show" with "tell." The SP's Visual field attempts to describe what the student sees, but the eval has no way to verify that the visual description actually corresponds to executable event behavior, or that events are placed at pedagogically appropriate moments (e.g., event before observation window, event to reinforce on_correct).

---

## 4. Guide/Prompt Mapping: Different Architecture, Same Intent

**What the eval checks:** Guide and Prompt are separate markdown fields that must each be independently sufficient (GP1). Guide contains conversational teaching; Prompt contains worksheet-style instruction. No teaching in Prompt (GP2).

**What the app actually does:** The Step's `dialogue` field serves as the Guide equivalent — conversational, voiced, teaching-rich. The `prompt.text` field serves as the Prompt equivalent — terse, action-oriented, displayed as UI text.

App examples confirm the eval's independence model is well-aligned:
- **Dialogue (Guide):** "Good. Now let's split the bar into two. Click right in the middle to make two equal parts."
- **Prompt text:** "Click once in the middle to split the bar into 2 equal parts."

**Assessment:** This is one area where the eval's model closely matches app reality. The independence requirement is validated by the app's architecture — a student who only reads the prompt text should be able to act. The eval's GP checks are well-designed here.

---

## 5. Validator Types and Student Action: Precision Lost in Translation

**What the eval checks:** "Student Action" and "Correct Answer" are free-text fields. The eval checks for their presence (I5, I6) but validates nothing about their technical accuracy.

**What the app actually does:** The app has a typed system of tools and validators:

| App Tool | App Validator | What Student Does |
|----------|--------------|-------------------|
| `Select` (is_single: true/false) | `SelectionValidator` (answer: index) | Click to choose from visual options |
| `Paint` | `ShadedValidator` (answer: "1/3") | Click to shade regions of a shape |
| `Place` | `TickValidator` (answer: ["0/2", "1/2", "2/2"]) | Click to place dividing lines |
| `Cut` | `FractionShapePartsValidator` | Cut/divide shapes into parts |
| `Select` + `choices` | `MultipleChoiceValidator` (answer: [0]) | Choose from text options |

**Gap:** The eval can't verify that a "Student Action: Click the bar with equal parts" actually maps to a valid `Select` tool with `SelectionValidator`, or that "Correct Answer: 1/3" maps to a valid `ShadedValidator` answer. More critically, the eval can't catch impossible configurations — e.g., a SP interaction that describes "shade one part" but specifies a tool type that doesn't support shading. The SP is an intent document; the app enforces hard mechanical constraints the eval doesn't know about.

**Potential improvement:** A vocabulary of supported tool types and validator types could be added to the eval, even if just as a warning: "This interaction describes a shading action but doesn't match any known app tool type."

---

## 6. Workspace/Tangible Configuration: High Specificity in App, Low Specificity in Eval

**What the eval checks:** The eval validates toy naming consistency (sp_toy_consistency.py), checks that toys in §1.5 match those used in interactions, and verifies configuration documentation. L2 agents check toy constraint alignment across phases.

**What the app actually does:** Workspace tangibles are precisely configured objects:

```json
{
  "@type": "NumLine",
  "visual": "bar",
  "intervals": "1/4",
  "lcm": 8,
  "intervals_is_shaded": [0],
  "is_visible": true,
  "sum_is_visible": false,
  "intervals_is_frac_label_visible": [0],
  "is_read_only": true
}
```

Fields like `lcm`, `intervals_is_shaded`, `is_read_only`, `is_visible`, and `intervals_is_frac_label_visible` control exact rendering behavior. The SP's Visual field might say "Bar model showing 1/4 with first part shaded" — but the eval has no way to verify this maps to a valid tangible configuration.

**Gap:** The eval checks that "Bar Model" is named consistently and documented in §1.5, but doesn't validate whether the described configurations are technically possible in the app, whether the `lcm` values are correct for the specified fractions, or whether the shading/visibility flags align with the pedagogical intent.

---

## 7. Phases the SP Doesn't Cover

**What the eval checks:** Warmup (§1.6), Lesson (§1.7), Exit Check (§1.8), Practice (§1.8.5), Synthesis (§1.9).

**What the app has:**
- `warmup.json` ✓
- `lesson.json` ✓
- `exit_check.json` ✓
- `practice.json` ✓ (references problem_pool)
- `synthesis.json` ✓
- **`start_of_day_recap.json`** ✗ — Not in SP template
- **`end_of_day_recap.json`** ✗ — Not in SP template

**Gap:** The app has start-of-day and end-of-day recap phases that are entirely outside the SP's scope. These contain student-facing dialogue with voice, vocabulary, event markers, and pedagogical design choices (the end_of_day_recap includes identity-building closure and bridge to next module). These phases are authored somewhere, but they're invisible to the eval.

**Question:** Are these authored separately? If so, is there a quality gate for them? The end_of_day_recap in Module 1 says "You didn't just follow steps - you understood WHY equal parts matter" — which is exactly the kind of feeling-assumption the eval's VO7 checker would flag if it could see it.

---

## 8. Practice/Pool Mechanics: Different Abstraction Levels

**What the eval checks:** Practice Inputs section with distribution targets, skill mapping to Lesson sections, toy constraints tables, cross-module spiral references. The eval validates that the SP documents these inputs clearly.

**What the app actually does:** Practice is a thin wrapper that references a `SequencePool`:

```json
{ "@type": "Step", "pool": { "@type": "PoolData", "id": "problem_pool", "requested_count": 2, "shuffle": false, "use_tiers": false } }
```

The actual problems live in `problem_pool.json` with rich metadata per problem:
```json
"mastery_verb": "IDENTIFY",
"mastery_tier": "BASELINE",
"mastery_component": "CONCEPTUAL",
"difficulty": 0.0,
"template_skill": "The student can recognize and identify equal versus unequal parts"
```

**Gap:** The eval checks that the SP documents distribution targets and skill mappings, but can't verify that the actual problem pool implements those targets. The metadata fields (mastery_verb, mastery_tier, mastery_component, difficulty) are a richer taxonomy than what the SP captures. The `requested_count`, `shuffle`, and `use_tiers` flags control runtime behavior that the SP doesn't specify and the eval doesn't check.

---

## 9. Vocabulary Markup: Inline vs. Table

**What the eval checks:** Vocabulary staging by phase (V3), assessment vocabulary presence (V4), terms to avoid (V1). All validated against the §1.3 vocabulary table.

**What the app does:** Vocabulary terms are wrapped inline: `[vocab]equal parts[/vocab]`. This is how the app renders term highlighting. The app also uses `[fraction numerator=N denominator=D]text[/fraction]` for fraction display.

**Assessment:** The eval's vocabulary staging checks are well-aligned in principle — they verify the right terms appear in the right phases. But the eval operates on free-text SP content and can't verify that vocab markup is correctly applied in the final JSON. A term could be listed as "introduced in Lesson S2" in the SP table but actually appear with `[vocab]` markup in the warmup JSON.

---

## 10. Scene Management: Untracked

**What the eval checks:** Nothing about scene/view changes.

**What the app does:** Steps include a `scene` field with values like `"Lesson"` and `"ZoomedOut"`. The Synthesis phase opens with `"scene": "ZoomedOut"` — a deliberate UX shift that signals reflection mode.

**Gap:** Scene transitions are a meaningful part of the student experience (zooming out literally changes the visual context), but the SP and eval have no way to specify or validate them.

---

## 11. Audio Integration: Entirely Outside Eval Scope

Every Step in the app has an `audio_dir` field pointing to a narration file. The eval has no concept of audio. This is probably fine — audio is generated from dialogue content — but it means the eval can't catch discrepancies between written dialogue and what's actually narrated.

---

## 12. Multiple Choice Architecture: Partially Captured

**What the eval checks:** I9 requires Options + Answer Rationale for MC interactions.

**What the app does:** MC uses a `choices` object with `WorkspaceChoices`:
```json
"choices": { "@type": "WorkspaceChoices", "allow_multiple": false, "options": ["Same", "Different"] }
```
Combined with `MultipleChoiceValidator`: `"answer": [0]`

**Assessment:** The eval's requirement for Options and Answer Rationale is directionally correct but doesn't map cleanly to the app structure. The app has no "Answer Rationale" — it has a validator answer (an index) and on_correct dialogue. The Answer Rationale in the SP is a design artifact that helps authors think about why each option exists, but it has no direct counterpart in the app JSON.

---

## 13. Empty/Structural Steps: App Has Them, SP Doesn't

The app uses empty Steps (`{"@type": "Step"}`) as phase openers — they appear at the start of warmup, practice, and other phases. These likely trigger initialization behavior in the Godot engine. The SP has no equivalent concept, and the eval doesn't account for them. This is low-risk but worth noting for anyone mapping SP content to app JSON.

---

## 14. Delay Markers: Untracked Timing

The app uses `[delay]` markers in dialogue to control narration pacing. Example: "Let's divide it into equal parts. Watch first.[delay] [event:68fa6df96e1a9c90]". The eval doesn't check for or validate timing/pacing, though this affects the student's experience of observation windows (which the L2 lesson eval does check conceptually).

---

## Summary: Where the Eval Is Strong vs. Where It's Blind

### Well-Aligned with App Reality
- **Guide/Prompt independence** — the app's dialogue/prompt.text split validates this design
- **Vocabulary staging** — the app's `[vocab]` markup confirms terms are phase-gated
- **CRA progression** — the app's lesson structures show clear concrete→relational→abstract flow
- **On Correct voice** — the app confirms these are brief, specific, and action-oriented
- **Pedagogical interaction types** — worked examples, activation, application all visible in app structure

### Partially Aligned (Eval Checks Intent, Can't Verify Execution)
- **Toy/tangible configuration** — eval checks naming/documentation, app has precise config objects
- **Practice distribution** — eval checks SP targets, can't verify pool metadata implements them
- **MC structure** — eval checks for Options/Rationale, app uses different mechanics
- **Vocabulary inline markup** — eval checks staging tables, can't verify `[vocab]` placement

### Blind Spots (App Content the Eval Never Sees)
- **Remediation content** (light/medium/heavy dialogue, events, scaffolding quality)
- **Event system** (animation triggers, visual coordination with dialogue)
- **Start-of-day and end-of-day recap phases**
- **Scene management** (Lesson vs. ZoomedOut transitions)
- **Audio alignment** (narration files vs. written dialogue)
- **Delay/timing markers** (pacing of observation windows)
- **Validator/tool type accuracy** (does the described action match a real app capability?)
- **Tangible rendering details** (lcm, shading arrays, visibility flags, read-only state)

---

---

## PART 2: GENERATION PROMPT MISALIGNMENTS

The following findings focus on the content generation side — the Playbooks, Cowork Guidance, and Template that instruct Claude how to write SP content. The question: does the generation guidance produce content that aligns with how the app actually executes it?

---

## 15. On Correct: The Generation Guidance Doesn't Account for the Skip Path

**What the generation guidance says:** On Correct must start with fact or observable action, never generic praise. Pattern #50 is enforced at generation time, at self-check, and at Gate 4. The guidance treats On Correct as a meaningful feedback moment.

**What actually happens in the app:** Students who receive heavy remediation **do not see the On Correct response.** They move directly to the next interaction. This means any pedagogical content in On Correct — conceptual connections, vocabulary reinforcement, pattern naming — is lost for the students who struggled most.

**The problem in our generation prompts:** The Lesson Phase Playbook's concrete phase template shows:
```
5. Explicit Confirmation: "You shaded 3 out of 4 equal parts. That shows three-fourths."
```
This "Explicit Confirmation" maps to On Correct. The generation guidance treats it as step 5 of a 5-step teaching sequence. But if a struggling student never sees step 5, and step 5 contains the explicit naming ("That shows three-fourths"), then the next interaction's Guide needs to carry that load instead.

**What should change in the generation prompts:**
- Add a rule: "On Correct must NOT contain information the student needs for the next interaction to make sense. Treat On Correct as a bonus confirmation for students who got it right on first try."
- Add a companion rule: "The next interaction's Guide must be self-sufficient — it should re-establish context without assuming the student saw the prior On Correct."
- The Lesson Playbook's 5-step concrete sequence should note that step 5 (Explicit Confirmation) is seen only by non-remediated students, and the setup for the next interaction should duplicate any critical naming or pattern statement.

**This is the highest-priority generation fix** because it affects pedagogical coherence for the students who need it most, and it's invisible unless you know the app's remediation skip path.

---

## 16. Student Action Vocabulary: Informal and Unmapped to App Tool Types

**What the generation guidance says:** Student Action field should describe the interaction type with terms like "MC selection / click-to-set / drag-to-place / etc."

**What the app actually supports:** Exactly 4 tool types with specific capabilities:

| App Tool | Behavior | SP Equivalent (if any) |
|----------|----------|----------------------|
| `Select` (is_single: true) | Click one visual element from multiple options | "MC selection" (when selecting visuals) |
| `Select` (is_single: false) | Click multiple visual elements | "Multi-select MC" |
| `Select` + `choices` | Choose from text-label options | "MC selection" (when selecting text) |
| `Paint` | Click regions to shade/color them | No standard SP term |
| `Place` | Click to place dividing lines/marks | "click-to-set" / "drag-to-place" |
| `Cut` | Cut/divide shapes into parts | No standard SP term |

**What actually appears in generated SPs:** A wide variety of informal descriptions with no standard vocabulary:
- "MC selection" (most common)
- "Multi-select MC"
- "Single-select MC"
- "Drag to place decomposition line (edge-to-edge, per Decision #6)"
- "Student decomposes (drag interaction)"
- "Full four-step workflow"
- "MC selection (visual regions as options)"
- "Multi-step MC"

**The problem:** The pipeline engineer who converts SP → app JSON has to interpret these informal descriptions and map them to one of 4 tool types + a validator type. "MC selection (visual regions as options)" could mean Select with visual tangibles, or it could mean Paint. "Full four-step workflow" tells the engineer almost nothing. This ambiguity creates a translation risk where the scripted interaction doesn't match the SP author's intent.

**What should change in the generation prompts:**
- Define a closed vocabulary of Student Action types that maps to app tool capabilities. Something like:
  - `Select (single)` — click one visual element
  - `Select (multiple)` — click multiple visual elements
  - `MC (text options)` — choose from labeled text choices
  - `Paint` — click to shade regions
  - `Place` — click to add dividing lines
  - `Cut` — divide a shape into parts
- The Template and Playbooks should use these exact terms and prohibit free-text descriptions.
- The eval's L1 checker could then validate Student Action against the closed vocabulary.

---

## 17. Think-Aloud Tags: Authoring Metadata That Could Leak into Narration

**What the generation guidance says:** Use metacognitive tags in Guide think-aloud text: `[PLANNING]`, `[ATTENTION]`, `[ACTION]`, `[SELF-CHECK]`, `[CONCLUSION]`. The Playbook shows them embedded in Guide dialogue:
```
Guide: "[PLANNING] First, I ask myself: 'What do I need to find?'
[ATTENTION] I'm going to look at [specific element] first..."
```

**What the app does with dialogue text:** It renders it as narrated speech (with audio) and displays it as text. Any bracketed content that isn't a recognized markup tag (`[vocab]`, `[event:]`, `[fraction]`, `[delay]`) would either render as literal text or cause a parse error.

**The problem:** The generation guidance doesn't clarify whether these tags are:
- (a) Author-facing structural markers that get stripped before scripting, or
- (b) Actual content that appears in the app

If (a), the scripting pipeline needs to know to strip them. If (b), the app needs to support rendering them (it currently doesn't — the app JSON has no metacognitive tags in any dialogue string across all 12 modules).

Looking at the actual app JSON, think-alouds appear as natural dialogue without tags:
```json
"dialogue": "Let me show you. Watch as I click right in the middle to make two equal parts."
```

**What should change in the generation prompts:**
- Clarify that `[PLANNING]`, `[ATTENTION]`, etc. are **authoring annotations only** and must be stripped during scripting.
- OR: Redesign them as annotations outside the Guide dialogue (e.g., as a Design Note) rather than inline in the spoken text.
- The current format invites confusion because the tags look like they belong in the dialogue text.

---

## 18. Visual Field Descriptions: Prose That Maps Ambiguously to App Tangibles

**What the generation guidance says:** Every Visual line must include: `[Toy Name] ([Mode]). [Orientation]. [Data]. [Scaffold state]. [Interaction type]. [Visibility flags].`

**What the app needs:** Structured tangible objects with specific typed fields:
```json
{
  "@type": "NumLine",
  "visual": "bar",
  "intervals": "1/4",
  "lcm": 8,
  "intervals_is_shaded": [0],
  "is_visible": true,
  "is_read_only": true,
  "intervals_is_frac_label_visible": [0]
}
```

**The mapping problem:** The Visual field description is rich prose, but it doesn't map 1:1 to app fields:

| SP Visual Description | App Tangible Field | Mapping Clarity |
|----------------------|-------------------|-----------------|
| "Bar Model" | `@type: NumLine, visual: bar` | Clear |
| "(Partition)" mode | Implies `Place` tool | Ambiguous — is this the tool or the visual state? |
| "Shows 1/4" | `intervals: "1/4"` | Clear for equal divisions |
| "First part shaded" | `intervals_is_shaded: [0]` | Requires index mapping |
| "Fraction labels hidden" | `intervals_is_frac_label_visible: []` | Which label types? Sum? Interval fracs? |
| "No pre-shading" | `intervals_is_shaded: []` or absent | Clear |
| "Click-to-place" | Tool: Place | Clear |
| "Read-only" | `is_read_only: true` | Clear if stated |

**What's actually generated in SPs (from the Grade 3 Unit 2 examples):** Descriptions like:
- "Composite Figures (room mode, labels only, Missing Sides mode). Same room. System highlights the first '?' (top-left horizontal edge)."
- "Composite Figures (room mode, decomposed, color-coded) + Equation Builder (additive mode)."

These are rich, contextual descriptions that communicate *intent* well but leave *implementation* ambiguous. What "color-coded" means in tangible configuration, what "Missing Sides mode" maps to as a field, and whether "Equation Builder (additive mode)" is a tangible, a separate UI component, or a prompt tool — these are all interpretation calls for the scripting pipeline.

**What should change in the generation prompts:**
- For the fractions unit specifically: provide a reference table of known tangible configurations with their Visual-field equivalents. For example: "When you write 'Bar Model showing 3 equal parts with first part shaded,' this maps to NumLine with intervals='1/3', intervals_is_shaded=[0]."
- Consider whether the Visual field should adopt a semi-structured format with explicit key-value pairs for the fields that matter most: toy type, division count, shaded indices, label visibility, read-only state.

---

## 19. Answer Rationale: Heavy Generation Investment, No App Counterpart

**What the generation guidance says:** Answer Rationale is REQUIRED for every MC interaction. All options must be explained with misconception IDs or error types:
```
- 1/3 = Correct (student identifies the shaded fraction)
- 1/4 = Misconception #2 (counts total pieces including unshaded)
- 3/1 = Misconception #3 (inverts numerator/denominator)
```

**What the app has:** No Answer Rationale field. The app has a validator with a correct answer index, and remediation steps that provide scaffolded help. The *content* of Answer Rationale doesn't appear anywhere in the app.

**Assessment:** Answer Rationale is one of the most labor-intensive fields to generate correctly. If it's consumed by the remediation pipeline to author light/medium/heavy hints, that's a strong justification. If it's purely a design artifact that gets discarded, that's a lot of generation effort with no downstream impact.

**Question for the pipeline team:** Does the remediation authoring pipeline actually read Answer Rationale to inform which misconception each distractor targets? If yes, this is well-designed. If no, the generation effort could be redirected to something the app actually uses.

---

## 20. Interaction Type Labels: Design Metadata with No App Execution

**What the generation guidance says:** Every interaction header must include a type label: `[WORKED EXAMPLE]`, `[ACTIVATION]`, `[GUIDED PRACTICE]`, `[CONCEPTUAL CHECK]`, etc.

**What the app has:** No concept of interaction types. Steps are Steps. The app executes them sequentially without knowing whether a Step is a "worked example" or an "activation."

**Assessment:** These labels are valuable for SP readability and for evaluation (the L2 agents use them to check pedagogical progression). They don't cause problems — they're just stripped during scripting. This is a fine design choice, but it means the labels are only as useful as the eval's ability to validate them. If the eval doesn't check that a `[WORKED EXAMPLE]` actually demonstrates before asking the student to try, the label is cosmetic.

---

## 21. Multi-Step Interaction Architecture: SP Sub-numbering vs. App Flat Sequences

**What the generation guidance says:** Multi-step interactions use sub-numbering (1.1a, 1.1b, 1.1c) under a parent interaction with shared Purpose and initial Visual. Each sub-step gets its own Correct Answer, On Correct, and Remediation.

**What the app does:** Steps are flat — they're sequential entries in a `steps` array with no nesting or grouping. There's no concept of "parent" and "child" steps.

**The gap:** The SP's multi-step grouping communicates pedagogical intent (these steps form one conceptual unit). The app can't represent this grouping. During scripting, the sub-steps become independent Steps, and any pedagogical coherence between them depends entirely on the dialogue content.

**What this means for generation:** The Guide for sub-step 1.1b should work even if the student struggled on 1.1a and received heavy remediation (and therefore didn't see 1.1a's On Correct). This reinforces finding #15 — the On Correct skip path affects multi-step sequences especially, because 1.1b might assume the student heard 1.1a's confirmation.

---

## 22. Scene Transitions: Not in Generation Vocabulary

**What the app does:** Steps include a `scene` field: `"Lesson"` for focused work, `"ZoomedOut"` for reflection/overview. Synthesis phases open with ZoomedOut. Some lesson steps use explicit scene setting.

**What the generation prompts say:** Nothing. The Synthesis Playbook describes an "Opening Frame" that should "signal a shift" and create "a different feel from the Lesson" — but never specifies that this maps to a scene change in the app.

**What should change:** The Synthesis Playbook should note that the app renders Synthesis in a zoomed-out view, and the Opening Frame's language should account for this visual shift (e.g., "Look at everything you've been working with" makes sense in ZoomedOut; "Look at this bar" might not).

---

## Summary: Generation-Side Priorities

### Must Fix
1. **On Correct as pedagogical dead-end (#15):** Add explicit rules to Playbooks and Cowork Guidance that On Correct must not carry load-bearing content, and the next interaction's Guide must be self-sufficient. This affects every interaction across every module.

2. **Student Action vocabulary (#16):** Define a closed set of action types mapped to app tool capabilities. The current free-text approach creates scripting ambiguity.

### Should Fix
3. **Think-aloud tag status (#17):** Clarify whether `[PLANNING]`/`[ATTENTION]`/etc. are authoring-only or content. If authoring-only, move them out of the Guide dialogue text.

4. **Visual field → tangible mapping (#18):** For each unit's toys, provide a reference table showing how Visual descriptions map to app tangible configurations. Reduces scripting interpretation risk.

### Investigate
5. **Answer Rationale consumption (#19):** Confirm whether the remediation pipeline actually reads Answer Rationale. If yes, document this dependency. If no, reduce the generation requirement.

6. **Multi-step On Correct dependencies (#21):** Audit existing SPs for cases where sub-step b/c assumes the student heard sub-step a's On Correct. Flag and restructure.
