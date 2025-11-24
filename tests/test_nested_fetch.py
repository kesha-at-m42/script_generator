"""
Test script for fetching nested fields using module_utils
"""

from utils.module_utils import get_module_field

# Test fetching phases.0 (the first phase from module 1)
print("Testing: get_module_field(1, 'phases.0')")
print("=" * 60)

try:
    first_phase = get_module_field(1, "phases.0")
    print("\nSuccess! Retrieved first phase:")
    print(f"Phase Name: {first_phase.get('phase_name')}")
    print(f"Purpose: {first_phase.get('purpose')}")
    print(f"Interaction Count: {first_phase.get('interaction_count')}")
    print(f"\nFull phase data:")
    print(first_phase)
except Exception as e:
    print(f"\nError: {e}")

print("\n" + "=" * 60)
print("\nTesting: get_module_field(1, 'phases.0')")
print("=" * 60)

try:
    phase_name = get_module_field(1, "phases.0")
    print(f"\nSuccess! Phase name: {phase_name}")
except Exception as e:
    print(f"\nError: {e}")

print("\n" + "=" * 60)
print("\nTesting: get_module_field(1, 'phases.*.phase_name')")
print("=" * 60)

try:
    all_phase_names = get_module_field(1, "phases.*.phase_name")
    print(f"\nSuccess! All phase names: {all_phase_names}")
except Exception as e:
    print(f"\nError: {e}")
