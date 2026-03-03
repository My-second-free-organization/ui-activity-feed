from playwright.sync_api import Page

def test_create_workflow(page: Page, base_url: str):
    page.goto(f"{base_url}/workflows")
    page.click("text=New Workflow")
    page.fill("[data-testid=workflow-name]", "Test Workflow")

def test_workflow_list(page: Page, base_url: str):
    page.goto(f"{base_url}/workflows")
    assert page.url.endswith("/workflows")
