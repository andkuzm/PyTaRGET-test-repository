from src.source import get_status_code


def test_get_status_code():
    # outdated expectation: assumes redirect
    code = get_status_code("https://httpbin.org/status/200")
    assert code == 302