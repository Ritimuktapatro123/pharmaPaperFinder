import csv
from typing import List, Dict

def write_csv(data: List[Dict], filename: str) -> None:
    if not data:
        print("No data to write.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            row["Non-academic Author(s)"] = "; ".join(row["Non-academic Author(s)"])
            row["Company Affiliation(s)"] = "; ".join(row["Company Affiliation(s)"])
            writer.writerow(row)
