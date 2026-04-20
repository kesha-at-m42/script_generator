# G3U5 VPSS → SP Migration Playbook

**Scope:** Grade 3 Unit 5 (Fractions), Modules 1–12
**Source format:** VPSS Starter Packs (legacy)
**Target format:** Module Starter Pack Template v3 (02.04.26, updated 03.30.26)
**Canonical reference for conflicts:** STARTER PACK STRUCTURAL SKELETON.md
**Calibrated against:** G3U2M1, G3U2M8, G3U2M11 (shipped, Notion-live)

---

## 1. PROCESS ORDER

For each module, execute in this sequence:

1. **Read the Lesson Reframing Tracker** — Module Mapping sheet first. Extract: OUR Lessons, standards, misconceptions, cluster, convergence status, EC focus, vocabulary scaffolds.
2. **Read the Misconceptions sheet** — Get IDs, descriptions, best visuals, risky visuals for the module's mapped misconceptions.
3. **Read the Toy Specifications file** — Get Notion URLs for all toys used in the module. These URLs must appear as `**Notion Spec:**` links in §1.5 of the SP (see Toy Specifications Format below).
4. **Read the VPSS source file** — Understand the existing content, interactions, and flow.
5. **Migrate to SP template** — Apply all conventions below.
6. **Run Gate 4 checkers** — Address MAJOR findings. Triage MINOR findings against this playbook.
7. **Apply calibration fixes** — Use Section 3 below as a checklist for conventions the checkers can't catch.
8. **Structural completeness check** — Before Notion-Ready, verify:
   - Exactly 3 H1s present: Module title, `# BACKBONE`, `# PHASE SPECIFICATIONS`
   - `# END OF MODULE [N] STARTER PACK` at the end
   - All lesson sections use `### 1.7.X LESSON SECTION X:` format
   - All interaction fields use `* **Field:**` bullet format
   - No `L.` prefix on lesson interaction IDs
   - All Visual fields name the toy: `* **Visual: [Toy Name].**` (not bare `* **Visual:**`)
   - §1.5 Toy Specifications include `**Notion Spec:**` link and `**Changes from M[N-1]:**` for each toy
9. **Sync Notion-Ready copy** — `cp` the SP to the `_Notion_Ready.md` variant. The Notion-Ready file is a direct copy of the Starter Pack (no transforms). At Notion page creation time:
   - Page title = "Module [N]: [Title] (VPSS)"
   - Properties: Module Number, Unit, IM/OUR Lessons, Primary Toys (relation URLs), Status → "Initial Draft"
   - Content pasted from `# BACKBONE` onward (module H1, Version line, and YAML block become page title/properties, not body content)

---

## 2. STRUCTURAL CONVENTIONS

### Heading Hierarchy
- Exactly 3 H1s: Module title, BACKBONE, PHASE SPECIFICATIONS
- All sections use H2 (e.g., `## 1.0 THE ONE THING`)
- Everything inside sections uses H3 (interactions, subsections, toys, checklists)
- NO H4s. Convert to bold inline labels if needed.
- NO bold markers on any heading (`## 1.0 THE ONE THING`, not `## **1.0 THE ONE THING**`)

### Interaction Header Format
```
### Interaction [ID]: [Title] [TYPE LABEL]
```
- H3, no bold
- Type label in square brackets, ALL CAPS (e.g., `[WORKED EXAMPLE]`, `[GUIDED PRACTICE]`, `[ACTIVATION]`)
- **Lesson interaction IDs** use `[section].[sequence]` numbering: `1.1`, `1.2`, `2.1`, `2.3`, etc. NO `L.` prefix (VPSS convention — do not carry forward).
- **Phase-prefixed IDs** for non-lesson phases: `W.1`, `W.2` (Warmup), `EC.1`, `EC.2` (Exit Check), `S.1`, `S.2` (Synthesis)

### Lesson Section Heading Format
```
### 1.7.X LESSON SECTION X: [Title]
```
- H3, no bold, with `1.7.X` numbering prefix and "LESSON SECTION" label
- CRA stage info goes in the Lesson Structure table (§1.7), NOT in the heading itself

### Interaction Field Bullet Format

Every field in an interaction block starts with `* ` (bulleted list item). This matches Template v3 and the Notion rendering format:

```
* **Purpose:** [text]
* **Visual: [Toy Name].** [state]
* **Guide:** "[dialogue]"
* **Prompt:** "[instruction]"
* **Student Action:** [type]
* **Correct Answer:** [answer]
* **On Correct:** "[feedback]"
* **Remediation:** Pipeline
```

Do NOT use bare paragraph-style fields (`**Purpose:** [text]` without `* ` prefix). This was an M2 lesson — bare fields required bulk-fixing before Notion paste.

### Field Order (student-facing interactions)
```
Purpose → Visual → Guide → Prompt → Student Action → [Options] → Correct Answer → [Answer Rationale] → On Correct → [Connection] → Remediation → [Remediation Note] → [Design Note] → [Voice Note]
```

### Field Order (teaching-only interactions)
```
Purpose → Visual → Guide → [additional Guide/Visual pairs for multi-step demos] → No student action. → [Design Note]
```

### Field Names — Use ONLY These
Standard: Purpose, Visual, Guide, Prompt, Student Action, Options, Correct Answer, Answer Rationale, On Correct, Connection, Remediation, Remediation Note, Design Note, Voice Note

Do NOT use: Guide [Strategy], Visual Demo, Scaffolding Note, Pattern Callout, Critical Design Note, Visual Comparison, Student Response

### Visual: Line Format
```
* **Visual: [Toy Name].** [State description]
```
- Toy Name must match the §1.5 header exactly
- For multi-toy scenes: `Visual: Grid Arrays and Hexagons.`
- Mode in parentheses after toy name when applicable: `Visual: Grid Arrays (Tiling Mode).`

### Toy Specifications Format (§1.5)

Each toy entry in §1.5 must include:

1. **H3 header:** `### 1.5.X [Toy Name]` (with `[NEW]` or `[FAMILIAR]` tag)
2. **Notion Spec link:** `**Notion Spec:** [Display Name](URL)` — URL from the Toy Specifications file
3. **Changes from prior module:** `**Changes from M[N-1]:** [description]` — what's new or different vs. the previous module that used this toy. For toys appearing for the first time in the unit, describe the initial configuration.

```
### 1.5.1 Grid Arrays [FAMILIAR]

**Notion Spec:** [Grid Arrays/Fraction Grids](https://www.notion.so/ocpgg/...)
**Changes from M01:** Pre-partitioned only; no student-created partitions...
```

**Why this matters:** Without the Notion Spec link, the Notion page has no connection back to the toy's canonical specification. Without the Changes line, authors can't see what's different about this module's use of the toy.

### Remediation
- Always `Pipeline` for assessed interactions
- No authored remediation dialogue
- Optional `Remediation Note:` for pipeline guidance (what it should do, not what it should say)
- Teaching-only interactions: no Remediation field

---

## 3. CALIBRATION CONVENTIONS (not enforced by checkers)

These were identified by comparing M1 against shipped reference SPs (G3U2M1, M8, M11). The Gate 4 checkers do not fully validate these — apply them manually.

### 3.1 On Correct: Observable/Factual Style

**Rule:** Start every On Correct with either the factual answer or an observable description of what the student did. No generic praise openers.

**Forbidden openers:**
- Excellent! / Amazing! / Perfect! / Wonderful! / Great! / Good!
- Right! / Yes! / Exactly right! / That's right!

**Correct patterns:**
- Factual: `"Six equal parts: sixths."`
- Observable action: `"You matched each symbol to the right rectangle."`
- Value restatement: `"1/4 means one part out of four equal parts."`
- Conceptual: `"When you share with fewer people, each person gets a bigger piece."`

**Why:** Reference SPs (M8, M11) explicitly list generic praise as a Forbidden Phrase. All On Correct feedback in shipped modules uses observable acknowledgments or factual restatements. This is grounded in growth mindset research — praise the observable work, not the person.

### 3.2 Forbidden Phrases Section

Every module's Lesson section must include a Forbidden Phrases list with at least these universal items plus module-specific additions:

**Universal (include in every module):**
- ❌ "Today we will learn..." / "Today you're going to..." — Non-session-relative, creates performance pressure
- ❌ "Yesterday" / "Today" / "Tomorrow" — Non-session-relative. Use "last time" / "this time" / "next time"
- ❌ "Perfect!" / "Excellent!" / "Amazing!" / "Great job!" — Generic overpraise. Use observable acknowledgments.
- ❌ "You carefully..." / "You understood..." / "You're thinking..." — Assumed internal states
- ❌ "You have to..." / "You need to..." — Controlling language. Use "Try..." or "You can..."
- ❌ "Formula" (standalone) — Suggests rote memorization

**Module-specific:** Add terms that are out of scope for the current module (e.g., M1 forbids "numerator/denominator" because that's M2 vocabulary).

### 3.3 Misconception Cross-References in Answer Rationale

When a distractor option in an MC interaction directly targets a documented misconception from the Lesson Reframing Tracker, tag it with the tracker ID:

```
- Rectangle B: #1 — Equality distractor; has 4 parts but they are unequal. Student who counts parts without checking size will select this (Misconception #1)
```

Format: `#[ID]` prefix on the distractor line, with `(Misconception #[ID])` or `(Misconception #[ID]: [Short Name])` at the end.

### 3.4 Verification Checklist Structure

Every phase needs a Verification Checklist. For the Lesson phase, use subsections:

```
### Verification Checklist (Lesson)

**CRA Structure:**
- [x] ...

**Explicit Instruction:**
- [x] ...

**Student Action:**
- [x] ...

**Voice & Format:**
- [x] ...

**Remediation:**
- [x] ...

**Cross-References:**
- [x] Required Phrases — ...
- [x] Forbidden Phrases — ...
- [x] Misconception Prevention — ...
```

### 3.5 Voice Conventions

- No em dashes in student-facing dialogue (Guide, On Correct, Prompt, Connection). Use commas, colons, periods, or parentheses.
- Max 1 exclamation per 3 interactions per phase
- Max 3 sentences in Guide before student action (exception: worked examples and multi-step demos)
- Contractions in all dialogue ("you've" not "you have", "we've got" not "we have")
- Session-relative language only ("last time" / "this time" / "next time")
- Red flag words to avoid: carefully, technique, method, understanding (rephrase with action verbs or concrete descriptions)
- Vocabulary in ALL CAPS on first formal introduction in dialogue

### 3.6 YAML Front Matter

```yaml
---
module_id: M[XX]
unit: Unit 5
domain: fractions
conceptual_spine_cluster: "[from tracker Module Mapping]"
primary_toys:
  - name: "[Toy Name]"
    notion_url: "[from Toy Specifications file]"
---
```

---

## 4. CHECKER TRIAGE GUIDE

When running Gate 4 checkers, use this guide to distinguish real issues from known false positives:

| Finding | Type | Action |
|---|---|---|
| ST5/ST6 in checklist meta-text | False positive | Ignore — these are checklist items mentioning tags, not actual tags |
| ST7 version line | Real | Add `**Version:** [date]` after H1 |
| ST13 Lesson checklist | Real | Ensure heading is `### Verification Checklist (Lesson)` |
| VO1 red flag words | Real | Replace with action verbs or concrete descriptions |
| VO2 exclamation density | Real | Thin exclamations to ≤1 per 3 interactions per phase |
| VO3 superlative_praise | **Real — MAJOR** | Rewrite On Correct per §3.1 above |
| VO3 command_language "need to" | Context-dependent | "if you need to" = false positive; "You need to [do X]" = real |
| VO3 rhetorical "Can you..." | Pedagogical choice | Keep if invitational framing for guided practice |
| VO4 verbose_guide | Context-dependent | Keep for worked examples/multi-step demos; shorten for simple prompts |
| VO5 missing contractions | Real | Fix — dialogue should use contractions |
| VO9 Perfect overuse | **Real** | Max 0 per module (use observable acknowledgments instead) |
| I6 missing Correct Answer | Real | Add for every student-action interaction |
| I12/I13 teaching-only fields | Real | Teaching-only: no Remediation, include "No student action." |
| I20 On Correct word count | Context-dependent | Teaching moments can exceed 20 words; pure confirmation should be ≤15 |
| TC1 multi-toy Visual | Checker limitation | "Grid Arrays and Hexagons" is valid for multi-toy scenes |
| V4 assessment terms in EC | Checker config | May flag terms not in EC dialogue; verify manually |
| MM* module map findings | **Ignore for G3U5** | Checker references Area/Measurement data, not Fractions |

---

## 5. MODULE-SPECIFIC NOTES

### Module 1: What Makes a Fraction?
- **Status:** Complete. Calibrated. Notion-Ready synced.
- **OUR Lessons:** 1, 2
- **Misconceptions:** #1 (Unequal Parts — PRIMARY), #2 (Misidentifying the Whole — SECONDARY)
- **Cluster:** Cluster 1: Defining Fractions through Equal Parts
- **Toys:** Grid Arrays, Hexagons, Pre-Partitioned Rectangles (Warmup only)

### Module 2: Naming Unit Fractions
- **Status:** Complete. Gate 4 PASS (0 findings). Notion-Ready synced. Pending Notion page creation.
- **OUR Lessons:** 3
- **Misconceptions:** #3 (Numerator/Denominator as Independent — PRIMARY), #6 (Reversing Numerator/Denominator — SECONDARY), #8 variant (Bigger Number = Bigger Piece — SECONDARY)
- **Cluster:** Cluster 2: Naming Unit Fractions
- **Toys:** Grid Arrays, Circles (NEW — requires [TOY_INTRO]), Hexagons (familiar)
- **Migration Notes:**
  - Baseline was much cleaner than M1 (52 findings vs 147)
  - Synthesis was already compliant at baseline (5 interactions)
  - Main work: structural reformatting, interaction field completion, §1.8.5 + §1.10 creation
  - Author Flags: EC.2 multi-step structure, Section 3 duration, circle partitions in [TOY_INTRO], non-unit fraction (2/3) in Synthesis S.1
- **Post-Gate 4 Revisions (6 items):** L.1.5 distractor fix, L.1.2 confirmation click added, S.1 Design Note for 2/3, EC.4 added, W.1 simplified, §1.5.1 orientation constraint
- **Format Fixes (caught during Notion calibration):** Bullet prefixes on all interaction fields, lesson section heading naming (`### 1.7.X LESSON SECTION X:`), `L.` prefix removal from interaction IDs, `# PHASE SPECIFICATIONS` H1 added, `**Notion Spec:**` links added to §1.5 Toy Specifications, all Visual fields updated to name the toy (`Visual: [Toy Name].`). These are now documented in §2 above so M3+ won't repeat them.

### Modules 3–12
- Pending. Populate this section as each module is migrated.

---

**Document Version:** 03.31.26
**Last Updated:** 2026-03-31
