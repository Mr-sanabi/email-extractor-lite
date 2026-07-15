from src.storage import save_csv
import csv
records = [
    {
        "source_url": "https://first.example",
        "email": "first@example.com",
        "email_type": "visible_text",
        "found_in": "page_text",
        "checked_at": "2026-07-15T10:00:00",
    },
    {
        "source_url": "https://second.example",
        "email": "second@example.com",
        "email_type": "mailto",
        "found_in": "mailto_href",
        "checked_at": "2026-07-15T10:01:00",
    },
]

def test_writer(tmp_path):
    output_path = tmp_path / "emails.csv"
    save_csv(output_path, records)
    assert output_path.exists()
    with open (output_path, "r",encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    assert len(rows) == 2
    assert "first@example.com" == rows[0]["email"]
    assert "second@example.com" == rows[1]["email"]
    assert rows[1]["email_type"] == "mailto"