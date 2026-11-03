import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_directory_search_returns_linda_anderson(
    authenticated_page: Page,
) -> None:
    page = authenticated_page
    page.get_by_role("link", name="Directory", exact=True).click()

    expect(page).to_have_url(
        re.compile(r".*/web/index\.php/directory/viewDirectory$")
    )
    expect(page.get_by_role("heading", name="Directory")).to_be_visible()

    employee_name = page.get_by_placeholder("Type for hints...")
    employee_name.fill("Linda")

    suggestion = page.get_by_role("option", name="Linda Anderson", exact=True)
    expect(suggestion).to_be_visible()
    suggestion.click()

    page.get_by_role("button", name="Search", exact=True).click()

    expect(page.get_by_text("(1) Record Found", exact=True)).to_be_visible()
    expect(page.get_by_text("Linda Anderson", exact=True)).to_have_count(1)
