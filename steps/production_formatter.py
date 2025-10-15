"""
Production Formatter - Converts nested sequences to flat production-ready structure
Maps to Godot SequenceSchema format
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step


class ProductionFormatter(Step):
    """Formats sequences into production-ready flat structure (no AI)"""
    
    def __init__(self):
        super().__init__(name="Production Formatter", prompt_id="production_formatter")
    
    def execute(self, input_data, **kwargs):
        """Convert nested sequences to flat steps[] structure"""
        
        if isinstance(input_data, dict):
            sequences = input_data.get("sequences", [])
        elif isinstance(input_data, list):
            sequences = input_data
        else:
            sequences = []
        
        print(f"  🔄 Converting {len(sequences)} sequences to production format...")
        
        production_sequences = []
        for seq in sequences:
            production_seq = self._convert_sequence(seq)
            production_sequences.append(production_seq)
        
        print(f"  ✓ Converted to production format")
        
        return {
            "sequences": production_sequences,
            "total_problems": len(production_sequences)
        }
    
    def _convert_sequence(self, sequence: dict) -> dict:
        """Convert one sequence from nested to flat structure"""
        
        # Extract metadata
        problem_id = sequence.get("problem_id")
        goal = sequence.get("goal", "")
        verb = sequence.get("verb", "")
        difficulty = sequence.get("difficulty")
        main_sequence = sequence.get("main_sequence", [])
        
        # Flatten to steps[] array
        steps = []
        
        for seq_step in main_sequence:
            # Convert each main sequence step to production steps
            production_steps = self._convert_step(seq_step)
            steps.extend(production_steps)
        
        return {
            "problem_id": problem_id,
            "goal": goal,
            "verb": verb,
            "difficulty": difficulty,
            "steps": steps
        }
    
    def _convert_step(self, step: dict) -> list:
        """Convert one nested step to flat production step(s)"""
        
        step_id = step.get("step_id")
        guide_says = step.get("guide_says", "")
        visuals = step.get("visuals", [])
        animations = step.get("animations", [])
        student_action = step.get("student_action")
        
        production_steps = []
        
        # Step 1: Dialogue + visuals (presentation step)
        if guide_says or visuals or animations:
            presentation_step = {
                "dialogue": guide_says or None,
                "audio_dir": None,  # To be filled in production
                "workspace": self._create_workspace(visuals),
                "scene": None  # "Classroom", "Workspace", etc.
            }
            
            # Add animations to workspace if present
            if animations:
                if presentation_step["workspace"] is None:
                    presentation_step["workspace"] = {}
                presentation_step["workspace"]["animations"] = self._format_animations(animations)
            
            production_steps.append(presentation_step)
        
        # Step 2: Student interaction (if present)
        if student_action:
            interaction_step = self._create_interaction_step(student_action)
            production_steps.append(interaction_step)
        
        return production_steps
    
    def _create_interaction_step(self, student_action: dict) -> dict:
        """Create a step with prompt and remediations"""
        
        description = student_action.get("description", "")
        validation = student_action.get("validation", {})
        
        # Build the prompt object
        prompt = {
            "text": description,
            "tool": None,  # e.g., "fraction_selector", "shape_partitioner"
            "validator": None,  # Validation rules
            "choices": None,  # For multiple choice
            "remediations": [],
            "on_correct": None
        }
        
        # Add success paths
        success_first = validation.get("success_first_attempt", {})
        success_after = validation.get("success_after_error", {})
        
        if success_first:
            prompt["on_correct"] = {
                "dialogue": success_first.get("guide_says", ""),
                "audio_dir": None
            }
        
        # Add error remediations
        errors = validation.get("errors", {})
        for error_name, error_data in errors.items():
            remediations = error_data.get("remediations", [])
            
            for rem in remediations:
                remediation = {
                    "id": error_name,
                    "step": {
                        "dialogue": rem.get("guide_says", ""),
                        "audio_dir": None
                    }
                }
                
                # Add animations if present
                animations = rem.get("animations", [])
                if animations:
                    remediation["step"]["workspace"] = {
                        "animations": self._format_animations(animations)
                    }
                
                prompt["remediations"].append(remediation)
        
        return {
            "dialogue": None,  # No dialogue on interaction step (it's in the prompt)
            "audio_dir": None,
            "workspace": None,
            "prompt": prompt,
            "scene": None
        }
    
    def _create_workspace(self, visuals: list) -> dict:
        """Create workspace object from visuals"""
        if not visuals:
            return None
        
        workspace = {
            "visuals": []
        }
        
        for visual in visuals:
            workspace["visuals"].append({
                "id": visual.get("id"),
                "type": visual.get("type"),
                "description": visual.get("description"),
                "state": visual.get("state", "default")
            })
        
        return workspace
    
    def _format_animations(self, animations: list) -> list:
        """Format animations for workspace"""
        formatted = []
        
        for anim in animations:
            formatted.append({
                "visual_id": anim.get("visual_id"),
                "type": anim.get("type"),
                "description": anim.get("description"),
                "duration": anim.get("duration", 1000),
                "params": anim.get("params", {})
            })
        
        return formatted


# Test
if __name__ == "__main__":
    import json
    
    print("Testing ProductionFormatter...\n")
    
    # Sample nested structure
    nested_data = {
        "sequences": [{
            "problem_id": 1,
            "goal": "Identify unit fractions",
            "verb": "identify",
            "difficulty": 1,
            "main_sequence": [
                {
                    "step_id": "1.1",
                    "guide_says": "Look at this circle divided into 4 parts.",
                    "visuals": [
                        {
                            "id": "circle_1",
                            "type": "circle",
                            "description": "Circle divided into 4 equal wedges, 1 shaded"
                        }
                    ],
                    "student_action": None
                },
                {
                    "step_id": "1.2",
                    "guide_says": None,
                    "visuals": [],
                    "student_action": {
                        "type": "multiple_choice",
                        "description": "Which fraction shows the shaded part?",
                        "validation": {
                            "success_first_attempt": {
                                "guide_says": "Perfect! You got it right away."
                            },
                            "success_after_error": {
                                "guide_says": "Nice work sticking with it."
                            },
                            "errors": {
                                "selected_1/2": {
                                    "remediations": [
                                        {
                                            "attempt": 1,
                                            "guide_says": "Count the sections with me.",
                                            "animations": [
                                                {
                                                    "visual_id": "circle_1",
                                                    "type": "highlight_sequence",
                                                    "description": "Each section highlights"
                                                }
                                            ]
                                        },
                                        {
                                            "attempt": 2,
                                            "guide_says": "There are 4 total parts.",
                                            "animations": []
                                        },
                                        {
                                            "attempt": 3,
                                            "guide_says": "Watch: 1 out of 4 is 1/4.",
                                            "animations": []
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            ]
        }]
    }
    
    formatter = ProductionFormatter()
    result = formatter.execute(nested_data)
    
    print("Production Format Output:")
    print(json.dumps(result, indent=2))
