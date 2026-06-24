import requests

def fetch_page(url):
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"
    except requests.exceptions.RequestException:
        print("Request error")
        return None

    if response.status_code != 200:
        print("Invalid status code")
        return None


    return response.text

