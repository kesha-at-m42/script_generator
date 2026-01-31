"""
BBCode Formatter Utility
Deterministic post-processing for Godot sequences after AI transformation

Core Functions:
1. format_vocab_tags() - Add vocab tags (auto-removes existing tags first)
2. format_fractions_bbcode() - Add fraction BBCode tags with or without words

Pipeline Functions (use in pipelines.json):
1. apply_vocab_formatting() - Pipeline step for vocab tags (loads vocab from module)
2. apply_fraction_formatting() - Pipeline step for fraction tags
"""

import re
import json
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.module_utils import get_module_field


# ============================================================================
# FRACTION WORDS MAPPING
# ============================================================================

FRACTION_WORDS = {
    # Unit fractions
    "1/2": "one half",
    "1/3": "one third",
    "1/4": "one fourth",
    "1/5": "one fifth",
    "1/6": "one sixth",
    "1/8": "one eighth",
    "1/10": "one tenth",
    "1/12": "one twelfth",
    
    # Common fractions
    "2/3": "two thirds",
    "2/4": "two fourths",
    "2/5": "two fifths",
    "2/6": "two sixths",
    "2/8": "two eighths",
    
    "3/4": "three fourths",
    "3/5": "three fifths",
    "3/6": "three sixths",
    "3/8": "three eighths",
    "3/10": "three tenths",
    
    "4/5": "four fifths",
    "4/6": "four sixths",
    "4/8": "four eighths",
    "4/10": "four tenths",
    
    "5/6": "five sixths",
    "5/8": "five eighths",
    "5/10": "five tenths",
    "5/12": "five twelfths",
    
    "6/8": "six eighths",
    "6/10": "six tenths",
    
    "7/8": "seven eighths",
    "7/10": "seven tenths",
    
    "8/10": "eight tenths",
    "9/10": "nine tenths",
    
    # Add more as needed
}


# ============================================================================
# FRACTION BBCODE FORMATTING
# ============================================================================

def format_fractions_bbcode(text, context_type, include_words=True):
    """
    Format fractions with BBCode tags.
    
    Args:
        text: String to process
        context_type: "dialogue", "prompt", or "choice" (for logging/debugging)
        include_words: If True, includes words in BBCode (for dialogue).
                      If False, empty BBCode (for prompts/choices).
    
    Returns:
        Formatted string with fraction BBCode
    
    Examples:
        >>> format_fractions_bbcode("Shade 3/4 of the bar", "dialogue", True)
        "Shade [fraction numerator=3 denominator=4]three fourths[/fraction] of the bar"
        
        >>> format_fractions_bbcode("3/4", "choice", False)
        "[fraction numerator=3 denominator=4][/fraction]"
    """
    if not text or not isinstance(text, str):
        return text
    
    def replace_fraction(match):
        numerator = match.group(1)
        denominator = match.group(2)
        fraction_str = f"{numerator}/{denominator}"
        
        if include_words:
            # For dialogue - include spoken words
            words = FRACTION_WORDS.get(fraction_str, "")
            if not words:
                # Generate generic words if not in mapping
                words = f"{numerator} {_ordinal_word(denominator)}s"
            return f"[fraction numerator={numerator} denominator={denominator}]{words}[/fraction]"
        else:
            # For prompts/choices - no words, just BBCode wrapper
            return f"[fraction numerator={numerator} denominator={denominator}][/fraction]"
    
    # Match fractions like 1/2, 3/4, 12/16, etc.
    # Use word boundaries to avoid matching non-fractions
    pattern = r'\b(\d+)/(\d+)\b'
    formatted = re.sub(pattern, replace_fraction, text)
    
    return formatted


def _ordinal_word(denominator_str):
    """Convert denominator to ordinal word (e.g., '3' -> 'third')"""
    ordinals = {
        '2': 'half', '3': 'third', '4': 'fourth', '5': 'fifth',
        '6': 'sixth', '7': 'seventh', '8': 'eighth', '9': 'ninth',
        '10': 'tenth', '11': 'eleventh', '12': 'twelfth'
    }
    return ordinals.get(denominator_str, f"{denominator_str}th")


# ============================================================================
# VOCABULARY TAGGING
# ============================================================================

def format_vocab_tags(text, vocabulary_list):
    """
    Wrap vocabulary terms with [vocab] tags.
    Automatically removes all existing vocab tags first, then adds new ones.

    Args:
        text: String to process
        vocabulary_list: List of vocabulary terms from module vocab array

    Returns:
        String with vocab tags properly formatted

    Examples:
        >>> format_vocab_tags("partition the bar into equal parts", ["partition", "equal parts"])
        "[vocab]partition[/vocab] the bar into [vocab]equal parts[/vocab]"

        >>> format_vocab_tags("[vocab]old[/vocab] partition the bar", ["partition"])
        "[vocab]partition[/vocab] the bar"
    """
    if not text or not vocabulary_list:
        return text

    # Step 1: Remove all existing vocab tags
    result = re.sub(r'\[vocab\](.*?)\[/vocab\]', r'\1', text)

    # Convert to list if comma-separated string
    if isinstance(vocabulary_list, str):
        vocabulary_list = [term.strip() for term in vocabulary_list.split(',')]

    # Sort by length (longest first) to avoid partial matches
    # e.g., "equal parts" before "equal" to avoid "[vocab]equal[/vocab] parts"
    sorted_vocab = sorted(vocabulary_list, key=len, reverse=True)

    # Step 2: Add vocab tags for terms in vocabulary_list
    for term in sorted_vocab:
        if not term:
            continue

        # Skip if already tagged
        if f"[vocab]{term}[/vocab]" in result:
            continue

        # Skip if inside BBCode tags (avoid breaking [fraction]...[/fraction])
        if re.search(r'\[.*' + re.escape(term) + r'.*\]', result):
            continue

        # Case-sensitive whole-word matching
        pattern = r'\b' + re.escape(term) + r'\b'

        # Replace only first occurrence (to be safe)
        result = re.sub(pattern, f"[vocab]{term}[/vocab]", result, count=1)

    return result


# ============================================================================
# MAIN PROCESSING FUNCTION
# ============================================================================

def process_godot_sequences(godot_data, vocabulary_list=None):
    """
    Apply BBCode formatting to entire Godot sequence data structure.
    
    This is the main entry point for post-processing after AI transformation.
    
    Args:
        godot_data: Godot schema dict (with @type: "SequencePool" and sequences array)
        vocabulary_list: Optional list of vocabulary terms for [vocab] tagging
    
    Returns:
        Modified godot_data with all text fields formatted
    
    Processing rules:
        - dialogue: fractions with words + vocab tags
        - prompt.text: fractions without words, no vocab tags
        - choices.options: fractions without words, no vocab tags
        - remediations[].step.dialogue: fractions with words + vocab tags
        - on_correct.dialogue: fractions with words + vocab tags
    """
    if not godot_data or '@type' not in godot_data:
        print("⚠️  Invalid Godot data structure - skipping BBCode formatting")
        return godot_data
    
    sequences = godot_data.get('sequences', [])
    
    for seq_idx, sequence in enumerate(sequences, 1):
        if '@type' not in sequence or sequence['@type'] != 'Sequence':
            print(f"⚠️  Sequence {seq_idx}: Invalid type, skipping")
            continue
        
        steps = sequence.get('steps', [])
        
        for step_idx, step in enumerate(steps, 1):
            try:
                # Process dialogue (fractions + vocab)
                if 'dialogue' in step and step['dialogue']:
                    step['dialogue'] = format_fractions_bbcode(
                        step['dialogue'],
                        "dialogue",
                        include_words=True
                    )
                    if vocabulary_list:
                        step['dialogue'] = format_vocab_tags(step['dialogue'], vocabulary_list)

                # Process prompt if present
                if 'prompt' in step and step['prompt']:
                    prompt = step['prompt']

                    # Prompt text (fractions only, no words, no vocab)
                    if 'text' in prompt and prompt['text']:
                        prompt['text'] = format_fractions_bbcode(
                            prompt['text'],
                            "prompt",
                            include_words=False
                        )

                    # Choices (fractions only, no words, no vocab)
                    if 'choices' in prompt and prompt['choices'] is not None and 'options' in prompt['choices']:
                        prompt['choices']['options'] = [
                            format_fractions_bbcode(choice, "choice", include_words=False)
                            for choice in prompt['choices']['options']
                        ]

                    # Remediations (dialogue = fractions with words + vocab)
                    for rem in prompt.get('remediations', []):
                        rem_step = rem.get('step', {})
                        if 'dialogue' in rem_step and rem_step['dialogue']:
                            rem_step['dialogue'] = format_fractions_bbcode(
                                rem_step['dialogue'],
                                "remediation_dialogue",
                                include_words=True
                            )
                            if vocabulary_list:
                                rem_step['dialogue'] = format_vocab_tags(
                                    rem_step['dialogue'],
                                    vocabulary_list
                                )

                    # on_correct (dialogue = fractions with words + vocab)
                    if 'on_correct' in prompt and prompt['on_correct'] is not None:
                        if 'dialogue' in prompt['on_correct'] and prompt['on_correct']['dialogue']:
                            prompt['on_correct']['dialogue'] = format_fractions_bbcode(
                                prompt['on_correct']['dialogue'],
                                "on_correct_dialogue",
                                include_words=True
                            )
                            if vocabulary_list:
                                prompt['on_correct']['dialogue'] = format_vocab_tags(
                                    prompt['on_correct']['dialogue'],
                                    vocabulary_list
                                )
            except Exception as e:
                print(f"⚠️  Error formatting step {step_idx} in sequence {seq_idx}: {e}")
                continue
    
    return godot_data


# ============================================================================
# PIPELINE-COMPATIBLE FUNCTIONS
# ============================================================================

def apply_vocab_formatting(godot_data, module_number=None):
    """
    Pipeline step: Apply vocabulary tags to all dialogue in Godot sequences.
    Automatically loads vocabulary from module and removes existing tags.

    Args:
        godot_data: Godot schema dict (with @type: "SequencePool" and sequences array)
        module_number: Module number (automatically passed by pipeline)

    Returns:
        Modified godot_data with vocab tags applied to dialogue

    Usage in pipeline (pipelines.json):
        {
            "name": "vocab_formatting",
            "type": "formatting",
            "function": "bbcode_formatter.apply_vocab_formatting",
            "description": "Apply vocabulary tags to dialogue",
            "function_args": {},
            "output_file": "vocab_formatted.json"
        }
    """
    if not godot_data or '@type' not in godot_data:
        print("⚠️  Invalid Godot data structure - skipping vocab formatting")
        return godot_data

    # Load vocabulary from module
    vocabulary_list = None
    if module_number:
        try:
            vocabulary_list = get_module_field(module_number, "vocabulary", required=False)
            if vocabulary_list:
                print(f"✓ Loaded {len(vocabulary_list)} vocabulary terms from Module {module_number}")
        except Exception as e:
            print(f"⚠️  Could not load vocabulary from Module {module_number}: {e}")

    if not vocabulary_list:
        print("⚠️  No vocabulary list found - skipping vocab formatting")
        return godot_data

    sequences = godot_data.get('sequences', [])

    for seq_idx, sequence in enumerate(sequences, 1):
        if '@type' not in sequence or sequence['@type'] != 'Sequence':
            continue

        steps = sequence.get('steps', [])

        for step_idx, step in enumerate(steps, 1):
            try:
                # Process dialogue (vocab only)
                if 'dialogue' in step and step['dialogue']:
                    step['dialogue'] = format_vocab_tags(step['dialogue'], vocabulary_list)

                # Process prompt if present
                if 'prompt' in step and step['prompt']:
                    prompt = step['prompt']

                    # Remediations (dialogue = vocab only)
                    for rem in prompt.get('remediations', []):
                        rem_step = rem.get('step', {})
                        if 'dialogue' in rem_step and rem_step['dialogue']:
                            rem_step['dialogue'] = format_vocab_tags(
                                rem_step['dialogue'],
                                vocabulary_list
                            )

                    # on_correct (dialogue = vocab only)
                    if 'on_correct' in prompt and prompt['on_correct'] is not None:
                        if 'dialogue' in prompt['on_correct'] and prompt['on_correct']['dialogue']:
                            prompt['on_correct']['dialogue'] = format_vocab_tags(
                                prompt['on_correct']['dialogue'],
                                vocabulary_list
                            )
            except Exception as e:
                print(f"⚠️  Error formatting vocab in step {step_idx} of sequence {seq_idx}: {e}")
                continue

    print(f"✓ Vocab formatting complete")
    return godot_data


def apply_fraction_formatting(godot_data, module_number=None):
    """
    Pipeline step: Apply fraction tags to all text in Godot sequences.
    Dialogue gets fractions with words, prompts/choices get fractions without words.

    Args:
        godot_data: Godot schema dict (with @type: "SequencePool" and sequences array)
        module_number: Module number (automatically passed by pipeline, not used)

    Returns:
        Modified godot_data with fraction tags applied

    Usage in pipeline (pipelines.json):
        {
            "name": "fraction_formatting",
            "type": "formatting",
            "function": "bbcode_formatter.apply_fraction_formatting",
            "description": "Apply fraction BBCode tags",
            "function_args": {},
            "output_file": "fraction_formatted.json"
        }
    """
    if not godot_data or '@type' not in godot_data:
        print("⚠️  Invalid Godot data structure - skipping fraction formatting")
        return godot_data

    sequences = godot_data.get('sequences', [])

    for seq_idx, sequence in enumerate(sequences, 1):
        if '@type' not in sequence or sequence['@type'] != 'Sequence':
            continue

        steps = sequence.get('steps', [])

        for step_idx, step in enumerate(steps, 1):
            try:
                # Process dialogue (fractions with words)
                if 'dialogue' in step and step['dialogue']:
                    step['dialogue'] = format_fractions_bbcode(
                        step['dialogue'],
                        "dialogue",
                        include_words=True
                    )

                # Process prompt if present
                if 'prompt' in step and step['prompt']:
                    prompt = step['prompt']

                    # Prompt text (fractions without words)
                    if 'text' in prompt and prompt['text']:
                        prompt['text'] = format_fractions_bbcode(
                            prompt['text'],
                            "prompt",
                            include_words=False
                        )

                    # Choices (fractions without words)
                    if 'choices' in prompt and prompt['choices'] is not None and 'options' in prompt['choices']:
                        prompt['choices']['options'] = [
                            format_fractions_bbcode(choice, "choice", include_words=False)
                            for choice in prompt['choices']['options']
                        ]

                    # Remediations (dialogue = fractions with words)
                    for rem in prompt.get('remediations', []):
                        rem_step = rem.get('step', {})
                        if 'dialogue' in rem_step and rem_step['dialogue']:
                            rem_step['dialogue'] = format_fractions_bbcode(
                                rem_step['dialogue'],
                                "remediation_dialogue",
                                include_words=True
                            )

                    # on_correct (dialogue = fractions with words)
                    if 'on_correct' in prompt and prompt['on_correct'] is not None:
                        if 'dialogue' in prompt['on_correct'] and prompt['on_correct']['dialogue']:
                            prompt['on_correct']['dialogue'] = format_fractions_bbcode(
                                prompt['on_correct']['dialogue'],
                                "on_correct_dialogue",
                                include_words=True
                            )
            except Exception as e:
                print(f"⚠️  Error formatting fractions in step {step_idx} of sequence {seq_idx}: {e}")
                continue

    print(f"[OK] Fraction formatting complete")
    return godot_data


# ============================================================================
# TESTING
# ============================================================================

def test_bbcode_formatter():
    """Quick test of BBCode formatting functions"""

    print("\n" + "=" * 70)
    print("BBCODE FORMATTER TESTS")
    print("=" * 70)

    # Test 1: Fraction Formatting (with words)
    print("\n1. Testing format_fractions_bbcode() with words:")
    print("-" * 70)

    dialogue = "Shade 3/4 of the rectangle and 1/2 of the circle."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")

    # Test 2: Fraction Formatting (without words)
    print("\n2. Testing format_fractions_bbcode() without words:")
    print("-" * 70)

    prompt = "Shade 3/4"
    result = format_fractions_bbcode(prompt, "prompt", include_words=False)
    print(f"Input:  {prompt}")
    print(f"Output: {result}")

    # Test 3: Vocab Tags with Auto-Removal
    print("\n3. Testing format_vocab_tags() with auto-removal:")
    print("-" * 70)

    vocab_list = ["partition", "equal parts", "shade"]
    text_with_old_tags = "[vocab]old word[/vocab] partition this shape into equal parts and shade it."
    result = format_vocab_tags(text_with_old_tags, vocab_list)
    print(f"Vocab:  {vocab_list}")
    print(f"Input:  {text_with_old_tags}")
    print(f"Output: {result}")

    # Test 4: Combined (Fractions + Vocab)
    print("\n4. Testing combined formatting (fractions + vocab):")
    print("-" * 70)

    dialogue = "Shade 3/4 of the bar using equal parts."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    result = format_vocab_tags(result, vocab_list)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")

    print("\n" + "=" * 70)
    print("ALL TESTS COMPLETED")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    test_bbcode_formatter()