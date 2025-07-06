import pytest
import os
from app.utils import normalize_json

VALID_JSON_PATH = os.path.join("data", "sample.json")


def test_normalize_valid_json():
    records = normalize_json(VALID_JSON_PATH)
    assert isinstance(records, list)
    assert len(records) == 100
    assert all("id" in rec and "title" in rec for rec in records)


def test_missing_required_field(tmp_path):
    bad_json = {
        "id": {"0": "abc"},
    }
    file_path = tmp_path / "bad.json"
    file_path.write_text(str(bad_json).replace("'", '"'))

    with pytest.raises(ValueError, match="Missing required fields in JSON"):
        normalize_json(str(file_path))


def test_invalid_type_coercion(tmp_path):
    bad_json = {
        "id": {"0": "abc"},
        "title": {"0": "Song"},
        "danceability": {"0": "not_a_float"},
        "energy": {"0": "0.8"},
        "mode": {"0": "1"},
        "acousticness": {"0": "0.3"},
        "tempo": {"0": "100.0"},
        "duration_ms": {"0": "200000"},
        "num_sections": {"0": "5"},
        "num_segments": {"0": "100"},
    }

    file_path = tmp_path / "bad_type.json"
    file_path.write_text(str(bad_json).replace("'", '"'))

    records = normalize_json(str(file_path))
    assert records[0]["danceability"] is None
