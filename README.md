# Email Extractor Lite

A Python 3.11+ CLI that finds public email addresses on supplied pages and same-domain contact pages, removes duplicates, and exports CSV.

## Run

Create `data/urls.txt` with one URL per line.

```bash
python -m pip install -r requirements.txt
python -m src.main data/urls.txt data/emails.csv
```

Columns: `source_url`, `email`, `email_type`, `found_in`, `checked_at`. No output file is written when no emails are found.

## Limits

Server-rendered HTML only; no JavaScript execution or decoding of obfuscated addresses. No built-in retries or rate limiting.
Use only pages you are authorized to inspect, and respect site terms, privacy, rate limits, and anti-spam rules.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
