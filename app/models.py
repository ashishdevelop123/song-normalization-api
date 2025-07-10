from pydantic import BaseModel, Field
from typing import Optional, List


class Song(BaseModel):
    id: str
    title: str
    danceability: float
    energy: float
    mode: int
    acousticness: float
    tempo: float
    duration_ms: int
    num_sections: int
    num_segments: int
    star_rating: Optional[float] = Field(default=None, ge=0, le=5)


class PaginatedSongs(BaseModel):
    items: List[Song]
    next_cursor: Optional[str]
    has_more: bool
