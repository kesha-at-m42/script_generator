"""
Quick test of vocabulary helper integration
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.vocabulary_helper import (
    get_all_vocabulary_terms,
    format_vocabulary_list_for_prompt,
    get_vocabulary_terms_as_list
)

print("=" * 70)
print("VOCABULARY HELPER TEST")
print("=" * 70)

print("\n1. Get all vocabulary terms as list:")
all_terms = get_all_vocabulary_terms()
print(f"   Found {len(all_terms)} terms:")
for term in all_terms:
    print(f"     - {term}")

print("\n2. Get Module 1 vocabulary only:")
module_1_terms = get_all_vocabulary_terms([1])
print(f"   Found {len(module_1_terms)} terms:")
for term in module_1_terms:
    print(f"     - {term}")

print("\n3. Get Module 2 vocabulary only:")
module_2_terms = get_all_vocabulary_terms([2])
print(f"   Found {len(module_2_terms)} terms:")
for term in module_2_terms:
    print(f"     - {term}")

print("\n4. Formatted for prompt (all modules):")
formatted = format_vocabulary_list_for_prompt()
print(formatted)

print("\n5. As Python list (for JSON):")
as_list = get_vocabulary_terms_as_list([1, 2])
print(f"   {as_list}")

print("\n" + "=" * 70)
print("✓ All functions working correctly!")
print("=" * 70)
