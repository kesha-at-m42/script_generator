"""
Test that metadata is correctly stripped from system blocks before API call
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.claude_client import ClaudeClient

def test_metadata_stripping():
    """Test that _strip_metadata removes metadata but keeps cache_control"""
    print("="*70)
    print("Testing Metadata Stripping")
    print("="*70)

    client = ClaudeClient()

    # Create test blocks with metadata
    test_blocks = [
        {
            "type": "text",
            "text": "Test block 1",
            "metadata": {
                "block_type": "role",
                "purpose": "Test purpose",
                "cacheable": True
            }
        },
        {
            "type": "text",
            "text": "Test block 2",
            "metadata": {
                "block_type": "reference_doc",
                "block_name": "test.md",
                "purpose": "Test doc",
                "cacheable": True
            },
            "cache_control": {"type": "ephemeral"}
        }
    ]

    print("\nOriginal blocks:")
    for i, block in enumerate(test_blocks, 1):
        print(f"Block {i}:")
        print(f"  - type: {block['type']}")
        print(f"  - text: {block['text']}")
        print(f"  - metadata: {block.get('metadata', 'None')}")
        print(f"  - cache_control: {block.get('cache_control', 'None')}")

    # Strip metadata
    cleaned_blocks = client._strip_metadata(test_blocks)

    print("\n" + "="*70)
    print("Cleaned blocks (ready for API):")
    print("="*70)
    for i, block in enumerate(cleaned_blocks, 1):
        print(f"Block {i}:")
        print(f"  - type: {block['type']}")
        print(f"  - text: {block['text']}")
        print(f"  - metadata: {block.get('metadata', 'None')}")
        print(f"  - cache_control: {block.get('cache_control', 'None')}")

    # Verify results
    print("\n" + "="*70)
    print("Verification:")
    print("="*70)

    assert len(cleaned_blocks) == 2, "Should have 2 blocks"

    # Block 1 checks
    assert cleaned_blocks[0]["type"] == "text", "Block 1 should have type"
    assert cleaned_blocks[0]["text"] == "Test block 1", "Block 1 should have text"
    assert "metadata" not in cleaned_blocks[0], "Block 1 should NOT have metadata"
    assert "cache_control" not in cleaned_blocks[0], "Block 1 should NOT have cache_control"

    # Block 2 checks
    assert cleaned_blocks[1]["type"] == "text", "Block 2 should have type"
    assert cleaned_blocks[1]["text"] == "Test block 2", "Block 2 should have text"
    assert "metadata" not in cleaned_blocks[1], "Block 2 should NOT have metadata"
    assert "cache_control" in cleaned_blocks[1], "Block 2 SHOULD have cache_control"
    assert cleaned_blocks[1]["cache_control"] == {"type": "ephemeral"}, "Block 2 cache_control should match"

    print("[OK] All blocks have correct structure")
    print("[OK] Metadata removed from all blocks")
    print("[OK] cache_control preserved where present")
    print("\n" + "="*70)
    print("SUCCESS: Metadata stripping works correctly!")
    print("="*70)

if __name__ == "__main__":
    test_metadata_stripping()
