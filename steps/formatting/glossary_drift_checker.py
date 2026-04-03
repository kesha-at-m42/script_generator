"""
glossary_drift_checker - Formatting Step

Pass-through step that scans the enriched spec for terminology not yet in the
canonical glossary. Writes drift_report.md alongside the step's output file,
then returns input data unchanged so the pipeline chain continues unmodified.

The drift report is a discovery document. It surfaces:
  - Visual phrases toy_spec_loader couldn't resolve to any spec file
  - workspace_specs toy/tool values not in the canonical glossary lists
  - Raw spec text using deprecated spec aliases (renamed or superseded terms)

This step does not block or modify generation.
"""

import sys
from datetime import datetime
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


def _load_glossary(unit_number, module_number):
    sys.path.insert(0, str(project_root / "core"))
    from path_manager import resolve_doc_path

    path = resolve_doc_path("glossary.md", unit_number=unit_number, module_number=module_number)
    if not path or not path.exists():
        return None

    sys.path.insert(0, str(project_root / "utils"))
    from glossary_parser import parse_glossary

    return parse_glossary(path)


_SCAN_FIELDS = ("visual", "guide", "prompt", "on_correct", "on_incorrect", "task", "hook")


def _find_snippet(text: str, term: str, context: int = 80) -> str:
    idx = text.lower().find(term.lower())
    if idx == -1:
        return text[:context].strip()
    start = max(0, idx - 20)
    end = min(len(text), idx + len(term) + context)
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."
    return snippet


def _scan_section(section: dict, glossary) -> list:
    findings = []
    ws = section.get("workspace_specs") or {}

    # 1. Phrases toy_spec_loader couldn't resolve
    for phrase in ws.get("unresolved", []):
        findings.append({
            "kind": "unresolved_phrase",
            "term": phrase,
            "field": "visual",
            "snippet": _find_snippet(section.get("visual", ""), phrase),
        })

    # 2. Resolved toy types not in canonical glossary list
    for toy in ws.get("toys", []):
        if toy and toy not in glossary.canonical_toys:
            findings.append({
                "kind": "toy_not_in_glossary",
                "term": toy,
                "field": "workspace_specs.toys",
                "snippet": None,
            })

    # 3. Inferred tool values not in canonical glossary list
    for tool in ws.get("tools", []):
        if tool and tool not in glossary.canonical_tools:
            findings.append({
                "kind": "tool_not_in_glossary",
                "term": tool,
                "field": "workspace_specs.tools",
                "snippet": None,
            })

    # 4. Tool inferred by fallback — no rule matched, defaulted to multiple_choice
    if ws.get("tool_inferred_by_fallback"):
        findings.append({
            "kind": "tool_fallback",
            "term": ", ".join(ws.get("tools", ["multiple_choice"])),
            "field": "workspace_specs.tools",
            "snippet": (section.get("task") or section.get("prompt") or "")[:80],
        })

    # 5. Deprecated spec aliases appearing in raw spec text fields
    for field in _SCAN_FIELDS:
        text = section.get(field) or ""
        if not text:
            continue
        text_lower = text.lower()
        for alias in glossary.spec_aliases:
            if alias in text_lower:
                findings.append({
                    "kind": "deprecated_alias_used",
                    "term": alias,
                    "resolves_to": glossary.spec_aliases[alias],
                    "field": field,
                    "snippet": _find_snippet(text, alias),
                })

    return findings


def _build_report(all_findings, unit_number, module_number, input_file, generated_at) -> str:
    by_kind = {
        "unresolved_phrase": [],
        "toy_not_in_glossary": [],
        "tool_not_in_glossary": [],
        "tool_fallback": [],
        "deprecated_alias_used": [],
    }
    for f in all_findings:
        by_kind[f["kind"]].append(f)

    unit_str = f"Unit {unit_number}" if unit_number else "—"
    module_str = f"Module {module_number}" if module_number else "—"

    lines = [
        "# UX/Script Terminology Drift Report",
        "",
        f"Generated: {generated_at}  ",
        f"Source: `{input_file}`  ",
        f"Scope: {unit_str}, {module_str}",
        "",
        "Discovery document — surfaces spec terminology that needs a glossary decision.",
        "This does not block generation.",
        "",
    ]

    def section_block(heading, description, findings, columns, row_fn):
        lines.append("---")
        lines.append("")
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(description)
        lines.append("")
        if findings:
            lines.append(f"| {' | '.join(columns)} |")
            lines.append(f"| {'|'.join(['---'] * len(columns))} |")
            for f in findings:
                lines.append(row_fn(f))
        else:
            lines.append(f"_None found._")
        lines.append("")

    section_block(
        "Unresolved Visual Phrases",
        "Phrases in `visual` fields that `toy_spec_loader` couldn't match to any spec file.\n"
        "These likely represent concepts not yet in the glossary or toy_specs directory.",
        by_kind["unresolved_phrase"],
        ["Phrase", "Section", "Snippet"],
        lambda f: (
            f"| `{f['term']}` | `{f['section_id']}` "
            f"| {(f['snippet'] or '').replace('|', '/').replace(chr(10), ' ')[:80]} |"
        ),
    )

    section_block(
        "Toys Resolved but Not in Glossary",
        "`toy_spec_loader` matched these to a spec file, but they have no canonical entry\n"
        "in the glossary's Canonical Toys table. They may need a new glossary entry.",
        by_kind["toy_not_in_glossary"],
        ["Toy type", "Section"],
        lambda f: f"| `{f['term']}` | `{f['section_id']}` |",
    )

    section_block(
        "Tools Inferred but Not in Glossary",
        "These `tool` values were inferred but have no canonical entry in the glossary.\n"
        "They may need a new glossary entry.",
        by_kind["tool_not_in_glossary"],
        ["Tool", "Section"],
        lambda f: f"| `{f['term']}` | `{f['section_id']}` |",
    )

    section_block(
        "Deprecated Spec Aliases Used",
        "These terms appeared in raw spec text and match a renamed or superseded alias.\n"
        "The spec writer used an older name — the canonical replacement is shown.",
        by_kind["deprecated_alias_used"],
        ["Spec term", "Canonical name", "Field", "Section", "Snippet"],
        lambda f: (
            f"| `{f['term']}` | `{f['resolves_to']}` | `{f['field']}` "
            f"| `{f['section_id']}` "
            f"| {(f['snippet'] or '').replace('|', '/').replace(chr(10), ' ')[:60]} |"
        ),
    )

    section_block(
        "Tool Inferred by Fallback",
        "No inference rule matched — `toy_spec_loader` defaulted to `multiple_choice`.\n"
        "Review these sections: the correct tool may be something else.",
        by_kind["tool_fallback"],
        ["Assigned tool", "Section", "Snippet"],
        lambda f: (
            f"| `{f['term']}` | `{f['section_id']}` "
            f"| {(f['snippet'] or '').replace('|', '/').replace(chr(10), ' ')[:80]} |"
        ),
    )

    # Section detail
    sections_with_findings = {}
    for f in all_findings:
        sections_with_findings.setdefault(f["section_id"], []).append(f)

    if sections_with_findings:
        lines += ["---", "", "## Section Detail", ""]
        for sid, findings in sorted(sections_with_findings.items()):
            lines.append(f"### `{sid}`")
            lines.append("")
            for f in findings:
                kind = f["kind"]
                term = f["term"]
                snippet = f.get("snippet") or ""

                if kind == "unresolved_phrase":
                    lines.append(f"- **Unresolved:** `{term}` in `{f['field']}`")
                elif kind == "toy_not_in_glossary":
                    lines.append(f"- **Toy not in glossary:** `{term}`")
                elif kind == "tool_not_in_glossary":
                    lines.append(f"- **Tool not in glossary:** `{term}`")
                elif kind == "tool_fallback":
                    lines.append(f"- **Tool fallback:** defaulted to `{term}` — no rule matched")
                elif kind == "deprecated_alias_used":
                    lines.append(
                        f"- **Deprecated alias:** `{term}` → `{f['resolves_to']}` "
                        f"(in `{f['field']}`)"
                    )

                if snippet:
                    lines.append(f"  > {snippet}")
            lines.append("")

    return "\n".join(lines)


def check_glossary_drift(
    input_data,
    unit_number: int = None,
    module_number: int = None,
    output_file_path: Path = None,
    verbose: bool = False,
    **kwargs,
):
    """
    Scan enriched_spec sections for terminology drift. Writes drift_report.md
    to the step's output directory as a side effect. Returns input_data unchanged.

    Args:
        input_data: Parsed enriched_spec.json (list of section dicts)
        unit_number: Unit number for locating glossary.md
        module_number: Module number for locating glossary.md
        output_file_path: Path where this step's output is saved (locates report dir)
        verbose: Enable verbose logging
    """
    glossary = _load_glossary(unit_number=unit_number, module_number=module_number)
    if not glossary:
        if verbose:
            print("  [DRIFT] glossary.md not found — skipping drift check")
        return input_data

    sections = input_data if isinstance(input_data, list) else input_data.get("sections", [])

    all_findings = []
    for section in sections:
        sid = section.get("id", "unknown")
        findings = _scan_section(section, glossary)
        for f in findings:
            f["section_id"] = sid
        all_findings.extend(findings)

    report_dir = output_file_path.parent if output_file_path else Path(".")
    report_path = report_dir / "drift_report.md"

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    input_file = output_file_path.name if output_file_path else "enriched_spec.json"

    report = _build_report(
        all_findings,
        unit_number=unit_number,
        module_number=module_number,
        input_file=input_file,
        generated_at=generated_at,
    )
    report_path.write_text(report, encoding="utf-8")

    if verbose or all_findings:
        counts = {k: sum(1 for f in all_findings if f["kind"] == k) for k in (
            "unresolved_phrase", "toy_not_in_glossary",
            "tool_not_in_glossary", "tool_fallback", "deprecated_alias_used",
        )}
        print(
            f"  [DRIFT] Report → {report_path}  |  "
            f"unresolved={counts['unresolved_phrase']}  "
            f"missing={counts['toy_not_in_glossary'] + counts['tool_not_in_glossary']}  "
            f"fallback={counts['tool_fallback']}  "
            f"deprecated={counts['deprecated_alias_used']}"
        )

    return input_data
