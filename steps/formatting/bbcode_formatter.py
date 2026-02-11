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
import os
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.module_utils import get_module_field


# ============================================================================
# FRACTION WORD CONVERSION
# ============================================================================

def _number_to_word(n):
    """Convert a number to its word form (1 -> 'one', 2 -> 'two', etc.)"""
    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"
    }

    try:
        num = int(n)
        if num in words:
            return words[num]
        # For numbers > 20, we can extend this if needed
        return str(num)
    except (ValueError, TypeError):
        return str(n)


def _denominator_to_word(n, is_unit_fraction=False):
    """
    Convert a denominator to its ordinal form (singular or plural).

    Args:
        n: The denominator number
        is_unit_fraction: If True, use singular form (e.g., 'third' not 'thirds')

    Examples:
        _denominator_to_word(3, is_unit_fraction=True) -> 'third'
        _denominator_to_word(3, is_unit_fraction=False) -> 'thirds'
        _denominator_to_word(2, is_unit_fraction=True) -> 'half'
        _denominator_to_word(2, is_unit_fraction=False) -> 'halves'
    """
    # Singular forms (for unit fractions)
    ordinal_singular = {
        2: "half",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
        13: "thirteenth",
        14: "fourteenth",
        15: "fifteenth",
        16: "sixteenth",
        17: "seventeenth",
        18: "eighteenth",
        19: "nineteenth",
        20: "twentieth"
    }

    # Plural forms (for non-unit fractions)
    ordinal_plural = {
        2: "halves",
        3: "thirds",
        4: "fourths",
        5: "fifths",
        6: "sixths",
        7: "sevenths",
        8: "eighths",
        9: "ninths",
        10: "tenths",
        11: "elevenths",
        12: "twelfths",
        13: "thirteenths",
        14: "fourteenths",
        15: "fifteenths",
        16: "sixteenths",
        17: "seventeenths",
        18: "eighteenths",
        19: "nineteenths",
        20: "twentieths"
    }

    try:
        denom = int(n)
        if is_unit_fraction:
            if denom in ordinal_singular:
                return ordinal_singular[denom]
            return f"{denom}th"
        else:
            if denom in ordinal_plural:
                return ordinal_plural[denom]
            return f"{denom}ths"
    except (ValueError, TypeError):
        return f"{n}th" if is_unit_fraction else f"{n}ths"


# ============================================================================
# DEBUG LOGGING HELPERS
# ============================================================================

class FormattingLogger:
    """Tracks and logs formatting changes"""
    def __init__(self, enabled=False):
        self.enabled = enabled
        self.changes = []
        self.vocab_words_added = set()  # Track unique vocab words added

    def log_change(self, location, field_type, original, formatted, change_type):
        """Log a formatting change"""
        if not self.enabled or original == formatted:
            return

        self.changes.append({
            'location': location,
            'field_type': field_type,
            'original': original,
            'formatted': formatted,
            'change_type': change_type
        })

        # Extract vocab words that were added
        if change_type == 'vocab':
            vocab_pattern = r'\[vocab\](.*?)\[/vocab\]'
            added_words = re.findall(vocab_pattern, formatted)
            self.vocab_words_added.update(added_words)

        print(f"\n[DEBUG] {change_type.upper()} - {location} ({field_type})")
        print(f"  BEFORE: {original}")
        print(f"  AFTER:  {formatted}")

    def summary(self):
        """Print summary of all changes"""
        if not self.enabled or not self.changes:
            return

        print(f"\n{'='*70}")
        print(f"FORMATTING SUMMARY: {len(self.changes)} changes made")
        print(f"{'='*70}")

        vocab_changes = [c for c in self.changes if c['change_type'] == 'vocab']
        fraction_changes = [c for c in self.changes if c['change_type'] == 'fraction']

        if vocab_changes:
            print(f"\n[OK] Vocabulary tags: {len(vocab_changes)} fields modified")
            if self.vocab_words_added:
                sorted_vocab = sorted(self.vocab_words_added)
                print(f"  Vocab words added: {', '.join(sorted_vocab)}")
        if fraction_changes:
            print(f"[OK] Fraction tags: {len(fraction_changes)} fields modified")


# ============================================================================
# FRACTION BBCODE FORMATTING
# ============================================================================

def format_fractions_bbcode(text, context_type, include_words=True):
    """
    Format fractions with BBCode tags.

    Dynamically converts fractions like "6/5" to:
    [fraction numerator=6 denominator=5]six fifths[/fraction]

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

        >>> format_fractions_bbcode("Place 6/5", "dialogue", True)
        "Place [fraction numerator=6 denominator=5]six fifths[/fraction]"

        >>> format_fractions_bbcode("3/4", "choice", False)
        "[fraction numerator=3 denominator=4][/fraction]"
    """
    if not text or not isinstance(text, str):
        return text

    def replace_fraction(match):
        numerator = match.group(1)
        denominator = match.group(2)

        if include_words:
            # For dialogue - dynamically generate spoken words
            numerator_word = _number_to_word(numerator)
            # Use singular form for unit fractions (numerator = 1)
            is_unit_fraction = (numerator == "1")
            denominator_word = _denominator_to_word(denominator, is_unit_fraction=is_unit_fraction)
            words = f"{numerator_word} {denominator_word}"
            return f"[fraction numerator={numerator} denominator={denominator}]{words}[/fraction]"
        else:
            # For prompts/choices - no words, just BBCode wrapper
            return f"[fraction numerator={numerator} denominator={denominator}][/fraction]"

    # Match fractions like 1/2, 3/4, 12/16, etc.
    # Use word boundaries to avoid matching non-fractions
    pattern = r'\b(\d+)/(\d+)\b'
    formatted = re.sub(pattern, replace_fraction, text)

    return formatted


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
        # Check if term is between an opening tag [tag] and closing tag [/tag]
        escaped_term = re.escape(term)
        # Match: [tag_name]...term...[/tag_name] or [tag_name attr=val]...term...[/tag_name]
        if re.search(r'\[(?!\/)[^\]]+\][^[]*\b' + escaped_term + r'\b[^\]]*\[\/[^\]]+\]', result):
            continue

        # Build pattern with word boundaries
        # Don't use \b at the end if term ends with non-word character (like hyphen)
        if re.search(r'\w$', term):
            # Term ends with word character - use boundaries on both sides
            pattern = r'\b' + escaped_term + r'\b'
        else:
            # Term ends with non-word character - only use boundary at start
            pattern = r'\b' + escaped_term

        # Replace ALL occurrences with case-preserving replacement
        # Use a function to preserve the original case from the matched text
        def replace_with_vocab(match):
            matched_text = match.group(0)  # Preserve original case
            return f"[vocab]{matched_text}[/vocab]"

        result = re.sub(pattern, replace_with_vocab, result, flags=re.IGNORECASE)

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

    # Initialize logger
    logger = FormattingLogger()

    # Load vocabulary from module
    vocabulary_list = None
    if module_number:
        try:
            vocabulary_list = get_module_field(module_number, "vocabulary", required=False)
            if vocabulary_list:
                print(f"✓ Loaded {len(vocabulary_list)} vocabulary terms from Module {module_number}")
                if logger.enabled:
                    print(f"  Terms: {', '.join(vocabulary_list[:10])}{'...' if len(vocabulary_list) > 10 else ''}")
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
                location = f"Seq{seq_idx}/Step{step_idx}"

                # Process dialogue (vocab only)
                if 'dialogue' in step and step['dialogue']:
                    original = step['dialogue']
                    step['dialogue'] = format_vocab_tags(step['dialogue'], vocabulary_list)
                    logger.log_change(location, 'dialogue', original, step['dialogue'], 'vocab')

                # Process prompt if present
                if 'prompt' in step and step['prompt']:
                    prompt = step['prompt']

                    # Remediations (dialogue = vocab only)
                    for rem_idx, rem in enumerate(prompt.get('remediations', []), 1):
                        rem_step = rem.get('step', {})
                        if 'dialogue' in rem_step and rem_step['dialogue']:
                            original = rem_step['dialogue']
                            rem_step['dialogue'] = format_vocab_tags(
                                rem_step['dialogue'],
                                vocabulary_list
                            )
                            logger.log_change(
                                f"{location}/Rem{rem_idx}",
                                'remediation.dialogue',
                                original,
                                rem_step['dialogue'],
                                'vocab'
                            )

                    # on_correct (dialogue = vocab only)
                    if 'on_correct' in prompt and prompt['on_correct'] is not None:
                        if 'dialogue' in prompt['on_correct'] and prompt['on_correct']['dialogue']:
                            original = prompt['on_correct']['dialogue']
                            prompt['on_correct']['dialogue'] = format_vocab_tags(
                                prompt['on_correct']['dialogue'],
                                vocabulary_list
                            )
                            logger.log_change(
                                location,
                                'on_correct.dialogue',
                                original,
                                prompt['on_correct']['dialogue'],
                                'vocab'
                            )
            except Exception as e:
                print(f"⚠️  Error formatting vocab in step {step_idx} of sequence {seq_idx}: {e}")
                continue

    logger.summary()
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

    # Initialize logger
    logger = FormattingLogger()

    sequences = godot_data.get('sequences', [])

    for seq_idx, sequence in enumerate(sequences, 1):
        if '@type' not in sequence or sequence['@type'] != 'Sequence':
            continue

        steps = sequence.get('steps', [])

        for step_idx, step in enumerate(steps, 1):
            try:
                location = f"Seq{seq_idx}/Step{step_idx}"

                # Process dialogue (fractions with words)
                if 'dialogue' in step and step['dialogue']:
                    original = step['dialogue']
                    step['dialogue'] = format_fractions_bbcode(
                        step['dialogue'],
                        "dialogue",
                        include_words=True
                    )
                    logger.log_change(location, 'dialogue', original, step['dialogue'], 'fraction')

                # Process prompt if present
                if 'prompt' in step and step['prompt']:
                    prompt = step['prompt']

                    # Prompt text (fractions without words)
                    if 'text' in prompt and prompt['text']:
                        original = prompt['text']
                        prompt['text'] = format_fractions_bbcode(
                            prompt['text'],
                            "prompt",
                            include_words=False
                        )
                        logger.log_change(location, 'prompt.text', original, prompt['text'], 'fraction')

                    # Choices (fractions without words)
                    if 'choices' in prompt and prompt['choices'] is not None and 'options' in prompt['choices']:
                        original_choices = prompt['choices']['options'][:]
                        prompt['choices']['options'] = [
                            format_fractions_bbcode(choice, "choice", include_words=False)
                            for choice in prompt['choices']['options']
                        ]
                        for choice_idx, (orig, new) in enumerate(zip(original_choices, prompt['choices']['options']), 1):
                            logger.log_change(
                                f"{location}/Choice{choice_idx}",
                                'prompt.choices.option',
                                orig,
                                new,
                                'fraction'
                            )

                    # Remediations (dialogue = fractions with words)
                    for rem_idx, rem in enumerate(prompt.get('remediations', []), 1):
                        rem_step = rem.get('step', {})
                        if 'dialogue' in rem_step and rem_step['dialogue']:
                            original = rem_step['dialogue']
                            rem_step['dialogue'] = format_fractions_bbcode(
                                rem_step['dialogue'],
                                "remediation_dialogue",
                                include_words=True
                            )
                            logger.log_change(
                                f"{location}/Rem{rem_idx}",
                                'remediation.dialogue',
                                original,
                                rem_step['dialogue'],
                                'fraction'
                            )

                    # on_correct (dialogue = fractions with words)
                    if 'on_correct' in prompt and prompt['on_correct'] is not None:
                        if 'dialogue' in prompt['on_correct'] and prompt['on_correct']['dialogue']:
                            original = prompt['on_correct']['dialogue']
                            prompt['on_correct']['dialogue'] = format_fractions_bbcode(
                                prompt['on_correct']['dialogue'],
                                "on_correct_dialogue",
                                include_words=True
                            )
                            logger.log_change(
                                location,
                                'on_correct.dialogue',
                                original,
                                prompt['on_correct']['dialogue'],
                                'fraction'
                            )
            except Exception as e:
                print(f"⚠️  Error formatting fractions in step {step_idx} of sequence {seq_idx}: {e}")
                continue

    logger.summary()
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

    # Test 1: Fraction Formatting (with words) - common fractions
    print("\n1. Testing format_fractions_bbcode() with words (common fractions):")
    print("-" * 70)

    dialogue = "Shade 3/4 of the rectangle and 1/2 of the circle."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")

    # Test 1b: Unit fractions (singular form)
    print("\n1b. Testing unit fractions (special singular form):")
    print("-" * 70)

    dialogue = "Place 1/3 and 1/5 on the number line."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")
    print(f"Note:   'one third' (singular) not 'one thirds' (plural)")

    # Test 1c: Dynamic conversion for improper fractions
    print("\n1c. Testing dynamic conversion for improper fractions:")
    print("-" * 70)

    dialogue = "Place 6/5 and 8/3 on the number line."
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