"""
toml_sequence_writer - Formatting Step

Converts a pull.json sequence (list of section dicts) into a TOML step file,
and reverse-stamps the generated TOML keys back into the source pull.json.

Step boundary rule: everything up to (not including) a current_scene beat is
one TOML step.

Beat mapping:
  dialogue      → dialogue = "..."
  prompt        → components = ["PromptComponent"], prompt_text = "..." (if text present)
  scene         → dropped
  current_scene → step terminator, dropped from TOML

Validator mapping (from prompt beats):
  is_correct=true  → [step_N_slug.correct]  dialogue + metadata = { "sting_id": "on_correct" }
  is_correct=false → [step_N_slug.step_M]   dialogue + id = <sting_id>

Sting ID resolution for non-correct validators (four tiers):
  1. selected value in condition → AI generates concise snake_case slug (specific wins)
  2. incorrect_count in condition (top-level or inside "and"):
       1 → "light", 2 → "medium", 3+ → "heavy"
  3. condition_id field on the validator → used directly
  4. AI fallback: Claude classifies description+condition → light/medium/heavy

Sub-step counter M starts at 501, increments globally for every validator
encountered (regardless of is_correct).

Stamping:
  _toml_key is written onto:
    - each section object (section key)
    - each current_scene beat that terminates a step (step key)
  For beats-format sections with no current_scene, only the section is stamped.
  _sting_id is written onto each non-correct validator after resolution.

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
    3: "chart_template",
    4: "chart_template",
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
    prompt_text: str | None = None
    for beat in beats:
        t = beat.get("type")
        if t == "dialogue":
            text = _normalize_quotes(beat.get("text", ""))
            dialogue_parts.append(_tag_vocab(text, vocab_open, vocab_close))
        elif t == "prompt":
            components.append("PromptComponent")
            if prompt_text is None and beat.get("text"):
                prompt_text = beat["text"]
        # scene → dropped
    fields: dict = {}
    if dialogue_parts:
        fields["dialogue"] = " ".join(dialogue_parts)
    if components:
        fields["components"] = components
    if prompt_text is not None:
        fields["prompt_text"] = prompt_text
    return fields


def _extract_validators(beats: list[dict]) -> list[dict]:
    """Return the validator list from the first prompt beat, or empty list."""
    for beat in beats:
        if beat.get("type") == "prompt":
            return beat.get("validator") or []
    return []


def _validator_dialogue(beats: list[dict], vocab_open: str, vocab_close: str) -> str | None:
    """Extract concatenated dialogue from a validator's beat list."""
    parts = []
    for beat in beats:
        if beat.get("type") == "dialogue":
            text = _normalize_quotes(beat.get("text", ""))
            parts.append(_tag_vocab(text, vocab_open, vocab_close))
    return " ".join(parts) if parts else None


def _extract_incorrect_count(condition: dict) -> int | None:
    """Find incorrect_count at top-level or inside an 'and' list."""
    count = condition.get("incorrect_count")
    if count is not None:
        return int(count)
    for item in condition.get("and", []):
        if isinstance(item, dict):
            count = item.get("incorrect_count")
            if count is not None:
                return int(count)
    return None


def _ai_slug_from_selected(selected: str) -> str:
    """Use Claude to produce a concise snake_case slug from a selected answer string."""
    try:
        import sys
        from pathlib import Path as _Path

        sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "core"))
        from claude_client import ClaudeClient

        prompt = (
            "Convert this multiple-choice answer into a concise snake_case identifier "
            "(2-4 words max, no articles, lowercase, underscores only).\n\n"
            f'Answer: "{selected}"\n\n'
            "Reply with only the identifier, nothing else."
        )
        client = ClaudeClient()
        result = client.generate(user_message=prompt, max_tokens=20, temperature=0).strip().lower()
        slug = re.sub(r"[^a-z0-9]+", "_", result).strip("_")
        return slug or re.sub(r"[^a-z0-9]+", "_", selected.lower()).strip("_")
    except Exception as e:
        print(f"  [TOML_SEQUENCE_WRITER] AI slug fallback failed: {e}")
        return re.sub(r"[^a-z0-9]+", "_", selected.lower()).strip("_")


def _sting_id_from_validator(validator: dict) -> str | None:
    """Deterministically resolve sting_id from condition or condition_id.

    Resolution order:
      1. selected value present → deferred to AI slug (specific condition wins)
      2. incorrect_count → light / medium / heavy
      3. condition_id → used directly
    """
    selected = (validator.get("condition") or {}).get("selected")
    if selected is not None:
        return None  # deferred to AI slug in _process
    count = _extract_incorrect_count(validator.get("condition") or {})
    if count is not None:
        if count <= 1:
            return "light"
        if count == 2:
            return "medium"
        return "heavy"
    cid = validator.get("condition_id")
    if cid:
        return cid
    return None


def _ai_infer_sting_id(validator: dict) -> str:
    """Use Claude to classify a validator as light / medium / heavy when
    condition-based logic cannot determine the sting_id."""
    try:
        import sys
        from pathlib import Path as _Path

        sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "core"))
        from claude_client import ClaudeClient

        dialogue_text = _validator_dialogue(validator.get("beats", []), "[vocab]", "[/vocab]") or ""
        condition_json = json.dumps(validator.get("condition", {}))
        description = validator.get("description", "")

        prompt = (
            "Classify this validator's remediation weight as exactly one of: "
            "light, medium, heavy.\n"
            "light = first-attempt hint  "
            "medium = second-attempt guidance  "
            "heavy = full model / final fallback\n\n"
            f"Description: {description}\n"
            f"Condition: {condition_json}\n"
            f"Feedback: {dialogue_text}\n\n"
            "Reply with exactly one word."
        )

        client = ClaudeClient()
        response = client.generate(user_message=prompt, max_tokens=20, temperature=0)
        result = response.strip().lower()
        if result in {"light", "medium", "heavy"}:
            return result
    except Exception as e:
        print(f"  [TOML_SEQUENCE_WRITER] AI sting_id fallback failed: {e}")
    return "light"


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
    if "\n" in s:
        return f'"""\n{s}\n"""'
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def _toml_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str):
        return _toml_str(v)
    if isinstance(v, list):
        items = ", ".join(_toml_str(i) if isinstance(i, str) else str(i) for i in v)
        return f"[{items}]"
    if isinstance(v, dict):
        pairs = ", ".join(f"{k} = {_toml_value(val)}" for k, val in v.items())
        return f"{{ {pairs} }}"
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
    use_ai_fallback: bool = True,
) -> str:
    """Stamp _toml_key into data in-place and return rendered TOML content."""
    lines: list[str] = [
        f"# {title}-script.toml",
        "",
        f'title = "{title}"',
        'type = "sequence"',
        "",
    ]

    section_counter = 101
    step_counter = 101
    sub_counter = 501  # global; increments for every validator (correct or not)
    section_display = 1
    first_step_in_script = True

    for section in data:
        raw_id = section.get("id", f"section_{section_counter}")
        slug = _slugify_id(raw_id)

        section_key = f"section_{section_counter}_{slug}"
        section_counter += 1

        section["_toml_key"] = section_key

        lines += [
            "# ---------------------------------------------------------------------------",
            f"# Section {section_display} - {slug}",
            "# ---------------------------------------------------------------------------",
            "",
            f"[{section_key}]",
            f'template = "{template}"',
            "",
        ]
        section_display += 1

        for active_beats, cs_beat in _iter_step_groups(section):
            fields = _beats_to_fields(active_beats, vocab_open, vocab_close)
            if not fields:
                continue

            if first_step_in_script:
                existing = fields.get("components", [])
                if "SceneComponent" not in existing:
                    fields["components"] = ["SceneComponent"] + existing
                first_step_in_script = False

            step_num = step_counter
            step_key = f"step_{step_num}_{slug}"
            step_key_bare = f"step_{step_num}"
            step_counter += 1

            if cs_beat is not None:
                cs_beat["_toml_key"] = step_key

            lines.append(f"[{step_key}]")
            for k, v in fields.items():
                lines.append(f"{k} = {_toml_value(v)}")
            lines.append("")

            # Emit sub-steps from validators in prompt beats
            validators = _extract_validators(active_beats)
            correct_emitted = False
            for validator in validators:
                dialogue = _validator_dialogue(validator.get("beats", []), vocab_open, vocab_close)
                if validator.get("is_correct"):
                    if not correct_emitted:
                        if dialogue:
                            sub_key = f"{step_key_bare}.correct"
                            lines.append(f"[{sub_key}]")
                            lines.append(f"dialogue = {_toml_value(dialogue)}")
                            lines.append(f"metadata = {_toml_value({'sting_id': 'on_correct'})}")
                            lines.append("")
                        correct_emitted = True
                    else:
                        cid = validator.get("condition_id", "")
                        condition = validator.get("condition") or {}
                        selected = condition.get("selected", "")
                        identifier = selected or cid or validator.get("description", "")
                        snippet = str(identifier)[:80].replace("\n", " ")
                        lines.append(f"# skipped correct branch: {snippet}")
                        lines.append("")
                else:
                    sting_id = _sting_id_from_validator(validator)
                    if sting_id is None:
                        selected = (validator.get("condition") or {}).get("selected")
                        if selected is not None:
                            sting_id = (
                                _ai_slug_from_selected(str(selected))
                                if use_ai_fallback
                                else re.sub(r"[^a-z0-9]+", "_", str(selected).lower()).strip("_")
                            )
                        else:
                            sting_id = _ai_infer_sting_id(validator) if use_ai_fallback else "light"
                    validator["_sting_id"] = sting_id
                    if dialogue:
                        sub_key = f"{step_key_bare}.step_{sub_counter}"
                        lines.append(f"[{sub_key}]")
                        lines.append(f"dialogue = {_toml_value(dialogue)}")
                        lines.append(f'id = "{sting_id}"')
                        lines.append("")
                sub_counter += 1

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
    use_ai_fallback: bool = True,
    verbose: bool = False,
    **_kwargs,
) -> str:
    """Convert a pull.json sequence to a TOML step file.

    Stamps _toml_key back into the source pull.json (section objects and
    current_scene beats). Also stamps _sting_id onto each non-correct validator.

    Args:
        data:             List of section dicts from pull.json.
        pull_json_path:   Path to the source pull.json to write stamps back into.
        output_path:      Where to write the .toml file.
        unit_number:      Used to build the title and auto-select template.
        module_number:    Used to build the title and auto-select template.
        phase:            Used to build the title (e.g. "lesson").
        template:         Section template name. Auto-detected from module if omitted.
        vocab_open:       Opening tag for vocab terms (default "[vocab]").
        vocab_close:      Closing tag for vocab terms (default "[/vocab]").
        use_ai_fallback:  Call Claude to infer sting_id when condition-based
                          logic cannot resolve it (default True).
        verbose:          Enable verbose logging.

    Returns:
        TOML content as a string.
    """
    if not isinstance(data, list):
        if verbose:
            print("  [TOML_SEQUENCE_WRITER] Input is not a list — skipping")
        return data

    resolved_template = template or (
        _MODULE_TEMPLATES.get(module_number, "PLACEHOLDER")
        if module_number is not None
        else "PLACEHOLDER"
    )
    title = _make_title(unit_number, module_number, phase)
    toml_content = _process(
        data,
        title,
        vocab_open,
        vocab_close,
        template=resolved_template,
        use_ai_fallback=use_ai_fallback,
    )

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

    project_root = Path(__file__).resolve().parents[2]
    tracked_scripts_root = project_root / "tracked_scripts"

    parser = argparse.ArgumentParser(description="Convert pull.json to a TOML sequence file.")
    parser.add_argument("-u", "--unit", type=int, required=True, help="Unit number (e.g. 1)")
    parser.add_argument("-m", "--module", type=int, required=True, help="Module number (e.g. 9)")
    parser.add_argument(
        "--phase", help="Phase name (e.g. warmup, lesson). Auto-detected if only one exists."
    )
    parser.add_argument(
        "--dest",
        help="Destination path or directory (overrides auto-detected path from SEQUENCES_DIR env)",
    )
    cli_args = parser.parse_args()

    unit_number = cli_args.unit
    module_number = cli_args.module
    module_dir = tracked_scripts_root / f"u{unit_number}" / f"m{module_number}"

    if not module_dir.exists():
        print(f"[ERROR] Module directory not found: {module_dir}")
        sys.exit(1)

    # Resolve phase directory
    if cli_args.phase:
        phase = cli_args.phase
        phase_dir = module_dir / phase
        if not phase_dir.exists():
            print(f"[ERROR] Phase directory not found: {phase_dir}")
            sys.exit(1)
    else:
        phase_dirs = [d for d in module_dir.iterdir() if d.is_dir()]
        if len(phase_dirs) == 1:
            phase_dir = phase_dirs[0]
            phase = phase_dir.name
        else:
            names = [d.name for d in phase_dirs]
            print(f"[ERROR] Multiple phases found — specify --phase: {names}")
            sys.exit(1)

    # Find the latest step_*_pull directory
    pull_dirs = sorted(
        [
            (int(m.group(1)), d)
            for d in phase_dir.iterdir()
            if d.is_dir() and (m := re.match(r"^step_(\d+)_pull$", d.name))
        ]
    )
    if not pull_dirs:
        print(f"[ERROR] No step_*_pull directory found in {phase_dir}")
        sys.exit(1)
    pull_path = pull_dirs[-1][1] / "pull.json"
    if not pull_path.exists():
        print(f"[ERROR] pull.json not found: {pull_path}")
        sys.exit(1)

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
                Path(sequences_base)
                / f"unit{unit_number}"
                / f"module_{module_number}"
                / output_path.name
            )

    if dest_path is not None:
        ingested_folder = dest_path.parent / dest_path.stem
        if ingested_folder.exists():
            print(
                f"  [WARNING] {ingested_folder.name}/ exists — "
                "Lesson Lab edits in that folder will be deleted on copy."
            )
        answer = input(f"Copy {output_path.name} to {dest_path}? [y/n] ").strip().lower()
        if answer == "y":
            module_dir = dest_path.parent
            is_new_dir = not module_dir.exists()
            module_dir.mkdir(parents=True, exist_ok=True)
            if ingested_folder.exists():
                shutil.rmtree(str(ingested_folder))
                print(f"  [TOML_SEQUENCE_WRITER] Deleted {ingested_folder.name}/")
            shutil.copy2(str(output_path), str(dest_path))
            print(f"  [TOML_SEQUENCE_WRITER] Copied to {dest_path}")
            # Copy .modtag from module_example if missing from module dir
            if not (module_dir / ".modtag").exists():
                sequences_base = os.environ.get("SEQUENCES_DIR", "").strip()
                if sequences_base:
                    modtag_src = (
                        Path(sequences_base) / f"unit{unit_number}" / "module_example" / ".modtag"
                    )
                    if modtag_src.exists():
                        shutil.copy2(str(modtag_src), str(module_dir / ".modtag"))
                        print(f"  [TOML_SEQUENCE_WRITER] Copied .modtag to {module_dir}")
        else:
            print(f"  [TOML_SEQUENCE_WRITER] Kept at {output_path}")
