"""
test_new_prompt - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

TEST_NEW_PROMPT_PROMPT = Prompt(
    role="""Lorem ipsum dolor sit amet, consectetur adipiscing elit.""",

    instructions="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
""",

    doc_refs=[],

    output_structure="""
{
  "field": "value"
}
""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
