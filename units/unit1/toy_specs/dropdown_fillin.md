# Drop Down/Fill-in-the-Blank

Category: Unit 1
Created: February 26, 2026 6:00 PM
Status: Initial Spec Draft

---

---

>
>
>
> **WHAT:** A sentence-frame response system where students complete statements by selecting words or phrases from icon-matched option palettes. One or more fill spaces are embedded inline within a sentence or paragraph. Each fill space is linked to its own palette of selectable options via a shared icon indicator, so students can track which space they are filling when multiple blanks are present.
>
> **WHY:** Fill-in-the-Blank tests whether students can supply the right word or phrase *within a meaningful context* — not just pick an answer from a list, but complete a mathematical statement, claim, or description. This requires comprehension of the surrounding sentence structure, not just recognition of the correct option in isolation. The format directly mirrors STAAR assessment items ("Choose the correct answer from each drop-down menu to complete the sentences"), so students build critical test-format familiarity. The icon-matching system solves a real cognitive tracking problem for young learners: when a sentence has two or three blanks, each with different option sets, students need a clear visual signal for "which choices go with which space." Without it, students waste cognitive energy on interface navigation instead of mathematical reasoning.
>

## Shape 🟡

### Sentence Frame

The containing text structure with one or more embedded fill spaces. The sentence frame is static — students cannot edit the surrounding text.

📷 *UX: visual of a complete sentence frame with fill spaces*

![image.png](image.png)

**Components:**

- **Static text:** The non-editable sentence or paragraph surrounding the fill spaces. Renders as standard body text.
- **Fill spaces:** Inline blank regions within the sentence where student selections will appear. Visually distinct from static text (underline, box outline, or highlighted region).
- **Icon indicators:** Small icons displayed adjacent to each fill space AND on the corresponding option palette. Icons link spaces to their palettes when multiple blanks exist.

**Example (single blank):**

> The stadium with the least number of seats is Stadium `[⚡ ________]`.
>

**Example (two blanks, icon-matched):**

> Bryon's claim is `[⚡ ________]` because 1/8 of a model should be represented by `[🍃 ________]`.
>

**Example (two blanks, same content domain):**

> The value of the 8 in the hundred thousands place is `[⚡ ________]` times greater than the value of the 8 in the thousands place. The value of the 8 in the hundred thousands place is `[🍃 ________]` times greater than the value of the 8 in the tens place.
>

### Fill Space

An inline blank region embedded within the sentence frame.

📷 *UX: visual of fill space in default, active, and filled states*

[Screen Recording 2026-02-26 161817.mp4](Screen_Recording_2026-02-26_161817.mp4)

![image.png](image%201.png)

**Visual form:** Rectangular region inline with text. Width accommodates the longest option in its palette. Displays the icon indicator for palette matching.

**Content when filled:** Student's selected word or phrase appears within the space, replacing the blank. Text styling matches surrounding sentence but may retain a subtle background or border to indicate it's a student-provided value.

### Option Palette

A set of selectable word/phrase options linked to a specific fill space via icon matching.

📷 *UX: visual of an option palette with icon indicator*

![image.png](image%202.png)

**Components:**

- **Icon indicator:** Matching icon displayed on the palette header or beside each option, identical to the icon on its linked fill space
- **Option items:** Clickable word or phrase selections. Displayed as a dropdown list, pop-over panel, or inline card set (UX determines rendering approach)
- **Selection behavior:** Click to select; selected option populates the linked fill space immediately

**Palette display trigger:** Student clicks or activates the fill space → palette appears showing available options for that space only.

### Palette Content Types

| Content Type | Description | Example | Notes |
| --- | --- | --- | --- |
| **Word/phrase** | Natural language term or short phrase | "multiply" / "correct" / "Stadium X" | Most common. Current spec default. |
| **Number** | Numeric value | "2" / "12" / "32" | Used for completing numeric statements. Palette functions as constrained numeric selection. |
| **Unit label** | Measurement unit or mathematical term | "square feet" / "inches" / "square units" | Used for unit identification and labeling tasks. |
| **Expression/equation** | Rendered mathematical notation | "4 × 3" / "5 + 3 = 8" | Must use same rendering approach as Response Input (MC) equation content. |
| **Mixed** | Text + number or text + equation | "Yes — 5 × 7 = 35" / "3 groups of 4" | Combines natural language with mathematical content in a single option. |

All content types follow the same interaction pattern: click
fill space → palette appears → click option → option populates
fill space. Content type does not change the interaction — only
the rendering.

### Icon Indicator System

Visual markers that link fill spaces to their option palettes.

📷 *UX: visual showing icon-matched spaces and palettes*

![image.png](image%203.png)

![image.png](image%204.png)

**Purpose:** When a sentence frame has multiple fill spaces, each space has a different set of valid options. The icon system lets students instantly see which palette belongs to which space without reading instructions or remembering position.

**Icon requirements:**

- Visually distinct from each other (different shape, not just different color)
- Simple, recognizable symbols (lightning bolt, leaf, star, circle, etc.)
- Small enough to sit inline beside the fill space without disrupting text flow
- Same icon appears on the fill space AND on its corresponding option palette
- Colorblind-safe: icons differ by shape, not only color

**Single-blank optimization:** When only one fill space exists, the icon indicator system is optional. A single blank with a single palette has no tracking ambiguity.

## Properties 🟡🔵

### Display Modes

| Mode | Description | Visual Treatment | When Used |
| --- | --- | --- | --- |
| **Single blank** | One fill space within the sentence frame | Fill space + one option palette. Icon indicator optional. | Simple completion tasks — "The scale of this graph is ____." |
| **Multi-blank (independent)** | Two or more fill spaces, each with its own independent option palette | Each fill space has a unique icon indicator matching its palette. Palettes contain different options. | STAAR-style multi-dropdown — "The least is ____ . The greatest is ____ ." |
| **Multi-blank (shared palette)** | Two or more fill spaces drawing from the same option pool | All fill spaces share one icon (or use no icon). Same palette opens for each space. An option selected for one space may or may not be available for another (configurable: allow reuse vs. remove on use). | Classification tasks — fill multiple blanks from the same category set |

### Shared Palette Layout Variants

When multiple fill spaces share a palette, two presentation approaches
are available:

| Variant | Description | When Used |
| --- | --- | --- |
| **Per-space popup** | Clicking each fill space opens the shared palette adjacent to that space. Standard palette behavior, shared pool. | When fill spaces are far apart in the sentence; when palette is short (3-4 options) |
| **Persistent word bank** | All shared options displayed persistently below or beside the sentence frame. Student clicks/drags from the bank to fill spaces. Used options visually move to or appear in the fill space. | When option count is high (5+); when seeing all options simultaneously aids reasoning; vocabulary/classification tasks |

Layout variant is a UX decision per interaction. Both use the same
underlying shared-palette data model. The persistent word bank is
the more common pattern for vocabulary completion tasks.

### State Properties

| State | Description | Visual Treatment |
| --- | --- | --- |
| **Default (empty)** | Fill space has no selection; awaiting student input | Blank region with subtle border/underline. Icon indicator visible. |
| **Active** | Student has clicked this fill space; its palette is open | Fill space border highlights. Linked palette is visible and interactive. Other fill spaces are dimmed or inactive. |
| **Filled (pre-submission)** | Student has selected an option; it now displays in the fill space | Selected word/phrase visible inline. Fill space retains subtle border indicating it's editable. Icon indicator remains. |
| **Correct (post-submission)** | System confirms this fill space's selection is correct | Indicator or or highlight on the fill space. |
| **Incorrect (post-submission)** | System confirms this fill space's selection is incorrect | Indicator or highlight on the fill space. Correct answer may replace or appear alongside. |
| **Disabled** | Fill space is locked during feedback or Guide dialogue | Reduced opacity; not clickable. Palette cannot be opened. |

📷 *UX: visuals for each state*

Default, active, filled:

![image.png](image%205.png)

Correct:

[Screen Recording 2026-02-26 163329.mp4](Screen_Recording_2026-02-26_163329.mp4)

Incorrect + Disabled

[Screen Recording 2026-02-26 164312.mp4](Screen_Recording_2026-02-26_164312.mp4)

### Palette Behavior

| Property | Specification | Notes |
| --- | --- | --- |
| **Trigger** | Click/tap on the fill space | Palette appears on activation |
| **Dismissal** | Selection made, click outside palette, or click a different fill space | Only one palette open at a time |
| **Option count** | 3 minimum; no hard maximum | Same rationale as Response Input — no binary guessing |
| **Selection action** | Click option → option text populates fill space → palette closes | Immediate visual feedback |
| **Re-selection** | Click filled space → palette reopens → student can change selection | Unlimited changes before submission |
| **Scroll** | Avoid if possible; all options visible at once preferred | If option count forces scrolling, ensure scroll affordance is clear |

## Allowed Student Actions 🟡🔵

### Activate Fill Space

**Description:** Student clicks a fill space to open its linked option palette.

**Behavior:** Click the fill space → palette appears adjacent to or below the space. If another palette was open, it closes first. Only one palette is open at a time.

**Purpose:** Initiate the selection process for a specific blank.

📷 *UX: Add interaction visual/video*

---

### Select Option from Palette

**Description:** Student clicks an option within the open palette.

**Behavior:** Selected option text appears in the fill space. Palette closes. Fill space transitions to Filled state. If the space previously had a different selection, the new selection replaces it immediately.

**Purpose:** Populate the blank with the student's chosen response.

📷 *UX: Add interaction visual/video*

---

### Change Selection (Pre-Submission)

**Description:** Student clicks an already-filled space to reopen its palette and select a different option.

**Behavior:** Palette reopens showing all options. Previously selected option may be visually marked (subtle indicator like a dot or checkmark) but is fully re-selectable along with all other options. New selection replaces old immediately.

**Purpose:** Support deliberate thinking and self-correction. No penalty for changes before submission.

---

### Navigate Between Fill Spaces

**Description:** In multi-blank frames, student clicks a different fill space to switch focus.

**Behavior:** Current palette closes (if open). New fill space activates and its palette opens. Student can fill spaces in any order — not forced to go left-to-right.

**Purpose:** Allow flexible completion order. Some students may want to fill the "easier" blank first.

## Teaching / Remediation Actions 🟡🔵

Fill-in-the-Blank is a response collection component. It does not perform teaching or remediation itself. Feedback content and remediation logic are governed by the **Remediation System FDB** and specified per-interaction in each module's starter pack.

### Feedback State Display

**Description:** After systemic submission, each fill space transitions to correct/incorrect visual state.

**Purpose:** Provide clear, per-blank visual signal of correctness before Guide delivers verbal feedback.

**Triggers:** System-triggered on submission. Not student-initiated.

**Behavior sequence (multi-blank):**

1. All fill spaces evaluated simultaneously on submission
2. Each space independently shows correct or incorrect
3. If incorrect → correct answer may replace the student's selection or appear alongside
4. States persist through Guide feedback dialogue
5. System advances to next interaction (states clear)

**Partial completion handling:** If student submits with one or more fill spaces still empty, system behavior is configurable:

- Option A: Prevent submission — Check/Submit remains inactive until all spaces are filled
- Option B: Allow submission — empty spaces marked as incorrect

📷 *UX: Add visual showing per-blank feedback states*

---

### Palette Option Elimination (Configurable — Off by Default)

**Description:** After an incorrect submission for a specific fill space, the system removes the student's incorrect selection (and optionally additional wrong options) from that space's palette, narrowing choices for a retry.

**Purpose:** Same as Response Input — scaffold process-of-elimination reasoning without revealing the answer. Applies per-palette, not globally.

**Default state:** OFF. Must be explicitly enabled per interaction in the starter pack or activity configuration.

**Triggers:** System-triggered after an incorrect submission, during remediation sequence. Not student-initiated.

**Behavior:**

1. Student submits → one or more fill spaces marked incorrect
2. For each incorrect fill space: system removes the student's wrong selection from that space's palette
3. Student re-activates the incorrect fill space → palette opens with reduced options
4. Correctly-filled spaces remain locked — student only retries incorrect blanks

**Elimination rules:**

- NEVER eliminate the correct answer from any palette
- NEVER eliminate down to fewer than 3 remaining options per palette
- Only the palettes for incorrect fill spaces are modified — correct fill spaces are untouched
- For shared palette mode: elimination applies only to the specific blank that was wrong, not globally across all blanks sharing the pool

**Configuration:** Same parameters as Response Input (`elimination_enabled`, `eliminate_student_pick`, `additional_eliminations`, `minimum_remaining`).

📷 *UX: Add visual showing per-palette elimination sequence*

---

### Disable Fill Spaces

**Description:** All fill spaces become non-interactive.

**Purpose:** Prevent changes during Guide feedback, remediation dialogue, or animation sequences.

**Triggers:** (1) After submission and during feedback display. (2) During Guide dialogue that precedes the response prompt. (3) During system animations or transitions.

## Constraints 🟡

Fill-in-the-Blank is a response collection component. It does not perform teaching or remediation itself. Feedback content and remediation logic are governed by the **Remediation System FDB** and specified per-interaction in each module's starter pack.

### Feedback State Display

**Description:** After systemic submission, each fill space transitions to correct/incorrect visual state.

**Purpose:** Provide clear, per-blank visual signal of correctness before Guide delivers verbal feedback.

**Triggers:** System-triggered on submission. Not student-initiated.

**Behavior sequence (multi-blank):**

1. All fill spaces evaluated simultaneously on submission
2. Each space independently shows correct  or incorrect
3. If incorrect → correct answer may replace the student's selection or appear alongside
4. States persist through Guide feedback dialogue
5. System advances to next interaction (states clear)

**Partial completion handling:** If student submits with one or more fill spaces still empty, system behavior is configurable:

- Option A: Prevent submission — Check/Submit remains inactive until all spaces are filled
- Option B: Allow submission — empty spaces marked as incorrect

📷 *UX: Add visual showing per-blank feedback states*

---

### Palette Option Elimination (Configurable — Off by Default)

**Description:** After an incorrect submission for a specific fill space, the system removes the student's incorrect selection (and optionally additional wrong options) from that space's palette, narrowing choices for a retry.

**Purpose:** Same as Response Input — scaffold process-of-elimination reasoning without revealing the answer. Applies per-palette, not globally.

**Default state:** OFF. Must be explicitly enabled per interaction in the starter pack or activity configuration.

**Triggers:** System-triggered after an incorrect submission, during remediation sequence. Not student-initiated.

**Behavior:**

1. Student submits → one or more fill spaces marked incorrect
2. For each incorrect fill space: system removes the student's wrong selection from that space's palette
3. Student re-activates the incorrect fill space → palette opens with reduced options
4. Correctly-filled spaces remain locked — student only retries incorrect blanks

**Elimination rules:**

- NEVER eliminate the correct answer from any palette
- NEVER eliminate down to fewer than 3 remaining options per palette
- Only the palettes for incorrect fill spaces are modified — correct fill spaces are untouched
- For shared palette mode: elimination applies only to the specific blank that was wrong, not globally across all blanks sharing the pool

**Configuration:** Same parameters as Response Input (`elimination_enabled`, `eliminate_student_pick`, `additional_eliminations`, `minimum_remaining`).

📷 *UX: Add visual showing per-palette elimination sequence*

---

### Disable Fill Spaces

**Description:** All fill spaces become non-interactive.

**Purpose:** Prevent changes during Guide feedback, remediation dialogue, or animation sequences.

**Triggers:** (1) After submission and during feedback display. (2) During Guide dialogue that precedes the response prompt. (3) During system animations or transitions.

## Layout Constraints 🔵

| Constraint | Value | Notes |
| --- | --- | --- |
| Maximum instances | 1 sentence frame per screen | One Fill-in-the-Blank interaction at a time |
| Can appear with | Any toy — graphs, fraction models, arrays, data tables, images | Fill-in-the-Blank describes/interprets what the toy shows |
| Cannot appear with | Response Input (MC) in the same interaction | One response system per interaction — never MC + FITB simultaneously |
| Typical position | Below the visual/toy; integrated with or below Guide prompt | Sentence frame is the response area |
| Palette position | Adjacent to or directly below the activated fill space | Must not obscure the sentence frame or the visual/toy |
| Fill space alignment | Inline with sentence text | Fill spaces are part of the sentence, not separate UI elements |

📷 *UX: Add layout diagram(s) showing Fill-in-the-Blank positioned relative to toys and Guide dialogue*

**Common Layout Patterns:**

- **Visual (top) + Sentence frame with fill spaces (bottom):** Standard — student observes toy, completes statement below
- **Data table/graph (top) + Multi-blank sentence frame (bottom):** STAAR-style — "The stadium with the least is ____ . The stadium with the greatest is ____ ."
- **Claim evaluation (visual + text stem + sentence frame):** Bryon's claim pattern — image and claim text above, completion frame with icon-matched blanks below

## Tool to Schema Vocab Translation 🟣

*Engineering: Fill this table as schema is finalized.*

| Curriculum Term | Schema Property | Notes |
| --- | --- | --- |
|  |  |  |

## Curriculum Animator Techs (CAT) 🟣

*Engineering: Add animation specifications, sequence events, GDScript references, and JSON schema examples here as implementation progresses.*

## Open Questions ⚪

- [ ]  **[UX]** Palette rendering: Dropdown list (overlays content below), pop-over panel (floats adjacent), or inline expansion (pushes content down)? Each has tradeoffs for sentence frame readability.
- [ ]  **[UX]** Icon indicator set: What is the standard icon library? Need 3+ distinct icons minimum (for 3-blank frames). Candidates: lightning bolt, leaf, star, diamond, circle, moon. Must be simple, small, recognizable.
- [ ]  **[UX]** Fill space width strategy: Fixed width (largest option)? Or dynamic width that adjusts when a shorter/longer option is selected? Fixed prevents layout shift but may look awkward with short selections.
- [ ]  **[UX]** Palette position on small screens: If fill space is near the bottom of the screen, does palette open upward? Needs responsive positioning logic.
- [ ]  **[UX]** Previously selected option indicator: When reopening a palette to change selection, how is the current selection marked? Checkmark? Highlight? Bold?
- [x]  **[UX]** Shared palette mode — option reuse: When two blanks share a palette, can the same option be selected for both blanks? Or does selecting an option for one blank remove it from the other's available options? Likely configurable per interaction.
- [ ]  **[Engineering]** Frame template parsing: How does the system distinguish fill space tokens from static text in the template string? Recommended: `{blank_id}` token syntax.
- [ ]  **[Engineering]** Partial completion on submission: Default to blocking submission until all blanks filled? Or allow and mark empties as incorrect?
- [ ]  **[Engineering]** Per-blank scoring: Each blank scored independently? Or all-or-nothing for the entire frame? Impacts remediation — if one blank is wrong, does remediation address just that blank or the whole statement?
- [ ]  **[Curriculum]** Maximum option length: At what word count does an option become too long for a palette item? If options are full sentences, should this be Response Input (MC) instead of Fill-in-the-Blank?
- [ ]  **[UX]** Palette Option Elimination visual: Same question as Response Input — removed entirely vs. grayed/strikethrough? Palette context may favor removal since palettes are smaller and reflow is less disorienting.
- [ ]  **[UX]** Palette rendering: Dropdown list, pop-over panel, or
inline expansion? Add reference: STAAR items often render options as
inline lettered bubbles (A/B/C/D) directly below or beside the fill
space, visually similar to MC but positionally anchored to the blank.
Consider this as a rendering variant.

## JSON Schema Formatting 🟣

*Engineering: Add JSON schema examples here as implementation progresses.*
---

