"""
phase_writer - Formatting Step

Reads phase_split.json (output of phase_splitter) and writes each phase's
markdown content to its corresponding file in the module directory:

  warmup    → units/unit{N}/module{M}/warmup.md
  lesson    → units/unit{N}/module{M}/lesson.md
  exitcheck → units/unit{N}/module{M}/exitcheck.md
  synthesis → units/unit{N}/module{M}/synthesis.md

Returns input data unchanged so the pipeline chain continues.
"""

import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

PHASE_FILES = {
    "warmup": "warmup.md",
    "lesson": "lesson.md",
    "exitcheck": "exitcheck.md",
    "synthesis": "synthesis.md",
}


def write_phases(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Write phase markdown files to the module directory.

    Args:
        input_data: Parsed phase_split.json — dict with keys: warmup, lesson, exitcheck, synthesis
        unit_number: Unit number for locating module directory
        module_number: Module number for locating module directory
        verbose: Enable verbose logging
    """
    if not isinstance(input_data, dict):
        if verbose:
            print("  [PHASE_WRITER] Input is not a dict — skipping")
        return input_data

    if unit_number is None or module_number is None:
        print("  [PHASE_WRITER] unit_number and module_number are required")
        return input_data

    module_dir = project_root / "units" / f"unit{unit_number}" / f"module{module_number}"
    if not module_dir.exists():
        print(f"  [PHASE_WRITER] Module directory not found: {module_dir}")
        return input_data

    written = []
    for phase_key, filename in PHASE_FILES.items():
        content = input_data.get(phase_key)
        if not content:
            if verbose:
                print(f"  [PHASE_WRITER] No content for '{phase_key}' — skipping {filename}")
            continue

        content = re.sub(r"<span[^>]*>(.*?)</span>", r"\1", content, flags=re.DOTALL)
        output_path = module_dir / filename
        output_path.write_text(content, encoding="utf-8")
        written.append(filename)

        if verbose:
            print(f"  [PHASE_WRITER] Wrote {filename} ({len(content)} chars)")

    print(f"  [PHASE_WRITER] Written: {', '.join(written)} → {module_dir}")
    return input_data
