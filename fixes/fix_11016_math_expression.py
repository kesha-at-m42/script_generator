"""
fix_11016_math_expression.py

For all sequences with template_id 11016:
  - Shuffle the fraction order in the MathExpression workspace
  - Insert " " between each fraction in terms
  - Create workspace with MathExpression if it doesn't exist yet

Usage:
    python fix_11016_math_expression.py <input_file> [output_file]

If output_file is omitted the input file is overwritten.
"""

import json
import random
import sys
from pathlib import Path


def process(data: dict | list) -> int:
    """Mutates data in place. Returns number of steps modified."""
    sequences = data.get("sequences", data) if isinstance(data, dict) else data
    count = 0

    for seq in sequences:
        if not isinstance(seq, dict):
            continue
        meta = seq.get("metadata", {})
        if str(meta.get("template_id")) != "11016":
            continue

        for step in seq.get("steps", []):
            if not isinstance(step, dict):
                continue

            # --- Find existing MathExpression (or decide we need to create one) ---
            workspace = step.get("workspace")
            tangibles = []
            math_tangible = None

            if isinstance(workspace, dict):
                tangibles = workspace.get("tangibles", [])
                for t in tangibles:
                    if isinstance(t, dict) and t.get("@type") == "MathExpression":
                        math_tangible = t
                        break

            # Collect the fraction terms (skip any existing " " spacers)
            if math_tangible is not None:
                fracs = [
                    term for term in math_tangible.get("terms", [])
                    if isinstance(term, str) and term.strip()
                ]
            else:
                # Fall back to identifiers
                fracs = list(meta.get("identifiers", []))

            if not fracs:
                continue

            # Shuffle then interleave with spaces
            random.shuffle(fracs)
            new_terms = []
            for i, frac in enumerate(fracs):
                new_terms.append(frac)
                if i < len(fracs) - 1:
                    new_terms.append(" ")

            if math_tangible is not None:
                math_tangible["terms"] = new_terms
            else:
                # Build workspace from scratch
                if not isinstance(workspace, dict):
                    workspace = {"@type": "WorkspaceData", "tangibles": []}
                    step["workspace"] = workspace
                workspace.setdefault("tangibles", []).append({
                    "@type": "MathExpression",
                    "is_read_only": True,
                    "terms": new_terms,
                })

            count += 1

    return count


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_11016_math_expression.py <input_file> [output_file]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    modified = process(data)
    print(f"Modified {modified} step(s) across 11016 sequences")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
