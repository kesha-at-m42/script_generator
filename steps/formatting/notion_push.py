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
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def push(
    data: Any,
    pipeline_name: str | None = None,
    module_number: int | None = None,
    path_letter: str | None = None,
    unit_number: int | None = None,
    output_file_path: Path | None = None,
    test_push: bool = False,
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
        from utils import notion_sync  # lazy: notion-client may not be installed

        if not notion_sync.is_configured():
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

        from utils.lesson_notion_format import lesson_to_blocks

        page_id = notion_sync.push_to_notion(
            data=data,
            title=title,
            # Pass file_path=None on test push so registry is never consulted or updated
            file_path=None if test_push else output_file_path,
            blocks_fn=lambda d: lesson_to_blocks(d, reviewer_user_id=reviewer_user_id),
        )
        url = notion_sync.get_page_url(page_id)
        print(f"\n  [NOTION] Pushed -> {url}")

        # Tag beats with Notion block IDs and write back to the source sections file
        if not test_push and isinstance(data, list) and output_file_path is not None:
            try:
                from utils.pipeline_utils import find_prior_sections_file

                source_file = find_prior_sections_file(Path(output_file_path))
                if source_file is not None:
                    source_content = json.loads(source_file.read_text(encoding="utf-8"))
                    client = notion_sync.get_notion_client()
                    tagged = notion_sync.tag_notion_ids(client, page_id, source_content)
                    source_file.write_text(
                        json.dumps(tagged, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8",
                    )
                    n_beats = sum(
                        1
                        for s in tagged
                        if isinstance(s, dict)
                        for b in s.get("beats", [])
                        if b.get("_notion_block_id")
                    )
                    print(f"  [NOTION] Tagged {n_beats} beats → {source_file.name}")
            except Exception as exc:
                print(f"  [NOTION] Tag-back failed (non-fatal): {exc}")

        return {"notion_url": url}

    except Exception as exc:
        print(f"\n  [NOTION] Push failed (non-fatal): {exc}")

    return data
