from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class MusicModel(BaseModel):
    title: str
    genre: str
    artist: str
    release_year: int

class MusicGet(BaseModel):
    title: str
    genre: str
    artist: str
    release_year: int

class SongCreateModel(BaseModel):
    title: str
    artist: str
    genre: str
    release_year: int

class MusicList(BaseModel):
    musics: list[MusicGet]

class MusicDelete(BaseModel):
    id: str