import json
import os


records_file = "records.json"


def load_records():
    if not os.path.exists(records_file):
        return {}
    with open(records_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_records(records):
    with open(records_file, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=4, ensure_ascii=False)
