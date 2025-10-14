import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step


class ScriptFormatter(Step):
    """Converts interactive sequences into human-readable scripts (no AI)"""
    
    def __init__(self):
        super().__init__(name="Script Formatter", prompt_id="script_formatter")
    
    def execute(self, input_data, **kwargs):
        """Execute step - formats sequences as readable scripts"""
        # Extract sequences from step 2 output
        if isinstance(input_data, dict):
            sequences = input_data.get("sequences", [])
        elif isinstance(input_data, list):
            sequences = input_data
        else:
            sequences = []
        
        print(f"  📝 Formatting {len(sequences)} sequences into scripts...")
        
        # Format all sequences into a single script
        combined_script = self._format_all_sequences(sequences)
        
        # Summary
        print(f"  ✓ Generated combined script with {len(sequences)} problems")
        
        # Get the run folder from kwargs if available (passed from pipeline)
        run_folder = kwargs.get("run_folder")
        
        if run_folder:
            # Save to the date-based folder
            self._save_combined_script(combined_script, run_folder)
        
        return {
            "combined_script": combined_script,
            "total_problems": len(sequences)
        }
    
    def _format_all_sequences(self, sequences: list) -> str:
        """Format all sequences into a single readable script"""
        script_lines = []
        
        for seq in sequences:
            # Format each problem
            problem_script = self._format_sequence(seq)
            script_lines.append(problem_script)
            script_lines.append("")  # Blank line between problems
            script_lines.append("=" * 80)
            script_lines.append("")
        
        return "\n".join(script_lines)
    
    def _format_sequence(self, sequence: dict) -> str:
        """Format a single sequence into a readable script"""
        problem_id = sequence.get("problem_id", "?")
        goal = sequence.get("goal", "No goal specified")
        verb = sequence.get("verb", "interact")
        difficulty_num = sequence.get("difficulty", "N/A")
        steps = sequence.get("steps", [])
        
        # Map difficulty number to name
        difficulty_names = {
            0: "Support",
            1: "Confidence", 
            2: "Baseline",
            3: "Stretch",
            4: "Challenge"
        }
        difficulty = difficulty_names.get(difficulty_num, str(difficulty_num))
        
        script_lines = []
        
        # Header with difficulty name
        script_lines.append(f"# Problem {problem_id}: {verb.title()} | {difficulty}")
        script_lines.append("")
        script_lines.append(f"**Goal:** {goal}")
        script_lines.append("")
        script_lines.append("---")
        script_lines.append("")
        
        # Process steps - no step numbers, just spacing
        for step in steps:
            dialogue = step.get("dialogue", "")
            prompt = step.get("prompt")
            visual = step.get("visual")
            
            # Guide dialogue with emoji
            if dialogue:
                script_lines.append(f"⚫ **Guide:** \"{dialogue}\"")
                script_lines.append("")
                script_lines.append("")
            
            # Visual with emoji
            if visual:
                for v in visual:
                    v_desc = v.get("description", "")
                    script_lines.append(f"🔵 **Visual:** {v_desc}")
                script_lines.append("")
            
            # Student action as [Description]
            if prompt:
                script_lines.append(f"[{prompt}]")
                script_lines.append("")
            
            # Extra spacing between interactions
            script_lines.append("")
        
        # Success feedback
        student_attempts = sequence.get("student_attempts", {})
        success_path = student_attempts.get("success_path", {})
        success_steps = success_path.get("steps", [])
        
        if success_steps:
            script_lines.append("---")
            script_lines.append("")
            script_lines.append("**On Success:**")
            script_lines.append("")
            for feedback in success_steps:
                if isinstance(feedback, str):
                    script_lines.append(f"⚫ **Guide:** \"{feedback}\"")
                    script_lines.append("")
            script_lines.append("")
        
        # Error paths
        error_paths = student_attempts.get("error_paths", {})
        if error_paths:
            script_lines.append("**Error Handling:**")
            script_lines.append("")
            for error_name, feedback_list in error_paths.items():
                error_label = error_name.replace("_", " ").title()
                script_lines.append(f"*{error_label}:*")
                for feedback in feedback_list:
                    script_lines.append(f"⚫ **Guide:** \"{feedback}\"")
                script_lines.append("")
        
        return "\n".join(script_lines)
    
    def _save_combined_script(self, script_content: str, run_folder: Path):
        """Save the combined script to the run folder"""
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"script_{timestamp}.md"
        filepath = Path(run_folder) / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(script_content)
        
        print(f"  💾 Saved combined script: {filepath}")


# Test it
if __name__ == "__main__":
    from core.pipeline import Pipeline
    
    print("Testing ScriptFormatter (Step 3 only)...\n")
    print("Note: For full pipeline test, run tests/test_full_pipeline.py\n")
    
    formatter = ScriptFormatter()
    
    # Sample sequence data (simulating output from SequenceGenerator - Step 2)
    sample_sequences = {
        "sequences": [
            {
                "problem_id": 1,
                "difficultyTier": 1,
                "verb": "partition",
                "goal": "Students can partition shapes into equal parts",
                "steps": [
                    {
                        "dialogue": "Let's work with fractions. You'll see a rectangle split into 3 equal parts.",
                        "prompt": None,
                        "visual": None,
                        "expected_student_input": "next button"
                    },
                    {
                        "dialogue": "Shade one of the three sections to show 1/3.",
                        "prompt": "Click on one section to shade it",
                        "visual": [
                            {
                                "id": "rect_1",
                                "type": "horizontal_rectangle_bar",
                                "state": "partitioned_3_vertical_empty",
                                "description": "A rectangle divided into 3 equal vertical sections, all unshaded"
                            }
                        ],
                        "expected_student_input": "shade_action"
                    },
                    {
                        "dialogue": "You got it. One out of three parts shaded is 1/3.",
                        "prompt": None,
                        "visual": None,
                        "expected_student_input": "next button"
                    }
                ],
                "valid_visual": [
                    {
                        "id": "rect_1",
                        "type": "horizontal_rectangle_bar",
                        "state": "partitioned_3_vertical_shaded_1",
                        "description": "A rectangle divided into 3 equal vertical sections with 1 section shaded"
                    }
                ],
                "student_attempts": {
                    "success_path": {
                        "steps": [
                            {
                                "dialogue": "You got it. One out of three parts shaded is 1/3.",
                                "expected_student_input": "next button"
                            }
                        ]
                    }
                }
            },
            {
                "problem_id": 2,
                "difficultyTier": 2,
                "verb": "identify",
                "goal": "Students can identify unit fractions",
                "steps": [
                    {
                        "dialogue": "Here's a circle divided into 8 equal pieces. One piece is colored red.",
                        "prompt": None,
                        "visual": [
                            {
                                "id": "circle_1",
                                "type": "circle",
                                "state": "divided_8_wedges_1_red",
                                "description": "A circle partitioned into 8 equal wedges with one wedge colored red"
                            }
                        ],
                        "expected_student_input": "next button"
                    },
                    {
                        "dialogue": "Which fraction represents the red piece?",
                        "prompt": "Select the correct fraction",
                        "visual": [
                            {
                                "id": "circle_1",
                                "type": "circle",
                                "state": "divided_8_wedges_1_red",
                                "description": "A circle partitioned into 8 equal wedges with one wedge colored red"
                            }
                        ],
                        "expected_student_input": "button_click"
                    },
                    {
                        "dialogue": "Correct! One piece out of eight is 1/8.",
                        "prompt": None,
                        "visual": None,
                        "expected_student_input": "next button"
                    }
                ],
                "valid_visual": [
                    {
                        "id": "circle_1",
                        "type": "circle",
                        "state": "divided_8_wedges_1_red_selected",
                        "description": "A circle partitioned into 8 equal wedges with the correct fraction identified"
                    }
                ],
                "student_attempts": {
                    "success_path": {
                        "steps": [
                            {
                                "dialogue": "Correct! One piece out of eight is 1/8.",
                                "expected_student_input": "next button"
                            }
                        ]
                    }
                }
            }
        ]
    }
    
    print("Input: Sample sequence data (from Step 2)")
    print(f"  • {len(sample_sequences['sequences'])} sequences\n")
    
    # Test with pipeline (auto-save enabled)
    pipeline = Pipeline("test_script_formatting", save_intermediate=True)
    pipeline.add_step(formatter)
    
    results = pipeline.execute(sample_sequences)
    
    # Display results
    result = pipeline.get_final_output()
    scripts = result.get("scripts", [])
    
    print(f"\n✨ Generated {len(scripts)} formatted scripts")
    
    # Show sample output
    if scripts:
        print(f"\n📄 Sample Script (Problem {scripts[0]['problem_id']}):")
        print("=" * 60)
        print(scripts[0]['markdown'][:500] + "...")
        print("=" * 60)
    
    # Save individual markdown files
    print(f"\n💾 Saving individual script files...")
    saved_files = formatter.save_scripts_to_files(scripts)
    print(f"  ✓ Saved {len(saved_files)} files to outputs/scripts/")
    for f in saved_files:
        print(f"    - {f}")
