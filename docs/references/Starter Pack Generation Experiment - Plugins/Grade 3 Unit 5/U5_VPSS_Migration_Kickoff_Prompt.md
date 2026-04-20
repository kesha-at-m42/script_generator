# Unit 5 VPSS Migration — Kickoff Prompt

**Copy this into a new Cowork chat to start the migration.**

---

## PROMPT

You are helping me migrate legacy VPSS (Visual–Procedural–Symbolic–Social) Starter Packs for **Grade 3, Unit 5: Fractions** to our current Module Starter Pack template and pipeline, then push them to Notion.

### Context

There are 12 legacy VPSS modules in `Grade 3 Unit 5/VPSS/`. These were written in December 2025–January 2026 — before our current SP template (02.04.26), Cowork Guidance doc (v4.2), phase playbooks, evaluation pipeline, or Notion integration existed. They need to be brought up to current standards and pushed to the Notion database.

**This is NOT regeneration from scratch.** The legacy files contain substantial pedagogical design work — learning goals, scope boundaries, misconception maps, toy specifications, interaction sequences, and dialogue. The task is to *migrate* this content into the current template structure, fill structural gaps, apply current voice/format standards, evaluate, and push.

### What's Different Between Legacy VPSS and Current Template

Read both a legacy file (e.g., `Grade 3 Unit 5/VPSS/MODULE 1_ WHAT MAKES A FRACTION_ - VPSS.WIP.12.18.25.md`) and the current template (`MODULE STARTER PACK TEMPLATE.02.04.26.md`) before starting. Key structural gaps to expect:

1. **Missing sections**: Legacy files lack §1.8.5 Practice Phase Inputs, §1.10 Key Design Decisions (KDD), and §1.11 Final Formatting Audit. These must be created.
2. **Interaction block format**: Legacy uses a loose bullet format (`* **Purpose:**`, `* **Visual:**`, `* **Guide:**`). Current template requires the full interaction block format with all fields: Purpose, Pattern, Phase, Visual, Student Action, Correct Answer, On Correct, On Incorrect, Remediation, Guide, Prompt. Many legacy interactions are missing fields (especially Pattern, Student Action classification, Correct Answer, On Correct/On Incorrect as separate fields).
3. **No YAML front matter**: Legacy files have an informal code-fenced metadata block. Convert to the template's YAML format.
4. **No KDD section**: Design decisions are scattered as inline comments. These need to be collected into a formal §1.10.
5. **Voice standards**: Legacy was written before the Voice Script Prompt and Guide Voice Design Reference. Dialogue needs a voice pass against current standards (observable behavior only, no assumed internal states, calibrated exclamation, session-relative language).
6. **Warmup structure**: Legacy warmups may not follow the current 3-interaction Warmup Phase Playbook structure (Hook → Escalation → Bridge). They have warmup content but may need restructuring.
7. **Synthesis structure**: Legacy synthesis may not follow the Synthesis Phase Playbook's required elements (Celebration, Retell, Connect, Preview).
8. **Lesson phase CRA compliance**: Current template requires explicit CRA (Concrete→Relational→Abstract) phase labeling on every Lesson interaction. Legacy files have pedagogical progression but may not label it.
9. **Remediation format**: Legacy uses informal L-M-H descriptions. Current template requires `Pipeline` only in the SP (remediation details go to a separate remediation document).
10. **Dimension tracking**: No dimension tracking exists. Needs to be created during migration.

### Source Documents Available

- `Module Starter Pack Cowork Guidance.md` — **Read this first.** It's the master process guide (v4.2, 45 Known Patterns). Follow its Task structure.
- `MODULE STARTER PACK TEMPLATE.02.04.26.md` — The target template format.
- `Warmup Phase Playbook.md`, `Lesson Phase Playbook.md`, `Exit Check Phase Playbook.md`, `Synthesis Phase Playbook.md` — Phase-specific requirements.
- `Guide Voice Design Reference - 01.09.26.md` and `Voice Script Prompt - 02.04.26.md` — Voice standards.
- `STARTER PACK STRUCTURAL SKELETON.md` — Quick-reference for section order and required fields.
- `Grade 3 Unit 5/Pedagogical Justification for Curriculum Adaptation.md` — Unit 5 design rationale (classroom→digital adaptation).
- `Grade 3 Unit 5/Grade 3, Unit 5 Lesson Reframing Tracker.xlsx` — Module-level tracking.
- `Grade 3 Toy Specifications - Notion Links.md` — Toy spec Notion pages (you'll need Unit 5 toy specs; check if they exist).

### Migration Process Per Module

For each module, follow a **5-step migration pipeline** (modified from the Cowork Guidance 4-task pipeline, with a pre-migration baseline step added):

**Step 0 (Baseline Evaluation) — Quantify the gap BEFORE migrating:**
- Run all L1 checkers at Gate 4 level against the raw legacy VPSS file.
- This gives you a concrete, quantitative checklist of what's structurally missing.
- **For Module 1, this has already been done.** Read the baseline report at `Grade 3 Unit 5/L1_EVALUATION_REPORT_M01_VPSS_Baseline.md`. Key findings:
  - Parser detected 24/24 interactions (good recall), 2 unknown patterns
  - **147 total findings** (55 MAJOR, 92 MINOR) — this is expected for a legacy file
  - Real structural gaps: Synthesis catastrophically under-scoped (1 interaction vs 3-8 expected), 19 interactions missing Purpose fields, 19 missing Correct Answer, no KDD section, session duration ~30-50% under budget
  - Format-only gaps: 12 instances of "Full L-M-H" remediation (→ Pipeline), 22 missing type labels, em dashes in dialogue
  - Core pedagogy is sound — the interaction sequence and conceptual progression are solid
- For M2-M12, run Step 0 yourself at the start of each migration chat. Save as `L1_EVALUATION_REPORT_M[XX]_VPSS_Baseline.md`.

**Step 1 (Backbone) — ADAPT, don't recreate:**
- Read the legacy VPSS file completely.
- Read the current template.
- Read the Step 0 baseline report — use it as your migration checklist.
- Map legacy sections → template sections. Identify what exists, what's missing, what needs restructuring.
- Create the Backbone by transplanting existing content into the template structure.
- Fill structural gaps: YAML front matter, Practice Phase Inputs, KDD shell.
- Create Working Notes documenting: what was carried forward, what was added, what was changed, and why.
- **Do NOT rewrite pedagogical content that is sound.** Preserve learning goals, scope boundaries, misconception maps, vocabulary architecture, and toy specifications as-is unless they conflict with current standards.
- **Run L1 at Gate 1 level** after completing the Backbone. Compare finding count to baseline — you should see structural findings drop significantly (template structure now present) while interaction-level findings remain (not yet addressed). Document the delta in Working Notes.

**Step 2 (Drafting) — Fill interaction-level gaps:**
- Convert every interaction to full block format (all required fields).
- Add missing fields: Pattern classification, Student Action type, Correct Answer, On Correct/On Incorrect as separate lines.
- Apply CRA phase labels to Lesson interactions.
- Restructure Warmup to playbook format (Hook → Escalation → Bridge) if needed.
- Restructure Synthesis to playbook format if needed — **for M1, this is a major gap: legacy has 1 synthesis interaction, current standard requires 3-8 with Celebration/Retell/Connect/Preview structure.**
- Standardize remediation to `Pipeline` only.
- Draft the KDD from scattered design decisions.
- Run voice pass on all dialogue.
- **Run L1 at Gate 2 level** after drafting. Interaction-level findings should now drop. Remaining findings should be mostly MINOR/NOTE (voice nuances, dimension tracking gaps). Document the delta.

**Step 3 (Gate 4 Evaluation) — Full pipeline:**
- Run L1 checkers (`sp-quick-check`) at Gate 4 level.
- Fix any CRITICALs and real MAJORs.
- Document false positives (expect some — the legacy content may have intentional patterns the checkers don't know about).
- **Target: fewer than 10 MAJORs at Gate 4, all documented as either fixed or intentional design.**
- Run L2 agents if available (warmup eval, voice eval at minimum).
- Produce a Gate 4 Evaluation Report: `G3U5M[XX]_Gate4_Evaluation_Report.md`.
- **Compare final finding count to Step 0 baseline.** This is the migration quality metric — e.g., "147 baseline → 8 final (5 by-design, 3 minor)" tells us the migration was thorough.

**Step 4 (Notion Page Creation + Handoff for Manual Paste):**

Per Known Pattern #32: the agent creates the page shell, the human pastes the content. Do NOT attempt to push 800+ lines of markdown through the Notion API.

- **Agent creates the page** in the "Level Math Curriculum Documents" database using `notion-create-pages`:
  - Parent: `data_source_id: "3185917e-ac52-80c0-a46b-000be3c6a416"`
  - Properties:
    - `Name`: "Module X: [Title]" (e.g., "Module 1: What Makes a Fraction?")
    - `Module Number`: integer (e.g., 1)
    - `Unit`: "Unit 5"
    - `Status`: "Initial Draft"
  - Content: Leave **empty** or include only a placeholder like "Content pending manual paste."
- **Agent produces a Notion-Ready file** (`G3U5M[XX]_Notion_Ready.md`) — this is the final migrated SP with all evaluation findings resolved, formatted for clean paste.
- **Human pastes** the Notion-Ready content into the page in the Notion web editor.
- **Human spot-checks**: interaction block formatting, tables, no content truncation, all section headers present.
- **Agent can verify** after paste by fetching the page and checking section header count, total length, and presence of key markers (§1.0 through §1.11).

### Scope for This Chat

**Start with Module 1 only.** Module 1 is the calibration module — we'll use it to establish the migration pattern, identify recurring issues, and refine the process before batching subsequent modules. Once Module 1 is migrated, evaluated, and pushed, we'll assess how much of the process can be templated for M2-M12.

Save the migrated file as `G3U5M1_Starter_Pack.md` and Working Notes as `G3U5M1_Working_Notes.md` in the `Grade 3 Unit 5/` folder.

### Important Constraints

- **Preserve pedagogical intent.** These modules were carefully designed. The migration is about format and structure, not redesign. If you think a pedagogical choice is wrong, flag it as an Author Flag — don't silently change it.
- **WIP status is expected.** The legacy files are marked WIP. Some may have incomplete sections (empty bullets, placeholder text, TODO markers). Document these in Working Notes and flag for author review rather than inventing content.
- **No TVP exists for Unit 5.** Unlike Unit 2 where we had TVPs (Teacher Vision Packs) as source documents, Unit 5's VPSS files ARE the source of truth. There is no upstream document to cross-reference against.
- **Unit 5 is Fractions, not Area.** The Known Patterns in the guidance doc are calibrated from Unit 2 (Area and Multiplication). Some patterns are universal (#1-30, #43-45); others are Unit-2-specific (#36-42). Apply judgment.
- **Cross-module awareness matters.** Unit 5 has a tight conceptual spine (12 modules building from "what is a fraction" to "comparing unlike fractions"). Read the Pedagogical Justification doc to understand the unit arc before starting Module 1.

### Start

1. Read the Cowork Guidance doc (at minimum: the Task descriptions and Known Patterns).
2. Read the Step 0 baseline report (`Grade 3 Unit 5/L1_EVALUATION_REPORT_M01_VPSS_Baseline.md`) — this is your migration checklist.
3. Read the Module 1 legacy VPSS file completely.
4. Read the current template.
5. Read the Warmup, Lesson, EC, and Synthesis playbooks (at minimum: the required elements checklists).
6. Read the Pedagogical Justification doc to understand Unit 5's conceptual arc.
7. Begin Step 1: Map legacy → template, create Backbone, document gaps in Working Notes.
8. Run L1 at Gate 1. Document delta vs baseline.
9. Proceed through Steps 2-4 with L1 runs at each gate.

The goal is a Module 1 that passes Gate 4 with a documented migration trail (baseline → Gate 1 → Gate 2 → Gate 4 finding counts) that proves the migration was thorough. This becomes the template for M2-M12.

Go.
