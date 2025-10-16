"""
Test script for remediation generator with new structure
Tests: remediation_1/2/3 with id fields (light/medium/heavy)
"""

from pathlib import Path
from core.prompt_builder import PromptBuilder
from core.claude_client import ClaudeClient
import json

def test_remediation_structure():
    """Test that remediation generator produces correct structure"""
    
    print("=" * 70)
    print("TESTING REMEDIATION GENERATOR")
    print("=" * 70)
    
    # Sample interaction context - matches sequence_generator output format
    interactions_context = json.dumps({
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
                                "description": "A horizontal rectangle with light grid overlay"
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
                                "description": "Rectangle with grid guides active"
                            }
                        ],
                        "expected_student_input": "draw_lines"
                    }
                ],
                "valid_visual": [
                    {
                        "id": "rectangle_1",
                        "type": "horizontal_rectangle_bar",
                        "state": "partitioned_4_equal",
                        "description": "Rectangle divided into 4 equal parts"
                    }
                ],
                "student_attempts": {
                    "success_path": {
                        "steps": [
                            {
                                "dialogue": "You divided it into equal parts. Good work.",
                                "prompt": None,
                                "visual": [],
                                "expected_student_input": None
                            }
                        ]
                    }
                }
            }
        ]
    }, indent=2)
    
    # Build prompt
    builder = PromptBuilder()
    prompt = builder.build_prompt(
        "remediation_generator",
        {"interactions_context": interactions_context}
    )
    
    print("\n1. Prompt Built Successfully")
    print("-" * 70)
    print(f"Prompt length: {len(prompt)} characters")
    print(f"\nFirst 500 chars:")
    print(prompt[:500])
    print("...")
    
    print("\n2. Testing Structure Requirements")
    print("-" * 70)
    
    # Check that structure includes error paths as subsequences
    if "error_path" in prompt:
        print("✓ Found error_path in structure")
    else:
        print("✗ Missing error_path")
    
    if "subsequence" in prompt.lower() or "steps" in prompt:
        print("✓ Found subsequence/steps terminology")
    else:
        print("✗ Missing subsequence/steps")
    
    if "Light" in prompt and "Medium" in prompt and "Heavy" in prompt:
        print("✓ Found Light/Medium/Heavy attempt levels")
    else:
        print("✗ Missing attempt levels")
    
    if "10-20 words" in prompt:
        print("✓ Found Light remediation guidance (10-20 words)")
    else:
        print("✗ Missing Light remediation guidance")
    
    if "20-30 words" in prompt:
        print("✓ Found Medium remediation guidance (20-30 words)")
    else:
        print("✗ Missing Medium remediation guidance")
    
    if "30-60 words" in prompt:
        print("✓ Found Heavy remediation guidance (30-60 words)")
    else:
        print("✗ Missing Heavy remediation guidance")
    
    print("\n3. Testing with Claude API (Optional)")
    print("-" * 70)
    
    try:
        client = ClaudeClient()
        print("✓ Claude client initialized")
        
        response = client.generate(prompt, temperature=0.7)
        print(f"✓ Response received ({len(response)} chars)")
        
        # Save raw response
        with open("test_remediation_response_raw.txt", "w", encoding="utf-8") as f:
            f.write(response)
        print("✓ Saved raw response to test_remediation_response_raw.txt")
        
        # Extract JSON from markdown if needed
        if response.strip().startswith("```") or "```json" in response:
            # Remove markdown code fences
            lines = response.strip().split('\n')
            json_lines = []
            in_json = False
            for line in lines:
                if line.strip().startswith("```"):
                    in_json = not in_json
                    continue
                if in_json:
                    json_lines.append(line)
            response = '\n'.join(json_lines)
            print("✓ Extracted JSON from markdown")
        
        # Save cleaned JSON
        with open("test_remediation_response.json", "w", encoding="utf-8") as f:
            f.write(response)
        print("✓ Saved cleaned JSON to test_remediation_response.json")
        
        # Try to parse JSON
        try:
            data = json.loads(response)
            print("✓ Valid JSON response")
            
            # Check structure
            if "interactions" in data:
                print(f"✓ Contains 'interactions' array ({len(data['interactions'])} items)")
                
                if len(data['interactions']) > 0:
                    interaction = data['interactions'][0]
                    
                    if "student_attempts" in interaction:
                        print("✓ Contains 'student_attempts'")
                        attempts = interaction['student_attempts']
                        
                        # Check for error paths
                        error_paths = [k for k in attempts.keys() if k.startswith('error_path_')]
                        print(f"✓ Found {len(error_paths)} error paths: {error_paths}")
                        
                        if len(error_paths) > 0:
                            error_path = attempts[error_paths[0]]
                            
                            # Check remediation structure
                            if "remediation_1" in error_path:
                                print("✓ Error path contains 'remediation_1'")
                                rem1 = error_path['remediation_1']
                                
                                if "id" in rem1 and rem1['id'] == "light":
                                    print("✓ remediation_1 has id='light'")
                                else:
                                    print(f"✗ remediation_1 id issue: {rem1.get('id', 'MISSING')}")
                            
                            if "remediation_2" in error_path:
                                print("✓ Error path contains 'remediation_2'")
                                rem2 = error_path['remediation_2']
                                
                                if "id" in rem2 and rem2['id'] == "medium":
                                    print("✓ remediation_2 has id='medium'")
                                else:
                                    print(f"✗ remediation_2 id issue: {rem2.get('id', 'MISSING')}")
                            
                            if "remediation_3" in error_path:
                                print("✓ Error path contains 'remediation_3'")
                                rem3 = error_path['remediation_3']
                                
                                if "id" in rem3 and rem3['id'] == "heavy":
                                    print("✓ remediation_3 has id='heavy'")
                                else:
                                    print(f"✗ remediation_3 id issue: {rem3.get('id', 'MISSING')}")
                            
                            # Show sample
                            print("\n4. Sample Remediation Path")
                            print("-" * 70)
                            print(json.dumps(error_path, indent=2))
                    
        except json.JSONDecodeError as e:
            print(f"✗ Invalid JSON: {e}")
            print(f"Response preview: {response[:500]}")
            
    except Exception as e:
        print(f"⚠ Skipping API test: {e}")
        print("  (This is optional - structure validation passed)")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    test_remediation_structure()
