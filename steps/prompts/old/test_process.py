"""
test_process - Test prompt for batch processing
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

TEST_PROCESS_PROMPT = Prompt(
    role="""You are a helpful assistant that processes template data.""",

    instructions="""
You are processing template {template_id}.

Template details:
- Problem type: {problem_type}
- Mastery verb: {goal_decomposition__mastery_verb}

Return a simple JSON object with the following structure:
{{
  "template_id": "{template_id}",
  "processed": true,
  "problem_type": "{problem_type}",
  "mastery_verb": "{goal_decomposition__mastery_verb}"
}}
""",

    doc_refs=[],

    output_structure="""
Return valid JSON only.
""",

    prefill="",

    examples=[],

    module_ref={{}},

    template_ref={{}},

    cache_docs=False,
    cache_ttl="5m",
    temperature=1.0,
    max_tokens=2000,
    stop_sequences=[]
)
