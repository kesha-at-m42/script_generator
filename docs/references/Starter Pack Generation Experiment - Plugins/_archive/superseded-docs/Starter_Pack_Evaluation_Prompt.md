# STARTER PACK EVALUATION PROMPT

**Version:** 03.12.26 v3
**Purpose:** Gate-specific evaluation checks for Module Starter Pack drafts. Each gate section is designed to be run by a separate agent with fresh context — no knowledge of the drafting process.
**Usage:** At each gate, the Cowork Guidance specifies which gate section to use. The evaluation agent receives this prompt + the relevant gate section + the documents listed for that gate.

---

## ROLE

You are evaluating a Module Starter Pack draft. Your job is to verify the draft against its upstream source documents, the Module Starter Pack Template, and the Phase Playbooks. You are checking for correctness, completeness, and internal consistency — not rewriting the SP.

**You are not the author.** Do not fix issues — report them with specific citations so the author can fix them. For each finding, cite: (1) what the SP says, (2) what the source document says, and (3) where they conflict or what's missing.

---

## SOURCE HIERARCHY

When source documents conflict, follow this priority order:

```
1. Tool Flow (TVP) — HIGHEST AUTHORITY for Starter Pack content
   What toys are used, how they're configured per module,
   scaffolding progressions, data constraints, key beats,
   SME-resolved decisions

2. Module Mapping (sheet) — Module architecture, learning goals,
   standards cascade, misconceptions, vocabulary sequence.
   AUTHORITATIVE for sequencing and cross-module continuity.

2a. Important Decisions (sheet) — Unit-level design constraints
    (CRA path, grid fading, scope boundaries, interaction modality).
    These are HARD CONSTRAINTS — violations are FAILs.

3. Phase Playbooks (Warmup, Lesson, EC, Synthesis, Practice)
   — Phase structure, CRA requirements, interaction patterns,
   quality checks. Applied as DESIGN FRAMEWORKS — if the TVP
   is missing an interaction that a Playbook requires, flag it.

4. Module Starter Pack Template (v2) — Structural requirements,
   section format, interaction block format, required fields

5. Notion Toy Specs — What each toy CAN do (capabilities).
   The TVP specifies what it DOES in each module.
   When TVP and Notion Spec conflict, TVP wins.

6. Guide Design Prompt / Voice Script Prompt — Universal
   script rules (module-specific constraints belong in the SP;
   universal rules should NOT be duplicated)

VALIDATION REFERENCES (not in the authority chain, but used to verify):
- Conceptual Spine Analysis (sheet) — concept intro/develop/master placement
- Conceptual Development (sheet) — cognitive demand levels per lesson
- Standards Mapping (sheet) — required vocabulary per standard
- Original Curriculum Mapping (sheet) — source curriculum details (supplementary only)
- Misconceptions (sheet) — global IDs, observable behaviors, priority, surfacing locations
```

**Critical rule:** The TVP specifies module-level toy behavior. The Notion Spec describes general toy capabilities. If the SP follows the Notion Spec on a point where the TVP says something different, that is a FAIL.

---

## RATING SCALE

For each criterion, assign one rating:

- **PASS** — SP matches source, no issues
- **FLAG** — Minor issue, discrepancy, or ambiguity that needs author attention but doesn't break pedagogy
- **FAIL** — SP contradicts source document, missing required element, or pedagogical error

---

## EVALUATION NOTES (apply to all gates)

**Do not evaluate against a reference implementation.** Compare the draft SP against its source documents, not against another SP. Every finding must cite a specific source document.

**"Missing" can be as important as "wrong."** A TVP key beat that has no corresponding SP interaction is a FAIL, even though the SP doesn't explicitly contradict the TVP — it just omits required content.

**Design decisions are valid if documented.** If the SP deliberately departs from a source document and documents the departure in §1.10 (KDD) or a Design Note, that is a PASS. Verify the KDD exists and is coherent. Undocumented departures are FAILs.

**Internal consistency errors are always FLAGs or FAILs.** If §1.5 says one thing and §1.7 says another, that's a problem regardless of which one is "right."

---

# GATE 1 EVALUATION: BACKBONE

## Documents Required

- [ ] The Backbone draft (§1.0–§1.5)
- [ ] Cross-Reference Tables A, B, C + Design Constraints (from Working Notes)
- [ ] Module Mapping sheet (fresh read for verification)
- [ ] Important Decisions sheet (fresh read — unit-level design constraints)
- [ ] Tool/Visual Plan (TVP) (fresh read for verification)
- [ ] Module Starter Pack Template v2 (§1.0–§1.5 structure)
- [ ] Misconceptions sheet
- [ ] Conceptual Spine Analysis sheet (concept placement validation)
- [ ] Standards Mapping sheet (required vocabulary per standard)
- [ ] M[X-1] Starter Pack (if available — §1.2 Must Not Include, §1.3 Vocabulary, §1.5 Toy Specs, §1.9 Synthesis closure, §1.10 KDDs)
- [ ] M[X+1] TVP section (required for A12 inter-module consistency check; if unavailable, note which A12 checks could not be completed)

If any document is missing, state which checks cannot be completed.

---

## Section A: Source Fidelity (TVP Cross-Reference)

For each item, look up what the TVP says for this module and compare to what the SP says.

### A1. Toy List and Configuration
- Do the toys in §1.5 match the TVP's Tool Requirements for this module?
- For each toy: does the SP's mode, interaction pattern, grid state, and feedback behavior match the TVP?
- Are there toys in the TVP not mentioned in the SP, or vice versa?

### A2. Scaffolding Progression
- Does the SP's scaffolding arc (across phases) match the TVP's Scaffolding Progression?
- Are scaffold states correctly assigned to phases?

### A3. Data Constraints
- Do the SP's dimension ranges, area ranges, factor limits, and shape types match the TVP's Data Constraints?
- Are specific values called out in the TVP reflected in the SP?
- **Computation check:** For any derived value in the SP (unit conversions, computed areas, ratios, or counts that result from applying constraints), verify the arithmetic is correct. Cross-check against TVP example values where available. Incorrect computations → FAIL.
- **Unstructured requirements:** Do not limit verification to the TVP's structured tables (Tool Requirements, Data Constraints). Also scan TVP prose, SME resolutions, and activity descriptions for specific constraints (e.g., "cap density at X during teaching," "factors may exceed Y for comparison pairs," teaching vs. practice splits for the same parameter). These carry the same authority as structured content.

### A4. Key Beats
- For each key beat in the TVP, does the SP contain a planned interaction that delivers it?
- Is the key beat's essential interaction preserved in the Section Plan?
- **Verbatim check:** For any TVP note explicitly tagged as "load-bearing," "Starter Pack note," or containing specific script language (dialogue in quotes), verify the SP includes the verbatim language — not just the intent. Paraphrases of load-bearing notes → FAIL.
- **Sequence completeness:** When the TVP describes a sequence of interactions for a single phase or moment (e.g., "Synthesis: rank, then match, then bridge"), verify each sub-interaction has a corresponding SP element — not just that the phase topic is addressed. Count the TVP's interactions and count the SP's; if the SP has fewer, identify what's missing.
- **Unstructured requirements:** Do not limit verification to the TVP's structured "Key Beats" or "Key Teaching Points" sections. Also scan TVP prose, SME resolutions, and activity descriptions for specific interaction requirements (e.g., "include an Easy/Hard MC before the grid switch," "intersperse these problems in Practice, not grouped separately"). These carry the same authority as structured content.

### A5. SME-Resolved Decisions
- For each resolved SME question in the TVP, is the resolution reflected in the SP?
- Are any decisions the TVP marks as resolved still listed as open in the SP?

### A6. Misconceptions
- Do the misconceptions in §1.4 match the TVP's "Misconceptions Targeted" section?
- Are priority levels (PRIMARY, SECONDARY, PREVIEW) consistent?
- Do misconception IDs match the Misconceptions database (global IDs, not module shorthand)?

### A7. Vocabulary Sequence
- Does §1.3's vocabulary staging match the TVP's vocabulary section?
- Are "Terms to Avoid" consistent between SP and TVP?
- Does every term in the Module Mapping's "Vocabulary to Teach" appear in §1.2 or §1.3?

### A8. Transition Notes
- Do §1.1.2 Module Bridges match the TVP's transition sections (M[X-1] → M[X] and M[X] → M[X+1])?
- If M[X-1] SP is available, does the "From" bridge match M[X-1]'s Synthesis closure?

### A9. CRA Stage
- Does §1.0 include a **CRA Stage** field? (Concrete / Relational / Abstract / Application)
- Does the stated CRA Stage accurately reflect the module's position in the unit's CRA progression?
- Is the CRA Stage consistent with the interaction types and scaffolding levels in the phase designs? (e.g., a "Concrete" module should not feature abstract notation without manipulative support)

### A10. Changes from M[X-1] Accuracy
- If §1.5 includes a "Changes from M[X-1]" table, verify each claim about M[X-1]'s behavior:
  - Against the M[X-1] SP (if available) — especially §1.5 Toy Specs and §1.2 Must Not Include
  - Against Important Decisions that constrain M[X-1]'s behavior (e.g., grid fading sequence, CRA stage assignments)
- Any M[X-1] description that contradicts M[X-1]'s own SP or the Important Decisions → FAIL
- If M[X-1] SP is not available, verify against Important Decisions only and FLAG any claims that cannot be verified

### A11. Phase and Convention Terminology
- Verify that all structural phase labels in the SP (Warmup, Lesson, Exit Check, Practice, Synthesis) match the established naming conventions from the Module Starter Pack Template and prior SPs
- Check for renamed, invented, or conflated phase labels (e.g., "Enrichment Challenge" for "Exit Check," "Assessment" for "Exit Check," "Activity" for "Lesson")
- If M[X-1] SP is available, verify terminology is consistent across both SPs
- Incorrect or invented phase labels → FAIL (these propagate into implementation and create confusion across the production pipeline)

### A12. Inter-Module Content Consistency (if adjacent module TVP sections are available)
- For any content planned in M[X]'s Practice, EC, or late phases, check whether M[X+1]'s learning goals claim that same content as NEW or INTRODUCED
- If M[X] plans substantial practice of a skill that M[X+1] claims to introduce, this is a source document conflict → FLAG with Author Flag recommendation
- Specifically check: Does M[X]'s Practice or EC include problem types, reasoning modes, or skill applications that M[X+1]'s learning goal describes as novel?
- This check requires reading both M[X] and M[X+1] TVP sections. If M[X+1] TVP is not available, note which checks cannot be completed.

---

## Section D: Scope and Vocabulary Enforcement (Backbone)

### D1. Vocabulary Completeness
- Walk through the Module Mapping "Vocabulary to Teach" list term by term — is every term accounted for in §1.2 Must Teach or §1.3?
- Walk through "Vocabulary to Avoid" — is every term in §1.3 Terms to Avoid?

### D2. Scope Boundary Completeness
- For each item in "Must Not Include," verify it aligns with the TVP's scope for this module
- Check: are there concepts the TVP explicitly defers to later modules that are missing from "Must Not Include"?

### D3. Critical Notes
- For each "Critical:" note in the Module Mapping, verify it is addressed in the backbone (§1.2, §1.3, or §1.5)
- Unaddressed Critical notes are FAILs

### D4. Cross-Reference Table Accuracy
- Spot-check 5 fields from Table A against the actual Module Mapping — are they verbatim?
- Spot-check 5 items from Table B against the actual TVP — are they verbatim?
- Are all Conflict Log entries genuine conflicts (not misreadings)?

### D5. Design Constraint Compliance
- For each decision in the Important Decisions sheet that applies to this module, verify it is reflected in the SP
- Check specific constraints: grid fading sequence (which modules get full/partial/tick/dimensions-only), scope boundaries (e.g., "do not introduce perimeter"), interaction modality rules (e.g., drag vs. tap), CRA path decisions
- Any applicable decision not reflected in the backbone → FAIL
- Any decision partially reflected or ambiguously implemented → FLAG

---

## Section E0: Backbone Internal Consistency

Gate 1 is the first evaluation pass, so internal contradictions within the backbone must be caught here — before they propagate into Task 2 phase designs.

### E0.1. Examples vs. Stated Constraints
- For each data table in §1.5, verify that every example value falls within the stated constraint ranges in the same table. If a constraint says "Factors 3–10" and an example uses factor 15, that is an internal contradiction → FLAG (or FAIL if the example is in a student-facing specification).

### E0.2. Cross-Section Consistency
- Do claims in §1.0 (e.g., about Warm-Up behavior, number of units shown, misconception strategies) match the detailed specifications in §1.5?
- Do scope boundary items in §1.2 match the tool guardrails in §1.5?
- Does the vocabulary staging in §1.3 match any phase-specific vocabulary notes in §1.5?
- Contradictions between sections → FLAG (or FAIL if the contradiction would produce conflicting implementation instructions).

### E0.3. Out-of-Scope Content
- Task 1 produces §1.0–§1.5 only. If the backbone includes sections beyond this range (§1.6, §1.7, Appendix, Notes for Next Author), check whether they contradict §1.0–§1.5 content. Contradictions → FAIL. Non-contradicting extra sections → FLAG (recommend relocation to Working Notes).

---

## Section SP: Conceptual Spine Validation

### SP1. Concept Placement
- For each concept the Conceptual Spine Analysis tracks for this module, verify the SP's treatment matches the expected stage (introduced / developed / mastered)
- If the Spine says a concept is "introduced" in this module, the SP should present it as new. If "developed," the SP should build on prior exposure. If "mastered," the SP should expect fluency.
- Check: do the CRA stages in the SP align with the cognitive demand level listed in the Conceptual Development sheet for this module's lessons?
- Mismatches → FLAG

---

## Gate 1 Output Format

```
### [Section.Criterion] [Name]
**Rating:** PASS | FLAG | FAIL
**Finding:** [What the SP says vs. what the source says]
**Source:** [Document, section — be specific]
**Recommendation:** [What to fix — only for FLAG and FAIL]
```

Summary:
```
## GATE 1 SUMMARY
- PASS: [X]  FLAG: [X]  FAIL: [X]

### Critical Issues (FAIL)
1. [Issue]

### Important Issues (FLAG)
1. [Issue]

### Strengths
1. [Notable quality]
```

---

# GATE 2 EVALUATION: WARMUP + LESSON

## Documents Required

- [ ] Warmup draft (§1.6)
- [ ] Lesson draft (§1.7)
- [ ] Approved Backbone (§1.0–§1.5)
- [ ] Working Notes (Cross-Reference Tables, Section Plan)
- [ ] Warmup Phase Playbook (fresh read)
- [ ] Lesson Phase Playbook (fresh read)
- [ ] Guide vs Prompt Structure Reference
- [ ] TVP (warmup + lesson sections for this module)
- [ ] Conceptual Development sheet (cognitive demand levels for CRA validation)
- [ ] Misconceptions sheet (M[X] entries for remediation design validation)
- [ ] Voice Script Prompt
- [ ] Guide Voice Design Reference (for Voice Agent checks)

If any document is missing, state which checks cannot be completed.

---

## Section B: CRA Phase Completeness

**CRA Relational phase deserves special attention.** The most common structural gap is a missing or weak Relational interaction — where concrete experience is explicitly connected to the abstract concept via a stated pattern. If the only thing between tiling/manipulation and vocabulary is a transition beat, that's a FAIL on B3.

### B1. Pre-CRA / Motivation (if applicable)
- If the module has a motivation arc before the CRA sequence, is it clearly marked as pre-CRA?
- Is there a KDD documenting the departure from standard CRA if Section 1 doesn't fit the CRA framework?

### B2. Concrete Phase
- Is there at least one interaction where the student physically manipulates the toy (drag, place, build)?
- Does a worked example with think-aloud precede the student's first attempt?
- Are think-aloud elements tagged: [PLANNING], [ATTENTION], [SELF-CHECK]?
- Is there an example-problem pair (Guide demos → student replicates)?

### B3. Relational Phase
- Is there a dedicated interaction where:
  - Two or more concrete examples are displayed simultaneously?
  - The Guide explicitly states the pattern or principle that connects them?
  - The student confirms understanding (typically via MC)?
- This interaction must exist as a SEPARATE interaction — not embedded in a vocabulary introduction or transition. If missing, FAIL.

### B4. Abstract Phase (Vocabulary)
- Are formal terms introduced AFTER at least one Concrete interaction AND the Relational interaction?
- Does the vocabulary introduction follow: (1) reference experience → (2) introduce term → (3) connect to visual?
- Is there a student-action interaction where the student applies new vocabulary immediately after the teaching-only introduction?

### B5. Application Phase
- Are there 2+ interactions where the student works independently with decreasing Guide support?
- Does support visibly decrease (compare Guide dialogue length and specificity)?
- Are new contexts introduced (different shapes, orientations, or parameters)?

### B6. Required/Forbidden Phrases Sections
- Does the Lesson include a dedicated `### Required Phrases` section listing every vocabulary word and key phrase that MUST appear in the script?
- Does the Lesson include a dedicated `### Forbidden Phrases` section listing phrases that create misconceptions, each with ❌ prefix and explanation?
- Are Terms to Avoid from §1.3 included in the Forbidden Phrases list?
- If either section is missing, FLAG.

### B7. Warmup Core Purpose
- Does §1.6 include a `### Core Purpose` section (not just a one-line purpose)?
- Does it include a **Key Function** explaining what the Warmup does for the module?
- Does it include a **Test** answering "If we removed this Warmup, would students lose mathematical preparation for the Lesson?" with a specific YES explanation?
- If the Core Purpose is just a purpose summary without Key Function and Test, FLAG.

### B8. Misconception Prevention Section
- Does the Lesson include a dedicated `### Misconception Prevention` section listing each targeted misconception with specific prevention strategies?
- Do the prevention strategies reference specific interaction IDs where prevention is embedded?
- If misconception prevention is only scattered in Design Notes without a consolidated section, FLAG.

### B9. Section Transition Markers
- Does each Lesson section end with a transition marker: `→ SECTION X COMPLETE. PROCEED TO SECTION Y.`?
- If transition markers are missing, FLAG.

---

## Section C: Interaction Format (spot-check)

### C3. Interaction Block Format
Spot-check 5 interactions across Warmup + Lesson:
- Pattern 1: Visual + Guide + Prompt + Student Action + Correct Answer + On Correct + Remediation: Pipeline?
- Pattern 2: Visual + Guide + No student action?
- MC interactions: Options listed + Answer Rationale with distractor analysis?
- Visual: lines on one line with all required components?
- No authored remediation (all `Pipeline`, no qualifiers)?

### C4. Interaction Type Labels
- Does every interaction in EVERY phase (Warmup, Lesson, EC, Synthesis) have a pedagogical type label in its header?
- Acceptable labels include: `[WORKED EXAMPLE]`, `[ACTIVATION]`, `[CURIOSITY GAP]`, `[CONCEPTUAL CHECK]`, `[GUIDED PRACTICE]`, `[INDEPENDENT]`, `[CONSOLIDATION]`, or other descriptive pedagogical labels.
- Legacy labels (`[Type A]`, `[Type B]`, `[Type C]`) from the old Guide vs Prompt classification system should NOT appear — these are formatting artifacts, not pedagogical labels.
- Comprehensive check, not spot-check: scan ALL interaction headers across ALL phases. If more than 2 interactions are missing type labels, FLAG. If more than 5, FAIL.

---

## Section D: Scope and Vocabulary (on Warmup + Lesson)

### D1. Forbidden Phrase Scan
- Scan ALL Guide: and Prompt: lines for every term in §1.3 "Terms to Avoid" and §1.7 "Forbidden Phrases"
- Report any matches with the specific interaction ID

### D2. Vocabulary Timing
- Verify no formal vocabulary term appears in any Guide or Prompt line BEFORE its designated staging phase in §1.3
- Check specifically: if §1.3 says formal terms are introduced in Lesson Section 2, do they appear in Warmup or Lesson Section 1?

---

## Section E: Internal Consistency (Backbone vs. Phases)

### E1. Toy Configuration Consistency
- Does §1.5 match the toy configurations actually used in §1.6–§1.7?
- Check: modes, grid states, interaction types, feedback behavior, tile supply, scaffold states

### E2. Misconception Alignment
- Does §1.4 match the Misconception Prevention section in §1.7?
- Are the same misconceptions listed with the same priority and strategies?

### E3. Data Constraint Compliance
- Do specific values in interactions fall within §1.5 constraints?
- Flag any values outside the stated ranges

### E4. Vocabulary Usage vs. Staging Plan
- Does the staging in §1.3 match when terms actually first appear in §1.6–§1.7?

---

## Gate 2 Output Format

Same format as Gate 1. Summary should flag interconnected findings (e.g., "B3, B4, and E4 are all related to the Concrete → Abstract transition — fix together").

---

# GATE 3 EVALUATION: EC + PRACTICE + SYNTHESIS + KDD

## Documents Required

- [ ] EC draft (§1.8) + Practice Inputs (§1.8.5)
- [ ] Synthesis draft (§1.9) + KDD (§1.10)
- [ ] Approved Backbone (§1.0–§1.5)
- [ ] Approved Warmup + Lesson (§1.6–§1.7)
- [ ] Working Notes
- [ ] Exit Check Phase Playbook (fresh read)
- [ ] Synthesis Phase Playbook (fresh read)
- [ ] TVP (EC, synthesis, transition sections)
- [ ] Misconceptions sheet (M[X] entries — "Where Likely to Surface" for EC targeting)
- [ ] Original Curriculum Mapping sheet (M[X] practice problems — supplementary reference)

If any document is missing, state which checks cannot be completed.

---

## Section F: Exit Check Alignment

### F1. Lesson-EC Alignment
- Does every EC problem test a skill explicitly taught in the Lesson (with student action, not just mentioned)?
- Does the Alignment Check table correctly map each EC problem to a Lesson section?
- Are the same toy modes and interaction types used in EC as in the Lesson?

### F2. No New Content in EC
- No new visual models, interaction types, vocabulary, or concepts introduced in EC
- EC difficulty does not exceed Lesson difficulty

### F3. Value Separation
- Are EC values (dimensions, areas) different from Lesson values?
- If any values are reused, is there a KDD or Design Note justifying it?

### F4. SUPPORT Tier
- If the TVP specifies SUPPORT tier problems, are they documented in the SP?
- Is the mastery threshold exclusion stated?
- Is the trigger condition specified?

---

## Section G: Synthesis Quality

### G1. Task Type Diversity
- Are at least 2 different Synthesis task types used? (Pattern Discovery, Representation Transfer, Real-World Bridge, Metacognitive Reflection)
- Is at least 1 Metacognitive Reflection task present?

### G2. Connection, Not New Teaching
- Does every Synthesis task connect to a Lesson experience rather than introducing new content?
- Is the Connection: field present on every Synthesis task?

### G3. Identity-Building Closure
- Is the closure behaviorally specific (names what the student actually did/discovered)?
- Does it avoid generic praise ("Great job!", "You're so smart!")?
- Does it preview the next module without teaching it?

### G4. Bridge to Next Module
- Does the bridge match the TVP's transition section (M[X] → M[X+1])?
- Does it match §1.1.2 Module Bridges "To [Next Module]"?

---

## Section H: Practice Phase Inputs

### H1. Skill Decomposition
- Does the Practice Inputs section provide enough information for the Pipeline?
- Does each skill map to a specific Lesson section?

### H2. Distribution Targets
- Are cognitive type percentages or weightings provided?
- Are they consistent with the Playbook's module-range recommendations?

### H3. Non-Assessed Skill Flagging
- If any skill is practiced but not assessed in EC (e.g., non-rectangle tiling), is it flagged as "exposure skill — not assessed"?

### H4. Cross-Module Spiral
- For modules 2+, are prior module skills listed for spiral review?

---

## Section E6: KDD Quality and Completeness

### E6. Key Design Decisions
**Completeness:**
- Does §1.10 document every deliberate departure from source documents or template conventions?
- Are there decisions visible in the phases (unusual toy configuration, non-standard CRA mapping, vocabulary timing choices, dimension reuse) that are NOT documented as KDDs?
- Do KDDs cover decisions from ALL phases (not just the most recent task)?

**Quality — pedagogical focus:**
- Does each KDD explain a pedagogical design choice that a writer needs to understand? (PASS)
- Or does it primarily document development process history (AF# resolutions, gate review chronology, author confirmations)? (FLAG — should be in Working Notes)
- **Quality test:** Would a writer seeing this module for the first time understand WHY it works this way from the KDDs alone? If most KDDs require development context to make sense, FLAG.

**Format:**
- Is each KDD 1-3 sentences? Title states the decision, body states the rationale. No multi-paragraph entries with Decision/Rationale/Sections subfields — inline paragraph style.
- If entries are verbose (4+ paragraphs) or use a structured subfield format instead of inline paragraphs, FLAG with recommendation to condense.

---

## Gate 3 Output Format

Same format as Gates 1-2. Pay special attention to F1 (EC Alignment) — alignment failures are always FAIL severity.

---

# GATE 4 EVALUATION: FULL STARTER PACK

## Documents Required

- [ ] Full assembled Starter Pack
- [ ] Module Starter Pack Template v2 (full)
- [ ] Working Notes (for Author Flag verification)
- [ ] M[X-1] Starter Pack (if available — full SP for cross-module checks X1-X3)
- [ ] Conceptual Spine Analysis sheet (cross-module concept progression validation)
- [ ] Important Decisions sheet (final design constraint compliance check)
- [ ] Voice Script Prompt (for Voice Agent checks)
- [ ] Guide Voice Design Reference (for Voice Agent checks)

If any document is missing, state which checks cannot be completed.

---

## Section C: Full Template Structural Compliance

### C1. Required Sections Present
- All of: §1.0, §1.1 (with 1.1.1–1.1.3), §1.2, §1.3, §1.4, §1.5, §1.6, §1.7, §1.8, §1.8.5, §1.9, §1.10, §1.11
- End marker present and correctly formatted

### C2. YAML / Hub Properties
- module_id, unit, domain, primary_toys (with Notion URLs), secondary_toys present?
- interaction_count matches actual count of interactions?

### C3. Interaction Block Format (comprehensive)
- Every student-action interaction: Visual, Guide, Prompt, Student Action, Correct Answer, On Correct, Remediation: Pipeline
- Every MC interaction: Answer Rationale with distractor analysis
- Every teaching-only interaction: Visual, Guide, "No student action."
- Every Synthesis task: Connection field present

### C4. Type Labels (comprehensive)
- Every student-action interaction labeled [Type A], [Type B], or [Type C]
- Assignments correct per Guide vs Prompt Structure Reference

### C5. Phase Infrastructure
- Warmup: Parameters table + Constraints table + Verification Checklist
- Lesson: Requirements Checklist + Pedagogical Flow + Lesson Structure table + Module-Specific Lesson Guidance (containing Required/Forbidden Phrases, Misconception Prevention, Incomplete Script Flags, Success Criteria as H3 subsections — see C7 for nesting rules) + Verification Checklist
- EC: Parameters + Constraints + Alignment Check table + Verification Checklist
- Synthesis: Verification Checklist

### C6. Scaffolding Annotations
- Are worked examples and fading stages labeled?
- Are CRA stage labels present on Lesson interactions?

### C7. Structural Conformity (Reference SP Comparison)
Compare the SP's section ordering, nesting, and heading levels against the M[X-1] reference SP (or the most recent approved SP if M[X-1] is unavailable). Check each of the following:

- **Section nesting:** Do sections that are subsections in the reference SP appear as subsections (not promoted to standalone sections) in M[X]? Key areas to verify:
  - Required Phrases, Forbidden Phrases, Misconception Prevention → must be H3 subsections WITHIN "Module-Specific Lesson Guidance" (not standalone H2 sections, and not cross-reference stubs that point elsewhere)
  - Incomplete Script Flags, Success Criteria → must be H3 subsections within their parent phase guidance section
- **Section ordering:** Does the sequence of sections within each phase match the reference SP? (e.g., interactions first, then Module-Specific Lesson Guidance, then Verification Checklist)
- **Heading hierarchy:** Are heading levels consistent with the reference? (e.g., phase sections at H2, interactions at H3, subsections at H3/H4)

If sections are present but in the wrong location or at the wrong heading level, FLAG with the specific deviation and the reference SP convention.

### C8. Format Consistency (Reference SP Comparison)
Compare the formatting of recurring structural elements against the reference SP. Check each of the following:

- **Incomplete Script Flags:** Must use bullet list format (`* **ISF-X: Description** — detail`), NOT markdown tables. Compare against reference SP.
- **Success Criteria:** Must use bullet list format (`* Criterion (verification)`), NOT markdown tables. Compare against reference SP.
- **Required Phrases / Forbidden Phrases:** Must use bullet list format (`* phrase (context)`), NOT subheaded groups with `-` lists or `❌` emoji prefixes. Compare against reference SP.
- **Verification Checklists:** Must use `- [x]` / `- [ ]` checkbox format. Compare against reference SP.
- **Parameters / Constraints / Distribution Targets:** Tables are expected and correct for these sections.

If a structural element uses a different format than the reference SP, FLAG with the specific element and what format the reference uses.

### C9. Section Content Boundaries (Negative Checks)
Verify that sections contain ONLY what they should contain — not extra subsections that belong elsewhere or don't belong at all. Check each of the following:

- **Practice (§1.8.5):** Must contain ONLY: Practice Phase Overview, Distribution Targets, Toy Constraints, Dimension Constraints (with Available Rectangle Pool), and Dimensions Used Tracking. Must NOT contain: Cross-Module Skill References, Anti-Pattern Detection, Practice Problem Type Templates, or Spiral Review Content as subsections. (These are Pipeline-level concerns, not SP-level.)
- **Module-Specific Lesson Guidance:** Must contain Required Phrases, Forbidden Phrases, Misconception Prevention, Incomplete Script Flags, and Success Criteria as direct subsections with actual content (not cross-reference stubs pointing to content elsewhere in the document).
- **No duplicate content:** Content should appear in exactly one location. If the same content appears both as a standalone section AND within its proper parent section, FLAG the duplicate.

If a section contains subsections that don't appear in the reference SP's equivalent section, FLAG with the specific extra content and recommend removal or relocation.

---

## Section E5: Standards vs. Content

### E5. Standards Alignment
- Do the standards listed in §1.1.1 match what the interactions actually teach and assess?
- Are there standards claimed but not evidenced in any interaction?
- Are there interactions that address standards not listed?

---

## Section E6: Final KDD Pass

### E6. KDD Final Check
Run ALL Gate 3 E6 checks again across the complete assembled document:

**Completeness (full-document scope):**
- Does §1.10 document every deliberate departure from source documents or template conventions across ALL phases?
- Are there decisions visible in ANY phase (unusual toy configuration, non-standard CRA mapping, vocabulary timing choices, dimension reuse) that are NOT documented as KDDs?
- Do KDDs cover decisions from ALL phases (not just the most recent task)?

**Quality — pedagogical focus:**
- Does each KDD explain a pedagogical design choice that a writer needs to understand? (PASS)
- Or does it primarily document development process history (AF# resolutions, gate review chronology, author confirmations)? (FLAG — should be in Working Notes)
- **Quality test:** Would a writer seeing this module for the first time understand WHY it works this way from the KDDs alone? If most KDDs require development context to make sense, FLAG.

**Format:**
- Is each KDD 1-3 sentences? Title states the decision, body states the rationale. No multi-paragraph entries with Decision/Rationale/Sections subfields — inline paragraph style.
- If entries are verbose (4+ paragraphs) or use a structured subfield format instead of inline paragraphs, FLAG with recommendation to condense.

**Author Flags:**
- Are all Author Flags either resolved in the SP or explicitly documented as open?
- Any unresolved flags without documentation = FAIL.

---

## Cross-Module Checks (if M[X-1] SP available)

### X1. Scope Continuity
- Do M[X]'s "Must Not Include" items align with M[X-1]'s deferrals?
- Does M[X]'s "From [Prior Module]" bridge match M[X-1]'s Synthesis closure?

### X2. Vocabulary Continuity
- Are terms M[X-1] introduced still used correctly in M[X]?
- Are terms M[X-1] deferred to M[X] actually introduced in M[X]?

### X3. Toy Configuration Continuity
- Where toys carry over, are configuration changes documented in "Changes from M[X-1]"?

---

## Gate 4 Output Format

Same format as earlier gates. Add a final section:

```
## FULL SP HEALTH CHECK
- Total interactions: [X]
- Author Flags open: [X] (list them)
- Sections with no issues: [list]
- Sections needing attention: [list]

## READY FOR SME REVIEW?
[YES / YES WITH CAVEATS / NO — explain]
```

---

# VOICE AUDIT CHECKS (Gates 2 and 4)

These checks are run by a separate voice agent. The agent reads the Guide Voice Design Reference + Voice Script Prompt, then audits all Guide:, Prompt:, and On Correct: lines.

## Voice Check V1: Observable vs. Assumed
- Every acknowledgment references observable behavior ("You found 12," "You covered the shape") not assumed states ("You understood," "You thought about that")
- No aspirational identity labels ("You're a mathematician!")
- Connecting observable behavior to mathematical practice IS permitted ("That's what strong mathematicians do")

## Voice Check V2: Conciseness
- Guide lines before student action: 1-3 sentences maximum
- Any Guide with 4+ sentences before action → FLAG with recommendation to split
- Relational bridges (like 2.4) may legitimately need 4-5 sentences — check if a visual beat is used to break the flow

## Voice Check V3: Praise Language
- On Correct lines use behavioral praise, not generic ("That's right. 12 square units." not "Great job!")
- Praise references what the student DID, not who they ARE

## Voice Check V4: Red Flag Words
- Scan all dialogue for: carefully, thoroughly, systematically, understanding, confused, persistent, thinking, realized, noticed
- Each hit → FLAG with the specific line and a suggested replacement

## Voice Check V5: Exclamation Calibration
- Count exclamation points across the full draft
- Zero across entire module → FLAG (too flat for elementary)
- More than 1 per 3 interactions → FLAG (too effusive)
- Check that exclamations land at genuine breakthrough moments, not routine correctness

## Voice Check V6: Tone Consistency
- Warmup: Medium-High energy, curious, inviting
- Lesson Section 1: Curious → builds to pivotal beat
- Lesson Section 2: Supportive, steady, scaffolding
- Lesson Section 3: Brief, confident (student is independent)
- EC: Calm, neutral, low-stakes
- Synthesis: Warm, reflective, celebratory (but behavioral)

## Voice Check V7: Controlling Language
- No "Let's" more than once per 3 interactions
- No "I want you to" or "I need you to"
- No "Can you" (rhetorical questions that are actually commands)
- Guide gives instructions, not requests

## Voice Audit Output Format

```
| # | Severity | Location | Current Text | Issue | Suggested Fix |
|---|----------|----------|-------------|-------|---------------|
| V.1 | MINOR/VERY MINOR | §1.7 Int 2.4 | "..." | [what's wrong] | [proposed change] |
```

Summary: count by severity, top 3 priority fixes, recommendation (act on / leave as-is for each).

---

**END OF EVALUATION PROMPT**
