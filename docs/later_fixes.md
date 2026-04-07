# Later Fixes

Items deferred during development — understood, not urgent, worth doing when the need arises.

---

## spec_splitter: body overflow + false-positive validation errors

**Status:** Pipeline working correctly (all 16 sections parsed, s3_2 present). Two cosmetic issues to clean up.

**Location:** `steps/formatting/spec_splitter.py`, `steps/prompts/starterpack_parser.py`, `config/pipelines.json`

**Issue 1 — Body overflow on last section**
The `Bridge to Exit Check` section body runs to end-of-file, capturing trailing spec metadata (Required Phrases, Forbidden Phrases, Commutative Property Deflection Script) as spurious fields. Fix: in `spec_splitter.py`, treat any `##`/`###` header that does NOT match the interaction pattern as a body terminator.

**Issue 2 — False-positive validation errors**
Every batch item gets a `validation_errors.json` entry. Two causes:
- `batch_id_field = "index"` → validator fires because input has `index` but output doesn't. Fix: add `"batch_output_id_field": "id"` to the `starterpack_parser` step in `pipelines.json`.
- `output_structure` example shows section 1.1 fields (`guide_2`, `vocabulary`, etc.) → validator treats them as required for all sections. Fix: simplify `output_structure` to `{"id": "..."}` only; move full example into `instructions`.

---

## Notion sync: ID-based structural sync in `_smart_sync_children`

**Location:** `utils/notion_sync.py:_smart_sync_children`

**Current behaviour:** When a section's beat structure changes (beat added, removed, or reordered), the entire section falls back to `_refresh_children` — all children archived and recreated. Comments on beats within that section are lost.

**Why it's fixable:** Beats that have been pushed before carry `_notion_block_id` — the Notion block UUID of their rendered callout. `existing` blocks in `_smart_sync_children` also have `id`. So we already have a stable mapping between beats and blocks.

**How to fix:**
1. In `lesson_to_blocks` renderers (`_render_dialogue`, `_render_scene`, `_render_prompt`), embed `beat["_notion_block_id"]` onto the rendered block dict if present.
2. In `_smart_sync_children`, when new blocks carry `_notion_block_id`, match against existing blocks by ID rather than by position:
   - Matched by ID → update in place (preserves comments)
   - New block (no ID or ID not found) → insert at correct position
   - Existing block not matched by any new block → archive
3. Strip `_notion_block_id` before any Notion API call.
4. Fall back to current skeleton logic when IDs are absent (first push, or beats without tag-back).

**Benefit:** Comments survive re-push even when beats are added or removed from a section.

**Implementation plan:** `C:\Users\kesha\.claude\plans\delightful-wibbling-sutherland.md` — full step-by-step with exact code for `_strip_meta`, the updated `_smart_sync_children`, embedding `_notion_block_id` in `_render_beat`, and a new live test.
