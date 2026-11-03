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

    employee_name = page.get_by_placeholder("Type for hints...")
    employee_name.fill("manda")

    # The shared demo's seeded employees can change. Choose a current matching
    # autocomplete result rather than depending on a fixed employee record.
    suggestion = page.get_by_role("option").filter(
        has_text=re.compile(r"manda", re.IGNORECASE)
    ).first
    expect(suggestion).to_be_visible()

    selected_name = suggestion.inner_text().strip()
    suggestion.click()
    page.get_by_role("button", name="Search", exact=True).click()

    expect(page.get_by_text(re.compile(r"\(1\)\s*Record Found", re.IGNORECASE))).to_be_visible()
    expect(page.get_by_text(selected_name, exact=True)).to_have_count(1)
