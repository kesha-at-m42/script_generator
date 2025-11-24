# Steps Directory

All pipeline steps organized by type.

## Structure

```
steps/
├── prompts/              # AI Steps (call Claude API)
│   ├── interaction_generator.py
│   ├── warmup_generator.py
│   └── ...
│
└── formatting/           # Deterministic Steps (no API calls)
    ├── script_formatter.py
    └── ...
```

## AI Steps (prompts/)

Define prompts that call Claude API. Each file should export a Prompt object:

```python
from core.prompt_builder import Prompt

INTERACTION_GENERATOR_PROMPT = Prompt(
    role="You are an educational content creator",
    instructions="Generate interactions...",
    # ...
)
```

## Formatting Steps (formatting/)

Deterministic post-processing functions. Each file contains functions:

```python
def format_interactions_to_markdown(input_data, module_number=None, path_letter=None):
    """Convert interactions to markdown"""
    # Your formatting logic
    return formatted_output
```

Functions in this folder automatically appear in the UI dropdown!
