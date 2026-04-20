"""
Pipeline Loader - Deserializes pipeline definitions from config into Step objects

This module is the bridge between config/pipelines.json (the declarative pipeline
definitions) and the rest of the application (which works with Step objects).

Responsibilities:
- Read and parse config/pipelines.json at import time
- Convert each JSON step definition into a typed Step object
- Validate batch mode configuration and emit warnings for common mistakes
- Expose the resulting PIPELINES dict for use by CLI commands and the UI

PIPELINES is a dict[str, list[Step]] keyed by pipeline name.
"""

import json
from pathlib import Path
from typing import Dict

from .pipeline import Step, run_pipeline, run_single_step

# config/pipelines.json sits one level up from this file (core/)
_JSON_PATH = Path(__file__).parent.parent / "config" / "pipelines.json"


def step_from_config(step_data: dict) -> Step:
    """Convert a single pipeline config dict to a Step object."""
    input_file = step_data.get("input_file")
    output_file = step_data.get("output_file")

    # Collect only the batch kwargs that are explicitly present in JSON
    # so Step defaults are not accidentally overridden.
    batch_kwargs = {}
    for key in (
        "batch_mode",
        "batch_id_field",
        "batch_output_id_field",
        "batch_id_start",
        "batch_skip_existing",
        "batch_only_items",
        "batch_skip_items",
        "batch_stop_on_error",
        "stop_on_validation_failure",
    ):
        if key in step_data:
            batch_kwargs[key] = step_data[key]

    if step_data.get("type") == "ai":
        return Step(
            prompt_name=step_data.get("prompt_name"),
            variables=step_data.get("variables", {}),
            input_file=input_file,
            output_file=output_file,
            model=step_data.get("model"),
            context_files=step_data.get("context_files", {}),
            **batch_kwargs,
        )
    else:  # formatting step
        return Step(
            function=step_data.get("function"),
            function_args=step_data.get("function_args", {}),
            input_file=input_file,
            output_file=output_file,
            **batch_kwargs,
        )


def load_pipelines_from_json() -> dict:
    """Parse config/pipelines.json and return a dict of pipeline name → [Step]."""
    if not _JSON_PATH.exists():
        return {}

    with open(_JSON_PATH, "r", encoding="utf-8") as f:
        pipelines_data = json.load(f)

    pipelines = {}
    for pipeline_name, steps_data in pipelines_data.items():
        steps = []
        for step_data in steps_data:
            # Warn when batch_mode is enabled without an id field — the step
            # will still run, but items will be identified by numeric index.
            if step_data.get("batch_mode") and not step_data.get("batch_id_field"):
                print(
                    f"  [WARN] Step '{step_data.get('name')}': "
                    "batch_mode without batch_id_field will use numeric indices"
                )

            steps.append(step_from_config(step_data))
        pipelines[pipeline_name] = steps

    return pipelines


# Loaded once at import time; all callers share the same dict.
PIPELINES = load_pipelines_from_json()


def run_pipeline_from_config(
    steps_config: list,
    pipeline_name: str = None,
    module_number: int = None,
    path_letter: str = None,
    unit_number: int = None,
    **kwargs,
) -> Dict:
    """Convert a list of step config dicts to Step objects and run the pipeline.

    This is the preferred entry point for both the CLI and the UI so that
    neither caller needs to know about step_from_config / Step internals.
    """
    steps = [sc if isinstance(sc, Step) else step_from_config(sc) for sc in steps_config]
    results = run_pipeline(
        steps=steps,
        pipeline_name=pipeline_name,
        module_number=module_number,
        path_letter=path_letter,
        unit_number=unit_number,
        **kwargs,
    )
    return results


def run_single_step_from_config(
    step_config: dict,
    module_number: int = None,
    path_letter: str = None,
    unit_number: int = None,
    previous_output_file: str = None,
    **kwargs,
) -> Dict:
    """Convert a single step config dict to a Step object and run it.

    Accepts an optional *previous_output_file* so the caller does not need to
    mutate the Step object after construction.
    """
    step = step_config if isinstance(step_config, Step) else step_from_config(step_config)
    if previous_output_file:
        step.input_file = previous_output_file
    return run_single_step(
        step=step,
        module_number=module_number,
        path_letter=path_letter,
        unit_number=unit_number,
        **kwargs,
    )
