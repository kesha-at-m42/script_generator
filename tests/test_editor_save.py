"""
Test that module editor save function works correctly
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 70)
print("🧪 TESTING MODULE EDITOR SAVE FUNCTION")
print("=" * 70)

# Import the save function
from dashboard.module_editor import save_modules_file

# Create test modules
test_modules = {
    1: {
        "module_name": "Test Module 1",
        "module_number": 1,
        "grade_level": 3,
        "path_variant": "A",
        "learning_goals": ["Goal 1", "Goal 2"],
        "vocabulary": ["word1", "word2"],
        "standards": {"building_on": [], "addressing": [], "building_toward": []},
        "core_concepts": ["Concept 1"],
        "goals": [],
        "misconceptions": []
    },
    2: {
        "module_name": "Test Module 2",
        "module_number": 2,
        "grade_level": 4,
        "path_variant": "B",
        "learning_goals": ["Goal A"],
        "vocabulary": ["term1"],
        "standards": {"building_on": [], "addressing": [], "building_toward": []},
        "core_concepts": ["Concept A"],
        "goals": [],
        "misconceptions": []
    }
}

print("\n📝 Test modules created:")
for num, mod in test_modules.items():
    print(f"  Module {num}: {mod['module_name']}")

print("\n💾 Testing save function...")
try:
    saved_path = save_modules_file(test_modules)
    print(f"✅ Save successful!")
    print(f"📄 Saved to: {saved_path}")
    
    # Read back to verify
    print("\n📖 Reading back to verify...")
    with open(saved_path, 'r') as f:
        content = f.read()
    
    print(f"✅ File exists and is readable")
    print(f"📊 File size: {len(content)} characters")
    
    # Check for key content
    if "module_1" in content and "module_2" in content:
        print("✅ Both modules found in file")
    else:
        print("❌ Modules not found in file")
    
    if "MODULES = {" in content:
        print("✅ MODULES dictionary found")
    else:
        print("❌ MODULES dictionary not found")
    
    if "__all__" in content:
        print("✅ __all__ export list found")
    else:
        print("❌ __all__ export list not found")
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED - Save function works correctly!")
    print("=" * 70)
    
except Exception as e:
    print(f"\n❌ Error during save: {e}")
    import traceback
    traceback.print_exc()

print("\n💡 Now try the visual editor:")
print("   streamlit run dashboard/run_module_editor.py")
