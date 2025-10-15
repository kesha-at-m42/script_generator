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
        main_sequence = sequence.get("main_sequence", [])
        
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
        
        # Process main sequence steps
        for step in main_sequence:
            step_id = step.get("step_id", "?")
            guide_says = step.get("guide_says", "")
            visuals = step.get("visuals", [])
            animations = step.get("animations", [])
            student_action = step.get("student_action")
            
            # Guide dialogue with emoji
            if guide_says:
                script_lines.append(f"⚫ **Guide:** \"{guide_says}\"")
                script_lines.append("")
            
            # Animations (if any)
            if animations:
                for anim in animations:
                    anim_type = anim.get("type", "")
                    anim_desc = anim.get("description", "")
                    script_lines.append(f"🎬 **Animation:** {anim_desc}")
                script_lines.append("")
            
            # Visuals with emoji
            if visuals:
                for v in visuals:
                    v_desc = v.get("description", "")
                    script_lines.append(f"🔵 **Visual:** {v_desc}")
                script_lines.append("")
            
            # Student action as [Description]
            if student_action:
                action_desc = student_action.get("description", "")
                validation = student_action.get("validation", {})
                
                if action_desc:
                    script_lines.append(f"[{action_desc}]")
                    script_lines.append("")
                
                # Format validation paths if present
                if validation:
                    script_lines.append("")
                    script_lines = self._format_validation(validation, script_lines)
            
            # Extra spacing between interactions
            script_lines.append("")
        
        return "\n".join(script_lines)
    
    def _format_validation(self, validation: dict, script_lines: list) -> list:
        """Format validation states (success paths and error remediations)"""
        
        # Remediation level emojis and labels
        remediation_levels = {
            1: {"emoji": "🟡", "label": "Light Remediation"},
            2: {"emoji": "🟠", "label": "Medium Remediation"},
            3: {"emoji": "🔴", "label": "Heavy Remediation"}
        }
        
        # Success on first attempt
        success_first = validation.get("success_first_attempt")
        if success_first and isinstance(success_first, dict):
            guide_says = success_first.get("guide_says", "")
            if guide_says:
                script_lines.append("**✅ Success (First Try):**")
                script_lines.append(f"⚫ **Guide:** \"{guide_says}\"")
                script_lines.append("")
        
        # Success after error
        success_after = validation.get("success_after_error")
        if success_after and isinstance(success_after, dict):
            guide_says = success_after.get("guide_says", "")
            if guide_says:
                script_lines.append("**✅ Success (After Hints):**")
                script_lines.append(f"⚫ **Guide:** \"{guide_says}\"")
                script_lines.append("")
        
        # Error paths with progressive remediations
        errors = validation.get("errors", {})
        if errors:
            script_lines.append("---")
            script_lines.append("")
            script_lines.append("**❌ ERROR PATHS:**")
            script_lines.append("")
            
            for error_name, error_data in errors.items():
                error_label = error_name.replace("_", " ").title()
                remediations = error_data.get("remediations", [])
                
                script_lines.append(f"**{error_label}:**")
                script_lines.append("")
                
                for i, rem in enumerate(remediations, 1):
                    guide_says = rem.get("guide_says", "")
                    animations = rem.get("animations", [])
                    
                    # Get remediation level info
                    level_info = remediation_levels.get(i, {"emoji": "⚪", "label": f"Attempt {i}"})
                    
                    script_lines.append(f"{level_info['emoji']} **{level_info['label']}:**")
                    
                    if guide_says:
                        script_lines.append(f"  ⚫ **Guide:** \"{guide_says}\"")
                    
                    if animations:
                        for anim in animations:
                            anim_desc = anim.get("description", "")
                            script_lines.append(f"  🎬 **Animation:** {anim_desc}")
                    
                    script_lines.append("")
                
                script_lines.append("")
        
        return script_lines
    
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
