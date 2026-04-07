# Notion Review Cycle — Test Checklist

## Manual (live Notion page — module 12 v4)

- [x] **No-op pull** — untouched page, diff vs stamped source = no differences
- [x] **False positive scene flag** — `remove` beat with no description no longer flagged (bug fixed)
- [x] **Options split bug** — legacy `, ` format with commas inside option text now guarded; `notion_flags.json` surfaces it with the raw Notion string
- [x] **notion_blocks.json backup** — raw Notion blocks saved alongside pull output

## Edit features (unit tests in `tests/test_notion_pull.py`)

- [ ] **Dialogue text edit** — reviewer changes 💬 text → `beat["text"]` updated
- [ ] **Prompt text edit** — reviewer changes ❔ text → `beat["text"]` updated
- [ ] **Scene description edit** — reviewer changes 🎬 text → `beat["params"]["description"]` updated, `notion_flag = "updated"`, flag in `notion_flags.json`
- [ ] **Scene no-description false positive** — fallback-rendered 🎬 text not treated as edit
- [ ] **New beat insertion** — `[new beat]` callout → suggested beat inserted before current position
- [ ] **Validator state dialogue edit** — 💬 inside toggle → `state["beats"]` dialogue updated
- [ ] **Extra step group** — callouts beyond JSON groups → suggested beats appended
- [ ] **Options JSON round-trip** — options with commas survive push/pull via JSON encoding
- [ ] **Section isolation** — edit in one section doesn't affect another

## Regression rule

After every lesson schema change, run a no-op pull on both reference pages and verify the diff is empty:

```
# Module 11 v31 — flat beats + _notion_block_id (latest format)
python cli/push_to_notion.py outputs/unit1/lesson_generator_dialogue_pass_module_11/v31/step_12_push/push.json --pull

# Module 12 v4 — steps format, no IDs (legacy format)
python cli/push_to_notion.py outputs/unit1/lesson_generator_dialogue_pass_module_12/v4/step_11_push/push.json --pull
```

## Still to test manually

- [ ] **Prompt options edit** — reviewer changes option text in Notion on a re-pushed (JSON format) page → options updated correctly in pull
- [ ] **Multiple sections edited** — edits across several sections in one pull
- [ ] **Re-push after pull** — push the pull output back, confirm Notion page updates cleanly
