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
            # Extract common parameters
            input_file = step_data.get("input_file")
            output_file = step_data.get("output_file")

            # Build batch kwargs dictionary - ONLY include if present in JSON
            batch_kwargs = {}
            if "batch_mode" in step_data:
                batch_kwargs["batch_mode"] = step_data["batch_mode"]
            if "batch_id_field" in step_data:
                batch_kwargs["batch_id_field"] = step_data["batch_id_field"]
            if "batch_output_id_field" in step_data:
                batch_kwargs["batch_output_id_field"] = step_data["batch_output_id_field"]
            if "batch_id_start" in step_data:
                batch_kwargs["batch_id_start"] = step_data["batch_id_start"]
            if "batch_skip_existing" in step_data:
                batch_kwargs["batch_skip_existing"] = step_data["batch_skip_existing"]
            if "batch_only_items" in step_data:
                batch_kwargs["batch_only_items"] = step_data["batch_only_items"]
            if "batch_skip_items" in step_data:
                batch_kwargs["batch_skip_items"] = step_data["batch_skip_items"]
            if "batch_stop_on_error" in step_data:
                batch_kwargs["batch_stop_on_error"] = step_data["batch_stop_on_error"]

            # Validate batch mode requirements
            if batch_kwargs.get("batch_mode"):
                if not input_file:
                    raise ValueError(
                        f"Step '{step_data.get('name', 'unnamed')}': "
                        "batch_mode=true requires 'input_file' pointing to a JSON array"
                    )
                if not batch_kwargs.get("batch_id_field"):
                    # Just a warning, not an error
                    print(f"  [WARN] Step '{step_data.get('name')}': "
                          "batch_mode without batch_id_field will use numeric indices")

            if step_data.get("type") == "ai":
                step = Step(
                    prompt_name=step_data.get("prompt_name"),
                    variables=step_data.get("variables", {}),
                    input_file=input_file,
                    output_file=output_file,
                    model=step_data.get("model"),
                    **batch_kwargs  # Unpack only the batch params that were specified
                )
            else:  # formatting step
                step = Step(
                    function=step_data.get("function"),
                    function_args=step_data.get("function_args", {}),
                    input_file=input_file,
                    output_file=output_file,
                    **batch_kwargs  # Same batch params
                )
            steps.append(step)
        pipelines[pipeline_name] = steps

    return pipelines


# Load pipelines from JSON file
PIPELINES = load_pipelines_from_json()
