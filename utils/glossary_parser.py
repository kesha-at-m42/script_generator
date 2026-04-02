"""
glossary_parser - Shared utility

Parses a glossary.md file into structured data. Used by toy_spec_loader
(for phrase → canonical name matching) and glossary_drift_checker (for
validation and drift reporting). No project-specific imports.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class GlossaryData:
    canonical_toys: set        # valid tangible_type values
    canonical_tools: set       # valid tool values in prompt beats
    phrase_map: dict           # natural language phrase → canonical (not flagged as drift)
    spec_aliases: dict         # renamed/superseded term → canonical (flagged as drift)

    @property
    def full_alias_map(self) -> dict:
        """Combined lookup for toy_spec_loader: phrase_map + spec_aliases → canonical."""
        return {**self.phrase_map, **self.spec_aliases}


def parse_glossary(glossary_path: Path) -> GlossaryData:
    """Parse glossary.md and return structured GlossaryData.

    Recognises four table types by their first column header:
      - `tangible_type`  → canonical_toys
      - `tool`           → canonical_tools
      - `spec phrase`    → phrase_map  (natural language, not drift-flagged)
      - `spec term`      → spec_aliases (deprecated terms, drift-flagged)
    """
    canonical_toys: set = set()
    canonical_tools: set = set()
    phrase_map: dict = {}
    spec_aliases: dict = {}

    lines = glossary_path.read_text(encoding="utf-8").splitlines()
    current_table = None

    for line in lines:
        stripped = line.strip()

        if not (stripped.startswith("|") and stripped.count("|") >= 2):
            continue

        cols = [c.strip().strip("`") for c in stripped.split("|")[1:-1]]
        if not cols:
            continue

        first = cols[0].lower()

        # Separator row
        if all(c.replace("-", "").replace(" ", "") == "" for c in cols):
            continue

        # Header row — sets table type for subsequent data rows
        if first == "tangible_type":
            current_table = "toys"
            continue
        if first == "tool":
            current_table = "tools"
            continue
        if first == "spec phrase":
            current_table = "phrases"
            continue
        if first in ("spec term", "do not use"):
            current_table = "aliases"
            continue

        # Data row
        val = cols[0]
        if not val:
            continue

        if current_table == "toys":
            canonical_toys.add(val)
        elif current_table == "tools":
            canonical_tools.add(val)
        elif current_table in ("phrases", "aliases") and len(cols) >= 2:
            target = cols[1].strip("`")
            if not target or target.startswith("—") or target.startswith("-"):
                continue
            key = val.lower()
            if current_table == "phrases":
                phrase_map[key] = target
            else:
                spec_aliases[key] = target

    return GlossaryData(
        canonical_toys=canonical_toys,
        canonical_tools=canonical_tools,
        phrase_map=phrase_map,
        spec_aliases=spec_aliases,
    )
