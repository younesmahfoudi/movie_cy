from datetime import date
from typing import List, Optional

from click import Option
from fastapi import APIRouter, Body, Depends, Query
from fastapi_pagination import Page, Params, add_pagination, paginate

from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_movie,
    retrieve_movies_filtered
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

def movie_helper(movie) -> dict:
    return {
        "id": str(movie["id"]),
        "image": movie["image"],
        "title": movie["title"],
        "email": movie["email"],
        "description": movie["description"],
        "runtimeStr": movie["runtimeStr"],
        "genres": movie["genres"],
        "genreList": movie["genreList"],
        "contentRating": movie["contentRating"],
        "imDbRating": movie["imDbRating"],
        "imDbRatingVotes" : movie["imDbRatingVotes"],
        "metacriticRating": movie["metacriticRating"],
        "plot": movie["plot"],
        "stars": movie["stars"],
        "starList": movie["starList"]
    }

@router.get("/", response_description="Movies data retrieved", response_model=Page[dict])
async def get_movies_data_filtered(
        title: str = None,
        genrelist: List[str] = Query(None),
        imdbrating: str = None,
        starlist: List[str] = Query(None),
        movielist: List[str] = Query([]),
        params: Params = Depends()
    ): 
    movies = await retrieve_movies_filtered(title,genrelist,starlist,imdbrating)
    moviesFiltered = list(filter(lambda x: x["id"] not in movielist, movies))
    if moviesFiltered:
        return paginate(moviesFiltered, params)
    return paginate(await add_movie_data(title=title, genres=genrelist, userRating=imdbrating), params)

async def add_movie_data(
        title: str = None, 
        types: List[str] = ["feature","tv_movie","tv_special","short"], 
        releaseDate: date = None, 
        userRating: float = None,
        votesNumber: int = None,
        genres: List[str] =  None,
        groups: List[str] = None,
        companies: List[str] = None,
        colorInfos: List[str] = None,
        countries: List[str] = None,
        keyword: str = None,
        languages: List[str] = None,
        filmingLocation: str = None,
        popularity: int = None,
        count: int = 250,
        sort: str = None
    ): 
    movies: List[MovieSchema] = []
    movies = advancedSearch(
        title, 
        types, 
        releaseDate, 
        userRating,
        votesNumber,
        genres,
        groups,
        companies,
        colorInfos,
        countries,
        keyword,
        languages,
        filmingLocation,
        popularity,
        count,
        sort
    )
    new_movies = []
    for movie in movies:
        movie = jsonable_encoder(movie)
        new_movies.append(await add_movie(movie))
    return new_movies

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message} 