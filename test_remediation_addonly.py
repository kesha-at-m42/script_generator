"""
Test remediation generator with actual sequence_generator output format
"""
import json
from core.prompt_builder import PromptBuilder

# Sample input matching the actual sequence_generator output
sample_input = {
    "sequences": [
        {
            "problem_id": 1,
            "difficulty": 1,
            "verb": "partition",
            "goal": "Students can partition shapes into equal parts",
            "steps": [
                {
                    "dialogue": "Let's figure out how to split this rectangle into 4 equal parts.",
                    "prompt": None,
                    "visual": [
                        {
                            "id": "rectangle_1",
                            "type": "horizontal_rectangle_bar",
                            "state": "empty",
                            "description": "A horizontal rectangle with light grid overlay showing possible division lines"
                        }
                    ],
                    "expected_student_input": None
                },
                {
                    "dialogue": "Draw lines to divide it into 4 parts that are the same size.",
                    "prompt": "Draw division lines on the rectangle",
                    "visual": [
                        {
                            "id": "rectangle_1",
                            "type": "horizontal_rectangle_bar",
                            "state": "empty_with_grid",
                            "description": "Rectangle with grid guides active for drawing"
                        }
                    ],
                    "expected_student_input": "draw_lines"
                },
                {
                    "dialogue": "Now shade one of the 4 equal parts.",
                    "prompt": "Click to shade one section",
                    "visual": [
                        {
                            "id": "rectangle_1",
                            "type": "horizontal_rectangle_bar",
                            "state": "partitioned_4_equal",
                            "description": "Rectangle divided into 4 equal vertical sections"
                        }
                    ],
                    "expected_student_input": "click_shade"
                }
            ],
            "valid_visual": [
                {
                    "id": "rectangle_1",
                    "type": "horizontal_rectangle_bar",
                    "state": "partitioned_4_equal_shaded_1",
                    "description": "Rectangle divided into 4 equal parts with one part shaded"
                }
            ],
            "student_attempts": {
                "success_path": {
                    "steps": [
                        "You divided it into equal parts. Good work.",
                        "Right there - each part is the same size."
                    ]
                }
            }
        }
    ]
}

print("=" * 70)
print("TESTING REMEDIATION GENERATOR - ADD ERROR PATHS ONLY")
print("=" * 70)

print("\n1. Input Structure")
print("-" * 70)
print(f"[OK] {len(sample_input['sequences'])} sequence(s)")
print(f"[OK] Sequence 1 has {len(sample_input['sequences'][0]['steps'])} steps")
print(f"[OK] Sequence 1 has success_path: {len(sample_input['sequences'][0]['student_attempts']['success_path']['steps'])} feedback lines")
print(f"[OK] No error paths yet")

# Format as context for the prompt
interactions_context = json.dumps(sample_input, indent=2)

print("\n2. Building Prompt")
print("-" * 70)

builder = PromptBuilder()
prompt = builder.build_prompt(
    "remediation_generator",
    {"interactions_context": interactions_context}
)

print(f"[OK] Prompt built: {len(prompt)} characters")

# Check that the prompt includes the input structure
if '"steps"' in prompt and '"valid_visual"' in prompt:
    print("[OK] Prompt includes input structure")
else:
    print("[FAIL] Prompt missing input structure")

if "DO NOT MODIFY" in prompt:
    print("[OK] Prompt includes DO NOT MODIFY instruction")
else:
    print("[FAIL] Prompt missing DO NOT MODIFY instruction")

if "ADD error_path" in prompt:
    print("[OK] Prompt includes ADD error_path instruction")
else:
    print("[FAIL] Prompt missing ADD error_path instruction")

print("\n3. Expected Output")
print("-" * 70)
print("The output should:")
print("  [OK] Keep all 3 steps unchanged")
print("  [OK] Keep valid_visual unchanged")
print("  [OK] Keep success_path unchanged")
print("  [OK] ADD error_path_unequal with remediation_1/2/3")
print("  [OK] ADD error_path_wrong_number with remediation_1/2/3")
print("  [OK] Each remediation has id: light/medium/heavy")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
print("\nTo test with Claude API, run: python test_remediation.py")
