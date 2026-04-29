"""utils/notion_codecs.py

Beat codec registry — single source of truth for encoding (push) and decoding (pull)
each beat type to/from Notion blocks.

Adding a new beat type or changing how an existing type renders in Notion:
  1. Subclass BeatCodec, implementing encode/matches/decode_new/apply_edit.
  2. Call BEAT_CODECS.register(YourCodec()) at module level.
  3. Nothing else needs to change.

Changing the serialization format (JSON → TOML, etc.) is orthogonal: the codecs
work with plain Python dicts regardless of how those dicts are read from disk.
"""
from __future__ import annotations

import difflib
import json
import re
from abc import ABC, abstractmethod

_RT_LIMIT = 1900  # Notion hard limit per rich_text span
_NEW_BEAT_TAG = re.compile(r"\s*\[new beat\]\s*", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Block primitives (self-contained — no notion.py dependency)
# ---------------------------------------------------------------------------


def _mk_rt(text: str) -> list[dict]:
    return [{"text": {"content": str(text)[:_RT_LIMIT]}}]


def _mk_callout(text: str, emoji: str) -> dict:
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": _mk_rt(text),
            "icon": {"type": "emoji", "emoji": emoji},
        },
    }


def _block_text(block: dict) -> str:
    """Extract plain text from any Notion block type."""
    btype = block.get("type", "")
    inner = block.get(btype, {})
    rt = inner.get("rich_text", []) if isinstance(inner, dict) else []
    return "".join(s.get("text", {}).get("content", "") for s in rt)


def _cleaned_text(block: dict) -> str:
    """Extract block text and strip any reviewer [new beat] annotation."""
    return _NEW_BEAT_TAG.sub("", _block_text(block)).strip()


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------


class BeatCodec(ABC):
    """
    Single source of truth for one beat type's Notion representation.

    encode() and decode() are co-defined here so they can never drift apart.
    To change how a beat type looks in Notion, edit only this class.
    """

    beat_type: str
    emoji: str | None = None  # set by emoji-keyed codecs; used by legacy pull paths

    @abstractmethod
    def encode(self, beat: dict, **ctx) -> list[dict]:
        """Beat dict → Notion block list (push)."""

    @abstractmethod
    def matches(self, block: dict) -> bool:
        """True if this Notion block was produced by this codec."""

    @abstractmethod
    def decode_new(self, block: dict) -> dict:
        """Unmatched Notion block → new suggested beat (reviewer added it)."""

    @abstractmethod
    def apply_edit(self, beat: dict, block: dict) -> bool:
        """Merge Notion block edits into an existing beat in place.
        Returns True if this is a prompt beat (caller needs that for validator tracking)."""

    def match_score(self, beat: dict, block: dict) -> float | None:
        """Confidence in [0, 1] that `block` corresponds to `beat` (legacy positional matching).
        Return None if this beat cannot match this block."""
        return None

    def encoded_text(self, beat: dict) -> str:
        """Primary display text that encode() would render — used for change detection."""
        blocks = self.encode(beat)
        return _block_text(blocks[0]) if blocks else ""


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


class CodecRegistry:
    def __init__(self) -> None:
        self._codecs: list[BeatCodec] = []
        self._by_type: dict[str, BeatCodec] = {}

    def register(self, codec: BeatCodec) -> None:
        self._codecs.append(codec)
        self._by_type[codec.beat_type] = codec

    def get(self, beat_type: str) -> BeatCodec | None:
        return self._by_type.get(beat_type)

    def identify(self, block: dict) -> BeatCodec | None:
        """Find codec by block structure (full matches() check)."""
        return next((c for c in self._codecs if c.matches(block)), None)

    def find_by_emoji(self, emoji: str) -> BeatCodec | None:
        """Find codec by emoji — shortcut for legacy pull paths that already extracted emoji."""
        return next((c for c in self._codecs if c.emoji == emoji), None)

    @property
    def beat_types(self) -> set[str]:
        return set(self._by_type)

    @property
    def all_codecs(self) -> list[BeatCodec]:
        return list(self._codecs)


BEAT_CODECS = CodecRegistry()


# ---------------------------------------------------------------------------
# Dialogue codec
# ---------------------------------------------------------------------------

_DIALOGUE_MATCH_COVERAGE = 0.6


def _strip_dialogue(text: str) -> str:
    s = text
    if s.startswith('"'):
        s = s[1:]
    s = re.sub(r'"\s*\[[^\]]*\]\s*$', "", s)
    if s.endswith('"'):
        s = s[:-1]
    return s


class DialogueCodec(BeatCodec):
    beat_type = "dialogue"
    emoji = "💬"

    def encode(self, beat: dict, **ctx) -> list[dict]:
        text = beat.get("text", "")
        tags = beat.get("tags", [])
        tag_str = f"  [{', '.join(tags)}]" if tags else ""
        return [_mk_callout(f'"{text}"{tag_str}', self.emoji)]

    def matches(self, block: dict) -> bool:
        if block.get("type") != "callout":
            return False
        icon = block.get("callout", {}).get("icon", {})
        return icon.get("type") == "emoji" and icon.get("emoji") == self.emoji

    def decode_new(self, block: dict) -> dict:
        return {
            "type": "dialogue",
            "text": _strip_dialogue(_cleaned_text(block)),
            "notion_flag": "suggested",
        }

    def apply_edit(self, beat: dict, block: dict) -> bool:
        beat["text"] = _strip_dialogue(_cleaned_text(block))
        return False

    def match_score(self, beat: dict, block: dict) -> float | None:
        if beat.get("type") != "dialogue":
            return None
        notion_words = [
            re.sub(r"[^\w]", "", w)
            for w in _strip_dialogue(_block_text(block)).lower().split()
        ]
        beat_words = [
            re.sub(r"[^\w]", "", w) for w in (beat.get("text") or "").lower().split()
        ]
        notion_words = [w for w in notion_words if w]
        beat_words = [w for w in beat_words if w]
        if not notion_words:
            return None
        sm = difflib.SequenceMatcher(None, notion_words, beat_words)
        matched = sum(b.size for b in sm.get_matching_blocks())
        score = matched / len(notion_words)
        return score if score >= _DIALOGUE_MATCH_COVERAGE else None

    def encoded_text(self, beat: dict) -> str:
        text = beat.get("text", "")
        tags = beat.get("tags", [])
        tag_str = f"  [{', '.join(tags)}]" if tags else ""
        return f'"{text}"{tag_str}'


# ---------------------------------------------------------------------------
# Scene codec
# ---------------------------------------------------------------------------


def _scene_display_text(beat: dict) -> str:
    method = beat.get("method", "").lower()
    tid = beat.get("tangible_id", "")
    params = beat.get("params", {})
    description = params.get("description", "").strip() if params else ""
    if description:
        return description
    if method == "update":
        skip = {"description"}
        changed = {k: v for k, v in (params or {}).items() if k not in skip}
        if changed:
            params_str = ", ".join(f"{k}: {v}" for k, v in changed.items())
            return f"Update {tid} [{params_str}]"
        return f"Update {tid}"
    action_map = {
        "show": f"Show {tid}",
        "hide": f"Hide {tid}",
        "remove": f"Remove {tid}",
        "lock": f"Lock {tid}",
        "unlock": f"Unlock {tid}",
        "animate": f"Animate {tid}",
        "add": f"Add {tid}",
    }
    return action_map.get(method, f"{method.upper()} {tid}")


class SceneCodec(BeatCodec):
    beat_type = "scene"
    emoji = "🎬"

    def encode(self, beat: dict, **ctx) -> list[dict]:
        method = beat.get("method", "").lower()
        tid = beat.get("tangible_id", "")
        params = beat.get("params", {})
        description = params.get("description", "").strip() if params else ""

        if method == "update":
            skip = {"description"}
            changed = {k: v for k, v in (params or {}).items() if k not in skip}
            fields_part = (
                f" [{', '.join(f'{k}: {v}' for k, v in changed.items())}]" if changed else ""
            )
            text = description or (f"Update {tid}{fields_part}" if fields_part else f"Update {tid}")
        else:
            action_map = {
                "show": f"Show {tid}",
                "hide": f"Hide {tid}",
                "remove": f"Remove {tid}",
                "lock": f"Lock {tid}",
                "unlock": f"Unlock {tid}",
                "animate": f"Animate {tid}",
                "add": f"Add {tid}",
            }
            action = action_map.get(method, f"{method.upper()} {tid}")
            text = description or action

        return [_mk_callout(text, self.emoji)]

    def matches(self, block: dict) -> bool:
        if block.get("type") != "callout":
            return False
        icon = block.get("callout", {}).get("icon", {})
        return icon.get("type") == "emoji" and icon.get("emoji") == self.emoji

    def decode_new(self, block: dict) -> dict:
        return {
            "type": "scene",
            "method": "PLACEHOLDER",
            "tangible_id": "PLACEHOLDER",
            "params": {"description": _cleaned_text(block)},
            "notion_flag": "suggested",
        }

    def apply_edit(self, beat: dict, block: dict) -> bool:
        text = _cleaned_text(block)
        if text != _scene_display_text(beat):
            original_desc = (beat.get("params") or {}).get("description", "").strip()
            beat.setdefault("params", {})["description"] = text
            beat["_original_description"] = original_desc
            beat["notion_flag"] = "updated"
        return False

    def match_score(self, beat: dict, block: dict) -> float | None:
        if beat.get("type") != "scene":
            return None
        first_line = _block_text(block).split("\n")[0].strip()
        # Structural key match (beats rendered without a description)
        key = f"{beat.get('method', '')} {beat.get('tangible_id', '')}".strip().lower()
        if key and first_line.lower().startswith(key):
            return 1.0
        # Description-based fuzzy match (beats rendered using description text)
        encoded = self.encoded_text(beat)
        if not encoded:
            return None
        notion_words = [re.sub(r"[^\w]", "", w) for w in first_line.lower().split() if w]
        encoded_words = [re.sub(r"[^\w]", "", w) for w in encoded.lower().split() if w]
        if not notion_words:
            return None
        sm = difflib.SequenceMatcher(None, notion_words, encoded_words)
        matched = sum(b.size for b in sm.get_matching_blocks())
        coverage = matched / len(notion_words)
        return coverage if coverage >= 0.5 else None

    def encoded_text(self, beat: dict) -> str:
        return _scene_display_text(beat)


BEAT_CODECS.register(DialogueCodec())
BEAT_CODECS.register(SceneCodec())


# ---------------------------------------------------------------------------
# Prompt codec
# ---------------------------------------------------------------------------


def _parse_prompt_fields(text: str) -> dict:
    """Parse a ❔ callout text into prompt field updates (tool, target, options, text)."""
    all_lines = text.split("\n")
    first_line = all_lines[0].strip() if all_lines else ""

    kv: dict = {}
    for pair in re.split(r"  +", first_line):
        if ": " in pair:
            k, v = pair.split(": ", 1)
            kv[k.strip()] = v.strip()

    fields: dict = {}
    if "tool" in kv:
        fields["tool"] = kv["tool"]
    if "target" in kv:
        raw = kv["target"]
        if raw.endswith(" (all)"):
            fields["target"] = {"type": raw[:-6].strip()}
        elif ", " in raw:
            fields["target"] = [t.strip() for t in raw.split(", ")]
        else:
            fields["target"] = raw
    if "options" in kv:
        raw_opts = kv["options"].strip()
        try:
            fields["options"] = json.loads(raw_opts)
        except (json.JSONDecodeError, ValueError):
            parsed_opts = []
            for o in raw_opts.split(", "):
                o = o.strip()
                try:
                    parsed_opts.append(int(o))
                except ValueError:
                    try:
                        parsed_opts.append(float(o))
                    except ValueError:
                        parsed_opts.append(o)
            fields["options"] = parsed_opts

    fields["text"] = all_lines[1].strip().strip('"') if len(all_lines) >= 2 else text.strip('"')
    return fields


class PromptCodec(BeatCodec):
    beat_type = "prompt"
    emoji = "❔"

    def encode(self, beat: dict, **ctx) -> list[dict]:
        text = beat.get("text", "")
        tool = beat.get("tool", "")
        target = beat.get("target")
        options = beat.get("options", [])

        parts = [f"tool: {tool}"]
        if target is not None:
            if isinstance(target, list):
                parts.append("target: " + ", ".join(str(t) for t in target))
            elif isinstance(target, dict):
                parts.append(f"target: {target.get('type', '?')} (all)")
            else:
                parts.append(f"target: {target}")
        if options:
            parts.append("options: " + json.dumps(options, ensure_ascii=False))

        callout_lines = ["  ".join(parts), f'"{text}"']
        return [_mk_callout("\n".join(callout_lines), self.emoji)]

    def matches(self, block: dict) -> bool:
        if block.get("type") != "callout":
            return False
        icon = block.get("callout", {}).get("icon", {})
        return icon.get("type") == "emoji" and icon.get("emoji") == self.emoji

    def decode_new(self, block: dict) -> dict:
        text = _cleaned_text(block)
        beat: dict = {"type": "prompt", "notion_flag": "suggested"}
        beat.update(_parse_prompt_fields(text))
        beat.setdefault("tool", "PLACEHOLDER")
        return beat

    def apply_edit(self, beat: dict, block: dict) -> bool:
        text = _cleaned_text(block)
        original_options = list(beat.get("options") or [])
        beat.update(_parse_prompt_fields(text))
        if len(beat.get("options") or []) != len(original_options):
            beat["options"] = original_options
            beat["notion_flag"] = "options_parse_failed"
            beat["_original_options"] = original_options
            first_line = text.split("\n")[0]
            m = re.search(r"options:\s*(.+?)(?:  |$)", first_line)
            beat["_notion_options_text"] = m.group(1).strip() if m else first_line
        return True

    def match_score(self, beat: dict, block: dict) -> float | None:
        if beat.get("type") != "prompt":
            return None
        tool = beat.get("tool", "")
        first_line = _block_text(block).split("\n")[0].strip()
        return 1.0 if (tool and f"tool: {tool}" in first_line) else None

    def encoded_text(self, beat: dict) -> str:
        text = beat.get("text", "")
        tool = beat.get("tool", "")
        target = beat.get("target")
        options = beat.get("options", [])

        parts = [f"tool: {tool}"]
        if target is not None:
            if isinstance(target, list):
                parts.append("target: " + ", ".join(str(t) for t in target))
            elif isinstance(target, dict):
                parts.append(f"target: {target.get('type', '?')} (all)")
            else:
                parts.append(f"target: {target}")
        if options:
            parts.append("options: " + json.dumps(options, ensure_ascii=False))

        callout_lines = ["  ".join(parts), f'"{text}"']
        return "\n".join(callout_lines)


BEAT_CODECS.register(PromptCodec())
