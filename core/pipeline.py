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
from path_manager import get_project_paths, get_project_root, get_template_path, ensure_dir

# Add utils directory to path for json_utils and template_utils
paths = get_project_paths()
utils_dir = paths['utils']
if str(utils_dir) not in sys.path:
    sys.path.insert(0, str(utils_dir))

from json_utils import extract_json, parse_json
from template_utils import get_template_by_id

# Import refactored modules
from path_manager import get_step_directory, get_step_output_paths, resolve_input_path
from version_manager import (
    get_next_version,
    get_latest_version,  # Export for rerun.py
    create_version_directory,
    update_latest_symlink,
    save_metadata
)
from batch_processor import BatchProcessor
from pipeline_executor import flatten_dict, run_formatting_step
from output_validator import validate_ai_output_structure

# Re-export for external use
__all__ = [
    'PipelineControl',
    'Step',
    'run_pipeline',
    'run_single_step',
    'get_latest_version'  # For rerun.py
]

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


# =============================================================================
# STEP RANGE HELPERS
# =============================================================================

def normalize_step_reference(step_ref: Union[int, str], steps: List[Step]) -> int:
    """Convert step number or name to 1-indexed integer

    Args:
        step_ref: Step reference (int index or string name)
        steps: List of Step objects

    Returns:
        1-indexed step number

    Raises:
        ValueError: If step name not found
    """
    if isinstance(step_ref, int):
        return step_ref

    # Find by name
    for i, step in enumerate(steps, 1):
        step_name = step.prompt_name if step.is_ai_step() else str(step.function).split('.')[-1]
        if step_name == step_ref:
            return i

    # Not found - provide suggestions
    available = [f"  {i}. {s.prompt_name if s.is_ai_step() else str(s.function).split('.')[-1]}"
                 for i, s in enumerate(steps, 1)]
    raise ValueError(
        f"Step '{step_ref}' not found.\nAvailable steps:\n" + "\n".join(available)
    )


def validate_step_index(idx: int, total_steps: int):
    """Validate step index is in valid range

    Args:
        idx: Step index to validate
        total_steps: Total number of steps

    Raises:
        ValueError: If index is out of range
    """
    if idx < 1:
        raise ValueError(f"Step index must be >= 1, got {idx}")
    if idx > total_steps:
        raise ValueError(f"Step index {idx} exceeds total steps ({total_steps})")


def validate_base_version_outputs(base_dir: Path, steps: List[Step],
                                  start_idx: int, end_idx: int):
    """Validate base version has outputs for specified step range

    Args:
        base_dir: Base version directory path
        steps: List of Step objects
        start_idx: First step index to check (1-indexed)
        end_idx: Last step index to check (1-indexed)

    Raises:
        FileNotFoundError: If any required outputs are missing
    """
    missing = []
    for i in range(start_idx, end_idx + 1):
        step = steps[i - 1]
        step_name = step.prompt_name if step.is_ai_step() else str(step.function).split('.')[-1]
        step_dir = get_step_directory(base_dir, i, step_name)
        step_paths = get_step_output_paths(step_dir, step_name, step.batch_mode)

        if not step_paths['main_output'].exists():
            missing.append(f"Step {i} ({step_name}): {step_paths['main_output']}")

    if missing:
        raise FileNotFoundError(
            f"Base version missing required outputs:\n  " + "\n  ".join(missing)
        )


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
      start_from_step: Union[int, str] = None,
      end_at_step: Union[int, str] = None,
      pipeline_status: str = None,
      notes: str = None,
      template_filename: str = "problem_templates.json"
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
        start_from_step: Skip steps 1 through N-1, start from step N (int or step name)
        end_at_step: Stop after step N (int or step name). Use with start_from_step for ranges.
        pipeline_status: Status/maturity label (e.g., "alpha", "beta", "rc", "final", "deprecated")
        notes: Optional notes about this version (e.g., "Fixed prompt for template 4002")
        template_filename: Template filename for template lookup (default: "problem_templates_v2.json")
                          Path will be constructed as: modules/module{module_number}/{template_filename}

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

    # Normalize and validate step range
    start_idx = 1  # default: start from step 1
    end_idx = len(steps)  # default: run through last step

    if start_from_step is not None:
        # Auto-detect base_version if not provided
        if base_version is None and pipeline_name:
            full_pipeline_name = pipeline_name
            if module_number is not None:
                full_pipeline_name += f"_module_{module_number}"
            if path_letter is not None:
                full_pipeline_name += f"_path_{path_letter.lower()}"

            outputs_dir = get_project_paths()['outputs']
            pipeline_dir = outputs_dir / full_pipeline_name
            base_version = get_latest_version(pipeline_dir)

            if not base_version:
                raise ValueError(
                    f"start_from_step requires a base version, but no versions found for '{full_pipeline_name}'. "
                    f"Run the full pipeline first."
                )

        start_idx = normalize_step_reference(start_from_step, steps)
        validate_step_index(start_idx, len(steps))

    if end_at_step is not None:
        end_idx = normalize_step_reference(end_at_step, steps)
        validate_step_index(end_idx, len(steps))

        if end_idx < start_idx:
            raise ValueError(f"end_at_step ({end_idx}) cannot be before start_from_step ({start_idx})")

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
                outputs_dir = get_project_paths()['outputs']
                pipeline_dir = outputs_dir / full_pipeline_name
                base_version = get_latest_version(pipeline_dir)

            version_dir, version_str, is_rerun, full_pipeline_name = create_version_directory(
                pipeline_name, module_number, path_letter, base_version
            )
            output_dir_path = version_dir

            metadata["version"] = version_str
            metadata["base_version"] = base_version

            # Determine mode
            if start_idx > 1 or end_idx < len(steps):
                metadata["mode"] = "partial_rerun"
                metadata["step_range"] = f"{start_idx}-{end_idx}"
                metadata["skipped_steps"] = list(range(1, start_idx)) + list(range(end_idx + 1, len(steps) + 1))
                metadata["executed_steps"] = list(range(start_idx, end_idx + 1))
            elif base_version:
                metadata["mode"] = "rerun"
            else:
                metadata["mode"] = "initial"

            metadata["full_pipeline_name"] = full_pipeline_name

            # Validate base version has outputs for skipped steps
            if start_idx > 1:
                outputs_dir = get_project_paths()['outputs']
                pipeline_dir = outputs_dir / full_pipeline_name
                base_version_dir = pipeline_dir / base_version
                validate_base_version_outputs(base_version_dir, steps, 1, start_idx - 1)

            if verbose:
                print(f"\n{'='*70}")
                print(f"PIPELINE: {full_pipeline_name}")
                print(f"Version: {version_str}" + (f" (rerun from {base_version})" if base_version else ""))
                if start_idx > 1 or end_idx < len(steps):
                    print(f"Step Range: {start_idx}-{end_idx} (executing {end_idx - start_idx + 1} of {len(steps)} steps)")
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
            output_dir_path = ensure_dir(Path(output_dir))
    else:
        output_dir_path = ensure_dir(Path(output_dir))

    builder = PromptBuilderV2(module_number, path_letter, verbose)

    # Project root for path resolution
    project_root = get_project_root()

    # Construct template path for template lookup
    template_path = None
    if module_number is not None and template_filename:
        template_path = get_template_path(module_number, template_filename)
        if verbose and template_path.exists():
            print(f"  [TEMPLATES] Using: {template_path.relative_to(project_root)}")

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
        step_type = "AI" if step.is_ai_step() else "FORMATTING"
        step_name = step.prompt_name if step.is_ai_step() else str(step.function).split('.')[-1]

        # Skip steps outside the execution range
        if i < start_idx or i > end_idx:
            if verbose:
                print(f"\n[STEP {i}/{len(steps)}] [{step_type}] {step_name}")
                print(f"  [SKIP] Outside execution range ({start_idx}-{end_idx})")
            continue

        # Check for pause/stop
        if control:
            control.check_and_wait()
            control.update_status(f"Running step {i}/{len(steps)}: {step_name}")

        # Create step directory and get paths
        step_dir = get_step_directory(output_dir_path, i, step_name)
        step_paths = get_step_output_paths(step_dir, step_name, step.batch_mode)

        # Create directories
        ensure_dir(step_dir)
        if step_paths['items_dir']:
            ensure_dir(step_paths['items_dir'])
        if step_paths['prompts_dir']:
            ensure_dir(step_paths['prompts_dir'])

        if verbose:
            print(f"\n[STEP {i}/{len(steps)}] [{step_type}] {step_name}")
            print(f"  [DIR] {step_dir.relative_to(output_dir_path)}")


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

        # Auto-chain: If input_file is None or empty, use previous step's main output
        input_file = step.input_file

        # Substitute variables in input_file path (e.g., module{module_number})
        if input_file and module_number is not None and path_letter:
            input_file = input_file.replace("{module_number}", str(module_number))
            input_file = input_file.replace("{path_letter}", path_letter.lower())

        # Auto-chaining logic
        if (input_file is None or input_file == "") and i > 1:
            # Get previous step's output
            prev_step = steps[i-2]  # i is 1-indexed
            prev_step_name = prev_step.prompt_name if prev_step.is_ai_step() else str(prev_step.function).split('.')[-1]

            # If this is first executed step in partial rerun, load from base version
            if i == start_idx and start_idx > 1:
                outputs_dir = get_project_paths()['outputs']
                pipeline_dir = outputs_dir / metadata['full_pipeline_name']
                base_version_dir = pipeline_dir / base_version
                prev_step_dir = get_step_directory(base_version_dir, i-1, prev_step_name)
                prev_step_paths = get_step_output_paths(prev_step_dir, prev_step_name, prev_step.batch_mode)
                input_file = str(prev_step_paths['main_output'])  # Use absolute path

                if verbose:
                    rel_path = prev_step_paths['main_output'].relative_to(base_version_dir)
                    print(f"  [AUTO-CHAIN] Using base version: {base_version}/{rel_path}")
            else:
                # Normal auto-chaining from current version
                prev_step_dir = get_step_directory(output_dir_path, i-1, prev_step_name)
                prev_step_paths = get_step_output_paths(prev_step_dir, prev_step_name, prev_step.batch_mode)
                input_file = str(prev_step_paths['main_output'].relative_to(output_dir_path))

                if verbose:
                    print(f"  [AUTO-CHAIN] Using previous step output: {input_file}")

        # Load input file if specified
        input_content = None
        input_data = None
        if input_file:
            # For partial reruns with explicit input, resolve from base version if first step
            if i == start_idx and start_idx > 1 and not Path(input_file).is_absolute():
                outputs_dir = get_project_paths()['outputs']
                pipeline_dir = outputs_dir / metadata['full_pipeline_name']
                base_version_dir = pipeline_dir / base_version
                input_path = resolve_input_path(
                    input_file,
                    output_dir=base_version_dir,  # Use base version for resolution
                    module_number=module_number,
                    path_letter=path_letter
                )
            else:
                # Normal resolution from current version
                input_path = resolve_input_path(
                    input_file,
                    output_dir=output_dir_path,
                    module_number=module_number,
                    path_letter=path_letter
                )

            if verbose:
                print(f"  [LOAD] Reading: {input_path}")
            try:
                # Debug: Check file size before reading
                file_size = input_path.stat().st_size
                if verbose:
                    print(f"  [DEBUG] File size: {file_size} bytes")

                with open(input_path, 'r', encoding='utf-8') as f:
                    input_content = f.read()

                if verbose:
                    print(f"  [DEBUG] Read {len(input_content)} chars from {file_size} bytes")

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
                if verbose:
                    print(f"  [DEBUG] Parsed {len(items)} items from JSON array")
            except Exception as e:
                print(f"  [ERROR] Failed to parse input as JSON array: {e}")
                raise

            # Calculate base version directory for rerun mode
            base_step_dir = None
            if base_version and rerun_items:
                outputs_dir = get_project_paths()['outputs']
                pipeline_dir = outputs_dir / metadata['full_pipeline_name']
                base_version_dir = pipeline_dir / base_version
                base_step_dir = get_step_directory(base_version_dir, i, step_name)

            # Determine which items to process
            # If step has explicit batch_only_items set, use that (takes priority)
            # Otherwise, use rerun_items if available
            # This allows step 1 (problem_generator) to use template IDs while other steps use problem instance IDs
            batch_filter = step.batch_only_items if step.batch_only_items else rerun_items

            # Initialize batch processor
            batch_proc = BatchProcessor(
                items=items,
                batch_id_field=step.batch_id_field,
                batch_id_start=step.batch_id_start,
                batch_output_id_field=step.batch_output_id_field,
                batch_only_items=batch_filter,
                batch_skip_items=step.batch_skip_items,
                batch_skip_existing=step.batch_skip_existing,
                items_dir=step_paths['items_dir'],
                base_version_dir=base_step_dir
            )

            if batch_filter and verbose:
                if step.batch_only_items:
                    print(f"  [BATCH] Processing only: {batch_filter}")
                elif rerun_items:
                    print(f"  [RERUN] Processing only: {batch_filter}")

            total_items = len(items)

            for item_idx, item in enumerate(items, 1):
                # Get item ID (with composite key support for multi-step items)
                if step.batch_id_field:
                    base_id = str(item.get(step.batch_id_field, item_idx))
                    # For multi-step items, append step_id to create unique file names
                    if 'step_id' in item:
                        item_id = f"{base_id}_{item['step_id']}"
                    else:
                        item_id = base_id
                else:
                    item_id = str(item_idx)

                # Check if should skip
                should_skip, skip_reason = batch_proc.should_skip_item(item, item_idx)
                if should_skip:
                    if verbose:
                        print(f"  [SKIP {item_idx}/{total_items}] {item_id} ({skip_reason})")
                    batch_proc.increment_skipped()
                    continue

                # Process this item
                if verbose:
                    print(f"\n  [BATCH {item_idx}/{total_items}] {item_id}")

                try:
                    # Flatten item to variables
                    item_vars = flatten_dict(item)
                    # Keep both original and flattened versions for prefill compatibility
                    merged_vars = {**step_vars, **item, **item_vars}

                    if verbose:
                        # Show some key variables
                        var_preview = {k: v for k, v in list(item_vars.items())[:3]}
                        print(f"    Variables: {var_preview}...")

                    # Execute step for this item
                    if step.is_ai_step():
                        # AI step - call Claude
                        prompt_save_path = step_paths['prompts_dir'] / f"{item_id}.md"

                        # Load prompt to check for template_ref
                        prompt = builder._load_prompt(step.prompt_name)

                        # Always pass entire item as input JSON
                        item_input = json.dumps(item, indent=2, ensure_ascii=False)

                        # Add full input JSON as variable for prefill support
                        merged_vars['__input__'] = item_input

                        # Template lookup: If template_ref exists, fetch template fields as variables
                        if prompt.template_ref and len(prompt.template_ref) > 0:
                            template_id = item.get("template_id")
                            if template_id and template_path:
                                try:
                                    # Fetch template using constructed template_path
                                    template = get_template_by_id(str(template_path), template_id)
                                    # Extract specified fields and add to variables
                                    template_vars = {k: template[k] for k in prompt.template_ref.keys()
                                                   if k in template}
                                    merged_vars.update(template_vars)
                                    if verbose:
                                        print(f"    [TEMPLATE] Loaded {template_id}: {list(template_vars.keys())}")
                                except Exception as e:
                                    if verbose:
                                        print(f"    [WARN] Template lookup failed for {template_id}: {e}")
                            elif not template_id and verbose:
                                print(f"    [WARN] template_ref specified but no template_id found in item")
                            elif not template_path and verbose:
                                print(f"    [WARN] template_ref specified but no template_path configured")

                        item_output = builder.run(
                            prompt_name=step.prompt_name,
                            variables=merged_vars,  # Includes template fields if lookup succeeded
                            input_content=item_input,  # Always full item as input
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

                        # Validate AI output structure (using prompt's schema)
                        # Use output ID field if specified, otherwise input ID field
                        expected_id_field = step.batch_output_id_field or step.batch_id_field
                        validation_error = validate_ai_output_structure(
                            item_result,
                            item,
                            batch_id_field=expected_id_field,
                            output_structure=prompt.output_structure
                        )
                        if validation_error:
                            error_msg = f"Validation failed: {validation_error}"
                            if verbose:
                                print(f"    [ERROR] {error_msg}")
                            raise ValueError(error_msg)

                    else:
                        # Formatting step - call Python function
                        item_result = run_formatting_step(step, item, None, module_number, path_letter, project_root, False)

                    # Save individual result
                    item_output_file = step_paths['items_dir'] / f"{item_id}.json"
                    with open(item_output_file, 'w', encoding='utf-8') as f:
                        json.dump(item_result, f, indent=2, ensure_ascii=False)

                    # Add result to batch processor (handles collation and ID assignment)
                    batch_proc.add_result(item_result)

                    if verbose:
                        print(f"    [OK] Completed")

                except Exception as e:
                    batch_proc.add_error(item_id, item_idx, e, i)

                    if verbose:
                        print(f"    [ERROR] {e}")

                    if step.batch_stop_on_error:
                        print(f"  [STOP] Stopping pipeline due to error (batch_stop_on_error=True)")
                        raise

            # Print batch summary
            summary = batch_proc.get_summary()
            if verbose:
                print(f"\n  [BATCH COMPLETE]")
                print(f"    Processed: {summary['processed']}/{summary['total']}")
                print(f"    Skipped: {summary['skipped']}")
                print(f"    Errors: {summary['errors']}")

            # Save errors if any
            errors = batch_proc.get_errors()
            if errors:
                errors_file = step_paths['errors_file']
                with open(errors_file, 'w', encoding='utf-8') as f:
                    json.dump(errors, f, indent=2, ensure_ascii=False)
                if verbose:
                    print(f"    Saved errors to: {errors_file.relative_to(output_dir_path)}")

            # Set output to collated array
            collated_results = batch_proc.get_collated_results()
            last_output = json.dumps(collated_results, indent=2, ensure_ascii=False)

        else:
            # NON-BATCH MODE: Single execution
            if step.is_ai_step():
                # AI step - call Claude
                # Save prompt to step directory
                prompt_save_path = step_paths['prompt_file']

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
                output = run_formatting_step(step, input_data, input_content, module_number, path_letter, project_root, verbose)
                last_output = output

        # Save main output file (always save to step directory)
        output_path = step_paths['main_output']

        if step.batch_mode:
            # BATCH MODE: Save collated array
            try:
                collated_data = json.loads(last_output)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(collated_data, f, indent=2, ensure_ascii=False)

                if verbose:
                    print(f"  [SAVE] Saved {len(collated_data)} items to: {output_path.relative_to(output_dir_path)}")

            except Exception as e:
                # Fallback to raw save
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(last_output)
                if verbose:
                    print(f"  [SAVE] Saved output to: {output_path.relative_to(output_dir_path)}")

        else:
            # NON-BATCH MODE: Save single output
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
                            print(f"  [SAVE] Saved JSON array with {len(parsed)} items to: {output_path.relative_to(output_dir_path)}")
                        elif isinstance(parsed, dict):
                            print(f"  [SAVE] Saved JSON object with {len(parsed)} keys to: {output_path.relative_to(output_dir_path)}")
                        else:
                            print(f"  [SAVE] Saved JSON to: {output_path.relative_to(output_dir_path)}")

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
                        print(f"  [SAVE] Saved JSON to: {output_path.relative_to(output_dir_path)}")
                else:
                    # Save as text
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(str(last_output))
                    if verbose:
                        print(f"  [SAVE] Saved {len(str(last_output))} chars to: {output_path.relative_to(output_dir_path)}")

        # Track last output file for reference
        last_output_file = str(output_path.relative_to(output_dir_path))

    # Save metadata and update symlink
    if pipeline_name:
        # Complete metadata
        end_time = datetime.now()
        metadata["duration_seconds"] = (end_time - start_time).total_seconds()
        metadata["status"] = "completed"
        metadata["output_dir"] = str(output_dir_path)

        # Save metadata
        save_metadata(output_dir_path, metadata)

        # Update latest symlink
        version_str = metadata.get("version")
        full_pipeline_name = metadata.get("full_pipeline_name", pipeline_name)
        if version_str:
            update_latest_symlink(full_pipeline_name, version_str)

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




