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
        model: str = None,
        # Batch processing parameters
        batch_mode: bool = False,
        batch_id_field: str = None,
        batch_output_id_field: str = None,
        batch_id_start: int = 1,
        batch_skip_existing: bool = False,
        batch_only_items: List[str] = None,
        batch_skip_items: List[str] = None,
        batch_stop_on_error: bool = False
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

            # Batch processing
            batch_mode: Enable item-by-item processing of input array
            batch_id_field: Field from input items to use as ID (e.g., "template_id")
            batch_output_id_field: Add sequential ID to output items (e.g., "interaction_id")
            batch_id_start: Starting number for sequential IDs (default: 1)
            batch_skip_existing: Skip items that already have outputs (resume mode)
            batch_only_items: Only process these item IDs (list of strings)
            batch_skip_items: Skip these item IDs (list of strings)
            batch_stop_on_error: Stop pipeline if any item fails (default: False, continue)

        Note: Either prompt_name OR function must be specified, not both.
        """
        self.prompt_name = prompt_name
        self.variables = variables or {}
        self.input_file = input_file
        self.output_file = output_file
        self.function = function
        self.function_args = function_args or {}
        self.model = model

        # Batch processing
        self.batch_mode = batch_mode
        self.batch_id_field = batch_id_field
        self.batch_output_id_field = batch_output_id_field
        self.batch_id_start = batch_id_start
        self.batch_skip_existing = batch_skip_existing
        self.batch_only_items = batch_only_items or []
        self.batch_skip_items = batch_skip_items or []
        self.batch_stop_on_error = batch_stop_on_error

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
      pipeline_name: str = None,
      initial_variables: Dict = None,
      module_number: int = None,
      path_letter: str = None,
      output_dir: str = None,
      verbose: bool = True,
      parse_json_output: bool = True,
      control: PipelineControl = None,
      interactive: bool = False,
      base_version: str = None,
      rerun_items: List[str] = None,
      pipeline_status: str = None,
      notes: str = None
  ) -> Dict:
    """Run a pipeline of steps with file I/O support

    Args:
        steps: List of Step objects to execute (can be AI or formatting steps)
        pipeline_name: Name for the pipeline (enables versioning: outputs/pipeline_name/v0, v1...)
        initial_variables: Variables available to all steps
        module_number: Module number for context (automatically passed to formatting steps)
        path_letter: Path letter for context (automatically passed to formatting steps)
        output_dir: Directory for output files (overrides versioning if specified)
        verbose: Enable verbose logging
        parse_json_output: Enable JSON extraction and formatting for AI steps (default: True)
        control: Optional PipelineControl object for pause/stop functionality
        interactive: Enable step-by-step confirmation before each step (default: False)
        base_version: Base version for reruns (e.g., "v0"). Automatically uses latest if None.
        rerun_items: List of item IDs to rerun (enables rerun mode)
        pipeline_status: Status/maturity label (e.g., "alpha", "beta", "rc", "final", "deprecated")
        notes: Optional notes about this version (e.g., "Fixed prompt for template 4002")

    Returns:
        Dict with final_output and metadata
    """
    if initial_variables is None:
        initial_variables = {}

    # Initialize metadata
    start_time = datetime.now()
    metadata = {
        "timestamp": start_time.isoformat(),
        "pipeline_name": pipeline_name,
        "module_number": module_number,
        "path_letter": path_letter,
        "pipeline_status": pipeline_status or "draft",  # Default to "draft"
        "notes": notes or "",
        "logs": [],
        "stats": {}
    }

    # Create output directory
    if output_dir is None:
        if pipeline_name:
            # Version-based structure: outputs/pipeline_name_module_X_path_Y/v0, v1, etc.
            # Build full pipeline name for directory lookup
            full_pipeline_name = pipeline_name
            if module_number is not None:
                full_pipeline_name += f"_module_{module_number}"
            if path_letter is not None:
                full_pipeline_name += f"_path_{path_letter.lower()}"

            if base_version is None and rerun_items:
                # Auto-use latest version for reruns
                project_root = Path(__file__).parent.parent
                pipeline_dir = project_root / "outputs" / full_pipeline_name
                base_version = _get_latest_version(pipeline_dir)

            version_dir, version_str, is_rerun, full_pipeline_name = _create_version_directory(
                pipeline_name, module_number, path_letter, base_version
            )
            output_dir_path = version_dir

            metadata["version"] = version_str
            metadata["base_version"] = base_version
            metadata["mode"] = "rerun" if is_rerun else "initial"
            metadata["full_pipeline_name"] = full_pipeline_name

            if verbose:
                print(f"\n{'='*70}")
                print(f"PIPELINE: {full_pipeline_name}")
                print(f"Version: {version_str}" + (f" (rerun from {base_version})" if is_rerun else ""))
                print(f"Status: {metadata['pipeline_status']}")
                if metadata.get('notes'):
                    print(f"Notes: {metadata['notes']}")
                print(f"{'='*70}")
        else:
            # Legacy date-based organization
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H%M%S")
            dir_name = f"pipeline_{time_str}"
            output_dir = f"outputs/{date_folder}/{dir_name}"
            output_dir_path = Path(output_dir)
            output_dir_path.mkdir(parents=True, exist_ok=True)
    else:
        output_dir_path = Path(output_dir)
        output_dir_path.mkdir(parents=True, exist_ok=True)

    prompts_dir = output_dir_path / "prompts"
    prompts_dir.mkdir(exist_ok=True)

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

        # Execute the step (batch or non-batch mode)
        if step.batch_mode:
            # BATCH MODE: Process input array item-by-item
            if verbose:
                print(f"  [BATCH] Processing items individually...")

            # Parse input as JSON array
            try:
                items = json.loads(input_content) if input_content else []
                if not isinstance(items, list):
                    raise ValueError("Batch mode requires input to be a JSON array")
            except Exception as e:
                print(f"  [ERROR] Failed to parse input as JSON array: {e}")
                raise

            # Create temp directory for individual items
            temp_dir = output_dir_path / "items"
            temp_dir.mkdir(exist_ok=True)

            # Track results and errors
            collated_results = []
            errors = []
            sequential_id = step.batch_id_start

            # Apply rerun filters if specified
            items_to_process = items
            if rerun_items:
                if verbose:
                    print(f"  [RERUN] Processing only: {rerun_items}")
                step.batch_only_items = rerun_items

            total_items = len(items)
            processed_count = 0
            skipped_count = 0

            for item_idx, item in enumerate(items, 1):
                # Get item ID
                item_id = str(item.get(step.batch_id_field, item_idx)) if step.batch_id_field else str(item_idx)

                # Check skip conditions
                should_skip = False
                skip_reason = ""

                if step.batch_only_items and item_id not in step.batch_only_items:
                    should_skip = True
                    skip_reason = "not in only_items"
                elif step.batch_skip_items and item_id in step.batch_skip_items:
                    should_skip = True
                    skip_reason = "in skip_items"
                elif step.batch_skip_existing:
                    item_output_file = temp_dir / item_id / f"{i:02d}_output.json"
                    if item_output_file.exists():
                        should_skip = True
                        skip_reason = "already exists"
                        # Load existing result for collation
                        try:
                            with open(item_output_file, 'r', encoding='utf-8') as f:
                                collated_results.append(json.load(f))
                        except Exception as e:
                            print(f"  [WARN] Failed to load existing result for {item_id}: {e}")

                if should_skip:
                    if verbose:
                        print(f"  [SKIP {item_idx}/{total_items}] {item_id} ({skip_reason})")
                    skipped_count += 1
                    continue

                # Process this item
                if verbose:
                    print(f"\n  [BATCH {item_idx}/{total_items}] {item_id}")

                try:
                    # Flatten item to variables
                    item_vars = _flatten_dict(item)
                    merged_vars = {**step_vars, **item_vars}

                    if verbose:
                        # Show some key variables
                        var_preview = {k: v for k, v in list(item_vars.items())[:3]}
                        print(f"    Variables: {var_preview}...")

                    # Execute step for this item
                    if step.is_ai_step():
                        # AI step - call Claude
                        prompt_save_path = prompts_dir / f"{i:02d}_{step.prompt_name}_{item_id}.md"

                        item_output = builder.run(
                            prompt_name=step.prompt_name,
                            variables=merged_vars,
                            input_content=None,  # Don't pass full array, variables have item data
                            model=step.model,
                            save_prompt_to=str(prompt_save_path)
                        )

                        # Parse JSON from AI output
                        try:
                            json_str = extract_json(item_output)
                            item_result = parse_json(json_str)
                        except Exception as e:
                            if verbose:
                                print(f"    [WARN] JSON parsing failed, using raw output: {e}")
                            item_result = {"raw_output": item_output}
                    else:
                        # Formatting step - call Python function
                        item_result = _run_formatting_step(step, item, None, module_number, path_letter, project_root, False)

                    # Add sequential ID if specified
                    if step.batch_output_id_field:
                        item_result[step.batch_output_id_field] = sequential_id
                        sequential_id += 1

                    # Keep original ID for traceability
                    if step.batch_id_field and step.batch_id_field in item:
                        item_result[f"source_{step.batch_id_field}"] = item[step.batch_id_field]

                    # Save individual result
                    item_dir = temp_dir / item_id
                    item_dir.mkdir(exist_ok=True)
                    item_output_file = item_dir / f"{i:02d}_output.json"
                    with open(item_output_file, 'w', encoding='utf-8') as f:
                        json.dump(item_result, f, indent=2, ensure_ascii=False)

                    collated_results.append(item_result)
                    processed_count += 1

                    if verbose:
                        print(f"    [OK] Completed")

                except Exception as e:
                    error_info = {
                        "item_id": item_id,
                        "item_index": item_idx,
                        "error": str(e),
                        "step": i
                    }
                    errors.append(error_info)

                    if verbose:
                        print(f"    [ERROR] {e}")

                    if step.batch_stop_on_error:
                        print(f"  [STOP] Stopping pipeline due to error (batch_stop_on_error=True)")
                        raise

            # Print batch summary
            if verbose:
                print(f"\n  [BATCH COMPLETE]")
                print(f"    Processed: {processed_count}/{total_items}")
                print(f"    Skipped: {skipped_count}")
                print(f"    Errors: {len(errors)}")

            # Save errors if any
            if errors:
                errors_file = output_dir_path / f"{i:02d}_errors.json"
                with open(errors_file, 'w', encoding='utf-8') as f:
                    json.dump(errors, f, indent=2, ensure_ascii=False)
                if verbose:
                    print(f"    Saved errors to: {errors_file.name}")

            # Set output to collated array
            last_output = json.dumps(collated_results, indent=2, ensure_ascii=False)

        else:
            # NON-BATCH MODE: Single execution (existing logic)
            if step.is_ai_step():
                # AI step - call Claude
                # Save prompt to prompts folder
                prompt_save_path = prompts_dir / f"{i:02d}_{step.prompt_name}.md"

                output = builder.run(
                    prompt_name=step.prompt_name,
                    variables=step_vars,
                    input_content=input_content,
                    model=step.model,
                    save_prompt_to=str(prompt_save_path)
                )
                last_output = output
            else:
                # Formatting step - call Python function
                output = _run_formatting_step(step, input_data, input_content, module_number, path_letter, project_root, verbose)
                last_output = output

        # Save output file if specified
        if step.output_file:
            if step.batch_mode:
                # BATCH MODE: Save collated array to collated/ directory
                collated_dir = output_dir_path / "collated"
                collated_dir.mkdir(exist_ok=True)

                step_prefix = f"{i:02d}_"
                output_filename = step_prefix + step.output_file
                output_path = collated_dir / output_filename

                # Parse last_output as JSON array
                try:
                    collated_data = json.loads(last_output)
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(collated_data, f, indent=2, ensure_ascii=False)

                    if verbose:
                        print(f"  [COLLATE] Saved {len(collated_data)} items to: collated/{output_filename}")

                except Exception as e:
                    # Fallback to raw save
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(last_output)
                    if verbose:
                        print(f"  [SAVE] Saved output to: collated/{output_filename}")

                last_output_file = f"collated/{output_filename}"

            else:
                # NON-BATCH MODE: Save single output (existing logic)
                step_prefix = f"{i:02d}_"
                output_filename = step_prefix + step.output_file
                output_path = output_dir_path.joinpath(output_filename)
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Handle JSON parsing for AI steps
                if step.is_ai_step() and parse_json_output:
                    try:
                        if verbose:
                            print(f"  [JSON] Extracting JSON from output...")

                        # Extract JSON from the output
                        json_str = extract_json(last_output)

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
                            f.write(last_output)
                else:
                    # Save output (for formatting steps or when parse_json_output=False)
                    if isinstance(last_output, (dict, list)):
                        # Save as JSON
                        with open(output_path, 'w', encoding='utf-8') as f:
                            json.dump(last_output, f, indent=2, ensure_ascii=False)
                        if verbose:
                            print(f"  [SAVE] Saved JSON output to: {step.output_file}")
                    else:
                        # Save as text
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(str(last_output))
                        if verbose:
                            print(f"  [SAVE] Wrote {len(str(last_output))} chars to: {step.output_file}")

                last_output_file = output_filename

    # Save metadata and update symlink
    if pipeline_name:
        # Complete metadata
        end_time = datetime.now()
        metadata["duration_seconds"] = (end_time - start_time).total_seconds()
        metadata["status"] = "completed"
        metadata["output_dir"] = str(output_dir_path)

        # Save metadata
        _save_metadata(output_dir_path, metadata)

        # Update latest symlink
        version_str = metadata.get("version")
        full_pipeline_name = metadata.get("full_pipeline_name", pipeline_name)
        if version_str:
            _update_latest_symlink(full_pipeline_name, version_str)

        if verbose:
            print(f"\n{'='*70}")
            print(f"PIPELINE COMPLETE")
            print(f"Version: {version_str}")
            print(f"Status: {metadata['pipeline_status']}")
            print(f"Duration: {metadata['duration_seconds']:.1f}s")
            print(f"Output: outputs/{full_pipeline_name}/latest/")
            print(f"{'='*70}")
    else:
        if verbose:
            print(f"\n{'='*70}")
            print(f"PIPELINE COMPLETE")
            print(f"{'='*70}")

    return {
        'final_output': last_output,
        'output_dir': str(output_dir_path),
        'last_output_file': last_output_file,
        'metadata': metadata
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


def _flatten_dict(obj, parent_key='', sep='__'):
    """Flatten nested dict with __ separator

    Example:
        {"goal_decomposition": {"mastery_verb": "create"}}
        → {"goal_decomposition__mastery_verb": "create"}

    Args:
        obj: Dictionary to flatten
        parent_key: Parent key for recursion
        sep: Separator for nested keys (default: __)

    Returns:
        Flattened dictionary
    """
    items = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(_flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Keep lists as-is, don't flatten further
                items.append((new_key, v))
            else:
                items.append((new_key, v))
    else:
        # Not a dict, return as-is
        return {parent_key: obj} if parent_key else {}

    return dict(items)


def _get_next_version(pipeline_dir: Path) -> str:
    """Get the next version number for a pipeline

    Args:
        pipeline_dir: Path to pipeline directory (e.g., outputs/problem_generator/)

    Returns:
        Version string (e.g., "v0", "v1", "v2")
    """
    if not pipeline_dir.exists():
        return "v0"

    # Find all existing version directories
    versions = []
    for item in pipeline_dir.iterdir():
        if item.is_dir() and item.name.startswith('v') and item.name[1:].isdigit():
            versions.append(int(item.name[1:]))

    if not versions:
        return "v0"

    return f"v{max(versions) + 1}"


def _get_latest_version(pipeline_dir: Path) -> str:
    """Get the latest version number for a pipeline

    Args:
        pipeline_dir: Path to pipeline directory

    Returns:
        Latest version string or None if no versions exist
    """
    if not pipeline_dir.exists():
        return None

    # Find all existing version directories
    versions = []
    for item in pipeline_dir.iterdir():
        if item.is_dir() and item.name.startswith('v') and item.name[1:].isdigit():
            versions.append(int(item.name[1:]))

    if not versions:
        return None

    return f"v{max(versions)}"


def _create_version_directory(pipeline_name: str, module_number: int = None, path_letter: str = None, base_version: str = None) -> tuple:
    """Create a new version directory for a pipeline

    Args:
        pipeline_name: Name of the pipeline
        module_number: Module number (optional, adds to directory name)
        path_letter: Path letter (optional, adds to directory name)
        base_version: Base version to build upon (for reruns)

    Returns:
        Tuple of (version_dir_path, version_str, is_rerun, full_pipeline_name)
    """
    project_root = Path(__file__).parent.parent
    outputs_dir = project_root / "outputs"

    # Build full pipeline name with module and path
    full_pipeline_name = pipeline_name
    if module_number is not None:
        full_pipeline_name += f"_module_{module_number}"
    if path_letter is not None:
        full_pipeline_name += f"_path_{path_letter.lower()}"

    pipeline_dir = outputs_dir / full_pipeline_name

    # Determine version number
    version_str = _get_next_version(pipeline_dir)
    version_dir = pipeline_dir / version_str

    # Create directory structure
    version_dir.mkdir(parents=True, exist_ok=True)
    (version_dir / "items").mkdir(exist_ok=True)
    (version_dir / "collated").mkdir(exist_ok=True)
    (version_dir / "prompts").mkdir(exist_ok=True)

    is_rerun = base_version is not None

    return version_dir, version_str, is_rerun, full_pipeline_name


def _update_latest_symlink(pipeline_name: str, version_str: str):
    """Update the 'latest' symlink to point to the newest version

    Args:
        pipeline_name: Name of the pipeline
        version_str: Version to point to (e.g., "v1")
    """
    project_root = Path(__file__).parent.parent
    outputs_dir = project_root / "outputs"
    pipeline_dir = outputs_dir / pipeline_name
    latest_link = pipeline_dir / "latest"

    # Remove existing symlink if it exists
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()

    # Create new symlink (relative to pipeline_dir)
    try:
        latest_link.symlink_to(version_str, target_is_directory=True)
    except OSError:
        # On Windows, symlinks may require admin - create a text file instead
        with open(latest_link.with_suffix('.txt'), 'w') as f:
            f.write(version_str)


def _save_metadata(version_dir: Path, metadata: Dict):
    """Save metadata.json for a pipeline version

    Args:
        version_dir: Path to version directory
        metadata: Metadata dictionary to save
    """
    metadata_path = version_dir / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def _load_base_version_items(pipeline_name: str, base_version: str, step_number: int) -> Dict:
    """Load items from a base version for merging

    Args:
        pipeline_name: Name of the pipeline
        base_version: Base version (e.g., "v0")
        step_number: Step number to load items from

    Returns:
        Dict mapping item_id to item data
    """
    project_root = Path(__file__).parent.parent
    base_dir = project_root / "outputs" / pipeline_name / base_version / "items"

    if not base_dir.exists():
        return {}

    items = {}
    for item_dir in base_dir.iterdir():
        if item_dir.is_dir():
            item_id = item_dir.name
            # Load the specific step output
            step_file = item_dir / f"{step_number:02d}_output.json"
            if step_file.exists():
                with open(step_file, 'r', encoding='utf-8') as f:
                    items[item_id] = json.load(f)

    return items
