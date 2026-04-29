import json
import glob
import os


def iter_prompts(data):
    for section in data:
        if not isinstance(section, dict):
            continue
        section_id = section.get("id", "?")
        if "beats" in section:
            for beat in section["beats"]:
                if isinstance(beat, dict) and beat.get("type") == "prompt":
                    yield section_id, beat
        elif "steps" in section:
            for step_group in section["steps"]:
                for step in step_group:
                    if isinstance(step, dict) and step.get("type") == "prompt":
                        yield section_id, step


def has_catchall(validator):
    """True if any validator entry has an empty condition (catches anything)."""
    return any(v.get("condition") == {} for v in validator)


files = glob.glob("tracked_scripts/u1/**/merge_remediation.json", recursive=True)
results = []

for filepath in sorted(files):
    norm = filepath.replace(os.sep, "/")
    parts = norm.split("/")
    rel = "/".join(parts[2:])

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    for section_id, prompt in iter_prompts(data):
        tool = prompt.get("tool", "")
        validator = prompt.get("validator", [])
        if not validator:
            continue

        correct_entries = [v for v in validator if v.get("is_correct") is True]
        incorrect_entries = [v for v in validator if v.get("is_correct") is False]

        # Only care about tools where wrong answers are possible
        if tool == "multiple_choice":
            options = prompt.get("options", [])
            covered = set()
            for v in validator:
                sel = v.get("condition", {}).get("selected")
                if sel is not None:
                    covered.add(sel)
            uncovered = [o for o in options if o not in covered]
            # Concerning: some options have no handler AND no catchall for wrong answers
            if uncovered and not incorrect_entries and not has_catchall(validator):
                results.append((rel, section_id, tool, uncovered))

        elif tool in ("click_component", "click_category"):
            # These have a discrete correct answer; flag if no wrong-answer handling and no catchall
            if correct_entries and not incorrect_entries and not has_catchall(validator):
                results.append((rel, section_id, tool, []))

print("=== Prompts with a correct answer but unhandled wrong answers: %d ===" % len(results))
for path, sid, tool, uncovered in results:
    if uncovered:
        print("  %-65s  %s  [%s]  unhandled: %s" % (path, sid, tool, uncovered))
    else:
        print("  %-65s  %s  [%s]" % (path, sid, tool))
