from fastapi import APIRouter, status, HTTPException
from src.schemas.search import SearchModel
from starlette.responses import JSONResponse

from src.service.impl.search import FiltersService


router = APIRouter()

@router.get(
    "/search/",
    response_model=SearchModel,
    response_class=JSONResponse,
    summary="Get all albums or musics by filters",
)
def get_all(name: str = None, year: int = None, genre: str = None):
    album_get_response = FiltersService.get_filters(name, year, genre)

    return album_get_response