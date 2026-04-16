# Later Fixes & Future Plans

Deferred bugs, improvements, and ideas — understood, not urgent, worth doing when the need arises.

---

## Specific Bugs / Known Issues

### Pull: validator state paragraphs still emit as `unparsed` in some sections

Sections where no `current_scene` separates the prompt from the branch column_list (e.g. `s3_4_open_specification_build_given_total` in lesson m11) still produce two `unparsed` beats for the "✅ 🔀 … — student moves forward" paragraphs. The regex and `last_prompt_beat` logic are correct; the likely cause is that `column_list` children are not embedded in the block object when `_all_blocks` returns a flat list for that section layout. Investigate whether `column_list["column_list"]["children"]` is populated for those sections, and fix the `column_list` handler in `_patch_section_beats` accordingly.

**Location:** `utils/notion.py` — `_patch_section_beats`, `_section_blocks_map`, `_all_blocks`

---

### Pull: adding and removing branches from Notion

Currently the pull only reads branch content from existing `column_list` blocks; it cannot create a new branch or delete an existing one based on Notion edits. Adding a new column in Notion or removing one has no effect on the JSON. Support for branch creation/deletion would require detecting column count changes and mapping them to `branch_name` insertions or removals in the beat list.

**Location:** `utils/notion.py` — `_patch_section_beats` `column_list` handler

---

### spec_splitter: body overflow + false-positive validation errors

**Status:** WIP

**Location:** `steps/formatting/spec_splitter.py`, `steps/prompts/starterpack_parser.py`, `config/pipelines.json`

**Issue 1 — Body overflow on last section**
The `Bridge to Exit Check` section body runs to end-of-file, capturing trailing spec metadata (Required Phrases, Forbidden Phrases, Commutative Property Deflection Script) as spurious fields. Fix: in `spec_splitter.py`, treat any `##`/`###` header that does NOT match the interaction pattern as a body terminator.

**Issue 2 — False-positive validation errors**
Every batch item gets a `validation_errors.json` entry. Two causes:
- `batch_id_field = "index"` → validator fires because input has `index` but output doesn't. Fix: add `"batch_output_id_field": "id"` to the `starterpack_parser` step in `pipelines.json`.
- `output_structure` example shows section 1.1 fields (`guide_2`, `vocabulary`, etc.) → validator treats them as required for all sections. Fix: simplify `output_structure` to `{"id": "..."}` only; move full example into `instructions`.

---

### Interactive walkthrough test: open items from last run

**Status:** In progress — `tests/test_notion_interactive.py`. Journeys 1–4 passed. Journey 5 partially passed. Journey 6 failed.

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

4. **Multimodal prompting from Notion images** — If prompts need to reference images stored on Notion pages, use the local API approach: fetch page blocks via `notion-client`, extract signed image URLs from image blocks, download bytes, base64-encode, and inject as `image` content blocks in the Claude API call. Do not use Notion MCP for this — MCP surfaces URLs as text strings, not image data, so Claude cannot see the image. Note that Notion-hosted image URLs are signed and expire (~1 hour), so download promptly after fetching the page. *(notion.py, multimodal pipeline)*

5. **Try tool calls/agentic behavior instead of API call chaining** — The current pipeline chains multiple sequential Claude API calls to build up outputs step by step. Consider using Claude's tool use / agentic capabilities instead, where a single orchestrating call can invoke tools (e.g., validators, formatters, structurers) as needed, reducing round-trips and giving Claude more context over the full pipeline. *(core/pipeline_executor.py, steps/)*

6. **Rework and clean starter pack template** — The starter pack template structure needs to be revisited and cleaned up for clarity and consistency, using the latest template doc as the reference.

7. **Add section metadata to lesson script schema** — Section-level metadata (e.g., phase name, purpose, interaction count) should be formally added to the schema. *(docs/references/lesson_script_schema_guide.md)*

8. **Restructure unit1 toy specs for pipeline ingestion** — Toy specs in `units/unit1/toy_specs/` are being replaced by per-toy `visuals.md` files. Once the new format is finalized, clean up the source docs: remove mode overloading, scope arrays.md to unit 1 only, clarify which "student actions" are actually array inputs vs response toy inputs. *(units/unit1/toy_specs/)*

9. **Split toy_specs.md + reusable tools as skills** — `units/unit1/toy_specs.md` is a single 64k-token file. Split into one file per toy (e.g. `toy_specs_picture_graph.md`). For reuse across both the pipeline and interactive Claude Code use, define tools in Python (`scripts/figma_tools.py`) and wrap them in a CLI entry point. Claude Code skills (`.claude/commands/`) call the CLI with `$ARGUMENTS`, so the same logic runs interactively (`/figma-scene find group builder`) and programmatically. Skills and Python tool_use cannot share definitions directly — the CLI wrapper is the bridge. Longer term, exposing tools as an MCP server would make them available natively in Claude Code without the wrapper.

10. **Reverse-assign `_notion_block_id` to early pipeline steps** — After a pull, `_notion_block_id` is only stamped onto the final merged step output. If the pipeline is re-run from an earlier step, those IDs are dropped and surgical sync falls back to full-replace. Fix: after a pull, walk backwards through the version's pipeline steps and propagate `_notion_block_id` onto the matching beat (by beat ID) in each earlier step's output file. Section heading block IDs should be stamped onto the section structurer output. This way, any rerun that starts from an intermediate step inherits the IDs automatically. *(cli/push_to_notion.py `_pull()`, utils/notion.py `pull_lesson()`)*

11. **Item ID glob matching in rerun** — Support glob-style item ID patterns (e.g. `s2_4*`) in `cli/rerun.py` so a single pattern targets all items whose ID starts with a given prefix. Section IDs are intended to be unique across a module — enforce/validate this to make glob matching unambiguous. *(cli/rerun.py, pipeline ID uniqueness validation)*

12. **Consolidate Notion management flags** — `--test-push` exists in `cli/run_pipeline.py` and `cli/push_to_notion.py` but not in `cli/rerun.py`. When the CLI entry points are merged (see item 13), Notion flags (`--test-push`, `--no-push`) should be unified in one place. Also consider whether `push_to_notion.py` should be folded into the main CLI or kept as a standalone utility. *(cli/run_pipeline.py, cli/rerun.py, cli/push_to_notion.py, steps/formatting/notion_push.py)*

13. **Consolidate `run_pipeline.py` and `rerun.py`** — Two separate CLI entry points with overlapping responsibilities: `cli/run_pipeline.py` runs a full pipeline from scratch; `cli/rerun.py` reruns specific items or step ranges from an existing run. These should be merged into a single CLI (e.g. `cli/run_pipeline.py`) where rerun behaviour is triggered by flags (`--start-from`, `--end-at`, item IDs). `rerun_multiselect.py` should be evaluated at the same time — fold it in or remove it. *(cli/run_pipeline.py, cli/rerun.py, cli/rerun_multiselect.py)*

14. **Section ID schema: numeric IDs starting from 100 with separate name field** — Section IDs currently embed both identity and a slug (e.g. `s1_1_most_votes`). Plan: switch to numeric IDs starting at 100 (e.g. `s1_100`, `s1_101`) and add a separate `name` field for the human-readable slug. This decouples identity from naming, making IDs stable when names change. Touches: section structurer output, all downstream pipeline steps, Notion push/pull, `_section_sort_key`, and any regex parsing of section IDs. *(schema-wide change)*

15. **Step design style guide and better examples for section_structurer** — The flat `beats` array with ⏭️ step-break toggles is the right schema (explicit step nesting is ruled out due to Notion nesting constraints). What's missing: a proper style guide for how a step should be designed — what belongs in one step vs. split across two, cognitive load guidelines, worked examples of good and bad step pacing, branching step patterns, transition vs. instructional step differences. Add this as a dedicated reference doc and tighten the examples in `section_structurer.py`. *(steps/prompts/section_structurer.py, docs/)*

---

## `--skip-batch-ids` with base-version merging

**Files:** `core/pipeline.py`, `core/batch_processor.py`, `cli/rerun.py`, `cli/run_pipeline.py`

**Problem:** There's no way to run a partial batch rerun (some items) while automatically
preserving other items' outputs from a prior version. Three root causes:

1. `base_step_dir` in `pipeline.py` is only set when `rerun_items` is non-None (~line 793).
   A pure step-range rerun (`--start-from N` with no item IDs) gets no base merging at all.

2. `BatchProcessor.should_skip_item()` silently drops `batch_skip_items` entries — it never
   tries to load them from `base_version_dir`, unlike the `batch_only_items` path which does.

3. `--skip-batch-ids` in `run_pipeline.py` is dead code — parsed but never forwarded to
   `run_pipeline_from_config`.

4. `rerun.py` has no `--skip-batch-ids` flag at all.

**Fix:**

Add `global_batch_skip_items: List[str] = None` to `run_pipeline()`. When set:

- Extend the condition that populates `base_step_dir`:
  ```python
  # pipeline.py ~line 793
  if base_version and (rerun_items or global_batch_skip_items):
      base_step_dir = get_step_directory(...)
  ```

- Merge into batch skip list when building `BatchProcessor`:
  ```python
  _batch_skip = list(step.batch_skip_items or [])
  if global_batch_skip_items:
      _batch_skip = list(set(_batch_skip + global_batch_skip_items))
  BatchProcessor(..., batch_skip_items=_batch_skip, ...)
  ```

- In `batch_processor.py` `should_skip_item()`, load from base when skipping:
  ```python
  if self.batch_skip_items:
      is_skipped = item_id in self.batch_skip_items or base_id in self.batch_skip_items
      if is_skipped:
          if self.base_version_dir:
              copied = self._load_from_base(item, item_id, base_id)
              if copied:
                  self.add_result(copied, preserve_id=True)
                  return True, "copied from base (skip)"
          return True, "in skip_items"
  ```

- Add `--skip-batch-ids` to `rerun.py`, pass as `global_batch_skip_items` to `run_pipeline`.

- Fix dead code in `run_pipeline.py`: pass `batch_skip_items` as `global_batch_skip_items`
  to `run_pipeline_from_config`.

**Resulting workflow** (e.g. dialogue_pass module 1 where only s3_5/s3_6/s3_7 have been run):
```
python cli/rerun.py lesson_generator_dialogue_pass --module 1 \
  --start-from 5 --base v10 \
  --skip-batch-ids s3_5_what_information_needed,s3_6_solving_with_selected_data,s3_7_two_step_sequential
```
Runs the 17 missing sections through all batch AI steps; loads the 3 already-done sections
from v10's collated outputs at each batch step.

**One-off workaround (no code changes needed):** Use `fixes/stitch_pipeline_outputs.py` to
create a composite stub version pre-seeded with existing batch outputs, then use `--batch-ids`
(not `--skip-batch-ids`) with the list of missing IDs. The existing `batch_only_items` +
`base_version_dir` merge path handles it correctly.
