"""
Batch Processor - Handles batch mode item processing
"""

from pathlib import Path
from typing import List, Dict, Any
import json


class BatchProcessor:
    """Manages batch processing of items"""

    def __init__(
        self,
        items: List[Dict],
        batch_id_field: str,
        batch_id_start: int,
        batch_output_id_field: str = None,
        batch_only_items: List[str] = None,
        batch_skip_items: List[str] = None,
        batch_skip_existing: bool = False,
        items_dir: Path = None
    ):
        """
        Args:
            items: List of items to process
            batch_id_field: Field to use as item ID
            batch_id_start: Starting number for sequential output IDs
            batch_output_id_field: Field to add sequential IDs to
            batch_only_items: Only process these item IDs
            batch_skip_items: Skip these item IDs
            batch_skip_existing: Skip items that already have output
            items_dir: Directory where item outputs are saved (for skip_existing)
        """
        self.items = items
        self.batch_id_field = batch_id_field
        self.batch_id_start = batch_id_start
        self.batch_output_id_field = batch_output_id_field
        self.batch_only_items = batch_only_items or []
        self.batch_skip_items = batch_skip_items or []
        self.batch_skip_existing = batch_skip_existing
        self.items_dir = items_dir

        self.collated_results = []
        self.errors = []
        self.sequential_id = batch_id_start
        self.processed_count = 0
        self.skipped_count = 0

    def should_skip_item(self, item: Dict, item_idx: int) -> tuple[bool, str]:
        """Check if an item should be skipped

        Args:
            item: Item data
            item_idx: Item index (1-indexed)

        Returns:
            Tuple of (should_skip, skip_reason)
        """
        item_id = str(item.get(self.batch_id_field, item_idx)) if self.batch_id_field else str(item_idx)

        # Check only_items filter
        if self.batch_only_items and item_id not in self.batch_only_items:
            return True, "not in only_items"

        # Check skip_items filter
        if self.batch_skip_items and item_id in self.batch_skip_items:
            return True, "in skip_items"

        # Check if already exists
        if self.batch_skip_existing and self.items_dir:
            item_output_file = self.items_dir / f"{item_id}.json"
            if item_output_file.exists():
                # Load existing result for collation
                try:
                    with open(item_output_file, 'r', encoding='utf-8') as f:
                        existing_result = json.load(f)
                        self.collated_results.append(existing_result)
                except Exception as e:
                    pass  # Ignore load errors for existing files
                return True, "already exists"

        return False, ""

    def add_result(self, result: Any):
        """Add a result to collated results with sequential ID assignment

        Args:
            result: Result data (can be dict, list, or other)
        """
        if isinstance(result, list):
            # Flatten array and assign sequential IDs during collation
            for sub_item in result:
                if isinstance(sub_item, dict) and self.batch_output_id_field:
                    sub_item[self.batch_output_id_field] = self.sequential_id
                    self.sequential_id += 1
                self.collated_results.append(sub_item)
        else:
            # Single result - assign sequential ID if dict
            if isinstance(result, dict):
                if self.batch_output_id_field:
                    result[self.batch_output_id_field] = self.sequential_id
                    self.sequential_id += 1
            self.collated_results.append(result)

        self.processed_count += 1

    def add_error(self, item_id: str, item_index: int, error: Exception, step_number: int):
        """Add an error to the error list

        Args:
            item_id: ID of the item that failed
            item_index: Index of the item (1-indexed)
            error: The exception that occurred
            step_number: Step number where error occurred
        """
        import traceback
        error_info = {
            "item_id": item_id,
            "item_index": item_index,
            "error": str(error),
            "traceback": traceback.format_exc(),
            "step": step_number
        }
        self.errors.append(error_info)

    def increment_skipped(self):
        """Increment skipped counter"""
        self.skipped_count += 1

    def get_summary(self) -> Dict:
        """Get processing summary

        Returns:
            Dict with processed, skipped, errors counts
        """
        return {
            'total': len(self.items),
            'processed': self.processed_count,
            'skipped': self.skipped_count,
            'errors': len(self.errors)
        }

    def get_collated_results(self) -> List:
        """Get collated results"""
        return self.collated_results

    def get_errors(self) -> List[Dict]:
        """Get error list"""
        return self.errors
