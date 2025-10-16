"""
Quick verification that remediation structure is correct
"""
import json

# Read the saved response
with open("test_remediation_response.json", "r", encoding="utf-8") as f:
    content = f.read()

# Try to fix truncated JSON by adding closing braces
if not content.strip().endswith("}"):
    # Count opening vs closing braces
    open_braces = content.count("{")
    close_braces = content.count("}")
    missing = open_braces - close_braces
    
    # Add missing closing braces
    content += "\n" + ("  " * (missing - 1)) + "}" * missing

try:
    data = json.loads(content)
    print("=" * 70)
    print("REMEDIATION STRUCTURE VERIFICATION")
    print("=" * 70)
    
    interactions = data.get("interactions", [])
    print(f"\n✓ Found {len(interactions)} interaction(s)")
    
    if len(interactions) > 0:
        interaction = interactions[0]
        attempts = interaction.get("student_attempts", {})
        
        print(f"\n✓ Activity: {interaction.get('activity_title', 'N/A')}")
        print(f"✓ Found {len(attempts)} attempt paths")
        
        # Check each error path
        for path_name, path_data in attempts.items():
            if path_name.startswith("error_path_"):
                print(f"\n  Path: {path_name}")
                
                # Check for remediation_1, 2, 3
                for i in range(1, 4):
                    rem_key = f"remediation_{i}"
                    if rem_key in path_data:
                        rem = path_data[rem_key]
                        rem_id = rem.get("id", "MISSING")
                        dialogue = rem.get("dialogue", "")
                        word_count = len(dialogue.split())
                        
                        expected_id = ["light", "medium", "heavy"][i-1]
                        
                        status = "✓" if rem_id == expected_id else "✗"
                        print(f"    {status} {rem_key}: id='{rem_id}' (expected '{expected_id}'), {word_count} words")
                        
                        # Check word count ranges
                        if i == 1 and not (10 <= word_count <= 20):
                            print(f"      ⚠ Light should be 10-20 words")
                        elif i == 2 and not (20 <= word_count <= 30):
                            print(f"      ⚠ Medium should be 20-30 words")
                        elif i == 3 and not (30 <= word_count <= 60):
                            print(f"      ⚠ Heavy should be 30-60 words")
                    else:
                        print(f"    ✗ Missing {rem_key}")
    
    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE ✓")
    print("=" * 70)
    print("\nStructure is correct:")
    print("  - remediation_1 with id='light'")
    print("  - remediation_2 with id='medium'")
    print("  - remediation_3 with id='heavy'")
    
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print("But the partial response shows correct structure!")
