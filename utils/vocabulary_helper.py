"""
Vocabulary Helper
Extracts vocabulary terms from module definitions for formatting
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from inputs.modules import MODULES


def get_all_vocabulary_terms(module_numbers=None):
    """
    Extract all vocabulary terms from specified modules
    
    Args:
        module_numbers: List of module numbers to extract from, or None for all modules
        
    Returns:
        List of unique vocabulary terms
    """
    vocabulary_terms = set()
    
    # Determine which modules to process
    if module_numbers is None:
        modules_to_process = MODULES.values()
    else:
        modules_to_process = [MODULES[num] for num in module_numbers if num in MODULES]
    
    # Extract terms from each module
    for module in modules_to_process:
        vocab_list = module.get('vocabulary', [])
        
        for vocab_item in vocab_list:
            if isinstance(vocab_item, dict):
                # Extract the term
                term = vocab_item.get('term', '')
                if term:
                    vocabulary_terms.add(term)
            elif isinstance(vocab_item, str):
                # Direct string vocabulary
                vocabulary_terms.add(vocab_item)
    
    # Return sorted list for consistency
    return sorted(list(vocabulary_terms))


def format_vocabulary_list_for_prompt(module_numbers=None):
    """
    Format vocabulary terms as a bulleted list for prompt inclusion
    
    Args:
        module_numbers: List of module numbers to extract from, or None for all modules
        
    Returns:
        Formatted string with bulleted vocabulary terms
    """
    terms = get_all_vocabulary_terms(module_numbers)
    
    if not terms:
        return "- (no vocabulary terms defined)"
    
    return "\n".join([f"- {term}" for term in terms])


def get_vocabulary_terms_as_list(module_numbers=None):
    """
    Get vocabulary terms as a simple Python list for JSON serialization
    
    Args:
        module_numbers: List of module numbers to extract from, or None for all modules
        
    Returns:
        List of vocabulary term strings
    """
    return get_all_vocabulary_terms(module_numbers)


if __name__ == "__main__":
    # Test the helper
    print("All Vocabulary Terms:")
    print("=" * 50)
    terms = get_all_vocabulary_terms()
    for term in terms:
        print(f"  - {term}")
    
    print(f"\nTotal: {len(terms)} terms")
    
    print("\n" + "=" * 50)
    print("Module 1 Only:")
    print("=" * 50)
    terms_m1 = get_all_vocabulary_terms([1])
    for term in terms_m1:
        print(f"  - {term}")
    
    print(f"\nTotal: {len(terms_m1)} terms")
    
    print("\n" + "=" * 50)
    print("Formatted for Prompt:")
    print("=" * 50)
    print(format_vocabulary_list_for_prompt())
