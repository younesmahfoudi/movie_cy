from typing import Optional, List
from datetime import date

from bson.objectid import ObjectId

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    nom: str = Field(...)
    prenom: str = Field(...)
    email: EmailStr = Field(...)
    mdp: str = Field(...)
    films: Optional[List[str]]
    groupes: List[str] = []
    mood: Optional[str]
    acteur: Optional[str]
    realisateur: Optional[str]
    genre: Optional[str]
    genreFlex: Optional[int]
    ddn: str = Field()
    avatar: str = Field()

    class Config:
        schema_extra = {
            "example": {
                "nom": "John Doe",
                "prenom": "John Doe",
                "email": "jdoe@x.edu.ng",
                "mdp": "exampleMDP",
                "films": ["film","film2"],
                "groupes": ["groupe", "groupe1"],
                "mood": "fun",
                "acteur": "exampleIDAuteur",
                "realisateur": "exampleIDRealisateur",
                "genre": "comedie",
                "genreFlex": 5,
                "ddn": date.today(),
                "avatar": "img"
            }
        }
        arbitrary_types_allowed = True


class UpdateUserModel(BaseModel):
    nom: Optional[str]  
    prenom: Optional[str] 
    email: Optional[EmailStr] 
    mdp: Optional[str] 
    films: Optional[List[str]] 
    groupes: Optional[List[str]] 
    mood: Optional[str] 
    acteur: Optional[str] 
    realisateur: Optional[str] 
    genre: Optional[str] 
    genreFlex: Optional[int] 
    ddn: Optional[str] 
    avatar: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "nom": "John Doe",
                "prenom": "John Doe",
                "email": "jdoe@x.edu.ng",
                "mdp": "exampleMDP",
                "films": ["film","film2"],
                "groupes": ["groupe", "groupe1"],
                "mood": "fun",
                "acteur": "exampleIDAuteur",
                "realisateur": "exampleIDRealisateur",
                "genre": "comedie",
                "genreFlex": 5,
                "ddn": "26-06-1992",
                "avatar": "image"

            }
        }
        arbitrary_types_allowed = True


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    mdp: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "mdp": "weakpassword"
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