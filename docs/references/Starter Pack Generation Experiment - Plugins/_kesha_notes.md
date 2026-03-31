# Kesha's Notes — Starter Pack Process Review
**Started:** 2026-03-30

---

## Thoughts & Observations (in order of reading)

### On modularity
Modules as currently designed depend on each other sequentially. For true modularity, concept isolation needs to happen at the **mapping level** — identify which modules have hard dependencies (e.g., tool introduction) vs. which could stand alone. Tool teaching sections should ideally be independent from module scripts and inserted programmatically when a student first encounters a tool, rather than baked into a specific module's flow.

### On Module Variables / "Fill in once"
The `HOW TO USE` section asks you to fill in Module Variables (Module ID, title, unit, domain, grade, prior/next module) as if it's a meaningful setup step. It's not — it's just metadata lookup. This information should already exist externally and be referenced, not re-entered. The way it's written makes it feel like a ritual when it should be a simple lookup.

- **Possible fix:** Module metadata lives in a persistent file (e.g., in Working Notes on first run, then reused). The Guidance should point to it, not ask Cowork to fill it in from scratch each time.
- **Kesha to verify:** whether this is actually being rebuilt each session or if there's already a reuse mechanism.

### On locally-first / Notion fallback
Liked the pattern of checking locally first, falling back to Notion if not found. Good default behavior to keep.

### On evaluation agents
Breaking evaluation into task-specific agents is good design. However the agent definitions need a closer audit for:
- Overlap between agents
- Conflicting instructions across agents
- **Kesha to do this herself** by reading each agent definition and observing them run.

### Q: Agents vs. plugins vs. skills — what's the difference?
*(Come back to this after seeing them in action.)*

### On `sp_interaction_check`
Curious how well Pattern 1/2 compliance checking works against markdown in practice. Test empirically when running.

### On Working Notes
Working Notes are doing double duty: continuity mechanism AND source extraction record. These could stay combined, BUT the Module Variables section in `HOW TO USE` shouldn't be a separate "fill in" step — it should be part of Working Notes on first run only, then reused. The Guidance should make this clearer.

### On "After completing Tables A, B, and C, before drafting."
Not a complete sentence. Reads like a note to self that got published as an instruction. Needs rewriting.

### On the Edit Reconciliation section
> "This is the single highest-ROI extraction step. M8 analysis showed 3 of 5 Backbone issues traced to edits that were footnoted but not applied."

Incomprehensible without M8 context. The Guidance references numbered TVP edits (Edit 83, 84, 88, 91) as if the reader knows what these are — but "edits" as a concept in the TVP is never introduced or explained.

### On the TVP
The TVP is described as a static "Tool/Visual Plan" but apparently it's a living document with numbered amendments. This is never explained in the Guidance. **Need to open `Grade 3 Unit 2_ Toy Flow.docx` during Task 1 execution to understand what this actually looks like.**

### On glossary/dictionary
The Guidance uses terms (Conceptual Spine, Backbone, KDD, TVP, CRA, etc.) without defining them anywhere. A glossary is needed — either as a standalone doc or as a section at the top of the Guidance.

---

## Open Questions
- [ ] What exactly are "numbered edits" in the TVP? Is the TVP versioned/amended over time?
- [ ] Agents vs. plugins vs. skills — what's the distinction in practice?
- [ ] Is module metadata actually being rebuilt each session or is there a reuse mechanism already?
- [ ] Why is there no M6 Notion_Ready file?

---

## Where to Continue Tomorrow

**You stopped at:** Task 1 — Edit Reconciliation Pass (the section about numbered TVP edits, ~line 354 of the Cowork Guidance).

**Next:**
1. Continue reading Task 1 from **Section 6: Data-Level Constraint Audit** through to the end of **GATE 1**.
2. Run Task 1 in Cowork on M9 (even though a backbone already exists — run it fresh to test the process).
3. Read Task 2, then run it.
4. Then Gate 2, etc.

**Note:** M9 already has a backbone and Working Notes from prior sessions. Running Task 1 fresh is a deliberate choice to test the process end-to-end, not to reuse prior work.
