# script_generator — Project Guide for Claude

## Project Layout

```
script_generator/
├── core/          # Core pipeline logic (claude client, prompt builder, pipeline executor, etc.)
├── config/        # Static config files: pipelines.json, misconceptions.json, animation_events.json
├── ui/            # Streamlit app (app.py, run_dev.py)
├── utils/         # Reusable utilities (json_utils, template_utils, validators, formatting, etc.)
├── modules/       # Standalone feature modules
├── cli/           # CLI entry points
├── tests/         # All test files — see naming conventions below
├── outputs/       # Generated script outputs (not committed)
├── good_outputs/  # Curated/approved outputs (not committed)
├── logs/          # Runtime logs (not committed)
├── docs/          # Documentation
├── fixes/         # One-off data fix scripts
└── steps/         # Step-by-step pipeline definitions
```

## Where to Put New Files

| File type                        | Directory                    |
|----------------------------------|------------------------------|
| Pipeline / orchestration logic   | `core/`                      |
| Claude API client changes        | `core/claude_client.py`      |
| Prompt construction logic        | `core/prompt_builder.py`     |
| Pipeline definitions (JSON)      | `config/`                    |
| Reusable utility functions       | `utils/`                     |
| Input validators                 | `utils/validators/`          |
| Formatting helpers               | `utils/formatting/`          |
| UI / Streamlit pages             | `ui/`                        |
| CLI commands                     | `cli/`                       |
| Standalone feature modules       | `modules/`                   |
| Formatting pipeline steps        | `steps/formatting/`          |
| Tests                            | `tests/`                     |

## Test Conventions

- Test files: `tests/test_<module_name>.py`
- Stepwise / multi-step tests: `tests/stepwise_tests/`
- Test output artifacts: `tests/test_outputs/`
- Run tests: `pytest tests/`

## Code Conventions

- Language: Python 3
- Formatter: `ruff format` (run before committing)
- Linter: `ruff check`
- Pre-commit hooks are configured — do not skip with `--no-verify`
- Virtual environment: `venv/` (never modify this)

## Steps Conventions

- `steps/formatting/` — all formatting pipeline steps (deterministic post-processing, no AI calls)
- `steps/prompts/` — AI prompt steps (generators, structurers, etc.)
- When a step becomes outdated or superseded, move it to `archive/` — do **not** leave old versions alongside new ones

## figma_experiment/ Directory

One-off and experimental scripts that are not part of the core pipeline. Not imported by other modules.

| File type                                        | Location                          |
|--------------------------------------------------|-----------------------------------|
| Experiments (dirty, exploratory, throwaway)      | `figma_experiment/`               |
| Figma integration utilities                      | `figma_experiment/figma_*.py`     |
| Figma node manifest (name → node ID mapping)     | `figma_experiment/figma_manifest.json` |
| Raw node tree dumps (auto-generated, throwaway)  | `figma_experiment/figma_nodes_raw.json` |

**Rules:**
- Scripts here are standalone — no imports from `core/`, `utils/`, etc.
- Once an experiment proves out and needs to integrate with the pipeline, move the logic to the appropriate `core/` or `utils/` module and delete the script.
- Do not create subdirectories inside `figma_experiment/` — keep it flat.

## When You're Not Sure Where a File Goes

**Ask before creating.** If a new file doesn't clearly fit an existing directory from the table above, ask the user rather than guessing. Prefer:
1. Extending an existing file over creating a new one
2. Asking over assuming

Common ambiguous cases and what to do:
- "Is this a reusable utility or a one-off script?" → ask
- "Should this be a CLI command or a module?" → ask
- "Does this belong in `core/` or `modules/`?" → ask; generally: if it's part of the generation pipeline it's `core/`, if it's a standalone feature (e.g. Notion sync) it's `modules/`

## Do Not Touch

- `venv/` — managed by pip/venv
- `outputs/`, `good_outputs/`, `logs/` — runtime artifacts, not source files
- `archive/` — legacy code kept for reference, do not add to it
