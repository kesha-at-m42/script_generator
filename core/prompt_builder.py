"""
Prompt Builder - Centralized prompt management system

Each prompt has 5 components:
1. role - System role/identity for Claude
2. docs - Reference documentation to include
3. examples - Example outputs to guide Claude
4. structure - Required output structure/schema
5. instructions - What to do (the actual task)
"""

from pathlib import Path
from typing import Dict, List, Optional
import sys

# Add prompts directory to path for imports
prompts_path = Path(__file__).parent.parent / "inputs" / "prompts"
if str(prompts_path) not in sys.path:
    sys.path.insert(0, str(prompts_path))


class PromptBuilder:
    """Builds prompts from structured components"""
    
    def __init__(self):
        self.docs_dir = Path(__file__).parent.parent / "inputs" / "docs"
        self.prompts_dir = Path(__file__).parent.parent / "prompts"
    
    def build_prompt(self, prompt_id: str, variables: Dict = None) -> str:
        """Build a complete prompt from components"""
        
        # Load prompt config
        config = self._get_prompt_config(prompt_id)
        
        # Build sections
        sections = []
        
        # 1. Role (if present)
        if config.get("role"):
            sections.append(f"<role>\n{config['role']}\n</role>")
        
        # 2. Documentation references
        if config.get("docs"):
            docs_content = self._load_docs(config["docs"])
            sections.append(docs_content)
        
        # 3. Examples
        if config.get("examples"):
            examples_content = self._format_examples(config["examples"])
            sections.append(f"<examples>\n{examples_content}\n</examples>")
        
        # 4. Output structure
        if config.get("structure"):
            sections.append(f"<required_output_format>\n{config['structure']}\n</required_output_format>")
        
        # 5. Instructions (the actual task)
        instructions = config.get("instructions", "")
        if variables:
            instructions = instructions.format(**variables)
        sections.append(instructions)
        
        return "\n\n".join(sections)
    
    def _get_prompt_config(self, prompt_id: str) -> Dict:
        """Get prompt configuration by ID"""
        
        configs = {
            "question_generator": self._question_generator_config(),
            "interaction_designer": self._interaction_designer_config(),
            "remediation_generator": self._remediation_generator_config(),
            "godot_formatter": self._godot_formatter_config(),
        }
        
        return configs.get(prompt_id, {})
    
    def _load_docs(self, doc_refs: List[str]) -> str:
        """Load documentation files"""
        sections = []
        
        for doc_ref in doc_refs:
            if isinstance(doc_ref, dict):
                # Embedded doc content
                title = doc_ref.get("title", "Reference")
                content = doc_ref.get("content", "")
                sections.append(f"<{title.lower().replace(' ', '_')}>\n{content}\n</{title.lower().replace(' ', '_')}>")
            else:
                # File reference
                filepath = self.docs_dir / doc_ref
                if filepath.exists():
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    tag = filepath.stem
                    sections.append(f"<{tag}>\n{content}\n</{tag}>")
        
        return "\n\n".join(sections)
    
    def _format_examples(self, examples: List[Dict]) -> str:
        """Format example outputs"""
        formatted = []
        
        for i, example in enumerate(examples, 1):
            example_text = f"Example {i}:\n"
            if "description" in example:
                example_text += f"{example['description']}\n\n"
            example_text += example.get("output", "")
            formatted.append(example_text)
        
        return "\n\n---\n\n".join(formatted)
    
    # ========================================================================
    # PROMPT CONFIGURATIONS
    # ========================================================================
    
    def _question_generator_config(self) -> Dict:
        """Question Generator prompt configuration"""
        from question_generator import (
            QUESTION_GENERATOR_ROLE,
            QUESTION_GENERATOR_DOCS,
            QUESTION_GENERATOR_EXAMPLES,
            QUESTION_GENERATOR_STRUCTURE,
            QUESTION_GENERATOR_INSTRUCTIONS
        )
        
        return {
            "role": QUESTION_GENERATOR_ROLE,
            "docs": QUESTION_GENERATOR_DOCS,
            "examples": QUESTION_GENERATOR_EXAMPLES,
            "structure": QUESTION_GENERATOR_STRUCTURE,
            "instructions": QUESTION_GENERATOR_INSTRUCTIONS
        }
    
    def _question_generator_config_OLD(self) -> Dict:
        """OLD Question Generator prompt configuration - DEPRECATED"""
        return {
            "role": "You are an expert educational content designer specializing in elementary mathematics. You create questions that are developmentally appropriate, clear, and aligned with learning objectives.",
            
            "docs": [
                "difficulty_levels.md",
                "question_types.md",
            ],
            
            "examples": [
                {
                    "description": "Sample questions for Goal: Students can partition shapes into equal parts (showing good variety)",
                    "output": """{
  "questions": [
    {
      "id": 1,
      "question_text": "Click once in the middle to divide the bar into 2 equal parts.",
      "interaction_type": "Click",
      "difficulty_level": 0,
      "question_type": "procedural",
      "cognitive_verb": "divide",
      "visual_context": "A horizontal rectangular bar, unpartitioned, solid color",
      "correct_answer": "Click once in the center to create 2 equal sections",
      "explanation": "This question teaches the most basic partitioning skill - creating two equal parts by finding the midpoint. It's procedural and concrete, requiring only one action to successfully partition a whole into halves.",
      "vocabulary_reinforced": ["partition", "equal parts"]
    },
    {
      "id": 2,
      "question_text": "Which circle shows 4 equal parts?",
      "interaction_type": "Multiple Choice",
      "difficulty_level": 2,
      "question_type": "conceptual",
      "cognitive_verb": "identify",
      "visual_context": "Three circles displayed: Circle A divided into 4 equal wedges, Circle B divided into 4 unequal wedges, Circle C divided into 3 equal parts",
      "correct_answer": "Circle A (the one with 4 equal wedges)",
      "explanation": "This question builds conceptual understanding by requiring students to distinguish between equal and unequal partitioning while also verifying the correct count. The circle shape adds complexity compared to rectangles, and the multiple distractors require careful visual discrimination.",
      "vocabulary_reinforced": ["equal parts"]
    },
    {
      "id": 3,
      "question_text": "A rectangular garden needs to be divided into 6 equal sections for planting different vegetables. Show how you would divide it.",
      "interaction_type": "Drag and Drop",
      "difficulty_level": 4,
      "question_type": "transfer",
      "cognitive_verb": "apply",
      "visual_context": "A large rectangle representing a garden, with draggable dividing lines (5 lines available) that can be positioned horizontally or vertically",
      "correct_answer": "Position 5 lines to create 6 equal sections (e.g., 2 rows × 3 columns or 3 rows × 2 columns)",
      "explanation": "This transfer question applies partitioning to a real-world scenario requiring spatial reasoning and strategic planning. Students must determine that creating 6 equal parts requires 5 dividing lines and discover that multiple valid arrangements exist (2×3 or 3×2 or 6×1), promoting flexible thinking about equal partitioning in context.",
      "vocabulary_reinforced": ["equal parts", "partition", "whole"]
    }
  ]
}"""
                }
            ],
            
            "structure": """{
  "questions": [
    {
      "id": <sequential number starting at 1>,
      "question_text": "<clear, age-appropriate question text>",
      "interaction_type": "<Multiple Choice|Multiple Select|Click|Shade|Drag and Drop|Input|True/False>",
      "difficulty_level": <integer 0-4>,
      "question_type": "<procedural|conceptual|transfer>",
      "cognitive_verb": "<main action verb from appropriate category>",
      "visual_context": "<description of what the student sees>",
      "correct_answer": "<expected correct answer or action>",
      "answer_choices": ["<option 1>", "<option 2>", "<option 3>", "<option 4>"],
      "explanation": "<how this question teaches the learning goal>",
      "vocabulary_reinforced": ["<term1>", "<term2>"]
    }
  ]
}

Note: answer_choices is only required for Multiple Choice and Multiple Select questions.

Return ONLY valid JSON.""",
            
            "instructions": """You are generating questions for this SPECIFIC learning goal:

GOAL ID: {goal_id}
GOAL: {goal_text}

VOCABULARY TERMS for this goal:
{vocabulary}

AVAILABLE VISUALS:
{visuals}

EXAMPLE QUESTIONS FROM CURRICULUM:
{examples}

Generate {num_questions} DIFFERENT questions that teach this learning goal for grade {grade_level} students.

CRITICAL - FOLLOW THE EXAMPLES CLOSELY:
The example questions above show the STYLE and APPROACH that works for this goal.
- Use similar question structures but vary the numbers/specifics
- Follow the same interaction patterns shown in examples
- Keep the same level of complexity and language
- Create variations, NOT exact copies

ENSURE VARIETY ACROSS ALL {num_questions} QUESTIONS:
1. Use DIFFERENT interaction types (vary as much as possible, minimal repeats)
   Available: Multiple Choice, Multiple Select, Click, Shade, Drag and Drop, Input, True/False
2. Use DIFFERENT difficulty levels following this distribution:
   - 1-2 questions at Level 0-1 (support/confidence building)
   - 2-3 questions at Level 2 (baseline mastery) ← FOCUS HERE
   - 2-3 questions at Level 3 (stretch/deeper) ← FOCUS HERE  
   - 1-2 questions at Level 4 (challenge/enrichment)
3. Use DIFFERENT question types: Mix procedural, conceptual, and transfer
4. Use DIFFERENT visual contexts: Vary the number of bars, number of parts (2,3,4,6,8), shading patterns
5. Use DIFFERENT cognitive verbs: partition, identify, recognize, shade, count, compare, apply, etc.
6. Create DIFFERENT scenarios: Don't repeat the same setup or wording

REQUIREMENTS FOR EACH QUESTION:
1. question_text: Write a clear, age-appropriate question (follow example style)
   - For Multiple Choice: Include all answer options in the question_text or answer choices field
2. interaction_type: Choose from the list above (vary as much as possible)
3. difficulty_level: Follow the distribution above - prioritize Levels 2 and 3
4. question_type: Vary between procedural, conceptual, and transfer
5. cognitive_verb: Use appropriate action verb that matches the question type
6. visual_context: Describe what visual the student sees using ONLY rectangle bars
   - For Multiple Choice: Describe all answer options/bars shown
7. correct_answer: State what the correct answer or action is
   - For Multiple Choice: Clearly identify which option is correct
8. explanation: Explain HOW this specific question teaches the learning goal (2-3 sentences)
9. vocabulary_reinforced: List which vocabulary terms from above are used/reinforced
10. answer_choices: (For Multiple Choice only) List all answer options

EXAMPLE OF GOOD VARIETY for "parts must be equal for unit fractions":
- Question 1: "Click on the bar that can represent a unit fraction" (Click, Level 3, conceptual)
  Visual: Shows 3 bars with unequal parts and 1 bar with equal parts
- Question 2: "Click on the bar that represents 1/4" (Click, Level 2, conceptual)  
  Visual: Two bars with 1 part shaded of 4 equal parts, one bar with 1 part shaded of 4 unequal parts
- Question 3: "Why can't this represent a unit fraction?" (Multiple Choice, Level 3, conceptual)
  Visual: Bar divided into unequal parts with one section shaded, options explain why

VISUAL CONSTRAINTS:
- Use ONLY rectangle bars (horizontal or vertical orientation)
- Bars can be divided into 2, 3, 4, 6, or 8 parts
- Parts can be equal or unequal (depending on the question)
- Parts can be shaded or unshaded
- Multiple bars can be shown for comparison questions"""
        }
    
    def _interaction_designer_config(self) -> Dict:
        """Interaction Designer prompt configuration"""
        from interaction_designer import (
            INTERACTION_DESIGNER_ROLE,
            INTERACTION_DESIGNER_DOCS,
            INTERACTION_DESIGNER_EXAMPLES,
            INTERACTION_DESIGNER_STRUCTURE,
            INTERACTION_DESIGNER_INSTRUCTIONS
        )
        
        return {
            "role": INTERACTION_DESIGNER_ROLE,
            "docs": INTERACTION_DESIGNER_DOCS,
            "examples": INTERACTION_DESIGNER_EXAMPLES,
            "structure": INTERACTION_DESIGNER_STRUCTURE,
            "instructions": INTERACTION_DESIGNER_INSTRUCTIONS
        }
    
    def _interaction_designer_config_OLD(self) -> Dict:
        """OLD Interaction Designer prompt configuration - DEPRECATED"""
        return {
            "role": "You are an expert in designing interactive educational experiences. You create clear visual flows and interaction mechanics WITHOUT writing dialogue or validation logic yet.",
            
            "docs": [
                "visual_guide.md",
            ],
            
            "examples": [
                {
                    "description": "Sample interaction design for fraction identification",
                    "output": """{
  "sequences": [
    {
      "problem_id": 1,
      "goal": "Identify unit fractions",
      "verb": "identify",
      "difficulty": 1,
      "main_sequence": [
        {
          "step_id": "1.1",
          "dialogue_placeholder": "OPENING [context: introduce visual]",
          "visuals": [
            {
              "id": "circle_1",
              "type": "circle",
              "description": "Circle 200px diameter, divided into 4 equal wedges, top-right wedge shaded blue"
            }
          ],
          "animations": [],
          "student_action": null
        },
        {
          "step_id": "1.2",
          "dialogue_placeholder": "OPENING [context: pose question]",
          "visuals": [
            {
              "id": "buttons",
              "type": "multiple_choice_buttons",
              "description": "Four buttons showing 1/2, 1/3, 1/4, 1/8"
            }
          ],
          "student_action": {
            "type": "button_click",
            "expected": "1/4",
            "description": "Click the correct fraction"
          }
        }
      ]
    }
  ]
}"""
                }
            ],
            
            "structure": """{
  "sequences": [
    {
      "problem_id": <number>,
      "goal": "<learning goal>",
      "verb": "<cognitive verb>",
      "difficulty": <0-4>,
      "main_sequence": [
        {
          "step_id": "<problem_id>.<step_number>",
          "dialogue_placeholder": "<STANDARD_TYPE> [context: ...]",
          "visuals": [
            {
              "id": "<unique_id>",
              "type": "<visual_type>",
              "description": "<detailed description with dimensions, colors, states>"
            }
          ],
          "animations": [
            {
              "visual_id": "<id>",
              "type": "<animation_type>",
              "description": "<what happens>"
            }
          ],
          "student_action": {
            "type": "<interaction_type>",
            "expected": "<expected_outcome>",
            "description": "<what student should do>"
          } | null
        }
      ]
    }
  ]
}

Return ONLY valid JSON.""",
            
            "instructions": """Design interactive visual sequences for these educational questions.

<questions>
{learning_goals_data}
</questions>

For each question, design the interaction flow:
- What visuals appear (with specific dimensions, colors, states)
- What students see and do
- What animations might happen
- Use visuals and animations from the visual guide

DO NOT:
- Write actual dialogue (use placeholders like "OPENING [context: ...]")
- Design validation logic (that's a separate step)
- Create error remediation (that's a separate step)

FOCUS ON:
- Clear visual descriptions
- Logical interaction flow
- Appropriate visual types for the learning goal"""
        }
    
    def _remediation_generator_config(self) -> Dict:
        """Configuration for remediation generation prompt"""
        from remediation_generator import (
            REMEDIATION_GENERATOR_ROLE,
            REMEDIATION_GENERATOR_INSTRUCTIONS,
            REMEDIATION_GENERATOR_STRUCTURE
        )
        
        return {
            "role": REMEDIATION_GENERATOR_ROLE,
            "docs": [
                "remediation_system.md"  # Reference documentation for error patterns
            ],
            "examples": [],  # Examples are embedded in the reference doc
            "structure": REMEDIATION_GENERATOR_STRUCTURE,
            "instructions": REMEDIATION_GENERATOR_INSTRUCTIONS
        }
    
    def _godot_formatter_config(self) -> Dict:
        """Godot Formatter prompt configuration"""
        from godot_formatter import (
            GODOT_FORMATTER_ROLE,
            GODOT_FORMATTER_DOCS,
            GODOT_FORMATTER_EXAMPLES,
            GODOT_FORMATTER_STRUCTURE,
            GODOT_FORMATTER_INSTRUCTIONS
        )
        
        return {
            "role": GODOT_FORMATTER_ROLE,
            "docs": GODOT_FORMATTER_DOCS,
            "examples": GODOT_FORMATTER_EXAMPLES,
            "structure": GODOT_FORMATTER_STRUCTURE,
            "instructions": GODOT_FORMATTER_INSTRUCTIONS
        }
    
    def build_remediation_generator_prompt(self, interactions_context: str) -> str:
        """Build prompt for remediation generation"""
        return self.build_prompt(
            "remediation_generator",
            {"interactions_context": interactions_context}
        )


# Test it
if __name__ == "__main__":
    builder = PromptBuilder()
    
    print("=" * 70)
    print("Testing PromptBuilder")
    print("=" * 70)
    
    print("\n1. Question Generator Prompt")
    print("-" * 70)
    
    prompt = builder.build_prompt(
        "question_generator",
        {
            "num_questions": 5,
            "grade_level": 3,
            "learning_goals": "- Students can partition shapes\n- Students can identify fractions"
        }
    )
    
    print(f"Length: {len(prompt)} chars")
    print(f"Preview (first 500 chars):\n{prompt[:500]}...")
    
    # Test interaction designer prompt
    print("\n2. Interaction Designer Prompt")
    print("-" * 70)
    
    prompt = builder.build_prompt(
        "interaction_designer",
        {
            "learning_goals_data": "[question data here]"
        }
    )
    
    print(f"Length: {len(prompt)} chars")
    print(f"Preview (first 500 chars):\n{prompt[:500]}...")
    
    print("\n" + "=" * 70)
    print("✓ PromptBuilder working!")
