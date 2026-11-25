import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_directory_autocomplete_search_returns_one_employee(
    authenticated_page: Page,
) -> None:
    page = authenticated_page
    page.get_by_role("link", name="Directory", exact=True).click()

    expect(page).to_have_url(
        re.compile(r".*/web/index\.php/directory/viewDirectory$")
    )
    expect(page.get_by_role("heading", name="Directory", level=5)).to_be_visible()

    # The shared demo's employees change often, so a hardcoded name breaks.
    # Read a name from the directory as it is right now and search for that.
    first_card_name = page.locator(".orangehrm-directory-card-header").first
    expect(first_card_name).to_be_visible()
    listed_name = " ".join(first_card_name.inner_text().split())
    first_word = listed_name.split(" ")[0]

    employee_name = page.get_by_placeholder("Type for hints...")
    employee_name.fill(first_word)

    suggestion = page.get_by_role("option").filter(
        has_text=re.compile(re.escape(first_word), re.IGNORECASE)
    ).first
    expect(suggestion).to_be_visible(timeout=10000)

    selected_name = " ".join(suggestion.inner_text().split())
    suggestion.click()
    page.get_by_role("button", name="Search", exact=True).click()

    expect(page.get_by_text(re.compile(r"\(1\)\s*Record Found", re.IGNORECASE))).to_be_visible()
    expect(page.get_by_text(selected_name, exact=True)).to_have_count(1)
