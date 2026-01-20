# Batch Processing & Versioning Guide

Complete guide to the new batch processing and versioning features in the pipeline system.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Batch Mode Features](#batch-mode-features)
- [Version Management](#version-management)
- [Workflow Examples](#workflow-examples)
- [CLI Tools](#cli-tools)
- [Output Structure](#output-structure)

## Overview

The pipeline now supports **batch processing** - processing JSON arrays item-by-item with separate API calls, automatic collation, and version-based output management.

### Key Features

✅ **Batch Processing**: Process array items one-by-one (better caching, parallel-friendly)
✅ **Auto-Collation**: Individual results automatically combined into arrays
✅ **Versioning**: Outputs organized as v0, v1, v2... with full history
✅ **Selective Rerun**: Reprocess specific items only
✅ **Error Handling**: Continue on failures, track errors separately
✅ **Variable Flattening**: Nested fields auto-available as `{field__nested__value}`
✅ **Sequential IDs**: Add sequential IDs to outputs

## Quick Start

### Basic Batch Pipeline

```python
from core.pipeline import run_pipeline, Step

result = run_pipeline(
    steps=[
        Step(
            prompt_name="generate_problem",
            input_file="inputs/modules/module4/problem_templates.json",
            batch_mode=True,                      # Enable batch processing
            batch_id_field="template_id",         # Field to use as ID
            batch_output_id_field="problem_id",   # Add sequential IDs
            output_file="problems.json"
        )
    ],
    pipeline_name="problem_generator",  # Enables versioning
    module_number=4,
    verbose=True
)
```

### What Happens

1. Loads `problem_templates.json` (array of 14 templates)
2. Processes each template individually (14 separate API calls)
3. Flattens each template to variables:
   - `{template_id}` = "4001"
   - `{problem_type}` = "Student clicks..."
   - `{goal_decomposition__mastery_verb}` = "create"
   - All fields available in prompt
4. Saves individual results: `items/4001/01_output.json`, `items/4002/01_output.json`, ...
5. Collates all results: `collated/01_problems.json` (array with 14 items)
6. Creates version: `outputs/problem_generator_module_4/v0/`

**Folder naming:** The output directory is automatically named `{pipeline_name}_module_{module_number}_path_{path_letter}`. This keeps outputs organized when working across different modules and paths.

## Batch Mode Features

### Step Parameters

```python
Step(
    # Batch processing
    batch_mode=True,                    # Enable item-by-item processing
    batch_id_field="template_id",       # Field from input items to use as ID
    batch_output_id_field="problem_id", # Add sequential ID field to outputs
    batch_id_start=1,                   # Starting number for sequential IDs

    # Selective processing
    batch_only_items=["4001", "4002"],  # Only process these IDs
    batch_skip_items=["4010"],          # Skip these IDs
    batch_skip_existing=True,           # Skip items with existing outputs (resume)

    # Error handling
    batch_stop_on_error=False,          # Continue on errors (default: continue)
)
```

### Variable Flattening

Nested fields are automatically flattened with `__` separator:

**Input Item:**
```json
{
  "template_id": "4001",
  "problem_type": "Click tick mark...",
  "goal_decomposition": {
    "mastery_verb": "create",
    "mastery_tier": ["baseline", "support"]
  },
  "parameter_coverage": {
    "fractions": ["1/2", "1/3", "1/4"]
  }
}
```

**Available Variables in Prompt:**
```
{template_id}                              → "4001"
{problem_type}                             → "Click tick mark..."
{goal_decomposition__mastery_verb}         → "create"
{goal_decomposition__mastery_tier}         → ["baseline", "support"]
{parameter_coverage__fractions}            → ["1/2", "1/3", "1/4"]
```

### Sequential IDs

Add sequential IDs to output items:

```python
Step(
    batch_output_id_field="problem_id",  # Field name for sequential ID
    batch_id_start=1                     # Start numbering from 1
)
```

**Output:**
```json
[
  {
    "problem_id": 1,
    "source_template_id": "4001",
    "question": "..."
  },
  {
    "problem_id": 2,
    "source_template_id": "4002",
    "question": "..."
  }
]
```

## Version Management

### Version Structure

When using `pipeline_name`, outputs are organized by version:

```
outputs/
└─ problem_generator_module_4/     # pipeline_name_module_X
   ├─ v0/                          # Version 0 (initial run)
   │  ├─ items/                    # Individual item results
   │  │  ├─ 4001/
   │  │  │  ├─ 01_output.json
   │  │  │  └─ 02_output.json
   │  │  ├─ 4002/
   │  │  └─ ...
   │  ├─ collated/                 # Collated arrays
   │  │  ├─ 01_step1.json
   │  │  └─ 02_step2.json
   │  ├─ prompts/                  # Saved prompts
   │  │  ├─ 01_prompt_4001.md
   │  │  └─ ...
   │  └─ metadata.json             # Version metadata
   ├─ v1/                          # Version 1 (rerun)
   │  ├─ items/                    # Only rerun items
   │  │  └─ 4002/
   │  ├─ collated/                 # Merged: v0 + v1
   │  └─ metadata.json
   └─ latest -> v1                 # Symlink to latest version
```

**Note:** If you also provide `path_letter`, the directory becomes: `problem_generator_module_4_path_a`

### Metadata

Each version has `metadata.json`:

```json
{
  "version": "v1",
  "pipeline_name": "problem_generator",
  "timestamp": "2026-01-20T14:30:00",
  "mode": "rerun",
  "base_version": "v0",
  "module_number": 4,
  "path_letter": null,
  "pipeline_status": "beta",
  "notes": "Fixed prompt issue for template 4002",
  "duration_seconds": 125.3,
  "status": "completed",
  "full_pipeline_name": "problem_generator_module_4",
  "logs": [],
  "stats": {}
}
```

**Pipeline Status Labels** (use to track maturity):
- `"draft"` - Default, experimental/work-in-progress
- `"alpha"` - Early testing, known issues
- `"beta"` - Testing with real data, mostly stable
- `"rc"` - Release candidate, ready for review
- `"final"` - Production-ready, approved version
- `"deprecated"` - Old version, superseded by newer
- Custom labels as needed

## Workflow Examples

### 1. Initial Run

```python
result = run_pipeline(
    steps=[
        Step(
            prompt_name="generate_interaction",
            input_file="inputs/modules/module4/problem_templates.json",
            batch_mode=True,
            batch_id_field="template_id",
            batch_output_id_field="interaction_id",
            output_file="interactions.json"
        )
    ],
    pipeline_name="problem_generator",
    module_number=4,
    pipeline_status="alpha",  # Mark as alpha - early testing
    notes="First run with new template structure"
)
```

**Output:** `outputs/problem_generator_module_4/v0/`

### 2. Review & Rerun

After reviewing outputs, you find issues with items 4002 and 4007:

```python
result = run_pipeline(
    steps=[...],  # Same steps
    pipeline_name="problem_generator",
    module_number=4,
    rerun_items=["4002", "4007"],  # Only process these
    pipeline_status="beta",  # Upgraded to beta after fixes
    notes="Fixed prompt issues for templates 4002 and 4007"
)
```

**Output:** `outputs/problem_generator_module_4/v1/`
- Items processed: 4002, 4007 (2 items)
- Collated output: Merges v0 (all items) + v1 (new 4002, 4007)

### 3. Continue Working

Next pipeline uses the latest collated output:

```python
result = run_pipeline(
    steps=[
        Step(
            prompt_name="process_interactions",
            input_file="outputs/problem_generator_module_4/latest/collated/01_interactions.json",
            batch_mode=True,
            batch_id_field="interaction_id",
            output_file="processed.json"
        )
    ],
    pipeline_name="interaction_processor",
    module_number=4
)
```

### 4. Resume After Failure

If pipeline crashes at item 8/14:

```python
result = run_pipeline(
    steps=[
        Step(
            prompt_name="generate_problem",
            batch_mode=True,
            batch_skip_existing=True,  # Skip completed items
            ...
        )
    ],
    pipeline_name="problem_generator"
)
```

Processes only items 8-14 (skips 1-7 that already have outputs).

## CLI Tools

### List Pipelines

```bash
# List all pipelines (default: shows beta, rc, final only)
python list.py

# List versions of a pipeline (default: shows beta, rc, final only)
python list.py problem_generator_module_4

# Show ALL versions (including draft and deprecated)
python list.py problem_generator_module_4 --all

# Filter by specific status
python list.py problem_generator_module_4 --status final
python list.py problem_generator_module_4 --status beta rc  # Multiple statuses
```

**Output (default - filtered):**
```
======================================================================
PIPELINE: problem_generator_module_4
Versions: 1 (hiding 1)
Latest: v1
Showing: beta, final, rc
Tip: Use --all to show all versions, or --status <status> to filter
======================================================================

v1 (latest)
  Created: 2026-01-20T14:30:00
  Status: beta
  Notes: Fixed prompt issues for templates 4002 and 4007
  Mode: rerun
  Base: v0
  Duration: 15.2s
  Items: 2
```

**Output (--all):**
```
======================================================================
PIPELINE: problem_generator_module_4
Versions: 2
Latest: v1
======================================================================

v0
  Created: 2026-01-20T10:00:00
  Status: alpha
  Notes: First run with new template structure
  Mode: initial
  Duration: 125.3s
  Items: 14

v1 (latest)
  Created: 2026-01-20T14:30:00
  Status: beta
  Notes: Fixed prompt issues for templates 4002 and 4007
  Mode: rerun
  Base: v0
  Duration: 15.2s
  Items: 2
```

### Compare Versions

```bash
# Basic comparison
python compare.py problem_generator_module_4 v0 v1

# Detailed comparison
python compare.py problem_generator_module_4 v0 v1 --detail
```

**Output:**
```
======================================================================
COMPARING: problem_generator_module_4
v0 vs v1
======================================================================

Version Info:
  v0:
    Created: 2026-01-20T10:00:00
    Status: alpha
    Notes: First run with new template structure
    Mode: initial
    Duration: 125.3s

  v1:
    Created: 2026-01-20T14:30:00
    Status: beta
    Notes: Fixed prompt issues for templates 4002 and 4007
    Mode: rerun
    Base: v0
    Duration: 15.2s

Items:
  Total in v0: 14
  Total in v1: 2
  In both: 2
  Only in v0: 4001, 4003-4014
  Only in v1: (none, merged with v0)
```

### Rerun Items

```bash
# Rerun specific items
python rerun.py problem_generator_module_4 4002

# Multiple items
python rerun.py problem_generator_module_4 4002 4007 4012

# With note
python rerun.py problem_generator_module_4 4002 --note "Fixed prompt issue"
```

Note: Currently shows usage instructions. Full automation requires saving step config in metadata.

## Output Structure

### Individual Item Outputs

Each processed item saves to: `items/{item_id}/{step_number}_output.json`

Example: `items/4001/01_output.json`
```json
{
  "problem_id": 1,
  "source_template_id": "4001",
  "question": "Place one-third on the number line.",
  "workspace": {...},
  ...
}
```

### Collated Outputs

All items combined: `collated/{step_number}_{output_file}`

Example: `collated/01_interactions.json`
```json
[
  {
    "problem_id": 1,
    "source_template_id": "4001",
    ...
  },
  {
    "problem_id": 2,
    "source_template_id": "4002",
    ...
  },
  ...
]
```

### Error Tracking

If items fail: `{step_number}_errors.json`

Example: `01_errors.json`
```json
[
  {
    "item_id": "4007",
    "item_index": 7,
    "error": "JSON parsing failed",
    "step": 1
  }
]
```

## Best Practices

### 1. Use Pipeline Status for Workflow Management

Mark your pipeline versions with appropriate statuses to track maturity:

```python
# Experimental/early work
run_pipeline(steps=[...], pipeline_status="draft")  # Default, hidden from list

# First real test
run_pipeline(steps=[...], pipeline_status="alpha", notes="Testing new approach")

# Stable for review
run_pipeline(steps=[...], pipeline_status="beta", notes="Ready for team review")

# Final candidate
run_pipeline(steps=[...], pipeline_status="rc", notes="Release candidate v1")

# Production-ready
run_pipeline(steps=[...], pipeline_status="final", notes="Approved by team")

# Old version
# (Manually mark old versions as deprecated in metadata.json)
```

**Status Workflow Example:**
1. `draft` (v0-v5) - Experimenting with prompts (hidden by default)
2. `alpha` (v6) - First working version (hidden by default)
3. `beta` (v7-v8) - Testing with real data (shown by default)
4. `rc` (v9) - Ready for review (shown by default)
5. `final` (v10) - Approved for production (shown by default)
6. `deprecated` - When v11 supersedes v10 (hidden by default)

**Benefits:**
- `python list.py` only shows important versions (beta/rc/final)
- `--all` flag shows everything when needed
- Clear progression from draft to final
- Easy to find production-ready versions

### 2. Use Versioning for Iterative Work

Always provide `pipeline_name` for work you'll iterate on:

```python
# Good: Enables versioning
run_pipeline(steps=[...], pipeline_name="problem_generator")

# Less ideal: One-off, no version history
run_pipeline(steps=[...])
```

### 3. Set Appropriate Error Handling

For exploratory work:
```python
batch_stop_on_error=False  # Continue, see all failures
```

For production:
```python
batch_stop_on_error=True   # Stop on first error
```

### 4. Use Sequential IDs for Chaining

When output feeds into next pipeline:
```python
batch_output_id_field="interaction_id"  # Makes next step easier
```

### 5. Resume Large Batches

For long-running batches, enable resume:
```python
batch_skip_existing=True  # Skip completed items on restart
```

### 6. Review Collated Outputs

Always use the collated outputs for the next pipeline step:
```python
input_file="outputs/problem_generator/latest/collated/01_problems.json"
```

## Advanced Usage

### Multi-Step Batch Pipeline

```python
run_pipeline(
    steps=[
        # Step 1: Templates → Interactions (batch)
        Step(
            prompt_name="generate_interaction",
            input_file="templates.json",
            batch_mode=True,
            batch_id_field="template_id",
            batch_output_id_field="interaction_id",
            output_file="interactions.json"
        ),

        # Step 2: Interactions → Formatted (batch)
        # Auto-chains from step 1 collated output
        Step(
            prompt_name="format_interaction",
            batch_mode=True,
            batch_id_field="interaction_id",
            output_file="formatted.json"
        ),

        # Step 3: Final processing (batch)
        Step(
            prompt_name="finalize",
            batch_mode=True,
            batch_id_field="interaction_id",
            output_file="final.json"
        )
    ],
    pipeline_name="full_pipeline",
    module_number=4
)
```

### Filtering Items

```python
# Only process baseline tier templates
Step(
    batch_mode=True,
    batch_only_items=["4001", "4003", "4005", "4007", "4009"]  # baseline IDs
)

# Skip problematic items
Step(
    batch_mode=True,
    batch_skip_items=["4010", "4011"]  # Known issues
)
```

## Troubleshooting

### Collation Not Working

**Problem:** Collated output has fewer items than expected

**Solution:** Check for errors in `{step}_errors.json`. Items that fail are not included in collation unless `batch_stop_on_error=True`.

### Variables Not Available

**Problem:** Variable `{goal_decomposition__mastery_verb}` not found

**Solution:**
1. Check verbose output to see available variables
2. Verify field exists in input JSON
3. Ensure using correct `__` separator for nesting

### Version Conflict

**Problem:** Rerun creates new version but you wanted to update existing

**Solution:** Versioning always creates new versions. This is intentional for full history. Use version compare tools to see changes.

## Migration from Old Pipelines

### Before (Single API Call with Array)

```python
Step(
    prompt_name="process_all",
    input_file="templates.json",  # Claude sees full array
    output_file="results.json"
)
```

### After (Batch Processing)

```python
Step(
    prompt_name="process_item",   # Process one at a time
    input_file="templates.json",
    batch_mode=True,
    batch_id_field="template_id",
    output_file="results.json"    # Auto-collated
)
```

**Benefits:**
- Better prompt caching (each item cached separately)
- Easier to rerun specific items
- Progress tracking per item
- Cleaner error handling

## See Also

- `example_batch_pipeline.py` - Working examples
- `core/pipeline.py` - Full API documentation
- `utils/template_utils.py` - Template loading utilities
