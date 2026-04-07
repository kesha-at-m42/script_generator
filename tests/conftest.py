import os
import pytest
from dotenv import load_dotenv
load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--keep-sandbox",
        action="store_true",
        default=False,
        help="Don't archive sandbox pages after tests — leave them open in Notion for inspection.",
    )
    parser.addoption(
        "--pause",
        action="store_true",
        default=False,
        help="Pause after each push so you can inspect/edit the page in Notion before continuing.",
    )


@pytest.fixture
def sandbox_page(request):
    """Create a blank child page under NOTION_PARENT_PAGE_ID, yield its ID, archive on teardown
    (unless --keep-sandbox is set)."""
    from utils.notion_sync import get_notion_client, get_page_url
    client = get_notion_client()
    parent_id = os.environ["NOTION_PARENT_PAGE_ID"]
    test_name = request.node.name
    page = client.pages.create(
        parent={"page_id": parent_id},
        properties={"title": {"title": [{"text": {"content": f"[TEST] {test_name}"}}]}},
    )
    page_id = page["id"]
    print(f"\n  sandbox: {get_page_url(page_id)}")
    yield page_id
    if request.config.getoption("--keep-sandbox"):
        print(f"  [kept]   {get_page_url(page_id)}")
    else:
        client.pages.update(page_id, archived=True)
