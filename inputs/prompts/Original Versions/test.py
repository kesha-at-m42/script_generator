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

TEST_PROMPT = Prompt(
    role="You are a funny and helpful assistant that generates greetings.",

    instructions="""
Generate a friendly greeting for {name}.

The greeting should be warm and welcoming. You should make a joke about their name as well.

Return your response in JSON format:
{{
  "greeting": "Your greeting here",
  "language": "en"
}}
""",

    doc_refs=["visuals.md", "difficulty_levels.md"],
    examples=[],
    output_structure=None,
    prefill="""
    {  
        "greeting": 
    """, 
    module_ref=[],
    # template_ref=[],
    cache_docs=True,
    cache_ttl="5m",
    temperature=0.7,
    max_tokens=500,
    stop_sequences=[]
)
