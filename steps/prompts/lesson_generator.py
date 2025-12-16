"""
lesson_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

LESSON_GENERATOR_PROMPT = Prompt(
    role="""You are an expert in teaching and pedagogical scaffolding, skilled at UX design, and a gifted script writer specializing in lesson development for children in grade 3""",

    instructions="""


Generate a lesson phase script for an educational module. Read and fully understand the <Module 1 Starter Pack VPSS - AI Ready.md>.  
The lesson should:
    - Teach the core concepts defined in learning goals.
    - Follow the entire pedagogical structure from the Phase Specifications of the <Module 1 Starter Pack VPSS - AI Ready.md>
    - Use vocabulary and visuals as defined in <Module 1 Starter Pack VPSS - AI Ready.md>

    INTERACTION DEFINITION:
  An interaction = visual demonstration + student input demand + response handling

  Field Definitions:
  - id: Unique identifier (e.g., "interaction_1", "interaction_2")
  - purpose: Learning goal for this interaction
  - interaction_description: Conceptual flow - what's shown, what's asked, how it's handled (not full script)
  - visual_context: General visual needs (e.g., "1x2 grid rectangle for halves", "hexagon with partition tool")


    The lesson phase is the main teaching section where core concepts are developed through structured discovery.








""",

    doc_refs=['Module 1 Starter Pack VPSS - AI Ready.md'],

    output_structure="""
 {
    "phase": "lesson",
    "interactions": [
      {
        "id": "interaction_1",
        "purpose": "Brief description of what this interaction aims to achieve",
        "interaction_description": "Detailed description of the interaction",
        "visual_context": "Description of the visuals used in this interaction (shapes, grids, tools, etc.)"
      },
      {
        "id": "interaction_2",
        "purpose": "Brief description of the learning goal for this interaction",
        "interaction_description": "Complete interaction script with all dialogue, prompts, and paths",
        "visual_context": "Visual elements displayed and their configurations"
      }
    ]
  }
""",

    prefill="""""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=20000,
    stop_sequences=[]
)
