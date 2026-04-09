# Later Fixes & Future Plans

Deferred bugs, improvements, and ideas — understood, not urgent, worth doing when the need arises.

---

## Specific Bugs / Known Issues

### spec_splitter: body overflow + false-positive validation errors

**Status:** Pipeline working correctly (all 16 sections parsed, s3_2 present). Two cosmetic issues to clean up.

**Location:** `steps/formatting/spec_splitter.py`, `steps/prompts/starterpack_parser.py`, `config/pipelines.json`

**Issue 1 — Body overflow on last section**
The `Bridge to Exit Check` section body runs to end-of-file, capturing trailing spec metadata (Required Phrases, Forbidden Phrases, Commutative Property Deflection Script) as spurious fields. Fix: in `spec_splitter.py`, treat any `##`/`###` header that does NOT match the interaction pattern as a body terminator.

**Issue 2 — False-positive validation errors**
Every batch item gets a `validation_errors.json` entry. Two causes:
- `batch_id_field = "index"` → validator fires because input has `index` but output doesn't. Fix: add `"batch_output_id_field": "id"` to the `starterpack_parser` step in `pipelines.json`.
- `output_structure` example shows section 1.1 fields (`guide_2`, `vocabulary`, etc.) → validator treats them as required for all sections. Fix: simplify `output_structure` to `{"id": "..."}` only; move full example into `instructions`.

---

### Notion sync: ID-based structural sync in `_smart_sync_children`

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

---

### Interactive walkthrough test: open items from last run

**Status:** `tests/test_notion_interactive.py` — Journeys 1–4 passed. Journey 5 partially passed. Journey 6 failed.

#### Journey 5 — Pull gaps

The pull ran after user edits in Notion. Only the s1_1 dialogue edit was captured. The s1_1 scene description edit (should have flagged `scene_description_updated`) and the s1_3 prompt text edit were not reflected in the pull output.

**Possible causes:**
- Notion API propagation delay: edits weren't flushed to API yet when the pull ran
- User edited the wrong callout (e.g. wrong section or non-editable block)
- The scene description comparison in `_scene_rendered_text` returned the edited text as a false-positive match (unlikely, but worth verifying)

**To investigate:** Re-run Journey 5 alone; add explicit assertion for all 3 edits; add a short wait after pressing Enter before pulling.

#### Journey 6 — `[new beat]` detection failed (0 suggested beats)

The test instructs the user to add a `[new beat] Let's take a moment to reflect.` callout with emoji 💬 inside the s1_3 toggle in Notion. The pull returned 0 suggested beats.

**Most likely cause:** The callout was added at the page level (outside the s1_3 toggle) rather than as a child of the heading toggle. `_section_callouts_from_blocks` only reads `heading_2.children`, so page-level callouts are invisible to the pull.

**Secondary cause:** The callout emoji wasn't set to 💬 (Notion default is something else; user needs to explicitly pick 💬).

**Workaround for next run:** Instruct the user more explicitly — expand the toggle first, click inside it, then add the callout. Add a reminder that the emoji must be 💬.

**Code fix to consider:** Add a note in the test instructions print to clarify placement. No code bug confirmed yet.

#### J4 double-divider visual

Each section renders as `[divider][heading]`. Inserting s1_2b between s1_2 and s1_3 gives two visible dividers in that gap. Cosmetic only — could be fixed by moving dividers to be "between" sections rather than "before" each one, but requires a renderer change.

---

## Future Plans & Ideas

1. **Reusable validator branch content** — Validator states currently define steps inline (switch-case style). If the same branch content needs to be reused across multiple prompts or sections, a `goto` field referencing a named shared section by ID could serve this purpose. Defer until a concrete reuse case arises. *(lesson script schema)*

2. **Overly pedantic content validator** — The AI-based content validator in `steps/prompts/sequence_structurer.py` generates false positive errors for mathematically correct content, contradicting itself. Fix: update the validation prompt (lines 361–436) to clarify metadata handling, remove self-contradicting rules, and add an explicit note to not flag mathematically correct content. *(sequence_structurer.py, pipelines.json, rerun.py)*

3. **Validator refactoring** — The AI-based validation approach is prone to false positives. Consider moving deterministic checks (indices, mathematical correctness) to Python-based validation and reserving AI validation for semantic/pedagogical concerns only. *(validation system)*

4. **Multimodal prompting from Notion images** — If prompts need to reference images stored on Notion pages, use the local API approach: fetch page blocks via `notion-client`, extract signed image URLs from image blocks, download bytes, base64-encode, and inject as `image` content blocks in the Claude API call. Do not use Notion MCP for this — MCP surfaces URLs as text strings, not image data, so Claude cannot see the image. Note that Notion-hosted image URLs are signed and expire (~1 hour), so download promptly after fetching the page. *(notion_sync.py, multimodal pipeline)*

5. **Try tool calls/agentic behavior instead of API call chaining** — The current pipeline chains multiple sequential Claude API calls to build up outputs step by step. Consider using Claude's tool use / agentic capabilities instead, where a single orchestrating call can invoke tools (e.g., validators, formatters, structurers) as needed, reducing round-trips and giving Claude more context over the full pipeline. *(core/pipeline_executor.py, steps/)*

6. **Rework and clean starter pack template** — The starter pack template structure needs to be revisited and cleaned up for clarity and consistency, using the latest template doc as the reference.

7. **Add section metadata to lesson script schema** — Section-level metadata (e.g., phase name, purpose, interaction count) should be formally added to the schema. *(docs/references/lesson_script_schema_guide.md)*

8. **Restructure unit1 toy specs for pipeline ingestion** — Toy specs in `units/unit1/toy_specs/` are being replaced by per-toy `visuals.md` files. Once the new format is finalized, clean up the source docs: remove mode overloading, scope arrays.md to unit 1 only, clarify which "student actions" are actually array inputs vs response toy inputs. *(units/unit1/toy_specs/)*

9. **Split toy_specs.md + reusable tools as skills** — `units/unit1/toy_specs.md` is a single 64k-token file. Split into one file per toy (e.g. `toy_specs_picture_graph.md`). For reuse across both the pipeline and interactive Claude Code use, define tools in Python (`scripts/figma_tools.py`) and wrap them in a CLI entry point. Claude Code skills (`.claude/commands/`) call the CLI with `$ARGUMENTS`, so the same logic runs interactively (`/figma-scene find group builder`) and programmatically. Skills and Python tool_use cannot share definitions directly — the CLI wrapper is the bridge. Longer term, exposing tools as an MCP server would make them available natively in Claude Code without the wrapper.

10. **Branching prompts — full pipeline support** — When a choice prompt leads to different follow-up interactions (e.g. student picks Rows vs Columns, then fills a branch-specific equation), the current schema collapses both paths into a single `condition: {}` validator, losing branch specificity. The solution designed so far:
    - **Spec authoring**: parenthetical context in Notion property names (e.g. `**Correct Answer (if rows):**`) is the branch signal. `starterpack_parser` now extracts `(if X)` into distinct keys (`correct_answer_if_rows`, `on_correct_if_columns`) rather than stripping them.
    - **section_structurer**: fields with parenthetical keys → one validator state per branch using `branch_condition` instead of `condition`. Both states are `is_correct: true`. For follow-up prompts, states carry both `branch_condition` and `condition` (multi-part).
    - **Individual beats**: branch-specific beats in the outer beats array get a `branch_condition` field (omitted when unconditional).
    - **Notion rendering**: validator states and beats with `branch_condition` render with a `🔀 <condition> —` prefix. Test page: https://notion.so/33b5917eac52816694afe40bb3f69306
    - **Still needed**: remediation generator support — skip pure-choice validators (all states have `branch_condition`, no wrong answer), and generate branch-tagged L/M/H incorrect states for branched answer prompts. *(starterpack_parser.py, section_structurer.py, lesson_notion_format.py, remediation_generator.py)*

12. **Item ID glob matching in rerun** — Support glob-style item ID patterns (e.g. `s2_4*`) in `cli/rerun.py` so a single pattern targets all items whose ID starts with a given prefix. Section IDs are intended to be unique across a module — enforce/validate this to make glob matching unambiguous. *(cli/rerun.py, pipeline ID uniqueness validation)*

13. **Consolidate Notion management flags** — `--test-push` exists in `cli/run_pipeline.py` and `cli/push_to_notion.py` but not in `cli/rerun.py`. When the CLI entry points are merged (see item 11), Notion flags (`--test-push`, `--no-push`) should be unified in one place. Also consider whether `push_to_notion.py` should be folded into the main CLI or kept as a standalone utility. *(cli/run_pipeline.py, cli/rerun.py, cli/push_to_notion.py, steps/formatting/notion_push.py)*

11. **Consolidate `run_pipeline.py` and `rerun.py`** — Two separate CLI entry points with overlapping responsibilities: `cli/run_pipeline.py` runs a full pipeline from scratch; `cli/rerun.py` reruns specific items or step ranges from an existing run. These should be merged into a single CLI (e.g. `cli/run_pipeline.py`) where rerun behaviour is triggered by flags (`--start-from`, `--end-at`, item IDs). `rerun_multiselect.py` should be evaluated at the same time — fold it in or remove it. *(cli/run_pipeline.py, cli/rerun.py, cli/rerun_multiselect.py)*
