# 🎵 Song Normalization API

A lightweight, FastAPI-based backend that loads song data from a normalized JSON file into memory and exposes RESTful endpoints for querying and rating songs.

---

## 🚀 Features

- ✅ Load and normalize raw JSON song data on startup
- 🔍 Filter and paginate songs
- 🎯 Query by song title
- ⭐ Rate songs (with validation)
- 🧪 Includes automated tests with `pytest`
- 🐳 Dockerized for easy local deployment

---

## 📁 Folder Structure

```
song-normalization-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   └── utils.py
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

Access the API at (http://localhost:8000)

---

## ✅ Running Tests

```bash
pytest
```

---

## 🔍 API Endpoints

| Method | Endpoint                  | Description                            |
|--------|---------------------------|----------------------------------------|
| GET    | `/songs`                  | Get all songs with optional pagination |
| GET    | `/songs/by_title`        | Get song details by title              |
| POST   | `/songs/{song_id}/rate`  | Update star rating for a song          |

---

## 📝 Notes

- All data is loaded from `data/sample.json` at startup.
- Ratings are stored in-memory (ephemeral).

---