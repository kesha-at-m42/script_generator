"""
problem_generator - AI Prompt
"""

import sys
from pathlib import Path

# Add parent directory to path to find core module
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.prompt_builder import Prompt

PROBLEM_GENERATOR_PROMPT = Prompt(
    role="""You are an expert educational content generator specializing in creating diverse,
high-quality practice problems for grade 3 mathematics students. You excel at taking problem
templates and generating specific, varied problem instances that maintain pedagogical quality
while maximizing engagement and coverage.""",

    instructions="""
## TASK

You will receive a problem template that defines a specific type of mathematical interaction.
Your task is to generate concrete problem instances that create meaningful variation across:
1. **Parameter values** (fractions tested)
2. **Mastery tiers** (difficulty levels 0-4)

## INPUT STRUCTURE

The problem template contains:
- **template_id**: Unique identifier for this template type
- **problem_type**: Type of cognitive action (identify, compare, create, apply)
- **workspace_description**: What the student sees on screen
- **prompt_examples**: Sample variations of how to ask the question
- **action_description**: What the student does to solve (maps to allowed actions from visuals.md)
- **parameter_coverage**: The mathematical parameters to vary (fractions, denominators, etc.)

## GENERATION STRATEGY

### Axes of Variation

**1. Parameter Coverage (Horizontal Variation)**
- Generate problems covering the range of parameter values
- Use fraction values from parameter_coverage
- Track in **variables_used** field (use "fractions" as key when possible)

**2. Mastery Tier (Vertical Variation)**
- Generate problems at different difficulty levels: support, confidence, baseline, stretch, challenge
- Use <difficulty_levels> guidance to design appropriate complexity.

### Mapping to Allowed Actions

Use **visuals.md** to ensure workspace and actions align with allowed student actions

## OUTPUT REQUIREMENTS

For each problem instance, generate:

**1. problem_instance_id:** Sequential number (1, 2, 3, ...)

**2. template_id:** Copy from template

**3. problem_type:** Copy from template

**4. action_description:** Map from template's action_description to allowed actions in visuals.md

**5. prompt:** Student-facing question based on prompt_examples

**6. workspace_description:** Visual setup based on workspace_description, aligned with visuals.md

**7. mastery_tier:** Single string (support, confidence, baseline, stretch, challenge) - use as axis of variation

**8. variables_used:** Fraction values tested (use "fractions" as key when possible)

**9. application_context:** (ONLY for "apply" problem_type with narrative context)

## QUALITY CHECKLIST

**Coverage:**
- Problems span multiple mastery tiers (not all at same difficulty)
- Parameter values are well-distributed
- Workspace descriptions match mastery tier complexity

**Alignment:**
- All prompts align with the template's **problem_type**
- Workspace descriptions use allowed configurations from **visuals.md**
- Actions described match allowed student actions (Select, Point, Label)
- Language is grade 3 appropriate

**Variation:**
- Prompts vary in phrasing while maintaining the same task
- Mastery tiers create meaningful difficulty progression
- No two problems are identical

Generate problem instances NOW with maximum variation and quality!
""",

    doc_refs=["difficulty_levels.md", "visuals.md"],

    output_structure="""
[
  {
    "problem_instance_id": 1,
    "template_id": "4001",
    "problem_type": "identify",
    "action_description": "Point at tick marks",
    "prompt": "Point to one-third on the number line.",
    "workspace_description": "Number line from 0 to 1 with tick marks at 0, 1/3, 2/3, 1. Only endpoints labeled.",
    "mastery_tier": "support",
    "variables_used": {
      "fractions": ["1/3"]
    }
  },
  {
    "problem_instance_id": 2,
    "template_id": "4002",
    "problem_type": "apply",
    "action_description": "Label tick marks by dragging",
    "prompt": "Maya ate 1/4 of a pizza. Show where 1/4 is on the number line.",
    "workspace_description": "Number line from 0 to 1 with tick marks at 0, 1/4, 1/2, 3/4, 1. Only endpoints labeled.",
    "mastery_tier": "baseline",
    "variables_used": {
      "fractions": ["1/4"]
    },
    "application_context": "Maya ate 1/4 of a pizza"
  }
]
""",

    prefill="""[{"problem_instance_id":""",

    examples=[],

    module_ref={},

    template_ref={},

    cache_docs=True,
    cache_ttl="5m",
    temperature=1,
    max_tokens=18000,
    stop_sequences=[]
)
