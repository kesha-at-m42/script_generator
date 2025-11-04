# Educational Content Generation Pipeline

An automated pipeline system for generating interactive educational content using Claude API. The system transforms learning goals into complete Godot-compatible interaction sequences with remediation paths.

## 🎯 Overview

The pipeline generates educational content through 4 main steps:

```
Learning Goals → Questions → Interactions → Remediations → Godot Format
     (input)        (AI)         (AI)          (AI)          (AI + deterministic)
```

Each step processes items individually and applies deterministic post-processing where needed (metadata correction, BBCode formatting).

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key

  ### Installing Python

  If you don't have Python installed, download it from the official website:

  **Windows/Mac/Linux:**
  1. Visit [python.org/downloads](https://www.python.org/downloads/)
  2. Download the latest Python 3.x version (3.8 or higher)
  3. Run the installer
     - **Windows**: Check "Add Python to PATH" during installation
     - **Mac**: Follow the installer prompts
     - **Linux**: Use your package manager (e.g., `sudo apt install python3`)

  **Verify installation:**
  ```bash
  python --version  # Should show Python 3.8 or higher

  If python --version doesn't work, try:
  python3 --version  # Linux/Mac often use python3 command

### Installation

1. Clone and navigate to the repository:
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

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

**Verify activation:** You should see `(venv)` at the start of your prompt:
```bash
(venv) user@computer ~/script_generator $  # ✅ Active
user@computer ~/script_generator $         # ❌ Not active - need to activate
```

**Note:** Keep the terminal window open after activation. The environment stays active until you close the terminal or run `deactivate`.

4. Install dependencies:
```bash
pip install anthropic python-dotenv
```

4. Create `.env` file:
```bash
ANTHROPIC_API_KEY=your-api-key-here
```

### Running the Pipeline

```bash
# Run full pipeline
python pipeline_runner.py --module 2 --path b --pipeline full

# Run specific steps only
python pipeline_runner.py --module 2 --path b --pipeline questions_only
python pipeline_runner.py --module 2 --path b --pipeline remediation_only

# Run with custom output directory
python pipeline_runner.py --module 2 --path b --pipeline full --output-dir outputs/custom
```

## 📁 Project Structure

```
script_generator/
├── core/                           # Core system components
│   ├── claude_client.py           # Claude API wrapper
│   ├── prompt_builder.py          # Prompt assembly and variable substitution
├── inputs/                        # Input data and prompts
│   ├── modules/                   # Module-specific content│   │
│   ├── prompts/                   # AI prompt definitions
│   │   ├── question_generator.py      # Generates questions from goals
│   │   ├── interaction_designer.py    # Creates interaction sequences
│   │   ├── remediation_generator.py   # Adds error remediation paths
│   │   └── godot_formatter.py         # Transforms to Godot schema
│   │
│   └── docs/                      # Reference documentation for prompts│
├── utils/                         # Utility functions
├── outputs/                       # Generated content (gitignored)
│   └── pipeline_module2_pathb_TIMESTAMP/
│       ├── questions.json             # Generated questions
│       ├── interactions.json          # Interaction sequences
│       ├── remediation.json          # With error paths added
│       ├── final.json                # Godot-formatted output
│       ├── question_generator/       # Raw LLM responses + prompts
│       ├── interaction_designer/
│       ├── remediation_generator/
│       └── godot_formatter/
│
├── tests/                         # Test files
│   ├── stepwise_tests/            # Individual step tests
│   │   ├── test_1_question_generator.py
│   │   ├── test_2_interaction_designer.py
│   │   ├── test_3_remediation_generator.py
│   │   └── test_4_godot_formatter.py
│   └── archived_tests/            # Legacy test files
│
├── pipeline_runner.py             # Main pipeline orchestration
├── .env                          # API keys (gitignored)
└── README.md                     # This file
```

## 🔄 Pipeline Steps

### 1. Question Generator
**Input**: Learning goals from `inputs/modules/moduleN/decomposed_goals.json`
**Output**: `questions.json` - Assessment questions for each goal
**Processing**: Item-by-item (one goal at a time)

Generates multiple questions per learning goal, including:
- Question prompts
- Cognitive type (IDENTIFY, CREATE, COMPARE, etc.)
- Visual context descriptions
- Variables used
- Difficulty level

### 2. Interaction Designer
**Input**: `questions.json`
**Output**: `interactions.json` - Interactive sequences with workspace definitions
**Processing**: Item-by-item (one question at a time)

Creates step-by-step interaction flows with:
- Workspace tangibles (bars, shapes, choice buttons)
- Dialogue and prompts
- Correct answers
- Success path feedback

### 3. Remediation Generator
**Input**: `interactions.json`
**Output**: `remediation.json` - Sequences with error paths
**Processing**: Item-by-item (one sequence at a time)

Adds three-tiered error remediation:
- **Light**: Simple redirect (no visuals)
- **Medium**: Hint + visual scaffolding
- **Heavy**: Full demonstration with annotations

**Uses dynamic prefills** to guide Claude's JSON structure.

### 4. Godot Formatter
**Input**: `remediation.json`
**Output**: `final.json` - Godot-compatible schema
**Processing**: Item-by-item (one sequence at a time)
**Post-processing**: Metadata correction + BBCode formatting

Transforms to Godot schema with:
- `@type` annotations
- Workspace → tangibles structure
- Embedded visual effects as metadata.events
- Corrected mastery metadata
- BBCode-formatted fractions and vocabulary

## 🛠️ Key Features

### Dynamic Prefills
The system uses dynamic prefills to guide Claude's JSON generation:
- **Question Generator**: Includes goal_id and goal_text
- **Interaction Designer**: Includes question metadata
- **Remediation Generator**: Includes full sequence structure up to error path opening

Prefills ensure consistent JSON structure and reduce hallucination.

### Deterministic Post-Processing
After AI transformation, deterministic functions correct and enhance output:
- **Metadata Mapper** (`utils/metadata_mapper.py`): Corrects mastery tier/component/verbs based on difficulty and question type
- **BBCode Formatter** (`utils/bbcode_formatter.py`): Wraps fractions with `[fraction]` tags and adds `[vocab]` tags for vocabulary terms

### Item-by-Item Processing
Each step processes items individually (one API call per item) to:
- Enable better error handling
- Apply per-item post-processing
- Support prefill generation
- Maintain manageable context windows

### Module System
Content is organized by modules with:
- Decomposed learning goals
- Module-specific vocabulary
- Path variations (path a, b, c, etc.)

## 📋 Configuration

### Pipeline Configs
Located in `pipeline_runner.py` under `EXAMPLE_PIPELINES`:

```python
"full": [
    {
        "name": "Question Generator",
        "prompt_id": "question_generator",
        "processing_mode": "item_by_item",
        "item_key": "goals",
        "extract_fields": {
            "goal_id": "id",
            "goal": "text",
            "difficulty_level": "difficulty_level"
        },
        "collect_key": "questions",
        "output_file": "questions.json"
    },
    # ... more steps
]
```

### Prompt Files
Each prompt file (in `inputs/prompts/`) defines:
- `ROLE`: System instructions
- `DOCS`: Reference documentation to include
- `EXAMPLES`: Example inputs/outputs
- `INSTRUCTIONS`: Task-specific instructions
- `PREFILL`: Optional prefill template

Variables are substituted using `{variable_name}` syntax.

## 🧪 Testing

### Run Individual Step Tests
```bash
# Test each step independently
python tests/stepwise_tests/test_1_question_generator.py
python tests/stepwise_tests/test_2_interaction_designer.py
python tests/stepwise_tests/test_3_remediation_generator.py
python tests/stepwise_tests/test_4_godot_formatter.py
```

### Run Custom Pipelines
```python
from pipeline_runner import PipelineRunner

runner = PipelineRunner(
    module_number=2,
    path_letter="b",
    output_dir="outputs/test_run",
    verbose=True
)

result = runner.run_pipeline([
    {
        "name": "Question Generator",
        "prompt_id": "question_generator",
        "processing_mode": "item_by_item",
        "input_file": "inputs/modules/module2/decomposed_goals.json",
        "item_key": "goals",
        "extract_fields": {"goal_id": "id", "goal": "text"},
        "collect_key": "questions",
        "output_file": "questions.json"
    }
])
```

## 📊 Output Format

### Final Godot Schema
```json
{
  "@type": "SequencePool",
  "sequences": [
    {
      "@type": "Sequence",
      "metadata": {
        "@type": "SequenceMetadata",
        "problem_id": 1,
        "goal_id": 5,
        "mastery_tier": 2,
        "mastery_component": "PROCEDURAL",
        "mastery_verbs": ["APPLY"]
      },
      "steps": [
        {
          "@type": "Step",
          "dialogue": "Here's a bar divided into 4 parts.",
          "workspace": {
            "@type": "WorkspaceData",
            "tangibles": [...]
          }
        },
        {
          "@type": "Step",
          "prompt": {
            "@type": "Prompt",
            "text": "Shade [fraction numerator=3 denominator=4]three fourths[/fraction]",
            "validator": {...},
            "remediations": [
              {"@type": "Remediation", "id": "light", ...},
              {"@type": "Remediation", "id": "medium", ...},
              {"@type": "Remediation", "id": "heavy", ...}
            ]
          }
        }
      ]
    }
  ]
}
```

## 🔐 Security

**Never commit sensitive files:**
- `.env` (contains API keys)
- `outputs/` (generated content)
- `venv/` (virtual environment)

These are excluded in `.gitignore`.

## 📝 Development

### Experimenting with Prompts and Documentation

#### ✅ Safe to Modify

**Prompt Content** (`inputs/prompts/*.py`):
- `*_ROLE`: Change the persona or expertise level
- `*_INSTRUCTIONS`: Modify task instructions, add examples, change formatting requirements
- `*_DOCS`: Add/remove documentation files from the list
- `*_MODULE_REF`: Add/remove variables for reference from modules.py
- `*_EXAMPLES`: Add more examples or modify existing ones

**Documentation Files** (`inputs/docs/*.md`):
- Add new sections, update guidelines, refine language patterns
- These are included in prompts as reference material

**Module Data** (`inputs/modules/moduleN/`):
- `decomposed_goals.json`: Add/modify learning goals
- `modules.py`: Change fields

#### ⚠️ Be Careful With

**Variable Names** in prompts - must match pipeline config:
```python
# In prompt file
"{goal_id}"  # Variable name

# Must match in pipeline config
"extract_fields": {
    "goal_id": "id"  # ← Must be "goal_id"
}
```

**JSON Structure** in `*_PREFILL`:
- Keep proper indentation (2 spaces)
- Use `{{` and `}}` for literal braces (Python f-string escaping)
- Match the nesting level that Claude should continue from

**Field Names** in `extract_fields`:
- These pull data from input JSON - field must exist in source data

#### ❌ Do Not Change

**Core System Files** (unless you know what you're doing):
- `core/claude_client.py` - API wrapper
- `core/prompt_builder.py` - Variable substitution logic
- `pipeline_runner.py` - Orchestration logic (except EXAMPLE_PIPELINES)
- `utils/prefill_generator.py` - Prefill truncation logic

**Pipeline Config Structure**:
```python
{
    "name": "...",           # Display name - safe to change
    "prompt_id": "...",      # Must match function name in prompt_builder.py
    "processing_mode": "...", # "item_by_item" or "batch" - don't change unless needed
    "item_key": "...",       # Field name in input JSON - must match actual data
    "collect_key": "...",    # Field name in output JSON - don't change
    "output_file": "..."     # Can change if you want different output names
}
```

**Output Schema** (Godot format):
- `@type` annotations - required by Godot
- Field names in final.json - must match Godot's expectations

#### 🧪 How to Test Changes

**1. Test with Small Dataset**
Modify pipeline config to use `"limit": 2` for testing:
```python
{
    "name": "Question Generator",
    "limit": 2,  # Only process first 2 items
    ...
}
```

**2. Check Raw Outputs**
After running pipeline, check intermediate files:
```bash
outputs/pipeline_moduleN_pathX_TIMESTAMP/
├── question_generator/
│   ├── item_1_prompt.txt    # See actual prompt sent to Claude
│   └── item_1_raw.txt       # See raw Claude response
```

#### 💡 Best Practices

**When modifying prompts:**
1. **Start with examples** - Add/modify examples in `*_EXAMPLES` first
2. **Test incrementally** - Change one thing at a time
3. **Check raw outputs** - Look at `*_prompt.txt` and `*_raw.txt` files
4. **Use verbose mode** - Run with `--verbose` or check test outputs

**When modifying documentation:**
1. **Keep formatting consistent** - Use same markdown structure
2. **Test with actual prompts** - Docs are included in prompts via `*_DOCS`
3. **Update all references** - If you change a term, update everywhere.

#### 📝 Example: Modifying Question Generator Prompt

```python
# inputs/prompts/question_generator.py

# ✅ SAFE: Add more guidance
QUESTION_GENERATOR_INSTRUCTIONS = """
Generate 5 questions per learning goal.

NEW: For difficulty 0-2, use concrete examples.
NEW: For difficulty 3-4, use abstract reasoning.

Variables:
- {goal}: The learning goal text
...
"""

# ✅ SAFE: Add examples
QUESTION_GENERATOR_EXAMPLES = [
    "NEW EXAMPLE HERE..."
]

# ⚠️ CAREFUL: Changing variables
# Old: {goal}
# New: {goal_text}  ← Must update pipeline config too!

# ❌ DON'T: Change function names or imports
# These are referenced by prompt_builder.py
```

### Adding a New Pipeline Step

1. **Create prompt file** in `inputs/prompts/your_step.py`:
```python
YOUR_STEP_ROLE = "You are an expert..."
YOUR_STEP_DOCS = ["doc1.md", "doc2.md"]
YOUR_STEP_INSTRUCTIONS = """Task description..."""
YOUR_STEP_PREFILL = """{{
  "output": [
    {{
      "field": {variable},"""
```

2. **Register in prompt_builder.py**:
```python
def _your_step_config(self) -> Dict:
    from your_step import (
        YOUR_STEP_ROLE,
        YOUR_STEP_DOCS,
        YOUR_STEP_INSTRUCTIONS,
        YOUR_STEP_PREFILL
    )
    return {
        "role": YOUR_STEP_ROLE,
        "docs": YOUR_STEP_DOCS,
        "instructions": YOUR_STEP_INSTRUCTIONS,
        "prefill": YOUR_STEP_PREFILL
    }
```

3. **Add to pipeline config**:
```python
{
    "name": "Your Step",
    "prompt_id": "your_step",
    "processing_mode": "item_by_item",
    "item_key": "input_items",
    "extract_fields": {"var1": "field1"},
    "collect_key": "output_items",
    "output_file": "your_output.json"
}
```

### Adding Post-Processing

For deterministic transformations after AI generation:

1. **Create utility function** in `utils/your_processor.py`
2. **Add to pipeline_runner.py** in `run_step_item_by_item()`:
```python
if prompt_id == "your_step":
    from utils.your_processor import process_data
    parsed = process_data(parsed)
```