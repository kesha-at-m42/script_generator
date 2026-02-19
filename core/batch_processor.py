"""
Batch Processor - Handles batch mode item processing
"""

from pathlib import Path
from typing import List, Dict, Any
import json


class BatchProcessor:
    """Manages batch processing of items"""

    @staticmethod
    def _get_item_id(item: Dict, id_field: str) -> str:
        """Get ID from item, checking nested paths if needed

        Args:
            item: Item dict
            id_field: Field name (e.g., 'problem_id')

        Returns:
            ID as string, or empty string if not found
        """
        # Try top-level field first
        value = item.get(id_field)
        if value is not None:
            return str(value)

        # Try metadata.{id_field} for nested IDs
        metadata = item.get('metadata')
        if isinstance(metadata, dict):
            value = metadata.get(id_field)
            if value is not None:
                return str(value)

        return ''

    def __init__(
        self,
        items: List[Dict],
        batch_id_field: str,
        batch_id_start: int,
        batch_output_id_field: str = None,
        batch_only_items: List[str] = None,
        batch_skip_items: List[str] = None,
        batch_skip_existing: bool = False,
        items_dir: Path = None,
        base_version_dir: Path = None
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
            base_version_dir: Base version directory to copy unchanged items from (for reruns)
        """
        self.items = items
        self.batch_id_field = batch_id_field
        self.batch_id_start = batch_id_start
        self.batch_output_id_field = batch_output_id_field
        self.batch_only_items = batch_only_items or []
        self.batch_skip_items = batch_skip_items or []
        self.batch_skip_existing = batch_skip_existing
        self.items_dir = items_dir
        self.base_version_dir = base_version_dir

        self.collated_results = []
        self.errors = []
        self.sequential_id = batch_id_start
        self.processed_count = 0
        self.skipped_count = 0

        # Cache for base collated items (avoid reloading file multiple times)
        self._base_collated_cache = None

    def should_skip_item(self, item: Dict, item_idx: int) -> tuple[bool, str]:
        """Check if an item should be skipped

        Args:
            item: Item data
            item_idx: Item index (1-indexed)

        Returns:
            Tuple of (should_skip, skip_reason)
        """
        # Get item ID (handles nested IDs like metadata.problem_id)
        if self.batch_id_field:
            base_id = self._get_item_id(item, self.batch_id_field)
            if not base_id:  # If no ID found, fall back to index
                base_id = str(item_idx)
                item_id = base_id
            else:
                # For multi-step items, append step_id to create unique file names
                if 'step_id' in item:
                    item_id = f"{base_id}_{item['step_id']}"
                else:
                    item_id = base_id
        else:
            base_id = str(item_idx)
            item_id = base_id

        # Check only_items filter
        # Support both exact matches (e.g., "75_1") and base ID matches (e.g., "75" matches "75_1" and "75_2")
        if self.batch_only_items:
            is_included = item_id in self.batch_only_items or base_id in self.batch_only_items
            if not is_included:
                # If base_version_dir provided, copy from base instead of skipping
                if self.base_version_dir:
                    copied_item = self._load_from_base(item, item_id, base_id)
                    if copied_item:
                        self.add_result(copied_item, preserve_id=True)
                        return True, "copied from base"
                    else:
                        # Base item not found (e.g. it was excluded from the base version).
                        # Advance sequential counter so fresh items downstream get correct IDs.
                        if self.batch_output_id_field:
                            self.sequential_id += 1
                return True, "not in only_items"

        # Check skip_items filter
        # Support both exact matches and base ID matches
        if self.batch_skip_items:
            is_skipped = item_id in self.batch_skip_items or base_id in self.batch_skip_items
            if is_skipped:
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

    def add_result(self, result: Any, preserve_id: bool = False):
        """Add a result to collated results with sequential ID assignment

        Args:
            result: Result data (can be dict, list, or other)
            preserve_id: If True, keep the item's existing batch_output_id_field value
                         instead of overwriting it. The sequential counter is advanced
                         past the preserved ID so fresh items don't collide.
        """
        if isinstance(result, list):
            # Flatten array and assign sequential IDs during collation
            for sub_item in result:
                if isinstance(sub_item, dict) and self.batch_output_id_field:
                    existing_id = sub_item.get(self.batch_output_id_field)
                    if preserve_id and existing_id is not None:
                        try:
                            self.sequential_id = max(self.sequential_id, int(existing_id) + 1)
                        except (TypeError, ValueError):
                            pass
                    else:
                        sub_item[self.batch_output_id_field] = self.sequential_id
                        self.sequential_id += 1
                self.collated_results.append(sub_item)
        else:
            # Single result - assign sequential ID if dict
            if isinstance(result, dict):
                if self.batch_output_id_field:
                    existing_id = result.get(self.batch_output_id_field)
                    if preserve_id and existing_id is not None:
                        try:
                            self.sequential_id = max(self.sequential_id, int(existing_id) + 1)
                        except (TypeError, ValueError):
                            pass
                    else:
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

        # Reserve IDs for the errored item(s)
        # For template-based generation, check base version to see how many IDs to reserve
        if self.batch_output_id_field:
            ids_to_reserve = 1  # Default: reserve 1 ID

            # For template errors: check base version to see how many items it generated
            if self.batch_id_field == 'template_id' and self.base_version_dir:
                # Create a minimal item dict with just the template_id for _load_from_base
                temp_item = {'template_id': item_id}
                base_items = self._load_from_base(temp_item, item_id)
                if base_items:
                    # Count items from base version
                    if isinstance(base_items, list):
                        ids_to_reserve = len(base_items)
                    else:
                        ids_to_reserve = 1

            # Reserve the appropriate number of IDs
            self.sequential_id += ids_to_reserve

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

    def _load_from_base(self, item: Dict, item_id: str, base_id: str = None) -> Dict:
        """Load item from base version (unchanged items during rerun)

        Args:
            item: Current item data (may contain template_id)
            item_id: Item ID to load (may include step_id suffix like "9_1")
            base_id: Base ID without step_id suffix (e.g., "9" for "9_1")

        Returns:
            Item data from base version, or None if not found
        """
        if not self.base_version_dir:
            return None

        # For step 1 (problem_generator): load ALL items from template file
        # Only use template_id logic if batch_id_field is 'template_id'
        if 'template_id' in item and self.batch_id_field == 'template_id':
            template_id = item['template_id']

            # IMPORTANT: Try collated file FIRST. Individual items/ files hold pre-re-collation
            # IDs (wrong sequential IDs from when the template was originally generated).
            # The collated file has the correct re-collated IDs. Loading from items/ and using
            # preserve_id=True would advance sequential_id to the wrong value, causing the next
            # fresh template's items to get incorrect problem_instance_ids.
            parent_dir_name = self.base_version_dir.name
            if 'step_' in parent_dir_name:
                parts = parent_dir_name.split('_', 2)
                if len(parts) >= 3:
                    step_name = parts[2]
                    collated_file = self.base_version_dir / f"{step_name}.json"
                    if collated_file.exists():
                        try:
                            # Load collated items (with caching)
                            if self._base_collated_cache is None:
                                with open(collated_file, 'r', encoding='utf-8') as f:
                                    self._base_collated_cache = json.load(f)

                            # Filter items by template_id
                            template_items = [
                                i for i in self._base_collated_cache
                                if str(i.get('template_id')) == str(template_id)
                            ]
                            if template_items:
                                return template_items
                        except Exception as e:
                            pass  # Ignore errors, fall through to individual file

            # Fallback: individual items/ file (only if not in collated)
            base_file = self.base_version_dir / f"items/{template_id}.json"
            if base_file.exists():
                try:
                    with open(base_file, 'r', encoding='utf-8') as f:
                        base_items = json.load(f)
                    # Return ALL items from this template (not just one)
                    # add_result() will flatten the list and add all items to collated_results
                    return base_items
                except Exception as e:
                    pass  # Ignore errors, will return None

            return None  # Template not found in base

        # For step 2+: Search in collated file (most reliable, always exists)
        # Extract step name from directory path
        # e.g., "v8/step_02_sequence_structurer" -> look for "sequence_structurer.json"
        parent_dir_name = self.base_version_dir.name
        if 'step_' in parent_dir_name:
            # Extract step name (e.g., "step_02_sequence_structurer" -> "sequence_structurer")
            parts = parent_dir_name.split('_', 2)  # Split on first 2 underscores
            if len(parts) >= 3:
                step_name = parts[2]
                collated_file = self.base_version_dir / f"{step_name}.json"

                if collated_file.exists():
                    try:
                        # Load collated items (with caching to avoid repeated file reads)
                        if self._base_collated_cache is None:
                            with open(collated_file, 'r', encoding='utf-8') as f:
                                self._base_collated_cache = json.load(f)

                        # Search for item by ID in cached items
                        # IMPORTANT: Use output ID field when searching base outputs
                        # (base files have the transformed field name from batch_output_id_field)
                        search_field = self.batch_output_id_field if self.batch_output_id_field else self.batch_id_field

                        # For multi-step items (e.g., "9_1"), search by base_id (e.g., "9")
                        # because base version has non-flattened items
                        search_id = base_id if base_id else item_id

                        for collated_item in self._base_collated_cache:
                            # Match by output ID field (handles nested IDs)
                            collated_id = self._get_item_id(collated_item, search_field)
                            if collated_id == str(search_id):
                                return collated_item
                    except Exception as e:
                        pass  # Ignore errors, fall through to individual file

        # Fallback: Try individual item file (legacy path, rarely used)
        base_file = self.base_version_dir / f"items/{item_id}.json"
        if base_file.exists():
            try:
                with open(base_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                pass  # Ignore errors

        return None
