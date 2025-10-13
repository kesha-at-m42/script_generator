"""
Compare different data storage approaches
Shows which is easiest to work with
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 70)
print("📦 DATA STORAGE COMPARISON")
print("=" * 70)

# ============================================================================
# APPROACH 1: Nested JSON (Original)
# ============================================================================
print("\n1️⃣  NESTED JSON (Original)")
print("-" * 70)

with open("inputs/module_1_fractions.json") as f:
    nested = json.load(f)

print("Code to access module name:")
print('  nested["moduleName"]')
print(f"  → {nested['moduleName']}")

print("\nCode to access vocabulary:")
print('  nested["moduleMetadata"]["keyVocabulary"]')
print(f"  → {nested['moduleMetadata']['keyVocabulary'][:3]}...")

print("\nCode to access goal text:")
print('  nested["deconstructedLearningGoals"][0]["goal"]')
print(f"  → {nested['deconstructedLearningGoals'][0]['goal'][:50]}...")

print("\n❌ Problems: Deep nesting, unclear key names, lots of dict navigation")

# ============================================================================
# APPROACH 2: Flat JSON
# ============================================================================
print("\n\n2️⃣  FLAT JSON (Simplified)")
print("-" * 70)

with open("inputs/module_1_flat.json") as f:
    flat = json.load(f)

print("Code to access module name:")
print('  flat["module_name"]')
print(f"  → {flat['module_name']}")

print("\nCode to access vocabulary:")
print('  flat["vocabulary"]')
print(f"  → {flat['vocabulary'][:3]}...")

print("\nCode to access goal text:")
print('  flat["goals"][0]["text"]')
print(f"  → {flat['goals'][0]['text'][:50]}...")

print("\n✅ Better: One level deep, clear names, easier to remember")

# ============================================================================
# APPROACH 3: Python Dictionary (No parsing!)
# ============================================================================
print("\n\n3️⃣  PYTHON DICT (Best for code)")
print("-" * 70)

from inputs.modules import module_1

print("Code to access module name:")
print('  module_1["module_name"]')
print(f"  → {module_1['module_name']}")

print("\nCode to access vocabulary:")
print('  module_1["vocabulary"]')
print(f"  → {module_1['vocabulary'][:3]}...")

print("\nCode to access goal text:")
print('  module_1["goals"][0]["text"]')
print(f"  → {module_1['goals'][0]['text'][:50]}...")

print("\n✅ Best: No file loading, no parsing, instant import, IDE autocomplete")

# ============================================================================
# COMPARISON TABLE
# ============================================================================
print("\n\n📊 COMPARISON")
print("=" * 70)
print(f"{'Feature':<25} {'Nested JSON':<15} {'Flat JSON':<15} {'Python Dict':<15}")
print("-" * 70)
print(f"{'Ease of Access':<25} {'⭐⭐':<15} {'⭐⭐⭐⭐':<15} {'⭐⭐⭐⭐⭐':<15}")
print(f"{'No Parsing Needed':<25} {'❌':<15} {'❌':<15} {'✅':<15}")
print(f"{'IDE Autocomplete':<25} {'❌':<15} {'❌':<15} {'✅':<15}")
print(f"{'Human Readable':<25} {'⭐⭐⭐':<15} {'⭐⭐⭐⭐':<15} {'⭐⭐⭐⭐⭐':<15}")
print(f"{'Easy to Edit':<25} {'⭐⭐':<15} {'⭐⭐⭐⭐':<15} {'⭐⭐⭐⭐⭐':<15}")
print(f"{'Comments Allowed':<25} {'❌':<15} {'❌':<15} {'✅':<15}")
print(f"{'Version Control':<25} {'✅':<15} {'✅':<15} {'✅':<15}")

print("\n" + "=" * 70)
print("🏆 WINNER: Python Dictionary (.py file)")
print("=" * 70)
print("\n💡 Why?")
print("  • No JSON parsing overhead")
print("  • Import like any Python module")
print("  • Can add comments and documentation")
print("  • IDE provides autocomplete")
print("  • Easier to maintain and edit")
print("  • Same version control as code")
print("\n✨ Just use: from inputs.modules import module_1")
print("=" * 70)
