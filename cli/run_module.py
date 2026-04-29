"""
Module Runner - Fetches the starter pack from Notion (if needed), then runs
warmup, lesson, exitcheck, and synthesis pipelines for a given module in parallel.

Usage:
    python cli/run_module.py --module 4 --unit 1
    python cli/run_module.py -m 4 -u 1
"""

import argparse
import subprocess
import sys
import threading
from pathlib import Path

project_root = Path(__file__).parent.parent

PIPELINES = [
    ("warmup", "warmup_generator_dialogue_pass", "warmup.md"),
    ("lesson", "lesson_generator_dialogue_pass", "lesson.md"),
    ("exitcheck", "exitcheck_generator_dialogue_pass", "exitcheck.md"),
    ("synthesis", "synthesis_generator_dialogue_pass", "synthesis.md"),
]

PIPELINES_V3 = [
    ("warmup", "warmup_generator_v3", "warmup.md"),
    ("lesson", "lesson_generator_v3", "lesson.md"),
    ("exitcheck", "exitcheck_generator_v3", "exitcheck.md"),
    ("synthesis", "synthesis_generator_v3", "synthesis.md"),
]

# lesson.md is the minimum required phase; others are optional
_REQUIRED_PHASE_FILES = ["lesson.md"]

_print_lock = threading.Lock()


def _module_dir(unit: int, module: int) -> Path:
    return project_root / "units" / f"unit{unit}" / f"module{module}"


def _starter_pack_ready(unit: int, module: int) -> bool:
    d = _module_dir(unit, module)
    return all((d / f).exists() for f in _REQUIRED_PHASE_FILES)


def _starter_pack_ref_exists(unit: int, module: int) -> bool:
    return (_module_dir(unit, module) / "_starter_pack_ref.md").exists()


def _run_ingestion(unit: int, module: int, pipeline: str = "starter_pack_ingestion") -> bool:
    """Run a starter pack ingestion pipeline. Returns True on success."""
    cmd = [
        sys.executable,
        str(project_root / "cli" / "run_pipeline.py"),
        "-p", pipeline,
        "-u", str(unit),
        "-m", str(module),
        "-y",
    ]
    print(f"[starter_pack] Running {pipeline} ...")
    proc = subprocess.run(cmd, cwd=str(project_root))
    return proc.returncode == 0


def _wait_for_starter_pack(unit: int, module: int) -> None:
    """Print manual instructions and block until _starter_pack_ref.md is placed."""
    dest = _module_dir(unit, module) / "_starter_pack_ref.md"
    dest.parent.mkdir(parents=True, exist_ok=True)

    print()
    print("=" * 60)
    print("STARTER PACK NOT FOUND — manual setup required")
    print("=" * 60)
    print()
    print("Either NOTION_API_KEY is not set or the Notion lookup failed.")
    print("To continue, manually download the starter pack:")
    print()
    print("  1. Open the module's starter pack page in Notion")
    print("  2. Export it as Markdown (··· menu → Export → Markdown & CSV)")
    print("  3. Place the exported .md file at:")
    print()
    print(f"       {dest}")
    print()

    while True:
        input("  Press Enter once the file is in place ...")
        if dest.exists():
            print("  [starter_pack] Found _starter_pack_ref.md — continuing")
            print()
            break
        print(f"  [starter_pack] File not found yet at {dest} — try again")
        print()


def prefixed_print(label, line):
    with _print_lock:
        print(f"[{label}] {line}", end="", flush=True)


def run_one(label, pipeline_name, module, unit, results):
    cmd = [
        sys.executable,
        str(project_root / "cli" / "run_pipeline.py"),
        "-p", pipeline_name,
        "-m", str(module),
        "-u", str(unit),
        "-y",
    ]

    prefixed_print(label, f"Starting {pipeline_name}\n")

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(project_root),
        )

        for line in proc.stdout:
            prefixed_print(label, line)

        proc.wait()
        results[label] = proc.returncode == 0

        status = "DONE" if proc.returncode == 0 else f"FAILED (exit {proc.returncode})"
        prefixed_print(label, f"{status}\n")

    except Exception as e:
        prefixed_print(label, f"ERROR: {e}\n")
        results[label] = False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch starter pack then run all pipeline types for a module in parallel"
    )
    parser.add_argument("-m", "--module", type=int, required=True, help="Module number")
    parser.add_argument("-u", "--unit", type=int, default=1, help="Unit number (default: 1)")
    args = parser.parse_args()

    print(f"\nModule Runner: unit {args.unit}, module {args.module}")
    print("=" * 60)

    # --- Starter pack ---
    if _starter_pack_ready(args.unit, args.module):
        print("[starter_pack] Phase files already present — skipping ingestion")
    elif _starter_pack_ref_exists(args.unit, args.module):
        print("[starter_pack] Ref found — running phase splitter and JSON loader")
        if not _run_ingestion(args.unit, args.module, pipeline="starter_pack_ingestion_from_ref"):
            print("[starter_pack] Ingestion failed — aborting")
            sys.exit(1)
        if not _starter_pack_ready(args.unit, args.module):
            print("[starter_pack] Phase files still missing after ingestion — aborting")
            sys.exit(1)
    else:
        _wait_for_starter_pack(args.unit, args.module)
        if not _run_ingestion(args.unit, args.module):
            print("[starter_pack] Ingestion failed — aborting")
            sys.exit(1)
        if not _starter_pack_ready(args.unit, args.module):
            print("[starter_pack] Phase files still missing after ingestion — aborting")
            sys.exit(1)

    # --- Generator pipelines ---
    pipeline_set = PIPELINES_V3 if args.unit >= 100 else PIPELINES
    mod_dir = _module_dir(args.unit, args.module)
    active_pipelines = [
        (label, pipeline_name)
        for label, pipeline_name, phase_file in pipeline_set
        if (mod_dir / phase_file).exists()
    ]
    skipped = [
        label for label, _, phase_file in pipeline_set
        if not (mod_dir / phase_file).exists()
    ]
    if skipped:
        print(f"[module] Skipping (no phase file): {', '.join(skipped)}")

    labels = [label for label, _ in active_pipelines]
    print(f"\nRunning in parallel: {', '.join(labels)}\n")

    results = {}
    threads = [
        threading.Thread(
            target=run_one,
            args=(label, pipeline_name, args.module, args.unit, results),
            daemon=True,
        )
        for label, pipeline_name in active_pipelines
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\n" + "=" * 60)
    print(f"MODULE {args.module} COMPLETE")
    print("=" * 60)
    for label in labels:
        ok = results.get(label, False)
        print(f"  {label:12s}  {'OK' if ok else 'FAILED'}")
    for label in skipped:
        print(f"  {label:12s}  SKIPPED (no phase file)")

    if not all(results.get(label, False) for label in labels):
        sys.exit(1)


if __name__ == "__main__":
    main()
