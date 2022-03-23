from datetime import date
from typing import List, Optional

from click import Option
from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_movie,
    retrieve_movies_with_parameters
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


@router.post("/", response_description="movies data added into the database")
async def add_movie_data(
        title: str = None, 
        types: List[str] = Query(None), 
        releaseDate: date = None, 
        userRating: float = None,
        votesNumber: int = None,
        genres: List[str] =  Query(None),
        groups: List[str] = Query(None),
        companies: List[str] = Query(None),
        colorInfos: List[str] = Query(None),
        countries: List[str] = Query(None),
        keyword: str = None,
        languages: List[str] = Query(None),
        filmingLocation: str = None,
        popularity: int = None,
        count: int = None,
        sort: str = None
    ): 
    movies : List[MovieSchema] = advancedSearch(
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
    return ResponseModel(new_movies, "movies added successfully.")  

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message} 
""" 
@router.get("/", response_description="Get movies")
async def get_movies():
    movies = await retrieve_movies()
    if movies:
        return ResponseModel(movies, "Groups data retrieved successfully")
    return ResponseModel(movies, "Empty list returned")
 """
@router.get("/", response_description="Get movies depends parameters")
async def get_movies_with_option(genreList: List[str] = Query(None), starList: List[str] = Query(None)):
    movies = await retrieve_movies_with_parameters(genreList,starList)
    if movies:
        return ResponseModel(movies, "Groups data retrieved successfully")
    return ResponseModel(movies, "Empty list returned")
