import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_dashboard_displays_primary_navigation_and_widgets(
    authenticated_page: Page,
) -> None:
    page = authenticated_page

    for item in (
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory",
        "Maintenance",
    ):
        expect(page.get_by_role("link", name=item, exact=True)).to_be_visible()

    for widget in (
        "Time at Work",
        "My Actions",
        "Quick Launch",
        "Employees on Leave Today",
        "Employee Distribution by Sub Unit",
        "Employee Distribution by Location",
    ):
        expect(page.get_by_text(widget, exact=True)).to_be_visible()
