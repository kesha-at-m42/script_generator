"""
Pipeline - Core pipeline functionality

Provides Step class and run_pipeline function for chaining prompts together.
Supports both AI steps (Claude API) and deterministic formatting steps (Python functions).
"""
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Callable, Union
import sys
import importlib

# Add core directory to path
core_dir = Path(__file__).parent
if str(core_dir) not in sys.path:
    sys.path.insert(0, str(core_dir))

from prompt_builder import PromptBuilderV2

# Add utils directory to path for json_utils
utils_dir = Path(__file__).parent.parent / "utils"
if str(utils_dir) not in sys.path:
    sys.path.insert(0, str(utils_dir))

from json_utils import extract_json, parse_json

import time


class PipelineControl:
    """Control object for pause/stop functionality"""

    def __init__(self):
        self.should_stop = False
        self.is_paused = False
        self.status_callback = None

    def stop(self):
        """Signal the pipeline to stop"""
        self.should_stop = True

    def pause(self):
        """Signal the pipeline to pause"""
        self.is_paused = True

    def resume(self):
        """Resume the pipeline"""
        self.is_paused = False

    def check_and_wait(self):
        """Check if stopped, and wait while paused"""
        if self.should_stop:
            raise StopIteration("Pipeline stopped by user")

        while self.is_paused:
            time.sleep(0.1)
            if self.should_stop:
                raise StopIteration("Pipeline stopped by user")

    def update_status(self, message):
        """Send status update to callback if available"""
        if self.status_callback:
            self.status_callback(message)


class Step:
    """A single step in a pipeline - can be either an AI step or a formatting step"""

    def __init__(
        self,
        prompt_name: str = None,
        variables: Dict = None,
        input_file: str = None,
        output_file: str = None,
        function: Union[str, Callable] = None,
        function_args: Dict = None,
        model: str = None
    ):
        """
        Args:
            prompt_name: Name of the prompt to run (for AI steps)
            variables: Static variables for this step
            input_file: Path to input file to load (supports auto-chaining from previous step)
            output_file: Path to save output file (enables human-in-loop editing)
            function: Python function for deterministic formatting steps. Can be:
                    - String: "module.function_name" (e.g., "bbcode_formatter.process_godot_sequences")
                    - Callable: Direct function reference
            function_args: Dict of additional arguments to pass to the formatting function.
                        Note: module_number and path_letter are automatically passed if the function accepts them.
            model: Claude model to use for AI steps (e.g., "claude-opus-4-5-20251101", "claude-sonnet-4-5-20250929").
                   If not specified, uses the default model from ClaudeClient.

        Note: Either prompt_name OR function must be specified, not both.
        """
        self.prompt_name = prompt_name
        self.variables = variables or {}
        self.input_file = input_file
        self.output_file = output_file
        self.function = function
        self.function_args = function_args or {}
        self.model = model

        # Validation
        if prompt_name and function:
            raise ValueError("Step cannot have both prompt_name and function - choose one")
        if not prompt_name and not function:
            raise ValueError("Step must have either prompt_name (AI step) or function (formatting step)")

    def is_ai_step(self) -> bool:
        """Returns True if this is an AI step (uses Claude API)"""
        return self.prompt_name is not None

    def is_formatting_step(self) -> bool:
        """Returns True if this is a formatting step (deterministic function)"""
        return self.function is not None


def run_pipeline(
      steps: List[Step],
      initial_variables: Dict = None,
      module_number: int = None,
      path_letter: str = None,
      output_dir: str = None,
      verbose: bool = True,
      parse_json_output: bool = True,
      control: PipelineControl = None,
      interactive: bool = False
  ) -> Dict:
    """Run a pipeline of steps with file I/O support

    Args:
        steps: List of Step objects to execute (can be AI or formatting steps)
        initial_variables: Variables available to all steps
        module_number: Module number for context (automatically passed to formatting steps)
        path_letter: Path letter for context (automatically passed to formatting steps)
        output_dir: Directory for output files (default: outputs/pipeline_TIMESTAMP)
        verbose: Enable verbose logging
        parse_json_output: Enable JSON extraction and formatting for AI steps (default: True)
        control: Optional PipelineControl object for pause/stop functionality
        interactive: Enable step-by-step confirmation before each step (default: False)

    Returns:
        Dict with final_output and metadata
    """
    if initial_variables is None:
        initial_variables = {}

    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/pipeline_{timestamp}"

    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    builder = PromptBuilderV2(module_number, path_letter, verbose)

    # Project root for path resolution
    project_root = Path(__file__).parent.parent

    last_output = None
    last_output_file = None

    if verbose:
        print(f"\n{'='*70}")
        print(f"RUNNING PIPELINE")
        print(f"Steps: {len(steps)}")
        print(f"Output Directory: {output_dir_path}")
        if interactive:
            print(f"Mode: INTERACTIVE (step-by-step confirmation)")
        print(f"{'='*70}")

    for i, step in enumerate(steps, 1):
        # Check for pause/stop
        if control:
            control.check_and_wait()
            control.update_status(f"Running step {i}/{len(steps)}: {step_name}")

        step_type = "AI" if step.is_ai_step() else "FORMATTING"
        step_name = step.prompt_name if step.is_ai_step() else str(step.function)

        if verbose:
            print(f"\n[STEP {i}/{len(steps)}] [{step_type}] {step_name}")


        # Interactive mode: Ask for confirmation
        if interactive:
            print("\n  [INTERACTIVE] About to execute this step.")
            if step.input_file:
                print(f"  Input: {step.input_file}")
            elif last_output_file:
                print(f"  Input: {last_output_file} (auto-chained)")
            if step.output_file:
                print(f"  Output: {step.output_file}")

            while True:
                response = input("\n  Proceed with this step? (y/n/q): ").strip().lower()
                if response == 'y':
                    print(f"  [INTERACTIVE] Proceeding with step {i}...")
                    break
                elif response == 'n':
                    print(f"  [INTERACTIVE] Skipping step {i}")
                    continue
                elif response == 'q':
                    print(f"  [INTERACTIVE] Quitting pipeline")
                    return {
                        'final_output': last_output,
                        'output_dir': str(output_dir_path),
                        'last_output_file': last_output_file,
                        'status': 'stopped',
                        'stopped_at_step': i
                    }
                else:
                    print(f"  Invalid input. Please enter 'y' (yes), 'n' (no), or 'q' (quit)")

            if response == 'n':
                continue

        step_vars = initial_variables.copy()
        step_vars.update(step.variables)

        # Auto-chain: If input_file is None, use previous step's output_file
        input_file = step.input_file
        if input_file is None and last_output_file is not None:
            input_file = last_output_file
            if verbose:
                print(f"  [AUTO-CHAIN] Using previous output: {input_file}")

        # Load input file if specified
        input_content = None
        input_data = None
        if input_file:
            input_path = _resolve_input_path(input_file, output_dir_path, project_root)
            if verbose:
                print(f"  [LOAD] Reading: {input_path}")
            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    input_content = f.read()

                # For formatting steps, try to parse as JSON
                if step.is_formatting_step():
                    try:
                        input_data = json.loads(input_content)
                        if verbose:
                            print(f"  [OK] Loaded and parsed JSON")
                    except:
                        input_data = input_content
                        if verbose:
                            print(f"  [OK] Loaded as text")
                else:
                    if verbose:
                        print(f"  [OK] Loaded {len(input_content)} chars")
            except Exception as e:
                print(f"  [ERROR] Failed to load input file: {e}")
                raise

        # Execute the step
        if step.is_ai_step():
            # AI step - call Claude
            output = builder.run(step.prompt_name, step_vars, input_content=input_content, model=step.model)
            last_output = output
        else:
            # Formatting step - call Python function
            output = _run_formatting_step(step, input_data, input_content, module_number, path_letter, project_root, verbose)
            last_output = output

        # Save output file if specified
        if step.output_file:
            output_path = output_dir_path / step.output_file
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Handle JSON parsing for AI steps
            if step.is_ai_step() and parse_json_output:
                try:
                    if verbose:
                        print(f"  [JSON] Extracting JSON from output...")

                    # Extract JSON from the output
                    json_str = extract_json(output)

                    # Parse to validate and format
                    parsed = parse_json(json_str)

                    # Save as formatted JSON
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(parsed, f, indent=2, ensure_ascii=False)

                    if verbose:
                        if isinstance(parsed, list):
                            print(f"  [OK] Parsed and saved JSON array with {len(parsed)} items")
                        elif isinstance(parsed, dict):
                            print(f"  [OK] Parsed and saved JSON object with {len(parsed)} keys")
                        else:
                            print(f"  [OK] Parsed and saved JSON")

                    # Update last_output to be the JSON string for chaining
                    last_output = json.dumps(parsed, indent=2, ensure_ascii=False)

                except Exception as e:
                    if verbose:
                        print(f"  [WARN] JSON parsing failed: {e}")
                        print(f"  [WARN] Saving raw output instead")

                    # Fall back to raw output
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(output)
            else:
                # Save output (for formatting steps or when parse_json_output=False)
                if isinstance(output, (dict, list)):
                    # Save as JSON
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(output, f, indent=2, ensure_ascii=False)
                    if verbose:
                        print(f"  [SAVE] Saved JSON output to: {step.output_file}")
                else:
                    # Save as text
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(str(output))
                    if verbose:
                        print(f"  [SAVE] Wrote {len(str(output))} chars to: {step.output_file}")

            last_output_file = step.output_file

    if verbose:
        print(f"\n{'='*70}")
        print(f"PIPELINE COMPLETE")
        print(f"{'='*70}")

    return {
        'final_output': last_output,
        'output_dir': str(output_dir_path),
        'last_output_file': last_output_file
    }


def run_single_step(
    step: Step,
    module_number: int = None,
    path_letter: str = None,
    output_dir: str = None,
    verbose: bool = True,
    parse_json_output: bool = True
) -> Dict:
    """
    Run a single pipeline step (convenience wrapper for UI/testing)

    NOTE: This is a temporary wrapper. TODO: Refactor to make run_step()
    the atomic operation and have run_pipeline() loop over run_step().
    That would be cleaner architecture but requires larger refactor.

    Args:
        step: Step object to execute
        module_number: Module number for context
        path_letter: Path letter for context
        output_dir: Directory for output files
        verbose: Enable verbose logging
        parse_json_output: Enable JSON extraction for AI steps

    Returns:
        Dict with step results (same format as run_pipeline)
    """
    return run_pipeline(
        steps=[step],
        module_number=module_number,
        path_letter=path_letter,
        output_dir=output_dir,
        verbose=verbose,
        parse_json_output=parse_json_output
    )


def _run_formatting_step(step: Step, input_data, input_content, module_number: int, path_letter: str, project_root: Path, verbose: bool):
    """Execute a deterministic formatting step

    Args:
        step: The Step object with function and function_args
        input_data: Parsed JSON data (if input was JSON)
        input_content: Raw input content (if input was not JSON)
        module_number: Module number (automatically passed to function if it accepts it)
        path_letter: Path letter (automatically passed to function if it accepts it)
        project_root: Project root path for module imports
        verbose: Verbose logging flag

    Returns:
        Output from the formatting function
    """
    if verbose:
        print(f"  [EXEC] Running formatting function...")

    # Load the function
    func = _load_function(step.function, project_root)

    # Prepare arguments - start with module context
    args = {}

    # Add module_number and path_letter if function accepts them
    import inspect
    sig = inspect.signature(func)
    param_names = list(sig.parameters.keys())

    # Check which parameters the function accepts and add them
    if 'module_number' in param_names:
        args['module_number'] = module_number
        if verbose:
            print(f"  [EXEC] Passing module_number={module_number}")

    if 'path_letter' in param_names:
        args['path_letter'] = path_letter
        if verbose:
            print(f"  [EXEC] Passing path_letter={path_letter}")

    # Add custom function_args (these override if there's a conflict)
    args.update(step.function_args)

    # Pass input as first positional argument if function expects it
    if len(param_names) > 0:
        first_param = param_names[0]
        # Check if first param is not in our keyword args (meaning it's positional)
        if first_param not in args:
            if verbose:
                print(f"  [EXEC] Passing input to parameter '{first_param}'")
            result = func(input_data if input_data is not None else input_content, **args)
        else:
            # All params are keyword args
            result = func(**args)
    else:
        # Function takes no arguments
        result = func(**args)

    if verbose:
        print(f"  [OK] Formatting complete")

    return result


def _load_function(function: Union[str, Callable], project_root: Path) -> Callable:
    """Load a function from string reference or return callable

    Args:
        function: Either "module.function_name" string or callable
        project_root: Project root for module imports

    Returns:
        The callable function
    """
    if callable(function):
        return function

    # Parse string like "bbcode_formatter.process_godot_sequences"
    if not isinstance(function, str):
        raise ValueError(f"function must be string or callable, got {type(function)}")

    if '.' not in function:
        raise ValueError(f"function string must be 'module.function_name', got '{function}'")

    module_name, func_name = function.rsplit('.', 1)

    # Try to import the module
    try:
        # Add utils for backwards compatibility (but lower priority)
        utils_dir = project_root / "utils"
        if str(utils_dir) not in sys.path:
            sys.path.insert(0, str(utils_dir))

        # Add formatting directory to path (higher priority - inserted after utils so it comes first)
        formatting_dir = project_root / "steps" / "formatting"
        if str(formatting_dir) not in sys.path:
            sys.path.insert(0, str(formatting_dir))

        module = importlib.import_module(module_name)
        func = getattr(module, func_name)

        if not callable(func):
            raise ValueError(f"{module_name}.{func_name} is not callable")

        return func
    except ImportError as e:
        raise ImportError(f"Could not import module '{module_name}': {e}")
    except AttributeError as e:
        raise AttributeError(f"Module '{module_name}' has no function '{func_name}': {e}")


def _resolve_input_path(input_file: str, output_dir: Path, project_root: Path) -> Path:
    """Resolve input file path with fallback chain

    Resolution order:
    1. Absolute path → use as-is
    2. Relative to output_dir (for chained files)
    3. Relative to project root
    4. As-is (will fail if not found)
    """
    input_path = Path(input_file)

    # 1. Absolute path
    if input_path.is_absolute():
        return input_path

    # 2. Relative to output_dir (chained files)
    output_relative = output_dir / input_file
    if output_relative.exists():
        return output_relative

    # 3. Relative to project root
    project_relative = project_root / input_file
    if project_relative.exists():
        return project_relative

    # 4. Use as-is (will error if doesn't exist)
    return input_path
