# Future Plans & Ideas

Deferred decisions, improvements, and ideas to revisit as the project matures.

---

1. **Reusable validator branch content** — Validator states currently define steps inline (switch-case style). If the same branch content needs to be reused across multiple prompts or sections, a `goto` field referencing a named shared section by ID could serve this purpose. Defer until a concrete reuse case arises. *(lesson script schema)*

2. **Overly pedantic content validator** — The AI-based content validator in `steps/prompts/sequence_structurer.py` generates false positive errors for mathematically correct content, contradicting itself. Fix: update the validation prompt (lines 361–436) to clarify metadata handling, remove self-contradicting rules, and add an explicit note to not flag mathematically correct content. *(sequence_structurer.py, pipelines.json, rerun.py)*

3. **Validator refactoring** — The AI-based validation approach is prone to false positives. Consider moving deterministic checks (indices, mathematical correctness) to Python-based validation and reserving AI validation for semantic/pedagogical concerns only. *(validation system)*

4. **Multimodal prompting from Notion images** — If prompts need to reference images stored on Notion pages, use the local API approach: fetch page blocks via `notion-client`, extract signed image URLs from image blocks, download bytes, base64-encode, and inject as `image` content blocks in the Claude API call. Do not use Notion MCP for this — MCP surfaces URLs as text strings, not image data, so Claude cannot see the image. Note that Notion-hosted image URLs are signed and expire (~1 hour), so download promptly after fetching the page. *(notion_sync.py, multimodal pipeline)*

5. **Try tool calls/agentic behavior instead of API call chaining** — The current pipeline chains multiple sequential Claude API calls to build up outputs step by step. Consider using Claude's tool use / agentic capabilities instead, where a single orchestrating call can invoke tools (e.g., validators, formatters, structurers) as needed, reducing round-trips and giving Claude more context over the full pipeline. *(core/pipeline_executor.py, steps/)*

6. **Rework and clean starter pack template** — The starter pack template structure needs to be revisited and cleaned up for clarity and consistency, using the latest template doc as the reference.

7. **Add section metadata to lesson script schema** — Section-level metadata (e.g., phase name, purpose, interaction count) should be formally added to the schema. *(docs/references/lesson_script_schema_guide.md)*

8. **Restructure unit1 toy specs for pipeline ingestion** — Toy specs in `units/unit1/toy_specs/` are being replaced by per-toy `visuals.md` files. Once the new format is finalized, clean up the source docs: remove mode overloading, scope arrays.md to unit 1 only, clarify which "student actions" are actually array inputs vs response toy inputs. *(units/unit1/toy_specs/)*

9. **Split toy_specs.md + reusable tools as skills** — `units/unit1/toy_specs.md` is a single 64k-token file. Split into one file per toy (e.g. `toy_specs_picture_graph.md`). For reuse across both the pipeline and interactive Claude Code use, define tools in Python (`scripts/figma_tools.py`) and wrap them in a CLI entry point. Claude Code skills (`.claude/commands/`) call the CLI with `$ARGUMENTS`, so the same logic runs interactively (`/figma-scene find group builder`) and programmatically. Skills and Python tool_use cannot share definitions directly — the CLI wrapper is the bridge. Longer term, exposing tools as an MCP server would make them available natively in Claude Code without the wrapper.
