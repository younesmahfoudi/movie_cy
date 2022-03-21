from typing import List

from pydantic import BaseModel

from .movie import (
    MovieSchema
)

class ImdbResponse(BaseModel):
    query_string: str
    results: List[MovieSchema]
    error_message: str

    def __init__(self, query_string, results, error_message):
        self.query_string = query_string
        self.results = results
        self.error_message = error_message