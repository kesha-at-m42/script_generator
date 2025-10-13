def get_test_prompt(topic: str) -> str:
    """A simple test prompt"""
    return f"Generate 3 simple quiz questions about {topic}. Return as JSON array."

# Test it
if __name__ == "__main__":
    prompt = get_test_prompt("fractions")
    print("Generated prompt:")
    print(prompt)
    print("\n✓ Prompt generation works!")