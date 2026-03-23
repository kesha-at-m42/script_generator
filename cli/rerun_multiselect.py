"""
rerun_multiselect.py - Batch rerun for multiselect MC remediations

Discovers all pipeline+module runs that contain multi_select questions and
reruns remediation_filter → remediation_generator → remediation_merger for
each, skipping notion_push.

Usage:
    python cli/rerun_multiselect.py [--unit N] [--trial] [--yes] [--verbose]

    --unit N   : unit number to scan (default: 1)
    --trial    : stop after the first matching module (for testing)
    --yes / -y : skip per-pipeline confirmation prompts
    --verbose  : verbose pipeline output
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.path_manager import get_project_paths  # noqa: E402
from core.version_manager import get_latest_version  # noqa: E402


def has_multiselect(json_path):
    """Return True if the JSON file contains any multi_select prompt beat."""
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    if isinstance(data, dict):
        data = data.get("data", [])
    if not isinstance(data, list):
        return False
    for section in data:
        for step_beats in section.get("steps", []):
            for beat in step_beats:
                if beat.get("type") == "prompt" and beat.get("tool") == "multi_select":
                    return True
    return False


def find_step1_output(version_dir):
    """Return the first non-error JSON file in the step_01_* directory."""
    for step_dir in sorted(version_dir.glob("step_01_*")):
        for f in sorted(step_dir.glob("*.json")):
            if f.name != "errors.json":
                return f
    return None


def discover_targets(unit_number):
    """Scan outputs/unit{N}/ and return targets with multi_select questions."""
    out_base = get_project_paths()["outputs"] / f"unit{unit_number}"
    if not out_base.exists():
        print(f"Error: outputs directory not found: {out_base}")
        sys.exit(1)

    targets = []
    for pipeline_dir in sorted(out_base.iterdir()):
        if not pipeline_dir.is_dir():
            continue

        match = re.match(r"(.+?)_module_(\d+)(?:_path_([abc]))?$", pipeline_dir.name)
        if not match:
            continue

        pipeline_name, module_str, path_letter = match.groups()

        # Skip pipelines without a remediation_filter step
        if "dialogue_pass" in pipeline_name:
            continue

        latest = get_latest_version(pipeline_dir)
        if not latest:
            continue

        version_dir = pipeline_dir / latest
        step1 = find_step1_output(version_dir)
        if step1 and has_multiselect(step1):
            targets.append(
                {
                    "pipeline_name": pipeline_name,
                    "module_number": int(module_str),
                    "path_letter": path_letter,
                    "unit_number": unit_number,
                    "label": pipeline_dir.name,
                }
            )

    return targets


def rerun_target(target, yes=False, verbose=False):
    """Call rerun.py via subprocess for the given target."""
    cmd = [
        sys.executable,
        str(project_root / "cli" / "rerun.py"),
        target["pipeline_name"],
        "--step-args",
        "remediation_filter",
        "mode=multiselect_mc",
        "--start-from",
        "filter_sections",
        "--end-at",
        "merge_remediation",
        "--module",
        str(target["module_number"]),
        "--unit",
        str(target["unit_number"]),
    ]
    if yes:
        cmd.append("--yes")
    if verbose:
        cmd.append("--verbose")
    if target.get("path_letter"):
        cmd += ["--path", target["path_letter"]]

    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Batch rerun multiselect MC remediations across all matching pipelines"
    )
    parser.add_argument("--unit", type=int, default=1, help="Unit number (default: 1)")
    parser.add_argument("--trial", action="store_true", help="Stop after first matching module")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompts")
    parser.add_argument("--verbose", action="store_true", help="Verbose pipeline output")
    args = parser.parse_args()

    print(f"\nScanning unit {args.unit} for pipelines with multiselect questions...")
    targets = discover_targets(args.unit)

    if not targets:
        print("No pipelines with multi_select questions found.")
        return

    print(f"\nFound {len(targets)} pipeline(s) with multiselect questions:")
    for t in targets:
        print(f"  {t['label']}")

    if args.trial:
        targets = targets[:1]
        print(f"\n[TRIAL] Running only: {targets[0]['label']}")

    print()
    for i, target in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {target['label']}")
        rerun_target(target, yes=args.yes, verbose=args.verbose)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
