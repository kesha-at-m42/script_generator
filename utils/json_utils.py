"""Utilities for extracting JSON from Claude responses"""
import json
import re

def extract_json(text: str) -> str:
    """Extract JSON from Claude's response"""
    
    # Try to find JSON in code blocks
    if "```json" in text:
        start = text.find("```json") + 7
        end = text.find("```", start)
        if end != -1:
            return text[start:end].strip()
        else:
            # Code fence not closed - might be truncated, extract everything after ```json
            return text[start:].strip()
    
    # Try to find JSON in regular code blocks
    if "```" in text:
        start = text.find("```") + 3
        end = text.find("```", start)
        if end != -1:
            return text[start:end].strip()
        else:
            # Code fence not closed - extract everything after ```
            return text[start:].strip()
    
    # Try to find JSON array or object
    for start_char, end_char in [('[', ']'), ('{', '}')]:
        start = text.find(start_char)
        end = text.rfind(end_char)
        if start != -1 and end != -1:
            potential_json = text[start:end+1]
            try:
                # Validate it's actually JSON
                json.loads(potential_json)
                return potential_json
            except:
                continue
    
    # If all else fails, return original
    return text

def parse_json(text: str) -> dict:
    """Extract and parse JSON in one step"""
    json_str = extract_json(text)
    return json.loads(json_str)

# Test it
if __name__ == "__main__":
    print("Testing JSON extraction...\n")
    
    # Test case 1: JSON in code block
    test1 = '''Here's your data:
```json
{"name": "test", "value": 123}
```
Hope that helps!'''
    
    result1 = extract_json(test1)
    print("Test 1 (code block):")
    print(result1)
    
    # Test case 2: Direct JSON
    test2 = 'Some text [{"a": 1}, {"b": 2}] more text'
    result2 = extract_json(test2)
    print("\nTest 2 (direct):")
    print(result2)
    
    # Test case 3: Parse it
    parsed = parse_json(test1)
    print("\nTest 3 (parsed):")
    print(parsed)
    print(f"Type: {type(parsed)}")
    
    print("\n✓ JSON extraction works!")