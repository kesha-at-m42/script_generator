"""
Module Runner - Runs warmup, lesson, exitcheck, and synthesis pipelines
for a given module in parallel.

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
    ("warmup", "warmup_generator_dialogue_pass"),
    ("lesson", "lesson_generator_dialogue_pass"),
    ("exitcheck", "exitcheck_generator_dialogue_pass"),
    ("synthesis", "synthesis_generator_dialogue_pass"),
]

_print_lock = threading.Lock()


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
        description="Run all pipeline types for a module in parallel"
    )
    parser.add_argument("-m", "--module", type=int, required=True, help="Module number")
    parser.add_argument("-u", "--unit", type=int, default=1, help="Unit number (default: 1)")
    args = parser.parse_args()

    labels = [label for label, _ in PIPELINES]
    print(f"\nModule Runner: unit {args.unit}, module {args.module}")
    print(f"Running in parallel: {', '.join(labels)}")
    print("=" * 60 + "\n")

    results = {}
    threads = [
        threading.Thread(
            target=run_one,
            args=(label, pipeline_name, args.module, args.unit, results),
            daemon=True,
        )
        for label, pipeline_name in PIPELINES
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

    if not all(results.get(label, False) for label in labels):
        sys.exit(1)


if __name__ == "__main__":
    main()
