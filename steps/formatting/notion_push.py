"""Notion Push — formatting step that pushes the current data to Notion.

Add this as the last step in a pipeline config:

    {
        "type": "formatting",
        "function": "notion_push.push",
        "function_args": {
            "pipeline_name": "warmup_generator"
        }
    }

Skips silently if NOTION_API_KEY / NOTION_PARENT_PAGE_ID are not set or if
notion-client is not installed.  Returns data unchanged.

After a successful push the step also pulls Notion block IDs and writes
``_notion_block_id`` back onto each beat in the source data file, enabling
ID-based sync on subsequent pushes.

After a confirmed push the step auto-stitches the current version into
tracked_scripts/ so they stay current without a manual stitch run.

Rate-limit errors are retried up to 3 times (60 / 120 / 180 s backoff)
before the failure is logged as non-fatal.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

_RETRY_DELAYS = [60, 120, 180]

_PIPELINE_NAME_TO_STITCH_TYPE: dict[str, str] = {
    "lesson": "lesson",
    "warmup": "warmup",
    "exit check": "exitcheck",
    "synthesis": "synthesis",
}


def _auto_stitch(unit_number: int | None, module_number: int | None, pipeline_name: str | None) -> None:
    stitch_type = _PIPELINE_NAME_TO_STITCH_TYPE.get((pipeline_name or "").lower())
    if not stitch_type or not module_number:
        return

    project_root = Path(__file__).parent.parent.parent
    stitch_script = project_root / "fixes" / "stitch_pipeline_outputs.py"
    unit_str = f"unit{unit_number or 1}"

    try:
        result = subprocess.run(
            [sys.executable, str(stitch_script), "--unit", unit_str, "--module", str(module_number), "--type", stitch_type],
            capture_output=True,
            text=True,
            cwd=str(project_root),
        )
        if result.returncode == 0:
            print(f"  [STITCH] Auto-stitched {stitch_type} m{module_number} -> tracked_scripts/u{unit_number or 1}/m{module_number}/{stitch_type}")
        else:
            print(f"  [STITCH] Auto-stitch failed (non-fatal):\n{result.stderr.strip()[:300]}")
    except Exception as exc:
        print(f"  [STITCH] Auto-stitch error (non-fatal): {exc}")


def push(
    data: Any,
    pipeline_name: str | None = None,
    module_number: int | None = None,
    path_letter: str | None = None,
    unit_number: int | None = None,
    output_file_path: Path | None = None,
    test_push: bool = False,
    rerun_items: list | None = None,
) -> Any:
    """Push *data* to Notion and return it unchanged.

    Args:
        data: JSON-serialisable data (list or dict) to push.
        pipeline_name: Used to build the Notion page title.
        module_number: Automatically injected by the pipeline runner.
        path_letter: Automatically injected by the pipeline runner.
        unit_number: Automatically injected by the pipeline runner.
        output_file_path: Automatically injected by the pipeline runner.
            Used to derive a stable, version-agnostic registry key so that
            re-runs (v0 → v1) update the same Notion page, while a new
            module always creates a fresh page.
        test_push: If True, always create a new temporary page and never
            update the registry. Useful for reviewing output without
            overwriting the canonical page.
    """
    try:
        from utils.notion import (  # lazy: notion-client may not be installed
            get_notion_client,
            get_page_url,
            is_configured,
            push_lesson,
            tag_notion_ids,
        )

        if not is_configured():
            return data

        title_parts = [pipeline_name or "Pipeline output"]
        if unit_number:
            title_parts.append(f"Unit {unit_number}")
        if module_number:
            title_parts.append(f"Module {module_number}")
        if path_letter:
            title_parts.append(f"Path {path_letter.upper()}")
        title = " — ".join(title_parts)
        if test_push:
            title = f"[TEST] {title}"

        reviewer_user_id = os.getenv("NOTION_REVIEWER_USER_ID")

        if rerun_items:
            print(f"  [NOTION] Rerun mode — pushing only: {rerun_items}")

        # Push with retry on rate limit
        page_id = None
        last_exc = None
        for attempt in range(len(_RETRY_DELAYS) + 1):
            try:
                page_id = push_lesson(
                    data=data,
                    title=title,
                    file_path=None if test_push else output_file_path,
                    reviewer_user_id=reviewer_user_id,
                    sections=rerun_items if rerun_items else None,
                )
                break
            except Exception as exc:
                last_exc = exc
                if "rate limit" in str(exc).lower() and attempt < len(_RETRY_DELAYS):
                    delay = _RETRY_DELAYS[attempt]
                    print(f"\n  [NOTION] Rate limited — retrying in {delay}s (attempt {attempt + 1}/{len(_RETRY_DELAYS)})...")
                    time.sleep(delay)
                else:
                    raise

        url = get_page_url(page_id)
        print(f"\n  [NOTION] Pushed -> {url}")

        # Tag beats with Notion block IDs and write back to the source sections file
        if not test_push and isinstance(data, list) and output_file_path is not None:
            try:
                from utils.pipeline_utils import find_prior_sections_file

                source_file = find_prior_sections_file(Path(output_file_path))
                if source_file is not None:
                    source_content = json.loads(source_file.read_text(encoding="utf-8"))
                    client = get_notion_client()
                    tagged = tag_notion_ids(client, page_id, source_content)
                    source_file.write_text(
                        json.dumps(tagged, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8",
                    )
                    n_sections = sum(1 for s in tagged if isinstance(s, dict) and s.get("_notion_block_id"))
                    n_beats = sum(
                        1
                        for s in tagged
                        if isinstance(s, dict)
                        for b in s.get("beats", [])
                        if b.get("_notion_block_id")
                    )
                    print(f"  [NOTION] Tagged {n_sections} sections + {n_beats} beats -> {source_file.name}")
            except Exception as exc:
                print(f"  [NOTION] Tag-back failed (non-fatal): {exc}")

        push_result = {"notion_url": url}

        # Write push result now so the stitch can include the push step directory.
        # The pipeline runner will write the same content again after we return — that's fine.
        if not test_push and output_file_path is not None:
            try:
                Path(output_file_path).parent.mkdir(parents=True, exist_ok=True)
                Path(output_file_path).write_text(
                    json.dumps(push_result, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
            except Exception:
                pass

        # Auto-stitch into tracked_scripts/
        if not test_push:
            _auto_stitch(unit_number, module_number, pipeline_name)

        return push_result

    except Exception as exc:
        print(f"\n  [NOTION] Push failed (non-fatal): {exc}")

    return data
