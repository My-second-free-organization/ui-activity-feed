import httpx
import pytest

def test_list_workflows(api_url: str):
    r = httpx.get(f"{api_url}/api/v1/workflows", params={"tenantId": "test"})
    assert r.status_code in (200, 401)

def test_health_check(api_url: str):
    r = httpx.get(f"{api_url}/health")
    assert r.status_code == 200
