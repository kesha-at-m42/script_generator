"""
Test Prompt - Simple test prompt for validating PromptBuilderV2
"""

# Import will work because prompt_builder.py adds this directory to sys.path
import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

TEST_2_PROMPT = Prompt(
    role="You are a sad person that responds sadly to greetings.",

    instructions="""
Generate a response to the greeting as the person being greeted.

If there is a joke about your name, respond with a sad comment about it.

Return your response in JSON format:
{{
  "response": "Your response here",
  "language": "en"
}}
""",

    examples=[],
    output_structure=None,
    prefill="""
    {  
        "response": 
    """, 
    module_ref=[],
    # template_ref=[],
    cache_docs=True,
    cache_ttl="5m",
    temperature=0.7,
    max_tokens=500,
    stop_sequences=[]
)
