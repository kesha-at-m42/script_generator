"""
Sequence Schema Fixer - Fixes and validates sequence schema structure
"""

import os

# Debug logging control
DEBUG_FORMATTING = os.getenv('DEBUG_FORMATTING', 'false').lower() == 'true'


# ============================================================================
# DEBUG LOGGING HELPERS
# ============================================================================

class SchemaLogger:
    """Tracks and logs schema fixing changes"""
    def __init__(self, enabled=DEBUG_FORMATTING):
        self.enabled = enabled
        self.changes = {
            'workspace_added': 0,
            'wrapped_in_pool': 0
        }

    def log_workspace_added(self, location):
        """Log when empty workspace is added"""
        if not self.enabled:
            return

        self.changes['workspace_added'] += 1
        print(f"\n[DEBUG] WORKSPACE ADDED - {location}")
        print(f"  Added empty workspace with tangibles: []")

    def log_wrapped_in_pool(self):
        """Log when sequences are wrapped in SequencePool"""
        if not self.enabled:
            return

        self.changes['wrapped_in_pool'] += 1
        print(f"\n[DEBUG] WRAPPED IN SEQUENCE POOL")
        print(f"  Added @type: SequencePool wrapper")

    def summary(self):
        """Print summary of all changes"""
        if not self.enabled:
            return

        print(f"\n{'='*70}")
        print(f"SCHEMA FIXER SUMMARY")
        print(f"{'='*70}")

        if self.changes['workspace_added'] > 0:
            print(f"[OK] Workspaces added: {self.changes['workspace_added']} steps")
        if self.changes['wrapped_in_pool'] > 0:
            print(f"[OK] Wrapped in SequencePool: {self.changes['wrapped_in_pool']} times")

        if not any(self.changes.values()):
            print("No changes made")


# Global logger instance
_logger = SchemaLogger()


def add_empty_workspace_to_first_step(sequences_data, module_number=None, path_letter=None):
    """
    Add empty workspace to the first step of the first sequence if it doesn't have one

    Args:
        sequences_data: List of sequence dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        Dictionary with sequences array, first step having workspace
    """
    # Reset logger for new run
    global _logger
    _logger = SchemaLogger()

    # Handle both list and dict with "sequences" key
    if isinstance(sequences_data, dict) and "sequences" in sequences_data:
        sequences = sequences_data["sequences"]
        wrapper = sequences_data
    elif isinstance(sequences_data, list):
        sequences = sequences_data
        wrapper = {"sequences": sequences}
    else:
        raise ValueError("Expected list of sequences or dict with 'sequences' key")

    # Navigate to first sequence's first step and add workspace if missing
    if sequences and len(sequences) > 0:
        first_sequence = sequences[0]
        if "steps" in first_sequence and len(first_sequence["steps"]) > 0:
            first_step = first_sequence["steps"][0]
            if "workspace" not in first_step:
                first_step["workspace"] = {
                    "@type": "WorkspaceData",
                    "tangibles": []
                }
                _logger.log_workspace_added("Seq1/Step1")

    _logger.summary()
    return wrapper


def wrap_in_sequence_pool(sequences_data, module_number=None, path_letter=None):
    """
    Wrap an array of sequences in a SequencePool structure

    Args:
        sequences_data: List of sequence dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        Dictionary with SequencePool wrapper structure
    """
    # Reset logger for new run
    global _logger
    _logger = SchemaLogger()

    # Handle both list and dict with "sequences" key
    if isinstance(sequences_data, dict) and "sequences" in sequences_data:
        # Already wrapped, return as-is
        _logger.summary()
        return sequences_data
    elif isinstance(sequences_data, list):
        sequences = sequences_data
    else:
        raise ValueError("Expected list of sequences or dict with 'sequences' key")

    # Wrap in SequencePool structure
    _logger.log_wrapped_in_pool()
    _logger.summary()

    return {
        "@type": "SequencePool",
        "sequences": sequences
    }
