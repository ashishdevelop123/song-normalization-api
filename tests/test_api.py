from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_songs_default():
    response = client.get("/songs?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) <= 5
    assert "next_cursor" in data
    assert "has_more" in data


def test_get_all_songs_with_cursor_pagination():
    first_page = client.get("/songs?limit=3")
    assert first_page.status_code == 200
    data = first_page.json()
    assert "items" in data and len(data["items"]) == 3
    next_cursor = data["next_cursor"]

    second_page = client.get(f"/songs?cursor={next_cursor}&limit=3")
    assert second_page.status_code == 200
    next_data = second_page.json()
    assert "items" in next_data


def test_get_all_songs_invalid_params():
    response = client.get("/songs?cursor=-1&limit=5")
    assert response.status_code == 400
    assert "Invalid cursor" in response.text


def test_get_song_by_title_exists():
    response = client.get("/songs/by_title?title=21 Guns")
    assert response.status_code == 200
    assert response.json()["title"].lower() == "21 guns"


def test_get_song_by_title_not_found():
    response = client.get("/songs/by_title?title=non_existent_title")
    assert response.status_code == 404
    assert "No song found" in response.text


def test_rate_song_success():
    song_id = "2jiI8bNSDu7UxTtDCOqh3L"  # exists in playlist
    response = client.post(f"/songs/{song_id}/rate?rating=4.5")
    assert response.status_code == 200
    song = response.json()
    assert song["id"] == song_id
    assert song["star_rating"] == 4.5


def test_rate_song_invalid_rating():
    song_id = "2jiI8bNSDu7UxTtDCOqh3L"
    response = client.post(f"/songs/{song_id}/rate?rating=6")
    assert response.status_code == 422


def test_rate_song_not_found():
    response = client.post("/songs/invalid_id/rate?rating=3")
    assert response.status_code == 404
