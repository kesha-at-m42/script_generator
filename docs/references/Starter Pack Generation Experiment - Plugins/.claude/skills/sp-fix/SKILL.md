# SP Fix — Apply Evaluation Findings to Starter Packs

You take evaluation findings from the Layer 1 checkers and Layer 2 agents and apply targeted fixes to a Starter Pack. This is the "action" skill — while `sp-quick-check` and `sp-gate-eval` diagnose problems, this skill resolves them.

---

## PRINCIPLES

1. **Fix mechanically where possible.** Structural issues (heading levels, section ordering, missing markers) have deterministic fixes. Apply them without ambiguity.

2. **Flag for human judgment where needed.** Content issues (voice tone, pedagogical choices, missing misconceptions) require decisions. Present options, don't auto-resolve.

3. **Preserve author intent.** When fixing structure, don't change content. When fixing formatting, don't change structure. Minimize blast radius.

4. **Track every change.** Maintain a change log so the author can review what was done and why.

5. **Verify after fixing.** Re-run the relevant checkers after applying fixes to confirm they resolve cleanly.

---

## STEP 1: GATHER FINDINGS

Get the evaluation findings to fix. Accept any of:
- Output from `sp-quick-check` (Layer 1 findings)
- Output from `sp-gate-eval` (Layer 1 + Layer 2 findings)
- Direct checker JSON output files
- The user pointing at specific finding IDs

If no findings are provided, run `sp-quick-check` first to generate them.

---

## STEP 2: TRIAGE FINDINGS INTO FIX CATEGORIES

Sort every finding into one of three categories:

### Category A: Auto-Fix (apply directly)

These are mechanical, deterministic fixes with no judgment required:

| Finding | Fix |
|---------|-----|
| **ST9** — Wrong H1 count | Convert extra H1s to H2, or add missing H1s |
| **ST10** — H4 headings present | Convert H4 → H3 (or bold inline label if it's a sub-sub-item) |
| **NC5** — Dash bullets instead of asterisk | Replace `- ` with `* ` (preserve checklists `- [ ]`) |
| **NC2** — Bold interaction header | Convert `**Interaction N:**` to `### Interaction N:` |
| **NC3** — KDD as numbered list | Convert `1. **KDD-N:**` to `### KDD-N:` |
| **NC4** — [Type A/B/C] in headers | Remove the `[Type X]` label |
| **NC6/NC7** — Old field names | Replace `Method:` → `Student Action:`, `Validation:` → `Correct Answer:` |
| **ST5** — Placeholder text `[TBD]` | Flag location — can't auto-fill, but highlight for author |
| **ST6** — Development tags | Remove `[Modeling]`, `[MODIFY]`, `[Vocab_Staging]`, `[Tool_Intro]` tags |
| **ST12** — Missing transition markers | Add `→ **SECTION X COMPLETE.**` at section boundaries |
| **NC9** — H4 headings (Notion) | Same as ST10 — convert to H3 or bold |
| **NC10** — Section at wrong heading level | Adjust heading level to H2 for §1.0–§1.10 |

### Category B: Semi-Auto (apply with confirmation)

These have a clear fix pattern but might need author validation:

| Finding | Fix | Why confirm? |
|---------|-----|-------------|
| **ST4** — Section out of order | Move section block to correct position | Large text moves risk losing context |
| **ST11** — §1.7 internal ordering | Reorder subsections per skeleton sequence | Need to verify interaction references still make sense after move |
| **VO3** — Superlative praise | Replace with warmer alternatives from Guide Voice doc | Context-dependent — "Excellent!" might be warranted in specific moments |
| **VO7** — Feeling assumptions | Rewrite to observable language | Requires understanding the pedagogical intent |
| **VO8** — Identity labels | Rewrite to behavior-based language | Need to preserve the encouragement function |
| **MM2** — Missing vocabulary term | Add term to §1.3 staging table | Need to determine staging position and informal bridge |

### Category C: Manual (present to author)

These require human judgment and can't be auto-resolved:

| Finding | Action |
|---------|--------|
| **MM1** — Learning goal drift | Show the Module Map verbatim vs SP current; author decides |
| **MM4** — Missing misconception | Present the misconception data; author writes prevention strategy |
| **MM5** — Missing TVP key beat | Show the key beat; author integrates into phase script |
| **L2 agent findings** — Pedagogical quality | Present finding + recommendation; author decides |
| **Voice eval findings** — Tone calibration | Present the Warmth Spectrum mapping; author adjusts |

---

## STEP 3: APPLY CATEGORY A FIXES

For each auto-fix finding:

1. Read the SP file
2. Locate the exact line(s) referenced in the finding
3. Apply the fix using the Edit tool
4. Log the change: `[finding_id] Line N: old → new`

### Fix Patterns

#### Heading Level Fixes (ST9, ST10, NC9, NC10)
```python
# H4 → H3
line = line.replace('#### ', '### ', 1)

# H1 → H2 (for non-title H1s)
line = line.replace('# ', '## ', 1)  # only the first occurrence

# H3 → H2 (for numbered sections wrongly at H3)
line = line.replace('### ', '## ', 1)
```

#### Bullet Style Fix (NC5)
```python
# Only for non-checklist dash bullets
if line.strip().startswith('- ') and not line.strip().startswith('- ['):
    line = line.replace('- ', '* ', 1)
```

#### Field Name Fixes (NC6, NC7)
```python
line = line.replace('**Method:**', '**Student Action:**')
line = line.replace('**Validation:**', '**Correct Answer:**')
line = line.replace('Detail Level:', '')  # remove entirely
```

#### Interaction Header Fix (NC2)
```python
# **Interaction 5: Title** → ### Interaction 5: Title
match = re.match(r'\*\*(Interaction\s+\d+.*?)\*\*', line)
if match:
    line = f'### {match.group(1)}'
```

#### KDD Format Fix (NC3)
```python
# 1. **KDD-3: Title** → ### KDD-3: Title
match = re.match(r'\d+\.\s+\*\*(KDD-\d+:.*?)\*\*', line)
if match:
    line = f'### {match.group(1)}'
```

#### Development Tag Removal (ST6)
```python
# Remove known dev tags: [Modeling], [MODIFY], [Vocab_Staging], [Tool_Intro]
for tag in ['[Modeling]', '[MODIFY]', '[Vocab_Staging]', '[Tool_Intro]']:
    line = line.replace(tag, '')
```

#### Section Transition Markers (ST12)
```
# Add at the end of each section, before the next ## heading:
→ **SECTION 1.X COMPLETE.**
```

---

## STEP 4: PRESENT CATEGORY B AND C FINDINGS

For Category B (semi-auto), present each finding with:
- The current text
- The proposed fix
- Ask: "Apply this fix? [y/n]"

For Category C (manual), present each finding with:
- The finding details
- The reference data (Module Map entry, TVP key beat, etc.)
- A recommended action
- "This needs your judgment — here's what I'd suggest..."

---

## STEP 5: VERIFY FIXES

After all fixes are applied:

1. Re-run the relevant Layer 1 checkers on the fixed file
2. Compare finding counts: before vs after
3. Present a **Fix Summary**:

```
SP Fix Summary: G3U2M3_Notion_Ready.md

Applied: 14 auto-fixes (Category A)
Confirmed: 3 semi-auto fixes (Category B)
Deferred: 2 manual items (Category C)

Before: 0 CRIT, 16 MAJ, 56 MIN = 72 total
After:  0 CRIT,  4 MAJ, 12 MIN = 16 total
Resolved: 56 findings (78%)

Remaining MAJOR findings:
• [ST11] §1.7 ordering — deferred (needs interaction reference check)
• [MM1] Learning goal drift — deferred (author judgment)
• ...
```

---

## STEP 6: SAVE AND REPORT

1. Save the fixed file (overwrite in place, or save as `_fixed` variant if the user prefers)
2. Present the fix summary
3. If fixing a Notion-synced SP, offer to push changes back using the Notion update tools

---

## BATCH MODE

When fixing multiple SPs, process them in order and track cumulative stats:

```
Batch Fix Summary: 6 modules processed

| Module | Before | After | Resolved | % |
|--------|--------|-------|----------|---|
| M1     | 22     | 8     | 14       | 64% |
| M2     | 18     | 5     | 13       | 72% |
| ...    |        |       |          |     |

Systemic fixes applied across all modules:
• H4 → H3 conversion: 34 instances
• Bullet style normalization: 89 instances
• Dev tag removal: 12 instances
```

---

## NOTION-NATIVE FIXES

When the SP lives in the 📖 Level Curriculum Documents database, **fix directly in Notion** instead of editing local files.

### Quick Fixes via `update_content`

For Category A fixes that map to clean search-and-replace, apply them directly on the Notion page:

```
notion-update-page:
  page_id: <module_page_id>
  command: update_content
  content_updates:
    - old_str: "# PHASE SPECIFICATIONS"
      new_str: "## PHASE SPECIFICATIONS"
    - old_str: "#### Module Configuration"
      new_str: "### Module Configuration"
    - old_str: "**Method:**"
      new_str: "**Student Action:**"
      replace_all_matches: true
    - old_str: "**Validation:**"
      new_str: "**Correct Answer:**"
      replace_all_matches: true
```

**Important**: You must `notion-fetch` the page first to get the exact text for `old_str` matching. Notion's internal markdown may differ slightly from what the local file has.

### Full Replacement via `replace_content`

For large structural changes (section reordering, extensive reformatting), use the full push flow:

1. Pull from Notion → local temp file
2. Apply all fixes locally (where you can verify with checkers)
3. Convert via `sp_notion_push.py --content-only`
4. Push back via `replace_content`

```
notion-update-page:
  page_id: <module_page_id>
  command: replace_content
  new_str: <fixed content from sp_notion_push.py>
```

### Post-Fix Comment

After applying fixes, post a summary comment on the Notion page:

```
notion-create-comment:
  page_id: <module_page_id>
  content: |
    🔧 **Auto-fixes applied — YYYY-MM-DD**

    14 fixes applied:
    • 1× H1→H2 (PHASE SPECIFICATIONS)
    • 5× H4→H3 (Module Config, Guardrails, etc.)
    • 397× dash→asterisk bullet normalization
    • 4× dev tag removal

    2 items deferred for author review:
    • [ST11] §1.7 ordering — Required/Forbidden Phrases placement
    • [MM1] Learning goal drift from Module Map

    Re-check: 0 CRITICAL, 2 MAJOR, 0 MINOR remaining
```

### Page ID Lookup

Reference the `sp-notion-sync` skill for the page ID table, or query:
```
notion-query-data-sources:
  data_source_urls: ["collection://3185917e-ac52-80c0-a46b-000be3c6a416"]
  query: SELECT url, "Name", "Module Number" FROM "collection://3185917e-ac52-80c0-a46b-000be3c6a416" WHERE "Module Number" = N
```

---

## SAFETY

- **Notion is the source of truth** — always fetch before editing to avoid overwriting others' changes
- **Never auto-fix Category C items** — these need human judgment
- **Never delete content** — only restructure, rename, or move
- **Preserve the `---` horizontal rules** between sections (they're Notion section markers)
- **Don't touch content inside interaction blocks** unless the finding specifically targets it
- **Watch for child pages** — `replace_content` will warn if it would delete child pages. Always preserve them
- When in doubt, use `update_content` (surgical edits) over `replace_content` (nuclear option)
