# Patches to Practice Template Prompt v1 — Spine Anchoring

**Purpose:** Four changes + one addition to anchor the v1 template generation prompt on the Unit Skill Spine, converting it into the "patched v1" (combined Stage 1+2) for Phase 1 testing.

**Test plan:** Run patched v1 on M1 (ground truth comparison), then M2 or M7 (generalization).

---

## PATCH 1: Add Skill Spine as Required Input

**Where:** After `### Input 2: Previous Module's Template Summary` (line ~39), before `### Input 3: Module Starter Pack`

**Insert:**

```
### Input 2B: Unit Skill Spine (REQUIRED)

The Unit Skill Spine is the unit-level skill registry generated in Stage 0 of the Practice Pipeline. It defines every assessable skill thread across all modules in the unit, with cross-module progression tracking. The spine is your **baseline** for skill decomposition — you anchor on it, not on §1.8.5 or your own bottom-up analysis.

You will use these sections:

| Spine Section | What You Extract | How You Use It |
|---|---|---|
| **Skill Threads** | Per-skill: ID, description, component, primary verb, thread type, module appearances (Introduced/Practiced/Extended), misconceptions, standards | Baseline for this module's Skill Decomposition. Every spine skill active in this module gets a row in your decomposition table. |
| **Cross-Module Matrix** | Which skills are INT/PRC/EXT in this module | Determines which skills to template. INT = newly introduced (focus on confidence/support/baseline). PRC = practiced (focus on baseline/stretch). EXT = extended (focus on stretch/challenge). |
| **Scoping Decisions Log** | Why skills were split, folded, or kept | Respect these decisions. If you disagree, flag it — don't silently override. |
| **Open Questions** | Unresolved scoping questions | If an open question affects this module, note it in your analysis and propose a resolution. |

**Critical rule:** The spine is the starting point for your Skill Decomposition, not the ceiling. Stage 1 may decompose a spine skill into module-level sub-skills when the module's teaching reveals distinct cognitive operations that produce different template designs (see Skill Decomposition Rules below).
```

---

## PATCH 2: Skill Decomposition Rules (replaces current Step 1C: Skill Inventory)

**Where:** Replace the current `**C. Skill Inventory**` section (lines ~435-440) with the following:

**Replace:**
```
**C. Skill Inventory**
Derive from Cognitive Focus + What Students DO + Exit Check:
- List each assessable skill with description, cognitive verb, and component
- Note which skills are paired (e.g., always tested together)
- Note which skills are observation-only (not assessable in Practice)
- If SP §1.8.5 exists, use its Skill Tracking table as the authoritative skill list
```

**With:**
```
**C. Skill Decomposition (spine-anchored)**

Start from the Unit Skill Spine, not from a blank slate.

**Step C.1 — Import spine skills active in this module.**
Read the Cross-Module Matrix. Every skill marked INT, PRC, or EXT in this module gets a row in your Skill Decomposition table. Copy the spine's ID, description, component, and verb.

**Step C.2 — Check practice-scope eligibility.**
Not every active skill produces practice templates in every module. A skill may be introduced in this module's warm-up or early lesson but not yet assessable independently. For each active skill, check:
- Does this module's EC test this skill (directly or as a component)?
- Does the Toy Flow's Practice subsection reference this skill's cognitive action?
- Is there at least one Lesson interaction where the student performs this action independently (not just observing)?

If the answer to all three is NO, mark the skill as `[TEACHING ONLY — no templates this module]` and explain why. The skill still appears in the decomposition table (it's in the spine) but gets 0 templates.

**Step C.3 — Check for sub-skill decomposition need.**
Some spine skills span broad cognitive territory. When a single spine skill covers multiple distinct cognitive operations that would produce fundamentally different template designs, decompose it into module-level sub-skills. Signs you need to decompose:

- The skill description uses "or" to join different operations (e.g., "answer comparison questions: how many more/fewer, how many in all")
- The EC tests the skill's sub-operations with different item types (e.g., EC.2 tests ordinal comparison, EC.3 tests difference calculation)
- Different sub-operations require different interaction types (e.g., click-to-select vs. MC with arithmetic distractors)
- Different sub-operations target different misconceptions
- Different sub-operations use different cognitive verbs (e.g., one is "compare," another is "apply")

When you decompose, use compound IDs: `SK6:ordinal`, `SK6:difference`, `SK6:combination`. The spine_skill_id in templates always references the parent spine skill (SK6); the sub-skill ID is a module-level annotation for template routing.

**Step C.4 — Check for skill additions.**
The spine may not capture every assessable action in this module. The Toy Flow or SP may reveal skills the spine missed. For each proposed addition:

- State the Toy Flow evidence (which interactions teach it, how many)
- State the EC evidence (is it tested?)
- Check if it folds into an existing spine skill's tier variant or distractor design
- If the skill has ≤1 teaching interaction AND no EC test → fold it, don't add it
- New skills are flagged as `[SPINE ADDITION PROPOSED]` with full justification

New skills flagged here get reviewed at the author gate and, if accepted, get added back to the spine for future modules.

**Step C.5 — §1.8.5 calibration (when SP available).**
If the SP has §1.8.5, compare your decomposition against its Skill Tracking table. Note:
- Skills in §1.8.5 that don't map to spine skills → check if the spine folded them (if so, note the fold; if not, flag as potential spine gap)
- Skills in the spine that §1.8.5 splits differently → note the divergence with rationale for your choice
- Distribution percentages from §1.8.5 → use as starting point for your Distribution Targets, then adjust based on spine progression data (INT skills get different weighting than EXT skills)

§1.8.5 is a **calibration check**, not the starting point. Significant divergence (2x the skills, different component balance) should be flagged with rationale.
```

---

## PATCH 3: Add spine_skill_id to Template Schema

**Where:** In the `### Template Schema (Teacher Review Format)` section, in the Technical Details code block (line ~151), add after `skill_id`:

**Replace:**
```
template_id: [MMXX — module digits + sequence]
template_type: [standard | misconception_remediation]
skill_id: [from Goal Decomposition — primary skill for tracking]
secondary_skill: [optional — for combined-skill templates, e.g., two-step problems]
```

**With:**
```
template_id: [MMXX — module digits + sequence]
template_type: [standard | misconception_remediation]
spine_skill_id: [from Unit Skill Spine — e.g., SK6. Always references the parent spine skill, even when sub-skill decomposition is used]
sub_skill: [module-level sub-skill annotation when applicable — e.g., SK6:difference. Omit if the spine skill maps 1:1 to this template's skill]
skill_id: [from Goal Decomposition — module-level skill ID for tracking, e.g., S4]
secondary_skill: [optional — for combined-skill templates, e.g., two-step problems]
```

**Also update** the Template Summary table format (Step 4, line ~630) to include spine_skill_id:

**Replace:**
```
#   │ ID   │ Type     │ Problem Type                  │ Verb     │ Tiers           │ Misc. Detected │ Problems
```

**With:**
```
#   │ ID   │ Type     │ Problem Type                  │ Spine Skill │ Sub-skill │ Verb     │ Tiers           │ Misc. Detected │ Problems
```

**And update** Skill Coverage in Coverage Validation (Step 5, line ~676) to group by spine skill:

**Replace:**
```
Skill ID │ Description (short)     │ Templates │ Tiers Covered    │ Status
─────────┼─────────────────────────┼───────────┼──────────────────┼────────
S1       │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
```

**With:**
```
Spine Skill │ Sub-skill     │ Description (short)     │ Templates │ Tiers Covered    │ Status
────────────┼───────────────┼─────────────────────────┼───────────┼──────────────────┼────────
SK1         │ —             │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
SK6         │ SK6:ordinal   │ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️
SK6         │ SK6:difference│ [desc]                  │ [IDs]     │ [tiers]          │ ✅ / ⚠️

Note: Coverage is assessed at BOTH the spine skill level (does every active spine skill have templates?)
and the sub-skill level (does every decomposed sub-skill have adequate tier coverage?).
```

---

## PATCH 4: Add Track Classification Step

**Where:** After Step 1E (Practice Phase Guidance, line ~456), before Step 1F (Dimension Budget):

**Insert:**

```
**F. Track Classification**

For every interaction pattern identified in the Toy Inventory (Step 1A), classify the RDR remediation track. This determines the remediation model for every template using that interaction.

| Interaction Pattern | RDR Track | Confidence | Notes |
|---|---|---|---|
| MC (4-option selection) | MC (RDR §3) | HIGH | Standard classification |
| Multi-select | MC (RDR §3) | HIGH | Treated as MC variant |
| Click-to-select (e.g., click tallest bar) | MC (RDR §3) | HIGH | Selection from visible options = MC |
| Drag-and-drop | Non-MC (RDR §2) | HIGH | Physical manipulation |
| Stepper (increment/decrement) | Non-MC (RDR §2) | HIGH | Construction tool |
| Equation builder (tile arrangement) | Non-MC (RDR §2) | HIGH | Construction tool |
| [Other module-specific patterns] | [classify] | [confidence] | [rationale] |

**Ambiguous cases** (e.g., drag items then MC confirm, or click-to-select from more than 6 options):
- Classify based on the PRIMARY interaction (what the student's cognitive effort is focused on)
- Mark confidence as MEDIUM
- Flag for author review at the gate

Track Classification becomes a column in the Template Summary (§PT.4). Every template's `remediation_track` must match the classification for its `action_description`.
```

**(Also renumber the existing Step 1F: Dimension Budget to Step 1G.)**

**And update the Template Summary table** (Step 4) to include Track:

**Replace:**
```
#   │ ID   │ Type     │ Problem Type                  │ Spine Skill │ Sub-skill │ Verb     │ Tiers           │ Misc. Detected │ Problems
```

**With:**
```
#   │ ID   │ Type     │ Problem Type                  │ Spine Skill │ Sub-skill │ Verb     │ Track  │ Tiers           │ Misc. Detected │ Problems
```

---

## PATCH 5: Source Readiness Check Updates

**Where:** In the `## SOURCE READINESS CHECK (Step 0)` section (line ~369), add after the existing checklist items:

**Add to the checklist (after the Toy Flow Completeness items):**

```
### Skill Spine Alignment
- [ ] Unit Skill Spine provided
- [ ] Cross-Module Matrix reviewed — skills active in this module identified
- [ ] Spine skill count for this module noted: [N] skills (INT: [n], PRC: [n], EXT: [n])
- [ ] Open Questions from spine reviewed — any affecting this module noted
```

**Add to the SP Enrichment checklist:**

```
- [ ] §1.8.5 Practice Phase Inputs present → **use as calibration check against spine-based decomposition** (not as authoritative skill list)
```

**Replace** the existing §1.8.5 checklist item:
```
- [ ] §1.8.5 Practice Phase Inputs present → **use for skill IDs, distribution targets, dimension budget**
```

**(Note the change: §1.8.5 is now calibration, not authority.)**

---

## PATCH 6: Output Format Updates

**Where:** In the Skill Decomposition output format (Step 2 artifact, line ~510):

**Replace:**
```
Skill ID │ Description                              │ Verb     │ Component   │ Source              │ Progression from M[N-1]
─────────┼──────────────────────────────────────────┼──────────┼─────────────┼─────────────────────┼─────────────────────────
S1       │ [description]                            │ create   │ procedural  │ [Lesson phase/EC]   │ [New / Extends / Builds on M[N-1] S[Y]]
```

**With:**
```
Spine ID │ Sub-skill       │ Mod. Skill │ Description                              │ Verb     │ Component   │ Source              │ Progression       │ Practice Scope
─────────┼─────────────────┼────────────┼──────────────────────────────────────────┼──────────┼─────────────┼─────────────────────┼───────────────────┼───────────────
SK1      │ —               │ S1         │ [description]                            │ identify │ conceptual  │ [Lesson phase/EC]   │ INT (from spine)  │ ✅ Practice-eligible
SK3      │ —               │ —          │ [description]                            │ create   │ procedural  │ [Warm-up only]      │ INT (from spine)  │ ❌ Teaching only
SK6      │ SK6:ordinal     │ S3         │ [description]                            │ compare  │ conceptual  │ [Lesson 1.1, 2.2a]  │ INT (from spine)  │ ✅ Practice-eligible
SK6      │ SK6:difference  │ S4         │ [description]                            │ compare  │ conceptual  │ [Lesson 3.1, 3.2]   │ INT (from spine)  │ ✅ Practice-eligible
SK6      │ SK6:combination │ S5         │ [description]                            │ apply    │ transfer    │ [Lesson 3.3]        │ INT (from spine)  │ ✅ Practice-eligible
—        │ —               │ S6         │ [SPINE ADDITION PROPOSED: description]    │ [verb]   │ [comp]      │ [evidence]          │ NEW               │ [TBD — needs gate review]
```

**Add after the table:**
```
SPINE ALIGNMENT NOTES
─────────────────────────────────────────────────────────────
Spine skills active in this module: [N]
  - Practice-eligible: [n]
  - Teaching only: [n]
Sub-skills decomposed: [list, with rationale for each]
Spine additions proposed: [count] — [list with evidence]
§1.8.5 delta (if SP provided): [divergences noted]
```

---

## PATCH 7: Anti-Patterns Addition

**Where:** At the end of the `## ANTI-PATTERNS` section (line ~833):

**Add:**

```
❌ **Don't ignore the Skill Spine.** Your decomposition starts from the spine's Cross-Module Matrix for this module, not from a blank-slate Toy Flow analysis. If you think a spine skill should be split, decompose it into sub-skills with compound IDs. If you think a skill is missing, propose it with evidence and flag it.

❌ **Don't create separate skills for every tier variant.** "Read picture graph at scale 2" and "Read picture graph at scale 5" are tier variants of SK1, not separate skills. The tier system handles parameter variation — skills handle cognitive variation.

❌ **Don't treat §1.8.5 as the authoritative skill list.** The spine is the baseline. §1.8.5 is calibration. If they disagree, document the delta and explain your choice.

❌ **Don't decompose a spine skill without evidence of distinct cognitive operations.** Sub-skill decomposition requires at least two of: different verb, different interaction type, different EC item, different misconception target. "It would be easier to template" is not sufficient justification by itself — though it's a supporting signal.
```

---

## WHAT THESE PATCHES DON'T CHANGE

The following v1 sections are carried forward without modification:

- **ROLE** — Same role description
- **WHAT YOU KNOW (Reference Knowledge)** — Character, Tier System, Cognitive Verb Requirements, Template Schema (except spine_skill_id addition), all sub-block specs (Distractor Types, Remediation Design, Recommended Contexts, Proactive Scaffold Suggestions, Key Teaching Moment)
- **TIER DERIVATION FROM SCAFFOLDING PROGRESSION** — Same mapping logic
- **Step 3: Template Generation** — Same template design rules (all 12 rules)
- **Step 4: Template Summary** — Same structure (with spine_skill_id column added)
- **Step 5: Coverage Validation** — Same checks (with spine-grouped skill coverage)
- **Misconception Targeting** — Same two-path model (standard detection + dedicated remediation)
- **Output Format** — Same page structure (§PT.0 through §PT.5)

---

## OPEN ITEM: Notion Knowledge Graph Alignment

**Deferred pending Jon's description of the Notion skill database schema.**

If the knowledge graph has its own skill ID format, the `spine_skill_id` field should match it — or include a mapping field. This affects:
- Template schema (what ID format to use)
- Spine output format (does it need a Notion page ID column?)
- Sync workflow (how templates get pushed to Notion with correct skill relations)

This patch set uses the spine's native format (U1.SK1, U1.SK6:difference, etc.). If the Notion schema uses a different convention, add a mapping step or update the spine output format.
