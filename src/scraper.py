
from fetcher import fetch_page
from extractor import extract_emails, extract_contact_links
from datetime import datetime

def scrape_emails(urls):
    all_rows = []
    seen_email = set()

    for url in urls:
        print(f"Fetching: {url}")
        html = fetch_page(url)

        if html is None:
            continue

        checked_at = datetime.now().isoformat(timespec="seconds")

        emails = extract_emails(html)

        for item in emails:
            email = item["email"]
            if email not in seen_email:
                seen_email.add(email)

                row = {
                    "source_url": url,
                    "email": item["email"],
                    "email_type": item["email_type"],
                    "found_in": item["found_in"],
                    "checked_at": checked_at
                }
            
                all_rows.append(row)

        contact_links = extract_contact_links(html, url)

        for contact_link in contact_links:
            print(f"Checking contact page: {contact_link}")

            contact_html = fetch_page(contact_link)

            if contact_html is None:
                continue

            contact_emails = extract_emails(contact_html)

            contact_checked_at = datetime.now().isoformat(timespec="seconds")

            for item in contact_emails:
                email = item["email"]
                if email not in seen_email:
                    seen_email.add(email)

                    row = {
                        "source_url": contact_link,
                        "email": item["email"],
                        "email_type": item["email_type"],
                        "found_in": item["found_in"],
                        "checked_at": contact_checked_at
                    }                    
                
                    all_rows.append(row)

        return all_rows