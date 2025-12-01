"""
script_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

SCRIPT_GENERATOR_PROMPT = Prompt(
    role="""You are an educator.""",

    instructions="""

Use the guidance in the starter pack to write an educational instructional script. It should have different phases. Start with warm up, then lesson.

""",

    doc_refs=['Module 1 Starter Pack VPSS.md'],

    output_structure="""



""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=16000,
    stop_sequences=[]
)
