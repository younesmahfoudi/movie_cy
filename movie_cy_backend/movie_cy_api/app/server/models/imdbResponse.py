from typing import List

from pydantic import BaseModel

from .movie import (
    MovieSchema
)

class ImdbResponse(BaseModel):
    query_string: str
    results: List[MovieSchema]
    error_message: str