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
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def push(
    data: Any,
    pipeline_name: str | None = None,
    module_number: int | None = None,
    path_letter: str | None = None,
    unit_number: int | None = None,
    output_file_path: Path | None = None,
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

        from utils.lesson_notion_format import lesson_to_blocks

        page_id = notion_sync.push_to_notion(
            data=data, title=title, file_path=output_file_path, blocks_fn=lesson_to_blocks
        )
        url = notion_sync.get_page_url(page_id)
        print(f"\n  [NOTION] Pushed -> {url}")
        return {"notion_url": url}

    except Exception as exc:
        print(f"\n  [NOTION] Push failed (non-fatal): {exc}")

    return data
