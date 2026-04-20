# **MODULE STARTER PACK TEMPLATE**

**Version:** 03.30.26 (v3) **Usage:** One Starter Pack per module. This is a structural template — all `[bracketed content]` must be replaced with module-specific content. **Companion Documents:** Warmup Phase Playbook, Exit Check Phase Playbook, Synthesis Phase Playbook, Practice Phase Playbook v3, Guide vs Prompt Structure Reference

**v3 Changelog (from v2):** Codifies H3 headers for interaction blocks (matching M8-M11 practice). Adds Pattern 4 (System-Driven Demonstration with Think-Aloud). Formalizes multi-phase interaction sub-numbering with per-phase field requirements. Adds Visual: completeness checklist. Strengthens remediation convention with explicit anti-patterns. Adds interaction block compliance self-check. Driven by M8-M12 deviation audit.

---

## **TEMPLATE CONVENTIONS**

### Heading Hierarchy

* Exactly 3 H1s in the SP: Module title, `BACKBONE`, `PHASE SPECIFICATIONS`
* All sections use H2: `## 1.0 THE ONE THING`, `## 1.6 WARMUP`, etc.
* Subsections and interactions use H3: `### Interaction W.1:`, `### Verification Checklist`
* **No H4s.** Convert to bold inline labels if needed.
* **No bold markers on headings.** Use `## 1.0 THE ONE THING`, NOT `## **1.0 THE ONE THING**`

### Section Tags

* **\[REQUIRED\]** — Must be present in every Starter Pack
* **\[MODULE-SPECIFIC\]** — Content varies by module; placeholders show what to include
* **\[IF APPLICABLE\]** — Include only when relevant to this module

### Interaction Design Rules

Every interaction follows one of four patterns:

**Pattern 1 — Student Action:** Both `Guide:` AND `Prompt:` are REQUIRED. Guide speaks the teaching/instruction. Prompt provides the standalone written instruction (worksheet-style). Both must be independently complete.

**Pattern 2 — No Student Action (Teaching-Only):** `Guide:` only. Interaction ends with `* **No student action.**`

**Pattern 3 — System-Driven Activity:** Used for games, animated reveals, or system-controlled demonstrations where the student participates but the interaction doesn't fit the Guide+Prompt→Answer structure. Document with a **specification table** and an `**On Complete:**` block. Flag with a Design Note explaining why Patterns 1/2 don't apply.

Specification table format:

```
| Parameter | Specification |
|---|---|
| **System Action** | [What the system does — animation, shading, highlighting, etc.] |
| **Duration** | [Estimated time in seconds] |
| **Student Role** | [Observe / Confirm via MC / Interact during animation] |
| **Visual State Change** | [What changes on screen from start to end] |

**On Complete:** [Guide dialogue + what happens next]
```

**Pattern 4 — Think-Aloud Demonstration:** A teaching-only interaction where the Guide models cognitive process. Used for worked examples where making the Guide's reasoning visible is pedagogically important. The Guide field is a single, continuous field of natural speech. Do NOT split the Guide into multiple bullet points or create a separate `[System Action]` field for think-alouds.

**Metacognitive tags (`[PLANNING]`, `[ATTENTION]`, `[SELF-CHECK]`, etc.) are authoring-only annotations.** They may be used during drafting to structure the think-aloud, but must be **stripped before publishing to Notion or handing off to scripting.** The app renders Guide dialogue as spoken narration — bracketed tags would be read aloud or cause parsing errors. The final Guide dialogue should read as natural speech.

```
### Interaction [ID]: [Title] [WORKED EXAMPLE]

* **Purpose:** [What this demonstrates]
* **Visual: [Toy Name] ([Mode]).** [State]
* **Guide:** "First, I need to find out how many parts there are. I'm looking at [specific element]... [result]. Does that match? Yes, because..."
* **No student action.**
```

Pattern 4 may be followed by a Pattern 1 interaction where the student attempts the same type of problem. Document this pairing with a Scaffolding Note.

If you're unsure which pattern applies, default to Pattern 1.

### Student Action Vocabulary

Use this standard vocabulary for the Student Action field. These terms describe what the student physically does and are stable across engineering changes. Do not invent free-text descriptions.

**Core Interaction Types (what the student does with the toy):**

| Student Action Term | What the Student Does | Typical Toys |
|---|---|---|
| Select (single) | Click one visual element from multiple on-screen options | Fraction strips, number lines, shapes, arrays |
| Select (multiple) | Click multiple visual elements | Grid cells, fraction parts, graph columns |
| MC (single) | Choose one option from labeled text/image cards (radio buttons) | Any toy — MC is a response overlay |
| MC (multiple) | Choose multiple options from labeled text/image cards (checkboxes) | Any toy — "Select ALL that apply" |
| Shade | Click regions to shade/color them | Fraction strips, fraction circles, area models |
| Place tick | Click to add tick marks that partition a line | Number lines |
| Place point | Snap a point to an existing tick on a line | Number lines |
| Drag label | Drag a fraction label from a palette onto a tick | Number lines |
| Drag to build | Drag parts from a palette to construct a representation | Equation Builder, Secret Code Cards |
| Drag to group | Drag cards onto each other to form groups by shared property | Card Grouping |
| Fill blank | Click a fill space, then select a word/phrase from a palette | Fill-in-the-Blank / Drop Down |
| Type number | Type digits via keyboard into an input field | Text-Based Numeric Entry |
| Enter number | Click on-screen digit buttons to compose a numeric answer | On-Screen Numeric Input |

**Toy-specific actions (used within multi-step interactions):**

| Student Action Term | What the Student Does | Typical Toys |
|---|---|---|
| Stack / Overlay | Drag or tap to stack place-value cards, hiding trailing zeros | Secret Code Cards |
| Separate | Tap or drag apart a stacked overlay to reveal component values | Secret Code Cards |
| Flip | Tap a card to flip between numeral and block representation | Secret Code Cards |
| Cut | Divide a shape into equal parts | Fraction shapes, area models |

**Combining terms:** When an interaction requires multiple steps, chain them with arrows: "Place tick → Shade" or "Drag to build → MC (single)." When sub-steps are sequential parts of one interaction, use sub-part numbering (a/b/c) with each sub-part getting its own Student Action.

**Extending this table:** If a toy's interaction does not map to any term above, the SP author proposes a new term following these conventions: (1) action-verb-based, describing what the student physically does, (2) no app tool names or engineering internals, (3) distinct from existing terms — not a synonym. Use the proposed term in the Student Action field with a `⚠️ NEW-ACTION` flag, and add it to the Working Notes for author review. Approved terms get added to this table in the next Template revision. If the action is a variant of an existing term, use the base term with a parenthetical qualifier instead (e.g., `Drag to build (slot-constrained)`).

**Observation-only:** When the student watches a Guide demonstration or system animation with no action required, use "No student action." (Pattern 2 or Pattern 4).

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

When a single conceptual interaction has multiple student response moments — whether from gradual release (Guide models → student attempts with support → student does independently) or from multi-step problems (Step 1 → Visual Update → Step 2) — use **sub-part numbering** (a/b/c).

**Structure:**

```
### Interaction 1.1: [Title] [TYPE LABEL]

* **Purpose:** [Overall purpose of the multi-step sequence]
* **Visual: [Toy Name] ([Mode]).** [Initial state for the full sequence]

#### Interaction 1.1a: [Sub-step title]

* **Guide:** "[Dialogue for this step]"
* **Prompt:** "[Instruction for this step]"
* **Student Action:** [Action type]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer for this step]
* **Answer Rationale:** [Required for every MC sub-part]
  - [Correct] = Correct ([why])
  - [Distractor] = [Misconception/error type]
* **On Correct:** "[Feedback for this step]"
* **Remediation:** Pipeline

#### Interaction 1.1b: [Sub-step title]

* **Visual:** [State change from 1.1a, if any]
* **Guide:** "[Dialogue for this step]"
* **Prompt:** "[Instruction for this step]"
* **Student Action:** [Action type]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer for this step]
* **Answer Rationale:** [Required for every MC sub-part]
* **On Correct:** "[Feedback for this step]"
* **Remediation:** Pipeline
```

**Requirements:**
- Every sub-part with a student action gets its own **Correct Answer**, **Answer Rationale** (if MC), **On Correct**, and **Remediation: Pipeline**.
- Do NOT combine multiple student actions into a single interaction block without sub-numbering. If a student submits more than one answer, there must be more than one sub-part.
- The parent interaction holds the shared Purpose and initial Visual. Sub-parts hold per-step fields.
- Label steps in Guide dialogue when the student sees them as separate submissions ("Step 1:" / "Step 2:").
- Document scaffolding changes across sub-parts with a Scaffolding Note after the block.

### Remediation Convention

**Starter Packs never author remediation dialogue.** Every assessed interaction includes:

```
* **Remediation:** Pipeline
```

The Remediation Pipeline generates content for each assessed interaction. The pipeline determines remediation depth from phase and interaction context — no intensity qualifier is needed in the Starter Pack. If a specific interaction requires highly contextual remediation the pipeline cannot infer, add a `**Remediation Note:**` annotation after the interaction block.

**Anti-patterns (do NOT do these):**
- `* **Remediation:** Light` / `Medium` / `Heavy` / `Full L-M-H` — no intensity qualifiers.
- Inline remediation scripts with numbered steps and dialogue — this is Pipeline output, not SP content.
- `If student [does X]: 1. Reorient... 2. Redirect...` — this belongs in the Remediation Pipeline, not in the SP.
- `* **Remediation:** Pipeline` followed by additional remediation bullets — the `Pipeline` keyword is terminal. Use a **Remediation Note** annotation (after the block, as a blockquote) if context is needed.

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
    notion_url: "[Link]"  # Use "In development" if spec doesn't exist yet. At Task 1, verify any "In development" links inherited from M[N-1] — the spec may now exist.
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
> **Task 1 check:** If M\[N-1\] listed this toy's Notion Spec as "In development," search the toy spec database to confirm whether a spec page now exists before carrying the placeholder forward.

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
| **Vocabulary** | NEW terms: forbidden. ESTABLISHED terms from prior modules: activate for review, not re-teaching. No `[vocab]` tags in Warmup — all Warmup terms are established. |

---

### Interaction W.1: \[Title\] \[TYPE LABEL\]

* **Purpose:** \[What this interaction accomplishes\]  
* **Visual: \[Toy Name\] (\[Mode\]).** \[Orientation\]. \[Data/content summary\]. \[Pre-completion/scaffold state\]. \[Interaction type\]. \[Visibility flags for paired elements\].  
* **Guide:** "\[Complete dialogue — what the guide says to set up and instruct\]"  
* **Prompt:** "\[Complete standalone instruction — what the student reads. Target 7–12 words.\]"
* **Student Action:** \[Use standard vocabulary from §Student Action Vocabulary table above. Chain multi-step with arrows.\]
  * \[If MC\] **Options:** \[A, B, C, D\]  
* **Correct Answer:** \[Answer\]  
* **On Correct:** "\[10–20 words. Fact/action first, never praise. No NEW information — heavy-remediation students skip this.\]"
* **Remediation:** Pipeline

### Interaction W.2: \[Title\] \[TYPE LABEL\]

\[Same structure\]

---

### Interaction W.X: Bridge to Lesson

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

### **Vocabulary Reinforcement Plan**

Track only **NEW** and **STATUS-CHANGE** terms (informal → formal) introduced in THIS module. Established terms from prior modules are reinforced through natural use but do not appear in this table and do not carry `[vocab]` tags.

| Term | Introduced At | Reinforced In | Target Density |
| :---- | :---- | :---- | :---- |
| \[vocab\]term 1\[/vocab\] | Interaction \[X.Y\] | \[List of subsequent interaction IDs where term appears in Guide dialogue\] | \[N\]x in \[M\] remaining interactions (\[%\]) |
| \[vocab\]term 2\[/vocab\] | Interaction \[X.Y\] | \[List\] | \[N\]x in \[M\] remaining (\[%\]) |

**Minimum target:** Each new/status-change term should appear in Guide dialogue for at least **50% of remaining interactions** after introduction. On Correct fields that reference the concept should also use the formal term with `[vocab]` markup.

**Warmup activation:** If this module's vocabulary builds on prior-module terms, list which established terms are activated in Warmup (for reference — no `[vocab]` tags on established terms).

---

### Purpose Frame \[RECOMMENDED\]

* **Purpose:** Orient students to what they will learn and why it matters. Reduces cognitive load by providing an advance organizer before instruction begins. See Lesson Phase Playbook §1A.  
* **Visual:** \[Typically same as Section 1 opening visual, or a transitional state from Warmup\]  
* **Guide:** "\[Connection to what they know\] \+ \[What they'll learn to DO\] \+ \[Why it's useful or interesting\]. Use only vocabulary students already know. 10-15 seconds maximum."  
* **No student action.**

*If omitting: Note rationale in §1.10 Key Design Decisions (e.g., "Purpose Frame omitted — Warmup bridge already establishes the driving question").*

---

### **1.7.1 LESSON SECTION 1: \[Title\]**

### Interaction 1.1: \[Title\] \[TYPE LABEL\]

* **Purpose:** \[What this interaction accomplishes\]
* **Visual: \[Toy Name\] (\[Mode\]).** \[Orientation\]. \[Data/content summary\]. \[Pre-completion/scaffold state\]. \[Interaction type\]. \[Visibility flags for paired elements\].
* **Guide:** "\[Complete dialogue including teaching content \+ instruction. Mark vocabulary terms with \[vocab\]term\[/vocab\] from introduction through end of module.\]"
* **Prompt:** "\[Complete standalone instruction — worksheet-style\]"
* **Student Action:** \[Interaction type\]
  * \[If MC\] **Options:** \[A, B, C, D\]
* **Correct Answer:** \[Answer\]
* **Answer Rationale:** \[REQUIRED for every MC interaction\]
  - \[Correct value\] \= Correct (\[explanation\])
  - \[Distractor 1\] \= \[Misconception \# or error type it targets\]
  - \[Distractor 2\] \= \[Misconception \# or error type\]
  - \[Distractor 3\] \= \[Misconception \# or error type\]
* **On Correct:** "\[Feedback dialogue. Use \[vocab\]term\[/vocab\] for established vocabulary.\]"
* **Remediation:** Pipeline
  * \[If needed\] **Remediation Note:** \[Contextual hint for pipeline\]

### Interaction 1.2: \[Title\] \[TYPE LABEL\]

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

### Interaction EC.1: \[Title\] \[COGNITIVE TYPE\]

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

### Interaction EC.2: \[Title\] \[COGNITIVE TYPE\]

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

### Interaction S.1: \[Title\] — \[Task Type: Pattern Discovery / Representation Transfer / Real-World Bridge / Metacognitive Reflection\]

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

### Interaction S.2: \[Title\] — \[Task Type\]

\[Same structure\]

### Interaction S.3: \[Title\] — \[Task Type\]

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

- [ ] Every interaction header uses H3 format: `### Interaction [ID]: [Title] [TYPE LABEL]`
- [ ] Every field uses inline bullet format: `* **Field:** value` (NOT field-as-paragraph)
- [ ] Field order matches spec in every interaction: Purpose → Visual → Guide → Prompt → Student Action → Correct Answer → Answer Rationale → On Correct → Remediation
- [ ] Every interaction with student action has BOTH Guide: AND Prompt:
- [ ] Every teaching-only interaction has Guide: AND `* **No student action.**`
- [ ] Every assessed interaction has exactly `* **Remediation:** Pipeline` — no inline scripts
- [ ] Every MC interaction has Answer Rationale with ALL options explained (including each distractor)
- [ ] Multi-step interactions use sub-numbering (a/b/c) with per-sub-part fields
- [ ] All Visual: lines pass the Visual: Completeness Checklist (Toy+Mode, Orientation, Data, State, Interaction type, Visibility)
- [ ] No ad-hoc field names (no `[System Action]`, `Guide (continuing)`, `Rationale for No Student Action`, etc.)
- [ ] Annotations use `>` blockquote format AFTER the interaction block, not as fields within it
- [ ] System-driven interactions use Pattern 3 specification table format
- [ ] Think-aloud demonstrations use Pattern 4 with tags inside a single Guide field

### **Phase Checklists**

- [ ] Verification Checklists present for Warmup, Exit Check, and Synthesis  
- [ ] Incomplete Script Flags and Success Criteria present in Lesson (§1.7.4, §1.7.5)  
- [ ] KDD Summary present (§1.10) with all significant decisions documented  
- [ ] Practice Phase Inputs present if Practice Phase is generated (§1.8.5)

### **Content Quality**

- [ ] No student-facing dialogue references "Module X" numbers
- [ ] No authored remediation dialogue (all remediation is `Pipeline` — no inline scripts, no L-M-H qualifiers)
- [ ] Misconceptions use global IDs from database
- [ ] Session-relative language throughout ("last time/this time," NOT "yesterday/today")
- [ ] Interaction block self-check passed on 3 random interactions (see QUICK REFERENCE)

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

### Formatting Rules (ENFORCED)

1. **Header format:** H3 Markdown header (`### Interaction [ID]: [Title] [TYPE LABEL]`). Not bold text, not H2, not H4.
2. **Field format:** Every field is a **single bullet line** starting with `* **Field Name:**` followed by the value on the same line. Do NOT promote fields to standalone bold headers with content as a separate paragraph below. Do NOT split a single field across multiple bullets.
3. **Field order:** Purpose → Visual → Guide → Prompt → Student Action → Options (if MC) → Correct Answer → Answer Rationale (if MC) → On Correct → Remediation. Do not skip fields; do not reorder.
4. **No ad-hoc fields:** Only the fields listed below are valid interaction fields. Do NOT invent new fields like `[System Action]`, `Rationale for No Student Action`, `Guide (continuing)`, etc. If you need to express something the template doesn't cover, use a **Design Note** annotation after the block.
5. **Annotations are blockquotes, not fields:** Use `> **Design Note:**` format, placed after the interaction block and a `---` separator. Not as bullet fields within the block.

### Pattern 1 — Full Interaction (Student Action)

```
### Interaction [ID]: [Title] [TYPE LABEL]

* **Purpose:** [What this interaction accomplishes]
* **Visual: [Toy Name] ([Mode]).** [Orientation]. [Data/content]. [Scaffold state]. [Interaction type]. [Visibility flags].
* **Guide:** "[Teaching + instruction dialogue. Mark NEW and STATUS-CHANGE vocabulary terms with [vocab]term[/vocab] from introduction/formalization through end of module. Do NOT tag established terms from prior modules.]"
* **Prompt:** "[Standalone written instruction]"
* **Student Action:** [MC selection / click-to-set / drag-to-place / hover-and-click]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer]
* **Answer Rationale:** [MC only — REQUIRED for every MC interaction, no exceptions]
  - [Correct] = Correct ([why])
  - [Distractor] = [Misconception/error type]
* **On Correct:** "[Feedback. Use [vocab]term[/vocab] markup for NEW/STATUS-CHANGE vocabulary terms only. No tags on established terms from prior modules.]"
* **Remediation:** Pipeline
```

### Pattern 2 — Teaching-Only (No Student Action)

```
### Interaction [ID]: [Title] [TYPE LABEL]

* **Purpose:** [What this accomplishes]
* **Visual: [Toy Name] ([Mode]).** [State]
* **Guide:** "[Dialogue]"
* **No student action.**
```

### Pattern 3 — System-Driven Activity

```
### Interaction [ID]: [Title] [TYPE LABEL]

* **Purpose:** [What this accomplishes]
* **Visual: [Toy Name] ([Mode]).** [Initial state]

| Parameter | Specification |
|---|---|
| **System Action** | [What the system does] |
| **Duration** | [Estimated seconds] |
| **Student Role** | [Observe / Confirm / Interact] |
| **Visual State Change** | [Start state → End state] |

* **On Complete:** "[Guide dialogue after system action finishes]"
* **No student action.** (Or Pattern 1 fields if student responds after system action.)
```

> **Design Note:** [Why Patterns 1/2 don't apply]

### Pattern 4 — Think-Aloud Demonstration

```
### Interaction [ID]: [Title] [WORKED EXAMPLE]

* **Purpose:** [What this demonstrates]
* **Visual: [Toy Name] ([Mode]).** [State]
* **Guide:** "[PLANNING] First, I need to... [ATTENTION] I'm looking at... [SELF-CHECK] Does that match? Yes, because..."
* **No student action.**
```

Note: The think-aloud tags (`[PLANNING]`, `[ATTENTION]`, `[SELF-CHECK]`) go INSIDE a single Guide field. Do not split Guide into multiple bullets. Do not create a separate `[Guide_Think_Aloud]` field.

### Annotations (appear AFTER an interaction block, not as fields within it)

Format: blockquote with `>` prefix, after a `---` separator.

```
---

> **Design Note:** Explains a non-obvious design choice for future developers
> **Voice Note:** Script-writing guidance for tone/delivery
> **Scaffolding Note:** Explains how scaffolding changes across a sequence
> **Remediation Note:** Contextual hint for the Remediation Pipeline
> **Connection:** Names the principle a task demonstrates (Synthesis phase)
```

### Interaction Block Self-Check

Before Gate 2, pick 3 interactions at random and verify each one against this checklist:

- [ ] Header is `### Interaction [ID]: [Title] [TYPE LABEL]`
- [ ] Every field is `* **Field:** value` on one line (not field-as-paragraph)
- [ ] Field order matches spec: Purpose → Visual → Guide → Prompt → Student Action → Correct Answer → Answer Rationale → On Correct → Remediation
- [ ] Visual line has all required sub-components (see Visual: Completeness Checklist below)
- [ ] MC interactions have Answer Rationale with every option explained
- [ ] Remediation is exactly `Pipeline` — no inline scripts, no intensity qualifiers
- [ ] Annotations use `>` blockquote format after the block, not as fields within
- [ ] No ad-hoc field names
- [ ] Prompt field contains only the student-facing instruction — answer choices live in Options, not in the Prompt text
- [ ] NEW and STATUS-CHANGE vocabulary terms marked with `[vocab]term[/vocab]` in Guide and On Correct fields (from introduction/formalization through end of module). Established terms from prior modules have NO `[vocab]` tags.

---

## **QUICK REFERENCE: VISUAL: LINE FORMAT**

The Visual: line tells the system what to render. It is a **single bullet field** starting with `* **Visual: [Toy Name] ([Mode]).**` — all sub-components on one continuous line (or wrapped naturally within the single bullet). Do NOT promote Visual to a standalone paragraph.

Required sub-components:

```
* **Visual: [Toy Name] ([Mode if applicable]).** [Orientation]. [Data/Content summary]. [Pre-completion/scaffold state]. [Interaction type]. [Visibility flags for paired elements].
```

| Sub-component | Example | When Required |
| :---- | :---- | :---- |
| **Toy Name + Mode** | `Grid Rectangles (Dimensions-only mode)` | Always |
| **Orientation** | `Horizontal` / `Vertical` | Whenever toy has orientation |
| **Data/Content summary** | `3 cm × 8 cm rectangle` | Always |
| **Pre-completion state** | `Partial grid: first row + first column visible.` | When partially pre-filled |
| **Interaction type** | `Click-to-set` / `Drag-to-place` / `MC selection` | When student manipulates the toy |
| **Visibility flags** | `Equation Builder visible.` / `Data Table not visible.` | When paired elements exist |

### Visual: Completeness Checklist

Every Visual: line must pass this checklist. If a sub-component is intentionally omitted, the line is incomplete.

- [ ] **Toy Name + Mode** present? (Not just toy name — include the mode if the toy has modes)
- [ ] **Orientation** present? (Required whenever the toy can be horizontal or vertical)
- [ ] **Data/Content** present? (What specific values, figures, or content is displayed?)
- [ ] **Scaffold state** present? (Full grid / partial grid / dimensions only / pre-filled / empty)
- [ ] **Interaction type** present? (How does the student physically interact — click, drag, select?)
- [ ] **Visibility flags** present? (Are there paired elements? Which are visible/hidden?)

**Anti-patterns:**
- `* **Visual:** Same L-shape from W.4` — not self-contained. Every Visual: line must be interpretable without reading prior interactions.
- `* **Visual:** Grid Rectangles: 2×4 rectangle` — missing Mode, Orientation, Interaction type, Visibility.
- Promoting Visual to a multi-line paragraph with prose description — keep it structured on one bullet line.

