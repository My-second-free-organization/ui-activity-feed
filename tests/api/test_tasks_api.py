import httpx

def test_get_task(api_url: str):
    r = httpx.get(f"{api_url}/api/v1/tasks/test-id")
    assert r.status_code in (200, 401, 404)
