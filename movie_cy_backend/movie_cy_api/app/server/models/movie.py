from enum import Enum
from multiprocessing.dummy import Array
from typing import Optional,List

from pydantic import BaseModel, Field

class Genre(BaseModel):
    key: str
    value: str

class StarList(BaseModel):
    id: str
    name: str


class MovieSchema(BaseModel):
    id: str
    image: str
    title: str
    description: str
    runtimeStr: Optional[str]
    genres: str
    genreList: List[Genre]
    contentRating: Optional[str]
    imDbRating: Optional[str]
    imDbRatingVotes: Optional[int]
    metacriticRating: Optional[int]
    plot: Optional[str]
    stars: Optional[str]
    starList: Optional[List[StarList]]

    class Config:
        schema_extra = {
            "example": {
                "id": "tt2463208",
                "image": "https://imdb-api.com/images/original/MV5BOWM0YWMwMDQtMjE5NS00ZTIwLWE1NWEtODViMWZjMWI2OTU3XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_Ratio0.6837_AL_.jpg",
                "title": "The Adam Project",
                "description": "(2022)",
                "runtimeStr": "106 min",
                "genres": "Action, Adventure, Comedy",
                "genreList": [
                    {
                        "key": "Action",
                        "value": "Action"
                    },
                    {
                        "key": "Adventure",
                        "value": "Adventure"
                    },
                    {
                        "key": "Comedy",
                        "value": "Comedy"
                    }
                ],
                "contentRating": "PG-13",
                "imDbRating": "6.9",
                "imDbRatingVotes": "49883",
                "metacriticRating": "55",
                "plot": "A time-traveling pilot teams up with his younger self and his late father to come to terms with his past while saving the future.",
                "stars": "Shawn Levy, Ryan Reynolds, Walker Scobell, Mark Ruffalo, Jennifer Garner",
                "starList": [
                    {
                        "id": "tt2463208",
                        "name": "Shawn Levy"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Ryan Reynolds"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Walker Scobell"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Mark Ruffalo"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Jennifer Garner"
                    }
                ]
            }
        }


class UpdateMovieModel(BaseModel):
    image: Optional[str]
    title: Optional[str]
    description: Optional[str]
    runtimeStr: Optional[str]
    genres: Optional[str]
    genreList: Optional[List[Genre]]
    contentRating: Optional[str]
    imDbRating: Optional[str]
    imDbRatingVotes: Optional[int]
    metacriticRating: Optional[int]
    plot: Optional[str]
    stars: Optional[str]
    starList: Optional[List[StarList]]

    class Config:
        schema_extra = {
            "example": {
                "image": "https://imdb-api.com/images/original/MV5BOWM0YWMwMDQtMjE5NS00ZTIwLWE1NWEtODViMWZjMWI2OTU3XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_Ratio0.6837_AL_.jpg",
                "title": "The Adam Project",
                "description": "(2022)",
                "runtimeStr": "106 min",
                "genres": "Action, Adventure, Comedy",
                "genreList": [
                    {
                        "key": "Action",
                        "value": "Action"
                    },
                    {
                        "key": "Adventure",
                        "value": "Adventure"
                    },
                    {
                        "key": "Comedy",
                        "value": "Comedy"
                    }
                ],
                "contentRating": "PG-13",
                "imDbRating": "6.9",
                "imDbRatingVotes": "49883",
                "metacriticRating": "55",
                "plot": "A time-traveling pilot teams up with his younger self and his late father to come to terms with his past while saving the future.",
                "stars": "Shawn Levy, Ryan Reynolds, Walker Scobell, Mark Ruffalo, Jennifer Garner",
                "starList": [
                    {
                        "id": "tt2463208",
                        "name": "Shawn Levy"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Ryan Reynolds"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Walker Scobell"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Mark Ruffalo"
                    },
                    {
                        "id": "tt2463208",
                        "name": "Jennifer Garner"
                    }
                ]
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}