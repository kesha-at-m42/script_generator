"""
One-off fix: convert v9 remediation_generator item files from [[states...]] format
to {"id": "...", "incorrects": [[states...]]} format, then rebuild the collated output.

Run from project root:
    python fixes/fix_v9_remediation_format.py
"""

import json
from pathlib import Path

V9 = Path("outputs/unit1/lesson_generator_module_1/v9")
STEP2 = V9 / "step_02_filter_sections" / "filter_sections.json"
STEP3 = V9 / "step_03_remediation_generator"
ITEMS_DIR = STEP3 / "items"
COLLATED = STEP3 / "remediation_generator.json"


def is_old_format(data):
    """Old format: a list whose elements are lists (array of arrays)."""
    return isinstance(data, list) and all(isinstance(el, list) for el in data)


def main():
    filter_output = json.loads(STEP2.read_text(encoding="utf-8"))
    batch_only_ids = set(filter_output["batch_only_items"])
    all_sections = filter_output["data"]

    # --- Fix item files and collect converted results ---
    converted = {}
    for item_path in sorted(ITEMS_DIR.glob("*.json")):
        item_id = item_path.stem
        data = json.loads(item_path.read_text(encoding="utf-8"))

        if is_old_format(data):
            wrapped = {"id": item_id, "incorrects": data}
            item_path.write_text(json.dumps(wrapped, indent=2), encoding="utf-8")
            print(f"  fixed  {item_id}")
            converted[item_id] = wrapped
        elif isinstance(data, dict) and "incorrects" in data:
            print(f"  ok     {item_id}")
            converted[item_id] = data
        else:
            print(f"  SKIP   {item_id}  (unexpected format: {type(data).__name__})")

    # --- Rebuild collated output ---
    # Order follows all_sections; processed items use {id, incorrects}, others passthrough.
    collated = []
    for section in all_sections:
        sid = section["id"]
        if sid in batch_only_ids:
            if sid in converted:
                collated.append(converted[sid])
            else:
                print(
                    f"  WARN   {sid} in batch_only_items but no item file found — using passthrough"
                )
                collated.append(section)
        else:
            collated.append(section)

    COLLATED.write_text(json.dumps(collated, indent=2), encoding="utf-8")
    print(f"\nWrote {len(collated)} items to {COLLATED}")
    print(
        f"  processed ({{id, incorrects}}): {sum(1 for x in collated if isinstance(x, dict) and 'incorrects' in x)}"
    )
    print(
        f"  passthrough (full section):    {sum(1 for x in collated if isinstance(x, dict) and 'incorrects' not in x)}"
    )


if __name__ == "__main__":
    main()
