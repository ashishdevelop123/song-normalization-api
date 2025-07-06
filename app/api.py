from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.utils import normalize_json
import os

router = APIRouter()

DATA_PATH = os.path.join("data", "sample.json")
songs_data: List[dict] = normalize_json(DATA_PATH)


@router.get("/songs", response_model=List[dict])
def get_all_songs(skip: int = 0, limit: int = 10):
    if skip < 0 or limit <= 0:
        raise HTTPException(status_code=400, detail="Invalid pagination parameters")
    return songs_data[skip: skip + limit]


@router.get("/songs/by_title", response_model=dict)
def get_song_by_title(title: str = Query(..., min_length=1)):
    for song in songs_data:
        if song.get("title", "").lower() == title.lower():
            return song
    raise HTTPException(status_code=404, detail=f"No song found with title: {title}")


@router.post("/songs/{song_id}/rate", response_model=dict)
def rate_song(song_id: str, rating: float = Query(..., ge=0, le=5)):
    for song in songs_data:
        if song.get("id") == song_id:
            song["star_rating"] = rating
            return song
    raise HTTPException(status_code=404, detail=f"Song with ID {song_id} not found")
