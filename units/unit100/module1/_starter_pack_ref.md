# MODULE 01: Rectangle Recognition & Tile-Based Production

<!--
HUB PROPERTIES BLOCK
module: G4U1M01
unit: Grade 4 Unit 1
grade: 4
prior_module: null
next_module: G4U1M02
phase8_version: "2.0"
rerun_date: 2026-04-27
compiler: claude_opus_4_7
skeleton_version: 03.25.26
tool_flow_input: Tool_Flow_Document_v3.md (Phase 7 rerun 2026-04-27)
worker_drafts_merged: worker_a (Sonnet 4.6, base) + worker_b (GPT-5.4, clarity overlays) + worker_c (Gemini 3.1 Pro, structural sanity)
-->

# BACKBONE

---

## 1.0 THE ONE THING

Students recognize rectangles by their row-and-column tile structure — counting rows of equal tiles rather than counting every tile individually — and produce each rectangle's area as a multiple of its fixed side length, stated through the full module sentence stem.

**CRA Stage:** Concrete (B-snap-OFF free tile placement) → Relational (B-snap-ON grid-snapped fixed-side-length build) → Abstract first encounter (equation form appears only inside the companion Drop Down stem, not on the toy surface). This is the unit's Concrete entry point.

**Critical Misconception:** U1.1 (M1) — tile-counting by 1s instead of multiplying rows. A student who counts every square one at a time arrives at the correct area total but bypasses the multiplicative grouping structure that makes "a multiple of" meaningful. Without row-based thinking, the connection between side length and area never forms, and M03's systematic search for finding every rectangle for a fixed area will feel arbitrary rather than principled.

**Success Indicator:** After M01, the student (a) builds a rectangle on Hundred Grid Mode B by extending full rows rather than placing one tile at a time (tile-by-tile detection signal stays OFF), (b) states its area as a complete multiple-statement stem (`___ is a multiple of ___ because ___ × ___ = ___`), and (c) holds this connection across varied side lengths without prompting.

**Biggest Risk:** If the warmup WODB options are trivially distinguishable by a non-structural visual attribute (e.g., color, label presence) rather than by row count or side length, students will not arrive at Beat 2 already attending to rectangle structure. The WODB authoring constraint (WP.M01.1 / WT.M01.2) is load-bearing for this transition.

**Open Questions Carried Forward (do not silently resolve):**
- **OQ-M01-ENTRY-V4** — Default M01 Concrete entry is HG Mode B / B-snap-OFF; Unit Square Tiles alternative path is documented but not authored here pending SME resolution.
- **OQ-M01-LABELS-V4** — Pre-Check visibility of locked-side numeric label in Beats 4–6 is unresolved; engineering implements both behaviors behind the label-visibility flag for prototype A/B testing.

---

## 1.1 LEARNING GOALS

*Verbatim from OUR Curriculum*

**L1:** "Find areas of rectangles with a fixed side length and explain that each area is a multiple of that side length."
**L2:** "Recognize that building rectangles with the same fixed side length produces areas that form a sequence of multiples of that side length."
**Module Goal (Student-Facing):** "You will build rectangles where one side stays the same, and discover that the areas you build are multiples of that side length."

**Exit Check Tests:**
* Given three rectangles, identify which has an area that is a multiple of a named side length (recognition)
* Given a prebuilt rectangle displayed on Hundred Grid Mode B, complete the full module sentence stem (`___ is a multiple of ___ because ___ × ___ = ___`)
* Build a rectangle on Hundred Grid Mode B with a given fixed side length and target area, then complete the module sentence stem independently

**Question/Test Language Stems (from Module Mapping v2):**
* "Which rectangle has an area that is a multiple of 3?" → Maps to §1.8 EC.1 (IDENTIFY, recognition)
* "Fill in: ___ is a multiple of ___ because ___ × ___ = ___" → Maps to §1.8 EC.2 (CONNECT, transfer)
* "Build a rectangle with a side length of 5 and an area of 30. Tap Check, then fill in the sentence." → Maps to §1.8 EC.3 (CREATE + CONNECT, procedural + transfer)

### 1.1.1 Standards Cascade

| Role | Standard | Description |
|------|----------|-------------|
| **Building On** | CCSS 3.MD.C | Geometric measurement: understand concepts of area and relate area to multiplication and addition. |
| **Building On** | CCSS 3.MD.C.7.a | Find the area of a rectangle with whole-number side lengths by tiling it and show the same area can be found by multiplying the side lengths. |
| **Addressing** | CCSS 4.OA.B.4 | Find all factor pairs for a whole number in the range 1–100; recognize that a whole number is a multiple of each of its factors; determine whether a given whole number is a multiple of a given one-digit number; determine whether a given whole number is prime or composite. (M01 addresses specifically the "multiple of each of its factors" strand via the fixed-side-length rectangle model. Factor-pair enumeration, prime/composite classification are deferred to M03 and M04 respectively.) |
| **Building Towards** | (none distinct) | Module Mapping v2 names no separate formal Building Towards standard for M01; this module feeds forward representationally to M02 and M03. |

### 1.1.2 Module Bridges

| Direction | Content |
|-----------|---------|
| **From (Depends on)** | Grade 3 area knowledge (3.MD.C, 3.MD.C.7.a) — the student has tiled rectangles and connected area to multiplication before entering M01. M01 does not re-teach area from scratch; it re-anchors area to the concept of "multiple." |
| **This module establishes** | (1) The vocabulary anchor "multiple" tied to the rectangle area model. (2) The sentence stem `___ is a multiple of ___ because ___ × ___ = ___` as the unit's primary production form. (3) The multiplicative grouping habit (row-extension thinking) that defeats U1.1. (4) §2.13 Hundred Grid Mode B as the unit's primary rectangle host. |
| **To (Feeds forward to)** | M02 (Both Ways Around — Mini) reuses M01's rectangle model to introduce both equation orientations. M03 (Finding Every Factor Pair) inverts the M01 rectangle model — area becomes fixed, side lengths become the focus. Both M02 and M03 assume the rectangle model is committed knowledge from M01. |

### 1.1.3 OUR Lesson Sources

- **Primary source:** IM 2019 Grade 4 Unit 1 Lesson 1 [adapted]
  - Warm-up "Which One Doesn't Belong?" preserved as the recognition entry beat (Beat 1 / Interaction W.1)
  - Area-tiling activity adapted into the §2.13 Hundred Grid Mode B Concrete build (Beat 2 / Interaction L.1)
  - Number Talk eliminated (unit-wide policy per Module Mapping v2 and Research Summary §2 Commitment 11)
- Phase 5 Module Mapping v2, M01 row and narrative
- Phase 6 Digital Toys & Interactables v4, §2.10, §2.11, §2.13
- Phase 7 Tool Flow v3, M01 beats and warmup patch
- BrainLift DOK4 / DOK3 constraints for observable language, recognition-before-production, and equation-after-check gating

---

## 1.2 SCOPE BOUNDARIES

### ✅ Must Teach

1. **The rectangle as area model:** Students build rectangles on §2.13 Hundred Grid Mode B and connect tile count to area.
2. **Fixed-side-length constraint:** Students experience building rectangles where one dimension is fixed and the other varies — the area keeps changing, always as a multiple of the fixed side length.
3. **"Multiple" definition via area:** Students arrive at the statement that each area they build is a multiple of the fixed side length because that side length times another whole number equals the area.
4. **The module sentence stem (required throughout):** `___ is a multiple of ___ because ___ × ___ = ___` — produced in full at every production beat.
5. **The concrete stem (Concrete phase only):** `___ tiles fill ___ rows of ___, so the area is ___ square units` — produced after the B-snap-OFF build to establish row structure.
6. **Multiplicative grouping habit (not tile-by-tile counting):** Instruction builds toward row-based thinking. The §2.13 Hundred Grid Mode B tile-by-tile count detection signal routes students to the row-structure scaffold when triggered.
7. **Recognition before production:** The IM "Which One Doesn't Belong?" warm-up establishes rectangle structure recognition before any production is demanded.
8. **CRA arc inside M01:** Concrete (B-snap-OFF free placement) → Relational (B-snap-ON grid-snapped, fixed-side-length) → Abstract first encounter (equation form appears only inside the companion Drop Down stem, not on the toy surface).
9. **Equation form in standard orientation only:** `a × b = c`. Reversed orientation (`c = a × b`) is M02's one new thing and must not appear here.
10. **Sentence stems present throughout M01.** Stems are required throughout this unit. Stem fading is deferred to a later iteration.

### ❌ Must Not Include

**HARD VOCABULARY FENCE — these four terms are forbidden in all M01 student-facing copy:**
- ❌ `factor` — deliberately withheld per IM sequencing (Module Mapping v2 §M01): "Vocabulary 'factor' and 'factor pair' are deliberately withheld here — IM's own sequencing — to prevent vocabulary overload at the conceptual entry point." Belongs to M03.
- ❌ `factor pair` — same rationale. M03 territory.
- ❌ `prime` — M04 (merged Prime and Composite Numbers) territory.
- ❌ `composite` — M04 territory.

**Other out-of-scope content for M01:**
- Paired dual-orientation equation display (`a × b = c` AND `c = a × b` side-by-side) — that is §2.13 Hundred Grid Mode C and belongs exclusively to M02. M01 is single-orientation only; Mode C must not appear.
- In-toy equation overlays inside Hundred Grid Mode B — suppressed in M01 at every beat including post-Check. Equation form first appears inside the companion Drop Down stem.
- Number Talk routine — eliminated unit-wide.
- Stem fading — Stems are required throughout this unit. Stem fading is deferred to a later iteration.
- Any reversed equation orientation (`c = a × b`) — M02's sole focus.
- Any systematic search for all rectangles with a given area — M03's focus.
- Classification of numbers as prime or composite — M04.
- Free-text explanation as the main explanation mode — M01 uses sentence stems throughout.
- Partner / Number-Talk discussion routines.
- Hundred Grid Mode C, or any second rectangle host as the default M01 path.
- Silent resolution of OQ-M01-ENTRY-V4 or OQ-M01-LABELS-V4.

### Scope Confirmation Checklist

- [ ] **SC-1:** All four fenced terms absent from every student-facing prompt, option label, stem slot, tooltip, and feedback text
- [ ] **SC-2:** Equation form `a × b = c` only — no `c = a × b` in M01
- [ ] **SC-3:** Mode C (dual-orientation display) does not appear at any beat
- [ ] **SC-4:** Every production beat includes a full sentence stem (module stem or concrete stem)
- [ ] **SC-5:** No Number Talk routine present
- [ ] **SC-6:** Both OQ-M01-ENTRY-V4 and OQ-M01-LABELS-V4 flagged (not silently resolved)

---

## 1.3 VOCABULARY ARCHITECTURE

M01 introduces exactly one new vocabulary anchor: **multiple**. The two bridging terms — **area** and **side length** — are re-anchored from Grade 3 rather than introduced fresh. The four terms in the vocabulary fence (`factor`, `factor pair`, `prime`, `composite`) are explicitly withheld. This tight vocabulary scope is a deliberate design choice: introducing factor vocabulary while students are forming the area-model-to-multiple connection would risk U1.5 (vocabulary confusion) before the concept of "multiple" is stable.

The word **multiple** does not appear in Hundred Grid Mode B toy chrome, tooltips, or overlays while the M01 mode flag is active. It enters the student's experience exclusively through the companion Drop Down sentence stem post-Check at Beat 5 — so the first time a student encounters "multiple" as a word, they are simultaneously holding a built rectangle whose area they have just counted. This sequencing is load-bearing.

### Vocabulary Staging by Phase

| Phase | Terms introduced or used | Notes |
|-------|--------------------------|-------|
| **Warmup (Recognition)** | rectangle, rows, side length, area (bridging — informal) | No formal vocabulary introduction; informal language only per Warmup Playbook §4B |
| **Concrete Phase (Beat 2, B-snap-OFF)** | area, side length, rows, tiles, squares (all bridging) | Concrete stem uses "rows of" language to defeat U1.1. No "multiple" yet. |
| **Relational Phase (Beat 4, B-snap-ON)** | area, side length, rows (bridging); "fixed side length" as informal phrase | Equation overlays suppressed. No "multiple" yet — it arrives with the stem. |
| **Abstract First Encounter (Beat 5+)** | **multiple** (formal, new anchor) | Introduced through companion Drop Down stem only. Never in toy chrome. |
| **Throughout (STRETCH, CHALLENGE)** | multiple, area, side length (all now active) | Module stem required at every production beat. |

### Vocabulary Notes

**"Multiple" introduction protocol:** The word appears for the first time in Beat 5 inside the sentence stem `___ is a multiple of ___ because ___ × ___ = ___`. Because equation overlays are suppressed inside Hundred Grid Mode B, the "because ___ × ___ = ___" clause is also the student's first encounter with the multiplication equation for a specific rectangle. Both the vocabulary anchor and the equation form arrive together in the stem — this pairing is intentional.

**"Rows" and "columns":** These are permitted informal terms throughout M01 (used in the concrete stem and row-structure scaffold). They are not formally introduced as mathematical vocabulary in M01.

**Toy-chrome vs. script separation:** The toy chrome stays simpler than the script: width / height / rows / squares language at the toy layer, while the script can introduce **multiple** in the companion stem.

### Terms to Avoid (Save for Later Modules)

| ❌ Term | Why it is forbidden in M01 student-facing copy |
|---------|------------------------------------------------|
| ❌ `factor` | Deliberately withheld per IM sequencing and Module Mapping v2 §M01. Belongs to M03. |
| ❌ `factor pair` | Same rationale. M03 territory. |
| ❌ `prime` | M04 (merged Prime and Composite Numbers) territory. |
| ❌ `composite` | M04 territory. |

*Engineering note: The §2.13 Hundred Grid Mode B M01 vocabulary fence flag suppresses all four terms from tooltips, stems, and overlays at the toy layer while the M01 mode flag is active.*

---

## 1.4 MISCONCEPTIONS

### 1.4.1 #U1.1: Tile-Counting by 1s Instead of Multiplying (PRIMARY)

**Global ID:** U1.1 (M1)
**Sources:** Phase 4 Research Summary §3 M1; Module Mapping v2 §6 Misconception Coverage Matrix; IM L1 Lesson Narrative (explicit flag).

The student places tiles one at a time and counts them individually (1, 2, 3, 4, …) rather than thinking in rows of a fixed number. This produces the correct area total but bypasses the multiplicative grouping that makes "a multiple of" conceptually meaningful. The student cannot transfer to M03 if they never formed the row-grouping concept.

**Observable signs:**
- Student places tiles one at a time without extending rows
- Student verbally or behaviorally counts every square instead of using rows of the same size
- Student states the total number of tiles correctly but cannot connect it to "side length × number of rows"

**Detection mechanism:** The **§2.13 Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4; replaces v3 Arrays Extension B) is active in both B-snap-OFF and B-snap-ON sub-states. This internal telemetry signal — never displayed to the student — broadcasts to the tutor layer when placement events are tile-by-tile rather than row/column handle extension.

**Three-Tier Remediation Ladder:**
- **Light:** On signal, the tutor layer highlights one already-completed row via §2.13 Mode B tutor-commanded row pulse. Prompt (vocabulary-fenced): "Look at this row — how many squares are in it?" No dimension label, area label, or equation is revealed.
- **Medium:** If tile-by-tile placement persists after Light, the tutor highlights a full row (all tiles pulse) and ghost-shows one full row extension from the current build, then returns control to the student. Scaffold stem: `I count ___ rows of ___ squares. ___ rows of ___ is ___`. Row-structure scaffold uses only M01-fenced language.
- **Heavy:** If tile-by-tile placement continues, the tutor presents a side-by-side comparison: one panel shows the student's tile-by-tile approach (animating individual tile adds), the other shows the row-extension approach (one handle drag fills an entire row). Prompt: "One of these builds the rectangle row by row. Which one builds faster?" No label reveals; no equation.

**Why high-stakes:** A student who exits M01 still counting by 1s lacks the multiplicative grouping concept, and M03's systematic search will feel arbitrary.

### 1.4.2 #M01-2: Row Size and Row Count Collapse Together (SECONDARY)

Some students can state the total area but blur the difference between "rows of 4" and "4 rows." This collapse weakens later equation reading: when the module stem requires the student to identify which numeric value names the side length and which names the row count, the conflated student picks at random. M01 addresses this by repeating both parts of the concrete stem and by pairing row highlights with "How many rows do you see?" and "How many squares are in each row?" as separate, sequential prompts — never combined into a single "how many altogether" question.

**Observable signs:** Student fills the stem's fixed-side-length blank with the row count, or vice versa. Student answers "rows" and "squares per row" with the same number unprompted.

**Intervention principle:** Always separate the two prompts in time. Highlight one row visually, ask "how many squares in this row?", then sweep across rows and ask "how many rows like this one?" before any stem completion.

### 1.4.3 #M01-3: Stem Completion Becomes Slot-Filling Instead of Meaning-Making (SECONDARY)

Students may try to fill the sentence stem from memory or guesswork without referencing the visible checked rectangle. M01 prevents this by leaving the checked rectangle visible during stem completion, delaying the stem until after Check, and keeping the teacher move tied to the visible labels and row structure. Incorrect stem entries trigger a "look back at the rectangle" redirect, never a direct answer reveal.

### 1.4.4 #U1.6: Equation Orientation Confusion (PREVENTION ONLY — addressed in M02)

**Global ID:** U1.6 (M6)
U1.6 is NOT a primary M01 instructional target. M01 deliberately introduces only `a × b = c` (standard orientation) so that M02 can introduce both orientations as its one new thing. M01's role with U1.6 is prevention: by keeping M01 to single-orientation only and explicitly suppressing any reversed-form display, M01 ensures U1.6 never gets accidentally seeded here. The Forbidden Phrases list explicitly prohibits any preview of the reversed form.

### 1.4.5 #U1.5: Later-Module Vocabulary Confusion (BACKGROUND — not a primary target)

**Global ID:** U1.5 (M5)
U1.5 is not a primary M01 target because M01 deliberately withholds the later-module vocabulary — there is nothing to confuse yet. The vocabulary fence that prevents U1.5 seeding is itself the M01 contribution to this misconception's arc. Formal vocabulary anchor introducing both later-module terms — and tying them to the dimensional roles (side length and area) — is sequenced into M03.

---

## 1.5 TOY SPECIFICATIONS

### 1.5.1 §2.13 Hundred Grid — Mode B (Primary Toy)

**Phase 6 v4 reference:** Digital_Toys_Interactables_v4.md §2.13 Mode B; sub-states added per SME follow-up 2026-04-27.

**M01 role:** Load-bearing rectangle host across all M01 beats (Beats 1–7 + documented alternative Beat 8). The single Concrete and Relational surface on the default M01 path. Activated with the M01 vocabulary fence flag ON.

**M01 does NOT use Arrays.** Arrays was deleted per SME 2026-04-27 directive ("Arrays should be removed — the hundred grid takes place of the needs of arrays in this unit"). The only Arrays references in this document are historical (§2.13 Mode B "replaces v3 Arrays Extension B" for the tile-by-tile detection signal).

**Module Configuration Table:**

| Configuration attribute | M01 setting |
|------------------------|-------------|
| **Primary host** | §2.13 Hundred Grid Mode B (Variable W×H Rectangle Build) |
| **Default entry sub-state** | B-snap-OFF (Concrete free-placement) |
| **Terminal sub-state** | B-snap-ON (Relational grid-snapped); transition via tutor-commanded snap-on toggle |
| **Snap-on toggle** | Tutor-commanded; never student-initiated; not reversible within student pass |
| **Fixed-side-length lock** | Active in Beats 4–7 (one dimension locked, the other student-built) |
| **Equation overlay (Mode C)** | SUPPRESSED throughout all M01 beats — Mode C activates only in M02 |
| **Free-side dimension label** | Hidden pre-Check; revealed post-Check unconditionally |
| **Area label** | Hidden pre-Check; revealed post-Check unconditionally |
| **Locked-side numeric label pre-Check** | ⚠️ See OQ-M01-LABELS-V4 — UNRESOLVED; engineering implements both behaviors behind label-visibility flag |
| **M01 vocabulary fence flag** | ON — toy chrome uses only "width / height / rows / squares" language; "multiple" appears exclusively in companion stem |
| **Tile-by-tile count detection signal** | ACTIVE in both B-snap-OFF and B-snap-ON sub-states |
| **Post-Check reveals on toy** | Dimension labels (W × H) and area label (center of rectangle); equation overlay remains SUPPRESSED |
| **"multiple" introduction point** | Companion Drop Down stem post-Check Beat 5, not toy chrome |
| **Sub-canvas fallback** | Active for side lengths 11–12 |

### 1.5.2 §2.10 Drop Down / Fill-in-the-Blank (Primary Companion Toy)

Present in every production beat. Sentence-stem mechanism for the module multiple stem and concrete stem. Linked values from Hundred Grid Mode B Check populate stem slots. Stem scaffolding arc: Pre-filled (linked values auto-pushed) → Partial (one or two blanks) → Blank (full production). Stems are required throughout this unit. Stem fading is deferred to a later iteration.

### 1.5.3 §2.11 Multiple Choice / Checkbox (Warmup Toy)

Used at Beat 1 (Warmup WODB) only and at recognition-style Exit Check / Practice items. No build-step scaffolding arc within M01 — serves the recognition entry beat and yields once production begins. Optional post-Check follow-up stem (`I chose ___ because ___`) is non-gating.

### 1.5.4 Open Questions and Flags

**OQ-M01-ENTRY-V4** *(Phase 6 v4 §6; SME follow-up 2026-04-27)*
Default M01 Concrete entry is §2.13 Hundred Grid Mode B / B-snap-OFF (single-toy). The legacy path via §2.3 Unit Square Tiles → §2.13 Mode B (cross-toy state transfer via the §2.3 "reveal grid overlay" trigger) is preserved as a documented authored alternative but is NOT the M01 default and is NOT authored into this starter pack. **Open Question:** Should the Unit Square Tiles alternative entry path be retained or fully demoted? Default until resolved: HG Mode B / B-snap-OFF is the sole authored M01 Concrete entry.

**OQ-M01-LABELS-V4** *(Phase 6 v4 §6; SME follow-up 2026-04-27)*
For Beat 4 and Beat 6 fixed-side-length builds, the pre-Check visibility of the **locked-side numeric label** is currently unresolved. Two conflicting behaviors exist in Phase 6 §2.13 Mode B. **Engineering instruction:** implement both candidate behaviors behind the label-visibility flag and expose for prototype A/B testing. Candidate (a): locked-side numeric label visible pre-Check. Candidate (b): all numeric labels hidden pre-Check. The free-side dimension label and area label are unconditionally hidden pre-Check regardless of flag setting.

---

### Interaction Constraints (All Toys)

**B-snap-OFF (default Concrete sub-state, Beat 2):**
- Tile placement: tap empty canvas area; tile renders at tap location with soft drop-shadow; placement is NOT grid-snapped
- Side handles: NOT exposed in B-snap-OFF
- Numeric cell labels: hidden (surface behaves as blank canvas, not numbered grid)
- Tile-by-tile count detection signal: active
- Undo: removes last tile placed (pre-Check only)
- Reset: clears all tiles; preserves W/H bounds, M01 mode flag, snap sub-state

**Snap-on toggle (Beat 3 — tutor-commanded):**
- Fires at authored beat progression or tutor routing decision; never student-initiated
- Each free-placed tile re-anchors to nearest grid coordinate via snap animation (smooth movement, not teleport)
- Ambiguous overlaps resolve to one tile per cell; extras silently removed with undo affordance
- Not reversible within student pass; Reset clears state for a fresh start
- Default M01 path: same-toy internal sub-state change (B-snap-OFF → B-snap-ON); NO second toy participates

**B-snap-ON (Relational sub-state, Beats 4–7):**
- Tile placement: grid-snapped
- Side handles: exposed; drag extends/contracts a full row or column simultaneously
- Locked-side label: see OQ-M01-LABELS-V4
- Free-side dimension label: hidden pre-Check; revealed post-Check unconditionally
- Area label: hidden pre-Check; revealed post-Check unconditionally
- Equation overlay: SUPPRESSED
- Tile-by-tile count detection signal: active

**Check (all beats):**
- Reveals: dimension labels (W × H) and area label in center of rectangle
- Does NOT reveal: equation overlay (suppressed in M01 mode throughout)
- After Check: companion Drop Down stem unlocks (Beat 5 onwards); linked values broadcast to stem slots

**Shared interaction grammar:** Check, Undo, Reset, tutor-controlled prompts, and linked highlighting when paired views are shown — constant across all M01 toys.

---

## 1.6 WARMUP (2–3 minutes)

### Core Purpose

**Key Function:** Activate rectangle-structure attention (rows, side lengths, area) before any tile placement occurs.

**Why this serves M01:** By presenting four rectangles that differ in structural properties — row count, side length, aspect ratio, area — and asking the student to identify which one does not belong with the others, the warmup primes the "rows and area" language that Beat 2 will formalize. The warmup preserves IM 2019 Grade 4 Unit 1 Lesson 1's "Which One Doesn't Belong?" activity as a tool-mediated, low-anxiety recognition task. The IM version relied on partner discussion; the M01 version substitutes a tap-and-companion-highlight interaction that preserves the recognition-before-production function without the classroom-social dependency.

**Necessity Test:** Removing this beat would leave students less prepared for Beat 2 — they would meet the Hundred Grid Mode B build surface without prior rectangle-structure recognition, increasing the rate of tile-by-tile counting (U1.1) at first contact and weakening the Concrete-to-Relational transition that follows.

No new vocabulary is introduced in the warmup. The word "multiple" is withheld until Beat 5. No equation form appears at any warmup beat.

---

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 2–3 minutes (60–90 seconds for W.1; 30–45 seconds for W.2; 15–20 seconds for bridge) |
| Toy(s) Used | §2.11 Multiple Choice / Checkbox (gating); §2.13 Hundred Grid Mode B (companion observation display, build affordances disabled); §2.10 Drop Down (non-gating optional follow-up) |
| Warmup Type | Which One Doesn't Belong (WODB) — Type 2 per Warmup Phase Playbook §4D |
| Tool interaction count | 1 gating tap (§2.11 option select + Check); 0 build interactions in warmup |
| Engagement Anchors | Choice (WODB structure: student selects which option doesn't belong) + Personalization / Prior Knowledge (Grade 3 area callback: at least one WODB option is a standard 3×4 or 4×3 rectangle recognizable from 3.MD.C.7.a work) |

### Constraints

| Constraint | Details |
|------------|---------|
| WODB authoring (WP.M01.1 / WT.M01.2) | All four options must be rectangle configurations where the "doesn't belong" reason is a structural rectangle property (row count, side length difference, area, or aspect ratio). No option may be trivially distinguishable by a non-mathematical visual attribute (e.g., the only option with a visible grid label, the only colored option). |
| Grade 3 callback (WE.M01.6) | At least one of the four WODB rectangles must be a standard 3×4 or 4×3 arrangement that Grade 3 students would recognize from area work (CCSS 3.MD.C). |
| Vocabulary fence | No M01 vocabulary-fence terms (the four later-module terms enumerated in §1.3) appear in any tutor copy, option label, or stem text. No equation form in Beat 1. The word "multiple" is not introduced at the warmup — it first appears in Beat 5. |
| U1.1 detection | OFF in Beat 1 — no tile placement occurs. |
| Companion display | §2.13 Mode B companion display loads with build affordances disabled; student observes rectangle structure only. |
| Follow-up stem | Use §2.10 Drop Down or §2.11 Multiple Choice only for the optional follow-up — no free-text response. |
| Bridge execution (WB.M01.4) | Companion Hundred Grid Mode B observation display transitions from prebuilt-observation mode (build affordances disabled) to B-snap-OFF mode (build affordances enabled) as Beat 2 begins. No vocabulary or concept is introduced in the transition. Session-relative language only. |

### Constraints — MUST / MUST NOT (per WD.M01.5)

**MUST:**
- Options authored for rectangle-structure discrimination (per WP.M01.1 / WT.M01.2)
- At least one WODB option is a standard 3×4 or 4×3 rectangle (Grade 3 area-work callback per WE.M01.6)
- Companion §2.13 Mode B display present in observation mode with build affordances disabled
- Bridge interaction (W.X) explicitly transitions companion Mode B from observation mode to B-snap-OFF (per WB.M01.4)
- Two engagement anchors active (Choice + Personalization/Prior Knowledge per WE.M01.10)

**MUST NOT:**
- Introduce any of the four M01 vocabulary-fence terms (enumerated in §1.3) — or the word "multiple" — in any warmup-facing text
- Render any equation form in any warmup beat
- Trigger U1.1 detection (no tile placement occurs)
- Use partner discussion or any classroom-social mechanism

### IM-Adaptation Decision Record (per WI.M01.3)

| Field | Value |
|-------|-------|
| **IM source** | "Which One Doesn't Belong?" warm-up, IM 2019 Grade 4 Unit 1 Lesson 1 |
| **Hidden skill target** | Rectangle recognition before production — PRESERVED via §2.11 tap-to-select with companion §2.13 Mode B linked highlight |
| **Classroom-dependency level** | HIGH — the IM version relies on partner discussion and community-reflection as the primary mechanism for surfacing why an option doesn't belong |
| **Decision** | **Transform** (social mechanism removed; tool-mediated recognition mechanism substituted) |
| **Rationale** | The recognition-before-production hidden skill is fully preservable through a tap-and-companion-highlight interaction, so the IM activity can be retained as a Mission 42 Warmup once the partner-discussion mechanism is replaced by a tool-mediated selection-with-visual-consequence pattern. Keep is rejected because the social mechanism cannot run on the platform; Drop is rejected because the recognition function is load-bearing for U1.1 priming into Beat 2. |

### Engagement Anchors

- **Choice:** the student chooses which rectangle does not belong via the WODB structure itself.
- **Personalization / Prior Knowledge:** at least one option is a familiar 3×4 or 4×3 rectangle that activates prior area knowledge from Grade 3 (CCSS 3.MD.C.7.a).

### Warmup Type Rationale

WODB (Type 2) is used for M01 rather than Binary Choice (the Warmup Playbook §4D default for Modules 1–3) for a content-specific reason: the IM 2019 source lesson uses WODB to instantiate the recognition-before-production mechanism directly, and the four-option format creates multiple valid structural attributes for students to notice (rows, side length, area, aspect ratio). This multi-attribute recognition load is intentional — it ensures students arrive at Beat 2 already attending to rectangle structure from at least one angle. Binary Choice would activate only one attribute and would not preserve the IM source's recognition breadth. This decision is documented per **KDD — Warmup type selection (WC.M01.8)** in Tool Flow Document v3.

---

### Interaction W.1: WODB Recognition [EXPOSURE]

**Setup:**
Four rectangles appear in a 2×2 grid via §2.11 Multiple Choice. Each rectangle is a prebuilt Hundred Grid Mode B observation display (build affordances disabled). A companion §2.13 Mode B display adjacent to the 2×2 grid is also in prebuilt-observation mode. Hook (curiosity gap, ≤15 words): "Four rectangles. Three go together. One is different. Which one?"

**Student Action:**
Student views all four rectangles — differing in row count, side length, area, or aspect ratio. Student taps the rectangle that does not share the property of the others, then taps Check. After Check, the tapped option is highlighted and the companion §2.13 Mode B display fires a linked highlight reflecting the student's selection. Optional non-gating follow-up stem surfaces via §2.10 Drop Down: `I chose ___ because ___` (pre-filled options; student selects reasoning without free text).

**Teacher Move:**
After Check, acknowledge the selection in observable terms without teaching: "You chose that one." or "Let's look at what you noticed." Do not evaluate or correct — WODB has no wrong answer in the warmup context. If the student selects the optional reasoning stem, acknowledge the selected reason briefly (5–10 words, observable only). Do not introduce vocabulary.

**Key Observation:**
Student uses structural language — rows, side, length, total squares, area — even informally. Any mention of row count or side-length difference signals readiness for Beat 2. *(Engineering note: if a student spontaneously uses any of the four fenced terms, the tutor should not correct it in the warmup; address the fence boundary at Beat 2 if needed.)*

**Common Detour:**
Student selects an option based on a non-structural visual cue (e.g., apparent size on screen, position in the grid) rather than a mathematical attribute. This is acceptable in the warmup (WODB is low-stakes). The bridge interaction will redirect attention to structure.

**Intervention:**
If student appears disengaged or taps randomly, the tutor acknowledges the selection and briefly names one structural property of the chosen rectangle in observable terms: "That one has ___ rows of ___ squares." Do not re-teach or evaluate. Continue to W.2.

**Next Move:**
Proceed to Interaction W.2 (Bridge to Lesson). The companion §2.13 Mode B observation display remains visible; the linked highlight from the student's selection persists briefly, then clears as the bridge begins.

**Duration:**
60–90 seconds (recognition-only; no production load).

---

### Interaction W.2: Bridge to Lesson [BRIDGE]

**Setup:**
The companion §2.13 Hundred Grid Mode B display — which the student observed during W.1 with build affordances disabled — transitions from prebuilt-observation mode to B-snap-OFF mode (build affordances enabled) as the bridge fires. This is a single sub-state change inside §2.13 Mode B: the same toy chrome remains on screen; only its build-enable flag flips and the prebuilt rectangle clears in preparation for student production. No new vocabulary or concept is introduced during the bridge.

**Student Action:**
Student observes the transition (the prebuilt rectangle disappears; the Mode B surface is now blank and ready for placement). This is an observational beat — no student production interaction required.

**Teacher Move:**
Optional brief session-relative tutor copy (non-gating, ≤15 words): "Now you'll build one." or "Your turn to build." No new vocabulary introduced. The word "multiple" is NOT introduced at the bridge — it first appears in Beat 5. *(Engineering note: M01 vocabulary fence holds in full at this beat; none of the four fenced terms appear in any tutor utterance.)*

**Key Observation:**
The bridge's function is transitional: the student sees the same Hundred Grid Mode B surface shift from observation mode to build mode, creating continuity between the warm-up rectangles they observed and the rectangle they are about to build. The §2.13 Mode B build-enable flag flip is the observable transition signal.

**Common Detour:**
None expected — this is an observational transition beat. Rare case: student attempts to tap before bridge animation completes; tap is silently absorbed.

**Intervention:**
If student appears confused by the transition animation, a single reassuring prompt suffices: "Same grid — now it's ready for your tiles." No further action.

**Next Move:**
Proceed to §1.7 Lesson, Beat 2 (Interaction L.1 — Concrete Build).

**Duration:**
15–20 seconds (transition only).

---

### Verification Checklist (Warmup)

- [ ] **W-WODB:** All four §2.11 options pass the rectangle-structure discrimination authoring constraint (no trivial non-mathematical contrast); at least one option is a standard 3×4 or 4×3 arrangement
- [ ] **W-Companion:** §2.13 Mode B companion display loads with build affordances disabled; linked highlight fires on student selection
- [ ] **W-Vocab:** No M01 vocabulary-fence terms (per §1.3) appear in tutor copy, option labels, or stem text; no equation form renders
- [ ] **W-Detection:** U1.1 detection is OFF in Beat 1 (no tile placement occurs)
- [ ] **W-Bridge:** Bridge transition (W.2) executes the §2.13 mode shift from observation mode to B-snap-OFF (build affordances enabled) as Beat 2 begins

---

## 1.7 LESSON (12–15 minutes)

### Core Purpose + Pedagogical Flow

The M01 lesson operationalizes the unit's Concrete entry: students physically build rectangles on §2.13 Hundred Grid Mode B, observe that the area of each rectangle is a product of its two side lengths, and then state that product as a "multiple of" the fixed side length through the module sentence stem. Three CRA sections unfold in sequence:

- **Section 1 (Concrete):** Free tile placement in B-snap-OFF establishes that a rectangle's area is determined by its rows and columns, not by counting individual tiles. This section directly addresses U1.1 through the row-structure scaffold.
- **Section 2 (Relational):** The snap-on toggle fires; the same rectangle re-anchors to the grid (B-snap-ON). Fixed-side-length lock engages. Students now build rectangles row by row using the handle, reading the structural organization the grid makes visible.
- **Section 3 (Abstract First Encounter):** The companion Drop Down stem produces the equation form for the first time — as a statement about the built rectangle. The word "multiple" enters the student's vocabulary anchored to a concrete artifact.

Required/Forbidden Phrases anchor the lesson by enforcing row-based language and blocking both vocabulary-fence violations and U1.1-reinforcing patterns. The Purpose Frame opens the lesson before any student action.

---

### Lesson Structure

| Phase | Duration | CRA Stage | Focus |
|-------|----------|-----------|-------|
| Purpose Frame | ~1 min | — | Teacher sets context; no student action |
| Section 1: Concrete Build | 4–5 min | Concrete | B-snap-OFF free tile placement; concrete stem; U1.1 scaffold |
| Section 2: Relational Build | 4–5 min | Relational | B-snap-ON fixed-side-length; row-extension handle; no equation in toy |
| Section 3: Abstract — First Stem | 3–4 min | Abstract (first encounter) | Companion Drop Down stem; "multiple" introduced; equation in stem |

---

### Required Phrases

* "Build a rectangle."
* "Build a rectangle that has a side length of ___."
* "Keep this side length the same."
* "Look at the rows."
* "Look at this row."
* "How many rows do you see?"
* "How many squares are in each row?"
* "How many rows of ___ do you see?"
* "Tap Check when your rectangle is ready."
* "The area is ___ square units."
* "___ is a multiple of ___ because ___ × ___ = ___."
* "Use the checked rectangle to fill the stem."
* "Try another rectangle with the same side length."

---

### Forbidden Phrases

❌ **"factor"** — fenced term; belongs to M03; using it now creates U1.5 vocabulary confusion before "multiple" is stable
❌ **"factor pair"** — same rationale; M03 territory
❌ **"prime"** — M04 territory
❌ **"composite"** — M04 territory
❌ **"multiply the two sides"** — premature abstraction; the area model must precede the equation; equation first appears in companion stem
❌ **"Just count every square one by one."** — directly reinforces U1.1; undermines row-based thinking
❌ **"count all the squares"** — same U1.1 risk; replaced by row-based language
❌ **"How many squares total?"** — implies tile-by-tile counting; replaced with "how many rows of ___"
❌ **"4 × 5 = 20 and 20 = 4 × 5"** — dual-orientation display is M02's one new thing; M01 is standard-orientation only
❌ **"This is the standard way; the other way is different."** — previews M02 framing
❌ **"We are finding every rectangle for this area."** — M03 territory
❌ **"You already know the product, so just fill it in."** — short-circuits the build; turns the rectangle into decoration instead of evidence
❌ **"Perfect!"** — SDT-incompatible generic enthusiasm; BrainLift DOK4 observable-only rule
❌ **"Amazing!"** — same rule
❌ **"You're so smart!"** — SDT-incompatible identity praise
❌ **"You understood it."** — inferred internal state the system cannot verify; BrainLift DOK4 observable-only rule
❌ **"You persisted."** — inferred internal state; same rule
❌ **"You paid attention."** — inferred internal state; same rule
❌ **"You thought carefully."** — inferred internal state; same rule

---

### Purpose Frame

Teacher opens lesson with this frame. No student action — teacher sets context, goal, relevance. Concrete language only. Why today matters.

> "You just saw four rectangles and noticed differences between them — things like how many rows they had or how long each row was. Now you're going to build your own rectangles on the grid, one row at a time. When you tap Check, you'll see how many squares you used — and we'll write a sentence that names what that area means. Everything we do today builds to one sentence: ___ is a multiple of ___ because ___ × ___ = ___. Let's build the first rectangle now."

---

### Section 1: Concrete Build — Free Tile Placement (CONCRETE)

The student places tiles freely on the Hundred Grid Mode B surface in B-snap-OFF mode. Numeric cell labels are hidden; grid-snap is off; side handles are not exposed. The surface behaves like a blank canvas with a light grid. The student's task: arrange a given number of tiles into a rectangle (no specified target area — just "make a rectangle"). After placement, the student taps Check; the snap-on toggle fires (Beat 3), and the concrete stem surfaces.

This section directly addresses U1.1 by giving the student the physical experience of placing tiles and then asking them to read the row structure — not just the total count. The concrete stem (`___ tiles fill ___ rows of ___, so the area is ___ square units`) encodes row-based thinking into a required production artifact.

---

### Interaction L.1: Free Tile Build — Find the Rectangle [EXPOSURE]

**Setup:**
§2.13 Hundred Grid Mode B is active in B-snap-OFF sub-state (numeric cell labels hidden, grid-snap off, side handles not exposed). Tutor prompt: "You have ___ tiles. Place them on the grid to make a rectangle, then tap Check." The tile count is authored (e.g., 12 tiles). No target dimensions specified — the student decides the arrangement. U1.1 detection is active.

**Student Action:**
Student taps or drags tiles onto the Mode B surface to form a rectangular arrangement with the given tile count. Tiles render at tap location with soft drop-shadow. Placement is not grid-snapped. Student taps Check when the rectangle is complete. If U1.1 detection signal fires (tile-by-tile placement without row structure), the row-structure scaffold activates (Light → Medium → Heavy per §1.4.1).

**Teacher Move:**
After Check, observe whether rows are formed. If tile-by-tile detection signal fired: redirect via the three-tier remediation ladder (§1.4.1). Do not reveal labels during remediation. Post-Check observable response: "Your rectangle has ___ tiles in ___ rows. Fill in the sentence."

**Key Observation:**
Student builds rows of equal length rather than placing tiles in arbitrary clusters. The concrete stem completion confirms row-structure reading: the student must distinguish "how many rows" from "how many tiles per row."

**Common Detour:**
Student places tiles in an L-shape or irregular cluster rather than a true rectangle. The Check button should not activate for non-rectangular configurations; the tutor prompts: "Tap the edge tiles and reshape so each row has the same number of squares."

**Intervention:**
If irregular shape persists, the tutor highlights one correctly formed row (row pulse per §2.13 Mode B) and prompts: "Make all rows look like this row." No equation, no label reveal.

**Next Move:**
After Check and concrete stem completion, proceed to L.2 (Concrete Readback with the Concrete Stem).

**Duration:**
2–3 minutes (placement + Check + concrete stem completion).

---

### Interaction L.2: Read the Built Rectangle with the Concrete Stem [CONCRETE READBACK]

**Setup:**
The checked rectangle remains visible. The concrete stem appears via §2.10 Drop Down: `___ tiles fill ___ rows of ___, so the area is ___ square units`. Numeric label reveals are paused at this beat — only the row count and row size are referenced.

**Student Action:**
Student uses the checked rectangle to fill the stem, selecting or entering the total tiles, number of rows, row size, and area. Student reads the completed stem aloud or silently with the visible rectangle in view.

**Teacher Move:**
Say: "Use the checked rectangle to fill the sentence. How many rows do you see? How many squares are in each row?" Keep the row count and row size separate in the prompts (defeats #M01-2 collapse).

**Key Observation:**
Student ties the built object to a structured sentence and distinguishes row count from row size. This separation is the M01-2 prevention move — never combine row count and row size into a single prompt.

**Common Detour:**
Student reverses the row count and row size (puts row count where row size goes), or fills the total slot from memory without referencing the picture.

**Intervention:**
Point back to the image verbally: "Count the rows first. Then tell how many squares are in each row." Do not advance until the two values are entered in the right slots.

**Next Move:**
Proceed to L.3 (Snap-On Transition / Beat 3).

**Duration:**
~2 minutes.

---

### Interaction L.3: Snap-On Transition — Same Rectangle, Grid-Snapped [TRANSITION]

**Setup:**
The snap-on toggle fires (tutor-commanded). The student's free-placed rectangle re-anchors to grid coordinates through a snap animation. Each tile moves from its loose position to a grid coordinate — smooth movement, not teleport. Ambiguous tile overlaps (if any) resolve to one tile per cell; extras silently removed with undo affordance. After the animation, the same §2.13 Hundred Grid Mode B surface is now in B-snap-ON. U1.1 detection continues active.

**Student Action:**
Student observes the snap animation. After the animation settles, the tutor highlights one row and prompts the student to tap a highlighted row or side to acknowledge the structure. This is a low-cognitive-load confirmation tap.

**Teacher Move:**
"Watch what happens to your rectangle — it's snapping into the grid. Same rectangle, easier to read." After the student's acknowledgment tap: "Do you see the rows? Every row has the same number of squares." No new vocabulary. No equation.

**Key Observation:**
Student's recognition that the snapped rectangle is "the same one" is the conceptual payload of this interaction — it establishes continuity between the Concrete (loose tiles) and Relational (grid-snapped) stages. If student expresses surprise at the shape change (e.g., tiles moved slightly), acknowledge it as part of the snap.

**Common Detour:**
Student expects a new rectangle to appear (thinks the snap is a reset). Reassure: "Your tiles just lined up — same number of squares, now organized in the grid."

**Intervention:**
No remediation needed for this beat; it is observational and guided. If the student is visibly confused, name continuity: "It has the same squares as before. Just easier to see now."

**Next Move:**
Proceed to L.4 (Fixed-Side-Length Build, B-snap-ON).

**Duration:**
45–60 seconds (transition + acknowledgment tap).

---

→ **SECTION 1 COMPLETE. PROCEED TO SECTION 2.**

---

### Section 2: Relational Build — Fixed Side Length (RELATIONAL)

The student builds new rectangles in B-snap-ON with a fixed side length locked. One dimension is locked by the authored activity; the other is student-built using the handle or cell taps. Tiles are grid-snapped. The locked-side label visibility follows the label-visibility flag (OQ-M01-LABELS-V4); the free-side dimension label and area label remain hidden until Check regardless of flag setting. Equation overlays remain SUPPRESSED. After Check, the module stem (Beat 5) unlocks — this is the student's first encounter with the equation form.

---

### Interaction L.4: Fixed-Side Build — Row Extension [ACTIVATION]

**Setup:**
§2.13 Hundred Grid Mode B is in B-snap-ON. Fixed-side-length lock is active (one dimension locked per authored task — e.g., side length = 4). Tutor prompt: "Build a rectangle where one side is ___ squares long. Drag the handle to extend the rectangle, then tap Check." Tile placement is grid-snapped. Side handle is exposed (B-snap-ON only). Locked-side label visibility governed by label-visibility flag (OQ-M01-LABELS-V4). Free-side label and area label are hidden until Check. U1.1 detection active.

**Student Action:**
Student drags the free-side handle (or taps cells) to extend the free dimension, building the rectangle one row at a time. Student taps Check when satisfied. Check reveals dimension labels (W × H) and area label at center. Equation overlay remains SUPPRESSED. Module stem (`___ is a multiple of ___ because ___ × ___ = ___`) unlocks for Interaction L.5.

**Teacher Move:**
Observe whether student uses the handle (row extension = multiplicative) or taps cells one at a time (tile-by-tile = U1.1 risk). If tile-by-tile detection fires in B-snap-ON: apply U1.1 remediation per §1.4.1 (row highlight + prompt "How many squares are in each row?"). Post-Check observable response: "Your rectangle is ___ wide and ___ tall. The area is ___ square units."

**Key Observation:**
Student uses the handle drag to extend a full row at once — this is the Relational-stage manifestation of row-based thinking. Handle drag is the observable signal that the student is thinking multiplicatively rather than by 1s.

**Common Detour:**
Student taps cells individually instead of using the handle, triggering U1.1 detection even in B-snap-ON. Apply U1.1 Medium remediation: row ghost-extension preview + scaffold stem.

**Intervention:**
"Try dragging the side of the rectangle to make it taller. Each drag adds a whole row at once."

**Next Move:**
Proceed to L.5 (Multiple Statement Stem — Abstract First Encounter).

**Duration:**
~2 minutes (build + Check).

---

→ **SECTION 2 COMPLETE. PROCEED TO SECTION 3.**

---

### Section 3: Abstract First Encounter — Multiple Statement (ABSTRACT)

The equation form appears for the first time — inside the companion Drop Down stem, not on the toy surface. The word "multiple" is introduced here. Because equations are suppressed on the Hundred Grid Mode B surface even post-Check, the "because ___ × ___ = ___" clause in the stem is the student's first encounter with the multiplication equation for this rectangle. The companion Mode B post-Check state (dimension labels + area label visible) remains on screen as reference while the student fills the stem.

---

### Interaction L.5: Multiple Statement Stem — First Completion [ACTIVATION]

**Setup:**
Hundred Grid Mode B is in post-Check state (dimension labels W × H and area label visible; equation overlay SUPPRESSED). The companion §2.10 Drop Down stem has unlocked: `___ is a multiple of ___ because ___ × ___ = ___`. At BASELINE, some slots are pre-filled via linked values from the Mode B Check (dimension values + area value auto-pushed); student confirms or fills remaining slots. At STRETCH/CHALLENGE, slots are blank (full production). Tutor prompt: "Now fill in the sentence about your rectangle."

**Student Action:**
Student taps each blank slot, selects from dropdown or types a numeric value, and taps Check on the stem. Linked slots (pre-filled values) are visually distinct from student-entered slots. If incorrect: the incorrect blank highlights in a distinct color without revealing the correct answer. Correct: all slots filled; stem confirms. Student reads the completed stem in context of the visible rectangle.

**Teacher Move:**
Post-Check correct: "Your sentence says ___ is a multiple of ___ because ___ × ___ = ___. That matches the rectangle you built." (Observable only — no "you understood," "you got it.") Incorrect slot highlight: "Check the area of the rectangle. Count the rows of ___."

**Key Observation:**
This is the moment "multiple" enters the student's vocabulary, anchored to a concrete artifact. The student should be able to point from the stem to the labeled rectangle: "The area is the first blank; the fixed side length is the second blank."

**Common Detour:**
Student fills the area blank and the side-length blank in reversed order (M01-3 / slot-filling pattern). Address by pointing to the labeled rectangle: "The area label is the big number. That's the number that is a multiple."

**Intervention:**
"Look at the rectangle. The area — the total squares — goes in the first blank. The side length — the fixed one — goes in the second blank. What's the area?"

**Next Move:**
BASELINE: Proceed to L.6 (additional fixed-side-length build, varied free dimension). STRETCH: Proceed to blank-build with a different fixed side length. CHALLENGE: Open-ended multiple discovery (find as many areas as possible for the given side length).

**Duration:**
~2 minutes (stem completion + Check).

---

### Interaction L.6: Second Fixed-Side Build — Varied Free Dimension [ACTIVATION]

**Setup:**
Same §2.13 Hundred Grid Mode B surface in B-snap-ON with the same fixed side length locked. Tutor prompt: "Build a different rectangle with the same side length. Drag the handle to a different height, then tap Check." This is the second production cycle; same module stem follows after Check.

**Student Action:**
Student builds a rectangle with the same fixed side length but a different number of rows — producing a different area. Taps Check; stem unlocks; student completes the stem with the new area and confirms that this area is also a multiple of the same side length.

**Teacher Move:**
After Check and stem completion: "You built two different rectangles with the same side length — ___ and ___. Both areas are multiples of ___. Every time you add a row of ___, you get the next multiple." (Observable, no inferred states.)

**Key Observation:**
Student recognizes that the two completed stems name different areas that are both multiples of the same side length. This is the seed of the "sequence of multiples" idea that M01 plants without naming it formally.

**Common Detour:**
Student builds the exact same rectangle dimensions as the first one. Prompt: "Try adding more rows — or fewer rows — to find a different area."

**Intervention:**
If student cannot vary the height, provide a target area: "Can you build a rectangle with the same side length and an area of ___?" (authored target; correct for the fixed side length.)

**Next Move:**
Proceed to §1.7 Exit Check Transition Frame, then §1.8.

**Duration:**
~2 minutes (build + Check + stem).

---

→ **SECTION 3 COMPLETE. PROCEED TO EXIT CHECK.**

---

### Misconception Prevention

**#U1.1 (Tile-Counting by 1s):** Addressed throughout the lesson:
- L.1 (Concrete Build): concrete stem requires students to articulate row count and rows-of count, not just total. U1.1 detection active; three-tier remediation available.
- L.2 (Concrete Readback): the concrete stem encodes row structure as a required artifact, not optional language.
- L.3 (Snap-On Transition): the snap animation makes row structure visually explicit — tiles line up into rows, making multiplicative grouping observable.
- L.4 (Fixed-Side Build): side handle drag is the Relational-stage observable of row-based thinking; U1.1 detection continues active in B-snap-ON.
- L.5–L.6 (Multiple Stem): the "because ___ × ___ = ___" clause in the stem requires students to identify the row count as the second multiplicand — directly operationalizing the multiplicative grouping that defeats U1.1.

**#M01-2 (Row Size and Row Count Collapse):** Addressed in L.2 and L.4 by always separating "How many rows?" and "How many squares are in each row?" into two distinct prompts. Never combine into a single "altogether" question.

**#M01-3 (Stem Slot-Filling Without Meaning):** Addressed in L.5–L.6 by keeping the checked rectangle visible during stem completion. Incorrect entries trigger a "look back at the rectangle" redirect, never a direct answer reveal.

**#U1.6 (Equation Orientation Confusion):** Prevention only in M01. All equation forms in M01 use standard orientation (`a × b = c`) exclusively. The Forbidden Phrases list prohibits any reversed-orientation display. Mode C is suppressed. M02 owns this misconception.

---

### Incomplete Script Flags (§1.7.4)

🚩 If teacher skips L.1 (Concrete Build in B-snap-OFF), students will meet the grid-snapped surface without prior free-placement experience — missing the U1.1 scaffold that B-snap-OFF provides and weakening the conceptual continuity of the snap-on transition.

🚩 If teacher skips L.2 (Concrete Readback) or skips the row-focused redirect within L.1, the lesson can devolve into tile counting and the row count / row size separation never lands.

🚩 If teacher skips L.3 (Snap-On Transition), students will not experience the continuity between the Concrete and Relational stages — the "same rectangle, easier to read" moment is load-bearing for CRA coherence.

🚩 If teacher skips L.5 (Multiple Statement Stem) or allows it to complete without requiring all slots, students will not encounter the word "multiple" anchored to a built rectangle. The vocabulary anchor is the lesson's primary learning output.

🚩 If the U1.1 remediation scaffold (tile-by-tile detection → row highlight → row-based prompt) is bypassed or replaced with equation reveal, students may produce correct answers without forming multiplicative grouping.

🚩 If the required phrases are replaced by looser paraphrases, the vocabulary fence and row-structure emphasis may erode.

---

### Success Criteria (§1.7.5)

✅ Student builds at least two rectangles on Hundred Grid Mode B (one Concrete / B-snap-OFF, at least one Relational / B-snap-ON) without triggering the U1.1 remediation scaffold at Heavy level.

✅ Student completes the concrete stem `___ tiles fill ___ rows of ___, so the area is ___ square units` with correct values after the B-snap-OFF build.

✅ Student completes the module stem `___ is a multiple of ___ because ___ × ___ = ___` with correct values for at least one rectangle.

✅ Student varies the free dimension across two builds with the same fixed side length, producing two different areas — both named as multiples in completed stems.

✅ Student can tell what stayed the same and what changed across two rectangles with the same fixed side length.

✅ No fenced vocabulary appears in any student production (student-entered slots, stem completions).

---

### Verification Checklist (Lesson)

- [ ] **L-Purpose:** Teacher opens with concrete Purpose Frame before any student action
- [ ] **L-CRA:** All three CRA stages are present; Concrete (B-snap-OFF) precedes Relational (B-snap-ON) precedes Abstract first encounter (Drop Down stem with "multiple")
- [ ] **L-Phrases:** Required phrases appear at appropriate beats; "Look at the rows," "___ is a multiple of ___," and "Try another rectangle with the same side length" appear at least once each
- [ ] **L-Fence:** No fenced vocabulary in any tutor copy, student prompt, stem option, or feedback text
- [ ] **L-Misconceptions:** U1.1 detection active in both B-snap-OFF and B-snap-ON; three-tier remediation ladder available; Heavy remediation uses side-by-side comparison, not equation reveal
- [ ] **L-Stem:** Module stem appears in every production beat starting at L.5; stems are required throughout this unit
- [ ] **L-Equation:** No equation overlay renders on Hundred Grid Mode B at any beat including post-Check; equation form appears only inside companion Drop Down stem
- [ ] **L-Continuity:** The same rectangle host carries the B-snap-OFF to B-snap-ON transition
- [ ] **L-Closure:** Lesson ends with Success Criteria confirmed and bridge to Exit Check ("Now you're ready to show me what you can do on your own")

---

## 1.8 EXIT CHECK (3–5 minutes)

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 3–5 minutes |
| Problem Count | 3 problems |
| Toy(s) Used | §2.11 Multiple Choice (EC.1); §2.13 Hundred Grid Mode B observation display (EC.2); §2.13 Hundred Grid Mode B / B-snap-ON build surface (EC.3) + §2.10 Drop Down |
| Mastery gate | 2/3 or 3/3 → proceed to Practice; 1/3 → intervention options; 0/3 → path switch strongly recommended |
| Vocabulary fence | Holds across all Exit Check items: no M01 vocabulary-fence terms (per §1.3) |
| Stems required | Module stem required on all production items |

### Constraints

| Constraint | Details |
|------------|---------|
| Lesson boundary | All EC problems test only what was taught in §1.7. No new visual models, orientations, or complexity introduced. |
| Cognitive type ceiling | EC uses IDENTIFY, CREATE, and CONNECT/TRANSFER only (per M01's position as Module 1 in the unit) |
| Transfer gate | At least one EC item must be CONNECT/TRANSFER (per Rulebook v6) — EC.2 serves this function |
| Equation orientation | Standard form only (`a × b = c`) — no reversed form |
| Mode C | Suppressed; no dual-orientation display |
| Independence Level | Light prompt only; no re-teaching during EC |
| Expression rule | Equation appears in the stem, not as an in-toy overlay |

### Alignment Check

| Exit Check Problem | L1 (Find area, explain multiple) | L2 (Fixed side length → multiples sequence) | Module Goal | Notes |
|-------------------|----------------------------------|----------------------------------------------|-------------|-------|
| EC.1 | ✓ | | ✓ | Recognition of multiple relationship from rectangle structure |
| EC.2 | ✓ | ✓ | ✓ | Transfer gate — stem completion from prebuilt rectangle |
| EC.3 | ✓ | ✓ | ✓ | Build + produce; STRETCH tier |

---

### EC Rectangle Selection

EC.1 uses three prebuilt rectangles (§2.11 Multiple Choice display); one has area that is a multiple of the named side length, two are distractors.
EC.2 uses a single prebuilt rectangle on §2.13 Mode B observation display (4×6 = 24; labels visible post-Check).
EC.3 uses §2.13 Mode B / B-snap-ON with fixed-side-length lock = 5; student builds free dimension to reach area = 30 (5 × 6).

---

### Transition Frame

> "You built rectangles with the same side length and wrote sentences about the areas. Now I want to see what you can do on your own. These three problems are for you to complete independently."

---

### EC.1: Rectangle Recognition — Which Is a Multiple? [IDENTIFY]

**Setup:**
Three rectangles presented via §2.11 Multiple Choice on a single screen: a 3×4 rectangle (area = 12, a multiple of 3); a 2×5 rectangle (area = 10, not a multiple of 3); a 1×7 rectangle (area = 7, not a multiple of 3). Build affordances disabled across all three. Tier: BASELINE.

**Student Action:**
Student reads the prompt — "Here are three rectangles. One of them has an area that is a multiple of 3. Tap that rectangle, then tap Check." — taps the chosen rectangle, then taps Check.

**Teacher Move:**
Light prompt only. Post-Check correct response: "Your rectangle has 3 rows of 4 squares. The area is 12. That is a multiple of 3." Post-Check incorrect (Light remediation): "Look at the number of rows in each rectangle. Which one has rows of 3 squares?" No re-teaching.

**Key Observation:**
Student uses rectangle structure (rows × side length) to recognize a valid multiple relationship without building. Mastery component: CONCEPTUAL (recognition).

**Common Detour:**
Student picks based on overall visual size ("looks bigger") rather than row structure.

**Intervention:**
Brief redirect to row structure: "Look at the rows. Which rectangle shows rows of 3 squares?" Do not reveal the correct option.

**Next Move:**
Advance to EC.2 (Transfer Gate item).

**Duration:**
45–60 seconds.

---

### EC.2: Stem Completion from Prebuilt Rectangle [CONNECT]

**Setup:**
A 4×6 rectangle is shown on a §2.13 Hundred Grid Mode B observation display (prebuilt; build affordances disabled; labels visible: W=4, H=6, area=24 in center). After the student taps Check to confirm observation, the stem unlocks via §2.10 Drop Down. Tier: BASELINE. Transfer Gate: this item satisfies the Rulebook v6 Transfer Gate requirement (must pass 1+ APPLY or CONNECT item).

**Student Action:**
Student fills the module stem `___ is a multiple of ___ because ___ × ___ = ___` from the visible rectangle. At BASELINE, some blanks are pre-filled via linked values; student confirms or fills remaining. Correct stem: `24 is a multiple of 4 because 4 × 6 = 24`. Student taps Check.

**Teacher Move:**
Light prompt: "Use the checked rectangle to fill the sentence." Post-Check correct: "Your sentence says 24 is a multiple of 4 because 4 × 6 = 24. That's what the rectangle shows." Post-Check incorrect: incorrect blank highlights in a distinct color without revealing the correct answer; redirect: "Check the area of the rectangle. Count the rows of 4."

**Key Observation:**
Student translates a visible rectangle into the module statement without additional teaching. Mastery component: TRANSFER.

**Common Detour:**
Student enters a correct area but mismatches the side length named in the sentence (M01-3 slot-filling pattern).

**Intervention:**
Brief structure prompt only: "Start with the area, then look back to the side length you are naming in the sentence." No direct answer reveal.

**Next Move:**
Advance to EC.3 (build-plus-transfer).

**Duration:**
60–75 seconds.

---

### EC.3: Build and Produce — Fixed Side Length [CREATE + CONNECT]

**Setup:**
§2.13 Hundred Grid Mode B / B-snap-ON; fixed-side-length lock = 5; labels hidden pre-Check; equation overlay SUPPRESSED. Companion §2.10 Drop Down stem ready to unlock at Check. Tier: STRETCH. Prompt: "Build a rectangle that has a side length of 5 and an area of 30. Tap Check when you are done, then fill in the sentence."

**Student Action:**
Student extends the free dimension via row-extension handle to reach area 30 (i.e., 6 rows of 5). Student taps Check; labels reveal (W=5, H=6, area=30). Stem unlocks. Student fills `___ is a multiple of ___ because ___ × ___ = ___` to produce `30 is a multiple of 5 because 5 × 6 = 30` and taps Check on the stem.

**Teacher Move:**
Light prompt: "Build the rectangle first. Then use the checked rectangle to fill the sentence." Post-Check correct: "Your rectangle is 5 squares wide and 6 squares tall. The area is 30. 30 is a multiple of 5 because 5 × 6 = 30." Post-Check incorrect build (Medium remediation): "Check the number of rows. You need 6 rows of 5 to reach 30. Try adding one more row." Do not reveal target dimensions directly.

**Key Observation:**
Student produces a valid build and a valid multiple statement independently. Mastery components: PROCEDURAL (build) + TRANSFER (stem).

**Common Detour:**
Student makes an off-target build (e.g., 5×5 = 25 or 5×7 = 35) or finishes the build but cannot complete the sentence correctly.

**Intervention:**
Brief redirect: "Check the side length that stayed the same and count how many rows of that side you made." If still off-target after one redirect, mark item as Needs Practice and route to Practice intervention path.

**Next Move:**
Record mastery state across all three EC items and route to §1.8.5 Practice (or intervention).

**Duration:**
~90 seconds.

---

### EC Verification Checklist

- [ ] **EC-Alignment:** Each exit check item maps to specific lesson content taught in §1.7; all three items test the same core concept (rectangle area as a multiple)
- [ ] **EC-Independence:** EC.3 student builds without toy support; EC.1–EC.2 use prebuilt/observation displays only; tutor uses light prompts only
- [ ] **EC-Language:** Module stem required on EC.2 and EC.3; no fenced vocabulary in any item, prompt, or feedback
- [ ] **EC-Transfer:** EC.2 satisfies the Rulebook v6 Transfer Gate requirement (CONNECT cognitive type)
- [ ] **EC-Readiness:** Passing grade (2/3+ with Transfer Gate item among correct items) indicates readiness for Practice

---

## 1.8.5 PRACTICE INPUTS

### Practice Phase Overview

Practice builds fluency in the core M01 skill: building rectangles with a fixed side length on Hundred Grid Mode B and completing the module sentence stem for each. The adaptive distribution (40% BASELINE / 45% STRETCH / 15% CHALLENGE) reflects the Module Mapping v2 P/C/T balance. Practice runs 10–12 problems per attempt; max 2 attempts before automatic path switch. No early exit (Rulebook v6 anti-gaming rule). Transfer gate: must pass 1+ APPLY or CONNECT item. SUPPORT and CONFIDENCE items do not count toward mastery.

Stems are required throughout this unit. Stem fading is deferred to a later iteration. Every counted practice item that involves production uses the module stem or (for SUPPORT items) the concrete stem.

---

### Distribution Targets

| Problem Type | Count | Rationale |
|--------------|-------|-----------|
| BASELINE / CONCEPTUAL (IDENTIFY) | 4–5 | Recognition of multiples from prebuilt rectangles; builds Module Mapping P=40% baseline |
| BASELINE / PROCEDURAL (CREATE) | 2 | Partial-build with fixed side length; reinforces row-based construction |
| BASELINE / TRANSFER (CONNECT) | 1 | Stem completion from prebuilt rectangle; ensures Transfer Gate coverage |
| STRETCH / PROCEDURAL (CREATE) | 3–4 | Blank-build with varied fixed side length; matches Module Mapping C=45% |
| STRETCH / TRANSFER (APPLY) | 2 | Real-world context; multiple identification in context |
| CHALLENGE (APPLY/bonus only) | 1–2 | Open-ended rectangle discovery; no-early-exit from authored sequence |
| SUPPORT (non-counting) | 1 | Pre-built observation with both dimensions labeled; inserted after 2 consecutive wrong |
| CONFIDENCE (non-counting) | 1 | Simple yes/no multiple identification with fully pre-filled stem; inserted after SUPPORT fails |

---

### Toy Constraints

| Constraint | Details |
|------------|---------|
| Primary build surface | §2.13 Hundred Grid Mode B exclusively (B-snap-ON for all build items in Practice) |
| Equation overlay | SUPPRESSED throughout all Practice items in M01 mode |
| Stem | Module stem required on all production items; SUPPORT items may use concrete stem |
| Vocabulary fence | Holds across all Practice items; no M01 vocabulary-fence terms (per §1.3) |
| Recognition items | §2.11 Multiple Choice or §2.13 Mode B observation display |
| Context items (STRETCH/APPLY) | Grade 4-appropriate real-world contexts only; verified-correct area values; on-scale data |
| Problem count | 10–12 |
| Max attempts | 2 |
| No early exit | Required (Rulebook v6) |
| Transfer gate | At least one APPLY or CONNECT item must be passed |
| Stem presence | Stems remain present throughout this unit |

---

### Dimension Constraints

- **BASELINE fixed side lengths:** 2–6
- **STRETCH fixed side lengths:** 2–10
- **CHALLENGE fixed side lengths:** up to 12 (sub-canvas fallback active for 11–12)
- **Maximum area per activity:** 120 square units (12 × 10)
- **No early exit** from any authored CHALLENGE sequence (Rulebook v6 / Mastery Framework v3)
- **Avoid repeating exact EC.1–EC.3 dimension pairs** in Practice

### Available Rectangle Pool (for Pipeline)

Side lengths 2–10 as fixed dimension; free dimensions 1–10; all resulting areas verified multiples of the fixed side length. For side length = 11 or 12, sub-canvas fallback per §2.13 Mode B.

---

### Dimensions Used Tracking (EC + Practice)

| Used in EC | Fixed side | Area | Free dim |
|------------|-----------|------|---------|
| EC.1 | 3 | 12 | 4 |
| EC.2 (prebuilt) | 4 | 24 | 6 |
| EC.3 | 5 | 30 | 6 |

Practice items should vary the fixed side length away from 3, 4, 5 in the first rotation to build generalization across multiple side-length values.

---

### Practice Item Templates (representative)

**P1 — BASELINE / CONCEPTUAL (IDENTIFY)**
*Which area is a multiple of 6? A) 14 B) 24 C) 35 D) 41*
Correct: B (6 × 4 = 24). Stem after Check: `24 is a multiple of 6 because 6 × 4 = 24`

**P2 — BASELINE / PROCEDURAL (CREATE)**
*Build a rectangle with a side length of 3. Make the area equal to 15. Tap Check.*
§2.13 Mode B / B-snap-ON; fixed side = 3; student builds free dimension to 5. Stem: `15 is a multiple of 3 because 3 × 5 = 15`

**P3 — BASELINE / TRANSFER (CONNECT)**
*Fill in: ___ is a multiple of ___ because ___ × ___ = ___ (showing a prebuilt 7×3 = 21 rectangle)*
Stem: `21 is a multiple of 7 because 7 × 3 = 21`

**P4 — STRETCH / PROCEDURAL (CREATE)**
*Build a rectangle with a side length of 8 and an area of 40. Tap Check.*
Fixed side = 8; student builds free dimension to 5. Stem: `40 is a multiple of 8 because 8 × 5 = 40`

**P5 — STRETCH / TRANSFER (APPLY)**
*A garden has rows that are each 6 feet long. The garden's area is 54 square feet. How many rows are there? Fill in: 54 is a multiple of 6 because 6 × ___ = 54*
Answer: 9 rows. Stem: `54 is a multiple of 6 because 6 × 9 = 54`

**P6 — STRETCH / TRANSFER (CONNECT)**
*Here is a rectangle on the grid. The area is shown. Write the complete sentence.*
Prebuilt §2.13 Mode B display showing a 9×4 = 36 rectangle. Stem: `___ is a multiple of ___ because ___ × ___ = ___`
Answer: `36 is a multiple of 9 because 9 × 4 = 36`

**P7 — SUPPORT (non-counting; does not count toward mastery)**
*A rectangle has 2 rows of 5 squares. The area is ___.*
Prebuilt §2.13 Mode B observation display with 2 rows highlighted. Concrete stem: `___ tiles fill ___ rows of ___, so the area is ___ square units`
Answer: `10 tiles fill 2 rows of 5, so the area is 10 square units`

**P8 — BASELINE / CONCEPTUAL (COMPARE)**
*Which two rectangles both show areas that are multiples of 4?* (§2.11 Multiple Choice / Checkbox; two correct: 4×3=12, 4×7=28; one distractor: 3×5=15)
After Check: `___ is a multiple of 4 because 4 × ___ = ___` for each correct selection.

**P9 — STRETCH / TRANSFER (APPLY)**
*A banner is 9 inches wide. The area of the banner is 72 square inches. How long is the banner? Fill in: 72 is a multiple of 9 because 9 × ___ = 72*
Answer: 8 inches. Stem: `72 is a multiple of 9 because 9 × 8 = 72`

**P10 — CHALLENGE (bonus only; no early exit)**
*Find three different areas that are multiples of 5. Build each rectangle on the grid, then fill in the sentence for each.*
Three separate Build + Check + Stem cycles on §2.13 Mode B; fixed side = 5. No early exit from the authored sequence.

**P11 — SUPPORT (inserted after 2 consecutive wrong)**
*Here is a rectangle. It has ___ rows and ___ squares in each row. The area is ___.*
Prebuilt observation-mode §2.13 Mode B; both dimensions labeled; concrete stem. Does not count toward mastery.

**P12 — CONFIDENCE (inserted after SUPPORT fails)**
*This rectangle has a side length of 2 and an area of 6. Is 6 a multiple of 2? Yes or No?*
§2.11 Multiple Choice; correct = Yes; post-Check stem pre-filled: `6 is a multiple of 2 because 2 × 3 = 6`. Does not count toward mastery.

**Practice Sentence-Stem Requirements:**
- Every counted explanation item uses `___ is a multiple of ___ because ___ × ___ = ___`
- SUPPORT items may also re-use `___ tiles fill ___ rows of ___, so the area is ___ square units`
- Stems are required throughout this unit. Stem fading is deferred to a later iteration.

---

## 1.9 SYNTHESIS (6–8 minutes)

### Parameters

| Parameter | Value |
|-----------|-------|
| Duration | 6–8 minutes |
| Toy(s) Used | §2.13 Hundred Grid Mode B (observation displays only — no new builds); §2.11 Multiple Choice for reflection selections; §2.10 Drop Down for stem recap |
| Student Grouping | Individual (1-on-1 digital tutor context) |
| Interaction Count | 2 connection tasks + 1 metacognitive reflection + 1 identity closure |

### Constraints

| Constraint | Details |
|------------|---------|
| No new teaching | Synthesis connects and generalizes; does not introduce new procedures or vocabulary |
| Vocabulary fence | Holds throughout synthesis: no M01 vocabulary-fence terms (per §1.3) |
| Observable language only | No inferred internal states in tutor copy; BrainLift DOK4 observable-only rule |
| M02 bridge | Synthesis previews M02 by referencing the equation form the student already produced ("Next time, you'll write the same equation a different way") — but does NOT reveal the reversed orientation `c = a × b`; that is M02's one new thing |
| Remediation | Light redirects only; if student needs more than a brief redirect, they were not ready for Synthesis |
| Closure style | Growth in demonstrated capability, not identity praise |

---

### Opening Frame [No Student Action]

Tutor references what the student actually did in the module — specific, system-tracked facts only. No inferred states.

> "In this module, you built rectangles on the grid and found areas that are multiples of a side length. You filled in sentences like '20 is a multiple of 4 because 4 × 5 = 20.' You built at least two different rectangles — both times, the area was a multiple of the same side length. Let's look at what that tells us."

---

### Connection Task S.1: Pattern Across Multiples [PATTERN DISCOVERY]

**Setup:**
Three rows of data appear, showing three completed stems from the student's session (specific values drawn from the student's actual session if available; otherwise authored examples):
- Row 1: `12 is a multiple of 4 because 4 × 3 = 12`
- Row 2: `16 is a multiple of 4 because 4 × 4 = 16`
- Row 3: `20 is a multiple of 4 because 4 × 5 = 20`

**Student Action:**
Student examines the three rows and selects from §2.11 Multiple Choice options: "They all go up by 4," "They are all even," "They are all the same," "I'm not sure." Student taps Check.

**Teacher Move:**
Prompt: "Look at all three sentences. What do you notice about the first blank in each one — the area number?" Post-selection (any selection): "You noticed that every time you added one more row of 4 squares, the area went up by 4. That's what multiples do — they go up by the same amount each time." (Observable — refers to what the data shows, not what the student thought.)

**Key Observation:**
This is the "sequence of multiples" insight seeded in M01 without formally naming it. The pattern prepares the conceptual ground for M03's systematic search.

**Common Detour:**
Student notices only the totals and misses the fixed-side-length relationship.

**Intervention:**
Light redirect: "Find the side length that matches in all three pictures. Now compare the rows."

**Next Move:**
Proceed to S.2 (real-world bridge).

**Duration:**
~1.5 minutes.

---

### Connection Task S.2: Real-World Bridge [REAL-WORLD CONNECTION]

**Setup:**
A brief real-world scenario appears with a visual (§2.13 Mode B observation display or illustrated image): "A bookshelf has rows of books. Each row holds 7 books. There are some rows on the shelf. Which of these could be the total number of books on the shelf?"

Options (§2.11 Multiple Choice): A) 23 books, B) 28 books, C) 31 books, D) 35 books.

**Student Action:**
Student selects one or more options that could be a valid total. Expected response: B (4 × 7 = 28) or D (5 × 7 = 35) — either is correct. Student taps Check.

**Teacher Move:**
Post-Check: "28 is a multiple of 7 because 7 × 4 = 28. 35 is also a multiple of 7 because 7 × 5 = 35. Both could be on the shelf. Multiples of 7 show up everywhere rows of 7 things appear." (Observable connection to real world; no inferred states.)

**Key Observation:**
Student applies the multiple concept in a non-grid context, demonstrating transfer. Any valid response (with correct reasoning) should be affirmed.

**Common Detour:**
Student selects 23 or 31 (not multiples of 7), reasoning from "feels close enough."

**Intervention:**
Light redirect: "Try counting by 7s: 7, 14, 21, 28, 35. Which of the options shows up when you count by 7s?"

**Next Move:**
Proceed to S.3 (metacognitive reflection).

**Duration:**
~1.5 minutes.

---

### Metacognitive Reflection S.3: Tool Preference [REFLECTION]

**Setup:**
Type 3 — Tool/Approach Preference; appropriate for M01 as an early module per Synthesis Playbook §3E. Prompt: "You built rectangles two ways today — first placing tiles freely, then using the handle to extend full rows. Which way helped you see the rows more clearly?"

Options (§2.11 Multiple Choice): A) Placing tiles one by one, B) Dragging the handle to extend a full row, C) Both ways helped equally, D) I'm not sure yet.

**Student Action:**
Student selects one option and taps Check. No correct answer; reflection is not graded.

**Teacher Move:**
- "Placing tiles" → "When you placed tiles, you had to decide where each one went — that takes focus. Good to know how you think." (Observable.)
- "Dragging the handle" → "Dragging the handle adds a whole row at once. That makes the row structure easier to see." (Observable.)
- "Both" → "Different moments, different tools — that kind of flexibility helps."
- "Not sure" → "Still figuring it out is fine. You'll notice over time."

**Key Observation:**
Student articulates a preference grounded in their actual session experience. The reflection itself — not the chosen option — is the artifact.

**Common Detour:**
Student picks randomly or always picks "Not sure."

**Intervention:**
None — reflection is non-gating. If student picks "Not sure" repeatedly across the module, log for tutor review.

**Next Move:**
Proceed to S.4 (identity closure + M02 bridge).

**Duration:**
~1 minute.

---

### Identity-Building Closure S.4 + M02 Bridge [No Student Action]

**Setup:**
A familiar checked rectangle remains visible for continuity. No new toy demand. The tutor speaks; student listens.

**Student Action:**
None — closure is teacher-spoken.

**Teacher Move:**
> "You built rectangles where one side stayed the same, and you found different areas — all multiples of that side length. You can write: ___ is a multiple of ___ because ___ × ___ = ___. In the next module, you're going to look at one of those rectangles one more time — and write the same equation in a second way. You'll be ready because you already know what the equation means."

(Vocab-fence holds across the closure — no M01-fenced terms appear. The bridge to M02 mentions "write the equation in a second way" without previewing the reversed orientation `c = a × b` — that is M02's one new thing.)

**Key Observation:**
Closure references what the student observably built and produced. M02 preview creates anticipation without revealing the new idea.

**Common Detour:**
Student asks for the next module's new equation form right away.

**Intervention:**
"The rectangle will stay familiar. The new sentence comes next time."

**Next Move:**
Close the module and hand off to the next authored sequence.

**Duration:**
~1 minute.

---

### Synthesis Verification Checklist

- [ ] **S-Connection:** At least two connection tasks (S.1 pattern discovery, S.2 real-world bridge) connect module learning to broader math or real world
- [ ] **S-Reflection:** S.3 metacognitive reflection included; student articulates which tool/approach helped
- [ ] **S-Identity:** S.4 identity closure specifically references what the student built and produced (observable); no generic praise
- [ ] **S-Bridge:** S.4 previews M02 goal without revealing the reversed orientation — bridge creates anticipation without teaching
- [ ] **S-Fence:** No fenced vocabulary appears in any synthesis task, reflection option, or closure text
- [ ] **S-Observable:** No inferred internal states in any tutor copy throughout synthesis

---

### Incomplete Script Flags (Synthesis)

🚩 If teacher skips S.1 (Pattern Across Multiples), students miss the "areas go up by the fixed side length" insight that seeds the M03 systematic search — the most forward-pointing conceptual output of M01 Synthesis.

🚩 If teacher skips S.4 identity closure, the bridge to M02 is absent and the module ends without a forward connection — M02's warmup will have no prior anchor to reference.

🚩 If S.4 over-previews M02 by revealing the reversed orientation, M02 loses the clean reveal of its one new thing.

---

## 1.10 KEY DESIGN DECISIONS (KDD)

### Purpose

KDDs document non-obvious choices that hold the module together — design trade-offs, pedagogical moves, and constraint decisions that a reader unfamiliar with M01 needs in order to understand the "why" behind structural choices. These are not content summaries; they are rationale records.

---

### KDD-1: M01 Vocabulary Fence — Withhold the Four Later-Module Terms

These four terms do not appear in any M01 student-facing copy: not in tutor prompts, stem options, dropdown lists, tooltips, or feedback text. "multiple" is M01's only intentional new vocabulary anchor.

Module Mapping v2 §M01 narrative: "Vocabulary 'factor' and 'factor pair' are deliberately withheld here — IM's own sequencing — to prevent vocabulary overload at the conceptual entry point." Introducing this vocabulary while the student is forming the area-model-to-multiple connection would create U1.5 (vocabulary confusion) before meaning is established. The two M04-territory terms belong to M04.

*Traces to:* Module_Mapping_v2.md §M01 narrative; Digital_Toys_Interactables_v4.md §2.13 Mode B M01 vocabulary fence flag; Tool Flow Document v3 §1.

---

### KDD-2: §2.13 Hundred Grid Mode B Is the Sole Rectangle Host in M01

M01 uses §2.13 Hundred Grid Mode B exclusively for all rectangle-building work (Concrete and Relational). §2.1 Arrays was deleted per SME 2026-04-27 directive. Unit Square Tiles is documented only as an authored alternative under OQ-M01-ENTRY-V4, not authored into this starter pack.

SME directive: "Arrays should be removed — the hundred grid takes place of the needs of arrays in this unit." The v4 §2.13 Mode B sub-states (B-snap-OFF / B-snap-ON with tutor-commanded snap-on toggle) absorb every formerly Arrays-hosted role. Single-toy design reduces cognitive load (BrainLift DOK3: "The fewer manipulatives that need to be made the better").

*Traces to:* Tool_Flow_Document_v3.md §1; Digital_Toys_Interactables_v4.md §2.13 Mode B; SME directive 2026-04-27.

---

### KDD-3: Equation Overlay (Mode C) Suppressed Throughout M01; Equation First Appears in Companion Stem

No `a × b = c` overlay renders inside §2.13 Hundred Grid Mode B at any beat in M01, including post-Check. The equation form first appears to the student inside the Drop Down module stem's "because ___ × ___ = ___" clause.

BrainLift DOK3: "Expression display (e.g., 3 × 5 = 15) in a manipulative should appear only after the student checks their work, not while the student is building. Premature symbolic expression scaffolds the answer and short-circuits Representational-to-Abstract progression." M01 goes further — even post-Check, the equation lives in the companion stem rather than the toy surface — so M02 can introduce Mode C as a focused, isolated conceptual move.

*Traces to:* Tool_Flow_Document_v3.md §1, §5; BrainLift DOK3; Digital_Toys_Interactables_v4.md §2.13 Mode B.

---

### KDD-4: Sentence Stems Required Throughout M01

The module stem (`___ is a multiple of ___ because ___ × ___ = ___`) and the concrete stem (`___ tiles fill ___ rows of ___, so the area is ___ square units`) are present in every production beat of M01. No stem is removed, faded, or replaced with free text in M01.

Module Mapping v2 §M01 narrative: "The sentence stem '___ is a multiple of ___ because ___ × ___ = ___' is introduced here and required throughout (Phase 4 §2 Commitment 4)." BrainLift DOK3 Commitment 4 (sentence stems for conceptual explanations, Grades 3–5). Stems are required throughout this unit. Stem fading is deferred to a later iteration.

*Traces to:* Module_Mapping_v2.md §M01; Research_Summary.md §2 Commitment 4; BrainLift DOK3.

---

### KDD-5: U1.1 Diagnosis via Tile-by-Tile Count Detection Signal — Not Inferred Intent

The primary diagnostic trigger for U1.1 is the **§2.13 Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4; replaces v3 Arrays Extension B). Active in both B-snap-OFF and B-snap-ON sub-states. Routes to the row-structure scaffold (Light / Medium / Heavy), never to early equation reveal.

Phase 4 Research Summary §3 M1 intervention: "Gate tile-counting affordance; require multiplication entry after a check." BrainLift DOK3 Commitment #12 (expression display only after student Check — corollary: do not reveal equation as U1.1 remediation). The detection signal is the only observable trigger that does not require inferring student intent.

*Traces to:* Research_Summary.md §3 M1; Digital_Toys_Interactables_v4.md §2.13 Mode B tile-by-tile count detection signal; Tool_Flow_Document_v3.md §4, §5.

---

### KDD-6: Snap-ON/OFF Sub-States Replace Cross-Toy Concrete-to-Relational Hand-Off

The Concrete-to-Relational transition in M01 is an internal sub-state change inside §2.13 Hundred Grid Mode B (B-snap-OFF → B-snap-ON via the tutor-commanded snap-on toggle), NOT a toy hand-off.

SME resolved Critical Issue #1 (Phase 6 v4 follow-up 2026-04-27) by extending §2.13 Mode B to absorb the Concrete entry. Single-toy design keeps the student's rectangle continuous across the CRA transition — no "your tiles disappear and a new tool appears" moment — consistent with BrainLift DOK3 ("Treat CRA as explicit, guided instruction rather than free exploration by modeling each transition").

*Traces to:* Tool_Flow_Document_v3.md §10, §11; Digital_Toys_Interactables_v4.md §2.13 Mode B sub-states; Phase 6 v4 follow-up 2026-04-27.

---

### KDD-7: M01 Equation Orientation Is Standard Form Only; Reversed Form Is M02's One New Thing

M01 introduces equations exclusively in standard form `a × b = c` within the companion stem. The reversed orientation `c = a × b` does not appear anywhere in M01.

Module Mapping v2 §M01: "Feeds forward to: M02 (equation orientation reuses M01's rectangle model)." BrainLift DOK3: "Equation orientation standard (`a × b = c`) AND reversed (`c = a × b`) must both be explicitly taught in the equations module." Placing M02 after M01 (rectangle model committed) and before M03 (factor pairs need both forms) is the intended cognitive load split. Previewing reversed orientation in M01 would dilute M02's one new thing.

*Traces to:* Module_Mapping_v2.md §M01; Research_Summary.md §2 Commitment 1; Tool_Flow_Document_v3.md §7; BrainLift DOK3.

---

### KDD-8: Two Open Questions Carried Forward Unresolved — Engineering Implements Both Behaviors Behind Flags

Two §2.13 Hundred Grid Mode B Open Questions are explicitly not resolved in this starter pack.

- **OQ-M01-ENTRY-V4 (Concrete entry path):** This starter pack authors only the default §2.13 Mode B / B-snap-OFF Concrete entry. Unit Square Tiles is preserved as a documented alternative path but not authored here until SME resolves whether UST is retained or fully demoted.
- **OQ-M01-LABELS-V4 (locked-side numeric label pre-Check visibility):** Engineering must implement both candidate behaviors behind the label-visibility flag for Beat 4 / Beat 6. SME prototype A/B testing will resolve. The free-side dimension label and area label are unconditionally hidden pre-Check.

SME (2026-04-27 follow-up) chose Option A on entry-path but explicitly deferred the cross-toy UST alternative pending evidence. On labels, Phase 6 §2.13 Mode B contains conflicting phrasings; SME deferred to prototype A/B. Both OQs surfaced rather than silently resolved per the briefing's "no silent OQ closure" rule.

*Traces to:* Digital_Toys_Interactables_v4.md §2.13 Mode B sub-states, §6 OQ-M01-ENTRY-V4, OQ-M01-LABELS-V4; Tool_Flow_Document_v3.md §3 Beat 4, §5, §8; Phase 6 v4 follow-up 2026-04-27.

---

### KDD-9: SDT-Compliant Tutor Language — Observable Feedback Only

All tutor-facing script in M01 (prompts, feedback, synthesis) uses only observable, system-tracked language. Forbidden: "you're smart," "perfect!", "amazing!", "you understood it," "you persisted," "you thought carefully."

BrainLift DOK4 hard rule: "Observable vs. Assumed is a hard rule. The system can only reference what it actually tracks." SDT rule: "forbid contingent rewards, social comparison, loss framing, identity praise, generic enthusiasm." These are SDT-incompatible motivational patterns that undermine intrinsic motivation (Ryan & Deci 2020; Reeve & Jang 2006). Acceptable framings: "your rectangle shows," "you built a rectangle," "that matches the sentence," "you found 3 different areas."

*Traces to:* BrainLift DOK4 (Observable vs. Assumed rule; SDT load-bearing architecture); Research_Summary.md §2 Commitments 8, 10.

---

### KDD-10: Exit Check / Practice Built on IDENTIFY / CREATE / CONNECT Balance with Transfer Gate

Exit Check items span CONCEPTUAL / PROCEDURAL / TRANSFER components and include a Transfer Gate item (EC.2). Practice runs 10–12 problems with the 40 / 45 / 15 BASELINE / STRETCH / CHALLENGE balance from Module Mapping v2. SUPPORT and CONFIDENCE items do not count toward mastery. No early exit. Two-attempt cap on Practice.

Mastery Framework v3 component balance and Rulebook v6 phase rules: at least one APPLY/CONNECT success required; no early exit; two-attempt cap on Practice. Three-state mastery only (Strong / Needs Practice / Still Gathering); binary pass/fail is not used.

*Traces to:* Edtech Activity Queue Rulebook v6; Universal Mastery Tracking Framework v3; Module_Mapping_v2.md §M01 (P/C/T = 40/45/15).

---

# END OF MODULE 01 STARTER PACK

---

## Compilation Notes

This compilation merges three worker drafts (worker_a Sonnet 4.6, worker_b GPT-5.4, worker_c Gemini 3.1 Pro) into a single Module 01 Starter Pack v2 conforming to the STARTER PACK STRUCTURAL SKELETON v03.25.26.

### Section-by-section base attribution

| Section | Base worker | Notes / supplements |
|---------|-------------|---------------------|
| §1.0 The One Thing | worker_a | Verbatim — bold inline labels exactly match skeleton. |
| §1.1 Learning Goals | worker_a | Italic subtitle from skeleton (`*Verbatim from OUR Curriculum*`). Adopted worker_a's stronger L1/L2 wording grounded in CCSS 4.OA.B.4. Added worker_b's BrainLift sources line. |
| §1.2 Scope Boundaries | worker_a | Worker_a's HARD VOCABULARY FENCE block was clearer than worker_b's. Kept SC-1..SC-6 checklist. |
| §1.3 Vocabulary Architecture | worker_a | Added worker_b's "Toy-chrome vs. script separation" note for clarity. |
| §1.4 Misconceptions | merged | Used worker_a's U1.1 detection-mechanism + 3-tier ladder; supplemented with worker_b's #M01-2 (row size/count collapse) and #M01-3 (slot-filling) as additional secondary misconceptions, since these are observable patterns that arise during stem completion. Renumbered to 1.4.1–1.4.5 to keep U1.1 PRIMARY first and prevention-only U1.6 / background U1.5 trailing. |
| §1.5 Toy Specifications | worker_a | Added worker_b's "Shared interaction grammar" line to Interaction Constraints for completeness. |
| §1.6 Warmup | worker_a + Tool Flow v3 patches | Verified all v3 patches present: Core Purpose 3-sentence block (Key Function / Why this serves M01 / Necessity Test); WODB authoring constraint; IM-Adaptation Decision Record (5 fields, H3 — not H4); Bridge interaction with §2.13 Mode B observation→B-snap-OFF transition; Parameters table; Constraints table; explicit MUST/MUST NOT block; Verification Checklist; Engagement Anchors (Choice + Personalization); Warmup Type Rationale. |
| §1.7 Lesson | worker_a | Added worker_b's L.2 (Concrete Readback with concrete stem) as a separate interaction — original worker_a folded this into L.1. Splitting it makes the row-count/row-size separation (M01-2 prevention) explicit. Renumbered subsequent interactions: L.2 (Snap-On) → L.3, L.3 (Fixed-Side) → L.4, L.4 (Stem) → L.5, L.5 (Second Build) → L.6. Used worker_b's clearer Forbidden Phrases formatting (`❌ **"phrase"** — explanation`) per Rule 8. |
| §1.8 Exit Check | worker_a, expanded | Worker_a's EC items used a stripped-down format (Prompt / Setup / Mastery component) — not the 9-field interaction format. Compiled version expands EC.1, EC.2, EC.3 to full 9 fields per Rule 3 (Setup / Student Action / Teacher Move / Key Observation / Common Detour / Intervention / Next Move / Duration), pulling the post-Check responses and remediation language from worker_a's terse version. |
| §1.8.5 Practice Inputs | worker_a | All 12 representative practice items kept verbatim. |
| §1.9 Synthesis | worker_a, expanded | Same field-coverage gap as §1.8: worker_a's S.1, S.2 lacked the full 9-field interaction structure. Expanded all four (S.1, S.2, S.3, S.4) to 9 fields. |
| §1.10 KDDs | worker_a | Worker_a's 10 KDDs are the most coverage. Worker_c only had 3 (insufficient). Worker_b's 10 KDDs were thinner per item — kept worker_a's depth. KDD-1 title generalized from "Withhold 'factor,' 'factor pair,' 'prime,' 'composite'" to "Withhold the Four Later-Module Terms" so the KDD title itself does not embed a fenced term in plain prose, though the body retains the engineering-facing references where the four terms are required for traceability (allowed per Rule 5). |

### Conflicts resolved

| Conflict | Resolution | Source |
|----------|-----------|--------|
| Forbidden Phrases format inconsistency | Adopted worker_b's bolded format (`❌ **"phrase"** — explanation`) per Rule 8. | STRUCTURAL SKELETON Example 3 |
| KDD count divergence (A=10, B=10, C=3) | Took worker_a's 10 (most depth). Worker_c's 3 KDDs are subsumed by worker_a's set. | Rule 2 |
| Misconception count divergence | Merged: 5 entries (U1.1 PRIMARY + worker_b's #M01-2 and #M01-3 SECONDARY + U1.6 prevention-only + U1.5 background). All five clearly labeled by tier. | Rule 8 (worker_a depth, worker_b sharper observable signs) |
| Worker_b's `## §1.0` style vs. skeleton's `## 1.0` | Used `## 1.0` per skeleton | Rule 1 (skeleton overrides) |
| Worker_b inserted "→ SECTION WARMUP COMPLETE. PROCEED TO SECTION 1." after warmup | Removed — skeleton only specifies section transition markers between Lesson sections (S1→S2→S3→Exit Check). Section transition markers between major H2 phases are not in the skeleton. | Rule 1 |
| Worker_a interaction L numbering had snap-on as L.2 but skipped the explicit concrete readback step | Reordered with L.2 (Concrete Readback) as a discrete interaction between L.1 (Free Build) and L.3 (Snap-On). Total L.* now 6 interactions: L.1 (Concrete), L.2 (Concrete Readback), L.3 (Snap-On Transition), L.4 (Fixed-Side Build), L.5 (Multiple Stem), L.6 (Second Fixed-Side Build). Aligns with playbook three-CRA-stage flow and matches Tool Flow v3 beat sequence. | Rule 4 (target 5–6 L.* interactions) |
| Worker_a Self-Critique sections (lines 1146–1164) | Removed entirely per Rule 7. | Rule 7 |
| Worker_b Self-Critique (lines 900–906) | Removed entirely per Rule 7. | Rule 7 |
| Worker_c Self-Critique | Removed entirely per Rule 7. | Rule 7 |

### Structural conformance summary

- **Exactly 3 H1 headings:** `# MODULE 01: Rectangle Recognition & Tile-Based Production`, `# BACKBONE`, `# END OF MODULE 01 STARTER PACK`. ✓
- **All §1.0–§1.10 are H2.** ✓
- **No H4 anywhere in the structural skeleton portion.** Verified via grep. ✓
- **§1.1 italic subtitle:** `*Verbatim from OUR Curriculum*` ✓
- **KDDs as `### KDD-N: Title`:** All 10 KDDs use H3 format. ✓
- **§1.7 order:** Required Phrases → Forbidden Phrases → Purpose Frame → Sections → Interactions ✓
- **Forbidden Phrases format:** `❌ **"phrase"** — explanation` ✓
- **Required Phrases format:** `* "phrase"` ✓
- **No "Module-Specific Lesson Guidance" wrapper.** ✓ — Misconception Prevention, Incomplete Script Flags, Success Criteria, Verification Checklist all stand as independent H3.
- **Section Transition Markers:** `→ **SECTION X COMPLETE. PROCEED TO SECTION Y.**` between L sections and at end of L.6. ✓

### Knowingly accepted divergences

- **§1.6 Warmup interaction count = 2** (W.1 + W.2 Bridge), where Rule 4 suggests "W (2–3)." This matches Tool Flow v3's authored Beat 1 + Bridge structure exactly. Adding a third interaction would require a synthetic beat not present in the source. Worker_a's self-critique explicitly addressed this — the Warmup Playbook's 2-interaction minimum is met by W.1 alone, and the bridge is a required structural element per the skeleton.
- **§1.5 Open Questions retained as `### 1.5.4 Open Questions and Flags`** despite skeleton not explicitly naming this subsection. Both OQs are load-bearing for engineering and per the briefing's "no silent OQ closure" rule. Consistent with worker_b's structure.

### Final interaction count

- **Warmup (W):** 2 — W.1 (WODB Recognition), W.2 (Bridge)
- **Lesson (L):** 6 — L.1 (Free Build), L.2 (Concrete Readback), L.3 (Snap-On), L.4 (Fixed-Side Build), L.5 (Multiple Stem), L.6 (Second Build)
- **Exit Check (EC):** 3 — EC.1 (Recognition), EC.2 (Stem Completion / Transfer Gate), EC.3 (Build + Produce)
- **Synthesis (S):** 4 — S.1 (Pattern Discovery), S.2 (Real-World Bridge), S.3 (Reflection), S.4 (Identity Closure)
- **Total:** 15 (target 13–15 per Rule 4) ✓

### Final KDD count

10 KDDs, H3 format, sequentially numbered KDD-1 through KDD-10. ✓

### Vocab-fence verification statement (post-revise)

A final scan was performed for the four fenced terms (`factor`, `factor pair`, `prime`, `composite`) across the full document, applying the strict allowlist (Forbidden Phrases, KDDs / engineering-facing notes, §1.1 standards/metadata, §1.2 / §1.3 metadata, Misconception Prevention prose, Standards canonical anchor text, Compilation Notes):

- Tutor prompts (Setup, Teacher Move, Intervention text, Purpose Frame, Transition Frame, Opening Frame): **0 occurrences**
- Required Phrases bullets: **0 occurrences**
- §2.10 Drop Down stem options (module stem, concrete stem, follow-up stems): **0 occurrences**
- §2.11 Multiple Choice option labels (W.1 WODB, S.1, S.2, S.3, EC.1, P-series MC): **0 occurrences**
- Sentence stems rendered to student: **0 occurrences**
- §1.6 / §1.8 / §1.8.5 / §1.9 Constraint and Verification-Checklist rows: **0 occurrences** (now use indirect reference "M01 vocabulary-fence terms (per §1.3)")
- §1.4.5 Misconception heading and body: **0 occurrences** (heading renamed; body uses "later-module vocabulary")
- §1.0 critical-misconception prose: **0 occurrences** (replaced "factor-pair search" with "finding every rectangle for a fixed area")
- §1.9 S.4 closure parenthetical: **0 occurrences** (rewrites to "Vocab-fence holds")

Allowed appearances retained per allowlist (post-revise count = 20 lines, all engineering-facing or canonical-text):
- §1.1.1 Standards Cascade — line 64 (CCSS 4.OA.B.4 canonical anchor text)
- §1.1.2 Module Bridges — line 73 (M03 module title "Finding Every Factor Pair" as proper-noun metadata)
- §1.2 Must Not Include — lines 106–109, 118 (terms named as fenced)
- §1.3 Vocabulary Architecture — lines 137, 163–166 (engineering reference)
- §1.7 Forbidden Phrases — lines 484–487 (where prohibition is the point)
- §1.10 KDD bodies — lines 1238, 1298 (engineering rationale prose)
- Compilation Notes — lines 1360, 1408+ (audit metadata)

The word "multiple" is used intentionally throughout student-facing surfaces (module stem, synthesis prompts, vocabulary-anchor introduction) and is not part of the M01 vocabulary fence.

**Vocab-fence verification: PASS — zero leaks across all surfaces (pre-revise leak count was 39 across 10 lines per GPT-5.4 reviewer; post-revise leak count is 0).**

---

### Revise Pass 1 (2026-04-27)

Reviewer (GPT-5.4) returned Gate 1 PASS, Gate 2 FAIL (10 leak locations totaling 39 fenced-term occurrences outside the strict allowlist), Gate 3 PASS. Compiler (Opus 4.7) executed iteration 1 of max 2 to apply the 10 surgical vocab-fence fixes. No structural changes (Gate 1 preserved). No Tool Flow alignment changes (Gate 3 preserved).

**Fixes applied (all 10):**

1. **§1.0, line 28** — Replaced "M03's systematic factor-pair search" with "M03's systematic search for finding every rectangle for a fixed area" in the Critical Misconception prose. Sentence meaning preserved; fenced term removed from non-allowlisted prose.
2. **§1.4.5, line 212 (heading)** — Renamed `### 1.4.5 #U1.5: Factor/Multiple Vocabulary Confusion (BACKGROUND — not a primary target)` to `### 1.4.5 #U1.5: Later-Module Vocabulary Confusion (BACKGROUND — not a primary target)`. TOC-anchor text now fence-safe.
3. **§1.4.5, line 215 (body)** — Rewrote the body sentence to: "U1.5 is not a primary M01 target because M01 deliberately withholds the later-module vocabulary — there is nothing to confuse yet. The vocabulary fence that prevents U1.5 seeding is itself the M01 contribution to this misconception's arc. Formal vocabulary anchor introducing both later-module terms — and tying them to the dimensional roles (side length and area) — is sequenced into M03." No fenced term appears.
4. **§1.6 Constraints table, line 331** — Replaced explicit four-term enumeration with indirect reference: "No M01 vocabulary-fence terms (the four later-module terms enumerated in §1.3) appear in any tutor copy, option label, or stem text." Beat-1 equation suppression and Beat-5 "multiple" sequencing preserved verbatim.
5. **§1.6 MUST NOT bullet, line 347** — Replaced explicit enumeration with: "Introduce any of the four M01 vocabulary-fence terms (enumerated in §1.3) — or the word 'multiple' — in any warmup-facing text".
6. **§1.6 Verification Checklist W-Vocab, line 433** — Replaced with: "No M01 vocabulary-fence terms (per §1.3) appear in tutor copy, option labels, or stem text; no equation form renders".
7. **§1.8 Parameters table, line 787** — Replaced with: "Holds across all Exit Check items: no M01 vocabulary-fence terms (per §1.3)".
8. **§1.8.5 Toy Constraints, line 952** — Replaced with: "Holds across all Practice items; no M01 vocabulary-fence terms (per §1.3)".
9. **§1.9 Synthesis Constraints, line 1065** — Replaced with: "Holds throughout synthesis: no M01 vocabulary-fence terms (per §1.3)".
10. **§1.9 S.4 Teacher Move parenthetical, line 1186** — Rewrote to: "(Vocab-fence holds across the closure — no M01-fenced terms appear. The bridge to M02 mentions 'write the equation in a second way' without previewing the reversed orientation `c = a × b` — that is M02's one new thing.)"

**Verification:** Post-revise scan shows 0 fenced-term occurrences outside allowlist zones; 20 lines of fenced-term occurrences remain, all in §1.1.1 Standards Cascade, §1.1.2 Module Bridges (M03 proper-noun title), §1.2, §1.3, §1.7 Forbidden Phrases, §1.10 KDD bodies, or Compilation Notes — every one classified ALLOWED by the reviewer's audit.

**Structural integrity (Gate 1 preserved):** 3 H1s, 0 H4s, 10 KDDs (KDD-1 through KDD-10 in H3 format), 15 total interactions (W=2, L=6, EC=3, S=4), §1.7 ordering preserved, Section Transition Markers preserved, no "Module-Specific Lesson Guidance" wrapper.

**Tool Flow v3 alignment (Gate 3 preserved):** §2.13 Mode B / B-snap-OFF / B-snap-ON references unchanged; §2.10 / §2.11 toy bindings unchanged; companion-display sequencing in W.2 bridge unchanged; equation-overlay suppression in Practice unchanged; module stem text unchanged.
