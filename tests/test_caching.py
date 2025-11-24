"""Test script to verify prompt caching is working with Claude API"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from core.claude_client import ClaudeClient

def test_cache_control():
    """Test that cache control works with consecutive API calls"""
    print("Testing Prompt Caching with Claude API")
    print("=" * 70)

    client = ClaudeClient()

    # Create a large static system content that should be cached
    large_doc = """
    This is a large documentation block that simulates real documentation.
    It contains multiple paragraphs and should be cached for cost savings.

    Section 1: Introduction
    This section provides an overview of the system and its capabilities.
    It includes detailed explanations of core concepts and terminology.

    Section 2: Architecture
    The system follows a modular architecture with clear separation of concerns.
    Each component has a specific responsibility and well-defined interfaces.

    Section 3: Best Practices
    - Always validate input data
    - Use proper error handling
    - Write clear documentation
    - Follow coding standards
    - Test thoroughly before deployment

    Section 4: Examples
    Here are various examples showing how to use the system effectively.
    Each example includes explanations and expected outcomes.

    Section 5: Troubleshooting
    Common issues and their solutions are documented here.
    This helps users resolve problems quickly and efficiently.
    """ * 5  # Repeat 5 times to make it larger (meet minimum cache size)

    # Build system blocks with cache control
    system_blocks = [
        {
            "type": "text",
            "text": "You are a helpful assistant."
        },
        {
            "type": "text",
            "text": f"<documentation>\n{large_doc}\n</documentation>"
        },
        {
            "type": "text",
            "text": "Always respond concisely and accurately."
        }
    ]

    print("\n[TEST 1] First API call - should CREATE cache")
    print("-" * 70)

    response1 = client.generate(
        system=system_blocks,
        user_message="Say 'First request' and nothing else.",
        max_tokens=50,
        temperature=0.5
    )

    print(f"Response: {response1}")
    stats1 = client.get_stats()
    print(f"\nStats after first call:")
    print(f"  Input tokens: {stats1['input_tokens']}")
    print(f"  Output tokens: {stats1['output_tokens']}")
    print(f"  Cache creation tokens: {stats1.get('cache_creation_tokens', 0)}")
    print(f"  Cache read tokens: {stats1.get('cache_read_tokens', 0)}")

    print("\n[TEST 2] Second API call - should READ from cache")
    print("-" * 70)

    response2 = client.generate(
        system=system_blocks,  # Same system blocks
        user_message="Say 'Second request' and nothing else.",  # Different user message
        max_tokens=50,
        temperature=0.5
    )

    print(f"Response: {response2}")
    stats2 = client.get_stats()
    print(f"\nStats after second call:")
    print(f"  Input tokens: {stats2['input_tokens']}")
    print(f"  Output tokens: {stats2['output_tokens']}")
    print(f"  Cache creation tokens: {stats2.get('cache_creation_tokens', 0)}")
    print(f"  Cache read tokens: {stats2.get('cache_read_tokens', 0)}")

    if 'cache_savings' in stats2:
        print(f"  Cache savings: {stats2['cache_savings']}")

    print("\n" + "=" * 70)
    print("[VERIFICATION]")

    # Verify caching worked
    cache_created = stats2.get('cache_creation_tokens', 0) > 0
    cache_hit = stats2.get('cache_read_tokens', 0) > 0

    if cache_created:
        print("[OK] Cache was created on first request")
    else:
        print("[WARN] No cache creation detected")

    if cache_hit:
        print("[OK] Cache was hit on second request")
        print("[OK] Prompt caching is working correctly!")
    else:
        print("[WARN] No cache hits detected")
        print("[INFO] Cache may need more time or larger content")

    print("=" * 70)

if __name__ == "__main__":
    test_cache_control()
