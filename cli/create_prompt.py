#!/usr/bin/env python3
"""
CLI script to generate a new prompt draft.
Usage: python cli/create_prompt.py <prompt_name>
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def create_prompt_draft(prompt_name: str):
    """Generate a new prompt file with placeholder content"""

    # Convert to snake_case
    prompt_name = prompt_name.lower().replace(" ", "_").replace("-", "_")

    # Create filename and constant name
    filename = f"{prompt_name}.py"
    constant_name = f"{prompt_name.upper()}_PROMPT"
    filepath = project_root / "steps" / "prompts" / filename

    # Check if file already exists
    if filepath.exists():
        print(f"Error: {filename} already exists")
        return False

    # Template with lorem ipsum placeholders
    template = f'''"""
{prompt_name} - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

{constant_name} = Prompt(
    role="""Lorem ipsum dolor sit amet, consectetur adipiscing elit.""",

    instructions="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
""",

    doc_refs=[],

    output_structure="""
{{
  "field": "value"
}}
""",

    prefill="""""",

    examples=[],

    module_ref={{}},

    template_ref={{}},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
'''

    # Write file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"Created: {filepath.relative_to(project_root)}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        prompt_name = input("Prompt name: ").strip()
    else:
        prompt_name = sys.argv[1]

    if not prompt_name:
        print("Error: Prompt name is required")
        sys.exit(1)

    create_prompt_draft(prompt_name)


if __name__ == "__main__":
    main()
