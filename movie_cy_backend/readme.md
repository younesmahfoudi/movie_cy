## Installation

Run Mongodb

```bash
  cd movie_cy_bdd

  docker-compose up -d
```

Install fastapi with lite server in a docker (Python 3.10 requiered!!) 

```bash
  cd movie_cy_api

  docker build -t moviecyapi .

  docker run -d --name apicontainer -p 81:81 moviecyapi
```

Install in dev

```bash
  cd movie_cy_api

  source .venv/bin/activate

  export PYTHONPATH=$PWD

  pip install -r requirements.txt

  python app/main.py
```
    
## Demo

BDD (admin:admin123) : http://localhost:8081/ 

swagger Docker : http://127.0.0.1:81/docs

swagger dev : http://localhost:8000/docs

## Documentation

[Documentation fastapi docker](https://fastapi.tiangolo.com/deployment/docker/)
[Documentation update python3.10](https://www.linuxcapable.com/fr/how-to-install-python-3-10-on-linux-mint-20/)
