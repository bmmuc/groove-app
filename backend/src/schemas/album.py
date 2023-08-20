from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class AlbumModel(BaseModel):
    title: str
    artist: str
    release_year: int

class AlbumGet(BaseModel):
    name: str
    artist: str

class AlbumCreateModel(BaseModel):
    title: str
    artist: str
    release_year: int

class AlbumList(BaseModel):
    albums: List[AlbumGet]

class AlbumDelete(BaseModel):
    id: str
