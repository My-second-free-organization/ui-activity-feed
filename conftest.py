import pytest
from playwright.sync_api import Page

@pytest.fixture
def base_url(): return "http://localhost:3000"

@pytest.fixture
def api_url(): return "http://localhost:8080"
