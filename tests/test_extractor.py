from src.extractor import extract_contact_links, extract_emails

html = """
<html>
    <body>
        <h1>Contact information</h1>

        <p>Write to Sales@Example.com</p>
        <p>Duplicate address: sales@example.com</p>

        <a href="mailto:Support@Example.com?subject=Question">
            Contact support
        </a>
    </body>
</html>
"""

def test_extract_contact_links_keeps_same_domain_only():
    contact_html = """
        <html>
            <body>
                <a href="/contact">Contact</a>
                <a href="/contact">Contact duplicate</a>
                <a href="https://example.com/about">About us</a>

                <a href="https://external.example/contact">
                    External contact
                </a>

                <a href="mailto:team@example.com">
                    Email
                </a>
            </body>
        </html>
        """
    result = extract_contact_links(contact_html, base_url = "https://example.com/products")
    assert "https://example.com/contact" and "https://example.com/about" in result


def test_extract():
    emails = []
    result = extract_emails(html)
    for record in result:
        emails.append(record["email"])
        if record["email"] == "sales@example.com":
            assert record["email_type"] == "visible_text"
            assert record["found_in"] == "page_text"
        
        if record["email"] == "support@example.com":
            assert record["email_type"] == "mailto"
            assert record["found_in"] == "mailto_href"
    
    assert "sales@example.com" in emails
    assert "support@example.com" in emails
    assert len(result) == 2