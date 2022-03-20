from typing import List
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_movie,
    add_movies,
)
from app.server.models.movie import (
    ErrorResponseModel,
    ResponseModel,
    MovieSchema,
    UpdateMovieModel,
)

from app.server.imdb import (
    advancedSearch
)

router = APIRouter()


# @router.post("/", response_description="movie data added into the database")
# async def add_movie_data(movie: MovieSchema = Body(...)):
#     movie = jsonable_encoder(movie)
#     new_movie = await add_movie(movie)
#     return ResponseModel(new_movie, "movie added successfully.")   

@router.post("/", response_description="movies data added into the database")
async def add_movie_data():
    movies : List[MovieSchema] = advancedSearch(genres=['action'])
    movies = jsonable_encoder(movies)
    new_movies = await add_movies(movies)
    return ResponseModel(new_movies, "movies added successfully.")   


    
