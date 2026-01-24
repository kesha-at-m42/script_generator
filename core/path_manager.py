"""
Path Manager - Handles all path resolution and directory structure for the project
"""

from pathlib import Path
from typing import Dict, Optional, List


# =============================================================================
# PROJECT STRUCTURE
# =============================================================================

def get_project_root() -> Path:
    """Get the project root directory

    Returns:
        Path to project root
    """
    return Path(__file__).parent.parent


def get_project_paths() -> Dict[str, Path]:
    """Get all standard project directory paths

    Returns:
        Dict with keys: project_root, docs, modules, prompts, utils, formatting, outputs, logs
    """
    root = get_project_root()
    return {
        'project_root': root,
        'docs': root / 'docs',
        'modules': root / 'modules',
        'prompts': root / 'steps' / 'prompts',
        'utils': root / 'utils',
        'formatting': root / 'steps' / 'formatting',
        'outputs': root / 'outputs',
        'logs': root / 'logs'
    }


def get_module_paths(module_number: int, path_letter: Optional[str] = None) -> Dict[str, Path]:
    """Get paths for a specific module

    Args:
        module_number: Module number
        path_letter: Optional path letter (a, b, c)

    Returns:
        Dict with keys: module_dir, path_dir (if path_letter provided)
    """
    root = get_project_root()
    module_dir = root / 'modules' / f'module{module_number}'

    paths = {'module_dir': module_dir}

    if path_letter:
        paths['path_dir'] = module_dir / f'path{path_letter.lower()}'

    return paths


def ensure_dir(path: Path) -> Path:
    """Ensure a directory exists, creating it if necessary

    Args:
        path: Directory path

    Returns:
        The path (for chaining)
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_parent_dir(file_path: Path) -> Path:
    """Ensure the parent directory of a file exists

    Args:
        file_path: File path

    Returns:
        The file path (for chaining)
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path


# =============================================================================
# PIPELINE PATHS
# =============================================================================

def get_step_directory(output_dir: Path, step_index: int, step_name: str) -> Path:
    """Get the directory for a step

    Args:
        output_dir: Version output directory
        step_index: 1-indexed step number
        step_name: Name of the step

    Returns:
        Path to step directory (e.g., step_01_problem_generator/)
    """
    step_dir_name = f"step_{step_index:02d}_{step_name}"
    return output_dir / step_dir_name


def get_step_output_paths(step_dir: Path, step_name: str, is_batch: bool) -> Dict[str, Path]:
    """Get output paths for a step

    Args:
        step_dir: Step directory path
        step_name: Name of the step
        is_batch: Whether this is a batch mode step

    Returns:
        Dict with keys: items_dir, prompts_dir, main_output, errors_file, prompt_file
    """
    if is_batch:
        return {
            'items_dir': step_dir / 'items',
            'prompts_dir': step_dir / 'prompts',
            'main_output': step_dir / f'{step_name}.json',
            'errors_file': step_dir / 'errors.json',
            'prompt_file': None  # Batch uses prompts_dir
        }
    else:
        return {
            'items_dir': None,
            'prompts_dir': None,
            'main_output': step_dir / f'{step_name}.json',
            'errors_file': None,  # Non-batch doesn't track errors separately
            'prompt_file': step_dir / 'prompt.md'
        }


def resolve_file_path(
    filename: str,
    module_number: int = None,
    path_letter: str = None,
    search_dirs: List[str] = None,
    output_dir: Path = None,
    required: bool = False
) -> Optional[Path]:
    """Unified file path resolution with customizable fallback chain

    Resolution order for relative paths:
    1. Absolute path → return as-is
    2. output_dir (if provided) - for chained pipeline outputs
    3. module/path directory (if module_number + path_letter provided)
    4. module directory (if module_number provided)
    5. Custom search_dirs (e.g., ['docs'], ['outputs'], etc.)
    6. None (file not found)

    Args:
        filename: File name or path (absolute or relative)
        module_number: Optional module number for module-specific search
        path_letter: Optional path letter for path-specific search
        search_dirs: List of directory names to check in project root (e.g., ['docs', 'outputs'])
        output_dir: Optional output directory to check first (for pipeline chaining)
        required: If True, raises FileNotFoundError when file not found

    Returns:
        Resolved Path if found (or absolute path as-is), None if not found

    Raises:
        FileNotFoundError: If required=True and file not found

    Examples:
        # Documentation files (check module/path, module, docs)
        resolve_file_path('visuals.md', module_number=4, path_letter='c', search_dirs=['docs'])

        # Pipeline input files (check output_dir, module/path, module, project root)
        resolve_file_path('data.json', module_number=4, output_dir=Path('outputs/v1'))

        # Just module-specific files
        resolve_file_path('problem_templates_v2.json', module_number=4)
    """
    file_path = Path(filename)

    # 1. Absolute path - return as-is
    if file_path.is_absolute():
        return file_path

    root = get_project_root()
    paths_to_check = []

    # 2. Output directory (for pipeline chaining)
    if output_dir is not None:
        paths_to_check.append(output_dir / filename)

    # 3-4. Module-specific locations
    if module_number is not None:
        module_paths = get_module_paths(module_number, path_letter)

        # 3. Module/path specific (if path_letter provided)
        if path_letter and 'path_dir' in module_paths:
            paths_to_check.append(module_paths['path_dir'] / filename)

        # 4. Module specific
        paths_to_check.append(module_paths['module_dir'] / filename)

    # 5. Custom search directories
    if search_dirs:
        for dir_name in search_dirs:
            paths_to_check.append(root / dir_name / filename)

    # Check each location
    for path in paths_to_check:
        if path.exists():
            return path

    # Not found
    if required:
        checked_locations = '\n  - '.join(str(p) for p in paths_to_check)
        raise FileNotFoundError(
            f"File '{filename}' not found. Checked:\n  - {checked_locations}"
        )

    return None


# Convenience wrappers for common use cases
def resolve_doc_path(
    filename: str,
    module_number: int = None,
    path_letter: str = None,
    required: bool = False
) -> Optional[Path]:
    """Resolve documentation/reference file path

    Checks: module/path → module → docs

    Args:
        filename: File name (e.g., 'visuals.md')
        module_number: Optional module number
        path_letter: Optional path letter
        required: If True, raises FileNotFoundError when not found

    Returns:
        Resolved Path or None
    """
    return resolve_file_path(
        filename,
        module_number=module_number,
        path_letter=path_letter,
        search_dirs=['docs'],
        required=required
    )


def resolve_input_path(
    input_file: str,
    output_dir: Path = None,
    module_number: int = None,
    path_letter: str = None
) -> Path:
    """Resolve pipeline input file path

    Checks: output_dir → module/path → module → project_root

    Args:
        input_file: Input file path
        output_dir: Output directory (for chained files)
        module_number: Optional module number
        path_letter: Optional path letter

    Returns:
        Resolved Path (returns input path as-is if not found)
    """
    result = resolve_file_path(
        input_file,
        module_number=module_number,
        path_letter=path_letter,
        search_dirs=['.'],  # project root
        output_dir=output_dir,
        required=False
    )

    # Return input path as-is if not found (will fail later with better error)
    return result if result else Path(input_file)


def get_template_path(module_number: int, template_filename: str = "problem_templates_v2.json") -> Path:
    """Get path to template file for a module

    Args:
        module_number: Module number
        template_filename: Template filename

    Returns:
        Path to template file
    """
    root = get_project_root()
    return root / 'modules' / f'module{module_number}' / template_filename
