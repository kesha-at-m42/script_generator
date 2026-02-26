"""
Pipeline Executor - Handles execution of individual pipeline steps
"""

from pathlib import Path
from typing import Dict, Any
import json
import sys
import importlib


def flatten_dict(obj, parent_key='', sep='__'):
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
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Keep lists as-is, don't flatten further
                items.append((new_key, v))
            else:
                items.append((new_key, v))
    else:
        # Not a dict, return as-is
        return {parent_key: obj} if parent_key else {}

    return dict(items)


def load_function(function, project_root: Path):
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


def run_formatting_step(step, input_data, input_content, module_number: int, path_letter: str, project_root: Path, verbose: bool):
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
    func = load_function(step.function, project_root)

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

    if 'verbose' in param_names:
        args['verbose'] = verbose
        if verbose:
            print(f"  [EXEC] Passing verbose={verbose}")

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
