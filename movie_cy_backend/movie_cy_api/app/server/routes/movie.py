from datetime import date
from typing import List, Optional

from click import Option
from fastapi import APIRouter, Body, Query
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
from app.server.models.user import UserSchema

router = APIRouter()

def movie_helper(movie) -> dict:
    print("test")
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

@router.get("/", response_description="Movies data retrieved")
async def get_movies_data_filtered(
        title: str = None,
        genrelist: List[str] = Query(None),
        imdbrating: str = None,
        starlist: List[str] = Query(None),
        movielist: List[str] = Query(None)
    ): 
    movies = await retrieve_movies_filtered(title,genrelist,starlist,imdbrating)
    moviesFiltered = filter(lambda x: x["id"] not in movielist, movies)
    res = list(moviesFiltered)
    if res:
        return ResponseModel(res, "movies get successfully.")  
    return await add_movie_data(title=title, genres=genrelist, userRating=imdbrating)

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
    if new_movies:
        return ResponseModel(new_movies, "movies added successfully.")  
    return ErrorResponseModel("An error occurred", 404, "check the parameters or the imdb token")

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message} 