"""
Demo: Multiple modules with dropdown selector
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from inputs.modules import MODULES

print("=" * 70)
print("🗂️  MULTIPLE MODULES DEMO")
print("=" * 70)

print(f"\n✨ Total Modules: {len(MODULES)}\n")

for module_num in sorted(MODULES.keys()):
    module = MODULES[module_num]
    print(f"📚 Module {module_num}: {module['module_name']}")
    print(f"   Grade: {module['grade_level']}")
    print(f"   Learning Goals: {len(module['learning_goals'])}")
    print(f"   Vocabulary: {len(module['vocabulary'])} terms")
    print(f"   Detailed Goals: {len(module['goals'])}")
    print()

print("=" * 70)
print("💡 USAGE IN CODE:")
print("=" * 70)
print("\nOption 1: Import specific module")
print("  from inputs.modules import module_1, module_2")
print("  print(module_1['module_name'])")
print()
print("Option 2: Import MODULES dict and select dynamically")
print("  from inputs.modules import MODULES")
print("  module = MODULES[1]  # Get module 1")
print("  print(module['module_name'])")
print()
print("Option 3: Loop through all modules")
print("  from inputs.modules import MODULES")
print("  for num, module in MODULES.items():")
print("      print(f'Module {num}: {module[\"module_name\"]}')")
print()
print("=" * 70)
print("✨ Visual Editor: streamlit run dashboard/run_module_editor.py")
print("   - Dropdown to select modules")
print("   - Add new modules")
print("   - Delete modules")
print("   - Edit all fields")
print("=" * 70)
