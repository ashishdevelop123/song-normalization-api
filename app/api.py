from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
from app.utils import normalize_json
import os

router = APIRouter()

DATA_PATH = os.path.join("data", "sample.json")
songs_data: List[dict] = normalize_json(DATA_PATH)


@router.get("/songs", response_model=dict)
def get_all_songs(cursor: Optional[str] = None, limit: int = 10):
    if limit <= 0:
        raise HTTPException(status_code=400, detail="Limit must be greater than 0")

    start_index = 0
    if cursor:
        for i, song in enumerate(songs_data):
            if song["id"] == cursor:
                start_index = i + 1
                break
        else:
            raise HTTPException(status_code=400, detail="Invalid cursor")

    paginated = songs_data[start_index:start_index + limit]
    next_cursor = paginated[-1]["id"] if len(paginated) == limit and (start_index + limit) < len(songs_data) else None
    has_more = next_cursor is not None

    return JSONResponse(content={
        "items": paginated,
        "next_cursor": next_cursor,
        "has_more": has_more
    })


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
