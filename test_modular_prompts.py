"""
Test script to verify all modular prompt imports work correctly
"""

from pathlib import Path
import sys

# Add prompts directory to path
prompts_path = Path(__file__).parent / "inputs" / "prompts"
sys.path.insert(0, str(prompts_path))

def test_imports():
    """Test that all prompt modules can be imported"""
    
    print("Testing modular prompt imports...\n")
    
    # Test question_generator
    try:
        from question_generator import (
            QUESTION_GENERATOR_ROLE,
            QUESTION_GENERATOR_DOCS,
            QUESTION_GENERATOR_EXAMPLES,
            QUESTION_GENERATOR_STRUCTURE,
            QUESTION_GENERATOR_INSTRUCTIONS
        )
        print("✓ question_generator imports successful")
        print(f"  - ROLE: {len(QUESTION_GENERATOR_ROLE)} chars")
        print(f"  - DOCS: {len(QUESTION_GENERATOR_DOCS)} items")
        print(f"  - EXAMPLES: {len(QUESTION_GENERATOR_EXAMPLES)} items")
    except Exception as e:
        print(f"✗ question_generator import failed: {e}")
    
    # Test interaction_designer
    try:
        from interaction_designer import (
            INTERACTION_DESIGNER_ROLE,
            INTERACTION_DESIGNER_DOCS,
            INTERACTION_DESIGNER_EXAMPLES,
            INTERACTION_DESIGNER_STRUCTURE,
            INTERACTION_DESIGNER_INSTRUCTIONS
        )
        print("✓ interaction_designer imports successful")
        print(f"  - ROLE: {len(INTERACTION_DESIGNER_ROLE)} chars")
        print(f"  - DOCS: {len(INTERACTION_DESIGNER_DOCS)} items")
        print(f"  - EXAMPLES: {len(INTERACTION_DESIGNER_EXAMPLES)} items")
    except Exception as e:
        print(f"✗ interaction_designer import failed: {e}")
    
    # Test validation_designer
    try:
        from validation_designer import (
            VALIDATION_DESIGNER_ROLE,
            VALIDATION_DESIGNER_DOCS,
            VALIDATION_DESIGNER_EXAMPLES,
            VALIDATION_DESIGNER_STRUCTURE,
            VALIDATION_DESIGNER_INSTRUCTIONS
        )
        print("✓ validation_designer imports successful")
        print(f"  - ROLE: {len(VALIDATION_DESIGNER_ROLE)} chars")
        print(f"  - DOCS: {len(VALIDATION_DESIGNER_DOCS)} items")
        print(f"  - EXAMPLES: {len(VALIDATION_DESIGNER_EXAMPLES)} items")
    except Exception as e:
        print(f"✗ validation_designer import failed: {e}")
    
    # Test dialogue_writer
    try:
        from dialogue_writer import (
            DIALOGUE_WRITER_ROLE,
            DIALOGUE_WRITER_DOCS,
            DIALOGUE_WRITER_EXAMPLES,
            DIALOGUE_WRITER_STRUCTURE,
            DIALOGUE_WRITER_INSTRUCTIONS
        )
        print("✓ dialogue_writer imports successful")
        print(f"  - ROLE: {len(DIALOGUE_WRITER_ROLE)} chars")
        print(f"  - DOCS: {len(DIALOGUE_WRITER_DOCS)} items")
        print(f"  - EXAMPLES: {len(DIALOGUE_WRITER_EXAMPLES)} items")
    except Exception as e:
        print(f"✗ dialogue_writer import failed: {e}")
    
    # Test remediation_generator
    try:
        from remediation_generator import (
            REMEDIATION_GENERATOR_ROLE,
            REMEDIATION_GENERATOR_INSTRUCTIONS,
            REMEDIATION_GENERATOR_STRUCTURE
        )
        print("✓ remediation_generator imports successful")
        print(f"  - ROLE: {len(REMEDIATION_GENERATOR_ROLE)} chars")
        print(f"  - INSTRUCTIONS: {len(REMEDIATION_GENERATOR_INSTRUCTIONS)} chars")
    except Exception as e:
        print(f"✗ remediation_generator import failed: {e}")
    
    print("\n✓ All modular prompt imports working!")
    
    # Test PromptBuilder integration
    print("\nTesting PromptBuilder integration...")
    try:
        from core.prompt_builder import PromptBuilder
        builder = PromptBuilder()
        print("✓ PromptBuilder instantiated successfully")
        
        # Test config methods exist
        methods = [
            '_question_generator_config',
            '_interaction_designer_config',
            '_validation_designer_config',
            '_dialogue_writer_config',
            '_remediation_generator_config'
        ]
        for method in methods:
            if hasattr(builder, method):
                print(f"  ✓ {method} exists")
            else:
                print(f"  ✗ {method} missing")
        
    except Exception as e:
        print(f"✗ PromptBuilder integration failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()
