"""Fix UTF-8 mojibake in module markdown files caused by incorrect encoding during Notion pull."""
import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

PHASE_FILES = ["_starter_pack_ref.md", "lesson.md", "exitcheck.md", "warmup.md", "synthesis.md"]

# Direct replacement map for the mojibake sequences found in these files.
# Source: UTF-8 bytes decoded as cp1252 → wrong chars → map back to correct Unicode.
REPLACEMENTS = [
    # Each entry: (mojibake string, correct unicode char)
    # Derivation: original char → UTF-8 bytes → incorrectly decoded as cp1252 → mojibake
    ("\u00c3\u2014", "\u00d7"),        # Ã—  → ×  (U+00D7 mult sign;  UTF-8: C3 97; cp1252: C3=Ã, 97=—)
    ("\u00e2\u20ac\u201d", "\u2014"),  # â€"  → —  (U+2014 em dash;   UTF-8: E2 80 94; cp1252: E2=â, 80=€, 94=")
    ("\u00e2\u20ac\u201c", "\u2013"),  # â€"  → –  (U+2013 en dash;   UTF-8: E2 80 93; cp1252: E2=â, 80=€, 93=")
    ("\u00e2\u2020\u2019", "\u2192"),  # â†'  → →  (U+2192 r-arrow;  UTF-8: E2 86 92; cp1252: E2=â, 86=†, 92=')
    ("\u00e2\u20ac\u2122", "\u2019"),  # â€™  → '  (U+2019 r-s-quote; UTF-8: E2 80 99; cp1252: E2=â, 80=€, 99=™)
    ("\u00e2\u20ac\u0153", "\u201c"),  # â€œ  → "  (U+201C l-d-quote; UTF-8: E2 80 9C; cp1252: E2=â, 80=€, 9C=œ)
    ("\u00e2\u20ac\u009d", "\u201d"),  # â€   → "  (U+201D r-d-quote; UTF-8: E2 80 9D; cp1252: E2=â, 80=€, 9D=undef→use raw)
    ("\u00e2\u20ac\u2022", "\u2022"),  # â€¢  → •  (U+2022 bullet;    UTF-8: E2 80 95; cp1252: 95=•)
    ("\u00e2\u20ac\u2026", "\u2026"),  # â€¦  → …  (U+2026 ellipsis;  UTF-8: E2 80 A6; cp1252: A6=... mapped)
    ("\u00c3\u00a9", "\u00e9"),        # Ã©   → é  (U+00E9)
    ("\u00c3\u00a0", "\u00e0"),        # Ã    → à  (U+00E0)
    ("\u00c3\u00b3", "\u00f3"),        # Ã³   → ó  (U+00F3)
]


def fix_text(text: str) -> str:
    for bad, good in REPLACEMENTS:
        text = text.replace(bad, good)
    return text


def fix_module(unit: int, module: int, dry_run: bool = False) -> None:
    module_dir = PROJECT_ROOT / "units" / f"unit{unit}" / f"module{module}"
    if not module_dir.exists():
        print(f"Module dir not found: {module_dir}")
        return

    for filename in PHASE_FILES:
        path = module_dir / filename
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        fixed = fix_text(original)
        if original == fixed:
            print(f"  [OK] {filename} — no changes")
        else:
            counts = {label: original.count(bad) for bad, _ in REPLACEMENTS
                      for label in [repr(bad)] if original.count(bad)}
            detail = ", ".join(f"{v}x {k}" for k, v in counts.items() if v)
            print(f"  [FIX] {filename} — {detail}")
            if not dry_run:
                path.write_text(fixed, encoding="utf-8")


if __name__ == "__main__":
    unit = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    module = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    dry = "--dry-run" in sys.argv
    print(f"{'DRY RUN: ' if dry else ''}Fixing unit {unit} module {module}")
    fix_module(unit, module, dry_run=dry)
    print("Done.")
