from src import fetcher
import requests

def test_fetch_page_returns_none_on_request_error(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.exceptions.RequestException("Connection failed")

    monkeypatch.setattr(fetcher.requests, "get", fake_get)
    result = fetcher.fetch_page("https://example.com")
    assert result is None