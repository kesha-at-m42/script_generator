import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your API key
api_key = os.environ.get('ANTHROPIC_API_KEY') or 'your-key-here'

print("Testing API connection...")
print(f"API Key loaded: {api_key[:15]}... (length: {len(api_key)})")
print(f"API Key starts with 'sk-ant-api03': {api_key.startswith('sk-ant-api03')}")

try:
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "Say 'API works!' and nothing else."}
        ]
    )
    
    response = message.content[0].text
    print(f"✓ Success! Claude said: {response}")
    print(f"✓ Tokens used: {message.usage.input_tokens} in, {message.usage.output_tokens} out")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check your API key is set correctly")
    print("2. Verify you have API credits")
    print("3. Check your internet connection")