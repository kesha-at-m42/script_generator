"""
new_prompt - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

NEW_PROMPT_PROMPT = Prompt(
    role="""test""",

    instructions="""
test
""",

    doc_refs=['test'],

    output_structure="""

""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1.0,
    max_tokens=8000,
    stop_sequences=[]
)
