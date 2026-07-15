from src import scraper

urls = [
    "https://first.example",
    "https://second.example",
]


first_html = """
<html>
    <body>
        <h1>First company</h1>
        <p>Contact us at first@example.com</p>
    </body>
</html>
"""

second_html = """
<html>
    <body>
        <h1>Second company</h1>
        <p>Contact us at second@example.com</p>
    </body>
</html>
"""

def fake_fetch_page(url):
    if url == "https://first.example":
        return first_html
    
    if url == "https://second.example":
        return second_html
    
    


def test_fake(monkeypatch):
    monkeypatch.setattr(scraper, "fetch_page", fake_fetch_page)
    emails = []
    result = scraper.scrape_emails(urls)
    for record in result:
        emails.append(record["email"])
    assert "first@example.com" in emails
    assert "second@example.com" in emails
    assert len(result) == 2