"""
Warmup Generator Prompt - Generates warmup phase scripts for educational modules
"""

# Import will work because prompt_builder.py adds this directory to sys.path
import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

WARMUP_GENERATOR_PROMPT = Prompt(
    role="You are an expert educational script writer specializing in warmup activities and familiar with interactive design.",

    instructions="""Generate a warmup phase script for an educational module. The warmup should:

    - Activate prior knowledge relevant to the lesson. These are the learning goals for the module: {learning_goals}
    - Create engagement and build student confidence
    - Include 2-4 interactions based on what visuals are available in the module: <visuals>
    - Use appropriate vocabulary and visuals as defined in the module data here {{phases[0]}}. Use the vocabulary naturally. No formal introduction yet.

      INTERACTION DEFINITION:
  An interaction = visual demonstration + student input demand + response handling

  Field Definitions:
  - id: Unique identifier (e.g., "interaction_1", "interaction_2")
  - purpose: Learning goal for this interaction (1-2 sentences)
  - interaction_description: Conceptual flow - what's shown, what's asked, how it's handled (not full script)
  - visual_context: General visual needs (e.g., "grids showing equal parts", "rectangle with partitioning tool")

  Requirements:
  - Number of interactions should match interaction_count from phase data
  - Keep it high-level and conceptual - details will be refined in next step

    The warmup phase prepares students for the main lesson content without teaching new core concepts.
    Focus on activating what students already know and creating curiosity for what's to come.""",

    doc_refs=["visuals.md"],
      output_structure="""

  {
    "phase": "warm_up",
    "interactions": [
      {
        "id": "interaction_1",
        "purpose": "Brief description of what this interaction aims to achieve",
        "interaction_description": "Detailed description of the interaction ",
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
    examples=[],
    module_ref={"phases[0]:phases.0", "learning_goals"},
    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
