from datetime import date
import os
import string
from typing import List
from urllib import response
import requests

import aiohttp
import asyncio

    


IMDBPATH =  'https://imdb-api.com/API'
IMDBTOKEN = 'k_ompp9716'

"""
advanced search 
string title
string type
date releaseDate

"""
def advancedSearch(
        title: string = None, 
        type: string = None, 
        realeaseDate: date = None, 
        userRating: List[float] = None 
    ):
    print(title)
    request = requests.get('https://imdb-api.com/API/AdvancedSearch/k_ompp9716?title_type=feature&count=250')
    return request

def runAdvancedSearch(
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
        return asyncio.run(advancedSearchSync(url))


async def advancedSearchSync(
        url : str
    ):
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                response = await resp.json()
                return response
    


if __name__ == "__main__":
    print(runAdvancedSearch(genres=['action']))
