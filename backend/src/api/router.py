from fastapi import APIRouter
from src.api import items
from src.api import songs
from src.api import search
api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(songs.router, prefix="/songs", tags=["songs"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
