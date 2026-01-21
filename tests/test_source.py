from src.source import get_status_code


def test_get_status_code():
    code, url = get_status_code("https://httpbin.org/status/200")
    assert code == 200
    assert url.startswith("https://")