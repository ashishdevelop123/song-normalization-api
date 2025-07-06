from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_songs_default():
    response = client.get("/songs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 10


def test_get_all_songs_with_pagination():
    response = client.get("/songs?skip=5&limit=3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 3


def test_get_all_songs_invalid_params():
    response = client.get("/songs?skip=-1&limit=5")
    assert response.status_code == 400
    assert "Invalid pagination parameters" in response.text


def test_get_song_by_title_exists():
    response = client.get("/songs/by_title?title=Song One")
    assert response.status_code == 200
    assert response.json()["title"].lower() == "song one"


def test_get_song_by_title_not_found():
    response = client.get("/songs/by_title?title=non_existent_title")
    assert response.status_code == 404
    assert "No song found" in response.text


def test_rate_song_success():
    song_id = "2b3c4d5e6f7g"
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
