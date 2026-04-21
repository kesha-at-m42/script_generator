"""
toml_sequence_writer - Formatting Step

Converts a pull.json sequence (list of section dicts) into a TOML step file,
and reverse-stamps the generated TOML keys back into the source pull.json.

Step boundary rule: everything up to (not including) a current_scene beat is
one TOML step.

Beat mapping:
  dialogue      → dialogue = "..."
  prompt        → components = ["PromptComponent"]
  scene         → dropped
  current_scene → step terminator, dropped from TOML

Stamping:
  _toml_key is written onto:
    - each section object (section key)
    - each current_scene beat that terminates a step (step key)
  For beats-format sections with no current_scene, only the section is stamped.

Numbering: sections and steps are numbered with independent counters, both
starting at 100.

Vocab tagging: words wrapped in {curly braces} in dialogue are replaced with
configurable open/close tags. Defaults to [vocab]word[/vocab]. Override via
vocab_open / vocab_close params.

CLI usage:
    python steps/formatting/toml_sequence_writer.py <pull_json_path> [--dest <path>]

    Phase, unit, and module are auto-detected from the path. The output file is
    named {phase}.toml (e.g. warmup.toml) and written into the existing step_*_toml
    directory, or a new auto-numbered one.

    Destination is auto-detected from SEQUENCES_DIR env variable as
    {SEQUENCES_DIR}/unit{N}/module_{M}/{phase}.toml. Override with --dest.
    Prompts y/n before copying in either case.

Pipeline config example:
    {
        "name": "toml_sequence_writer",
        "type": "formatting",
        "function": "toml_sequence_writer.write",
        "function_args": {
            "pull_json_path": "tracked_scripts/unit1/module_1/lesson/step_14_pull/pull.json",
            "output_path": "tracked_scripts/unit1/module_1/lesson/step_15_toml/lesson.toml",
            "unit_number": 1,
            "module_number": 1,
            "phase": "lesson"
        }
    }
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Module → template mapping
# ---------------------------------------------------------------------------

# Modules not listed here fall back to "PLACEHOLDER".
_MODULE_TEMPLATES: dict[int, str] = {
    1: "chart_template",
    2: "chart_template",
    11: "array_template",
    12: "array_template",
}


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------

def _slugify_id(raw_id: str) -> str:
    """Strip leading sN_N_ prefix to get a friendly slug.

    s1_1_data_collection  ->  data_collection
    """
    match = re.match(r"^s\d+_\d+_(.+)$", raw_id)
    return match.group(1) if match else raw_id


def _make_title(unit_number: int | None, module_number: int | None, phase: str | None) -> str:
    if phase:
        return phase
    if unit_number is not None and module_number is not None:
        return f"unit_{unit_number}_module_{module_number}"
    return "lesson"


# ---------------------------------------------------------------------------
# Beat helpers
# ---------------------------------------------------------------------------

def _normalize_quotes(text: str) -> str:
    """Convert Unicode curly quotes to straight ASCII double quotes.

    Trailing curly right quotes are stripped first — they are authoring
    artifacts, not valid punctuation.
    """
    text = text.rstrip("\u201d")
    return text.replace("\u201c", '"').replace("\u201d", '"')


def _tag_vocab(text: str, open_tag: str, close_tag: str) -> str:
    """Replace {word} patterns with open_tag + word + close_tag."""
    return re.sub(r"\{([^}]+)\}", lambda m: f"{open_tag}{m.group(1)}{close_tag}", text)


def _beats_to_fields(beats: list[dict], vocab_open: str, vocab_close: str) -> dict:
    """Map a beat group to TOML step fields."""
    dialogue_parts: list[str] = []
    components: list[str] = []
    for beat in beats:
        t = beat.get("type")
        if t == "dialogue":
            text = _normalize_quotes(beat.get("text", ""))
            dialogue_parts.append(_tag_vocab(text, vocab_open, vocab_close))
        elif t == "prompt":
            components.append("PromptComponent")
        # scene → dropped
    fields: dict = {}
    if dialogue_parts:
        fields["dialogue"] = " ".join(dialogue_parts)
    if components:
        fields["components"] = components
    return fields


def _iter_step_groups(section: dict):
    """Yield (active_beats, current_scene_beat_or_None) for each step in a section.

    For steps-format sections: each inner array is one step; the current_scene
    beat at its end is the stamp target.

    For beats-format sections: split the flat list on current_scene beats.
    """
    if "steps" in section:
        for inner in section["steps"]:
            cs = next((b for b in inner if b.get("type") == "current_scene"), None)
            active = [b for b in inner if b.get("type") != "current_scene"]
            yield active, cs

    elif "beats" in section:
        current: list[dict] = []
        for beat in section["beats"]:
            if beat.get("type") == "current_scene":
                yield current, beat
                current = []
            else:
                current.append(beat)
        if current:
            yield current, None  # no current_scene terminator


# ---------------------------------------------------------------------------
# TOML serialisation
# ---------------------------------------------------------------------------

def _toml_str(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def _toml_value(v: Any) -> str:
    if isinstance(v, str):
        return _toml_str(v)
    if isinstance(v, list):
        items = ", ".join(_toml_str(i) if isinstance(i, str) else str(i) for i in v)
        return f"[{items}]"
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


# ---------------------------------------------------------------------------
# Core: assign keys, stamp source data, render TOML
# ---------------------------------------------------------------------------

def _process(
    data: list[dict],
    title: str,
    vocab_open: str,
    vocab_close: str,
    template: str = "PLACEHOLDER",
) -> str:
    """Stamp _toml_key into data in-place and return rendered TOML content."""
    lines: list[str] = [
        f'title = "{title}"',
        'type = "sequence"',
        "",
    ]

    section_counter = 100
    step_counter = 100

    for section in data:
        raw_id = section.get("id", f"section_{section_counter}")
        slug = _slugify_id(raw_id)

        section_key = f"section_{section_counter}_{slug}"
        section_counter += 1

        section["_toml_key"] = section_key

        lines += [
            f"# --- Section: {slug} ---",
            f"[{section_key}]",
            f'template = "{template}"',
            "",
        ]

        first_step_in_section = True

        for active_beats, cs_beat in _iter_step_groups(section):
            fields = _beats_to_fields(active_beats, vocab_open, vocab_close)
            if not fields:
                continue

            if first_step_in_section:
                existing = fields.get("components", [])
                if "SceneComponent" not in existing:
                    fields["components"] = ["SceneComponent"] + existing
                first_step_in_section = False

            step_key = f"step_{step_counter}_{slug}"
            step_counter += 1

            if cs_beat is not None:
                cs_beat["_toml_key"] = step_key

            lines.append(f"[{step_key}]")
            for k, v in fields.items():
                lines.append(f"{k} = {_toml_value(v)}")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public step function
# ---------------------------------------------------------------------------

def write(
    data: Any,
    pull_json_path: str | Path | None = None,
    output_path: str | Path | None = None,
    unit_number: int | None = None,
    module_number: int | None = None,
    phase: str | None = None,
    template: str | None = None,
    vocab_open: str = "[vocab]",
    vocab_close: str = "[/vocab]",
    verbose: bool = False,
    **_kwargs,
) -> str:
    """Convert a pull.json sequence to a TOML step file.

    Stamps _toml_key back into the source pull.json (section objects and
    current_scene beats).

    Args:
        data:           List of section dicts from pull.json.
        pull_json_path: Path to the source pull.json to write _toml_key stamps back into.
        output_path:    Where to write the .toml file.
        unit_number:    Used to build the title and auto-select template.
        module_number:  Used to build the title and auto-select template.
        phase:          Used to build the title (e.g. "lesson").
        template:       Section template name. Auto-detected from module if omitted.
        vocab_open:     Opening tag for vocab terms (default "[vocab]").
        vocab_close:    Closing tag for vocab terms (default "[/vocab]").
        verbose:        Enable verbose logging.

    Returns:
        TOML content as a string.
    """
    if not isinstance(data, list):
        if verbose:
            print("  [TOML_SEQUENCE_WRITER] Input is not a list — skipping")
        return data

    resolved_template = template or (
        _MODULE_TEMPLATES.get(module_number, "PLACEHOLDER") if module_number is not None else "PLACEHOLDER"
    )
    title = _make_title(unit_number, module_number, phase)
    toml_content = _process(data, title, vocab_open, vocab_close, template=resolved_template)

    if output_path is not None:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(toml_content)
        print(f"  [TOML_SEQUENCE_WRITER] Written TOML: {out}")

    if pull_json_path is not None:
        src = Path(pull_json_path)
        src.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  [TOML_SEQUENCE_WRITER] Stamped pull.json: {src}")
    elif verbose:
        print("  [TOML_SEQUENCE_WRITER] No pull_json_path — _toml_key stamps not persisted")

    return toml_content


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    import os
    import shutil
    import sys

    from dotenv import load_dotenv

    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Convert pull.json to a TOML sequence file."
    )
    parser.add_argument("pull_json_path", help="Path to pull.json")
    parser.add_argument(
        "--dest",
        help="Destination path or directory (overrides auto-detected path from SEQUENCES_DIR env)",
    )
    parser.add_argument("--unit", type=int, help="Unit number (auto-detected from path if omitted)")
    parser.add_argument(
        "--module", type=int, help="Module number (auto-detected from path if omitted)"
    )
    parser.add_argument("--phase", help="Phase name (auto-detected from path if omitted)")
    cli_args = parser.parse_args()

    pull_path = Path(cli_args.pull_json_path).resolve()
    if not pull_path.exists():
        print(f"[ERROR] File not found: {pull_path}")
        sys.exit(1)

    # Auto-detect phase from path: .../u1/m11/warmup/step_13_pull/pull.json → warmup
    phase_dir = pull_path.parent.parent
    phase = cli_args.phase or phase_dir.name

    # Auto-detect unit/module from path segments (e.g. u1/m11)
    unit_number = cli_args.unit
    module_number = cli_args.module
    if unit_number is None or module_number is None:
        for part in pull_path.parts:
            if unit_number is None:
                um = re.match(r"^u(\d+)$", part)
                if um:
                    unit_number = int(um.group(1))
            if module_number is None:
                mm = re.match(r"^m(\d+)$", part)
                if mm:
                    module_number = int(mm.group(1))

    # Reuse existing step_*_toml dir, or auto-number a new one
    existing_toml_dirs = sorted(
        [
            (int(tm.group(1)), d)
            for d in phase_dir.iterdir()
            if d.is_dir() and (tm := re.match(r"step_(\d+)_toml$", d.name))
        ]
    )
    if existing_toml_dirs:
        out_dir = existing_toml_dirs[-1][1]
    else:
        existing_nums = [
            int(nm.group(1))
            for d in phase_dir.iterdir()
            if d.is_dir() and (nm := re.match(r"step_(\d+)_", d.name))
        ]
        next_num = max(existing_nums) + 1 if existing_nums else 1
        out_dir = phase_dir / f"step_{next_num:02d}_toml"
        out_dir.mkdir(parents=True, exist_ok=True)

    output_path = out_dir / f"{phase}-script.toml"

    data = json.loads(pull_path.read_text(encoding="utf-8"))

    write(
        data=data,
        pull_json_path=pull_path,
        output_path=output_path,
        unit_number=unit_number,
        module_number=module_number,
        phase=phase,
    )

    # Resolve destination: explicit --dest → SEQUENCES_DIR env → skip
    dest_path: Path | None = None
    if cli_args.dest:
        dest_path = Path(cli_args.dest)
        if dest_path.is_dir():
            dest_path = dest_path / output_path.name
    elif unit_number is not None and module_number is not None:
        sequences_base = os.environ.get("SEQUENCES_DIR", "").strip()
        if sequences_base:
            dest_path = (
                Path(sequences_base) / f"unit{unit_number}" / f"module_{module_number}" / output_path.name
            )

    if dest_path is not None:
        answer = input(f"Copy {output_path.name} to {dest_path}? [y/n] ").strip().lower()
        if answer == "y":
            module_dir = dest_path.parent
            is_new_dir = not module_dir.exists()
            module_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(output_path), str(dest_path))
            print(f"  [TOML_SEQUENCE_WRITER] Copied to {dest_path}")
            # Copy .modtag from module_example if missing from module dir
            if not (module_dir / ".modtag").exists():
                sequences_base = os.environ.get("SEQUENCES_DIR", "").strip()
                if sequences_base:
                    modtag_src = Path(sequences_base) / f"unit{unit_number}" / "module_example" / ".modtag"
                    if modtag_src.exists():
                        shutil.copy2(str(modtag_src), str(module_dir / ".modtag"))
                        print(f"  [TOML_SEQUENCE_WRITER] Copied .modtag to {module_dir}")
        else:
            print(f"  [TOML_SEQUENCE_WRITER] Kept at {output_path}")
