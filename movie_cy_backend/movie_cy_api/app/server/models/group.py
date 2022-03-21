from multiprocessing.dummy import Array
from typing import Optional,List

from pydantic import BaseModel, Field


class GroupSchema(BaseModel):
    nom: str = Field(...)
    membres: List[str]=  Field(...) 
    admin: str = Field(...) 
    photo: str = Field(...)

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
    nom: Optional[str]
    membres: Optional[str]
    admin: Optional[int]
    photo: Optional[str]

    class Config:
        schema_extra = {
            "example": {
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