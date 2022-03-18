from enum import Enum
from multiprocessing.dummy import Array
from typing import Optional,List

from pydantic import BaseModel, Field

class GenreList(BaseModel):
    key: str
    value: str


class MovieSchema(BaseModel):
    id: str
    image: str
    title: str
    description: str
    runtime_str: Optional[str]
    genres: str
    genre_list: List[str]
    content_rating: Optional[str]
    im_db_rating: Optional[str]
    im_db_rating_votes: Optional[int]
    metacritic_rating: Optional[int]
    plot: Optional[str]
    stars: Optional[str]
    star_list: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "nom": "La coloc",
                "membres": ["iduser1","iduser2"],
                "admin": "idAdmin",
                "photo": "/path/example/",
            }
        }


class UpdateGroupModel(BaseModel):
    ##id: Optional[str]
    nom: Optional[str]
    membres: Optional[str]
    admin: Optional[int]
    photo: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "nom": "La coloc",
                "membres": ["iduser1","iduser2"],
                "admin": "idAdmin",
                "photo": "/path/example/",
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