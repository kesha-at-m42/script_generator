"""
Pipelines Configuration
Loads pipeline configurations from pipelines.json
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.pipeline import Step


# =============================================================================
# LOAD PIPELINES FROM JSON
# =============================================================================

def load_pipelines_from_json():
    """Load pipelines from config/pipelines.json and convert to Step objects"""
    json_path = Path(__file__).parent / "pipelines.json"

    if not json_path.exists():
        return {}

    with open(json_path, 'r', encoding='utf-8') as f:
        pipelines_data = json.load(f)

    # Convert JSON format to Step objects
    pipelines = {}
    for pipeline_name, steps_data in pipelines_data.items():
        steps = []
        for step_data in steps_data:
            if step_data.get("type") == "ai":
                step = Step(
                    prompt_name=step_data.get("prompt_name"),
                    variables=step_data.get("variables", {}),
                    output_file=step_data.get("output_file"),
                    model=step_data.get("model")
                )
            else:  # formatting step
                step = Step(
                    function=step_data.get("function"),
                    function_args=step_data.get("function_args", {}),
                    output_file=step_data.get("output_file")
                )
            steps.append(step)
        pipelines[pipeline_name] = steps

    return pipelines


# Load pipelines from JSON file
PIPELINES = load_pipelines_from_json()
