from datetime import date
import json
import os
from typing import List
import aiohttp
import asyncio
from models.imdbResponse import ImdbResponse
from types import SimpleNamespace

IMDBPATH =  'https://imdb-api.com/API'
IMDBTOKEN = 'k_ompp9716'

def advancedSearch(
        title: str = None, 
        types: List[str] = None, 
        releaseDate: date = None, 
        userRating: float = None,
        votesNumber: int = None,
        genres: List[str] = None,
        groups: List[str] = None,
        companies: List[str] = None,
        colorInfos: List[str] = None,
        countries: List[str] = None,
        keyword: str = None,
        languages: List[str] = None,
        filmingLocation: str = None,
        popularity: int = None,
        count: int = None,
        sort: str = None
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
        return asyncio.run(getRequest(url))


async def getRequest(
        url : str
    ):
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                responseJsn = await resp.json(content_type=None)
                # Parse JSON into an object with attributes corresponding to dict keys.
                responseStr = json.dumps(responseJsn)
                responseObj : ImdbResponse = json.loads(responseStr, object_hook=lambda d: SimpleNamespace(**d))
                return responseObj


if __name__ == "__main__":
    print(advancedSearch(genres=['action']).results)
