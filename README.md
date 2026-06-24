# Email Extractor Lite

A Python CLI tool that extracts publicly visible email addresses from provided public URLs and their contact pages, then exports the results to a clean CSV file.

This project demonstrates a practical data extraction workflow: reading URLs from a file, fetching public pages, extracting visible emails and `mailto:` links, checking contact/about pages, deduplicating results, and saving structured output.

## Features

* Reads public URLs from a `.txt` file
* Fetches pages with `requests`
* Extracts emails from visible page text
* Extracts emails from `mailto:` links
* Finds contact-related pages such as `/contact`, `/about`, and `/impressum`
* Checks contact pages for additional public emails
* Skips `mailto:` and `tel:` links when searching for contact pages
* Deduplicates emails
* Exports results to CSV
* Handles request errors without crashing
* Uses a simple CLI interface

## Tech Stack

* Python
* requests
* BeautifulSoup
* re
* csv
* argparse
* datetime

## Project Structure

```text
email-extractor-lite/
  src/
    main.py
    fetcher.py
    extractor.py
    scraper.py
    storage.py
    logger_config.py

  data/
    .gitkeep
    urls.txt

  README.md
  requirements.txt
  .gitignore
```

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Add URLs to `data/urls.txt`:

```text
https://example.com
https://example.org/contact
```

Run the tool:

```bash
python src/main.py data/urls.txt data/emails.csv
```

## Input

The input file should be a plain `.txt` file with one URL per line:

```text
https://example.com
https://example.org
https://example.net/contact
```

Empty lines are ignored.

## Output

The tool exports a CSV file with the following columns:

```text
source_url
email
email_type
found_in
checked_at
```

Example output:

```csv
source_url,email,email_type,found_in,checked_at
https://example.com/contact,info@example.com,visible_text,page_text,2026-06-24T14:12:11
```

## Email Types

```text
visible_text
```

The email was found directly in the visible page text.

```text
mailto
```

The email was found inside a `mailto:` link.

## What I Practiced

* Building a CLI tool with `argparse`
* Reading input files
* Fetching public web pages with `requests`
* Parsing HTML with BeautifulSoup
* Extracting emails with regex
* Extracting `mailto:` links
* Finding contact/about/impressum pages
* Building absolute URLs with `urljoin`
* Deduplicating extracted data
* Exporting structured CSV data
* Separating logic into clean modules

## Compliance Note

This tool is intended only for extracting publicly visible business emails from provided public URLs and their contact pages.

It does not guess email addresses, bypass logins, scrape private data, use third-party lead databases, or collect personal contact data from restricted sources.

Use this tool only on websites where automated access is allowed and respect each website’s terms of service and robots.txt.
