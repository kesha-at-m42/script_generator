# Script Generator

Automated pipeline for generating interactive math lesson scripts from curriculum specs. Takes a Notion-hosted Module Starter Pack as input and produces structured JSON lesson scripts for Warmup, Lesson, Exit Check, and Synthesis phases.

## How It Works

There are two pipeline families defined in `config/pipelines.json`:

- **`starter_pack_ingestion`** — one-time setup: pulls a module's starter pack from Notion and converts it to local files
- **`*_generator_dialogue_pass`** (lesson, warmup, exitcheck, synthesis) — main generation pipelines: parse a phase spec and produce a fully structured `*_sections.json`

The UI is a Streamlit app (`ui/app.py`) where you select a pipeline, configure it, and run it step by step or end to end.

---

## Pipeline 1: Starter Pack Ingestion

**Purpose:** Pull a module's curriculum data from Notion before running any generator.

```
notion_pull_starter_pack → phase_splitter → starter_pack_json_loader
```

| Step | File | What it does |
|------|------|--------------|
| `notion_pull_starter_pack` | `steps/formatting/notion_pull_starter_pack.py` | Fetches the Notion starter pack page and writes `starter_pack_ref.md` |
| `phase_splitter` | `steps/formatting/phase_splitter.py` | Splits the markdown by section heading into `warmup.md`, `lesson.md`, `exitcheck.md`, `synthesis.md` |
| `starter_pack_json_loader` | `steps/formatting/starter_pack_json_loader.py` | Extracts structured metadata (module title, standards, vocabulary, toy types) into `starter_pack.json` |

**Output:** A local `starter_pack.json` and one `.md` spec file per phase, ready for generation.

---

## Pipeline 2: Dialogue Pass Generator (Lesson / Warmup / Exit Check / Synthesis)

**Purpose:** Convert a phase spec into a fully structured, dialogue-enriched `*_sections.json`.

All four phases share the same step pattern. Using `lesson_generator_dialogue_pass` as the example:

```
spec_splitter → starterpack_parser → toy_spec_loader → glossary_drift_checker
    → section_structurer → id_stamper → dialogue_extractor → dialogue_rewriter
    → dialogue_merger → remediation_filter → remediation_generator → remediation_merger
    → notion_push
```

### Step-by-Step Breakdown

#### Phase 1 — Parse the Spec

**`spec_splitter`** · `steps/formatting/spec_splitter.py`
Deterministically splits the raw `lesson.md` into one item per interaction (Interaction 1.1, 1.2, Opening Hook, Section Transition, etc.) using regex header detection. No AI. Output: `split_spec.json` — array of `{index, major, minor, header, body}` objects.

**`starterpack_parser`** · `steps/prompts/starterpack_parser.py` · AI (batch, one call per section)
Extracts structured fields from each section's markdown body. Parses `**Label:** value` pairs into a JSON schema with fields like `visual`, `guide`, `prompt`, `correct_answer`, `on_incorrect`. Derives a stable `id` from the section's position (e.g., `s1_2`). Output: `structured_spec.json`.

**`toy_spec_loader`** · `steps/formatting/toy_spec_loader.py`
Scans the structured spec for interactive toy types (bar graphs, number lines, etc.) and injects their technical specs from reference files. Output: `enriched_spec.json`.

**`glossary_drift_checker`** · `steps/formatting/glossary_drift_checker.py`
Flags any terms in the spec not found in the canonical module glossary. Writes a `drift_report.md` side-effect. Passes `enriched_spec.json` through unchanged.

#### Phase 2 — Structure the Sections

**`section_structurer`** · `steps/prompts/section_structurer.py` · AI (batch with continuous context)
The core generation step. Converts each enriched spec section into a fully structured section object with a flat `beats` array — scene beats, dialogue beats, prompt beats, `current_scene` beats. Runs with rolling context (`prior_section_summaries`) so later sections can reference visual state from earlier ones (e.g., "the graph you built"). Output: `lesson_sections.json`.

**`id_stamper`** · `steps/formatting/id_stamper.py`
Stamps stable, deterministic IDs on every beat (`{section_id}_b{index}`) and validator-state beat (`{prompt_beat_id}_v{vi}_b{bi}`). Also normalizes any legacy section formats to the canonical flat-beats schema. Idempotent — re-running preserves existing IDs if structure is unchanged.

#### Phase 3 — Rewrite Dialogue

**`dialogue_extractor`** · `steps/formatting/dialogue_extractor.py`
Walks each section and extracts all dialogue beats into a flat list with context labels (`"lesson"` for main flow, `"on_correct"` for validator responses). Produces `dialogue_extracted.json` ready for the AI rewrite pass.

**`dialogue_rewriter`** · `steps/prompts/dialogue_rewriter.py` · AI (batch)
Rewrites all extracted dialogue to improve voice, warmth, and naturalness while preserving pedagogical intent. Output: `dialogue_rewritten.json`.

**`dialogue_merger`** · `steps/formatting/dialogue_merger.py`
Merges the rewritten dialogue texts back into the full section objects positionally (same traversal order as the extractor). Output: final `lesson_sections.json` with polished dialogue.

#### Phase 4 — Generate Remediations

**`remediation_filter`** · `steps/formatting/remediation_filter.py`
Identifies which sections have prompts that need AI-generated incorrect feedback (skips dialogue-only sections and any-response-advances). Output: `sections_to_remediate.json`.

**`remediation_generator`** · `steps/prompts/remediation_generator.py` · AI (batch)
For each prompt in each section, generates incorrect validator states at three severity levels:
- **Non-MC prompts:** Light (dialogue only), Medium (scene + redirect), Heavy (animated demonstration)
- **Single-select MC:** Per-distractor Medium feedback + one Heavy
- **Multi-select MC:** Per-branch Medium feedback + Heavy

Output: `lesson_sections_incorrects.json` — array of `{id, incorrects}` pairs.

**`remediation_merger`** · `steps/formatting/remediation_merger.py`
Merges the incorrect states back into the full section objects, appending them to each prompt beat's validator array. Output: final `lesson_sections.json` with complete correct + incorrect validator coverage.

#### Phase 5 — Push to Notion

**`notion_push`** · `steps/formatting/notion_push.py`
Pushes the completed sections JSON to the corresponding Notion lesson page.

---

## Exporting to Lesson Lab (TOML)

After generation and Notion push, a final optional step converts the finished script into a TOML file for consumption by Lesson Lab (LLP/LLL).

**`toml_sequence_writer`** · `steps/formatting/toml_sequence_writer.py`

Takes a `pull.json` (a Notion-pulled script with `_notion_block_id` stamps) and writes a `.toml` sequence file in the format Lesson Lab expects.

**What it produces:**

```toml
title = "lesson"
type = "sequence"

[section_100_data_collection]
template = "chart_template"

[step_100_data_collection]
dialogue = "Let's look at this data together."
components = ["SceneComponent", "PromptComponent"]

[step_101_data_collection]
dialogue = "Which category has the most?"
components = ["PromptComponent"]
```

**Key rules:**
- Each section becomes a `[section_N_slug]` block with a `template` (auto-selected per module: `chart_template` for M1/M2, `array_template` for M11/M12, `PLACEHOLDER` otherwise)
- Within a section, beats are grouped into steps by `current_scene` boundaries — everything before a `current_scene` beat is one TOML step
- `dialogue` beats are joined into a single string per step; `prompt` beats add `"PromptComponent"` to `components`; `scene` beats are dropped
- The first step in each section always gets `"SceneComponent"` prepended to `components`
- Vocabulary terms wrapped in `{curly braces}` in dialogue are converted to `[vocab]word[/vocab]` tags
- `_toml_key` stamps are written back into the source `pull.json` on each `current_scene` beat, linking TOML steps to Notion block IDs for round-trip traceability
- Section and step counters start at 100 and increment independently

**Running it as a pipeline step** (add to `pipelines.json`):
```json
{
  "name": "toml_sequence_writer",
  "type": "formatting",
  "function": "toml_sequence_writer.write",
  "function_args": {
    "pull_json_path": "tracked_scripts/u1/m3/lesson/step_14_pull/pull.json",
    "output_path": "tracked_scripts/u1/m3/lesson/step_15_toml/lesson-script.toml",
    "unit_number": 1,
    "module_number": 3,
    "phase": "lesson"
  }
}
```

**Running it from the CLI** (auto-detects unit/module/phase from path, prompts before copying to `SEQUENCES_DIR`):
```bash
python steps/formatting/toml_sequence_writer.py tracked_scripts/u1/m3/lesson/step_14_pull/pull.json
# or with explicit dest:
python steps/formatting/toml_sequence_writer.py tracked_scripts/u1/m3/lesson/step_14_pull/pull.json --dest /path/to/sequences/
```

Set the `SEQUENCES_DIR` env variable to your local Lesson Lab sequences directory to have the CLI offer to copy the TOML there automatically.

> **Note:** TOML output files must use LF line endings (enforced by `.gitattributes`). The writer opens output files with `newline="\n"` to guarantee this.

---

## Running a Pipeline

# Run a pipeline directly from CLI
python cli/run_pipeline.py --pipeline lesson_generator_dialogue_pass --module u1/m3 --phase lesson
```

Intermediate outputs are written to `outputs/<pipeline_name>/v{N}/` for each run. Each step's output file is listed in `config/pipelines.json` under `"output_file"`.

---

## Key Files at a Glance

```
config/pipelines.json          # All pipeline definitions — start here
steps/prompts/                 # AI prompt steps (Claude API calls)
steps/formatting/              # Deterministic post-processing steps
core/pipeline.py               # Pipeline execution engine (batch, retry, versioning)
core/claude_client.py          # Claude API client
ui/app.py                      # Streamlit UI
cli/                           # CLI entry points
```

## Step Types

Every step in `pipelines.json` is one of two types:

| Type | How it runs | Defined in |
|------|-------------|------------|
| `"type": "ai"` | Claude API call, driven by a prompt file | `steps/prompts/<prompt_name>.py` |
| `"type": "formatting"` | Pure Python function, no AI | `steps/formatting/<function>.py` |

AI steps support `"batch_mode": true` to process items independently (one Claude call per item) with skip/resume on failure.
