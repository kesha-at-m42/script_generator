"""
Version Manager - Handles version directory creation and management
"""

from pathlib import Path
from typing import Tuple, Optional
import json


def get_next_version(pipeline_dir: Path) -> str:
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


def get_latest_version(pipeline_dir: Path) -> Optional[str]:
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


def create_version_directory(
    pipeline_name: str,
    module_number: int = None,
    path_letter: str = None,
    base_version: str = None,
    outputs_dir: Path = None
) -> Tuple[Path, str, bool, str]:
    """Create a new version directory for a pipeline

    Args:
        pipeline_name: Name of the pipeline
        module_number: Module number (optional, adds to directory name)
        path_letter: Path letter (optional, adds to directory name)
        base_version: Base version to build upon (for reruns)
        outputs_dir: Outputs directory (defaults to project_root/outputs)

    Returns:
        Tuple of (version_dir_path, version_str, is_rerun, full_pipeline_name)
    """
    if outputs_dir is None:
        from pathlib import Path
        outputs_dir = Path(__file__).parent.parent / "outputs"

    # Build full pipeline name with module and path
    full_pipeline_name = pipeline_name
    if module_number is not None:
        full_pipeline_name += f"_module_{module_number}"
    if path_letter is not None:
        full_pipeline_name += f"_path_{path_letter.lower()}"

    pipeline_dir = outputs_dir / full_pipeline_name

    # Determine version number
    version_str = get_next_version(pipeline_dir)
    version_dir = pipeline_dir / version_str

    # Create directory structure (step directories will be created per-step)
    version_dir.mkdir(parents=True, exist_ok=True)

    is_rerun = base_version is not None

    return version_dir, version_str, is_rerun, full_pipeline_name


def update_latest_symlink(pipeline_name: str, version_str: str, outputs_dir: Path = None):
    """Update the 'latest' symlink to point to the newest version

    Args:
        pipeline_name: Name of the pipeline
        version_str: Version to point to (e.g., "v1")
        outputs_dir: Outputs directory (defaults to project_root/outputs)
    """
    if outputs_dir is None:
        from pathlib import Path
        outputs_dir = Path(__file__).parent.parent / "outputs"

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


def save_metadata(version_dir: Path, metadata: dict):
    """Save metadata.json for a pipeline version

    Args:
        version_dir: Path to version directory
        metadata: Metadata dictionary to save
    """
    metadata_path = version_dir / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
