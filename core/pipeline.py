"""
Pipeline - Core pipeline functionality

Provides Step class and run_pipeline function for chaining prompts together.
"""

from pathlib import Path
from typing import List, Dict
import sys

# Add core directory to path
core_dir = Path(__file__).parent
if str(core_dir) not in sys.path:
    sys.path.insert(0, str(core_dir))

from prompt_builder import PromptBuilderV2


class Step:
    """A single step in a pipeline"""

    def __init__(self, prompt_name: str, variables: Dict = None, output_key: str = None):
        """
        Args:
            prompt_name: Name of the prompt to run
            variables: Static variables for this step
            output_key: Key to store output (accessible to later steps)
        """
        self.prompt_name = prompt_name
        self.variables = variables or {}
        self.output_key = output_key


def run_pipeline(
    steps: List[Step],
    initial_variables: Dict = None,
    module_number: int = None,
    path_letter: str = None,
    verbose: bool = True
) -> Dict:
    """Run a pipeline of steps

    Args:
        steps: List of Step objects to execute
        initial_variables: Variables available to all steps
        module_number: Module number for context
        path_letter: Path letter for context
        verbose: Enable verbose logging

    Returns:
        Dict with all outputs plus 'final_output'
    """
    if initial_variables is None:
        initial_variables = {}

    builder = PromptBuilderV2(module_number, path_letter, verbose)

    # Accumulated variables (shared across all steps)
    accumulated_vars = initial_variables.copy()
    outputs = {}
    last_output = None

    if verbose:
        print(f"\n{'='*70}")
        print(f"RUNNING PIPELINE")
        print(f"Steps: {len(steps)}")
        print(f"{'='*70}")

    for i, step in enumerate(steps, 1):
        if verbose:
            print(f"\n[STEP {i}/{len(steps)}] {step.prompt_name}")

        # Merge step variables with accumulated variables
        step_vars = {**accumulated_vars, **step.variables}

        # Run the prompt
        output = builder.run(step.prompt_name, step_vars)

        # Store output if key provided
        if step.output_key:
            accumulated_vars[step.output_key] = output
            outputs[step.output_key] = output
            if verbose:
                print(f"  [OK] Stored as '{step.output_key}'")

        last_output = output

    outputs['final_output'] = last_output

    if verbose:
        print(f"\n{'='*70}")
        print(f"PIPELINE COMPLETE")
        print(f"{'='*70}")

    return outputs
