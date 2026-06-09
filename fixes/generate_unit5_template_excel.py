"""One-off script: generate CSV of all Unit 5 problem templates."""

import csv
import json
from pathlib import Path

UNIT5_DIR = Path(__file__).parent.parent / "units" / "unit5"
OUTPUT_PATH = Path(__file__).parent.parent / "outputs" / "unit5_templates.csv"

COLS = [
    "Unit",
    "Module",
    "Template ID",
    "Skill ID",
    "Skill Description",
    "Problem Type (Template Description)",
]


def load_modern(path, module_num):
    """Load modern array-format problem_templates.json."""
    rows = []
    seen = set()
    with open(path, encoding="utf-8") as f:
        templates = json.load(f)
    for t in templates:
        tid = str(t.get("template_id", ""))
        if tid in seen:
            continue
        seen.add(tid)
        rows.append(
            {
                "Unit": "Unit 5",
                "Module": f"Module {module_num}",
                "Template ID": tid,
                "Skill ID": str(t.get("skill_id", "")),
                "Skill Description": str(t.get("skill", "")),
                "Problem Type (Template Description)": str(t.get("problem_type", "")),
            }
        )
    return rows


def load_legacy(path, module_num):
    """Load legacy goals-format problem_templates.json (modules 1–3)."""
    rows = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    goals = data.get("goals", [])
    for g in goals:
        gid = g.get("id", "")
        rows.append(
            {
                "Unit": "Unit 5",
                "Module": f"Module {module_num}",
                "Template ID": f"M{module_num}-{str(gid).zfill(2)}",
                "Skill ID": f"M{module_num}-{str(gid).zfill(2)}",
                "Skill Description": str(g.get("text", "")),
                "Problem Type (Template Description)": str(g.get("text", "")),
            }
        )
    return rows


def build_rows():
    all_rows = []
    for module_num in range(1, 13):
        path = UNIT5_DIR / f"module{module_num}" / "problem_templates.json"
        if not path.exists():
            print(f"  WARNING: {path} not found, skipping")
            continue
        with open(path, encoding="utf-8") as f:
            raw = f.read().strip()
        if raw.startswith("["):
            rows = load_modern(path, module_num)
        else:
            rows = load_legacy(path, module_num)
        print(f"  Module {module_num}: {len(rows)} templates")
        all_rows.extend(rows)
    return all_rows


def write_csv(rows):
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSaved: {OUTPUT_PATH}")
    print(f"Total rows: {len(rows)}")


if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    print("Building rows...")
    rows = build_rows()
    print("\nWriting CSV...")
    write_csv(rows)
