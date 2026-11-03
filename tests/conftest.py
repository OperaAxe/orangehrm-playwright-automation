import os
import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = os.getenv(
    "ORANGEHRM_BASE_URL",
    "https://opensource-demo.orangehrmlive.com",
).rstrip("/")
USERNAME = os.getenv("ORANGEHRM_USERNAME", "Admin")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "admin123")


@pytest.fixture
def login_url() -> str:
    return f"{BASE_URL}/web/index.php/auth/login"


@pytest.fixture
def authenticated_page(page: Page, login_url: str) -> Page:
    """Sign in using the credentials displayed by the public demo."""
    page.goto(login_url, wait_until="domcontentloaded")
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login", exact=True).click()
    expect(page).to_have_url(re.compile(r".*/web/index\.php/dashboard/index$"))
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    return page
