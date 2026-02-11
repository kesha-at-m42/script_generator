"""
Summary Generator - Adds statistical summary to SequencePool
"""

from collections import Counter
from typing import Dict, List, Any


def generate_summary(sequences: List[Dict]) -> Dict:
    """
    Generate a summary of sequences based on current metadata structure

    Counts sequences by:
    - mastery_tier (BASELINE, STRETCH, CHALLENGE, etc.)
    - template_id
    - mastery_verb / cognitive_verb
    - mastery_skill_id
    - misconceptions (both ID and tags)

    Also detects:
    - Missing sequence IDs (gaps in numbering)
    """
    summary = {
        'total_sequences': len(sequences),
        'by_mastery_tier': {},
        'by_template_id': {},
        'by_mastery_verb': {},
        'by_cognitive_verb': {},
        'by_mastery_skill_id': {},
        'by_misconception_id': {},
        'by_misconception_tag': {},
        'by_tier_and_verb': {},
        'matched': 0,
        'unmatched': 0,
        'unmatched_indices': [],
        'missing_ids': [],
        'id_range': {}
    }

    # Collect all problem_ids to detect gaps
    problem_ids = []
    for seq in sequences:
        metadata = seq.get('metadata', {})
        problem_id = metadata.get('problem_id') or seq.get('problem_id')
        if problem_id is not None:
            problem_ids.append(int(problem_id))

    # Detect missing IDs
    if problem_ids:
        problem_ids_sorted = sorted(problem_ids)
        min_id = problem_ids_sorted[0]
        max_id = problem_ids_sorted[-1]
        expected_ids = set(range(min_id, max_id + 1))
        actual_ids = set(problem_ids)
        missing = sorted(expected_ids - actual_ids)

        summary['missing_ids'] = missing
        summary['id_range'] = {
            'min': min_id,
            'max': max_id,
            'expected_count': max_id - min_id + 1,
            'actual_count': len(problem_ids),
            'missing_count': len(missing)
        }

    for idx, seq in enumerate(sequences):
        metadata = seq.get('metadata', {})

        if not metadata:
            summary['unmatched'] += 1
            # Try to get problem_id from root level, fallback to index
            problem_id = seq.get('problem_id', idx)
            summary['unmatched_indices'].append(problem_id)
            continue

        summary['matched'] += 1

        # Count by mastery_tier
        tier = metadata.get('mastery_tier', 'UNKNOWN')
        summary['by_mastery_tier'][tier] = summary['by_mastery_tier'].get(tier, 0) + 1

        # Count by template_id
        template_id = metadata.get('template_id', 'UNKNOWN')
        summary['by_template_id'][template_id] = summary['by_template_id'].get(template_id, 0) + 1

        # Count by mastery_verb
        mastery_verb = metadata.get('mastery_verb', 'UNKNOWN')
        summary['by_mastery_verb'][mastery_verb] = summary['by_mastery_verb'].get(mastery_verb, 0) + 1

        # Count by cognitive_verb from telemetry_data
        telemetry = metadata.get('telemetry_data', {})
        cognitive_verb = telemetry.get('cognitive_verb', 'UNKNOWN')
        summary['by_cognitive_verb'][cognitive_verb] = summary['by_cognitive_verb'].get(cognitive_verb, 0) + 1

        # Count by mastery_skill_id
        skill_id = telemetry.get('mastery_skill_id', 'UNKNOWN')
        summary['by_mastery_skill_id'][skill_id] = summary['by_mastery_skill_id'].get(skill_id, 0) + 1

        # Count by misconception_id (expand arrays)
        misconception_ids = telemetry.get('misconception_id', [])
        for misc_id in misconception_ids:
            key = str(misc_id)
            summary['by_misconception_id'][key] = summary['by_misconception_id'].get(key, 0) + 1

        # Count by misconception_tag (expand arrays)
        misconception_tags = telemetry.get('misconception_tag', [])
        for tag in misconception_tags:
            summary['by_misconception_tag'][tag] = summary['by_misconception_tag'].get(tag, 0) + 1

        # Count by tier and verb combination
        combo_key = f"{tier} - {cognitive_verb}"
        summary['by_tier_and_verb'][combo_key] = summary['by_tier_and_verb'].get(combo_key, 0) + 1

    return summary


def add_summary(data, module_number=None, path_letter=None):
    """
    Add summary metadata to SequencePool

    Args:
        data: SequencePool dict with sequences array
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        SequencePool dict with metadata field added
    """
    # Validate input structure
    if not isinstance(data, dict) or "@type" not in data or data["@type"] != "SequencePool":
        raise ValueError("Expected SequencePool structure with @type and sequences")

    sequences = data.get("sequences", [])

    # Generate summary
    summary = generate_summary(sequences)

    # Add summary to data (after @type)
    result = {
        "@type": data["@type"],
        "metadata": summary
    }

    # Add remaining fields
    for key, value in data.items():
        if key not in ("@type", "metadata"):
            result[key] = value

    return result
