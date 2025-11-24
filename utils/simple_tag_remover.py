"""
Simple tag remover - removes bracketed pedagogical tags
"""
import sys

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # List of exact tags to remove (with escaped chars as they appear in file)
    tags_to_remove = [
        r'[CLEAR\]',
        r'[MODIFY\]',
        r'[Visual\_Anchor\]',
        r'[System\_Leverage\]',
        r'[Meta\_Prompt\]',
        r'[Transfer\_Thinking\]',
        r'[Identity\_Builder\]',
        r'[Misconception\_\#1\]',
        r'[Misconception\_\#2\]',
        r'[Misconception\_\#3\]',
        r'[Processing\_Pause - 2 seconds\]',
    ]

    for tag in tags_to_remove:
        content = content.replace(tag, '')

    # Remove double spaces left behind
    while '  ' in content:
        content = content.replace('  ', ' ')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Done cleaning {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simple_tag_remover.py <filepath>")
        sys.exit(1)
    clean_file(sys.argv[1])
