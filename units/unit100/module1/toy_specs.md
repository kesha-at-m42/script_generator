# M01 Tool Flow — Rectangles Make Multiples — v3 (Phase 7 rerun)

**Grade 4 Unit 1 — Factors and Multiples**
**Phase 7 Tool Flow Document · v3 (Phase 7 rerun 2026-04-27, Pass B targeted patch on top of v2)**
**Module position:** M01 (first required module; the unit's Concrete entry point)
**Audience:** Engineering + UX/UI Design

> **Patch note (v3, 2026-04-27):** This document is v2 with a surgical, additive Beat 1 / Warmup patch applied per the m42-tool-flow-warmup-eval findings (5 MAJOR + 3 MINOR + 4 NOTE). All non-Beat-1 content from v2 is preserved verbatim. See §12 Document Version History at the bottom for the full change ledger. The internal v4-language headings below are retained from v2 verbatim — only Beat 1 / Warmup material has been modified, and the document title now tracks the Phase 7 artifact version (v3) rather than the internal CRA-shape revision label.

---

## 1. Module Summary

**The one new thing:** A multiple of a number is what you get when you multiply that number by another whole number, anchored in the area-of-rectangle model.

**Track / Type / Source:** Required · Standard · L1 [adapted].

**CRA shape inside M01:** Concrete (Hundred Grid Mode B in the **B-snap-OFF** sub-state — authored W×H bounds, free-placement, numeric cell labels hidden, M01 vocabulary fence on — as the default Concrete entry) → Relational (the same Hundred Grid Mode B surface transitioned to **B-snap-ON** via the tutor-commanded **snap-on toggle**, with grid-snap engaged and a fixed-side-length lock) → first multiple-statement stem (Drop Down). The B-snap-OFF / B-snap-ON sub-states and the snap-on toggle are §2.13 Mode B sub-states defined in Phase 6 v4 follow-up 2026-04-27. The legacy v3 path (§2.3 Unit Square Tiles → §2.13 Mode B via the §2.3 "reveal grid overlay" trigger) is preserved as an authored alternative Concrete entry per **OQ-M01-ENTRY-V4** (Phase 6 §6), but is NOT the M01 default; the default M01 Concrete entry is single-toy. M01 stays inside the vocabulary fence; equations are NOT revealed inside the build surface in M01 — only the multiple-of stem renders post-Check. M01 is the unit's Concrete entry point. In the default path, the Concrete-to-Relational transition is an internal sub-state change inside Hundred Grid Mode B (B-snap-OFF → B-snap-ON), not a toy hand-off; in the authored alternative path, the transition involves a real cross-toy state transfer from §2.3 Unit Square Tiles into §2.13 Mode B before snap-on engages.

**Primary misconception:** U1.1 — tile-counting by 1s instead of multiplying. The **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B) is the diagnostic trigger; detection routes the student to the row-structure scaffold, not to early equation reveal.

**Tier distribution:** 40 BASELINE / 45 STRETCH / 15 CHALLENGE.

**Vocabulary introduced in M01:** area, side length, multiple.
**Vocabulary deliberately withheld:** factor, factor pair, prime, composite. These terms must not appear in any M01 activity text, stem slot, dropdown option, tooltip, or tutor prompt. Inside Hundred Grid Mode B while the M01 mode flag is active, the toy chrome itself uses only width / height / rows / squares language; the word **multiple** is introduced exclusively in the companion post-Check module stem, never in toy tooltips or overlays.

**Sentence stems (required throughout M01, no fading):**
- Module stem: `___ is a multiple of ___ because ___ × ___ = ___`
- Concrete stem: `___ tiles fill ___ rows of ___, so the area is ___ square units`

**Warm-up preserved from IM:** "Which One Doesn't Belong?" adapted as the recognition entry beat via Multiple Choice / Checkbox.

---

## 2. Toolset for M01

| Toy | Priority | Phase 6 v4 reference | Role in M01 | Cognitive verbs supported |
|---|---|---|---|---|
| **Multiple Choice / Checkbox** | Primary | §2.11 (single-select; optional companion-toy linked highlight) | Recognition entry at the Which One Doesn't Belong beat; yields once the build sequence begins | IDENTIFY → CONCEPTUAL; COMPARE → CONCEPTUAL |
| **Hundred Grid (Mode B)** | Primary | §2.13 Mode B + Extension I (variable W×H rectangle build, vocabulary-fenced; M01 mode flag active; **B-snap-OFF / B-snap-ON sub-states with tutor-commanded snap-on toggle** per Phase 6 v4 follow-up 2026-04-27; Hundred Grid Mode B tile-by-tile count detection signal; fixed-side-length lock; label-visibility flag governs locked-side label visibility per OQ-M01-LABELS-V4; post-Check reveal with equation overlays SUPPRESSED in M01 mode) | **Load-bearing M01 rectangle host** across observation (Beat 1), Concrete build in B-snap-OFF (Beat 2 default), internal snap-on toggle from B-snap-OFF → B-snap-ON (Beat 3 default), Relational fixed-side-length build in B-snap-ON (Beats 4–7); hosts the internal sub-state change (B-snap-OFF → B-snap-ON); M01 mode flag suppresses factor / factor pair / prime / composite tooltips, stems, and overlays at the toy layer; equation overlay (Mode C) SUPPRESSED in M01 (Mode C is M02-only) | CREATE → PROCEDURAL; IDENTIFY → CONCEPTUAL; CONNECT → TRANSFER; APPLY → TRANSFER |
| **Unit Square Tiles** | Alternative-path | §2.3 (free-placement mode; row-structure hint; "reveal grid overlay" trigger) | **Authored alternative** M01 Concrete entry path per OQ-M01-ENTRY-V4 — not the default. Available for activities that benefit from a visually distinct Concrete surface before any grid edges appear; on the alternative path, tile state transfers cross-toy into Hundred Grid Mode B (engaged in B-snap-ON via the §2.3 "reveal grid overlay" trigger) before Beat 4. Per Phase 6 v4 follow-up 2026-04-27 / OQ-M01-ENTRY-V4, default M01 Concrete entry is HG Mode B / B-snap-OFF; UST is documented but not authored into the M01 starter pack until SME resolves the OQ. | CREATE → PROCEDURAL |
| **Drop Down / Fill-in-the-Blank** | Primary | §2.10 (linked-value slots from companion toy; stems-required policy) | Sentence-stem mechanism, present in every production beat; no fading | IDENTIFY → CONCEPTUAL; CONNECT → TRANSFER |
| **Equal Groups with Pictures or Dots** | Secondary | §2.9 ("groups of" framing; pre-filled / partial / blank) | Optional alternative entry for students needing explicit "groups of" framing before the area-model leap; not a parallel additive surface | CREATE → PROCEDURAL |
| **On-Screen Numeric Input** | Secondary | §2.12 (single-number response; sentence-stem pairing after correct entry) | Area-value entry where authored, between the Hundred Grid Mode B Check and the multiple-statement stem | APPLY → TRANSFER |

**What M01 does NOT include:**
- Paired (dual-orientation) post-Check display — that is Hundred Grid **Mode C** and belongs to M02 mini (where Mode C layers onto Mode B post-Check). M01 stays single-orientation only; Mode C is M02-only.
- In-toy equation overlays inside Hundred Grid — M01 suppresses them at every point, including post-Check. The post-Check reveal in M01 surfaces dimension labels and area label only; the equation form first appears inside the Drop Down module stem ("because ___ × ___ = ___").
- Number Talk routine — eliminated unit-wide.
- Stem fading — deferred to a later iteration.
- Any preview of factor, factor pair, prime, or composite vocabulary.

---

## 3. Activity Sequence (Early → Mid → Late)

### Beat 1 — Recognition Entry: Which One Doesn't Belong?

#### Warmup — Core Purpose (consolidated per WD.M01.7)

- **Key Function:** Recognition entry beat that preserves the IM 2019 Grade 4 Unit 1 Lesson 1 "Which One Doesn't Belong?" warm-up as a tool-mediated, low-anxiety rectangle-recognition task before any production occurs.
- **Why this serves M01:** Activates U1.1 row-and-area thinking by surfacing rectangle-structure attention (rows, side lengths, area) before tile placement begins in Beat 2, so the student arrives at the build surface already attending to row structure rather than discrete tile counts.
- **Necessity Test:** Removing this beat would leave students less prepared for Beat 2 — they would meet the Hundred Grid Mode B build surface without prior rectangle-structure recognition, increasing the rate of tile-by-tile counting (U1.1) at first contact and weakening the Concrete-to-Relational transition that follows.

#### Beat 1 Specification Table

| Field | Value |
|---|---|
| **Cognitive verb / component** | IDENTIFY → CONCEPTUAL |
| **Tools** | Multiple Choice / Checkbox (§2.11); optional companion §2.10 follow-up; prebuilt Hundred Grid Mode B observation display (§2.13, build affordances disabled) |
| **What students do (observable)** | The student views four authored rectangle (or rectangle-area pair) options laid out as a 2×2 grid, taps the option that does not share the property of the others, then taps Check. After Check, the student fills a brief recognition follow-up stem. |
| **Scaffolding level** | Pre-filled (all four options authored; recognition only — no production) |
| **Stem(s)** | Optional post-Check follow-up: `I chose ___ because ___` (non-gating; surfaced after Check) |
| **Interaction patterns** | Tap to select; tap Check; companion linked highlight in adjacent prebuilt-rectangle Hundred Grid Mode B display (§2.11); dropdown / Reset where authored |
| **Bridge (Beat 1 → Beat 2)** | See "Beat 1 → Beat 2 Bridge" sub-block below. In summary: companion Hundred Grid Mode B observation display transitions from prebuilt-observation mode (build affordances disabled) to **B-snap-OFF** mode (build affordances enabled) as Beat 2 begins. No vocabulary or concept is introduced in the transition. |
| **Notes** | U1.1 detection is OFF in this beat — no tile placement occurs. The Hundred Grid Mode B surface, if shown, is in prebuilt observation mode (build affordances disabled; student observes rectangle structure only). The beat preserves IM's "Which One Doesn't Belong?" warm-up and establishes recognition-before-production at the front of M01. **WODB authoring constraint (per WP.M01.1 / WT.M01.2):** all four options must be rectangle configurations where the 'doesn't belong' reason is a structural rectangle property (number of rows, side length difference, area difference, or aspect ratio). No option may be trivially distinguishable by a non-mathematical visual attribute (e.g., the only option with a visible grid, the only colored option, the only option with a number label). At least one option should be distinguishable by row count or side length in a way that activates the 'rows and area' language Beat 2 will formalize. **Authoring note (per WE.M01.6):** at least one of the four WODB rectangles should be a standard 3×4 or 4×3 arrangement that Grade 3 students would recognize from area work (CCSS 3.MD.C). This makes the prior-knowledge anchor tool-state-activated, not just a tutor verbal reference. **KDD — Warmup type selection (per WC.M01.8):** WODB used at M01 rather than Binary Choice (Warmup Phase Playbook §4D M1–3 default) because the IM 2019 source WODB directly instantiates the recognition-before-production mechanism for rectangles and has no classroom-social-dependency residue; the choice is content-specific, not convenience-driven. **Engagement Anchors (per WE.M01.10):** two anchor types are active at Beat 1 — *Choice* (via the WODB structure itself: the student selects which option doesn't belong) and *Personalization / Prior Knowledge* (via the Grade 3 area callback realized through the standard 3×4 or 4×3 rectangle, per the authoring note above). |

#### Warmup — IM-Adaptation Decision Record (per WI.M01.3)

| Field | Value |
|---|---|
| **IM source** | "Which One Doesn't Belong?" warm-up, IM 2019 Grade 4 Unit 1 Lesson 1 |
| **Hidden skill target** | Rectangle recognition before production — PRESERVED via §2.11 tap-to-select with companion §2.13 Mode B linked highlight |
| **Classroom-dependency level** | HIGH — the IM version relies on partner discussion and community-reflection as the primary mechanism for surfacing why an option doesn't belong |
| **Decision** | **Transform** (social mechanism removed; tool-mediated recognition mechanism substituted) |
| **Rationale** | The recognition-before-production hidden skill is fully preservable through a tap-and-companion-highlight interaction, so the IM activity can be retained as a Mission 42 Warmup once the partner-discussion mechanism is replaced by a tool-mediated selection-with-visual-consequence pattern; Keep is rejected because the social mechanism cannot run on the platform, and Drop is rejected because the recognition function is load-bearing for U1.1 priming into Beat 2. |

#### Beat 1 → Beat 2 Bridge (per WB.M01.4)

- **(a) Tool state change:** Companion Hundred Grid Mode B observation display transitions from prebuilt-observation mode (build affordances disabled) to **B-snap-OFF** mode (build affordances enabled) as Beat 2 begins. The transition is a single sub-state change inside §2.13 Mode B — the same toy chrome remains on screen; only its build-enable flag flips and the prebuilt rectangle clears in preparation for student production.
- **(b) Optional brief tutor prompt:** A short tutor copy line directing the student's attention to the build surface may accompany the transition (e.g., a session-relative cue along the lines of "Now you'll build one" — author at item time, with no new vocabulary). This prompt is optional, non-gating, and never required to fire.
- **(c) Constraint:** No vocabulary or concept is introduced in the transition; session-relative language only. The M01 vocabulary fence applies in full: no "factor", no "factor pair", no "prime", no "composite". The word "multiple" is not introduced at the bridge — it first appears in Beat 5 inside the companion stem. No equation form (a × b = c) renders during the bridge.

#### Warmup Parameters (per WD.M01.5)

| Parameter | Value |
|---|---|
| Tools used | §2.11 Multiple Choice / Checkbox (gating); §2.13 Hundred Grid Mode B (companion observation, build affordances disabled); §2.10 Drop Down (non-gating optional follow-up) |
| Tool interaction count | 1 gating tap (§2.11 option select + Check); 0 build interactions in Beat 1 |
| Visual states | 2 — (i) initial 4-rectangle display (2×2 grid in §2.11; companion §2.13 in prebuilt-observation mode); (ii) post-tap state with §2.13 linked highlight reflecting the student's selection |
| Duration target | 60–90 seconds (recognition-only beat; no production load) |

#### Warmup Constraints — MUST / MUST NOT (per WD.M01.5)

**MUST:**
- Options authored for rectangle-structure discrimination per the WODB authoring constraint above (per WP.M01.1 / WT.M01.2)
- §2.13 Mode B companion display loads in observation mode with build affordances disabled
- §2.11 linked highlight to the companion §2.13 display fires on student selection (timing per §5 — simultaneous-with-tap or on-Check, UX to confirm)
- At least one WODB option is a standard 3×4 or 4×3 rectangle (Grade 3 area-work callback per WE.M01.6)
- Bridge transition (Beat 1 → Beat 2) executes the §2.13 mode shift from observation to B-snap-OFF

**MUST NOT:**
- Use the M01-fenced vocabulary in any tutor copy, option label, or stem text: "factor", "factor pair", "prime", "composite"
- Show any equation form (no a × b = c notation anywhere in Beat 1, including option labels and the optional follow-up stem)
- Require "multiple" language before the §2.11 Check fires (the word "multiple" is reserved for Beat 5)
- Use a free-text response field for the optional follow-up (use §2.10 Drop Down or §2.11 Multiple Choice only)
- Run with U1.1 detection ON in Beat 1 (U1.1 detection must remain OFF until Beat 2 tile placement begins)

#### Warmup Verification Checklist (per WD.M01.5)

- [ ] All four §2.11 options pass the rectangle-structure discrimination authoring constraint (no trivial non-mathematical contrast)
- [ ] §2.13 Mode B companion display loads with build affordances disabled
- [ ] §2.11 linked highlight to the §2.13 companion display fires on student selection
- [ ] No M01-fenced vocabulary ("factor", "factor pair", "prime", "composite") appears in tutor copy, option labels, or stem text; no equation form renders
- [ ] Bridge transition (Beat 1 → Beat 2) executes the §2.13 mode shift from observation mode to B-snap-OFF (build affordances enabled) as Beat 2 begins

---

### Beat 2 — Concrete Build: Free-Placement Tile Arrangement (HG Mode B / B-snap-OFF)

| Field | Value |
|---|---|
| **Cognitive verb / component** | CREATE → PROCEDURAL |
| **Tools** | **Hundred Grid Mode B / B-snap-OFF** (§2.13, M01 mode flag, free-placement sub-state, numeric cell labels hidden, vocabulary fence on) as the default Concrete host — per Phase 6 v4 follow-up 2026-04-27 / OQ-M01-ENTRY-V4; Drop Down / Fill-in-the-Blank (§2.10) |
| **What students do (observable)** | The student taps or drags individual unit tiles onto the Hundred Grid Mode B build surface in the **B-snap-OFF** sub-state to form a rectangular arrangement with a given quantity of tiles. Tiles render at the tap location with a soft drop-shadow on the gridded background; numeric cell labels are hidden so the surface visually behaves as a blank grid rather than a numbered hundred grid. Placement is **not** grid-snapped; the interaction feels Concrete (sand-tray) rather than gridded. After arranging, the student taps Check, then fills the concrete stem. |
| **Scaffolding level** | Partial (tile count authored; build surface blank; no grid-snap or row/column hints visible in B-snap-OFF) |
| **Stem(s)** | `___ tiles fill ___ rows of ___, so the area is ___ square units` (post-Check) |
| **Interaction patterns** | Tap surface to place tile (free position, not snapped); drag to reposition; remove tile per toy-specific grammar; tap Check; dropdown selection; numeric slot fill; Undo / Reset per §1.5 shared grammar. Side-handle drag is **not** exposed in B-snap-OFF (per §2.13 Mode B sub-state spec). |
| **Notes** | The concrete-area stem appears here for the first time. This beat is still the unit's Concrete layer; the B-snap-OFF sub-state inside Hundred Grid Mode B replaces the v3 §2.3 → §2.1 cross-toy hand-off with a single-toy mode change per Phase 6 v4 follow-up 2026-04-27. If the student keeps adding single tiles rather than extending rows, the row-structure scaffold is primed for the transition beat; the **Hundred Grid Mode B tile-by-tile count detection signal** (replaces v3 Arrays Extension B) is active in B-snap-OFF and continues uninterrupted into B-snap-ON at Beat 3. **Authored alternative entry path (per OQ-M01-ENTRY-V4):** Unit Square Tiles (§2.3, free-placement) may be used in place of HG Mode B / B-snap-OFF for activities that benefit from a visually distinct Concrete surface before any grid edges appear; on this alternative path the student uses UST first and rejoins Hundred Grid Mode B at Beat 3 via a real cross-toy state transfer (§2.3 "reveal grid overlay" trigger). The default M01 Concrete entry is HG Mode B / B-snap-OFF; the UST alternative is documented but not authored into the M01 starter pack until SME resolves OQ-M01-ENTRY-V4. |

---

### Beat 3 — Concrete → Relational Transition: Snap-On Toggle inside HG Mode B (B-snap-OFF → B-snap-ON)

| Field | Value |
|---|---|
| **Cognitive verb / component** | CONNECT → TRANSFER (the student links the loose-tile rectangle to the gridded structure without changing the quantity) |
| **Tools** | **Hundred Grid Mode B — tutor-commanded snap-on toggle (B-snap-OFF → B-snap-ON)** per §2.13 Mode B sub-state spec (Phase 6 v4 follow-up 2026-04-27). On the default path, this is a single-toy internal sub-state change — no second toy participates. (Alternative-path tools, when authored: §2.3 Unit Square Tiles → §2.13 Mode B cross-toy state transfer via the §2.3 "reveal grid overlay" trigger; UST tile state re-anchors into HG Mode B in B-snap-ON before the transition completes.) |
| **What students do (observable)** | At the authored or tutor-triggered transition, the snap-on toggle fires; the student observes the same rectangle re-anchor to grid coordinates through a snap animation, then taps a highlighted row or side to acknowledge the structure. Hundred Grid Mode B remains the active build surface before, during, and after the transition; only its sub-state changes (B-snap-OFF → B-snap-ON). On the authored alternative path (when Unit Square Tiles was used in Beat 2 per OQ-M01-ENTRY-V4), tile state first transfers cross-toy from §2.3 into HG Mode B via the §2.3 "reveal grid overlay" trigger, then the snap-on toggle engages B-snap-ON. The default M01 path is single-toy; the alternative path is cross-toy. |
| **Scaffolding level** | Pre-filled transition (the system carries the student's built quantity into the gridded state; no rebuild from scratch) |
| **Stem(s)** | None new at this beat. The concrete stem may persist as a companion read-back; the module multiple stem arrives in Beats 4–5. |
| **Interaction patterns** | Tutor-commanded snap-on toggle fires (never student-initiated, per §2.13 Mode B sub-state spec); snap-to-grid animation displays; tap highlighted row or side; Undo / Reset per §1.5. The snap-on toggle is **not student-reversible within the same student pass** — Reset clears state for a fresh start. |
| **Notes (engineering / UX)** | The snap animation must visually preserve tile positions — each tile moves from its loose-placement position to a grid coordinate, no teleport. **Default path: this is an internal sub-state change inside Hundred Grid Mode B (B-snap-OFF → B-snap-ON via the snap-on toggle), NOT a toy hand-off; the same toy chrome, the same Reset/Undo/Check buttons, and the same lock-state / label-visibility / M01-vocabulary-fence flags carry through.** Ambiguous tile overlaps resolve to one tile per cell on snap-on (extras silently removed with an undo affordance), per §2.13 Mode B snap-on toggle spec. **Authored alternative path (per OQ-M01-ENTRY-V4):** when Unit Square Tiles was used in Beat 2, tile state transfers cross-toy from §2.3 into Hundred Grid Mode B via the §2.3 "reveal grid overlay" trigger; this is a real cross-toy state transfer, not a same-toy mode change — it must terminate inside HG Mode B (B-snap-ON engaged) before any structure work begins. U1.1 detection is load-bearing here through the **Hundred Grid Mode B tile-by-tile count detection signal** (replaces v3 Arrays Extension B), which is active in both B-snap-OFF and B-snap-ON. The transition should feel like the same rectangle becoming easier to read, not like a new task surface appearing. |

---

### Beat 4 — Fixed-Side-Length Build (HG Mode B / B-snap-ON): Label Visibility Gated by OQ-M01-LABELS-V4

| Field | Value |
|---|---|
| **Cognitive verb / component** | CREATE → PROCEDURAL (building); IDENTIFY → CONCEPTUAL (post-Check label interpretation) |
| **Tools** | Hundred Grid Mode B in the **B-snap-ON** sub-state (§2.13 Mode B, fixed-side-length lock; one dimension locked, the other student-built; M01 mode flag active; **label-visibility flag governs locked-side label pre-Check rendering per OQ-M01-LABELS-V4**; equation overlay SUPPRESSED) |
| **What students do (observable)** | The student builds a rectangle on the Hundred Grid Mode B build surface (B-snap-ON) by dragging the free-side handle or tapping cells (grid-snapped) to extend the free dimension, while one dimension is locked. The locked-side numeric label is rendered or hidden pre-Check according to the activity's label-visibility flag (see OQ-M01-LABELS-V4 below). The free-side dimension label and the area label remain hidden until the student taps Check, regardless of the flag setting. After Check, the toy reveals all dimension labels and the area label in the center of the rectangle. The equation overlay (Mode C) remains SUPPRESSED — equations do not appear on the build surface in M01. The multiple-statement stem (Beat 5) unlocks at Check. |
| **Scaffolding level** | BASELINE: Partial-build (one side fixed; one side built by student). STRETCH transition: Blank-build under the same fixed-side-length constraint. (Whether the locked-side label is visible during building is governed by the label-visibility flag per OQ-M01-LABELS-V4 — not by the scaffold tier.) |
| **Stem(s)** | None pre-Check. The module stem unlocks for Beat 5 at the moment of Check. |
| **Interaction patterns** | Drag free-side handle to extend / contract a full row or column (§2.13 Mode B side-handle extension; B-snap-ON only); tap empty cell to place a tile (tile-by-tile placement, grid-snapped in B-snap-ON); tap Check (reveals all dimension labels and area label; multiple-statement stem unlocks; equation overlay remains SUPPRESSED per M01 mode flag); Undo (pre-Check only); Reset (clears the rectangle, preserves fixed-side-length constraint, restarts U1.1 detection) |
| **Notes** | **OQ-M01-LABELS-V4 — OPEN QUESTION (Phase 6 v4 §6; v4 follow-up 2026-04-27):** The pre-Check visibility of the **locked-side numeric label** is currently unresolved. Phase 6 §2.13 Mode B contains both "one dimension may be locked, label shown" (legacy phrasing) and "dimension labels hidden until Check" (BrainLift DOK3 reading); the SME (2026-04-27 follow-up) decided to flag this as an Open Question and defer to prototype A/B testing rather than committing one behavior in v4. **Engineering instruction:** implement both candidate behaviors behind the label-visibility flag and expose the flag for prototype A/B testing. Candidate (a): locked-side numeric label is **visible pre-Check** (easier scaffold for U1.1; the student sees "one side = 3" from the start and infers the other from the tile count). Candidate (b): **all numeric labels are hidden pre-Check** including the locked side (strict BrainLift DOK3 reading; locked side is visually distinguishable but unlabeled until Check). The Phase 6 §2.13 inconsistency is acknowledged as an Open Question at the spec level — not a Phase 7 inconsistency to resolve. **Check gating (BrainLift DOK3, load-bearing):** the **free-side** dimension label and the **area** label are hidden during building and reveal exclusively on the student's Check tap, regardless of the label-visibility flag setting. No animation preview or intermediate render may expose free-side or area label data. **Equation suppression (M01 mode flag, load-bearing):** unlike v3, no `a × b = c` overlay appears inside Hundred Grid in M01 at any point, including post-Check. The equation form first appears to the student inside the Drop Down module stem at Beat 5. Mode C (dual-orientation paired display) is M02-only and must not appear here. **U1.1 routing (load-bearing):** when the **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B) fires, the tutor layer triggers the row-structure scaffold — one already-placed row is highlighted and a row-based prompt fires without revealing the row count or equation. |

---

### Beat 5 — Multiple-of Statement Production

| Field | Value |
|---|---|
| **Cognitive verb / component** | CONNECT → TRANSFER (the student links the checked rectangle to the multiple-of definition through the sentence stem) |
| **Tools** | Drop Down / Fill-in-the-Blank (§2.10); Hundred Grid Mode B (§2.13, post-Check companion display) |
| **What students do (observable)** | After the Hundred Grid Mode B Check in Beat 4, the student focuses on the multiple-statement stem. Because equations are suppressed on the build surface in M01 mode, the "because ___ × ___ = ___" clause in the stem is the student's first encounter with the equation form for this rectangle. If linked values were auto-pushed from the Hundred Grid Mode B Check (the two dimension values and the area value), the student reviews and confirms them, then taps Check on the stem. If slots are blank (production mode), the student taps each slot, selects from a dropdown or types a numeric value, and taps Check. |
| **Scaffolding level** | Pre-filled (Hundred Grid Mode B Check pushes the dimension values and area value into stem slots; student confirms) → Partial (Check pushes one or more values; student fills remaining slots from dropdown) → Blank (student produces all values from inspection of the checked rectangle). Pre-filled / Partial appear in BASELINE; Blank dominates in STRETCH and CHALLENGE. |
| **Stem(s)** | `___ is a multiple of ___ because ___ × ___ = ___` |
| **Interaction patterns** | Tap blank slot; select from dropdown or type value; tap Check on stem; incorrect blank highlights in distinct color without revealing the correct answer (§2.10 post-Check behavior); Undo reverts last slot entry; Reset clears all student-entered slots |
| **Notes** | The companion Hundred Grid Mode B post-Check state remains visible during stem completion — the student references the labeled rectangle (dimension labels + area label) while filling the stem. Because equations are SUPPRESSED on the Mode B build surface in M01, the "because ___ × ___ = ___" clause in the stem is the load-bearing moment where the student first connects the area-model result to the multiplication equation. The equation belongs to the stem, not to a graphical overlay. The word **multiple** is introduced here in the companion stem, not inside the Hundred Grid toy chrome. This beat occurs in every production cycle in M01 (BASELINE, STRETCH, CHALLENGE); the stem is never removed or replaced with free text. |

---

### Beat 6 — STRETCH: Varied Side Length, Varied Target Area

| Field | Value |
|---|---|
| **Cognitive verb / component** | APPLY → TRANSFER |
| **Tools** | Hundred Grid (Mode B) (§2.13 Mode B, fixed-side-length or authored W×H bounds, blank-build); Drop Down / Fill-in-the-Blank (§2.10); On-Screen Numeric Input (§2.12, where authored) |
| **What students do (observable)** | The student is given a different fixed side length than in the BASELINE beats and builds rectangles on the Hundred Grid Mode B build surface to produce specific areas that are multiples of that side length. After each Check, the student completes the multiple-statement stem. Where the authored task separates area-value recording, the student taps the On-Screen Numeric Input field, types the area value, and taps Check on that field; the stem then unlocks. |
| **Scaffolding level** | Blank-build (no pre-placed tiles; fixed-side-length constraint or authored W×H bounds locked; student builds the free dimension) |
| **Stem(s)** | Same module stem applies after each Check. If §2.12 is used, the stem unlocks after correct numeric entry. |
| **Interaction patterns** | Drag free-side handle or tap cells on Hundred Grid Mode B build surface; tap Check (dimension and area label reveal; equation overlay SUPPRESSED); tap numeric field, type digits, backspace, tap Check on field; tap stem slots, dropdown / type, tap Check; Undo / Reset per §1.5 |
| **Notes** | U1.1 detection via the **Hundred Grid Mode B tile-by-tile count detection signal** (replaces v3 Arrays Extension B) remains active across STRETCH — same routing rail as BASELINE. The On-Screen Numeric Input use is "where applicable" — only when the authored task separates area-value recording from the post-Check label reveal. If the task merges area entry into the stem, §2.12 is not surfaced for that item. For rectangles requiring a side length of 11 or 12, Hundred Grid Mode B uses the sub-canvas fallback to render the rectangle adjacent to the main frame (§2.13 Mode B sub-canvas fallback). |

---

### Beat 7 — CHALLENGE: Open-Ended Multiple Discovery

| Field | Value |
|---|---|
| **Cognitive verb / component** | APPLY → TRANSFER (rectangle enumeration); CONNECT → TRANSFER (pattern articulation across areas that are multiples of the fixed side length) |
| **Tools** | Hundred Grid (Mode B) (§2.13 Mode B, fixed-side-length lock, blank-build); Drop Down / Fill-in-the-Blank (§2.10) |
| **What students do (observable)** | The student is prompted to find as many different areas as possible for a given fixed side length (e.g., "How many different areas can you make with a side length of 4?"). The student builds rectangles in succession on the Hundred Grid Mode B build surface, taps Check after each one, and completes the multiple-statement stem for each accepted case. After completing one stem, the student taps a "Build another" affordance (tutor-authored) to reset the rectangle while preserving the fixed-side-length constraint. |
| **Scaffolding level** | Blank-build, within authored challenge bounds |
| **Stem(s)** | `___ is a multiple of ___ because ___ × ___ = ___` — completed after each individual Check; no stem fading |
| **Interaction patterns** | Build on Hundred Grid Mode B surface, Check, stem — repeated cycle; each Check reveals dimension and area labels (equation overlay SUPPRESSED in M01 mode); Reset for next rectangle preserves constraint; Undo per §1.5 |
| **Notes** | **No early exit (Mastery v3):** The student completes the authored CHALLENGE set rather than exiting after the first correct rectangle. CHALLENGE is bonus-only and does not gate advancement, but the no-early-exit rule still applies to the authored sequence. Whether the count is authored-capped or student-terminated by an "I'm done" affordance is an open SME question (§8). The vocabulary fence holds at the toy layer; the companion stem continues to carry the explicit multiple language. For rectangles requiring a side length of 11 or 12, the sub-canvas fallback applies per §2.13 Mode B. |

---

### Beat 8 — Optional Alternative Entry: Equal Groups Path

| Field | Value |
|---|---|
| **Cognitive verb / component** | CREATE → PROCEDURAL (groups build), then CONNECT → TRANSFER (into the rectangle model) |
| **Tools** | Equal Groups with Pictures or Dots (§2.9, partial or blank); Drop Down / Fill-in-the-Blank (§2.10); rejoins Hundred Grid Mode B (§2.13) at Beat 3 |
| **What students do (observable)** | When routed to this alternative, the student arranges a set of groups (e.g., 3 groups of 4 dots) instead of placing tiles freely. The student taps Check, fills the equal-groups stem, then transitions into the standard sequence at Beat 3 (snap-on toggle inside Hundred Grid Mode B engages B-snap-ON) and resumes Beats 4–7. |
| **Scaffolding level** | Partial (group count or items-per-group authored; the other dimension produced by the student) or Blank (full production) |
| **Stem(s)** | Equal-groups stem: `There are ___ groups of ___, so the total is ___`. After transition, the standard module multiple stem applies. |
| **Interaction patterns** | Tap to add / remove items; drag items between groups; tap Check; transition to Hundred Grid Mode B / B-snap-ON is tutor-triggered (snap-on toggle) as in Beat 3 |
| **Notes** | Equal Groups is a Secondary alternative path, not a parallel additive surface. It replaces the Concrete entry for students who need "groups of" framing before the area-model leap. The path rejoins the spine at Beat 3; Beats 4–7 are identical regardless of entry path. The routing trigger (student-elected vs. tutor-routed) is an SME open item (§8). |

---

## 4. Scaffolding Progressions Per Tool

### Hundred Grid Mode B (§2.13 Mode B) — Inside M01

Hundred Grid Mode B operates as the **single load-bearing rectangle host** throughout M01 (Beats 1–7). The support-decreasing arc:

| Level | Description | Beat(s) | §2.13 Mode B mechanism |
|---|---|---|---|
| **Pre-filled / Recognition** | Prebuilt rectangle in observation-only mode (build affordances disabled); student observes structure and identifies a property | Beat 1 (companion anchor); Beat 3 post-snap acknowledgment | "Fully prebuilt rectangle (recognition-stage observation only); build affordances disabled per M01 mode flag" |
| **B-snap-OFF (Concrete free-placement sub-state)** | Same Mode B surface in the **B-snap-OFF** sub-state — free-placement, numeric cell labels hidden, side-handle drag not exposed — so the student first arranges a loose rectangle before gridded structure is emphasized | Beat 2 default path | §2.13 Mode B / B-snap-OFF (Phase 6 v4 follow-up 2026-04-27): "Tiles can be placed at arbitrary canvas positions inside the grid frame; placement is not grid-snapped… Numeric cell labels are hidden by default in this sub-state" |
| **B-snap-ON grid-snap partial-build** | Same Mode B surface transitioned to **B-snap-ON** via the snap-on toggle. One side locked; student drags handle or taps cells on the free side; locked-side label visibility governed by the label-visibility flag per OQ-M01-LABELS-V4 | Beat 4 BASELINE | §2.13 Mode B / B-snap-ON: "Partial-build mode: one side fixed/locked via authored lock state; student builds the other; equations SUPPRESSED" |
| **B-snap-ON grid-snap blank-build** | Same Mode B surface in **B-snap-ON**. Student builds under authored W×H bounds or fixed-side-length constraints with no prebuilt support | Beat 4 STRETCH transition; Beats 6–7 | §2.13 Mode B / B-snap-ON: "Blank-build mode: student builds from scratch under authored constraints; equations SUPPRESSED in M01 mode; sub-canvas fallback for sides 11–12" |

**Internal mode-change rail:** Beat 3 is the same toy shifting from B-snap-OFF (loose-placement readability) to B-snap-ON (gridded readability) via the **tutor-commanded snap-on toggle** defined in §2.13 Mode B sub-states (Phase 6 v4 follow-up 2026-04-27). No second rectangle toy takes over on the default path. The snap-on toggle is never student-initiated, is not reversible within a single student pass, and re-anchors free-placed tiles to the nearest grid coordinate via a snap animation.

**U1.1 detection rail:** The **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B) is active in **both** B-snap-OFF and B-snap-ON sub-states per §2.13 Mode B spec. The signal becomes load-bearing for U1.1 routing from Beat 3 onward (B-snap-ON engaged). On signal, the tutor layer fires the row-structure hint via the §2.13 Mode B row-highlight capability — one already-placed row highlighted, row-based prompt — without revealing dimension labels, area label, or equation. Whether this rail is one-shot or persistent is an SME open item (§8).

**Equation suppression in M01:** Dimension labels and area label reveal on Check. The equation overlay (Mode C) is SUPPRESSED throughout M01 — it does not render on the build surface regardless of Check state. The equation first appears to the student inside the module stem's "because ___ × ___ = ___" clause, which is authored in §2.10 Drop Down. Mode C activates only in M02 mini.

**Post-Check stem linkage:** After the Hundred Grid Mode B Check, the two dimension values (fixed side length and student-built free dimension) and the area value are broadcast to the paired Drop Down (§2.10) and populate the linked stem slots. UX must make linked-slot population visually distinct from student-entered values, and must guarantee linked values are populated before the student can interact with the stem (race-condition avoidance).

**M01 vocabulary fence at the toy layer:** While the M01 mode flag is active, Hundred Grid Mode B uses only width / height / rows / squares language in its own prompts, tooltips, and overlays. The module's explicit **multiple** language lives in the companion stem, not inside the toy chrome.

### Unit Square Tiles (§2.3) — Inside M01 (Authored Alternative Path Only)

Unit Square Tiles is preserved in v4 as an **authored alternative Concrete entry path** (per OQ-M01-ENTRY-V4, Phase 6 §6; Phase 6 v4 follow-up 2026-04-27), **not** as the primary rectangle host and not as the M01 default. UST is not authored into the M01 starter pack until SME resolves OQ-M01-ENTRY-V4. The capability arc, when authored:

| Level | Description | Beat | §2.3 mechanism |
|---|---|---|---|
| **Free-placement alternative entry** | Snap-to-grid disabled; tiles placed anywhere on blank canvas | Beat 2 alternative path only | "Free-placement mode (M01 alternative Concrete entry path per OQ-M01-ENTRY-V4)" |
| **Grid-assist (precision support)** | Snap-to-grid enabled when the student places tiles in irregular gaps | Beat 2 alternative path (support routing) | "Grid-assist mode: snap-to-grid enabled; reduces precision demand" |
| **Row-structure hint** | One row highlighted; row-based prompt fires after tile-by-tile behavior persists | Beat 2 alternative path | "Row-structure hint: after the Hundred Grid Mode B tile-by-tile count detection signal (replaces v3 Arrays Extension B) fires, tutor highlights one row…" |
| **Cross-toy state transfer into Hundred Grid Mode B (B-snap-ON)** | Student quantity is carried cross-toy into Hundred Grid Mode B via the §2.3 "reveal grid overlay" trigger; HG Mode B engages B-snap-ON to receive the transferred tiles | Beat 3 only when alternative path is used | "Tutor command: §2.3 'reveal grid overlay' fires; tile state transfers from Unit Square Tiles into Hundred Grid Mode B surface, which engages B-snap-ON" |

This is the **authored alternative path**, not the default. The default M01 path uses Hundred Grid Mode B / B-snap-OFF for Beat 2 and the snap-on toggle (B-snap-OFF → B-snap-ON) for Beat 3 — single-toy throughout. After Beat 3, regardless of entry path, Unit Square Tiles is no longer the active build surface within M01; both Concrete-style tile placement (B-snap-OFF) and Relational-grid build (B-snap-ON) are hosted inside Hundred Grid Mode B.

### Drop Down / Fill-in-the-Blank (§2.10) — Inside M01

Present in every production beat. Stems are required at every level — the frame is never removed, only the fill-support shifts:

| Level | Description | Beat(s) | §2.10 mechanism |
|---|---|---|---|
| **Pre-filled (linked values)** | Hundred Grid Mode B Check pushes the two dimension values and the area value into all stem slots; student reviews and confirms | Beat 1 (recognition follow-up); Beat 5 (early BASELINE) | "Linked values from companion toys" |
| **Partial (one or two blanks)** | Companion toy pushes some values; student fills remaining slots from dropdown | Beat 5 (mid-BASELINE) | "Pre-filled recognition mode (all but one or two blanks filled)" |
| **Blank (full production)** | Student produces all values from inspection of the checked surface | Beats 5–7 (STRETCH, CHALLENGE) | "Fully-blank production mode" |

Dropdown option lists are tutor-authored and narrowed to plausible values (correct value plus 1–2 distractors) at the partial level. UX must visually distinguish auto-pushed values from student-entered values.

### Multiple Choice / Checkbox (§2.11) — Inside M01

Used at Beat 1 only. No scaffolding arc within M01 — the toy serves the recognition entry beat and yields once production begins. The optional post-Check stem (`I chose ___ because ___`) is non-gating.

### Equal Groups (§2.9) — Inside M01 (Secondary)

Pre-filled / Partial / Blank arc per §2.9, used at Beat 8 as an alternative entry only. After the equal-groups Check, the path rejoins the spine at Beat 3 and shifts into Hundred Grid Mode B; no further §2.9 scaffolding occurs within M01.

### On-Screen Numeric Input (§2.12) — Inside M01 (Secondary)

Used at Beat 6 only, where the authored task separates area-value recording from the Hundred Grid Mode B post-Check label reveal. Sentence-stem pairing is automatic per §2.12: correct numeric entry unlocks the Drop Down stem.

---

## 5. Interaction Patterns — Engineering / UX Call-outs

- **Equation suppression in M01; labels gated until Check (with locked-side label visibility = OQ-M01-LABELS-V4).** Across every Hundred Grid Mode B beat in M01 (Beats 1–7), the equation overlay (Mode C — dual-orientation paired display) is SUPPRESSED by the M01 mode flag. No multiplication equation, equation strip, or paired-orientation display is visible during building or post-Check in M01. The **free-side dimension label** and the **area label** are hidden during building and reveal exclusively on the student's Check tap; no animation preview, hover state, or pre-render may expose free-side or area label data. Whether the **locked-side numeric label** (Beat 4 / Beat 6 fixed-side-length lock) is visible pre-Check is the subject of **OQ-M01-LABELS-V4** (Phase 6 §6; v4 follow-up 2026-04-27); engineering must implement both candidate behaviors (locked-side label visible pre-Check vs. all numeric labels hidden pre-Check) behind the **label-visibility flag** and expose it for prototype A/B testing. The equation form first appears inside the module stem's "because ___ × ___ = ___" clause (Drop Down), not on the build surface. Mode C activates only in M02 mini.

- **Hundred Grid Mode B tile-by-tile count detection signal → row-structure hint (U1.1 routing).** Hundred Grid Mode B must distinguish single-tile placement from row/column handle extension and emit the **Hundred Grid Mode B tile-by-tile count detection signal** (replaces v3 Arrays Extension B; defined in §2.13 Mode B; internal — never displayed to the student; active in both B-snap-OFF and B-snap-ON sub-states). On signal, the tutor layer highlights one already-placed row (§2.13 Mode B "Tutor-commanded highlighting") and fires a row-based prompt without revealing the row count or equation. Engineering should confirm the existing Hundred Grid Mode B telemetry exposes per-tile vs. per-row events.

- **Concrete-to-Relational transition = snap-on toggle inside Hundred Grid Mode B (B-snap-OFF → B-snap-ON).** At Beat 3, the **tutor-commanded snap-on toggle** (defined in §2.13 Mode B sub-state spec, Phase 6 v4 follow-up 2026-04-27) fires; each tile must animate from its current loose-placement position (B-snap-OFF) to a grid coordinate (B-snap-ON) — smooth movement, not teleport. After the animation, the same Hundred Grid Mode B surface remains active in the B-snap-ON sub-state. **On the default M01 path, this is NOT a toy hand-off — it is an internal sub-state change.** Ambiguous tile overlaps resolve to one tile per cell on snap-on (extras silently removed with an undo affordance) per §2.13 Mode B snap-on toggle spec. The toggle is never student-initiated and is not reversible within a single student pass. **Authored alternative path (per OQ-M01-ENTRY-V4):** when Unit Square Tiles was used in Beat 2, engineering must confirm the cross-toy tile-state transfer mechanism (§2.3 → §2.13 Mode B / B-snap-ON via the §2.3 "reveal grid overlay" trigger) so that pre-placed tiles map correctly to Hundred Grid Mode B grid coordinates.

- **Stem-slot linkage from companion toy.** After Hundred Grid Mode B Check, the two dimension values (fixed side length and student-built free dimension) and the area value must be broadcast to the paired Drop Down (§2.10) and populate the corresponding linked slots ("Linked values from companion toys"). UX must make linked-slot population visually distinct from student-entered values, and must guarantee linked values are populated before the student can interact with the stem (race-condition avoidance).

- **Recognition Multiple Choice → linked highlight in companion toy.** At Beat 1, tapping an option in §2.11 should visually highlight the corresponding rectangle in the adjacent prebuilt-rectangle Hundred Grid Mode B display (§2.11 "Optional linked highlight in companion toy on selection"). UX must confirm highlight timing — simultaneous with tap, or on Check.

- **On-Screen Numeric Input area-value entry linkage.** In Beat 6 (where authored), the numeric field must be positioned relative to the Hundred Grid Mode B post-Check display so the student can verify their entry against the visible area label. Correct entry automatically invites the Drop Down stem (§2.12 "Sentence-stem pairing"). Engineering must confirm whether this is a single combined surface or two sequenced Check events.

- **M01 vocabulary fence enforcement at the toy layer.** Hundred Grid Mode B has an authored M01 mode flag that suppresses all "factor," "factor pair," "prime," and "composite" strings from any tooltip, stem, or overlay while M01 mode is active. The only term from later-unit vocabulary that intentionally appears in M01 is **"multiple"** — and it appears exclusively inside the companion Drop Down module stem, not inside the Hundred Grid toy chrome. Per §2.13 Mode B Extension I (authored mode flags): the M01-vocabulary-fence flag is a per-activity authored signal, not a student-visible setting.

- **Reset / Undo behaviors per toy.**
  - **Hundred Grid Mode B:** Reset clears the active rectangle and restarts U1.1 detection while preserving authored W / H bounds, lock states, the M01 mode flag, the label-visibility flag, and the current snap sub-state. Undo removes the last tile / handle action (pre-Check only); post-Check, Undo is disabled and Reset is the path. The **snap-on toggle** (B-snap-OFF → B-snap-ON) is not student-reversible within the same student pass per §2.13 Mode B sub-state spec; Reset clears state for a fresh start.
  - **Unit Square Tiles (alternative-path only):** Reset clears all tiles. Undo removes the last tile action. The cross-toy state transfer into Hundred Grid Mode B (§2.3 "reveal grid overlay" trigger) cannot be undone by the student — it is tutor-triggered.
  - **Drop Down / Fill-in-the-Blank:** Undo reverts the last slot entry. Reset clears all student-entered slots; pre-filled linked values are cleared and must be re-populated by a new Hundred Grid Mode B Check.
  - **Multiple Choice / Checkbox:** Undo deselects last selection. Reset returns to unselected.
  - All toys honor the §1.5 shared interaction grammar (Check, Undo, Reset).

---

## 6. Quality Checks

Before implementation sign-off, confirm all of the following:

1. **Default M01 path is single-toy; alternative path is cross-toy and gated on OQ-M01-ENTRY-V4.** Hundred Grid Mode B carries observation, Concrete build (B-snap-OFF), the snap-on toggle transition (B-snap-OFF → B-snap-ON), Relational build (B-snap-ON), STRETCH, and CHALLENGE. Unit Square Tiles may appear only as the authored alternative Concrete entry path per OQ-M01-ENTRY-V4 — it must resolve into Hundred Grid Mode B (engaged in B-snap-ON via the §2.3 "reveal grid overlay" trigger) before Beat 4 and is not authored into the M01 starter pack until SME resolves the OQ.
2. **Beat 3 default path is written and built as a same-toy sub-state change via the snap-on toggle.** The B-snap-OFF → B-snap-ON transition happens inside Hundred Grid Mode B per §2.13 Mode B sub-state spec (Phase 6 v4 follow-up 2026-04-27); no "transitions to a second rectangle toy" language survives in the default flow. The authored alternative path is documented as a real cross-toy state transfer and is not the default.
3. **U1.1 routing uses the correct telemetry.** The diagnostic signal is the **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B), referenced consistently by full label or by its `(replaces v3 Arrays Extension B)` attribution form everywhere it appears.
4. **M01 equation overlays are suppressed at the toy layer.** No `a × b = c` render appears inside Hundred Grid Mode B in Beats 1–7. Equation-display work belongs to M02 Mode C and must not appear in M01.
5. **The M01 vocabulary fence is enforced at the toy layer.** While the M01 mode flag is active, Hundred Grid Mode B surfaces no "factor," "factor pair," "prime," or "composite" language in any tooltip, stem, overlay, or tutor prompt.
6. **The word "multiple" appears where intended.** It is introduced through the companion Drop Down module stem, not through the Hundred Grid toy chrome.
7. **Beat 4 locked-side label visibility is documented as OQ-M01-LABELS-V4.** Both candidate behaviors (locked-side label visible pre-Check vs. all numeric labels hidden pre-Check) are documented as authored options behind the label-visibility flag; engineering implements both behaviors and the SME prototype A/B will resolve. The free-side dimension label and the area label are unconditionally hidden until Check.
8. **Phase 6 references are updated to v4 and cite the v4 follow-up where applicable.** All "§2.1 Arrays" and "Phase 6 v2" citations are removed or repointed to "§2.13 Mode B" / "§2.13 Mode C" as appropriate; references to the snap sub-states / OQ-M01-ENTRY-V4 / OQ-M01-LABELS-V4 cite Phase 6 v4 follow-up 2026-04-27 in the change log.

---

## 7. Transition into M02

By the end of M01, the student has built and checked rectangles on the Hundred Grid Mode B build surface, observed that the resulting areas form a sequence of multiples of the fixed side length, and produced the multiple-statement stem in every production beat. The Hundred Grid Mode B has revealed dimension labels and area labels post-Check across every M01 encounter, with equation overlays suppressed — the student knows the area and dimensions, but has seen equations only inside the Drop Down stem. M02 ("Both Ways Around") picks up the same Hundred Grid Mode B rectangle representation the student already knows — it does not re-teach the area model — and introduces the dual-orientation post-Check display via §2.13 Mode C (layered onto Mode B post-Check) so that `a × b = c` and `c = a × b` are presented as equivalent forms of the same fact. M01 deliberately suppresses equations at the toy layer so M02 can introduce Mode C as a focused, isolated conceptual move rather than as background noise. No M02 internals belong here.

---

## 8. SME Review Questions

The following questions name decision points Phase 7 cannot resolve without SME input.

1. **Equal Groups routing trigger (Beat 8).** Is the §2.9 alternative entry path offered (a) by student election at the start of M01, (b) by tutor routing on the **Hundred Grid Mode B tile-by-tile count detection signal** (replaces v3 Arrays Extension B) after a Concrete attempt, or (c) by some other tutor signal such as an incorrect Check on the first rectangle build? This determines whether Equal Groups is a proactive scaffold or a reactive rescue.

2. **Concrete-to-Relational snap-on toggle trigger (Beat 3).** Per §2.13 Mode B sub-state spec, the snap-on toggle is tutor-commanded (never student-initiated). The remaining open question is **what tutor signal fires the toggle**: (a) automatically when the student taps Check on the B-snap-OFF Concrete state, (b) on student request via a visible "See the grid" affordance routed through the tutor, or (c) on tutor command after a threshold of placed tiles or after the Hundred Grid Mode B tile-by-tile count detection signal (replaces v3 Arrays Extension B) fires above an authored threshold. This determines whether the transition is student-paced, student-elected, or tutor-controlled. Note: this is distinct from OQ-M01-ENTRY-V4 (which asks whether UST should remain as an authored alternative entry at all).

   *Related: **OQ-M01-ENTRY-V4** (Phase 6 §6) — should the §2.3 Unit Square Tiles → §2.13 Mode B alternative entry path be retained for activities that benefit from a visually distinct Concrete surface, or fully demoted out of the M01 path so there is exactly one Concrete entry route? Default until SME resolves: HG Mode B / B-snap-OFF is the M01 Concrete entry; UST alternative is documented but not authored into the M01 starter pack.*

   *Related: **OQ-M01-LABELS-V4** (Phase 6 §6) — for Beat 4 / Beat 6 fixed-side-length builds, is the locked-side numeric label visible pre-Check (easier U1.1 scaffold) or hidden pre-Check (strict BrainLift DOK3 reading)? v4 default until resolved: flag for prototype A/B testing; engineering implements both behaviors behind the label-visibility flag.*

3. **First surface point of the module multiple stem.** Should `___ is a multiple of ___ because ___ × ___ = ___` first appear (a) only after the first Hundred Grid Mode B Check in Beat 5, or (b) earlier — alongside the concrete stem at Beat 2 in partial form? The module stem needs an equation to complete, but Phase 7 cannot decide whether early visibility (slots blank) is pedagogically useful or premature given that M01 suppresses in-toy equation overlays.

4. **U1.1 row-structure scaffold persistence.** Is the row-structure hint (Hundred Grid Mode B tile-by-tile count detection signal → row highlight → prompt) a one-shot intervention per task, or does it re-fire on every subsequent tile-by-tile detection within the same build attempt and across subsequent build attempts? The answer affects scaffold density and mastery routing.

5. **CHALLENGE termination behavior.** For the open-ended "find as many areas as you can with side length 4" task, does the system (a) set an authored cap (e.g., 8 build-Check-stem cycles) that the student must complete, or (b) leave the count open with a student-initiated "I'm done" affordance? Mastery v3's no-early-exit rule clearly applies to BASELINE / STRETCH; whether it applies identically to CHALLENGE bonus exploration is the open call.

6. **On-Screen Numeric Input position in M01.** Is §2.12 area entry (a) a required component of every STRETCH cycle, or (b) an optional authored insert for selected items? The answer drives whether §2.12's "Initial Spec Draft" status is a build-blocker for M01 or only a partial schedule risk.

---

## 9. Open Items / Risks (One-Liners)

- **OQ-M01-ENTRY-V4 (Phase 6 §6; v4 follow-up 2026-04-27) — default Concrete entry path resolution.** Default M01 Concrete entry is HG Mode B / B-snap-OFF (single-toy). Unit Square Tiles is preserved as an authored alternative but is not authored into the M01 starter pack until SME resolves whether to retain it. If retained, Phase 8 must author both entry paths; if demoted, only the HG-as-Concrete-host single-toy path is authored.
- **OQ-M01-LABELS-V4 (Phase 6 §6; v4 follow-up 2026-04-27) — locked-side label visibility pre-Check.** Engineering implements both candidate behaviors behind the label-visibility flag and exposes it for prototype A/B testing. SME prototype A/B will resolve. The free-side dimension label and the area label are unconditionally hidden until Check regardless of flag setting.
- **Unit Square Tiles UX-in-Process status (Phase 6 OQ-UST1).** Authored alternative Concrete entry path only (per OQ-M01-ENTRY-V4); if it is unavailable at launch, the default M01 Concrete path via Hundred Grid Mode B / B-snap-OFF is unaffected. Build-start delay in Unit Square Tiles no longer blocks the full Concrete spine.
- **On-Screen Numeric Input "Initial Spec Draft" status (Phase 6 OQ-NI1).** Secondary in M01, but if STRETCH items systematically require area-value entry, schedule risk propagates to STRETCH authoring.
- **Hundred Grid Mode B tile-by-tile detection telemetry.** The **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B) is the U1.1 routing trigger for M01's primary misconception. Engineering must confirm Hundred Grid Mode B telemetry distinguishes per-tile placement from row/column handle extension and emits the internal signal in both B-snap-OFF and B-snap-ON sub-states before M01 authoring begins.
- **Concrete-to-Relational state transfer (alternative path only).** If the student enters via the OQ-M01-ENTRY-V4 alternative path (§2.3 Unit Square Tiles), tile-state transfer into Hundred Grid Mode B at Beat 3 is a cross-toy data flow via the §2.3 "reveal grid overlay" trigger; engineering must confirm the handoff mechanism and validate that tile positions map correctly to Hundred Grid Mode B grid coordinates (HG Mode B engages B-snap-ON to receive the transferred tiles). For students who entered via the default Hundred Grid Mode B / B-snap-OFF path, the Beat 3 transition is an internal sub-state change (B-snap-OFF → B-snap-ON) with no cross-toy transfer.
- **Stem-slot auto-population race condition.** The Hundred Grid Mode B Check-to-Drop-Down linked-value broadcast must arrive before the student can interact with the stem; any async delay in post-Check rendering could let the stem appear before linked values populate.
- **Beat 3 snap-on toggle trigger semantics not yet fixed.** The snap-on toggle's tutor-signal trigger (SME question 2) is the same engineering surface as the trigger for U1.1 routing entry into Hundred Grid Mode B; if engineering implements one before SME resolves the other, the scaffold arc may not match the intended sequence.
- **Hundred Grid Mode B snap-fill (OQ-HG-V4-7).** The snap-fill drag gesture (drag across blank rectangular region to snap-fill a W×H rectangle) is pending SME review. If kept, it adds a third tile-placement interaction pattern in M01 STRETCH and CHALLENGE beats. If dropped, tile-by-tile placement and side-handle extension remain the only patterns. Engineering judgment must keep this consistent with the BrainLift simplicity rule.
- **Hundred Grid Mode B sub-canvas fallback for sides 11–12.** Beats 6–7 may author tasks with side length 11 or 12 (or area above 100). Per §2.13, rectangles exceeding the main grid render in a paired sub-canvas adjacent to the main frame. Engineering must confirm sub-canvas behavior (same toy chrome; same Reset/Undo/Check behavior) is consistent with M01's interaction grammar before CHALLENGE authoring begins.

---

## 10. Compiler Notes

### v4 revise iteration 1 (this revise pass) — post Phase 6 v4 follow-up 2026-04-27

This revision addresses the GPT-5.4 reviewer's two critical issues and two minor issues against the prior v4 compile, after the SME issued a 2026-04-27 follow-up resolving both critical issues at the Phase 6 spec level. The follow-up edits to Phase 6 §2.13 Mode B added named **B-snap-OFF (Concrete free-placement)** and **B-snap-ON (Relational grid-snapped)** sub-states with a tutor-commanded **snap-on toggle**, and added two new Open Questions in §6: **OQ-M01-ENTRY-V4** (HG B-snap-OFF default vs. UST → HG handoff alternative) and **OQ-M01-LABELS-V4** (locked-side label visibility pre-Check).

**(a) Phase 6 follow-up = SME Option A.** The SME chose to extend §2.13 to truly absorb the Concrete entry rather than to re-promote §2.3 Unit Square Tiles as a peer Concrete host. The legacy v3 §2.3 → §2.13 path is preserved as a documented authored alternative under OQ-M01-ENTRY-V4 but is NOT the M01 default and is not authored into the M01 starter pack until the OQ resolves.

**(b) Changes in this revise pass to align Phase 7 with the Phase 6 follow-up:**
- §1 Module Summary CRA shape rewritten to use the canonical §2.13 sub-state names (B-snap-OFF / B-snap-ON / snap-on toggle) and to distinguish default single-toy path from authored alternative cross-toy path.
- §2 Toolset table: Hundred Grid (Mode B) row updated with sub-state spec, label-visibility flag, and new OQ pointers; Unit Square Tiles row demoted from "Primary" to "Alternative-path" with explicit OQ-M01-ENTRY-V4 framing.
- §3 Beat 2 Tools cell now lists HG Mode B / B-snap-OFF as the default host; UST appears in the Notes cell only as the authored alternative entry path per OQ-M01-ENTRY-V4. Beat 2 header retitled to make the default sub-state visible.
- §3 Beat 3 rewritten as the snap-on toggle inside Hundred Grid Mode B (B-snap-OFF → B-snap-ON). Removed the prior "Either way, the transition stays inside one toy" sentence (Reviewer Minor Issue #2) and replaced it with explicit text distinguishing the default same-toy sub-state change from the authored alternative cross-toy state transfer (§2.3 "reveal grid overlay" trigger). Beat 3 header retitled to make the sub-state transition visible.
- §3 Beat 4 reframed: locked-side label visibility is now explicitly an Open Question (OQ-M01-LABELS-V4); both candidate behaviors are documented as authored options behind the label-visibility flag with an "engineering implements both, SME prototype A/B will resolve" instruction. The previous Phase 6-level inconsistency is acknowledged as the OQ rather than reproduced in Phase 7. Free-side label and area label remain unconditionally hidden until Check.
- §4 scaffolding tables for HG Mode B and UST rewritten using the B-snap-OFF / B-snap-ON sub-state names verbatim from §2.13.
- §5 Interaction Patterns: Concrete-to-Relational bullet rewritten to cite §2.13 Mode B sub-state spec as the source of the snap-on toggle (the prior compile described the snap-off / snap-on as a Phase 7-only mechanic). Equation-suppression bullet expanded to call out OQ-M01-LABELS-V4 for locked-side label visibility. Reset/Undo bullet updated to cite the snap-on toggle's not-student-reversible rule from §2.13.
- §6 Quality Checks expanded from 7 to 8 items to include explicit OQ-M01-LABELS-V4 documentation check and to standardize the U1.1 signal label requirement.
- §8 SME Review Questions: question 2 updated to acknowledge that the snap-on toggle being tutor-commanded is now spec-resolved (§2.13), and that the remaining open question is the **tutor-signal trigger** for the toggle. Two related-OQ pointers added (OQ-M01-ENTRY-V4 and OQ-M01-LABELS-V4).
- §9 Open Items: two new top-of-list entries added for OQ-M01-ENTRY-V4 and OQ-M01-LABELS-V4. UST and cross-toy state-transfer entries rewritten to reflect the alternative-path-only framing.
- **Minor Issue #1 (U1.1 signal full label):** standardized every reference to either the full label "Hundred Grid Mode B tile-by-tile count detection signal" or the attribution form "tile-by-tile count detection signal (replaces v3 Arrays Extension B)". No bare "tile-by-tile detection signal" or "tile-by-tile count detection signal" without context survives.

**(c) Acknowledgment.** The authored alternative UST → HG path is preserved end-to-end in this document (§1 CRA shape, §2 toolset row, §3 Beat 2 / Beat 3 Notes, §4 UST scaffolding table, §5 Concrete-to-Relational bullet, §6 Quality Check #1, §8 OQ pointer, §9 Open Items entries). It is documented as a real cross-toy path — not as a same-toy mode change — and it is gated behind OQ-M01-ENTRY-V4. SME resolution will determine whether Phase 8 authors both paths or only the default HG-as-Concrete-host path.

### v4 merge decisions (initial compile pass)

- **Backbone = Worker A.** Worker A's draft was structurally the most complete v4 ripple — every "Arrays" reference, every "Phase 6 v2" citation, and the Concrete-to-Relational hand-off had been relocated correctly, and the toolset table accurately captured the M01 mode flag as the load-bearing v4 mechanism. Beats 4 and 5 in particular use Worker A's equation-suppression framing because A explicitly anchors "the equation first appears inside the module stem" — which is the load-bearing v4 pedagogical move.
- **Quality Checks (§6) sourced from Worker B.** Worker A folded its quality-check language into the §5 call-outs and dropped the standalone numbered checklist that v3 had as §6. Worker B preserved the standalone numbered list in §6, which is the cleaner v3-structure-preserving choice and gives engineering a discrete sign-off checklist. This compile reinstates the numbered §6 from Worker B's framing.
- **Beat 2 default-path framing borrowed from Worker B.** Worker B's "default Hundred Grid Mode B with snap disabled / alternative Unit Square Tiles" framing is cleaner than Worker A's "Unit Square Tiles default" wording because it matches the SME's "Hundred Grid absorbs ALL M01 roles" directive and the v4 §3 mapping table where Hundred Grid is the M01 Primary host. Worker C's Beat 2 still listed Unit Square Tiles as the default tool in the row, which contradicts the v4 toolset table — overridden.
- **Beat 3 framing.** All three workers correctly framed Beat 3 as an internal mode change, but Worker C's Beat 3 sub-header still read "Grid Overlay" (v3 language); replaced with Worker A's "Same-Toy Mode Change (Snap-Grid Enable)" wording, which makes the v4 reframing visible at the section level.
- **Vocabulary fence wording.** Worker C's Interaction-Patterns fence statement included "multiple" inside the suppression list, which contradicts the worker briefing's load-bearing rule that "multiple" IS introduced in M01. Used Worker A and Worker B's correct framing: the fence suppresses "factor / factor pair / prime / composite" at the toy layer; "multiple" is intentionally introduced via the companion Drop Down stem only.
- **Mode C placement.** All three workers correctly kept Mode C out of M01 live flow. Mode C now appears only in §2 ("What M01 does NOT include"), §4 (equation-suppression note), §5 (UX call-out), and §7 (M02 transition). No beat references it as live behavior.
- **U1.1 routing label.** Standardized on "Hundred Grid Mode B tile-by-tile count detection signal (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B)" — Worker A's exact phrasing — used consistently in §1, §3 Beats 2–4, §4, and §5.

### v3 → v4 cognitive verb continuity

- **Beat 3 cognitive verb remains CONNECT → TRANSFER.** The load-bearing move is linking one rectangle across two readability states of the same Hundred Grid toy, not identifying a new property and not handing off to a new host.
- **Beat 5 cognitive verb remains CONNECT → TRANSFER.** The student links the checked rectangle to the verbal multiple statement through the companion stem, even though the toy itself suppresses equation overlays.
- **Beat 7 cognitive verb remains APPLY → TRANSFER plus CONNECT → TRANSFER.** The student first generates new valid cases under a constraint, then articulates the repeating multiple relationship case by case.

### Out-of-scope content

No timing estimates, scripts, remediation dialogue, transfer gates, paired-orientation display, factor / factor pair / prime / composite previews, Number Talks, or stem-fading language appear. Row-based prompts remain framed as generic "row-based prompt" references to avoid drifting into Phase 8 script territory.

### Reviewer focus areas

Three places to check carefully in this v4 compile: (1) Beat 3 and §5 must consistently describe a same-toy mode change, not a hidden toy hand-off; (2) Beats 4–7 and §6 must consistently suppress in-toy equation overlays in M01; (3) the toy-layer vocabulary fence must remain strict (factor / factor pair / prime / composite suppressed) even while the companion stem legitimately introduces the word **multiple**.

---

## 11. v4 Change Log (SME Ripple 2026-04-27)

**SME directive date:** 2026-04-27
**SME (verbatim):** *"Arrays should be removed -- the hundred grid takes please [sic] of the needs of arrays in this unit. Revise the output from Phase 6 and 7 accordingly."*

### Substitution rules applied

| v3 language | v4 language |
|---|---|
| Arrays (toy name) | Hundred Grid (Mode B) / §2.13 Hundred Grid, Mode B |
| Arrays grid / Relational grid | Hundred Grid Mode B build surface / rectangle build surface |
| §2.1 (fixed-side-length mode) | §2.13 Mode B (fixed-side-length lock; one dimension locked, other student-built) |
| §2.1 Extension B (U1.1 detection) | **Hundred Grid Mode B tile-by-tile count detection signal** (Phase 6 v4 §2.13 Mode B; replaces v3 Arrays Extension B) |
| Arrays single-orientation post-Check reveal (equation revealed) | Hundred Grid Mode B post-Check reveal: dimension labels + area label ONLY; equation overlay SUPPRESSED in M01 mode flag (Mode C is M02-only) |
| "transitions to Arrays via grid overlay" / "Concrete-to-Relational transition trigger" (toy hand-off) | Internal mode change inside Hundred Grid Mode B (free-placement → grid-snap); NOT a toy hand-off; both Concrete and Relational build hosted inside one toy |
| §2.1 Extension A (paired-orientation display) | §2.13 Mode C (M02-only; must not appear in M01) |
| "Phase 6 v2" | "Phase 6 v4" |
| "M01 is single-orientation only (§2.1 Extension A)" | "M01 is single-orientation only; Mode C is M02-only; equations SUPPRESSED at the toy layer in M01" |
| Unit Square Tiles as "Concrete entry that hands off to Arrays" | Unit Square Tiles as "optional alternative Concrete entry path" (Hundred Grid Mode B is the primary M01 Concrete and Relational host) |

### CRA shape rewrite (Module Summary, §1)

v3: *"Concrete (Unit Square Tiles, free-placement) → Relational (Arrays grid, fixed-side-length) → first equation pairing (Drop Down stem)."*

v4 (initial compile): *"Concrete (Hundred Grid Mode B with W×H bounds and snap disabled as the default Concrete entry, with Unit Square Tiles preserved as an optional alternative entry path) → Relational (the same Hundred Grid Mode B surface with grid-snap enabled and a fixed-side-length lock) → first multiple-statement stem (Drop Down). M01 stays inside the vocabulary fence; equations are NOT revealed inside the build surface in M01 — only the multiple-of stem renders post-Check."*

v4 revise iteration 1 (post Phase 6 v4 follow-up 2026-04-27): *"Concrete (Hundred Grid Mode B in the **B-snap-OFF** sub-state — free-placement, numeric cell labels hidden, M01 vocabulary fence on — as the default Concrete entry) → Relational (the same Hundred Grid Mode B surface transitioned to **B-snap-ON** via the tutor-commanded **snap-on toggle**, with grid-snap engaged and a fixed-side-length lock) → first multiple-statement stem (Drop Down). The legacy v3 path (§2.3 Unit Square Tiles → §2.13 Mode B via the §2.3 'reveal grid overlay' trigger) is preserved as an authored alternative Concrete entry per OQ-M01-ENTRY-V4, but is NOT the M01 default. M01 stays inside the vocabulary fence; equations are NOT revealed inside the build surface in M01 — only the multiple-of stem renders post-Check."*

### Pedagogical moves preserved across v3 → v4

- M01 pedagogical sequence (Recognition → Concrete → Concrete-to-Relational → Relational → Stem pairing → STRETCH → CHALLENGE).
- M01 sentence stems verbatim (Module stem and Concrete stem).
- M01 vocabulary fence: factor / factor pair / prime / composite withheld; multiple introduced in M01 via the companion stem.
- Tier distribution (40 BASELINE / 45 STRETCH / 15 CHALLENGE).
- Cognitive verbs and components per beat.
- IM 2019 "Which One Doesn't Belong?" warm-up adaptation.
- Cross-cutting toys (Drop Down, Multiple Choice, Numeric Input, Equal Groups) and their roles.
- M01 misconception U1.1 as the primary target.

---

**v3 Attribution:** Phase 7 Tool Flow Document originally compiled from Worker A (Claude Sonnet 4.6), Worker B, Worker C — Phase 7 v3 Compiler.
**v4 Attribution:** Phase 7 v4 revision per SME directive 2026-04-27. Compiled from Worker A (Claude Sonnet 4.6), Worker B (GPT-5.4), Worker C (Gemini 3.1 Pro). Initial compile pass by Phase 7 v4 Compiler (Claude Opus 4.7). Arrays → Hundred Grid Mode B substitution per Phase 6 v4 §2.13 spec.
**v4 revise iteration 1 Attribution:** Revised by Phase 7 v4 Compiler (Claude Opus 4.7) after Phase 6 v4 follow-up 2026-04-27 (which added §2.13 Mode B B-snap-OFF / B-snap-ON sub-states + snap-on toggle, OQ-M01-ENTRY-V4, OQ-M01-LABELS-V4) to address GPT-5.4 reviewer's two critical issues + two minor issues. SME (2026-04-27 follow-up) decisions binding: Critical Issue #1 = Option A (extend §2.13 to absorb Concrete entry); Critical Issue #2 = DEFER (flag as OQ-M01-LABELS-V4).

---

## 12. Document Version History

### v3 — Phase 7 rerun (2026-04-27, Pass B targeted patch)

- **Patch date:** 2026-04-27
- **Source:** `m42-tool-flow-warmup-eval` findings on Tool_Flow_Document_v2.md (Phase 7 / M01) — 5 MAJOR + 3 MINOR + 4 NOTE; verdict PASS WITH CONDITIONS. Findings file: `phase-6_toys_interactables_rerun-2026-04-27/M01_Warmup_Eval_Findings.md`.
- **Patch type:** Targeted, additive Beat 1 / Warmup patch. **No design-level restructuring.** All non-Beat-1 content from v2 (Beats 2–8, §4 Scaffolding Progressions, §5 Interaction Patterns, §6 Quality Checks, §7 Transition into M02, §8 SME Review Questions, §9 Open Items / Risks, §10 Compiler Notes, §11 v4 Change Log) is preserved verbatim from v2.
- **Pass scope:** Single-spawn Pass B patch on top of Pass A v2 compile; no swarm spawned for v3.

#### Conditions resolved (5 MAJOR → all closed)

| Finding | Severity | Resolution location in v3 |
|---|---|---|
| WP.M01.1 | MAJOR | Beat 1 Notes — "WODB authoring constraint" paragraph; Warmup Constraints MUST item; Verification Checklist item 1 |
| WT.M01.2 | MAJOR | Beat 1 Notes — same authoring constraint plus "At least one option should be distinguishable by row count or side length" sentence; Warmup Constraints MUST |
| WI.M01.3 | MAJOR | New "Warmup — IM-Adaptation Decision Record" sub-block (5 fields) immediately after Beat 1 Specification Table |
| WB.M01.4 | MAJOR | New "Bridge" row added to Beat 1 Specification Table; new "Beat 1 → Beat 2 Bridge" sub-block with parts (a) tool state change, (b) optional tutor prompt, (c) constraint |
| WD.M01.5 | MAJOR | Three new sub-blocks added to Beat 1: "Warmup Parameters", "Warmup Constraints — MUST / MUST NOT", "Warmup Verification Checklist" |

#### Additional documentation improvements applied (2 MINOR + 2 NOTE)

| Finding | Severity | Resolution location in v3 |
|---|---|---|
| WD.M01.7 | MINOR | New "Warmup — Core Purpose" sub-block at the top of the Beat 1 section (Key Function / Why this serves M01 / Necessity Test — 3 sentences) |
| WE.M01.6 | MINOR | Beat 1 Notes — "Authoring note" paragraph specifying a standard 3×4 or 4×3 rectangle as Grade 3 area-work callback; mirrored in Warmup Constraints MUST |
| WC.M01.8 | NOTE | Beat 1 Notes — "KDD — Warmup type selection" sentence justifying WODB at M01 over Playbook §4D M1–3 default |
| WE.M01.10 | NOTE | Beat 1 Notes — "Engagement Anchors" sub-bullet labelling the two anchor types (Choice via WODB structure; Personalization / Prior Knowledge via Grade 3 area callback) |

#### Closed transitively (1 NOTE)

- **WB.M01.9** — Closed transitively by the WE.M01.6 Authoring Note (the standard 3×4 / 4×3 rectangle is the Grade 3 prior-anchor callback the WB.M01.9 Note flagged as missing). No independent fix required, per the findings file's recommended disposition.

#### Vocabulary fence verification (v3 patch content only)

All new content authored in v3 was checked against the M01 vocabulary fence: "factor", "factor pair", "prime", "composite" do not appear in any new student-facing or tutor-copy text introduced by the patch. Where the fenced terms appear in the Constraints MUST NOT block, they are surrounded by quotation marks as terms-being-prohibited rather than as authored copy. The word "multiple" is mentioned only in references to Beat 5 / the companion stem (where its introduction is intended), not in any new Beat 1 student-facing copy.

#### Files touched in v3

- Created: `phase-7_tool_flow_rerun-2026-04-27/Tool_Flow_Document_v3.md`
- v2 file (`phase-7_tool_flow/M01/Tool_Flow_Document_v2.md`) was NOT modified; v3 is the canonical Phase 7 artifact going forward.

#### Attribution

- **v3 patch attribution:** Phase 7 rerun Pass B targeted patch executed by a single subagent against v2 per parent-agent task brief 2026-04-27. No swarm spawned.
- **v2 attribution:** Inherited verbatim from v2 — see §11 v4 Change Log and the v2 attribution lines below for prior compile history.
