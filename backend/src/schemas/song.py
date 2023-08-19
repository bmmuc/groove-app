from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SongModel(BaseModel):
    id: str
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: int

class SongGet(BaseModel):
    id: str
class SongGet(BaseModel):
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: int
    id : str

class SongCreateModel(BaseModel):
    id: str
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: int

class SongList(BaseModel):
    songs: list[SongGet]

class SongDelete(BaseModel):
    id: str
