import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_login_page_displays_expected_controls(page: Page, login_url: str) -> None:
    page.goto(login_url, wait_until="domcontentloaded")

    expect(page).to_have_title(re.compile("OrangeHRM", re.IGNORECASE))
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    expect(page.locator('input[name="password"]')).to_have_attribute("type", "password")
    expect(page.get_by_role("button", name="Login", exact=True)).to_be_visible()

    # These are the public demo credentials printed on the demo login screen.
    expect(page.get_by_text("Username : Admin")).to_be_visible()
    expect(page.get_by_text("Password : admin123")).to_be_visible()


@pytest.mark.smoke
def test_valid_demo_login_opens_dashboard(authenticated_page: Page) -> None:
    expect(authenticated_page).to_have_url(
        re.compile(r".*/web/index\.php/dashboard/index$")
    )
    expect(authenticated_page.get_by_role("heading", name="Dashboard")).to_be_visible()
