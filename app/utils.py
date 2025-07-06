import json
from typing import List, Dict, Any

REQUIRED_FIELDS = [
    "id", "title", "danceability", "energy", "mode", "acousticness",
    "tempo", "duration_ms", "num_sections", "num_segments"
]

OPTIONAL_FIELDS = ["star_rating"]


def normalize_json(json_path: str) -> List[Dict[str, Any]]:
    with open(json_path, 'r') as f:
        raw_data = json.load(f)

    missing = [field for field in REQUIRED_FIELDS if field not in raw_data]
    if missing:
        raise ValueError(f"Missing required fields in JSON: {missing}")

    num_rows = len(raw_data[REQUIRED_FIELDS[0]])

    records = []
    for i in range(num_rows):
        record = {}
        for field in REQUIRED_FIELDS + OPTIONAL_FIELDS:
            value = raw_data.get(field, {}).get(str(i), None)
            if field in REQUIRED_FIELDS and value is None:
                raise ValueError(f"Missing value for required field '{field}' at row {i}")
            record[field] = parse_value(field, value)
        records.append(record)

    return records


def parse_value(field: str, value: Any) -> Any:
    if field in ["danceability", "energy", "acousticness", "tempo", "star_rating"]:
        try:
            return float(value) if value is not None else None
        except ValueError:
            return None
    elif field in ["mode", "duration_ms", "num_sections", "num_segments"]:
        try:
            return int(float(value)) if value is not None else 0
        except ValueError:
            return 0
    return value
