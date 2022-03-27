from datetime import date
import json
import os
import requests
from typing import List
from app.server.models.imdbResponse import ImdbResponse
from collections import namedtuple
from app.server.models.movie import MovieSchema

IMDBPATH =  'https://imdb-api.com/API'
IMDBTOKEN = 'k_ompp9716'
# IMDBTOKEN = 'k_szftjjr3'

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

#python 3.10
def advancedSearch(
        title: str | None, 
        types: List[str] | None, 
        releaseDate: date | None, 
        userRating: float | None,
        votesNumber: int | None,
        genres: List[str] | None,
        groups: List[str] | None,
        companies: List[str] | None,
        colorInfos: List[str] | None,
        countries: List[str] | None,
        keyword: str | None,
        languages: List[str] | None,
        filmingLocation: str | None,
        popularity: int | None,
        count: int | None,
        sort: str | None
    ):
        url = os.path.join(IMDBPATH,'AdvancedSearch',IMDBTOKEN)+'?'
        if count is not None : url = url + f'count={count}&'
        if title is not None : url = url + f'title={title}&'
        if types is not None : url = url + 'title_type=' + ','.join(types) + '&'
        if releaseDate is not None : url = url + f'release_date={releaseDate},&'
        if userRating is not None : url = url + f'user_rating={userRating},&'
        if votesNumber is not None : url = url + f'num_votes={votesNumber},&'
        if genres is not None : url = url + 'genres=' + ','.join(genres) + '&'
        if groups is not None : url = url + 'groups=' + ','.join(groups) + '&'
        if companies is not None : url = url + 'companies' + ','.join(companies) + '&'
        if colorInfos is not None : url = url + 'colors=' + ','.join(colorInfos) + '&'
        if countries is not None : url = url + 'countries=' + ','.join(countries) + '&'
        if groups is not None : url = url + 'groups=' + ','.join(groups) + '&'
        if keyword is not None : url = url + f'keyword={keyword}&'
        if languages is not None : url = url + 'languages=' + ','.join(languages) + '&'
        if filmingLocation is not None : url = url + f'locations={filmingLocation}&'
        if popularity is not None : url = url + f'moviemeter={popularity},&'
        if sort is not None : url = url + f'sort={sort}&'
        return getRequest(url)


def getRequest(
        url : str
    ):
        response = requests.get(url)
        print(response)   
        jsonResponse: ImdbResponse = response.json()
        results: List[MovieSchema] = jsonResponse['results']
        return results
     