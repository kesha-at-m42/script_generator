import anthropic
import os
from dotenv import load_dotenv
from core.prompts import get_test_prompt

# Load environment variables from .env file
load_dotenv()

# Set your API key
api_key = os.environ.get('ANTHROPIC_API_KEY') or 'your-key-here'

client = anthropic.Anthropic(api_key=api_key)

print("Testing prompt with Claude API...\n")

# Get prompt
prompt = get_test_prompt("basic addition")
print(f"Prompt: {prompt}\n")

# Call API
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=500,
    messages=[{"role": "user", "content": prompt}]
)

response = message.content[0].text
print("Claude's response:")
print(response)
print(f"\n✓ Tokens: {message.usage.input_tokens} in, {message.usage.output_tokens} out")