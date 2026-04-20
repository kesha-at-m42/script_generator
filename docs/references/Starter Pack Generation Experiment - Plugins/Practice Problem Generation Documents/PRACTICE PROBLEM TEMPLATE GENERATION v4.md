# PRACTICE PROBLEM TEMPLATE GENERATION v4

## YOUR TASK

Generate Practice Problem Templates for **Module \[X\], Path \[Y\]**.

You will produce FIVE outputs:

1. **Lesson Analysis** — Constraints, fraction coverage, misconception priority, skill progression  
2. **Goal Decomposition** — Teacher-readable skill breakdown with lineage  
3. **Template Summary** — Quick reference table  
4. **Templates** — Complete JSON specifications (teacher review schema)  
5. **Coverage Summary** — Teacher-readable validation with explicit issue flagging

---

## INPUT DOCUMENTS

### Document 1: Practice Phase Playbook v3

\[REFERENCE — already loaded in project\]

Use the Playbook for:

- Lesson analysis framework (Section 2B)  
- Skill Progression Analysis (Section 2D)  
- Misconception prioritization (Section 2C)  
- Template schema (Section 4B — teacher review schema)  
- Tier distribution targets (Section 4\)  
- Cognitive type targets by module level (Section 5B)  
- Helper voice guidelines (Section 5F)  
- Output artifact formats (Section 7\)

---

### Document 2: Module Starter Pack (Sections 1.1-1.5)

\[PASTE MODULE SECTIONS 1.1-1.5 HERE\]

Extract from these sections:

- **1.1** Learning Goal (use VERBATIM)  
- **1.2** Core Concepts  
- **1.3** Standards  
- **1.4** Misconceptions to Address  
- **1.5** Fraction Requirements

**⚠️ IMPORTANT: Ignore any VPSS (Path C) material if** generation is for Path B (Singapore) only.

---

### Document 3: Lesson JSON (REQUIRED)

\[PASTE LESSON JSON HERE\]

**⚠️ The Lesson JSON is REQUIRED.** It is the source of truth for what was actually taught. Do not proceed without it.

Extract from the Lesson JSON:

- Available `toy` values (visual tools used)  
- `action_list` items demonstrated  
- Workspace constraints (range, orientation, scaffolds)  
- Which fractions were explicitly taught (by step)  
- Which concepts were explicitly introduced  
- Any constraints on interactions (e.g., pre-partitioned vs student-created)

---

### Document 4: Previous Module Outputs (REQUIRED for Modules 2+)

\[PASTE PREVIOUS MODULE GOAL DECOMPOSITION HERE\]

\[PASTE PREVIOUS MODULE TEMPLATE SUMMARY HERE\]

**⚠️ For Modules 2+, these are REQUIRED.** They show what skills students have already mastered, enabling explicit skill building.

Extract from these documents:

- Previous module's skill IDs and statements  
- What was practiced (template types)  
- Which skills this module will build upon

**Module 1 only:** Skip this document (no previous module exists).

---

### Input Parameters

| Parameter | Value |
| :---- | :---- |
| Module | \[X\] |
| Path | B (Singapore) |

---

## GENERATION INSTRUCTIONS

### Step 1: Analyze the Lesson

Before decomposing skills, analyze the Lesson JSON and previous module outputs.

**1a. Fraction Coverage Analysis**

Review the Lesson JSON step-by-step. For each required fraction from Section 1.5, determine:

- Was it explicitly used in a Lesson step? (✅ Yes — cite the step / ❌ No)  
- If No, what's the Practice Strategy? (Skill transfer — describe which generalizable skill applies)

**1b. Toy Constraints**

From the Lesson JSON, document each toy that appears with:

- Description  
- Student interaction type (from `action_list`)  
- Any constraints evident from the Lesson (e.g., "pre-partitioned" vs "student creates")

**1c. Key Constraints**

From the Lesson JSON, identify critical constraints that affect problem design. Look for:

- What students DO vs what the system DOES  
- Any scaffolds that appear/disappear  
- Range limitations (0-1 vs 0-2)  
- Interaction limitations

**1d. Misconception Priority**

Classify each misconception from Section 1.4 as:

- **Primary:** High likelihood based on Lesson interactions, target in 3+ templates  
- **Secondary:** Lower likelihood or narrower scope, target in 1-2 templates

**1e. Skill Progression Analysis (Modules 2+ only)**

Review the previous module's Goal Decomposition and Template Summary. For this module's learning goal:

1. List all previous module skills  
2. Identify which previous skills are prerequisites  
3. Classify anticipated progressions:  
   - **BUILDS ON** — extends previous skill to harder content  
   - **EXTENDS** — applies previous skill to new context/representation  
   - **COMBINES** — integrates multiple previous skills  
   - **NEW** — genuinely new skill not dependent on previous module

This analysis directly informs Goal Decomposition.

---

### Step 2: Decompose the Learning Goal

Break the learning goal into skills by component. For Modules 2+, use the Skill Progression Analysis to document each skill's lineage.

**PROCEDURAL (30-40%)** — What students DO

- Skill IDs: MX-01, MX-02, etc.  
- Each skill needs: statement, builds on (Modules 2+), lesson alignment, verbs, tiers, templates

**CONCEPTUAL (30-40%)** — What students UNDERSTAND

- Skill IDs continue sequentially  
- Each skill needs: statement, builds on (Modules 2+), lesson alignment, verbs, tiers, templates

**TRANSFER (20-30%)** — How students APPLY

- Skill IDs continue sequentially  
- Each skill needs: statement, builds on (Modules 2+), lesson alignment, verbs, tiers, templates

**Lesson Alignment Requirement:** Every skill MUST show which Lesson step(s) taught it, OR note "Skill transfer" with rationale.

**Progression Requirement (Modules 2+):** Every skill MUST include `Builds on:` field referencing previous skill IDs or "NEW" with rationale.

---

### Step 3: Generate Templates

For each skill, generate 1-3 templates varying by tier and presentation.

**Cognitive Type Targets** (from Playbook Section 5B — adjust for module stage):

| Module Stage | create | identify | compare | apply |
| :---- | :---- | :---- | :---- | :---- |
| Early (1-3) | 25-35% | 35-45% | 15-20% | 5-15% |
| Building (4-6) | 40-50% | 25-30% | 15-20% | 10-15% |
| Advancing (7+) | 30-40% | 20-25% | 20-25% | 15-25% |

---

### Step 4: Validate Coverage

Before finalizing, verify:

- [ ] All skills have at least one template  
- [ ] All skills have lesson alignment documented  
- [ ] All skills have progression documented (Modules 2+)  
- [ ] Tier distribution includes all five tiers appropriately  
- [ ] Cognitive type distribution matches module stage targets  
- [ ] All required fractions from Section 1.5 covered  
- [ ] All PRIMARY misconceptions targeted in 3+ templates  
- [ ] All SECONDARY misconceptions targeted in 1-2 templates  
- [ ] Skill progressions from Lesson Analysis match Goal Decomposition

---

## REMINDERS

1. **Lesson JSON is REQUIRED** — Do not generate templates without analyzing the actual Lesson  
     
2. **Previous Module Outputs REQUIRED (Modules 2+)** — Goal Decomposition and Template Summary from Module N-1 enable skill progression tracking  
     
3. **Skill Progression flows through outputs** — Analysis in Output 1 → Applied in Output 2 → Validated in Output 5  
     
4. **Lesson Alignment is REQUIRED** — Every skill must document which Lesson step taught it  
     
5. **Helper voice** — Keep `prompt_examples` and `success_dialogue` direct and task-focused  
     
6. **Stay within Lesson boundaries** — Use toys and actions that appear in the Lesson JSON or previous modules templates. Ask in chat for verification or other possibilities.   
     
7. **Use Section 1.1 Learning Goal VERBATIM** — Do not paraphrase  
     
8. **Prioritize misconceptions** — PRIMARY in 3+ templates, SECONDARY in 1-2 templates  
     
9. **Teacher Review Schema** — Use the Practice Phase Playbook template; engineering details are added in a later pipeline step  
     
10. **Flag issues explicitly** — Coverage Summary must list options to fix any gaps  
      
11. **Module 1 is special** — Skip Document 4, Skill Progression Analysis, and `Builds on` fields

---

## BEGIN GENERATION

Start with Lesson Analysis, then Goal Decomposition, then Template Summary, then Templates (JSON), then Coverage Summary.  
