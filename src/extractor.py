import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_emails(html):
    results = []
    seen_email = set()

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(" ")

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)

    for email in emails:
        email = email.lower()
        if email not in seen_email:
            seen_email.add(email)
            results.append({
                "email": email,
                "email_type": "visible_text",
                "found_in": "page_text"
            })
    
    links = soup.select("a[href]")

    for link in links:
        href = link.get("href")
        if href.startswith("mailto:"):
            email = href.replace("mailto:", "")
            email = email.split("?")[0]
            email = email.strip().lower()

            if email not in seen_email:
                seen_email.add(email)

                results.append({
                    "email": email,
                    "email_type": "mailto",
                    "found_in": "mailto_href"})                
    
    return results


def extract_contact_links(html, base_url):
    results = []
    seen_links = set()

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a[href]")

    keywords = ["contact", "contact-us", "contacts", "about", "impressum"]

    parsed = urlparse(base_url).netloc
    for link in links:
        href = link.get("href", "")
        link_text = link.get_text(" ", strip=True)

        if href.startswith("mailto:"):
            continue

        if href.startswith("tel:"):
            continue

        href_lower = href.lower()
        text_lower = link_text.lower()

        is_contact_link = False

        for keyword in keywords:
            if keyword in href_lower or keyword in text_lower:
                is_contact_link = True
                break

        if is_contact_link:
            full_url = urljoin(base_url, href)
            full_parsed = urlparse(full_url).netloc

            if full_parsed == parsed and full_url not in seen_links:
                seen_links.add(full_url)
                results.append(full_url)


    return results