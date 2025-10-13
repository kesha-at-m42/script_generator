"""
Quick demo: Show how easy it is to use module data now
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from inputs.modules import module_1

print("=" * 70)
print("🚀 MODULE DATA - DIRECT ACCESS DEMO")
print("=" * 70)

print("\n✨ No parsing, no file loading, just import and use!\n")

print("CODE:")
print("  from inputs.modules import module_1")
print()

print("-" * 70)
print("📊 MODULE INFO")
print("-" * 70)
print(f"Name:         {module_1['module_name']}")
print(f"Number:       {module_1['module_number']}")
print(f"Grade:        {module_1['grade_level']}")
print(f"Variant:      {module_1['path_variant']}")

print("\n" + "-" * 70)
print("🎯 LEARNING GOALS")
print("-" * 70)
for i, goal in enumerate(module_1['learning_goals'], 1):
    print(f"{i}. {goal}")

print("\n" + "-" * 70)
print("📚 VOCABULARY")
print("-" * 70)
print(", ".join(module_1['vocabulary']))

print("\n" + "-" * 70)
print("🎓 DETAILED GOALS")
print("-" * 70)
for goal in module_1['goals']:
    print(f"\nGoal {goal['id']}: {goal['text']}")
    print(f"  Categories: {', '.join(goal['content_categories'])}")
    print(f"  Examples: {len(goal['examples'])} questions")

print("\n" + "-" * 70)
print("⚠️  MISCONCEPTIONS")
print("-" * 70)
for misc in module_1['misconceptions']:
    print(f"\n❌ {misc['misconception']}")
    print(f"✅ {misc['correction']}")

print("\n" + "=" * 70)
print("💡 TO EDIT THIS DATA:")
print("=" * 70)
print("\nOption 1: Use the visual editor")
print("  streamlit run dashboard/run_module_editor.py")
print("\nOption 2: Edit inputs/modules.py directly")
print("  (It's just a Python dictionary!)")
print("\n" + "=" * 70)
