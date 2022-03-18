import requests

r = requests.get('https://imdb-api.com/API/AdvancedSearch/k_ompp9716?title_type=feature&count=250', auth=('user', 'pass'))
r.status_code

r.headers['content-type']
print(r.json)