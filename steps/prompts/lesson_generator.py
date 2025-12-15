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
    role="""You are an expert educational script writer specializing in lesson development and familiar with interactive design patterns.""",

    instructions="""
Generate a lesson phase script for an educational module. The lesson should:

    - Teach the core concepts defined in learning goals: {learning_goals}
    - Follow the three-section pedagogical structure from the <starter_pack>
    - Use vocabulary and visuals as defined in the lesson phase data: {phase}
    - Include interactions based on what visuals are available in the module: <visuals>
    - Address misconceptions: {misconceptions}

    LESSON STRUCTURE (from starter pack):

    Section 1: Grid Mastery with Fraction Words (No Notation)
      - Critical Moment 1: Introducing "The Whole"
      - Critical Moment 2: Creating and Naming with Words (Halves, Fourths)
      - Critical Moment 3: Pattern Extension (Thirds, Sixths, Eighths)

    Section 2: Mathematical Notation Bridge
      - Critical Moment 4: Introduce notation as written form of fraction words

    Section 3: Hexagon Extension
      - Critical Moment 5: Shape Transfer with Complete Naming

    INTERACTION DEFINITION:
  An interaction = visual demonstration + student input demand + response handling

  Field Definitions:
  - id: Unique identifier (e.g., "interaction_1", "interaction_2")
  - purpose: Learning goal for this interaction
  - interaction_description: Conceptual flow - what's shown, what's asked, how it's handled (not full script)
  - visual_context: General visual needs (e.g., "1x2 grid rectangle for halves", "hexagon with partition tool")

  Requirements:
  - Generate interactions covering all the Critical Moments
  - Include vocabulary staging at key moments based of how it is defined in phase.
  - Emphasize partition → shade → name pattern throughout

    The lesson phase is the main teaching section where core concepts are developed through structured discovery.
""",

    doc_refs=['visuals.md', 'starter_pack.md'],

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

    module_ref={'phase': 'phases.1', 'learning_goals': 'learning_goals', 'vocabulary': 'vocabulary', 'misconceptions': 'misconceptions'},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=20000,
    stop_sequences=[]
)
