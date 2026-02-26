"""
Template Filter - Filters problem templates based on criteria

Can be used as:
1. Standalone script: python steps/formatting/template_filter.py
2. Pipeline formatting step: filters templates before generation
"""
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


def filter_templates(
    templates: List[Dict[str, Any]],
    include_template_ids: Optional[List[str]] = None,
    exclude_template_ids: Optional[List[str]] = None,
    include_skill_ids: Optional[List[str]] = None,
    exclude_skill_ids: Optional[List[str]] = None,
    include_mastery_verbs: Optional[List[str]] = None,
    exclude_mastery_verbs: Optional[List[str]] = None,
    include_tiers: Optional[List[str]] = None,
    exclude_tiers: Optional[List[str]] = None,
    verbose: bool = False
) -> List[Dict[str, Any]]:
    """
    Filter templates based on multiple criteria.

    Args:
        templates: List of template dictionaries
        include_template_ids: Only keep these template IDs (e.g., ["4010", "4011"])
        exclude_template_ids: Remove these template IDs
        include_skill_ids: Only keep these skill IDs (e.g., ["M4-07", "M4-10"])
        exclude_skill_ids: Remove these skill IDs
        include_mastery_verbs: Only keep these mastery verbs (e.g., ["CREATE", "IDENTIFY"])
        exclude_mastery_verbs: Remove these mastery verbs
        include_tiers: Only keep these tiers (e.g., ["BASELINE", "STRETCH"])
        exclude_tiers: Remove these tiers
        verbose: Print filtering details

    Returns:
        Filtered list of templates

    Examples:
        >>> # Keep only specific templates
        >>> filter_templates(templates, include_template_ids=["4010", "4013"])

        >>> # Exclude specific skill
        >>> filter_templates(templates, exclude_skill_ids=["M7-04"])

        >>> # Only BASELINE tier CREATE/IDENTIFY problems
        >>> filter_templates(templates,
        ...     include_mastery_verbs=["CREATE", "IDENTIFY"],
        ...     include_tiers=["BASELINE"])
    """
    if verbose:
        print(f"Starting with {len(templates)} templates")

    filtered = templates.copy()

    # Apply include filters (whitelist)
    if include_template_ids:
        filtered = [t for t in filtered if t.get('template_id') in include_template_ids]
        if verbose:
            print(f"  After include_template_ids filter: {len(filtered)} templates")

    if include_skill_ids:
        filtered = [t for t in filtered if t.get('skill_id') in include_skill_ids]
        if verbose:
            print(f"  After include_skill_ids filter: {len(filtered)} templates")

    if include_mastery_verbs:
        filtered = [t for t in filtered if t.get('mastery_verb') in include_mastery_verbs]
        if verbose:
            print(f"  After include_mastery_verbs filter: {len(filtered)} templates")

    if include_tiers:
        # Handle both single tier and array of tiers
        def has_tier(template):
            tiers = template.get('mastery_tier')
            if isinstance(tiers, list):
                return any(tier in include_tiers for tier in tiers)
            return tiers in include_tiers

        filtered = [t for t in filtered if has_tier(t)]
        if verbose:
            print(f"  After include_tiers filter: {len(filtered)} templates")

    # Apply exclude filters (blacklist)
    if exclude_template_ids:
        filtered = [t for t in filtered if t.get('template_id') not in exclude_template_ids]
        if verbose:
            print(f"  After exclude_template_ids filter: {len(filtered)} templates")

    if exclude_skill_ids:
        filtered = [t for t in filtered if t.get('skill_id') not in exclude_skill_ids]
        if verbose:
            print(f"  After exclude_skill_ids filter: {len(filtered)} templates")

    if exclude_mastery_verbs:
        filtered = [t for t in filtered if t.get('mastery_verb') not in exclude_mastery_verbs]
        if verbose:
            print(f"  After exclude_mastery_verbs filter: {len(filtered)} templates")

    if exclude_tiers:
        # Handle both single tier and array of tiers
        def has_excluded_tier(template):
            tiers = template.get('mastery_tier')
            if isinstance(tiers, list):
                return any(tier in exclude_tiers for tier in tiers)
            return tiers in exclude_tiers

        filtered = [t for t in filtered if not has_excluded_tier(t)]
        if verbose:
            print(f"  After exclude_tiers filter: {len(filtered)} templates")

    if verbose:
        removed_count = len(templates) - len(filtered)
        print(f"\nFiltered: {removed_count} removed, {len(filtered)} remaining")

        if removed_count > 0:
            removed_ids = set(t.get('template_id') for t in templates) - set(t.get('template_id') for t in filtered)
            print(f"Removed template IDs: {sorted(removed_ids)}")

    return filtered


# ============================================================================
# COMMAND-LINE INTERFACE
# ============================================================================

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Filter problem templates based on criteria",
        epilog="""
Examples:
  # Exclude specific template
  python steps/formatting/template_filter.py modules/module7/problem_templates.json \\
    --exclude-template-ids 7010 \\
    -o modules/module7/problem_templates_filtered.json

  # Only keep BASELINE tier
  python steps/formatting/template_filter.py modules/module7/problem_templates.json \\
    --include-tiers BASELINE

  # Exclude specific skill
  python steps/formatting/template_filter.py modules/module7/problem_templates.json \\
    --exclude-skill-ids M7-04

  # Multiple filters
  python steps/formatting/template_filter.py modules/module7/problem_templates.json \\
    --include-mastery-verbs CREATE IDENTIFY \\
    --exclude-tiers CHALLENGE
        """
    )

    parser.add_argument(
        "input_file",
        help="Path to problem_templates.json file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: overwrites input)"
    )
    parser.add_argument(
        "--include-template-ids",
        nargs="+",
        help="Only keep these template IDs"
    )
    parser.add_argument(
        "--exclude-template-ids",
        nargs="+",
        help="Remove these template IDs"
    )
    parser.add_argument(
        "--include-skill-ids",
        nargs="+",
        help="Only keep these skill IDs"
    )
    parser.add_argument(
        "--exclude-skill-ids",
        nargs="+",
        help="Remove these skill IDs"
    )
    parser.add_argument(
        "--include-mastery-verbs",
        nargs="+",
        help="Only keep these mastery verbs (CREATE, IDENTIFY, COMPARE, APPLY)"
    )
    parser.add_argument(
        "--exclude-mastery-verbs",
        nargs="+",
        help="Remove these mastery verbs"
    )
    parser.add_argument(
        "--include-tiers",
        nargs="+",
        help="Only keep these tiers (SUPPORT, CONFIDENCE, BASELINE, STRETCH, CHALLENGE)"
    )
    parser.add_argument(
        "--exclude-tiers",
        nargs="+",
        help="Remove these tiers"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show filtering details"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be filtered without writing"
    )

    args = parser.parse_args()

    # Read input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)

    print(f"Loaded {len(templates)} templates from {input_path}")

    # Apply filters
    filtered = filter_templates(
        templates,
        include_template_ids=args.include_template_ids,
        exclude_template_ids=args.exclude_template_ids,
        include_skill_ids=args.include_skill_ids,
        exclude_skill_ids=args.exclude_skill_ids,
        include_mastery_verbs=args.include_mastery_verbs,
        exclude_mastery_verbs=args.exclude_mastery_verbs,
        include_tiers=args.include_tiers,
        exclude_tiers=args.exclude_tiers,
        verbose=args.verbose or args.dry_run
    )

    # Write output
    if not args.dry_run:
        output_path = Path(args.output) if args.output else input_path

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(filtered, f, indent=2, ensure_ascii=False)

        print(f"\nSaved {len(filtered)} filtered templates to {output_path}")
    else:
        print("\n[DRY RUN] No files modified")
        print(f"Would save {len(filtered)} templates")
