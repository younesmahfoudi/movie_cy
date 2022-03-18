from typing import Optional, List
import datetime
from xmlrpc.client import DateTime
from bson.objectid import ObjectId

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    nom: str = Field(...)
    prenom: str = Field(...)
    email: EmailStr = Field(...)
    mdp: str = Field(...)
    films: List[str] = Field(...)
    groupes: List[str] = Field(...)
    mood: str = Field(...)
    acteur: str = Field(...)
    realisateur: str = Field(...)
    genre: str = Field(...)
    genreFlex: str = Field(...)
    ddn: str = Field(...)
    age: int = Field(...)

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
                "genreFlex": "comedie",
                "ddn": "1998-08-28",
                "age": 20,
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
    genreFlex: Optional[str] 
    ddn: Optional[str] 
    age: Optional[int] 

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
                "genreFlex": "comedie",
                "ddn": "1998-08-28",
                "age": 20,
            }
        }
        arbitrary_types_allowed = True


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}