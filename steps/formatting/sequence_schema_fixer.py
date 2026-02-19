"""
Sequence Schema Fixer - Fixes and validates sequence schema structure
"""

import os


# ============================================================================
# DEBUG LOGGING HELPERS
# ============================================================================

class SchemaLogger:
    """Tracks and logs schema fixing changes"""
    def __init__(self, enabled=False):
        self.enabled = enabled
        self.changes = {
            'workspace_added': 0,
            'wrapped_in_pool': 0,
            'shuffle_tangibles_added': 0
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

    def log_shuffle_tangibles_added(self, location):
        """Log when shuffle_tangibles is added to a workspace"""
        if not self.enabled:
            return

        self.changes['shuffle_tangibles_added'] += 1
        print(f"\n[DEBUG] SHUFFLE TANGIBLES ADDED - {location}")
        print(f"  Set shuffle_tangibles: true on workspace")

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
        if self.changes['shuffle_tangibles_added'] > 0:
            print(f"[OK] shuffle_tangibles added: {self.changes['shuffle_tangibles_added']} steps")

        if not any(self.changes.values()):
            print("No changes made")


# Global logger instance
_logger = SchemaLogger()


def add_empty_workspace_to_first_step(sequences_data, module_number=None, path_letter=None):
    """
    Add empty workspace to the first step of ALL sequences if they don't have one

    Args:
        sequences_data: List of sequence dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        Dictionary with sequences array, all first steps having workspaces
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

    # Navigate to each sequence's first step and add workspace if missing
    for seq_idx, sequence in enumerate(sequences):
        if "steps" in sequence and len(sequence["steps"]) > 0:
            first_step = sequence["steps"][0]
            if "workspace" not in first_step:
                first_step["workspace"] = {
                    "@type": "WorkspaceData",
                    "tangibles": []
                }
                _logger.log_workspace_added(f"Seq{seq_idx+1}/Step1")

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


def _is_select_tool(tool):
    """Return True if the tool value represents a Select tool."""
    if isinstance(tool, str):
        return tool in ("select", "multi_select")
    if isinstance(tool, dict):
        return tool.get("@type") == "Select"
    return False


def _has_read_only_tangible(workspace):
    """Return True if any tangible in the workspace is marked is_read_only."""
    tangibles = workspace.get("tangibles", [])
    return any(t.get("is_read_only", False) for t in tangibles)


def add_shuffle_tangibles_for_select(sequences_data, module_number=None, path_letter=None):
    """
    Set shuffle_tangibles: true on the workspace of any step whose prompt tool
    is Select and whose workspace contains no read-only tangibles.

    Args:
        sequences_data: List of sequence dictionaries or dict with "sequences" key
        module_number: Module number (automatically passed by pipeline)
        path_letter: Path letter (automatically passed by pipeline)

    Returns:
        The (possibly modified) sequences_data in its original wrapper form
    """
    global _logger
    _logger = SchemaLogger()

    if isinstance(sequences_data, dict) and "sequences" in sequences_data:
        sequences = sequences_data["sequences"]
        wrapper = sequences_data
    elif isinstance(sequences_data, list):
        sequences = sequences_data
        wrapper = {"sequences": sequences}
    else:
        raise ValueError("Expected list of sequences or dict with 'sequences' key")

    for seq_idx, sequence in enumerate(sequences):
        for step_idx, step in enumerate(sequence.get("steps", [])):
            workspace = step.get("workspace")
            if not workspace:
                continue

            prompt = step.get("prompt")
            if not prompt:
                continue

            tool = prompt.get("tool")
            if not _is_select_tool(tool):
                continue

            if _has_read_only_tangible(workspace):
                continue

            workspace["shuffle_tangibles"] = True
            _logger.log_shuffle_tangibles_added(f"Seq{seq_idx + 1}/Step{step_idx + 1}")

    _logger.summary()
    return wrapper
