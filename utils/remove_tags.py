"""
Remove pedagogical tags from markdown files
"""
import re
import sys

def remove_tags(content):
    """Remove all bracketed tags from content"""

    # Remove tags like [Visual_Anchor], [Misconception_#1], etc. but keep option notes
    # Keep: [Option to add...], [Student...], [Blank rectangle]
    # Remove: [CLEAR], [Visual_Anchor], [Misconception_#1], etc.

    patterns_to_remove = [
        r'\[CLEAR\]\s*',
        r'\[NEW\]\s*',
        r'\[MODIFY\]\s*',
        r'\[Visual_Anchor\]\s*',
        r'\[System_Leverage\]\s*',
        r'\[Meta_Prompt\]\s*',
        r'\[Transfer_Thinking\]\s*',
        r'\[Identity_Builder\]\s*',
        r'\[Misconception_#\d+\]\s*',
        r'\[Misconception_\\\#\d+\]\s*',  # Escaped version
    ]

    result = content
    for pattern in patterns_to_remove:
        result = re.sub(pattern, '', result)

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python remove_tags.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove tags
    cleaned = remove_tags(content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"Cleaned tags from {filepath}")

if __name__ == "__main__":
    main()
