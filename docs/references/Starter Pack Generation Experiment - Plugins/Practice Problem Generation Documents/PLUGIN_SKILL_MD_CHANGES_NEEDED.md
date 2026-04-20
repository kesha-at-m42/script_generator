# Plugin SKILL.md Changes Needed — Global Skill ID Migration

**Created:** 2026-04-16
**Context:** The practice pipeline migrated from unit-scoped numeric skill IDs (`U1.SK1`, `spine_skill_id`) to global descriptive CamelCase IDs (`ReadPicGraph`, `skill_id`). The actual generation prompts have been updated, but the plugin orchestration SKILL.md files are read-only and still reference the old format.

**Impact:** LOW — the SKILL.md files provide process guidance, but the actual prompts (`practice_template_prompt_v1.1.md` and `stage_0_skill_spine_prompt.md`) define the output format and have already been updated. Generated output will use the new format regardless of SKILL.md wording.

---

## pt-gen/SKILL.md

### Line 128 — Sub-skill decomposition example
**Old:** `SK6:ordinal`, `SK6:difference`
**New:** `CompareData:ordinal`, `CompareData:difference`

### Line 144 — Template schema description
**Old:**
```
Every template includes `spine_skill_id` (parent spine skill, matching Notion 🧬 Skill Spine database format: `U[unit].SK[number]`) and `sub_skill` (module-level annotation, omit if 1:1 mapping).
```
**New:**
```
Every template includes `skill_id` (global descriptive CamelCase name matching Notion 🧬 Skill Spine database "Skill ID" property, e.g., `CompareData`) and `sub_skill` (Parent:qualifier notation when applicable, e.g., `CompareData:difference`. Sub-skills have their own rows in the Notion Skill Spine database. Omit if 1:1 mapping).
```

---

## pt-spine/SKILL.md

### Lines 236-240 — Concept-to-Skill Alignment example
**Old:** `U[X].SK[N] — [skill name]`
**New:** `[SkillName] — [skill description]` (CamelCase global IDs)

### Line 246 — Skill Thread header example
**Old:** `U[X].SK1 — [Skill name: verb + object + qualifier]`
**New:** `[SkillName] — [Skill name: verb + object + qualifier]`

### Line 254 — Transforms reference
**Old:** `M[N] → U[X].SK[Y]`
**New:** `M[N] → [SkillName]`

### Line 261 — Second skill thread example
**Old:** `U[X].SK2 — [Skill name]`
**New:** `[AnotherSkill] — [Skill name]`

### Lines 269-270 — Cross-Module Matrix examples
**Old:** `U[X].SK1`, `U[X].SK2`
**New:** `[SkillName]` (e.g., `ReadPicGraph`, `ReadBarGraph`)

### Line 304 — Misconception Coverage table
**Old:** `U[X].SK[N]`
**New:** `[SkillName]`

---

---

## pt-gen/SKILL.md — Representations Field

### Template schema description (near Line 144)
**Add:** Mention of `representation` as an optional template field for skills with multiple toy types. This field was added to `practice_template_prompt_v1.1.md` but the plugin SKILL.md doesn't reference it yet.

---

## pt-spine/SKILL.md — Representations Field

### Skill thread output template (near where the output format is described)
**Add:** `Representations:` as a standard field in the skill thread output block, between `Primary Verb` and `Thread Type`. This was added to `stage_0_skill_spine_prompt.md` but the plugin SKILL.md doesn't reference it yet.

---

## How to Apply

These changes need to be applied via the plugin update mechanism (editing the plugin source and republishing). The changes are cosmetic — they align the orchestration guidance with the already-updated prompt files and Notion database.

Priority: LOW — apply at next plugin version bump.
