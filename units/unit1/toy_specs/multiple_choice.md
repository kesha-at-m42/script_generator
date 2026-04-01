# Multiple Choice/Checkbox

Category: Unit 1
Created: February 26, 2026 4:54 PM
Status: Initial Spec Draft

---

---

> **WHAT:** A selection-based response system where students choose from 3+ pre-defined options displayed as clickable cards. Supports two selection modes: single-select (radio — choose one) and multi-select (checkbox — choose one or more). Options can contain text, equations, images, or extended passages. Layout adapts automatically based on option content length.
>
>
> **WHY:** Response Input is the lowest-friction way for students to demonstrate understanding without construction overhead. It serves two distinct pedagogical roles: (1) **Recognition assessment** — confirming students can identify correct answers, relationships, or representations before being asked to produce them (e.g., selecting the correct expression before building one in Equation Builder), and (2) **Decision-making tasks** — choosing between strategies, categories, or interpretations where the cognitive work is in the evaluation, not the response mechanics. Single-select tests discrete judgment ("which one?"); multi-select tests categorical reasoning ("which ones belong?"). Both modes appear on STAAR and are essential test-format familiarity skills. By keeping response mechanics simple, cognitive energy stays on the mathematical thinking, not the interface.
>

## Shape 🟡

### Option Card

A clickable rectangular region containing the option content and a selection indicator.

📷 *UX: Add visual of option card in default, hover, and selected states*

**Components:**

- **Selection indicator:** Radio button (single-select) or checkbox (multi-select), positioned consistently (left edge or top-left corner)
- **Content area:** Text, equation, image, or combination. Content determines card sizing.
- **Card boundary:** Clear visual boundary defining the clickable region. Entire card is the click target, not just the indicator or text.

**Content Formats:**

| Format | Description | Example | Typical Card Size |
| --- | --- | --- | --- |
| **Short text** | Single word, number, or brief phrase | "Stadium X" / "25" / "Scale of 5" | Compact |
| **Equation/expression** | Mathematical notation | `3 × 4` / `45 - 10 = 35` / `5 × 9 = 45` / `(4 × 3) + (5 × 2)` /
`___ × 5 = 30` | Compact |
| **Extended text** | Sentence or short paragraph | "There were 8 baskets. There were 2 apples in each basket. What is the total number of apples in all of the baskets?" | Tall |
| **Image/visual** | Picture, diagram, graph thumbnail, or toy
rendering (Grid Rectangle, Composite Figure, etc.) | Equal groups illustration,, toy or scaled toy | Fixed option card size; image content scales to fit within card.
When options ARE visual representations (e.g., different rectangles),
proportional differences between options are intentional — do not
normalize aspect ratios. |
| **Mixed Content** | Text + equation or text + number in a single
option | "3 × 8 = 24 square feet" / "Yes — 5 × 7 = 35" /
"Scale of 5"  | Compact to Tall (depends on length) | |

### Selection Indicator

**Single-select (radio):** Open circle when unselected → filled circle when selected. Only one option can be selected at a time. Selecting a new option deselects the previous.

**Multi-select (checkbox):** Open square when unselected → checked square when selected. Multiple options can be selected simultaneously. Re-clicking a selected option deselects it.

📷 *UX: Add visual showing radio vs checkbox indicators*

## Properties 🟡🔵

### Selection Modes

| Mode | Indicator | Behavior | Prompt Language | When Used |
| --- | --- | --- | --- | --- |
| **Single-select** | Radio button (○ / ●) | One selection at a time; new selection replaces previous | "Which...?" / "Select the..." / "Choose the correct..." | Most interactions — identification, comparison, computation |
| **Multi-select** | Checkbox (☐ / ☑) | Multiple selections allowed; toggle on/off | "Select ALL that apply" / "Which categories do you need?" | Category identification, classification, "select all" tasks |

**Mode determination:** Specified per interaction in the starter pack. The prompt language signals the mode to the student. Multi-select prompts ALWAYS include explicit language indicating multiple selections are expected.

**Correct count disclosure (multi-select):** By default, multi-select
prompts do NOT tell students how many correct options exist ("Select
ALL that apply"). This tests exhaustive reasoning — students must
evaluate every option independently rather than stopping after finding
a known number.

When pedagogically appropriate, prompts MAY disclose the count
("Select the TWO that apply"). Count disclosure reduces cognitive
demand and may be used for early scaffolding of multi-select tasks.

Starter packs specify prompt language; the system does not enforce
count constraints — a "select two" prompt with three correct options
is a curriculum error, not a system error. The system accepts any
number of selections regardless of prompt wording.

### Multi-Select Scoring Modes

Multi-select scoring is configured per interaction in the starter pack.
The system supports the following scoring modes:

| Mode | Rule | Use When |
| --- | --- | --- |
| **All-or-nothing** | Full credit only if ALL correct options selected AND no incorrect options selected | Low option count; clear correct set |
| **Partial (no false positives)** | Partial credit for selecting some correct options, IF no incorrect options are selected. Any incorrect selection = no credit. | Rewarding partial knowledge while penalizing guessing |
| **Partial (per-option)** | Each option scored independently: +1 correct selection, -0 or -1 incorrect selection | High option count; exploratory tasks |
| **Custom** | Scoring rule defined in starter pack | Edge cases not covered above |

### Layout Modes

| Layout | Description | When Used | Option Count |
| --- | --- | --- | --- |
| **Vertical list** | Options stacked vertically, full-width cards | Extended text content; image options; any option exceeding ~15 words; 5+ options | 3+ options |
| **Grid (2×2)** | Options arranged in 2-column grid | Short text or equation content where all options are compact | 4 options (2 rows × 2 columns) |
| **Grid (2×3)** | Options arranged in 2-column, 3-row grid | Short text or equation content, 5–6 compact options | 5–6 options |

📷 *UX: Add visual showing each layout mode*

**Layout selection logic:** Layout is determined by content length of the LONGEST option. If any option exceeds the compact threshold, all options use vertical list layout. All options within a single interaction use the same layout — no mixing.

**Responsive behavior:** If screen width cannot support grid layout, fall back to vertical list.

### State Properties

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Default** | No selection made; all options available | Neutral card styling; indicators empty |
| **Hover** | Cursor over an option card | Subtle highlight (border glow or background shift). Entire card boundary responds, not just indicator. |
| **Selected** | Student has chosen this option (pre-submission) | Indicator filled (radio ● or checkbox ☑); card highlight or border change to confirm selection |
| **Unselected** | Option not chosen (only visually distinct from Default when another option IS selected) | Neutral styling; indicator empty |
| **Correct (post-submission)** | Student's selection confirmed correct by system | Green indicator or card border; checkmark overlay |
| **Incorrect (post-submission)** | Student's selection confirmed incorrect by system | indicator or card border; X overlay |
| **Correct-reveal (post-submission)** | Shows which option WAS correct after an incorrect submission | highlight on correct option (shown alongside red on student's incorrect selection) |
| **Disabled** | Options locked after submission or during Guide dialogue | Reduced opacity or grayed styling; not clickable |

📷 *UX: Add visuals for each state*

**Post-submission state display:** After submission, the system simultaneously shows: (1) student's selection marked correct or incorrect, AND (2) if incorrect, the correct option revealed. Both persist until Guide feedback completes and system advances.

## Allowed Student Actions 🟡🔵

### Select Option

**Description:** Student clicks an option card to indicate their choice.

**Behavior (single-select):** Clicking an option selects it and deselects any previously selected option. Selection is immediate and visual — no confirmation step required before the systemic Check/Submit action.

**Behavior (multi-select):** Clicking an option toggles its selection state. Multiple options can be active simultaneously. Student can freely toggle options on and off before the systemic Check/Submit action.

**Purpose:** Capture student's response with minimal interaction overhead.

**Click target:** The ENTIRE card is clickable — selection indicator, content area, and any whitespace within the card boundary. Students do not need to click precisely on the radio button or checkbox.

📷 *UX: Add interaction visual/video*

---

### Change Selection (Pre-Submission)

**Description:** Student changes their mind before submitting.

**Behavior (single-select):** Click a different option. Previous selection immediately deselects; new selection activates. No limit on changes before submission.

**Behavior (multi-select):** Click any selected option to deselect it. Click any unselected option to select it. No limit on changes before submission.

**Purpose:** Support deliberate thinking and self-correction before commitment. No penalty for changing selections.

## Teaching / Remediation Actions 🟡🔵

Response Input is a response collection component. It does not perform teaching or remediation itself. Feedback content and remediation logic are governed by the **Remediation System FDB** and specified per-interaction in each module's starter pack.

### Feedback State Display

**Description:** After systemic submission, Response Input transitions selected option(s) to correct/incorrect visual states and reveals the correct answer if needed.

**Purpose:** Provide immediate, clear visual signal of correctness before Guide delivers verbal feedback.

**Triggers:** System-triggered on submission. Not student-initiated.

**Behavior sequence:**

1. Student's selection → correct state  OR incorrect state
2. If incorrect → correct option simultaneously shown in correct-reveal state
3. States persist through Guide feedback dialogue
4. System advances to next interaction (states clear)

📷 *UX: Add visual showing correct and incorrect feedback states*

---

### Disable Options

**Description:** All option cards become non-interactive.

**Purpose:** Prevent selection changes during Guide feedback, remediation dialogue, or animation sequences.

**Triggers:** (1) After submission and during feedback display. (2) During Guide dialogue that precedes the response prompt. (3) During system animations or transitions.

📷 *UX: Add visual of disabled state*

---

### Option Elimination (Configurable — Off by Default)

**Description:** After an incorrect submission, the system removes one or more confirmed-wrong options from the visible set, narrowing the student's choices for a retry.

**Purpose:** Scaffold process-of-elimination reasoning. Helps students who are stuck by reducing the decision space without revealing the answer. Teaches a transferable test-taking strategy.

**Default state:** OFF. Must be explicitly enabled per interaction in the starter pack or activity configuration.

**Triggers:** System-triggered after an incorrect submission, during remediation sequence. Not student-initiated.

**Behavior:**

1. Student submits incorrect selection → incorrect state displays, feedback delivered
2. System removes the student's incorrect selection (and optionally one additional wrong option) from visible options
3. Remaining options re-render in default state — student retries with a smaller set
4. Process can repeat across remediation tiers (light → medium → heavy) with progressive elimination

**Elimination rules:**

- NEVER eliminate the correct answer
- NEVER eliminate down to fewer than 3 remaining options (preserves the no-binary-guess principle even during remediation)
- Student's own incorrect selection is always the first option eliminated
- Additional eliminations (beyond the student's wrong pick) are optional and configurable
- Eliminated options visually disappear or become clearly unavailable (grayed + strikethrough, or removed entirely — UX decision)

**Configuration parameters:**

- `elimination_enabled: true/false` — master toggle (default: false)
- `eliminate_student_pick: true/false` — remove the option they chose (default: true when elimination enabled)
- `additional_eliminations: 0-N` — how many extra wrong options to remove beyond student's pick (default: 0)
- `minimum_remaining: 3` — floor for visible options after elimination (hard constraint)

---

---

### Disable Options

**Description:** All option cards become non-interactive.

**Purpose:** Prevent selection changes during Guide feedback, remediation dialogue, or animation sequences.

**Triggers:** (1) After submission and during feedback display. (2) During Guide dialogue that precedes the response prompt. (3) During system animations or transitions.

📷 *UX: Add visual of disabled state*

## Constraints 🟡

### Behavior Constraints

| Constraint | Description |
| --- | --- |
| No keyboard/text input | All interaction through click/tap on option cards |
| No partial credit (single-select) | Exactly one option is correct; all others are incorrect |
| Multi-select scoring | Defined per interaction — may require ALL correct selections, or may accept partial |
| Selection required before submission | Systemic Check/Submit is inactive (grayed) until at least one option is selected |
| No option reordering | Options display in the order specified by the starter pack. System does not randomize unless explicitly configured. |
| Mode is fixed per interaction | An interaction is either single-select OR multi-select, never both. Mode does not change mid-interaction. |

### Content Constraints

| Property | Constraint | Notes |
| --- | --- | --- |
| Option count | 3 minimum; no hard maximum | 3–4 most common. 5–6 acceptable when content warrants (e.g., word problem matching, category selection). Never fewer than 3 — binary choice allows guessing and students ignore remediation after a coin-flip miss. |
| Option content length | No maximum, but options within a single interaction should be roughly similar in length | Prevents one option standing out as "the long one must be right" |
| Equation rendering | Must support ×, ÷, =, +, −, ☐, ?, and parentheses | Standard mathematical notation |
| Image options | Fixed aspect ratio; uniform size across all options in interaction | Prevents size-based selection bias |
| **NOT:** Free-form text entry | Never | All responses through pre-defined options |
| **NOT:** Fewer than 3 options | Never | Binary choice enables guessing; students bypass remediation |
| **NOT:** Scrollable option lists | Never | All options visible simultaneously without scrolling |

### Visual / Teaching Constraints

| Feature | Constraint | Notes |
| --- | --- | --- |
| Option order | Curriculum-specified; not auto-randomized | Distractor placement is pedagogically intentional |
| Equal visual weight | All option cards same size within an interaction | Prevents visual bias toward any option |
| Content alignment | Text left-aligned; equations centered within card | Consistent reading pattern |
| Selection indicator position | Consistent across all options (left edge or top-left) | Predictable interaction target |
| Feedback color | TBD | Universal, no colorblind-only signaling  |
| In-option color coding |  Configurable — off by default  | When enabled,
specific text or equation elements within an option card can be rendered
in a designated color. Color must never be the sole differentiator
between options (accessibility). Used when options reference color-coded
elements in an accompanying toy (e.g., matching a term to a highlighted
region). Color values specified per interaction in the starter pack. |
| Accessibility: colorblind support | TBD | Color is not the sole indicator |

## Layout Constraints 🔵

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum instances | 1 per screen | One active Response Input interaction at a time |
| Minimum touch target | 44×44px per option card | Accessibility standard |
| Can appear with | Any toy — graphs, arrays, equal groups, equation builder, data tables, images, word problem stems | Response Input is a universal response layer |
| Cannot appear with | Another active Response Input | One response interaction at a time |
| Typical position | Below the visual/toy; below Guide prompt | Response area is consistently at the bottom of the content space |
| Spacing between options | Consistent gap between all option cards | Prevents accidental mis-clicks; visual clarity |

📷 *UX: Add layout diagram(s) showing Response Input positioned relative to toys and Guide dialogue*

**Common Layout Patterns:**

The following are representative configurations. Response Input can
appear with any toy in any layout that maintains simultaneous
visibility of the visual context and all options. Specific layouts
per interaction are determined by the toy's dimensions and the
option content length. The patterns below cover the most common
arrangements:

- **Toy (top/center) + Response Input (bottom):** Standard — student observes visual, responds below
- **Side-by-side toy + Response Input (right):** Used when toy and options need simultaneous visibility
- **Word Problem stem (top) + Response Input (bottom):** Text-heavy interactions
- **Image options (grid):** When options ARE the visuals (e.g., "Which picture shows 3 groups of 4?")

## Tool to Schema Vocab Translation 🟣

*Engineering: Fill this table as schema is finalized.*

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
|  |  |  |

## Curriculum Animator Techs (CAT) 🟣

*Engineering: Add animation specifications, sequence events, GDScript references, and JSON schema examples here as implementation progresses.*

## Open Questions ⚪

- [ ]  **[UX]** Grid vs list threshold: What word count or character count triggers vertical list layout? Needs testing with actual curriculum content.
- [ ]  **[UX]** Hover state on touch devices: Touch has no hover. How does the interaction differ on tablet if platform expands beyond PC?
- [ ]  **[UX]** Selected state persistence: When student selects an option, does the card stay highlighted until they select another, or does it show a brief "selected" animation then settle to a subtler indicator?
- [ ]  **[UX]** Image option sizing: For visual options (e.g., "which picture shows 3 groups of 4?"), what is the maximum image size per card while maintaining all-option visibility without scrolling?
- [ ]  **[UX]** Multi-select submission threshold: Does system require a minimum number of selections before Check is active, or is 1 selection enough to enable Check for multi-select?
- [ ]  **[UX]** Feedback timing: How long do correct/incorrect states persist before system advances? Fixed duration, or until Guide dialogue completes?
- [ ]  **[Engineering]** Partial credit scoring for multi-select: Binary (all correct or fail) vs. partial (credit per correct selection)? Or configurable per interaction?
- [ ]  **[Engineering]** Option content rendering: Is equation content rendered via LaTeX, MathML, or custom renderer? Needs alignment with Equation Builder's rendering approach.
- [ ]  **[Curriculum]** Should option randomization ever be supported as a configurable parameter for Practice phase (where pedagogical ordering is less critical)?
- [ ]  **[UX]** Practical upper bound: At what option count does the no-scroll constraint break on standard screen sizes? Likely 6–8 depending on content length. Needs testing to establish layout grid limits.

## JSON Schema Formatting 🟣

*Engineering: Add JSON schema examples here as implementation progresses.*
---

