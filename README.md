# Educational Content Generation Pipeline

An automated pipeline system for generating interactive educational content using Claude API. The system transforms learning goals into complete Godot-compatible interaction sequences with remediation paths.

## 🎯 Overview

The pipeline generates educational content through multiple steps:

```
Templates → Problems → Sequences → BBCode Format → Godot Output
  (input)      (AI)       (AI)       (formatting)    (formatting)
```

Each step processes items individually with AI and deterministic post-processing.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key

### Installation

1. Clone and navigate:
```bash
git clone https://github.com/kesha-at-m42/script_generator.git
cd script_generator
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows (Git Bash)
source venv/Scripts/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install anthropic python-dotenv
```

5. Create `.env` file:
```bash
ANTHROPIC_API_KEY=your-api-key-here
```

### Running the Pipeline

**Interactive Mode (Recommended):**
```bash
python cli/run_pipeline.py
```
Follow prompts to select pipeline, module, and path.

**Command Line Mode:**
```bash
# Run full pipeline
python cli/run_pipeline.py --pipeline problem_generator --module 4 --path a

# Run with custom status
python cli/run_pipeline.py --pipeline problem_generator --module 4 --path a --status alpha
```

## 📁 Project Structure

```
script_generator-content/
├── core/                           # Core pipeline components
│   ├── pipeline.py                 # Main pipeline orchestration
│   ├── claude_client.py            # Claude API wrapper
│   ├── prompt_builder.py           # Prompt assembly
│   ├── batch_processor.py          # Batch processing logic
│   ├── version_manager.py          # Version control
│   └── path_manager.py             # Path resolution
│
├── cli/                            # Command-line interfaces
│   ├── run_pipeline.py             # Interactive pipeline runner
│   ├── rerun.py                    # Rerun specific items/steps
│   ├── list.py                     # List versions/outputs
│   └── create_prompt.py            # Create new prompts
│
├── config/                         # Configuration
│   ├── pipelines.json              # Pipeline definitions
│   └── pipelines.py                # Pipeline loader
│
├── steps/                          # Step definitions
│   ├── prompts/                    # AI prompt files
│   │   ├── problem_generator.py
│   │   ├── sequence_structurer.py
│   │   └── ...
│   └── formatting/                 # Deterministic formatters
│       ├── bbcode_formatter.py
│       └── ...
│
├── modules/                        # Module-specific content
│   ├── module4/
│   │   ├── problem_templates_v2.json
│   │   ├── patha/
│   │   │   ├── visuals.md
│   │   │   └── ...
│   │   └── pathb/
│   │       └── ...
│   └── module5/
│       └── ...
│
├── docs/                           # Reference documentation
│   ├── remediation_system.md
│   ├── guide_design.md
│   └── ...
│
├── outputs/                        # Generated content (gitignored)
│   └── problem_generator_module_4_path_a/
│       ├── v0/                     # Initial version
│       │   ├── step_01_problem_generator/
│       │   │   ├── items/          # Individual outputs
│       │   │   ├── prompts/        # Prompts sent to Claude
│       │   │   └── problem_generator.json
│       │   ├── step_02_sequence_structurer/
│       │   └── metadata.json
│       ├── v1/                     # Rerun version
│       └── latest -> v1            # Symlink to latest
│
└── utils/                          # Utility functions
    ├── json_utils.py
    └── template_utils.py
```

## 🔄 Pipeline System

### Pipeline Configuration

Pipelines are defined in `config/pipelines.json`:

```json
{
  "problem_generator": [
    {
      "type": "ai",
      "prompt_name": "problem_generator",
      "batch_mode": true,
      "batch_id_field": "template_id",
      "batch_output_id_field": "problem_id",
      "batch_id_start": 4001
    },
    {
      "type": "ai",
      "prompt_name": "sequence_structurer",
      "batch_mode": true,
      "batch_id_field": "problem_id"
    },
    {
      "type": "formatting",
      "function": "bbcode_formatter.process_godot_sequences",
      "batch_mode": true,
      "batch_id_field": "problem_id"
    }
  ]
}
```

### Step Types

**AI Steps:**
- Call Claude API with prompt
- Process items individually
- Auto-chain outputs between steps

**Formatting Steps:**
- Run deterministic Python functions
- Apply post-processing (BBCode, metadata)
- No API calls

### Batch Processing

Steps can process items individually with:
- `batch_mode: true` - Process array item-by-item
- `batch_id_field` - Field to use as item ID
- `batch_output_id_field` - Add sequential IDs to outputs
- `batch_id_start` - Starting number for IDs

## 🔁 Rerun System

### Item-Level Reruns

Rerun specific items from batch steps:

```bash
# Rerun items 4001 and 4005
python cli/rerun.py problem_generator 4001 4005 --module 4 --path a

# Rerun with note
python cli/rerun.py problem_generator 4001 --note "Fixed prompt" --module 4 --path a

# Rerun from specific base version
python cli/rerun.py problem_generator 4001 --base v2 --module 4 --path a
```

### Step-Level Reruns (NEW)

Rerun specific step ranges without re-running earlier steps:

```bash
# Run from step 3 onwards
python cli/rerun.py problem_generator --start-from 3 --module 4 --path a

# Run ONLY step 3
python cli/rerun.py problem_generator --start-from 3 --end-at 3 --module 4 --path a

# Run steps 2-4
python cli/rerun.py problem_generator --start-from 2 --end-at 4 --module 4 --path a

# Use step names instead of numbers
python cli/rerun.py problem_generator --start-from sequence_structurer --module 4 --path a
```

**How it works:**
- Steps outside the range are skipped
- First executed step loads input from base version
- Subsequent steps chain normally from current version
- Creates a new version with only executed steps

**Combined mode:**
Rerun specific items within a step range:
```bash
python cli/rerun.py problem_generator 4001 4005 --start-from 2 --end-at 3 --module 4 --path a
```

### Use Cases for Step Reruns

1. **Iterate on a specific step's prompt** - Change step 3's prompt, rerun only step 3
2. **Debug a single step** - Isolate and test one step
3. **Resume from failure** - Continue from where pipeline failed
4. **Skip expensive steps** - Skip early steps that don't need changes

## 📊 Version Control

### Automatic Versioning

Each pipeline run creates a new version:
```
outputs/problem_generator_module_4_path_a/
├── v0/         # Initial run
├── v1/         # First rerun
├── v2/         # Second rerun
└── latest/     # Symlink to latest version
```

### Metadata Tracking

Each version includes `metadata.json`:

```json
{
  "version": "v1",
  "base_version": "v0",
  "mode": "partial_rerun",
  "step_range": "3-3",
  "skipped_steps": [1, 2, 4, 5],
  "executed_steps": [3],
  "timestamp": "2026-01-24T10:30:00",
  "duration_seconds": 12.5,
  "pipeline_name": "problem_generator",
  "module_number": 4,
  "path_letter": "a",
  "pipeline_status": "alpha",
  "notes": "Testing updated prompt for step 3"
}
```

**Modes:**
- `initial` - First run of pipeline
- `rerun` - Full pipeline rerun
- `partial_rerun` - Step range execution

## 🛠️ CLI Tools

### run_pipeline.py

Interactive pipeline execution:
```bash
python cli/run_pipeline.py
# Prompts for: pipeline, module, path, status, notes
```

### rerun.py

Rerun items or steps:
```bash
# Item reruns
python cli/rerun.py <pipeline> <item_ids> --module N --path X

# Step reruns
python cli/rerun.py <pipeline> --start-from N --end-at N --module N --path X
```

### list.py

List available pipelines and versions:
```bash
# List all pipelines
python cli/list.py

# List versions for a pipeline
python cli/list.py problem_generator_module_4_path_a
```

### create_prompt.py

Create new prompt files:
```bash
python cli/create_prompt.py my_new_prompt
```

## 📝 Development

### Creating a New Pipeline

1. **Define steps** in `config/pipelines.json`:
```json
{
  "my_pipeline": [
    {
      "type": "ai",
      "prompt_name": "my_prompt",
      "batch_mode": true,
      "batch_id_field": "id"
    }
  ]
}
```

2. **Create prompt** in `steps/prompts/my_prompt.py`:
```python
ROLE = "You are an expert..."
DOCS = ["reference_doc.md"]
MODULE_REF = ["field1", "field2"]
INSTRUCTIONS = """
Generate output based on {field1} and {field2}.
"""
EXAMPLES = ["example1", "example2"]
```

3. **Run pipeline**:
```bash
python cli/run_pipeline.py --pipeline my_pipeline --module 4 --path a
```

### Adding a Formatting Step

1. **Create function** in `steps/formatting/my_formatter.py`:
```python
def process_data(data, module_number=None, path_letter=None):
    """Process data deterministically"""
    # Transform data
    return processed_data
```

2. **Add to pipeline**:
```json
{
  "type": "formatting",
  "function": "my_formatter.process_data",
  "batch_mode": true,
  "batch_id_field": "id"
}
```

### Modifying Prompts

**Safe to modify:**
- `ROLE` - Change persona/expertise
- `INSTRUCTIONS` - Update task description
- `DOCS` - Add/remove reference docs
- `EXAMPLES` - Add more examples

**Be careful with:**
- Variable names in `{brackets}` - must match `MODULE_REF`
- JSON structure in examples

**Documentation references:**
Add docs to `DOCS` list, then reference with XML tags:
```python
DOCS = ["my_guide.md"]
INSTRUCTIONS = """
Follow guidelines in <my_guide> for formatting.
"""
```

## 🔐 Security

Never commit:
- `.env` (API keys)
- `outputs/` (generated content)
- `venv/` (virtual environment)

These are in `.gitignore`.

## 📋 Output Format

### Final Output Structure

```json
{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "metadata": {
        "@type": "SequenceMetadata",
        "problem_id": 4001,
        "template_id": 5,
        "mastery_tier": 2,
        "mastery_component": "PROCEDURAL"
      },
      "steps": [
        {
          "@type": "Step",
          "dialogue": "Here's a [fraction]3/4[/fraction] bar.",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [...]
          }
        }
      ]
    }
  ]
}
```

## 💡 Best Practices

**Running pipelines:**
1. Use interactive mode for first run
2. Check outputs in `outputs/pipeline_name/latest/`
3. Use step reruns to iterate on prompts
4. Add notes to track changes

**Debugging:**
1. Check `prompts/` directory for exact prompts sent
2. Check `items/` directory for individual outputs
3. Look at `errors.json` for failed items
4. Use `--verbose` for detailed logging

**Version management:**
1. Keep base versions when iterating
2. Use meaningful notes for reruns
3. Use pipeline status (alpha/beta/rc/final) to track maturity

## 🆘 Common Issues

**Import errors:**
```bash
# Make sure you're in project root
cd /path/to/script_generator-content

# Activate virtual environment
source venv/Scripts/activate  # Windows Git Bash
```

**API key not found:**
```bash
# Create .env file in project root
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

**No versions found:**
```bash
# Run full pipeline first before rerun
python cli/run_pipeline.py --pipeline problem_generator --module 4 --path a
```

**Step range requires base version:**
```bash
# Either specify base version or run full pipeline first
python cli/rerun.py problem_generator --start-from 3 --base v0 --module 4 --path a
```
