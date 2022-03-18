from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_movie,
)
from app.server.models.movie import (
    ErrorResponseModel,
    ResponseModel,
    MovieSchema,
    UpdateMovieModel,
)

router = APIRouter()


@router.post("/", response_description="movie data added into the database")
async def add_movie_data(movie: MovieSchema = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = await add_movie(movie)
    return ResponseModel(new_movie, "movie added successfully.")   