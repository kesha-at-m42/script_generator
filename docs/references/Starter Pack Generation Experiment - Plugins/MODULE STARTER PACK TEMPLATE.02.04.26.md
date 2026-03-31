# **MODULE STARTER PACK TEMPLATE**

**Version:** 02.26.26 (v2) **Usage:** One Starter Pack per module. This is a structural template — all `[bracketed content]` must be replaced with module-specific content. **Companion Documents:** Warmup Phase Playbook, Exit Check Phase Playbook, Synthesis Phase Playbook, Practice Phase Playbook v3, Guide vs Prompt Structure Reference

---

## **TEMPLATE CONVENTIONS**

### Section Tags

* **\[REQUIRED\]** — Must be present in every Starter Pack  
* **\[MODULE-SPECIFIC\]** — Content varies by module; placeholders show what to include  
* **\[IF APPLICABLE\]** — Include only when relevant to this module

### Interaction Design Rules

Every interaction follows one of two patterns:

**Pattern 1 — Student Action:** Both `Guide:` AND `Prompt:` are REQUIRED. Guide speaks the teaching/instruction. Prompt provides the standalone written instruction (worksheet-style). Both must be independently complete.

**Pattern 2 — No Student Action:** `Guide:` only. Interaction ends with `**No student action.**`

**Pattern 3 — System-Driven Activity:** Used for games, animated reveals, or system-controlled demonstrations where student participates but the interaction doesn't fit the Guide+Prompt→Answer structure. Document with a specification table (parameters, duration, student role) and an `**On Complete:**` block for what happens after. Flag with a Design Note explaining why Pattern 1/2 don't apply.

If you're unsure which pattern applies, default to Pattern 1\.

### Interaction Type Labels

Every interaction header includes a pedagogical type label in brackets after the title. These labels communicate the interaction's instructional purpose at a glance. Common labels:

* `[ACTIVATION]` — Retrieves prior knowledge or primes a concept
* `[WORKED EXAMPLE]` — Guide demonstrates while student observes or follows along
* `[GUIDED PRACTICE]` — Student acts with scaffolding or Guide support
* `[INDEPENDENT PRACTICE]` — Student acts without scaffolding
* `[CONCEPTUAL CHECK]` — Verifies understanding of a concept (not just procedure)
* `[APPLICATION]` — Student applies learning to a new context or representation
* `[TRANSFER]` — Student extends learning to a novel situation
* `[REFLECTION]` — Student articulates or reviews what they learned

Additional module-specific labels may be created when none of the above fit. Each label should be self-explanatory — a writer reading the SP for the first time should understand the interaction's pedagogical role from the label alone.

### Multi-Step Interactions

When a single conceptual interaction has multiple student response moments — whether from gradual release (Guide models → student attempts with support → student does independently) or from multi-step problems (Step 1 → Visual Update → Step 2\) — use **sub-part numbering** (a/b/c).

The parent interaction (e.g., W.3 or 3.4) gets the Purpose and overall Visual setup. Each sub-part gets its own Guide, Prompt, Student Action, Correct Answer, and Remediation fields as needed. Label steps explicitly when the student sees them as separate submissions ("Step 1:" / "Step 2:"). Document scaffolding changes across sub-parts with a Scaffolding Note.

### Remediation Convention

**Starter Packs never author remediation dialogue.** Every assessed interaction includes:

```
* **Remediation:** Pipeline
```

The Remediation Pipeline generates content for each assessed interaction. The pipeline determines remediation depth from phase and interaction context — no intensity qualifier is needed in the Starter Pack. If a specific interaction requires highly contextual remediation the pipeline cannot infer, add a \`\*\*Remediation Note:\*\*\` annotation after the interaction block.

### Flexibility

Additional sections may be added within any phase if the module requires specialized guidance. Mark these as `### [Module-Specific: Title]` and briefly explain why the section is needed.

---

# **MODULE \[NUMBER\]: \[TITLE\]**

**Version:** \[Date\]

```
---
module_id: M[XX]
unit: [Unit number]
domain: [data_graphs | multiplication | fractions | measurement | geometry | etc.]
primary_toys:
  - name: "[Toy Name]"
    notion_url: "[Link]"  # Use "In development" if spec doesn't exist yet
  - name: "[Toy Name]"
    notion_url: "[Link]"
secondary_toys:
  - name: "[Toy Name]"
    notion_url: "[Link]"
---
```

---

# BACKBONE

---

## **1.0 THE ONE THING**

**\[REQUIRED\]**

\[One sentence: What is the single most important understanding students must leave with?\]

**CRA Stage:** \[Concrete / Relational / Abstract / Application — where this module sits in the unit's CRA progression\]

**Critical Misconception:** \[Which misconception poses the biggest threat to this understanding?\]

**Success Indicator:** \[Observable behavior showing student "gets it"\]

**Biggest Risk:** \[What could derail learning if not addressed?\]

---

## **1.1 LEARNING GOALS**

**\[REQUIRED\]**

*Verbatim — Script Must Achieve These*

**L1:** "\[First learning goal from curriculum\]"

**L2:** "\[Second learning goal if applicable\]"

**Module Goal (Student-Facing):** "\[How would you explain this module's purpose to the student?\]"

**Exit Check Tests:** \[What specific capabilities does Exit Check verify?\]

### **1.1.1 Standards Cascade**

| Building On | \[Prior standard\] |
| :---- | :---- |
| **Addressing** | \[Current standard(s)\] |
| **Building Toward** | \[Future standard(s)\] |

### **1.1.2 Module Bridges**

**From \[Prior Module/Grade\]:** \[What students already know that this module builds on\]

**This Module:** \[What students learn in this module\]

**To \[Next Module\]:** \[How this prepares students for what comes next\]

### **1.1.3 OUR Lesson Sources**

**\[REQUIRED\]**

| OUR Lesson | Content Used | Adaptation Notes |
| :---- | :---- | :---- |
| L\[X\] | \[What content from this lesson is used\] | \[How it was adapted for digital 1:1 delivery\] |
| L\[Y\] | \[Content used\] | \[Adaptation notes\] |

---

## **1.2 SCOPE BOUNDARIES**

**\[REQUIRED\]**

### **✅ Must Teach**

* \[Concept 1\]  
* \[Concept 2\]  
* \[Relevant vocabulary: term1, term2, term3\]

### **❌ Must Not Include**

* \[Out-of-scope concept 1\] (Module X)  
* \[Out-of-scope concept 2\] (Module Y)  
* \[Out-of-scope concept 3\] (Unit Z)

⚠️ **\[PRINCIPLE NAME IF APPLICABLE\]:** \[Explanation of key constraint\]

### **Scope Confirmation Checklist**

*Resolve these questions before drafting:*

- [ ] What concepts are IN scope vs. deferred to later modules?  
- [ ] What vocabulary is introduced vs. just used vs. forbidden?  
- [ ] What specific values/parameters are required? (scales, factor ranges, denominators, etc.)  
- [ ] What value constraints apply? (range limits, multiples-only, etc.)  
- [ ] Are there any "both X and Y" situations (not just X)?  
- [ ] What OUR lessons does this module combine (if any)?  
- [ ] What are the scope boundaries with adjacent modules?

---

## **1.3 VOCABULARY ARCHITECTURE**

**\[REQUIRED\]**

**Assessment Vocabulary (appears on state test):** \[term1\], \[term2\], \[term3\], \[term4\]

### **Vocabulary Staging by Phase**

| Phase | Terms | Introduction Approach |
| :---- | :---- | :---- |
| **Warm-Up** | \[terms\] | \[approach — typically "Use naturally, no formal introduction"\] |
| **Lesson Section 1** | \[terms\] | \[approach — when/how introduced\] |
| **Lesson Section 2** | \[terms\] | \[approach\] |
| **Practice** | (All terms) | \[approach — typically "Use in question contexts"\] |
| **Synthesis** | (All terms) | \[approach — typically "Expect natural student use"\] |

### **Terms to Avoid (Save for Later Modules)**

* \[term\] (Module X)  
* \[term\] (Module Y)

---

## **1.4 MISCONCEPTIONS**

**\[REQUIRED\]** — Include 1-3 misconceptions most relevant to this module. Use global IDs from the Misconceptions database for cross-referencing.

### **1.4.1 \#\[Global ID\]: \[Misconception Name\] (\[PRIMARY/SECONDARY\])**

**Trigger Behavior:** \[What does the student do/say that signals this misconception?\]

**Why It Happens:** \[Cognitive or experiential reason for the misconception\]

**Visual Cue:** \[What visual support helps address this?\]

**Prevention Strategy:** \[How does instruction prevent this from forming?\]

---

### **1.4.2 \#\[Global ID\]: \[Second Misconception Name\]**

\[Same structure as above\]

---

## **1.5 TOY SPECIFICATIONS**

**\[REQUIRED\]** — Include all Toys used in this module. This section defines the **module-specific configuration** of each toy — not what the toy *can* do (that's the Notion spec), but what it *does* do in this module.

### **1.5.1 \[Primary Toy Name\]**

**Notion Spec:** \[Link\] | In development **Changes from M\[N-1\]:** \[What's different about this toy's configuration vs. the previous module. M1 of a unit states "First appearance."\]

#### Module Configuration (M\[X\])

| Aspect | This Module |
| :---- | :---- |
| **Mode** | \[Which mode is active\] |
| **\[Key parameter 1\]** | \[Module-specific value\] |
| **\[Key parameter 2\]** | \[Module-specific value\] |
| **Interaction** | \[How student interacts in this module\] |

#### M\[X\] Guardrails

| DO | DO NOT |
| :---- | :---- |
| \[Permitted behavior in this module\] | \[Forbidden behavior — with reason or future module reference\] |

#### \[IF toy behavior changes across phases\] Progression Within M\[X\]

| Phase | Configuration |
| :---- | :---- |
| **Warmup** | \[State\] |
| **Lesson (Early)** | \[State\] |
| **Lesson (Late)** | \[State\] |
| **Exit Check** | \[State\] |

#### \[IF applicable\] Visibility Rules

\[Specify per-phase visibility for this toy and any paired elements. Example: "Data Table visible in Warmup and Lesson Sections 1-2. NOT visible in Lesson Section 3, Exit Check, or Synthesis."\]

---

### **1.5.2 \[Secondary Toy Name\]**

\[Same structure as Primary Toy\]

---

### **\[IF APPLICABLE\] 1.5.X Display Requirements**

\[For non-interactive display elements. Specify: what it looks like, where it appears (table by phase), how it is generated.\]

### **\[IF APPLICABLE\] 1.5.X Data Constraints by Section**

| Section | \[Domain-specific constraint columns\] |
| :---- | :---- |
| Warmup | \[Constraints\] |
| Lesson S1 | \[Constraints\] |
| Lesson S2 | \[Constraints\] |
| EC | \[Constraints\] |

### **\[IF APPLICABLE\] 1.5.X UX Component Requirements and Fallbacks**

| Component | Requirement | Where Used | Fallback |
| :---- | :---- | :---- | :---- |
| \[Component\] | \[Requirement\] | \[Phases/Interactions\] | \[Fallback if not available\] |

---

### **Interaction Constraints (All Toys)**

* NO verbal/spoken student responses — Guide speaks, student acts  
* NO keyboard/text input — all responses via click/tap/drag  
* NO open-ended questions requiring typed answers — use selection or action tasks  
* Questions in Guide speech must be either rhetorical (Guide answers) or answered through on-screen action

---

## **\[IF APPLICABLE: Additional Backbone Sections\]**

If this module requires specialized guidance not covered above, add sections here:

### **1.X \[Module-Specific: Section Title\]**

\[Content. Explain why this section is needed.\]

---

# PHASE SPECIFICATIONS

---

## **1.6 WARMUP (3-5 minutes)**

**\[REQUIRED\]**

### **Core Purpose**

**Key Function:** \[One sentence: What prior knowledge does this activate and what does it prime for the Lesson?\]

**Why this serves the concept:**

* \[Connection 1 — how this Warmup specifically prepares students for the Lesson's core concept\]
* \[Connection 2 — what prior skill or representation it activates\]
* \[Connection 3 — how it establishes the visual/toy context students will need\]

**Test:** If we removed this Warmup and went straight to the Lesson, students would struggle with \[specific gap\] because \[reason\].

### **Warmup Parameters**

| Element | Specification |
| :---- | :---- |
| **Time** | \[3-5 minutes\] |
| **Interactions** | \[2-3 typical, 5 max\] |
| **Cognitive Load** | 20-30% |
| **Remediation** | Pipeline  |
| **Vocabulary** | Informal only — no formal introduction |

---

**Interaction W.1: \[Title\]**

* **Purpose:** \[What this interaction accomplishes\]  
* **Visual: \[Toy Name\] (\[Mode\]).** \[Orientation\]. \[Data/content summary\]. \[Pre-completion/scaffold state\]. \[Interaction type\]. \[Visibility flags for paired elements\].  
* **Guide:** "\[Complete dialogue — what the guide says to set up and instruct\]"  
* **Prompt:** "\[Complete standalone instruction — what the student reads\]"  
* **Student Action:** \[Interaction type: MC selection / click-to-set / drag-to-place / etc.\]  
  * \[If MC\] **Options:** \[A, B, C, D\]  
* **Correct Answer:** \[Answer\]  
* **On Correct:** "\[Feedback dialogue\]"  
* **Remediation:** Pipeline

**Interaction W.2: \[Title\]**

\[Same structure\]

---

**Interaction W.X: Bridge to Lesson**

* **Purpose:** Create anticipation for Lesson without teaching.  
* **Visual: \[Toy Name\] (\[Mode\]).** \[State description\]  
* **Guide:** "\[Bridge dialogue — teases what Lesson will deliver\]"  
* **No student action.**

---

### **Verification Checklist**

**Universal:**

- [ ] Hook appears in first 15-20 seconds  
- [ ] 2+ engagement anchors from approved types (Narrative, Personalization, Choice, Strength Prompt)  
- [ ] 2+ meaningful interactions requiring judgment (not just clicking)  
- [ ] Bridge creates anticipation without teaching  
- [ ] No vocabulary from Terms to Avoid list appears  
- [ ] Maximum 2 visual states (exceptions require KDD)  
- [ ] Total time 3-5 minutes  
- [ ] Cognitive load feels light (20-30%)  
- [ ] Session-relative language only ("last time/this time," NOT "yesterday/today")  
- [ ] Every interaction with student action has both Guide: and Prompt:

**Module-specific additions:**

- [ ] \[Module-specific check\]  
- [ ] \[Module-specific check\]

---

## **1.7 LESSON (\[TIME RANGE\])**

**\[REQUIRED\]**

### **Core Purpose**

\[What understanding/skills does this Lesson build?\]

### **Pedagogical Flow**

\[Brief description of the learning progression through sections — how does the student's understanding develop?\]

### **Lesson Structure**

| Section | Focus | Time |
| :---- | :---- | :---- |
| Section 1 | \[Focus area\] | \[X-Y min\] |
| Section 2 | \[Focus area\] | \[X-Y min\] |
| Section 3 | \[Focus area if applicable\] | \[X-Y min\] |

---

### Purpose Frame \[RECOMMENDED\]

* **Purpose:** Orient students to what they will learn and why it matters. Reduces cognitive load by providing an advance organizer before instruction begins. See Lesson Phase Playbook §1A.  
* **Visual:** \[Typically same as Section 1 opening visual, or a transitional state from Warmup\]  
* **Guide:** "\[Connection to what they know\] \+ \[What they'll learn to DO\] \+ \[Why it's useful or interesting\]. Use only vocabulary students already know. 10-15 seconds maximum."  
* **No student action.**

*If omitting: Note rationale in §1.10 Key Design Decisions (e.g., "Purpose Frame omitted — Warmup bridge already establishes the driving question").*

---

### **1.7.1 LESSON SECTION 1: \[Title\]**

**Interaction 1.1: \[Title\] \[TYPE LABEL\]**

* **Purpose:** \[What this interaction accomplishes\]
* **Visual: \[Toy Name\] (\[Mode\]).** \[Orientation\]. \[Data/content summary\]. \[Pre-completion/scaffold state\]. \[Interaction type\]. \[Visibility flags for paired elements\].
* **Guide:** "\[Complete dialogue including teaching content \+ instruction\]"
* **Prompt:** "\[Complete standalone instruction — worksheet-style\]"
* **Student Action:** \[Interaction type\]
  * \[If MC\] **Options:** \[A, B, C, D\]
* **Correct Answer:** \[Answer\]
* **Answer Rationale:** \[REQUIRED for every MC interaction\]
  - \[Correct value\] \= Correct (\[explanation\])
  - \[Distractor 1\] \= \[Misconception \# or error type it targets\]
  - \[Distractor 2\] \= \[Misconception \# or error type\]
  - \[Distractor 3\] \= \[Misconception \# or error type\]
* **On Correct:** "\[Feedback dialogue\]"
* **Remediation:** Pipeline
  * \[If needed\] **Remediation Note:** \[Contextual hint for pipeline\]

**Interaction 1.2: \[Title\] \[TYPE LABEL\]**

\[Same structure — include all interactions for this section\]

**\[SECTION TRANSITION if applicable\]**

* **Visual: \[Toy Name\] (\[Mode\]).** \[State\]  
* **Guide:** "\[Transition language\]"  
* **No student action.**

**→ SECTION 1 COMPLETE. PROCEED TO SECTION 2\.**

---

### **1.7.2 LESSON SECTION 2: \[Title\]**

\[Same interaction structure as Section 1\]

**→ SECTION 2 COMPLETE. \[PROCEED TO SECTION 3 / LESSON COMPLETE.\]**

---

### **1.7.3 LESSON SECTION 3: \[Title\]**

**\[IF APPLICABLE\]**

\[Same interaction structure\]

**→ SECTION 3 COMPLETE. LESSON COMPLETE.**

---

### **Required Phrases (Must Appear in Script)**

* "\[Required phrase 1\]"  
* "\[Required phrase 2\]"  
* \[All vocabulary words that must be explicitly stated\]

### **Forbidden Phrases (Create Misconceptions)**

* ❌ "\[Phrase 1\]" (\[why it's problematic\])  
* ❌ "\[Phrase 2\]" (\[why it's problematic\])

### **\[IF APPLICABLE: Module-Specific Lesson Guidance\]**

\[E.g., special toy behaviors, orientation constraints, etc.\]

---

### **Misconception Prevention**

**\#\[Global ID\] (\[Name\]):**

* \[Prevention strategy 1\]  
* \[Prevention strategy 2\]

---

### **1.7.4 Incomplete Script Flags**

**If ANY of these are true, STOP and resolve:**

- [ ] \[Critical missing element 1\]  
- [ ] \[Critical missing element 2\]  
- [ ] Total interaction count below \[X\]  
- [ ] Missing any required phrase  
- [ ] Contains any forbidden phrase  
- [ ] Purpose Frame missing with no KDD justification for omission

### **1.7.5 Success Criteria**

**The One Thing:** \[Restate from 1.0 — what students must understand\]

**Ready for Module \[X+1\]:** \[What capabilities student now has for next module\]

---

## **1.8 EXIT CHECK (\[TIME RANGE\])**

**\[REQUIRED\]**

### **Purpose**

Verify Lesson understanding before Practice. Tests whether student can \[specific capabilities\] using \[specific Toys/modes\] taught in Lesson.

### **Parameters**

| Element | Specification |
| :---- | :---- |
| **Problems** | \[Number\] |
| **Cognitive Types** | \[Types — e.g., IDENTIFY and CREATE only\] |
| **Time** | \[Time range\] |
| **Tone** | Calm, low-stakes |
| **Remediation** | Pipeline (full L-M-H) |

### **Constraints**

| MUST | MUST NOT |
| :---- | :---- |
| Use same visual models as Lesson | Introduce new visual models |
| Use only \[specific items\] taught | Use \[items\] not covered |
| Use same interactions as Lesson | Add new interaction types |
| Match Lesson difficulty | Increase complexity beyond Lesson |

### **Alignment Check**

| Problem | Tests | Lesson Source |
| :---- | :---- | :---- |
| EC.1 | \[Skill tested\] | Section \[X\]: \[Name\] |
| EC.2 | \[Skill tested\] | Section \[X\]: \[Name\] |
| EC.3 | \[Skill tested\] | Section \[X\]: \[Name\] |

---

### **Transition into Exit Check**

* **Purpose:** Signal shift from learning to low-stakes assessment.  
* **Visual: \[Toy Name\] (\[Mode\]).** \[State\]  
* **Guide:** "\[Framing that references what student practiced in Lesson; conveys 'let's see what you know' tone without pressure\]"  
* **No student action.**

---

**Interaction EC.1: \[Title\]**

* **Purpose:** \[What skill this tests — reference Alignment Check table\]  
* **Visual: \[Toy Name\] (\[Mode\]).** \[Orientation\]. \[Data/content summary\]. \[Interaction type\]. \[Visibility flags\].  
* **Guide:** "\[Instruction dialogue\]"  
* **Prompt:** "\[Standalone instruction\]"  
* **Student Action:** \[Interaction type\]  
  * \[If MC\] **Options:** \[A, B, C, D\]  
* **Correct Answer:** \[Answer\]  
* **Answer Rationale:** \[REQUIRED for MC\]  
  - \[Correct\] \= Correct (\[explanation\])  
  - \[Distractor 1\] \= \[Misconception/error\]  
  - \[Distractor 2\] \= \[Misconception/error\]  
* **On Correct:** "\[Feedback\]"  
* **Remediation:** Pipeline

**Interaction EC.2: \[Title\]**

\[Same structure\]

---

### **Verification Checklist**

**Structure:**

- [x] \[X\] problems testing \[X\] distinct skills  
- [ ] Each problem maps to a Lesson section (see Alignment Check)  
- [ ] Transition frame at start (low-stakes, no pressure)  
- [ ] Total time \[X-Y\] minutes

**Alignment:**

- [ ] All visual models appeared in Lesson  
- [ ] All interaction types appeared in Lesson  
- [ ] All values/parameters within Lesson constraints  
- [ ] No skill tested that wasn't explicitly taught  
- [ ] Different cognitive types across problems

**Constraints:**

- [ ] No new vocabulary introduced  
- [ ] No new visual models introduced  
- [ ] No complexity increase beyond Lesson  
- [ ] Every interaction has both Guide: and Prompt:

---

## **\[IF APPLICABLE\] 1.8.5 PRACTICE PHASE INPUTS**

**\[REQUIRED if Practice Phase is generated for this module\]**

This section provides the required inputs for the Practice Phase Playbook (§7).

### **Skill Tracking**

\[Decompose the learning goal into trackable sub-skills for the Practice Phase goal decomposition.\]

| Skill ID | Description | Lesson Source |
| :---- | :---- | :---- |
| \[S1\] | \[Skill description\] | Section \[X\] |
| \[S2\] | \[Skill description\] | Section \[X\] |

### **Distribution Targets**

\[How should practice problems be distributed across skill areas?\]

### **Toy Constraints for Practice**

\[Any differences from Lesson toy configuration? If none, state "Same as Lesson."\]

### **Cross-Module Skill References**

**\[For Modules 2+\]** — Skills from previous modules that should appear in spiral review:

* M\[N-1\] Skill: \[Description\]  
* M\[N-2\] Skill: \[Description\] (if applicable)

---

## **1.9 SYNTHESIS (5-7 minutes)**

**\[REQUIRED\]**

### **Purpose**

\[What connections should students make? How does this consolidate Lesson understanding and preview the next module?\]

---

**Opening Frame**

* **Purpose:** Signal shift to reflection.  
* **Visual: \[Toy Name\] (\[Mode\]).** \[State — typically a completed artifact from the Lesson\]  
* **Guide:** "\[Brief, warm framing that signals reflection mode\]"  
* **No student action.**

---

**Interaction S.1: \[Title\] — \[Task Type: Pattern Discovery / Representation Transfer / Real-World Bridge / Metacognitive Reflection\]**

* **Purpose:** \[What connection this task builds\]  
* **Visual: \[Toy Name\] (\[Mode\]).** \[State\]  
* **Guide:** "\[Reflection prompt\]"  
* **Prompt:** "\[Student instruction\]"  
* **Student Action:** \[Interaction type\]  
  * \[If MC\] **Options:** \[A, B, C, D\]  
* **Correct Answer:** \[Answer\]  
* **On Correct:** "\[Feedback that names the connection\]"  
* **Connection:** "\[The principle or pattern this task demonstrates — Guide states this after the task\]"  
* **Remediation:** Pipeline

**Interaction S.2: \[Title\] — \[Task Type\]**

\[Same structure\]

**Interaction S.3: \[Title\] — \[Task Type\]**

\[Same structure\]

---

**Identity-Building Closure**

* **Purpose:** Specific, growth-oriented affirmation connecting to future learning.  
* **Visual: \[Toy Name\] (\[Mode\]).** \[State — typically shows student's work or a culminating visual\]  
* **Guide:** "\[Module-specific closure that names what student discovered and previews next module. Must be behaviorally specific — not generic praise.\]"  
* **No student action.**

---

### **Verification Checklist**

**Structure:**

- [ ] Opening frame signals shift to reflection (30-45 sec)  
- [x] \[X\] connection tasks (\[X-Y\] min total)  
- [ ] 1 metacognitive reflection moment  
- [ ] Identity-building closure previews Module \[X+1\]  
- [ ] Total time 5-7 minutes

**Task Coverage:**

- [ ] \[Task Type\]: \[Task ID\] — \[specific connection\]  
- [ ] \[Task Type\]: \[Task ID\] — \[specific connection\]  
- [ ] \[Task Type\]: \[Task ID\] — \[specific connection\]  
- [ ] \[If applicable: Generalization task\]

**Known Synthesis Task Types:** Pattern Discovery, Representation Transfer, Real-World Bridge, Metacognitive Reflection. Use at least 2 different types.

**Alignment:**

- [ ] Uses only Toys from Lesson  
- [ ] Visual support for every task  
- [ ] Connections emerge from student experience (not told)

**Constraints:**

- [ ] Remediation via Pipeline (light)  
- [ ] No new procedures introduced  
- [ ] No new vocabulary introduced  
- [ ] Closure is behaviorally specific (not "Great job\!")  
- [ ] Every interaction with student action has both Guide: and Prompt:

---

## **\[IF APPLICABLE: Additional Phase Sections\]**

### **1.X \[Module-Specific: Section Title\]**

\[Content with appropriate structure. Explain why this section is needed.\]

---

## **1.10 KEY DESIGN DECISIONS SUMMARY**

**\[REQUIRED\]**

Master list of cross-cutting design decisions for this module. References phase-level KDDs where relevant. Numbered for easy reference in reviews and feedback.

1. **\[Decision Title\].** \[Statement of what was decided and why. Reference specific interactions, playbook sections, or SME feedback as appropriate.\]  
     
2. **\[Decision Title\].** \[Statement.\]  
     
3. **\[Decision Title\].** \[Statement.\]

\[Continue as needed. Typical range: 5-15 KDDs per module.\]

---

# **END OF MODULE \[X\] STARTER PACK**

---

## **1.11 FINAL FORMATTING AUDIT**

*Complete before submitting Starter Pack:*

### **Tag Removal**

- [ ] All development tags removed: `[Modeling]`, `[MODIFY]`, `[Vocab_Staging]`, `[Tool_Intro]`, etc.  
- [ ] No placeholder text remaining: `[Section X to be added]`, `[TBD]`, etc.

### **Version & Structure**

- [ ] Version line updated (no "DRAFT" unless intentional)  
- [ ] All standard sections present (1.0 through 1.10)  
- [ ] Section headers match template: `## **1.X SECTION NAME**`  
- [ ] No duplicate sections or orphaned content at end of document

### **YAML & Metadata**

- [ ] YAML front matter complete (module\_id, unit, domain, toys with Notion links)  
- [ ] Standards Cascade table format matches template  
- [ ] Module Bridges include From/This/To structure  
- [ ] OUR Lesson Sources table populated  
- [ ] "Changes from M\[N-1\]" present for every toy in §1.5

### **Interaction Block Compliance**

- [ ] Every interaction with student action has BOTH Guide: AND Prompt:  
- [ ] Every teaching-only interaction has Guide: AND "No student action."  
- [ ] Every assessed interaction has `**Remediation:** Pipeline`  
- [ ] Every MC interaction has Answer Rationale with distractor analysis  
- [ ] All Visual: lines include: Toy Name (Mode), orientation, data summary, visibility flags

### **Phase Checklists**

- [ ] Verification Checklists present for Warmup, Exit Check, and Synthesis  
- [ ] Incomplete Script Flags and Success Criteria present in Lesson (§1.7.4, §1.7.5)  
- [ ] KDD Summary present (§1.10) with all significant decisions documented  
- [ ] Practice Phase Inputs present if Practice Phase is generated (§1.8.5)

### **Content Quality**

- [ ] No student-facing dialogue references "Module X" numbers  
- [ ] No authored remediation dialogue (all remediation is `Pipeline`)  
- [ ] Misconceptions use global IDs from database  
- [ ] Session-relative language throughout ("last time/this time," NOT "yesterday/today")

---

## **TEMPLATE USAGE NOTES**

### **What to Keep Consistent Across All Modules**

* Section numbering (1.0 through 1.11 for standard sections)  
* Phase order (Warmup → Lesson → Exit Check → \[Practice Inputs\] → Synthesis)  
* Interaction block format (Visual/Guide/Prompt/Student Action/etc.)  
* Remediation convention (`Pipeline` marker, never authored dialogue)  
* Verification checklists for Warmup, Exit Check, and Synthesis  
* Incomplete Script Flags and Success Criteria for Lesson  
* KDD Summary section  
* YAML front matter with Notion links

### **What Varies by Module**

* Number of Lesson sections (2-4 typical)  
* Number of interactions per phase  
* Specific Toys and their configurations in §1.5  
* Vocabulary staging timeline  
* Misconception focus  
* Synthesis task types and connections  
* Module-specific backbone or phase sections

### **When to Add Module-Specific Sections**

Add sections when:

* A Toy's module-specific behavior needs documentation beyond the standard §1.5 structure  
* A pedagogical approach unique to this module needs explanation  
* The module bridges multiple concepts requiring explicit connection guidance  
* Engineering needs UX component requirements or fallback specifications

### **Naming Convention for Added Sections**

* Backbone additions: `### 1.X [Module-Specific: Title]`  
* Within-phase additions: `### [Module-Specific: Title]`  
* Always explain why this section is needed

---

## **QUICK REFERENCE: INTERACTION BLOCK FORMAT**

### Full Interaction (Warmup, Lesson, Exit Check, Synthesis)

```
**Interaction [ID]: [Title]**

* **Purpose:** [What this interaction accomplishes]
* **Visual: [Toy Name] ([Mode]).** [Orientation]. [Data/content]. [Scaffold state]. [Interaction type]. [Visibility flags].
* **Guide:** "[Teaching + instruction dialogue]"
* **Prompt:** "[Standalone written instruction]"
* **Student Action:** [MC selection / click-to-set / drag-to-place / hover-and-click]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer]
* **Answer Rationale:** [MC only]
  - [Correct] = Correct ([why])
  - [Distractor] = [Misconception/error type]
* **On Correct:** "[Feedback]"
* **Remediation:** Pipeline
```

### Teaching-Only (No Student Action)

```
**Interaction [ID]: [Title]**

* **Purpose:** [What this accomplishes]
* **Visual: [Toy Name] ([Mode]).** [State]
* **Guide:** "[Dialogue]"
* **No student action.**
```

### Annotations (appear after an interaction block, not as fields)

* **Design Note:** Explains a non-obvious design choice for future developers  
* **Voice Note:** Script-writing guidance for tone/delivery  
* **Scaffolding Note:** Explains how scaffolding changes across a sequence  
* **Remediation Note:** Contextual hint for the Remediation Pipeline  
* **Connection:** Names the principle a task demonstrates (Synthesis phase)

---

## **QUICK REFERENCE: VISUAL: LINE FORMAT**

The Visual: line tells the system what to render. Required sub-components:

```
**Visual: [Toy Name] ([Mode if applicable]).** [Orientation]. [Data/Content summary]. [Pre-completion/scaffold state]. [Interaction type]. [Visibility flags for paired elements].
```

| Sub-component | Example | When Required |
| :---- | :---- | :---- |
| **Toy Name \+ Mode** | `Picture Graphs (Mode 2: Creating)` | Always |
| **Orientation** | `Horizontal` / `Vertical` | Whenever toy has orientation |
| **Data/Content summary** | `Pizza=20, Tacos=30, Sandwiches=15` | Always |
| **Pre-completion state** | `Category A complete. Categories B and C empty.` | When partially pre-filled |
| **Interaction type** | `Click-to-set` / `Drag-to-place` | When student manipulates the toy |
| **Visibility flags** | `Data Table not visible.` / `Key visible.` | When paired elements exist |

