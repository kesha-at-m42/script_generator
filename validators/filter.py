"""
QA Filter - Orchestrates validation and filtering of pipeline outputs
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple

from .system_validator import SystemValidator
from .ai_validator import AIValidator


class QAFilter:
    """
    Orchestrates validation and filtering of items through the pipeline

    Process:
    1. System validation (fast, structural checks)
    2. AI validation (semantic quality checks) - only on items that pass system validation
    3. Composite scoring (30% system, 70% AI)
    4. Filtering (keep top N% or top N items)
    """

    def __init__(self, module_data: dict, verbose: bool = False):
        self.module_data = module_data
        self.verbose = verbose
        self.system_validator = SystemValidator(verbose=verbose)
        self.ai_validator = AIValidator(verbose=verbose)

    def validate_and_filter(
        self,
        items: List[dict],
        validation_type: str,
        filter_strategy: str = "top_percent",
        filter_value: float = 0.5,  # Keep top 50% by default
        min_score_threshold: float = 50.0  # Minimum composite score
    ) -> Tuple[List[dict], Dict]:
        """
        Validate items and filter to keep only high-quality ones

        Args:
            items: List of items to validate
            validation_type: 'question' or 'interaction'
            filter_strategy: 'top_percent', 'top_count', or 'threshold'
            filter_value:
                - For 'top_percent': 0.0-1.0 (e.g., 0.5 = keep top 50%)
                - For 'top_count': integer (e.g., 10 = keep top 10 items)
                - For 'threshold': minimum score (e.g., 70 = keep all above 70)
            min_score_threshold: Absolute minimum score to keep any item

        Returns:
            (filtered_items, report)
        """
        if not items:
            return [], {'total': 0, 'filtered': 0, 'removed': 0}

        if self.verbose:
            print(f"\n{'='*70}")
            print(f"QA FILTER: {validation_type.upper()}")
            print(f"{'='*70}")
            print(f"  Input items: {len(items)}")
            print(f"  Filter strategy: {filter_strategy}")
            print(f"  Filter value: {filter_value}")

        # Step 1: System validation
        if self.verbose:
            print(f"\n  Step 1: System Validation")

        system_results = self.system_validator.validate_batch(
            items, validation_type, self.module_data
        )

        # Only pass items that passed system validation to AI
        passed_system = [
            r for r in system_results['results'] if r['is_valid']
        ]

        if self.verbose:
            print(f"    → {len(passed_system)} items passed system validation")

        if not passed_system:
            if self.verbose:
                print(f"  ⚠️  No items passed system validation!")
            return [], {
                'total': len(items),
                'filtered': 0,
                'removed': len(items),
                'system_validation': system_results,
                'ai_validation': None
            }

        # Step 2: AI validation (only on items that passed system checks)
        if self.verbose:
            print(f"\n  Step 2: AI Validation")

        ai_items = [r['item'] for r in passed_system]
        ai_results = self.ai_validator.validate_batch(
            ai_items, validation_type, self.module_data
        )

        # Step 3: Composite scoring
        if self.verbose:
            print(f"\n  Step 3: Composite Scoring (30% system, 70% AI)")

        scored_items = []
        for sys_result in passed_system:
            item = sys_result['item']

            # Find corresponding AI result
            ai_result = next(
                (r for r in ai_results['results'] if r['item'] == item),
                None
            )

            if ai_result:
                # Composite score: 30% system, 70% AI
                composite_score = (0.3 * sys_result['score']) + (0.7 * ai_result['score'])

                scored_items.append({
                    'item': item,
                    'composite_score': composite_score,
                    'system_score': sys_result['score'],
                    'ai_score': ai_result['score'],
                    'system_issues': sys_result.get('issues', []),
                    'ai_details': ai_result.get('details', {}),
                    'is_valid': ai_result['is_valid'] and composite_score >= min_score_threshold
                })

        # Sort by composite score (highest first)
        scored_items.sort(key=lambda x: x['composite_score'], reverse=True)

        # Step 4: Apply filtering strategy
        if self.verbose:
            print(f"\n  Step 4: Filtering")

        if filter_strategy == "top_percent":
            keep_count = max(1, int(len(scored_items) * filter_value))
            filtered_items = scored_items[:keep_count]
        elif filter_strategy == "top_count":
            keep_count = min(int(filter_value), len(scored_items))
            filtered_items = scored_items[:keep_count]
        elif filter_strategy == "threshold":
            filtered_items = [
                item for item in scored_items
                if item['composite_score'] >= filter_value
            ]
        else:
            raise ValueError(f"Unknown filter strategy: {filter_strategy}")

        # Only keep items that are marked as valid
        filtered_items = [item for item in filtered_items if item['is_valid']]

        if self.verbose:
            print(f"    Kept: {len(filtered_items)} items")
            print(f"    Removed: {len(scored_items) - len(filtered_items)} items")

            if filtered_items:
                avg_score = sum(item['composite_score'] for item in filtered_items) / len(filtered_items)
                print(f"    Avg score of kept items: {avg_score:.1f}/100")
                print(f"    Score range: {filtered_items[-1]['composite_score']:.1f} - {filtered_items[0]['composite_score']:.1f}")

        # Extract just the items (without scoring metadata)
        final_items = [item['item'] for item in filtered_items]

        report = {
            'total': len(items),
            'filtered': len(final_items),
            'removed': len(items) - len(final_items),
            'system_validation': system_results,
            'ai_validation': ai_results,
            'scored_items': scored_items,  # Full scoring details
            'filter_strategy': filter_strategy,
            'filter_value': filter_value
        }

        return final_items, report

    def save_report(self, report: Dict, output_path: Path):
        """Save detailed validation report to file"""
        # Create a simplified version for JSON serialization
        simplified_report = {
            'summary': {
                'total_items': report['total'],
                'items_kept': report['filtered'],
                'items_removed': report['removed'],
                'filter_strategy': report.get('filter_strategy'),
                'filter_value': report.get('filter_value')
            },
            'system_validation': {
                'total': report['system_validation']['total'],
                'valid': report['system_validation']['valid'],
                'invalid': report['system_validation']['invalid']
            },
            'ai_validation': {
                'total': report['ai_validation']['total'],
                'valid': report['ai_validation']['valid'],
                'invalid': report['ai_validation']['invalid']
            } if report['ai_validation'] else None,
            'item_scores': [
                {
                    'item_id': item.get('item', {}).get('question_id') or item.get('item', {}).get('sequence_id', 'unknown'),
                    'composite_score': item['composite_score'],
                    'system_score': item['system_score'],
                    'ai_score': item['ai_score'],
                    'is_valid': item['is_valid'],
                    'system_issues': item['system_issues'],
                    'ai_summary': item['ai_details'].get('summary', 'N/A')
                }
                for item in report.get('scored_items', [])
            ]
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(simplified_report, f, indent=2)

        if self.verbose:
            print(f"  ✓ Validation report saved to: {output_path}")
