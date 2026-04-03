# MODULE STARTER PACK AUDIT PROMPT

**Version:** 02.27.26 **Purpose:** Run against any completed or in-progress Module Starter Pack to verify compliance with Template v2 conventions. Produces structured findings with severity, location, and recommended fix.

### Setup

**Required context:** (1) the Starter Pack being audited, (2) the Module Starter Pack Template v2 as reference.

**Recommended context:** Phase playbooks (Warmup, Lesson, Exit Check, Synthesis, Practice), Guide vs Prompt Structure Reference, Misconceptions database.

**Environment options:**

| Environment | How to provide context |
| :---- | :---- |
| **Claude Project** | Add Template v2 and playbooks to Project Knowledge. Starter Packs can live in Project Knowledge or be uploaded per conversation. Adjacent modules (M\[N-1\], M\[N+1\]) are searchable automatically — enables Pass 7\. |
| **Claude Cowork** | Load Template v2 and the target Starter Pack as files. Load adjacent module Starter Packs to enable Pass 7\. |
| **Single conversation** | Attach all documents directly. Practical limit: target SP \+ template \+ 1-2 adjacent SPs. |

**To start:** Tell the auditor which module to audit. Example: *"Audit M7."* or *"Run the audit on the attached Starter Pack."*

---

## INSTRUCTIONS

You are auditing a Module Starter Pack for compliance with the Module Starter Pack Template v2. You will run **6 sequential audit passes** (plus an optional 7th cross-module pass), each focused on a distinct category. After each pass, present your findings and wait for confirmation before proceeding to the next.

**Before Pass 1:** Identify the module being audited and confirm you have access to the Starter Pack and Template v2. If adjacent modules (M\[N-1\] and/or M\[N+1\]) are available in context (Project Knowledge, loaded files, or attached), note which ones you can see — this determines whether Pass 7 is available. If you are in a Project, search Project Knowledge for adjacent modules before declaring them unavailable.

### Output Format

For each pass, produce:

1. **Pass Title and Scope** — What you're checking  
2. **Findings Table** — One row per finding:

| \# | Severity | Location | Finding | Recommended Fix |
| :---- | :---- | :---- | :---- | :---- |
| P1.01 | CRITICAL / MAJOR / MINOR / NOTE | §X.X or Interaction ID | What's wrong | What to do |

3. **Pass Summary** — Total counts by severity \+ any patterns worth calling out  
4. **"Ready for Pass \[N+1\]?"** — Wait for user before continuing

### Severity Definitions

- **CRITICAL** — Structural violation that will break downstream pipeline or create ambiguity for script writers. Must fix. Examples: missing Guide or Prompt on a student-action interaction, authored remediation dialogue where Pipeline marker should be, missing YAML field that the pipeline reads.  
- **MAJOR** — Convention violation that creates inconsistency across modules or between this Starter Pack and the template. Should fix. Examples: wrong §1.5 naming convention, missing "Changes from M\[N-1\]", old remediation notation instead of Pipeline marker, missing Answer Rationale on MC interaction.  
- **MINOR** — Stylistic or formatting deviation that doesn't affect functionality but degrades consistency. Fix when convenient. Examples: end marker says "END OF STARTER PACK" instead of "END OF MODULE \[X\] STARTER PACK", missing Warmup Parameters table, non-canonical Visual: line that nonetheless contains the right information.  
- **NOTE** — Observation, not a violation. Something the auditor noticed that might warrant discussion. Examples: unusually high interaction count, KDD that seems to contradict a playbook principle, a scope decision that might affect adjacent modules.

### Important Principles

- **Audit the document as written.** Don't assume intent — flag what's actually on the page.  
- **Distinguish "missing" from "wrong."** Missing a required section is different from having the section but with wrong content.  
- **Quote the specific text** that triggers a finding when possible. Location should be precise enough that the author can find it without searching.  
- **Don't re-audit previous passes.** Each pass is self-contained. If Pass 1 found a missing section, Pass 3 shouldn't re-flag that same section as missing.  
- **The template is the standard, not perfection.** Some modules legitimately need departures from template structure. If a departure is documented in a KDD with rationale, flag it as NOTE, not MAJOR.

---

## PASS 1: STRUCTURE & METADATA

Check the document's skeleton against the template v2 required sections.

**Check each of these:**

### 1A. YAML Front Matter

- [ ] `module_id` present and formatted as M\[XX\]  
- [ ] `unit` present  
- [ ] `domain` present  
- [ ] `primary_toys` present as list with `name` and `notion_url` for each  
- [ ] `secondary_toys` present (or explicitly empty)  
- [ ] `interaction_tools` present with MC, Drag and Drop, Word Problems (or documented reason for omission)  
- [ ] No legacy fields (`path`, `fractions_required`, `shapes`)  
- [ ] Toys listed as flat strings instead of name/url objects → MAJOR

### 1B. Required Sections Present

Walk through each required section and confirm it exists with correct numbering:

- [ ] §1.0 THE ONE THING (with Critical Misconception, Success Indicator, Biggest Risk)  
- [ ] §1.1 LEARNING GOALS (with L1/L2, Module Goal, Exit Check Tests)  
- [ ] §1.1.1 Standards Cascade  
- [ ] §1.1.2 Module Bridges (From/This/To)  
- [ ] §1.1.3 OUR Lesson Sources (table format)  
- [ ] §1.2 SCOPE BOUNDARIES (Must Teach / Must Not Include / Scope Confirmation Checklist)  
- [ ] §1.3 VOCABULARY ARCHITECTURE (Assessment Vocabulary, Staging table, Terms to Avoid)  
- [ ] §1.4 MISCONCEPTIONS (at least 1, with global ID in header)  
- [ ] §1.5 TOY SPECIFICATIONS (at least one toy subsection)  
- [ ] Interaction Constraints block (the universal NO list)  
- [ ] §1.6 WARMUP  
- [ ] §1.7 LESSON (with at least one section)  
- [ ] §1.7.4 Incomplete Script Flags  
- [ ] §1.7.5 Success Criteria  
- [ ] §1.8 EXIT CHECK  
- [ ] §1.9 SYNTHESIS  
- [ ] §1.10 KEY DESIGN DECISIONS SUMMARY  
- [x] End marker: `END OF MODULE [X] STARTER PACK`

### 1C. Conditional Sections

Flag as NOTE if potentially applicable but absent:

- [ ] §1.1.4 Phase Structure Preview — present if module restructures source curriculum significantly?  
- [ ] §1.5.X Data Constraints by Section — present if toy data varies across phases?  
- [ ] §1.5.X UX Component Requirements — present if toy has engineering dependencies?  
- [ ] §1.5.X Display Requirements — present if module uses non-interactive display elements?  
- [ ] Module-Specific Interaction Tool Notes — present if MC/DnD/WP deviate from FDB defaults?  
- [ ] §1.8.5 Practice Phase Inputs — present if Practice Phase exists for this module?  
- [ ] Any \[Module-Specific\] sections that seem needed but missing?

### 1D. Section Ordering

- [ ] Backbone sections (1.0-1.5) before PHASE SPECIFICATIONS header  
- [ ] Phases in order: Warmup → Lesson → Exit Check → \[Practice Inputs\] → Synthesis  
- [ ] KDD Summary (§1.10) after Synthesis  
- [ ] End marker after KDD Summary  
- [ ] No duplicate sections  
- [ ] No orphaned content after end marker (except §1.11 Final Formatting Audit, which is a template appendix)

### 1E. Version & Housekeeping

- [ ] Version line present (not "DRAFT" unless intentional)  
- [ ] No leftover placeholder text: `[TBD]`, `[Section to be added]`, `[PLACEHOLDER]`  
- [ ] No leftover development tags: `[Modeling]`, `[MODIFY]`, `[Vocab_Staging]`, `[Tool_Intro]`, etc.  
- [ ] "Detail Level:" markers absent (removed in v2)

---

## PASS 2: TOY SPECIFICATIONS (§1.5)

Check that §1.5 follows the configuration-layer convention: Notion defines capability, Starter Pack defines module-specific usage.

**For each toy subsection:**

### 2A. Structure

- [ ] **Notion Spec:** line present with link or "In development"  
- [ ] **Changes from M\[N-1\]:** line present (M1 of a unit says "First appearance")  
- [x] **Module Configuration (M\[X\])** table present (not "Core Specifications" — old naming)  
- [x] **M\[X\] Guardrails** table present (not "M\[X\]-Specific Constraints" — old naming)  
- [x] Conditional subsections present where applicable: Progression Within M\[X\], Visibility Rules

### 2B. Configuration vs. Capability

- [ ] Does the section describe what the toy DOES in this module (configuration)? → CORRECT  
- [ ] Does the section describe what the toy CAN do in general (capability documentation)? → MAJOR: capability belongs in Notion, not Starter Pack  
- [ ] Look for signs of capability creep: interaction type inventories, general feature lists, mode catalogs that aren't specific to this module

### 2C. Naming

- [ ] Toy name matches Notion spec name exactly  
- [ ] No descriptive suffixes: "— Reduced Role", "— Full Variety", "— PRIMARY TOY"  
- [ ] Mode specified in parentheses only when referencing a non-default mode  
- [ ] Consistent naming throughout document (same toy isn't called different things in §1.5 vs. Lesson vs. EC)

### 2D. Cross-Reference

- [ ] Every toy mentioned in interactions (Warmup, Lesson, EC, Synthesis) appears in §1.5  
- [ ] Every toy in §1.5 is actually used in at least one phase  
- [ ] Primary vs. secondary classification makes sense (primary \= core teaching tool, secondary \= supporting)

---

## PASS 3: INTERACTION BLOCK COMPLIANCE

The most detailed pass. Check every interaction in every phase against the canonical block format.

### 3A. Student-Action Interactions (Pattern 1\)

For each interaction where a student does something:

- [ ] **Visual:** line present, starting with `**Visual: [Toy Name] ([Mode]).**`  
- [ ] **Guide:** line present with complete dialogue in quotes  
- [ ] **Prompt:** line present with standalone instruction in quotes  
- [ ] Both Guide and Prompt are independently complete (Prompt isn't just "Do it" — it must make sense without hearing the Guide)  
- [ ] **Student Action:** line present with typed action (MC selection, click-to-set, drag-to-place, etc.)  
- [ ] **Correct Answer:** line present  
- [ ] **On Correct:** line present with feedback dialogue  
- [ ] **Remediation:** Pipeline (not authored dialogue, no intensity qualifiers)

### 3A-2. System-Driven Interactions (Pattern 3\)

For interactions that use games, animated reveals, or system-controlled demos:

- [ ] Documented with specification table (parameters, duration, student role) or equivalent structured description  
- [ ] **On Complete:** block present describing what happens after the activity  
- [ ] Design Note present explaining why Pattern 1/2 don't apply  
- [ ] Not flagged as a Pattern 1 violation (Pattern 3 is valid for game-type interactions)

### 3A-3. Multi-Step Interactions

For interactions with sub-parts (a/b/c) — whether gradual release or sequential submission:

- [ ] Parent interaction has Purpose and overall Visual setup  
- [ ] Each sub-part with student action has its own Guide, Prompt, Student Action, Correct Answer, and Remediation fields  
- [ ] Scaffolding changes or visual updates between sub-parts are documented (Scaffolding Note or Design Note)  
- [ ] Answer Rationale present for MC sub-parts

### 3B. MC-Specific Checks

For each Multiple Choice interaction:

- [ ] **Options:** line present with labeled choices  
- [ ] **Answer Rationale:** section present after Correct Answer  
- [ ] Rationale includes the correct answer with explanation  
- [ ] Rationale includes every distractor with the misconception ID or error type it targets  
- [ ] Distractors are diagnostic (each targets a different error, not just random wrong answers)

### 3C. Teaching-Only Interactions (Pattern 2\)

For each interaction with no student action:

- [ ] **Visual:** line present  
- [ ] **Guide:** line present  
- [ ] Ends with `**No student action.**`  
- [ ] Does NOT have a Prompt: line  
- [ ] Does NOT have Student Action:, Correct Answer:, or Remediation: lines

### 3D. Visual: Line Format

For each Visual: line:

- [ ] Starts with Toy Name and Mode  
- [ ] Includes orientation (when toy has orientation)  
- [ ] Includes data/content summary  
- [ ] Includes pre-completion/scaffold state (when applicable)  
- [ ] Includes interaction type (when student manipulates the toy)  
- [ ] Includes visibility flags for paired elements (when applicable)  
- [ ] Is ONE line (not a multi-line description — animation sequences belong in Design Notes)

### 3E. Remediation Convention

Across the entire document:

- [ ] No `**On Incorrect:**` lines with authored dialogue (all should be `**Remediation:** Pipeline`)  
- [ ] No intensity qualifiers on Pipeline markers (no `Pipeline (light)`, `Pipeline (full L-M-H)`, etc. — just `Pipeline`)  
- [ ] No inline authored remediation within interaction blocks  
- [ ] `**Remediation Note:**` annotations appear AFTER interaction blocks (not inside them) when used  
- [ ] Misconception remediation strategies in §1.4 are prevention-focused, not script dialogue

### 3F. Annotation Usage

- [ ] Design Notes, Voice Notes, Scaffolding Notes, Remediation Notes appear AFTER interaction blocks, not as fields within them  
- [ ] Connection statements in Synthesis appear as a field within the block (this is correct — Connection is a Synthesis-specific field)

---

## PASS 4: PEDAGOGICAL COHERENCE

Check that the content makes sense as curriculum — not just formatting, but whether the pieces fit together.

### 4A. Scope ↔ Content Alignment

- [ ] Everything in §1.2 "Must Teach" appears somewhere in the Lesson interactions  
- [ ] Nothing in §1.2 "Must Not Include" appears in any interaction  
- [ ] Vocabulary in §1.3 "Terms to Avoid" does not appear in Guide or Prompt dialogue  
- [ ] Vocabulary in §1.3 "Staging by Phase" matches actual first appearance in interactions  
- [ ] Assessment vocabulary from §1.3 appears in Exit Check problems

### 4B. Misconception ↔ Interaction Alignment

- [ ] Each misconception in §1.4 has at least one interaction that explicitly prevents or detects it  
- [ ] MC distractors in Answer Rationale reference misconception global IDs from §1.4  
- [ ] Critical Misconception from §1.0 receives the most prevention attention in Lesson

### 4C. Exit Check ↔ Lesson Alignment

- [ ] EC Alignment Check table present, mapping each problem to a Lesson section  
- [ ] Each EC problem tests a skill that was explicitly taught (not just mentioned) in Lesson  
- [ ] EC uses the same toys and interaction types as Lesson  
- [ ] EC values/parameters are within Lesson constraints but not identical to Lesson examples  
- [ ] EC difficulty does not exceed Lesson difficulty  
- [ ] No skill tested in EC that wasn't practiced in Lesson with student action

### 4D. Synthesis ↔ Lesson Alignment

- [ ] Synthesis tasks reference concepts from Lesson (not new material)  
- [ ] At least 2 different Synthesis task types used (Pattern Discovery, Representation Transfer, Real-World Bridge, Metacognitive Reflection)  
- [ ] Identity-building closure names specific observable accomplishments (not generic praise)  
- [ ] Closure previews the next module without teaching it

### 4E. Warmup ↔ Lesson Flow

- [ ] Warmup activates prior knowledge relevant to the Lesson  
- [ ] Bridge to Lesson creates anticipation without teaching  
- [ ] No formal vocabulary introduction in Warmup (per Playbook §4B)  
- [x] Warmup cognitive load is light (20-30% — no complex multi-step tasks)  
- [ ] **Purpose Frame Check:**  
      1. Purpose Frame present at Lesson opening (between bridge and first interaction)  
         1. OR: Omission documented in KDD with clear rationale  
      2. Purpose Frame uses concrete/behavioral language (not formal learning objectives)  
      3. Purpose Frame uses only previously-introduced vocabulary  
      4. Purpose Frame connects backward (prior knowledge) and forward (what they'll learn)  
      5. Purpose Frame does not duplicate Warmup bridge content  
      6. Purpose Frame ≤ 15 seconds delivery time (\~2-3 sentences)

### 4F. Learning Goal Thread

- [ ] §1.0 The One Thing is testable in Exit Check  
- [ ] §1.1 Learning Goals are achievable through Lesson interactions  
- [ ] §1.1 Exit Check Tests list matches actual EC problems  
- [ ] §1.7.5 Success Criteria restates §1.0 in terms of observable student capability  
- [ ] Module Bridges "To \[Next Module\]" is specific enough that the next module's author can write a Warmup callback from it

**Cross-module check (if adjacent modules available):**

- [ ] "To \[Next Module\]" description aligns with M\[N+1\]'s "From \[This Module\]" (concepts, vocabulary, and toy references match)  
- [ ] "From \[Prior Module\]" description aligns with M\[N-1\]'s "To \[This Module\]"  
- [ ] Synthesis closure preview matches what M\[N+1\] actually teaches (not a different topic)  
- [ ] Warmup callback references align with what M\[N-1\] actually taught

If adjacent modules are in Project Knowledge, search for them now. Flag mismatches as MAJOR.

---

## PASS 5: CROSS-PHASE CONSISTENCY

Check that conventions, values, and references are consistent across the entire document.

### 5A. Toy Consistency

- [ ] Same toy name used in §1.5, Warmup, Lesson, EC, and Synthesis  
- [ ] Toy modes referenced in interactions match modes described in §1.5  
- [ ] Visibility rules from §1.5 are respected in interactions (e.g., "Data Table not visible in EC" → EC interactions don't reference Data Table)

### 5B. Value Consistency

- [ ] Data constraints from §1.5 respected across all phases  
- [ ] EC values differ from Lesson values (no exact repeats at same cognitive demand)  
- [ ] Synthesis values differ from both Lesson and EC  
- [ ] Factor ranges, scale values, or other domain parameters stay within declared bounds

### 5C. Vocabulary Consistency

- [ ] Terms to Avoid don't appear in ANY phase (including Synthesis)  
- [ ] New vocabulary introduced in Lesson is used correctly in EC and Synthesis  
- [ ] No vocabulary is used before its staging phase (e.g., formal term in Warmup that §1.3 says is introduced in Lesson Section 2\)

### 5D. Interaction Counting

- [ ] Warmup: 2-5 interactions \+ bridge (count)  
- [ ] Lesson: 6+ interactions minimum (count)  
- [ ] Exit Check: problem count matches the module's own §1.8 Parameters table (typically 3-4)  
- [ ] Synthesis: typically 3-4 tasks \+ opening frame \+ closure (count)  
- [ ] Total interaction count is reasonable for the module's scope  
- [ ] If §1.1.4 Phase Structure Preview exists, actual counts match estimated counts

### 5E. Verification Checklists

- [ ] Warmup Verification Checklist present and completed (checked or unchecked)  
- [ ] Exit Check Verification Checklist present and completed  
- [ ] Synthesis Verification Checklist present and completed  
- [ ] Lesson has Incomplete Script Flags (§1.7.4)  
- [ ] Checklist items match actual content (e.g., checklist says "3 connection tasks" and there are indeed 3\)

---

## PASS 6: VOICE & CONTENT QUALITY

Check dialogue, framing, and authorial conventions.

### 6A. Session-Relative Language

- [ ] No "yesterday" / "today" / "tomorrow" in Guide dialogue  
- [ ] Uses "last time" / "this time" / "next time" for cross-module references  
- [ ] No "Module X" numbers in student-facing dialogue (Guide and Prompt)  
- [ ] Module numbers OK in author-facing annotations (Design Notes, Voice Notes)

### 6B. Guide Dialogue Quality

- [ ] Guide dialogue contains both teaching content AND complete instruction  
- [ ] Guide dialogue uses contractions naturally ("Let's", "you'll", "that's")  
- [ ] Guide dialogue doesn't assume internal states ("You feel proud", "You noticed")  
- [ ] Guide dialogue uses observable acknowledgments ("You found 12", "You picked Scale of 10")  
- [ ] No overpraise ("Amazing\!", "Incredible\!", "You're a genius\!")  
- [ ] Warm, clear tone — not overly formal or clinical

### 6C. Prompt Quality

- [ ] Prompts are standalone — a student reading ONLY the prompt can understand what to do  
- [ ] Prompts are concise (typically 1-2 sentences)  
- [ ] Prompts don't duplicate Guide teaching — they're worksheet-style instructions only  
- [ ] Prompts don't reference what the Guide just said ("Like I explained...")

### 6D. Feedback Quality (On Correct)

- [ ] Feedback names what the student did correctly (not just "Correct\!")  
- [ ] Feedback reinforces the concept, not just the answer  
- [ ] Feedback is brief (1-2 sentences typical)  
- [ ] No assumed emotional states in feedback

### 6E. KDD Quality

- [ ] Each KDD has a clear decision title and rationale  
- [ ] KDDs reference specific interactions, playbook sections, or SME feedback  
- [ ] Playbook departures are documented as KDDs with justification  
- [ ] No KDD contradicts another KDD within the same document  
- [ ] If 10+ KDDs, organized by section (Backbone, Warmup, Lesson, EC, Synthesis)

### 6F. No Authored Remediation (Final Check)

This is important enough to check twice (also in Pass 3E). Do a final sweep:

- [ ] No authored dialogue that scripts what to say when a student gets something wrong  
- [ ] Misconception §1.4 contains prevention/detection strategies, not remediation scripts  
- [ ] All remediation is `Pipeline` with no intensity qualifiers — no exceptions within interaction blocks

---

## PASS 7: CROSS-MODULE COHERENCE (Optional — requires adjacent modules)

**Skip this pass if M\[N-1\] and M\[N+1\] are not available.** If you are in a Project, search Project Knowledge before skipping. This pass catches the seams between modules — the places where one module's assumptions about its neighbors don't match reality.

### 7A. Scope Boundary Handoffs

Compare §1.2 of this module with §1.2 of adjacent modules:

- [ ] Everything this module's "Must Not Include" defers to M\[N+1\] actually appears in M\[N+1\]'s "Must Teach"  
- [ ] Everything M\[N-1\] defers to this module (in M\[N-1\]'s "Must Not Include") appears in this module's "Must Teach"  
- [ ] No concept falls through the gap — deferred by one module but not picked up by the next  
- [ ] No concept is claimed by both modules (duplicate teaching)

### 7B. Vocabulary Handoffs

Compare §1.3 across modules:

- [ ] Terms this module introduces are listed as "carried" (not re-introduced) in M\[N+1\]  
- [ ] Terms this module lists as "Terms to Avoid" are not used in M\[N-1\] either (or if they are, M\[N-1\] explicitly introduces them)  
- [ ] Assessment vocabulary accumulates correctly — M\[N+1\] doesn't drop terms this module established  
- [ ] No vocabulary is introduced in this module that M\[N-1\] already introduced (redundant introduction)

### 7C. Toy Progression

Compare §1.5 across modules:

- [ ] "Changes from M\[N-1\]" accurately describes what actually changed (compare this module's §1.5 with M\[N-1\]'s §1.5)  
- [ ] Toy modes used in this module match what M\[N-1\]'s "To Next Module" bridge implies  
- [ ] Any toy that appears for the "first time" in this module is not actually used in M\[N-1\]  
- [ ] Any toy that this module says is used for the "last time" is indeed absent from M\[N+1\]

### 7D. Misconception Continuity

Compare §1.4 across modules:

- [ ] Misconceptions flagged here but first introduced in M\[N-1\] are consistent in description and global ID  
- [ ] Prevention strategies don't contradict M\[N-1\]'s approach (e.g., this module doesn't undo scaffolding M\[N-1\] deliberately built)  
- [ ] If a misconception is marked PRIMARY here but was SECONDARY in M\[N-1\], there's a pedagogical reason (the concept that triggers it is now central)

### 7E. Data Value Continuity

- [ ] Value ranges/constraints don't regress (e.g., M\[N-1\] used products to 100 but this module caps at 30 without explanation)  
- [ ] Data constraints are appropriately progressive (this module's "early" difficulty ≈ M\[N-1\]'s "late" difficulty)  
- [ ] If this module introduces new value types (e.g., non-multiples for the first time), it's documented in §1.2 or a KDD

### 7F. Bridge Symmetry

- [ ] M\[N-1\]'s Synthesis closure preview matches this module's Warmup callback  
- [ ] This module's Synthesis closure preview matches M\[N+1\]'s Warmup callback  
- [ ] The "story" a student experiences crossing module boundaries is coherent — no jarring topic shifts, no concepts referenced that the student hasn't seen

---

## FINAL SUMMARY

After all passes (6 or 7), produce:

### Compliance Scorecard

| Pass | Critical | Major | Minor | Note |
| :---- | :---- | :---- | :---- | :---- |
| 1: Structure & Metadata |  |  |  |  |
| 2: Toy Specifications |  |  |  |  |
| 3: Interaction Blocks |  |  |  |  |
| 4: Pedagogical Coherence |  |  |  |  |
| 5: Cross-Phase Consistency |  |  |  |  |
| 6: Voice & Content Quality |  |  |  |  |
| 7: Cross-Module Coherence |  |  |  |  |
| **TOTAL** |  |  |  |  |

(Mark Pass 7 as "SKIPPED" if adjacent modules were unavailable.)

### Top 5 Priority Fixes

List the 5 highest-impact findings across all passes, in recommended fix order.

### Patterns

Any recurring issues that suggest a systematic habit rather than isolated errors (e.g., "Author consistently writes On Incorrect dialogue — 14 instances across Lesson and EC" or "Visual: lines are prose throughout — none match canonical format").

### Cross-Module Issues (Pass 7 only)

If Pass 7 ran, summarize any boundary mismatches that require coordination with adjacent modules. These are especially important because fixing them may require edits to TWO documents, not just this one. Flag which module "owns" the fix (i.e., which one should change to match the other).

### Template Gaps (if any)

If the audit revealed a legitimate document need that the template v2 doesn't accommodate, flag it here. This feeds back into template evolution.  
