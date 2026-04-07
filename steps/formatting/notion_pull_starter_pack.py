"""
notion_pull_starter_pack - Formatting Step

Fetches a Notion starter pack page and converts its blocks to markdown,
writing _starter_pack_ref.md to the module directory.

Two modes:
  1. Direct page URL:  supply `page_url` in function_args.
  2. Database lookup:  supply `database_url` in function_args — the step
     queries the "📖 Level Math Curriculum Documents" database and finds
     the entry matching unit_number + module_number automatically.

Returns the markdown text so the next step (phase_splitter) can auto-chain.

Usage in pipelines.json:
    {
      "name": "notion_pull_starter_pack",
      "type": "formatting",
      "function": "notion_pull_starter_pack.pull",
      "function_args": {
        "database_url": "https://www.notion.so/ocpgg/<database-id>"
      }
    }
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


# ---------------------------------------------------------------------------
# Page ID extraction
# ---------------------------------------------------------------------------


def _page_id_from_url(url_or_id: str) -> str:
    """Extract Notion page ID from a URL or return as-is if already a bare ID."""
    # Full UUID with dashes
    m = re.search(
        r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
        url_or_id,
        re.IGNORECASE,
    )
    if m:
        return m.group(1).replace("-", "")
    # 32-char hex (no dashes) — as it appears at the end of Notion URLs
    m = re.search(r"([0-9a-f]{32})(?:\?|#|$)", url_or_id, re.IGNORECASE)
    if m:
        return m.group(1)
    # Assume it's already a bare ID
    return url_or_id.strip()


# ---------------------------------------------------------------------------
# Rich-text → markdown
# ---------------------------------------------------------------------------


def _rt_to_md(rich_text: list) -> str:
    """Convert a Notion rich_text array to a markdown string."""
    parts = []
    for span in rich_text:
        text = span.get("text", {}).get("content", "")
        if not text:
            continue
        ann = span.get("annotations", {})
        link = span.get("text", {}).get("link")

        # Code annotation wraps everything else
        if ann.get("code"):
            text = f"`{text}`"
        else:
            if ann.get("bold") and ann.get("italic"):
                text = f"***{text}***"
            elif ann.get("bold"):
                text = f"**{text}**"
            elif ann.get("italic"):
                text = f"*{text}*"
            if ann.get("strikethrough"):
                text = f"~~{text}~~"

        if link:
            url = link.get("url", "")
            text = f"[{text}]({url})"

        parts.append(text)
    return "".join(parts)


# ---------------------------------------------------------------------------
# Database lookup
# ---------------------------------------------------------------------------


def _lookup_page_in_database(
    client, database_url: str, unit_number: int, module_number: int
) -> str:
    """Query the curriculum database and return the page URL for the given unit/module.

    Retrieves the database to find its data source ID, then queries via
    data_sources.query (notion_client v3 API).

    Filters by Unit = "Unit {unit_number}" and Module Number = {module_number}.
    Raises ValueError if no matching page is found.
    """
    db_id = _page_id_from_url(database_url)

    # Step 1: resolve the data source ID from the database object
    db_meta = client.databases.retrieve(database_id=db_id)
    data_sources = db_meta.get("data_sources", [])
    if not data_sources:
        raise ValueError(f"No data sources found on database {db_id}")
    ds_id = data_sources[0]["id"].replace("-", "")

    # Step 2: query the data source
    response = client.data_sources.query(
        data_source_id=ds_id,
        filter={
            "and": [
                {
                    "property": "Unit",
                    "select": {"equals": f"Unit {unit_number}"},
                },
                {
                    "property": "Module Number",
                    "number": {"equals": module_number},
                },
            ]
        },
    )
    results = response.get("results", [])
    if not results:
        raise ValueError(
            f"No starter pack page found in database for Unit {unit_number} "
            f"Module {module_number}. Check that Unit and Module Number "
            "properties are set correctly on the Notion page."
        )
    if len(results) > 1:
        print(
            f"  [NOTION_PULL] WARNING: {len(results)} pages found for "
            f"Unit {unit_number} Module {module_number} — using the first result."
        )
    page = results[0]
    page_id = page["id"].replace("-", "")
    return f"https://www.notion.so/{page_id}"


# ---------------------------------------------------------------------------
# Block fetching (with pagination + recursive children)
# ---------------------------------------------------------------------------


def _fetch_all_blocks(client, block_id: str) -> list:
    """Fetch all child blocks (paginated), then recursively fetch their children."""
    results: list = []
    cursor = None
    while True:
        kwargs: dict = {"block_id": block_id}
        if cursor:
            kwargs["start_cursor"] = cursor
        response = client.blocks.children.list(**kwargs)
        results.extend(response["results"])
        if not response["has_more"]:
            break
        cursor = response["next_cursor"]

    for block in results:
        if block.get("has_children"):
            btype = block.get("type", "")
            block.setdefault(btype, {})
            block[btype]["children"] = _fetch_all_blocks(client, block["id"])

    return results


# ---------------------------------------------------------------------------
# Table block → markdown
# ---------------------------------------------------------------------------


def _table_to_md(bdata: dict) -> str:
    """Convert a Notion table block (with children already fetched) to markdown."""
    has_col_header = bdata.get("has_column_header", False)
    rows = bdata.get("children", [])
    if not rows:
        return ""

    md_rows = []
    for row_block in rows:
        cells = row_block.get("table_row", {}).get("cells", [])
        md_rows.append([_rt_to_md(cell) for cell in cells])

    if not md_rows:
        return ""

    ncols = max(len(r) for r in md_rows)
    md_rows = [r + [""] * (ncols - len(r)) for r in md_rows]

    lines = []
    if has_col_header:
        lines.append("| " + " | ".join(md_rows[0]) + " |")
        lines.append("| " + " | ".join(["---"] * ncols) + " |")
        for row in md_rows[1:]:
            lines.append("| " + " | ".join(row) + " |")
    else:
        for row in md_rows:
            lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Blocks → markdown
# ---------------------------------------------------------------------------


def _blocks_to_md(blocks: list, depth: int = 0) -> list[str]:
    """
    Recursively convert a list of Notion blocks to markdown lines.

    Returns a list of strings (one per logical line/paragraph).
    Caller joins them with newlines.
    """
    indent = "  " * depth
    lines: list[str] = []

    for block in blocks:
        btype = block.get("type", "")
        bdata = block.get(btype, {})
        rt = bdata.get("rich_text", [])
        text = _rt_to_md(rt)
        children = bdata.get("children", [])

        if btype == "heading_1":
            lines.append(f"# {text}")
            lines.append("")
        elif btype == "heading_2":
            lines.append(f"## {text}")
            lines.append("")
        elif btype == "heading_3":
            lines.append(f"### {text}")
            lines.append("")
        elif btype == "paragraph":
            lines.append(indent + text if text.strip() else "")
            lines.append("")
        elif btype == "bulleted_list_item":
            lines.append(f"{indent}* {text}")
            if children:
                lines.extend(_blocks_to_md(children, depth + 1))
        elif btype == "numbered_list_item":
            lines.append(f"{indent}1. {text}")
            if children:
                lines.extend(_blocks_to_md(children, depth + 1))
        elif btype == "code":
            language = bdata.get("language", "")
            lines.append(f"```{language}")
            lines.append(text)
            lines.append("```")
            lines.append("")
        elif btype == "divider":
            lines.append("---")
            lines.append("")
        elif btype == "quote":
            for ln in text.split("\n"):
                lines.append(f"> {ln}")
            lines.append("")
        elif btype == "callout":
            icon = bdata.get("icon", {})
            emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            prefix = f"{emoji} " if emoji else ""
            lines.append(f"> **{prefix}{text}**")
            lines.append("")
        elif btype == "toggle":
            # Expand as a bold label + indented children
            if text.strip():
                lines.append(f"**{text}**")
                lines.append("")
            if children:
                lines.extend(_blocks_to_md(children, depth))
        elif btype == "table":
            md_table = _table_to_md(bdata)
            if md_table:
                lines.append(md_table)
                lines.append("")
        elif btype == "column_list":
            # Flatten multi-column layouts
            for col_block in children:
                col_children = col_block.get("column", {}).get("children", [])
                if col_children:
                    lines.extend(_blocks_to_md(col_children, depth))
        elif btype == "image":
            caption = _rt_to_md(bdata.get("caption", []))
            url = (
                bdata.get("external", {}).get("url")
                or bdata.get("file", {}).get("url", "")
            )
            lines.append(f"![{caption}]({url})" if url else "")
            lines.append("")
        # child_page, child_database, embed, link_preview, etc. are silently skipped

    return lines


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def pull(
    input_data,
    page_url: str = None,
    database_url: str = None,
    unit_number: int = None,
    module_number: int = None,
    output_file_path: Path = None,
    verbose: bool = False,
    **kwargs,
) -> str:
    """
    Fetch a Notion starter pack page and convert it to markdown.

    Writes _starter_pack_ref.md to the module directory as a side effect.
    Returns the markdown text (auto-chains into phase_splitter).

    Args:
        input_data: Ignored — Notion is the source, no prior step needed.
        page_url: Notion page URL or bare page ID (direct mode).
        database_url: URL of the curriculum database — the step will query it
                      for the entry matching unit_number + module_number (lookup mode).
        unit_number: Unit number (required for database lookup; also used to
                     locate the module directory).
        module_number: Module number (required for database lookup; also used
                       to locate the module directory).
        output_file_path: Pipeline step output path (passed automatically).
        verbose: Enable verbose logging.
    """
    if not page_url and not database_url:
        raise ValueError(
            "notion_pull_starter_pack requires either 'page_url' or 'database_url' in function_args"
        )

    # Load .env if not already loaded
    try:
        from dotenv import load_dotenv
        load_dotenv(project_root / ".env")
    except ImportError:
        pass

    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        raise ValueError("NOTION_API_KEY is not set in your .env file.")

    from notion_client import Client

    client = Client(auth=api_key)

    # Resolve page URL via database lookup if needed
    if not page_url:
        if unit_number is None or module_number is None:
            raise ValueError(
                "database_url mode requires unit_number and module_number"
            )
        if verbose:
            print(
                f"  [NOTION_PULL] Looking up Unit {unit_number} Module {module_number} "
                "in database ..."
            )
        page_url = _lookup_page_in_database(
            client, database_url, unit_number, module_number
        )
        print(f"  [NOTION_PULL] Found page: {page_url}")

    page_id = _page_id_from_url(page_url)

    if verbose:
        print(f"  [NOTION_PULL] Fetching page {page_id} ...")

    # ---- Page title --------------------------------------------------------
    page_meta = client.pages.retrieve(page_id)
    title_rt = (
        page_meta.get("properties", {}).get("title", {}).get("title", [])
    )
    title = "".join(span.get("plain_text", "") for span in title_rt)

    if verbose:
        print(f"  [NOTION_PULL] Title: {title}")

    # ---- Blocks ------------------------------------------------------------
    blocks = _fetch_all_blocks(client, page_id)

    if verbose:
        print(f"  [NOTION_PULL] Fetched {len(blocks)} top-level blocks")

    # ---- Convert to markdown -----------------------------------------------
    md_lines: list[str] = []
    if title:
        md_lines.append(f"# **{title}**")
        md_lines.append("")

    md_lines.extend(_blocks_to_md(blocks))

    # Collapse excessive blank lines (3+ → 2)
    markdown = re.sub(r"\n{3,}", "\n\n", "\n".join(md_lines)).strip() + "\n"

    # ---- Write _starter_pack_ref.md to module dir --------------------------
    if unit_number is not None and module_number is not None:
        module_dir = (
            project_root / "units" / f"unit{unit_number}" / f"module{module_number}"
        )
        if module_dir.exists():
            out_path = module_dir / "_starter_pack_ref.md"
            out_path.write_text(markdown, encoding="utf-8")
            print(f"  [NOTION_PULL] Written: {out_path.relative_to(project_root)}")
        else:
            print(f"  [NOTION_PULL] WARNING: module dir not found: {module_dir}")
    else:
        print("  [NOTION_PULL] No unit/module number — skipping _starter_pack_ref.md write")

    return markdown
