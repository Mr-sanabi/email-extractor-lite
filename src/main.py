import argparse
from src.scraper import scrape_emails
from src.storage import save_csv

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    return parser.parse_args()

def load_urls(input_file):
    rows = []
    
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            urls = file.readlines()

        for url in urls:
            clean_url = url.strip()

            if clean_url == "":
                continue

            rows.append(clean_url)
        
        return rows

    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return []
    
def main():
    args = parse_args()

    urls = load_urls(args.input_file)

    if not urls:
        return

    rows = scrape_emails(urls)

    if not rows:
        print("No emails found. CSV file was not created")
        return
    
    print(f"Total emails found: {len(rows)}")

    save_csv(args.output_file, rows)
    print(f"Saved {len(rows)} rows to {args.output_file}")

if __name__ == "__main__":
    main()

