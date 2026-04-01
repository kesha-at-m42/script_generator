# Word Problems

Category: Unit 1
Created: February 26, 2026 6:21 PM
Status: Initial Spec Draft

---

---

>
>
>
> **WHAT:** A screen-level container that composes a text stem, optional visual support, and a hosted response mechanism into a coherent problem-solving interaction. Word Problems is not itself a toy or response component — it is the orchestration layer that arranges domain toys (Bar Graphs, Arrays, Equal Groups), response components (Response Input, Fill-in-the-Blank, Equation Builder), and Guide dialogue into a structured problem-solving experience. For multi-step problems, it manages chained submission sequences where each step's result feeds into the next.
>
> **WHY:** Mathematical problem-solving requires students to integrate reading comprehension, information extraction, operation selection, and computation into a single coherent task. The Word Problem container ensures this integration happens in a consistent, scaffoldable way across all curriculum units. By separating the *container* (how a problem is presented and sequenced) from the *response mechanism* (how the student answers) and the *visual support* (what the student sees), each component can evolve independently while the problem-solving experience remains coherent. The multi-prompt architecture is particularly critical — it enables prompt-level remediation for multi-step problems (catching errors at Prompt 1 before they propagate to Prompt 2) while the single-prompt mode builds toward STAAR test independence where students must plan and execute without scaffolding.
>

## Shape 🟡

### Screen Layout Zones

The Word Problem container divides the screen into functional zones. Not all zones are active for every problem, and zones may activate or deactivate during the interaction lifecycle.

📷 *UX: Add wireframe showing all zones in both configurations*

![image.png](image.png)

![image.png](image%201.png)

![image.png](image%202.png)

![image.png](image%203.png)

![image.png](image%204.png)

**Zone 1 — Context Visual (top or left):**
**Data Source Visuals** — Problem is unsolvable without this visual.

Any domain toy that contains information the student must extract to
answer the question. The toy provides DATA, not just illustration.

Characteristics:

- Contains values, relationships, or structures not fully stated in the stem
- Student must read, measure, count, or extract from the visual
- Removing the visual makes the problem unsolvable
- May contain extraneous information (tests filtering)

Examples by unit documented in Tool Flow / Starter Packs.

---

**Illustrative Context Visuals** — Stem text is self-sufficient;
visual reinforces comprehension.

Any domain toy that makes the problem's structure concrete for visual
learners. The stem carries all solvability-critical information.

Characteristics:

- Student COULD solve from text alone
- Visual makes structure concrete (groupings, arrangements, spatial layout)
- Removing the visual doesn't make the problem unsolvable, but may
reduce accessibility
- Visual matches the stem exactly — reinforces, doesn't extend

Examples by unit documented in Tool Flow / Starter Packs.

**Zone 2 — Problem Stem (persistent content area):**
The persistent narrative context for the problem. This is NOT Guide dialogue (which cycles one line at a time in the top bar) and NOT the Prompt (which changes with each question). The stem establishes the situation and stays visible while multiple prompts cycle underneath it. The Guide may read the stem aloud, but the text persists on screen so the student can re-read it while working. For single-prompt problems, the stem may include the question itself. For multi-prompt problems, the stem is the shared story — individual questions appear as separate prompts below.

**Zone 3 — Response Area (bottom):**
The hosted response component — Response Input (MC), Fill-in-the-Blank, Equation Builder, or other input mechanism. This zone changes content between prompts.

**Zone 4 — Prompt Progress (conditional):**
For multi-prompt interactions only. Shows which prompt the student is on and, for chained patterns, accumulates completed results. May appear as a progress indicator ("Question 2 of 3"), accumulated calculations from prior prompts, or both. For shared-stem patterns, this may simply indicate position ("2 of 3") without displaying prior results.

**Zone 5 — Scaffolding Visual (conditional, dynamic)** Reasoning tools, not data sources.

Any domain toy that helps students UNDERSTAND problem structure or
REASON through solutions. Never contains data required to solve the
problem. Always removable without making the problem unsolvable.

Injection patterns:

- Pre-loaded: Appears at problem presentation (early instruction)
- Remediation-injected: Appears after incorrect submission (medium/heavy)
- Step-triggered: Appears at a specific chained prompt
- Absent: No scaffolding visual (late practice, exit check, STAAR prep)

Fading pattern: Pre-loaded → remediation-only → absent

Specific toy assignments per unit documented in Tool Flow / Starter Packs.

**Zone 1 vs. Zone 5 — Critical Distinction:**

|  | Zone 1: Context Visual | Zone 5: Scaffolding Visual |
| --- | --- | --- |
| **Purpose** | Provides the DATA the problem asks about | Provides a REASONING TOOL to understand the problem |
| **Lifecycle** | Static — appears at problem start, persists | Dynamic — may appear at start, appear during remediation, or never appear |
| **Example** | Bar graph showing field trip votes | Tape diagram showing "combine then compare" structure |
| **Student interaction** | Read/extract values | Observe structure; may interact if toy allows |
| **Required** | For visual-context problems (optional for pure text) | Never required — always optional scaffolding |
| **Fades with mastery** | No — the graph IS the problem | Yes — scaffolding visuals are removed as students internalize the reasoning |

### Problem Stem

The persistent text block that establishes the narrative context. One of three text layers on a Word Problem screen:

📷 *UX: Add visual showing all three text layers and their lifecycle*

**Three Text Layers:**

| Layer | Location | Lifecycle | Example |
| --- | --- | --- | --- |
| **Guide dialogue** | Top bar (speech bubble with avatar) | Ephemeral — cycles one line at a time; may read stem aloud or provide coaching | "Read the problem carefully. What do you notice?" |
| **Stem** | Content area, below Guide bar | Persistent — stays visible across all prompts | "A store has 45 toy cars in 5 different colors. There are the same number of cars in each color." |
| **Prompt** | Below stem, above response area | Changes per question — each prompt is a new question about the same stem | "Which equation could be used to find the number of cars in each of the 5 colors?" |

**For single-prompt problems:** Stem and prompt may merge into a single text block (the stem IS the question). No visible separation needed.

**For multi-prompt problems:** Stem and prompt are visually distinct. Stem stays fixed; prompt text swaps as each new question appears.

**Stem components:**

- **Narrative setup:** 1–3 sentences establishing the situation
- **Key data (optional):** Numbers, constraints, or relationships embedded in text. For pure-text problems (no context visual), ALL solvability-critical data lives here.
- **Expression or equation (optional):** May include "8 × 2" or "45 ÷ 5 = ?" as part of the narrative

**Rendering requirements:**

- Grade-appropriate font size and line spacing
- Clear visual separation between stem and prompt when both are present
- Stem never scrolls out of view while prompt/response area is active
- Expression/equation content within the stem should render with math formatting (not plain text)

### Result Accumulator (Chained Pattern Only)

A persistent display showing completed prompt results that carries forward into subsequent prompts. Only relevant for chained multi-prompt patterns where later prompts depend on earlier results. Not used for shared-stem patterns (where prompts are independent).

📷 *UX: Add visual of result accumulator showing completed Prompt 1 feeding into Prompt 2*

**Example progression:**

- Prompt 1 complete: "Scooters and skateboards combined = 50" (displayed, locked)
- Prompt 2 active: "How many more is bikes than 50?" (new prompt in response area)

## Properties 🟡🔵

### Submission Modes

| Mode | Description | Prompts | Remediation | When Used |
| --- | --- | --- | --- | --- |
| **Single prompt** | Stem + one question, one response | 1 | After answer | Simple single-step problems |
| **Multi-prompt** | Stem persists; multiple prompts appear sequentially underneath | 2–5 | After each prompt independently | Multi-step problems; passage-style items; complex problem-solving |

**Multi-prompt has two conceptual patterns that share the same implementation:**

### Multi-Prompt Patterns

**Pattern A: Chained Steps** — Sequential parts of ONE problem where earlier results inform later steps.

| Property | Description |
| --- | --- |
| **Dependency** | Prompt 2 depends on Prompt 1's result. Getting Prompt 1 wrong makes Prompt 2 harder or impossible without correction. |
| **Result carry-forward** | Completed prompt results display in the Result Accumulator and persist through subsequent prompts. |
| **Error handling** | Student must get (or be given) the correct Prompt 1 answer before attempting Prompt 2. |
| **Curriculum purpose** | Scaffold multi-operation problem-solving; enable step-level remediation that catches errors before they propagate. |
| **Example** | Stem: "The graph shows votes for field trips." → Prompt 1: "What should we find first?" → Prompt 2: "What's museum and farm combined?" → Prompt 3: "How many fewer than zoo?" |

**Pattern B: Shared-Stem Prompts** — Independent questions that reference the same narrative context.

| Property | Description |
| --- | --- |
| **Dependency** | None. Each prompt is independently answerable. Student can get Prompt 1 wrong and Prompt 3 right. |
| **Result carry-forward** | Not needed (no dependency), but prior answers may remain visible. |
| **Error handling** | Standard per-prompt remediation. Failure on one prompt doesn't affect others. |
| **Curriculum purpose** | Explore multiple facets of a single context; match STAAR passage-style items; build transfer within a scenario. |
| **Example** | Stem: "A store has 45 toy cars in 5 different colors. There are the same number in each color." → Prompt 1: "Which equation could find the number per color?" → Prompt 2: "How many cars are in each color?" → Prompt 3: "A student says there are 10 of each color. Is the student correct?" |

**Implementation note:** Both patterns use the same underlying mechanism — persistent stem, sequential prompts with independent response areas. The distinction is conceptual and documented in the starter pack so curriculum authors signal intent. The system does not need to differentiate technically, but starter pack authors should tag each multi-prompt interaction as `chained` or `shared_stem` for clarity.

**Scaffolding intersection:** Chained steps naturally fade into shared-stem prompts. Early instruction uses chained (dependent steps with carry-forward) for the same problem type that later becomes shared-stem (independent questions, no scaffolding) or eventually single-prompt (student plans all steps internally).

**Note:** Chained and shared-stem examples in this spec are illustrative,
not exhaustive. Each unit's Tool Flow specifies which problems use which
pattern. The container supports any sequencing — curriculum determines
the specific deployment.

### Prompt Types

Within either multi-prompt pattern, each prompt serves a function:

| Prompt Type | Purpose | Typical Response Mechanism | Example |
| --- | --- | --- | --- |
| **Strategy identification** | Student identifies what to do first | Response Input (MC) | "What should we find first?" → [Add museum and farm / Compare zoo to museum / Add all five] |
| **Intermediate computation** | Student computes a partial result | Response Input (MC) or Equation Builder | "What's the combined total of museum and farm?" → [10 / 30 / 40 / 45] |
| **Final computation** | Student uses prior information to compute the answer | Response Input (MC) or Equation Builder | "How many fewer is 40 than 45?" → [85 / 45 / 40 / 5] |
| **Operation selection** | Student identifies the needed operation | Response Input (MC) | "Now what?" → [Add them / Find the difference / We're done] |
| **Interpretation** | Student draws a conclusion from the data | Response Input (MC) or Fill-in-the-Blank | "Is the student correct? Explain why." → [Yes, because... / No, because...] |
| **Expression/equation matching** | Student matches context to notation | Response Input (MC) or Equation Builder | "Which equation could be used to find the number of cars?" |

**Sequencing rules (chained pattern):**

- Strategy identification, when present, is always Prompt 1
- Each prompt must be answerable given prior prompt results
- The system carries forward completed results visually (Result Accumulator)

**Sequencing rules (shared-stem pattern):**

- Prompts may appear in any pedagogically appropriate order
- No dependency between prompts — each is self-contained
- Prompts typically progress from easier to harder (but not required)

### Scaffolding Progression

The same problem type moves through scaffolding levels across a module's activities. The fade path is: chained → shared-stem → single-prompt.

| Level | Pattern | Prompts | Guide Support | When Used |
| --- | --- | --- | --- | --- |
| **Full scaffolding** | Chained | Explicit per-prompt guidance ("What should we find first?") | Full narration; strategy naming; step transitions | First exposure to problem type |
| **Reduced scaffolding** | Chained | First prompt guided, subsequent prompts lighter | Lighter narration; less hand-holding | Mid-lesson guided practice |
| **Minimal scaffolding** | Chained | Prompts still sequential but no explicit strategy cues | Prompts presented without "What should we find first?" | Late lesson / early Practice |
| **Independent multi-prompt** | Shared-stem | Independent questions, no dependency | No scaffolding prompts; questions explore the context | Mid-Practice; STAAR-style items |
| **Fully independent** | Single-prompt | One question, one response | No prompts; no step separation; student plans internally | Late Practice; Exit Check; STAAR prep |

### Context Visuals (Zone 1)

Toys that provide CONTEXT for the problem. Static for the life of the problem. Two sub-types based on how essential the visual is:

**Data Source Visuals — Problem is unsolvable without this visual.** The stem references information that lives only in the visual. Student must extract values, read axes, or identify categories from the toy to answer the question.

| Data Source Toy | What Student Extracts | Example Stem |
| --- | --- | --- |
| **Bar Graph (reading mode)** | Bar heights / values at scale intervals | "How many more votes did pizza get than tacos and salad combined?" |
| **Data Table** | Numeric values by category | "Use the table to find which stadium has the most seats." |
| **Picture Graph** | Symbol counts × scale | "Each symbol = 5. How many more chose cats?" |
| **Composite data display** | Values from graph + table together | "The graph shows votes. The table shows costs. How much would the winning choice cost?" |

**Illustrative Context Visuals — The stem text is self-sufficient; the visual reinforces comprehension.** Student COULD solve from text alone, but the visual makes the structure concrete and supports students who process visually.

| Illustrative Context Toy | What It Shows | Example Stem |
| --- | --- | --- |
| **Equal Groups with Pictures** | The grouping structure described in text | "There are 3 bags with 5 apples each." + image of 3 bags with 5 apples |
| **Arrays with Pictures** | The row/column arrangement described in text | "The muffin tin has 4 rows of 6." + image of 4×6 array |
| **Image (static)** | Real-world context | STAAR-style photo of the scenario |
| **No visual** | N/A — pure text problem | "Maria has 4 boxes of crayons. Each box has 8 crayons..." |

**Lifecycle difference:** Data Source visuals are ALWAYS present and persistent — removing them makes the problem unsolvable. Illustrative Context visuals are pedagogically valuable but could theoretically be removed at high independence levels (the text carries the information). This removal is a scaffolding decision, not a constraint.

**Visual-stem relationship:** Data Source visuals may contain more information than needed — extraneous data in a graph with 5 categories where only 2 are relevant is intentional (tests information filtering). Illustrative Context visuals should match the stem exactly — they reinforce, not extend.

### Scaffolding Visuals (Zone 5)

Toys that help students REASON about the problem structure. Dynamic — may be pre-loaded, remediation-injected, or absent. Never contain data required to solve the problem. Always removable without making the problem unsolvable.

| Scaffolding Visual Toy | Reasoning Purpose | Injection Trigger | Example |
| --- | --- | --- | --- |
| **Tape/Bar Diagram** | Visualize part-whole relationships in multi-step problems | Pre-loaded during instruction; remediation-injected for Medium/Heavy | Two-step problem: tape shows "combined total" segment vs. comparison target |
| **Equal Groups with Pictures** | Make multiplicative structure visible when student doesn't extract it from text | Remediation-injected when student misidentifies operation or structure | Text says "4 shelves with 6 books each" → student adds instead of multiplies → equal groups visual appears showing 4 groups of 6 |
| **Number Line** | Show magnitude relationships or operation sequences | Remediation-injected for comparison errors | Student miscalculates "how many more" → number line appears showing the jump from 25 to 40 |
| **Arrays with Pictures** | Show row/column structure for arrangement problems | Pre-loaded for early instruction; removed at independence | Array visual accompanies "rows of" language to reinforce structure |
| **Equation Builder (observation mode)** | Show equation structure for reference | Pre-loaded or remediation-injected | Display `___ × ___ = ___` template alongside word problem to scaffold notation |

**Injection lifecycle:**

| Timing | Behavior | When Used |
| --- | --- | --- |
| **Pre-loaded** | Scaffolding visual appears with the problem at presentation | Early instruction — students are learning the problem type; visual models the reasoning approach |
| **Remediation-injected** | Scaffolding visual appears AFTER incorrect submission | Medium/Heavy remediation — student needs structural support they didn't get at presentation |
| **Step-triggered** | Scaffolding visual appears at a specific chained prompt | Mid-problem scaffolding — e.g., tape diagram appears at Prompt 2 to show how intermediate result connects to final question |
| **Absent** | No scaffolding visual used | Late Practice, Exit Check, STAAR prep — students reason without visual scaffolding |

**Fading pattern:** Pre-loaded scaffolding visuals are progressively removed across a module's activities:

- Early activities: Scaffolding visual always present (pre-loaded)
- Mid activities: Scaffolding visual available only on remediation (not pre-loaded)
- Late activities: No scaffolding visual (full independence)

This fading is configured per-interaction in the starter pack — the Word Problem container supports all states; curriculum determines which state each problem uses.

**Critical constraint:** A scaffolding visual should NEVER contradict or conflict with the Context Visual. If Zone 1 shows a bar graph and Zone 5 shows a tape diagram, they must represent the same data/relationships. The scaffolding visual re-represents the context data in a more structurally transparent way — it doesn't introduce new information.

### State Properties

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Presenting** | Stem and visual displayed; response area not yet active | Stem and visual render; response zone may be empty or grayed until Guide finishes setup dialogue |
| **Active** | Current prompt and response area are live; student can interact | Stem persists; prompt visible; response component in default state |
| **Prompt complete (multi-prompt)** | Current prompt submitted and evaluated; result locked | For chained: result displays in Accumulator, next prompt loads. For shared-stem: next prompt loads, prior answer may or may not remain visible |
| **All prompts complete** | Final prompt submitted and evaluated | Full results visible; feedback states shown; system advances |
| **Disabled** | Interaction paused during Guide dialogue or feedback | Response area locked; stem and visual remain visible |

## Allowed Student Actions 🟡🔵

### Read Problem Stem

**Description:** Student reads the word problem text and processes the question.

**Behavior:** Stem is displayed with visual support. Student reads at their own pace. Guide may read the stem aloud (audio) while text is displayed. No interaction required — this is a comprehension step.

**Purpose:** Ensure the student understands what is being asked before responding.

---

### Interact with Context Visual (Zone 1)

**Description:** Student interacts with the domain toy as needed to extract information for the problem.

**Behavior:** Depends on the hosted toy's allowed actions. For bar graphs in reading mode, this may be observation only. For equal groups, it may include clicking to highlight groups. The Word Problem container does not add or remove any toy actions — the toy behaves according to its own spec.

**Purpose:** Information extraction. The student reads values, identifies structures, or observes relationships needed to answer the question.

---

### Observe Scaffolding Visual (Zone 5)

**Description:** Student views the scaffolding visual that models the problem's reasoning structure.

**Behavior:** Primarily observational — Guide directs attention to the scaffolding visual ("Look at the tape diagram. See how the two parts combine?"). Student may interact if the scaffolding toy supports it (e.g., clicking segments of a tape diagram), but interaction is secondary to observation. When remediation-injected, the Guide introduces it: "Let me show you something that might help."

**Purpose:** Structural understanding. The student sees the reasoning pathway, not just the data.

---

### Respond via Hosted Response Component

**Description:** Student uses the response mechanism (MC, FITB, Equation Builder) to answer the current step.

**Behavior:** Standard behavior of the hosted component. Response Input follows its spec; Fill-in-the-Blank follows its spec; Equation Builder follows its spec. The Word Problem container does not modify response component behavior.

**Purpose:** Capture the student's answer for the current step.

---

### Review Prior Prompt Results (Chained Pattern)

**Description:** Student can see results from completed prompts in the Result Accumulator.

**Behavior:** Prior prompt results are displayed and locked (not editable). Student can reference them while working on the current prompt. Results remain visible through all subsequent prompts.

**Purpose:** Reduce working memory load. Students don't need to remember intermediate calculations — they're displayed.

## Teaching / Remediation Actions 🟡🔵

Word Problems is a container. Teaching and remediation actions are primarily delivered by the Guide and by the hosted toys/response components according to their own specs and the Remediation System FDB.

### Prompt-Level Remediation (Chained Pattern)

**Description:** When a student answers a chained prompt incorrectly, remediation occurs at that prompt before advancing. The student does not proceed to Prompt 2 with a wrong Prompt 1 result.

**Purpose:** Prevent error propagation. A wrong intermediate calculation would make all subsequent prompts unsolvable, creating frustration without learning.

**Triggers:** Incorrect submission at any chained prompt.

**Behavior:**

1. Student submits incorrect answer for current prompt
2. Response component shows incorrect state (per its spec)
3. Guide delivers prompt-specific remediation feedback
4. Student retries the current prompt (with or without Option Elimination, per response component configuration)
5. On correct: result locks, system advances to next prompt
6. On exhausted retries: system provides correct answer, locks result, advances (student needs the correct intermediate value to attempt subsequent prompts)

**Critical design requirement:** If a student exhausts retries on Prompt 1 and the system provides the correct answer, Prompt 2 must still be attempted. The student should not be skipped past the remaining problem — they may understand Prompt 2 even if Prompt 1 failed. The provided Prompt 1 result enables them to try.

📷 *UX: Add visual showing prompt-level remediation flow*

---

### Prompt-Level Remediation (Shared-Stem Pattern)

**Description:** When a student answers a shared-stem prompt incorrectly, remediation addresses that prompt independently. Other prompts in the sequence are unaffected.

**Purpose:** Each question stands alone. Failure on one doesn't imply failure on others.

**Triggers:** Incorrect submission on any shared-stem prompt.

**Behavior:** Standard remediation per Remediation System FDB. No result carry-forward needed. System advances to next prompt regardless of outcome.

---

### Single-Prompt Remediation

**Description:** When a student answers a single-prompt problem incorrectly, remediation addresses the complete problem.

**Purpose:** Diagnose where the student's reasoning broke down without the scaffolding of chained prompts.

**Triggers:** Incorrect submission on single-prompt problem.

**Behavior:** Standard remediation per Remediation System FDB. Guide may retrospectively walk through the steps ("Let's think about this. What should we find first?"), effectively converting the problem into a teaching moment even though it was delivered as single-prompt.

---

### Highlight Relevant Visual Information

**Description:** Guide or system highlights specific elements of the Context Visual (Zone 1) to direct attention to relevant data.

**Purpose:** Help students filter extraneous information and focus on what the problem asks about.

**Triggers:** Guide-directed during instruction or remediation. May be automatic during prompt transitions (e.g., highlighting the two bars being combined in Prompt 1).

**Behavior:** Uses the hosted toy's highlighting/emphasis capabilities (bar highlight, group highlight, etc.) — the Word Problem container triggers the action but doesn't implement it.

---

### Inject Scaffolding Visual

**Description:** A reasoning-support toy appears in Zone 5 that was not present at problem presentation. This is the primary mechanism for visual remediation in word problems.

**Purpose:** When verbal remediation alone isn't enough, provide a structural visual that makes the problem's reasoning pathway visible. The scaffolding visual re-represents the same information from the Context Visual (or stem text) in a more transparent format.

**Triggers:** Medium or Heavy remediation tier (per Remediation System FDB). Configured per-interaction — the starter pack specifies WHICH scaffolding toy to inject and WHAT configuration to use.

**Behavior:**

1. Student submits incorrect answer → feedback displays → Guide begins remediation dialogue
2. Guide introduces the scaffolding visual: "Let me show you something that might help."
3. Zone 5 activates — scaffolding toy renders with animation/transition
4. Guide narrates the scaffolding visual, connecting it to the problem: "See how these two parts combine to make this total? That's what the problem is asking you to find first."
5. Student retries the problem with the scaffolding visual now visible
6. Scaffolding visual persists through retry and any subsequent steps

**Configuration per interaction:**

- `scaffolding_visual: null` — no scaffolding available (late Practice, STAAR prep)
- `scaffolding_visual: { toy: "tape_diagram", config: {...}, trigger: "preloaded" }` — appears at presentation
- `scaffolding_visual: { toy: "equal_groups", config: {...}, trigger: "remediation", tier: "medium" }` — appears only on Medium+ remediation
- `scaffolding_visual: { toy: "number_line", config: {...}, trigger: "remediation", tier: "heavy" }` — appears only on Heavy remediation

**Multiple scaffolding levels:** A single problem can have BOTH a medium-tier and a heavy-tier scaffolding visual configured. Medium might inject a tape diagram; if the student still fails, Heavy replaces it with a more concrete visual (equal groups with pictures). The progression mirrors the remediation tier escalation.

📷 *UX: Add visual showing scaffolding injection sequence — before incorrect, during remediation, after injection*

---

### Display Intermediate Calculation

**Description:** System displays the result of a completed prompt as a persistent visual element.

**Purpose:** Reduce working memory load during chained multi-prompt problems. Students see "Scooters + Skateboards = 50" while working on the comparison prompt.

**Triggers:** Automatic after a chained prompt is completed correctly.

**Behavior:** Intermediate result appears in the Result Accumulator zone. May include the operation performed ("30 + 20 = 50") or just the result ("Combined total: 50"). Persists through all subsequent prompts.

📷 *UX: Add visual showing intermediate calculation display*

## Constraints 🟡

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| One problem per screen | No side-by-side or stacked problems |
| Stem always visible | Stem text never scrolls out of view while prompt/response area is active |
| Context visual persists across prompts | The Zone 1 toy stays visible through all prompts — it's the data reference |
| Scaffolding visual persists once injected | Once Zone 5 activates (whether pre-loaded or remediation-injected), it stays visible through remaining prompts and retries |
| Prompt results are immutable (chained) | Completed chained prompt results cannot be changed (prevents backtracking that would invalidate subsequent prompts) |
| Response component is interchangeable | Any response mechanism can be hosted — the container doesn't assume MC. Different prompts within the same stem can use different response types. |
| Prompts advance linearly | No branching, no skipping prompts, no reordering |
| Mode is fixed per interaction | An interaction is single-prompt or multi-prompt for its entire lifecycle; doesn't change mid-problem |
| Scaffolding visual never introduces new data | Zone 5 re-represents Zone 1 / stem information; it never adds solvability-critical information that wasn't already available |

### Content Constraints

| Property | Constraint | Notes |
| --- | --- | --- |
| Stem reading level | Grade-appropriate vocabulary and sentence structure | Follows module vocabulary architecture — only uses terms that have been taught |
| Stem length | 1–4 sentences typical | Narrative setup (1–3 sentences). May include expression or equation. |
| Prompts per stem | 1–5 | Single-prompt (1) is most common. Chained typically 2–3. Shared-stem can go to 5 for passage-style items. |
| Operations per problem | 1–2 for Grade 3 (per 3.OA.D.8) | Two-step is the ceiling; three-operation problems excluded |
| Visual data scope | 3–5 categories for graphs; 2–5 groups for equal groups | Enough extraneous data to require filtering; not so much as to overwhelm |
| Answer format | Always via hosted response component | No free-form text entry; no verbal responses |
| Mixed response types | Allowed across prompts within one stem | Prompt 1 could be MC, Prompt 2 could be Equation Builder |
| **NOT:** Three or more operations | Never for Grade 3 | Beyond standard scope |
| **NOT:** Problems requiring estimation | Never | All values readable precisely from visuals |
| **NOT:** Stem text that changes between prompts | Never | Stem is static; only the prompt and response area change |

Every prompt has a DETERMINISTIC correctness evaluation. Three patterns:

1. **Single correct answer** — Exactly one option/response is correct.
(Most common: computation, identification, comparison)
2. **Correct answer set** — A defined set of correct responses; student
must identify all/some. Correctness is per-option, evaluated against
a known set. (Multi-select MC, factor-pair enumeration)
3. **Validation-rule correct** — Any response satisfying a stated rule
is correct. The system validates against the rule, not against a
pre-defined answer list. (Design problems: "any factor pair where
product = 24"; strategy problems: "any valid first step"; open
production tasks)

All three patterns produce unambiguous system evaluation — the system
always knows whether the student's response is correct. What differs
is whether the correct response(s) are enumerated in advance or
evaluated dynamically.

**NOT:** Prompts where correctness is subjective or unevaluable by the
system. Every response the system accepts must be programmatically
validatable.

### Visual / Teaching Constraints

| Feature | Constraint | Notes |
| --- | --- | --- |
| Extraneous data | Graphs should include categories NOT needed for the answer | Tests information filtering; matches STAAR format |
| Visual-stem alignment | Visual must contain all information needed to solve the problem | No information only available in a tooltip or hidden state |
| Prompt clarity (chained) | Each chained prompt must be answerable from available information | Prompt 2 can reference Prompt 1 results; it can't require information not yet provided |
| Distractor design | Distractors for each prompt are pedagogically intentional | Common errors: adding instead of comparing, stopping at intermediate result, using wrong values |
| Strategy language | Scaffolding phrases fade across activities | "What should we find first?" → no prompt → single-prompt |

### Problem Type Taxonomy

The following taxonomy captures the structural patterns used across curriculum units. This is the Layer 1 (core) taxonomy — each unit uses a subset.

**Single-Step Types:**

| Type | Structure | Operation | Example |
| --- | --- | --- | --- |
| **Direct reading** | Read a single value from visual | None (retrieval) | "How many voted for red?" |
| **Simple comparison** | Compare two values | Subtraction | "How many more cats than dogs?" |
| **Simple total** | Combine two values | Addition | "How many cats and dogs altogether?" |
| **Expression matching** | Match visual to symbolic notation | None (recognition) | "Which expression shows 3 groups of 4?" |
| **Structure identification** | Identify mathematical structure in context | None (recognition) | "How many groups? How many in each?" |

**Multi-Step Types:**

| Type | Structure | Operations | Example |
| --- | --- | --- | --- |
| **Combine then compare** | (A + B) − C | Add, then subtract | "How many more pizza than tacos and salad combined?" |
| **Combine then compare (flipped)** | C − (A + B) | Add, then subtract | "How many fewer tacos and salad combined than pizza?" |
| **Target minus combined** | Target − (A + B) | Add, then subtract | "100 people voted. How many more needed than A and B?" |
| **Compare two totals** | (A + B) − (C + D) | Add, add, then subtract | "How many more did A+B get than C+D?" (Practice only) |
| **Sum of multiple** | A + B + C + ... | Sequential addition | "How many total across all categories?" (Practice only) |

**Extending the Taxonomy:**
Unit-specific problem types are compositions of Layer 1 structural patterns,
documented in each unit's Tool Flow and Starter Packs — not in this spec.

If a new unit reveals a structural pattern not captured in Layer 1 (not just
new content in an existing pattern), add it to Layer 1 as a generalized type
with a content-neutral description. The test: "Could this pattern appear in
a different mathematical domain?" If yes, it's structural. If no, it belongs
in the unit documentation.

## Layout Constraints 🔵

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum instances | 1 Word Problem container per screen | One problem at a time |
| Context visual zone (Zone 1) position | Top or left (configurable) | Top for wide visuals (graphs); left for tall visuals (equal groups, arrays) |
| Scaffolding visual zone (Zone 5) position | Adjacent to context visual or between context and stem | Must not obscure stem or response area. UX determines optimal placement — may be beside Zone 1, below Zone 1, or in a collapsible panel |
| Stem zone position | Below visual(s) or right of visual(s) | Must remain visible during response |
| Response zone position | Bottom | Consistent position across all problem types |
| Result accumulator position | Between stem and response zones (chained only) | Grows as prompts complete |
| Can host (response) | Response Input (MC), Fill-in-the-Blank, Equation Builder, any response component | Container is response-mechanism agnostic |
| Can display (Zone 1) | Any domain toy as data source or illustrative context | Bar Graphs, Data Tables, Equal Groups, Arrays, Picture Graphs, static images |
| Can display (Zone 5) | Any domain toy as reasoning scaffold | Tape Diagrams, Equal Groups, Number Lines, Arrays, Equation Builder (observation) |
| Cannot contain | Another Word Problem container | No nesting |
| Zone 5 animation | Must have entry animation when remediation-injected | Scaffolding visual shouldn't "pop" — it should slide, fade, or expand into place so student registers the new element |

📷 *UX: Add layout diagrams for each configuration — especially Zone 1 + Zone 5 together*

**Common Layout Configurations:**

- **Graph problem (standard):** Bar Graph Zone 1 (top, full width) → Stem (middle) → MC response (bottom). No Zone 5.
- **Graph problem (chained):** Bar Graph Zone 1 (top, full width) → Stem (middle-left) → Result accumulator (middle-right) → MC response (bottom). No Zone 5.
- **Graph problem (with scaffolding):** Bar Graph Zone 1 (top-left) → Tape Diagram Zone 5 (top-right) → Stem (middle) → MC response (bottom). Zone 5 may be pre-loaded or injected.
- **Equal groups problem:** Equal Groups Zone 1 (top-left) → Stem (top-right) → Equation Builder response (bottom). No Zone 5.
- **Equal groups problem (remediation injection):** Equal Groups Zone 1 (top-left) → Stem (top-right) → [Student fails] → Number Line Zone 5 (middle, injected) → MC retry (bottom).
- **Pure text problem:** Stem (top, full width) → MC response (bottom). No Zone 1. No Zone 5.
- **Pure text problem (remediation injection):** Stem (top) → [Student fails] → Equal Groups Zone 5 (middle, injected) → MC retry (bottom). Zone 5 makes the text concrete.
- **STAAR format:** Static image Zone 1 (top-left) → Stem (top-right) → MC or FITB (bottom). No Zone 5 (independence).

## Tool to Schema Vocab Translation 🟣

*Engineering: Fill this table as schema is finalized.*

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
|  |  |  |

## Curriculum Animator Techs (CAT) 🟣

*Engineering: Add animation specifications, sequence events, GDScript references, and JSON schema examples here as implementation progresses.*

## Open Questions ⚪

- [ ]  **[UX]** Result Accumulator design: Text summary ("Combined total: 50"), equation display ("30 + 20 = 50"), or visual annotation on the graph itself (e.g., bracket over combined bars with "50" label)? Graph annotation is richest but hardest to implement.
- [ ]  **[UX]** Problem stem audio: Does Guide always read the stem aloud? Or only during instruction (not Practice/Exit Check)? Reading aloud supports struggling readers but adds time.
- [ ]  **[UX]** Stem + question separation: Is the question typographically distinct (bold, larger, different color)? Or is the entire stem rendered uniformly? STAAR uses uniform rendering — should we match that or scaffold differently?
- [ ]  **[UX]** Chained step transitions: Does the response area animate (slide, fade) between steps, or does it snap-change? Animation provides continuity; snap-change is faster.
- [ ]  **[UX]** Visual highlighting ownership: When the Word Problem container triggers a highlight on a hosted toy (e.g., "highlight the pizza and taco bars"), who controls the highlight — the container or the toy? Recommendation: container sends a signal, toy renders the highlight per its own spec.
- [ ]  **[Engineering]** Result carry-forward: How does Prompt 1's correct answer get injected into Prompt 2's text? Template variable substitution ("How many more is bikes than {prompt_1_result}?")? Or system assembles the prompt dynamically?
- [ ]  **[Engineering]** Exhausted retries in chained pattern: When system provides the correct Prompt 1 answer, how is this distinguished visually from a student-earned result? Different color/icon? Label "System provided"?
- [ ]  **[Curriculum]** Problem type taxonomy completeness: The Layer 1 taxonomy above covers Units 1 and partial Unit 4. Full extraction from Units 2–5 needed to confirm all structural patterns are captured. Plan: Use curriculum extraction workflow to process remaining unit PDFs.
- [ ]  **[Curriculum]** "What should we find first?" prompt: Should this always be the first prompt in chained patterns during instruction? Or can some chained problems skip strategy identification and go straight to intermediate computation? Current practice varies — M6 Activities 3–6 include it, Activities 7–9 don't.
- [ ]  **[Curriculum]** Single-prompt multi-step in Exit Check: M6 Exit Check uses chained. At what module/unit does Exit Check shift to single-prompt for multi-step problems?
- [ ]  **[Cross-Unit]** Scaffolding visual library: Which toys are confirmed available as Zone 5 scaffolding visuals? Tape Diagrams are not yet specced (Unit 3 introduces them). Number Lines may come from other units. Need cross-unit inventory of scaffolding-eligible toys.
- [ ]  **[UX]** Zone 5 placement when Zone 1 is a full-width graph: Does the scaffolding visual (e.g., tape diagram) appear below the graph, beside it (requiring graph to shrink), or in a slide-out panel? Full-width graphs leave no room for a side-by-side Zone 5.
- [ ]  **[UX]** Zone 5 remediation injection animation: How does the scaffolding visual enter? Slide from side? Fade in? Expand from a point? Needs to be noticeable (student should register something new appeared) but not jarring.
- [ ]  **[Engineering]** Zone 5 configuration in schema: Is the scaffolding visual config embedded in the problem schema (per-interaction), or defined at a higher level (per-module or per-remediation-tier) and referenced? Per-interaction is most flexible; per-module reduces redundancy.
- [ ]  **[Curriculum]** Scaffolding visual progression documentation: Should starter packs specify Zone 5 configuration for every interaction, or just for the first/last interaction in a scaffolding block (with "same as above" for middle interactions)?
- [ ]  **[Engineering]** Multiple scaffolding tiers: If Medium remediation injects a tape diagram and Heavy remediation injects equal groups, does the tape diagram get replaced or do both display? Recommendation: replace (one Zone 5 visual at a time) to avoid screen overload.

## JSON Schema Formatting 🟣

*Engineering: Add JSON schema examples here as implementation progresses.*
