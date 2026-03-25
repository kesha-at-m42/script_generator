# Pipeline & Schema Design Reference

**Last Updated:** March 2026
**Purpose:** Key design considerations and decisions behind the script_generator pipeline system and data schema

---

## TABLE OF CONTENTS

**SECTION 1** — Pipeline Architecture
**SECTION 2** — Step Model
**SECTION 3** — Batch Processing
**SECTION 4** — Schema & Validation
**SECTION 5** — Prompt Construction & Caching
**SECTION 6** — File I/O & Versioning
**SECTION 7** — Rerun & Partial Rerun
**SECTION 8** — Cross-Cutting Decisions

---

## SECTION 1: Pipeline Architecture

### 1.1 Declarative vs. Imperative Definition

Pipelines are defined declaratively in `config/pipelines.json` rather than as Python code. Each pipeline is a named array of step configs; each step declares its type, inputs, outputs, and parameters.

**Why declarative?**
- Steps can be inspected, reordered, or replaced without touching Python.
- Non-engineers can read the pipeline definition.
- The executor (`core/pipeline.py`) is generic — it doesn't know or care what a lesson is.

**Tradeoff:** Dynamic logic (branching, conditional steps) can't live in the JSON. It is pushed to formatting steps that return control signals (see Section 3.3).

### 1.2 Two Step Types: `ai` vs. `formatting`

Every step is one of two types:

| Type | What it does | Entry point |
|------|-------------|-------------|
| `ai` | Calls Claude, validates output, retries | `core/pipeline.py` → `run_single_step()` |
| `formatting` | Runs a deterministic Python function | `core/pipeline_executor.py` → `execute_formatting_step()` |

**Why this split?**
- Keeps AI calls isolated and retryable without complicating pure-transform logic.
- Formatting steps are cheap, fast, and fully testable without API calls.
- The boundary is explicit: if a step mutates data without calling Claude, it is a formatting step.

### 1.3 Auto-Chaining Between Steps

If a step's `input_file` is omitted, the pipeline automatically feeds the previous step's output as input.

**Why auto-chain?**
- Eliminates repetitive path declarations for sequential pipelines.
- Makes reruns cleaner: when starting mid-pipeline, the executor loads the equivalent step output from the base version rather than requiring an explicit path.

Explicit `input_file` is reserved for steps that pull from a fixed source (e.g., a shared template or module definition) rather than the preceding step.

---

## SECTION 2: Step Model

### 2.1 Mutually Exclusive Step Kinds

A `Step` object carries either `prompt_name` (AI) or `function` (formatting), never both. This is enforced at construction time (`core/pipeline.py:197-203`).

**Why enforce at construction?** Mixing the two kinds would make the execution path ambiguous and validation logic undefined.

### 2.2 Parameter Injection for Formatting Steps

Formatting step functions are called via `inspect.signature()` — the executor detects which of the standard parameters (`module_number`, `path_letter`, `unit_number`, `verbose`, `output_file_path`) the function accepts and injects only those.

**Why reflection-based injection?**
- Functions can declare exactly what they need with no boilerplate glue code.
- Adding a new context variable to the executor doesn't break existing functions.
- Keeps formatting step signatures minimal and self-documenting.

### 2.3 Batch Configuration Override via Formatting Step Output

A formatting step can return a dict containing `batch_only_items` or `batch_skip_items`. If these keys are present, the executor uses them to override the *next* step's batch configuration.

**Why?** This lets a step like `remediation_filter` decide at runtime which items need processing, without requiring the pipeline author to hardcode item IDs in `pipelines.json`. The formatting step is the correct place for this logic because it is deterministic and cheap.

The actual data the next step should process lives in an optional `data` field in the same dict.

---

## SECTION 3: Batch Processing

### 3.1 Item-Level vs. Step-Level Granularity

In batch mode, each item is written to its own file under `items/` before collation into the step's final output. This means:
- A crash mid-batch preserves all completed items.
- Resume (`batch_skip_existing`) works by checking for the presence of the per-item file.
- IDs are assigned sequentially at collation time, not generation time.

### 3.2 Sequential ID Assignment at Collation

Output IDs (`batch_output_id_field`) are assigned by the `BatchProcessor` when results are added, not by Claude. This guarantees:
- IDs are always sequential and gapless in the collated output.
- Claude never needs to know or infer IDs.
- Reruns that skip items (via `batch_skip_existing`) can still produce correct IDs by advancing the counter past items loaded from the base version.

### 3.3 Base Version Inheritance for Reruns

When rerunning a subset of items, unchanged items are loaded from the base version and re-included in the collated output. Their IDs are "reserved" before new items are added, so the final ID sequence remains stable.

**Why preserve IDs across reruns?** Downstream steps, Notion pages, and other systems may reference items by ID. Reordering IDs when only a few items changed would invalidate those references.

---

## SECTION 4: Schema & Validation

### 4.1 Schema Inferred from Output Example

There is no separate schema file. The expected output structure is inferred at runtime from the `output_structure` block in each prompt's JSON — specifically, the example JSON provided there. `parse_schema_from_example()` (`core/output_validator.py:19-75`) extracts:
- Whether the output is an array or object.
- Required top-level fields and their types.

**Why infer rather than declare?**
- Schema stays co-located with the prompt that produces the output.
- No separate schema file to keep in sync.
- Tradeoff: schema inference is shallow (top-level only); deep structural validation is handled by domain-specific validators.

### 4.2 Two-Phase Validation: Structural then Content

Every AI step runs validation in two phases:
1. **Structural** (`validate_ai_output_structure`) — checks shape, required fields, types, ID inheritance.
2. **Content** (optional, via `validation_prompt`) — a second Claude call that scores quality and flags specific issues.

Structural validation always runs. Content validation is opt-in per prompt.

**Why separate phases?**
- Structural errors are cheap to catch and almost always indicate a malformed response worth retrying immediately.
- Content validation is expensive (another Claude call) and only useful when structure is already correct.
- Keeping them separate means retries on structural failures don't burn content-validation budget.

### 4.3 Retry Loop with Conversation History

On validation failure, the pipeline does *not* start a fresh Claude call. Instead, it appends the validation error as a user message to the existing conversation and continues the thread. This means Claude sees:
1. The original prompt and its (failed) response.
2. The specific validation error.
3. An instruction to fix it.

**Why maintain conversation history?**
- Claude can correct targeted errors without regenerating the entire response from scratch.
- Preserves generated content that was correct.
- Reduces token cost compared to full regeneration on every retry.

### 4.4 Domain-Specific Godot Validation

Beyond generic structural validation, `validate_godot_schema()` enforces rules specific to the Godot interaction engine:
- NumLine tangibles: label format, range validity, tick configuration.
- MC questions: no two distractors may be equivalent (would make the question ambiguous).
- Selection: reference bar must match declared options.

**Why in the pipeline validator, not Godot?** Catching these errors at generation time is far cheaper than discovering them at runtime in the game engine. The validator serves as a contract between the AI output and what Godot can consume.

---

## SECTION 5: Prompt Construction & Caching

### 5.1 System Block Ordering for Prompt Caching

The `PromptBuilderV2.build()` method assembles system blocks in a fixed order:
1. Role & context
2. Reference documentation (loaded from `docs/`)
3. Task instructions
4. Examples
5. Output structure

Prompt cache control (`cache_control`) is applied to the *last* block. This means all blocks above it are eligible for caching. Dynamic content (the actual item data) lives in the user message, which is never cached.

**Why this order?** Anthropic's prompt caching is prefix-based — the cache hits if the prefix matches. Placing stable, large content (docs, examples) before dynamic content maximizes cache reuse across calls within a batch.

### 5.2 Module and Template References

Prompts can declare `module_ref` or `template_ref` to pull in live module or template data at build time. These are resolved by `PromptBuilderV2` before the prompt is sent to Claude.

**Why not pass module data as a pipeline variable?** Module data can be large and deeply nested. Declaring the specific fields a prompt needs (via dot-path syntax) keeps the system message minimal and the prompt self-documenting about its own dependencies.

### 5.3 Prefill

Prompts can declare a `prefill` string. The executor injects this as the start of Claude's response before the model continues generating.

**Why?** Prefilling a known structural prefix (e.g., `[`) reliably constrains Claude to produce a JSON array. It also eliminates the need to strip preamble text from responses.

---

## SECTION 6: File I/O & Versioning

### 6.1 Versioned Step Directories

Every pipeline run produces a version directory (`v0`, `v1`, etc.) containing one subdirectory per step. Each step directory holds:
- The step's collated output JSON.
- Per-item files (in batch mode) under `items/`.
- A console log.

Versions are immutable after a run completes. A `latest` symlink points to the most recent version.

**Why immutable versions?** Reruns should never silently overwrite prior outputs. Having all versions on disk makes it possible to diff runs, roll back, and understand what changed between attempts.

### 6.2 Partial Rerun Copies Skipped Steps

When a partial rerun starts at step N, steps 0 through N-1 are copied (symlinked or referenced) from the base version. This keeps the directory structure consistent — a partial rerun's version directory looks the same as a full run's.

**Why copy skipped steps?** Downstream steps use relative paths to find prior step outputs. If skipped steps were absent from the new version directory, those paths would break.

---

## SECTION 7: Rerun & Partial Rerun

### 7.1 Three Execution Modes

| Mode | When used |
|------|-----------|
| `initial` | First run of a pipeline version |
| `rerun` | Full re-execution, all steps, against a base version |
| `partial_rerun` | Subset of steps executed; remainder copied from base |

Modes are tracked in version metadata and affect how the `BatchProcessor` handles ID inheritance and item skipping.

### 7.2 Item-Level Rerun (`rerun_items`)

A rerun can target specific item IDs rather than re-running everything. Specified items are regenerated; all others are loaded from the base version and re-collated unchanged.

**Why support item-level reruns?** Regenerating an entire batch because two items failed is wasteful. Item-level reruns let the operator fix targeted failures while preserving the rest of the run's output exactly.

---

## SECTION 8: Cross-Cutting Decisions

### 8.1 No Branching in AI Steps

AI steps do not branch — they process one item and produce one output. Conditional logic (e.g., "only process MC items") is handled by a preceding formatting step that returns a `batch_only_items` filter.

**Why?** Branching inside an AI step would couple control flow to AI output, making the pipeline harder to reason about and test. Formatting steps are deterministic and independently testable.

### 8.2 Flat Dict for Variable Passing

Variables passed to formatting steps are flattened from nested dicts to `__`-separated keys (e.g., `goal_decomposition__mastery_verb`). This avoids passing arbitrary nested structures through a generic interface.

### 8.3 Validation Errors Do Not Halt the Batch

A validation failure on item N does not stop items N+1 onward from being processed. The failed item is logged and excluded from the collated output, but the batch continues.

**Why?** Halting on a single failure would waste API budget already spent on subsequent items (in async scenarios) and require the operator to restart the entire batch. Logging failures and continuing lets the operator inspect and rerun only the failed items.

### 8.4 Claude Model Is Per-Step

Each AI step can declare its own `model` in `pipelines.json`. There is no single global model for the pipeline.

**Why?** Different steps have different complexity and cost profiles. A structuring step may need a more capable model; a validation step may be fine with a lighter one. Per-step model selection keeps costs proportional to task complexity.

### 8.5 Formatting Steps Are Stateless

Formatting steps receive their input, produce their output, and return. They do not read from or write to step directories themselves — the executor handles all file I/O.

**Why?** Stateless functions are easier to unit-test and can be called independently outside the pipeline (e.g., in tests or one-off scripts) without needing the full pipeline context.

### 8.6 JSON Throughout, Not Markdown

All pipeline data — step inputs, step outputs, pipeline config, per-item files — is JSON. This is not incidental; it is load-bearing for how the pipeline validates, retries, reruns, and ingests reviewed content.

**What JSON gives us that markdown cannot:**

- **Addressable fields.** Downstream steps extract specific fields (`incorrects`, `beats`, `tangibles`) by name. The retry loop (Section 4.3) points Claude at a named field when asking it to fix an error. Markdown has no named fields — parsing it requires fragile heuristics that break when Claude varies its phrasing.
- **Structural validation before acceptance.** A malformed JSON response is caught immediately and retried. A subtly malformed markdown block — missing a section, wrong heading level — may pass into the pipeline undetected and corrupt later steps.
- **Addressable items for targeted reruns.** Every item is a discrete JSON object with a stable ID. The pipeline can regenerate item 7 and copy items 1–6 and 8–N verbatim from the base version. There is no equivalent unit of addressability in a markdown document.
- **Deterministic ingestion of reviewed content.** Reviewers can edit a step output file — correcting a field value, tightening wording — and a later step re-ingests it exactly as written, without passing it back through Claude. This is the foundation of the review workflow: humans make surgical edits to JSON, and the pipeline treats those edits as ground truth. If outputs were markdown, ingesting reviewed content would require Claude to re-parse and re-render it, introducing drift and removing the reviewer's control over exactly what lands in the final output.
- **Direct consumption by downstream systems.** Godot and Notion take structured data. JSON maps to their models without a translation layer; markdown would require a conversion step that adds failure surface.

**Why not YAML or TOML?** Claude produces valid JSON more reliably than YAML (indentation sensitivity causes subtle errors at generation time). Python's `json` module is stdlib with no extra dependency, and JSON is the native format of the Anthropic API response body.

**Where markdown does appear:** `docs/` reference files are markdown because they are human-authored and read by Claude as context — not produced by the pipeline or consumed programmatically. Prompt `instructions` and `examples` fields inside `pipelines.json` also contain markdown prose, because that content is interpreted by Claude, not by code.

The rule of thumb: if a file crosses a programmatic boundary (produced by a step, consumed by a step, pushed to Notion or Godot), it is JSON. If it is written by a human for Claude to read, it may be markdown.
