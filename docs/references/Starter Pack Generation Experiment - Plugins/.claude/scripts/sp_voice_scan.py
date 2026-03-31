#!/usr/bin/env python3
"""
sp_voice_scan.py — Mechanical voice rule violation checker for Starter Packs.

Authority: Guide Voice Design Reference (01.09.26) + Starter Pack evaluation rules.

Checks:
  VO1:  Red flag word scan (assumed internal states, formal language)
  VO2:  Exclamation count per phase (flag if 0 across module, or >1 per 3 interactions)
  VO3:  Anti-pattern scan (superlative praise, command language, excessive "Let's")
  VO4:  Conciseness check (Guide lines with 4+ sentences before instruction)
  VO5:  Contraction check (formal "let us", "you are", etc. instead of contractions)
  VO6:  Generic praise scan (praise without specifics)
  VO7:  Feeling assumptions (Guide Voice §4.3 — never claim to know student thoughts/feelings)
  VO8:  Identity labels (Guide Voice §1.2, §4.5 — no aspirational identity claims)
  VO9:  "Perfect!" density (Guide Voice §7.1 — max once per phase)
  VO10: "Remember" overuse (Guide Voice §9.4 — limit 2-3 per module)
  VO11: Empty encouragement (Guide Voice §7.2 — "You can do it!" etc. without specificity)
  VO12: Academic language (Guide Voice §7.1, §9.2 — "systematically", "furthermore", etc.)
  VO13: Em dash in dialogue (prohibited — use comma, colon, or period instead)

Gate scoping:
  Gate 1: Skipped (no dialogue)
  Gate 2: Warmup + Lesson dialogue
  Gate 3: All phases
  Gate 4: All phases (same as Gate 3)

Usage:
  python sp_voice_scan.py <sp_file.md> --gate N [--json] [--output PATH]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_parse_interactions import parse_sp, filter_by_gate


# ---------------------------------------------------------------------------
# VO1: Red flag words (assumed internal states, formal language)
# ---------------------------------------------------------------------------

RED_FLAG_WORDS = [
    # Assumed internal states (when used to describe student)
    "carefully", "thoroughly",
    "understanding", "clarity",
    "persistence", "perseverance", "determination",
    # Note: "excited", "proud", "confident", "frustrated" etc. moved to VO7
    # (feeling assumptions) for more precise matching with context
    # Note: "systematically" moved to VO12 (academic language)
    # Formal/academic language (in dialogue context)
    "approach", "method", "technique",
    # Note: "strategy" removed — Guide Voice §5.1 explicitly uses "What strategy
    # did you use?" as valid metacognitive prompt language
]

RED_FLAG_PHRASES = [
    "to be sure", "because you wanted", "in order to", "so that you could",
]


def check_red_flags(dialogue_lines: list) -> list:
    findings = []

    word_patterns = [(w, re.compile(r'\b' + re.escape(w) + r'\b', re.IGNORECASE))
                     for w in RED_FLAG_WORDS]
    phrase_patterns = [(p, re.compile(re.escape(p), re.IGNORECASE))
                       for p in RED_FLAG_PHRASES]

    for dl in dialogue_lines:
        for word, pattern in word_patterns:
            if pattern.search(dl.text):
                findings.append({
                    "check": "VO1",
                    "severity": "MAJOR",
                    "category": "red_flag_word",
                    "matched": word,
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "context": dl.text[:120],
                })
        for phrase, pattern in phrase_patterns:
            if pattern.search(dl.text):
                findings.append({
                    "check": "VO1",
                    "severity": "MAJOR",
                    "category": "red_flag_phrase",
                    "matched": phrase,
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO2: Exclamation density
# ---------------------------------------------------------------------------

def check_exclamation_density(dialogue_lines: list, interactions: list) -> list:
    findings = []

    # Count exclamations per phase
    phase_exclamations = {}
    phase_interactions = {}
    for ix in interactions:
        phase_interactions[ix.phase] = phase_interactions.get(ix.phase, 0) + 1

    for dl in dialogue_lines:
        count = dl.text.count('!')
        if count > 0:
            phase_exclamations[dl.phase] = phase_exclamations.get(dl.phase, 0) + count

    # Check: zero exclamations across entire module
    total_exclamations = sum(phase_exclamations.values())
    if total_exclamations == 0 and len(dialogue_lines) > 0:
        findings.append({
            "check": "VO2",
            "severity": "MINOR",
            "category": "zero_exclamations",
            "detail": "No exclamation marks found in any dialogue — module may feel flat",
            "total_dialogue_lines": len(dialogue_lines),
        })

    # Check: >1 per 3 interactions in any phase
    for phase, ex_count in phase_exclamations.items():
        int_count = phase_interactions.get(phase, 1)
        ratio = ex_count / max(int_count, 1)
        threshold = int_count / 3.0  # 1 per 3 interactions
        if ex_count > max(threshold, 1):
            findings.append({
                "check": "VO2",
                "severity": "MINOR",
                "category": "high_exclamation_density",
                "phase": phase,
                "exclamation_count": ex_count,
                "interaction_count": int_count,
                "ratio": round(ratio, 2),
                "detail": f"{phase}: {ex_count} exclamations across {int_count} interactions "
                         f"(ratio {ratio:.1f}, threshold ~1 per 3 interactions)",
            })

    return findings


# ---------------------------------------------------------------------------
# VO3: Anti-pattern scan
# ---------------------------------------------------------------------------

ANTI_PATTERNS = [
    # Superlative praise (Guide Voice §7.1)
    ("Excellent!", "superlative_praise"),
    ("Amazing!", "superlative_praise"),
    ("Incredible!", "superlative_praise"),
    ("Fantastic!", "superlative_praise"),
    ("Wonderful!", "superlative_praise"),
    # Note: "Perfect!" moved to VO9 (density check, max 1/phase)
    # Note: Identity labels ("mathematician", "so smart") moved to VO8
    # Command language (Guide Voice §7.2)
    ("You have to", "command_language"),
    ("You need to", "command_language"),
    ("You'll need to", "command_language"),
    ("I want you to", "command_language"),
    ("I need you to", "command_language"),
]

RHETORICAL_CAN_RE = re.compile(r'\bCan you\b', re.IGNORECASE)


def check_anti_patterns(dialogue_lines: list, interactions: list) -> list:
    findings = []

    for dl in dialogue_lines:
        for pattern_text, category in ANTI_PATTERNS:
            if pattern_text.lower() in dl.text.lower():
                findings.append({
                    "check": "VO3",
                    "severity": "MAJOR",
                    "category": category,
                    "matched": pattern_text,
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "context": dl.text[:120],
                })

        # Rhetorical "Can you..." in Guide/Prompt (command disguised as question)
        if dl.field_type in ("Guide", "Prompt") and RHETORICAL_CAN_RE.search(dl.text):
            findings.append({
                "check": "VO3",
                "severity": "MINOR",
                "category": "rhetorical_command",
                "matched": "Can you...",
                "interaction_id": dl.interaction_id,
                "field_type": dl.field_type,
                "phase": dl.phase,
                "line_number": dl.line_number,
                "context": dl.text[:120],
            })

    # "Let's" frequency: >1 per 3 interactions per phase
    phase_lets_count = {}
    phase_int_count = {}
    for ix in interactions:
        phase_int_count[ix.phase] = phase_int_count.get(ix.phase, 0) + 1

    for dl in dialogue_lines:
        count = len(re.findall(r"\bLet's\b", dl.text, re.IGNORECASE))
        if count > 0:
            phase_lets_count[dl.phase] = phase_lets_count.get(dl.phase, 0) + count

    for phase, lets_count in phase_lets_count.items():
        int_count = phase_int_count.get(phase, 1)
        threshold = int_count / 3.0
        if lets_count > max(threshold, 1):
            findings.append({
                "check": "VO3",
                "severity": "MINOR",
                "category": "lets_overuse",
                "phase": phase,
                "lets_count": lets_count,
                "interaction_count": int_count,
                "detail": f"{phase}: \"Let's\" used {lets_count} times across {int_count} interactions "
                         f"(threshold ~1 per 3)",
            })

    return findings


# ---------------------------------------------------------------------------
# VO4: Conciseness (Guide lines with 4+ sentences before instruction)
# ---------------------------------------------------------------------------

def check_conciseness(dialogue_lines: list) -> list:
    findings = []

    for dl in dialogue_lines:
        if dl.field_type != "Guide":
            continue

        # Count sentences (rough: split on . ! ? followed by space or end)
        sentences = re.split(r'(?<=[.!?])\s+', dl.text.strip())
        sentences = [s for s in sentences if len(s.strip()) > 3]

        if len(sentences) >= 4:
            findings.append({
                "check": "VO4",
                "severity": "MINOR",
                "category": "verbose_guide",
                "sentence_count": len(sentences),
                "interaction_id": dl.interaction_id,
                "phase": dl.phase,
                "line_number": dl.line_number,
                "detail": f"Guide line has {len(sentences)} sentences (max recommended: 3 before action)",
                "context": dl.text[:120],
            })

    return findings


# ---------------------------------------------------------------------------
# VO5: Contraction check
# ---------------------------------------------------------------------------

FORMAL_CONTRACTIONS = [
    ("let us", "let's"),
    ("you are", "you're"),
    ("do not", "don't"),
    ("it is", "it's"),
    ("that is", "that's"),
    ("we are", "we're"),
    ("they are", "they're"),
    ("does not", "doesn't"),
    ("did not", "didn't"),
    ("cannot", "can't"),
    ("will not", "won't"),
    ("would not", "wouldn't"),
    ("should not", "shouldn't"),
    ("could not", "couldn't"),
    ("is not", "isn't"),
    ("was not", "wasn't"),
    ("were not", "weren't"),
    ("have not", "haven't"),
    ("has not", "hasn't"),
    ("I am", "I'm"),
    ("I have", "I've"),
    ("you have", "you've"),
    ("we have", "we've"),
]


def check_contractions(dialogue_lines: list) -> list:
    findings = []

    for dl in dialogue_lines:
        if dl.field_type != "Guide":
            continue

        for formal, contraction in FORMAL_CONTRACTIONS:
            pattern = re.compile(r'\b' + re.escape(formal) + r'\b', re.IGNORECASE)
            match = pattern.search(dl.text)
            if match:
                # Skip if in ALL CAPS (emphasis)
                matched_text = match.group()
                if matched_text.isupper():
                    continue

                findings.append({
                    "check": "VO5",
                    "severity": "MINOR",
                    "category": "missing_contraction",
                    "matched": matched_text,
                    "suggested": contraction,
                    "interaction_id": dl.interaction_id,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO6: Generic praise
# ---------------------------------------------------------------------------

GENERIC_PRAISE_PATTERNS = [
    re.compile(r'\bGood job\b[.!]?(?!\s+\w)', re.IGNORECASE),
    re.compile(r'\bGreat work\b[.!]?(?!\s+\w)', re.IGNORECASE),
    re.compile(r'\bWell done\b[.!]?(?!\s+\w)', re.IGNORECASE),
    re.compile(r'\bNice\b[.!](?!\s+\w)', re.IGNORECASE),  # "Nice!" alone
    re.compile(r'\bGood\b[.!](?!\s+\w)', re.IGNORECASE),   # "Good!" alone
]


def check_generic_praise(dialogue_lines: list) -> list:
    findings = []

    for dl in dialogue_lines:
        if dl.field_type not in ("On Correct", "Guide"):
            continue

        for pattern in GENERIC_PRAISE_PATTERNS:
            match = pattern.search(dl.text)
            if match:
                findings.append({
                    "check": "VO6",
                    "severity": "MINOR",
                    "category": "generic_praise",
                    "matched": match.group(),
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "detail": f"Generic praise '{match.group()}' — add specific observable acknowledgment",
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO7: Feeling assumptions (Guide Voice §4.3)
# "NEVER claim to know: Thoughts, Feelings, History, Preferences"
# ---------------------------------------------------------------------------

FEELING_ASSUMPTION_PATTERNS = [
    # Thought assumptions
    (re.compile(r"\bYou'?re thinking\b", re.IGNORECASE), "thought assumption"),
    # "You think X" (claim) vs "What do you think?" (question) — only flag claims
    (re.compile(r"(?<!\bdo )\bYou think\b(?!\s+about)(?!.*\?)", re.IGNORECASE), "thought assumption"),
    (re.compile(r"\bYou probably\b", re.IGNORECASE), "thought assumption"),
    (re.compile(r"\bI know you'?re\b", re.IGNORECASE), "thought assumption"),
    (re.compile(r"\bI can tell you\b", re.IGNORECASE), "thought assumption"),
    # Feeling assumptions
    (re.compile(r"\bYou feel\b", re.IGNORECASE), "feeling assumption"),
    (re.compile(r"\bYou'?re feeling\b", re.IGNORECASE), "feeling assumption"),
    (re.compile(r"\bYou must be\s+(?:proud|frustrated|confused|excited|happy|nervous|scared|worried|bored|tired)", re.IGNORECASE), "feeling assumption"),
    (re.compile(r"\bYou'?re (?:proud|frustrated|confused|excited|happy|nervous|eager|thrilled)", re.IGNORECASE), "feeling assumption"),
    (re.compile(r"\bYou'?re excited about\b", re.IGNORECASE), "feeling assumption"),
    # Preference assumptions (without evidence)
    (re.compile(r"\bYou like\b", re.IGNORECASE), "preference assumption"),
    (re.compile(r"\bYou love\b", re.IGNORECASE), "preference assumption"),
    (re.compile(r"\bYou enjoy\b", re.IGNORECASE), "preference assumption"),
    # History assumptions (beyond session)
    (re.compile(r"\bYesterday you\b", re.IGNORECASE), "history assumption"),
    (re.compile(r"\bLast time you\b", re.IGNORECASE), "history assumption"),
]


def check_feeling_assumptions(dialogue_lines: list) -> list:
    """VO7: Scan for language that assumes student thoughts, feelings, or preferences."""
    findings = []

    for dl in dialogue_lines:
        if dl.field_type not in ("Guide", "On Correct", "Remediation"):
            continue

        for pattern, category in FEELING_ASSUMPTION_PATTERNS:
            match = pattern.search(dl.text)
            if match:
                findings.append({
                    "check": "VO7",
                    "severity": "MAJOR",
                    "category": category,
                    "matched": match.group(),
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "detail": f"Feeling/thought assumption: '{match.group()}' — "
                             f"only reference observable actions (Guide Voice §4.3)",
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO8: Identity labels (Guide Voice §1.2, §4.5)
# "No Aspirational Labels: Avoid 'mathematician', 'expert' identity claims"
# ---------------------------------------------------------------------------

IDENTITY_LABEL_PATTERNS = [
    (re.compile(r"\bYou'?re an? (?:mathematician|math expert|expert|genius|star|champion|whiz|pro)\b", re.IGNORECASE), "identity label"),
    (re.compile(r"\bLike an? (?:mathematician|scientist|expert|real)\b", re.IGNORECASE), "identity label"),
    (re.compile(r"\bYou'?re (?:so smart|a natural|brilliant|gifted)\b", re.IGNORECASE), "identity label"),
    (re.compile(r"\bmath (?:wizard|whiz|star|superstar|genius|champion)\b", re.IGNORECASE), "identity label"),
    # The doc explicitly allows behavioral alternatives:
    # "You're developing that skill" is OK
    # "You're a mathematician" is NOT OK
]


def check_identity_labels(dialogue_lines: list) -> list:
    """VO8: Scan for aspirational identity labels (use behavioral praise instead)."""
    findings = []

    for dl in dialogue_lines:
        for pattern, category in IDENTITY_LABEL_PATTERNS:
            match = pattern.search(dl.text)
            if match:
                findings.append({
                    "check": "VO8",
                    "severity": "MAJOR",
                    "category": category,
                    "matched": match.group(),
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "detail": f"Identity label: '{match.group()}' — "
                             f"use behavioral praise instead (Guide Voice §1.2)",
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO9: "Perfect!" density (Guide Voice §7.1)
# "'Perfect!' used more than once per phase" is a red flag
# ---------------------------------------------------------------------------

def check_perfect_density(dialogue_lines: list) -> list:
    """VO9: 'Perfect!' should appear at most once per phase."""
    findings = []

    # Count per phase
    phase_counts = {}
    for dl in dialogue_lines:
        count = len(re.findall(r'\bPerfect\s*[!.]', dl.text, re.IGNORECASE))
        if count > 0:
            phase_counts[dl.phase] = phase_counts.get(dl.phase, 0) + count

    for phase, count in phase_counts.items():
        if count > 1:
            findings.append({
                "check": "VO9",
                "severity": "MINOR",
                "category": "perfect_overuse",
                "phase": phase,
                "count": count,
                "detail": f"{phase}: 'Perfect' used {count} times (max 1 per phase, Guide Voice §7.1)",
            })

    return findings


# ---------------------------------------------------------------------------
# VO10: "Remember" overuse (Guide Voice §9.4)
# "Limit to 2-3 per module"
# ---------------------------------------------------------------------------

def check_remember_density(dialogue_lines: list) -> list:
    """VO10: 'Remember' frequency — limit 2-3 per module."""
    findings = []

    total = 0
    for dl in dialogue_lines:
        total += len(re.findall(r'\bRemember\b', dl.text, re.IGNORECASE))

    if total > 3:
        findings.append({
            "check": "VO10",
            "severity": "MINOR",
            "category": "remember_overuse",
            "count": total,
            "detail": f"'Remember' used {total} times across module (limit 2-3, Guide Voice §9.4)",
        })

    return findings


# ---------------------------------------------------------------------------
# VO11: Empty encouragement (Guide Voice §7.2)
# "You can do it!" / "I believe in you!" / "Give it your best!" without context
# ---------------------------------------------------------------------------

EMPTY_ENCOURAGEMENT_PATTERNS = [
    re.compile(r"\bYou can do (?:it|this)\s*[!.]", re.IGNORECASE),
    re.compile(r"\bI believe in you\s*[!.]", re.IGNORECASE),
    re.compile(r"\bGive it your (?:best|all)\s*[!.]", re.IGNORECASE),
    re.compile(r"\bYou'?ve got this\s*[!.]", re.IGNORECASE),
    re.compile(r"\bI know you can\s", re.IGNORECASE),
    re.compile(r"\bKeep going\s*[!.](?!\s+\w)", re.IGNORECASE),  # "Keep going!" alone
]


def check_empty_encouragement(dialogue_lines: list) -> list:
    """VO11: Encouragement without specificity."""
    findings = []

    for dl in dialogue_lines:
        if dl.field_type not in ("Guide", "On Correct", "Remediation"):
            continue

        for pattern in EMPTY_ENCOURAGEMENT_PATTERNS:
            match = pattern.search(dl.text)
            if match:
                # Check if surrounding text adds specificity (>5 more words after)
                after = dl.text[match.end():].strip()
                if len(after.split()) < 3:
                    findings.append({
                        "check": "VO11",
                        "severity": "MINOR",
                        "category": "empty_encouragement",
                        "matched": match.group(),
                        "interaction_id": dl.interaction_id,
                        "field_type": dl.field_type,
                        "phase": dl.phase,
                        "line_number": dl.line_number,
                        "detail": f"Empty encouragement: '{match.group()}' — "
                                 f"add specific behavioral reference (Guide Voice §7.2)",
                        "context": dl.text[:120],
                    })

    return findings


# ---------------------------------------------------------------------------
# VO12: Academic/unnatural language (Guide Voice §7.1, §9.2)
# "Let's systematically explore" / "furthermore" / performed enthusiasm
# ---------------------------------------------------------------------------

ACADEMIC_LANGUAGE_PATTERNS = [
    (re.compile(r"\bsystematically\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bfurthermore\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bmoreover\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bconsequently\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bnevertheless\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bthus\b", re.IGNORECASE), "academic"),
    (re.compile(r"\btherefore\b", re.IGNORECASE), "academic"),
    (re.compile(r"\bI'm excited to show you\b", re.IGNORECASE), "fake enthusiasm"),
    (re.compile(r"\bI'm so excited\b", re.IGNORECASE), "fake enthusiasm"),
    (re.compile(r"\bHow exciting\b", re.IGNORECASE), "fake enthusiasm"),
    (re.compile(r"\bIsn't that (?:exciting|amazing|incredible|wonderful)\b", re.IGNORECASE), "fake enthusiasm"),
    (re.compile(r"\bBrilliant\b[!.]", re.IGNORECASE), "banned_word"),
]


def check_academic_language(dialogue_lines: list) -> list:
    """VO12: Academic/unnatural language that breaks voice authenticity."""
    findings = []

    for dl in dialogue_lines:
        if dl.field_type not in ("Guide", "Prompt", "On Correct", "Remediation"):
            continue

        for pattern, category in ACADEMIC_LANGUAGE_PATTERNS:
            match = pattern.search(dl.text)
            if match:
                findings.append({
                    "check": "VO12",
                    "severity": "MINOR",
                    "category": category,
                    "matched": match.group(),
                    "interaction_id": dl.interaction_id,
                    "field_type": dl.field_type,
                    "phase": dl.phase,
                    "line_number": dl.line_number,
                    "detail": f"Unnatural language: '{match.group()}' — "
                             f"use conversational phrasing (Guide Voice §7.1)",
                    "context": dl.text[:120],
                })

    return findings


# ---------------------------------------------------------------------------
# VO13: Em dash in dialogue (prohibited punctuation)
# Em dashes (U+2014) are banned from all Guide dialogue. Use comma, colon,
# or period instead. This is a style rule, not a grammar rule.
# ---------------------------------------------------------------------------

EM_DASH = '\u2014'


def check_em_dashes(dialogue_lines: list) -> list:
    """VO13: Flag any em dash (U+2014) in Guide dialogue text."""
    findings = []

    for dl in dialogue_lines:
        if dl.field_type not in ("Guide", "Prompt", "On Correct", "Remediation"):
            continue

        count = dl.text.count(EM_DASH)
        if count > 0:
            # Find position of first em dash for context
            idx = dl.text.find(EM_DASH)
            context_start = max(0, idx - 30)
            context_end = min(len(dl.text), idx + 30)
            context = dl.text[context_start:context_end]

            findings.append({
                "check": "VO13",
                "severity": "MAJOR",
                "category": "em_dash_in_dialogue",
                "matched": EM_DASH,
                "count": count,
                "interaction_id": dl.interaction_id,
                "field_type": dl.field_type,
                "phase": dl.phase,
                "line_number": dl.line_number,
                "detail": f"Em dash in {dl.field_type} text ({count} instance{'s' if count > 1 else ''}) "
                         f"-- use comma, colon, or period instead",
                "context": context,
            })

    return findings


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run_voice_scan(filepath: str, gate: int) -> dict:
    sp = parse_sp(filepath)

    if gate == 1:
        return {
            "checker": "sp_voice_scan",
            "file": filepath,
            "gate": gate,
            "checks_run": [],
            "total_findings": 0,
            "severity_counts": {},
            "check_counts": {},
            "findings": [],
            "meta": {"note": "Gate 1 — no dialogue to scan"},
        }

    sp_filtered = filter_by_gate(sp, gate)
    all_findings = []

    all_findings.extend(check_red_flags(sp_filtered.dialogue_lines))
    all_findings.extend(check_exclamation_density(sp_filtered.dialogue_lines, sp_filtered.interactions))
    all_findings.extend(check_anti_patterns(sp_filtered.dialogue_lines, sp_filtered.interactions))
    all_findings.extend(check_conciseness(sp_filtered.dialogue_lines))
    all_findings.extend(check_contractions(sp_filtered.dialogue_lines))
    all_findings.extend(check_generic_praise(sp_filtered.dialogue_lines))

    # Guide Voice Design Reference checks (VO7–VO13)
    all_findings.extend(check_feeling_assumptions(sp_filtered.dialogue_lines))
    all_findings.extend(check_identity_labels(sp_filtered.dialogue_lines))
    all_findings.extend(check_perfect_density(sp_filtered.dialogue_lines))
    all_findings.extend(check_remember_density(sp_filtered.dialogue_lines))
    all_findings.extend(check_empty_encouragement(sp_filtered.dialogue_lines))
    all_findings.extend(check_academic_language(sp_filtered.dialogue_lines))
    all_findings.extend(check_em_dashes(sp_filtered.dialogue_lines))

    checks_run = sorted(set(f["check"] for f in all_findings)) or [
        "VO1", "VO2", "VO3", "VO4", "VO5", "VO6",
        "VO7", "VO8", "VO9", "VO10", "VO11", "VO12", "VO13",
    ]

    severity_counts = {}
    check_counts = {}
    for f in all_findings:
        sev = f.get("severity", "INFO")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1
        c = f.get("check", "?")
        check_counts[c] = check_counts.get(c, 0) + 1

    return {
        "checker": "sp_voice_scan",
        "file": filepath,
        "gate": gate,
        "checks_run": checks_run,
        "total_findings": len(all_findings),
        "severity_counts": severity_counts,
        "check_counts": check_counts,
        "findings": all_findings,
        "meta": {
            "dialogue_lines_scanned": len(sp_filtered.dialogue_lines),
            "interactions_in_scope": len(sp_filtered.interactions),
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_findings_table(result: dict):
    print(f"\n{'='*80}")
    print(f"VOICE SCAN — {result['file']} — Gate {result['gate']}")
    print(f"{'='*80}")
    print(f"Dialogue lines scanned: {result['meta'].get('dialogue_lines_scanned', '?')}")
    print(f"Total findings: {result['total_findings']}")

    if result['severity_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['severity_counts'].items())]
        print(f"Severity: {', '.join(parts)}")

    if result['check_counts']:
        parts = [f"{k}: {v}" for k, v in sorted(result['check_counts'].items())]
        print(f"By check: {', '.join(parts)}")

    if result['findings']:
        print(f"\n{'─'*80}")
        print("FINDINGS:")
        print(f"{'─'*80}")

        for f in result['findings']:
            check = f.get('check', '?')
            sev = f.get('severity', '?')
            cat = f.get('category', '')
            matched = f.get('matched', '')
            int_id = f.get('interaction_id', '')
            phase = f.get('phase', '')
            loc = f"{phase}/{int_id}" if phase and int_id else phase or ''
            line = f.get('line_number', '')
            line_str = f" L{line}" if line else ""

            detail = f.get('detail', '')
            if not detail and matched:
                detail = f"'{matched}'"
            if f.get('suggested'):
                detail += f" → use '{f['suggested']}'"

            print(f"  [{check:3s}] {sev:8s} | {cat:22s} | {loc:20s} |{line_str} {detail}")

            if 'context' in f:
                ctx = f['context'][:70]
                print(f"           {ctx}...")
    else:
        print("\n  ✓ No findings.")


def main():
    parser = argparse.ArgumentParser(description="SP Voice Rule Scanner")
    parser.add_argument("sp_file", help="Path to the Starter Pack markdown file")
    parser.add_argument("--gate", type=int, required=True, choices=[1, 2, 3, 4])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    result = run_voice_scan(args.sp_file, args.gate)

    if args.json or args.output:
        json_str = json.dumps(result, indent=2)
        if args.output:
            os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
            with open(args.output, 'w') as f:
                f.write(json_str)
            print(f"Output written to {args.output}")
        if args.json:
            print(json_str)
    else:
        print_findings_table(result)


if __name__ == '__main__':
    main()
