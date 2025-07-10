# 🎵 Song Normalization API

A lightweight, FastAPI-based backend that loads song data from a normalized JSON file into memory using Pydantic models and exposes RESTful endpoints for querying and rating songs.

---

## 🚀 Features

- ✅ Load and normalize raw JSON song data on startup using Pydantic
- 🔍 Cursor-based pagination for consistent retrieval
- 🎯 Query by song title
- ⭐ Rate songs (with validation)
- 🧪 Includes automated tests with `pytest`
- 🐳 Dockerized for easy local deployment
- 📦 Strong typing and data validation with Pydantic models

---

## 📁 Folder Structure

```
song-normalization-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   ├── utils.py
│   └── models.py
├── data/
│   └── sample.json
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_utils.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧑‍💻 Getting Started (Locally)

### ⚖️ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate 
```

### 📆 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the server

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Instructions

### 🛠 Build the image

```bash
docker build -t song-api .
```

### ▶️ Run the container

```bash
docker run -d -p 8000:8000 song-api
```

Access the API at [http://localhost:8000](http://localhost:8000)

---

## ✅ Running Tests

```bash
pytest
```

---

## 🔍 API Endpoints

| Method | Endpoint                  | Description                                         |
|--------|---------------------------|-----------------------------------------------------|
| GET    | `/songs`                  | Get paginated songs using cursor-based pagination  |
| GET    | `/songs/by_title`         | Get song details by title                          |
| POST   | `/songs/{song_id}/rate`   | Update star rating for a song                      |

### 📘 `/songs` Endpoint Details

Supports cursor-based pagination:

```http
GET /songs?limit=5                      # first page
GET /songs?cursor=<song_id>&limit=5     # next page using the last returned ID
```

Response:

```json
{
  "items": ["Song", "Song", ...],
  "next_cursor": "abc123",
  "has_more": true
}
```

---

## 📝 Notes

- All song data is loaded from `data/sample.json` at startup and parsed into Pydantic models.
- Ratings are stored in-memory and reset on server restart.
- Invalid or missing fields are gracefully handled during data normalization.
