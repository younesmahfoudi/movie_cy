## MOVIE CY BACKEND

## Installation

Todo Back end (Mongodb and FastApi) 

```bash
  cd movie_cy_api
```

```bash
  docker-compose up -d
```

## Run Locally

Run Mongodb 

```bash
  cd movie_cy_bdd
```

```bash
  docker-compose up -d
```

Run fastapi (Python 3.10 requiered) 

```bash
  cd movie_cy_api
```

```bash
  docker build -t moviecyapi .
```

```bash
  docker run -d --name apicontainer -p 8000:8000 moviecyapi
```

Run FastApi

```bash
  cd movie_cy_api
```

```bash
  python3.10 -m venv .venv
```

```bash
  source .venv/bin/activate
```

```bash
  export PYTHONPATH=$PWD
```

```bash
  pip install -r requirements.txt
```

```bash
  python app/main.py
```

    
## Demo
BDD Docker: http://127.0.0.1:8081

BDD dev (admin:admin123) : http://localhost:8081 

swagger Docker : http://127.0.0.1:8000/docs

swagger dev : http://localhost:8000/docs

## Documentation

[Documentation fastapi docker](https://fastapi.tiangolo.com/deployment/docker/)
[Documentation update python3.10](https://www.linuxcapable.com/fr/how-to-install-python-3-10-on-linux-mint-20/)
