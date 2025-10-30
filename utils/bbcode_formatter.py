"""
BBCode Formatter Utility
Deterministic post-processing for Godot sequences after AI transformation

Handles:
1. Fraction formatting with [fraction numerator=N denominator=D]words[/fraction]
2. Vocabulary tagging with [vocab]term[/vocab] (dialogue only)
"""

import re
import json


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

def add_vocab_tags(text, vocabulary_list):
    """
    Wrap vocabulary terms with [vocab] tags.
    Only applies to dialogue text.
    
    Args:
        text: String to process
        vocabulary_list: List of vocabulary terms (strings or list)
    
    Returns:
        String with vocab tags added
    
    Examples:
        >>> add_vocab_tags("partition the bar into equal parts", ["partition", "equal parts"])
        "[vocab]partition[/vocab] the bar into [vocab]equal parts[/vocab]"
    """
    if not text or not vocabulary_list:
        return text
    
    # Convert to list if comma-separated string
    if isinstance(vocabulary_list, str):
        vocabulary_list = [term.strip() for term in vocabulary_list.split(',')]
    
    # Sort by length (longest first) to avoid partial matches
    # e.g., "equal parts" before "equal" to avoid "[vocab]equal[/vocab] parts"
    sorted_vocab = sorted(vocabulary_list, key=len, reverse=True)
    
    result = text
    for term in sorted_vocab:
        if not term:
            continue
        
        # Skip if already tagged
        if f"[vocab]{term}[/vocab]" in result:
            continue
        
        # Skip if inside BBCode tags (avoid breaking [fraction]...[/fraction])
        # Simple heuristic: don't tag if between [ and ]
        if re.search(r'\[.*' + re.escape(term) + r'.*\]', result):
            continue
        
        # Case-sensitive whole-word matching
        # Use word boundaries for whole words
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
                        step['dialogue'] = add_vocab_tags(step['dialogue'], vocabulary_list)
                
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
                        choices = prompt['choices']['options']
                        prompt['choices']['options'] = [
                            format_fractions_bbcode(choice, "choice", include_words=False)
                            for choice in choices
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
                                rem_step['dialogue'] = add_vocab_tags(
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
                                prompt['on_correct']['dialogue'] = add_vocab_tags(
                                    prompt['on_correct']['dialogue'], 
                                    vocabulary_list
                                )
            except Exception as e:
                print(f"⚠️  Error formatting step {step_idx} in sequence {seq_idx}: {e}")
                continue
    
    return godot_data


# ============================================================================
# TESTING
# ============================================================================

def test_bbcode_formatter():
    """Quick test of BBCode formatting functions"""
    
    print("Testing Fraction Formatting:")
    print("=" * 70)
    
    # Test dialogue (with words)
    dialogue = "Shade 3/4 of the rectangle and 1/2 of the circle."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")
    print()
    
    # Test prompt (no words)
    prompt = "Shade 3/4"
    result = format_fractions_bbcode(prompt, "prompt", include_words=False)
    print(f"Input:  {prompt}")
    print(f"Output: {result}")
    print()
    
    # Test vocab tagging
    print("Testing Vocabulary Tagging:")
    print("=" * 70)
    
    vocab_list = ["partition", "equal parts", "shade"]
    dialogue = "Let's partition this shape into equal parts and shade 2 sections."
    result = add_vocab_tags(dialogue, vocab_list)
    print(f"Vocab:  {vocab_list}")
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")
    print()
    
    # Test combined
    print("Testing Combined (Fractions + Vocab):")
    print("=" * 70)
    
    dialogue = "Shade 3/4 of the bar using equal parts."
    result = format_fractions_bbcode(dialogue, "dialogue", include_words=True)
    result = add_vocab_tags(result, vocab_list)
    print(f"Input:  {dialogue}")
    print(f"Output: {result}")


if __name__ == "__main__":
    test_bbcode_formatter()