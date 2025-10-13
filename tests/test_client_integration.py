"""Test 4: Integrate client with prompts"""
from core.claude_client import ClaudeClient
from core.prompts import get_test_prompt

print("Testing client + prompts integration...\n")

# Create client
client = ClaudeClient()

# Get prompt
prompt = get_test_prompt("multiplication")
print(f"Prompt: {prompt}\n")

# Generate
response = client.generate(prompt, max_tokens=500)
print("Response:")
print(response)

# Stats
stats = client.get_stats()
print(f"\n✓ Used {stats['total_tokens']} tokens")
print("✓ Integration works!")