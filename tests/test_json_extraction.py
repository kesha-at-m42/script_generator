"""Test 5: Extract JSON from real Claude responses"""
from core.claude_client import ClaudeClient
from utils.json_utils import parse_json

print("Testing JSON extraction with Claude...\n")

client = ClaudeClient()

prompt = """Generate 2 math questions about addition.
Return ONLY as a JSON array like this:
[
  {"question": "What is 2+2?", "answer": 4},
  {"question": "What is 5+3?", "answer": 8}
]"""

print("Sending prompt...\n")
response = client.generate(prompt, max_tokens=300)

print("Raw response:")
print(response)
print("\n" + "="*60 + "\n")

try:
    parsed = parse_json(response)
    print("Extracted JSON:")
    print(parsed)
    print(f"\n✓ Successfully parsed {len(parsed)} questions!")
    
except Exception as e:
    print(f"✗ Failed to parse: {e}")