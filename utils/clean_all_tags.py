"""
Remove ALL pedagogical tags from markdown files
"""
import re
import sys

def clean_tags(filepath):
    """Remove all tag references from file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all variations of pedagogical tags
    # Pattern: anything in brackets with escaped characters like \_ or \#
    content = re.sub(r'\[CLEAR\\\?\]\s*', '', content)
    content = re.sub(r'\[MODIFY\\\?\]\s*', '', content)
    content = re.sub(r'\[Visual\\_Anchor\\\?\]\s*', '', content)
    content = re.sub(r'\[System\\_Leverage\\\?\]\s*', '', content)
    content = re.sub(r'\[Meta\\_Prompt\\\?\]\s*', '', content)
    content = re.sub(r'\[Transfer\\_Thinking\\\?\]\s*', '', content)
    content = re.sub(r'\[Identity\\_Builder\\\?\]\s*', '', content)
    content = re.sub(r'\[Misconception\\_\\#\d+\\\?\]\s*', '', content)
    content = re.sub(r'\[Processing\\_Pause[^\]]*\]\s*', '', content)

    # Remove problem type tags (keep as-is, they're meaningful)
    content = re.sub(r'## \*\*PROBLEM \d+: \[.*?\] - ', '## **PROBLEM \\1: ', content)
    content = re.sub(r'## \*\*PROBLEM \d+: ', '## **PROBLEM \\1: ', content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned tags from {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_all_tags.py <filepath>")
        sys.exit(1)

    clean_tags(sys.argv[1])
