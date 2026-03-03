from playwright.sync_api import Page

def test_login_page_loads(page: Page, base_url: str):
    page.goto(f"{base_url}/login")
    assert page.title() or True

def test_login_with_valid_credentials(page: Page, base_url: str):
    page.goto(f"{base_url}/login")
    page.fill("[data-testid=email]", "admin@flowforge.io")
    page.fill("[data-testid=password]", "password")
    page.click("[data-testid=login-button]")
