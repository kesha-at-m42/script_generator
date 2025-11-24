"""
Predefined Pipelines
Define reusable pipeline configurations here
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pipeline import Step


# =============================================================================
# PREDEFINED PIPELINES
# =============================================================================

PIPELINES = {
    "test": [
        Step(
            prompt_name='test',
            variables={'name': 'Kesha'},
            output_file='greeting.txt'
        ),
        Step(
            prompt_name='test_2',
            output_file='response.txt'
        )
    ],

    "script_generator": [
        Step(
            prompt_name='warmup_generator',
            output_file='warmup.json'
        ),
        Step(
            prompt_name='interaction_generator',
            output_file='interactions.json'
        ),
        Step(
            function="script_formatter.format_interactions_to_markdown",
            output_file="script.md"
        )
    ],

    # Add more predefined pipelines here
}
