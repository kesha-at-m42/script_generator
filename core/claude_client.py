"""Simple Claude API wrapper"""
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ClaudeClient:
    """Basic wrapper around Anthropic API"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("API key required!")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-5-20250929"
        
        # Track usage
        self.total_input_tokens = 0
        self.total_output_tokens = 0
    
    def generate(self, prompt: str, max_tokens: int = 1000, temperature: float = 1.0, prefill: str = None) -> str:
        """Generate response from Claude
        
        Args:
            prompt: The user prompt
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            prefill: Optional text to prefill the assistant's response with
        """
        # Build messages
        messages = [{"role": "user", "content": prompt}]
        
        # Add prefill if provided
        if prefill:
            messages.append({"role": "assistant", "content": prefill})
        
        # Use streaming for large outputs (>10K tokens) to avoid timeouts
        if max_tokens > 10000:
            full_response = ""
            with self.client.messages.stream(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=messages
            ) as stream:
                for text in stream.text_stream:
                    full_response += text
                
                # Get final message for usage stats
                final_message = stream.get_final_message()
                self.total_input_tokens += final_message.usage.input_tokens
                self.total_output_tokens += final_message.usage.output_tokens
            
            # Prepend prefill to response if it was used
            if prefill:
                return prefill + full_response
            return full_response
        else:
            # Standard non-streaming for smaller outputs
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=messages
            )
            
            # Track tokens
            self.total_input_tokens += message.usage.input_tokens
            self.total_output_tokens += message.usage.output_tokens
            
            response_text = message.content[0].text
            
            # Prepend prefill to response if it was used
            if prefill:
                return prefill + response_text
            return response_text
    
    def get_stats(self):
        """Get usage statistics"""
        return {
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens
        }

# Test it
if __name__ == "__main__":
    print("Testing ClaudeClient...\n")
    
    client = ClaudeClient()
    
    # Test 1: Simple generation
    response = client.generate("Say 'Hello!' and nothing else.")
    print(f"Response: {response}")
    
    # Test 2: Check stats
    stats = client.get_stats()
    print(f"\n✓ Stats: {stats}")
    
    print("\n✓ ClaudeClient works!")