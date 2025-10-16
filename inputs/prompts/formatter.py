"""
Formatter - Converts JSON interaction sequences to human-readable markdown scripts

This is a DETERMINISTIC step (no AI) that formats the remediation JSON into 
a readable markdown script for review and implementation.
"""

# NOTE: This formatter doesn't use Claude - it's pure Python formatting
# The config below is just for consistency with other prompt modules

FORMATTER_ROLE = """This step doesn't use AI - it's a deterministic formatter."""

FORMATTER_DOCS = []

FORMATTER_EXAMPLES = []

FORMATTER_INSTRUCTIONS = """This is a deterministic formatting step."""

FORMATTER_STRUCTURE = """Output is markdown text, not JSON."""
