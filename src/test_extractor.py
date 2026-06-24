from extractor import extract_emails

with open("data/test_email_page.html", "r", encoding="utf-8") as file:
    html = file.read()

emails = extract_emails(html)

print(f"Emails found: {len(emails)}")

for item in emails:
    print(item)