"""Simple Claude API wrapper with prompt caching support and logging"""
import anthropic
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ClaudeClient:
    """Basic wrapper around Anthropic API with caching support"""

    def __init__(self, api_key=None, log_file=None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("API key required!")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = "claude-sonnet-4-5-20250929"

        # Track usage
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cache_creation_tokens = 0
        self.total_cache_read_tokens = 0

        # Logging setup
        if log_file:
            self.log_file = Path(log_file)
        else:
            # Default log location: logs/claude_usage.jsonl
            project_root = Path(__file__).parent.parent
            logs_dir = project_root / "logs"
            logs_dir.mkdir(exist_ok=True)
            self.log_file = logs_dir / "claude_usage.jsonl"

        self.request_count = 0

    def generate(self,
                 system=None,
                 user_message: str = "",
                 max_tokens: int = 1000,
                 temperature: float = 1.0,
                 prefill: str = None,
                 stop_sequences=None,
                 model: str = None,
                 # Legacy support
                 prompt: str = None) -> str:
        """Generate response from Claude with prompt caching support

        Args:
            system: List of system blocks (for caching) or string (legacy)
            user_message: The user prompt
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            prefill: Optional text to prefill the assistant's response
            stop_sequences: Optional list of stop sequences
            model: Claude model to use (e.g., "claude-opus-4-5-20251101"). If None, uses self.model
            prompt: Legacy parameter for backwards compatibility

        Returns:
            Generated text response
        """
        # Legacy support: if prompt is provided, use old behavior
        if prompt is not None:
            system = None
            user_message = prompt

        # Build messages
        messages = [{"role": "user", "content": user_message}]

        # Add prefill if provided
        if prefill:
            messages.append({"role": "assistant", "content": prefill})

        # Build API parameters
        api_params = {
            "model": model if model is not None else self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages
        }

        # Add system if provided (supports both list and string)
        if system:
            api_params["system"] = system

        # Add stop_sequences if provided
        if stop_sequences:
            api_params["stop_sequences"] = stop_sequences

        # Use streaming for large outputs (>10K tokens) to avoid timeouts
        if max_tokens > 10000:
            full_response = ""
            with self.client.messages.stream(**api_params) as stream:
                for text in stream.text_stream:
                    full_response += text

                # Get final message for usage stats
                final_message = stream.get_final_message()
                self._track_usage(final_message.usage)
                self._log_request(final_message.usage, max_tokens, temperature)

            # Prepend prefill to response if it was used
            if prefill:
                return prefill + full_response
            return full_response
        else:
            # Standard non-streaming for smaller outputs
            message = self.client.messages.create(**api_params)

            # Track tokens
            self._track_usage(message.usage)
            self._log_request(message.usage, max_tokens, temperature)

            response_text = message.content[0].text

            # Prepend prefill to response if it was used
            if prefill:
                return prefill + response_text
            return response_text

    def _track_usage(self, usage):
        """Track token usage including cache stats"""
        self.total_input_tokens += usage.input_tokens
        self.total_output_tokens += usage.output_tokens

        # Track cache stats if available
        if hasattr(usage, 'cache_creation_input_tokens'):
            self.total_cache_creation_tokens += usage.cache_creation_input_tokens
            self.total_cache_read_tokens += usage.cache_read_input_tokens

    def _log_request(self, usage, max_tokens, temperature):
        """Log request details to file"""
        self.request_count += 1

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "request_number": self.request_count,
            "model": self.model,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        # Add cache stats if available
        if hasattr(usage, 'cache_creation_input_tokens'):
            log_entry["cache_creation_tokens"] = usage.cache_creation_input_tokens
            log_entry["cache_read_tokens"] = usage.cache_read_input_tokens
            log_entry["cache_hit"] = usage.cache_read_input_tokens > 0

        # Append to log file (JSONL format - one JSON object per line)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')

    def get_stats(self):
        """Get usage statistics including cache metrics"""
        stats = {
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "requests": self.request_count
        }

        # Add cache stats if any caching occurred
        if self.total_cache_creation_tokens > 0 or self.total_cache_read_tokens > 0:
            stats["cache_creation_tokens"] = self.total_cache_creation_tokens
            stats["cache_read_tokens"] = self.total_cache_read_tokens
            stats["cache_savings"] = self._calculate_cache_savings()

        return stats

    def _calculate_cache_savings(self):
        """Calculate cost savings from caching"""
        if self.total_cache_read_tokens == 0:
            return "0%"

        # Without caching, all cache reads would have been normal input tokens
        # Cache reads cost 10% of normal input, so savings = 90%
        savings_pct = 90  # Cache reads are 90% cheaper

        return f"{savings_pct}% (saved {self.total_cache_read_tokens} tokens)"

# Test it
if __name__ == "__main__":
    print("Testing ClaudeClient with Logging...")
    print("="*70)

    client = ClaudeClient()

    # Test 1: Legacy usage (backwards compatibility)
    print("\nTest 1: Legacy usage")
    response = client.generate(prompt="Say 'Hello!' and nothing else.")
    print(f"Response: {response}")

    # Test 2: New structured usage with caching
    print("\nTest 2: New structured usage")
    system_blocks = [
        {
            "type": "text",
            "text": "You are a helpful assistant."
        },
        {
            "type": "text",
            "text": "."
        }
    ]
    response = client.generate(
        system=system_blocks,
        user_message="Say 'Hi!' and nothing else.",
        max_tokens=100,
        temperature=0.5
    )
    print(f"Response: {response}")

    # Test 3: Check stats
    print("\nTest 3: Usage stats")
    stats = client.get_stats()
    print("Stats:", stats)

    print(f"\n[OK] ClaudeClient with logging works!")
    print(f"Log file location: {client.log_file}")
